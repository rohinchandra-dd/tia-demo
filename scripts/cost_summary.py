#!/usr/bin/env python3
"""Render the naive vs tia-parallel cost comparison as a GitHub step summary.

The speed story is already visible in the Actions UI; the cost story is not,
because GitHub never shows you per-leg totals. This reads a run's own job
records and prints the markdown table.

Billed minutes, not raw seconds, is the honest number: GitHub bills each job
separately and rounds every one UP to a whole minute. That rounding is why
fanning out to many short jobs can cost as much as a slow serial run --
measured on run 37250040102, where `tia-parallel` on 4 runners billed the same
9 minutes as `naive` while running a fifth of the tests.

    gh api "repos/$SLUG/actions/runs/$ID/jobs" --paginate \
      --jq '.jobs[] | {name, started_at, completed_at}' \
      | python3 scripts/cost_summary.py >> "$GITHUB_STEP_SUMMARY"

Input is one JSON object per line (jq's default output), not a JSON array.
"""

from __future__ import annotations

import json
import math
import sys
from datetime import datetime

LEGS = ("naive", "tia-parallel")


def ts(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def main() -> int:
    legs: dict[str, list[tuple[str, datetime, datetime]]] = {leg: [] for leg in LEGS}
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        job = json.loads(line)
        if not (job.get("started_at") and job.get("completed_at")):
            continue
        for leg in LEGS:
            if job["name"].startswith(leg):
                legs[leg].append((job["name"], ts(job["started_at"]), ts(job["completed_at"])))

    rows = []
    for leg, jobs in legs.items():
        if not jobs:
            continue
        # Runners = jobs that actually ran tests. The sequential `plan` job is
        # counted in both cost and wall clock, but it is not a parallel runner
        # and inflating the count with it would flatter the wrong leg.
        runners = sum(1 for name, _, _ in jobs if "(node" in name)
        wall = (max(c for _, _, c in jobs) - min(s for _, s, _ in jobs)).total_seconds()
        seconds = sum((c - s).total_seconds() for _, s, c in jobs)
        billed = sum(math.ceil((c - s).total_seconds() / 60) for _, s, c in jobs)
        rows.append((leg, runners, wall, seconds, billed))

    if not rows:
        print("_No completed leg jobs found for this run._")
        return 0

    print("## Cost comparison\n")
    print("| leg | runners | wall clock | runner-seconds | billed minutes |")
    print("|---|---|---|---|---|")
    for leg, runners, wall, seconds, billed in rows:
        print(f"| `{leg}` | {runners} | {wall:.0f}s | {seconds:.0f}s | **{billed}** |")
    print()

    by_leg = {r[0]: r for r in rows}
    if "naive" in by_leg and "tia-parallel" in by_leg:
        base, smart = by_leg["naive"], by_leg["tia-parallel"]
        print(
            f"`tia-parallel` used **{smart[1]} runner(s)** against {base[1]}, "
            f"finished in **{smart[2]:.0f}s** against {base[2]:.0f}s, "
            f"and billed **{smart[4]} minute(s)** against {base[4]}.\n"
        )
        print(
            "> Billed minutes round each job up to a whole minute, so they are "
            "what you are actually invoiced. The sequential `plan` job is "
            "counted against `tia-parallel`, not hidden."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
