# Tick protocol

Run this checklist at every tick, in any session, before any other action. Never trust conversation memory.

0. Preflight: verify the `feature-loop-worker` agent type is available AND the deny rules are loaded (user-level or project-level). Either absent → STOP: "install the user-level agent def + deny rules, then restart the session."
1. Re-read the Features, Approvals, and Tickets databases.
2. Recompute the spec digest (SHA-256) from the spec file.
3. Compare the file digest to the approval page's Digest — the page is the authority — and verify the page-body mirror still matches the digested file; a Feature-row-mirror-vs-page mismatch or a mirror-vs-file divergence = FAIL-CLOSED.
4. Classify the one gate: SATISFIED (Approved + digest equality), AWAITING-HUMAN (page absent or Decision=Pending), FAIL-CLOSED (Rejected, Revoked, digest mismatch, or unreadable store). Post-flip ticks never park on plan approval — the plan is internal.
5. Verify the git base and the manifest against the approved spec; any drift is FAIL-CLOSED.
6. Any FAIL-CLOSED → STOP the affected path and notify. Never guess.
7. Gate AWAITING-HUMAN (and nothing FAIL-CLOSED) → PARK: noop tick, ~30-minute spacing. A Pending or absent approval never advances and never stops the feature.
8. Parity: the Tickets rows for this feature must match the approved spec's task list one-for-one by idempotency key; an unknown, extra, or missing ticket = FAIL-CLOSED for that ticket's path — sibling ready tickets may run.
9. If the gate is SATISFIED and no tickets exist for the feature yet → run plan-forge refinement + the internal critic (max 2 cycles), then project the spec's tasks one-for-one into the Tickets database with idempotency keys; then continue.
10. Select a ready ticket: State=TicketApproved, every Depends On is TicketCompleted, Attempts < Attempt Cap. If no ticket is ready → PARK.
11. A TicketApproved ticket with Attempts ≥ Attempt Cap → set TicketBlockedForStefano and write a decision packet.
12. Take pre-snapshots: Approvals database content and repo inventory.
13. Execute: run the coordinator ticket yourself, or launch exactly one worker with its envelope prompt.
14. Take post-snapshots and compare to the pre-snapshots; an out-of-envelope delta invalidates the run.
15. Run or inspect the ticket's named proof yourself.
16. If the proof passes → set TicketCompleted and record the proof output in Evidence.
17. If the proof fails → increment Attempts; if Attempts < Attempt Cap retry the same approach, else apply step 11.
18. If the work hits an open fork → resolve by 1→3→1 against `references/preferences.md`; an irreversible, scope-changing, spend, or security fork instead → set TicketBlockedForStefano and write a decision packet.
19. Append every 1→3→1 resolution this tick (options, choice, deciding preference) to the feature's Notion page before the tick ends.
20. If all tickets are TicketCompleted → set FeatureEvidenceReady → run the advisory review → assemble the decision packet; set AwaitingStefano only if the spec names an irreversible action, else close at review + decision log.

## Standing rules

- **Park budget.** Each feature has a park budget (default 14 days). When it is exhausted → dry stop: State=Stopped, Disposition=dry_stopped, all evidence preserved.
- **Decision fields.** Never write a Decision field on a real approval page — only on FIXTURE-prefixed pages inside an approved spec's explicit test carve-out, archived when the test ends; Stefano alone flips everything else.
