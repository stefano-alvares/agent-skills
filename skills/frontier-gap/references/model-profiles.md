# Per-model failure profiles and preambles

(Absorbed from the retired `model-steering` skill, 2026-07-24. Full sourcing: `evidence.md`.)

The same forcing functions don't fail all weaker models the same way, because the models don't fail the
same way. A preamble telling GPT-5.5 "keep going, don't stop early" solves Composer 2's problem, not
Composer 2.5's. Name the model and its known failure before starting — then pre-empt that specific
failure, not failure in general. The same fixed model has been measured swinging **+12.8pp** between
harnesses; how you steer it is not a rounding error.

## Cursor Composer 2.5 — failure: silent plan/shortcut drift + scope creep

Early stopping was **Composer 2**; 2.5 fixed that and now keeps going while tests are red. Its residual
failure is diverging from the plan mid-task to take a faster shortcut *without saying so*, and touching
files outside the request. Cursor itself says self-verification can't be trusted (reward-hacking observed).

> Preamble: *"Restate the plan in one line before you start, and again if you change it. If you deviate
> from it or take a shortcut for speed, say so explicitly and why — don't change the approach silently.
> Touch only what the task requires; list any file you're about to edit that wasn't in the plan and
> justify it. You are not the verifier — I will check the diff and the tests."*

## GPT-5.5 — failure: dropped constraints + overeager action

Strong autonomy and throughput, but documented for "overeagerly taking action" and ignoring user
constraints on code changes; trails on repo-level multi-file work. Responds well to an explicit rubric.

> Preamble: *"List every constraint from my request as a checklist before you start, and tick each one
> against your output before you finish. Don't take action beyond what I asked — propose, don't expand.
> For anything non-trivial, first write a 5–7 point rubric for what a correct solution looks like, then
> build against it."* (The rubric pattern is OpenAI's own one-shot-quality recommendation.)

## Local models (Gemma / GLM / etc.) — failure: fast drift, short memory

Drift fastest; lose sequential constraints soonest. The working-memory file (protocols.md → Context
strategy) does the heaviest lifting here.

> Preamble: *"Re-read WORKING_MEMORY.md and my original request before each step. Work in small units;
> after each, state what you just did and what's left. If you're unsure, decide the most reasonable
> assumption, proceed, and write it down — don't stop to ask."*

## Claude Sonnet 5 — failure: plausible-instead-of-verified details, weak verification, silent-hang defaults

Observed repeatedly in Stefano's own sessions (training-app Garmin ingest, June 2026), all caught only by
a review agent or the next session:

- **Documented values from plausibility, not source.** Wrote all 4 error strings in an ops README as
  verbose plausible variants; none matched what `ingestion_run.py` actually emits.
- **Weak verification greps.** A "confirm old strings gone" grep false-positived on gloss text; a
  call-order test asserted 3 of 4 required steps and the task was reported done.
- **Scope creep on "minimal change" tasks.** A minimal-specced task added 91+ lines and new components to
  page.tsx — blocking review issue.
- **Silent-hang defaults.** A poll loop handled only known statuses; unknown/missing status spun silently
  to timeout. Fail-fast had to be retrofitted.

> Preamble: *"Never write down a string, value, or behavior claim without grepping the canonical source
> and citing file:line — docs written from memory are the #1 review-rejection cause here. When you verify
> with a grep, anchor the exact expected string and read the matches — don't trust match-count. A test
> that verifies N of M required steps is not done. Touch only files the task names; list and justify any
> addition. In state handling, unknown/missing = fail fast and loud, never silently continue."*

## Claude Opus 4.8 — failure: rushed single pass, quality variance

Community-confirmed elevated error incidents (June 2026) plus low-effort "scopes work to the literal ask."
The documented fix is to raise effort, not to prompt around it.

> Preamble: *"This is a [high-stakes/long-horizon] task — spend effort proportional to that. Don't stop
> early on token-budget worries; context will compact. Before saying done, make one full pass over every
> claim in your summary and point each at a tool result (file:line, test output, render). Resolve the
> query completely before handing back."*

## The cross-model floor (every preamble inherits this)

These appear, in some form, in both OpenAI's and Anthropic's published guidance:

- **Don't stop early.** "Keep going until the query is completely resolved; only terminate when you're sure."
- **Decide and document, don't stall.** On uncertainty, choose the most reasonable assumption, proceed,
  and record it — rather than bouncing it back.
- **Ground progress claims in evidence.** Before saying something works, point to the tool result that
  shows it. This "nearly eliminated fabricated status reports" in Anthropic's testing.

## Calibrate effort to stakes

Effort tunes *depth per step*; on a throwaway script keep it low, on an auth or payment path raise it.
The preamble's job is to stop the model quitting or drifting *below* the floor the stakes demand — not to
make everything maximal. Maximal effort on routine work invites the opposite failure (over-engineering).

## Evolving these profiles

Ground profiles in the user's own history first: before writing or updating one, run claude-mem
`mem-search` for real incidents (bugfixes, review rejections, retrofitted fixes) — a profile citing
"training-app Task 7, June 2026" steers harder than a published benchmark. Published research is the
floor; session history is the target. Recurring per-model mistakes discovered in WORKING_MEMORY.md fold
back into the preamble.
