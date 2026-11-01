---
name: discussion-pack
description: "Build a three-minute prep pack before a client or prospect conversation — state of play, the one outcome, the say-versus-need gap, three questions, likely objections, money boundaries, and landmines. Use before any call, meeting, DM thread, or pitch with a client or lead; when Stefano says 'I'm talking to <name> tomorrow', 'prep me for this call', or 'what do I ask them'; and after the conversation to log what happened. Reads the client's own records — never invents what they said."
---

# Discussion Pack

One page, read in three minutes on the way to the call. It is prep, not a record. The
record is the call notes in the client record, and Step 6 puts it there afterwards.

**Read, do not guess.** Every line in the pack traces to a source. Where you are reasoning
past the evidence, mark it `(inferred)`. A pack that invents what a client said is worse
than no pack, because he will say it back to them.

Load `brutal-honesty` for the landmines and the money sections. A prep doc that flatters
the state of the relationship gets him blindsided in the room.

## Step 1: Find the client

Locate the client in the client record, the business vault (or Plane, if the project uses it). A client is usually
named `<Brand> - <Person>`, e.g. `Ulta Pulta - Kripa`. Fuzzy-match on either half.

**No matching record?** Two cases:

- A client or lead with no record yet — say so, and offer to start one in the client record
  before prepping. A pack built on nothing is a guess with headings.
- Not a client at all (uni, a teammate, a collaborator) — skip Step 2, ask him directly
  for who, what they want, and what he wants, then run Steps 3 to 5 from his answers.
  The pack goes in the reply.

Read Stefano's voice profile file if it exists. It governs anything in the pack he might
say out loud or paste into a message.

## Step 2: Read the record

In this order. Do not skip the call notes — they are the only part that knows what was
actually said.

| Part of the client record | What you take from it |
|---|---|
| Status fields | `status`, `last_contact`, `next_step`, `next_step_due`, `rate`, `engagement` |
| Main entry | "What they want" versus "What they actually need", Commercials, Risk read |
| Call notes | The two or three newest entries. Every **Flags** and **Next** line, however old |
| Scope | What is explicitly in, and explicitly out |
| Brand research | Only if the conversation is about their brand or positioning |

Compute days since `last_contact` against today. If `next_step_due` has passed, that is
the first thing in the pack, not a footnote.

If the record keeps an index or overview of all clients, read that too. It sometimes carries
a one-line summary that the client's own entry does not.

The studio's client journey (stages, checkpoints, who approves, what written proof each stage
needs) is mapped in
`/Users/stefanoalvares/Desktop/Business-projects/studio-ops/docs/drafts/client-journey-map.md`.
It is a draft proposal until both partners approve it: read it before prepping any client step,
label what you take from it as proposed, and if it and the client record disagree, stop and
ask Stefano.

## Step 3: Force the outcome

Ask him one question and wait:

> What is the one thing that has to be true when this conversation ends?

If the answer is a list, make him pick. A conversation with three goals has none. If he
does not know, that is the finding — say plainly that the call is not ready, and offer to
run the pack anyway as a scoping conversation with "learn X" as the stated outcome.

## Step 4: Build the pack

Seven sections. Nothing else. Anything that does not change what he says or does not
belong in a document read while walking.

```
# Discussion pack — <Client> — <YYYY-MM-DD>

**<status>** · last contact <N> days ago · <overdue next step, or the open one>

## The outcome
<The one thing from Step 3, in one sentence.>

## What they say versus what they need
**They say:** <from "What they want" — their words>
**Actually:** <from "What they actually need">
**The gap is the job:** <one line on how to raise it without contradicting them>

## Three questions
1. <question> — *why:* <what the answer changes>
2. <question> — *why:* <what the answer changes>
3. <question> — *why:* <what the answer changes>

## What they will push back on
- **"<the objection, in their likely words>"** → <the answer, one or two sentences>

## Money
**Agreed:** <rate + engagement from the client record, or "nothing agreed">
**Open:** <what has not been settled>
**Do not commit to:** <the specific things he must not say yes to today>

## Landmines
- <constraint, risk, or sensitivity — with its source>
```

Rules for the sections that go wrong:

**Questions.** Three, never more. Each one must be answerable only by them, and its answer
must change what he does next. "What's your budget?" is fine if budget is genuinely open;
it is filler if the record already holds a rate. Cut any question the record answers.

**Objections.** Pull from the call notes' **Flags** lines and the Risk read. If the record
shows no hesitation yet, write the one objection the scope invites and mark it `(inferred)`.

**Money.** Read from the client record, never improvised. If `rate: TBD`, say TBD — do not
suggest a number in the pack. The "do not commit to" line matters most on a friendly call,
which is where scope gets given away.

**Landmines.** Relationship constraints are landmines. Where the record says a client is
family or a favour, that goes at the top of this section and it overrides commercial
advice everywhere else in the pack.

### Website discovery branch

When the conversation is website discovery, onboarding, or an audit discussion, read
[references/website-discovery.md](references/website-discovery.md) before Step 4. Steps 1 to 3
still run. The reference supplies the core conversation prompts and the conditional branches
(no website, existing website, established or missing brand, bookings and integrations), plus
how to turn confirmed answers into a website/brand brief.

- Select only the prompts and branches that apply, and skip anything the record or his
  answers already settle. The client should not repeat what is already known.
- In the pack, the Three questions are the three unanswered prompts that matter most. Other
  selected prompts go to internal facilitator notes as optional follow-ups. If a shareable
  question sheet or brief for the client is wanted, it is a client document (below), sized for
  quick reading: normally one or two pages, a target and not a reason to hide a material
  decision.
- Keep technical checks and deeper follow-ups in the internal notes.
- Close with the 1–3–1 format below when the choices are ready.

## Step 5: Give it

The pack goes in the reply. Save it to the client record only when he asks; then it is a
snapshot for one conversation, overwritten each run, not a log — the log is the call notes.

If the pack sits on more inference than record, say so at the close in one line: which
sections are thin and which part of the record would fix them.

If the pack was saved to the record, print only the outcome line and the three questions.
Nothing else.

## Step 6: After the conversation

When he comes back, append one entry to the call notes in the client record, in the shape
those notes already define — newest first, `## <YYYY-MM-DD> — <call | email | meeting | dm>`,
with **Present**, **Said**, **Decided**, **Flags**, **Next**. Never rewrite an existing
entry, and check that the write landed. With no client record, give the entry in the reply.

**No automatic mirroring.** Do not copy the outcome across the record's other notes or into
other systems on your own. Offer the follow-on updates, and make each one only when he says to:

- Commercial decisions into the record's Commercials and status fields.
- Scope decisions into the scope note.
- New `last_contact`, `next_step`, `next_step_due`.
- A `status` change if one is warranted. A change to `active` does not create a project or
  entry anywhere else by itself.

What was proposed in the call stays a proposal until he confirms it. Delete nothing. A saved
pack is overwritten by the next run on its own.

## Recommendation: 1–3–1

When a recommendation is useful (the close of a website discovery, the first move after a
call), use this option format: one priority problem, three credible approaches with their
tradeoffs and dependencies, and one recommended next step with a completion check. Do not
fabricate options just to reach three. Before discovery, label the problem provisional;
after the meeting, call it agreed only when the client confirmed it. Do not prescribe a
rebuild before weighing targeted improvements that would do the job.

## Clean client documents

When a shareable document for the client is requested (not the pack itself), make a clean
client-facing artifact. The pack's facilitator material — internal notes, objections,
audit scores, technical skill names, sales claims — stays in a separate internal section or
file, never in the exported client copy.

- The business's current brand guidelines are the visual source of truth. Proposed studio
  styling can be used for a local review draft; say internally that it is a proposal. Never
  substitute the studio palette for the client's own website identity.
- Clear title, the client or business name when known, a short purpose, grouped questions,
  generous whitespace, restrained accent colour, a legible body face, a consistent heading
  hierarchy. No decorative cover pages or dense grids. Leave room for answers only when the
  document is meant to be filled in. Keep source links useful and readable.
- Make the format requested; otherwise a PDF with selectable text if tooling is available.
  If not, a standalone print-ready HTML file, and say what the format limitation is.
- Before reporting it ready, look at the exported pages for clipping, awkward breaks,
  contrast, working links, and accidental internal content. Claude Code: its preview and
  screenshot tools. Hermes: `node ~/.hermes/tools/shots/shots.cjs <url> <out> <routes>`
  (1440 and 390 px) on a locally served HTML file. Do not claim a rendered check you did
  not make.
- Never send or publish it without his authorization.

## Boundaries

Not a pitch. Positioning and offer work is `pitch-craft`, and if the conversation needs a
pitch built first, run that and come back. Not a proposal or a quote. Not a place to
decide the rate — that decision lives in the client record and is his to make. Sending,
commercial commitments and scope changes stay his decision.
