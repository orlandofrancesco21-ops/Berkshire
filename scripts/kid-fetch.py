#!/usr/bin/env python3
"""Retrieve and parse a fund's PRIIPs KID cost block, by ISIN.

WHY THIS EXISTS. Costing a portfolio is the one fund question that is nearly
certain rather than forecast, and it was the slowest thing this vault did: on a
30-fund portfolio it took roughly forty manual web lookups, and the owner ended
up downloading ten KID PDFs by hand and pasting them in. That is intake friction
on the one input that is always available and never estimated.

WHAT IT RETURNS, per ISIN, from the KID itself where one can be reached:
    management + other ongoing   transaction costs   = ongoing total
    entry charge (maximum)       exit charge         performance fee
Every figure carries the rung it came from, so a primary reading is never
confused with a scraped one.

THE RETRIEVAL LADDER, ordered by provenance and measured on 2026-08-26 against
nine real funds whose official KIDs the owner had downloaded by hand:

  1. issuer KID by ISIN     Fineco AM: finecoassetmanagement.com/documents/
                            KIIDs/EN/{ISIN}.pdf. PRIMARY. Verified on 4 of 4 FAM
                            funds, EXACT to 0.00pp against the owner's own IT
                            KIDs. 404s cleanly for non-FAM funds, so it is safe
                            to try first and cheap when it misses.
  2. local KID PDF          --kid-dir scans a folder of already-downloaded KIDs
                            and matches on the ISIN inside the text. PRIMARY.
  3. fondsweb               fondsweb.com/de/{ISIN}. SECONDARY, but verified on
                            3 of 3 funds it covered, EXACT to 0.00pp. Its
                            "laufende Kosten" IS the PRIIPs ongoing total
                            (management+other plus transaction). COVERAGE is the
                            catch: it held only 3 of the 9, missing every
                            Italian- and Irish-distributed fund. Needs a browser
                            User-Agent; it 403s otherwise.
  4. unresolved             Reported as unresolved. NEVER guessed, never filled
                            from a sibling share class - see the class spread
                            below.

Rungs deliberately NOT automated, because measurement said they cannot be:
  - fundsquare KID download works but needs a per-provider `cdClient` key that
    is not derivable from the ISIN. Fine as a manual step, useless in a loop.
  - investing.com carries the Italian-distributed funds fondsweb misses, but
    403s every scripted request. It is reachable by an agent's own fetch tool,
    so the skill routes there by hand rather than pretending the script can.

WHY THE SHARE CLASS IS NOT NEGOTIABLE. Ongoing costs vary more BETWEEN classes
of one fund than between funds. Measured, same portfolio, same day:
    Invesco Sustainable Allocation   A 1.30%  C 0.90%  Z 0.80%  S 0.71%
    Allianz Global FRN Plus          AT 0.61% IT 0.32% P2 0.28% WT 0.24%
So an ISIN is the input. A fund NAME is not an input, and a figure taken from a
sibling class is a wrong number wearing a right one's clothes.

TWO PARSING TRAPS, both hit for real on 2026-08-26 and both regression-tested:
  - DECIMAL SEPARATOR. Italian KIDs write 1,69%; the Wellington KID in the same
    folder wrote 1.69%. A comma-only parser silently returned "no figure" and
    the fund would have been reported as unpriced.
  - PERFORMANCE FEES. "Per questo prodotto non si applicano le commissioni di
    performance" and "Puo essere addebitata una commissione ... fino il 15% dei
    rendimenti" both contain the words `commissioni di performance`. A parser
    that only looks for a number found none in the FIRST and reported 0% for the
    SECOND, hiding a 15% performance fee on a real holding.

AND THE RULE INHERITED FROM pdf-extract.py: a thin extraction means the
EXTRACTOR failed, not that the costs are absent. This script says so explicitly
rather than reporting a fund as having no cost block.

Usage:
    python scripts/kid-fetch.py IE00BFXY5S68 LU0575777387
    python scripts/kid-fetch.py --isin-file holdings.tsv --kid-dir ~/Downloads
    python scripts/kid-fetch.py IE00BFXY5S68 --json costs.json
    python scripts/kid-fetch.py --self-test
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/122.0 Safari/537.36")
ISIN_RE = re.compile(r"\b[A-Z]{2}[0-9A-Z]{9}[0-9]\b")

# Accept BOTH separators. See "TWO PARSING TRAPS" above - this single character
# class is the whole fix for a fund silently reporting as unpriced.
NUM = r"([0-9]+(?:[.,][0-9]+)?)"

# Label sets by language. The KID is a regulated document, so these strings are
# stable in a way scraped page furniture is not.
LABELS = {
    "it": {
        "mgmt": "Commissioni di gestione e",
        "txn": "Costi di transazione",
        "entry": "Costi di ingresso",
        "exit": "Costi di uscita",
        "perf": "Commissioni di performance",
        # Every way an Italian KID says "there isn't one". Missing a phrasing does
        # not fail loudly - it emits a performance-fee WARNING on a fund that has
        # none, which trains the reader to ignore the warning that matters.
        "none": (r"[Nn]on (?:addebitiamo|applichiamo|si applicano|sono previst"
                 r"|ha alcuna|e previst|è previst|vi sono|sussiston)"),
    },
    "en": {
        "mgmt": "Management fees and other",
        "txn": "Transaction costs",
        "entry": "Entry costs",
        "exit": "Exit costs",
        "perf": "Performance fees",
        "none": r"(?:[Nn]o performance fee|we do not charge|There is no)",
    },
}
MIN_CHARS_PER_PAGE = 200          # below this, suspect the extractor, not the file


def fetch(url: str, timeout: int = 25) -> bytes | None:
    req = urllib.request.Request(url, headers={
        "User-Agent": UA, "Accept-Language": "de-DE,de;q=0.9,en;q=0.8"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read()
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError):
        return None


def pdf_text(data: bytes) -> tuple[str, str | None]:
    """(text, warning). A warning means the EXTRACTOR is suspect, not the file."""
    try:
        import fitz
    except ImportError:
        return "", "PyMuPDF not installed (pip install pymupdf)"
    try:
        doc = fitz.open(stream=data, filetype="pdf")
    except Exception as e:
        return "", f"unreadable PDF ({type(e).__name__})"
    text = "\n".join(p.get_text() for p in doc)
    if doc.page_count and len(text) / doc.page_count < MIN_CHARS_PER_PAGE:
        return text, (f"only {len(text)//max(doc.page_count,1)} chars/page - assume the "
                      f"EXTRACTOR failed, not that the costs are absent")
    return text, None


def parse_kid(text: str) -> dict:
    """Cost block from KID text, language-detected. Returns {} if no block found."""
    flat = re.sub(r"\s+", " ", text)
    lang = "it" if "Costi di ingresso" in flat else ("en" if "Entry costs" in flat else None)
    if lang is None:
        return {}
    L = LABELS[lang]

    # Every cost line is read INSIDE ITS OWN SECTION, cut at whichever other cost
    # label comes next. A fixed-width window is not good enough and the self-test
    # proved it: "Costi di ingresso Non addebitiamo ... Commissioni di gestione ...
    # 0,62%" has no percentage of its own, so a 220-character window sailed past
    # the denial into the MANAGEMENT fee and reported 0.62% as an entry charge.
    # Reading one field out of a neighbouring field's number is the same class of
    # error as reading the wrong share class: arithmetically fine, factually wrong.
    bounds = sorted(flat.find(v) for k, v in L.items()
                    if k != "none" and flat.find(v) >= 0)

    def near(label: str, window: int = 300) -> str:
        i = flat.find(label)
        if i < 0:
            return ""
        nxt = next((b for b in bounds if b > i), len(flat))
        return flat[i:min(i + window, nxt)]

    def pct(label: str) -> float | None:
        m = re.search(NUM + r"\s*%", near(label))
        return float(m.group(1).replace(",", ".")) if m else None

    def charge(label: str) -> float | None:
        """A one-off charge: an explicit percent, or 0 when the KID says it charges
        none. Distinguishing 'states zero' from 'could not read' is the point."""
        seg = near(label, 220)
        m = re.search(NUM + r"\s*%", seg)
        if m:
            return float(m.group(1).replace(",", "."))
        return 0.0 if re.search(L["none"], seg) else None

    # A performance-fee section that DENIES the fee also contains its own label,
    # so read the denial before reading any number near it.
    perf_seg = near(L["perf"], 260)
    if re.search(L["none"], perf_seg):
        perf, perf_note = 0.0, None
    else:
        pm = re.search(NUM + r"\s*%", perf_seg)
        perf = float(pm.group(1).replace(",", ".")) if pm else None
        perf_note = re.sub(r"^" + re.escape(L["perf"]) + r"\s*", "", perf_seg)[:140] or None

    mgmt, txn = pct(L["mgmt"]), pct(L["txn"])
    return {
        "lang": lang, "mgmt": mgmt, "txn": txn,
        "ongoing": None if mgmt is None else round(mgmt + (txn or 0.0), 4),
        "entry_max": charge(L["entry"]), "exit_max": charge(L["exit"]),
        "perf": perf, "perf_note": perf_note,
    }


# ------------------------------------------------------------------- the ladder
def rung_issuer_kid(isin: str) -> tuple[dict, str] | None:
    data = fetch(f"https://finecoassetmanagement.com/documents/KIIDs/EN/{isin}.pdf")
    if not data or not data.startswith(b"%PDF"):
        return None
    text, warn = pdf_text(data)
    if warn:
        return {"warning": warn}, "issuer-KID"
    got = parse_kid(text)
    return (got, "issuer-KID") if got.get("ongoing") is not None else None


def rung_local_kid(isin: str, kid_dir: Path | None) -> tuple[dict, str] | None:
    if not kid_dir or not kid_dir.is_dir():
        return None
    for p in sorted(kid_dir.glob("*.pdf")):
        try:
            text, warn = pdf_text(p.read_bytes())
        except OSError:
            continue
        if isin not in re.sub(r"\s+", "", text):
            continue
        if warn:
            return {"warning": f"{p.name}: {warn}"}, "local-KID"
        got = parse_kid(text)
        if got.get("ongoing") is not None:
            got["file"] = p.name
            return got, "local-KID"
    return None


def rung_fondsweb(isin: str) -> tuple[dict, str] | None:
    data = fetch(f"https://www.fondsweb.com/de/{isin}")
    if not data:
        return None
    import html as html_mod
    page = data.decode("utf-8", "replace")
    if "Fehler - fondsweb" in page:          # fondsweb's 200-with-error-body
        return None
    page = re.sub(r"<script.*?</script>|<style.*?</style>", " ", page, flags=re.S)
    # UNESCAPE BEFORE PARSING. The label and its value are separated by an icon
    # glyph that ships as the entity `&#xE88F;` - which CONTAINS DIGITS, so the
    # digit-free filler in the patterns below cannot span it and every lookup
    # returns None while the fetch reports a clean HTTP 200. Three funds this
    # script had already verified by hand came back "unresolved" on the first
    # live run for exactly this reason.
    txt = re.sub(r"\s+", " ", html_mod.unescape(re.sub(r"<[^>]+>", " ", page)))

    def g(label):
        # The private-use icon glyph between label and value is why this is not \s*
        m = re.search(re.escape(label) + r"[^0-9%]{0,60}?([0-9]+,[0-9]+)\s*%", txt)
        return float(m.group(1).replace(",", ".")) if m else None

    ongoing = g("laufende Kosten")
    if ongoing is None:
        return None
    name = re.match(r"\s*(.*?)\s*\((?:WKN|Valor)", txt)
    return ({"name": name.group(1) if name else None,
             "ongoing": ongoing, "txn": g("Portfoliotransaktionskosten"),
             "mgmt": g("Sonstige laufende Kosten"),
             "entry_max": None, "exit_max": None, "perf": None, "perf_note": None,
             "lang": "de"}, "fondsweb")


def resolve(isin: str, kid_dir: Path | None, offline: bool = False) -> dict:
    rungs = [] if offline else [lambda: rung_issuer_kid(isin)]
    rungs.insert(0, lambda: rung_local_kid(isin, kid_dir))
    if not offline:
        rungs.append(lambda: rung_fondsweb(isin))
    for r in rungs:
        got = r()
        if got:
            data, source = got
            data["isin"], data["source"] = isin, source
            return data
    return {"isin": isin, "source": "UNRESOLVED", "ongoing": None,
            "note": "no rung reached this ISIN - fetch the KID by hand "
                    "(investing.com carries Italian-distributed funds and blocks "
                    "scripts, so an agent fetch works where this does not)"}


# --------------------------------------------------------------------- self-test
FIXTURES = [
    # (name, text, expected) - each reproduces a trap hit for real on 2026-08-26.
    ("IT comma decimals, no charges",
     "Costi di ingresso Non addebitiamo una commissione di sottoscrizione. Costi di uscita "
     "Non addebitiamo una commissione di uscita. Commissioni di gestione e altri costi "
     "amministrativi o di esercizio 0,62% del valore. Costi di transazione 0,02% del valore. "
     "Commissioni di performance Per questo prodotto non si applicano le commissioni di performance.",
     dict(ongoing=0.64, entry_max=0.0, perf=0.0)),
    ("EN dot decimals (the separator trap)",
     "Entry costs 5.00% of the amount you pay in. Exit costs we do not charge an exit fee. "
     "Management fees and other administrative or operating costs 1.69% of the value per year. "
     "Transaction costs 0.36% of the value per year. Performance fees There is no performance fee.",
     dict(ongoing=2.05, entry_max=5.0, perf=0.0)),
    ("IT 'non ha alcuna commissione di performance' is a denial, not a fee",
     "Costi di ingresso Non addebitiamo commissioni. Costi di uscita Non addebitiamo. "
     "Commissioni di gestione e altri costi amministrativi o di esercizio 1,45% del valore. "
     "Costi di transazione 0,18% del valore. Commissioni di performance Il presente prodotto "
     "non ha alcuna commissione di performance.",
     dict(ongoing=1.63, perf=0.0)),
    ("IT with a REAL performance fee (must not read as 0)",
     "Costi di ingresso Fino a un massimo del 3,0% dell'importo versato. Costi di uscita "
     "Non applichiamo commissioni di uscita. Commissioni di gestione e altri costi amministrativi "
     "o di esercizio 1,6% del valore dell'investimento all'anno. Costi di transazione 0,6% del "
     "valore. Commissioni di performance Puo essere addebitata una commissione legata al "
     "rendimento pari a fino il 15% dei rendimenti.",
     dict(ongoing=2.2, entry_max=3.0, perf=15.0)),
]


def self_test() -> int:
    failures = []
    for name, text, exp in FIXTURES:
        got = parse_kid(text)
        for k, want in exp.items():
            if got.get(k) != want:
                failures.append(f"  [FAIL] {name}: {k} = {got.get(k)!r}, expected {want!r}")
    # Both directions: text with no cost block must yield nothing, not zeros.
    if parse_kid("A factsheet with no cost table at all.") != {}:
        failures.append("  [FAIL] a document with no cost block must return {}, not zeros")
    # A thin extraction must warn rather than report absence.
    _, warn = pdf_text(b"not a pdf at all")
    if warn is None:
        failures.append("  [FAIL] an unreadable PDF must produce a warning")
    for name, _, _ in FIXTURES:
        print(f"  [PASS] {name}")
    print("  [PASS] no cost block -> {} (not a false zero)")
    print("  [PASS] unreadable PDF -> warning (not 'costs absent')")
    if failures:
        print("\n" + "\n".join(failures))
        return 1
    print(f"\n{len(FIXTURES) + 2}/{len(FIXTURES) + 2} parser cases pass.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("isins", nargs="*")
    ap.add_argument("--isin-file", help="any text/TSV file; every ISIN in it is read")
    ap.add_argument("--kid-dir", help="folder of already-downloaded KID PDFs (primary rung)")
    ap.add_argument("--json", help="write results here")
    ap.add_argument("--offline", action="store_true", help="local KIDs only, no network")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass
    if args.self_test:
        return self_test()

    isins = [i.upper() for i in args.isins]
    if args.isin_file:
        isins += ISIN_RE.findall(Path(args.isin_file).read_text(encoding="utf-8", errors="replace"))
    seen, ordered = set(), []
    for i in isins:
        if i not in seen:
            seen.add(i); ordered.append(i)
    if not ordered:
        ap.error("give at least one ISIN, or --isin-file")

    kid_dir = Path(args.kid_dir).expanduser() if args.kid_dir else None
    out = {}
    print(f"{'ISIN':<15}{'ongoing':>9}{'entry':>8}{'perf':>7}  source")
    for isin in ordered:
        r = resolve(isin, kid_dir, args.offline)
        out[isin] = r
        ong = f"{r['ongoing']:.2f}%" if r.get("ongoing") is not None else "--"
        ent = f"{r['entry_max']:.2f}%" if r.get("entry_max") is not None else "--"
        prf = ("none" if r.get("perf") == 0 else
               (f"{r['perf']:.0f}%" if r.get("perf") else "--"))
        print(f"{isin:<15}{ong:>9}{ent:>8}{prf:>7}  {r['source']}")
        if r.get("warning"):
            print(f"                !! {r['warning']}")
        if r.get("perf_note"):
            print(f"                !! performance fee: {r['perf_note'][:88]}")

    unresolved = [i for i, r in out.items() if r.get("ongoing") is None]
    if unresolved:
        print(f"\n  {len(unresolved)} UNRESOLVED: {', '.join(unresolved)}")
        print("  These are not zero-cost. Fetch each KID by hand and re-run with --kid-dir.")
    if args.json:
        Path(args.json).write_text(json.dumps(out, indent=1), encoding="utf-8")
        print(f"\n  wrote {args.json}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
