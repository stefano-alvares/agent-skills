# Worked example (compressed)

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
