---
name: valuation-check
description: For a position already held (or a watchlist name), check the current price against the fair value range in valuation.md and produce a clear hold/trim/add/exit recommendation. Reads thesis.md and valuation.md. Use during portfolio monitoring, when tempted to act on price movement alone, or when running a portfolio-wide review. Triggered by "valuation-check X", "should I add to X", "X just dropped Y%, what does the system say".
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

1. **Locate the company files.** Find `sectors/{sector}/companies/{TICKER}/thesis.md` and `valuation.md`. If they don't exist, stop — you can't valuation-check a name without prior analysis.

2. **Check freshness.** Look at the "Last updated" date on `valuation.md`. If it's > 6 months old or there's been a major earnings release since, recommend running `company-deep-dive` to refresh before acting on the recommendation.

3. **Pull current data:**
   - Current price
   - Last 30 days price action
   - Current value of the multiples specified in `valuation.md` (the primary multiple plus cross-checks)

4. **Compare against the saved fair value range:**
   - Current price vs low / base / high from `valuation.md`
   - Current multiple vs sector median (from `kpis.md` if available)
   - Current multiple vs 5y average and 10y range (from the framework)

5. **Has anything in the thesis changed?** Check recent news and the most recent earnings release date. If there's been a material event since the last `valuation.md` update, the recommendation is REVIEW, not a price-based action.

6. **Produce the recommendation:**

   - **HOLD** — price within fair value range, thesis intact, no material change
   - **TRIM** — price > top of fair value range AND no thesis-positive change to justify expanding the range
   - **ADD** — price < bottom of fair value range AND thesis intact
   - **REVIEW** — thesis may have changed; run `thesis-check` first
   - **EXIT** — only if the thesis is broken (this requires explicit judgment, not a price-based trigger)

7. **Append a dated note to `thesis.md`** under the Update log:
   ```
   ### YYYY-MM-DD — valuation check
   - Current price: $X
   - Fair value range: $Y – $Z (last updated: {date})
   - Position vs midpoint: {X}%
   - Recommendation: {HOLD/TRIM/ADD/REVIEW}
   - Reasoning: {one sentence}
   ```

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

If running across the portfolio: a table with one row per name, plus a summary of which names need attention.

## Notes

- Never recommend EXIT based on price alone. Exit requires thesis change. "Cheaper than I thought" usually means ADD, not EXIT.
- "Price went up so trim" is fine. "Price went down so panic-sell" is not. The framework exists to prevent the second behavior.
- If the recommendation feels uncomfortable (e.g. ADD on a name that has been falling), trust the system. Re-litigate the thesis if you must, but do it explicitly via `thesis-check`, not implicitly by ignoring the recommendation.
- This skill is most useful precisely when emotions run high. That's when the framework is most valuable.
