#!/usr/bin/env python3
"""Objective fund measures against a benchmark — the arithmetic half of judging a fund.

WHY THIS EXISTS. A factsheet leads with trailing return, which is the least
useful number on it. The question that matters is whether a fund delivered
something a cheap benchmark did not, and whether that difference is
distinguishable from luck. Both are computable from price history, and neither
is on the factsheet.

WHAT IT COMPUTES, per fund, on the COMMON overlapping period with the benchmark:
  return and volatility (annualised)   Sharpe, Sortino
  max drawdown and time to recover     tracking error, information ratio
  CAPM alpha and beta, each with a t-statistic, plus R-squared
  up-capture and down-capture          correlation matrix across everything

THE THREE THINGS IT REFUSES TO LET YOU FORGET:

1. ALPHA WITHOUT A t-STATISTIC IS A NUMBER, NOT A FINDING. Every alpha is
   reported with its t-stat, its observation count, and — the line that ends most
   arguments — how many YEARS of the fund's own tracking error would be needed to
   distinguish that alpha from zero. Usually it is more years than the fund has
   existed. That arithmetic is `years = (2 x tracking error / alpha)^2`, and at a
   2% alpha with 4% tracking error it is sixteen years.

2. LOW R-SQUARED MEANS THE BENCHMARK IS WRONG, AND THEN THE ALPHA IS MEANINGLESS.
   Alpha is defined relative to a benchmark. If the fund only shares half its
   variance with the index you chose, the residual is mostly unexplained
   exposure rather than skill, and it is flagged rather than reported quietly.

3. THE COMMON PERIOD IS THE ONLY HONEST WINDOW. Comparing a three-year fund's
   record against a fifteen-year fund's is the standard silent error in fund
   comparison, so every series is truncated to the overlap and the window is
   printed above the table.

Usage:
    python scripts/fund-metrics.py IWDA.AS --benchmark URTH
    python scripts/fund-metrics.py FUND1 FUND2 FUND3 --benchmark SPY --rf 4.0
    python scripts/fund-metrics.py ARKK --benchmark QQQ --years 5
"""

from __future__ import annotations

import argparse
import sys

TRADING_MONTHS = 12


def fx_series(base: str, quote: str, index):
    """Monthly {base}->{quote} rate aligned to `index`, or None if unavailable."""
    import yfinance as yf
    if base == quote:
        return None
    h = yf.Ticker(f"{base}{quote}=X").history(period="max", auto_adjust=False)
    if h is None or h.empty:
        return None
    r = h["Close"].dropna().resample("ME").last()
    r.index = r.index.tz_localize(None) if r.index.tz is not None else r.index
    return r.reindex(index, method="ffill")


def price_series(ticker: str, target_ccy: str | None):
    """Monthly price series converted into `target_ccy`, plus its native currency.

    THE BUG THIS EXISTS TO PREVENT, measured rather than imagined: over the three
    years to 2026-08, IWDA.AS (EUR) and URTH (USD) — two listings of the same
    MSCI World exposure — annualise at +17.2% and +20.3%. The 3.1 points a year
    between them is entirely EUR/USD, and a currency-blind tool reports it as
    alpha. For a EUR-base owner comparing European UCITS against US-listed
    benchmarks that is not an edge case, it is the normal case.

    GBp is pence, not pounds: the London listings quote in 1/100 of GBP and a
    naive FX conversion is then wrong by two orders of magnitude.
    """
    import yfinance as yf
    tk = yf.Ticker(ticker)
    h = tk.history(period="max", auto_adjust=True)
    if h is None or h.empty:
        return None, None, None
    px = h["Close"].dropna().resample("ME").last()
    if px.index.tz is not None:
        px.index = px.index.tz_localize(None)

    native = ((tk.info or {}).get("currency") or "").upper() or "?"
    if native == "GBP" and (tk.info or {}).get("currency") == "GBp":
        native = "GBP"
    raw = (tk.info or {}).get("currency") or ""
    if raw == "GBp":                      # pence -> pounds before any conversion
        px = px / 100.0
        native = "GBP"

    if not target_ccy or native in ("?", target_ccy):
        return px, native, (native == target_ccy or not target_ccy)
    rate = fx_series(native, target_ccy, px.index)
    if rate is None or rate.isna().all():
        return px, native, False          # caller warns; do not silently pretend
    return (px * rate).dropna(), native, True


def monthly_returns_from(px):
    return px.pct_change().dropna()


def ols(y, x):
    """alpha, beta, t_alpha, t_beta, r2, residual sigma. numpy only."""
    import numpy as np
    n = len(y)
    X = np.column_stack([np.ones(n), x])
    coef, *_ = np.linalg.lstsq(X, y, rcond=None)
    resid = y - X @ coef
    dof = n - 2
    if dof <= 0:
        return coef[0], coef[1], float("nan"), float("nan"), float("nan"), float("nan")
    s2 = float(resid @ resid) / dof
    cov = s2 * np.linalg.inv(X.T @ X)
    se = np.sqrt(np.diag(cov))
    ss_tot = float(((y - y.mean()) ** 2).sum())
    r2 = 1 - float(resid @ resid) / ss_tot if ss_tot > 0 else float("nan")
    return coef[0], coef[1], coef[0] / se[0], coef[1] / se[1], r2, float(np.sqrt(s2))


def max_drawdown(cum):
    peak, mdd, peak_i, trough_i, worst = cum[0], 0.0, 0, 0, (0, 0)
    for i, v in enumerate(cum):
        if v > peak:
            peak, peak_i = v, i
        dd = v / peak - 1
        if dd < mdd:
            mdd, trough_i, worst = dd, i, (peak_i, i)
    recovered = None
    p_i, t_i = worst
    for j in range(t_i, len(cum)):
        if cum[j] >= cum[p_i]:
            recovered = (j - p_i) / TRADING_MONTHS
            break
    return mdd, recovered


def analyse(name, r, rb, rf_monthly):
    import numpy as np
    ex_f = (r - rf_monthly).to_numpy()
    ex_b = (rb - rf_monthly).to_numpy()
    n = len(r)

    ann_ret = float((1 + r).prod() ** (TRADING_MONTHS / n) - 1)
    ann_vol = float(r.std(ddof=1) * np.sqrt(TRADING_MONTHS))
    sharpe = float(ex_f.mean() / ex_f.std(ddof=1) * np.sqrt(TRADING_MONTHS)) if ex_f.std(ddof=1) > 0 else float("nan")
    downside = r[r < 0]
    sortino = (float(ex_f.mean() * TRADING_MONTHS / (downside.std(ddof=1) * np.sqrt(TRADING_MONTHS)))
               if len(downside) > 1 and downside.std(ddof=1) > 0 else float("nan"))

    active = (r - rb).to_numpy()
    te = float(active.std(ddof=1) * np.sqrt(TRADING_MONTHS))
    ir = float(active.mean() * TRADING_MONTHS / te) if te > 0 else float("nan")

    # Regressing the benchmark on itself leaves residuals that are zero only to
    # floating-point tolerance, so the standard error collapses and the t-stat
    # becomes a large spurious number. Report the exact identity instead.
    is_self = bool(np.allclose(ex_f, ex_b))
    if is_self:
        a_m, beta, t_a, r2, resid_sd = 0.0, 1.0, float("nan"), 1.0, 0.0
    else:
        a_m, beta, t_a, _t_b, r2, resid_sd = ols(ex_f, ex_b)
    alpha_ann = (1 + a_m) ** TRADING_MONTHS - 1
    te_resid = resid_sd * np.sqrt(TRADING_MONTHS)
    years_needed = ((2 * te_resid / alpha_ann) ** 2) if alpha_ann not in (0,) and abs(alpha_ann) > 1e-9 else float("inf")

    up = rb > 0
    dn = rb < 0
    up_cap = float(r[up].mean() / rb[up].mean()) if up.sum() > 1 and rb[up].mean() != 0 else float("nan")
    dn_cap = float(r[dn].mean() / rb[dn].mean()) if dn.sum() > 1 and rb[dn].mean() != 0 else float("nan")

    cum = (1 + r).cumprod().to_numpy()
    mdd, rec = max_drawdown(cum)

    return dict(name=name, n=n, years=n / TRADING_MONTHS, ann_ret=ann_ret, ann_vol=ann_vol,
                sharpe=sharpe, sortino=sortino, te=te, ir=ir, alpha=alpha_ann, t_alpha=t_a,
                beta=beta, r2=r2, years_needed=years_needed, up=up_cap, dn=dn_cap,
                mdd=mdd, rec=rec)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("tickers", nargs="+")
    ap.add_argument("--benchmark", required=True)
    ap.add_argument("--rf", type=float, default=0.0, help="annual risk-free %%, e.g. 4.0")
    ap.add_argument("--years", type=int, help="limit to the last N years of the common period")
    ap.add_argument("--currency", help="convert every series into this currency before comparing "
                                       "(default: the benchmark's own currency). Mixing currencies "
                                       "silently turns FX moves into alpha.")
    args = ap.parse_args()
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass

    import pandas as pd
    # Resolve the target currency from the benchmark unless told otherwise, then
    # convert every series into it before a single return is computed.
    bench_px, bench_ccy, _ = price_series(args.benchmark, None)
    if bench_px is None:
        print(f"{args.benchmark}: no price history", file=sys.stderr)
        return 1
    target = (args.currency or bench_ccy or "").upper()

    series, natives, unconverted = {}, {}, []
    for t in args.tickers + [args.benchmark]:
        px, native, ok = price_series(t, target)
        if px is None or len(px) < 14:
            print(f"{t}: insufficient price history", file=sys.stderr)
            return 1
        if not ok:
            unconverted.append(f"{t} ({native})")
        natives[t] = native
        series[t] = monthly_returns_from(px)

    df = pd.DataFrame(series).dropna()          # <- the common period, enforced
    if args.years:
        df = df.tail(args.years * TRADING_MONTHS)
    if len(df) < 13:
        print("Common period is under 13 months — nothing meaningful to compute.", file=sys.stderr)
        return 1

    rf_m = (1 + args.rf / 100) ** (1 / TRADING_MONTHS) - 1
    rb = df[args.benchmark]
    rows = [analyse(t, df[t], rb, rf_m) for t in args.tickers]
    bench = analyse(args.benchmark, rb, rb, rf_m)

    span = f"{df.index[0].date()} to {df.index[-1].date()}"
    print(f"\n{'=' * 78}")
    print(f"FUND METRICS vs {args.benchmark}")
    print(f"{'=' * 78}")
    print(f"  Common period : {span}  ({len(df)} months, {len(df)/12:.1f} years)")
    print(f"  Risk-free     : {args.rf:.2f}%/yr    Basis: monthly total return, dividends reinvested")
    mixed = sorted(set(natives.values()))
    print(f"  Currency      : all series converted to {target}"
          + (f"  (native: {', '.join(mixed)})" if len(mixed) > 1 else ""))
    if unconverted:
        print(f"  !! NOT CONVERTED: {', '.join(unconverted)} — no FX series available. Any excess")
        print(f"     return for these is contaminated by currency and must not be read as alpha.")
    print(f"  Every series is truncated to the overlap above. A longer record for one fund is")
    print(f"  not used, because a comparison across different windows is not a comparison.\n")

    hdr = (f"  {'Fund':<12} {'Return':>8} {'Vol':>7} {'Sharpe':>7} {'Sortino':>8} {'MaxDD':>8}"
           f" {'TE':>7} {'IR':>6} {'Beta':>6} {'R2':>6} {'Alpha':>8} {'t':>6}")
    print(hdr)
    print(f"  {'-' * 100}")
    for m in rows + [bench]:
        tag = "  (bench)" if m["name"] == args.benchmark else ""
        print(f"  {m['name'][:12]:<12} {m['ann_ret']:>7.1%} {m['ann_vol']:>6.1%} {m['sharpe']:>7.2f}"
              f" {m['sortino']:>8.2f} {m['mdd']:>7.1%} {m['te']:>6.1%} {m['ir']:>6.2f}"
              f" {m['beta']:>6.2f} {m['r2']:>6.2f} {m['alpha']:>+7.1%}"
              f" {('    --' if m['t_alpha'] != m['t_alpha'] else f'{chr(37)}6.2f' % m['t_alpha'])}{tag}")

    print(f"\n  {'Fund':<12} {'Up-capture':>11} {'Down-capture':>13} {'DD recovery':>13}")
    print(f"  {'-' * 52}")
    for m in rows:
        rec = f"{m['rec']:.1f}y" if m["rec"] else "not yet"
        print(f"  {m['name'][:12]:<12} {m['up']:>10.2f}  {m['dn']:>12.2f} {rec:>13}")

    print(f"\n  CORRELATION (monthly, common period)")
    corr = df.corr()
    cols = list(df.columns)
    print("  " + " " * 12 + "".join(f"{c[:8]:>10}" for c in cols))
    for c in cols:
        print(f"  {c[:12]:<12}" + "".join(f"{corr.loc[c, d]:>10.2f}" for d in cols))

    # --- the honesty block: what the numbers above do and do not support --------
    print(f"\n  READING THIS")
    for m in rows:
        notes = []
        if m["r2"] < 0.80:
            notes.append(f"R2 {m['r2']:.2f} — the benchmark explains only {m['r2']:.0%} of this "
                         f"fund's variance, so its alpha is mostly unexplained exposure rather "
                         f"than skill. Find a benchmark that fits before quoting alpha.")
        if abs(m["t_alpha"]) < 2:
            notes.append(f"alpha {m['alpha']:+.1%} has t={m['t_alpha']:.2f} on {m['n']} months — "
                         f"NOT distinguishable from zero at conventional significance.")
        if m["years_needed"] != float("inf") and m["years_needed"] > m["years"]:
            notes.append(f"at this alpha and tracking error it would take ~{m['years_needed']:.0f} "
                         f"years to reach t=2; the record is {m['years']:.1f}.")
        if m["years"] < 10:
            notes.append(f"{m['years']:.1f} years of common history is short — it may contain no "
                         f"full drawdown-and-recovery cycle.")
        if notes:
            print(f"    {m['name']}:")
            for nte in notes:
                print(f"      - {nte}")
        else:
            print(f"    {m['name']}: alpha {m['alpha']:+.1%} at t={m['t_alpha']:.2f} over "
                  f"{m['years']:.1f}y with R2 {m['r2']:.2f} — statistically meaningful on this record.")

    print(f"\n  These are CAPM alphas: one benchmark, no factor controls. A manager selling size,")
    print(f"  value or momentum beta will show alpha here that a Carhart regression absorbs, so")
    print(f"  label anything quoted from this tool a CAPM alpha rather than just an alpha.")
    print(f"  Costs are not in these numbers beyond what price history already reflects, and a")
    print(f"  fee difference is near-certain while an alpha difference usually is not. Settle the")
    print(f"  cost comparison from the wrapper lens before attributing anything to a manager.\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
