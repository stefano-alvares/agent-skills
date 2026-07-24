---
name: assembly-line
description: >-
  Stefano's phased work pattern (from c3po_vault CLAUDE.md, made invocable): research agent → draft agent →
  polish/verify agent, each phase in fresh context with the previous phase's OUTPUT FILE as input. Use for
  content production (marketing drafts, reports, specs), multi-source research, or any work where one long
  session degrades quality. Backed by Anthropic guidance: fresh-context resets with file handoffs beat one
  long session (context degradation, Sonnet "context anxiety").
---

# Assembly Line

One session doing research + drafting + polish rots its own context: by the polish phase it defends the
draft instead of judging it. Split into phases; the FILE is the handoff, never chat history.

## The line

1. **Research** — gather, verify sources, output `01-research.md`: findings + citations + open questions.
   No drafting.
2. **Draft** — fresh context (`/clear` or subagent). Input: `01-research.md` only. Output: `02-draft.md`.
   No new research; gaps become `[GAP: …]` markers, not invented facts.
3. **Polish + verify** — fresh context. Input: `02-draft.md` + `01-research.md`. Checks every claim in the
   draft against the research file (docs-vs-source rule), resolves or escalates GAP markers, fixes voice.
   Output: final artifact.

Rules:
- Each handoff file must be self-contained — the next phase reads NOTHING else (frontier-gap Protocol 1
  benchmark: a stranger could execute it).
- Phase outputs live in the project folder (or scratchpad for throwaway work), named `NN-phase.md`.
- Verifier phase is externally attributed by construction — it judges "the draft", not "my draft". Don't
  collapse phases to save time; that recreates the single-session failure.
- 2 phases (draft → verify) is fine for small work. YAGNI applies to phases too.
