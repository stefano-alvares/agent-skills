#!/usr/bin/env python3
"""Lint this repo's own skills. Run from anywhere: python3 scripts/check-skills.py

Checks only tracked skills (git ls-files), so the git-ignored third-party
skills that sit in skills/ on a working machine are skipped.

  1. Each active SKILL.md has frontmatter with a name equal to the folder and a
     description of 1 to 1024 characters (the Agent Skills limit). Archived
     skills are not loaded, so only their names are used.
  2. Every references/, scripts/, assets/ or templates/ path a SKILL.md
     mentions exists in that skill, or in another skill named on the same line.
  3. No active skill names an archived skill in backticks as if it were live.
  4. README: every active skill has a row; every skill in a README row is
     active, or archived with "archived" in its row.

Exit 0 when clean, 1 with one line per problem otherwise. Standard library only.
"""
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
problems = []


def tracked_skills(area):
    try:
        out = subprocess.run(["git", "-C", ROOT, "ls-files", f"{area}/*/SKILL.md"],
                             capture_output=True, text=True, check=True).stdout.split()
    except (OSError, subprocess.CalledProcessError):
        base = os.path.join(ROOT, area)
        out = [f"{area}/{d}/SKILL.md" for d in sorted(os.listdir(base))
               if os.path.isfile(os.path.join(base, d, "SKILL.md"))]
    return {p.split("/")[1]: os.path.join(ROOT, p) for p in out}


def frontmatter(text):
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    fields, key, block = {}, None, []
    for line in m.group(1).splitlines():
        top = re.match(r"([A-Za-z_-]+):\s*(.*)$", line)
        if top and not line.startswith((" ", "\t")):
            if key:
                fields[key] = " ".join(block).strip()
            key, value = top.group(1), top.group(2).strip()
            block = [] if value in (">", ">-", "|", "|-", "") else [value]
        elif key:
            block.append(line.strip())
    if key:
        fields[key] = " ".join(block).strip()
    for k, v in fields.items():
        if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
            fields[k] = v[1:-1]
    return fields


active = tracked_skills("skills")
archived = tracked_skills("archive")

for name, path in active.items():
    rel = os.path.relpath(path, ROOT)
    text = open(path, encoding="utf-8").read()
    fm = frontmatter(text)
    if fm is None:
        problems.append(f"{rel}: no frontmatter block")
        continue
    if fm.get("name") != name:
        problems.append(f"{rel}: name '{fm.get('name')}' does not match folder '{name}'")
    desc = fm.get("description", "")
    if not 1 <= len(desc) <= 1024:
        problems.append(f"{rel}: description is {len(desc)} characters (must be 1-1024)")
    skill_dir = os.path.dirname(path)
    for n, line in enumerate(text.splitlines(), 1):
        for ref in re.findall(r"(?<![\w/~.-])((?:references|scripts|assets|templates)/[\w./-]+\.\w+)", line):
            if os.path.exists(os.path.join(skill_dir, ref)):
                continue
            if any(other in line and os.path.exists(os.path.join(ROOT, "skills", other, ref))
                   for other in active):
                continue
            problems.append(f"{rel}:{n}: '{ref}' does not exist")
        for old in archived:
            if old not in active and f"`{old}`" in line:
                problems.append(f"{rel}:{n}: names archived skill `{old}` as if live")

readme_path = os.path.join(ROOT, "README.md")
if os.path.exists(readme_path):
    rows = {}
    for line in open(readme_path, encoding="utf-8"):
        m = re.match(r"\|\s*\*\*([a-z0-9-]+)\*\*\s*\|", line)
        if m:
            rows[m.group(1)] = line
    for name in active:
        if name not in rows:
            problems.append(f"README.md: active skill '{name}' has no row")
    for name, line in rows.items():
        if name in active:
            continue
        if name in archived and "archived" in line.lower():
            continue
        state = "archived but its row does not say so" if name in archived else "not in skills/ or archive/"
        problems.append(f"README.md: '{name}' is {state}")

if problems:
    print("\n".join(problems))
    sys.exit(1)
print(f"OK: {len(active)} active and {len(archived)} archived skills checked.")
