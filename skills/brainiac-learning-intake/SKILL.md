---
name: brainiac-learning-intake
description: "Use when filing a personal learning resource into Brainiac."
---

# Brainiac Learning Intake

A saved resource is not learning. Brainiac turns a source into one bounded capability, proof of use, and a review signal.

## 1. Capture the source

Record the URL/file, author, date, source type, exact claim, and linked primary material. For a Reel or video, capture the visible steps, spoken claims, transcript when available, and any linked code or documentation.

Treat demonstration polish as separate from mechanism. If the mechanism cannot be inspected, record it as **Watch**, never as established knowledge.

## 2. Classify the learning job

Choose exactly one domain:

- **Coding** - programming, computer science, web, systems, data, security.
- **Embedded & electrical** - electronics, circuits, microcontrollers, sensors, firmware, PCB, robotics.
- **Tech systems** - AI, cloud, networking, product technology, tools, technical trends.
- **Business & world** - markets, economics, geopolitics, business models, regulation, history relevant to decisions.

Then choose one job:

- **Build** - make a working artifact.
- **Diagnose** - find and correct a fault.
- **Explain** - form a reliable mental model.
- **Decide** - make a current business or world decision using evidence.
- **Reference** - preserve a source for later, with no active study commitment.

## 3. Define the capability before filing

Write one capability statement:

```text
After this, Stefano can <observable action> using <constraints>, proven by <artifact or explanation>.
```

Reject vague goals such as "learn Arduino" or "understand geopolitics." Replace them with a small demonstrated action.

## 4. Score before committing attention

Score 0-2 each:

| Dimension | Question |
|---|---|
| Leverage | Does this unlock a real project, decision, or repeated capability? |
| Timeliness | Is it needed within the next 90 days or likely to remain useful? |
| Evidence | Is the source primary, inspectable, and specific enough to test? |
| Practice path | Can a proof artifact be produced without expensive equipment, credentials, or a full course? |
| Prerequisites | Are the required foundations known or explicitly planned? |
| Cost | Is time, money, and equipment proportionate to the expected gain? |

Interpretation: 9-12 = Learn now; 6-8 = Backlog; 3-5 = Reference or Watch; 0-2 = Reject. A 0 in Evidence, Practice path, or Cost blocks Learn now.

## 5. File to the correct route

### Brainiac Learning Queue (Notion)

Use the `Brainiac Learning Queue` table for all personal learning candidates. It holds the source, domain, capability statement, score, current status, next action, proof link, and review date.

When Hermes must create an entry, use the local writer instead of creating a vault file:

```bash
python3 ~/.hermes/scripts/brainiac_intake.py \
  --topic "<bounded capability>" \
  --domain "<Coding|Embedded & Electrical|Tech Systems|Business & World>" \
  --job "<Build|Diagnose|Explain|Decide|Reference>" \
  --capability "After this, Stefano can ... proven by ..." \
  --source "<URL when available>" \
  --evidence-notes "<claim, source quality, unknowns>" \
  --next-action "<one-session action>" \
  --proof-description "<observable proof>" \
  --status Inbox
```

Report the returned Notion URL. If the writer fails, say so plainly; do not create an unstructured vault fallback.

Keep no more than two items in **Learning now**. Every active entry needs a next action that fits one session and an observable proof artifact.

### Curated knowledge (vault wiki)

When the source produces durable, cross-project knowledge, create or update a page in `c3po_vault/wiki/wiki/` and log it in `wiki/log.md`. Do not put personal progress or project status in the wiki.

### Harness route (not Brainiac)

If the candidate changes Hermes, its skills, memory, configuration, automations, models, or other agents, route it to `skill-intake` instead. That is the Harness Intake and keeps agent-system changes out of the personal learning queue.

## 6. Close the learning loop

A resource becomes **Applied** only when its proof exists. Examples: a repository/commit, circuit photo plus measurement, sourced memo, solved exercise, or a concise teach-back that survives questioning.

Create a learning record only after demonstrated understanding, a corrected misconception, a stated prior capability, or a mission change. Exposure alone is not a learning record.

For current affairs, set a short review date and label claims with source date. Do not turn a time-sensitive briefing into permanent truth.

## Output

```text
Route: Learn now | Backlog | Reference | Watch | Reject
Domain:
Capability:
Next action:
Proof:
Why now / why not:
```