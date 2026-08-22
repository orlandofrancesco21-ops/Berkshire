# {TICKER} — expected return

Companion to `thesis.md`. **This file is canonical for this fund's return scenarios per VAL-P5** — any range quoted elsewhere reconciles to the table below or declares itself a different object.

**Last updated:** YYYY-MM-DD
**Horizon:** {10 years — state it explicitly; a valuation anchor that works over a decade says almost nothing about a year}
**Vehicle lens:** `../../frameworks/etf-vehicle-mechanics.md`
**Exposure lens:** `../../frameworks/{exposure-slug}.md`

<!--
A fund is not cheap or expensive the way a company is. You cannot buy it below
intrinsic value, and there is no management team to close the gap. The only
honest question is: what real return does this exposure plausibly deliver over
my horizon, what does the wrapper take off that, and does the remainder beat the
alternatives by enough to justify the allocation?

So the output is an expected REAL return range, decomposed so each term can be
argued and falsified separately. Never a single number (VAL-P1).
-->

---

## Starting point

| | | Source |
|---|---|---|
| Price / NAV | {x.xx CCY, YYYY-MM-DD} | |
| Premium / discount to NAV | {x.xx%} | |
| Valuation anchor | {CAPE / P/E / earnings yield / yield-to-maturity — whichever the exposure framework says has predictive power for this asset class} | |
| Anchor vs its own history | {percentile, over what window} | |
| Dividend / distribution yield | {x.xx%, gross or net — say which} | |

**What the anchor is worth here.** {The exposure framework's honest read on this anchor's track record: the horizon at which it has explanatory power and the horizon at which it does not, with the counter-case stated. For equities, starting valuation explains a meaningful share of 10-year real returns and very little of 1-3 year returns. For bonds, starting yield is a far stronger predictor. Do not treat "valuation" as one thing across asset classes.}

## Expected return, decomposed

Each term is separately arguable and separately wrong. That is the point of decomposing rather than quoting one number.

| Term | Bear | Base | Bull | Basis |
|---|---|---|---|---|
| Starting yield | | | | {the one term that is nearly known today} |
| Real growth | | | | {per share, not aggregate — dilution and buybacks are the difference} |
| Valuation change | | | | {mean-reversion assumption, and over what period; state whether it is assumed to complete within the horizon} |
| **Gross real return** | | | | |
| Less: vehicle drag | | | | {realised tracking difference, not TER — see below} |
| Less: tax drag | | | | {withholding + local treatment; verify with a tax adviser} |
| **Net real return to me** | **{x.x%}** | **{y.y%}** | **{z.z%}** | |
| Probability | {%} | {%} | {%} | {argued, not asserted} |

**Probability-weighted net real return: {w.w%} over {horizon}.**

**The vehicle drag, stated as its own line because it is the certain part.** {TER vs the realised tracking difference over N years; spread on entry; tax. The wrapper's cost is nearly deterministic while every other line is a forecast — which is why it deserves disproportionate research effort and why a basis-point difference compounds into real money over a decade.}

## What the historical record says from here

{The wealth-manager section, and the reason the vault stores this at all. From comparable starting valuations, what did this exposure actually deliver? Rolling real returns over the horizon, the distribution rather than the average, and the worst realised outcome. Then the drawdown record: depth, duration, and time-to-recovery — the numbers that decide whether an allocation is survivable rather than merely attractive.}

{`python scripts/exposure-history.py {TICKER}` computes the realised distribution from available price history. It cannot compute the valuation-conditional relationship, which needs long-horizon data the vault must ABSORB as a source rather than remember — name the source and queue it in sources.md if it is not yet in library/.}

## Alternatives

{An allocation is always against something. What else buys this exposure (other funds, direct holdings), and what else could hold the same money (cash at the current risk-free rate, bonds at their starting yield, an existing position). A fund whose expected real return does not clear cash plus a risk premium is not an allocation, whatever its narrative.}

## Allocation bands

Keyed to expected return and valuation percentile, not to price. Price bands are a company construct.

| Action | Trigger | Reasoning |
|---|---|---|
| **ADD / INITIATE** | {expected net real return above {x}%, or anchor below {n}th percentile} | |
| **HOLD** | {band} | |
| **TRIM / REBALANCE** | {band, or drift beyond {x}pp from target weight} | {rebalancing is a rule, not a view} |
| **EXIT** | exposure-level kill switch, or a vehicle-level switch with no better wrapper available | Never a price level alone (ASYM-P1) |

## Update log

### YYYY-MM-DD — initial
