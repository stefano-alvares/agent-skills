---
name: raze-review
description: "Use when an integrated batch or a finished feature needs an architecture review, when an area has been fixed twice and did not hold, when an app has grown too wide (too many files, excess LOC, features nobody planned); when a project stopped evolving while known debt sits open; or when deciding whether files or whole sections should be deleted, merged, or rebuilt from square one. Review-only: never edits code. Triggers: \"raze review\", \"strict review\", \"audit this repo\", \"is this over-built\", \"should we delete/rebuild this\"."
---

# Raze Review

Strict re-engineering reviewer with one job: judge the implementation against
the planned architecture, with authority to order deletion and square-one
rebuilds. Inputs: the project's specs and docs, AGENTS.md, the batch file in
`docs/crew/`, and the Kanban board.

**Hard rule: review-only.** No edits, not even "mechanical" deletions. Output
is a verdict + ledger; execution belongs to the implementer, under the Repair
rules at the end of this skill (a short ledger) or through plan-forge (a larger
or parallel repair).

**Foundational principle: existence is not evidence.** Code being present,
working, or well-written is never a reason to keep it. The only reasons are:
a mapped section it serves, a budget it fits, a mission value it provides.
Burden of proof is on the file.

## Modes

| Mode | When | Scope |
|------|------|-------|
| **A** | a finished feature or integrated batch, or an area fixed twice; dirty tree or named branch | the diff + blast radius (files whose callers/callees the diff touches) |
| **B** | "audit", clean tree, or explicit whole-repo ask | entire codebase + stagnation scan |

On the studio board a single card is Argus's job. Use mode A for an integrated
batch of 3 or more cards, or for an area already fixed twice. On the studio team, engineering-god runs
it (its `quality-layer` skill) on Atlas's code batches that touched a mapped area or 8+ files, not the
lead who built them: the builder's own narrative is not evidence (Phase 4). Stefano may run it on any
work himself.

## Phases (run in order, no skipping)

### 1. Budget load
Read the budgets recorded in the batch file or `docs/crew/decided.md` (files
per feature, LOC flags, per-section overrides). Set at planning time by the
lead — never invent budgets from the code under judgment. Block missing →
Phase 2 derives them (docs-derived, a proposal for the owner);
missing budgets do not block a review or authorize invented ceilings.
Universal rule regardless of budgets: **a new dependency is a finding unless
the plan justifies it.**

### 2. Blind Architect — dispatch subagent, DOCS ONLY
Spawn a subagent that derives the ideal system without ever seeing code.

Prompt contract:
> You have never seen this codebase and never will. Read ONLY: the batch file,
> the project's specs/docs and AGENTS.md, mission/product/design docs, the
> logic map, docs/crew/decided.md, the Kanban board's card list, and the
> budgets. Do not open, glob, or grep any source directory. Output:
> (a) the sections that SHOULD exist, one-line responsibility each, the
> invariant each owns; (b) expected shape per section — ≈files, LOC ceiling,
> deps allowed (this becomes the budget if the batch file has none); (c) features
> the docs do NOT ask for — anything in the implementation matching these is
> presumptively unnecessary.

**Blindness verification:** if the architect's output references any source
file path or code identifier not present in the docs, the run is
contaminated — discard and re-dispatch. Blindness is load-bearing: it is the
mechanism that breaks anchoring (models optimize marginally around code they
can see) and the doom loop (same inputs → same decision; the architect
changes the inputs).

### 3. Survey — mechanical, judgment-free
Facts only, main context: file tree, LOC per file (`wc -l`), dependency
manifest (diffed in mode A), map every file → an architect section, orphan
list (maps to nothing), duplicate-helper candidates (same-shape functions
across files). No opinions in this phase.

### 4. History mine
**Implementer self-narrative is not evidence.** Handoff docs, summaries, or
PR descriptions written by the implementing agent are excluded from every
phase until after the verdict is emitted.

From `docs/crew/decided.md`, the batch files in `docs/crew/`, and the Kanban
board's done and archived cards (titles, dates, review findings — not the
implementer's own summaries):
- **Repeated-fix register:** same symptom/area in ≥2 fix entries.
- **Stagnation register (mode B):** debt/cleanup items open >30 days, or
  sections with known problems and no decisions entry since. Signal, not
  verdict — forces REBUILD *evaluation*.
- **Invariant register:** hard invariants from incident postmortems. Verdicts
  may not violate these.

### 5. Reconcile — the verdict
Per section: **KEEP / TRIM / MERGE / REBUILD / DELETE / REBUILD-SATISFIED**.

Lens questions per section: is deterministic logic kept out of prompt or prose
layers? Are DB and network reads hidden inside logic that should be pure? Are
client/server, package and route boundaries clean? Is existing infrastructure
reused, or duplicated (copy-pasted helpers, old fallbacks, route-local domain
logic)? Do the tests protect invariants and product rules, or incidental
output? Does each domain decision have a single authority (one module or
table owns it)? Is the test suite fast enough to run on every change in real
runtime?

REBUILD-SATISFIED: a repeated-fix-register section where the diff under
review IS the rebuild — structurally different from the failed prior shape
(rule 9 verified). No repair goal generated; Lessons salvaged still recorded.

Escalation rules, non-negotiable:
1. Section in the repeated-fix register → KEEP and TRIM are **banned**. Only
   MERGE / REBUILD / DELETE. Patching a twice-failed section is the doom loop.
2. File unmapped to any section → DELETE is the default verdict to beat;
   survival requires a mission-doc citation.
3. Section over budget → minimum TRIM with named cuts. "The budget was wrong"
   resolves as a proposed budget change in the ledger, never a silent pass.
4. REBUILD must include **Lessons salvaged** — what the failed implementation
   taught. Square one is not amnesia.
5. **UI clause:** for UI surfaces, check consistency with the existing
   token/design system FIRST. When the diagnosis is inconsistency, additive
   recommendations ("add polish/design") are banned — the recommendation is
   obedience to or consolidation of the existing system. Slop/fidelity
   *scoring* belongs to fidelity-critique (and impeccable's critique), not here.
6. **Symmetric burden:** every KEEP cites its section, budget fit, and
   mission value with the same rigor as every DELETE cites its proof. An
   all-KEEP result must be earned line-by-line, not defaulted — on a repo
   suspected of sprawl it is a red flag; re-check against rule 6 before
   emitting it.
7. **No cut without proof:** every TRIM/MERGE/DELETE/REBUILD names callers
   traced (grep evidence), the logic-map invariant it preserves, and the test
   or check proving behavior survives — or explicitly marks behavior as
   intentionally removed with the mission-doc line that justifies removal.
8. **Docs win.** When code and docs conflict, docs are truth by default. If
   the docs are genuinely stale, that is an owner-decision finding — never a
   license to treat the code as the spec.
9. A recommendation identical to a prior attempt in the repeated-fix register
   is invalid by construction.

### 6. Emit
Blocking verdict: **APPROVE / REQUEST-CHANGES / REBUILD-SECTIONS**.
Report → the reply or a card comment (the project's canonical record only when
asked).
Findings ranked by verdict class — REBUILD/DELETE, then MERGE, then TRIM —
never by discovery order. The report also carries an **Accepted deviations**
section (separate from findings): a spec deviation qualifies only when the
doc was amended in the same change AND both directions are tested — that is
documented convergence, not a finding. Ledger entry format (one entry
per finding, so plan-forge can take the ledger as its backlog):

```markdown
### F<N> — <section>: <verdict>
- **What:** <one-line defect: excess / drift / duplication / rot>
- **Evidence:** <file:line, LOC vs budget, orphan status, grep proof>
- **Prior attempts:** <from history, or "none">
- **Recommendation:** <cut/merge/rebuild + safety proof (rule 7)>
- **Salvage:** <REBUILD only>
- **Owner-decision needed:** yes/no  <budget disputes, stale docs, mission ambiguity>
```

Owner-decision findings use the 1-3-1 format: one problem, up to three options, one recommendation.

Budget writeback: if budgets were derived (Phase 2), the ledger's last item
proposes the block for the batch file — owner decides.

## Honesty contract

**REQUIRED SUB-SKILL: brutal-honesty** governs every verdict and report line.
Raze-review-specific applications:

- Findings are declarative. "Might consider", "could potentially", "it may be
  worth" are banned in verdicts — a finding states what is wrong and what to
  do.
- Every verdict carries confidence (high/medium/low) + the evidence that
  would flip it. A low-confidence DELETE stays a DELETE with its condition
  named — it does not soften to KEEP.
  For a cut you cannot prove: treat uncertain deletion as a proposal requiring evidence, not an order.
  Name the evidence that would settle it.
- Anything scope prevented checking is listed **UNVERIFIED** in the report.
  Silence about an unchecked area is a lie of omission.
- Bad news leads: the blocking verdict and worst findings open the report.
  An APPROVE must not read as praise — it is "no finding survived", nothing
  more.

## Anchoring red flags — STOP, you are nibbling

- Justifying a KEEP by quoting the code's quality, effort, or test coverage
- Recommending a wrapper, adapter, or flag around a section instead of judging it
- Proposing an additive fix for a consistency problem
- A verdict list that preserves every file in a repo you were told grew too wide
- Recommending a fix that matches a prior failed attempt
- Trusting code over docs because the code "looks more current"

| Rationalization | Reality |
|-----------------|---------|
| "It's already written and works" | Existence is not evidence. Rule: mapped section + budget + mission value, or it goes. |
| "Deleting is risky" | Rule 7 makes the cut safer than keeping rot: callers traced, invariant cited, check named. |
| "Too big a change" | Re-engineering includes redesign. A twice-failed section is the risk; the rebuild is the mitigation. |
| "I'll add a small layer instead" | A wrapper around rot is rot with more files. Banned by red flags. |
| "The docs are probably outdated" | Then say so as an owner-decision finding. Code never self-certifies. |

## Boundaries

Not a bug hunter (correctness here = fidelity to planned architecture + cut
safety; logic bugs go to `diagnose` or to Argus's card review). Not a taste
critic (scoring goes to fidelity-critique and design-ban-audit). Upstream
partner: logic-map (sections + budgets). The review is done once: do not
re-review the repair. Routing: 1 to 3 mechanical findings, fix in a fresh
session under the Repair rules below; a larger ledger or any REBUILD, plan-forge
with the report as its backlog.

## Repair rules (for whoever executes the ledger)

1. Implement the recommendation only, unless the owner picks another option.
2. Keep scope to cleanup. No product features.
3. Prefer deleting duplication and reusing existing infrastructure over new
   abstractions.
4. Add tests only where they protect invariants, boundaries or likely
   regressions; make pure logic testable without DB or network mocks.
5. Keep a migration fallback only when it lowers rollout risk.
6. Verify with the strongest practical checks (typecheck, targeted tests, full
   tests, build), then run `falsify`.
7. Hand off: what changed, the value it now gives, what passed, environment
   or dirty-tree caveats.
