# Profile — DeepSeek V4 Flash (0731)

Model ids: `deepseek/deepseek-v4-flash`, `openrouter/deepseek-v4-flash`.

## Observed signature

Source: illness-protocol implementation, training-app, 2026-08-01, opencode + `/frontier-gap`.
One run — treat as a hypothesis with evidence, not a law.

This model **initiates well and propagates badly.** Given invariants stated once in a spec, it
held all five, including two that required reading unfamiliar code to honour (folding an
insufficiency flag into a norms check; ordering a persisted state transition before a forced
regeneration). Initiation is not the gap here. Frontier-gap's core thesis is already satisfied —
do not spend tokens re-teaching it.

The gap is at the **sibling boundary**:

- Wrote one writer idempotent, documented *why* in its docstring, then wrote the paired writer
  twenty lines below with an unconditional insert. The reader of those rows used a
  single-row accessor that errors on duplicates — a live 500 on the second tap.
- Used `if not exists` four times in one migration, then a bare `drop constraint` in the same
  file.
- Tests seeded exactly the row count the happy path expects, and asserted the insert it had just
  performed. The database double modelled no constraints, so no test in that design could have
  failed on the defect.
- Reported "complete and fully green" with accurate counts and no unverified-surface line.

The failure is not carelessness and not rationalization under pressure. It applies a rule at the
site it is thinking about and does not sweep outward.

## Weighting

**Pass 1 is the one that pays.** Run it before Pass 2, and run it even when the change feels
local. Two additions for this model:

- Include the migration and the route in the sibling list, not just the module you edited.
  Its misses cross file boundaries.
- For every writer, name its **undo** — the dismiss for the confirm, the drop for the create,
  the close for the open — and check the invariant there explicitly. This is where every observed
  miss landed.

**Pass 2 needs the mock clause spelled out.** Naming the one-line breaking change is not enough
on its own here: it wrote tests where that line existed but the double could not express the
constraint being violated. Column 3 is the load-bearing one.

## Delivery

Short mechanical tables land. Long prose protocols do not — the `/frontier-gap` run produced
correct invariant handling and still shipped the sibling defect, so more prose is not the lever.
Give it the table to fill and let the empty cell be the finding.
