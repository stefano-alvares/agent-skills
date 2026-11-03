# agent-skills

Self-authored [Agent Skills](https://code.claude.com/docs/en/skills) for Claude Code and Hermes — 23 skills,
all written by me. Third-party skills are deliberately not vendored here (see
[Third-party skills](#third-party-skills)).

Most of them are forcing functions: they make a model run the loop a frontier model runs on its own: interpret the ask, plan from evidence, verify against reality and close everything instead of
shipping the first plausible output. The rest are personal workflow skills.

## Skills

### The loop

| Skill | What it does |
|---|---|
| **frontier-gap** | Recovery for a long task that is dropping requirements or stopping early: re-interpret the ask, keep a nothing-skipped ledger, verify before done. Not something to load before every task. |
| **feature-loop** | v0.9, archived: explicit opt-in only. Its Notion control plane and the Forge and Raze profiles are retired; `decision-burst.md` and the pre-commit proof hook are worth reusing. |

### Before code

| Skill | What it does |
|---|---|
| **idea-gate** | Gates a new idea before anything gets built — six forcing questions, a scorecard, and a build / narrow / shelve verdict. |
| **logic-map** | Turns an app or spec into its systems, the invariants each one owns, and the causal chains that must hold. Decides what is correct before code decides it. |
| **ship-spec** | Step one for substantial work: what ships and how you know it is done (his words numbered, Definition of shipped, ask ledger). Also consolidates a pile of audits into one spec. |
| **plan-forge** | Step two: plans how and in what order, from the ship spec. Quick mode for 2-3 file changes needs no spec. Parallel sessions split by file ownership (goal-split was merged in). |

### Debugging

| Skill | What it does |
|---|---|
| **logic-first-debug** | Reason about the system's logic before reading or changing code — find which link in the causal chain cannot be intact given the symptom. |
| **mission-debug** | For behaviour that "feels wrong" rather than crashes. Traces the felt symptom to the contract, prompt, schema or state rule that forces it. |

### Before calling it done

| Skill | What it does |
|---|---|
| **critic-pass** | Validation against external evidence — run it, or use a fresh-context verifier. Never bare introspection, which measurably lowers accuracy. |
| **falsify** | For the moment you are about to report work as green, especially when the only evidence is a test suite you wrote yourself. |
| **raze-review** | Blind strict review before commit, and audit mode for repos that have grown too wide. Review-only, never edits. |
| **mission-systems-cleanup** | Post-implementation review: right systems, clean boundaries, no excess code. |
| **brutal-honesty** | Anti-sycophancy register for verdicts, reviews and brainstorms. Existence is not evidence. |

### Design and frontend

| Skill | What it does |
|---|---|
| **brand-idiom** | Replaces generic web components with ones derived from the brand's native idiom. |
| **design-ban-audit** | Mechanical grep audit for mid-fi design tells — gradient text, glassmorphism, and the rest of the list. |
| **fidelity-critique** | Grades UI on a low-fi → high-fi commitment ladder with cited evidence, then names the single next commitment. |
| **pixel-critique-loop** | Render the UI, screenshot it at desktop and mobile width, critique the actual pixels before calling frontend work done. |

### Writing and positioning

| Skill | What it does |
|---|---|
| **voice-profile** | Builds a writing voice profile measured from real samples, not guessed. |
| **pitch-craft** | Turns a project or offer into one positioning line and a tightened offer. |
| **discussion-pack** | A three-minute prep pack before a client conversation — state of play, the one outcome, the say-versus-need gap. |

### Personal harness

| Skill | What it does |
|---|---|
| **brainiac-learning-intake** | Files a learning resource into my notes system. |
| **skill-intake** | Evaluates proposed changes to this harness before they land. |

> 31 Oct 2026: the in-place rewrite of 5 Sep to 9 Oct was parked in `git stash` and the 21 Aug
> originals restored, with references to retired systems (the c3po vault, Notion, Feature Loop, the
> Forge and Raze profiles, ponytail) repointed. See `docs/skill-evaluations/2026-10-31-rewrite-vs-original.md`.
> `brainiac-learning-intake` still reads the private vault.

Claims inside these skills are pinned to a published result or a logged real incident —
`frontier-gap/references/evidence.md` keeps measured findings separate from marketing.

## Install

Claude Code loads skills from `~/.claude/skills`. Clone anywhere, then link the ones you want:

```bash
git clone https://github.com/stefano-alvares/agent-skills ~/.agents
ln -s ~/.agents/skills/frontier-gap ~/.claude/skills/frontier-gap
```

Per-skill symlinks, not one link for the whole folder — `~/.claude/skills` normally also holds
skills from other sources, so it cannot be a symlink to this repo.

To link every skill in one go:

```bash
for s in ~/.agents/skills/*/; do ln -sfn "$s" ~/.claude/skills/"$(basename "$s")"; done
```

For Codex and Cursor, see `skills/frontier-gap/references/deploy.md` — it copies
`frontier-gap/assets/AGENTS.md` and `.cursor/rules` into a repo.

Sync across machines: edit, commit, push, `git pull` on the other machine.

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

MIT — see [LICENSE](LICENSE). Applies to the skills in this repo, which are all my own.
