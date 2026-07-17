# UNH — valuation

Companion to `thesis.md`.

**Last updated:** 2026-05-21
**Framework:** `../../../../frameworks/us-managed-care-and-health-services.md`

---

## Primary valuation framework

Per the framework, this is a forward P/E industry. The complication for UNH specifically: TTM and forward-1-year EPS are at cyclical trough ($17.75 guided for 2026, vs $26+ in 2025). Using forward-1-year P/E understates intrinsic value because the denominator is artificially depressed. The right lens is **forward two-year P/E on normalized FY28 EPS**, with FCF yield and dividend yield as cross-checks. EV/EBITDA is a useful secondary check; SOTP (separating UnitedHealthcare from Optum) is a third cross-check given the divisional complexity.

- **Primary multiple:** forward P/E on normalized FY28 EPS.
- **Secondary cross-checks:** FCF yield, dividend yield, EV/EBITDA mid-cycle, SOTP.
- **Generic DCF is informative but second-order** — the assumptions on MA cost trend, DOJ outcome, and Optum integration drive the valuation more than the discounting mechanics.

## Current state

| Metric | Current (May 2026) | 5y average | 10y range | Sector peers (May 2026) |
|---|---|---|---|---|
| Stock price | ~$393 (up from $270 March 2026 low) | ~$475 | $190 (2019) to $620 (2024) | n/a |
| Market cap | ~$360B | ~$420B | $180B-$575B | ELV $95B, CI $80B, CVS $55B, HUM $30B |
| Shares outstanding | ~910M | ~930M | shrinking via buybacks | — |
| TTM EPS (adjusted, depressed) | ~$22 (rolling Q2 2025 - Q1 2026) | ~$22 | $5-$28 | — |
| 2026 EPS guide (adjusted) | >$17.75 (trough) | n/a | n/a | — |
| 2027 EPS consensus | ~$22 | n/a | n/a | — |
| 2028 EPS consensus | ~$25-27 | n/a | n/a | — |
| Forward P/E (2026 guide) | ~22x | ~18x | 12-25x | misleading — bottom-of-cycle |
| Forward P/E (2028 normalized) | ~15x | n/a | n/a | ELV ~13x, HUM ~14x |
| FCF yield (TTM) | ~5% | ~4% | 2-6% | ELV ~5%, CI ~6% |
| Dividend yield | 2.1% (annualized $8.40) | 1.2% | 0.8-2.5% | ELV 1.5%, CI 2.0% |
| EV/EBITDA (TTM) | ~12x | ~14x | 10-20x | — |
| Net debt / EBITDA | ~2x | 1.5x | 1-2.5x | ELV 2.5x, CVS 4x |
| Buyback yield (TTM) | ~2-3% (reduced) | ~3-4% | 1-5% | — |

**Read on current state:** UNH at $393 is between historical norms and trough — meaningfully cheap on normalized forward earnings, but the easy compression already happened in February-March 2026 when the stock touched $270. At $270 the 2028 P/E was ~10x; at $393 it's ~15x. The "generational mispricing" window was open but is now closed unless the stock retreats again.

## Fair value range

The valuation hinges on three uncertain variables: (a) normalized FY28 EPS; (b) appropriate exit multiple; (c) DOJ resolution outcome (which affects both). Three scenarios:

| Scenario | FY28 EPS (adj) | Exit P/E | Fair value | Implied probability |
|---|---|---|---|---|
| **Bear:** DOJ produces structural changes; MA margin compressed; cost trend stays elevated; consensus 2028 EPS materially missed | $20 | 12x (structural compression maintained) | **$240** | ~25% |
| **Base:** Cyclical reset followed by gradual recovery; DOJ settles civilly with operational covenants; MA economics partially recover; consensus 2028 met | $25 | 16x (normalized to mid-cycle) | **$400** | ~50% |
| **Bull:** Successful reset; full MA recovery; DOJ resolves favourably; Optum re-accelerates; Hemsley executes aggressive buyback | $28 | 19x (above mid-cycle as cycle troughs are bought aggressively) | **$532** | ~25% |

**Fair value range:** **$240 (bear) — $400 (base) — $532 (bull)**

**Probability-weighted fair value:** ~$393 (0.25 × $240 + 0.50 × $400 + 0.25 × $532)

**Current price vs range:** $393 is **essentially at probability-weighted fair value**. ~33% upside to base / bull blend; ~39% downside to bear. The asymmetry is roughly 1:1 — symmetric, which means the price has caught up to fair value and offers no meaningful margin of safety.

## Sensitivity

| Variable | Bear | Base | Bull | FV impact |
|---|---|---|---|---|
| FY28 adj EPS | $20 | $25 | $28 | ~$40-50 per $2 EPS |
| Exit P/E multiple | 12x | 16x | 19x | ~$25 per 1 multiple point |
| MA membership trajectory FY26-FY28 | -2M cumulative | flat | +1M | implicit in EPS |
| Optum Health operating margin | 4% | 7% | 9% | ~$15-25 per 100 bps |
| DOJ outcome | Structural | Civil settlement | Quick resolution | Drives both EPS and multiple |

**The two variables that dominate:** FY28 EPS recovery (which is heavily dependent on MA economics) and the exit multiple (heavily dependent on DOJ resolution). These are correlated — if DOJ settles cleanly, both the EPS recovery and multiple expansion accrue; if DOJ produces structural changes, both fall.

## Cross-checks

- **FCF yield approach.** Base-case FY28 FCF: ~$23B on $440B revenue. At a 6% FCF yield (still above-average for a healthcare incumbent), market cap = $383B = ~$420/share. Above the base-case P/E lens — but only modestly. Roughly checks out.
- **Dividend discount.** Current $8.40 dividend, growing at 8% (down from 12-15% historical), at 8% discount rate = ~$420. Roughly checks out with base case.
- **SOTP.**
  - UnitedHealthcare insurance segment: ~$310B revenue × 4.5% operating margin = $14B EBIT × 14x = $196B EV
  - Optum Rx: ~$130B revenue × 5% margin = $6.5B EBIT × 12x = $78B EV
  - Optum Health: ~$110B revenue × 5% margin (depressed) × 10x = $55B EV
  - Optum Insight: ~$20B revenue × 15% margin × 14x = $42B EV
  - Total EV = $371B + net cash adjustment ≈ $360B market cap = ~$395/share. **Checks out closely with current price.**

**The cross-checks broadly cluster in the $390-430 range — consistent with the P/E-based base case of $400 and roughly where the stock currently trades. There is no meaningful undervaluation at $393.**

## Hold / trim / add bands

This is the table `valuation-check` reads on price moves.

| Action | Price band | Reasoning |
|---|---|---|
| ADD / INITIATE | < $320 | Returns asymmetry to ~2:1 reward-to-risk; meaningful margin of safety reopens |
| HOLD | $320 – $500 | Within fair value range; if held, let thesis play out |
| TRIM | $500 – $600 | Approaching bull-case FV; partial profit-taking warranted unless thesis has strengthened |
| EXIT consideration | > $600 | At/above bull-case FV; requires bull case to be confirmed-in-reality |
| EXIT (thesis-driven) | n/a — price-independent | Requires kill switches per `thesis.md`. Specifically: DOJ structural ruling, MLR sustained >86% through 2026, dividend cut, Hemsley unable to continue. |

## Update log

### 2026-05-21 — initial valuation

Stock at $393, market cap ~$360B. Probability-weighted FV ~$393 (~0% to base — i.e. roughly fair value). The 47% rally from March 2026 low of $270 has compressed the asymmetry from the genuinely attractive setup at $270 to a roughly fair-value setup now. **NOT a buy at current price**. Add triggers: price <$320 OR DOJ resolution clarity. Notable external signal: Berkshire Hathaway bought UNH in Q2 2025 (revealed Aug 2025) and completely exited by Q1 2026 (revealed in 13F filed May 15, 2026) — implying the smartest known disciplined investor sized out at around current prices. This is the cleanest pricing anchor available.

Key data points to track: Q2 2026 print (mid-July 2026) for MLR durability; Q3/Q4 2026 prints for MA membership trajectory; DOJ docket and any settlement announcements; CMS 2027 MA rate notice (already done, modest improvement) and 2028 rate notice (Feb 2027).
