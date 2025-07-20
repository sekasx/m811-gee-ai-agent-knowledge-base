#!/usr/bin/env python
"""
html-href-extraction.py
-----------------------

Extract hrefs that match a CSS selector, optionally prepend a base URL to
relative paths, and write the results to JSON.

Example
-------
python html-href-extraction.py resources/GEE-all-datasets.2025-07-19.html \
    --selector "td.ee-dataset > a" \
    --base-url "https://developers.google.com/" \
    --output resources/datasets.json \
    --unique --pretty
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Iterable, List
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup

DEFAULT_ENCODING = "utf-8"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="html-href-extraction.py",
        description=(
            "Extract href URLs from an HTML file using a CSS selector and "
            "output them as JSON. Optionally prefix a base URL to relative links."
        ),
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("input", help="Path to the HTML file, or '-' for stdin.")
    parser.add_argument(
        "-s",
        "--selector",
        required=True,
        help="CSS selector targeting elements whose hrefs you want.",
    )
    parser.add_argument("-o", "--output", metavar="FILE", help="Destination JSON file.")
    parser.add_argument(
        "-b",
        "--base-url",
        help="If supplied, any href that is not an absolute URL will be joined "
             "to this base (e.g. 'https://developers.google.com/').",
    )
    parser.add_argument(
        "--encoding",
        default=DEFAULT_ENCODING,
        help="Encoding of the HTML file (ignored for stdin).",
    )
    parser.add_argument("-u", "--unique", action="store_true", help="Deduplicate URLs.")
    parser.add_argument("-p", "--pretty", action="store_true", help="Pretty‑print JSON.")
    parser.add_argument("-q", "--quiet", action="store_true", help="Suppress messages.")
    return parser.parse_args(argv)


def read_html(src: str, encoding: str) -> str:
    return sys.stdin.read() if src == "-" else Path(src).read_text(encoding=encoding)


def extract_hrefs(html: str, selector: str) -> List[str]:
    soup = (
        BeautifulSoup(html, "lxml")
        if _lxml_available()
        else BeautifulSoup(html, "html.parser")
    )
    return [el["href"] for el in soup.select(selector) if el.has_attr("href")]


def normalize_hrefs(hrefs: Iterable[str], base_url: str | None) -> List[str]:
    if not base_url:
        return list(hrefs)

    # Make sure base URL ends with '/' so urljoin keeps path segments correct
    if not base_url.endswith("/"):
        base_url += "/"

    parsed_base = urlparse(base_url)
    absolute = []
    for h in hrefs:
        # If already absolute, keep as‑is
        if urlparse(h).scheme:
            absolute.append(h)
        else:
            absolute.append(urljoin(base_url, h.lstrip("/")))
    return absolute


def write_json(urls: Iterable[str], dest: str | None, pretty: bool) -> None:
    data = json.dumps(list(urls), indent=2 if pretty else None)
    if dest:
        Path(dest).write_text(data, encoding="utf-8")
    else:
        print(data)


def _lxml_available() -> bool:
    try:
        import lxml  # noqa: F401
        return True
    except ModuleNotFoundError:
        return False


def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)

    html_text = read_html(args.input, args.encoding)
    hrefs = extract_hrefs(html_text, args.selector)
    hrefs = normalize_hrefs(hrefs, args.base_url)

    if args.unique:
        hrefs = sorted(set(hrefs))

    if not args.quiet:
        sys.stderr.write(f"Extracted {len(hrefs)} URL(s)\n")

    write_json(hrefs, args.output, args.pretty)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:  # pragma: no cover
        sys.stderr.write(f"Error: {exc}\n")
        sys.exit(1)
