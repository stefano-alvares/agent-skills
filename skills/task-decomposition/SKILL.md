---
name: task-decomposition
description: Decompose complex coding tasks into independent, parallelizable subtasks with explicit file scopes, dependency ordering, and per-task subagent prompts. Use whenever the user asks to break down a large task, prepare work for parallel coding agents, or create a build plan.
source: /Users/stefanoalvares/.agents/skills/task-decomposition
---

# Task Decomposition for Parallel Coding Agents

Decompose complex coding tasks into independent, parallelizable subtasks with **explicit file scopes** and **dependency ordering**. Each subtask gets a ready-to-dispatch prompt for a subagent (Pi instance or subagent) with bounded context.

## When to Activate

- The user says "decompose [task]", "break down", "parallel plan", "subagent plan", or similar
- A task touches 5+ files, spans multiple concerns, or takes >20 minutes to describe
- The user asks to prepare work for multiple agents or parallel sessions
- After a plan/feature is agreed upon but before implementation starts

## When NOT to Activate

- Single-file changes, hotfixes, or bug patches under 5 files
- Pure refactoring of one module (just describe the refactor)
- Exploration/research tasks (no code boundaries to enforce)

## Core Principles (from Claude's Subagent-Driven-Development)

The best parts of Claude's official subagent skill are preserved and adapted for Pi:

1. **Fresh context per task** — each subagent gets exactly the files it needs, nothing more
2. **Explicit file boundaries** — each subtask declares which files it creates/modifies; overlapping scopes = not parallelizable
3. **Two-stage review** — after each subtask: spec compliance review first, then code quality review
4. **Implementer status protocol** — each subagent reports DONE / DONE_WITH_CONCERNS / NEEDS_CONTEXT / BLOCKED
5. **Model selection by complexity** — cheap model for mechanical tasks, expensive model for reviews and integrations

## The Process

```
┌─────────────────────────────────────────────────────────────┐
│ Phase 0: DECOMPOSE (this skill)                              │
│  • Analyze the task against the codebase                     │
│  • Identify independent vs dependent subtasks                │
│  • Map file scopes (no overlap = parallelizable)             │
│  • Output: numbered build plan with dependency graph          │
│  • Output: per-task subagent prompts ready to dispatch        │
└──────────────────────┬──────────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────────┐
│ Phase 1: EXECUTE (sequential with this skill)                │
│  • For each task (respecting dependency order):               │
│    a. Dispatch subagent with scoped prompt                    │
│    b. Subagent reports status                                 │
│    c. Spec compliance review → loop if issues                 │
│    d. Code quality review → loop if issues                    │
│    e. Commit or escalate                                      │
└──────────────────────┬──────────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────────┐
│ Phase B: EXECUTE (parallel — requires multi-pi-launcher)     │
│  • Spawn multiple Pi instances, one per parallel batch        │
│  • Each instance gets its scoped prompt                      │
│  • Monitor for merge conflicts after completion               │
│  • Merge results and run review phase                         │
└─────────────────────────────────────────────────────────────┘
```

## Phase 0: Decomposition Rules

When decomposing a task:

### Step 1: Survey the Codebase

Before decomposing, read the relevant parts of the codebase:
- `ls -R` the directories the task will touch
- Read key files: entry points, route definitions, shared types, configuration
- Understand existing patterns (file structure, naming conventions, how features are organized)

### Step 2: Extract Subtasks

Break the task into the smallest independent units that make sense. Each subtask must have:

- **A clear deliverable** — one feature, one module, one integration
- **Explicit file scope** — which files it creates, which it modifies
- **Dependencies** — which other subtasks it depends on (or "none")
- **Complexity level** — `mechanical` (1-2 files, straightforward), `integration` (multiple files, coordination), or `architecture` (design judgment needed)
- **Estimated duration** — rough minutes for a competent developer

### Step 3: Analyze Parallelizability

Two subtasks are parallelizable if:
- They touch **zero overlapping files**
- They have **no data dependency** (one doesn't call/use the other's output)
- They don't share **side effects** (e.g., both modifying the same DB table schema, both adding to the same route file)

If subtasks must share a file (e.g., both add routes to `src/routes.ts`):
- **Option A**: One subtask owns the file entirely and the other declares it as a dependency
- **Option B**: Split the shared file (e.g., `src/routes/auth.ts` and `src/routes/billing.ts`, imported from a central registry)

### Step 4: Output the Build Plan

```markdown
# Build Plan: [Task Name]

## Parallel Execution Map

### Batch 0 (no dependencies — run ALL in parallel)
| # | Subtask | Files | Complexity | Est. |
|---|---------|-------|------------|------|
| 0.1 | Auth middleware | Create: src/middleware/auth.ts<br>Modify: src/app.ts | integration | 30min |
| 0.2 | Rate limiter | Create: src/middleware/rate-limit.ts | mechanical | 20min |
| 0.3 | DB schema for users | Create: prisma/schema.prisma | mechanical | 10min |

### Batch 1 (depends on Batch 0)
| # | Subtask | Depends On | Files | Complexity | Est. |
|---|---------|-----------|-------|------------|------|
| 1.0 | Login endpoint | 0.1, 0.3 | Create: src/routes/auth.ts<br>Modify: src/routes.ts | integration | 45min |

### Batch 2 (depends on Batch 1)
| # | Subtask | Depends On | Files | Complexity | Est. |
|---|---------|-----------|-------|------------|------|
| 2.0 | Billing dashboard | 1.0 | Create: src/routes/billing.ts, src/pages/billing.tsx | integration | 60min |

**Total serial estimate:** ~165min
**Parallel estimate (Batch 0 parallel):** ~135min
**Parallelism gain:** 30min saved by running Batch 0 in parallel

## Subtask Details

### Task 0.1: Auth Middleware
**Description:** [2-3 sentence description of what to build]
**Files to create:** `src/middleware/auth.ts`
**Files to modify:** `src/app.ts` — add middleware registration
**Dependencies:** None
**Complexity:** integration
**Subagent prompt:** [see prompt template below]
```

### Step 5: Generate Per-Task Subagent Prompts

For each subtask, generate a ready-to-dispatch prompt using the implementer prompt template below. The dispatcher uses this to feed a subagent.

## Implementer Dispatch Template

Adapted from Claude's subagent-driven-development skill, with Pi-specific changes:

```
You are implementing Task [N]: [task name]

## Context
[2-3 sentences: what this task is, where it fits in the larger system]

## Codebase Structure
[Relevant parts of the repo structure — only directories this task touches]

## Files in Scope

### Existing files you MUST read before touching:
- `path/to/file.ts` — [what it does, what to preserve]

### Existing files you MAY modify:
- `path/to/file.ts` — [how to modify it, what to preserve]

### New files to create:
- `path/to/new-file.ts` — [what it should contain]

## Requirements

[Paste the exact requirements / spec for this task]

## Constraints

- **Do NOT modify files outside the list above** unless you discover a genuine need — if so, flag it as a concern and ask before proceeding
- Follow existing patterns in the codebase for naming, structure, and style
- Write tests that verify behavior, not just coverage
- Keep new files focused — one responsibility per file

## Before You Begin

If anything is unclear about:
- The requirements or acceptance criteria
- The approach or implementation strategy
- Dependencies, assumptions, or existing code you need to understand

**Ask now.** Don't guess or make assumptions.

## When Done: Self-Review

Before reporting back, review your own work:
1. Did I implement everything in the requirements?
2. Did I miss any edge cases?
3. Is the code clean, named clearly, following existing patterns?
4. Did I avoid overbuilding?
5. Do tests actually verify behavior?

Fix any issues you find before reporting.

## Report Format

Return your status using exactly one of:

**STATUS: DONE** — Everything implemented, tested, self-reviewed.
**STATUS: DONE_WITH_CONCERNS** — Work is complete but you have doubts about correctness, scope, or approach. List concerns.
**STATUS: NEEDS_CONTEXT** — You need information not provided (specific files, API docs, config). Describe what.
**STATUS: BLOCKED** — You cannot complete this task. Explain the blocker specifically.

Also report:
- Files changed (created/modified)
- What you tested and results
- Any concerns or flags
```

## Spec Compliance Review Template

```
You are reviewing whether Task [N]'s implementation matches its specification.

**DO NOT trust the implementer's report — verify by reading the actual code.**

## What Was Specified

[paste the task requirements]

## What Implementer Claims

[paste the implementer's report]

## Your Job

Read the actual code in these files:
- [list of files changed]

Verify:
1. **Missing:** Did they build everything requested? Anything skipped?
2. **Extra:** Did they add features not in spec?
3. **Misunderstood:** Did they implement the right thing the wrong way?

Report:
- ✅ Spec compliant (everything matches)
- ❌ Issues found: [list with file:line references]
```

## Code Quality Review Template

```
You are reviewing Task [N]'s implementation for code quality.

## What Was Built

[implementer's summary of what they built]

## Your Job

Read the actual code in these files:
- [list of files changed]

Check:
1. **Single responsibility:** Does each file have one clear purpose?
2. **Naming:** Do names accurately describe what things do?
3. **Testing:** Do tests verify real behavior (not just mocking)?
4. **Patterns:** Does this follow existing codebase conventions?
5. **No overbuilding:** YAGNI — is there unnecessary abstraction?
6. **File growth:** Did this create files that are already too large?

Report:
- Strengths
- Issues: [Critical / Important / Minor]
- Assessment: approve / approve-with-minor-notes / needs-fixes
```

## Implementer Status Protocol

Handle each implementer status appropriately:

| Status | Meaning | Action |
|---|---|---|
| DONE | Work complete, tested, self-reviewed | Proceed to spec compliance review |
| DONE_WITH_CONCERNS | Work done but implementer has doubts | Read concerns first, address correctness issues before review |
| NEEDS_CONTEXT | Missing information | Provide the context, re-dispatch |
| BLOCKED | Cannot complete | If context → provide + re-dispatch. If complexity → escalate. If scope → split into smaller tasks. |

**Never** silently proceed past a BLOCKED status. Never retry the same task with the same instructions without changing something.

## Model Selection Guide

| Task type | Recommended model |
|---|---|
| Mechanical (1-2 files, clear spec, TDD) | Cheapest/fastest available |
| Integration (multiple files, coordination) | Mid-tier model |
| Review (spec compliance, code quality) | Most capable model available |
| Architecture / design judgment | Most capable model available |

## Phase B: Parallel Execution Notes (for the launcher)

When the multi-pi-launcher (Phase B) is available:

1. **Batch = parallel group** — all tasks in a batch spawn simultaneously
2. **Each Pi instance gets** its own system prompt scoped to its file boundaries
3. **File watcher monitors** for conflicts (two instances writing to the same file)
4. **After each batch completes**, run reviews sequentially before starting the next batch
5. **Conflict resolution** — if two subagents modified the same file, the coordinator agent merges with git diff

## Anti-Patterns (Never Do These)

- **Don't** dispatch subagents with the full session context — always curate what they see
- **Don't** let a subagent read the full plan file — paste only its task's text
- **Don't** skip reviews because "it looked fine" — both spec and quality review are mandatory
- **Don't** accept DONE from an implementer without self-review first
- **Don't** start code quality review before spec compliance passes
- **Don't** dispatch multiple implementers on overlapping file scopes (they WILL conflict)
- **Don't** ignore a BLOCKED status — escalate, don't retry blindly
- **Don't** move to the next task while the current one has open review issues
