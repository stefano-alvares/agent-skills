---
name: frontier-gap
description: >-
  The entry point and routing layer for closing the measurable gap between a frontier agentic model
  (Claude Fable 5) and whatever model is actually doing the work (Cursor Composer 2.5, GPT-5.5, a local
  model, or Claude/Opus on a rushed pass). Fable 5's documented edge is not single-shot generation — on
  saturated benchmarks it is only modestly ahead — it is sustaining correctness over long autonomous runs:
  it reflects on and validates its own work (at high effort), keeps notes across millions of tokens, and
  doesn't stop early. Weaker models can do every one of those things; they just don't initiate them. This
  family imposes those habits externally as forcing-function skills, each grounded in a specific published
  result (GDPval 15%→97% self-inspection, Reflexion, edit-localization studies, Anthropic's own production
  guidance). Use this skill when the user wants output "as good as Fable can get on this model," when
  starting substantial agentic work on a non-frontier or lower-effort model, or when asking which of the
  forcing-function skills (pixel-critique-loop, critic-pass, working-memory, model-steering, plan-lock) to
  reach for. It routes to the right one and houses the evidence base so the others stay lean. It also ships
  the whole system as a deployable AGENTS.md + .cursor/rules set (in assets/) so the same operating system
  runs natively in Codex and Cursor, which it is specifically tuned for.
---

# Frontier Gap

Frontier agentic models are not mainly better at *generating* — on saturated evals Fable 5 is only modestly
ahead of Opus 4.8 and GPT-5.5. The gap opens on **hard, long-horizon** work (FrontierCode Diamond: Fable
2.2× Opus), and it comes from three habits Fable runs more or less on its own: it **validates its own work
against external evidence** at high effort, it **keeps notes** across long runs, and it **doesn't stop
early**. Weaker models — Composer 2.5, GPT-5.5, local models, or Claude itself on a low-effort pass — have
the raw ability to do all three. The gap is **initiation**: they won't unless made to.

That's the one finding to internalize, and it's measured, not vibes: in OpenAI's GDPval study a single
instruction to render-and-inspect output moved self-inspection from **15% to 97% of runs**. Same model,
same vision ability — one forcing function. This family is a set of those forcing functions, each pinned to
a published result. Full citations live in [references/evidence.md](references/evidence.md); read it before
repeating any "frontier models do X" claim, because some of the popular framing is positioning and that note
separates proven from marketing.

## The family — and when each fires

| Reach for… | When | The frontier habit it imposes | Core evidence |
|---|---|---|---|
| **`pixel-critique-loop`** | Building, replicating, or polishing any UI | Render it, screenshot desktop+mobile, critique the actual pixels before "done" | GDPval 15%→97% |
| **`critic-pass`** | Before declaring ANY substantive output done | Hunt for what's wrong against *external evidence* (run it / fresh-context verifier), not introspection | Reflexion; Huang (bare self-review hurts); edit-localization |
| **`working-memory`** | Long or multi-session tasks; anything where mistakes recur | Keep a notes file: status, locked decisions, and failed-approaches-and-why, re-read on resume | Anthropic memory guidance; long-running-Claude |
| **`model-steering`** | Any model doing substantial work — including Sonnet 5 and Opus 4.8 (profiles added 2026-07-06 from Stefano's own incident history) | A per-model preamble that forbids that model's specific failure, and sets the effort bar | OpenAI/Anthropic persistence guidance + own session incidents |
| **`plan-lock`** | Starting a multi-step feature/refactor, esp. on Composer 2.5 / GPT-5.5 | Write the plan + constraints, restate it, flag any deviation out loud — never drift silently | Composer 2.5 silent-drift reports; GPT-5.5 constraint-dropping |
| **`lean-build`** | Start of any feature/refactor/multi-file change | Pre-implementation gate: mission fit + simplicity ladder → a short build contract; UI work exempt from minimalism | Merged from ponytail + mission-systems-cleanup, 2026-07-06 |
| **`fable-standard`** | Start of any substantive turn on Sonnet 5 / Opus 4.8; also to upgrade a prompt draft | Interpret the goal behind the ask, keep a nothing-skipped ledger, plan UI direction-first, review by refuting own findings — each with an explicit "benchmark" line | Fable 5 introspection, 2026-07-06; SWE-bench Pro 80.3 vs 69.2 vs 63.2, FrontierCode Diamond 29.3 vs 13.4 |
| **`fable-plan`** | Before code on any multi-step implementation | Evidence-first, dependency+risk-ordered plan; every step green with its own proof; explicit context strategy (progress file, checkpoints, fresh-session handoffs); review scheduled in the plan | Confucius harness > vendor harness (52.7/54.3 SWE-Bench-Pro, arXiv 2512.10398); Anthropic long-horizon guidance |

They compose into one loop. A real long build runs all of them: `fable-standard` interprets the request and
opens the ledger → `model-steering` sets the floor → `lean-build` writes the build contract → `plan-lock`
locks it → build with `working-memory` open → `pixel-critique-loop` per UI unit → `critic-pass` before done
→ `fable-standard` ledger walk before ending the turn. Interpret, floor, contract, plan, remember, build,
look, verify, close the ledger — that sequence is the system. (`render-loop` is deprecated — same job as
`pixel-critique-loop`.)

## Evolving this family

Two rules, learned 2026-07-06:
1. **Ground profiles in the user's own history first.** Before writing or updating a failure profile, run
   claude-mem `mem-search` for real incidents (bugfixes, review rejections, retrofitted fixes) — a profile
   citing "training-app Task 7, June 2026" steers harder than a published benchmark. Published research is
   the floor; session history is the target.
2. **Every new/updated skill gets a `~/.claude/skills/` symlink immediately** — an unlinked skill is
   invisible to Claude Code, and unfindable skills get recreated from scratch (render-loop: 8+ times).
3. **Append one line to `SCORECARD.md` (this directory) at the end of every substantive session** —
   model, skills fired, catches, escapes. The iteration rule needs data, not vibes; a skill that never
   catches anything in 10 sessions gets cut, a recurring escape becomes the next skill update.
3. **Append one line to `SCORECARD.md` (this directory) at the end of every substantive session** —
   model, skills fired, catches, escapes. The iteration rule needs data, not vibes; a skill that never
   catches anything in 10 sessions gets cut, a recurring escape becomes the next skill update.

## How to use this skill

1. **Name the model and the stakes.** Which model is doing the work, and what does a wrong answer cost? That
   sets effort (see `model-steering`) and how thorough the critic pass must be.
2. **Route to the forcing functions the task needs** (table above). Don't run all four on a one-line edit —
   the family also warns against over-engineering, which is itself a documented frontier-model failure at
   high effort.
3. **The non-negotiable across all of them:** verification must touch *reality* — a run, a render, a
   diff, a fresh-context check. The single most important research finding here is that introspective
   "reflect harder" self-review without external evidence makes weaker models *worse*, not better
   (Huang et al.). Every skill in this family is built around that constraint.

## Deploy as a system to Codex / Cursor / any harness

In Claude Code these load as skills automatically. Other harnesses don't read `~/.claude/skills/`, so the
whole system is also shipped as portable, self-contained instruction files in this skill's `assets/` — the
five forcing functions compressed into one sequenced operating system, tuned for the exact models that run
there (Composer 2.5, GPT-5.5/Codex).

- **`assets/AGENTS.md`** — the canonical orchestrator. One file, the open `AGENTS.md` standard, read natively
  by **Codex** (repo root) and **Cursor** (and Copilot, Windsurf, Aider, …). It inlines the floor, the loop,
  the critic-pass checklist, the render-and-look step, and per-model preambles — so it works with no skill
  files present.
- **`assets/cursor-rules/*.mdc`** — Cursor's conditional layer: an always-on orchestrator
  (`00-operating-system.mdc`) plus a glob-scoped UI rule (`40-render-and-look.mdc`) that only attaches on
  frontend files, so it doesn't bloat backend sessions.

Install (per repo):
```bash
SK=~/.agents/skills/frontier-gap/assets
cp "$SK/AGENTS.md" ./AGENTS.md                 # Codex + Cursor + any AGENTS.md reader
mkdir -p ./.cursor/rules && cp "$SK"/cursor-rules/*.mdc ./.cursor/rules/   # Cursor conditional layer
ln -sf AGENTS.md CLAUDE.md                      # optional: same system for Claude Code in this repo
```
For a personal cross-repo default in Codex, also copy `AGENTS.md` to `~/.codex/AGENTS.md` (lowest precedence;
repo files layer on top). Keep the root file well under Codex's 32 KiB cap — it already is. Notes:
`.cursorrules` is deprecated (don't use it); Cursor User Rules live in the settings UI, not a committable
file, so the portable system goes in `.cursor/rules/` + `AGENTS.md`.

## What this family is NOT

- **Not a parity claim.** The bar is "as close to frontier as this model gets on this task," and naming the
  shortfall honestly is part of the job — Fable's edge on the hardest long-horizon work is real and not fully
  closable by scaffolding alone.
- **Not a taste layer.** It enforces *process* (look, verify, remember, persist). What "good" looks like is
  the job of `frontend-design` / `impeccable` / `redesign-existing-projects`.
- **Not free.** Each forcing function spends tokens and time. Calibrate to stakes; the research is explicit
  that verification should be proportional to the cost of an error.
