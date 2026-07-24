---
name: frontier-gap
description: >-
  The operating system for closing the measurable gap between a frontier agentic model (Claude Fable 5)
  and whatever model is actually doing the work (Sonnet 5, Opus 4.8, Cursor Composer 2.5, GPT-5.5, a local
  model, or Claude on a rushed pass). The gap is not single-shot generation (SWE-bench Pro: Fable 80.3%,
  Opus 69.2%, Sonnet 63.2%) — it is long-horizon habits (FrontierCode Diamond: 29.3% vs 13.4%): a frontier
  model interprets the goal behind the ask, drops zero threads, plans from evidence, keeps notes, validates
  against reality, and doesn't stop early. Weaker models can do all of that; they just don't initiate it —
  one instruction to inspect rendered output moved self-inspection from 15% to 97% of runs (GDPval). This
  skill IS that initiation: it runs the full loop — interpret the request, open the ledger, set the
  per-model floor, plan by dependency and risk, build with a working-memory file, then route to critic-pass
  / pixel-critique-loop before done. Use at the START of any substantive turn or multi-step implementation
  on any model; also standalone to upgrade a prompt draft (Protocol 1) or to pick the right forcing
  function. Absorbs the former fable-standard, fable-plan, plan-lock, working-memory, and model-steering
  skills. Skip for trivial single-ask turns — over-process on small work is itself a failure.
---

# Frontier Gap

Frontier models are not mainly better at *generating* — on saturated evals Fable 5 is only modestly ahead.
The gap opens on **hard, long-horizon** work (FrontierCode Diamond: 2.2× Opus), and it comes from habits
Fable runs on its own: it interprets before acting, **validates against external evidence**, **keeps
notes**, and **doesn't stop early**. Weaker models have the raw ability for all of it. The gap is
**initiation** — measured, not vibes: one instruction to render-and-inspect moved self-inspection from
**15% to 97% of runs** (GDPval). This skill is the forcing function. Citations for every number:
[references/evidence.md](references/evidence.md) — read it before repeating any "frontier models do X"
claim.

## The loop

Every substantive task runs this sequence. Full protocol detail (the task-spec template, the per-step
contract, the benchmarks each pass must meet): [references/protocols.md](references/protocols.md) — read
it when actually executing a phase, not before.

1. **Interpret** (Protocol 1) — rewrite the request as a task spec: goal behind the ask, explicit +
   implicit constraints, done-means, ambiguity forks. A stranger could execute the spec; the user would
   recognize intent they didn't type.
2. **Open the ledger** (Protocol 2) — every ask in a multi-part message, including buried ones
   (parentheticals, "also…", trailing "and clean up X"), numbered. Nothing ends the turn undone,
   undeferred, or undeclined.
3. **Set the floor** — name the model in play and prepend the preamble that blocks *its* documented
   failure (silent drift for Composer 2.5, dropped constraints for GPT-5.5, plausible-not-verified for
   Sonnet 5, rushed pass for Opus): [references/model-profiles.md](references/model-profiles.md).
4. **Plan** (Protocol 3) — read the code first (no plan before evidence), decompose by dependency and
   risk (riskiest step first as a spike), four-line per-step contract (FILES / PROOF / RISK), green after
   every step. Lock it in one sentence; deviations announced out loud, never silent. Plan the context
   strategy: WORKING_MEMORY.md progress file, commit checkpoints, fresh-session handoffs. `lean-build`
   gates the approach (simplest thing that works) before the plan locks.
5. **Build** — with the working-memory file open: log locked decisions and failed-approaches-with-why the
   moment you learn them; re-read on every resume. For UI, Protocol 4: direction → tokens → ban-list →
   structure → render loop, never code-first.
6. **Verify** — route to the standalone verifiers before "done": `pixel-critique-loop` for anything
   rendered (screenshot desktop + mobile, critique the actual pixels), `critic-pass` for everything
   (external evidence, never introspection — bare self-review measurably *lowers* accuracy). Reviewing
   someone else's diff instead? Protocol 5: trace, hunt named failure classes, refute before reporting.
7. **Close the ledger** (Protocol 2) — walk it; only then end the turn.

Interpret, ledger, floor, plan, build, look, verify, close. That sequence is the system.

## The family — standalone skills this routes to

| Skill | Fires when | The habit it imposes |
|---|---|---|
| **`critic-pass`** | Before declaring ANY substantive output done | Validate against external evidence (run it / fresh verifier), hunt measured failure classes |
| **`pixel-critique-loop`** | Building or polishing any UI | Render, screenshot desktop+mobile, critique the pixels — never un-looked-at |
| **`lean-build`** | Start of any feature/refactor | Mission fit + simplicity ladder → short build contract; UI exempt from minimalism |

The former `fable-standard`, `fable-plan`, `plan-lock`, `working-memory`, and `model-steering` skills are
absorbed here (protocols.md and model-profiles.md); `render-loop` is retired — `pixel-critique-loop` is
the same job.

## Calibration

Name the stakes before choosing depth. A one-line edit gets none of this; an auth path gets all of it.
Each forcing function costs tokens and time, and *over*-process is a documented frontier-model failure at
high effort — verification proportional to the cost of an error. The non-negotiable that survives every
calibration: verification must touch **reality** — a run, a render, a diff, a fresh-context check.
Introspective "reflect harder" with no external signal makes weaker models *worse* (Huang et al.).

## Deploy outside Claude Code

The whole system ships as a portable `AGENTS.md` + `.cursor/rules` set for Codex, Cursor, and any
AGENTS.md reader: [references/deploy.md](references/deploy.md).

## Evolving this system

1. **Ground profiles in the user's own history first** — mem-search real incidents before citing
   benchmarks; session history steers harder than published numbers.
2. **Every new/updated skill gets a `~/.claude/skills/` symlink immediately** — an unlinked skill is
   invisible and gets recreated from scratch (render-loop: 8+ times).
3. **Append one line to `SCORECARD.md` (this directory) after every substantive session** — model, skills
   fired, catches, escapes. A skill that catches nothing in 10 sessions gets cut; a recurring escape
   becomes the next update.

## What this is NOT

- **Not a parity claim.** The bar is "as close to frontier as this model gets on this task"; naming the
  shortfall honestly is part of the job.
- **Not a taste layer.** It enforces *process*. What "good" looks like is the job of the design skills
  (`fidelity-critique`, `brand-idiom`, `design-ban-audit`, `frontend-design`).
- **Not free.** Calibrate to stakes (above).
