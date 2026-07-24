# Deploy the system to Codex / Cursor / any harness

In Claude Code the family loads as skills automatically. Other harnesses don't read `~/.claude/skills/`,
so the whole system also ships as portable, self-contained instruction files in this skill's `assets/` —
the forcing functions compressed into one sequenced operating system, tuned for the exact models that run
there (Composer 2.5, GPT-5.5/Codex).

- **`assets/AGENTS.md`** — the canonical orchestrator. One file, the open `AGENTS.md` standard, read
  natively by **Codex** (repo root) and **Cursor** (and Copilot, Windsurf, Aider, …). It inlines the
  floor, the loop, the critic-pass checklist, the render-and-look step, and per-model preambles — so it
  works with no skill files present.
- **`assets/cursor-rules/*.mdc`** — Cursor's conditional layer: an always-on orchestrator
  (`00-operating-system.mdc`) plus a glob-scoped UI rule (`40-render-and-look.mdc`) that only attaches on
  frontend files, so it doesn't bloat backend sessions.

Install (per repo):

```bash
SK=~/.agents/skills/frontier-gap/assets
cp "$SK/AGENTS.md" ./AGENTS.md                 # Codex + Cursor + any AGENTS.md reader
mkdir -p ./.cursor/rules && cp "$SK"/cursor-rules/*.mdc ./.cursor/rules/   # Cursor conditional layer
ln -sf AGENTS.md CLAUDE.md                      # optional: same system for Claude Code in this repo
```

For a personal cross-repo default in Codex, also copy `AGENTS.md` to `~/.codex/AGENTS.md` (lowest
precedence; repo files layer on top). Keep the root file well under Codex's 32 KiB cap — it already is.
Notes: `.cursorrules` is deprecated (don't use it); Cursor User Rules live in the settings UI, not a
committable file, so the portable system goes in `.cursor/rules/` + `AGENTS.md`.
