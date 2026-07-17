# NKE — valuation

Companion to `thesis.md`.

**Last updated:** 2026-05-20
**Framework:** `../../../../frameworks/branded-athletic-footwear-and-apparel.md`

---

## Primary valuation framework

Per the framework, this is a P/E + FCF yield industry. Branded athletic footwear is capital-light enough that EBITDA and FCF don't diverge meaningfully, and revenue multiples are uninformative for incumbents at scale. The right lens for Nike is:

- **Forward P/E on normalized (FY28) earnings.** TTM P/E is misleading because TTM earnings are at a cyclical/turnaround low — using TTM understates intrinsic value.
- **FCF yield as the income-style cross-check.**
- **Dividend yield + buyback yield as a "return of capital" cross-check** — for the mature global incumbent like Nike, total return to shareholders is a meaningful sanity check.
- **EV/EBITDA mid-cycle** as a third cross-check.

Generic valuation lenses (DCF, sum-of-parts) are not the primary lens. The brand is the franchise and it's not separately valuable from the operating business.

## Current state

| Metric | Current (May 2026) | 5y average | 10y range | Sector peers (May 2026) |
|---|---|---|---|---|
| Stock price | ~$43 | ~$95 (peak $179 Nov 2021) | $25 (2015) to $179 (2021) | n/a |
| Market cap | ~$63B | ~$140B | $40B-$280B | LULU $30B, DECK $18B, ADS $40B, ONON $15B |
| TTM EPS | $1.53 | $2.85 | $0.85-$3.75 | LULU $14, DECK $5, ADS €3 |
| P/E (TTM) | ~28x | ~33x | 18-50x | LULU 18-20x, ONON ~50x, DECK ~22x, ADS ~25x |
| Forward P/E (FY27 est, ~$2.30) | ~19x | ~28x | 18-40x | ADS ~22x, LULU ~18x |
| Forward P/E (FY28 est, ~$3.10) | ~14x | n/a | n/a | n/a |
| FCF yield (TTM) | ~5% | ~3% | 2-7% | LULU ~5%, ONON ~2% |
| Dividend yield | 3.7% | 1.2% | 0.8-3.7% | ADS 1.5%, PUM 2% |
| EV/EBITDA (TTM) | ~16x | ~22x | 14-30x | LULU ~13x, DECK ~14x |
| EV/Sales (TTM) | ~1.3x | ~3.0x | 1.3-5.0x | LULU ~3x, ONON ~5x |

**Read on current state:** Nike trades at the bottom decile of its 10-year valuation range on every metric except TTM P/E (which is depressed by trough earnings). Dividend yield at 3.7% is the highest since 2009. FCF yield ~5% is near the top of the historical range. The 10-year low EV/Sales of ~1.3x is essentially where the stock traded in 2015 before the 2017-2021 bull run.

## Fair value range

The valuation hinges on what FY28 (fiscal year ending May 2028) normalized earnings look like. Three scenarios:

| Scenario | FY28 EPS | Multiple | Fair value | Implied probability |
|---|---|---|---|---|
| **Bear:** Turnaround stalls; GM stuck at 40-41%, China declines persist, insurgent share loss continues | $2.00 | 14x (down from current 19x as franchise narrative breaks) | **$28** | ~25% |
| **Base:** Wholesale rebuild works, GM recovers to 44-45%, operating margin to 11%, China stabilises at -5% growth | $3.10 | 20x (modest re-rate as turnaround validates) | **$62** | ~50% |
| **Bull:** Hill turnaround compounds, Jordan and basketball lead a brand-heat recovery, GM back to 46%+, China returns to growth | $3.80 | 24x | **$91** | ~25% |

**Fair value range:** **$28 (bear) — $62 (base) — $91 (bull)**

**Probability-weighted fair value:** ~$60.75 (0.25 × $28 + 0.50 × $62 + 0.25 × $91)

**Current price vs range:** $43 is ~31% below the probability-weighted fair value, and ~12% above the bear-case fair value.

## Sensitivity

The 2-3 inputs that matter:

| Variable | Bear | Base | Bull | FV impact |
|---|---|---|---|---|
| FY28 gross margin | 41% | 44.5% | 46.5% | ~$8 per 100 bps on FY28 EPS, ~$15-20 per 100 bps on FV |
| FY28 revenue ($B) | $48 | $54 | $58 | ~$5 per $2B revenue at constant margin |
| Greater China revenue (FY28, $B vs FY22 peak $7.5B) | $4.5 | $5.5 | $6.5 | ~$3-5 per $1B on FV (China is highest-margin region) |
| Exit P/E multiple | 14x | 20x | 24x | ~$3 per 1 P/E turn on FV |

**The two variables that dominate:** FY28 gross margin and the exit multiple. These two together account for ~70% of the spread between bear and bull. The narrative ("structural brand impairment" vs "successful turnaround") drives both — they're correlated, not independent.

## Cross-checks

Other valuation lenses that should agree:

- **FCF yield approach.** Base-case FY28 FCF: ~$5.5B on $54B revenue at 10% FCF/sales. At a 6% FCF yield (reasonable for a mature brand growing low-single-digits), market cap = ~$92B = ~$66/share. Slightly above the P/E-based base case of $62 — checks out.
- **EV/EBITDA mid-cycle.** Mid-cycle EBITDA in the base case: ~$8B (operating income ~$6B + D&A ~$2B). At 15x EV/EBITDA (historical mean), EV = $120B; less ~$0 net debt = market cap ~$120B = ~$85/share. Higher than the P/E base case — but 15x is mid-cycle peak, not depressed turnaround. At 12x EV/EBITDA, $96B = ~$68/share. Roughly checks out.
- **Dividend discount approach (sanity check, not primary).** Current dividend ~$1.60/share growing at 6% perpetuity discounted at 8% = ~$80. Sensitive to growth/discount assumptions but suggests fair value north of current price.
- **Sum-of-parts (not appropriate here).** The brand is the business; not separable.

The cross-checks broadly agree on a fair value range centred in the $60s. The bear case at $28 is the genuinely-pessimistic scenario and not what cross-checks suggest is fair if the company executes the turnaround within the typical 3-year window.

## Hold / trim / add bands

This is the table `valuation-check` reads on price moves.

| Action | Price band | Reasoning |
|---|---|---|
| ADD | < $38 | Approaches bear-case fair value; asymmetry becomes very favourable (5-7% downside vs 60%+ upside to base) |
| HOLD | $38 – $65 | Within fair value range; let thesis play out |
| TRIM | $65 – $80 | Approaching/exceeding base-case FV; partial profit-taking warranted unless thesis has strengthened |
| EXIT consideration | > $85 | At/above bull-case FV; requires bull case to be confirmed-in-reality, not just narrative |
| EXIT (thesis-driven) | n/a — price-independent | Requires thesis kill switches per `thesis.md`. Specifically: GM <40% sustained 3Q, op margin <8% sustained 4Q, OR a material adverse cultural-permission signal (athlete defection, sell-through collapse, China -25%+) |

## Update log

### 2026-05-20 — initial valuation

Stock at $43. Probability-weighted FV ~$60.75. Base case $62 implies +44% upside over 2-3y as turnaround validates and multiple expands from 19x forward FY27 to 20x forward FY28; bear case $28 implies -35% on persistent brand erosion; bull case $91 implies +112%. Asymmetry ~2:1 reward-to-risk, supportive of starting position but not exceptional. Most sensitive to FY28 gross margin trajectory and exit multiple — both driven by the same underlying narrative about brand health. Key data points to track: Q4 FY26 print (late June 2026) for full-year wholesale data; Q1 FY27 print (Sep 2026) for the cleanest first quarter under the "Win Now" plan.
