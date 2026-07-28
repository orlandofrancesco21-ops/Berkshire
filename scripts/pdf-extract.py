#!/usr/bin/env python3
"""Extract a PDF's text to the vault's canonical page-addressed form, using PyMuPDF.

Why this exists (learned in the sibling RevOps vault, 2026-07-28, the hard way):
`pdftotext -layout` SILENTLY UNDER-EXTRACTS some PDFs. On an 18-page research
report it returned 281 characters; PyMuPDF returned 12,446 from the same file,
including every benchmark table. The near-empty extraction read as "this report
is infographic-only, the numbers aren't retrievable" when the whole text layer
was there — and an entry was nearly written at teaser depth on that false premise.
That is the failure class this vault's grounding rules exist to prevent, one layer
down: not distilled-from-vibes, but distilled-from-a-broken-extractor. The
grounding gate cannot see it, because a file genuinely exists on disk.

Investor letters and annual reports are exactly the shape that trips this
(multi-column layouts, tables, charts with embedded text).

So: PyMuPDF is the primary extractor, and the yield check below is mandatory.
A suspiciously low chars-per-page ratio means TRY ANOTHER TOOL or render the
pages as images for visual reading — it does NOT mean the content is absent.

Output convention (matches the rest of library/sources/): pages separated by
form feeds, so printed page N == the Nth form-feed segment, which is what
`scripts/source-pages.py` and every entry locator address into.

Usage:
    python scripts/pdf-extract.py <in.pdf> <out.txt> [--append-file FILE --append-label LABEL]

Never re-extract over an existing archived .txt that an entry already cites —
a different tool or version shifts page boundaries and silently breaks every
locator (canonical rule: docs/build-plan.md "Source archive & deep retrieval").

Any library entry claiming content "was not retrievable" MUST name which
extractors were actually tried. A low yield licenses trying another tool; it
never licenses claiming the content is absent.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Below this, assume the extractor failed rather than the PDF being empty.
MIN_CHARS_PER_PAGE = 200


def main() -> int:
    ap = argparse.ArgumentParser(description="Extract PDF text, page-addressed, via PyMuPDF.")
    ap.add_argument("pdf")
    ap.add_argument("out")
    ap.add_argument("--append-file", help="extra text file to append as a labeled trailing section")
    ap.add_argument("--append-label", default="APPENDIX", help="label for the appended section")
    args = ap.parse_args()

    try:
        import fitz  # PyMuPDF
    except ImportError:
        print("PyMuPDF missing: python -m pip install pymupdf", file=sys.stderr)
        return 2

    doc = fitz.open(args.pdf)
    pages = [page.get_text() for page in doc]
    text = "\f".join(pages)

    total = len(text)
    per_page = total / max(len(pages), 1)
    print(f"{args.pdf}: {len(pages)} pages, {total} chars ({per_page:.0f}/page)")

    if per_page < MIN_CHARS_PER_PAGE:
        print(
            f"WARNING: only {per_page:.0f} chars/page — assume the EXTRACTOR failed, not that the\n"
            f"         content is absent. Render pages as images and read them visually before\n"
            f"         writing any entry that claims content was unavailable.",
            file=sys.stderr,
        )

    if args.append_file:
        extra = Path(args.append_file).read_text(encoding="utf-8", errors="replace")
        text += f"\f===== {args.append_label} =====\n\n{extra}"
        print(f"appended {len(extra)} chars as '{args.append_label}'")

    Path(args.out).write_text(text, encoding="utf-8", newline="\n")
    print(f"wrote {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
