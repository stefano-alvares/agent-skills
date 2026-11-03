# Scenario map: logic-map writes into Floorplan (lead: engineering-god)

## His words (verbatim)

> could you look at this skill: https://github.com/haydenschmitty/floorplan Its like my logic map but a bit
> different. My logic map is for the agents, this is for me to see. Can we find a middle ground that helps the
> agents plan out the apps but is also good for me? question me if you dont understand what i want

> Also to be used by the agents for debugging. the different things i want out of the app should be noted and
> made into flows. This is for all processes like in the studio too, not only for the app logic. Its basically
> to compare desired scenario output compared to what is actually implemented

> Really nice. go.

## Decided (clarify, 2 Nov 2026)

- When: both. He approves the plan on the map before building, and checks what changed after.
- The map shows: the rules each part guarantees, step-by-step flows of the main journeys, open questions and
  risks, what each card changed; agents use it for debugging; desired scenarios vs what is implemented.
- Gate: Atlas waits for his OK on the map for new apps and big features; small batches skip the map.
- Scope: everything (his apps, studio client sites, studio processes).
- Tool: Floorplan's viewer, with logic-map writing into it.

## Defaults (he can override any)

- Scenario and rule data lives in `docs/crew/scenarios.json` (tracked). Floorplan's `architecture.json`,
  `plan.json` and `descriptions/` are tracked too; generated files (`index.html`, `graph.json`, `.cache/`,
  servers) stay ignored. (He was asked; "go" did not answer it, so this is a default.)
- Floorplan is vendored at a pinned upstream tag with a reapplyable Hermes patch, git-ignored in ~/.agents
  like other third-party skills.
- Nothing Atlas loads changes until he says his current Atlas test is over.

## Definition of shipped

1. On a real app (revision-app, scratch copy), `scenarios check` runs every scenario's check and the map's
   Flows list shows met / not met / unverified per scenario.
2. A planted bug turns one scenario to not met, and the map plus `diagnose` locate the failing step.
3. The studio delivery process has its own scenario map with real measurements.
4. Drafts for logic-map, diagnose, crew-board, dev-build, studio-build and plan-forge are ready to switch, and
   team-skill-check passes after the switch.

## Plan

1. Vendor Floorplan (pinned tag) with the Hermes patch; install script reapplies it.
2. `~/.hermes/tools/scenarios/scenarios.mjs` (zero deps): validate, check, sync (into Floorplan files), report.
3. Pilot on a scratch copy of revision-app: code map by a Sonnet worker using the vendored skill; scenarios by
   me from its docs; check, sync, view; planted-bug debug test.
4. Studio process map from the 1 Nov spike, with team-stats as a real check.
5. Staged drafts of the skill changes; switch after his Atlas test; boot and planning check Atlas.

KILL-TEST: the riskiest assumption is that a scenario's check can be made runnable for most of what he wants.
If most checks end up "manual", the desired-vs-actual board is prose, and the map is only a picture.

## Pilot results (3 Nov 2026)

- revision-app (scratch copy): code map 333 files / 42 parts (Sonnet, about 10 min); 5 scenarios from README and
  the PRODUCT INVARIANT, all met, 237 offline tests, about 15 s; 7 rules (5 checked, all hold; 1 unowned); 2 open
  questions; 4 Floorplan health false positives verified and dismissed.
- Planted bug (dashboard route reads `timezone`, client sends `tz`): the `progress` scenario stayed met. Its check
  covered only the pure functions. Lesson built in: `validate` now names steps no probe or check crosses; logic-map
  requires checks that cross every boundary. Run before the bug, the warning names `api.progress`.
- A/B debug, one Sonnet run each, isolation verified in the transcripts: both found the root cause at
  route.ts:31. With the map: 5.5 min, 26 calls, went straight to 3 files and proposed the missing scenario check.
  Without: 7.8 min, 22 calls, and also found two more UTC bugs nearby (sparkline dates, DST loop). Anecdote, n=1:
  the map saved some time and focused the search; it did not make the debugger better.
