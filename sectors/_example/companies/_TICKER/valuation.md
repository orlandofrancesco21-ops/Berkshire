# {TICKER} — valuation

Companion to `thesis.md`. The valuation must use the multiples specified in the relevant industry framework — generic DCF is not the default unless the framework calls for it.

**Last updated:** YYYY-MM-DD
**Framework:** `../../../frameworks/{industry}.md`

---

## Primary valuation framework

Which multiple drives the valuation for this industry, per the framework. Why generic multiples (P/E, EV/EBITDA) may mislead here if applicable.

## Current state

| Metric | Current | 5y average | 10y range | Sector peers |
|---|---|---|---|---|
|  |  |  |  |  |

## Fair value range

**Low:** $X (justification: bear-case multiple × bear-case earnings/NAV/etc.)
**Base:** $Y (justification: base-case multiple × base-case earnings)
**High:** $Z (justification: bull-case multiple × bull-case earnings)

**Current price vs range:** %

## Sensitivity

What variables move the fair value most? Stress-test the 2-3 inputs that matter, not all 20.

| Variable | Bear | Base | Bull | FV impact |
|---|---|---|---|---|
|  |  |  |  |  |

## Cross-checks

Other valuation lenses that should agree. If they disagree materially, understand why before trusting the primary lens.

-
-

## Hold / trim / add bands

This is the table `valuation-check` reads when deciding whether to act on price moves.

| Action | Price band | Reasoning |
|---|---|---|
| ADD | < $X | Below low end of fair value, thesis intact |
| HOLD | $X – $Z | Within fair value range |
| TRIM | > $Z | Above high end without thesis-positive change |
| EXIT | n/a — requires thesis change, not price |

## Update log

### YYYY-MM-DD — initial valuation

(Summary of base case assumptions)
