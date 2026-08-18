---
name: feature-loop
description: Use when Stefano asks to run one bounded feature through the Feature Loop v0.5 pipeline, when a coordinator session must run or resume a tick against the Feature Loop Control Plane in Notion, or when a Feature row sits in any Feature Loop state awaiting a gate, execution, review, repair, or disposition. Read the full body before acting; the description does not describe the procedure.
disable-model-invocation: true
argument-hint: "Feature request and repository"
version: 0.5.0
created_by: agent
---

# Feature Loop v0.5

## Overview

Core principle: **sealed runway**. Stefano flips one Ship Spec gate; after the flip the coordinator refines the plan, projects tickets, executes, verifies, reviews, and logs decisions without returning routine work to him. He flips again only for irreversible or external actions — merge, install-target change, spend, publish. A spec may pre-authorize named reversible actions.

Two stores, no third. **Notion** owns control authority and operational tickets. **Git** owns code, immutable spec snapshots, and proof. Serial, Claude Code executor. No graph runtime.

Before projecting or executing work, load `references/authority-boundary.md`.

## Store contract

Control Plane page: `3bfe90b1-9ba7-812b-9cba-d362956ba4e9` ("Feature Loop — Control Plane"). Three databases:

| DB | Data source | Properties |
|----|-------------|------------|
| Features | `5818292c-7974-49c7-bc7b-dcf74791bce2` | Name (title); State (select: Draft, DesignApproved, PlanProposed, ExecutionAuthorized, FeatureEvidenceReady, ReviewReported, ReviewInconclusive, AwaitingStefano, RepairAuthorized, ReadyToMerge, Merged, Released, Stopped, Cancelled); Contract Digest, Plan Digest, Authorisation Version, Repo, Branch, Worktree (text); Attempt Cap, Repair Cycles (number); Disposition (select: shipped, dry_stopped, cancelled); Tickets, Approvals (relations) |
| Tickets | `8c679b3c-c04b-4bc4-95b1-3a04b0957106` | Name (title); State (select: TicketApproved, TicketRunning, TicketCompleted, TicketBlockedForStefano, TicketStoppedRecoverable, TicketDryStopped); Feature (relation); Depends On / Unblocks (dual self-relation); Attempts, Attempt Cap (number); Wall Clock Cap, Plan SHA256, Idempotency Key, Envelope, Evidence (text) |
| Approvals | `3fb0e54f-0bec-4432-8444-563c4e9a587b` | Name (title); Artifact (select: Build Contract, Plan Packet, Repair Plan, Disposition); Feature (relation); Digest (text); Decision (select: Pending, Approved, Rejected, Revoked); Approved At (date); Notes (text) |

## Skill routing

| Moment | Skill |
|--------|-------|
| Building the gate artifact (the spec) | ship-spec |
| Post-gate plan refinement | plan-forge |
| Projecting the refined plan into the Tickets DB | to-tickets |

## The one gate — Ship Spec

Intake and spec drafting run inside a tick — preflight (step 0) gates them like all other work. Intake the feature and fill `templates/ship-spec.md`; the BLUF (≤8 lines) is required. Create ONE approval page (Artifact=Build Contract): its Digest field records the spec file's SHA-256, and its body carries the complete spec text as a mirror. The repo file is the digested authority; the page body is a mirror. Mirror-vs-file divergence at any tick = STOP.

**Pre-approval revision loop.** Stefano edits or comments → the coordinator revises the file → the same Pending page gets the new digest and a refreshed mirror. Post-approval change = new spec version + new flip.

**Digest binding.** Execution requires Decision=Approved AND digest equality, recomputed from the file at every tick against the approval page's Digest. The approval page is the digest authority; Feature row digests are mirrors, cross-checked but never governing. In-file "Status:" lines are non-authoritative — they sit inside the digested bytes.

**Decision fields.** The coordinator and every subagent never write a Decision field on a real approval page — only on FIXTURE-prefixed pages inside an approved spec's explicit test carve-out, archived when the test ends; Stefano alone flips everything else. The MCP connection writes as Stefano's own Notion user, so editor identity cannot prove authorship — the prohibition is procedural, proven by pre/post content snapshots of the Approvals database accompanying every coordinator Notion operation.

## After the flip

Plan refinement and projection run without human approval, bound by the spec's digest. Load plan-forge and refine the spec's task list into tickets: dependencies, envelopes, proof commands, attempt caps. Run a fresh internal critic against the refined plan, max 2 cycles. Then project the tickets one-for-one into the Tickets DB using `templates/ticket.md` — manual, coordinator-verified. No extra ticket, no follow-up, no cross-feature work.

## Decisions without gates

At every open fork, load `references/preferences.md`. Resolve by 1→3→1: state the fork, draft three options, choose by recorded preferences, then log options, choice, and deciding preference to the feature's Notion page. Park only irreversible, scope-changing, spend, or security forks.

## The tick

Every tick, in any session: load `references/tick-protocol.md` and follow it exactly. The tick starts at step 0 — the environment must prove itself (worker agent type + deny rules present) before any work; a preflight failure names the remediation. Summary: reconstruct state from Notion + Git — re-read the three databases, recompute the spec digest from the file, verify the approved git base. Never trust conversation memory.

Awaiting the gate is a noop tick: the /loop dynamic wakeup parks, ~30-minute spacing. A Pending or absent approval parks; it never advances the feature and never stops it — STOP is reserved for Rejected, Revoked, digest mismatch, or an unreadable store. A per-feature park budget (default 14 days) turns eternal waiting into a dry stop: State=Stopped, Disposition=dry_stopped, evidence preserved.

## Serial execution

At most one mutating worker at any time. No exceptions. Select only a ticket with State=TicketApproved whose every Depends On is TicketCompleted and Attempts < Attempt Cap. The worker: agent type `feature-loop-worker`, isolated git worktree, envelope prompt naming allowed paths, allowed commands, proof obligations, attempt context, stop conditions. A blocked ticket stops only its path; another already-approved ready ticket in the same feature may still run; otherwise consolidate one decision packet (`templates/decision-packet.md`) and park.

## Evidence gate

The coordinator independently runs or inspects the ticket's named proof before setting TicketCompleted. Worker confidence alone advances nothing. Record proof output in the ticket's Evidence field.

## Review and decision log

After all tickets: launch a fresh read-only reviewer, root context frozen before code access. Verdict: no_issue_found / issue_reported / inconclusive (`templates/review-report.md`). Findings create no repair authority. Assemble the decision packet and confirm every 1→3→1 resolution sits in the feature's decision log. Routine features end here — review + decision log, no flip — unless the spec says otherwise.

## Irreversible actions

When merge, install, or stop choices arise, the five-way disposition template (`templates/disposition.md`) still governs: repair / accept / install / merge / stop — each a separate explicit Stefano decision. Repair requires a new spec version + new flip. Merge, install-target change, spend, publish: Stefano only, unless the spec pre-authorizes a named reversible action. Silence grants nothing.

## Fail-closed conditions

STOP the affected path, notify, never guess, when: digest mismatch against the approval page (the digest authority); mirror-vs-file or mirror-vs-page divergence; approval Rejected or Revoked; Notion unreadable; unknown, extra, or missing ticket; changed manifest; out-of-envelope snapshot delta; attempt or wall-clock cap exhausted; proof incomplete. A stopped path authorizes no new work.

## Honest limits

Worker isolation is not a hard boundary. Workers of type `feature-loop-worker` have no MCP tools; Bash deny rules block the known Notion vectors (ntn CLI, api.notion.com, credential files); but deny rules are best-effort pattern matching. Isolation = deny rules + permission classifier + pre/post snapshot detection, together. An out-of-envelope delta in the pre/post snapshots invalidates the run. This is not a sandbox.

In unattended mode the Decision-write prohibition has no prompt friction — nothing in the permission layer blocks it; it is procedural only, enforced by the pre/post Approvals snapshots. The permission classifier does block coordinator Decision=Approved writes even on FIXTURE pages — Stefano flips fixtures himself; the asymmetry is safety-positive.

## Recovery

A fresh session loses nothing. State reconstructs from Notion + Git: re-read the three databases, recompute the spec digest, verify the git base, resume at the tick protocol.
