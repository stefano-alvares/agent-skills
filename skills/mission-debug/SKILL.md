---
name: mission-debug
description: Diagnose product behaviors that "feel wrong" — flow, explanations, AI outputs, generated content, teaching quality, tone — by tracing the felt symptom to the exact contract, prompt, schema, state rule, or UI affordance that FORCES it, then judging the root cause against the product's own mission docs. Use whenever the user says something "feels wrong/off/broken" about how their app behaves (not crashes), reports that an AI feature misunderstands users or explains badly, asks why a flow is frustrating, wants a "big repair" of product behavior, or asks to find more behaviors like a known-bad one. Also use before rewriting prompts or UX copy in response to a complaint — the wrongness usually lives one layer below where it is felt, and this skill finds that layer first. Not for crashes, test failures, or stack traces (use systematic-debugging) and not for code-structure cleanup (use mission-systems-cleanup).
---

# Mission Debug

Systematic debugging for product behavior. The "bug" is not a crash — it's a surface that violates the product's mission: an AI that misunderstands, an explanation that overwhelms, a flow that tests instead of teaches, a revision that can't revise. The user reports a *feeling*; your job is to find the *mechanism*.

**Core principle (the Iron Law, inherited):** no repairs without root cause. A felt wrongness always has a forcing mechanism — a schema, prompt, state rule, or affordance that makes the bad behavior inevitable. Patching the copy on top of a forcing contract is a symptom fix, and symptom fixes are failure.

**Second principle (inherited from mission review):** the standard of judgment is the product's OWN mission, not generic quality. Read the canonical product docs first. A behavior is wrong because it breaks a promise the product makes — name the promise.

## Hard rule

Diagnose first, always. Produce the diagnosis output before proposing or making any change. If the user already asked for fixes, still diagnose first — then spec repairs at the root layer only.

## Phase 1 — Reproduce the feeling

You cannot debug a behavior you haven't experienced.

1. **Read the mission docs first** — whatever defines the product's promises (product system doc, spec, README). Extract the 3–6 promises the product makes to its user. These are your assertions.
2. **Walk the surface as the target user**, not as the developer. Use the persona the docs define (skill level, vocabulary, patience). Drive the real app (browser, CLI, device) through the flow where the wrongness was reported — and do what a frustrated real user does: give vague input, give a weak answer, fail twice, ask for the thing you're not supposed to get.
3. **Capture verbatim evidence.** Screenshot or copy the exact prompt text, AI output, button states, and copy. Diagnosis quality is capped by evidence quality — "the explanation was complex" is a symptom; the six-line spec-register paragraph is evidence.
4. **Name each symptom in the user's terms**, one line each: *"the AI needs me to be very specific"*, *"revision only adds points"*. Resist translating to technical language yet — the user's phrasing tells you which promise broke.

## Phase 2 — Trace to the forcing layer

Product behavior in AI-driven apps is downstream of a stack of governing artifacts. Walk DOWN this ladder for each symptom until you find the layer that *forces* the behavior:

1. **Copy/UI text** — what the surface says.
2. **Affordances** — what actions exist, what's disabled, what's hidden, what order things appear in.
3. **State rules** — what transitions/gates the reducer or flow logic allows.
4. **Prompt/policy text** — what the model is instructed to do.
5. **Contract/schema** — what responses can structurally exist.
6. **Data/config** — taxonomies, thresholds, seed content, difficulty bounds.

**The forcing test, at each layer:** *could a maximally good model / perfectly-written copy still produce the right behavior under this layer's constraints?*
- If NO → you've found the root. ("The schema can only return a scope — it cannot ask a clarifying question. Given a vague idea the model is FORCED to guess.") Stop descending; this is the repair layer.
- If YES → the layer below is suspect; keep descending. ("The prompt says *preserve the previous scope* — the misunderstanding the user wants corrected is in context marked keep-this.")

Cite the exact artifact and line: the schema field that doesn't exist, the prompt sentence that forbids, the guard that never fires, the compound question the compiler emitted. If you can't point at it, you haven't found it — you're still describing the symptom.

**Absences force too.** A missing difficulty bound, a missing voice contract, a missing escalation branch are root causes exactly as much as a wrong line. Ask: "what constraint would have prevented this, and where is it?" The answer "nowhere" IS the diagnosis.

## Phase 3 — Judge against the mission

For each root cause, name the specific promise it breaks, quoting the product's own docs. Two questions do most of the work:

- **Does this surface do the product's job, or merely gesture at it?" (e.g., for a teaching product: does this surface TRAIN, or merely TEST? For a trust product: does this surface prove, or merely claim?)
- **Whose skill does this surface assume?** The most common mission bug: the surface demands the exact skill the product exists to build ("the front door hands the learner a blank textarea and grades them on specification — the skill they came to learn").

If a behavior is annoying but breaks no promise, say so and rank it low. Mission-debug is not a polish pass.

## Phase 4 — Sweep for siblings

A forcing mechanism is never used once. Before writing the report:

- Grep every consumer of the same contract/schema — do they force the same wrongness elsewhere?
- Every surface sharing the same prompt style or missing constraint (no voice contract in prompt A → check prompts B–F).
- Every flow shaped like the broken one (if Reason dumps five corrections, check review/transfer/explain feedback too).
- List suspected siblings you did NOT walk, explicitly, so the sweep is honest about its coverage.

## Output format

Per behavior, in severity order (mission-breaking first):

```
### N. <symptom in the user's words>
**Felt as:** what the user experiences, one sentence.
**Root cause:** the forcing layer + exact artifact/line + the forcing test result.
**Broken promise:** the mission doc line it violates.
**Repair (root layer):** what changes at the forcing layer — contract, prompt, rule — never just copy on top. Include cost (calls/hours) when the product has stated budgets.
```

Close with: the sibling-sweep list (walked vs suspected), and — for any contested or expensive repair — the 1-3-1 treatment (one problem, three viable repairs with tradeoffs, one recommendation).

Then STOP. Repairs are implemented only after the diagnosis is accepted, and only at the diagnosed layer.

## Worked example (compressed)

Symptom: *"the AI needs you to be very specific and sometimes doesn't understand you"* (project-intake step).
- Layer walk: copy fine → affordance fine → prompt says "create a focused scope from the idea" → **schema: response can ONLY be a scope; no question type exists.** Forcing test: even a perfect model must guess when the idea is vague. Root found: contract layer.
- Broken promise: product's own thesis says decomposition/specification is the skill the learner lacks — yet the first screen demands it unsupported.
- Repair at root: response contract gains a `questions` variant (≤3, one round, then must propose). Copy improvements alone would have been a symptom fix.
- Sibling found by the sweep: revision "only adds points" — same contract family; prompt says *preserve previous scope*, so re-conception is structurally impossible. Second repair: a `rethink` revision mode that passes the old scope only as a negative example.

## Red flags — you're about to symptom-fix

| Thought | Reality |
|---|---|
| "I'll just improve the prompt wording" | Run the forcing test first. If the schema forces it, no wording survives contact. |
| "The explanation needs editing" | One bad explanation is copy. Every explanation bad the same way = missing voice contract (config layer). |
| "Users should be more specific" | The surface assumes the skill the product exists to build. That's the bug. |
| "Add a tooltip explaining it" | Explaining a wrong behavior is not repairing it. |
| "This one's obvious, skip the walk" | Un-walked diagnoses produce plausible-but-wrong roots. The walk is the evidence. |
