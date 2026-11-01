---
name: pixel-critique-loop
description: >-
  Force the model to actually LOOK at the running UI — render it, screenshot it at desktop (1440) AND mobile (390)
  width, and critique against the real pixels — before calling any frontend work done. This is the
  vision-self-correction loop: initiation, not ability, is the gap — models see images fine but rarely look
  unprompted, and even strong ones skip it on a rushed pass. This skill is the forcing function. Run it ON TOP OF a
  taste skill (frontend-design, brand-idiom, fidelity-critique) — they decide WHAT good looks like; this enforces the
  did-it-actually-look-right check they don't. Trigger when building, replicating, or polishing ANY UI, when
  implementing a screenshot or Figma reference, or when UI output still feels generic after a taste pass. In Claude
  Code, drive preview_start plus the browser tools (computer screenshot / resize_window / read_console_messages) to
  capture and self-critique; in Hermes, run `node ~/.hermes/tools/shots/shots.cjs <url> <out> <routes>` (1440 and 390).
  If the environment genuinely can't render and screenshot, this skill says so loudly rather than pretending a
  screenshot happened.
---

# Pixel-Critique Loop

Your taste layer (`frontend-design`, `impeccable`, `redesign-existing-projects`) decides *what good looks like*. It reasons about **code** and **described** UI. The one thing it never does is force you to render the running page, look at the actual pixels, and iterate against what you see. A scored critique of code is not the same as looking at the thing.

That gap is where frontend quality is actually made or lost, and initiation, not ability, is the gap: a model sees a screenshot perfectly well but does not look unless it is made to, so this skill is the forcing function that makes any model do it.

## The one rule

**Never let a render go un-looked-at.** Every build unit ends by viewing a screenshot of it running. If you are about to call UI "done" without having looked at a picture of it, stop — that is the exact failure this skill exists to prevent.

## Where this sits

This skill is the engine in the middle of your existing stack, not a replacement for any of it:

```
1. taste skill (frontend-design / impeccable)   → the design plan, tokens, anti-slop rules — WHAT good is
2. ── PIXEL-CRITIQUE LOOP ──                     → build a unit → render → screenshot → critique pixels → fix → re-look
3. taste skill's scored/static critique          → code-level anti-patterns the eye misses, on the converged unit
4. correctness pass                              → does the interactive behavior actually work, not just look right
```

Order matters: **pixels → static analysis → correctness.** Polishing a unit that still has a structural rendering problem polishes the wrong thing. Do not re-derive taste rules or re-pin project context here — read `PRODUCT.md` / `DESIGN.md` if present and build to them; that's the taste layer's job.

This is the UI specialization of `critic-pass` (the "run it" step is the render loop) and one of the forcing functions in the `frontier-gap` family — pair it with the project's `docs/crew/bans.md` or notes for the render log.

## Phase 0 — Confirm you can actually see (load-bearing)

The whole method dies silently if the environment can't render. State honestly what this setup can do before building:

- **Render + screenshot?** In **Claude Code**, the Browser-pane toolset is this harness: `preview_start` (dev server by name from `.claude/launch.json`, or a URL), `preview_logs` / `preview_stop`, then `computer` (action `screenshot`, plus `left_click` / `type` / `scroll`), `resize_window`, `read_page`, `read_console_messages`, `read_network_requests`, `javascript_tool`, `navigate`, `form_input`. That IS the render loop — never run a dev server via Bash. In **Hermes**, run `node ~/.hermes/tools/shots/shots.cjs <url> <out> <routes>`: it writes frames at 1440 and 390 plus sheets and a report (overflow, console errors, failed requests). Elsewhere: headless Chromium, a dev server + screenshot step, an artifact preview. Non-negotiable for the real loop.
- **File persistence?** For the attempt log (Phase 4). A real file is best.

If render-and-screenshot is genuinely unavailable, say so plainly — don't fake it:

> "This setup can't show the model its own output, which is the gap this skill closes. Start a dev server (`preview_start`), enable a browser preview, or add a screenshot step — otherwise this degrades to static critique only."

Then either stop, or proceed in **explicit degraded mode** (taste-skill static critique only, no pixel check). Never narrate a screenshot that didn't happen.

If vision is unavailable, label the visual limitation; capturing a screenshot is not seeing it; never fabricate a visual inspection.

## Phase 1 — Build one unit, small

Build the smallest complete, *renderable* unit first — one hero, one screen, one component — to the design plan. Not the whole page. You want to reach the loop early and cheap, because the loop is where quality is made, and a structural mistake caught in one component is a mistake you don't repeat across twelve.

## Phase 2 — The pixel-critique loop (the actual skill)

Minimum **two full passes** per unit you build (a new page or component); more while structural problems remain. Scope the loop to the change: a local visual edit need not trigger an app-wide screenshot tour — look at the affected view at 1440 and 390, fix, re-look.

**1. Render and capture — actually view both widths: 1440 (desktop) and 390 (mobile).**
In Claude Code:
- `preview_start` if no server is running; reload with `navigate` to the current URL, or `javascript_tool` (`window.location.reload()`), only if HMR isn't already live.
- `resize_window` `{width: 1440}` → `computer` `{action: "screenshot"}` at desktop width.
- `resize_window` `{width: 390}` → screenshot again for mobile.
- When an eyeball check is ambiguous (is that 16px or 24px?), `javascript_tool` with `getComputedStyle` for exact values; `read_console_messages` / `read_network_requests` / `preview_logs` to confirm nothing is silently broken behind a screenshot that *looks* fine.

In Hermes: `node ~/.hermes/tools/shots/shots.cjs <url> <out> <routes>` writes frames at 1440 and 390 for each route, sheets, and `report.json`. Read the report, look at the sheets first, and open a single frame only where something needs a closer look — every image viewed is re-sent with each later call.

**2. Critique against the pixels — not the code, not your description of it.** Use these questions verbatim (an explicit list does far better than "review this"):
- Did the rendered hierarchy match the type scale, or did it flatten in the browser?
- Is spacing on the intended rhythm, or did it drift to eyeball-default once rendered?
- Is the signature element carrying the page, or did it get visually buried?
- At mobile width (390): does it hold, or crowd / break / overflow?
- Does the rendered result look like THIS brief, or the generic version of the category?
- Floor, visually confirmed: keyboard focus visible, contrast real, reduced-motion respected.

**3. Name the top 1–3 concrete problems.** Specific and fixable, tied to what you see: *"accent appears in 5 places in the render, diluting it — restrict to primary action + active nav."* Not "could be tighter."

**4. Fix, re-render, re-look.** Confirm the fix landed *on screen* — re-screenshot, don't assume. New problems are fine; repeated ones go to the attempt log (Phase 4).

Stop a unit's loop when a render pass surfaces only nitpicks, not structure.

## Phase 3 — Static check, then correctness

Once a unit looks right in the loop:
1. Run the **taste skill's scored/static critique** (e.g. `impeccable critique`) on the converged unit for code-level anti-patterns the eye misses — a banned font, a card-in-card, a contrast fail the screenshot flattered. Low score → its named findings become new loop inputs, back to Phase 2.
2. Then a **correctness pass**: does the interactive behavior actually work, not just look right? `computer` (`left_click` / `type`) or `form_input` to exercise it, `read_console_messages` for errors, `read_page` to confirm state changed. Looking right and being right are different claims.

## Phase 4 — Attempt log (never repeat a mistake)

Persistent notes are replicable with a plain file — this is plan-forge's context strategy, and render findings are one of its inputs. Keep them under a `## Render notes` heading in the project's `docs/crew/bans.md` or its notes (don't spawn a second file):

```
## Render notes
- Recurring: this model defaults nav to centered-logo + 3 links. Specify nav explicitly up front.
- Recurring: mobile hero text overflows at 375px unless font-size is fluid-clamped.
- Tried & rejected: gradient hero bg → generic SaaS tell. Replaced with [x].
- Locked: accent only on primary action + active state. Don't relitigate.
```

Read it at the start of each unit and before each critique. This is what lets a weaker model with good notes beat a stronger model with amnesia on a long build. If files can't persist, keep this block live in context and re-paste it.

## Phase 5 — Hand off honestly

State plainly: render passes per unit, taste-skill score if any, what's solid, what you'd still push on, and what's a model limitation versus a design choice. The bar is "as close to frontier as this model gets," not parity — naming the shortfall is part of the job, not a failure of it.

## Model / harness notes

- **Claude Code:** the Browser pane IS the loop — `preview_start` → `resize_window` 1440 → `computer` screenshot (desktop) → `resize_window` 390 → screenshot again. The harness's own rule already applies: never ask the user to check manually — verify and share proof (a final screenshot for the user once converged).
- **Hermes:** `node ~/.hermes/tools/shots/shots.cjs <url> <out> <routes>` is the loop — frames and sheets at 1440 and 390, plus a report of overflow, console errors and failed requests. Look at the sheets first; share the most telling 1440 and 390 frames as proof.

## What this skill is NOT

- **Not a replacement for the taste skill.** It assumes one and slots beside it. If you're re-pinning context or re-deriving taste rules here, stop — that's their job.
- **Not a one-shot generator.** Producing UI without entering the loop defeats the entire purpose.
- **Not usable blind.** Phase 0's honesty is load-bearing; a loop with no render step is theater.
- **Not a parity claim.** "As close as possible" is the bar, and saying where it falls short is part of the work.
