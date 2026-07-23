---
name: lean-build
description: >-
  Pre-implementation gate combining the ponytail ladder (simplest thing that works) with
  mission-systems-cleanup's review questions (right system, mission fit, reuse) — run BEFORE writing code so
  clean code is written from the start instead of reviewed into shape after. Use at the start of any feature,
  refactor, or multi-file change. Output is a short build contract the implementation must follow. Skip for
  trivial one-line edits. UI/design work gets a partial exemption (see UI clause) — minimalism rules produce
  mid-fi interfaces when applied to visual work.
---

# Lean Build

Review-after-build (mission-systems-cleanup) catches problems at the most expensive moment: after the code
exists. The ladder (ponytail) prevents them, but says nothing about whether you're building the right system
at all. This runs both BEFORE implementation, as one pass, and emits a contract.

## Step 1 — Mission fit (60 seconds, answer in one line each)

1. What user/app value does this create? If you can't say it plainly, stop and ask.
2. Is this the right *system* for that value, or just more code near the symptom?
3. Single authority: which one module owns the domain decision (dates, state, scores, ownership)?
   New logic goes there, not route-local.
4. What existing infrastructure/helper/pattern in this codebase already does part of this? Grep first.

## Step 2 — The ladder (stop at the first rung that holds)

1. Does it need to exist at all? Speculative = skip, say so.
2. Already in this codebase? Reuse it.
3. Stdlib does it? Use it.
4. Native platform feature covers it? (`<input type="date">`, CSS over JS, DB constraint over app code.)
5. Already-installed dependency solves it? Never add a new one for a few lines' work.
6. Can it be one line? One line.
7. Only then: minimum code that works.

Bug fix = root cause: grep every caller first; one guard in the shared function beats a guard per caller.

## Step 3 — The build contract (write it, then follow it)

```
VALUE: [one line]
SYSTEM: [where the logic lives and why there]
REUSE: [existing things this builds on]
FILES: [exhaustive list — anything not here needs a stated reason]
NOT BUILDING: [the abstractions/features deliberately skipped, and when to add them]
CHECK: [the one runnable check that fails if the logic breaks]
```

Deviating from the contract mid-build is allowed only out loud — name the change and why. Silent drift is
the failure this exists to stop.

## Rules during implementation

- No unrequested abstractions: no interface with one implementation, no config for a constant.
- Boring over clever. Deletion over addition. Fewest files.
- Deliberate shortcut with a known ceiling → `// lean: <ceiling>, <upgrade path>` comment.
- Unknown/missing state = fail fast and loud, never silently continue (see code-style.md).
- Non-trivial logic leaves ONE runnable check behind (the contract's CHECK line). No frameworks unless asked.
- Tests protect invariants and product rules, not prompt strings or incidental output.

## UI clause — minimalism rules do NOT govern visual quality

Applying "minimum viable" to design work is why UI comes out mid-fi. For UI/frontend tasks:

- The ladder still governs *mechanism* (reuse tokens/components, CSS over JS, no new deps).
- It does NOT govern *design ambition*. Design quality IS the spec — full sections, real typography scale,
  deliberate spacing/color systems, motion where it serves the design. Never "smallest diff that renders."
- Requires: design tokens + a ban-list (no gradient text, no glassmorphism, no layout-prop animations —
  see the project's DESIGN.md if present), then pixel-critique-loop before done.

## Never lean about

Input validation at trust boundaries, error handling preventing data loss, security, accessibility basics,
anything explicitly requested. Understanding the problem — read fully, then be lazy.

## Relationship to the parents

- `ponytail` (plugin, always-on): stays as the ambient floor. This skill is its explicit per-task front-end.
- `mission-systems-cleanup`: still the right tool for reviewing code that ALREADY exists (its 1-3-1 format).
  For new work, run lean-build instead — cheaper to prevent than to review.
