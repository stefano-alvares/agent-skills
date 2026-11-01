# Batch 2026-10-31: restore Stefano's skills, never forget them, fix the handoff system

## His words (verbatim)

> So now we know why the performance is so weird. You need to use these processes. /ship-spec /plan-forge
> Not sure what ship-plan is. maybe i merged them but forgot. Look through my custom skills and evaluate them. These things exist for a reason yk?

> Lets get them all sorted. Make sure that you dont forget to use them again, and fix the delegation system. set a goal and dont stop working

## Ship spec

Mission: his self-authored skills are back to their working method, every agent loads them at the right step, and the handoff system delivers work back without a person nudging it.

**Definition of shipped (checkable):**
1. `git -C ~/.agents diff --stat` shows the 21 Aug originals restored with only repoints and named merges; the October rewrite sits in `stash@{0}`.
2. The dead-reference grep (below) over `skills/*/SKILL.md` returns only intended mentions (feature-loop's archive note, brainiac-learning-intake).
3. Every changed `SKILL.md` has YAML frontmatter that parses, and a description with its original trigger phrases.
4. A `kanban_create` from an Atlas session that has not loaded ship-spec, plan-forge and to-tickets (or goal-split) is refused by the `planning-gate` plugin, and allowed once they are loaded.
5. A card created from a desktop session wakes Atlas: its subscription's `last_event_id` reaches the completion event.

**Ground truth (31 Oct, probed):** the rewrite was 34 files, +326 / −2,635 lines, in waves on 5 Sep, 1 Oct and 9 Oct, never committed. It is now `stash@{0}` in `~/.agents`. fidelity-critique and feature-loop were taken back from the stash, because their rewrites were evolutions. Desktop wakes: 0 of 13 delivered on stable v0.22.5; the fixes are on canary from 26 Oct. The review lane works (test card t_9524c3f8, real card c4b t_ce2c2726). `~/.claude/skills/ship-spec` is a separate copy identical to the original.

**Document map:** `docs/skill-evaluations/2026-10-31-rewrite-vs-original.md` holds the per-skill verdicts. Every skill has a bucket there: TASK (repoint or merge), KEEP-REWRITE (fidelity-critique), RETIRE as default (feature-loop, opt-in archive), or unchanged (brainiac-learning-intake).

## Decided (stamped into every card)

- **Base:** the 21 Aug original is the base. Add back only the rewrite lines the evaluation marks "keep".
- **Dead references and their repoints:**
  - Notion, Feature Loop filing and the Projects or Clients databases → "the project's canonical record when asked, else the reply".
  - `c3po_vault`, planning-standard and `/phase-plan` → remove.
  - `c3po_vault/context/voice.md` → "Stefano's voice profile file (location to be named by Stefano)".
  - ponytail → "simplest thing that works; reuse before building".
  - `WORKING_MEMORY.md` → "the batch file in docs/crew/ or the project's notes".
  - Forge and Raze profiles → planning by the lead, review by the independent reviewer.
  - Brainiac → remove (except in brainiac-learning-intake itself).
  - "commit at each green step" → "commits only with Stefano's explicit yes".
- **mission-systems-cleanup** is restored and stays, so references to it remain valid.
- **Shared by two harnesses:** these skills serve both Claude Code and Hermes. Write harness-neutral text, and where a tool is named, give both: Claude Code's preview tools, and Hermes's `node ~/.hermes/tools/shots/shots.cjs <url> <out> <routes>` (1440 and 390). `superpowers:*` skills are labelled "Claude Code only, optional".
- **raze-review keeps his original rules:** the ban on repeating a failed fix, and docs win over code. Stefano can override.
- **Descriptions:** keep the original trigger phrases. Add the rewrite's "skip for …" scope guard where the evaluation says so.
- **No commits.** Nothing outside the card's own skill folders is touched.

Dead-reference grep:

`rg -n "c3po_vault|Notion|ponytail|WORKING_MEMORY|planning-standard|/phase-plan|Brainiac|Forge|caveman|lean-build" ~/.agents/skills/<skill>/`

## Plan (plan-forge)

**VALUE:** his procedures run again, every time, for both teams.
**SYSTEM:** `~/.agents/skills` is the one source; Claude Code and the Hermes profiles symlink to it.
**REUSE:** the 21 Aug originals and the evaluation's per-skill lists.
**NOT BUILDING:** new skills (except the staged to-tickets), or edits to third-party skills.
**CHECK:** the dead-reference grep, plus frontmatter parsing, plus the gate test.

**Spike (riskiest step):** the canary update plus gateway restart, which can break every agent. Code update and restart go last, while the board is idle, with the pre-update snapshot as rollback. Weakest assumption: that canary's 25 Oct fixes make desktop wakes land. If they don't, the fallback is build batches from Telegram (already in SOUL).

**Waves:**
- **Wave 1, in parallel:**
  - k1, k2 and k3 (skill groups, disjoint folders, each Review: yes).
  - Atlas: the planning trio, fidelity-critique triggers, feature-loop archive note, README, links, the planning-gate plugin, memory.
- **Wave 2:** integrate and verify all of it (dead-ref grep, YAML parse, `has-skills.sh`).
- **Wave 3:** canary update; unsubscribe stale desktop wakes; gateway restart; wake test card.

## Cards

| Card | Skills owned (folders) | Review |
|---|---|---|
| k1 judgement core | logic-map, raze-review, brutal-honesty, critic-pass, falsify, frontier-gap | yes |
| k2 debug, intake, UI checks | logic-first-debug, mission-debug, idea-gate, skill-intake, design-ban-audit, pixel-critique-loop | yes |
| k3 design and writing | brand-idiom, voice-profile, pitch-craft, discussion-pack, mission-systems-cleanup | yes |
| Atlas (inline) | ship-spec, plan-forge, goal-split, fidelity-critique (description only), feature-loop (archive note), assembly-line (retire), README.md | — |

## Results (31 Oct, 16:40)

- **Planning trio:** ship-spec, plan-forge and goal-split were repointed by Atlas.
  - ship-spec gained a "new batch" section and the ship-spec → plan-forge → to-tickets hand-off.
  - plan-forge dropped c3po, ponytail and WORKING_MEMORY, and gained "a plan creates no permission gate".
  - goal-split now maps its goal doc, launch message and merge gate onto Kanban.
- **The other skills:**
  - k1 (t_3ca41ef9), k2 (t_5f7b2c27) and k3 (t_42f09dbd) ran in parallel; each got Argus PASS on the same card, with no changes requested.
  - Atlas re-checked independently: YAML parses for every changed skill, the dead-reference grep is clean (intended mentions: plan-forge's own title and its "absorbs the former lean-build" history line), and every keep-line is present.
  - Headings lost on purpose: voice-profile Step 7, pitch-craft Part 3 (Notion filing), frontier-gap Model profiles. logic-map Budgets and discussion-pack Step 5 were renamed, not lost.
  - mission-systems-cleanup needed no change.
- **Retired:** assembly-line (still in git history). feature-loop is an archived opt-in.
- **Links:**
  - `~/.claude/skills/ship-spec` now points to `~/.agents/skills/ship-spec`; the old copy is in `~/.claude/backups/`.
  - Atlas gained critic-pass, frontier-gap and skill-intake, and lost studio-site-redesign. Liaison gained voice-profile.
- **Never forget:**
  - The planning-gate plugin is live for atlas. Verified in a real Atlas session: the call was blocked and 0 cards were created.
  - Memory entry, plus SOUL lines for Atlas, Mason, Argus and liaison.
  - Staged for Stefano's approval: to-tickets (dff39521) and the studio-build chain note (a5849563).
