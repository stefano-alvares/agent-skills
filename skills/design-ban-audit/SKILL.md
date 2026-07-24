---
name: design-ban-audit
description: >-
  Mechanical grep audit for Stefano's design ban-patterns — the mid-fi tells. Use before calling any UI/CSS
  work done, when auditing an existing frontend for generic-AI aesthetics, or as the ban-list step of
  frontier-gap Protocol 4 (UI) / pixel-critique-loop. Origin: the-one-jewellery DESIGN.md audit (June 2026).
---

# Design Ban Audit

Run these against the changed CSS/markup (adjust paths). Every hit is a finding: fix it or justify it in
one line. Zero silent passes.

```bash
# gradient text
grep -rn "background-clip: text\|-webkit-background-clip" --include="*.css" --include="*.astro" --include="*.tsx" src/
# glassmorphism
grep -rn "backdrop-filter" --include="*.css" --include="*.astro" --include="*.tsx" src/
# layout-property animations (jank + amateur tell)
grep -rnE "transition:.*\b(height|width|top|left|margin|padding)\b" --include="*.css" src/
# borders thicker than 1px used decoratively
grep -rnE "border[^:]*:\s*[2-9]px" --include="*.css" src/
# hardcoded colors bypassing tokens (when a tokens file exists)
grep -rnE "#[0-9a-fA-F]{3,8}\b|rgb\(" --include="*.css" src/ | grep -v "tokens\|variables"
```

Also check (manual, not greppable): generic shadows (`box-shadow` with no design intent), default font
stacks where a face was specced, spacing values off the project's scale.

Output format: one line per hit — `file:line — pattern — fix or justification`. Then state: PASS (zero
unjustified hits) or FAIL (list).

Extend this list when a new mid-fi tell gets caught in review — this file is the accumulating ban-list.
