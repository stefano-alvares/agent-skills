# Team rebuild, 1 Nov 2026 (lead: engineering-god)

## His words (verbatim)

> i want you to make the best team possible for development work. with /brutal-honesty how would you rate the current setup? Look at my custom skills and the bot profiles, dont be biased towards anything. Read only for now.

> Do all the changes youve suggested, these are super good. Youre right now just critiquing, or you can take over atlas' role and build your own file, or take over implementer role. Id suggest atlas, but let me know.

Question round answers:
- Role: "Lead: I write a batch file and the core files (SOULs, merged skills, dev playbook) myself, send mechanical work to Sonnet subagents, then get one independent review"
- Liaison: "Keep it and fix the wiring: Atlas pins its writing skills on liaison cards, and liaison gets talk-normal"
- Claude Code crew plugin: "dont freeze, i use it sometimes, just dont pay attention to it. Basically use it to see how claude performs in the native harness to compare and improve"
- Atlas's commit-floor finding: "Yes, all of it" (baseline commit per repo on crew/baseline-2026-11-01 after a secrets scan, a standing yes for local agent commits on crew/* branches only, and 4 more git deny rules)

## Decided

- One source of truth: `~/.agents/skills`. Every profile link and every `~/.claude/skills` entry is an absolute symlink into it. Single-consumer skills (Atlas playbooks, Mason/Argus forks) stay profile-local.
- Cut skills are archived, never deleted: self-authored ones go to `~/.agents/archive/` (tracked), third-party ones to `~/.agents/archive/vendor/` (git-ignored, matching the README rule that third-party skills are not vendored).
- One planner (`plan-forge`, with light / standard / high-risk modes), one done-gate (`falsify`), one debugger (`diagnose`), one architecture review (`raze-review`), and one taste bar (`premium-site-standard`), where the project's own DESIGN.md / bans.md / decided.md win over every taste skill.
- Atlas works alone by default. Cards are for 3 or more file-disjoint units with a settled plan. Logic-heavy code is written by Atlas on Opus; Sonnet cards suit page work after the keyframe is approved, plus mechanical slices.
- Atlas auto-loads only `crew-board` (the shared board mechanics plus the router). `studio-build` (web) and `dev-build` (code) load per batch.
- Agents may commit locally on `crew/*` branches only (the pre-commit crew guard enforces this when HERMES_HOME is set). Push and merge to main stay his.
- The crew plugin in `~/Desktop/crew` and `~/.claude/skills/studio-site-redesign` are left untouched.

## Defaults (he can override any)

- The voice profile's canonical path is `~/Desktop/Business-projects/business vault/voice-profile.md`.
- prototype is archived rather than merged into the bundled `sketch` skill.
- After the baseline commit, each repo stays on `crew/baseline-2026-11-01` (working tree unchanged). Previous branches are untouched.
- Repos outside the team (minicardiac-marketing 358 files, training-app, student-council, others) were not committed; they are listed in the report.
- Claude Code crew files that reference merged skills (critic-pass, pixel-critique-loop, goal-split, frontier-gap, logic-first-debug, diagnosing-bugs, feature-loop) are left as they are; the report says which.

## Done already (with evidence)

- Backups: `~/.hermes/backups/team-rebuild-2026-11-01/` (profiles.tgz, agents.tgz, claude-skills.tgz, SOULs, configs, atlas pending).
- Baseline commits on `crew/baseline-2026-11-01`: kuva-botanicals 4afd585 (396 files; 2 gitleaks hits were file-hash false positives in evidence/compact-full-rebuild-checks.json), sol-sports 2a93983, studio-naach 6741e2d, revision-app 4686a76, The One Jewellery Store 1a4c661, forge-bot 191271d. All clean afterwards.
- Crew guard pre-commit hook in kuva, sol-sports, naach, webforge (common dir _archive/webforge-vite), revision-app, The One, forge-bot. Tested in a scratch repo: an agent commit on main is blocked, his own commit on main is allowed, an agent commit on crew/x is allowed.
- Deny rules added on atlas, implementer, reviewer, liaison (41 each): git restore, checkout -- / . / HEAD --, stash drop/clear, worktree remove --force/-f, --no-verify, commit -n/-an/-nm, core.hookspath.

## Plan

FILES: ~/.agents/skills/*, ~/.agents/archive/*, ~/.agents/.gitignore, ~/.claude/skills/* (symlinks only),
~/.hermes/profiles/{atlas,implementer,reviewer,liaison,engineering-god,codoach}/skills/* (links; local skills),
the SOULs of atlas, implementer, reviewer, liaison and engineering-god, the atlas and engineering-god config.yaml,
~/.hermes/tools/team-skill-check.py (new).

1. Plumbing (script, dry run first): archive the cut skills; centralize identical multi-profile copies (project-health, vibe-security, next-best-practices, supabase-postgres-best-practices); move the 19.7 KB design-taste-frontend into ~/.agents; reconcile the 9 diverged ~/.claude copies; rebuild every profile's link set from the manifest below; repair broken links on codoach and engineering-god; write .gitignore.
   PROOF: team-skill-check reports 0 broken links, 0 plain duplicates in ~/.claude/skills, and every SOUL/card skill resolves.
2. Core files (lead): plan-forge, falsify, diagnose, raze-review, premium-site-standard, studio-build, crew-board, dev-build, and 5 SOULs.
3. Mechanical fixes (3 Sonnet subagents, disjoint files): G1 design skills, G2 misc shared skills, G3 dev/reviewer/liaison locals.
4. Configs: atlas auto_load [crew-board]; engineering-god delegation Sonnet, background_review off, compression 0.85.
5. Verify: team-skill-check, boot checks per profile, an Atlas planning check (one web brief, one code brief), and a tool proof (deny rules, guard).
6. Independent review (fresh context), fix the findings, commit ~/.agents locally (self-authored only), write CHANGES.md.

KILL-TEST: the riskiest assumption is that moving Atlas's playbook from auto-load to on-demand does not cost
it the web rules. Mitigation: crew-board (auto-loaded) carries the router line, and the SOUL names the load step;
the planning check must show Atlas loading studio-build for the web brief.

## Manifest

Archive (self): frontier-gap, feature-loop, critic-pass, mission-systems-cleanup, logic-first-debug, ship-spec, goal-split, pixel-critique-loop.
Archive (vendor): ask-matt, wayfinder, triage, setup-matt-pocock-skills, implement, improve-codebase-architecture, to-spec, to-tickets, grill-with-docs, graphify, find-skills, stitch-design-taste, brandkit, prototype, diagnosing-bugs, design-taste-frontend (87 KB version).
Archive (profile-local): atlas prospecting, fp-check, constraint-driven-development, plan-eng-review (its review sections become plan-forge/references/high-risk-review.md); reviewer fp-check, constraint-driven-development; implementer deprecation-and-migration (expand/contract folded into supabase-postgres-best-practices).

Link sets (S = ~/.agents/skills, L = profile-local, B = bundled):
- atlas: L crew-board, studio-build, dev-build, ship-check, retro; B hermes-agent, web-pentest; S premium-site-standard, plan-forge, logic-map, diagnose, mission-debug, falsify, raze-review, brutal-honesty, brand-idiom, fidelity-critique, design-ban-audit, impeccable, design-taste-frontend, project-health, vibe-security, resolving-merge-conflicts.
- implementer: L tdd (studio fork), knip, code-simplification, ast-grep; B hermes-agent; S premium-site-standard, brand-idiom, design-ban-audit, falsify, diagnose, next-best-practices, supabase-postgres-best-practices, project-health, vibe-security.
- reviewer: L sdlc-review (+ code-review lens), qa, differential-review; B hermes-agent; S falsify, diagnose, design-ban-audit, vibe-security, project-health, next-best-practices, supabase-postgres-best-practices.
- liaison: L cold-email; B hermes-agent; S discussion-pack, pitch-craft, voice-profile, brand-idiom, talk-normal, brutal-honesty.
- engineering-god, codoach: repair only (absolute links to live targets; drop links to archived or missing skills).

## Learned

(filled at the end)
