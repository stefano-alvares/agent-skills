# Profile: deepseek-v4-flash

Status: provisional — evaluation planned 2026-08-01 (obs 4659), not yet run.
Everything below is prior + falsify's profile, to be replaced by observed
behavior after the first full-loop session at maximum pressure.

## Phases skipped when unforced
UNVERIFIED — assume the common weak-model set until measured: ledger not
re-read (buried asks dropped), Verify done by introspection, Look skipped
entirely, stops at first plausible output.

## Pressure settings
- Checklist: re-print at every phase until measured otherwise
- Verification: force fresh-context verifier; forbid bare self-review
- Deviation discipline: require restate-before-every-step

## Context / memory cadence
UNVERIFIED. Start with WORKING_MEMORY re-read on every resume + commit
checkpoint per green step.

## Known failure modes
See `falsify/profiles/deepseek-v4-flash.md` for the refutation-side profile.

## Effort dial
Unknown. First session: full loop, maximum pressure, log everything it skips
to SCORECARD.md, then write this profile from evidence.
