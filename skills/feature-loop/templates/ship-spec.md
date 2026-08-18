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
- **Cost/risk:** {time, spend, blast radius}

## Definition of shipped

3–5 checkable lines. Each line is verifiable by a probe, not by opinion.

- [ ] {check 1}
- [ ] {check 2}
- [ ] {check 3}

## Ground truth

Probes, not citations. Mark any unverifiable claim "⚠ assumed".

| Claim | State | Evidence |
|---|---|---|
| {claim} | {verified / ⚠ assumed} | {the probe run and its output} |

## Tasks

Phased, dependency-ordered. Each task: owner (coordinator | worker | operator), envelope, done-check, cap.

### Phase 1 — {name}

- **T1** — {task}. Owner: {owner}. Envelope: {allowed paths/commands}. Done-check: {probe}. Cap: {attempts/time}.

## Accepted losses

Each loss with its reason, so it stops resurfacing.

- {loss} — {reason}

## Revision log

Dated lines, newest last.

- {YYYY-MM-DD}: {change}

## Approval

Fixed text — do not edit:

The Status line in this file is non-authoritative; it sits inside the digested bytes. The Notion approval page governs. Artifact=Build Contract. The page body must carry this spec's COMPLETE text (mirror) and its Digest must be the file's SHA-256. Pre-approval revisions update the SAME Pending page: new digest, refreshed mirror. Post-approval changes are a new spec version and a new flip. Decision is founder-only. Silence changes nothing.
