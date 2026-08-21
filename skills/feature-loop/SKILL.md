---
name: feature-loop
description: Use when Stefano asks to run one bounded feature through the Feature Loop pipeline, when a coordinator session must run or resume a tick against the Feature Loop Control Plane in Notion, or when a Feature row sits in any Feature Loop state awaiting a gate, execution, review, repair, or disposition. Read the full body before acting; the description does not describe the procedure.
disable-model-invocation: true
argument-hint: "Feature request and repository"
version: 0.8.0
created_by: agent
---

# Feature Loop v0.8

## North star

This system is built to succeed on its own — it has what it needs from Stefano up front,
and still uses him as a resource for what is genuinely his: creative direction, his ideas,
scope, spend, and irreversible calls. He is the controller, not a mid-flight crutch and
not a technical arbiter. A code-based decision he cannot fairly evaluate must never be
routed to him — the loop resolves it itself (preferences, then technical counsel). Every
agent gets the maximum capability to succeed: real context, empirical grounding, and a
return path for every situation it can land in. When the loop REQUIRES Stefano to catch
what an agent could have caught, that is a defect in the loop, not in Stefano. His
voluntary input is always welcome — it routes as ordinary findings, never as a bypass.

## Overview

Core principle: **sealed runway**. Stefano flips one Ship Spec gate; after the flip the coordinator refines the plan, projects tickets, executes, verifies, reviews, and logs decisions without returning routine work to him. He flips again only for irreversible or external actions — merge, install-target change, spend, publish. A spec may pre-authorize named reversible actions.

Two stores, no third. **Notion** owns control authority, operational tickets, and every document the loop produces. **Git** owns code, the digested spec file, immutable spec snapshots, and proof artifacts. Claude Code executor. No graph runtime.

**Doc centralisation — all means all.** Every document the loop produces — spec mirror, plan packet, review report, decision packets, retrospectives, grill outputs, counsel transcripts — lands in Notion as the feature row's page body or a child page of the Control Plane, the tick it is produced. Git keeps only the spec file (digested authority), code, and proof artifacts — where a proof artifact is strictly the output of a proof command referenced from a ticket's Evidence field; nothing else qualifies for the carve-out. At wave end the coordinator reconciles: every repo doc created during the wave is listed against its Notion page. The repo is the workbench; Notion is the record.

Before projecting or executing work, load `references/authority-boundary.md`.

## Store contract

Control Plane page: `3bfe90b1-9ba7-812b-9cba-d362956ba4e9` ("Feature Loop — Control Plane"). Three databases:

| DB | Data source | Properties |
|----|-------------|------------|
| Features | `5818292c-7974-49c7-bc7b-dcf74791bce2` | Name (title); State (select: Draft, DesignApproved, PlanProposed, ExecutionAuthorized, FeatureEvidenceReady, ReviewReported, ReviewInconclusive, AwaitingStefano, RepairAuthorized, ReadyToMerge, Merged, Released, Stopped, Cancelled); Contract Digest, Plan Digest, Authorisation Version, Repo, Branch, Worktree (text); Attempt Cap, Repair Cycles (number); Disposition (select: shipped, dry_stopped, cancelled); Tickets, Approvals (relations) |
| Tickets | `8c679b3c-c04b-4bc4-95b1-3a04b0957106` | Name (title); State (select: TicketApproved, TicketRunning, TicketCompleted, TicketBlockedForStefano, TicketStoppedRecoverable, TicketDryStopped); Feature (relation); Depends On / Unblocks (dual self-relation); Attempts, Attempt Cap (number); Wall Clock Cap, Plan SHA256, Idempotency Key, Envelope, Evidence (text) |
| Approvals | `3fb0e54f-0bec-4432-8444-563c4e9a587b` | Name (title); Artifact (select: Build Contract, Plan Packet, Repair Plan, Disposition); Feature (relation); Digest (text); Decision (select: Pending, Approved, Rejected, Revoked); Approved At (date); Notes (text) |

Legacy select values: this skill sets only the states its tick protocol names. "Build Contract" is the legacy artifact name of the Ship Spec approval; Plan Packet and Repair Plan pages are never created (plan approval was abolished in v0.5). Never set a state or artifact value no protocol step names.

## Skill routing

| Moment | Skill |
|--------|-------|
| Intake grill (live or async doc) | grilling |
| Producing/refreshing the project's logic map at intake | logic-map |
| Building the gate artifact (the spec) | ship-spec |
| Post-gate plan refinement | plan-forge |
| Splitting the wave goal into per-ticket goals | goal-split |
| Projecting the refined plan into the Tickets DB | to-tickets |
| Issue evaluation (same surface failing >2×) | raze-review + logic-first-debug |

## The one gate — Ship Spec

Intake and spec drafting run inside a tick — preflight (step 0) gates them like all other work. The gate is the point of least knowledge: Stefano decides before any work has tested the spec's claims. Two controls compensate.

**One grill session at intake.** Before drafting, run one thorough grill session (load the grilling skill) against Stefano's feature idea: intent, creative direction, non-goals, acceptance, and the facts the spec will rest on. One session, thorough, at the gate — it front-loads the controller's knowledge into the one artifact he approves, so nothing mid-flight needs him. Skip only if Stefano declines it for that feature.

**Every spec claim carries its probe.** A BLUF figure sampled from a subset states the sample size. A claim checkable by one command is checked before the spec is presented, not after the flip.

**Ground in the staple docs.** The spec cites the project's DESIGN.md, PRODUCT.md, and logic map. A project missing its logic map gets one at intake (logic-map skill) — the map is what lets every later agent understand the app's goals, not just its files. A new project's stack is an evaluated architecture decision recorded in Ground truth (what the app needs → what the stack provides), never an inherited default.

**Shipped is a transformation, not a test result.** Every DoD line states what changes in the app in feature/logic terms — what a user or system can do after that it could not before — with the probe as its evidence, never as its meaning. "Tests pass" is evidence, not a definition of shipped.

**Budget range.** The BLUF's Cost/risk line carries an estimated range, advisory only — cost never gates planning or implementation quality. Waste is prevented by issue evaluation (below), not ceilings.

**Pre-flip counsel.** While drafting, the coordinator may convene technical counsel on any technical claim it is unsure of — cheaper to argue before approval than after, and it removes the bias of handing counsel a bad base later.

Intake the feature and fill `templates/ship-spec.md`; the BLUF (≤8 lines) is required. Create ONE approval page (Artifact=Build Contract): its Digest field records the spec file's SHA-256, and its body carries the complete spec text as a mirror for Stefano's reading. The repo file is the digested authority. The mirror is the page body ABOVE the first `## Errata` heading, and it is advisory: a diverged mirror is repaired from the file and the repair logged — never executed from. The only equality that gates execution is file digest vs the approval page's Digest property.

**Pre-approval revision loop.** Stefano edits or comments → the coordinator revises the file → the same Pending page gets the new digest and a refreshed mirror. Post-approval change = new spec version + new flip.

**Errata path.** A defect found post-flip in the approved artifact is not a reinterpretation call and not automatically a re-flip. The coordinator writes a dated erratum — what was wrong, the evidence, the correction — appended under the `## Errata` heading on the approval page (the spec file and its digest stay untouched) and to the feature's decision log. The corrected reading governs where an erratum speaks. Three subtypes, nothing else:

- **Spec-fact erratum** — a wrong figure, wrong path, internal contradiction. Coordinator-authored; Stefano notified.
- **Amendment erratum** — a correction to a ticket's body, envelope, or proof, from an accepted `envelope-wrong` return, a critic finding, or a mid-flight-pass finding. May name at most one repair ticket per finding; that ticket is parity-legal.
- **Acceptance erratum** — a defect in a DoD or BLUF line (e.g. an unsatisfiable acceptance check). Stefano must ack before the affected path continues; other paths keep running. Never silent, never a full re-version for a one-line defect.

Every erratum notifies Stefano. Scope, spend, and authorization changes are never errata — those stay new spec version + new flip. A digest proves you are executing the approved document; only errata make it honest about being wrong.

**The errata path survives the feature's end.** A correction discovered after the feature is terminal lands the same way: erratum on the approval page. When the correction must also live in the spec file for future readers (a revision-log entry), the file edit is legal only WITH a same-tick erratum recording the file's new digest as a post-execution revision. An in-file "divergence is deliberate" note without the page erratum is the waiver-note failure mode — three real instances forced this rule.

**Founder override.** A mid-flight instruction from Stefano that changes the spec is a same-turn revision: edit the file, recompute the digest, refresh the mirror, he flips in the same exchange — he is present by definition. A waiver note instructing readers to ignore a fail-closed condition is itself a fail-closed condition.

**Digest binding.** Execution requires Decision=Approved AND digest equality, recomputed from the file at every tick against the approval page's Digest. The approval page is the digest authority; Feature row digests are mirrors, cross-checked but never governing. In-file "Status:" lines are non-authoritative — they sit inside the digested bytes.

**Decision fields.** The coordinator and every subagent never write a Decision field on a real approval page — only on FIXTURE-prefixed pages inside an approved spec's explicit test carve-out, archived when the test ends; Stefano alone flips everything else. The MCP connection writes as Stefano's own Notion user, so editor identity cannot prove authorship — the prohibition is procedural, proven by pre/post content snapshots of the Approvals database accompanying every coordinator Notion operation.

## After the flip

Plan refinement and projection run without human approval, bound by the spec's digest. Load plan-forge and refine the spec's task list into tickets: dependencies, envelopes, proof commands, attempt caps. Run a fresh internal critic against the refined plan, max 2 cycles.

**Every ticket gets a goal — goal-split, adapted.** Load goal-split at refinement and apply its discipline one level down: the wave goal (the spec's "What ships") splits into per-ticket goals. Each ticket carries a **Goal** — one line, zero-context, stating what this ticket changes in the app in feature/logic terms — and a **done-line** the coordinator can verify in behavior terms. Partition by FILE OWNERSHIP, never by feature: envelopes derive from the ownership partition (goal-split phase 4 — cluster by touched files, zero shared files across parallel tickets, cross-dependencies named with fallbacks). A ticket whose goal cannot be stated in one line is two tickets; a ticket whose goal restates its diff ("edit paper-type.ts") is not a goal. The worker's prompt LEADS with the goal — an agent that knows what the change is FOR recovers from surprises; an agent that only knows which lines to edit cannot.

**The critic must touch reality.** Document-only reasoning is the known failure mode, not self-authorship. The critic reproduces the plan's load-bearing claims empirically: runs the greps, reads the real inputs, does the arithmetic, times what a cap depends on. Any ticket claim checkable by one command gets that command run at authoring time. The critic's output is a claim→command→output ledger, landed on the feature's Notion page — a critic without a ledger has not run, and the final reviewer re-runs at least two ledger entries.

**Sequence doc-sync last.** A doc line quoting a number or a path is a claim that decays; mid-wave doc corrections get re-falsified by later tickets. All doc-sync work lands in one final ticket after every code ticket.

Then project the tickets one-for-one into the Tickets DB using `templates/ticket.md` — manual, coordinator-verified. Projection asserts at least one ticket flagged `riskiest`, or records why none qualifies. Parity is measured against the spec's task list as corrected by logged errata — an amendment erratum's named repair ticket is parity-legal; anything else extra is not. No follow-up, no cross-feature work.

**Ceremony scales to blast radius.** Light ticket test — all three or it is not light: zero behavior change, no authority-bearing file (scoring/marking rules, schemas, security, spend surfaces), rollback is a pure revert. A light ticket projects as envelope + one proof + evidence, minimal Notion round-trips. A light ticket that blocks or hits a fork upgrades to full ceremony on the spot. The `light` and `riskiest` flags live inside the ticket's Envelope text — no schema change.

## Decisions without gates

At every open fork, load `references/preferences.md`. Resolve by 1→3→1: state the fork, draft three options, choose by recorded preferences, then log options, choice, and deciding preference to the feature's Notion page. The park list — the forks nothing may resolve — lives in `references/preferences.md` alone; this file does not restate it.

**Technical counsel.** A code-based fork that recorded preferences do not decide AND that is not on the park list — never routes to Stefano: he cannot fairly evaluate it, and asking him is the loop failing its north star. Architecture-adjacent means reversible inside the envelope with no interface, dependency, or persistence change — anything past that line is Stefano's architecture authority. The coordinator launches one fresh Fable subagent (general-purpose, strongest model available) as counsel. Counsel sees the raw fork and gets repo access BEFORE seeing the coordinator's three options — framing is the known capture vector. Counsel must probe reality before opining, and its transcript must contain its own claim→command→output probe ledger. The debate runs under brutal-honesty on both sides. Argue to a decision, max 2 rounds; log fork, options, counsel's probes, choice. Unresolved after 2 rounds → park as a decision packet with the transcript attached, so Stefano rules on a fully-argued question, not a raw one. Cap: 3 counsel launches per wave; overflow parks.

**Model economics.** The coordinator need not be Fable — Stefano's session limits are real. The standing pattern: an Opus coordinator at high effort running frontier-gap, with Fable as counsel — Fable writes or blesses the plan and makes the final call on contested code decisions; the coordinator executes. Workers are tiered by ticket difficulty (session model by default, higher or lower per the ticket's goal); trivial coordinator tickets run inline. What never varies: counsel is the strongest model available, and evidence rules bind every tier equally.

**Envelope-wrong arbitration.** When the coordinator rejects a worker's `envelope-wrong` amendment twice, counsel arbitrates before anything parks: counsel and coordinator debate until they can state, in one line or one paragraph, what this implementation must do to the app — the ticket's goal, re-derived. The ruling follows from that statement. Still unresolved → park with the transcript.

**Preference capture.** When any fork gets resolved by counsel or parked because no recorded preference decided it, that is a preference gap. Log the gap; the next preference grill (see `references/preference-grill.md`) closes it.

## The tick

Every tick, in any session: load `references/tick-protocol.md` and follow it exactly. The tick starts at step 0 — the environment must prove itself (worker agent type + deny rules present) before any work; a preflight failure names the remediation. Summary: reconstruct state from Notion + Git — re-read the three databases, recompute the spec digest from the file, verify the approved git base. Never trust conversation memory.

Awaiting the gate is a noop tick: the /loop dynamic wakeup parks, ~30-minute spacing. A Pending or absent approval parks; it never advances the feature and never stops it — STOP is reserved for Rejected, Revoked, digest mismatch, or an unreadable store. A per-feature park budget (default 14 days) turns eternal waiting into a dry stop: State=Stopped, Disposition=dry_stopped, evidence preserved.

## Execution

At most one mutating worker per file. Tickets may run in parallel, each in its own worktree, only when their envelopes are disjoint across BOTH declared paths AND effect surfaces — lockfiles, generated files, caches, anything an allowed command can write. Any shared effect surface → serial. Set TicketRunning before launch; a TicketRunning row with no live worker in the session reconstructs as stopped-recoverable. Worktree output integrates onto the feature branch serially, coordinator-committed — the coordinator holds commit authority on the feature branch, nothing else — and proofs count only on the integrated state. Select only a ticket with State=TicketApproved whose every Depends On is TicketCompleted and Attempts < Attempt Cap. The worker: agent type `feature-loop-worker`, isolated git worktree, envelope prompt naming allowed paths, allowed commands, proof obligations, attempt context, stop conditions. A blocked ticket stops only its path; another already-approved ready ticket in the same feature may still run; otherwise consolidate one decision packet (`templates/decision-packet.md`) and park.

**The operator-batch wave.** A wave whose tickets are operator-gated batch operations — paid extraction runs, DB writes under a leased-writer rule — may be entirely coordinator-run: the spec declares it, worker isolation is N/A by that declaration, and containment is the substitute baseline plus serialized execution. A strictly linear coordinator wave may carry its execution order in Envelope text instead of Depends On relations; the order stays store-visible either way.

**Worker returns: done, blocked, envelope-wrong, stopped-recoverable.** A worker that can show its envelope, stop condition, or proof obligation is itself wrong — an impossible instruction, a proof broader than its finding, a stop condition a correct fix must breach — returns `envelope-wrong` with a proposed amendment and reasoning. Access it NEEDS but was not granted is envelope-wrong; access it TAKES is a fail-closed violation. The coordinator logs the return verbatim on the ticket row, then rules: accept → amendment erratum, amend, relaunch; reject → the worker complies or blocks. An accepted amendment that narrows a proof obligation states what the narrowed proof no longer covers, and the final reviewer receives the full amendment list as frozen context. A correct worker never has to choose between violating its envelope and stalling — and the coordinator never silently amends a ticket a worker flagged nothing about.

## Evidence gate

The coordinator independently runs or inspects the ticket's named proof before setting TicketCompleted. Worker confidence alone advances nothing. Record proof output in the ticket's Evidence field. Completion also checks the diff against the ticket's envelope in both directions — every named deliverable present, nothing outside it. The proof answers "does it work"; the envelope check answers "is it all there" — a green proof with a missing named deliverable is an incomplete ticket, not a done one.

**The absence law.** An absence-based claim — "no matches", "zero failures", "nothing refused", "no_issue_found" — needs proof the measurement happened. "None found" cannot on its own distinguish *nothing matched* from *nothing was searched*. Known instances, all hit in real runs:

- A file with a NUL byte makes grep skip it silently; the audit reads "clean" having read nothing. Use `grep -a` where binary skip is possible.
- An exit code read through a pipe (`cmd | tail; echo $?`) reports the pipe's tail, not the command. Never read `$?` through a pipe.
- A fan-out score of "0 findings survived" when all refuters crashed. Verdicts returned must equal items submitted, or the result is UNRESOLVED — never clean.

Every negative result runs beside a positive control: a variant that must match or fail, proving the instrument works. A proof must show it ran — exit code and output; the positive control is the only acceptable explanation for an empty result.

**Retries re-diagnose.** A failed attempt with attempts remaining does not retry the same approach by default. The retry states the diagnosed cause — what was wrong — and what this attempt changes to address it; "attempt 1 failed" is not a diagnosis. If nothing changed, apply the cap route early.

**Issue evaluation — the losing-horse rule.** The same surface failing more than twice (across attempts, repairs, or waves) triggers a diagnosis before any further work or any packet: raze-review + logic-first-debug answer one question — is this wrong at the core and due a scrap-and-rebuild, or worth fixing? The resulting decision packet leads with that verdict and its evidence. Scrapping is always Stefano's call — and the packet recommends rebuild when the evidence says so, without the model's hesitation to "waste" sunk work. Cost never decides this; the diagnosis does.

**The suite is living.** A behavior change that breaks an existing test is a flag, not an obstacle: the ticket updates or removes the test to match the spec'd behavior — inside its envelope, logged in Evidence — or returns `envelope-wrong` if the tests are outside it. Never write around a stale test, never keep a red test as tribute, never mass-generate tests to bury one. An old test asserting the behavior the spec ordered removed is the defect.

## Review and decision log

Three review moments, none skippable. (1) The empirical pre-projection critic (above) catches plan defects with zero code written — the cheapest point. (2) When the FIRST riskiest ticket lands (the spec flags them; default: any ticket touching a public interface, authority-bearing logic such as scoring or marking rules, or persistence), run one mid-flight adversarial pass — a finding becomes an amendment erratum plus at most one repair ticket, pre-commit cost; post-commit the same finding costs a spec version and a flip. (3) After all tickets: a fresh read-only reviewer, root context frozen before code access — it receives the critic's probe ledger (re-runs at least two entries), the full errata and amendment list, and the decision log, and cross-checks the riskiest tickets' diffs against the logged forks. It reviews against the tickets' GOALS, not just their diffs — did the wave deliver the transformations the DoD names? Verdict: no_issue_found / issue_reported / inconclusive (`templates/review-report.md`) — under the absence law, a no_issue_found verdict must prove its refuters actually ran. An issue_reported verdict gets a second-agent cross-exam (counsel, brutal-honesty both sides) before it enters the decision packet — the double-agent evaluation. Findings create no repair authority. Assemble the decision packet. Routine features end here: State=ReviewReported, terminal — no flip, unless the spec names an irreversible action.

## Irreversible actions

When merge, install, or stop choices arise, the five-way disposition template (`templates/disposition.md`) still governs: repair / accept / install / merge / stop — each a separate explicit Stefano decision. Repair requires a new spec version + new flip. Merge, install-target change, spend, and publish are Stefano-only and NEVER pre-authorizable — a spec's pre-authorization clause covers only other named reversible actions. Silence grants nothing.

**Deferred-cost actions gate as irreversible.** An action that is cheap at the moment but whose reversal cost lands later — a write that a version bump must invalidate, records a paid run must redo — is irreversible-class. The test is the cost of undoing, not the cost of doing. The spec's Cost/risk line names any deferred costs it knows about.

## Fail-closed conditions

STOP the affected path, notify, never guess, when: digest mismatch against the approval page (the digest authority); approval Rejected or Revoked; Notion unreadable; a ticket outside parity (task list + logged errata); changed manifest; out-of-envelope snapshot delta or out-of-envelope access taken; attempt or wall-clock cap exhausted; proof incomplete; a waiver note telling readers to ignore a fail-closed condition. A stopped path authorizes no new work. (A diverged mirror is repaired and logged, not fail-closed — the mirror is advisory.)

## Honest limits

Worker isolation is not a hard boundary. Workers of type `feature-loop-worker` have no MCP tools; Bash deny rules block the known Notion vectors (ntn CLI, api.notion.com, credential files); but deny rules are best-effort pattern matching. Isolation = deny rules + permission classifier + pre/post snapshot detection, together. An out-of-envelope delta in the pre/post snapshots invalidates the run. This is not a sandbox.

**Containment coverage depends on the wave's character.** Git-based snapshots and worktree isolation see only what git tracks. A wave that mutates git-excluded data — a corpus, generated assets, anything ignored — gets zero coverage from them: the worktree materializes none of it and `git status` is blind to it. The spec must declare which controls the wave's character disables and name the substitute baseline (file inventory + checksums of the affected tree, taken pre and post) before the flip. A wave that skips the declaration is claiming coverage it does not have.

In unattended mode the Decision-write prohibition has no prompt friction — nothing in the permission layer blocks it; it is procedural only, enforced by the pre/post Approvals snapshots. The permission classifier does block coordinator Decision=Approved writes even on FIXTURE pages — Stefano flips fixtures himself; the asymmetry is safety-positive.

## Recovery

A fresh session loses nothing. State reconstructs from Notion + Git: re-read the three databases, recompute the spec digest, verify the git base, resume at the tick protocol.
