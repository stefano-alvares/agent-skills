# Review sections: checklists

Load this when running section 3 of high-risk-review.md ("Four sections, in order"). Each section ends with findings (most severe first, or "No issues found") and a disposition per finding.

## 1. Architecture

- Component boundaries, dependencies and coupling.
- Data flow, bottlenecks, scaling limits, single points of failure.
- Security: auth, data access, API and form boundaries, secrets.
- Flows that need an ASCII diagram in the plan (or inline in complex code).
- For each new path or integration, one realistic production failure: does the plan handle it?
- New artifacts (packages, deploy targets): how they build, deploy and update. Preview deploys are `vercel deploy --yes`; production is Stefano's.

### Design twice (only when the plan adds a module, service, package or boundary)

A plan with one design usually took the first shape that compiled in the author's head. Before judging it, write a second shape that is **structurally** different: another owner for the state, another split of responsibilities, another place for the boundary. A point fix inside the first shape is not a second candidate. When the plan has none, sketch one in five lines (types and signatures, bodies `not implemented`).

Compare on **interface depth**: how much behaviour and policy each hides behind how small a public surface. Prefer the one that hides more behind less. A deep module is not a deep call chain: the chain scatters understanding across layers; the module concentrates it behind one interface.

**The eight red flags.** Assume the next contributor is an agent that sees only the files it opened, copies the nearest example and takes the shortest path that compiles. Prefer the design where a change that looks right from one file is right for the whole repo. A flag is a finding with a file or symbol and a reason to revise the shape.

1. **Shallow module:** a large interface over little hidden complexity; several calls per operation; options that expose internal stages.
2. **Information leakage:** one decision (a representation, policy, wire or storage detail) lives in more than one module. Parse external data into domain types at the boundary.
3. **Temporal decomposition:** modules split by execution order (load, validate, transform, save) instead of by the knowledge they own.
4. **Pass-through method:** forwards the same arguments to another function of the same shape.
5. **Split ownership:** two modules write the same state or each keep a copy. One owner per piece of state.
6. **Two ways to do one task:** keep one, move the callers, delete the rest in the same change.
7. **Importable internals:** the shortest path imports them and they become interface. Make an outside import fail the build.
8. **Hand-synced list:** the same items in two places. Derive the second, or fail the build when they disagree.

Record both shapes, the pick, the depth argument, and each flag with its fix. ("Design twice" and the red flags derive from pstack's architect skill, Lauren Tan, MIT, via gstack.)

## 2. Code quality

- Organisation and module structure.
- Error-handling gaps and missing edge cases, named explicitly.
- Technical debt, fragility, needless complexity.
- Accuracy of ASCII diagrams in touched files.

### Shared-code rubric

- **Prove the callers:** at least two verified first-party source locations, with functions and lines. A plan review may use proposed callers, labelled as assumptions. Similar names alone do not prove equivalent behaviour; generated and vendored copies never count.
- **Reuse before extracting:** check existing helpers and libraries first; compare inputs, outputs, errors, side effects, security and runtime boundaries. Preserve differences callers need.
- **Keep the helper small:** name its destination, contract, the callers to migrate and the smallest adoption order. Avoid option-heavy helpers.
- **Account for the whole change:** lines removed, added and saved, separately for implementation and for tests plus integration. Say when the total grows.
- **Rank:** reliability gains and net savings first, then low adoption risk. Reject similarities with incompatible contracts.

Extraction is its own ledger entry; scope approval does not approve it.

## 3. Tests

1. **Detect the framework:** the `## Testing` section of `CLAUDE.md` or `AGENTS.md`; else configs (`vitest.config.*`, `jest.config.*`, `playwright.config.*`, `pytest.ini`), the `test` script in `package.json`, test file counts. Unknown framework: say so and continue; a new framework is a ledger entry, never installed during review.
2. **Trace every codepath:** from each entry point (route, handler, exported function, component render), follow input → transforms → outputs and side effects; at each step, what can go wrong (null, invalid, network failure, empty collection).
3. **Map user flows:** the full journey, plus interaction edges (double-submit, navigate away mid-action, stale page after 30 minutes, slow network, two tabs), visible error states (clear message or silent failure, can the user recover), and empty, single, maximum and 10,000-item states.
4. **Check each branch against existing tests** and rate them: ★★★ behaviour plus edges plus errors; ★★ happy path only; ★ smoke or existence check (never counts as coverage).
5. **Draw the coverage diagram:**

```
CODE PATHS                                   USER FLOWS
[+] src/lib/cart.ts                          [+] Add to bag
  ├── addItem()                                ├── [★★★ TESTED] add, then view bag — cart.test.ts:14
  │   ├── [★★ TESTED] happy path — :22         ├── [GAP] [→E2E] add without JavaScript
  │   └── [GAP] quantity over stock            └── [GAP] double-tap Add
  └── removeItem()
      └── [GAP] last item → empty state
COVERAGE: 2/6 paths (33%) · QUALITY ★★★:1 ★★:1 · GAPS: 4 (1 E2E)
```

6. **Choose the test kind:** end-to-end (`[→E2E]`) for flows across 3+ components, integration points where mocks hide real failures, and auth, payment or data-destruction flows; eval (`[→EVAL]`) for prompt or LLM-output changes; unit tests for pure functions, helpers and single-function edges.
7. **Regression rule:** when the plan puts existing behaviour at risk without regression coverage, that coverage is a critical requirement. The ledger asks how to cover it (behaviour to preserve, intended differences, acceptance assertions), never whether to skip it. A proposed rewrite is a regression risk, not proof of a break: name the callers and behaviour at risk.
8. **Value bar** for every proposed test (else extend an existing test or drop it): what behaviour it protects; what credible regression fails it; why existing coverage misses it; whether it needs a production seam (if so, test at the real boundary instead). A test that breaks under a behaviour-preserving refactor asserts implementation.
9. List **tests made obsolete** by the plan.

Fast path: all paths covered → "Test review: all new code paths have coverage", and still write the test plan.

## 4. Performance

- N+1 queries and access patterns; queries in loops; unbounded queries or caches; missing indexes.
- Memory: whole-file loads, unbounded arrays, listeners without cleanup.
- Caching opportunities and cache invalidation.
- Blocking calls without timeouts; slow or complex paths.
- Web pages: image weight and format, font loading, JavaScript bundle on first load, layout shift, animation cost on phones.

Give each finding its scale (rows, requests per second, bytes, frames) or mark it unknown. Never invent a benchmark.

## Cognitive patterns (apply throughout)

1. **State diagnosis:** is the team falling behind, treading water, repaying debt or innovating (Larson)?
2. **Blast radius:** trace worst-case harm to systems and people.
3. **Boring by default:** three innovation tokens; otherwise proven technology (McKinley).
4. **Incremental change:** strangler migrations and canaries over big bangs (Fowler).
5. **Systems over heroes:** design for a tired human at 3 am.
6. **Reversibility:** flags and incremental rollouts make mistakes cheap to undo.
7. **Failure is information:** blameless postmortems, error budgets.
8. **Conway's law:** design team and system boundaries together.
9. **DX signals quality:** slow builds and deploys predict quality trouble.
10. **Essential vs accidental complexity** (Brooks).
11. **Two-week smell:** a small feature taking two weeks signals structural trouble.
12. **Make the change easy first:** refactor before behaviour changes, in separate steps (Beck).
