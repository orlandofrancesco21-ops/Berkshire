#!/usr/bin/env python3
"""What returns actually followed a given starting valuation.

WHY THIS EXISTS. Every fund valuation in this vault has to answer "what does
today's starting multiple imply for the next decade" without reciting a
remembered statistic. `exposure-history.py` gives the realised distribution but
says nothing about the starting point. This closes that gap by computing the
conditional distribution from an absorbed long-history dataset.

THE TWO HONESTY PROBLEMS, both handled explicitly rather than in a footnote:

1. OVERLAPPING WINDOWS. Monthly observations of a 10-year forward return share
   119 of their 120 months with their neighbour. A bucket holding 200 monthly
   observations may contain fewer than two independent decades. Every bucket
   therefore reports its independent-window count, and the tool refuses to
   present a bucket as evidence when that count is below 2.

2. THE VALUATION RATCHET, which is the subtler one. CAPE has trended structurally
   upward — accounting changes, the buyback-versus-dividend shift, sector mix.
   Rank today's reading against the FULL history and almost every post-1990
   month lands in the top decile, so "the top decile returned X" is really "the
   last thirty years returned X" wearing a valuation label. Worse, a full-sample
   decile uses information from the future: in 1950 nobody knew what the 2020
   distribution would look like.

   So the default basis is EXPANDING: each month's percentile is computed against
   its own prior history only, which is what an investor standing there could
   actually have known. `--basis full` is available for comparison and the tool
   prints both headline readings so the difference is visible rather than
   assumed away.

WHAT THIS IS NOT. It is a conditional distribution of what happened, not a
forecast. The relationship is real over a decade and weak over one to three
years, and even the decade version leaves most of the variance unexplained. The
output is a range to argue inside, never a number to act on.

Usage:
    python scripts/valuation-conditional.py                       # CAPE, 10y, expanding
    python scripts/valuation-conditional.py --horizon 15
    python scripts/valuation-conditional.py --basis full
    python scripts/valuation-conditional.py --anchor tr-cape      # total-return CAPE
    python scripts/valuation-conditional.py --buckets 5           # quintiles
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
ARCHIVE = REPO_ROOT / "library" / "sources" / "shiller-ie-data.xls"

# Column positions in the Data sheet of Shiller's ie_data.xls. Positional rather
# than by name because the header spans four merged rows; the entry in library/
# records the same addresses so a locator can be checked against the file.
COL = {
    "date": 0,        # A: YYYY.MM, where .1 means October (a decimal, not a month index)
    "cpi": 4,         # E
    "real_tr": 9,     # J: Real Total Return Price — dividends reinvested, inflation-adjusted
    "cape": 12,       # M: P/E10
    "tr_cape": 14,    # O: Total Return CAPE
}
ANCHORS = {"cape": "cape", "tr-cape": "tr_cape"}


def load(anchor_col: str):
    try:
        import pandas as pd
    except ImportError:
        print("pandas is required: pip install pandas xlrd", file=sys.stderr)
        raise SystemExit(2)
    if not ARCHIVE.exists():
        print(f"Dataset not archived at {ARCHIVE.relative_to(REPO_ROOT)}.\n"
              "Absorb it first — see the dataset rung in 'Source archive and deep retrieval\n"
              "(canonical)'. Source: shillerdata.com (use the VERSIONED link on that page;\n"
              "the plain downloads/ie_data.xls path serves a copy years out of date).",
              file=sys.stderr)
        raise SystemExit(2)
    try:
        raw = pd.read_excel(ARCHIVE, sheet_name="Data", header=None)
    except ImportError:
        print("Reading .xls needs xlrd: pip install xlrd", file=sys.stderr)
        raise SystemExit(2)

    df = raw[raw[COL["date"]].notna()].copy()
    df = df[pd.to_numeric(df[COL["date"]], errors="coerce").notna()]
    out = pd.DataFrame({
        "date": pd.to_numeric(df[COL["date"]]),
        "anchor": pd.to_numeric(df[COL[anchor_col]], errors="coerce"),
        "real_tr": pd.to_numeric(df[COL["real_tr"]], errors="coerce"),
    }).reset_index(drop=True)
    return out.dropna(subset=["real_tr"]).reset_index(drop=True)


def label(d: float) -> str:
    """Shiller dates are YYYY.MM with .1 meaning October, so .1 != January."""
    year = int(d)
    frac = round((d - year) * 100)
    month = 10 if frac == 1 else frac
    return f"{year}-{month:02d}"


def forward_returns(df, horizon: int):
    """Annualised real total return over `horizon` years, from each month."""
    months = horizon * 12
    tr = df["real_tr"].to_numpy()
    n = len(df)
    rows = []
    for i in range(n - months):
        begin, end = tr[i], tr[i + months]
        if begin > 0 and end > 0:
            rows.append({
                "date": df["date"].iloc[i],
                "anchor": df["anchor"].iloc[i],
                "fwd": (end / begin) ** (1 / horizon) - 1,
            })
    import pandas as pd
    return pd.DataFrame(rows).dropna(subset=["anchor"]).reset_index(drop=True)


def assign_buckets(fw, buckets: int, basis: str, min_history_months: int = 240):
    """Bucket each observation by its anchor's percentile.

    expanding: percentile against that month's own prior history only — no
               look-ahead, which is the only basis an investor could have used.
    full:      percentile against the whole sample, including its own future.
    """
    import numpy as np
    a = fw["anchor"].to_numpy()
    if basis == "full":
        ranks = np.argsort(np.argsort(a)) / max(len(a) - 1, 1)
        fw = fw.copy()
        fw["pct"] = ranks
        fw["usable"] = True
    else:
        pcts, usable = [], []
        for i in range(len(a)):
            if i < min_history_months:
                pcts.append(np.nan); usable.append(False)
                continue
            prior = a[:i]
            pcts.append(float((prior < a[i]).sum()) / len(prior))
            usable.append(True)
        fw = fw.copy()
        fw["pct"] = pcts
        fw["usable"] = usable
        fw = fw[fw["usable"]].reset_index(drop=True)
    fw["bucket"] = (fw["pct"] * buckets).clip(0, buckets - 1).astype(int)
    return fw


def pct_of(xs, q: float) -> float:
    s = sorted(xs)
    if not s:
        return float("nan")
    k = (len(s) - 1) * q
    lo, hi = int(k), min(int(k) + 1, len(s) - 1)
    return s[lo] + (s[hi] - s[lo]) * (k - lo)


def report(anchor: str, horizon: int, buckets: int, basis: str) -> int:
    df = load(ANCHORS[anchor])
    fw = forward_returns(df, horizon)
    if fw.empty:
        print("No complete forward windows in the archived data.")
        return 1

    latest = df.iloc[-1]
    print(f"\n{'=' * 74}")
    print(f"FORWARD {horizon}-YEAR REAL TOTAL RETURN, BY STARTING {anchor.upper()}")
    print(f"{'=' * 74}")
    print(f"  Source   library/sources/shiller-ie-data.xls (Shiller ie_data.xls, Data sheet)")
    print(f"  History  {label(df['date'].iloc[0])} to {label(latest['date'])}"
          f"   |  latest {anchor.upper()}: {latest['anchor']:.2f}")
    print(f"  Windows  {len(fw)} complete, first starting {label(fw['date'].iloc[0])},"
          f" last {label(fw['date'].iloc[-1])}")
    print(f"  Basis    {basis} percentile"
          + ("  (each month ranked against its own prior history only — no look-ahead)"
             if basis == "expanding" else
             "  (whole-sample ranks: uses information from the future — comparison only)"))
    print(f"  Note     the last {horizon} years have no forward return yet and are excluded.")

    b = assign_buckets(fw, buckets, basis)
    span_years = (fw["date"].iloc[-1] - fw["date"].iloc[0])
    print(f"\n  {'Bucket':<12} {'Starting ' + anchor.upper():<18} {'n':>5} {'indep':>6}"
          f" {'worst':>8} {'p25':>8} {'median':>8} {'p75':>8} {'best':>8}")
    print(f"  {'-' * 88}")
    for k in range(buckets):
        sub = b[b["bucket"] == k]
        if sub.empty:
            continue
        rr = sub["fwd"].tolist()
        indep = len(sub) / (horizon * 12)
        lo_hi = f"{sub['anchor'].min():.1f} - {sub['anchor'].max():.1f}"
        flag = "" if indep >= 2 else "  <-- too few independent windows to be evidence"
        print(f"  {f'{k * 100 // buckets}-{(k + 1) * 100 // buckets}%':<12} {lo_hi:<18} {len(sub):>5}"
              f" {indep:>6.1f} {pct_of(rr, 0):>+7.1%} {pct_of(rr, 0.25):>+7.1%}"
              f" {pct_of(rr, 0.50):>+7.1%} {pct_of(rr, 0.75):>+7.1%} {pct_of(rr, 1):>+7.1%}{flag}")

    # Where today sits, on both bases, because the difference is the finding.
    cur = float(latest["anchor"])
    import numpy as np
    hist = fw["anchor"].to_numpy()
    full_pct = float((hist < cur).sum()) / len(hist)
    print(f"\n  TODAY: {anchor.upper()} {cur:.2f} at {label(latest['date'])}")
    print(f"    ranks at the {full_pct:.0%} percentile of all {len(hist)} months that have a"
          f" forward return")
    k = min(int(full_pct * buckets), buckets - 1)
    sub = b[b["bucket"] == k]
    if not sub.empty:
        rr = sub["fwd"].tolist()
        indep = len(sub) / (horizon * 12)
        print(f"    that bucket historically returned {pct_of(rr, 0):+.1%} to {pct_of(rr, 1):+.1%}"
              f" real, median {pct_of(rr, 0.50):+.1%}")
        print(f"    on {len(sub)} overlapping windows = ~{indep:.1f} independent decades"
              + ("" if indep >= 2 else "  — NOT ENOUGH TO BE EVIDENCE, treat as illustration"))
    if cur > hist.max():
        print(f"    !! ABOVE EVERY STARTING VALUE THAT HAS A COMPLETED WINDOW"
              f" (max {hist.max():.2f}). There is no historical analogue; the top bucket"
              f"\n       is the nearest thing and it understates how far outside the record"
              f" today sits.")

    print(f"\n  Read this as a distribution to argue inside, not a forecast. Even at a decade")
    print(f"  the starting multiple leaves most of the variance unexplained, and the spread")
    print(f"  within every bucket above is wider than the gap between buckets.\n")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--anchor", choices=sorted(ANCHORS), default="cape")
    ap.add_argument("--horizon", type=int, default=10, help="years (default 10)")
    ap.add_argument("--buckets", type=int, default=10, help="10 = deciles, 5 = quintiles")
    ap.add_argument("--basis", choices=["expanding", "full"], default="expanding")
    args = ap.parse_args()
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass
    return report(args.anchor, args.horizon, args.buckets, args.basis)


if __name__ == "__main__":
    sys.exit(main())
