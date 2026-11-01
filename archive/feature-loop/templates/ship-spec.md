<!-- Ship-spec template. The internal critic must verify every slot below before the spec is presented.
     A missing slot means the spec is not presentable — do not send it to the founder.
     Fill each slot per its one-line instruction; delete the instructions before presenting. -->

# Ship spec: {feature name} — v{n}

## BLUF

At most 8 lines, in this exact order. More than 8 lines, or any line missing, fails the internal critic.

- **Decision:** {the one flip being requested}
- **Issue:** {the problem, one line}
- **What ships:** {the deliverable, one line}
- **What approving authorizes:** {exact scope granted}
- **NOT authorized:** {what approval does not grant}
- **Cost/risk:** {time, spend RANGE (advisory — never gates quality), blast radius — including deferred costs: actions cheap now whose reversal is expensive later}

## Definition of shipped

3–5 lines, each a TRANSFORMATION in feature/logic terms — what a user or system can do after this wave that it could not before — followed by the probe that evidences it. The probe is the evidence, never the meaning: "tests pass" or "command exits 0" alone fails the internal critic.

- [ ] {transformation} — probe: {command/check}
- [ ] {transformation} — probe: {command/check}
- [ ] {transformation} — probe: {command/check}

## Ground truth

Probes, not citations. Mark any unverifiable claim "⚠ assumed". Cite the staple docs consulted (DESIGN.md, PRODUCT.md, logic map — produce the missing map at intake). For a new project, record the stack evaluation here: what the app needs → what the chosen stack provides.

| Claim | State | Evidence |
|---|---|---|
| {claim} | {verified / ⚠ assumed} | {the probe run and its output} |

## Tasks

Phased, dependency-ordered. Each task: owner (coordinator | worker | operator), envelope, done-check, cap.

### Phase 1 — {name}

- **T1** — {task}. Owner: {owner}. Envelope: {allowed paths/commands}. Done-check: {probe}. Cap: {attempts/time}. Flags: {riskiest / light / neither}.

Mark every task: `riskiest` (public interface, authority-bearing logic such as scoring/marking rules, persistence — the mid-flight pass runs when the first of these lands) or `light` (all three: zero behavior change, no authority-bearing file, revert-only rollback). At least one task is riskiest, or state here why none qualifies. Doc-sync tasks go last.

## Containment coverage

Which controls this wave's character disables, and the substitute baseline. A wave touching only git-tracked files writes "full git coverage" and stops.

- Git-excluded data in the blast radius: {none / paths}
- Disabled controls: {e.g. worktree isolation and git snapshots are blind to the above}
- Substitute baseline: {e.g. file inventory + checksums of the affected tree, pre and post}

## Accepted losses

Each loss with its reason, so it stops resurfacing.

- {loss} — {reason}

## Revision log

Dated lines, newest last.

- {YYYY-MM-DD}: {change}

## Approval

Fixed text — do not edit:

The Status line in this file is non-authoritative; it sits inside the digested bytes. The Notion approval page governs. Artifact=Build Contract. The page body must carry this spec's COMPLETE text (mirror) and its Digest must be the file's SHA-256. Pre-approval revisions update the SAME Pending page: new digest, refreshed mirror. Post-approval changes are a new spec version and a new flip. Decision is founder-only. Silence changes nothing.
