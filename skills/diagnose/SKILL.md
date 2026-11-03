---
name: diagnose
description: >-
  Use when something is broken, throwing, failing, slow or intermittent and the cause is not one obvious
  line: a bug that spans files, layers or services, a stack trace that makes no sense, a fix that already
  failed, or a performance regression. Red loop first, then a logic map to locate the fault by
  contradiction, then fix at the link with a regression test.
---

# Diagnose

A bug is a contradiction, not a mystery. The system was built so that a chain of claims produces correct
output; the symptom proves one of them false. Two things find it fast: a **red loop** (one command that
goes red on this bug) and a **logic map** (the chain the correct behaviour needs). The loop gives you
evidence; the map tells you which two files to read instead of eight.

Skip this skill for a bug with one obvious local cause (a typo, a stack trace naming the exact wrong
line): fix it, run the check, done.

**Read-only role.** A reviewer builds the red loop, adds instrumentation and runs bisect only in a
scratch clone (`cp -cR <repo> ~/.hermes/profiles/reviewer/cache/scratch/diag-<card>`), never in the repo
under review, and reports the fault and the proposed fix as text.

## 0. Start from the scenario (mapped projects)

If the project has `docs/crew/scenarios.json`, find the scenario the symptom breaks and run
`node ~/.hermes/tools/scenarios/scenarios.mjs check <root> <id> --no-save` (read-only: it writes nothing).
Its `want` and `expected` are the desired output; its steps are the chain, so the map in step 3 is half
built already; the first failing step, when probes exist, is your first bracket. A scenario that says met
while the symptom exists means its check does not cross the broken link: walk its steps against the code.
No scenario covers the symptom: that is a finding for `logic-map`. After the fix, whoever owns the batch
(not a reviewer, not a card that does not own the file) re-runs `check` and `sync` so the map shows it met.

## 1. Build a red loop

Get one command that drives the real code path and asserts the user's exact symptom. Try, roughly in
order: a failing test at the seam that reaches the bug; curl against the dev server; a CLI run diffed
against a known-good output; a headless browser script asserting on DOM, console or network; a replayed
captured payload; a throwaway harness around one function; a fuzz loop for "sometimes wrong"; a
`git bisect run` harness between a good and a bad state; old versus new on the same input. When a
person must click, drive them with `scripts/hitl-loop.template.sh`.

Then tighten it: faster (narrow scope, skip unrelated setup), sharper (assert the symptom, not "didn't
crash"), deterministic (pin time, seed randomness, freeze network). For flaky bugs, raise the
reproduction rate (loop 100 times, add stress) until it is debuggable.

**Done when** you have run the command at least once and can paste the invocation and its output, and it
is red-capable, deterministic (or a pinned high rate), fast and runnable unattended.

If you cannot build one, stop and say so: list what you tried and ask for access, a captured artefact
(HAR, log, recording) or permission to instrument. A Kanban worker blocks the card with that request. No
red loop, no hypotheses.

## 2. Reproduce and minimise

Run the loop and confirm it shows the failure the user described, not a neighbour. Capture the exact
symptom. Then cut inputs, callers, config and steps one at a time, re-running after each cut, until every
remaining element is load-bearing.

## 3. Map the logic

If the project already has a `## Logic map` (the `logic-map` skill writes one), read it and check it is
not older than the code it describes. Otherwise write one now, from contracts (docs, types, tests,
names), not from the implementation:

```
<system> takes: <input + invariant> gives: <output + invariant> owns: <invariant/state> fails: <throws | degrades | silent>
```

Persistent state and the clock are systems. The `fails` column is read from each consumer's error
handling, never assumed: the consumer that catches and continues with a default is the quiet, dangerous
one. Say which systems you exclude and why.

Then the causal chain, 6 to 12 links at the grain of decisions, each with its mechanism:

```
1. <trigger>
2. therefore <claim>   because <mechanism>
...
N. therefore <correct output>
```

## 4. Locate the fault by contradiction

Work backwards from the output. For each link ask: **if this link held exactly as written, would the
observed symptom still be possible?** No means the fault is at or upstream of this link; yes means it
survives. The fault lives between the last surviving link and the first failing one.

- **Absences are faults.** "Nothing re-sorts the list after the merge" is a located fault.
- **True but unordered.** Every link holds and the symptom still happens: suspect ordering, concurrency,
  staleness or caching. Ask the test again as "held before link N+1 ran".
- **Jointly wrong.** Two contracts disagree at a boundary (optional on one side, required on the other).
  The repair belongs on the side that owns the invariant.

Inside the bracket, write 2 to 4 ranked, falsifiable hypotheses: "If X is the cause, changing Y makes the
bug disappear." Show them to the user if one is around; do not block on it.

## 5. Instrument

Each probe tests one prediction; change one variable at a time. Prefer a debugger or REPL, then targeted
logs at the boundaries that separate hypotheses, tagged with a unique prefix such as `[DEBUG-a4f2]`.
Performance: measure a baseline first (timing harness, profiler, query plan), then bisect.

## 6. Fix at the link

| What step 4 found | The fix |
|---|---|
| A mechanism that does not do what its link claims | Correct the mechanism |
| A missing link | Add it at the layer that owns the invariant, not where the symptom showed |
| Two contracts disagreeing | Enforce the invariant on the owning side; let the other rely on it |
| A link that holds too late | Fix the ordering or trigger, not the value |

Grep the link's other consumers before editing. Write the regression test before the fix at a seam
that exercises the real bug pattern; on a board card, only where the card's `Test seams:` line names a seam,
otherwise the red loop's output is the proof; a missing seam is a finding to report. Watch it fail,
fix, watch it pass, then re-run the original red loop on the un-minimised scenario. Then run `falsify`.

Authorization to fix covers the repair; ask again only for changed scope, a reserved decision or a
security confirmation. Confirm the bracket once with the cheapest read; if it surprises you, your map was
wrong: go back to the mapping step (step 3).

Three failed fixes means the map is wrong: go back to step 3 and question a contract you assumed.

## 7. Clean up

- [ ] The original loop no longer goes red
- [ ] The regression test passes, or the missing seam is reported
- [ ] Every `[DEBUG-...]` line removed (grep the prefix)
- [ ] Throwaway harnesses deleted or clearly parked
- [ ] The confirmed cause is written in the return or commit message

If the honest answer to "what would have prevented this?" is structural (no seam, tangled callers),
note it for `raze-review` after the fix is in.

## Output

```
## Loop      <command, and the red output>
## Systems   <contract lines; excluded systems and why>
## Map       <numbered links>
## Fault     Bracket: link N held, N+1 cannot have. Fault: <false or missing claim, file:line>.
             Why it surfaces where it does: <...>. Confirmed by: <the read or command>.
## Repair    <the change at the link, other consumers checked, regression test, loop now green>
```

An unconfirmed cause is a hypothesis: leave "Confirmed by" empty and name the smallest command that would
settle it. A worked example is in `references/worked-example.md`.

## Routing

| Situation | Skill |
|---|---|
| Designing what should be guaranteed, not fixing | `logic-map` |
| Nothing crashed, the product behaves wrongly (AI misreads, a flow frustrates) | `mission-debug` |
| The code works but is tangled or over-built | `raze-review` |

## Red flags

| Thought | Reality |
|---|---|
| "The trace names this file, so the bug is here" | It names where the bug surfaced. Map first. |
| "Let me add logging and see" | With no bracket there are no candidates; you are collecting noise. |
| "Let me read a few more files" | Unbounded reading means the map is missing. |
| "Probably X, quick fix" | Run the impossibility test on X first. |
| "Intermittent, so environmental" | Usually a link that is true but unordered, or state outliving a run. |
| "Grep listed the consumers, blast radius done" | Read each catch: one throws, another silently degrades. |
| "My map says the code should work, so the code is fine." | The symptom outranks the map. A map that predicts no bug is wrong: go back to step 3. |

Loop phases adapted from Matt Pocock's diagnosing-bugs (github.com/mattpocock/skills); the map and
contradiction method is Stefano's logic-first-debug. Both originals are in `~/.agents/archive/`.
