---
name: valuation-check
description: For a position already held (or a watchlist name), check the current price against the fair value range in valuation.md and produce a clear hold/trim/add/exit recommendation. Reads thesis.md and valuation.md, resolved through both position tiers — sectors/{sector}/companies/{TICKER}/ and funds/{TICKER}/. For a fund the comparison is not price against fair value: it is expected net real return against the allocation bands, plus drift from target weight. Use during portfolio monitoring, when tempted to act on price movement alone, or when running a portfolio-wide review. Triggered by "valuation-check X", "should I add to X", "X just dropped Y%, what does the system say".
---

# valuation-check

## When to use

Either invoked directly on a single name, or by `portfolio-review` across all positions. Common phrasings:

- "Run valuation-check on [TICKER]"
- "Should I add to my [TICKER] position?"
- "[TICKER] just dropped 15%, what does the system say?"
- "Run valuation-check across the whole portfolio"

This is the skill that prevents emotional trading. Trust the framework. If the framework was wrong, the answer is to update the framework — not to override the recommendation in real time.

## Inputs

- Ticker (or "all" / "portfolio" to run across every position in `portfolio.md`)

## Process

1. **Locate the position's files.** Two tiers hold positions, so try both, in this order — the same lookup the lint's own `position_doc()` performs: `sectors/{sector}/companies/{TICKER}/`, then `funds/{TICKER}/`. Either way you want `thesis.md` and `valuation.md`. If neither tier has them, stop — you can't valuation-check a name without prior analysis.

   A hit in `funds/` puts this run on the **fund branch**: take step 4's FUND BRANCH instead of the price-vs-fair-value comparison, and read step 6 and step 7's fund variants. Per "Funds tier (canonical)" a fund has no fair value range, so there is nothing here for a price to be compared against.

2. **Check freshness.** Apply the canonical stale-thesis rule in `docs/build-plan.md` (Shared rules). If the thesis is stale by that definition, recommend `company-deep-dive` to refresh before acting on the recommendation — do not produce a price-based ADD or TRIM against a stale thesis. On the fund branch the refresh skill is `fund-deep-dive`, and that rule's clause (b) reads against the fund's annual report rather than an earnings release — `fund-deep-dive` step 0 owns that mapping.

3. **Pull current data** (per the canonical price-sourcing rule in `docs/build-plan.md` Shared rules — yfinance, snapshot date + currency):
   - Current price
   - Last 30 days price action
   - Current value of the multiples specified in `valuation.md` (the primary multiple plus cross-checks)

4. **Compare against the saved fair value range:**
   - Current price vs low / base / high from `valuation.md`
   - Current multiple vs sector median (from `kpis.md` if available)
   - Current multiple vs 5y average and 10y range (from the framework)

   **FUND BRANCH — there is no fair value range, so nothing here compares a price to one.** Per "Funds tier (canonical)" the canonical table in `funds/{TICKER}/valuation.md` is an expected **real** return over a stated horizon plus **allocation bands**. The comparison is:

   - **Refresh only the terms that actually move.** Restamp the **starting yield** and the **valuation anchor's percentile** — the anchor the exposure framework names, not a multiple chosen here — each per the canonical price-sourcing rule. Real growth, cost and tax terms do not move on a price feed: carry them forward and say in the entry that you did. A term you silently re-estimated is a `fund-deep-dive` refresh wearing this skill's name.
   - **Recompute the net real return** from those terms and read it against the **allocation bands** table as written — ADD / INITIATE, HOLD, TRIM / REBALANCE, EXIT. The band is the recommendation. Do not re-derive a band here; if the bands look wrong, that is a refresh, not an override.
   - **Check drift from target weight separately.** Current weight — recomputed from shares × current price, not the stored column — against the target weight and the drift threshold in the bands table. Rebalancing is a rule, not a view, so it can fire a TRIM while the expected-return band still says HOLD. When the two disagree, report both and name which one fired.
   - **Check the certain term.** Realized tracking difference and ongoing charge against what the last run assumed. A drag that has widened is a *vehicle* finding: it routes to `thesis-check`'s vehicle-level kill switches, not to a band change.
   - Never quote a price against an expected-return band. NAV and any premium/discount enter as execution facts, not as the comparison.

5. **Has anything in the thesis changed?** Check recent news and the most recent earnings release date. If there's been a material event since the last `valuation.md` update, the recommendation is REVIEW, not a price-based action.

6. **Produce the recommendation:**

   - **HOLD** — price within fair value range, thesis intact, no material change
   - **TRIM** — price > top of fair value range AND no thesis-positive change to justify expanding the range
   - **ADD** — price < bottom of fair value range AND thesis intact
   - **REVIEW** — thesis may have changed; run `thesis-check` first
   - **EXIT** — only if the thesis is broken (this requires explicit judgment, not a price-based trigger)

   On the fund branch the tokens are the same but their meaning comes from the bands table: **ADD / HOLD / TRIM** is the band the recomputed net real return (or the drift rule) lands in; **REVIEW** means the decomposition itself is stale — a term moved that this skill does not own — and routes to a `fund-deep-dive` refresh; **EXIT** means an *exposure-level* kill switch fired. A **vehicle-level** break is never an EXIT here: per "Funds tier (canonical)" it is a fund switch, so the recommendation is REVIEW with the substitute question handed to `fund-deep-dive`. ASYM-P1 applies unchanged — neither is ever triggered by the quote alone.

7. **Append a dated note to `thesis.md`** under the Update log:
   ```
   ### YYYY-MM-DD — valuation-check
   - Current price: $X ({currency}, pulled {date} via yfinance)
   - Fair value range: $Y – $Z (last updated: {date})
   - Position vs midpoint: {X}%
   - Recommendation: {HOLD/TRIM/ADD/REVIEW/EXIT}
   - Reasoning: {one sentence}
   ```

   On the fund branch, same heading token, the fund's own fields:
   ```
   ### YYYY-MM-DD — valuation-check
   - NAV: {x.xx CCY, pulled {date} via yfinance}; premium/discount: {x.xx%}
   - Starting yield: {x.xx%} ({date}); anchor percentile: {n}th ({series}, {date})
   - Terms carried forward unchanged: {list}
   - Net real return, recomputed: {x.x–y.y%} over {horizon}
   - Band: {ADD / HOLD / TRIM / EXIT} (from the allocation bands in valuation.md)
   - Weight vs target: {x.x%} vs {y.y%} — drift {z}pp against a {t}pp threshold
   - Vehicle drag vs last assumed: {x}bp vs {y}bp
   - Recommendation: {HOLD/TRIM/ADD/REVIEW/EXIT} — fired by: {band / drift rule / kill switch}
   - Reasoning: {one sentence}
   ```

   The heading token is the hyphenated skill name (`— valuation-check`), matching every other skill's Update-log convention — `decision-log` extracts "most recent valuation-check verdict" by that token. It is the same token on both tiers, so nothing downstream needs to know which tier the position lives in.

8. **Do not overwrite** any prior entries in the thesis. Append only.

## Output

Single recommendation in the format:

```
{TICKER} — current price: $X
Fair value range (last set {date}): $Y – $Z
Position vs midpoint: {X% above/below}
Recommendation: {HOLD/TRIM/ADD/REVIEW/EXIT}
Reasoning: {one sentence}
```

For a fund, the same shape with the fund's own axes:

```
{TICKER} ({ISIN}) — NAV: {x.xx CCY}
Expected net real return (recomputed {date}): {x.x–y.y%} over {horizon}
Band: {ADD / HOLD / TRIM / EXIT}   Weight vs target: {x.x%} vs {y.y%} (drift {z}pp)
Recommendation: {HOLD/TRIM/ADD/REVIEW/EXIT} — fired by: {band / drift rule / kill switch}
Reasoning: {one sentence}
```

If running across the portfolio: a table with one row per name, plus a summary of which names need attention. Funds and companies share the table; the column that would hold a price holds NAV, and the one that would hold a fair value range holds the expected real return range with its horizon.

## Notes

- Never recommend EXIT based on price alone. Exit requires thesis change. "Cheaper than I thought" usually means ADD, not EXIT.
- "Price went up so trim" is fine. "Price went down so panic-sell" is not. The framework exists to prevent the second behavior.
- If the recommendation feels uncomfortable (e.g. ADD on a name that has been falling), trust the system. Re-litigate the thesis if you must, but do it explicitly via `thesis-check`, not implicitly by ignoring the recommendation.
- This skill is most useful precisely when emotions run high. That's when the framework is most valuable.
- On a fund, the emotional trade this skill prevents is a different one. The company failure mode is panic-selling a drawdown; the fund failure mode is abandoning a rebalancing rule because the band says ADD into something that has been falling for a year. The bands table exists so that decision was made once, calmly, in `fund-deep-dive`, and is merely read here.
- **If you act on a `valuation-check` recommendation outside of `portfolio-review`, run `decision-log` to capture the decision in the journal.** The thesis-log append from this skill is not a substitute for the decision log. Standalone valuation-checks don't write to `journal/` by design — keeping the skill lean — so the journal trail depends on you routing through `decision-log` when the result drives action.
