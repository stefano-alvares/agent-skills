# Pre-execution decision burst

Use Stefano as the highest-value product resource in one concentrated exploration before the team starts. This phase is Atlas + Stefano only: no Forge, worker, or Raze lane begins until the reserved decisions are closed and the Ship Spec is approved.

## When

Run for consequential software work with unresolved product direction, scope, architecture, domain/data model, persistence, public behaviour, customization, security/privacy, spend, or reversibility. Skip it for routine, reversible work already decided by an approved spec or established project contract.

## Before asking

Atlas must first:

1. Inspect the relevant repository, callers, project docs, prior decisions, and current behaviour.
2. Research current alternatives using primary documentation and credible measurements where the choice depends on changing technology.
3. Separate facts from assumptions and identify the decisions that actually belong to Stefano.
4. Gather every foreseeable reserved decision into one batch. Do not interrupt him serially with facts that can be retrieved or scope-neutral implementation choices the team can resolve.

## The 1→3→1 packet

Handle one problem or fork at a time, but present the foreseeable packets together.

1. **Problem:** one decision statement, why it matters now, and the current constraints.
2. **Three options:** exactly three genuinely viable options under those constraints. For each, give its fit, evidence, material trade-offs, and reversibility or migration cost. No strawmen and no cosmetic variants.
3. **Recommendation:** choose one, explain why it best serves the approved outcome, and state the evidence or changed condition that would reverse the recommendation.

“Absolute best” cannot be guaranteed honestly. The obligation is the three strongest credible options found under current evidence and project constraints.

Stefano chooses, modifies, or rejects the recommendation. A recommendation never authorizes itself.

## Flexibility standard

Prefer architecture that is cheap to change, not architecture that predicts every future:

- isolate genuinely volatile boundaries behind clear contracts;
- keep persistence, retrieval, providers, and external services replaceable where change is plausible;
- define migration and rollback paths when state is durable;
- use configuration only for known variation;
- avoid speculative layers, generic frameworks, and abstractions with no current second use.

The target is the simplest implementation that meets today’s requirement without trapping tomorrow’s change.

## Close and hand off

After Stefano’s answers, Atlas refines the decision set once, states any remaining unknowns, and binds the decisions into the Ship Spec. Atlas then gives the approved inputs and execution command to Forge. Forge plans inside those decisions; one worker implements; Raze reviews read-only; Atlas verifies evidence, coordinates any authorized repair, and owns progress to shipment.

If an unforeseen reserved decision appears after the gate, park only the affected path, continue unrelated authorized work, and return a 1→3→1 decision packet to Stefano. Never let Forge, a worker, Raze, or Atlas silently convert a recommendation into product or architecture authority.
