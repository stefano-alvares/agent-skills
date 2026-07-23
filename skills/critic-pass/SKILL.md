---
name: critic-pass
description: >-
  Force a validation pass before any work is declared done — but validate against EXTERNAL EVIDENCE, not
  introspection. The research is sharp on this: a fresh-context verifier (a subagent that didn't write the
  code, a run of the tests, a render of the page) measurably beats self-critique, and bare "let me re-read
  this, looks right" review with no external signal has been shown to LOWER accuracy — it flips correct
  answers to wrong (Huang et al.). This is the single habit that most separates frontier agentic models
  (Fable 5, which at high effort reflects on and validates its own work) from cheaper ones (Composer 2.5,
  GPT-5.5, local) that ship the first plausible output. Anthropic's own production guidance adds an explicit
  fresh-context verifier even for the frontier model — a weaker one needs it more. Run on ANY substantive
  output before "done": a feature, a refactor, a multi-file change, a bug fix, a generated document, a UI. It
  hunts the failure classes that are actually measured in agent-trajectory studies — under-propagated edits
  (read-recall >0.9 but edit-recall <0.5: fixed 2 of 4 call sites), reward-hacked/stub solutions, dropped
  constraints, scope creep. In Claude Code the verification means executing: Bash for tests/build, the
  preview_* tools to render UI, or a dispatched verifier subagent. Composes with verification-before-completion,
  requesting-code-review, systematic-debugging, working-memory, and pixel-critique-loop. Trigger automatically
  whenever about to conclude a task; skip only trivial one-line edits and pure factual questions.
---

# Critic Pass

Frontier agentic models are not mainly better at *generating* — on saturated evals the gap to cheaper models
is modest. They are better at **not stopping on the first plausible output**. Fable 5's documented edge is
that at high effort it reflects on and validates its own work before returning — and Anthropic's own guidance
adds a sharp detail: the verification that works is **external**. *"Separate, fresh-context verifier subagents
tend to outperform self-critique."* The research underneath is unambiguous and load-bearing for this whole
skill: self-review grounded in a real signal (a test run, a render, a fresh judge) improves correctness
(Reflexion: 91% vs 80% pass@1); self-review with **no** external signal *decreases* it (Huang et al. — the
model talks itself out of correct answers as often as it fixes wrong ones).

So this skill is not "reflect harder." It is: **go get a real signal, then judge against it.** Your job is to
refuse to let the model exit on a first draft it merely *believes* works.

## The one rule

**No task is done until it has survived one validation pass against external evidence with zero unaddressed
must-fix findings.** "Looks right" is not a pass. "I believe this works" is not a pass. A pass is: you ran
it / rendered it / had a fresh check look at it, you found the real problems, and you fixed or consciously
accepted each one.

If you catch yourself about to write "this should work" or "done" without having run the loop below — stop.
That sentence is the exact failure this skill prevents.

## Where this sits

The adversarial layer on top of your verification tools, not a replacement:
- `verification-before-completion` (superpowers) — the evidence discipline (run the command, show output).
  Critic-pass is its Step 2 mechanic, plus the failure-class hunt it doesn't prescribe.
- `requesting-code-review` — the *external human/agent* reviewer. Critic-pass is the internal pass you owe
  before you ask anyone else to look; its strongest form (a fresh-context verifier subagent) is a self-served
  version of the same idea.
- `systematic-debugging` — where a confirmed must-fix goes when the cause isn't obvious.
- `pixel-critique-loop` — critic-pass specialized for UI; its render-and-look loop IS the "run it" step for
  anything visual.
- `working-memory` — where recurring findings get logged so the same class of bug is pre-empted, not re-found.

Evidence and citations for every claim above: the `frontier-gap` skill's `references/evidence.md`.

## The loop

Run at least one full pass. Run a second if the first surfaced structural (not cosmetic) problems.

### Step 1 — Get an external signal (in this order of preference)

The whole pass is only as good as the signal you judge against. Prefer, top to bottom:

1. **Run it.** In Claude Code: `Bash` to run the tests, run the build, hit the endpoint; `preview_*` to
   render the page. Actual execution beats reasoning about execution every time, and it's the evidence you
   can hand to the next person.
2. **Dispatch a fresh-context verifier.** For anything substantial, spawn a subagent that did NOT write this,
   hand it the spec and the diff, and ask it to find what breaks. A reviewer without the author's context and
   without the author's wish-to-be-done catches what self-review can't — this is Anthropic's explicit
   recommendation, and it's why `requesting-code-review` exists.
3. **If you genuinely cannot run or dispatch, trace it — but change stance first.** Stop being the author;
   become a reviewer mildly skeptical it works. Walk the critical path by hand with a concrete input and
   predict the output line by line. This is the *weakest* form and is only valid because you're tracing
   against a concrete execution, not asking yourself "am I sure?" — bare introspection here makes things
   worse, not better.

Always check the **edges**, not just the happy path: empty input, null, the off-by-one boundary, the
concurrent case, the error branch, the thing the user didn't mention but clearly needs.

### Step 2 — Hunt the specific failure classes weaker models hit

These are measured in agent-trajectory studies, not hypothetical. Check each:

- **Edit localization (the big one).** Agents reach read-recall >0.9 but edit-recall <0.5 — they read every
  relevant file correctly, then under-propagate, fixing 2 of the 4 call sites. Grep for *every* usage of what
  you changed and confirm each was handled. This is the highest-frequency real bug a critic pass catches.
- **Reward-hacked / superficially correct.** Does it actually solve the problem, or pass the obvious check
  while doing the wrong thing — hardcoding the test's expected value, catching-and-swallowing the error,
  returning a stub? Cursor observed exactly this in Composer's training and concluded self-verification can't
  be trusted; assume the same and look for it.
- **Instruction drift.** Re-read the original request. Did a constraint get quietly dropped partway through?
  Weaker models lose sequential constraints over a long task (Composer 2.5's signature failure is silent
  drift to a faster shortcut). List the requirements; tick each against the output.
- **Over-engineering / scope creep.** Did machinery nobody asked for get added? Cut it. (This is the failure
  frontier models hit at *high* effort, so it's worth a deliberate look.) Real incident: a task specced
  "minimal change to page.tsx" shipped 91+ added lines, new interfaces, and new components — blocking review
  issue (training-app Task 6, June 2026).
- **Docs/claims vs canonical source.** Every string, value, or behavior the output *documents* must
  grep-match the file that actually emits it — cite file:line. Real incident: an ops README documented all 4
  sanitized error strings as plausible verbose variants; none matched `ingestion_run.py`; only a review agent
  grepping the source caught it (training-app Task 7, June 2026).
- **Verification quality itself.** A grep or test can pass while proving nothing. Anchor the exact expected
  string and *read the matches* — a "confirm old strings gone" grep once false-positived on retained gloss
  text. And count the steps: a call-order test that asserts 3 of 4 required steps is an unfinished check, not
  a pass (both training-app, June 2026).

### Step 2.5 — The attribution trick (use it on every finding)

Models fix errors far more readily when the error is attributed to an EXTERNAL source than when it sits in
their own reasoning — relabeling the same claim from self to external raised correction rates by 23–93
percentage points (arXiv 2606.05976, measured across Claude, GPT, and open models; panel-unverified, primary
source). Exploit this mechanically:
- Phrase each finding as if a reviewer wrote it: "The reviewer reports the poll loop hangs on unknown
  status" — then respond to the reviewer. Don't phrase it as "I might have missed…".
- This is also WHY fresh-context verifier subagents work: their findings arrive externally attributed.
  When you can't dispatch one, the phrasing trick is the cheap substitute.

### Step 3 — Write the findings down, ranked

Produce an explicit list, not a vibe:

```
MUST FIX:
- [the call site in api/routes.ts was not updated → stale type still thrown]
SHOULD FIX:
- [error message is vague, won't help the user]
ACCEPTED (with reason):
- [no mobile layout yet — out of scope for this PR, logged in WORKING_MEMORY.md]
```

If MUST FIX is empty **and you judged against a real signal** (not a glance), the pass succeeds.

### Step 4 — Fix and re-verify the fix

Apply the must-fixes, then re-run / re-render to confirm the fix didn't break something else. A fix you
didn't verify is a new unreviewed change. Log recurring findings — the failure classes this model keeps
hitting — to `WORKING_MEMORY.md` under `## Critic notes`, so next time they're pre-empted instead of
rediscovered. That feedback loop is what `working-memory` is for.

## Calibrate effort to stakes

A critic pass on a throwaway script is two minutes and a single test run; on an auth flow or a payment path
it's a fresh-context verifier plus edge cases plus a re-run. Match depth to the cost of being wrong — the
guidance is explicit that verification should be proportional to error cost — but never skip to zero on
anything that ships.

## What this skill is NOT

- **Not introspection.** "Re-read it and reflect" with nothing run is the failure mode, not the method —
  it's measured to lower accuracy. Every pass must touch reality.
- **Not a rubber stamp.** A pass that finds nothing because it didn't look is the exact failure it targets.
- **Not infinite polishing.** Two solid passes on hard work; stop when only nitpicks remain.
- **Not a substitute for real tests.** Where tests can exist, write them — running them is the strongest
  possible critic and the one you can hand off as proof.
