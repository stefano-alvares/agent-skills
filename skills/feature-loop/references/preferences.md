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
4. **Standing engineering defaults**:
   - boring over clever
   - stdlib over dependency
   - deletion over addition
   - smallest working diff
   - calibration knobs left in for physical or tunable systems

Use the first source that decides the fork. Cite that one source in the decision log.

## What still parks

Never preference-resolved:

- irreversible actions
- scope changes
- new dependencies or spend
- security or privacy
- anything the spec lists as not-authorized

Route: TicketBlockedForStefano + decision packet with a Reframe option.

## Accountability

An unlogged decision is an envelope violation. The decision log is re-read at review.
