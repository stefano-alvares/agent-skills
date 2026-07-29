---
name: pixel-critique-loop
description: >-
  Force the model to actually LOOK at the running UI — render it, screenshot it at desktop AND mobile width,
  and critique against the real pixels — before calling any frontend work done. This is the vision-self-correction
  loop frontier models (Fable 5) run on their own with almost no scaffolding; weaker and cheaper models (Composer 2.5,
  GPT-5.5, local) can do it too but rarely initiate it, and even strong models skip it on a rushed pass. The gap is
  not vision ability — it's initiation. One instruction to inspect rendered output moved self-inspection from 15% to
  97% of runs in OpenAI's GDPval study and erased a class of artifacts affecting half of outputs. This skill is that
  forcing function. Run it ON TOP OF a taste skill (frontend-design, brand-idiom, fidelity-critique) — they
  decide WHAT good looks like; this enforces the did-it-actually-look-right check they don't. Trigger when building,
  replicating, or polishing ANY UI, when implementing a screenshot or Figma reference, or when UI output still feels
  generic after a taste pass. In Claude Code, drive preview_start plus the browser tools (computer
  screenshot / resize_window / read_console_messages) to capture and self-critique. If the environment genuinely can't render and
  screenshot, this skill says so loudly rather than pretending a screenshot happened.
---

# Pixel-Critique Loop

Your taste layer (`frontend-design`, `impeccable`, `redesign-existing-projects`) decides *what good looks like*. It reasons about **code** and **described** UI. The one thing it never does is force you to render the running page, look at the actual pixels, and iterate against what you see. A scored critique of code is not the same as looking at the thing.

That gap is where frontend quality is actually made or lost. Frontier frontend models feel better at UI largely because they self-review against their own rendered output and keep notes across a long session — independent testing found their raw single-shot generation only marginally better than the prior generation; the gains were this loop. Weaker models see images perfectly well — they just don't *initiate* the look on their own. The cleanest proof is OpenAI's GDPval study: one instruction to render deliverables to images and inspect them moved self-inspection from **15% to 97% of runs** and eliminated a rendering-artifact class that had affected over half of generated PDFs. Same model, same vision ability — the gap was initiation. (That result was measured on generated *documents*, PDF/PPTX; the principle — render your output and look at it — transfers directly to UI. Full citation in the `frontier-gap` skill's `references/evidence.md`.) This skill is the forcing function that makes any model do it.

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

This is the UI specialization of `critic-pass` (the "run it" step is the render loop) and one of the forcing functions in the `frontier-gap` family — pair it with frontier-gap's WORKING_MEMORY.md file for the render log.

## Phase 0 — Confirm you can actually see (load-bearing)

The whole method dies silently if the environment can't render. State honestly what this setup can do before building:

- **Render + screenshot?** In **Claude Code**, the Browser-pane toolset is this harness: `preview_start` (dev server by name from `.claude/launch.json`, or a URL), `preview_logs` / `preview_stop`, then `computer` (action `screenshot`, plus `left_click` / `type` / `scroll`), `resize_window`, `read_page`, `read_console_messages`, `read_network_requests`, `javascript_tool`, `navigate`, `form_input`. That IS the render loop — never run a dev server via Bash. Elsewhere: headless Chromium, a dev server + screenshot step, an artifact preview. Non-negotiable for the real loop.
- **File persistence?** For the attempt log (Phase 4). A real file is best.

If render-and-screenshot is genuinely unavailable, say so plainly — don't fake it:

> "This setup can't show the model its own output, which is the gap this skill closes. Start a dev server (`preview_start`), enable a browser preview, or add a screenshot step — otherwise this degrades to static critique only."

Then either stop, or proceed in **explicit degraded mode** (taste-skill static critique only, no pixel check). Never narrate a screenshot that didn't happen.

## Phase 1 — Build one unit, small

Build the smallest complete, *renderable* unit first — one hero, one screen, one component — to the design plan. Not the whole page. You want to reach the loop early and cheap, because the loop is where quality is made, and a structural mistake caught in one component is a mistake you don't repeat across twelve.

## Phase 2 — The pixel-critique loop (the actual skill)

Minimum **two full passes** per unit; more while structural problems remain.

**1. Render and capture — actually view both images.**
In Claude Code:
- `preview_start` if no server is running; reload with `navigate` to the current URL, or `javascript_tool` (`window.location.reload()`), only if HMR isn't already live.
- `computer` `{action: "screenshot"}` at desktop width.
- `resize_window` `{preset: "mobile"}` (375×812) or `{width: 390}` → screenshot again for mobile.
- When an eyeball check is ambiguous (is that 16px or 24px?), `javascript_tool` with `getComputedStyle` for exact values; `read_console_messages` / `read_network_requests` / `preview_logs` to confirm nothing is silently broken behind a screenshot that *looks* fine.

**2. Critique against the pixels — not the code, not your description of it.** Use these questions verbatim (rubric-following models like GPT-5.5/Codex do far better with the explicit list than with "review this"):
- Did the rendered hierarchy match the type scale, or did it flatten in the browser?
- Is spacing on the intended rhythm, or did it drift to eyeball-default once rendered?
- Is the signature element carrying the page, or did it get visually buried?
- At mobile width: does it hold, or crowd / break / overflow?
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

A frontier model's persistent-notes advantage is replicable with a plain file — this is frontier-gap's context strategy (protocols.md, Protocol 3 Phase 3), and render findings are one of its inputs. Keep them under a `## Render notes` heading in `WORKING_MEMORY.md` (project root, alongside `PRODUCT.md` — don't spawn a second file):

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

- **Claude Code (here):** the Browser pane IS the loop — `preview_start` → `computer` screenshot (desktop) → `resize_window` mobile → screenshot again. The harness's own rule already applies: never ask the user to check manually — verify and share proof (a final screenshot for the user once converged).
- **Composer 2.5 (Cursor):** enable browser preview so the capture step is native. Its effort-calibration under-spends on "small" tweaks — push it into the loop explicitly or it calls things done after one render.
- **GPT-5.5 / Codex:** follows an explicit rubric well — feed Phase 2's questions verbatim rather than "review this."
- **Gemini CLI / AI Studio:** native multimodal makes reference-screenshot → tokens sharp; AI Studio Build preview is a clean render target.
- **Local models (Gemma / GLM):** Phase 4 carries the most weight — they drift fastest, so the attempt log does the heaviest lifting.

## What this skill is NOT

- **Not a replacement for the taste skill.** It assumes one and slots beside it. If you're re-pinning context or re-deriving taste rules here, stop — that's their job.
- **Not a one-shot generator.** Producing UI without entering the loop defeats the entire purpose.
- **Not usable blind.** Phase 0's honesty is load-bearing; a loop with no render step is theater.
- **Not a parity claim.** "As close as possible" is the bar, and saying where it falls short is part of the work.
