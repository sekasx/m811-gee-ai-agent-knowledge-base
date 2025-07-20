#!/usr/bin/env python
"""
md-token-stats.py
-----------------

Scan a directory of Markdown files, compute OpenAI‑token statistics using tiktoken,
and print:

  • Overall total, average, median, std‑dev, min and max
  • The same stats for the bottom 90%, 99% and 99.9% of files (i.e. with top outliers removed)

Optional: export the per‑file counts to CSV.

Example
-------
python md-token-stats.py resources/markdown --model gpt-4o-mini --csv stats.csv
"""

from __future__ import annotations

import argparse
import csv
import math
import statistics as stats
import sys
from pathlib import Path
from typing import Dict, List, Tuple

import tiktoken


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Compute token statistics for Markdown files using tiktoken.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    p.add_argument("directory", help="Folder containing *.md files.")
    p.add_argument(
        "--model",
        default="gpt-4o-mini",
        help="OpenAI model encoding to use (passed to tiktoken).",
    )
    p.add_argument(
        "--csv",
        metavar="FILE",
        help="Optional path to write per‑file token counts as CSV.",
    )
    return p.parse_args()


def count_tokens(path: Path, encoding) -> int:
    text = path.read_text(encoding="utf-8", errors="ignore")
    return len(encoding.encode(text))


def gather_counts(folder: Path, encoding) -> Dict[str, int]:
    counts: Dict[str, int] = {}
    for md_file in folder.rglob("*.md"):
        try:
            counts[str(md_file)] = count_tokens(md_file, encoding)
        except Exception as exc:
            print(f"[WARN] Could not process {md_file}: {exc}", file=sys.stderr)
    return counts


def summarise(counts: Dict[str, int]) -> Tuple[str, str, int, int, float, float, float]:
    if not counts:
        raise ValueError("No Markdown files found or processed.")

    total = sum(counts.values())
    n = len(counts)
    avg = total / n
    median = stats.median(counts.values())
    stddev = stats.pstdev(counts.values()) if n > 1 else 0.0
    max_file = max(counts, key=counts.get)
    min_file = min(counts, key=counts.get)

    return max_file, min_file, total, n, avg, median, stddev


def write_csv(counts: Dict[str, int], csv_path: Path) -> None:
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["filename", "tokens"])
        for fname, tok in sorted(counts.items()):
            writer.writerow([fname, tok])


def percentile_subset_stats(
        counts_sorted: List[int], keep_fraction: float
) -> Tuple[int, int, int, float, float, float]:
    """
    Return (n_files, total, avg, median, stddev, max, min)
    for the bottom keep_fraction of files (counts_sorted is ascending).
    """
    if not counts_sorted:
        return (0, 0, 0.0, 0.0, 0.0, 0, 0)
    n = len(counts_sorted)
    # how many to keep
    k = max(1, math.ceil(keep_fraction * n))
    subset = counts_sorted[:k]
    total = sum(subset)
    avg = total / k
    median = stats.median(subset)
    stddev = stats.pstdev(subset) if k > 1 else 0.0
    return (k, total, avg, median, stddev, subset[-1], subset[0])


def main() -> None:
    args = parse_args()

    try:
        enc = tiktoken.encoding_for_model(args.model)
    except Exception as e:
        sys.exit(f"Error: could not load encoding for model '{args.model}': {e}")

    folder = Path(args.directory).expanduser()
    if not folder.is_dir():
        sys.exit(f"Error: {folder} is not a directory.")

    counts = gather_counts(folder, enc)
    max_file, min_file, total, n_files, avg, median, stddev = summarise(counts)

    print(f"Scanned {n_files} Markdown file(s) in {folder}")
    print(f"  Total tokens : {total:,}")
    print(f"  Average      : {avg:,.2f}")
    print(f"  Median       : {median:,.2f}")
    print(f"  Std dev      : {stddev:,.2f}")
    print(f"  Max file     : {max_file}  ({counts[max_file]:,} tokens)")
    print(f"  Min file     : {min_file}  ({counts[min_file]:,} tokens)")

    # Prepare sorted list of counts
    counts_sorted = sorted(counts.values())

    for pct in (0.999, 0.99, 0.95, 0.90):
        keep_pct = int(pct * 100)
        k, sub_total, sub_avg, sub_median, sub_std, sub_max, sub_min = percentile_subset_stats(
            counts_sorted, pct
        )
        print(f"\nStats for bottom {keep_pct}% of files ({k} files):")
        print(f"  Total tokens : {sub_total:,}")
        print(f"  Average      : {sub_avg:,.2f}")
        print(f"  Median       : {sub_median:,.2f}")
        print(f"  Std dev      : {sub_std:,.2f}")
        print(f"  Max tokens   : {sub_max:,}")
        print(f"  Min tokens   : {sub_min:,}")

    if args.csv:
        write_csv(counts, Path(args.csv))
        print(f"\nPer‑file breakdown written to {args.csv}")


if __name__ == "__main__":
    main()
