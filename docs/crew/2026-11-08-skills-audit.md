# Skills audit and gap fill, 8 Nov 2026 (Claude Code cloud session)

## His words (verbatim)
> Ah ok cool. Anyways, could you critique all my skills individually and as a whole process, and rate each on 10? Let's fill the gaps and improve

> done, github is connected now, push it

> But make  a note of your changes.

1. Critique every skill individually  2. Critique them as a whole process  3. Rate each out of 10
4. Fill the gaps and improve  5. Push it  6. Make a note of the changes (this file)

## Ship spec
Mission: his skills are scored honestly, and the gaps that can be fixed without his taste calls are fixed and pushed.
Definition of shipped:
- `python3 scripts/check-skills.py` -> `OK: 18 active and 7 archived skills checked.`
- `docs/skill-evaluations/2026-11-08-full-audit.md` -> a score and a critique for each of the 18 active skills, plus the process verdict
- `git ls-remote origin claude/crew-skill-repo-check-d4v6xq` -> the local HEAD
- He reads the audit and this note -> needs his eye
Ask ledger:
| # | Ask | Bucket | Done-check |
|---|---|---|---|
| 1 | Critique each skill | DONE | audit, "Per skill" section |
| 2 | Critique the whole process | DONE | audit, "Verdict" and "The process as a whole" |
| 3 | Rate each out of 10 | DONE | audit, "Scores" table, 18 rows |
| 4 | Fill gaps and improve | DONE, except four taste or ownership calls | "What changed" below; the rest under Needs your call |
| 5 | Push | DONE | Close-out |
| 6 | Note the changes | DONE | this file |
Out of scope: the archived skills, the profile-local Hermes skills (crew-board, studio-build, dev-build,
quality-layer), the crew plugin in `~/Desktop/crew`, and the Hermes tools. None are in this repo.
Needs your call: grill-me rewrite or retire; commit the Hermes tools to this repo; give
premium-site-standard a PASS/FAIL output; name where client records live for discussion-pack. Details and
recommendations are in the audit's "Needs your call".

## Decided
- 8 Nov: fixes stay surgical (no rewrites), because the in-place rewrite of 5 Sep to 9 Oct had to be
  parked and the originals restored.
- 8 Nov: proposed changes that are his taste or need his facts are recommended, not made.

## What changed
Commit `bce0f0d` on `claude/crew-skill-repo-check-d4v6xq` (16 files, +608 / -64 against `ce813f5`).

| File | Change | Why |
|---|---|---|
| `skills/falsify/SKILL.md` | New step 7: at batch end, run each Definition of shipped check, settle every ask, write the Close-out with Learned lines that go to skill-intake. New "Spec" line in the completion report. Description mentions it. Linux clone command next to `cp -cR`. | Nothing closed the Definition of shipped, and nothing captured lessons (team-rebuild's Learned is still empty) |
| `skills/ship-spec/references/batch-file.md` | New `## Close-out` section in the skeleton | Where step 7 writes |
| `skills/ship-spec/SKILL.md` | Says falsify closes the Definition of shipped. The logic-map trigger list now copies logic-map's wording and names logic-map as its owner | The "big feature" threshold existed in four versions |
| `skills/diagnose/SKILL.md` | Step 3 starts from the scenario's steps instead of a `## Logic map` section. "Confirm the bracket" moved before the fix. Linux clone command | logic-map stopped writing `## Logic map` on 2 Nov; the bracket check was placed after the fix |
| `skills/idea-gate/SKILL.md` | Build hands off to ship-spec, not plan-forge (description too). Confirm what the brief already answers instead of asking again. Cap rule: a 1 on problem severity or willingness to pay caps the verdict at Narrow | Skipped ship-spec; a total could outvote a fatal score; repeat questions |
| `skills/grill-me/SKILL.md` | Rule 6 saves per the Output section, never the vault. Read existing memory and docs first, grill only the gaps. `review_after` says who acts on it. Attribution corrected to Matt Pocock | It banned the vault and saved to it; it credited "Matt Porigity" (the correction is inferred from his skills repo) |
| `skills/logic-map/SKILL.md` | Fallback when `scenarios.mjs` is missing (scenarios.json by hand, checks run by hand, never met on a check not run). One-line budget format | Unrunnable in Claude Code or the cloud; raze-review depends on budgets that had no format |
| `skills/pitch-craft/SKILL.md` | Read before asking: pre-fill from README, client record, brief, show for confirmation, ask only what is missing. Credits Dunford and Hormozi | Nine interview turns even when the answers were on disk |
| `skills/skill-intake/SKILL.md` | Description with real triggers. New "Read everything that runs": scripts, hooks, MCP configs, install commands; an unexplained risky one scores 0 on cost and permissions | 134-character description; no security read of third-party skills |
| `skills/fidelity-critique/SKILL.md` | Description adds "looks generic", "looks like every AI site", "feels template-y", "is not premium enough" | Description had none of the words he uses |
| `skills/design-ban-audit/SKILL.md` | Two greps: raw colours as Tailwind arbitrary values (`bg-[#...]`), and in inline styles | Raw colours were only searched in CSS files |
| `skills/voice-profile/SKILL.md`, `scripts/measure.py` (new) | Step 4 runs the counter: sentence length, range, paragraphs, openers, punctuation per 1,000 words, phrases recurring across samples. Stdlib only | The skill's value is counted numbers, and models miscount by eye |
| `scripts/check-skills.py` (new) | Lints tracked skills: frontmatter name and description length, every referenced `references/` or `scripts/` file exists, no active skill names an archived one, README lists exactly the active skills | The drift above went a week with nothing to catch it |
| `README.md` | Rewritten to match the repo: the pipeline, a situation-to-skill table, all 18 active skills, an Archived table, honest credits, an install example on a live skill, a Maintaining section | Listed 6 archived skills as active, missed 3 active ones, listed a deleted skill, pointed at a `deploy.md` that does not exist |
| `docs/skill-evaluations/2026-11-08-full-audit.md` (new) | Scores, per-skill critique, process critique, gap table, Needs your call | Asks 1 to 3 |

## Log
- 8 Nov: read all 18 SKILL.md files and their references; checked cross-references and frontmatter.
- 8 Nov: tested the new design-ban-audit greps in a scratch repo, whole-repo and card-diff modes: both
  arbitrary-value and inline-style hits found, `href="#about"` not flagged.
- 8 Nov: first measure.py run split hard-wrapped lines into fake sentences ("different."); fixed by
  joining a line break with no end punctuation followed by a lower-case line.
- 8 Nov: check-skills.py first run flagged the archived skills' long descriptions; scoped the
  description check to active skills, since archived ones are never loaded.
- 8 Nov: push refused twice (403, no GitHub App access); pushed after he reconnected GitHub.

## Close-out  (falsify step 7, at batch end)
Definition of shipped:
- check-skills -> met (`OK: 18 active and 7 archived skills checked.`; also caught all three faults planted in a scratch copy: a missing reference, a backticked archived skill, a wrong name)
- audit with 18 scores -> met (18 score rows in the table)
- pushed -> met for `bce0f0d` (`git ls-remote` returned `bce0f0ded346...`, same as local HEAD); this note is pushed in the commit after it
- he reads the audit and this note -> needs his eye
Ask ledger: 1 DONE, 2 DONE, 3 DONE, 4 DONE except the four Needs-your-call items, 5 DONE, 6 DONE
Verified: every active SKILL.md parses as YAML with a name and description; the grep and script tests in the Log.
Unverified: no skill was triggered in a real harness, so descriptions and the new steps are judged by reading only.
Learned:
- Skills drifted for a week after a rebuild with no check -> `scripts/check-skills.py` before each skill commit
- Push access was first tried at the end, after all the work -> a `git push --dry-run` at session start would have surfaced the 403 before the work began
- Proposed skill changes (for skill-intake): the four items under Needs your call, with evidence in the audit
