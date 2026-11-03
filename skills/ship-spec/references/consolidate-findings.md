# Consolidating a pile of findings (ship-spec)

Use when several audits, reviews or repair plans on one system have produced little shipped work. After
the second or third audit, the findings become the problem: they duplicate, go stale, disagree, and
every session re-reads them instead of landing anything. This turns that inventory into one task list
where every finding has a disposition.

**Core rule: documents are witnesses, the system is the evidence.**

## 1. Ground truth

No claim enters the spec quoted from a doc. Re-verify every open, done, blocked or gated claim:

- DB claims: run the read-only probe and record the number.
- "On branch X", "merged", "started": `git branch -v` and `git log base..branch` for every work branch.
  Verdicts and artifacts hide on unmerged branches.
- "File exists" claims: `ls` it. "Check passes" claims: run the check.
- Stopping rule: every local branch, the stash list and tags; the reflog only when a claim still
  disagrees with what you found.
- A claim you cannot verify now is written `assumed`, visibly.

A stale doc is a finding: record it as claim | actual state | evidence, and schedule the doc fix.

## 2. Document map

One line per prior document: its takeaway and status (done, superseded, feeds task N). Two documents
that disagree get a line naming both; doc versus doc is an owner decision.

## 3. Consolidated invariants

Deduplicate the invariants the audits each numbered their own way. Each names its owner and the task that
protects it. Cite an existing logic map; never fork it. With no prior invariant ledger, derive one claim
per finding (the claim that would have prevented it) and say they are derived.

## 4. Dispositions

Every finding lands in exactly one bucket (TASK, DONE, DEFERRED / ACCEPTED LOSS, REFUTED; definitions in
ship-spec section 4). Default task order: land already-built work, then cheap repairs on what is already paid for,
then gated spend, then doc-rot closure.

## Output skeleton

```
# <system>: consolidated spec, <date>
Mission + definition of shipped (3-5 checkable lines)
## 0. Ground truth as of <date>   (claim | state | evidence)
## 1. Document map
## 2. Consolidated invariants
## 3. Task list                   (phased, owner, done-check, gate)
## 4. Accepted losses             (with reasons)
## 5. Why this order              (one paragraph)
```

Write it into the batch file's Ship spec, then continue with plan-forge on the task list.
