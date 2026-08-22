#!/usr/bin/env python3
"""Realised return and drawdown distributions for an exposure — the wealth-manager view.

WHY THIS EXISTS. A fund valuation has to answer "what has this exposure actually
returned, and what did it put you through on the way" without reciting remembered
statistics. The vault forbids inventing figures, so the choice is between a
computed answer and no answer. This computes the part that price history can
support: rolling returns over the horizon that matters, the DISTRIBUTION rather
than the average, drawdown depth, and time to recovery.

WHAT IT DELIBERATELY DOES NOT DO. It cannot tell you what returns followed a
given STARTING VALUATION, because that needs decades of valuation history no
price feed carries (Shiller's series for US equities, and its equivalents
elsewhere). That evidence belongs in `library/` via `absorb`, cited like any
other external source — not hardcoded here where it would rot silently and
carry no provenance. The exposure framework names which sources close that gap.

Also honest about its own limits:
  - Most ETFs are younger than one full cycle. A 10-year rolling window on a
    12-year fund gives ~3 independent observations pretending to be hundreds;
    the script reports the overlap so the number is read correctly.
  - yfinance total-return handling varies by ticker. Use the index or a long-
    lived proxy for history and the fund itself only for tracking behaviour.
  - Nominal unless --cpi is supplied. Real returns are what matter over a decade
    and the difference is not small.

Usage:
    python scripts/exposure-history.py SPY                    # default 10y windows
    python scripts/exposure-history.py IWDA.AS --years 5 10
    python scripts/exposure-history.py SPY --start 1993-01-01 --cpi 2.5
    python scripts/exposure-history.py SPY VOO IWDA.AS        # compare
"""

from __future__ import annotations

import argparse
import sys
from datetime import datetime


def load(ticker: str, start: str | None):
    import yfinance as yf
    t = yf.Ticker(ticker)
    h = t.history(period="max" if not start else None, start=start, auto_adjust=True)
    if h is None or h.empty:
        return None, None
    px = h["Close"].dropna()
    return px, t


def rolling_returns(px, years: int) -> list[float]:
    """Annualised return for every window of `years` that fits in the history.

    Windows overlap heavily by construction. That is standard practice and also
    the main way this kind of table misleads, so the caller reports the
    independent-window count alongside.
    """
    if px is None or px.empty:
        return []
    out = []
    for i in range(len(px)):
        start_date = px.index[i]
        target = start_date + __import__("pandas").DateOffset(years=years)
        later = px.index[px.index >= target]
        if len(later) == 0:
            break
        j = px.index.get_loc(later[0])
        begin, end = float(px.iloc[i]), float(px.iloc[j])
        if begin > 0:
            out.append((end / begin) ** (1 / years) - 1)
    return out


def pct(xs: list[float], q: float) -> float:
    if not xs:
        return float("nan")
    s = sorted(xs)
    k = (len(s) - 1) * q
    lo, hi = int(k), min(int(k) + 1, len(s) - 1)
    return s[lo] + (s[hi] - s[lo]) * (k - lo)


def drawdowns(px):
    """Every peak-to-trough decline, with the time taken to regain the prior peak."""
    if px is None or px.empty:
        return []
    peak, peak_date = float(px.iloc[0]), px.index[0]
    trough, trough_date = peak, peak_date
    episodes, in_dd = [], False
    for date, raw in px.items():
        val = float(raw)
        if val >= peak:
            if in_dd:
                episodes.append({
                    "peak_date": peak_date, "trough_date": trough_date,
                    "depth": trough / peak - 1,
                    "recovery_days": (date - peak_date).days,
                })
                in_dd = False
            peak, peak_date = val, date
            trough, trough_date = val, date
        else:
            if val < trough:
                trough, trough_date = val, date
            if trough / peak - 1 <= -0.05:
                in_dd = True
    if in_dd:  # still under water at the end of the series
        episodes.append({
            "peak_date": peak_date, "trough_date": trough_date,
            "depth": trough / peak - 1, "recovery_days": None,
        })
    return sorted(episodes, key=lambda e: e["depth"])


def report(ticker: str, years_list: list[int], start: str | None, cpi: float | None) -> int:
    px, t = load(ticker, start)
    if px is None or len(px) < 30:
        print(f"{ticker}: no usable price history (need a longer window or another ticker)")
        return 1

    span_years = (px.index[-1] - px.index[0]).days / 365.25
    print(f"\n{'=' * 68}\n{ticker}   {px.index[0].date()} to {px.index[-1].date()}"
          f"   ({span_years:.1f} years, {len(px)} sessions)")
    try:
        name = (t.info or {}).get("shortName")
        if name:
            print(f"  {name}")
    except Exception:
        pass
    print(f"  Total-return basis (auto_adjust=True: dividends reinvested)."
          f"{'  Real, CPI %.1f%%/yr.' % cpi if cpi else '  NOMINAL — subtract inflation for the real figure.'}")

    for years in years_list:
        rr = rolling_returns(px, years)
        if not rr:
            print(f"\n  {years}-year windows: history too short ({span_years:.1f}y available)")
            continue
        if cpi:
            rr = [(1 + r) / (1 + cpi / 100) - 1 for r in rr]
        independent = span_years / years
        print(f"\n  {years}-YEAR ANNUALISED, {len(rr)} overlapping windows "
              f"(~{independent:.1f} independent — read the spread, not the count)")
        print(f"    worst {pct(rr,0):+6.1%}   p10 {pct(rr,0.10):+6.1%}   median {pct(rr,0.50):+6.1%}"
              f"   p90 {pct(rr,0.90):+6.1%}   best {pct(rr,1):+6.1%}")
        neg = sum(1 for r in rr if r < 0) / len(rr)
        print(f"    windows ending below zero: {neg:.0%}")

    dd = drawdowns(px)
    if dd:
        print(f"\n  WORST DRAWDOWNS (peak to trough, and time to regain the peak)")
        for e in dd[:5]:
            rec = (f"{e['recovery_days']/365.25:.1f}y" if e["recovery_days"]
                   else "NOT YET RECOVERED")
            print(f"    {e['depth']:+7.1%}  {e['peak_date'].date()} -> {e['trough_date'].date()}"
                  f"   recovered in {rec}")
    print()
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("tickers", nargs="+")
    ap.add_argument("--years", nargs="+", type=int, default=[10],
                    help="rolling window lengths in years (default: 10)")
    ap.add_argument("--start", help="ISO date to start the history from")
    ap.add_argument("--cpi", type=float,
                    help="annual inflation %% to deflate by, e.g. 2.5 for a real-return view")
    args = ap.parse_args()
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass
    rc = 0
    for tk in args.tickers:
        rc |= report(tk, args.years, args.start, args.cpi)
    print("Reminder: this is REALISED history, not a forecast, and it says nothing about")
    print("what follows from today's valuation. That evidence belongs in library/ via absorb.")
    return rc


if __name__ == "__main__":
    sys.exit(main())
