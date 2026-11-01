---
name: plan-forge
description: >-
  Use when a batch, feature, refactor or repair wave touches more than one file and needs a plan before
  building; when the owner hands over a brief or an approved design; or when audits and findings have
  piled up on one system and need one executable spec. Three modes: light (design batches), standard
  (multi-file code), high-risk (checkout, payments, auth, personal data, a database, 8+ code files).
---

# Plan Forge

The one planner. It turns a brief into a locked plan ordered by dependency and risk. Standing rules:
evidence only, done-checks runnable, every ask lands in a bucket, deviations said out loud.

Skip it for a single-file change. A plan for a one-liner is theatre.

## Pick the mode

| Mode | When | Output |
|---|---|---|
| **Light** | Design, page, copy and polish batches: anything his eye judges on a preview | The batch file: his words, Decided, Defaults, Definition of shipped, cards split by file |
| **Standard** | A multi-file code change | Light, plus the evidence pass, steps with FILES / CHANGE / PROOF / RISK, and the build contract |
| **High-risk** | Checkout, payments, auth, personal data, a database, 8+ code files or 2+ new services | Standard, plus the high-risk review in `references/high-risk-review.md` |

Page, copy and polish batches stay Light however many files they touch; a form that only posts to an
existing endpoint does not make a batch high-risk.

## 1. Interpret and open the ledger (all modes)

Rewrite the request as a task spec a stranger could execute: the goal behind the ask, explicit and
implicit constraints, what done means. Number every ask in his words, including parentheticals and
trailing "also" clauses. By the end, each ask sits in exactly one bucket:

| Bucket | Requirement |
|---|---|
| **TASK** | Ordered into the plan with an owner (agent, or operator plus the named human action), a gate (spend, DB write, decision or none) and a runnable done-check. A gated task is not carded until he has answered |
| **DONE** | Already true, proved by a check you ran now, not by a doc |
| **DEFERRED / ACCEPTED LOSS** | His reason recorded, so it stops resurfacing |
| **REFUTED** | False when written, with the evidence |

Nothing stays open. A claim you could not verify is written `assumed`, visibly.

## 2. Decide before dividing (all modes)

Sweep the brief for decisions that are his: taste forks, sitemap, scope, spend, architecture, new
dependencies. Ask them in one round, recommendation first. Record the answers in the batch file under
Decided; lasting taste calls also go to `docs/crew/decided.md`. A fork that cannot be closed yet is
scoped out of the plan explicitly. A worker who meets an undecided fork mid-card either stalls or decides
something it does not own.

## 3. Evidence pass (standard, high-risk)

No plan before evidence. Read the code the change touches, trace the real flow end to end, grep the
callers of anything you will modify. Probe instead of quoting: re-check every claim about state (DB
rows, branches, files, checks passing) against the live system, and check every work branch when
"merged" or "landed" matters. A doc that disagrees with reality is a finding and a task, not an
embarrassment.

## 4. Definition of shipped (all modes)

Three to five checkable lines, written before any step: what he will click or run to know the work is
over. If you cannot write them, the brief is not understood yet. Stop and ask.

## 5. Decompose by dependency and risk

- Order by what blocks what and what is riskiest, never by category ("types, then components, then
  tests" is filing, not planning). The riskiest or least-known step goes first, as a spike.
- **Vertical slices.** A unit is a narrow, complete path someone can see or a check can prove: one page
  with its signature idea, or one feature through schema, API, UI and its test. Never a layer.
- **Partition by file ownership.** List the files each unit touches (grep, do not guess). Units whose
  files overlap are one unit. Parallel units share zero files, or one named file with disjoint hunks
  assigned to each. Every cross-dependency names a fallback. Balance units by risk, not size. A merge
  conflict between units with disjoint files means ownership broke: stop and say so.
- **Shared seam.** When two or more units depend on one contract (a type, schema, API or state shape),
  write it as a one-page spec in the batch file and give it to one unit, or build it yourself as the
  prefactor. Fixed interfaces are a precondition for carding code.
- **Wide refactors** (a rename or retype across the codebase): expand first, migrate in batches, then
  contract once every migration has landed.
- Light mode stops here: cards by file, each with Goal, Done when and what makes it differ from its
  siblings. Standard and high-risk give every step a contract:

```
FILES:  exact paths; anything unlisted needs a stated reason
CHANGE: the behaviour contract, what and why, not keystrokes
PROOF:  a runnable check or observable fact; never "looks right"
RISK:   what breaks if wrong, and a one-line rollback (omit for trivial steps)
```

Green after every step: build passes, tests pass, nothing half-wired.

## 6. Build contract (standard, high-risk)

```
VALUE:        one line: the user or app value this creates
SYSTEM:       where the logic lives and why there (one authority per domain decision)
REUSE:        existing helpers, patterns and infra this builds on, grep'd, not assumed
FILES:        the exhaustive list across all steps
NOT BUILDING: what is deliberately skipped, and when to add it
CHECK:        the one runnable check that fails if the core logic breaks
```

If VALUE does not fit one plain line, the design is not understood yet.

## 7. High-risk review (high-risk mode)

Load `references/high-risk-review.md` and run it inside a 20-minute box: REALITY lines on the plan's
premises, the four review sections (architecture with a second design, code quality, tests with a
coverage map, performance), and a decision ledger asked in one round.

## 8. Kill-test, then lock

State the strongest case that this plan is wrong: the assumption that, if false, breaks the sequence,
and the step most likely to surprise. If it lands, replan. If it does not, record it as the plan's
weakest point. Then lock the plan in one sentence. Deviations during the build are announced with a
reason, never silent.

A plan creates no new permission gate: if the work is authorised, continue into it or hand it off in
the same turn. The lead owns the plan; implementers may propose narrow, evidence-backed amendments.

## 9. Working memory and hand-off

For anything longer than about three steps, write the plan into the batch file
(`docs/crew/<date>-<slug>.md`) before building. Log locked decisions and failed approaches with the
reason as they happen; re-read the file on every resume. On the studio team agents may commit locally on
`crew/*` branches; anywhere else a commit needs his yes.

Work going to the Kanban board: Atlas's `crew-board` skill has the card call and body template. Work
for one session: build it.

## Consolidating a pile of findings

When several audits, reviews or repair plans on one system have produced little shipped work, first run
the consolidation in `references/consolidate-findings.md` (ground truth, document map, invariants,
dispositions), then plan from its task list.

## Routing

| Situation | Go to |
|---|---|
| The shape of the thing is still open | his question round, with `brutal-honesty` on the options |
| New systems or invariants with no owner | `logic-map` first |
| The system is not diagnosed yet | `diagnose` or `raze-review` first |
| Build done | `falsify`; for an integrated batch or a twice-failed area, `raze-review` mode A |

## Red flags

| Thought | Reality |
|---|---|
| "Types, then components, then tests" | Category order hides dependencies. Order by blockers and risk. |
| "We'll figure that step out later" | That is the spike. It goes first. |
| "The proof is that it looks correct" | PROOF is runnable or observable. |
| "The doc says it's still open" | Probe it. Docs are witnesses, the system is the evidence. |
| "Both cards touch globals.css, it's small" | Two owners means one lost edit. Prefactor it or serialise. |
| "This ask is awkward, leave it open" | Open limbo is banned. TASK, DONE, DEFERRED or REFUTED. |
| "Small deviation, no need to mention" | Silent drift is the most common implementation failure. |
| "More steps is more thorough" | Steps isolate risk and prove progress. Padding is theatre. |
