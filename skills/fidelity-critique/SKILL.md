---
name: fidelity-critique
description: Use when asked to assess visual fidelity or define fidelity targets, to set rung targets
  before building a premium page, and before premium UI work is called done when no fidelity check
  has run. Not a mandatory gate for small UI edits.
---

> **Cross-harness ownership.** In Claude Code, the `fidelity-critique` subagent
> (`~/.claude/agents/fidelity-critique.md`) owns the trigger and reads this canonical long-form rubric
> when a dimension is ambiguous. It is deliberately unlinked from `~/.claude/skills/` so one trigger
> phrase has one Claude outcome. Hermes may expose this file directly as a skill because it has no
> equivalent custom-agent surface. Keep this path stable; do not relocate the rubric under any
> single consumer.

# Fidelity Critique

Fidelity is not polish. It is **commitment**: a design is high-fidelity when
every element can answer "why does this look like THIS product and not any
product in the category?" Low-fi → hi-fi is not a smoothness gradient, it is
a ladder of commitments, and work stalls at the rung where the last
commitment was made. Your job: find the rung, prove it with evidence, and
name the ONE next commitment.

Why this needs a skill: models plateau at rung 2 (template-fi) because rung
3+ requires making a decision the prompt didn't ask for — a premise, a
grammar, a rule that bans a familiar pattern. This skill forces those
decisions to be found (or found missing) in the code, so the critique never
runs on vibes.

## The ladder

Score the target 0–5 where evidence supports it. Source establishes structural
commitments, not every rendered appearance or interaction. A verified design
sits at the HIGHEST rung where ALL checks pass — one
un-ported page or one unratified rule-violation drags the whole target down
(inconsistency reads as "unfinished," which is worse than uniformly mid).

**0 — Wireframe.** Boxes and defaults. Placeholder text/images, browser or
framework default type, no palette.

**1 — Dressed wireframe.** A palette and a font were chosen, applied
globally, and that's the whole design system. Spacing is uniform; every
section is a centered container.

**2 — Template-fi (the AI plateau).** Real content, competent execution,
zero commitments. Tells: identical card grids for anything list-shaped;
mono-uppercase kicker above every heading; pill buttons; icon-title-text
triplets; hover states that lift+shadow; the palette/theme is guessable
from the product category alone. Nothing is *wrong* — and nothing belongs
to this product specifically. Most "looks generic" complaints are rung 2.

**3 — Committed style.** A real token system (no raw color literals outside
the tokens file), a typography contract (which face carries display / body
/ data, and where numerals must be tabular), a named palette with stated
rules ("accent X only on grounds Y"), and at least one BAN on a familiar
pattern, written down and enforced. Still interchangeable: swap the logo
and another brand could ship it.

**4 — High fidelity.** The design has a **premise (found, native or declared)**:
one sentence naming the world the interface derives from (a real
scene/object/ritual, the product's own native system, or a declared
construct with stated laws), and at least two **signature mechanics**
derived from that premise, not from a component library. It has a **register grammar**: the house's own answer
to "how does inventory render / how do sections announce themselves / what
is the wayfinding device," different from the category default. Interactive
mechanics have static-complete fallbacks (touch, reduced-motion, no-JS
where it matters). Swap the logo now and the design stops making sense.

**5 — Crafted.** Rung 4 survives interrogation: token discipline is
absolute (grep-clean), contrast is verified in every palette/mode pair,
docs and implementation agree on a single source of truth, contract tests
encode the design decisions so regressions fail CI, and data is truthful
(no placeholder strings can reach a rendered page). The fidelity is
load-bearing, not decorative.

## The six dimensions (score each, then take the minimum)

Score each 0–5 against the ladder. Keep dimension scores HONEST (a 5 stays
a 5 even when another dimension drags the target); the headline rung is the
MINIMUM across dimensions, because fidelity is conjunctive: a beautiful
premise with token chaos still reads unfinished. The table above the
headline is what protects the wins from a shallow reading. Every score
requires cited evidence (file:line, a grep result, or an inspected render/test
with its viewport and state). A score without evidence is invalid — that is
the anti-taste-drift rule. Missing access or evidence is UNKNOWN, not a zero
or a pass. Distinguish an observed absence from a surface you could not check.
If any dimension is unknown, do not assert a verified headline rung; report
the supported dimension scores and, if useful, a labeled source-only provisional
assessment. The 0–5 ladder and minimum-across-all-six rule remain unchanged.

**Inconsistency scoring rule** (how much one gap costs): a surface that
falls back to the category default with no documented house answer caps
THAT dimension at 3 (a gap, not a collapse). A live violation of the
project's own written ban caps its dimension at 2 — drifted-from rules read
worse than absent rules. The minimum-across-dimensions rule then propagates
the cap to the headline; never cap the other dimensions' scores to match.

**Rendered vs. source triage:** grep hits inside code comments, docs, or
test files are not violations — bans on copy (em dashes, placeholder
strings) apply to what a visitor can see. When grepping, triage every hit:
comment/doc → note and drop; content files, markdown pages, template
strings, data consumed by templates → candidate: trace whether it reaches
visitor-visible output. A generated static-output match can establish emitted
content for that build, but not every runtime state or visual property.

1. **Premise.** Is there one sentence, in docs or legible from the code,
   naming the premise (found, native or declared) the design derives
   from? Do mechanics derive from it? (Evidence: design docs, CSS comments, mechanic implementations
   that reference the premise's logic, e.g. light behaving like a lamp, a
   blinking cursor in a terminal brand, or a declared law, not a
   decoration.)
2. **Register grammar.** For each list-shaped surface (inventory, nav,
   sections, menus): does it render in a house-specific form, or the
   category default (card grid, hamburger drawer, kicker+heading)? A
   grammar counts only if it is CONSISTENT — the same answer everywhere,
   or a documented ratified exception.
3. **Token discipline.**
   `grep -rnE "#[0-9a-fA-F]{3,8}\b|rgba?\(" --include="*.css" <src> | grep -v "tokens\|variables"`
   (adjust the exclusion to the project's token file names; triage comment
   hits per the rendered-vs-source rule). Also: is there a stated rule for
   when each accent may appear, and is it followed? Hardcoded-literal
   islands are the clearest mid-fi tell available to a model — they need
   zero taste to find.
4. **Type & data contract.** Named face per role (display/body/data),
   tabular-nums on every money/count surface, real data shapes (refs,
   units, certifications) rather than lorem-adjacent filler. Check the
   highest-stakes number on the highest-stakes page first.
5. **Fallback completeness.** Every pointer/hover mechanic: what does it
   look like on touch, under prefers-reduced-motion, before JS runs? The
   rest state must be complete, not broken-waiting-for-input. (Evidence:
   the media queries and JS guards, or their absence, establish source intent;
   exercise the relevant touch, reduced-motion, and pre-JS states to verify
   the rendered fallback. Mark unexercised behavior unknown.)
6. **Coherence & truth.** Do docs and code agree (is a source of truth
   declared)? Are the design's own bans enforced everywhere or explicitly
   ratified? Can placeholder/unfinished content reach a rendered page?
   Run the project's build + tests if present; a failing design-contract
   test is evidence here.

## Procedure

1. **Resolve the target** (page, component, or whole app). Read the
   project's design docs first if they exist (DESIGN.md, PRODUCT.md);
   score against the project's own stated rules before generic ones.
2. **Collect evidence per dimension** — greps, file reads, build/test runs,
   and permitted rendered/interaction checks. Label source-only evidence.
   Source presence does not prove contrast, legibility, responsive appearance,
   or working fallbacks. Do not screenshot unless the environment permits it;
   if rendered access is missing, state the affected unknowns rather than
   substituting source inspection for visual verification.
3. **Score the six dimensions** only where evidence supports them. When all
   six are verified, minimum = the rung. Otherwise label the headline unverified
   and distinguish any source-only provisional assessment from rendered proof.
4. **Name the next commitment.** One paragraph: the single decision that
   moves the target up exactly one rung, phrased as a commitment to make
   ("choose the premise and derive the inventory display from
   it"), not a list of chores. If the target is at rung 2, the answer is
   almost always a premise + one ban, never "add more polish."
5. **Report** in this exact structure:

```
## Fidelity: rung N — <rung name>

Evidence scope: <source-only / rendered states checked; exclusions and unknowns>
If a dimension is unknown: headline UNVERIFIED, not a verified rung N.

| Dimension | Score | Evidence |
|---|---|---|
| Premise | n | file:line — one clause |
| Register grammar | n | ... |
| Token discipline | n | grep result summary |
| Type & data contract | n | ... |
| Fallback completeness | n | ... |
| Coherence & truth | n | ... |

**What is already committed:** <2-3 bullets, so wins are protected>
**The next commitment:** <one paragraph>
**Drag-downs:** <anything scoring below the mode — the inconsistencies>
```

## Using this to DEFINE fidelity before building

When invoked before/while building (not critiquing): run the ladder in
reverse. Write the rung-4 commitments FIRST — premise sentence, 2 mechanics
derived from it, register grammar answers for every list-shaped surface,
the ban list — into the project's DESIGN.md. Then build. A model given
committed rules executes rung 4; a model asked for "a nice page" returns
rung 2. That asymmetry is the entire reason this skill exists.

## Boundaries

- Impeccable's critique owns slop-detection, heuristics, personas, and UX
  scoring. When both run, run impeccable first; this skill answers only
  "which rung, and what's the next commitment."
- Do not conflate fidelity with maximalism: a rung-5 design can be austere.
  Motion, texture, and interactivity only count when derived from the
  premise; otherwise they are rung-2 decoration and should be scored as
  such.
- Respect the project's ratified exceptions (a documented rule beats this
  skill's defaults) — but an exception documented AFTER the violation, with
  no constraint attached, is drift wearing a ratification costume; flag it.
