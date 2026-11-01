---
name: idea-gate
description: "Gate a new idea before any code gets written — six forcing questions, a seven-dimension scorecard, and a build / narrow / shelve verdict. Use when Stefano floats a new project, app, tool, or game; when he asks 'should I build this', 'is this worth doing', 'validate this idea'; or when a half-started project needs a keep-or-kill call. Run BEFORE plan-forge: it plans work, this decides whether the work should exist."
---

# Idea Gate

Stefano starts more projects than he finishes. This skill is the gate that costs an hour
instead of a month. It ends in a verdict, not encouragement.

**Honest, not kind.** A weak idea scored honestly is worth more than an encouraging lie.
Load `brutal-honesty` alongside this if the pull toward agreement shows up.

**Never write code in this skill.** The only output is the verdict and its assessment (given in the reply, or
saved when asked — Step 5). If the idea passes, the next step is `plan-forge`, not a build.

**Do not reopen an already authorized build.** If Stefano has already decided to build it and said so, this
gate does not apply; the question is closed.

## Step 0: Mode

Ask which this is, because two dimensions change meaning:

- **Commercial** — client work, or something meant to earn. Full scorecard as written.
- **Personal** — a tool for himself, a game, a learning project. "Willingness to pay" becomes
  "will you still use this in a month", "market size" becomes "who else has this problem".

Read Stefano's voice profile at `~/Desktop/Business-projects/business vault/voice-profile.md`
if it exists and write the output in that voice. The verdict itself stays blunt regardless.

## Step 1: The idea

> What is the idea? One or two sentences.

## Step 2: Six forcing questions

One at a time. Wait for each answer. Do not batch. Vague answers are normal on the first
pass — push **once** with the follow-up, then move on. Do not soften a question to make it
comfortable. Comfort means the question landed shallow.

**1. Demand reality.** What is the strongest evidence someone actually wants this? Would
anyone be genuinely annoyed if it vanished tomorrow?
*Push once if the answer is interest, a waitlist, or "people seem excited":* Interest is
free. Has anyone paid, asked when it ships, or complained when it broke?

**2. Status quo cost.** What are people doing right now to solve this, even badly? What does
that workaround cost them in hours or money?
*Push once if the answer is "nothing exists":* No workaround at all usually means the problem
is not painful enough to make anyone act. Is there really nothing, or has nobody looked?

**3. Desperate specificity.** Name the actual person who needs this most. A role and a
situation, not a category.
*Push once if the answer is a category:* You cannot message a category. Name one real person
you could ask this week.

**4. Narrowest wedge.** What is the smallest version someone would use — or pay for — this
week, before the full thing exists?
*Push once if the answer is "it needs the whole platform":* That is attachment to the
architecture, not the value. With zero setup and no login, what is the one useful thing?

**5. Real observation.** Have you watched someone use this, or an early version, without
helping them? What surprised you?
*Push once if the answer is a survey, a demo call, or nothing:* Surveys say what people think
they would do. Watching says what they do.

**6. Future-fit.** In three years, does this become more essential or less?
*Push once if the answer leans on a general trend:* Every competitor can claim the same
trend. What is the specific bet about how this person's world changes?

## Step 3: Score seven dimensions

Score 1-5 each. A 3 is average, not a diplomatic middle. Be honest, not generous.

| Dimension | Commercial | Personal |
|---|---|---|
| Problem severity | How painful for the person who has it | Same |
| Reach | How many have this problem | Who else has it, or is it only you |
| Willingness to pay | Will they pay enough, soon enough | Will you still use it in a month |
| Competition gap | Real room, or crowded and won | Does something free already do this |
| Distribution | Can he reach users at sustainable cost | Can he actually ship it to anyone |
| Timing | Right moment, early, late, or evergreen | Same |
| Founder fit | Real specific advantage at building this | Does it teach him something he wants |

Show the scorecard as a table: dimension, score, one-line note. Total out of 35.

**Founder fit is where Stefano scores himself generously.** He is a strong builder, so it
feels like fit on every idea. Fit means a specific advantage on *this* problem — access to
the user, domain knowledge, an existing asset. General coding skill is not an advantage.
Score it that way.

## Step 4: Verdict

- **28-35 — Build it.** Name the single most important thing to do this week.
- **14-27 — Narrow it.** Name the specific wedge or angle that would make it stronger. Not
  "improve it". A named change.
- **Below 14 — Shelve it.** Say why plainly. If an adjacent problem is worth more, name it.

Do not soften the verdict. Do not average away a 1 with a 5 and call it fine — a single
dimension scoring 1 or 2 is usually the whole answer. Name it.

Cross-check the total against the six answers. If most answers were vague but the score came
out high, the score is wrong. Re-score.

## Step 5: File it

Save the assessment to the project's canonical record only when asked, else give it in the reply.
Either way it has the same shape:

- Title: `Idea gate: <idea name>`
- Body: the idea, all six answers with a one-line read on each, the scorecard table, the
  verdict with reasoning, and the one next action.
- The verdict is the record that the question was asked. It does not change any project's
  status by itself — see "What this does not do".

If a requested save fails, say so and give the assessment in the reply instead. Never silently
skip it.

## Step 6: Close

After the assessment, one line: the verdict and the next action. Nothing else.

## What this does not do

No code. No scaffolding. No stack recommendation. Evaluation is not execution authority: a verdict
does not create a project, start a build, or change a status. If the verdict is Build, hand off to
`plan-forge`.
