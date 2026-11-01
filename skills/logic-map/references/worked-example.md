# Logic map: worked example and mismatch table

Referenced from SKILL.md (Phase 4 mismatch test, and the worked example).

## Mismatch table

Every difference between the map from the promises and the map derived from the code is exactly one of
these three:

| Difference | What it means | Where it goes |
|---|---|---|
| Code guarantees something the spec never claimed | An undocumented decision | Append to the batch file's Decided section or `docs/crew/decided.md`, add to the map |
| Spec claims something the code doesn't guarantee | A bug, or vapour | `diagnose` if it misbehaves; scope if it was never built |
| Both exist but disagree about the invariant | The dangerous one: two owners | Pick the owner, enforce there, delete the other |

## Worked example (compressed)

Spec: "the dashboard shows which projects shipped something this week."

- **Invariants harvested:** a project appears in the shipped list only if it has a Shipped item dated
  within the window; the window is the same for every project on one render.
- **Systems:** vault markdown *owns the ship date* → parser *owns date→calendar-day conversion* →
  scoring *owns the window comparison* → renderer *owns nothing, pure format*.
- **Ownership check:** "the window is the same for every project": owned by nobody. Scoring computes
  `now` per project. Two projects rendered either side of midnight get different windows. Found on paper,
  in one line, before any code existed.
- **Violation test:** can anything break "only if dated in the window"? Yes, the parser returns a
  timestamp, so scoring compares instants, and any consumer that forgets to normalise re-introduces the
  timezone bug. Move it: the parser returns a *calendar day in a declared zone*, and the timestamp is not
  representable in the type. Now the bug can't be written.
- **Decomposition:** rejected "scoring reads files directly": fewer boundaries, but it gives scoring two
  owned invariants (parsing and windowing), so a parsing change would silently alter windowing.
- **Box:** scoring's contract is `takes: (calendar day, window) → gives: boolean — owns: the comparison`.
  Any implementation satisfying that is correct, and the eventual `shippedSince()` was interchangeable.

Note the payoff: a defect like this normally surfaces after it ships, as a timezone bug in production. Here
the ownership check catches it on paper, for the cost of one line.
