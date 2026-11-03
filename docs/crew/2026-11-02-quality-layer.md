# Quality layer (lead: engineering-god)

## His words (verbatim)

> Also since youre going to be a tuner, do you want to take over the reviewer role of argus? I think its the
> best fit. I need a really good system to keep good code quality and architecture

## Decided (clarify, 2 Nov 2026)

- Team shape: keep Argus (Sonnet) on per-card review; engineering-god owns the quality layer above it.
- Findings: to Stefano first as a short digest; Atlas acts only on his yes.
- Cadence: batch-end architecture review on code batches, plus a weekly sweep.

## The layer (as proposed and accepted)

| Layer | Who | When | What |
|---|---|---|---|
| Card gate | Argus (Sonnet), unchanged | every card with checkable risk | one round, PASS or one finding |
| Done-gate | Atlas / Mason | every change | falsify plus the repo's CONSTRAINTS.md floor |
| Architecture review | engineering-god (Opus), read-only | end of each code batch touching a mapped area or 8+ files | raze-review mode A on the integrated batch against scenarios.json, rule owners, budgets; digest to Stefano |
| Quality ratchet | engineering-god (mechanical part on Sonnet) | weekly | health trend (health.jsonl), knip unused, deps, scenario checks, files past size limits; one digest |
| Standards | engineering-god, Stefano decides | when patterns recur | CONSTRAINTS.md floors, Argus checklist, budgets |
| Reviewer audit | engineering-god | monthly sample | re-check a few Argus PASSes for missed defects |

Architecture decisions stay Stefano's.

## Built (3 Nov 2026)

- Skill `quality-layer` on engineering-god (procedures, digest format); SOUL duty line added (backup:
  ~/.hermes/backups/quality-layer-2026-11-03/).
- `~/.hermes/tools/quality/sweep.py`: read-only weekly data (health without history, scenarios --no-save,
  large files, stale crew branches, deltas). First real run on revision-app: health 8.2, repo untouched,
  4 min per repo.
- Cron "quality sweep" (e23a54ce3c60): Mondays 03:00, catches up on wake, note into the engineering-god chat.
- Batch-end trigger: `~/.hermes/tools/quality/request-review.py <repo> <batch> [branch]` appends to
  engineering-god's inbox; cron "batch reviews" (9b5858d38b7c, hourly) wakes only when a request is pending.
  Tested: request, dedupe, bad path refused, recorded review clears it.
- Finding: Atlas cannot use message_agent from Telegram (Hermes injects it only into a bot's Bot Chat), so the
  trigger is a script, not a ping.
- Staged, not live: `~/.agents/staging/2026-11-02-scenario-map/apply-quality.py` adds the request step to
  Atlas's crew-board and dev-build. Apply with the scenario-map switch after his Atlas test.

## Not built

- Monthly Argus audit: procedure in the skill; no schedule yet (run by hand monthly until it proves useful).
