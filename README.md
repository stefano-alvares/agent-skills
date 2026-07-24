# agent-skills

Self-authored [Agent Skills](https://code.claude.com/docs/en/skills) — forcing functions that impose a
frontier model's agentic habits (interpret → plan → build → verify, against external evidence) on
whatever model is doing the work. Written for Claude Code; the core system also ships as a portable
`AGENTS.md` for Codex, Cursor, and any AGENTS.md reader.

## The skills

| Skill | What it does |
|---|---|
| **frontier-gap** | The operating system: interpret the request, keep a nothing-skipped ledger, set a per-model failure-mode floor, plan by dependency+risk, build with a working-memory file, verify before done. `references/` has full protocols, per-model profiles, the evidence base, and cross-harness deploy. |
| **critic-pass** | Validation before "done" against external evidence (run it / fresh-context verifier) — never bare introspection, which measurably lowers accuracy. |
| **pixel-critique-loop** | Render the UI, screenshot desktop + mobile, critique the actual pixels before calling frontend work done. |
| **lean-build** | Pre-implementation gate: simplest thing that works + mission fit → a short build contract. |
| **fidelity-critique** | Grades UI on a low-fi → high-fi commitment ladder with cited evidence; names the next commitment. |
| **brand-idiom** | Replaces generic web components with ones derived from the brand's native idiom. |
| **design-ban-audit** | Mechanical grep audit for mid-fi design tells (gradient text, glassmorphism, …). |
| **mission-debug** | Traces "this feels wrong" product behavior to the contract/prompt/state rule that forces it. |
| **mission-systems-cleanup** | Post-implementation review: right system, clean boundaries, no excess code. |
| **assembly-line** | Research → draft → polish in fresh contexts with file handoffs, not one rotting session. |

Every claim in these skills is pinned to a published result or a logged real incident —
`frontier-gap/references/evidence.md` separates measured findings from marketing.

## Install

```bash
git clone https://github.com/stefano-alvares/agent-skills ~/.agents
# Claude Code registers skills via ~/.claude/skills — link the whole set:
ln -s ~/.agents/skills ~/.claude/skills   # or per-skill symlinks for a subset
```

For Codex / Cursor: see `skills/frontier-gap/references/deploy.md` (copies
`frontier-gap/assets/AGENTS.md` + `.cursor/rules` into a repo).

Sync across machines: edit → commit → push, `git pull` elsewhere.
