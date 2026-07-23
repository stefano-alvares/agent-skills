---
name: render-loop
description: Use when building, reviewing, or polishing frontend UI and the agent must verify the rendered result instead of trusting code alone. Trigger for premium UI work, screenshot-driven implementation, interaction tuning, responsive QA, or when using impeccable and make-interfaces-feel-better on Astro or similar frontend stacks and you need a real desktop-plus-mobile render loop before calling the work done.
---

# Render Loop

> **DEPRECATED (2026-07-06)** — superseded by `pixel-critique-loop`, which covers the same
> render/screenshot/critique loop with the evidence base attached. This skill was recreated 8+ times across
> sessions because it was never symlinked into `~/.claude/skills/` and each session couldn't find it. Kept
> for its stack-specific sequencing note below (impeccable → make-interfaces-feel-better → render loop);
> do not extend this file — extend `pixel-critique-loop` instead.

`render-loop` is the practical wrapper for the stack used here:

1. `impeccable` sets context and runs the scored critique.
2. `make-interfaces-feel-better` sharpens tactile details and motion.
3. `render-loop` forces the missing part: render, screenshot, look, fix, re-look.

Do not use this instead of a taste skill. Use it after context is pinned and while implementation is in flight.

## Output contract

Never close a UI task without reporting:

- which routes or components were rendered
- which viewports were checked
- how many render passes each unit received
- the top concrete issues found in pixels
- what changed after the fixes
- what proof commands ran
- what visual risk remains if render tooling was blocked

## Phase 0: Confirm the harness

Before editing, establish whether this environment can actually render and capture screenshots.

Required:

- a running dev or preview server
- a screenshot path
- a place for render notes

If render plus screenshot is unavailable, say so plainly and switch to degraded mode:

> Render loop blocked: this environment cannot show the running UI back to the model, so visual review is limited to static code critique only.

Do not imply that screenshots were checked if they were not.

## Phase 1: Load taste and constraints first

For this stack, use this order:

1. Read `PRODUCT.md` and `DESIGN.md`, or use `impeccable` if already active.
2. If the task is substantial, lock the design intent first with the existing spec or plan.
3. Read `references/astro-premium-storefront.md` when the repo matches the Astro storefront shape described there.

Do not re-invent the aesthetic in this skill. It exists to verify rendered truth, not define taste.

## Phase 2: Build one unit at a time

Work in small renderable units:

- one hero
- one nav state
- one product card system
- one drawer
- one PDP section

Do not rebuild the whole site before first render. The point is to catch structural mistakes early.

## Phase 3: Run the render loop

Each unit gets at least two full passes.

### Pass structure

1. Render desktop.
2. Render mobile.
3. Critique the screenshots, not the code.
4. Name the top one to three issues.
5. Fix them.
6. Re-render both widths.
7. Confirm the fix landed on screen.

### Critique rubric

Use these questions directly:

- Did the hierarchy survive the browser, or flatten?
- Did the spacing rhythm hold, or drift into default evenness?
- Is the signature moment actually carrying the page?
- Does mobile still feel composed, or does it crowd and leak?
- Do interactions feel premium, deliberate, and calm?
- Are focus, contrast, hit areas, and reduced motion visibly correct?
- Does this look like this brand, or the generic version of this category?

Do not report vague notes like "could be tighter." Name concrete visual failures.

## Phase 4: Use the right polish layer

When the issue is about feel rather than structure, route through `make-interfaces-feel-better`.

Typical triggers:

- hit area too small
- transitions too broad
- padding animation on sticky UI
- outlines dirtying imagery
- press scale missing or too aggressive
- spacing or radii feel slightly off

Then re-render. Never assume a micro-polish edit improved the actual screen.

## Phase 5: Run the static and behavioral checks

Once a unit looks right:

1. Run `impeccable critique` on the converged surface.
2. If needed, apply `impeccable polish`.
3. Exercise the interaction itself, not just the still image.

Visual correctness and behavioral correctness are separate claims.

## Notes file

Keep a persistent notes file while the pass is active. Prefer `WORKING_MEMORY.md` if that workflow is already in use. Otherwise use `RENDER_NOTES.md`.

Minimum structure:

```md
## Render notes
- Recurring: mobile menu still feels attached to page content unless backdrop and scroll lock are both present.
- Recurring: transparent imagery needs scoped outlines, not global image outlines.
- Locked: accent stays restrained; do not spread it across every interaction.
```

Read the notes before each new unit so the same visual mistake is not repeated.

## Repo routing

If the repo contains all of the following:

- `PRODUCT.md`
- `DESIGN.md`
- `web/package.json`
- `web/tools/shot.mjs`

then load `references/astro-premium-storefront.md` and follow that path exactly.

Otherwise, adapt the same loop to the local frontend stack and state the substitutions explicitly.

## Hand-off format

Report completion in this shape:

```md
Render loop complete.

Units checked:
- header and mobile menu: 3 passes, desktop 1440 and mobile 390
- product cards: 2 passes, desktop 1440 and mobile 390

Pixel findings fixed:
- mobile overlay was not modal enough; added backdrop, scroll lock, and escape close
- sticky header was animating layout properties; moved to transform-safe behavior

Proof:
- npm test
- npm run build
- node tools/crawl.mjs

Residual risk:
- no live browser harness for gesture feel beyond screenshots
```

## What this is not

- Not a replacement for `impeccable`
- Not a replacement for `make-interfaces-feel-better`
- Not a one-shot generator
- Not permission to skip mobile
- Not permission to claim visual QA from code inspection alone
