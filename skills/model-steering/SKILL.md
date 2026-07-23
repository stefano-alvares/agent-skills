---
name: model-steering
description: >-
  Set an explicit per-model preamble before substantial agentic work that forbids the specific failure the
  current model is prone to — early stopping, silent plan/shortcut drift, dropped constraints, or
  overeager scope creep — and raises its effort to match the stakes. Frontier models (Fable 5) hold a high
  effort bar and don't hand back early on their own; weaker and cheaper models need it imposed. This is
  documented, not generic: OpenAI ships a verbatim persistence preamble for GPT-5 ("keep going until the
  query is completely resolved… only terminate when sure"); Cursor admits Composer 2.5 self-verification
  can't be trusted and that the same fixed model swung double digits under a different harness; Anthropic
  says raise effort rather than prompting around shallow reasoning. Crucially, the failure differs by model —
  Composer 2.5's problem is silent drift (NOT early stopping, which was Composer 2), GPT-5.5's is
  constraint-dropping and overeager action, a local model's is fast drift. Use this when driving a non-Claude,
  local, or low-effort model, when starting a long autonomous run, or when output is rushed/lazy/half-done;
  it picks the right preamble for the model in play. Skip for trivial edits and pure questions.
---

# Model Steering

The same forcing functions don't all weaker models the same way, because they don't fail the same way. A
preamble that tells GPT-5.5 to "keep going and don't stop early" is solving Composer 2's problem, not
Composer 2.5's — and will do nothing about the drift that 2.5 actually exhibits. This skill sets the right
preamble for the model actually in play, and raises the effort bar to the stakes. It's the cheapest lever in
the family and often the highest-leverage on a weak model: the same fixed model has been measured swinging
**+12.8pp** between harnesses, so how you steer it is not a rounding error.

## The one rule

**Name the model and its known failure before you start — then pre-empt that specific failure, not failure
in general.** A generic "be thorough" preamble is weak because it's untargeted. "Composer 2.5 drifts from the
plan silently to take shortcuts — restate the plan and flag any deviation out loud" is strong because it
blocks the actual hole.

## Pick the preamble for the model in play

Read the model's profile, then prepend the matching preamble to the task. Full sourcing in `frontier-gap`'s
`references/evidence.md`.

### Cursor Composer 2.5 — failure: silent plan/shortcut drift + scope creep
Early stopping was **Composer 2**; 2.5 fixed that and now keeps going while tests are red. Its residual
failure is diverging from the plan mid-task to take a faster shortcut *without saying so*, and touching files
outside the request. Cursor itself says self-verification can't be trusted (reward-hacking observed).
> Preamble: *"Restate the plan in one line before you start, and again if you change it. If you deviate from
> it or take a shortcut for speed, say so explicitly and why — don't change the approach silently. Touch only
> what the task requires; list any file you're about to edit that wasn't in the plan and justify it. You are
> not the verifier — I will check the diff and the tests."*

### GPT-5.5 — failure: dropped constraints + overeager action
Strong autonomy and throughput, but documented for "overeagerly taking action" and ignoring user constraints
on code changes; trails on repo-level multi-file work. Responds well to an explicit rubric.
> Preamble: *"List every constraint from my request as a checklist before you start, and tick each one
> against your output before you finish. Don't take action beyond what I asked — propose, don't expand. For
> anything non-trivial, first write a 5–7 point rubric for what a correct solution looks like, then build
> against it."* (The rubric pattern is OpenAI's own one-shot-quality recommendation.)

### Local models (Gemma / GLM / etc.) — failure: fast drift, short memory
Drift fastest; lose sequential constraints soonest. `working-memory` does the heaviest lifting here.
> Preamble: *"Re-read WORKING_MEMORY.md and my original request before each step. Work in small units; after
> each, state what you just did and what's left. If you're unsure, decide the most reasonable assumption,
> proceed, and write it down — don't stop to ask."*

### Claude Sonnet 5 — failure: plausible-instead-of-verified details, weak verification, silent-hang defaults
Observed repeatedly in Stefano's own sessions (training-app Garmin ingest, June 2026), all caught only by a
review agent or the next session:
- **Documented values from plausibility, not source.** Wrote all 4 error strings in an ops README as verbose
  plausible variants; none matched what `ingestion_run.py` actually emits. Would have misled on-call operators.
- **Weak verification greps.** A "confirm old strings gone" grep false-positived on gloss text; a call-order
  test asserted 3 of 4 required steps and the task was reported done.
- **Scope creep on "minimal change" tasks.** Task specced as minimal added 91+ lines and new components to
  page.tsx — blocking review issue.
- **Silent-hang defaults.** A poll loop handled only known statuses; unknown/missing status spun silently to
  timeout. Fail-fast had to be retrofitted.
> Preamble: *"Never write down a string, value, or behavior claim without grepping the canonical source and
> citing file:line — docs written from memory are the #1 review-rejection cause here. When you verify with a
> grep, anchor the exact expected string and read the matches — don't trust match-count. A test that verifies
> N of M required steps is not done. Touch only files the task names; list and justify any addition. In state
> handling, unknown/missing = fail fast and loud, never silently continue."*

### Claude Opus 4.8 — failure: rushed single pass, quality variance
Community-confirmed elevated error incidents (June 2026) plus low-effort "scopes work to the literal ask."
The documented fix is to raise effort, not to prompt around it.
> Preamble: *"This is a [high-stakes/long-horizon] task — spend effort proportional to that. Don't stop early
> on token-budget worries; context will compact. Before saying done, make one full pass over every claim in
> your summary and point each at a tool result (file:line, test output, render). Resolve the query completely
> before handing back."*

## The cross-model floor (every preamble inherits this)

These appear, in some form, in both OpenAI's and Anthropic's published guidance:
- **Don't stop early.** "Keep going until the query is completely resolved; only terminate when you're sure."
- **Decide and document, don't stall.** On uncertainty, choose the most reasonable assumption, proceed, and
  record it — rather than bouncing it back.
- **Ground progress claims in evidence.** Before saying something works, point to the tool result that shows
  it. This "nearly eliminated fabricated status reports" in Anthropic's testing.

## Calibrate effort to stakes

Effort tunes *depth per step*; on a throwaway script keep it low, on an auth or payment path raise it. The
preamble's job is to stop the model quitting or drifting *below* the floor the stakes demand — not to make
everything maximal. Maximal effort on routine work invites the opposite failure (over-engineering).

## Composes with

- `plan-lock`: the preamble's "don't drift silently" clause is the floor; `plan-lock` is the discipline that
  enforces it — write the plan, restate it, announce deviations. Most load-bearing for Composer 2.5.
- `critic-pass`: the preamble sets the "don't stop early" bar that makes the critic pass actually run instead
  of getting skipped.
- `working-memory`: recurring per-model mistakes you discover get written there and fold back into the preamble.
- `frontier-gap`: the per-model profiles and their sources live in `references/evidence.md`.

## What this is NOT

- **Not fine-tuning.** Despite the old "model-tuning" name, nothing here touches weights — it's prompt-level
  steering only.
- **Not a generic pep talk.** An untargeted "try hard" preamble underperforms one aimed at the model's actual
  failure mode. Specificity is the whole point.
- **Not a license to skip verification.** Steering reduces the failure rate; it doesn't replace `critic-pass`.
