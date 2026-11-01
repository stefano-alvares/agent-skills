# Preference grill

One bounded decision session that captures Stefano's preferences so the loop decides more
forks without him. Mine and research first, then present every foreseeable
confirm-or-correct question in one batch, each with a recommended answer. Ask one
follow-up batch only when an answer cannot decide the underlying preference.

**Async mode.** When Stefano is not live, project the grill as a DOC instead: every
question written out with its recommended answer and an answer slot, landed in Notion as
a child page of the Control Plane. He answers in his own time; the coordinator harvests
the answers into the output contract below on the next tick that finds them. Async keeps
the same batch shape and gets at most two round-trips: the harvest, plus ONE follow-up
doc for answers that cannot yet decide a fork. Still open after that → logged as gaps
for the next live session.

## When to run

- Once, at system setup or after a skill version bump that changes decision routing.
- Again when logged preference gaps reach 5, or before the first wave on a new project.
- Never mid-wave. The grill is gate-side work, like the spec.

## Before asking anything

Mine what already exists — never ask what a document already answers:

1. Logged preference gaps (Notion, from counsel-resolved or parked forks).
2. Decision logs of past waves — every 1→3→1 whose deciding preference was a
   "standing engineering default" is a preference that deserves his own words.
3. Counsel transcripts — each one marks a fork the recorded preferences failed to decide.
4. `c3po_vault/context/code-style.md`, `stack-defaults.md`, `soul.md`, and per-project
   DESIGN.md / PRODUCT.md.

Bring each mined item to the session as a confirm-or-correct question, not an open one.

## Question domains

Walk every domain; skip a question only when a recorded preference already decides it.

| Domain | What a captured preference must decide |
|---|---|
| Naming and structure | file layout, module boundaries, naming style at a fork |
| Dependency policy | when a new dependency is acceptable vs stdlib/hand-rolled |
| Testing depth | what a ticket's proof must cover; when a test is overkill |
| Error handling | fail loud vs degrade; what a user-facing error says |
| Docs style | what gets documented, where, in what register |
| Performance vs simplicity | which wins by default, and the threshold that flips it |
| Risk appetite | what makes a ticket "riskiest" (mid-flight review trigger) |
| Speed vs cost | parallelism defaults, model tier per role, spend comfort |
| Review strictness | what severity of finding warrants a repair flip |
| Creative direction (per project) | voice, visual register, audience, non-goals |
| Acceptance standards | what "shipped" means beyond the DoD checkboxes |

## Output contract

- Each answer becomes ONE preference line: `**{domain}:** {rule}` — decidable alone,
  no hedging, citable in a decision log. If it cannot decide a fork by itself, it is
  not captured yet — ask the follow-up.
- Operative home: `references/preferences.md` (vault defaults) or the project's own
  DESIGN.md / PRODUCT.md for per-project direction. The coordinator appends them.
- Record home: the full session — questions, answers, gaps closed — lands in Notion as
  a child page of the Control Plane: "Preference Grill — YYYY-MM-DD". Notion owns the
  record; the preference files own the operative contract.

## Stop condition

The gap list is empty, every domain is walked, or Stefano calls it. One session,
thorough — not a standing interrogation.
