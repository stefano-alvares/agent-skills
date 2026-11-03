---
name: design-ban-audit
description: Use when UI/CSS work is about to be called done, or when auditing an existing frontend for generic-AI aesthetics. Runs mechanical greps for the default design bans plus the project's own docs/crew/bans.md, and returns file:line hits with a PASS/FAIL verdict.
---

# Design Ban Audit

1. Read `docs/crew/bans.md` and `DESIGN.md`. They add to or override the defaults below: permitted tokens,
   ratified exceptions, bans the project already made.
2. Turn each ban in `bans.md` into a grep where it is greppable (a class, property, colour, word, character).
   Run it with the defaults. List the bans you cannot grep as manual checks.
3. Run the defaults. A raw match is a candidate; set it aside only if it is in a comment, a permitted token,
   a functional border, or a ratified exception. Every other hit is a finding: fix it or justify it in one
   line. Zero silent passes.

Whole-repo mode (below) is Atlas's once-per-round audit on the integrated preview. Reviewing a card? Use
Review mode at the end instead.

```bash
# search the source dirs plus root-level source files, or the repo root if none exist (bash and zsh)
DIRS=$(for d in src app components pages styles lib public; do [ -d "$d" ] && echo "$d"; done); ROOTF=$(find . -maxdepth 1 -type f \( -name '*.css' -o -name '*.scss' -o -name '*.html' -o -name '*.astro' -o -name '*.js' -o -name '*.mjs' -o -name '*.tsx' \) | sed 's#^\./##'); SCOPE=$(printf '%s\n%s\n' "$DIRS" "$ROOTF" | grep -v '^$'); SCOPE=${SCOPE:-.}
g() { printf '%s\n' "$SCOPE" | while read -r d; do grep -rnE --exclude-dir=node_modules --exclude-dir=.next --exclude-dir=dist --exclude-dir=build --exclude-dir=out --exclude-dir=coverage --exclude-dir=.vercel --exclude-dir=.turbo --exclude-dir=.crew --exclude-dir=.git "$@" "$d"; done; }

g 'background-clip: ?text|bg-clip-text' --include=\*.{css,scss,astro,tsx,jsx,html}                  # gradient text
g 'backdrop-filter|backdrop-blur' --include=\*.{css,scss,astro,tsx,jsx,html}                         # glassmorphism
g 'transition:.*\b(height|width|top|left|margin|padding)\b' --include=\*.{css,scss}   # layout animation
g 'transition-all|transition: ?all' --include=\*.{css,scss,astro,tsx,jsx,html}                       # animate-everything
g 'border(-(top|right|bottom|left))?(-width)?[[:space:]]*:[[:space:]]*[2-9]px' --include=\*.{css,scss}  # decorative thick borders
g '#[0-9a-fA-F]{3,8}\b|rgba?\(|hsla?\(|oklch\(' --include=\*.{css,scss} | grep -v 'tokens\|variables'  # raw colours
g 'h-screen|100vh' --include=\*.{css,scss,astro,tsx,jsx,html}                                        # use min-h-[100dvh]
g "addEventListener\(['\"]scroll['\"]|onScroll" --include=\*.{js,jsx,ts,tsx,astro}   # scroll listeners
g "$(printf '\342\200\224')" --include=\*.{tsx,jsx,html,md,mdx}   # em dashes (U+2014) in copy
```

Em dashes count only where a visitor can see them: drop hits in comments, docs and tests.

Manual checks (not greppable): generic shadows with no design intent, default font stacks where a face was
specced, spacing off the project's scale.

This audit reads source only. Pair it with a real render check (on Hermes: `node ~/.hermes/tools/shots/shots.cjs`;
in Claude Code: a browser screenshot at desktop and phone width).

Output: one line per hit, `file:line - rule - violation or justification`. Then the verdict: PASS (every hit
fixed or justified) or FAIL (list the violations). Use UNVERIFIED only when the files cannot be read. A
reviewer returns PASS or the single top finding.

When review catches a new mid-fi tell, a reviewer proposes the new ban line in its return (under Later); the
builder or Atlas adds it to the project's `docs/crew/bans.md`, and to this list if it applies to every site.

## Review mode (scoped to a card)

When reviewing a card, a hit counts only on an ADDED line of the card's diff (the core test is
`git diff -U0 <base>...HEAD -- . | grep -E '^\+' | grep -E '<pattern>'`, plus untracked files from
`git ls-files -o --exclude-standard`). Pre-existing hits go under Later with a count (whole-repo hits minus
review-mode hits), never as the gating finding. Run the whole-repo count first, before switching to the
diff-scoped form. Whole-repo mode stays for Atlas's once-per-round audit on the integrated preview.
Read-only: only `git diff` and `git ls-files` run.

Set `BASE` to the card's base ref, run this block (it replaces `g` and adds the file:line), then run the
same `g` rule lines from the whole-repo block. It also counts uncommitted edits to tracked files. Review
mode excludes `md` and `mdx` from the em-dash check: run that line with `--include=\*.{tsx,jsx,html}` only.

```bash
BASE=${BASE:?set BASE to the card base ref}; SKIP='^([^:]*/)?(node_modules|\.next|dist|build|out|coverage|\.vercel|\.turbo|\.crew|\.git)/'
D() { git diff -U0 --no-prefix --no-color "$@"; }
added() { { D "$BASE"...HEAD -- .; D HEAD -- .; git ls-files -o --exclude-standard | grep -vE "$SKIP" | while read -r f; do D --no-index -- /dev/null "$f"; done; } | awk '/^diff /{h=0; next} /^@@/{h=1; split($3,a,","); n=substr(a[1],2)+0; next} !h && /^\+\+\+ /{f=substr($0,5); next} h && /^\+/{print f":"n":"substr($0,2); n++}'; }
g() { local pat=$1 ex= a; shift; for a in "$@"; do case $a in --include=*) ex="$ex|${a##*.}";; esac; done; added | grep -vE "$SKIP" | grep -E "^[^:]*\.(${ex#|}):[0-9]+:.*($pat)"; }
```
