#!/usr/bin/env python3
"""Address the local source archive by page — the deep-retrieval rung.

`library/sources/<slug>.txt` is the CANONICAL, immutable extracted text of a
source (produced once, at absorb time, by `scripts/pdf-extract.py` — PyMuPDF,
page breaks = form feeds; NOT pdftotext, which silently under-extracts some PDFs).
Printed page N == the Nth form-feed-delimited segment, 1-based (a trailing empty
segment from the final form feed is ignored). Library entries cite pages against
THIS text, so the same page numbers address it here.

Never re-extract over an existing .txt: locators point into it, and a different
tool/version can shift page boundaries silently. If a .txt is lost but the PDF
survives, re-extract and re-verify the entry's cited figures against it before
trusting the locators again (docs/build-plan.md).

RETRIEVAL, NOT EVIDENCE. A hit or a page dump here is a POINTER, never a citable
fact. Nothing from a source .txt may enter a principle, a thesis, a flag, or a
decision directly — it goes through `absorb` first, which is what applies the
verification chain (canonical rule "Source archive & deep retrieval" in
docs/build-plan.md).

Usage:
  source-pages.py <slug> <page>            print one page
  source-pages.py <slug> <start-end>       print a page range (inclusive)
  source-pages.py --grep "<regex>" [slug]  page-addressed search; all sources if
                                           no slug given. Reports `slug  p.N: line`
                                           so hits line up with entry locators.

Options:
  -i   case-insensitive grep (default: case-sensitive)
  -C   context: also print the whole page, not just the matching line
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

SOURCES_DIR = Path(__file__).resolve().parent.parent / "library" / "sources"


def load_pages(slug: str) -> list[str]:
    """Return the source's pages, 1-based via list index+1. Trailing empty
    segment (from the final form feed) is dropped so len() == real page count."""
    path = SOURCES_DIR / f"{slug}.txt"
    if not path.exists():
        sys.exit(f"no extracted text at {path} (is the slug right? is it archived?)")
    pages = path.read_text(encoding="utf-8").split("\f")
    if pages and pages[-1].strip() == "":
        pages.pop()
    return pages


def known_slugs() -> list[str]:
    if not SOURCES_DIR.is_dir():
        return []
    return sorted(p.stem for p in SOURCES_DIR.glob("*.txt"))


def cmd_print(slug: str, page_spec: str) -> int:
    pages = load_pages(slug)
    n = len(pages)
    m = re.fullmatch(r"(\d+)(?:\s*-\s*(\d+))?", page_spec.strip())
    if not m:
        sys.exit(f"page spec '{page_spec}' not a page or range (e.g. 34 or 34-36)")
    start = int(m.group(1))
    end = int(m.group(2)) if m.group(2) else start
    if start < 1 or end > n or end < start:
        sys.exit(f"pages {start}-{end} out of range for {slug} (1-{n})")
    for p in range(start, end + 1):
        print(f"===== {slug}  p.{p}/{n} =====")
        print(pages[p - 1].rstrip("\n"))
        print()
    return 0


def cmd_grep(pattern: str, slugs: list[str], ignore_case: bool, full_page: bool) -> int:
    flags = re.IGNORECASE if ignore_case else 0
    try:
        rx = re.compile(pattern, flags)
    except re.error as e:
        sys.exit(f"bad regex: {e}")
    targets = slugs or known_slugs()
    if not targets:
        sys.exit(f"no sources in {SOURCES_DIR}")
    hits = 0
    for slug in targets:
        pages = load_pages(slug)
        for i, page in enumerate(pages, 1):
            if not rx.search(page):
                continue
            hits += 1
            if full_page:
                print(f"===== {slug}  p.{i} =====")
                print(page.rstrip("\n"))
                print()
            else:
                line = next((ln.strip() for ln in page.splitlines() if rx.search(ln)), "")
                print(f"{slug}  p.{i}: {line[:160]}")
    if not hits:
        print(f"no match for /{pattern}/ in {len(targets)} source(s)")
        return 1
    return 0


def main() -> int:
    # The extracted text carries Unicode (>=, x, curly quotes); the Windows console
    # defaults to cp1252 and would crash on a page dump. Force UTF-8 out.
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass
    ap = argparse.ArgumentParser(add_help=True, description="Page-address the local source archive.")
    ap.add_argument("--grep", metavar="REGEX", help="page-addressed search")
    ap.add_argument("-i", action="store_true", help="case-insensitive grep")
    ap.add_argument("-C", "--context", action="store_true", help="print whole matching page")
    ap.add_argument("args", nargs="*", help="<slug> <page|start-end>  OR  [slug ...] with --grep")
    ns = ap.parse_args()

    if ns.grep is not None:
        return cmd_grep(ns.grep, ns.args, ns.i, ns.context)
    if len(ns.args) == 2:
        return cmd_print(ns.args[0], ns.args[1])
    ap.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
