---
name: voice-profile
description: "Build or refresh Stefano's WRITING voice profile at c3po_vault/context/voice.md — measured from real samples, not guessed. Use when writing anything in his name (pitch, cold email, post, README intro, client message, application) and voice.md is missing or stale; when he says his writing sounds generic or AI-written; or when he asks to build/update/sharpen his voice profile. Not for the agent's own reply register — that is soul.md."
---

# Voice Profile

Builds one file: `c3po_vault/context/voice.md`. Every later writing task reads it.

**This is not `soul.md`.** `soul.md` governs how the agent talks to Stefano. This governs
how Stefano's own writing sounds when the agent drafts in his name. Two different voices.
Never merge them.

## Rule: measure, do not guess

The value of this file is the counted numbers. A voice profile assembled from adjectives
is worth nothing — every writer describes themselves as "direct and clear". If there are
no samples, say so in the file and mark the rhythm as unmeasured. Do not invent a number.

## Step 1: Check for an existing profile

Read `c3po_vault/context/voice.md` if it exists. Say what is already there and ask whether
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

From the samples, by counting — not by impression:

- Average sentence length in words. State the number.
- Longest and shortest sentence. The spread matters more than the mean.
- Sentence openers he repeats. List the actual ones with counts.
- Paragraph length in sentences.
- Whether he leads with the claim or builds to it.
- Punctuation habits: em dashes, colons, parentheses, one-line paragraphs.
- Words that recur across all samples. These are the real signature phrases, and they often
  contradict what he named in Step 2. When they do, say so and keep the counted ones.

## Step 5: Write the file

Write `c3po_vault/context/voice.md`:

```
# Writing Voice — Stefano

How Stefano's own writing sounds. Read this before drafting anything in his name.
Not the agent's reply register — that is soul.md.

Built: <YYYY-MM-DD> from <N> samples: <name them>

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

## Step 6: Prove it

Take a paragraph of default AI copy. Show it as **Before**. Rewrite it under the profile you
just wrote — tone, counted rhythm, real signature phrases, banned words — and show it as
**After**. A word swap is not a rewrite. If the After does not read differently in structure,
the profile is too thin. Say that and go back to Step 4.

## Step 7: Wire it in

Tell him to add one line to `c3po_vault/CLAUDE.md` under "Read these":

```
**Writing in Stefano's name, additionally:** `context/voice.md`
```

Do not edit `CLAUDE.md` yourself unless he says to.

## Refresh trigger

Re-run when the samples are more than six months old, or when a new surface appears that
the current profile was not built for.
