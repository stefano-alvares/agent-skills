# scenarios.json format (scenarios@1)

Lives at `<root>/docs/crew/scenarios.json`. Validated by `scenarios.mjs validate`; drawn by `sync`.

```json
{
  "$schema": "scenarios@1",
  "rules": [
    { "id": "r-no-fake-coverage", "rule": "AS Level never generates a question without enough real examples",
      "owner": "lib.coverage", "enforced_in": "src/lib/as-coverage.ts",
      "check": { "run": "npx tsx --test src/lib/as-coverage.test.ts" } }
  ],
  "scenarios": [
    { "id": "as-refuses", "title": "AS Level refuses what it cannot ground",
      "want": "Stefano's words: what he wants",
      "expected": "the observable result",
      "steps": [
        { "node": "web.quiz", "note": "The student asks for short-answer Waves questions" },
        { "node": "lib.coverage", "note": "Counts the real examples", "because": "the floor is 3",
          "rule": "r-no-fake-coverage", "probe": "npx tsx --test src/lib/coverage-plan.test.ts" }
      ],
      "check": { "run": "npx tsx --test src/lib/as-coverage.test.ts", "expect": "optional regex", "timeout": 300 }
    }
  ],
  "questions": [ { "question": "Open decision, in plain words", "about": ["node ids or file paths"] } ]
}
```

| Field | Meaning |
|---|---|
| `rules[].owner` | One Floorplan node id. Empty means nothing guarantees it (shown under Review). |
| `rules[].enforced_in` | The file that enforces it; the map pins a note there. |
| `rules[].check` | Optional; written back as `status` holds / broken. |
| `scenarios[].want` | His words. Never paraphrase into a feature list. |
| `scenarios[].steps[].node` | A node id (preferred: survives blueprint to code) or a file path. |
| `scenarios[].steps[].probe` | Optional cheap command proving that link; runs only after a failed check. `validate` warns about steps with no probe. |
| `scenarios[].steps[].covered_by` | Optional: a test file the scenario's check already runs that crosses this link (silences the warning). |
| `scenarios[].steps[].external` | `true` for a step on an outside service that cannot be checked offline. |
| `scenarios[].check` | `{run, expect?, timeout?}` or `{manual}`. Exit 0 met, other not met, 3 could not measure. |
| `status`, `measured`, `failed_step` | Written by `check` and `set`; do not edit by hand. `planned` before code exists. |

Commands (root = the folder holding `docs/` and `floorplan/`):

```
node ~/.hermes/tools/scenarios/scenarios.mjs validate <root>
node ~/.hermes/tools/scenarios/scenarios.mjs check <root> [scenario ids]
node ~/.hermes/tools/scenarios/scenarios.mjs set <root> <id> "met" --evidence "what was observed"
node ~/.hermes/tools/scenarios/scenarios.mjs sync <root>        # writes into the map and rebuilds it
node ~/.hermes/tools/scenarios/scenarios.mjs report <root>      # markdown table for reports
```

On the map: each scenario is a flow titled with its status (Met, NOT MET, Unchecked, Planned); each part
lists the rules it guarantees and the scenarios through it; Review lists scenarios not met (important),
broken rules (important), unowned rules and open questions (worth fixing) and unchecked scenarios (minor).
