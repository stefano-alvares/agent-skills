---
name: discussion-pack
description: "Build a three-minute prep pack before a client or prospect conversation — state of play, the one outcome, the say-versus-need gap, three questions, likely objections, money boundaries, and landmines. Use before any call, meeting, DM thread, or pitch with a client or lead; when Stefano says 'I'm talking to <name> tomorrow', 'prep me for this call', or 'what do I ask them'; and after the conversation to log what happened. Reads the client's own records — never invents what they said."
---

# Discussion Pack

One file, read in three minutes on the way to the call. It is prep, not a record. The
record is `notes.md`, and Step 6 puts it there afterwards.

**Read, do not guess.** Every line in the pack traces to a file. Where you are reasoning
past the evidence, mark it `(inferred)` — the same rule `c3po_vault/clients/README.md`
sets for brand research, applied here. A pack that invents what a client said is worse
than no pack, because he will say it back to them.

Load `brutal-honesty` for the landmines and the money sections. A prep doc that flatters
the state of the relationship gets him blindsided in the room.

## Step 1: Find the client

Locate the folder in `c3po_vault/clients/`. Folders are named `<Brand> - <Person>`, e.g.
`Ulta Pulta - Kripa`. Fuzzy-match on either half.

**No matching folder?** Two cases:

- A client or lead with no record yet — say so, and offer to create one from
  `clients/_template/` before prepping. A pack built on nothing is a guess with headings.
- Not a client at all (uni, a teammate, a collaborator) — skip Step 2, ask him directly
  for who, what they want, and what he wants, then run Steps 3 to 5 from his answers.
  Write the pack to `outputs/` instead of `clients/`.

Read `c3po_vault/context/voice.md` if it exists. It governs anything in the pack he might
say out loud or paste into a message.

## Step 2: Read the record

In this order. Do not skip `notes.md` — it is the only file that knows what was actually
said.

| File | What you take from it |
|---|---|
| `client.md` frontmatter | `status`, `last_contact`, `next_step`, `next_step_due`, `rate`, `engagement` |
| `client.md` body | "What they want" versus "What they actually need", Commercials, Risk read |
| `notes.md` | The two or three newest entries. Every **Flags** and **Next** line, however old |
| `scope.md` | What is explicitly in, and explicitly out |
| `brand/profile.md`, `brand/competitors.md` | Only if the conversation is about their brand or positioning |

Compute days since `last_contact` against today. If `next_step_due` has passed, that is
the first thing in the pack, not a footnote.

The index at the bottom of `clients/README.md` sometimes carries a one-line summary that
the client folder does not. Read it too.

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
**Agreed:** <rate + engagement from client.md, or "nothing agreed">
**Open:** <what has not been settled>
**Do not commit to:** <the specific things he must not say yes to today>

## Landmines
- <constraint, risk, or sensitivity — with its source file>
```

Rules for the sections that go wrong:

**Questions.** Three, never more. Each one must be answerable only by them, and its answer
must change what he does next. "What's your budget?" is fine if budget is genuinely open;
it is filler if `client.md` already records a rate. Cut any question the record answers.

**Objections.** Pull from `notes.md` **Flags** lines and the Risk read. If the record shows
no hesitation yet, write the one objection the scope invites and mark it `(inferred)`.

**Money.** Read from `client.md`, never improvised. If `rate: TBD`, say TBD — do not
suggest a number in the pack. The "do not commit to" line matters most on a friendly call,
which is where scope gets given away.

**Landmines.** Relationship constraints are landmines. Where the record says a client is
family or a favour, that goes at the top of this section and it overrides commercial
advice everywhere else in the pack.

## Step 5: Write it

`c3po_vault/clients/<client-slug>/discussion-pack.md`, overwritten each run. It is a
snapshot for one conversation, not a log — the log is `notes.md`.

If the pack sits on more inference than record, say so at the close in one line: which
sections are thin and which file would fix them.

Print the outcome line and the three questions. Nothing else.

## Step 6: After the conversation

When he comes back, append one entry to `notes.md` in the shape that file already defines
— newest first, `## <YYYY-MM-DD> — <call | email | meeting | dm>`, with **Present**,
**Said**, **Decided**, **Flags**, **Next**. Never rewrite an existing entry.

Then mirror, per `clients/README.md`:

- Commercial decisions into `client.md` Commercials and frontmatter.
- Scope decisions into `scope.md`.
- New `last_contact`, `next_step`, `next_step_due` in `client.md` frontmatter.
- A `status` change if one is warranted — and on `active`, the README's promotion rule
  says to create the Notion project entry so execution is tracked outside this folder.

Delete nothing. `discussion-pack.md` is overwritten by the next run on its own.

## Boundaries

Not a pitch. Positioning and offer work is `pitch-craft`, and if the conversation needs a
pitch built first, run that and come back. Not a proposal or a quote. Not a place to
decide the rate — that decision lives in `client.md` and is his to make.
