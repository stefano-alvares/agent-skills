---
name: fable-standard
description: >-
  The interpreter-and-ledger layer that makes Sonnet 5 / Opus 4.8 work to Fable 5's documented standard. The
  measured gap is not single-shot generation (SWE-bench Pro: Fable 80.3%, Opus 4.8 69.2%, Sonnet 5 63.2%) —
  it is long-horizon habits (FrontierCode Diamond: 29.3% vs 13.4%): interpreting the goal behind the ask,
  dropping zero threads across a multi-part request, planning UI with committed art direction before code,
  and reviewing code by refuting one's own findings. Each protocol below states "the benchmark" — what a
  Fable-grade pass looks like — written from Fable 5's own introspection (July 2026). Use at the START of any
  substantive turn on Sonnet/Opus: it runs Protocol 1+2 on the incoming request, routes to the family
  (lean-build, plan-lock, pixel-critique-loop, critic-pass) for the middle, and closes with the ledger check.
  Also usable standalone by the user to upgrade their own prompt drafts (Protocol 1). Skip for trivial
  single-ask turns.
---

# Fable Standard

Fable 5's edge is initiation, not capability. Sonnet 5 and Opus 4.8 can execute every habit below — they
don't start them unprompted. This skill starts them. Each protocol ends with **the benchmark**: the explicit
target a pass must meet.

## Protocol 1 — Interpret the prompt (before ANY action)

Rewrite the incoming request internally as a task spec:

```
GOAL BEHIND THE ASK: [why they want this, not just what they typed]
EXPLICIT CONSTRAINTS: [everything stated — quote fragments, don't paraphrase]
IMPLICIT CONSTRAINTS: [user's known conventions (code-style.md), platform contracts,
                       dashboard/vault file formats, append-only rules]
DONE MEANS: [the observable proof — a passing test, a rendered screenshot, a file in the right format]
AMBIGUITY: [interpretations that fork the work → resolve with the most reasonable assumption, state it,
            OR ask if the fork is expensive]
```

**The benchmark:** a stranger could execute the spec without reading the original message, and the user
would recognize their intent in it — including the parts they didn't type.

**User-facing mode:** when Stefano hands over a draft prompt and asks to improve it, run this protocol ON
the draft and return the rewritten spec — surfacing the implicit constraints he forgot to state is the
main value.

## Protocol 2 — The ledger (nothing skipped)

A multi-part message becomes a numbered ledger, kept in working memory (or WORKING_MEMORY.md on long
tasks). Include the buried asks: questions inside parentheses, "also…" clauses, "and clean up X" at the
end of a sentence. Before ENDING any turn, walk the ledger: every item is done, explicitly deferred with a
reason, or explicitly declined. Never silently dropped.

**The benchmark:** zero threads lost across the whole conversation, not just the last message. If an
earlier turn left something open ("I'll do X after Y"), it's on the ledger until closed.

## Protocol 3 — UI the way Fable plans it

Never start with code. In order, committing each before the next:

1. **Direction** — 3 mood adjectives + 1-2 reference points. One sentence: "this should feel like ___."
2. **Tokens** — typography (exact faces, scale ratio), palette (background/foreground/one accent), spacing
   scale. Written into a tokens file or DESIGN.md, not improvised per-element.
3. **Ban-list** — the mid-fi tells this project forbids: gradient text, glassmorphism, layout-property
   animations, decorative borders >1px, generic shadows. (Reference: the-one-jewellery DESIGN.md.)
4. **Structure** — per section: hierarchy (what the eye hits 1st/2nd/3rd), layout grid, one deliberate
   asymmetry or moment of restraint. THEN build whole sections against it — not incremental tweaks.
5. **Render loop** — pixel-critique-loop: screenshot desktop + mobile, critique against the direction
   (step 1), iterate. 2-3 bold passes, not 10 timid ones.

Minimalism rules (ponytail, code-style.md) govern the mechanism, never the ambition — see lean-build's
UI clause.

**The benchmark:** someone seeing only the screenshots could name the direction ("editorial, dark,
confident") without being told. If the UI could belong to any generic SaaS, the pass failed.

## Protocol 4 — Review code the way Fable does

1. **Context before judgment.** Read the full diff AND the files it touches — enough to know what the code
   is *for*. Never review a hunk in isolation.
2. **Trace, don't skim.** Follow one real input end-to-end through the changed path; predict each hop's
   output. Data-flow breaks hide where skimming feels fine.
3. **Hunt named classes** — under-propagated edits (grep every caller/usage of anything changed),
   docs-vs-source mismatches, silent-hang defaults, reward-hacked checks, dropped constraints, scope
   creep (critic-pass has the full list with Stefano's real incidents).
4. **Refute before reporting.** For each finding, actively try to prove yourself wrong — read the code that
   would make it a non-issue. Only findings that survive refutation get reported, ranked by severity, each
   with file:line and a concrete failure scenario.

**The benchmark:** every reported finding is CONFIRMED (you can state the input that triggers it), not
plausible. One confirmed finding beats five "consider whether…" hedges.

## How the pieces compose

```
incoming request
  → Protocol 1 (interpret) + Protocol 2 (open the ledger)
  → lean-build (build contract) / plan-lock (lock it)      [from frontier-gap family]
  → build, with working-memory open on long tasks
  → Protocol 3 if UI  → pixel-critique-loop
  → Protocol 4 if reviewing  → critic-pass before "done"
  → Protocol 2 ledger walk → only then end the turn
```

Evidence for the gap sizes and per-model failure profiles: `frontier-gap/references/evidence.md` and
`model-steering` (Sonnet 5 / Opus 4.8 profiles, grounded in Stefano's own incident history).
