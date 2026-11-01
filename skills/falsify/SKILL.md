---
name: falsify
description: >-
  Use when about to call work done, green or passing: especially when the only evidence is tests you
  wrote yourself or tests on mocks, after adding a guard or invariant at one call site, or when checking
  another agent's completion claim. The one done-gate: get a real signal, scan siblings, break each
  test, report verified and unverified surface.
---

# Falsify

Passing tests prove the code matches the mental model that wrote it. They do not prove the model is
right. Self-review with no external signal makes answers worse; review against a real signal (a run, a
render, a fresh reviewer) makes them better. So this skill is not "reflect harder". It is: get a real
signal, then try to break the work against it.

**The rule:** nothing is done until it has survived one pass against external evidence with no open
must-fix finding. "Looks right" and "should work" are not passes.

Misses cluster on the undo path, the negative path and the second file. Check those first.

## 1. Get a real signal

Take the strongest one available:

1. **Run it.** Tests, build, typecheck, the endpoint from a shell, the page rendered (Hermes:
   `node ~/.hermes/tools/shots/shots.cjs <url> <out> <routes>`; Claude Code: a browser screenshot at
   desktop and phone width).
2. **A fresh-context check.** For anything substantial, hand the spec and the diff to someone who did
   not write it (a subagent, or Argus on the board) and ask what breaks.
3. **A hand trace, only if you cannot run or dispatch.** Take a concrete input and predict the output
   line by line along the critical path. This is the weakest form. Mark it as a trace in the report.

Always try the edges: empty, null, the off-by-one boundary, the error branch, the concurrent case.

## 2. Sibling scan

Every invariant you applied at one site, apply to its siblings or say why it does not belong there.

1. List what you wrote: functions, guards, migration statements, route handlers, copy strings.
2. For each, list its siblings: same file, same table, same resource, same verb family
   (`create`/`delete`, `confirm`/`dismiss`, `open`/`close`). Grep every caller of what you changed.
3. Fill the table. A row you cannot fill is a finding.

| invariant | applied at | sibling | applied there? / N-A because |
|---|---|---|---|

Idempotency, uniqueness, rate limits, auth checks, `if exists` guards, timezones, caps on input size and
null handling are the invariants most often applied once and dropped twenty lines below.

## 3. Break each test

For every test the claim rests on:

1. **Mutate.** Name the one-line source change that should make it fail. Where that is cheap, apply it,
   run the test, confirm it goes red, and revert. A test that stays green under the mutation asserts
   the call you made, not the behaviour you meant. Rewrite it.
   Read-only role (reviewer): `cp -cR <repo> ~/.hermes/profiles/reviewer/cache/scratch/mut-<card>`
   (APFS clone, fast, node_modules included), apply the mutation there, run the test, delete the clone.
   Never mutate the repo under review. Builders mutating in place: `cp <file> <scratch>/<name>.orig`,
   mutate, run, `cp` it back (git restore and checkout are denied), then confirm `git diff --stat`
   matches what it was before.
2. **Doubles.** If it uses a mock, stub, fake or in-memory store, name one real behaviour the double
   does not model (constraints, ordering, transactions, partial failure, error shapes). That is
   unverified surface.

| test | mutation | ran red? (yes / named only) | what the double cannot model |
|---|---|---|---|

## 4. Check the usual failure classes

- **Superficially correct:** hardcoded expected values, swallowed errors, stubs returned as results.
- **Drift:** re-read the original request and the card. Tick each requirement against the output.
- **Scope creep:** machinery nobody asked for. Cut it or list it.
- **Docs versus source:** every string or value the output documents must match the file that emits
  it. Cite file:line.
- **The check itself:** a grep or test can pass while proving nothing. Anchor the exact expected string
  and read the matches. Count the steps a sequence test asserts.

## 5. Findings, ranked

Write each finding as a reviewer's report ("The check shows the retry path skips the cap"), then answer
it. Findings framed as someone else's report get fixed more readily than doubts about your own work.

```
MUST FIX:   <finding, file:line, the evidence>
SHOULD FIX: <finding>
ACCEPTED:   <finding, and why it is out of scope or safe>
```

## 6. Fix, then re-run

Apply the must-fixes and re-run the signal from step 1. A fix you did not re-run is a new unreviewed
change. Re-run once after fixes. If a must-fix remains, report it; do not start a third pass. In a
read-only role (Argus), report the repair instead of making it.

## Required completion report

Never report "done", "green" or a test count on its own. Fill all three:

- **Verified:** each command you ran, with the lines of output that matter (counts, the red-then-green
  mutation results).
- **Unverified surface:** column 4 from step 3, traces, and anything deliberately not tested.
- **Not run:** checks you skipped, and why.

An empty Unverified line is a claim that the doubles model reality completely. Write that claim out or
fill the line. Report in the `brutal-honesty` register: failures first.

## Calibrate

A throwaway script gets one run and a sibling glance. Auth, payments, data and anything a client sees
get the full pass, with a fresh-context check. Never skip to zero on anything that ships.

## Common mistakes

| Mistake | What it looks like |
|---|---|
| Scanning only the file you edited | The sibling lives in the migration, the route or the caller |
| Treating the mock as neutral | The double decides which bugs any test can reach |
| A test count as proof | Nothing about a count says the suite could fail |
| Naming a mutation but never running it | The test may still be green under it |
| Stopping at the happy path | The skipped sibling is usually the negative or undo path |

## When not to use

One-line changes with no siblings and no new tests, pure formatting, reading tasks.
