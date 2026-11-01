---
name: frontier-gap
description: "Use at the start of any substantive or multi-step task, on ANY model — frontier on a rushed pass, mid-tier, or small open-source — to force the full frontier work loop: interpret, track every ask, plan from evidence, keep notes, verify against reality, close everything. Use when a model ships the first plausible output, stops early, drops threads from multi-part requests, skips verification, or misses steps it was never told to run. Skip for trivial single-ask turns — over-process on small work is itself a failure."
---

# Frontier Gap

A general system for replicating a frontier model's work breakdown on any
model. The gap between a frontier run and a weak run is not raw generation —
it is long-horizon habits: interpreting the goal behind the ask, dropping
zero threads, planning from evidence, keeping notes, validating against
reality, not stopping early. Any capable model can do all of it; most don't
*initiate* it. One instruction to inspect rendered output moved
self-inspection from 15% to 97% of runs (GDPval) — the habits are cheap, the
initiation is the whole gap. This skill is the initiation. Numbers and
citations: [references/evidence.md](references/evidence.md).

**This skill orchestrates; it does not implement any phase itself.** Each
phase routes to the expert skill that owns it. One job: make sure the whole
loop runs and no step closes without evidence.

This is a recovery checklist, not an operating system to load before every task. For a clear short task, skip this skill and do the work.

## The loop — emit as todos, then walk it

At task start, write the loop as an explicit checklist (todo list, working
file, or printed list — whatever the harness has). A phase without named
evidence does not get ticked. This externalized checklist IS the
missed-steps mechanism: a model that must tick steps cannot silently skip
them.

| # | Phase | Routes to | Evidence that closes it |
|---|-------|-----------|-------------------------|
| 1 | **Interpret + ledger** | `plan-forge` Step 1 (or inline for small tasks) | task spec + numbered ledger of every ask, buried ones included |
| 2 | **Design** (if shape is open) | brainstorming (superpowers; Claude Code only, optional) + `brutal-honesty` | approved design; user's idea kill-tested, not flattered |
| 3 | **Logic** (if new systems/invariants) | `logic-map` | map with owned invariants + `budgets:` block |
| 4 | **Plan** | `plan-forge` | locked plan: build contract + per-step FILES/CHANGE/PROOF/RISK |
| 5 | **Build** | notes file (the batch file in `docs/crew/` or the project's notes); simplest thing that works, reuse before building; UI → design skills | green after every step; decisions + failed-approaches logged as learned |
| 6 | **Look** (anything rendered) | `pixel-critique-loop` | screenshots desktop + mobile, critiqued against the real pixels |
| 7 | **Verify** | `critic-pass` / `falsify`; strict review → `raze-review` mode A | external evidence: a run, a render, a diff, a fresh-context check — never introspection |
| 8 | **Close** | ledger from phase 1 | every item done, deferred-with-reason, or declined-out-loud |

Multi-session work: `goal-split` after phase 4. All reporting in the
`brutal-honesty` register.

## The floor — three rules that hold in every phase, every model

1. **Don't stop early.** Terminate only when the query is completely
   resolved — the ledger is the definition of resolved.
2. **Decide and document, don't stall.** On uncertainty, take the most
   reasonable assumption, proceed, record it. Bouncing decidable questions
   back is a dropped thread with extra steps.
3. **Ground every progress claim in evidence.** Before saying something
   works, point at the tool result that shows it (file:line, test output,
   render). Introspective self-review with no external signal measurably
   *lowers* accuracy — verification touches reality or it isn't verification.

## Calibration

Name the stakes before choosing depth. A one-line edit gets none of this; an
auth or data-loss path gets all of it. Every forcing function costs tokens,
and over-process on small work is a documented failure in its own right. The
non-negotiable that survives every calibration: verification must touch
reality.

## Evolving this system

1. Every new/updated skill is linked into each harness that reads
   `~/.agents/skills` (Claude Code and the Hermes profiles) immediately — an
   unlinked skill is invisible and gets recreated from scratch.
2. Note which skills fired, what they caught and what escaped anyway, in the
   batch file in `docs/crew/` or the project's notes. A skill that catches
   nothing in 10 sessions gets cut; a recurring escape becomes the next
   update.

## What this is NOT

- **Not a planning skill.** Planning is `plan-forge`; this only makes sure
  planning happens.
- **Not a parity claim.** The bar is "as close to frontier as this model
  gets on this task"; naming the shortfall honestly is part of the job
  (`brutal-honesty` register).
- **Not a taste layer.** What "good" looks like belongs to the design skills.
- **Not free.** Calibrate to stakes.
