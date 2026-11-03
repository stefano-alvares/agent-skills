---
name: grill-me
description: "Use when setting up a new project, onboarding a tool or business area, or when the assistant needs Stefano's context (business, life, preferences) to stop sounding like a stranger. Interviews him with relentless questions and saves what it learns where the assistant keeps durable context. For stress-testing a plan, use grilling instead."
---

# Grill Me: knowledge extraction interview

## When to use

- Setting up a new project and the AI needs context
- The AI's answers sound like a "stranger" instead of a "teammate"
- Onboarding to a new tool, workflow, or business area
- Before a big planning session — extract knowledge first, then plan
- Periodic "refresh" of the AI's understanding (quarterly or after major changes)

## The Pattern

The AI interviews you with increasingly specific questions. The goal is to extract knowledge that lives in your head into markdown files the OS can reference.

### Rules for the Interviewer (AI)

1. **Start broad, then drill down.** First pass: high-level questions about the domain. Second pass: specifics, edge cases, preferences.
2. **Ask 15-30 questions minimum.** Don't stop at 5. The good stuff comes after question 10.
3. **Play devil's advocate.** Push back on vague answers. "You said X — can you give me a specific example?"
4. **Extract contradictions.** If something doesn't add up, flag it. "Earlier you said X, now you said Y — which is it?"
5. **Write as you go.** After every 3-5 questions, update the relevant markdown file with what you've learned. Don't wait until the end.
6. **End with a summary.** After the interview, produce a structured summary and save it to the vault.

### Question Categories (rotate through these)

**Business/Project Context:**
- What does this business/project actually do? (Force a 1-sentence answer)
- Who is the customer? (Be specific — demographics, pain points)
- What's the #1 goal right now? What would make this quarter a success?
- What's the biggest blocker?
- What have you tried that didn't work?

**Preferences and Style:**
- How do you like to work? (Morning vs evening, batch vs iterative)
- What does "done" look like for you?
- What do you never want to see in the output? (Forbidden patterns)
- What's an example of work you loved? What made it good?

**Relationships and Stakeholders:**
- Who are the key people involved? (Decision makers, approvers, blockers)
- Who has the final say on [X]?
- What's the communication cadence with [person/team]?

**Systems and Tools:**
- Where does [type of data] live today?
- What tools do you open daily? Weekly?
- What's the current workflow for [process]? (Step by step)
- What's broken about the current workflow?

**Edge Cases and Exceptions:**
- What's the weirdest edge case you've encountered?
- When would you NOT want the AI to do [X]?
- What's the one thing that always goes wrong?

## Output

Save what you learn where this assistant already keeps durable context. Never recreate the archived
C3PO vault folders (`context/`, `projects/`).
- Who he is, his preferences and operating principles: the profile's memory (user profile for who he is,
  memory for standing facts). Keep entries short; skills hold procedures.
- A project's context: that project's own docs (`README.md`, `CLAUDE.md` or `AGENTS.md`), and its
  decisions as dated lines in `docs/crew/decided.md`.
- C-3PO's operational state lives in Notion: write there only when he asks.

## After the Interview

1. **Verify:** Read back what you wrote. "Here's what I understood — is this correct?"
2. **Identify gaps:** "I still don't know about [X]. Should we do another round?"
3. **Set a review date:** Knowledge goes stale. Set a `review_after` date (30 days for wiki, 14 days for project context).

## Gotcha — Don't Overclutter

If a concept or rule already exists in memory, a workflow file, or another skill, **point to it — don't duplicate it.** Adding a named pattern or reference file for something the system already knows adds maintenance burden without value. Keep skills lean. When in doubt, ask: "Does the system already know this?" before writing.

---

*Based on the "Grill Me" pattern by Matt Porigity, adapted by Nate Herk for AI OS setup.*
