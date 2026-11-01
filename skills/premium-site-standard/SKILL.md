---
name: premium-site-standard
description: >-
  Use when planning, building or checking any studio website page: the studio's
  quality bar (bespoke objects, brand system, subtle motion, one journey per page,
  client autonomy, real handover) and its standing direction. Not for inventing a
  brand mechanic (brand-idiom) or scoring fidelity (fidelity-critique).
---
# Premium site standard

Use this as the standing process for every website, from first plan through
handover. It turns the premium-vs-cheap bar into a repeatable checklist.
Do not invent prices, support windows, or platform choices the project has
not agreed. Brand-specific objects and interactions still go through
brand-idiom; scoring goes through fidelity-critique; taste and polish go
through impeccable.

## What "premium" means here

A site earns the bar when a visitor can tell it belongs to this business,
can follow one clear path to act, and the owner can keep it alive after
handover. Generic competence is not enough.

## Before any page

1. Name the audience, the one action the site must earn, and whether the
   work is repair, redesign, or new.
2. Load the project's DESIGN.md / PRODUCT.md, `docs/crew/bans.md` and
   `docs/crew/decided.md` if they exist. Written project truth wins over this
   skill and over every generic taste skill (design-taste-frontend, impeccable)
   when they conflict on a settled choice.
3. Plan the page as a journey: opening claim, proof or offer, then one
   primary action. Do not leave the main action in the footer only.
4. Plan visual assets as **objects** that stand for something real and
   amplify the nearby text (a spanner for repair, paired frames for a
   redesign, a blank ruled sheet for a new site). Derive those objects
   with brand-idiom. They are not stock photos, free icon packs, or
   miniature page layouts unless the brief asks for a layout study.
5. Confirm the token jobs before inventing new colours: primary, secondary,
   highlight, soft neutral, divider, body text. About five cohesive colours
   with stated roles beat a large unruled palette.

## Build bars (every surface)

### Bespoke graphics
- Custom HTML/CSS (or project-owned) graphics that match tone and brand.
- Each graphic has a job: break up content, guide the eye, or make a claim
  easier to grasp.
- A mismatched graphic is worse than none. Drop it.

### Brand system
- Logo is intentional, not a throwaway mark.
- Type is thoughtful: named roles for display, body, and labels; readable
  sizes; no childish or illegible faces.
- Colour roles are written and followed. No random accents.

### Motion
- Subtle only: fade or settle on scroll, honest hover on controls.
- Nothing that bounces, spins, or distracts from reading.
- Reduced-motion and no-JS must leave the page complete.

### Structure and CTA
- Every page has one purpose and a next step a stranger can find.
- Internal links and hierarchy must make sense to people and to search.
- The primary action is obvious on the page that should convert.

### Client autonomy
- Prefer an editable setup the owner can update without a developer for
  ordinary content changes, when the project has chosen that model.
- Do not claim a CMS or editor the build does not actually include.

### Handover
- Plan training, how to update, and what support window exists only from
  agreed project terms. Do not invent a free-support duration.
- Do not treat "publish" as the end of the job when handover is in scope.

## Studio standing direction

Stefano can override any of these per project (check `decided.md` first; Studio
Naach has an explicit "go all out" motion override).

- Each section gets its own deliberate arrangement, not one repeated ruled
  two-column pattern. Implied hierarchy (space, scale, tone) over borders and
  dividers.
- The AI-default look (cream ground, display serif, earthy accent lifted from the
  product) reads as generic to him. Never present it as the plan.
- Confident wording without hedging disclaimers. Copy sounds like a person
  talking: contractions, varied rhythm, at most one list of three per section, no
  clipped two-beat slogans ("Clear decisions. Visible progress.").
- Colour is visibly present: one palette accent per service, as tone in surfaces
  and drawings, never as pills, badges or coloured borders.
- Motion is "intriguing, not overwhelming": one hero per moment; flourishes play
  once per visit and end exactly on the static state. Describe motion by its end
  state.
- Compact navigation: tight padding, 44 px targets kept; state changes morph
  continuously and can be interrupted, instant under reduced motion.
- No site-within-a-site: never render a miniature of a website as an
  illustration or animation end state.
- No extra visible controls that cost fidelity (a pause button); meet the need
  through interaction.

## When setting up each page

1. Write the page purpose in one sentence.
2. List the objects/assets that must sit beside the offers or claims.
3. Place the primary action where the journey ends, not only in chrome.
4. Check the page against the bans in the project's design note, then
   against this skill's avoid list.

## Avoid

- Plain text on a plain field with no object or structure that earns it
- Stock photos and free icon libraries used as "premium" decoration
- Card grids, pills, lift-shadows, and kickers when the project bans them
- Loud motion, scroll-jacking, or animation that hides required content
- Buried CTAs and pages that dump the visitor into a maze
- Fake testimonials, metrics, prices, or support claims

## After a material visual change

1. Atlas runs fidelity-critique (and impeccable for critique or polish) when the ask is commitment or the
   look must rise. Workers do not; they hand back shots.
2. Verify in a real render for the changed surfaces (Hermes:
   `node ~/.hermes/tools/shots/shots.cjs`; Claude Code: a browser screenshot at
   desktop and phone width). Source-only is not a ship claim.

## Boundaries

- This skill is the bar. brand-idiom invents the objects. plan-forge locks
  scope and sequences the work.
- Do not reopen a sealed project design note to chase taste from a single
  reference; raise the look inside the project's own premise, or replace the
  premise with the owner when a redesign is authorised.
