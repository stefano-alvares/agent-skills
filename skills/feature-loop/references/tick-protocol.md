# Tick protocol

Run this checklist at every tick, in any session, before any other action. Never trust conversation memory.

1. Re-read the Features, Approvals, and Tickets databases.
2. Recompute the contract digest and the plan digest (SHA-256) from the artifact files.
3. Compare each digest to the Feature row and classify each gate: SATISFIED (Approved + digest equality), AWAITING-HUMAN (page absent or Decision=Pending), FAIL-CLOSED (Rejected, Revoked, digest mismatch, or unreadable store).
4. Verify the git base and the manifest against the approved plan; any drift is FAIL-CLOSED.
5. Any FAIL-CLOSED → STOP the affected path and notify. Never guess.
6. Any gate AWAITING-HUMAN (and nothing FAIL-CLOSED) → PARK: noop tick, ~30-minute spacing. A Pending or absent approval never advances and never stops the feature.
7. All gates SATISFIED → select a ready ticket: State=TicketApproved, every Depends On is TicketCompleted, Attempts < Attempt Cap. If no ticket is ready → PARK.
8. Take pre-snapshots: Approvals database content and repo inventory.
9. Execute: run the coordinator ticket yourself, or launch exactly one worker with its envelope prompt.
10. Take post-snapshots and compare to the pre-snapshots; an out-of-envelope delta invalidates the run.
11. Run or inspect the ticket's named proof yourself.
12. If the proof passes → set TicketCompleted and record the proof output in Evidence.
13. If the proof fails and Attempts < Attempt Cap → retry the same approach; increment Attempts.
14. If the proof fails out-of-cap, or the work forks → set TicketBlockedForStefano and write a decision packet.
15. If all tickets are TicketCompleted → set FeatureEvidenceReady → run the advisory review → assemble the decision packet → set AwaitingStefano.

## Standing rules

- **Park budget.** Each feature has a park budget (default 14 days). When it is exhausted → dry stop: set the dry-stop states, preserve all evidence, record Disposition=dry_stopped.
- **Decision fields.** Never write a Decision field on any real approval page. No exceptions. Stefano alone flips Decision. Fixture pages ("FIXTURE — " name prefix, inside an approved plan's explicit gate-test carve-out) are the sole exception; archive them when the test ends.
