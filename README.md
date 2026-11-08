# agent-skills

Self-authored [Agent Skills](https://code.claude.com/docs/en/skills) for Claude Code and Hermes: 18 active
skills in `skills/`, plus retired ones kept in `archive/`. Third-party skills are deliberately not vendored
here (see [Third-party skills](#third-party-skills)). A few skills adapt someone else's method and credit it
inside the skill: diagnose (Matt Pocock's diagnosing-bugs), plan-forge's high-risk review (gstack, MIT,
license included), grill-me (Matt Pocock's pattern via Nate Herk) and pitch-craft (April Dunford's
positioning, Alex Hormozi's value equation).

Most of them are forcing functions: they make a model run the loop a frontier model runs on its own:
interpret the ask, plan from evidence, verify against reality and close everything instead of shipping
the first plausible output. The rest are personal workflow skills.

## How they fit together

```
idea-gate -> ship-spec -> logic-map* -> plan-forge -> build -> falsify -> raze-review**
```

\* only for a new app, site or process, or a big feature; he approves the map before building.
\** at the end of an integrated batch (a mapped area, 8+ files, or an area fixed twice).

The batch file (`docs/crew/<date>-<slug>.md`) carries the work from end to end: ship-spec writes his words
and the Definition of shipped, plan-forge writes the plan, and falsify closes it with a Close-out (each
Definition of shipped line checked, every ask accounted for, what was learned). Proposed skill changes from
a Close-out go through skill-intake.

| Situation | Skill |
|---|---|
| A new idea: should this exist at all? | idea-gate |
| The assistant does not know his context yet | grill-me |
| Substantial work is about to start | ship-spec, then plan-forge |
| A new app, process or big feature | ship-spec, logic-map (map approved), plan-forge |
| A studio web page | premium-site-standard (the bar), brand-idiom (the objects), then build |
| Something is broken, failing or slow | diagnose |
| Nothing is broken, but the product behaves wrongly | mission-debug |
| About to say done, green or passing | falsify |
| UI about to be called done | design-ban-audit plus a real render; fidelity-critique for premium work |
| A batch is integrated, or an area keeps breaking | raze-review |
| Writing in his name | voice-profile (once), then pitch-craft or the task |
| A client call is coming up, or just happened | discussion-pack |
| Any verdict, review or brainstorm | brutal-honesty, as the register |
| A skill, plugin or harness change is proposed | skill-intake |

## Skills

### Before code

| Skill | What it does |
|---|---|
| **idea-gate** | Gates a new idea before anything gets built: six forcing questions, a scorecard, and a build / narrow / shelve verdict. |
| **grill-me** | Interviews him to pull durable context (business, preferences, a project) out of his head and into memory and project docs. |
| **ship-spec** | Step one for substantial work: what ships and how he will know it is done (his words numbered, Definition of shipped, ask ledger). Also consolidates a pile of audits into one spec. |
| **logic-map** | Turns an app, spec or process into scenarios with checks, the rules each part guarantees and who owns each, drawn on a Floorplan map he approves before building. |
| **plan-forge** | Step two: plans how and in what order, from the ship spec. Quick, light, standard and high-risk modes; parallel work split by file ownership. |

### Debugging

| Skill | What it does |
|---|---|
| **diagnose** | Red loop first, then a logic map to locate the fault by contradiction, then a fix at the broken link with a regression test. |
| **mission-debug** | For behaviour that "feels wrong" rather than crashes. Traces the felt symptom to the contract, prompt, schema or state rule that forces it. |

### Before calling it done

| Skill | What it does |
|---|---|
| **falsify** | The one done-gate: a real signal, a sibling scan, every test broken on purpose, verified versus unverified surface. At batch end it closes the ship spec. |
| **raze-review** | Blind strict architecture review of an integrated batch, and audit mode for repos that have grown too wide. Review-only, never edits. |
| **brutal-honesty** | Anti-sycophancy register for verdicts, reviews and brainstorms. Existence is not evidence. |

### Design and frontend

| Skill | What it does |
|---|---|
| **premium-site-standard** | The studio's quality bar for every website, from first plan to handover, plus his standing direction. |
| **brand-idiom** | Replaces generic web components with ones derived from the brand's native idiom. |
| **fidelity-critique** | Grades UI on a low-fi to high-fi commitment ladder with cited evidence, then names the single next commitment. |
| **design-ban-audit** | Mechanical grep audit for mid-fi design tells (gradient text, glassmorphism, raw colours and the rest), whole repo or one card's diff. |

### Writing and positioning

| Skill | What it does |
|---|---|
| **voice-profile** | Builds his writing voice profile measured from real samples (a counting script is included), not guessed. |
| **pitch-craft** | Turns a project or offer into one positioning line and a tightened offer. |
| **discussion-pack** | A three-minute prep pack before a client conversation: state of play, the one outcome, the say-versus-need gap. Logs the call afterwards. |

### Harness

| Skill | What it does |
|---|---|
| **skill-intake** | Evaluates a proposed harness change (a third-party skill, or an edit to one of these) before it lands, including a read of everything it would run. |

### Archived

Kept in `archive/` for reference. Not linked into any harness.

| Skill | Status |
|---|---|
| **frontier-gap** | Archived. Its loop now lives in ship-spec, plan-forge and falsify. `references/evidence.md` still holds the measured findings these skills cite. |
| **feature-loop** | Archived, v0.9, explicit opt-in only. `decision-burst.md` and the pre-commit proof hook are worth reusing. |
| **critic-pass** | Archived. Merged into falsify. |
| **pixel-critique-loop** | Archived. Its render check is in falsify, premium-site-standard and design-ban-audit. |
| **logic-first-debug** | Archived. Merged into diagnose (the map and contradiction method). |
| **mission-systems-cleanup** | Archived. Post-build architecture review is raze-review's mode A. |
| **goal-split** | Archived. Merged into plan-forge (parallel sessions split by file ownership). |

> 31 Oct 2026: the in-place rewrite of 5 Sep to 9 Oct was parked in `git stash` and the 21 Aug
> originals restored, with references to retired systems (the c3po vault, Notion, Feature Loop, the
> Forge and Raze profiles, ponytail) repointed. See `docs/skill-evaluations/2026-10-31-rewrite-vs-original.md`.
> 1 Nov 2026: the team rebuild merged the planners, done-gates and debuggers and archived the rest; see
> `docs/crew/2026-11-01-team-rebuild.md`. `brainiac-learning-intake` was removed then (it read the retired
> vault); it is in git history at `265bbc5`.

Claims inside these skills are pinned to a published result or a logged real incident;
`archive/frontier-gap/references/evidence.md` keeps measured findings separate from marketing.

## Install

Claude Code loads skills from `~/.claude/skills`. Clone anywhere, then link the ones you want:

```bash
git clone https://github.com/stefano-alvares/agent-skills ~/.agents
ln -s ~/.agents/skills/falsify ~/.claude/skills/falsify
```

Per-skill symlinks, not one link for the whole folder: `~/.claude/skills` normally also holds
skills from other sources, so it cannot be a symlink to this repo.

To link every skill in one go:

```bash
for s in ~/.agents/skills/*/; do ln -sfn "$s" ~/.claude/skills/"$(basename "$s")"; done
```

Some skills call Hermes tools that live outside this repo (`~/.hermes/tools/scenarios/`, `shots.cjs`).
Each one says what to do when the tool is missing.

Sync across machines: edit, commit, push, `git pull` on the other machine.

## Maintaining

Run `python3 scripts/check-skills.py` before committing a skill change. It checks frontmatter, that every
`references/` or `scripts/` path a skill mentions exists, that no active skill points at an archived one,
and that this README lists exactly the active skills.

## Third-party skills

This repo holds only my own work. Skills I use from other authors live directly in
`~/.claude/skills` on my machines and are installed from their own sources.

Commits before 2026-08-21 did vendor third-party skills into `skills/`, without their licenses
attached. They came from [mattpocock/skills](https://github.com/mattpocock/skills) (MIT),
[Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) (MIT),
[UditAkhourii/adhd](https://github.com/UditAkhourii/adhd) (MIT) and
[Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) (Apache-2.0). Copyright stays
with those authors under their respective licenses. Go to the upstream repos for current versions.

## License

MIT, see [LICENSE](LICENSE). Applies to the skills in this repo; the adapted parts keep the credits and
licenses named in the skills that use them.
