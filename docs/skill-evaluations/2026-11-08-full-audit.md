# Full audit of the active skills (8 Nov 2026)

Scope: the 18 skills in `skills/` (SKILL.md plus references), read in full, and how they work together.
Out of scope: the archived skills, the profile-local Hermes skills (crew-board, studio-build, dev-build,
quality-layer), the Claude Code crew plugin in `~/Desktop/crew`, and the Hermes tools the skills call.
None of those are in this repo. Scores are as found, before the fixes below. No skill was run against a
live project in this pass, so every score is a reading score: UNVERIFIED in use.

## Verdict

**Whole process: 7.5/10.** The core path (ship-spec, plan-forge, falsify, diagnose) is strong: 8 to 9, built
on rules that hold up (verbatim asks, buckets with no limbo, done means a runnable check, documents are
witnesses). What drags it down is decay at the edges after the 1 to 3 Nov rebuild. The README described a
different set of skills. Three skills pointed at things that no longer exist. One skill (grill-me)
contradicted the house rules. The planning loop had no step that closed the Definition of shipped.
logic-map could not run outside Hermes. None of that is a design flaw; it is drift with nothing to catch it.

## Scores

| Skill | /10 | One line |
|---|---|---|
| ship-spec | 8.5 | Best contract in the set. Weak spot: nothing closed the Definition of shipped at the end (fixed). |
| falsify | 8.5 | Real signal, sibling scan and mutation are the right three moves. Missing the batch close-out (fixed). |
| diagnose | 8.5 | Red loop plus contradiction is a strong merge. Pointed at a `## Logic map` logic-map no longer writes (fixed). |
| brutal-honesty | 8.5 | Short, sharp, well-bounded. Overlaps raze-review's honesty contract, which is fine. |
| plan-forge | 8 | Modes, vertical slices, file ownership and the kill-test are excellent. Re-explains ship-spec in three places. |
| mission-debug | 8 | The forcing-layer ladder is genuinely distinctive. Ignores scenarios.json as the mission source. |
| raze-review | 8 | Rigorous and anchored against nibbling. No calibration: the blind architect costs the same on a 10-file repo. |
| fidelity-critique | 8 | The commitment ladder is the right model. Repeats its evidence caveats twice; description lacked triggers (fixed). |
| brand-idiom | 8 | Rich, original method. At 285 lines it is the costliest load; worked tables could move to references. |
| idea-gate | 7.5 | Good forcing questions. Handed off to plan-forge, skipping ship-spec (fixed); no cap for a fatal dimension (fixed). |
| discussion-pack | 7.5 | Anti-fabrication is right. Hard-coded `/Users/...` path, vague client-record location, client-document scope creep. |
| logic-map | 7 | Concept is 9 (one owner per rule, the check crosses every boundary). Unrunnable without the Hermes tool (fallback added); budgets were a stub (format added). |
| voice-profile | 7 | Measure-don't-guess is right, but it asked a model to count by eye (script added). |
| pitch-craft | 7 | Solid frameworks. Interviewed nine questions even when the README already answered them (fixed); no credit to its sources (fixed). |
| design-ban-audit | 7 | Useful and mechanical. Missed raw colours in Tailwind arbitrary values and inline styles (fixed); dense one-liners. |
| premium-site-standard | 6.5 | Good standing direction, but no verdict or output format, several uncheckable lines ("logo is intentional"). |
| skill-intake | 6 | Sound verdict ladder. Description had no triggers (fixed); no step to read what a candidate executes (fixed). |
| grill-me | 4.5 | Generic import. Said "save it to the vault" while also banning the vault; wrong attribution (fixed); 15-30 questions with no skip-what's-known (fixed). Still the weakest. |

## Per skill

**ship-spec (8.5).** Verbatim, numbered asks with a bucket each; a Definition of shipped written before tasks;
claims probed, not quoted. The split from plan-forge ("what and when" versus "how") is the most valuable
boundary in the repo. Gaps: the Definition of shipped had an author but no closer; the "big feature" list
was a fourth copy of a threshold that already differed between skills. Changed: Close-out pointer, and the
threshold now copies logic-map's wording and names logic-map as its owner.

**plan-forge (8).** Ordering by dependency and risk, spike first, vertical slices, zero shared files between
parallel units, a kill-test before lock. Gaps: sections 1, 2 and 4 restate ship-spec; Hermes roles
(Atlas, Argus, engineering-god) leak into a skill meant to be harness-neutral. Not changed: the restating is
redundant but harmless, and trimming it is the kind of rewrite that went wrong in October.

**logic-map (7).** Scenarios with runnable checks, one owner per rule, the narrowest owner that can enforce
it, and "the check must cross every boundary" (learned from a real pilot). Gaps: every command needs
`~/.hermes/tools/scenarios/scenarios.mjs`, which is not in the repo, so in Claude Code or a cloud session
the skill could not run; Budgets, which raze-review depends on, was three sentences with no format; the
Evidence rules sit between Phase 5 and Phase 6. Changed: a no-tool fallback (scenarios.json by hand, checks
run by hand, never "met" on a check not run) and a one-line budget format.

**grill-me (4.5).** The only skill not written in the house style. Rule 6 said to save to the vault while the
Output section forbids recreating the vault. The attribution named "Matt Porigity"; the pattern is Matt
Pocock's (inferred from his skills repo, which this repo vendored earlier). "15-30 questions minimum" with no
instruction to skip what memory already holds. Changed: those three, plus a review_after line that says who
acts on it. Still open: see Needs your call.

**idea-gate (7.5).** Six forcing questions with one push each, an honest scorecard, a note that founder fit is
where he scores himself high. Gaps: it handed a Build verdict to plan-forge, skipping ship-spec; it said a
single 1 is "usually the whole answer" but the thresholds let a total override it; it asked questions the
brief had already answered. Changed: all three (hand-off to ship-spec, a cap rule, pre-fill and confirm).

**diagnose (8.5).** One red-capable command before any hypothesis, then the map and the backwards
impossibility test, with "absences are faults". Gaps: step 3 read a `## Logic map` section that logic-map
stopped writing on 2 Nov; "confirm the bracket" sat after the fix instructions; `cp -cR` is macOS only.
Changed: step 3 starts from the scenario's steps, the bracket check moved before the fix, Linux clone added.

**mission-debug (8).** The ladder from copy down to data and the forcing test ("could a perfect model still
do the right thing under this layer?") find roots other skills miss. Gaps: on a mapped project the
scenarios' `want` lines are the promises it re-derives from docs; the 622-character description is the
longest in the set. Not changed.

**falsify (8.5).** Strongest-signal-first, the sibling table, real mutations, an honest unverified line.
Gap: it checked drift against "the request and the card" but nothing ran the Definition of shipped checks
or closed the ask ledger, and nothing captured what the batch taught (the team rebuild's own batch file
still says "Learned: (filled at the end)"). Changed: step 7 closes the spec and writes the Close-out with
Learned lines that go to skill-intake.

**raze-review (8).** Blind architect, burden of proof on the file, banned verdicts for twice-failed
sections, symmetric burden for KEEP. Gaps: no calibration for small repos; depends on budgets that
logic-map barely defined (format now added there). Not changed.

**brutal-honesty (8.5).** Seven rules, a clear boundary against rudeness and contrarianism. Nothing to fix.

**premium-site-standard (6.5).** The standing direction is specific and his ("no site-within-a-site", the
AI-default cream-and-serif look). Gaps: it is a checklist with no output (no PASS/FAIL per bar, no
evidence), several lines cannot be checked as written, and it assigns roles ("Atlas runs...") inside a
shared skill. Not changed: the bar is a taste document, so its shape is his call.

**design-ban-audit (7).** Mechanical greps with whole-repo and card-diff modes, zero silent passes. Gap: raw
colours were only searched in CSS, so `bg-[#1a2b3c]` and `style={{ color: '#f00' }}` in TSX passed.
Changed: two greps added, tested in both modes in a scratch repo.

**fidelity-critique (8).** "Fidelity is commitment" and the minimum-across-dimensions rule are the right
model. Gaps: the evidence caveats appear twice; the description had none of the words he actually says.
Changed: description triggers.

**brand-idiom (8).** Found, built and imagined sources with a THEREFORE sentence, a fallback contract before
the flourish, an idiom budget. Gap: length. Not changed.

**voice-profile (7).** Counted rhythm, sample size stated, never "measured" when interview-only. Gap: the
whole value is counted numbers and models count sentence lengths badly. Changed: `scripts/measure.py`
(stdlib, tested on his messages quoted in docs/crew), and Step 4 now runs it.

**pitch-craft (7).** Positioning before offer, one push per vague answer, weakest lever named. Gaps: nine
interview turns even when the README or client record answered them; no credit for Dunford or Hormozi.
Changed: both.

**discussion-pack (7.5).** Every line traced to the record, `(inferred)` marked, money from the record only,
family and favours as landmines. Gaps: hard-coded `/Users/stefanoalvares/...` path, "the business vault (or
Plane)" as the client record, and the client-document section is a second job. Not changed: needs where
client records live now.

**skill-intake (6).** Adopt / Adapt / Trial / Watch / Reject with a score floor is sound. Gaps: a 134-character
description with no trigger phrases; nothing told the evaluator to read the scripts, hooks and MCP configs a
third-party skill would run with his permissions. Changed: both.

## The process as a whole

What works:
- One planner, one done-gate, one debugger, one architecture review. The 1 Nov consolidation removed the
  overlap that existed before.
- Shared rules repeated consistently across skills: probe, do not quote; every ask in a bucket; done is a
  check he can run; silence is not a yes; deviations announced.
- Routing tables in nearly every skill, so a skill that loads in the wrong place says where to go.

Gaps found, and what happened to each:

| # | Gap | Evidence | Status |
|---|---|---|---|
| 1 | The loop did not close. ship-spec opened a Definition of shipped that nothing checked at the end, and no step captured lessons | team-rebuild batch file: "Learned: (filled at the end)" | Fixed: falsify step 7, Close-out in the batch skeleton |
| 2 | No map of the whole process. Each skill routes locally; the README was stale | README listed 6 archived skills as active and missed 3 active ones | Fixed: README pipeline and situation table |
| 3 | Drift had nothing to catch it | the stale README and three stale cross-references | Fixed: `scripts/check-skills.py` (catches all of the above; tested with planted faults) |
| 4 | Thresholds copied across skills drifted apart | "big feature" defined four ways | Partly fixed: ship-spec defers to logic-map. plan-forge's high-risk mode is a different gate and keeps its own table |
| 5 | Hermes coupling. Tools the skills need are outside the repo | scenarios.mjs, shots.cjs, `cp -cR` | Partly fixed: fallbacks. The real fix needs your call |
| 6 | Interview fatigue. Four skills interview one question at a time with no skip-the-known rule | idea-gate 6, pitch-craft 9, voice-profile 5, grill-me 15-30 | Fixed in idea-gate, pitch-craft, grill-me. voice-profile already reads the existing profile first |
| 7 | Third-party skills got no security read | skill-intake had no step for scripts or hooks | Fixed |

## Needs your call

1. **grill-me: rewrite or retire.** Recommendation: rewrite it in the house style (purpose, one question
   round per category, where each fact is saved, a stop rule), keeping its question bank. The alternative
   is to retire it: memory plus the third-party `grilling` skill covers most of it.
2. **Put the Hermes tools in this repo.** Recommendation: commit `~/.hermes/tools/scenarios/` (and
   `shots.cjs`) to `tools/` here if they are yours, so the skills and the tools they call version together
   and logic-map works in Claude Code and cloud sessions without the fallback.
3. **premium-site-standard: gate or reference?** Recommendation: give it an output (each bar PASS or FAIL
   with the evidence) so it can gate a page, and move the role lines into crew-board.
4. **discussion-pack: where do client records live now?** It names an absolute Mac path, "the business
   vault" and Plane. One canonical location, named once, would fix three lines.
5. **Trim the long loads** (brand-idiom 285 lines, fidelity-critique 201): move the worked tables to
   `references/`. Low priority, and only with your OK given what happened in October.
6. **raze-review calibration**: a short rule for when to skip the blind architect (for example under 15
   files, or a single section). Your call on the threshold.

## Not checked

- No skill was triggered in a real harness in this pass; descriptions were judged by reading only.
- The Hermes tools and profile-local skills these skills call were not available.
- The Claude Code crew plugin was not reviewed.
