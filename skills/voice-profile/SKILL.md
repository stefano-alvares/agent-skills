---
name: voice-profile
description: "Build or refresh Stefano's WRITING voice profile — measured from real samples, not guessed. Use when writing anything in his name (pitch, cold email, post, README intro, client message, application) and his voice profile file is missing or stale; when he says his writing sounds generic or AI-written; or when he asks to build/update/sharpen his voice profile. Not for the agent's own reply register — that is the agent's persona and reply-style instructions."
---

# Voice Profile

Builds one file: Stefano's voice profile, at `~/Desktop/Business-projects/business vault/voice-profile.md`.
Every later writing task reads it.

**One canonical location.** One file, read by every agent and harness. Never keep a copy per
harness, and never edit a global prompt or instructions file to wire it in unless he says to.

**This is not the agent's persona.** The agent's persona and reply-style instructions govern
how the agent talks to Stefano. This governs how Stefano's own writing sounds when the agent
drafts in his name. Two different voices. Never merge them.

## Rule: measure, do not guess

The value of this file is the counted numbers. A voice profile assembled from adjectives
is worth nothing — every writer describes themselves as "direct and clear". If there are
no samples, say so in the file and mark the rhythm as unmeasured. Do not invent a number.

State the sample size wherever you state a number: how many samples, roughly how many words.
A rhythm counted from two short messages is a hint, and the file says so.

**Never call an interview-only profile "measured"** — not in the file, not in your reply.
It is "built from the interview", with the rhythm unmeasured.

## Rule: no forced interview

The interview in Step 2 runs only when he asked to build or refresh the profile. A drafting
task that finds the profile missing or old does not start an interview: draft from what is
in front of you, say that no profile was used, and offer to build one.

## Step 1: Check for an existing profile

Read the voice profile file if it exists. Say what is already there and ask whether
this is a refresh (new samples, keep the rest) or a rebuild.

## Step 2: Interview

Five questions, one at a time. Wait for each answer.

1. What is the writing for? Name the real surfaces — cold emails, client proposals, README
   intros, posts, uni applications. This shapes the register, and a profile built for one
   surface misfires on another.
2. What do you do, in one line, as a reader would need it?
3. Three words a reader would use for your writing.
4. Two or three phrases you actually reach for. Signature phrases, not aspirational ones.
5. Words you never want to see in your writing.

## Step 3: Get real samples

Ask for two or three things **he wrote**, not AI-drafted. File paths or pasted text both work.
Old messages, a proposal, a post, a README he wrote by hand.

If there is nothing available: build from the interview alone, and mark the rhythm section
as unmeasured. Tell him at the close how to sharpen it later.

## Step 4: Count

From the samples, by counting — not by impression. Models miscount by eye, so run the counter and
copy its numbers: save each sample as a text file and run
`python3 scripts/measure.py <sample1> <sample2> ...` from this skill's folder (stdlib only; `-` reads
stdin). It prints everything below except whether he leads with the claim, which you judge by reading.
Where the script cannot run, count by hand and say in the file that the numbers are hand-counted.

- Average sentence length in words. State the number.
- Longest and shortest sentence. The spread matters more than the mean.
- Sentence openers he repeats. List the actual ones with counts.
- Paragraph length in sentences.
- Whether he leads with the claim or builds to it.
- Punctuation habits: em dashes, colons, parentheses, one-line paragraphs.
- Words that recur across all samples. These are the real signature phrases, and they often
  contradict what he named in Step 2. When they do, say so and keep the counted ones.

State the sample size (how many samples, roughly how many words) next to the numbers.

## Step 5: Write the file

Write the voice profile to the canonical path at the top of this skill:

```
# Writing Voice — Stefano

How Stefano's own writing sounds. Read this before drafting anything in his name.
Not the agent's reply register — that is the agent's persona and reply-style instructions.

Built: <YYYY-MM-DD> from <N> samples (~<N> words): <name them>

## Surfaces
<what this voice is for>

## Who
<one-line role, reader-facing>

## Tone
<three words>

## Rhythm
Average sentence: <N> words. Range <min> to <max>.
Paragraphs run <N> sentences.
<Leads with the claim / builds to it.>

## Signature phrases (counted from samples)
- <phrase> — appears <N> times
- <phrase> — appears <N> times

## Habits
<punctuation and structure habits, one line each>

## Banned words
delve, tapestry, leverage, robust, seamless, foster, realm, elevate, underscore,
plethora, myriad, holistic, synergy, cornerstone, paramount, pivotal, nuanced,
multifaceted, game-changer, unlock the power
<plus his own>

## Portable
Paste this file into any model before asking it to write as Stefano.
```

If built without samples, replace the Rhythm block with:
`Rhythm: unmeasured — built from interview only. Re-run with real samples to set this.`

Report the saved path and the evidence basis (N samples, or interview-only).

## Step 6: Prove it

Take a paragraph of default AI copy. Show it as **Before**. Rewrite it under the profile you
just wrote — tone, counted rhythm, real signature phrases, banned words — and show it as
**After**. A word swap is not a rewrite. If the After does not read differently in structure,
the profile is too thin. Say that and go back to Step 4.

## Refresh trigger

Re-run when a new surface appears that the current profile was not built for. Age alone is
not a trigger.
