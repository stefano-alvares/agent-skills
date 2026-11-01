---
name: mission-systems-cleanup
description: Review an implementation before cleanup for app mission fit, system architecture, infrastructure choice, redundant or excessive code, clean client/server or package boundaries, test efficiency, and whether the code advances the app's user value. Use when the user asks to review, audit, clean up, simplify, harden, or decide whether an implementation built the right systems before making changes.
---

# Mission Systems Cleanup

Use this skill to review first, then clean up only after the review direction is clear. The goal is not generic neatness. The goal is to make sure an implementation uses the right systems, removes redundancy, fits the app's existing infrastructure, and strengthens the app's core value to its users.

## Hard Rule

Review first always. Do not edit code before producing the review output.

If the user already asked for fixes, still review first. After the review, implement only the recommended path unless the user chooses a different solution.

## Required Context Pass

Before judging the implementation:

1. Read the user's named plan/spec/handoff/doc first.
2. Read app mission/product/design docs that define the value the app provides.
3. Inspect the touched code, nearby patterns, package boundaries, and tests.
4. Identify existing infrastructure that should have been reused.
5. Check git status and avoid reverting unrelated dirty-tree work.

Do not rely on the implementation's own structure as proof that it is right. Treat it as a proposal to validate against the app.

## Review Output

Default to the 1-3-1 breakdown.

### Problem

State one clear root problem. Ground it in code, docs, app purpose, or system behavior. Avoid vague complaints like "needs cleanup."

Answer:
- What is wrong or risky?
- Why does it matter for the app's mission/user value?
- What system boundary or infrastructure choice is involved?

### 3 Best Solutions

Give exactly three good, viable solutions. All three must be relevant and fitting. Do not include a weak option as filler.

For each solution, include:
- what changes
- why it fits the app
- tradeoff or risk
- verification path

### Recommendation

Pick the best solution for this app now. Explain why it is the best balance of mission fit, system cleanliness, efficiency, and risk.

## Small-Issue Format

Use the shorter format only when the issue is genuinely small: little or no behavior impact, no architecture risk, no product-direction risk, and one obvious cleanup.

Still include the breakdown:

### Problem

What is wrong, redundant, or not clean.

### Recommended Solution

The one obvious fix.

### Recommendation

Why this is enough and what verification proves it.

## Review Checklist

Use these questions to find the real problem:

- What app value is this implementation supposed to create?
- Did it build the right system, or just add more code?
- Is there a single authority for domain decisions like dates, plans, score, state, or ownership?
- Are deterministic decisions kept out of LLM voice/prose layers?
- Are DB/network reads hidden inside logic that should be pure?
- Are client/server, package, and route boundaries clean?
- Is existing infrastructure reused instead of duplicated?
- Is there redundant code, copy-pasted helpers, old fallbacks, or route-local domain logic?
- Are tests protecting system invariants and product rules, or just prompt strings and incidental output?
- Is the suite efficient enough in real runtime, even if the count is high?
- What should be deleted, merged, moved, or simplified?

## Implementation Rules

After the review is accepted or the user says to proceed:

1. Implement the recommendation only, unless the user chooses another solution.
2. Keep scope to cleanup. Do not add product features.
3. Prefer deleting duplication and using existing infrastructure over adding abstractions.
4. Add tests only where they protect system invariants, boundaries, or likely regressions.
5. Make pure logic testable without DB/network mocks when feasible.
6. Preserve migration fallbacks only when they reduce rollout risk.
7. Verify with the strongest practical checks: typecheck, targeted tests, full tests, and build when the environment allows it.

## Final Handoff

End with:

- what changed
- what user value/system value it now gives the app
- what verification passed
- any environment caveat, such as build blocked by networked font fetches
- any dirty-tree caveat if unrelated changes existed
