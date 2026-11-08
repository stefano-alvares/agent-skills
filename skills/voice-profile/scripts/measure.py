#!/usr/bin/env python3
"""Count the numbers voice-profile needs from real writing samples.

Usage: python3 measure.py sample1.txt sample2.md ...   (use - for stdin)

Prints sample size, sentence length (mean, median, range), paragraph length,
repeated sentence openers, punctuation habits per 1,000 words, and the words
and two-word phrases that recur across samples. Standard library only.

Method (stated so the profile can quote it): code blocks, URLs and markdown
markers are stripped; paragraphs split on blank lines; sentences split after
. ! ? and at line breaks (chat messages often end a thought with Enter rather
than a full stop), except where a line break looks like a hard wrap (no end
punctuation, next line starts in lower case). Whether he leads with the claim
is a judgement this script does not make.
"""
import re
import statistics
import sys
from collections import Counter

STOP = set("""a an the and or but if then so of to in on at by for with from as is are was were be been
being it its it's this that these those i me my we our you your he she they them their his her not no
do does did done have has had will would can could should just than too very also into out up about
there here what which who when where why how all any some more most other such only own same over
again once am im i'm i've i'd i'll don't dont can't cant isn't isnt that's thats there's""".split())

def clean(text):
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"https?://\S+", " ", text)
    text = re.sub(r"^\s{0,3}(#+|[-*+]|\d+\.|>)\s+", "", text, flags=re.M)
    return text.replace("**", "").replace("__", "")

def words(s):
    return re.findall(r"[A-Za-z][A-Za-z'’-]*", s)

def sentences(paragraph):
    # A line break ends a sentence unless it looks like a hard wrap: the line has no end
    # punctuation and the next line starts in lower case.
    lines = []
    for line in paragraph.splitlines():
        line = line.strip()
        if lines and line[:1].islower() and not re.search(r"[.!?:][\"'”’)]?$", lines[-1]):
            lines[-1] += " " + line
        elif line:
            lines.append(line)
    out = []
    for line in lines:
        for s in re.split(r"(?<=[.!?])[\"'”’)]?\s+", line.strip()):
            if words(s):
                out.append(s.strip())
    return out

def analyse(text):
    text = clean(text)
    paras = [p for p in re.split(r"\n\s*\n", text) if words(p)]
    sents = [s for p in paras for s in sentences(p)]
    return {
        "text": text,
        "paras": paras,
        "sents": sents,
        "para_sents": [len(sentences(p)) for p in paras],
        "words": words(text),
    }

def main(paths):
    if not paths:
        sys.exit(__doc__)
    samples = []
    for p in paths:
        text = sys.stdin.read() if p == "-" else open(p, encoding="utf-8", errors="replace").read()
        samples.append((p, analyse(text)))

    all_sents = [s for _, a in samples for s in a["sents"]]
    all_words = [w for _, a in samples for w in a["words"]]
    if not all_sents:
        sys.exit("No sentences found in the samples.")
    lengths = [len(words(s)) for s in all_sents]
    para_sents = [n for _, a in samples for n in a["para_sents"]]
    n_words = len(all_words)

    print(f"Samples: {len(samples)} (~{n_words} words, {len(all_sents)} sentences)")
    for p, a in samples:
        print(f"  - {p}: ~{len(a['words'])} words, {len(a['sents'])} sentences")
    if n_words < 300:
        print("  NOTE: under 300 words. Treat every number below as a hint, and say so in the profile.")

    print("\nRhythm")
    print(f"  Average sentence: {statistics.mean(lengths):.1f} words (median {statistics.median(lengths):g})")
    print(f"  Range: {min(lengths)} to {max(lengths)} words")
    short = sum(1 for n in lengths if n <= 6) / len(lengths)
    long_ = sum(1 for n in lengths if n >= 25) / len(lengths)
    print(f"  Short (<=6 words): {short:.0%} of sentences; long (>=25): {long_:.0%}")
    print(f"  Paragraphs: {statistics.mean(para_sents):.1f} sentences on average; "
          f"one-sentence paragraphs: {sum(1 for n in para_sents if n == 1)}/{len(para_sents)}")
    print(f"  Longest: \"{max(all_sents, key=lambda s: len(words(s)))}\"")
    print(f"  Shortest: \"{min(all_sents, key=lambda s: len(words(s)))}\"")

    print("\nRepeated sentence openers (count >= 2)")
    first = Counter(words(s)[0].lower() for s in all_sents)
    first2 = Counter(" ".join(words(s)[:2]).lower() for s in all_sents if len(words(s)) >= 2)
    rows = [(k, v) for k, v in first2.most_common(10) if v >= 2] or [(k, v) for k, v in first.most_common(10) if v >= 2]
    print("\n".join(f"  {k!r}: {v}" for k, v in rows) or "  none")

    print("\nPunctuation per 1,000 words")
    text = "\n".join(a["text"] for _, a in samples)
    marks = {"em dash —": text.count("—") + len(re.findall(r"\s--\s", text)), "en dash –": text.count("–"),
             "colon": len(re.findall(r":(?!//)", text)), "semicolon": text.count(";"),
             "parentheses": text.count("("), "exclamation": text.count("!"), "question": text.count("?"),
             "ellipsis": text.count("...") + text.count("…")}
    for k, v in marks.items():
        print(f"  {k}: {v} ({v * 1000 / max(n_words, 1):.1f})")

    print("\nRecurring words and phrases (in 2+ samples; the real signature candidates)")
    per_sample_words, per_sample_bigrams = [], []
    totals_w, totals_b = Counter(), Counter()
    for _, a in samples:
        ws = [w.lower() for w in a["words"]]
        content = [w for w in ws if w not in STOP and len(w) > 2]
        bigrams = [f"{x} {y}" for x, y in zip(ws, ws[1:]) if not (x in STOP and y in STOP)]
        per_sample_words.append(set(content)); per_sample_bigrams.append(set(bigrams))
        totals_w.update(content); totals_b.update(bigrams)
    if len(samples) < 2:
        print("  Needs 2+ samples to tell a habit from a topic word.")
    else:
        def recurring(totals, sets):
            return [(k, v) for k, v in totals.most_common() if v >= 2 and sum(k in s for s in sets) >= 2][:12]
        for label, rows in (("words", recurring(totals_w, per_sample_words)),
                            ("phrases", recurring(totals_b, per_sample_bigrams))):
            print(f"  {label}: " + (", ".join(f"{k} ({v})" for k, v in rows) or "none"))
        print("  Topic words (a client name, a product) recur too: keep only habits of voice.")

if __name__ == "__main__":
    main(sys.argv[1:])
