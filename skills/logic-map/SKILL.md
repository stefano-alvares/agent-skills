---
name: logic-map
description: "Use when starting an app, a big feature or a process and the design should be right before the work; when Stefano wants to see or approve a plan; or when comparing what he wants with what is built. Maps his wanted outcomes into scenarios (flows with a check), the rules each part must guarantee and who owns each, then draws them on a Floorplan map he can read. Also for debugging against the scenarios, checking a spec against drifted code, onboarding, or 'map the logic' / 'what are the systems here'. Run before plan-forge. Skip for a single-file change with no new rule."
---

# Logic Map

Code is the cheapest part of a system and the most replaceable. Logic is neither. Design the claims the
system must guarantee and who owns each one; any code that honours them is correct and can be rewritten.

A map states what must be true regardless of order; `plan-forge` sequences the work. Run this first so the
plan builds the right thing.

This skill has two readers. The agents read `docs/crew/scenarios.json`. Stefano reads the same content
drawn on a Floorplan map (`floorplan` skill): every part with the rules it guarantees, every scenario as a
flow with its expected result, its check and the last measured result, and every hole in the design as
an item under Review. One source, two views.

## Where it lives

| What | Where | Tracked |
|---|---|---|
| Scenarios, rules, open questions | `docs/crew/scenarios.json` | yes |
| Parts, names, descriptions (Floorplan) | `floorplan/architecture.json`, `plan.json`, `descriptions/` | yes |
| The drawn map | `floorplan/index.html`, `graph.json` | no (generated) |

For a studio process (no repo), the root is `~/.agents/maps/<process>/`. Format and fields:
`references/scenarios-format.md`. Commands: `node ~/.hermes/tools/scenarios/scenarios.mjs
<validate|check|set|sync|report> <root>`.

**No scenarios tool on this machine** (it lives in `~/.hermes/tools/scenarios/`, not in this repo, so a
cloud session or another machine may not have it): keep the same `scenarios.json` by hand. Validate by
reading it against `references/scenarios-format.md` (every rule one owner or an empty owner, every step a
node). Check by running each scenario's `check.run` yourself: exit 0 met, 3 could not measure, anything
else not met; this is the one case where you write `status` and `measured` by hand, with the date and the
output line that decided it. Skip `sync` and the drawn map: show him the Flows as a table in the reply
(id, want, status, failing step) and say the map was not drawn. Never mark a scenario met on a check you
did not run.

## Phase 1: Harvest what he wants

Sources, newest decision wins: the batch file's Decided section and `docs/crew/decided.md`, the batch
scope, the spec, `CLAUDE.md` or `AGENTS.md` product rules, the product docs. For existing code, also the
tests: a test is a rule someone cared enough to freeze.

Write two kinds of thing:

- **Scenarios**: outcomes he wants, in his words (`want`), with the observable result (`expected`). "I
  pick a topic and get fresh questions, marked straight away" is a scenario. Map the 3 to 6 that carry
  the product's promise, not every feature.
- **Rules**: statements that must hold after any operation. "A question is never shown without a source
  chunk attached" is a rule; "the app shows questions" is a feature and cannot guide a design.

A promise that exists only in someone's head is the most valuable output: write it down and flag it.

## Phase 2: Name the parts and give each one a box

The parts are Floorplan nodes (`architecture.json`): stable, short, dotted ids, because scenarios point at
them. For each part, know its box:

```
<part> | takes: <input + its rule> | gives: <output + its rule> | owns: <rules> | fails: throws, degrades or silent
```

Put the takes/gives/fails line in the node's `summary` or `details` in plain words. Ownership goes in
`scenarios.json`: each rule's `owner` is one node id.

- **Every rule has exactly one owner.** Two owners means two places to disagree. No owner means the rule
  is aspirational: leave `owner` empty and the map shows "Nothing guarantees: ..." under Review.
- **The owner is the narrowest part that can enforce it.** A database constraint beats a service check,
  which beats a component check. Set `enforced_in` to the file where it is enforced.
- For existing code the fails column is read, never assumed: grep finds consumers, only their catch
  blocks classify them.

## Phase 3: Write each scenario as a chain

Each scenario's `steps` are the causal chain, 4 to 10 links, each on the part that owns it:

```json
{ "node": "lib.coverage", "note": "Counts the real past-paper examples for the topic and type",
  "because": "below the floor the request is refused", "rule": "r-no-fake-coverage",
  "probe": "npx tsx --test src/lib/as-coverage.test.ts" }
```

A link no part owns is a design gap found on paper. `probe` is optional: a cheap command that proves this
link holds. When the scenario's check fails, the probes run in order and the first failing one is
recorded as the step where it breaks.

## Phase 4: Give every scenario a check

The check is what turns the map into desired against actual:

- **Runnable** (preferred): a test or command. Exit 0 = met; any other exit = not met; exit 3 = could not
  measure (no data yet). Use the project's offline tests where they exist; write a narrow one where they
  do not. Never a check that needs secrets or changes live data.
- **By hand**: `{"manual": "<what to look at>"}`, recorded with `scenarios.mjs set <root> <id> met
  --evidence "<what was observed>"`. A map where most checks are by hand is a picture, not a board: say
  so in the report.

**The check must cross every boundary in the chain.** A scenario checked only through its pure functions
can say met while the link between the screen and the server is broken (pilot, 3 Nov 2026: a renamed query
parameter stayed "met"). Prefer one check that drives the scenario through its entry point (the route
handler with I/O stubbed, the CLI command, the page), and give each step that the check does not cross a
`probe`. `validate` names the steps nothing covers; treat that warning as a gap, not noise. Steps on an
outside service (`"external": true`) are exempt.

Rules can carry a check too; a failing one shows "Rule broken" under Review.

## Phase 5: Attack the map before it becomes code

1. **Violation test:** can any part break a rule without another noticing? Move the rule to a boundary
   where breaking it is impossible: a type, a schema constraint, one chokepoint.
2. **Gap test:** for each step, what if its precondition fails? Empty input, a second concurrent call, a
   retry after partial failure, the dependency down. A scenario with only the happy path is half a design.
3. **Domain test:** for each input, walk every value class (every enum member, null, absent, the legacy
   row), not just the typical one.
4. **Mismatch test** (existing code): run the checks. Every not-met scenario or broken rule is exactly one
   of: an undocumented decision, a bug or vapour, or two owners. Name which.

Holes become `questions` (with the node ids they touch) or empty owners; they show under Review on the
map. A worked example of the invariants and the mismatch table (written before the scenario format,
so its output shape is older): `references/worked-example.md`.

## Evidence rules

1. Artifact claims are read, not remembered. Open the file before citing it; mark anything unverified
   `assumed`.
2. Cross-artifact claims require reading both artifacts.
3. A shared-contract change sweeps the whole compile scope (`tsconfig` include), tests and scripts too.

## Phase 6: Choose the decomposition

When more than one split is plausible, compare in this order: rules made impossible to violate; number
of boundaries where two assumptions meet; blast radius of the most likely change; only then familiarity
and taste. Record rejected splits with one-line reasons in the batch file.

## When it runs, and what Stefano sees

- **Before building** (new app, new process, big feature): make a Floorplan **blueprint** from the brief
  (`floorplan` skill, blueprint path; in Claude Code read `~/.agents/skills/floorplan/SKILL.md`
  directly, since the skill is vendored for Hermes), write `scenarios.json` with every scenario at status `planned`,
  `validate`, `sync`, and open the map for him: `node ~/.agents/skills/floorplan/scripts/open.mjs
  <root>` (local), or attach a screenshot of the Flows list and Review. **Wait for his OK** on the map
  before building: this is the one approval gate he chose for planning (2 Nov 2026). Big means a new app,
  site or process; work touching checkout, payments, auth, personal data, a database or 8+ code files;
  or a new user-facing flow across 2 or more parts. It runs after `ship-spec` and before `plan-forge`. Everything else (quick and light work inside existing flows) skips the map.
- **After building** (every round that touched a mapped area): refresh the map from code (`refresh.mjs`,
  or `--from-code` for the first build from a blueprint), mark recent work (`recent.mjs` and
  `recent-work.json`, one task per thing he asked for), then `check` and `sync`. Paste the `report` table
  into the round report: scenarios met, not met, unchecked.
- **Debugging**: `diagnose` starts from the not-met scenario: its `want` is the desired output, its
  steps are the chain, the first failing step is the first bracket.

After every change to `scenarios.json` or the map: `validate`, then `sync`. Commit `scenarios.json` and
the Floorplan sources on the crew branch.

## Budgets

Per-section expected shape (files, LOC ceiling, dependencies allowed), derived from the decomposition,
never from existing code. Write them into the batch file's Decided section; `raze-review` judges against
them. One line per part, so raze-review can read it without interpretation:

```
Budgets (<date>, his OK: yes | proposed):
- <node id>: ~<n> files, <= <n> LOC per file, deps: none new | <named package and why>
```

## Routing

| Situation | Skill |
|---|---|
| What should this guarantee, who owns it, what does he want | **this one** |
| Draw or refresh the picture | `floorplan` |
| In what order to build it | `plan-forge` |
| Did the build honour the map | `raze-review`, plus `scenarios.mjs check` |
| Something is broken | `diagnose`, starting from the scenario |
| The product behaves wrongly but nothing is broken | `mission-debug` |

## Red flags

| Thought | Reality |
|---|---|
| "The parts are just the folders" | Then you mapped the implementation. Ask what each guarantees. |
| "This rule is obvious" | Unwritten rules have no owner, and unowned rules are false. |
| "We'll handle that edge in the code" | If a part can break a rule, it eventually will. Move the rule. |
| "Map every feature" | A map of everything is a transcription. Map the promise-carrying scenarios. |
| "The check is hard, I'll mark it by hand" | Then the board is prose. Write the narrow test. |
| "Code and spec disagree, update the spec" | Classify it first: undocumented decision, bug, or two owners. |
| "I'll write the map after building" | Then it records what was done, not what is correct, and can never disagree with the code. |
| "Status says met" | Only if the check ran on the current code and crosses every step. Re-run `check` after every round. |
