#!/usr/bin/env bash
# Feature Loop mechanical commit gate.
# Installed as the target repo's .git/hooks/pre-commit at wave start.
# Git refuses the commit if the active ticket's proof is undeclared or fails.
# This is the mechanical backstop under the coordinator's procedural evidence gate:
# a coordinator that forgets to run the proof cannot commit anyway.
#
# Protocol (coordinator, per the skill's Evidence gate section):
#   wave start        : install this file as .git/hooks/pre-commit (chmod +x),
#                       write .git/feature-loop-active (marker, any content)
#   before each commit: write the ticket's proof command to .git/feature-loop-proof
#   wave end          : rm .git/feature-loop-active
#
# Files live under .git/ — never tracked, never committed, invisible to `git status`.
# When the marker is absent the hook is inert, so normal commits in the same repo
# are unaffected. When the marker is present the gate is fail-closed: no declared
# proof means no commit.

set -euo pipefail

git_dir="$(git rev-parse --git-dir)"
marker="$git_dir/feature-loop-active"
proof_file="$git_dir/feature-loop-proof"

# Inert unless a wave is active.
[ -f "$marker" ] || exit 0

if [ ! -s "$proof_file" ]; then
  echo "feature-loop: commit blocked — no proof declared for this ticket." >&2
  echo "  Write the ticket's proof command to $proof_file before committing," >&2
  echo "  or remove $marker to end the wave." >&2
  exit 1
fi

proof_cmd="$(cat "$proof_file")"
echo "feature-loop: running ticket proof before commit: $proof_cmd" >&2
if ! bash -c "$proof_cmd"; then
  echo "feature-loop: commit blocked — proof failed (nonzero exit)." >&2
  exit 1
fi

# Force per-commit re-declaration: a stale green proof cannot ride a later commit.
rm -f "$proof_file"
echo "feature-loop: proof passed — commit allowed." >&2
exit 0
