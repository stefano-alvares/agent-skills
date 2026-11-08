---
name: ship-spec
description: >-
  Use when Stefano asks for a ship spec (/ship-spec), or before planning substantial work: a new batch,
  feature, redesign, cleanup or repair wave; or when audits, reviews and findings have piled up on one
  system with little shipped ("tie these together", "ship this once and for all", "it's been too long").
  Defines what ships and how he will know it is done; plan-forge then plans how and in what order. Skip
  for a clear single-path fix or plan-forge's quick mode.
---

# Ship Spec

Step one of two. **ship-spec says what ships and when it is done. `plan-forge` says how, and in what
order.** The spec is the contract he approves; the plan serves it. Keeping them apart stops a plan from
quietly redefining the goal to fit the work.

Output: the **Ship spec** section at the top of the batch file, `docs/crew/<date>-<slug>.md`, in both
harnesses. Skeleton in `references/batch-file.md`. The batch file is the one authority; never write a
second spec document beside it.

**Documents are witnesses; the system is the evidence.** Any claim the spec depends on (a row exists, a
branch merged, a check passes, a file is missing) is probed now, not quoted from a doc.

## 1. His words

Copy his request verbatim, typos included, and number every ask in it, including parentheticals and
trailing "also" clauses. Each number gets a bucket in section 4. An ask you drop is a silent scope cut.

## 2. Mission

One plain line: who gets what value when this ships. If it does not fit one line, the work is not
understood yet: ask before writing anything else.

## 3. Definition of shipped

Three to five checkable lines, written before any task: what he will click, open or run to know the work
is over. Each line names its check (a URL at a viewport, a command and its expected output, a row count).
"Looks good" is not a line; "he approves the preview" is, when taste is the point. On a mapped project
(`docs/crew/scenarios.json`), the scenarios the batch touches being met is one of the lines. These lines
are closed at batch end by `falsify` step 7, which runs each check and writes the Close-out.

## 4. Ask ledger

Every numbered ask lands in exactly one bucket. Nothing stays open.

| Bucket | Requirement |
|---|---|
| **TASK** | What must be true, an owner (agent, or operator plus the named human action), a gate (spend, DB write, decision, or none) and a runnable done-check |
| **DONE** | Already true, proved by a check you ran now, not by a doc |
| **DEFERRED / ACCEPTED LOSS** | His reason recorded, so it stops resurfacing |
| **REFUTED** | False when written, with the evidence |

A claim you could not verify is written `assumed`, visibly. A task he must do himself (a migration, a
dashboard setting, a payment) names the exact action.

## 5. Out of scope, and his calls

- **Out of scope:** what this batch deliberately does not ship, and when it would be added.
- **Needs your call:** the decisions that are his (scope, taste forks, sitemap, architecture, new
  dependencies, data changes, spend), each with your recommendation first. Ask them in one round with the
  spec. Answers go under **Decided**; an unanswered fork stays out of scope and is listed again in the
  next report. Silence is not a yes.

## 6. Piles of findings

When several audits, reviews or repair plans on one system produced little shipped work, run
`references/consolidate-findings.md` first (ground truth table, document map, consolidated invariants,
every finding dispositioned), then write sections 2 to 5 from its result. If the findings are unbounded,
the system needs `raze-review`, not another document.

## 7. Hand off

If he asked for the spec to review, stop and show it: the mission, the Definition of shipped and the
Needs-your-call list first. A new app, site or process; work touching checkout, payments, auth, personal
data, a database or 8+ code files; or a new user-facing flow across 2 or more parts (`logic-map` owns
this definition: change it there first, then here): `logic-map` next. It turns the spec
into scenarios on a map, and his OK on the map and the Needs-your-call list come in one round. Otherwise
continue into `plan-forge` in the same turn; it reads this section and does not redo it.

## Red flags

| Thought | Reality |
|---|---|
| "The doc says it's still open" | Probe it. Docs drift; the system is the evidence. |
| "I'll summarise the request" | Verbatim and numbered. A summary drops asks. |
| "Done means the code is written" | Done is what he clicks or runs. Write those lines first. |
| "This ask is awkward, leave it open" | TASK, DONE, DEFERRED or REFUTED. Open limbo is banned. |
| "The metric drops if we do the honest task" | His decision, named in the task's gate. Never softened silently. |
| "I'll put the plan in the spec" | Order, files and steps belong to plan-forge. The spec is what and when, not how. |
