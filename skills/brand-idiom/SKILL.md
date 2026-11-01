---
name: brand-idiom
description: >-
  Use when the user asks for unique, creative or non-generic elements, says an element feels like every
  other website, wants components that feel real or brand-native, or wants a standard control (toggle,
  card grid, drawer, badge, carousel, paginator, spinner, modal) redesigned in brand language. Also use when building interactive elements for a brand
  with a committed direction, or listing the element inventory when porting a site from mid-fi to
  high-fi. Names the brand's native idiom (physical-object, editorial, instrument, archival, terminal,
  architectural), then derives each element by 1-3-1 brainstorming from found objects, built systems or
  declared constructs.
---

# Brand Idiom

> **Builder mode.** If you are implementing a card that already names the idiom, do not run the
> full 1-3-1 walk. Read only step 4 (the fallback contract) and step 6 (the implementation contract), and
> build inside the named idiom. Run the full walk only when the card asks you to choose or change the idiom.

Generic elements are answers copied from other websites. An idiom-derived
element is an answer taken from the brand's own world: not "a toggle
styled gold" but "the lamp in the dealer's room, which happens to be
flippable"; not "a spinner styled green" but "the blinking block cursor,
because in a terminal waiting IS a cursor." The difference is where the
behavior comes from — decoration sits on top of a control; the idiom's
logic replaces the control's logic.

Why a skill: models default to the component library because the prompt
names the generic element ("add a theme toggle"). The library answer is
always available and never wrong, so nothing forces the two better
questions: *which world does this brand actually live in?* and *what does
this job look like in that world?* This skill forces both, and refuses
decoration as an answer.

## Step 0: identify the idiom (the right -ism for THIS brand)

Reuse an idiom already approved in the handoff; do not reopen an approved
direction. Otherwise, before any element work, name the brand's **native
idiom**: the world where the product's substance already lives. This is a finding, not a
style choice — it must be defensible from the brand's actual facts
(PRODUCT.md, what the product is, who touches it, what its artifacts
look like in real life), never from aesthetics shopping.

Idiom families to test against (not exhaustive — name a truer one if the
brand demands it):

- **Physical-object** — the product is a thing presented, handled,
  stored: jewellery under a lamp, furniture in a workshop, coffee at a
  roastery. Elements derive from objects and rituals (trays, seals,
  drawers, lamps). This is the only family where skeuomorphism is even
  on the table, and even here the object contributes logic, rarely skin.
- **Typographic / editorial** — the product is words, judgement, or
  curation: a journal, a research house, a foundry. Elements derive from
  print conventions: folios, running heads, marginalia, footnotes,
  colophons, pull quotes, imprint pages.
- **Archival / bureaucratic** — the product is records and trust:
  registries, provenance, compliance, finance. Elements derive from
  ledgers, card catalogues, stamps, dockets, carbon copies, tallies.
- **Instrument / control-panel** — the product operates something real:
  monitoring, audio, flight, machines. Elements derive from meters,
  toggles-with-guards, dials, annunciator lights, test points.
- **Terminal / digital-native** — the product lives in the machine
  itself: dev tools, infra, CLIs. Elements derive from prompts, cursors,
  exit codes, diffs, man pages, pipes. (A devtool wrapped in a physical
  metaphor reads as costume; its real world is already on screen.)
- **Architectural / spatial** — the product is places or structure:
  galleries, hotels, real estate. Elements derive from thresholds,
  floor plans, wayfinding plates, sight lines.
- **Cartographic / field** — the product is territory, journeys,
  expeditions, logistics. Elements derive from map furniture: scale
  bars, bearings, route logs, waypoint marks.

**The artifact test** (run it before choosing): what does the user
physically hold or see in the real-world version of this job? That
object votes louder than the product category. For a digital-native
product the artifact is already on screen (a prompt, a diff, a log), and
that counts. Process-heavy but
document-native products (tax filing, insurance claims, legal case
management, medical records) FEEL like instrument-panel — a real
external process succeeds or fails — but their users never touch a
gauge; they touch returns, reference numbers, files. Discriminator:
a dial or meter in the user's real hands → instrument; a reference
number or file → archival.

Write the choice as one sentence naming the world and the evidence:
"This brand's substance is X, handled by Y, in world Z — therefore the
idiom is W." If two families are defensible, note both and run the
artifact test; if still tied, the element derivations (below) will
reveal which one carries. A brand may keep ONE
secondary idiom for a bounded surface (e.g. archival idiom inside a
physical-object house for its provenance pages) — but name the boundary,
or drift follows.

If the project already has a committed premise/direction in DESIGN.md,
that decision wins; your job is only to derive within it.

The premise can be found (an object or convention that already exists),
native (the product's own system, such as a terminal or a ledger of its
own data) or declared (an imagined construct with stated laws). A
physical object is one option, not a requirement. This matches
fidelity-critique rung 4: "a premise (found, native or declared)".

## The derivation, step by step

1. **Name the JOB, not the element.** Strip the request to its function:
   a toggle is "a binary state the visitor flips"; pagination is "moving
   through a register"; a badge is "a status attached to an object"; a
   modal is "an interruption demanding attention"; a skeleton loader is
   "the moment before the thing is present." The generic element is one
   answer to the job; you need the idiom's answer.

2. **Pick the source — found or built.** Two source types, both legal:

   **Found sources**: objects, artifacts, or conventions that already
   perform this job in the idiom's world. A dealer's room has lamps,
   trays, drawers, ledgers, loupes, seals, engraved plates, tally
   marks. A terminal has prompts, cursors, exit codes, diffs, pagers.
   A broadsheet has folios, rules, running heads, corrections notices.
   List 4-6 candidates before choosing — the first association is
   usually the most clichéd one.

   **Built systems**: an invented apparatus derived from the PRODUCT'S
   OWN NATURE — its physics, name, form, or imagery elevated into an
   organizing system that no real room contains. Star stones show a
   star figure, and stars form systems, therefore a collection of star
   stones can render as an orrery: each room an orbital system whose
   own data (count, kind) drifts in orbit around the gem. A roastery's
   roast curve can become the navigation spine; a foundry's glyphs can
   populate a specimen sheet that IS the index. Built systems are the
   distinctiveness ceiling — nobody else can have your orrery — and
   they cost more: they usually need autonomous motion (a documented,
   earned exception), more JS, and a stronger misread mitigation.

   Rules for building: the leap must be anchored in a REAL property of
   the product (asterism is real gemology; a pun or vibe is not an
   anchor); the built system must still OBEY the idiom's physics rather
   than replace them (the orrery's stones still ignite under the same
   pointer-lamp as everything else — it extends the world, it doesn't
   fork it); and its moving parts should carry real data (the orbiting
   text is the room's actual count and kinds), because an apparatus
   that displays nothing is a screensaver.

   **Imagined constructs**: a third source with no real-world anchor at
   all — a fictional apparatus, an invented ritual, a world that exists
   only for this brand (a vault with no address, an instrument nobody
   has built, a cartography of something unmappable). Fully legal, and
   sometimes the strongest answer for brands whose substance is itself
   abstract (software, finance, ideas). The discipline changes, not
   the standard: since there is no reality to borrow logic from, you
   must DECLARE the construct's logic in two or three laws ("the vault
   only opens for one visitor at a time; light inside it has weight"),
   and then obey those laws with the same rigor a physical source gets
   — the THEREFORE sentence derives from your declared laws instead of
   real physics. An imagined construct that breaks its own laws is
   worse than a generic element, because it teaches the visitor the
   design means nothing. Coherence is the anchor; realism was never
   the point. Expect the highest misread risk of the three sources and
   budget the mitigation up front.

   Spend rule across all three: found sources for infrastructure (nav,
   toggles, forms), where a visitor needs recognition more than
   wonder; built systems and imagined constructs for the product's own
   display moments — collection, hero, showcase — where wonder pays.

3. **Derive behavior from the source's own logic.** The mechanic must be
   a consequence of how the source actually works — its physics if it's
   an object, its conventions' internal logic if it's a medium — stated
   as a causal sentence: "a star stone shows its rays only under a point
   light, THEREFORE ray sharpness follows pointer distance"; "a terminal
   signals 'still working' with a blinking cursor at the prompt,
   THEREFORE the loading state is the cursor, and completion prints a
   result line, not a toast." If you cannot write the THEREFORE
   sentence, the source is decoration and you must pick another. The
   source's logic also sets the limits: nothing loops for decoration,
   nothing sparkles for attention, a terminal never animates what it
   would print.

4. **Write the fallback contract before the flourish.** Every derived
   mechanic needs: a static-complete rest state (fully legible with zero
   interaction), a touch answer (no hover exists), reduced-motion and
   no-JS answers, keyboard parity (focus does what pointer proximity
   does), and real semantics (a lamp that is a theme toggle still
   carries role="switch" and aria-checked). An element that only works
   under a fine pointer is a demo, not a component. Run the
   autonomous-motion check here too (see Guards): if the element moves
   without the visitor, is that motion driven by real external state
   changes (earned) or by a self-running loop (decoration)? This is the
   cheapest moment to catch it — retrofitting the answer after step 6
   means respeccing.

5. **Diverge and converge: 1 → 3 → 1.** One job frame in, three
   candidates out, one recommendation. The three candidates should span
   source types — aim for one found, one built, one imagined (settle
   for two types when the third is genuinely forced) — because three
   variations of the same source type is one idea wearing three hats,
   not divergence. For each: the source and its type, the THEREFORE
   sentence (from real logic or declared laws), interaction cost (JS
   weight, motion budget, viewport story — how it behaves at every
   width the element actually lives at), and the risk (what breaks if
   it's misread). A comparison table works well. Then converge:
   recommend the strongest and say why; name the runner-up and when
   review should prefer it — the second-choice source often survives
   review better.

6. **Write the implementation contract** for the chosen source, as the
   ONE shippable spec: restate the step-4 fallback contract inside it
   (a spec that references another section isn't handoff-complete), then
   add what only this step knows — files touched, which design tokens it
   may use, what it must never use (raw literals, the project's banned
   patterns), elevation semantics (raised, recessed, or deliberately
   coplanar with an existing surface), what changes when real assets
   (photography, logos) land, and the contract tests that will encode
   the element's behavior.

## Worked derivations

**Physical-object idiom** (a jewellery house: "a dealer presents rare
star stones one at a time under a single point light"):

| Generic element | Job | House source | THEREFORE sentence |
|---|---|---|---|
| Theme toggle | flip a binary state | the room's lamp | the room is lit or dark, therefore the control IS the lamp: a dot that slides to the lit end and glows |
| Product card grid | arrange inventory | dealer's gem tray | stones sit in recessed velvet wells under one lamp, therefore stones near the pointer ignite and distant ones rest dim |
| Infinite carousel | rotate featured items | scrolling accession ledger | a register is read line by line, therefore it scrolls like a ledger, pauses under the hand, never accelerates |
| Primary button | commit an action | engraved brass plate | an engraved plate is pressed into, therefore the CTA recesses and tilts under the finger, max a few degrees |
| Scroll progress | show position | margin tally | an archivist tallies rooms in the margin, therefore a hairline rail with a gold tick marks the current room |
| Status badge | mark an object's state | wax seal / filed stamp | sold pieces are filed, therefore they rest desaturated with a small rotated seal, not a colored pill |
| Collection overview | show the archive's structure | BUILT: the orrery | star stones are stars and stars form systems, therefore each room is an orbital system whose count and kind drift in orbit around its gem — still ignited by the same lamp |

**Terminal idiom** (a CI/devtool: "the product's real home is the
terminal where its users already live"):

| Generic element | Job | Native source | THEREFORE sentence |
|---|---|---|---|
| Spinner | show work in progress | the blinking cursor | a terminal signals work at the prompt, therefore loading is a block cursor and completion prints a result line, not a toast |
| Status badge | mark pass/fail | exit code | processes end in codes, therefore status renders as `0` green / non-zero red with the code itself, not "Success!" |
| Onboarding modal | teach first use | man page / `--help` | a CLI teaches via help text on demand, therefore onboarding is an inline help pane summoned by `?`, never an interrupting overlay |
| Data table | compare records | column-aligned output | terminals align with monospace columns, therefore the table IS tabular mono text with a header rule, not zebra-striped cards |

Same skill, opposite surfaces — nothing in the terminal table is
"physical," and applying the jewellery table's trays and seals to a
devtool would be exactly the costume this skill exists to prevent.

The tables show only each derivation's WINNER — every row still went
through the full step-2 candidate walk and step-5 three-way comparison
before earning its place; do not skip those steps because the winning
source seems obvious.

## Guards

- **Idiom budget.** The idiom is load-bearing at a few moments (the
  signature mechanics), quiet everywhere else. If every element gets a
  costume, the result is a theme park. Rule of thumb: per page, 1-2
  elements carry full derived behavior; the rest obey the token system
  and stay flat-but-refined.
- **Wrong-ism check.** Before deriving, re-test the idiom itself: would
  this brand's actual users recognize this world as theirs? A bank in
  terminal idiom, a devtool in velvet — the derivations can be executed
  perfectly and still be costume. When an element resists derivation
  ("there's just no ledger answer for this"), that resistance is
  evidence the idiom is wrong or the element should stay conventional.
- **The autonomous-motion exception must be earned.** Anything that runs
  by itself (an orbit, a ledger scroll, a blinking cursor) is allowed
  only when the idiom says the world moves without the visitor, it is
  documented as a named exception, and it freezes complete under
  reduced motion.
- **Conversion surfaces stay legible.** A mechanic may reward attention
  (ignite, sharpen, glow) but never withhold information a buyer needs —
  price, title, and status are readable in the rest state, always.
- **Interrogate the misread.** For the chosen candidate, name what a
  first-time visitor might think it is. If the misread blocks the job
  (they don't realize the lamp is a toggle), add a conventional
  affordance (position, grouping, label) rather than abandoning the
  source.

## Boundaries

- fidelity-critique SCORES commitment; this skill CREATES it — run this
  when fidelity-critique says "the next commitment is a premise-derived
  element." A critique does not itself authorize a redesign; use this
  when that work is requested. Taste critique (general taste, layout, and
  slop review) belongs to impeccable.
- This skill designs and specs; building still goes through the project's
  normal build/test/verification discipline. The spec output should name
  files, tokens, fallbacks, and the contract test that will encode the
  element's behavior.
