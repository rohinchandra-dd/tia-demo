#!/usr/bin/env python3
"""Measure what a CI runner actually costs us, so CI_JOB_OVERHEAD is evidence-backed.

`ddtest plan` decides how many runners to use by scoring each candidate as

    score(n) = wall(n) + n * CI_JOB_OVERHEAD

and taking the minimum. CI_JOB_OVERHEAD is therefore a cost input: it says how
much fixed waste one extra runner buys you. Set it too low and the planner
fans out to machines that spend most of their life on `pip install`.

This script measures that waste from a real run instead of guessing it:

    overhead = (started_at - created_at)      queue / provisioning wait
             + (completed_at - started_at)    job wall clock
             - pytest seconds                 actual testing, from the log

It reports the p50 across the `tia-parallel (node N)` jobs specifically. Those
are the right population: they pay a download-artifact step the `naive` nodes
do not, and they are the jobs the planner is actually sizing.

It then replays the planner's arithmetic at that value, so you can see which
runner count the measurement implies before changing any workflow.

    python3 scripts/measure_job_overhead.py                 # latest PR run
    python3 scripts/measure_job_overhead.py --run 37250040102

Note the planner's `wall(n)` comes from ITS model, not from real durations. On
a demo PR, TIA skipping suppresses the backend duration lookup and ddtest falls
back to one second per test -- so it sizes 17 light suites as 17 x 12s. The
--walls default encodes that; pass measured walls from a plan log to override.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import statistics
import subprocess
import sys
from datetime import datetime

# Planner wall estimates for the TIA-selected set, read off the Candidates
# block of run 37250040102: ceil(17 files / n) x 12s per file.
DEFAULT_WALLS = {1: 204, 2: 108, 3: 72, 4: 60}

PYTEST_LINE = re.compile(r"(\d+) passed(?:, (\d+) skipped)? in ([\d.]+)s")
ANSI = re.compile(r"\x1b\[[0-9;]*m")


def gh(*args: str) -> str:
    result = subprocess.run(["gh", *args], capture_output=True, text=True, errors="replace")
    if result.returncode != 0:
        raise RuntimeError(f"gh {' '.join(args)} failed: {result.stderr.strip()}")
    return result.stdout


def latest_run(repo: str) -> str:
    out = gh(
        "run",
        "list",
        "--repo",
        repo,
        "--workflow",
        "parallel-pr-demo.yml",
        "--event",
        "pull_request",
        "--limit",
        "1",
        "--json",
        "databaseId",
        "--jq",
        ".[0].databaseId",
    ).strip()
    if not out:
        raise RuntimeError("no Parallel PR Demo pull_request runs found")
    return out


def ts(value: str | None) -> datetime | None:
    if not value:
        return None
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def pytest_seconds(repo: str, job_id: int) -> float | None:
    """Total pytest time reported by the job, or None if it ran no tests."""
    try:
        raw = gh(
            "api",
            f"repos/{repo}/actions/jobs/{job_id}/logs",
            "--allow-escape-sequences",
        )
    except RuntimeError:
        return None
    text = ANSI.sub("", raw.replace("\0", ""))
    # Sum every pytest summary line: `ddtest run` can invoke pytest more than
    # once, and taking only the last would understate the testing time and so
    # overstate the overhead.
    totals = [float(m.group(3)) for m in PYTEST_LINE.finditer(text)]
    return sum(totals) if totals else None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--run",
        action="append",
        dest="runs",
        help="run id; repeat to pool several runs (default: latest PR run)",
    )
    parser.add_argument("--repo", default="rohinchandra-dd/tia-demo")
    parser.add_argument(
        "--job-pattern",
        default="tia-parallel (node",
        help="substring identifying the runner jobs to measure",
    )
    parser.add_argument(
        "--billing-run",
        help="which run's real test time to cost out (default: the first --run)",
    )
    parser.add_argument(
        "--walls",
        help="override planner walls, e.g. '1=204,2=108,3=72,4=60'",
    )
    args = parser.parse_args()

    run_ids = args.runs or [latest_run(args.repo)]
    jobs = []
    for run_id in run_ids:
        payload = json.loads(gh("api", f"repos/{args.repo}/actions/runs/{run_id}/jobs"))
        for job in payload.get("jobs", []):
            job["_run"] = run_id
            jobs.append(job)
    if not jobs:
        print(f"runs {', '.join(run_ids)} have no jobs", file=sys.stderr)
        return 1

    print(f"{len(run_ids)} run(s): {', '.join(run_ids)}  ({args.repo})\n")
    rows = []
    for job in sorted(jobs, key=lambda j: (j["_run"], j["name"])):
        if args.job_pattern not in job["name"]:
            continue
        created, started, completed = (
            ts(job.get("created_at")),
            ts(job.get("started_at")),
            ts(job.get("completed_at")),
        )
        if not (created and started and completed):
            continue
        queue = max(0.0, (started - created).total_seconds())
        wall = (completed - started).total_seconds()
        tests = pytest_seconds(args.repo, job["id"])
        if tests is None:
            print(f"  ! {job['name']}: no pytest summary in log, skipping")
            continue
        rows.append((f"{job['_run'][-4:]} {job['name']}", queue, wall, tests, queue + wall - tests))

    if not rows:
        print(f"no jobs matching {args.job_pattern!r}", file=sys.stderr)
        return 1

    print(f"  {'job':<31} {'queue':>7} {'wall':>8} {'pytest':>8} {'overhead':>9}")
    for name, queue, wall, tests, overhead in rows:
        print(f"  {name:<31} {queue:>6.0f}s {wall:>7.0f}s {tests:>7.1f}s {overhead:>8.0f}s")

    overheads = [r[4] for r in rows]
    p50 = statistics.median(overheads)
    print(
        f"\n  p50 overhead {p50:.0f}s   "
        f"(queue p50 {statistics.median(r[1] for r in rows):.0f}s, "
        f"max {max(overheads):.0f}s, n={len(rows)})"
    )

    walls = dict(DEFAULT_WALLS)
    if args.walls:
        walls = {int(k): float(v) for k, v in (pair.split("=") for pair in args.walls.split(","))}

    scores = {n: w + n * p50 for n, w in walls.items()}
    best = min(scores, key=lambda n: (scores[n], n))
    runner_up = min((n for n in scores if n != best), key=lambda n: scores[n])

    print(f"\n  planner arithmetic at CI_JOB_OVERHEAD={p50:.0f}s:")
    for n in sorted(walls):
        mark = "  <- would be chosen" if n == best else ""
        label = "runner " if n == 1 else "runners"
        print(f"    {n} {label}  wall {walls[n]:>5.0f}s  score {scores[n]:>5.0f}s{mark}")
    print(f"\n  => {best} runner(s), by {scores[runner_up] - scores[best]:.0f}s over {runner_up}")

    # ---------------------------------------------------------------- billing
    # The score above optimises WALL CLOCK with a penalty per runner. What you
    # are actually invoiced for is different: GitHub bills each job separately
    # and rounds every one UP to a whole minute. So a runner's true marginal
    # cost is never less than 60s however briefly it runs, and a plan that
    # fans out to short jobs pays that rounding over and over.
    #
    # https://docs.github.com/en/billing/managing-billing-for-github-actions
    # Per-RUN total, never pooled: a preprod push runs the whole 344s suite
    # while a demo PR runs only the TIA-selected set, so summing across runs
    # would invent work that no single run ever does.
    billing_run = args.billing_run or run_ids[0]
    selected = sum(r[3] for r in rows if r[0].startswith(billing_run[-4:]))
    if not selected:
        print(f"\n  (no jobs from run {billing_run}; skipping billing model)")
        return 0
    plan_minutes = 1  # the sequential `ddtest plan` job, ~25s -> 1 billed minute
    print(
        f"\n  billable minutes (GitHub rounds each job up to a whole minute),"
        f"\n  run {billing_run}: {selected:.0f}s of real test time"
        f" + {p50:.0f}s overhead per runner, + 1 min for the plan job:"
    )
    billed = {}
    for n in sorted(walls):
        job = selected / n + p50
        billed[n] = plan_minutes + n * math.ceil(job / 60)
        print(
            f"    {n} {'runner ' if n == 1 else 'runners'}  "
            f"job {job:>5.0f}s  ->  {billed[n]:>2d} billed min"
        )
    cheapest = min(billed, key=lambda n: (billed[n], n))
    print(f"\n  cheapest: {cheapest} runner(s) at {billed[cheapest]} billed minutes")

    # Overhead that would make the planner agree with the billing optimum.
    aligned = None
    for candidate in range(0, 181, 1):
        sc = {n: w + n * candidate for n, w in walls.items()}
        if min(sc, key=lambda n: (sc[n], n)) == cheapest:
            aligned = candidate
            break
    print(
        f"\n  measured overhead {p50:.0f}s  -> planner picks {best}"
        f"\n  60s (one billed minute, the true marginal cost of a runner)"
        f" -> planner picks "
        f"{min({n: w + n * 60 for n, w in walls.items()}, key=lambda n: (walls[n] + n * 60, n))}"
    )
    if aligned is not None:
        print(f"  smallest overhead that reaches the billing optimum: {aligned}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
