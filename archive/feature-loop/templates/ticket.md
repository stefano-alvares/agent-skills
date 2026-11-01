# Ticket — <name>

## Goal

One line, zero-context, feature/logic terms: what this ticket changes in the app — what works after that did not before. Never a restatement of the diff. The worker's prompt leads with this line.

-

**Done-line (behavior terms):**

-

## Row (Tickets database)

| Property | Value |
|---|---|
| Name |  |
| Feature |  |
| State |  |
| Depends On |  |
| Unblocks |  |
| Attempts |  |
| Attempt Cap |  |
| Wall Clock Cap |  |
| Plan SHA256 |  |
| Idempotency Key |  |
| Envelope | (one-line summary; full envelope below — the `light`/`riskiest` flags live inside this text, no dedicated DB property) |
| Evidence | (filled at completion) |

## Envelope

- Flags: {riskiest / light / neither} (light test in SKILL.md, Ceremony scales)
- Allowed paths:
- Allowed commands:
- Effect surfaces of allowed commands (lockfiles, generated files, caches):
- Forbidden actions:

## Proof obligations

What the coordinator will run to verify. A proof no broader than the finding it comes from. Every negative proof names its positive control.

-

## Evidence

Filled at completion:

-

## Stop conditions / block route

- Stop if:
- On block: set State = TicketBlockedForStefano; coordinator sends a decision packet. Silence changes nothing.
- On envelope-wrong (the envelope, stop condition, or proof obligation is itself demonstrably wrong): return `envelope-wrong` with the proposed amendment and reasoning; the coordinator rules. Never violate the envelope to be right.
