# Authority boundary

## Ownership

- **Stefano** owns product purpose, outcome, creative direction, scope, non-goals, priority, architecture, domain/data model, public behaviour, acceptance, consequential trade-offs, spend, security/privacy, production, client commitments, merge, install, release, disposition, and irreversible action.
- **Coordinator** may research, challenge, prepare contracts and plans, project approved tickets, select already-approved ready tickets, launch one worker at a time, verify evidence, consolidate blockers, and coordinate review.
- **Workers** may implement and test one approved ticket inside its envelope. Nothing else.
- **Reviewer** may report findings read-only. It owns no code, state, repair, acceptance, merge, or release authority.

Silence grants nothing. Execution and review cannot create authority.

## Store contract

Each fact has one owner. No third store.

- **Notion:** Build Contract, plan digest, approvals, revocation, human decisions, disposition, and operational tickets — state, dependencies, attempts, envelopes, evidence.
- **Git:** immutable plan snapshots, commits and diffs, code, durable proof artifacts.

A Notion ticket carries approved authority; it does not create it.

## v0.4 controls

- One Control Plane page: `3bfe90b1-9ba7-812b-9cba-d362956ba4e9`.
- Projection is manual and coordinator-verified before any worker starts.
- At most one mutating worker at any time. No exceptions.
- Reviewer sessions stay read-only and outside automatic request-changes routing.
- Configuration is not proof. Inspect the live databases and the worker tool surface before each feature.

## Fail-closed conditions

Stop the affected path when:

- an approval is Rejected, Revoked, or digest-mismatched (absent or Pending approvals park the feature instead — they never advance it);
- a ticket's identity, body, or dependencies differ from the approved plan;
- a proposed action changes scope, architecture, domain/data model, public interface, dependency, runtime/toolchain, persistence, security/privacy, deployment, recurring cost, production, client communication, acceptance, or reversibility;
- the worker needs files, tools, credentials, services, or network access outside the ticket envelope;
- the attempt or wall-clock cap is exhausted;
- proof is incomplete;
- the worktree, Notion databases, or snapshots cannot be reconstructed or compared safely.

A stopped path authorizes no new work. The coordinator may select only another already-approved ready ticket in the same feature.

## Evidence and completion

Ticket completion requires the proof named before plan approval. The worker supplies artifacts; the coordinator independently runs or inspects the proof before setting TicketCompleted.

Reviewer findings remain advisory. Repair, waiver, acceptance, merge, install, release, and stop remain explicit Stefano decisions. Repair requires a newly approved plan.

## Runtime threshold

Do not build a graph runtime. Add the smallest adapter only after a named enforcement failure that Notion, Git, and Claude Code primitives cannot handle. Likely candidates: stale-digest preflight, revocation check before worker launch, idempotent exact-ticket projection.
