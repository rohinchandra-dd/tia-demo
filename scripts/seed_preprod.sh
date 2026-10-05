#!/usr/bin/env bash
#
# Seed Datadog with fresh demo data by landing full test runs on `preprod`.
#
# Both demos read data that Datadog can only learn by WATCHING the suite run:
#
#   demo-tia            per-test coverage, so Test Impact Analysis knows which
#                       tests a given source file actually exercises
#   demo-parallel-smart p50 suite durations, so `ddtest plan` can split the
#                       selected set evenly instead of guessing from file size
#
# `preprod` is a TIA-excluded branch, so a push there runs all 965 tests and
# refreshes both. An empty commit is enough -- the push triggers of
# tia-pr-demo.yml and parallel-pr-demo.yml deliberately carry no `paths` filter
# precisely so that works.
#
# Run this after ANY change to scripts/domain_spec.json. Regenerating test files
# invalidates their coverage and timings, and until it is re-seeded TIA will
# refuse to skip the churned suites -- which silently flattens the demo rather
# than failing it. Measured once: billing and compliance both ran in full on a
# PR that touched neither, and the TIA bar came out level with the naive bar.
#
#   scripts/seed_preprod.sh [rounds]     # default 3
#   scripts/seed_preprod.sh 2 --yes      # skip the confirmation prompt
#
# Rounds are serialised on purpose: Datadog derives a p50, so a handful of
# samples spread over separate runs beats one run repeated concurrently.
#
set -euo pipefail

BRANCH="preprod"
REMOTE="origin"
WORKFLOWS=("tia-pr-demo.yml" "parallel-pr-demo.yml")

rounds=3
assume_yes=0
for arg in "$@"; do
  case "$arg" in
    -y | --yes) assume_yes=1 ;;
    '' | *[!0-9]*) echo "usage: $0 [rounds] [--yes]" >&2; exit 2 ;;
    *) rounds="$arg" ;;
  esac
done

for cmd in git gh jq; do
  command -v "$cmd" >/dev/null || { echo "error: $cmd is required" >&2; exit 1; }
done

git fetch --quiet "$REMOTE" "$BRANCH"
base="$(git rev-parse "$REMOTE/$BRANCH")"

echo "Seeding $REMOTE/$BRANCH (currently ${base:0:7}) with $rounds empty commit(s)."
echo "Each round runs the full 965-test suite across both demo workflows."
if [ "$assume_yes" -ne 1 ]; then
  read -r -p "Continue? [y/N] " reply
  [[ "$reply" =~ ^[Yy]$ ]] || { echo "aborted"; exit 1; }
fi

# Wait for the run of $1 whose head is $2, then block until it finishes.
wait_for_run() {
  local workflow="$1" sha="$2" id="" waited=0
  while [ -z "$id" ]; do
    id="$(gh run list --workflow "$workflow" --branch "$BRANCH" --event push \
      --limit 20 --json databaseId,headSha \
      --jq "[.[] | select(.headSha == \"$sha\")] | .[0].databaseId // empty")"
    [ -n "$id" ] && break
    if [ "$waited" -ge 180 ]; then
      echo "  ! $workflow never appeared for ${sha:0:7}; check GitHub Actions" >&2
      return 1
    fi
    sleep 10
    waited=$((waited + 10))
  done
  echo "  - $workflow -> run $id"
  # The seeding run's job results do not matter, only that it finished and
  # shipped its traces, so a non-zero exit here is not fatal.
  gh run watch "$id" --exit-status >/dev/null 2>&1 || true
  echo "  - $workflow run $id finished"
}

for i in $(seq 1 "$rounds"); do
  echo
  echo "=== round $i/$rounds ==="
  git fetch --quiet "$REMOTE" "$BRANCH"
  parent="$(git rev-parse "$REMOTE/$BRANCH")"
  # Build the commit with plumbing so the working tree and current branch are
  # never touched -- this is safe to run mid-task from any branch.
  sha="$(git commit-tree -p "$parent" \
    -m "chore: seed TIA coverage and ddtest timings ($i/$rounds)" \
    "$(git rev-parse "$parent^{tree}")")"
  git push --quiet "$REMOTE" "$sha:refs/heads/$BRANCH"
  echo "pushed ${sha:0:7} to $REMOTE/$BRANCH"
  for wf in "${WORKFLOWS[@]}"; do
    wait_for_run "$wf" "$sha" || true
  done
done

echo
echo "Done. Verify with the 'Demo Preflight' workflow:"
echo "  gh workflow run demo-preflight.yml --ref $BRANCH && sleep 20 && gh run watch"
