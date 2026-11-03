---
name: plan-forge
description: >-
  Use when a batch, feature, refactor or repair wave touches more than one file and needs a plan before
  building, usually right after ship-spec defined what ships; or when the owner hands over a brief or an
  approved design. Four modes: quick (2-3 files, one obvious design), light (design batches), standard
  (multi-file code), high-risk (checkout, payments, auth, personal data, a database, 8+ code files).
---

# Plan Forge

Step two of two. `ship-spec` says what ships and when it is done; plan-forge says how, and in what order.
It turns the spec into a locked plan ordered by dependency and risk. Standing rules: evidence only,
done-checks runnable, every ask lands in a bucket, deviations said out loud.

Skip it for a single-file change. A plan for a one-liner is theatre.

## Pick the mode

| Mode | When | Output |
|---|---|---|
| **Quick** | Code touching 2 or 3 files with one obvious design and no data, auth or payments | Three lines in the reply: the change, the files, one PROOF. No batch file, no build contract |
| **Light** | Design, page, copy and polish batches: anything his eye judges on a preview | The batch file: his words, Decided, Defaults, Definition of shipped, cards split by file |
| **Standard** | A multi-file code change | Light, plus the evidence pass, steps with FILES / CHANGE / PROOF / RISK, and the build contract |
| **High-risk** | Checkout, payments, auth, personal data, a database, 8+ code files or 2+ new services | Standard, plus the high-risk review in `references/high-risk-review.md` |

Page, copy and polish batches stay Light however many files they touch; a form that only posts to an
existing endpoint does not make a batch high-risk.

## 1. Start from the ship spec (light, standard, high-risk)

The batch file's **Ship spec** section (`ship-spec`) is the contract: his words numbered, the mission,
the Definition of shipped and the ask ledger (TASK, DONE, DEFERRED, REFUTED). Read it and plan only the
TASK rows; do not redo it. With no spec yet, run `ship-spec` first for standard and high-risk work; for a
light batch write the Ship spec section inline by its rules. The skeleton for the whole batch file is
`ship-spec`'s `references/batch-file.md`. A gated task is not carded until he has answered.

## 2. Decide before dividing (all modes)

The ship spec asked his calls. Sweep for the ones it could not see (forks the evidence pass or the
decomposition surfaces: taste, sitemap, scope, spend, architecture, new dependencies) and ask them in one
round, recommendation first. Record the answers in the batch file under
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

It comes from the ship spec. Every step's PROOF must serve one of its lines; a line no step serves is a
gap in the plan. In quick mode, the one PROOF line is the definition.

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
PROOF:  a runnable check or observable fact; for logic, the test and the seam it runs at; never "looks right"
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
weakest point. Then lock the plan in one sentence, and write the weakest point into the batch file's Plan section (quick
mode: one line in the reply).
Deviations during the build are announced with a
reason, never silent.

A plan creates no new permission gate: if the work is authorised, continue into it or hand it off in
the same turn. The one exception he chose: the map gate in `logic-map` (a new app, site, process or big
feature waits for his OK on the map). The lead owns the plan; implementers may propose narrow, evidence-backed amendments.

## 9. Working memory and hand-off

For anything longer than about three steps, write the plan into the batch file
(`docs/crew/<date>-<slug>.md`) before building. Log locked decisions and failed approaches with the
reason as they happen; re-read the file on every resume. On the studio team agents may commit locally on
`crew/*` branches; anywhere else a commit needs his yes.

Where it goes next:
- **One session** (Claude Code, or an agent working solo): build it.
- **Hermes board:** Atlas's `crew-board` skill has the card call and body template.
- **Parallel Claude Code sessions:** one goal file per session, readable with zero context: the owned
  files, the done-check, and his standing rules verbatim (database read-only, migrations written but never
  run, no spend, commits need his yes). The planning session holds the merge.

## Consolidating a pile of findings

Findings piled up on one system with little shipped: that is `ship-spec`'s consolidation. Plan from the
task list it produces.

## Routing

| Situation | Go to |
|---|---|
| Substantial work with no ship spec yet | `ship-spec` first |
| The shape of the thing is still open | his question round, with `brutal-honesty` on the options |
| New app, process or big feature; rules with no owner | `logic-map` after the ship spec, before this plan (scenarios and the map; his OK before building) |
| The system is not diagnosed yet | `diagnose` or `raze-review` first |
| Build done | `falsify`; a twice-failed area: `raze-review` mode A; an integrated batch: an independent batch review (on the studio team, engineering-god's, requested at batch end) |

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
