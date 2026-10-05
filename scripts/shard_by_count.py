#!/usr/bin/env python3
"""Print the test files belonging to one shard of a naive, count-based split.

This is deliberately the dumb sharding most teams hand-roll: sort the test
files, chop them into N contiguous chunks of equal FILE COUNT, and hope each
chunk costs about the same. It does not, and that is the point — both demos
use this as the "before" picture:

    shard 0: 10 files, 204s    <- analytics x4 (30s), auth x4, billing 2x40s
    shard 1: 10 files, 124s    <- compliance x4 (30s), catalog x4, billing 2x0s
    shard 2: 10 files,   8s
    shard 3: 11 files,   8s

Used by tia-pr-demo.yml (both legs) and parallel-pr-demo.yml (the naive leg),
so all three produce the identical partition and their node times are directly
comparable across the two demos.

    python scripts/shard_by_count.py --shard 0 --nodes 4
"""

from __future__ import annotations

import argparse
import pathlib
import sys

# tests/flaky is excluded everywhere: test_intermittent.py fails by design and
# test_retry_recoverable.py cannot pass without Auto Test Retries, so including
# it would fail these jobs for reasons unrelated to what they demonstrate.
EXCLUDED_DIRS = ("flaky",)


def discover(root: pathlib.Path) -> list[str]:
    files = [
        p for p in root.rglob("test_*.py") if not any(part in EXCLUDED_DIRS for part in p.parts)
    ]
    return sorted(str(p) for p in files)


def shard(files: list[str], index: int, nodes: int) -> list[str]:
    total = len(files)
    start = index * total // nodes
    end = (index + 1) * total // nodes
    return files[start:end]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--shard", type=int, required=True, help="zero-indexed")
    parser.add_argument("--nodes", type=int, required=True)
    parser.add_argument("--tests-dir", default="tests")
    args = parser.parse_args()

    if args.nodes < 1:
        parser.error("--nodes must be >= 1")
    if not 0 <= args.shard < args.nodes:
        parser.error(f"--shard must be in [0, {args.nodes - 1}]")

    files = discover(pathlib.Path(args.tests_dir))
    if not files:
        print(f"no test files found under {args.tests_dir}/", file=sys.stderr)
        return 1

    for path in shard(files, args.shard, args.nodes):
        print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
