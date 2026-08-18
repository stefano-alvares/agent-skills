# Disposition — <feature>

Each section is a separate explicit decision. Never bundled.

## Repair

- Authorises: a new plan cycle only. Requires a newly approved plan — new gates (Gate 2 again).
- Does NOT authorise: any code change before the new plan is approved.
- Notion: Features → State = RepairAuthorized; Approvals row → Artifact = Disposition, Decision = Approved.

## Accept without install

- Authorises: keeping the work as-is in the worktree/branch; no install, no merge.
- Does NOT authorise: symlink, merge, or release.
- Notion: Features → Disposition = shipped, State = ReadyToMerge only if merge is also decided separately; otherwise State stays.
- Decision reference: Approvals row → Artifact = Disposition, Decision = Approved.

## Install (symlink)

- Authorises: creating the symlink named here, nothing else.
- Symlink:
- Rollback: remove the symlink; restore prior link if one existed.
- Does NOT authorise: merge or release.
- Notion: Features → Disposition = shipped; Approvals row → Artifact = Disposition, Decision = Approved.

## Merge

- Authorises: merging the named branch to the named target, nothing else.
- Branch → target:
- Backup/rollback: record pre-merge SHA; revert to it on failure.
- Does NOT authorise: install or release.
- Notion: Features → State = Merged, Disposition = shipped; Approvals row → Artifact = Disposition, Decision = Approved.

## Stop and archive

- Authorises: stopping work and archiving the branch/worktree.
- Does NOT authorise: deletion of evidence or history.
- Notion: Features → State = Stopped, Disposition = dry_stopped (or cancelled); Approvals row → Artifact = Disposition, Decision = Approved.

---

Silence selects nothing. Every consequential action needs its own explicit decision.
