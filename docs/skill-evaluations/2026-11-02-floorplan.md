# Skill intake: floorplan

- Source: https://github.com/haydenschmitty/floorplan (Hayden Smith, MIT, v0.1.5, created 27 Oct 2026)
- Evaluated: 2026-11-02
- Verdict: Adapt
- Score: 8/12

## Claim and mechanism

Claim: an interactive, plain-English map of an app (parts, files, screens, endpoints, connections, outside
services, flows), or a "blueprint" of an app planned from a PRD before code exists.

Mechanism: plain Node scripts (zero dependencies) scan imports and match HTTP calls to routes; the agent
writes `architecture.json` (parts, flows, tour) and, for a blueprint, `plan.json` (planned files,
endpoints, access, assumptions, open questions). `build.mjs` renders a self-contained `floorplan/index.html`.
The design review lists open questions, endpoints with no access rule, open endpoints that change data,
and orphans. The Ask bar needs the Claude Code (or Codex) CLI.

## Evidence and unknowns

- Ran `scan.mjs` on a scratch copy of revision-app: 2.5 s, 731 import links, 25 routes, 21 call-to-route
  matches; wrote only its self-ignoring `floorplan/` folder; git stayed clean.
- Spike: drew the studio delivery process (no code) as a blueprint with three desired scenarios as flows
  (expected, measured, status in each flow's description), rules in each part's details and two open
  questions. `plan.mjs` and `build.mjs` passed; the Flows list shows expected vs measured per scenario;
  the design review shows the questions. Screens: engineering-god scratch `fp-shots/`.
- Flow steps must be a node id or a file path, not an endpoint.
- UNVERIFIED: token cost of the describe pass on a real code map (it names every file); behaviour of the
  Ask/Change bar; upstream stability (six days old, single author; it has tests and CI).

## Fit score

| Dimension | Score | Evidence |
|---|---:|---|
| Problem fit | 2 | Stefano wants to see and approve the plan, compare desired scenarios with what is built, and have agents debug against it (2 Nov 2026). |
| System fit | 1 | File-based and repo-local, but written for Claude Code: `${CLAUDE_SKILL_DIR}` (Hermes uses `${HERMES_SKILL_DIR}`), `!` context injection, and it edits `CLAUDE.local.md` and `.git/info/exclude`. Ignores its whole folder, so the scenarios would not be versioned. |
| Distinctness | 2 | logic-map has the rules and chains but no viewer and no planned-file/endpoint structure; nothing else in the library draws a map. |
| Reliability | 1 | Inspectable source, tests, CI; scan and blueprint verified here; very young upstream. |
| Cost and permissions | 1 | Local only, no network, no deps; a full code map spends tokens on every file. |
| Maintenance | 1 | Our Hermes adaptation must be re-applied on upstream updates. |

## Existing overlap

`logic-map` (invariants, owners, causal chains, attacks: the part that prevents bugs). Floorplan has none
of that; logic-map has no picture. They complement each other.

## Disproof test

Pilot on one real app after the current Atlas test: map revision-app's two promise-carrying scenarios,
then plant one broken step and check that an agent using `diagnose` finds the first failing step from the
map faster than without it. If the map adds no speed or Stefano does not use it to approve plans, drop it.

## Decision

Adapt: install Floorplan as a vendored skill with the Hermes path fix; keep logic-map as the method and
make it write its map into Floorplan's files (rules on parts, scenarios as flows with expected, check,
measured and status, unowned rules as open questions). Atlas waits for Stefano's OK on the map for new
apps and big features. Applies to studio processes too.

## Smallest next action

Build the adapted logic-map and the Floorplan vendor copy as drafts, pilot on revision-app, and switch the
live skills only after Stefano's current Atlas test ends.
