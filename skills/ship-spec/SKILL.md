---
name: ship-spec
description: Use when multiple audits, reviews, findings docs, or repair plans have piled up on one system with only minor improvement to show — "tie these together", "mega spec", "ship this once and for all", "it's been too long" — or when project docs (CLAUDE.md, kanban, status blocks) are suspected of drifting from the live system and one authoritative document must replace re-reading them all. Consumes audit ledgers, logic-map mismatch tables, and raze reports; produces the ship spec that to-tickets, goal-split, or plan-forge executes. Skip for greenfield features (to-spec) and for undiagnosed systems (run the audit first — this skill consolidates evidence, it does not create it).
---

# Ship Spec

An audit that doesn't end in a shipped system is inventory. After the second or third audit of the
same system, the findings themselves become the problem: they duplicate, they go stale, they
disagree, and every new session re-reads all of them and re-litigates instead of landing. This
skill converts audit inventory into ONE document where every prior finding has a disposition and
"shipped" has a definition someone can check.

**Core principle: the documents are witnesses, not evidence.** The system — the database, the
branches, the filesystem, the running checks — is the evidence. A ship spec that quotes docs
inherits their rot; the observed baseline for this skill included a repair marked "open, blocked
on operator" in two documents for days after the live DB showed it done, and a decisive verdict
sitting invisible on an unmerged branch.

## Phase 1 — Ground truth

No claim enters the spec quoted from a doc. Every open/done/blocked/gated claim is re-verified
against the live system before it is written down:

- DB claims → run the probe (read-only) and record the number.
- "On branch X" / "merged" / "started" claims → `git branch -v` + `git log base..branch` for
  EVERY work branch, not just the current one. Verdicts and artifacts hide on unmerged branches.
- "File exists/missing" claims → `ls` it.
- "Check passes" claims → run the check.
- A claim that cannot be verified in this pass is written `⚠ assumed`, visibly — never silently
  promoted to fact.
- Hidden-artifact floor (the stopping rule): every local branch, the stash list, and tags —
  reflog only when a claim still disagrees with what you found.

A stale doc is a **finding, not an embarrassment**: record the correction in the spec's
ground-truth table (claim | actual state | evidence) and schedule the doc fix as a task. Silently
fixing docs hides the drift-rate signal.

## Phase 2 — Document map

One line per prior audit/spec/review/plan: its takeaway + current status (done / superseded /
feeds task N). The map's purpose is that nobody re-reads eight documents again. Two docs that
disagree get a ledger line naming both — docs-win vs code is raze-review's rule; doc-vs-doc is an
owner decision, flagged.

## Phase 3 — Consolidate the invariants

Prior audits each grow their own numbering (I1–I9, M12–M15, N1–N7...). Deduplicate into one list;
each invariant names its owner and the task that establishes or protects it. If a logic map exists
(`architecture.md`), cite it — never fork it. If NO prior invariant ledger exists, derive the
invariants from the findings — for each, the claim that would have prevented it — and say they are
derived; that synthesis is licensed, not scope creep.

## Phase 4 — Definition of shipped

Three to five checkable lines, before any task is written. If "shipped" cannot be stated
checkably, the mission is not understood yet and the spec is not ready (plan-forge's VALUE rule,
inherited). This is the section the owner reads to decide the work is actually over.

## Phase 5 — The disposition rule

**Every finding from every mapped document lands in exactly one bucket. Zero findings left in
"open" limbo is the completeness check.**

| Bucket | Requirement |
|---|---|
| **DONE** | Named verification that proved the fix — a probe run in Phase 1, not a doc's say-so |
| **REFUTED** | The finding was false when written (never true, not fixed-later) — evidence named; correcting the doc that asserted it becomes a task |
| **TASK** | Dependency-ordered into phases; each task carries owner (agent \| operator), a runnable done-check, and its gate (spend / DB write / decision / none — gates legitimately degrade to "none" on small systems) |
| **ACCEPTED LOSS** | The reason recorded, so it stops resurfacing as a "new" finding in the next audit |

Default phase order (adjust with reasons, not vibes): land already-built work (no spend, no risk)
→ cheap repairs on assets already paid for → the gated spend → doc-rot closure. Big spends go
last: by then they run through every guard the earlier phases landed.

## Phase 6 — Hand off

The spec is the authority; execution routes elsewhere: `to-tickets` to ticket-ize the task list,
`goal-split` when tasks partition across parallel sessions, `plan-forge` for one session's worth.
Stale-doc corrections from Phase 1 are tasks too — a ship spec that leaves CLAUDE.md lying has
scheduled the next drift.

## Output skeleton

```
# <system> — consolidated ship spec — <date>
Mission + definition of shipped (3-5 checkable lines)
## 0. Ground truth as of <date>       ← claim | state | evidence table, probes not citations
## 1. Document map                    ← one line per prior doc
## 2. Consolidated invariants         ← deduped, owned
## 3. Task list                      ← phased, dependency-ordered, owner + done-check + gate
## 4. Accepted losses                 ← with reasons
## 5. Sequencing rationale            ← why this order, in one paragraph
```

## Routing

| Situation | Skill |
|---|---|
| Greenfield feature from a conversation | `to-spec` |
| System not yet diagnosed | `raze-review` / `logic-map` / `logic-first-debug` first |
| Spec done, needs tickets | `to-tickets` |
| Tasks split across parallel sessions | `goal-split` |
| One session's execution plan | `plan-forge` |

## Red flags — you are making more inventory

| Thought | Reality |
|---|---|
| "The doc says it's still open" | Probe it. The baseline case sat "open" in two docs days after the DB showed it done. |
| "I'll summarize the audits" | A summary is more inventory. Every finding gets a disposition or the spec isn't one. |
| "Current branch state is enough" | The decisive verdict in the baseline case lived on an unmerged branch nobody had checked. |
| "This finding is awkward, leave it open" | Open limbo is banned. DONE, TASK, or ACCEPTED LOSS — pick with the owner. |
| "The metric will drop if we do the honest task" | Owner decision, named in the task's gate — never silently softened. |
| "Too many findings to disposition" | That accumulation is the disease this skill treats. If truly unbounded, the system needs raze-review, not another doc. |
| "I remember what the audit said" | Reading ≠ remembering. The map is built from the docs open in front of you, the truth from probes. |
