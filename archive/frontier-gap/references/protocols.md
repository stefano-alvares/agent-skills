# The protocols — full detail

The complete interpret → plan → build → review discipline. (Merged from the retired `fable-standard`,
`fable-plan`, `plan-lock`, and `working-memory` skills, 2026-07-24 — written from Fable 5's own
introspection, July 2026.) Each protocol ends with **the benchmark**: the explicit target a pass must meet.

## Protocol 1 — Interpret the prompt (before ANY action)

Rewrite the incoming request internally as a task spec:

```
GOAL BEHIND THE ASK: [why they want this, not just what they typed]
EXPLICIT CONSTRAINTS: [everything stated — quote fragments, don't paraphrase]
IMPLICIT CONSTRAINTS: [user's known conventions (AGENTS.md, DESIGN.md, the project's notes), platform
                       contracts, the project's file formats, append-only rules]
DONE MEANS: [the observable proof — a passing test, a rendered screenshot, a file in the right format]
AMBIGUITY: [interpretations that fork the work → resolve with the most reasonable assumption, state it,
            OR ask if the fork is expensive]
```

**The benchmark:** a stranger could execute the spec without reading the original message, and the user
would recognize their intent in it — including the parts they didn't type.

**User-facing mode:** when Stefano hands over a draft prompt and asks to improve it, run this protocol ON
the draft and return the rewritten spec — surfacing the implicit constraints he forgot to state is the
main value.

## Protocol 2 — The ledger (nothing skipped)

A multi-part message becomes a numbered ledger, kept in working memory (or the batch file in `docs/crew/` or
the project's notes on long tasks). Include the buried asks: questions inside parentheses, "also…" clauses, "and clean up X" at the
end of a sentence. Before ENDING any turn, walk the ledger: every item is done, explicitly deferred with a
reason, or explicitly declined. Never silently dropped.

**The benchmark:** zero threads lost across the whole conversation, not just the last message. If an
earlier turn left something open ("I'll do X after Y"), it's on the ledger until closed.

## Protocol 3 — Plan by dependency and risk, not category

*The working version of Protocols 1–3 lives in `plan-forge` (interpret, ledger, evidence pass, order by
dependency and risk, step contract, build contract, kill-test then lock, working memory). What follows is the
long form and the reasoning behind it; when the two differ, `plan-forge` is the one to run.*

Sonnet's planning failure is not bad plans — it's shallow ones: category-ordered ("first types, then
components, then tests"), no per-step proof, no risk ordering, written before reading the code.

### Phase 0 — Earn the right to plan (read first)

No plan before evidence. Read every file the change plausibly touches; trace ONE real flow end-to-end
(request → handler → logic → storage → response, or user action → state → render). Note existing patterns
and helpers you must reuse (plan-forge's build contract, REUSE line, overlaps — run them together).

**The benchmark:** you can name the exact line ranges each step will touch and cite how the current flow
behaves. A plan citing files you haven't opened is a guess wearing a plan's clothes.

### Phase 1 — Decompose

1. List the shippable units — each one user-observable or test-observable on its own. One feature at a
   time; never plan to one-shot the whole thing (documented failure: context exhausts mid-implementation).
2. Order them so the system is GREEN after every step — each step lands and verifies (commits only with
   Stefano's explicit yes). Never "it'll compile again after step 4."
3. **Riskiest step first as a spike.** The step with the most unknowns (new API, unclear data shape,
   platform contract) can invalidate the plan — surface that before investing in the rest. Check the
   platform-gotcha log in AGENTS.md or the project's notes before assuming a hang/timeout is your logic.

**The benchmark:** if interrupted after any step, what's landed is releasable. If step N fails, steps
1..N-1 don't need reverting.

### Phase 2 — Per-step contract

For each step, four lines — no essays:

```
STEP n: [name]
FILES: [exact paths — anything else needs announcing]
PROOF: [the runnable check that fails if this step is wrong — test, build, curl, screenshot]
RISK:  [what this could break + the caller-grep that clears it]
```

A step whose PROOF line is "looks right" is not a step; find the runnable check or merge it into a step
that has one. Harvest a **constraints checklist** from the original request too — every "must", "don't",
"keep", "only" — ticked before "done" (this is the checklist the critic pass inherits).

### Phase 3 — Context strategy (the part everyone skips)

Long tasks fail on context, not capability. Plan the memory explicitly:

- **Progress file** — one notes file: the batch file in `docs/crew/` or the project's notes (or fold into an
  existing `PRODUCT.md` — don't spawn a second). Four sections: `## Status`, `## Locked decisions (don't
  relitigate)`, `## Failed approaches (and why)` — the load-bearing one — and `## Recurring mistakes to
  pre-empt`. Update after every step. Measured: notes files cut cost ~11% AND raise resolve rate; a
  file-based memory helped Fable 5 "three times more than Opus 4.8" on Anthropic's long-horizon eval.
- **Write the note when you learn the thing, not when you remember to.** A note written at session end,
  from memory, has already lost the details that make it useful. And keep the *why*: "tried gradient hero
  → rejected" is useless; "tried gradient hero → generic SaaS tell, diluted the brand" transfers.
- **Re-read on resume and before each unit.** A notes file nobody re-reads is theater. On a fresh session
  or after compaction, reading it is the first action. This is what lets a weaker model with good notes
  beat a stronger model with amnesia. Curate per Anthropic's rules: one lesson per entry, don't save what
  the repo/git already records, update rather than duplicate, delete what turns out wrong.
- **Checkpoints:** mark each green step in the notes file; commits only with Stefano's explicit yes.
- **Fresh sessions over long ones:** plan where a fresh session + file-handoff happens (between shippable
  units). Full resets with structured handoffs beat compaction; Sonnet specifically exhibits "context
  anxiety" in long sessions. The plan + progress file must contain everything a fresh session needs.
- **Delegate exploration:** codebase searches go to subagents; keep the main context for the plan and the
  diffs.

### Phase 4 — Lock the plan, schedule the review

- **Lock:** restate the approach in ONE sentence before starting ("Plan: add the rate-limiter as
  middleware in `api/`, wire it into the 3 existing routes, no auth changes"). If you can't say it in a
  sentence, the plan isn't clear enough to build yet. That line is what you check yourself against.
- **Deviations announced, never silent.** The moment the plan stops fitting — a step is wrong, a shortcut
  is genuinely better, a new file needs touching — STOP, say so and why, update the plan, then continue.
  A deviation announced is fine and often correct; a deviation taken quietly is the failure (Composer
  2.5's most-reported bug: shortcuts taken "for faster implementation speed" without saying so). A model
  holding the plan only in its head has nothing to drift *against* — writing it down creates the
  reference that makes drift visible, even to itself.
- **Schedule the exit review NOW, in the plan:** after the last step, `critic-pass` with a fresh-context
  verifier. Premature completion is a documented long-horizon failure — a later glance sees partial
  progress and declares done; the scheduled review is the guard.
- **Write the plan's DONE line:** the observable end state (all PROOFs green + constraints ticked +
  ledger walked).

**The benchmark:** the plan names its own reviewer and its own done-proof before any code exists.

### Planning anti-patterns this replaces

- Category-ordered plans (types → components → tests) that leave the system red for hours.
- Plans written before opening the code.
- Steps with no proof, verified in one batch "at the end".
- 12-step plans for 2-step work — match plan weight to task weight; over-planning small work is itself a
  failure.
- The plan living only in chat history, evaporating at compaction.

## Protocol 4 — UI the way Fable plans it

Never start with code. In order, settling each before the next:

1. **Direction** — 3 mood adjectives + 1-2 reference points. One sentence: "this should feel like ___."
2. **Tokens** — typography (exact faces, scale ratio), palette (background/foreground/one accent), spacing
   scale. Written into a tokens file or DESIGN.md, not improvised per-element.
3. **Ban-list** — the mid-fi tells this project forbids: gradient text, glassmorphism, layout-property
   animations, decorative borders >1px, generic shadows. (Reference: the-one-jewellery DESIGN.md; run
   `design-ban-audit` for the mechanical check.)
4. **Structure** — per section: hierarchy (what the eye hits 1st/2nd/3rd), layout grid, one deliberate
   asymmetry or moment of restraint. THEN build whole sections against it — not incremental tweaks.
5. **Render loop** — `pixel-critique-loop`: screenshot desktop + mobile, critique against the direction
   (step 1), iterate. 2-3 bold passes, not 10 timid ones.

Minimalism rules (simplest thing that works; reuse before building) govern the mechanism, never the
ambition.

**The benchmark:** someone seeing only the screenshots could name the direction ("editorial, dark,
confident") without being told. If the UI could belong to any generic SaaS, the pass failed.

## Protocol 5 — Review code the way Fable does

1. **Context before judgment.** Read the full diff AND the files it touches — enough to know what the code
   is *for*. Never review a hunk in isolation.
2. **Trace, don't skim.** Follow one real input end-to-end through the changed path; predict each hop's
   output. Data-flow breaks hide where skimming feels fine.
3. **Hunt named classes** — under-propagated edits (grep every caller/usage of anything changed),
   docs-vs-source mismatches, silent-hang defaults, reward-hacked checks, dropped constraints, scope
   creep (`critic-pass` has the full list with Stefano's real incidents).
4. **Refute before reporting.** For each finding, actively try to prove yourself wrong — read the code that
   would make it a non-issue. Only findings that survive refutation get reported, ranked by severity, each
   with file:line and a concrete failure scenario.

**The benchmark:** every reported finding is CONFIRMED (you can state the input that triggers it), not
plausible. One confirmed finding beats five "consider whether…" hedges.
