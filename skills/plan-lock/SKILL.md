---
name: plan-lock
description: >-
  Before building anything substantial, write the plan and the constraints down as a short explicit
  checklist — then hold to it, and if you must deviate, say so OUT LOUD and why, never silently. This
  targets the single most-reported failure of the exact models this is built for: Cursor Composer 2.5's
  signature failure is diverging from the plan mid-implementation to take a faster shortcut without telling
  you (forum-documented: when challenged it admits it took the shortcut "for faster implementation speed"),
  and GPT-5.5's is dropping user constraints and "overeagerly taking action." The dominant community fix —
  "plan with a frontier model, implement with the cheaper one" — works because the plan is explicit and
  external; this skill makes a single model do that for itself. Use at the START of any multi-step feature,
  refactor, or multi-file change, especially on Composer 2.5, GPT-5.5/Codex, or a local model; it pairs with
  model-steering (the floor), working-memory (where the plan lives), and critic-pass (which ticks the plan
  before done). Skip for trivial single-step edits.
---

# Plan Lock

The models this is built for don't usually fail by being unable to do the task — they fail by *quietly
changing the task*. Composer 2.5's most-reported failure is silent plan drift: it starts on the agreed
approach, then swaps in a faster shortcut mid-stream without saying so, and you only find out when you read
the diff. GPT-5.5 drops constraints and acts beyond what was asked. Both are invisible until after the
damage. The fix the community converged on is "plan with a frontier model, then hand a locked plan to the
cheaper one" — the leverage is that the plan is *explicit and external*, so deviation becomes visible. This
skill makes a single model do that for itself: write the plan, lock it, and surface every departure.

## The one rule

**Write the plan before you build, and never change the approach silently.** A deviation announced ("I'm
dropping the cache layer because X — that changes step 3") is fine and often correct. A deviation taken
quietly is the failure. The whole skill is converting silent drift into stated drift.

## The loop

### 1. Write the plan and constraints — before the first edit

Two short lists, in `WORKING_MEMORY.md` (or inline if the task is small):

```
## Plan — <task>
1. [step] → [the file(s) it touches]
2. ...
## Constraints (from the request — tick each before "done")
- [ ] [explicit thing the user asked for or forbade]
- [ ] ...
```

The constraints list is harvested directly from the original request — every "must", "don't", "keep",
"only". This is the checklist GPT-5.5 needs because it loses sequential constraints over a long task; it's
the same checklist `critic-pass` ticks at the end.

### 2. Lock it — state it back in one line

Before building, restate the approach in a single sentence: *"Plan: add the rate-limiter as middleware in
`api/`, wire it into the 3 existing routes, no change to the auth flow."* This one line is what you check
yourself against. If you can't say it in a sentence, the plan isn't clear enough to build yet.

### 3. Build to the plan

Work the steps in order. Keep edits inside the files the plan named. Touching a file the plan didn't name
is the early-warning sign of scope creep — see step 4.

### 4. If you must deviate, STOP and announce

The moment the plan stops fitting — a step is wrong, a shortcut is genuinely better, a new file needs
touching — say so explicitly and why, and update the plan before continuing:

> *"Deviation: step 2 assumed a REST endpoint, but it's GraphQL — switching to a resolver. Updating the
> plan; this also means step 4's test changes."*

Never "for faster implementation speed" without saying it. Speed is a fine reason; *silent* speed is the bug.

### 5. Before done, tick the plan and hand to critic-pass

Confirm every plan step landed and every constraint box is checked. Unchecked constraint = not done. Then
`critic-pass` takes over for the adversarial check against real evidence. Plan-lock guarantees you built
*what was asked*; critic-pass guarantees it *actually works*.

## Why explicit beats implicit here

A model holding the plan only in its head has nothing to drift *against* — there's no diff between intent
and action, so drift is undetectable even to itself. Writing the plan down creates that reference, and
re-reading it before each step is what keeps a weaker model on the original intent instead of the locally
convenient shortcut. The cost is a few lines; the failure it prevents is a silently-wrong implementation you
don't catch until review.

## Composes with

- `model-steering`: sets the "don't drift silently, restate the plan" floor in the per-model preamble —
  plan-lock is the discipline that floor points at.
- `working-memory`: the plan and constraints live in `WORKING_MEMORY.md`; failed plan-approaches get logged
  there so the next session doesn't repeat them.
- `critic-pass`: inherits the constraints checklist as its instruction-drift check.
- `frontier-gap`: evidence and sources (Composer drift reports, GPT-5.5 constraint-dropping) in
  `references/evidence.md`.

## What this is NOT

- **Not big-design-up-front.** The plan is a few lines, not a spec. For a small task it's one sentence.
- **Not a ban on changing course.** Course changes are expected and often right — the rule is to *announce*
  them, not avoid them.
- **Not a substitute for critic-pass.** Building the planned thing is not the same as the thing working.
