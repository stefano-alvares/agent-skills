---
name: logic-first-debug
description: Debug by reasoning about the system's logic BEFORE reading or changing code — decompose the feature into systems, map the causal chain the correct behaviour requires, then locate the fault by finding which link cannot be intact given the observed symptom. Use whenever a bug spans more than one file, layer, or service; when the stack trace points somewhere that "makes no sense"; when you or the user has already tried a fix that didn't hold; when the symptom is intermittent, ordering-dependent, or state-dependent; when you are tempted to add print statements or read a fifth file to "see what's going on"; or when the user says any of "debug the logic first", "break it into systems", "map the logic", "think before you patch", "stop guessing", or "where does this actually go wrong". Also use before a large refactor to confirm the fault is where you think it is. Skip for a bug with one obvious local cause — a typo, an off-by-one in a single visible loop, a failure whose stack trace names the exact wrong line — where reasoning ceremony costs more than reading the line.
---

# Logic-First Debug

Most debugging goes wrong the same way: the agent reads the error, opens the file it names, sees something
plausible, and changes it. That is pattern-matching on the *symptom's location*, and it fails whenever the
symptom surfaces somewhere other than where the fault lives — which is most non-trivial bugs.

**Core principle:** a bug is a contradiction, not a mystery. The system was built so that some chain of
claims produces correct output. The symptom proves at least one claim in that chain is false. Find which
one *cannot be true* given what you observed, and the fix is no longer a guess — it is whatever restores
that claim.

**Why this beats reading code first:** reading code tells you what it does; it does not tell you what it
was *supposed* to do, so you have nothing to compare against and every line looks defensible. The logic
map is the comparison. It is also cheap — it is reasoning, not tool calls — and it tells you which two
files to read instead of eight.

## Hard rule

Map the logic before reading implementation. Build the map before you read implementation code beyond what
the map needs, and before you add any instrumentation. Instrumentation is what you reach for when reasoning has narrowed the fault to two links
and cannot choose between them — not a substitute for narrowing.

If the user asked for a fix, still map first. The map is fast and it is what makes the fix small.
Existing authorization to fix carries through diagnosis. Map, locate, then repair without asking again;
ask again only for changed scope, reserved decisions, or actual security confirmation.

## Phase 0 — Check whether the map already exists

Before deriving anything, look for a `## Logic map` section in the project's architecture or spec file (the
`logic-map` skill writes one). If it is there and current, Phases 1 and 2 are a *read*, not a derivation —
jump to Phase 3 and test the existing chain against the symptom.

Two things to watch. The map states what the system is *supposed* to guarantee, so treat it as the
comparison, never as evidence about what the code does now. And if the map's own dependencies have moved
(a file it names was renamed, a module it describes changed, the project's architecture or spec file is
older than the code), re-derive the links you rely on rather than trusting them —
a stale map is more dangerous than none, because it is persuasive.

## Phase 1 — Decompose into systems

A "system" is anything with a boundary you can state a contract across: a module, a layer, a service, a
build step, a schema, a cache, a scheduler, a third-party API, the filesystem, the clock. Persistent state
and time are systems — they are the two people forget, and they cause the bugs that "make no sense".

For each system in the path of the broken behaviour, write one line:

```
<system> — takes: <input + its invariant> → gives: <output + its invariant> — owns: <the invariant(s) and state it is responsible for> — fails: <throws | degrades | silent>
```

State the contract as you believe it *should* be, from docs, types, tests, and naming — not from reading
the implementation. Believing the implementation is how you inherit the bug into your own model.

The `fails` column is the exception: it CANNOT be assumed, only read. When a system in the path breaks,
its consumers split into those that throw (visible outage) and those that catch-and-continue with a
default (silent degradation) — and grep only names the consumers, it never classifies them. Read each
consumer's error handling before stating blast radius. A blast-radius claim without failure modes
overstates what is down and hides what is quietly wrong — and the quietly-wrong consumer is the more
dangerous finding, because nothing reports it.

Then draw the boundaries data crosses, in order. The boundaries are where bugs live, because that is the
only place two different sets of assumptions meet. A single system with a clean contract is rarely wrong;
two systems that disagree about whether a field can be null, whether a path is absolute, whether a list is
sorted, or whether an id is a string always are.

Say out loud which systems you are *excluding* from the path, and why. An excluded system that turns out
to be in the path is the single most common reason this method fails.

## Phase 2 — Map the logic

Write the causal chain the correct behaviour requires, as numbered links, from trigger to observed output:

```
1. <trigger> happens
2. therefore <claim>          ← because <mechanism>
3. therefore <claim>          ← because <mechanism>
...
N. therefore <correct output>
```

Each link is a claim that must hold for the next to follow, and each names the mechanism that makes it
hold. "Therefore" is doing real work here: if you cannot say why link 4 follows from link 3, you have found
either a gap in your understanding or a gap in the system — and at this stage you do not yet know which.
That ambiguity is fine and worth writing down; Phase 3 resolves it.

Keep links at the grain of *decisions and transformations*, not lines of code. Six to twelve links is
usually right for a feature. If you have thirty, you are transcribing the code instead of modelling it. If
you have three, you have skipped the boundaries where the fault probably is.

## Phase 3 — Locate the fault by contradiction

Now use the symptom. For each link, ask the **impossibility test**:

> If this link held exactly as written, would the observed symptom still be possible?

- **No** → this link is the fault, or the fault is upstream of it. A link whose truth makes the symptom
  impossible, in a world where the symptom demonstrably happens, is false. This is the strongest signal
  available and it costs no tool calls.
- **Yes** → the link survives; the fault is elsewhere. Move on.

Work the chain from the *output end backwards*. The last link that survives the test brackets the fault:
it lives between the last surviving link and the first failing one. Backwards is better than forwards
because you start adjacent to the evidence you actually have.

A contradiction brackets hypotheses; it does not prove a root cause by logic alone. That is why the
bracket gets checked against reality below before anything is built on it.

Three refinements that catch what a naive pass misses:

- **Absences are faults.** "There is no link that re-sorts the list after the merge" is a located fault,
  exactly as much as a wrong line. Ask what claim *would* have prevented the symptom and where it would
  live; "nowhere" is a diagnosis, and usually a better one than any edit to an existing link.
- **A link can be true-but-unordered.** Everything holds individually and the symptom still happens →
  suspect ordering, concurrency, staleness, or caching. Re-ask the test as "if this link held *before*
  link N+1 ran". Intermittent symptoms are nearly always this.
- **Two links can be individually true and jointly wrong.** Each system honours its own contract, but the
  contracts disagree — a field optional on one side and required on the other. The fault is the boundary,
  not either system, and the repair belongs in whichever side owns the invariant.

Then confirm the bracket against reality *once*, cheaply, before building anything: read the two suspect
functions, or run the smallest command that discriminates. You are checking your model, not exploring —
if the read surprises you, your map was wrong and you return to Phase 2 rather than pressing on with a
map you no longer believe.

## Phase 4 — Let the fix follow

The located fault names its own repair, which is why the code is the easy part:

| What Phase 3 found | What the fix is |
|---|---|
| A link whose mechanism doesn't do what the link claims | Correct the mechanism to honour the claim it already advertises |
| A missing link | Add it — at the layer that owns the invariant, not where the symptom appeared |
| Two contracts disagreeing at a boundary | Pick which side owns the invariant, enforce it there, and let the other side rely on it |
| A link that holds but too late | Fix the ordering or the trigger, not the value |

Fix at the link, not at the symptom's location, and not at each caller. When the broken link is shared,
one repair inside it is both smaller and more complete than a guard in every consumer — and the callers
you would otherwise have missed stay fixed. Grep the link's other consumers before you edit, so you learn
whether the repair changes behaviour you did not intend to change.

Then hand off to the disciplined fix loop (`superpowers:systematic-debugging` — Claude Code only, optional;
elsewhere follow the same steps): a failing test that reproduces the symptom first, one change at a time,
rerun the same check on the repaired state. Don't restate them; use them. Its Phase 4.5 rule still applies
and is worth keeping: if three fixes have failed, the architecture is the suspect, not your next hypothesis.
In this skill's terms, three failed fixes means the *map* is wrong — go back to Phase 1 and question a
contract you assumed rather than derived.

## Output format

Lead with the map, because it is the part that survives after the bug is closed:

```
## Systems
<one contract line per system, plus what you excluded and why>

## Logic map
<numbered links with their mechanisms>

## Fault
**Bracket:** link N held, link N+1 cannot have → fault lives between them.
**Fault:** <the false or missing claim, and the artifact/line that owns it>
**Why the symptom looks like it does:** <how the fault reaches the surface where it was reported>
**Confirmed by:** <the one read or command you ran>

## Repair
<the change at the link, its other consumers, and the check that proves it>
```

If the cause is unconfirmed, say so instead of presenting an elegant map as proof: leave **Confirmed by**
empty, call the fault a hypothesis, and name the smallest read or command that would settle it.

## Worked example (compressed)

Symptom: a dashboard shows a project's ship date as yesterday for a few users, correct for everyone else.

- **Systems:** stored project records (own: the date string) → parser (takes text, gives a Date) → scoring
  (takes Date + now, gives "shipped this week") → renderer. Excluded: the network, no fetch in the path.
  *The clock is a system and it owns "now".*
- **Map:** 1. record holds `(2026-07-29)` → 2. parser yields that calendar day → 3. scoring compares it to
  today's calendar day → 4. difference in days is 0 → 5. renders "today".
- **Impossibility test, backwards:** link 5 holds (renderer is a pure format). Link 4 — if the difference
  really were 0, "yesterday" could not render. So the fault is at or upstream of 4. Link 3: comparing a
  *Date* to *now* is not comparing calendar days — a parsed midnight UTC is the previous evening in a
  negative-offset zone. Holding link 3 as written does not make the symptom impossible; holding it as
  *intended* does. Fault found at link 3, and it explains "only some users" without any new evidence:
  those users are the ones west of UTC.
- **Absence check:** there is no link that normalises both sides to one timezone. That's the real fault —
  a missing claim, not a wrong one.
- **Repair:** compare calendar days in a single declared zone, inside the scoring module that owns the
  comparison — not by shifting the string in the parser, which would corrupt every other consumer of the
  date. Then the failing-test-first handoff.

Note what the map bought: the timezone never appeared in the symptom, the stack trace, or the file the
bug was reported against. Reading the renderer first would have found nothing, twice.

## Routing — which debug skill

| Situation | Skill |
|---|---|
| Multi-system, confusing, or a fix already failed; you need to know *where* | **this one**, then hand off |
| Designing or specifying, not fixing — what *should* be guaranteed and by whom | `logic-map` (writes the map this skill reads) |
| Bug's location is already known and local; you need the disciplined fix loop | `superpowers:systematic-debugging` (Claude Code only, optional) |
| Nothing crashed — the product *behaves* wrongly: AI misunderstands, flow frustrates, copy overwhelms | `mission-debug` |
| The code works but is tangled, duplicated, or over-built | `mission-systems-cleanup` |

`mission-debug` is this skill's sibling: same reasoning move — find the layer that *forces* the behaviour —
applied to product promises rather than technical logic. If a "technical" bug turns out to be a product
contract that was never specified, switch to it rather than inventing the missing intent yourself.

## Red flags — you are pattern-matching, not mapping

| Thought | Reality |
|---|---|
| "The trace names this file, so the bug is here" | The trace names where it *surfaced*. Map first; those differ on every interesting bug. |
| "Let me add some logging and see" | Instrumentation discriminates between two candidate links. With no map there are no candidates, so you are collecting noise. |
| "Let me read a few more files for context" | Unbounded reading is the symptom of a missing map. The map tells you which two files matter. |
| "This is probably X, quick fix" | Run the impossibility test on X. If X holding still permits the symptom, X is not it — and you were about to spend the afternoon proving that. |
| "Intermittent, so it's flaky/environmental" | Intermittent almost always means a link that is true but unordered, or state that outlives one run. Re-ask the test with ordering. |
| "The map is obvious, I'll keep it in my head" | Unwritten maps quietly lose the link you were least sure about, which is where the bug is. Write the six lines. |
| "My map says the code should work, so the code is fine" | Then your map is wrong, and that is the finding. A map that cannot explain an observed symptom is refuted by it. |
| "I'll fix it at the call site that broke" | One repair in the shared link fixes the callers you haven't found yet. Guarding each caller does not. |
| "Grep listed the consumers, blast radius done" | Consumers differ in failure mode — one throws, another catches and continues with empty data. Read each catch before claiming what is broken vs silently degraded. |
| "Both files/docs agree, one of them says so" | A claim spanning two artifacts (ordering, compatibility) is only verified by reading BOTH. One file's header asserting "order doesn't matter" does not bind the other file's gate. |
