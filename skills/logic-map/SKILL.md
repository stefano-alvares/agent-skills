---
name: logic-map
description: "Use when starting a feature or app and the design should be right before the code: map the app, feature or spec into its systems, the invariants each system owns, and the causal chains that must hold. Also use when comparing ways to split a system, checking a spec against code that may have drifted, onboarding onto an unfamiliar codebase, or when asked to 'map the logic', 'what are the systems here' or 'where do the contracts live'. Run before plan-forge: the map decides what is correct, plan-forge sequences the work. Skip for a single-file change with no new invariant."
---

# Logic Map

Code is the cheapest part of a system and the most replaceable. Logic is neither. A codebase where the
logic is right and the code is ugly can be cleaned up incrementally; a codebase where the code is elegant
and the logic is wrong has to be rethought, and usually gets patched instead.

**Core principle:** design the *claims* the system must guarantee and *who owns each one*, then let the
implementation be whatever fills that box. A well-drawn box makes a whole class of bugs impossible to
write, which is worth more than any amount of careful coding inside a badly-drawn one.

**Why a map rather than a plan:** a plan sequences work — do this, then that. A map states what must be
true regardless of order. Plans go stale the moment the order changes; maps only go stale when the
system's promises change, which is much rarer and much more worth noticing. `plan-forge` sequences the
work; run this first so it sequences the *right* work.

## Where the map lives

The project already has the right home: its architecture or spec file, under a `## Logic map` section,
next to the `## Invariants` and `## Data shapes & contracts` sections it complements. Don't create a
parallel document — a map that lives beside the invariants it complements gets read and updated when they
move.

For a project with no architecture or spec file, put it at the top of the spec it came from. One map, one
home.

## Phase 1 — Harvest what is promised

Before naming any system, collect the claims the thing is supposed to guarantee. Sources, in priority
order: the batch file's Decided section or `docs/crew/decided.md` (newest wins — decisions beat briefs), the
batch file's scope, the spec, the invariants already in the project's architecture or spec file, the
product docs. For an existing codebase also read the tests: a test is an
invariant someone cared enough to freeze.

Write them as **invariants** — statements that must be true after any operation, not features:

- Good: "a question is never shown to a learner without a source chunk attached."
- Bad: "the app shows questions." That's a feature; it can't be violated, so it can't guide a design.

If a promise only exists in someone's head, that is the most valuable output of this phase — write it
down and flag it, because an unstated invariant is the one no system will own.

## Phase 2 — Name the systems and give each one a box

A system is anything you can state a contract across. One line each, in a shape a debugger can read later:

```
<system> — takes: <input + its invariant> → gives: <output + its invariant> — owns: <invariant(s)> — fails: <throws | degrades | silent>
```

The `fails` column declares what a consumer may assume when this system breaks: throw (callers see the
outage), degrade (callers get a documented default), or silent (callers get nothing and no signal —
which should be a deliberate choice, almost never the right one). For existing code this column is
*read*, never assumed — grep names consumers, only their catch blocks classify them.

The `owns` column is where the design happens. Then apply the two rules that do most of the work:

- **Every invariant has exactly one owner.** Two owners means two places to change and two chances to
  disagree — that is a bug generator, and it is the origin of most "we fixed it but it came back". Zero
  owners means the invariant is aspirational; the system does not actually guarantee it, whatever the
  docs say.
- **The owner should be the narrowest system that *can* enforce it.** An invariant enforced at the
  database is stronger than one enforced in a service, which is stronger than one enforced in a
  component, which is barely enforced at all. Push each one down as far as it will go.

Now the boxes exist. Inside a box, implementation is free — any code that honours `takes`/`gives`/`owns`
is correct, and can be rewritten later without consulting anyone. That freedom is the whole point: it is
what makes the code disposable and the map durable.

## Phase 3 — Map the causal chains

For each user-visible behaviour, write the chain that must hold, as numbered links naming their mechanism:

```
1. <trigger>
2. therefore <claim>     ← because <mechanism, and which system owns it>
3. therefore <claim>     ← because <mechanism, and which system owns it>
N. therefore <correct outcome>
```

Six to twelve links per behaviour. Every link names its owning system — a link no system owns is a gap in
the design, discovered on paper instead of in production. Map the two or three behaviours that carry the
product's promise, not all of them; a map of everything is a transcription and nobody maintains it.

## Phase 4 — Attack the map before it becomes code

This is the phase that pays for the skill. Four tests, in order (the mismatch test applies to existing code only):

**The violation test** — for each invariant, ask: *can any system violate this without another system
noticing?* If yes, the design permits the bug, and no amount of careful implementation prevents it
forever. Move the invariant to a boundary where violating it is structurally impossible — a type that
can't represent the bad state, a schema constraint, a single chokepoint every caller goes through. This
is how you choose between designs: prefer the decomposition that makes more invariants *unviolatable*
rather than the one that reads more nicely.

**The gap test** — walk each chain and ask what happens when a link's precondition doesn't hold. Empty
input, second concurrent call, retry after partial failure, clock moving backwards, the dependency being
down. A chain that only describes the happy path is half a design, and the missing half is where the
bugs go.

**The domain test** — for each input a chain consumes, enumerate its *actual* value domain — every enum
member, every mode/board/type value that can reach the link, plus null and absent — and walk the chain
once per class, not once for the typical value. The class you didn't enumerate (the `Custom` board, the
legacy row with the null column, the script-only caller) is where a gate designed for the mainstream
silently blocks or breaks the outlier. Where do the domain's values live? If the answer is "a string
column" rather than a type or table, list them by query before trusting the list in your head.

**The mismatch test** (existing code only) — derive a second map from what the code actually does, and
diff it against the map from Phase 1's promises. Every difference is exactly one of three things: an
undocumented decision, a bug or vapour, or two owners. Naming which is the deliverable. The table of what
each means and where it goes is in `references/worked-example.md`.

## Evidence rules — what a map may claim

A map (or a spec/plan derived from one) earns trust only if its factual claims survive contact with the
artifacts they cite. Three rules, each bought by a real spec error:

1. **Artifact claims are read, not remembered.** Any claim citing a file, schema, migration, type, or
   line is verified by opening it before it goes in the map. A plan that writes data conforming to an
   existing schema reads the schema's actual types first — a literal union rejects the value you invented
   for it. Mark anything you could not verify `⚠ assumed`, visibly.
2. **Cross-artifact claims require reading BOTH artifacts.** "These two migrations can run in either
   order", "these modules are compatible" — one file's header comment asserting it does not bind the
   other file's own gate. The contradiction between two artifacts is exactly the kind of fact neither
   one states.
3. **A shared-contract change sweeps the whole compile scope.** When the chosen decomposition changes a
   type or signature, the consumer list spans everything the compiler sees — tests, scripts, eval
   harnesses — not just runtime paths. `tsconfig`'s `include` is the boundary, not `src/`. The caller
   you find in `scripts/` after shipping was findable by one grep before.

## Phase 5 — Choose the decomposition

When more than one split is plausible, lay them side by side and compare on these, in order:

1. **Invariants made impossible to violate** — more is better, and this outranks everything below.
2. **Number of boundaries where two assumptions meet** — fewer is better; every boundary is a place for
   two systems to disagree.
3. **Blast radius of the most likely change** — which split confines the change you already expect?
4. Only then: familiarity, ecosystem, and how pleasant it is to write.

Elegance that loses on 1 and 2 is a trap; it reads well and it generates bugs. Record the rejected
options and why in one line each — the next person to propose the rejected split deserves the reason,
and that person is usually you in three months.

## Output format

```
## Logic map — <feature or app>
*Derived from: <sources>. Owns: the claims below. Code inside each box is free to change.*

### Invariants
- <invariant> — owned by <system>
- <invariant> — owned by <system>  ⚠ unowned / two owners  ← flag, don't hide

### Systems
<one takes/gives/owns line per system>

### Chains
<numbered links per behaviour, each naming its owning system>

### Attacks
**Violations possible:** <invariant → who can break it unnoticed → where to move it>
**Gaps:** <link → unhandled precondition>
**Mismatches:** <spec-vs-code differences, each classified: undocumented decision, bug or vapour, or two owners>

### Decomposition chosen
<the split, and the rejected alternatives with one-line reasons>

### Budgets  ← write into the batch file's Decided section or docs/crew/decided.md
<per-section expected shape: ≈files, LOC ceiling, deps allowed — derived from
the decomposition, never from existing code. raze-review judges against these.
A map without them is still a map — missing budgets do not block.>
```

Then hand off: `plan-forge` turns the map into ordered steps. Each step's
done-check writes itself from the map — a step is done when the invariant it was supposed to establish
actually holds, which is a far better check than "tests pass".

For a team handoff, make the relevant invariant, enforcement owner, failure behavior, and observable acceptance clear to implementers and reviewers. Identify the integrated or reviewed state when a claim depends on implementation. Put this context in the existing assignment or map; do not require a new document or whole-app map.

## Worked example

The dashboard ship-date example, and the mismatch classification table, are in `references/worked-example.md`.

## Routing

| Situation | Skill |
|---|---|
| What should this system guarantee, and who owns it | **this one** |
| In what order do we build it | `plan-forge` |
| Did the implementation honor this map | `raze-review` — its blind architect reads this map |
| Something is broken and we don't know where | `diagnose` |
| The product behaves wrongly but nothing is broken | `mission-debug` |

A project with a current `## Logic map` makes debugging mostly a lookup, because the chain is already
written and only needs testing against the symptom.

## Red flags — you're drawing boxes around code instead of logic

| Thought | Reality |
|---|---|
| "The systems are just the folders/services we already have" | Then you mapped the implementation, not the logic. Ask what each *guarantees*; some folders own nothing and some invariants live nowhere. |
| "This invariant is obvious, everyone knows it" | Unwritten invariants have no owner, and unowned invariants are false. Write it. |
| "We'll handle that edge case in the code" | If a system *can* violate an invariant, eventually it will. Move it to where violating is impossible, then the code doesn't have to remember. |
| "Both designs are fine, pick either" | Run the violation test. The one that forecloses more bugs wins, even if it reads worse. |
| "Let me map every feature for completeness" | A map of everything is a transcription nobody updates. Map the promise-carrying behaviours. |
| "The code and spec disagree, I'll update the spec" | First classify it — undocumented decision, bug, or two owners. Silently updating the spec turns a bug into a documented feature. |
| "I'll write the map after building, when I know more" | Then it records what you did, not what is correct, and it can never contradict the code — which is the only useful thing a map does. |
| "The doc/header says so, good enough" | A claim spanning two artifacts is verified by reading both. Repeating one file's comment about another file is how "order does not matter" ships next to a gate that says STOP. |
| "I checked the callers in src/" | The compiler checks tests, scripts, and eval harnesses too. Sweep the tsconfig scope or the build breaks in the file you skipped. |
