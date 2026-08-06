---
name: plan-forge
description: "Use when a feature, refactor, repair wave, or multi-file change needs a plan before implementation — at the start of any substantive session-level work, when the user says \"plan this\", \"make a plan\", \"how should we build this\", or hands over an approved design/spec to execute. Session-level plans only: project-level roadmaps belong to /phase-plan + planning-standard.md. Skip for single-file trivial changes — a plan for a one-liner is process theater."
---

# Plan Forge

The one session-level planning skill. Consumes an approved design (from
brainstorming) and a logic map (if the work has new systems or invariants);
produces a locked, dependency-and-risk-ordered plan ending in a build
contract. Project-level phasing lives in `c3po_vault/context/planning-standard.md`
(/phase-plan) — this skill plans ONE feature/change inside a session, and
inherits that standard's rules (evidence only, done-checks runnable, deviation
out loud) without restating them.

**Absorbs the former lean-build (build contract) and frontier-gap Protocols
1–3 (interpret, ledger, plan). Replaces both for planning.**

## Preconditions — check before planning

- Design approved? If the shape of the thing is still open, that's
  brainstorming (+ brutal-honesty), not planning.
- New systems or invariants involved? Run `logic-map` first — sequencing a
  design whose invariants have no owner schedules the rework. The map also
  supplies the `budgets:` block the plan (and later raze-review) answers to.
- A diagnosed backlog going to multiple sessions? That's `goal-split`, run
  AFTER this skill locks what's being built.

## Step 1 — Interpret

Rewrite the request as a task spec a stranger could execute: the goal behind
the ask, explicit + implicit constraints, done-means, ambiguity forks
(resolved with the most reasonable assumption, recorded). Open the ledger:
every ask in the message — including parentheticals, "also…" clauses,
trailing "and clean up X" — numbered. Nothing ends the session undone,
undeferred, or undeclined.

## Step 2 — Evidence pass

No plan before evidence. Read the code the change touches, trace the real
flow end to end, grep the callers of anything being modified. A plan written
from memory of the codebase is a guess with formatting.

## Step 3 — Decompose by dependency and risk

- Order by DEPENDENCY and RISK, never by category ("types, then components,
  then tests" is a filing system, not a plan).
- The riskiest / least-known step goes FIRST as a spike — fail early while
  the sunk cost is one step, not seven.
- Every step carries a four-line contract:
  ```
  FILES: exact paths — anything not listed needs a stated reason
  CHANGE: behavior contract, what and why — not keystrokes
  PROOF:  runnable check or observable fact; never "looks right"
  RISK:   what breaks if wrong + one-line rollback (omit for trivial steps)
  ```
- Green after every step: build passes, tests pass, nothing half-wired.

## Step 4 — Build contract (the plan's output header)

```
VALUE: [one line — what user/app value this creates]
SYSTEM: [where the logic lives and why there — single authority for the domain decision]
REUSE: [existing helpers/patterns/infra this builds on — grep'd, not assumed]
FILES: [exhaustive list across all steps]
NOT BUILDING: [abstractions/features deliberately skipped + when to add them]
CHECK: [the one runnable check that fails if the core logic breaks]
```

If VALUE can't be said in one plain line, stop — the design isn't understood
yet. The ponytail ladder governs SYSTEM and REUSE (simplest thing that
works); it is ambient in every session and not restated here.

## Step 5 — Kill-test, then lock

Before locking, brutal-honesty rule 5 applies to the plan itself: state the
strongest case that this plan is WRONG — the assumption that, if false,
invalidates the sequence; the step most likely to surprise. If the kill-test
lands, replan; if it doesn't, record it as the plan's known-weakest point.

Then lock in one sentence. Deviations during build are announced out loud
with a reason, never silent. The plan is the authority until a deviation is
declared.

## Step 6 — Working memory

For any plan longer than ~3 steps or expected to span context windows:
open `WORKING_MEMORY.md` (or the project's equivalent) before building. Log
locked decisions and failed-approaches-with-why the moment they happen;
re-read on every resume. Commit checkpoints at green steps.

## Routing

| Situation | Skill |
|---|---|
| Shape of the thing still open | brainstorming + `brutal-honesty` |
| New systems/invariants, no map | `logic-map` first |
| Project-level roadmap | `/phase-plan` per planning-standard.md |
| Plan spans multiple agent sessions | `goal-split` after lock |
| Plan done, building UI | `pixel-critique-loop` before done |
| Build done | `critic-pass` / `raze-review` mode A |

## Red flags — the plan is about to fail

| Thought | Reality |
|---|---|
| "Plan: types, then components, then tests" | Category order hides dependencies. Order by what blocks what and what's riskiest. |
| "We'll figure that step out when we get there" | That's the spike. It goes first, or the plan is seven steps of sunk cost before the surprise. |
| "The proof is that the code looks correct" | PROOF is runnable or observable. "Looks right" is not a check. |
| "Small deviation, no need to mention" | Silent drift is the #1 documented implementation failure. Out loud, with reason, every time. |
| "The plan can skip reading X, I remember it" | Memory of code is a guess. Evidence pass first. |
| "More steps = more thorough" | Steps exist to isolate risk and prove progress. Padding a plan is planning theater. |
