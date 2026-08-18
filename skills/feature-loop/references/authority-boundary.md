# Authority boundary

## Ownership

- **Stefano** owns product purpose, outcome, creative direction, scope, non-goals, priority, architecture, domain/data model, public behaviour, acceptance, consequential trade-offs, spend, security/privacy, production, client commitments, merge, install, release, disposition, and irreversible action.
- **Coordinator** may research, challenge, prepare the spec, refine the plan after the flip, run the internal critic, project tickets, select already-approved ready tickets, launch one worker at a time, verify evidence, resolve open forks by 1→3→1 against `references/preferences.md` — with the obligation to log options, choice, and deciding preference to the feature's Notion page — consolidate blockers, and coordinate review.
- **Workers** may implement and test one approved ticket inside its envelope. Nothing else.
- **Reviewer** may report findings read-only. It owns no code, state, repair, acceptance, merge, or release authority.

Silence grants nothing. Execution and review cannot create authority.

## Store contract

Each fact has one owner. No third store.

- **Notion:** the Ship Spec approval page (its Digest is the digest authority), the spec mirror in the page body, revocation, human decisions, disposition, the decision log, and operational tickets — state, dependencies, attempts, envelopes, evidence.
- **Git:** the spec file (the digested authority), immutable spec snapshots, commits and diffs, code, durable proof artifacts.

A Notion ticket carries approved authority; it does not create it.

## v0.5 controls

- One gate: the Ship Spec. Plan refinement, the internal critic, and projection are post-flip internal steps — no human approval, bound by the spec's digest.
- The coordinator and every subagent never write a Decision field on a real approval page — only on FIXTURE-prefixed pages inside an approved spec's explicit test carve-out, archived when the test ends; Stefano alone flips everything else.
- One Control Plane page: `3bfe90b1-9ba7-812b-9cba-d362956ba4e9`.
- Projection is manual and coordinator-verified before any worker starts.
- At most one mutating worker at any time. No exceptions.
- Reviewer sessions stay read-only and outside automatic request-changes routing.
- Configuration is not proof. Inspect the live databases and the worker tool surface before each feature.

## Fail-closed conditions

Stop the affected path when:

- the spec digest mismatches the approval page's Digest — the page is the digest authority; a Feature-row mirror that disagrees with the page, or a page-body mirror that diverges from the file, also fails closed (absent or Pending approvals park the feature instead — they never advance it);
- an approval is Rejected or Revoked;
- a ticket's identity, body, or dependencies differ from the approved spec's task list;
- a proposed action changes scope, architecture, domain/data model, public interface, dependency, runtime/toolchain, persistence, security/privacy, deployment, recurring cost, production, client communication, acceptance, or reversibility — unless the spec pre-authorizes it as a named reversible action;
- the worker needs files, tools, credentials, services, or network access outside the ticket envelope;
- the attempt or wall-clock cap is exhausted;
- proof is incomplete;
- the worktree, Notion databases, or snapshots cannot be reconstructed or compared safely.

A stopped path authorizes no new work. The coordinator may select only another already-approved ready ticket in the same feature.

## Evidence and completion

Ticket completion requires the proof named before projection. The worker supplies artifacts; the coordinator independently runs or inspects the proof before setting TicketCompleted.

Reviewer findings remain advisory. Repair requires a new spec version and a new flip. Waiver, acceptance, merge, install, release, and stop remain explicit Stefano decisions.

## Runtime threshold

Do not build a graph runtime. Add the smallest adapter only after a named enforcement failure that Notion, Git, and Claude Code primitives cannot handle. Likely candidates: stale-digest preflight, revocation check before worker launch, idempotent exact-ticket projection.
