---
name: goal-split
description: Turn a diagnosed backlog into parallel agent goals — ground in the logic map, extract every open decision BEFORE writing goals, mini-spec shared seams, partition work by FILE OWNERSHIP (never by feature), write zero-context goal docs, condense each into a paste-ready launch message, and hold the merge gate as reviewer. Use when dividing implementation across two or more agent sessions ("divide goals and specs accordingly", "split this between agents", "create goals for the agents", "one fable one opus"); when a repair wave or spec backlog is ready to execute and needs owners; when a previous parallel run hit merge conflicts or agents blocked on each other; or before launching any second concurrent session in the same repo. Consumes the logic map's mismatch ledger (logic-map) and findings docs; hands each goal to executing-plans/subagent-driven-development in the target session (Claude Code), or to Kanban cards via to-tickets (Hermes). Skip for single-agent work — one agent needs a plan, not a split.
---

# Goal Split

Parallel agents fail two ways: they collide (same file, merge conflict, clobbered work) or they
block (waiting on each other, on a decision, on the operator). Both are partition failures, not
agent failures. This skill produces partitions where collision is structurally impossible and
blocking is explicit, decided, or has a fallback.

**Core principle:** divide by FILE OWNERSHIP, never by feature. Features share files; files
don't share files. A goal is a set of files one agent owns absolutely, a mission those files
can deliver, and a done-line the reviewer can verify — in that order of design.

## Phase 1 — Ground

The backlog must already be diagnosed: a logic map with a mismatch ledger, findings docs with
evidence, or a spec with severities. If it isn't, stop and run `logic-map` /
`logic-first-debug` first — goals written from vibes inherit vibes. Every goal item must trace
to a finding id or an invariant, so the executing agent implements, never re-audits ("Diagnosis
is complete — implement, don't re-audit" belongs in every goal doc).

## Phase 2 — Decide before dividing

Sweep the backlog for every open decision — anything where two defensible options exist and
the choice is the owner's, not the implementer's. Present them as one batch with a
recommendation each ("say 'use your defaults' and nothing blocks"). Record the calls in the
decisions log BEFORE writing goals (the batch file's Decided section; lasting taste calls also go to docs/crew/decided.md).

A plan is not "too vague" because decisions are open; it is too vague only if vagueness sits
where WORK happens. Decision-points are the owner's to close, and an agent discovering an
undecided fork mid-flight either stalls or decides product questions it doesn't own — both
failure modes this phase exists to prevent. If a decision genuinely can't be made yet,
scope the fork OUT of both goals explicitly.

## Phase 3 — Mini-spec the shared seams

When several findings are symptoms of ONE unowned contract (three persistence bugs = one
"what does a saved record mean" question), patching them separately risks three inconsistent
answers. Write a one-page spec for that seam — invariants, design, done-means — and have one
goal implement it verbatim. Signs a seam needs this: findings in different files that all
answer the same question; a fix in one that would constrain the fix in another.

## Phase 4 — Partition by ownership

1. List every file each backlog item touches (grep, don't guess — the evidence rules apply).
2. Cluster items whose files overlap; clusters are indivisible — they go to the same goal.
3. Assign clusters to goals so that shared files across goals = **zero**, or at most ONE named
   file with **disjoint hunks** explicitly assigned ("A owns the board-refusal edit at the top
   of the handler; B owns the preflight hunk"). Two goals editing one function is not a
   partition, it's a queue.
4. Name every **cross-dependency** with a fallback: "A lands the field before B's task
   consumes it; B checks the log for it and uses <fallback> if absent." A dependency without a
   fallback is a block waiting to happen.
5. Balance by RISK, not size — the eval-gated experimental work and the mechanical batch are
   different kinds of load; give each goal a spine of certain work plus at most one
   experiment.
6. Decide territory: existing worktree reused, new branch off current base, or main checkout —
   and write down who merges first and that the LATER merger rebases (merges and commits need
   Stefano's explicit yes; on the studio board the lead integrates uncommitted diffs). With zero shared files
   the merge must be conflict-free; a conflict means ownership broke — stop and say so, don't
   resolve it silently.

## Phase 5 — Write the goal docs (zero-context)

One doc per goal, written into the repo (`docs/crew/`; committed only with Stefano's yes), for an
agent with NO chat history. On a Kanban board the card body is the goal doc (`to-tickets` template). The doc is
the authority; anything not in it does not exist for the executing agent. Structure:

```
# Goal <X> — <mission phrase> — <date>
Agent + where it works (worktree/branch/checkout) + counterpart goal by filename
Mission: one paragraph; "diagnosis is complete — implement" + pointer to findings ledger
Read-first list (specs, map sections, invariants)
## In scope, in order      — each item traces to finding ids; failing-test-first stated
## Explicitly NOT in scope — the other goal's domain, deferred decisions, banned reintroductions
## Owned files             — exhaustive; the other agent's list is untouchable
## Standing rules          — verbatim, every time: DB read-only / migrations written-and-handed-
                             over-never-run / spend rules / product invariants / suite-green +
                             tsc-clean every commit / failing test before each fix
## Done line               — verifiable by the reviewer without the agent's transcript
```

Handoff contract, stated in the doc: anything blocked on the operator goes at the TOP of the
handoff, never buried; an unmet done-item stays honestly unticked ("not faked") — an honest ⛔
is worth more than a false ✅, and the reviewer treats it as evidence of discipline, not
failure.

## Phase 6 — Condense to a launch message

Chat inputs have length limits and get skimmed. The paste message is a POINTER, not a copy (on a
Kanban board the launch is the `kanban_create` call, and the card body points at the batch file):

```
Execute Goal <X>: <repo path to the goal doc>
Read that file FIRST and follow it exactly — it is the authority; this message is only a summary.
Context docs: <3-4 paths>
Where you work: <one line>  |  counterpart + zero-shared-files warning
Mission, in order: <compressed numbered list>
Hard rules: <the standing rules, compressed but complete — safety rules never fall to compression>
Handoff: operator items at the TOP.
```

Target well under the limit (~1,800 chars is comfortable under 4,000). If summary and doc ever
disagree, the doc wins — say so in the message.

## Phase 7 — Hold the merge gate

The splitting session stays alive as REVIEWER. It does not implement; it verifies. At each
handoff:

1. Enumerate the agent's changes (commits, or the worktree diff) and diff the touched files against the owned-files list —
   ownership compliance is checked mechanically, not assumed.
2. Run the suites and typecheck on the agent's branch yourself.
3. Read the highest-risk hunks against the goal's invariants (the goal doc's done-line names
   them). Spot-verify any surprising claim in the handoff before accepting it.
4. Verify the cross-dependency landed in the order declared.
5. Perform or approve the merge per the Phase 4 protocol; re-run the suite on the merged
   result before calling it integrated.

## Red flags — the partition is about to fail

| Thought | Reality |
|---|---|
| "Split it by feature — generation vs grading" | Features share files. Two agents in one file is a merge conflict with extra steps. Cluster by files first, name the goals after. |
| "They can both touch that file, the edits are far apart" | Then name the hunks and assign them, or give the file to one goal. "Far apart" is how conflicts describe themselves before they happen. |
| "The agent can ask when it hits the decision" | Separate sessions can't ask you mid-flight reliably, and an agent deciding product questions is drift. Decide in Phase 2 or scope the fork out. |
| "The goal message can carry the whole plan" | Length limits truncate and summaries drift. The committed doc is the authority; the message is a pointer. |
| "B can start once A is done" | That's a queue, not a split. If the dependency chain is total, you wanted one agent with one plan. |
| "The handoff says done, merge it" | Enumerate commits, check ownership, run the suite, read the risky hunks. A handoff is a claim; the merge gate exists to test claims. |
| "Both goals need this standing rule, one copy is enough" | Each doc is read alone by an agent with no context. Safety rules are duplicated verbatim, every goal, every time. |
| "The seam findings are in different sections, split them" | If they answer one question, they get one spec and one owner — three consistent symptoms beat three inconsistent fixes. |

## Routing

| Situation | Skill |
|---|---|
| Backlog not yet diagnosed | `logic-map` / `logic-first-debug` / `mission-debug` first |
| One agent, multi-step work | `plan-forge` — a plan, not a split |
| Executing a received goal | `superpowers:executing-plans` / `subagent-driven-development` (Claude Code only); a Kanban worker on Hermes |
| Reviewing a handoff at the gate | `critic-pass` (Hermes: the reviewer's same-card review for cards marked Review: yes) |
| Same-session parallel subtasks | `superpowers:dispatching-parallel-agents` (Claude Code only) or `delegate_task` (Hermes) — this skill is for separate SESSIONS with separate contexts |
