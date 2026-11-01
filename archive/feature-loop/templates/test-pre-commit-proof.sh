#!/usr/bin/env bash
# One runnable check for the pre-commit proof gate's three states:
# inert (no marker), blocked (marker, no proof / failing proof), allowed (passing proof).
set -euo pipefail

hook="$(cd "$(dirname "$0")" && pwd)/pre-commit-proof.sh"
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT

cd "$tmp"
git init -q
git config user.email t@t; git config user.name t
git_dir="$tmp/.git"

run_hook() { ( cd "$tmp" && bash "$hook" ); }

# 1. Inert: no marker -> exit 0.
run_hook && echo "PASS inert" || { echo "FAIL inert"; exit 1; }

# 2. Blocked: marker present, no proof declared -> nonzero.
touch "$git_dir/feature-loop-active"
if run_hook 2>/dev/null; then echo "FAIL block-no-proof"; exit 1; else echo "PASS block-no-proof"; fi

# 3. Blocked: failing proof -> nonzero, proof file kept.
echo 'exit 7' > "$git_dir/feature-loop-proof"
if run_hook 2>/dev/null; then echo "FAIL block-bad-proof"; exit 1; else echo "PASS block-bad-proof"; fi
[ -s "$git_dir/feature-loop-proof" ] || { echo "FAIL proof-cleared-on-failure"; exit 1; }

# 4. Allowed: passing proof -> exit 0, proof file cleared.
echo 'true' > "$git_dir/feature-loop-proof"
run_hook 2>/dev/null && echo "PASS allow-good-proof" || { echo "FAIL allow-good-proof"; exit 1; }
[ ! -f "$git_dir/feature-loop-proof" ] || { echo "FAIL proof-not-cleared-on-pass"; exit 1; }

echo "ALL PASS"
