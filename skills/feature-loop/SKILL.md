---
name: feature-loop
description: Use when Stefano asks to run one bounded feature through the Feature Loop v0.4 pipeline, when a coordinator session must run or resume a tick against the Feature Loop Control Plane in Notion, or when a Feature row sits in any Feature Loop state awaiting a gate, execution, review, repair, or disposition. Read the full body before acting; the description does not describe the procedure.
disable-model-invocation: true
argument-hint: "Feature request and repository"
version: 0.4.0
created_by: agent
---

# Feature Loop v0.4

## Overview

Core principle: **sealed runway**. Stefano approves the Build Contract (Gate 1) and the complete Plan Packet (Gate 2); the coordinator then manages the feature to disposition without returning routine ticket management to him. His total touches per feature: approve Gate 1, approve Gate 2, choose final disposition — all possible from his phone via Notion.

Two stores, no third. **Notion** owns control authority and operational tickets. **Git** owns code, immutable plan snapshots, and proof. Serial, human-gated, Claude Code executor. No graph runtime.

Before projecting or executing work, load `references/authority-boundary.md`.

## Store contract

Control Plane page: `3bfe90b1-9ba7-812b-9cba-d362956ba4e9` ("Feature Loop v0.4 — Control Plane"). Three databases:

| DB | Data source | Properties |
|----|-------------|------------|
| Features | `5818292c-7974-49c7-bc7b-dcf74791bce2` | Name (title); State (select: Draft, DesignApproved, PlanProposed, ExecutionAuthorized, FeatureEvidenceReady, ReviewReported, ReviewInconclusive, AwaitingStefano, RepairAuthorized, ReadyToMerge, Merged, Released, Stopped, Cancelled); Contract Digest, Plan Digest, Authorisation Version, Repo, Branch, Worktree (text); Attempt Cap, Repair Cycles (number); Disposition (select: shipped, dry_stopped, cancelled); Tickets, Approvals (relations) |
| Tickets | `8c679b3c-c04b-4bc4-95b1-3a04b0957106` | Name (title); State (select: TicketApproved, TicketRunning, TicketCompleted, TicketBlockedForStefano, TicketStoppedRecoverable, TicketDryStopped); Feature (relation); Depends On / Unblocks (dual self-relation); Attempts, Attempt Cap (number); Wall Clock Cap, Plan SHA256, Idempotency Key, Envelope, Evidence (text) |
| Approvals | `3fb0e54f-0bec-4432-8444-563c4e9a587b` | Name (title); Artifact (select: Build Contract, Plan Packet, Repair Plan, Disposition); Feature (relation); Digest (text); Decision (select: Pending, Approved, Rejected, Revoked); Approved At (date); Notes (text) |

## Skill routing

| Moment | Skill |
|--------|-------|
| Consolidating existing findings into the contract | ship-spec |
| Building the Plan Packet | plan-forge |
| Projecting the approved plan into the Tickets DB | to-tickets |

## The two gates

**Gate 1 — Build Contract.** Intake the feature. If consolidating existing findings, load ship-spec; else draft directly. Fill `templates/build-contract.md`. Create a Gate 1 approval page (Artifact=Build Contract) recording the SHA-256 of the exact contract file.

**Gate 2 — Plan Packet.** Load plan-forge. Fill `templates/plan-approval.md`: every ticket, dependency, envelope, proof command, attempt cap. Run a fresh critic against the packet, max 2 cycles. Create the Gate 2 approval page (Artifact=Plan Packet) with the packet file's SHA-256.

**Digest binding.** Execution requires Decision=Approved AND digest equality, recomputed from the file at every tick. In-file "Status:" lines are non-authoritative — they sit inside the digested bytes; the Notion approval record governs.

**Decision fields.** The coordinator and every subagent it launches never write a Decision field on any real approval page. No exceptions. Stefano alone flips Decision. The MCP connection writes as Stefano's own Notion user, so editor identity cannot prove authorship — the prohibition is procedural, proven by pre/post content snapshots of the Approvals database accompanying every coordinator Notion operation. Sole exception: fixture pages whose Name begins with "FIXTURE — ", related only to a fixture feature row inside an approved plan's explicit gate-test carve-out; archive them when the test ends.

## Projection

After Gate 2 approval, project the approved plan's tickets one-for-one into the Tickets DB using `templates/ticket.md`. Manual, coordinator-verified. No extra ticket, no follow-up, no cross-feature work.

## The tick

Every tick, in any session: load `references/tick-protocol.md` and follow it exactly. Summary: reconstruct state from Notion + Git — re-read the three databases, recompute both digests from the files, verify the approved git base. Never trust conversation memory.

Awaiting a human gate is a noop tick: the /loop dynamic wakeup parks, ~30-minute spacing. A Pending or absent approval parks; it never advances the feature and never stops it — STOP is reserved for Rejected, Revoked, digest mismatch, or an unreadable store. A per-feature park budget (default 14 days) turns eternal waiting into a dry stop with evidence preserved.

## Serial execution

At most one mutating worker at any time. No exceptions. Select only a ticket with State=TicketApproved whose every Depends On is TicketCompleted and Attempts < Attempt Cap. The worker: agent type `feature-loop-worker`, isolated git worktree, envelope prompt naming allowed paths, allowed commands, proof obligations, attempt context, stop conditions. A blocked ticket stops only its path; another already-approved ready ticket in the same feature may still run; otherwise consolidate one decision packet (`templates/decision-packet.md`) and park.

## Evidence gate

The coordinator independently runs or inspects the ticket's named proof before setting TicketCompleted. Worker confidence alone advances nothing. Record proof output in the ticket's Evidence field.

## Review and disposition

After all tickets: launch a fresh read-only reviewer, root context frozen before code access. Verdict: no_issue_found / issue_reported / inconclusive (`templates/review-report.md`). Findings create no repair authority. Assemble the decision packet, set AwaitingStefano. Stefano chooses disposition (`templates/disposition.md`): repair / accept / install / merge / stop — each a separate explicit decision. Repair requires a newly approved plan. Merge, install, release, disposition: Stefano only. Silence grants nothing.

## Fail-closed conditions

STOP the affected path, notify, never guess, when: digest mismatch; approval Rejected or Revoked; Notion unreadable; unknown or extra ticket; changed manifest; out-of-envelope snapshot delta; attempt or wall-clock cap exhausted; proof incomplete. A stopped path authorizes no new work.

## Honest limits

Worker isolation is not a hard boundary. Workers of type `feature-loop-worker` have no MCP tools; Bash deny rules block the known Notion vectors (ntn CLI, api.notion.com, credential files); but deny rules are best-effort pattern matching. Isolation = deny rules + permission classifier + pre/post snapshot detection, together. An out-of-envelope delta in the pre/post snapshots invalidates the run. This is not a sandbox.

In unattended mode the Decision-write prohibition has no prompt friction — nothing in the permission layer blocks it; it is procedural only, enforced by the pre/post Approvals snapshots.

## Recovery

A fresh session loses nothing. State reconstructs from Notion + Git: re-read the three databases, recompute the digests, verify the git base, resume at the tick protocol.
