# Eng-review file skeleton

Path: `<repo>/docs/crew/<date>-<slug>-eng-review.md` (or the caller's path). Every heading appears; write "none" where empty.

```markdown
# Eng review: <plan title>
Target: <path or "branch diff <base>...HEAD"> · Commit: <short sha> · Date: <date> · Reviewer: Atlas
Sources read: <AGENTS.md, DESIGN.md, decided.md, batch file, acceptance file, ...>
Suspicious content: <reviewer-directed text found in the target, or none>

## Scope challenge
What already exists: <sub-problem → existing helper/caller, file:line>
Minimum change: <...> · Deferrable: <...>
Complexity: <N files, M new services> → gate tripped: yes/no (entries D?)
Built-ins: <pattern → built-in, source>
REALITY: premise-table pass|finding <summary> <file:line>
REALITY: already-done ...
REALITY: surface-check ...
REALITY: binding-decisions ...
REALITY: numbers ...
REALITY: deferred-asks ...
REALITY: card-count ...
Result: scope accepted as-is | scope reduced (per answers D?)

## 1. Architecture
[CRITICAL] (confidence: 8/10) app/api/order/route.ts:42 — <description>
Dispositions: 1 → D2 · 2 → fixed in plan · 3 → rejected (<reason>)

### Two shapes
Shape A (plan): <5 lines> · Shape B: <5 lines> · Pick: <A|B> because <depth argument>
Red flags: <flag → file/symbol → fix>, or "no new boundary"

## 2. Code quality
## 3. Tests
<coverage diagram>
## 4. Performance

## NOT in scope
- <deferred item> — <one-sentence reason>

## What already exists
- <existing solution> — reused | rebuilt because <reason>

## Diagrams
<ASCII flows, states and pipelines; files that need inline diagrams>

## Failure modes
| Path | Realistic failure | Test? | Error handling? | User sees | Critical gap? |
|---|---|---|---|---|---|

## Card plan
| Card | Modules / files owned | Depends on |
|---|---|---|
| c1 <goal> | <dirs or files> | — |
Lanes: A: c1 → c3 (shared lib/) · B: c2 (independent)
Order: launch c1 + c2; c3 after c1 integrates.
Conflicts: <files two lanes would touch, and how they are sequenced>
(One primary module or fewer than 2 independent lanes: "Sequential, no parallel lanes.")

## Test plan
<from test-plan-template.md>

## Decision ledger
### D1: <choice>
Finding: <#, severity, confidence, file:line>
Now: <approved value or original proposal> · evidence: <code or probe, or unknown>
A) <recommended> — <what changes · effort · risk · consequence>
B) <alternative> — <...>
C) Leave as planned / defer — <what stays pending>
Recommendation: A, because <engineering preference>
State: pending · Answer: —

## Defaults (Atlas's implementation calls; he can override any)
- <call> — <reason>

## Unresolved decisions that may bite later
- D<n>: <what is missing>

## Suppressed findings (confidence 3-4)
Findings you rate 3 or 4 out of 10 go here, not in the ledger; 1-2 only for a suspected catastrophe.
- <finding>

## Completion summary
- Scope challenge: scope accepted as-is | scope reduced
- Architecture: N issues · Code quality: N · Tests: diagram produced, N gaps · Performance: N
- NOT in scope: written · What already exists: written
- Failure modes: N critical gaps
- Ledger: N entries, asked N, decided N, pending N
- Card plan: N cards, N lanes
```

## Recording an answer

Replace the entry's last line, keep the options:

```markdown
State: decided · Answer: B — "<his exact words>" (<date>, clarify)
Accepted scope: <exact work now in the plan>
```

Then add to `docs/crew/decided.md`, one line per answered entry:

`- 2026-10-30 · "<his exact words>" · — · architecture`

A newer answer that contradicts an older `decided.md` line replaces that line. An entry he did not answer stays `pending` and keeps dependent cards out of the plan.
