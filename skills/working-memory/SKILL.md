---
name: working-memory
description: >-
  Keep a persistent notes file during any long or multi-session agentic task — status, locked decisions, and
  most importantly the failed approaches and WHY they failed — and re-read it on resume and before each unit
  of work. This is the cheap, external version of the single mechanism that helped Claude Fable 5 "three
  times more than Opus 4.8" on Anthropic's own long-horizon eval: it stays focused across millions of tokens
  by improving its outputs using its own notes. Weaker and cheaper models (Composer 2.5, GPT-5.5, local) and
  any model after a context reset drift fastest and re-attempt the same dead ends precisely because they have
  no memory across the run — Anthropic's guidance is explicit that without a failed-approaches log "successive
  sessions will re-attempt the same dead ends." Use this whenever a task spans more than one sitting, will be
  compacted, hands off between agents, or keeps hitting the same class of mistake; it is the durable-notes
  file that pixel-critique-loop and critic-pass write their recurring findings into. Trigger at the START of
  substantial work, not after the mistakes have already repeated.
---

# Working Memory

Anthropic's most-quantified long-horizon result is not about a smarter model — it's about notes. Fable 5
"stays focused across millions of tokens… and improves its outputs using its own notes," and a file-based
memory helped it *three times more than Opus 4.8*. The mechanism is replicable with a plain markdown file,
and it matters *most* for the weaker models, because they drift fastest and a context reset wipes everything
they learned. Without a record of what was already tried, a fresh session re-walks every dead end. This skill
is that record, made mandatory and external.

## The one rule

**Write the note when you learn the thing, not when you remember to.** The value is captured at the moment a
mistake is understood or a decision is locked — log it *then*. A note written at the end of the session, from
memory, has already lost the details that make it useful.

## The file

One file at the project root: `WORKING_MEMORY.md` (or fold into an existing `PRODUCT.md` / `CHANGELOG.md` if
the project already keeps one — don't spawn a second). It is the single home for the durable notes that the
other forcing-function skills produce. Keep it to four sections:

```markdown
# Working Memory — <project/task>

## Status
- Where the work actually is right now. One or two lines, updated as it moves.

## Locked decisions (don't relitigate)
- [decision] — [one-line why]. e.g. "Accent only on primary action + active state — restraint."

## Failed approaches (and why) — the load-bearing section
- Tried [X] → [what went wrong]. Don't retry without [what would have to change].
  e.g. "Tried generateObject for tool-calling → silently dropped the tool schema. Use streamText + tools."

## Recurring mistakes to pre-empt (this model, this project)
- [the pattern this model keeps falling into]. e.g. "Defaults nav to centered-logo+3-links — specify nav up front."
- (pixel-critique-loop writes ## Render notes findings here; critic-pass writes ## Critic notes findings here.)
```

## How to run it

1. **At the start of substantial or resumed work, read the file first.** Before planning, before the first
   edit — so you inherit the failed approaches instead of rediscovering them. On a fresh session or after a
   compaction, this is the first action.
2. **Append the moment you learn something durable:** a decision you'd be annoyed to relitigate, an approach
   that failed and why, a mistake you've now made twice. Not a running log of everything — only what a future
   session (or a weaker model) would waste time without.
3. **Follow Anthropic's curation rules so the file stays an asset, not noise:** one lesson per entry with a
   one-line summary; record corrections *and* confirmed approaches, with the *why* (the why is what makes it
   transferable); don't save what the repo, git history, or chat already records; update an existing entry
   rather than duplicating; delete entries that turn out to be wrong. A memory file that isn't pruned stops
   being read.
4. **Re-read before each unit and before each critic pass.** This is what lets a weaker model with good notes
   beat a stronger model with amnesia on a long build.

## Why the "why" is non-negotiable

"Tried gradient hero bg → rejected" is nearly useless next session — it reads as an arbitrary ban. "Tried
gradient hero bg → generic SaaS tell, diluted the brand" transfers: it teaches the principle, so the model
generalizes instead of just avoiding one specific thing. The failed-approaches log is only as good as its
reasons.

## Composes with

- `pixel-critique-loop`: its recurring render findings live here under `## Render notes`.
- `critic-pass`: its recurring findings (the failure classes this model keeps hitting) live here under
  `## Critic notes` — so the same bug class gets pre-empted, not re-found.
- `model-steering`: the per-model "recurring mistakes" you discover here feed back into the preamble.
- `frontier-gap`: evidence and citations for the memory result are in its `references/evidence.md`.

## What this is NOT

- **Not a log of everything.** A transcript is not memory. Memory is the distilled, curated subset a future
  session needs — heavy on *why*, pruned of the obvious.
- **Not a substitute for the repo or git history.** If the code or commits already record it, don't.
- **Not write-only.** A notes file nobody re-reads is theater. The re-read on resume is the whole point.
