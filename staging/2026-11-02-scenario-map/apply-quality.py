#!/usr/bin/env python3
"""Stage 2 of the switch: quality-layer hooks in Atlas's playbooks. Run with apply.py, after his Atlas test.
  python3 apply-quality.py [--apply]
"""
import os, sys, shutil, datetime
H = os.path.expanduser('~')
APPLY = '--apply' in sys.argv
BK = f'{H}/.hermes/backups/scenario-map-switch-{datetime.date.today().isoformat()}'
log = []

def edit(path, old, new, label):
    p = os.path.expanduser(path); s = open(p).read()
    if new in s: log.append(f'skip (applied) {label}'); return
    if s.count(old) != 1: raise SystemExit(f'ANCHOR {s.count(old)}x in {path} for {label}')
    dst = os.path.join(BK, os.path.relpath(p, H))
    if APPLY and not os.path.exists(dst):
        os.makedirs(os.path.dirname(dst), exist_ok=True); shutil.copy2(p, dst)
    if APPLY: open(p, 'w').write(s.replace(old, new))
    log.append(f'edit {label}')

edit('~/.hermes/profiles/atlas/skills/crew-board/SKILL.md',
'''Never let one worker merge another's conflicting work.''',
'''Never let one worker merge another's conflicting work.

**Batch end, code batches** that touched a mapped area or 8+ files: once integrated, request the
architecture review: `python3 ~/.hermes/tools/quality/request-review.py <repo> <batch file> <batch branch>`.
engineering-god reviews it read-only within the hour and reports to Stefano; do not wait for it, and act on
its findings only when he says so.''', 'crew-board batch-end ping')

edit('~/.hermes/profiles/atlas/skills/dev-build/SKILL.md',
'''## 5. Hand back''',
'''## 5. Hand back

If the batch touched a mapped area or 8+ files, request the architecture review (`crew-board` section 7)
before your final report, and say in the report that it was requested.
''', 'dev-build batch-end ping')

print('\n'.join(log))
print(('APPLIED; backups in ' + BK) if APPLY else 'DRY RUN (pass --apply)')
