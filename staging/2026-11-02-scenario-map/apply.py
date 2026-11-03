#!/usr/bin/env python3
"""Switch the scenario-map drafts live (engineering-god, 2 Nov 2026). Run ONLY after Stefano's Atlas test ends.
Idempotent: each edit checks whether it is already applied. Backs up every touched file first.
  python3 apply.py            dry run (shows what would change)
  python3 apply.py --apply
Rollback: restore from the backup folder printed at the end (same relative paths).
"""
import os, sys, shutil, datetime

H = os.path.expanduser('~')
STAGE = os.path.dirname(os.path.abspath(__file__))
APPLY = '--apply' in sys.argv
BK = f'{H}/.hermes/backups/scenario-map-switch-{datetime.date.today().isoformat()}'
log = []

def backup(p):
    rel = os.path.relpath(p, H)
    dst = os.path.join(BK, rel)
    if APPLY and os.path.exists(p) and not os.path.exists(dst):
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(p, dst)

def edit(path, old, new, label):
    p = os.path.expanduser(path)
    s = open(p).read()
    if new in s:
        log.append(f'skip (applied) {label}'); return
    if s.count(old) != 1:
        raise SystemExit(f'ANCHOR {s.count(old)}x in {path} for {label}')
    backup(p)
    if APPLY: open(p, 'w').write(s.replace(old, new))
    log.append(f'edit {label}')

def copy(src, dst, label):
    d = os.path.expanduser(dst)
    if os.path.exists(d) and open(d).read() == open(src).read():
        log.append(f'skip (same) {label}'); return
    backup(d)
    if APPLY:
        os.makedirs(os.path.dirname(d), exist_ok=True); shutil.copy2(src, d)
    log.append(f'copy {label}')

# 1. logic-map v2
copy(f'{STAGE}/logic-map/SKILL.md', '~/.agents/skills/logic-map/SKILL.md', 'logic-map SKILL.md v2')
copy(f'{STAGE}/logic-map/references/scenarios-format.md', '~/.agents/skills/logic-map/references/scenarios-format.md', 'logic-map scenarios-format.md')

# 2. diagnose: start from the scenario
edit('~/.agents/skills/diagnose/SKILL.md', '## 1. Build a red loop',
'''## 0. Start from the scenario (mapped projects)

If the project has `docs/crew/scenarios.json`, find the scenario the symptom breaks and run
`node ~/.hermes/tools/scenarios/scenarios.mjs check <root> <id>`. Its `want` and `expected` are the desired
output; its steps are the chain (step 3 is half done); the first failing step, when probes exist, is your
first bracket. No scenario covers the symptom: that is a finding for `logic-map`. After the fix, re-run
`check` and `sync` so the map shows it met.

## 1. Build a red loop''', 'diagnose step 0')

# 3. crew-board router: the map gate
edit('~/.hermes/profiles/atlas/skills/crew-board/SKILL.md',
'''- Plan with `plan-forge` in the mode the risk calls for (light, standard, high-risk).''',
'''- Write the Ship spec with `ship-spec`, then plan with `plan-forge` in the mode the risk calls for (quick, light,
  standard, high-risk).
- **The map gate.** A new app, new site, new process or big feature: `logic-map` first (his wanted
  scenarios, the rules and owners, drawn on a Floorplan blueprint). Show him the map and wait for his OK
  before building. Small batches skip it.
- **Mapped projects** (`docs/crew/scenarios.json` exists): after each round, refresh the map, mark recent
  work, run `scenarios.mjs check` and `sync`; the round report carries its table (met, not met,
  unchecked). Commands: `logic-map`, `references/scenarios-format.md`.''', 'crew-board map gate')

# 4. dev-build
edit('~/.hermes/profiles/atlas/skills/dev-build/SKILL.md',
'''- New systems or invariants: `logic-map` before the plan.''',
'''- New app or big feature, or new rules with no owner: `logic-map` before the plan (scenarios, owners,
  the map gate in `crew-board`). A mapped project: read `docs/crew/scenarios.json` first; the batch's
  definition of shipped includes the scenarios it touches being met.''', 'dev-build logic-map line')
edit('~/.hermes/profiles/atlas/skills/dev-build/SKILL.md',
'''per change, the checks run with results, decisions needed, and his exact commands''',
'''per change, the checks run with results, the scenarios table on a mapped project, decisions needed,
and his exact commands''', 'dev-build hand-back table')

# 5. plan-forge
edit('~/.agents/skills/plan-forge/SKILL.md',
'''| New systems or invariants with no owner | `logic-map` first |''',
'''| New app, process or big feature; rules with no owner | `logic-map` first (scenarios and the map; his OK before building) |''',
'plan-forge routing row')
edit('~/.agents/skills/ship-spec/SKILL.md',
'''"Looks good" is not a line; "he approves the preview" is, when taste is the point.''',
'''"Looks good" is not a line; "he approves the preview" is, when taste is the point. On a mapped project
(`docs/crew/scenarios.json`), the scenarios the batch touches being met is one of the lines.''',
'ship-spec definition of shipped (was plan-forge)')

# 6. Atlas SOUL
edit('~/.hermes/profiles/atlas/SOUL.md',
'''  - planning `plan-forge`, with `logic-map` first when the work adds systems or invariants;''',
'''  - planning `ship-spec` (what ships and how he will know it is done), then `plan-forge`, with `logic-map` first for a new app, site, process or big feature (his scenarios on a Floorplan map he approves before building; `floorplan` draws it);''',
'atlas SOUL skills line')

# 7. Atlas gets the floorplan skill
link = f'{H}/.hermes/profiles/atlas/skills/floorplan'
if os.path.islink(link) or os.path.exists(link):
    log.append('skip (exists) atlas floorplan link')
else:
    if APPLY: os.symlink(f'{H}/.agents/skills/floorplan', link)
    log.append('link atlas floorplan -> ~/.agents/skills/floorplan')

print('\n'.join(log))
print(('APPLIED; backups in ' + BK) if APPLY else 'DRY RUN (pass --apply)')
