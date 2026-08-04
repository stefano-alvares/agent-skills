---
name: falsify
description: >-
  Use when about to report work as done, complete, green, or passing — especially when the only
  evidence is a test suite you wrote yourself, when tests rely on mocks/stubs/fakes, or after
  applying a guard, constraint, or invariant at one call site. Also use when reviewing another
  model's finished work before trusting its completion claim.
---

# Falsify

Passing tests prove the code matches the mental model that produced it. They do not prove the
mental model is right. A test written alongside the code inherits its blind spots — including
which bugs the mocks make reachable at all.

Two passes. Each produces a table. Run both before saying done.

**Model profile:** if `profiles/<model-id>.md` exists for the model you are running as, read it
first — it names that model's observed failure signature and which pass to weight. No matching
profile: run the core passes as written.

## Pass 1 — Sibling scan

Every invariant you applied at one site, apply to its siblings or state why it does not belong.

1. List what you wrote: functions, guards, migration statements, route handlers.
2. For each, list its **siblings** — same file, same table, same resource, same verb family
   (`confirm`/`dismiss`, `create`/`drop`, `add`/`remove`, `open`/`close`).
3. Fill the table. Any row you cannot fill is the finding.

| invariant | applied at | sibling | applied there? / N-A because … |
|---|---|---|---|

Idempotency, uniqueness, rate limits, auth checks, `if exists` guards, timezone arguments, and
null handling are the invariants that most often get applied once and dropped on the sibling
twenty lines below.

## Pass 2 — Falsify each test

For every test you wrote:

1. Name the **one-line source change that makes it fail.** If you cannot name one, the test
   asserts the call you just made rather than the behaviour you intended. Rewrite it.
2. If it uses a mock, stub, fake, or in-memory double: name one real behaviour the double does
   **not** model — uniqueness constraints, concurrency, ordering, transactions, partial failure,
   error shapes. That is unverified surface, not covered surface.

| test | one-line change that breaks it | what the double cannot model |
|---|---|---|

## Required completion report

Never report "done", "green", or a test count on its own. Two slots, both filled:

- **Verified:** what ran, what passed, counts.
- **Unverified surface:** every entry from Pass 2 column 3, plus anything deliberately not tested.

An empty Unverified surface line is a claim that the doubles model reality completely. Write that
claim explicitly or fill the line.

## Common mistakes

| Mistake | What it looks like |
|---|---|
| Scanning only the file you edited | The sibling lives in the migration, the route, or the caller |
| Treating the mock as neutral | The double decides which bugs are reachable by any test |
| Reporting a test count as proof | A count is a count. Nothing about it says the suite could fail |
| Stopping the scan at the happy path | The sibling that got skipped is usually the negative or undo path |

## When not to use

Single-line changes with no siblings and no new tests. Pure formatting. Reading tasks.
