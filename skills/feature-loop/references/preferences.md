# Preferences contract

Replaces mid-flight human gates. At any open fork during post-flip execution, resolve it here — never ask, never pick silently.

## When

Any open fork in post-flip execution: naming, structure, library-vs-stdlib, copy tone, ordering, any scope-neutral implementation choice.

## The 1→3→1 contract

1. State the fork in one line.
2. Generate exactly three genuinely distinct options. Not one real option and two strawmen.
3. Choose one by the recorded preferences below.
4. Log to the feature's Notion page body:
   - the fork (one line)
   - the three options (one line each)
   - the choice
   - the single preference that decided it

Never ask. Never pick silently.

## Preference sources, in precedence order

1. **The approved spec's own text.** If the spec speaks to the fork, it wins.
2. **Per-project docs**, when present: DESIGN.md, PRODUCT.md, the project brief.
3. **Vault defaults**:
   - `c3po_vault/context/code-style.md` — small, surgical diffs; no unrequested abstractions
   - `c3po_vault/context/stack-defaults.md`
   - `c3po_vault/soul.md` — BLUF, plain words, one term per concept
4. **Grill harvest 2026-08-19** (Stefano's answers, Notion: Preference Grill — 2026-08-19):
   - **Ticket goal:** make it work and succeed first; make it better in a later wave. Uncertain implementations stay flexible — seams and knobs left in, marked for repair.
   - **Tests:** the suite is living. A behavior change updates or removes the tests it breaks — flagged, never worked around, never buried under new tests. No mass test generation.
   - **Stack:** no hardcoded stack. A new project's architecture is decided by an evaluation against the app's needs (RAG → Next.js+Supabase-shaped; animation-rich → Astro-shaped are examples, not rules). Docs never freeze a stack choice.
   - **Dependencies:** spec pre-authorizes a named list; unlisted parks.
   - **Budget:** a RANGE in the BLUF, advisory only — cost never gates planning or implementation quality. No cost hard-gates. Waste is prevented by issue evaluation, not ceilings.
   - **Issue evaluation:** the same surface failing more than twice → raze-review + logic-first-debug diagnose rebuild-vs-repair; scrapping needs Stefano's approval, never the model's hesitation.
   - **Models:** coordinator may be Opus at high effort running frontier-gap; Fable counsel writes/blesses the plan and makes final code decisions; both debate under brutal-honesty. Workers tiered by ticket difficulty; trivial work runs inline.
   - **Simplicity:** function first; every implementation goes through plan-forge, tiered to the task.
   - **Staple docs per project:** DESIGN.md, PRODUCT.md, and the logic map. Intake produces the missing ones.
   - **Shipped:** defined in feature/logic transformations, never "tests pass". Every ticket carries a goal.
   - **Error-path reviews** use the brutal-honesty register.
   - **Cadence:** one daily digest, one notification, approvals at Stefano-set windows.
   - Unconfirmed (recommendation stands as default until he says otherwise): parallel-on-by-default (Q5), repair-flip severity split (Q8), the riskiest-list contents (Q4 answered orthogonally).
5. **Standing engineering defaults**:
   - boring over clever
   - stdlib over dependency
   - deletion over addition
   - smallest working diff
   - calibration knobs left in for physical or tunable systems

Use the first source that decides the fork. Cite that one source in the decision log.

## What routes to technical counsel

A code-based fork these preferences do not decide AND that is not on the park list below
goes to counsel, never to Stefano. Mechanics live in SKILL.md (Technical counsel): raw
fork first, counsel's own probe ledger, max 2 rounds, cap 3 per wave, overflow and
deadlock park with the transcript. Every counsel-resolved fork is also a preference gap —
log it for the next preference grill (`references/preference-grill.md`).

## What still parks

Never preference- or counsel-resolved:

- irreversible actions
- scope changes
- new dependencies or spend
- security or privacy
- anything the spec lists as not-authorized

Route: TicketBlockedForStefano + decision packet with a Reframe option.

## Accountability

Every fork resolution is logged before the tick ends. The final reviewer cross-checks the
riskiest tickets' diffs against the log: a design choice visible in a diff with no
matching log entry is a reportable finding.
