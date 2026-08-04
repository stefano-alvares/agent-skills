# Profile: <model-id>

Status: <observed | provisional — from N sessions on <dates>>

## Phases skipped when unforced
<Which loop phases this model silently drops (e.g. never re-reads the ledger,
skips Look, verifies by introspection). One line each, with the session/incident
that proved it.>

## Pressure settings
- Checklist: <emit once | re-print at every phase | require tick + evidence quote>
- Verification: <standard | force fresh-context verifier | forbid self-review entirely>
- Deviation discipline: <standard | require restate-before-every-step (planning-standard §4.2)>

## Context / memory cadence
<Context window size, degradation point, WORKING_MEMORY re-read frequency,
commit-checkpoint frequency.>

## Known failure modes
<Model-specific: format drift, tool-call reliability, hallucinated APIs,
overconfident dones. Link falsify profile if one exists — don't duplicate.>

## Effort dial
<What "push its limits" means here: where extra passes pay off vs where the
model loops. Cost per session observed.>
