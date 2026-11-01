# Skill evaluation: originals vs the uncommitted rewrite (31 Oct 2026)

Evaluator: Atlas (Hermes), with three read-only Sonnet helpers comparing `git show HEAD:skills/<name>/SKILL.md` (21 Aug 2026) against the working tree. Nothing in `skills/` was changed by this evaluation.

## What happened

- The working tree of this repo was rewritten in place and never committed: 34 files, +326 / −2,635 lines, in three waves.
  - **5 Sep:** the "core bot rebuild" (`~/hermes-bot-sync/docs/skill-evaluations/cleanup-20260905-160950/status.md`: "Rewrote 18 canonical shared skills"). Its aim was to make planning, delegation and review conditional instead of a compulsory pipeline.
  - **1 Oct and 9 Oct:** further passes. The session that made them was not found in the Claude Code, Codex or Hermes logs.
- The aim was right: clear work should not be forced through planning. But most rewrites deleted the method along with the compulsion, so a skill now says *when* it applies but no longer *how* to do it. Descriptions shrank to about 10 words, which also stopped them auto-loading.
- Claude Code loads these through symlinks, so it runs the cut versions too. The exception is `ship-spec`: `~/.claude/skills/ship-spec` is a separate copy identical to the original. Hermes Atlas linked the same files.
- Usage since Aug, Claude Code (Skill tool calls): brutal-honesty 50, pixel-critique-loop 22, plan-forge 14, ship-spec 13, logic-map 11, logic-first-debug 11, brand-idiom 7, design-ban-audit 6, mission-debug 5, goal-split 4, raze-review 4, feature-loop 4, to-tickets 3, skill-intake 2, frontier-gap 2.
  - Hermes Atlas, in its 7 planning sessions (14–30 Oct, 55 cards): ship-spec 0, plan-forge 0, goal-split 0.

## Verdicts

Lines are original → current.

| Skill | Lines | Verdict | Restore / keep |
|---|---|---|---|
| ship-spec | 116 → 19 | RESTORE | Ground truth by probe, document map, invariants, definition of shipped, the DONE/REFUTED/TASK/ACCEPTED LOSS disposition rule, output skeleton, routing to to-tickets / goal-split / plan-forge. Widen the trigger so it fires for any substantial batch, not only piled-up audits. |
| plan-forge | 112 → 22 | RESTORE | Interpret plus the ledger of buried asks, evidence pass, order by dependency and risk with the spike first, the FILES / CHANGE / PROOF / RISK step contract, the build contract (VALUE / SYSTEM / REUSE / FILES / NOT BUILDING / CHECK), kill-test then lock, deviations out loud. Keep from the rewrite: a plan is not a permission gate; commits need explicit authority. |
| goal-split | 141 → 18 | RESTORE | Partition by file ownership, decide before dividing, mini-spec shared seams, cross-dependencies with a fallback, zero-context goal docs, launch message as a pointer, merge gate. Repoint the goal doc to the Kanban card body or batch file, the launch to `kanban_create`, and the merge gate to Atlas integration plus Argus's same-card review. |
| logic-map | 235 → 21 | MERGE | Box format (takes → gives → owns → fails), one owner per invariant, violation test, mismatch table, decomposition criteria, output template, red flags. Keep the rewrite's team-handoff paragraph. |
| raze-review | 178 → 21 | RESTORE | Mode A/B, blind architect, history registers, escalation rules, F-ledger, confidence contract. **Policy changes need Stefano:** the rewrite reversed the repeat-fix ban and "docs win". |
| brutal-honesty | 72 → 17 | MERGE | Fact / inference / guess labels, "say don't-build first", the pushback script, the hedge-word ban, red flags, the wide trigger. Keep "a no-problem result is valid". |
| critic-pass | 159 → 18 | MERGE (small) | A checklist by failure class (grep every usage, tick each requirement) and the MUST / SHOULD / ACCEPTED triage. |
| falsify | 72 → 16 | MERGE | Sibling table and test table, the Verified / Unverified report, "misses land on the undo path". |
| frontier-gap | 97 → 20 | MERGE | Spec template, ledger of buried asks, floor rules. Its Protocol 3 moved into plan-forge, which was then cut, so restore it there. |
| logic-first-debug | 218 → 18 | MERGE, leaning restore | Phases 0–4, the "map before reading code" rule (the rewrite reversed it), the impossibility test, the output format, the worked example. Keep the rewrite's "a contradiction brackets hypotheses, it doesn't prove the cause". |
| mission-debug | 106 → 16 | MERGE | The six-layer ladder, absences, promise extraction and persona walk, the walked-versus-suspected list, the output format. |
| idea-gate | 121 → 16 | RESTORE | Mode choice, the six forcing questions asked one at a time, the scored table and thresholds. Repoint filing and voice; keep "not execution authority". |
| skill-intake | 128 → 18 | RESTORE | Untrusted-source stance, capture checklist, scored dimensions and gates, the overlap check, the adopted-skill checklist. Drop Notion and Brainiac. |
| design-ban-audit | 33 → 40 | MERGE | Restore "every hit is a finding: fix it or justify it in one line", the five greps as default bans, and "extend when a new tell is caught" (into the project's `bans.md`). Keep "read bans.md first". |
| pixel-critique-loop | 122 → 16 | MERGE | "Never leave a render unlooked-at", the loud no-render statement, the six questions verbatim, top 1–3 problems, re-look after each fix, the stop rule, two passes for new pages. Name 1440 / 390 and `shots.cjs`. |
| brand-idiom | 263 → 271 | MERGE, close to restore | The original description, 4–6 candidates, 1→3→1, "every row goes through the full walk". Keep the corrected Step 0 sentence and the Boundaries line. |
| fidelity-critique | 180 → 198 | KEEP-REWRITE | It evolved rather than being cut. Optionally restore the two trigger phrases. |
| feature-loop | 176 → 179 | RETIRE as default | Keep it as an explicit opt-in archive. Salvage `decision-burst.md` and the pre-commit proof hook. |
| voice-profile | 124 → 16 | MERGE | Counting checklist, output template, banned-word seed list, the before/after proof. Stefano names the current file location. |
| pitch-craft | 100 → 15 | MERGE | Vagueness tests, the one-sentence line, "name the single weakest lever", the definition of concrete, the one next move. |
| discussion-pack | 146 → 44 | MERGE | Trace every line to a file, force one outcome, the seven-section pack (money: agreed / open / do not commit to; landmines), the post-call log. Keep the new website-discovery reference. |
| brainiac-learning-intake | 107 → 107 | unchanged | |

Also deleted in the working tree: `mission-systems-cleanup` (several originals route to it) and `assembly-line`.

## Dead references to repoint during the restore

Notion control plane and Projects / Clients databases; `c3po_vault` (planning-standard, `/phase-plan`, voice.md, clients/); the Forge and Raze profiles; ponytail; `WORKING_MEMORY.md`; model profiles folders; "commit at every green step" (commits need Stefano's yes); `mission-systems-cleanup`; Brainiac (added by the rewrite).

## Who loads what (Hermes)

- **Atlas:** ship-spec → plan-forge → to-tickets for every batch bigger than a quick fix. Also logic-map, goal-split, brutal-honesty, raze-review, logic-first-debug, brand-idiom, fidelity-critique, design-ban-audit, pixel-critique-loop as the preview rubric. Add critic-pass, frontier-gap and skill-intake.
- **Mason:** pixel-critique-loop after each section and before handoff; design-ban-audit before handoff on UI; falsify; brand-idiom, but only for elements the handoff does not cover.
- **Argus:** critic-pass on every review, design-ban-audit on UI diffs, falsify on key tests. Output stays PASS or one finding.
- **liaison:** pitch-craft, discussion-pack, and reading the voice-profile file before drafts in Stefano's name.

## Proposed execution (needs Stefano's yes)

1. Make the original versions the working tree, keeping the October rewrite recoverable: `git -C ~/.agents stash push -m "rewrite-2026-09-05..10-09" -- skills README.md`.
2. Repoint the dead references and fold in the rewrite lines marked "keep" above, one card per skill group with no shared files. Argus checks each card mechanically: no dead references left (grep), frontmatter parses, the named sections are present.
3. Stefano reads the diffs and commits them himself.
