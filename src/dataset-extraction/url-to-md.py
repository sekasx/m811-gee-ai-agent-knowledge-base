#!/usr/bin/env python
"""
url-to-md.py
============

Read a JSON list of URLs, call Gendox's /web-scrape in *scrape* mode for each
one, and save the returned Markdown into <slug>.md files in the given folder.

Usage
-----
python url-to-md.py urls.json output_dir [options]

Typical:
python url-to-md.py resources/datasets.json resources/markdown \
    --gendox-url http://localhost:8000 \
    --elements main
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path
from typing import List
from urllib.parse import urljoin, urlparse

import requests


# --------------------------------------------------------------------------- #
# CLI parsing
# --------------------------------------------------------------------------- #


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Convert each URL in a JSON list to Markdown via Gendox "
                    "/web-scrape (mode=scrape).",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    p.add_argument("urls_file", help="JSON file containing a list of URLs.")
    p.add_argument("output_dir", help="Directory to write <slug>.md files into.")
    p.add_argument(
        "--gendox-url",
        default="http://localhost:8000",
        help="Base URL where the Gendox service is running.",
    )
    p.add_argument(
        "--depth",
        type=int,
        default=0,
        help="Depth parameter for the web‑scrape call.",
    )
    p.add_argument(
        "--elements",
        nargs="*",
        metavar="TAG",
        default=["main"],
        help="HTML elements to extract (passed as JSON list).",
    )
    p.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite .md files that already exist.",
    )
    p.add_argument(
        "--delay",
        type=float,
        default=0.0,
        help="Seconds to sleep between requests (politeness).",
    )
    return p.parse_args()


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #


def slug_from_url(url: str) -> str:
    """Use final path segment as filename‑safe slug."""
    path = urlparse(url).path.rstrip("/")
    return (path.split("/")[-1] or "index").replace(":", "_")



def request_markdown(
        url: str,
        session: requests.Session,
        gendox_base: str,
        depth: int,
        elements: List[str],
) -> str:
    """
    Call /web-scrape (mode=scrape) and return Markdown text.

    Handles three server reply shapes:

    1) {"markdown_text": "..."}                               – single string
    2) {"results": ["...markdown...", "...markdown..."]}      – list of strings
    3) {"results": [{"url": "...", "text": "markdown"}, ...]} – list of dicts
    """
    endpoint = urljoin(gendox_base.rstrip("/") + "/", "gendox/api/v1/web-scrape")
    params = {
        "domain": url,
        "mode": "scrape",
        "depth": depth,
        "allow_external": "false",
        "parser": "html5lib",
        "encoding": "utf-8",
        "unparsable_urls": "false",
        "elements_to_extract": json.dumps([{"tag": tag} for tag in elements]),
    }

    resp = session.get(endpoint, params=params, timeout=120)
    resp.raise_for_status()
    data = resp.json()

    # 1) single‑string payload
    if isinstance(data, dict) and "markdown_text" in data:
        return data["markdown_text"]

    # 2) list of strings  OR  3) list of {"text": "..."}
    if isinstance(data, dict) and "results" in data:
        parts = []
        for item in data["results"]:
            if isinstance(item, str):
                parts.append(item)
            elif isinstance(item, dict) and "text" in item:
                parts.append(item["text"])
        if parts:
            return "\n\n".join(parts)

    # If nothing matched, raise an informative error
    raise ValueError(f"Unexpected Gendox reply for {url!s}: {data!r}")



# --------------------------------------------------------------------------- #
# Main driver
# --------------------------------------------------------------------------- #


def main() -> None:
    args = parse_args()

    urls: List[str] = json.loads(Path(args.urls_file).read_text())
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    session = requests.Session()
    ok, fail = 0, 0

    for url in urls:
        slug = slug_from_url(url)
        md_path = out_dir / f"{slug}.md"

        if md_path.exists() and not args.overwrite:
            print(f"[skip] {md_path} exists")
            ok += 1
            continue

        try:
            md_text = request_markdown(
                url,
                session,
                args.gendox_url,
                depth=args.depth,
                elements=args.elements,
            )
            md_path.write_text(md_text, encoding="utf-8")
            try:
                rel = md_path.relative_to(Path.cwd())
            except ValueError:
                rel = md_path.resolve()

            print(f"[ ok ] {url} → {rel}")
            ok += 1
        except Exception as exc:
            print(f"[FAIL] {url}: {exc}", file=sys.stderr)
            fail += 1
        finally:
            if args.delay:
                time.sleep(args.delay)

    print(f"\nCompleted: {ok} succeeded, {fail} failed.")
    if fail:
        sys.exit(1)


if __name__ == "__main__":
    main()




