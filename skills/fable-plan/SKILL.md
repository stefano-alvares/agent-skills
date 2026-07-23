---
name: fable-plan
description: >-
  Plan implementations the way Fable 5 does — written from Fable's own introspection (July 2026). The
  measured basis: harness-level planning discipline alone lifted Sonnet 4.5 past the best research agent on
  SWE-Bench-Pro (52.7%) and Opus 4.5 past Anthropic's own harness (54.3% vs 52.0%, arXiv 2512.10398);
  Anthropic's long-horizon guidance prescribes one-feature-at-a-time, progress files, and fresh-context
  review. Use BEFORE any multi-step feature, refactor, or multi-file change on Sonnet 5 / Opus — after
  fable-standard interprets the request, before code. Produces a dependency-ordered plan where every step
  leaves the system green and carries its own proof. Ends by scheduling the review (critic-pass). Skip for
  single-file trivial changes — over-planning small work is itself a failure.
---

# Fable Plan

Sonnet's planning failure is not bad plans — it's shallow ones: category-ordered ("first types, then
components, then tests"), no per-step proof, no risk ordering, written before reading the code. Fable plans
from evidence, orders by dependency and risk, and makes every step independently verifiable. That
discipline, imposed by harness, measurably outperforms the model's default (arXiv 2512.10398).

## Phase 0 — Earn the right to plan (read first)

No plan before evidence. Read every file the change plausibly touches; trace ONE real flow end-to-end
(request → handler → logic → storage → response, or user action → state → render). Note existing patterns
and helpers you must reuse (lean-build Step 1 overlaps — run them together).

**The benchmark:** you can name the exact line ranges each step will touch and cite how the current flow
behaves. A plan citing files you haven't opened is a guess wearing a plan's clothes.

## Phase 1 — Decompose by dependency and risk, not category

1. List the shippable units — each one user-observable or test-observable on its own. One feature at a
   time; never plan to one-shot the whole thing (documented failure: context exhausts mid-implementation).
2. Order them so the system is GREEN after every step — each step lands, verifies, commits. Never "it'll
   compile again after step 4."
3. **Riskiest step first as a spike.** The step with the most unknowns (new API, unclear data shape,
   platform contract) can invalidate the plan — surface that before investing in the rest. Check the
   platform-gotcha log in code-style.md before assuming a hang/timeout is your logic.

**The benchmark:** if interrupted after any step, what's committed is releasable. If step N fails, steps
1..N-1 don't need reverting.

## Phase 2 — Per-step contract

For each step, four lines — no essays:

```
STEP n: [name]
FILES: [exact paths — anything else needs announcing]
PROOF: [the runnable check that fails if this step is wrong — test, build, curl, screenshot]
RISK:  [what this could break + the caller-grep that clears it]
```

A step whose PROOF line is "looks right" is not a step; find the runnable check or merge it into a step
that has one.

## Phase 3 — Context strategy (the part everyone skips)

Long tasks fail on context, not capability. Plan the memory explicitly:
- **Progress file** (WORKING_MEMORY.md / claude-progress.txt): update after every step — status, locked
  decisions, failed approaches + why. Measured: notes files cut cost ~11% AND raise resolve rate.
- **Checkpoints:** commit after each green step (matches Stefano's 1-feature-1-commit rule).
- **Fresh sessions over long ones:** plan where a `/clear` + file-handoff happens (between shippable
  units). Full resets with structured handoffs beat compaction; Sonnet specifically exhibits "context
  anxiety" in long sessions. The plan + progress file must contain everything a fresh session needs.
- **Delegate exploration:** codebase searches go to subagents; keep the main context for the plan and the
  diffs.

## Phase 4 — Lock and schedule the review

- The plan is the contract (plan-lock): restate it in one line before starting; deviations announced, never
  silent.
- Schedule the exit review NOW, in the plan: after the last step, critic-pass with a fresh-context
  verifier. Premature completion is a documented long-horizon failure — a later glance sees partial
  progress and declares done; the scheduled review is the guard.
- Write the plan's DONE line: the observable end state (all PROOFs green + ledger walked).

**The benchmark:** the plan names its own reviewer and its own done-proof before any code exists.

## Anti-patterns this replaces

- Category-ordered plans (types → components → tests) that leave the system red for hours.
- Plans written before opening the code.
- Steps with no proof, verified in one batch "at the end".
- 12-step plans for 2-step work — match plan weight to task weight.
- The plan living only in chat history, evaporating at compaction.

## Composes

fable-standard P1 (interpret) → **fable-plan** (+ lean-build contract merged into Phase 0/2) → plan-lock →
build with working-memory → critic-pass / fable-standard P4 (review) → ledger walk. Evidence:
frontier-gap/references/evidence.md.
