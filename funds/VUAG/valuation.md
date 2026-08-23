# VUAG — expected return

Companion to `thesis.md`. **This file is canonical for this fund's return scenarios per VAL-P5.**

**Last updated:** 2026-08-23
**Horizon:** **10 years** (the only horizon at which the S&P 500's valuation anchor has measurable predictive power; it says almost nothing at 1–3 years).
**Vehicle lens:** `../../frameworks/etf-vehicle-mechanics.md`
**Exposure lens:** `../../frameworks/sp500.md`

---

## Starting point

| | | Source |
|---|---|---|
| Price / NAV | 108.88 GBP (VUAG.L market price; NAV struck in USD) | yfinance, 2026-08-22 [verified] |
| Premium / discount to NAV | ~flat — not separately established; VUAG is deeply liquid and trades near iNAV | [partial] |
| Valuation anchor | **Shiller CAPE (P/E10)** — the anchor `frameworks/sp500.md` says has 10-year predictive power (R² 0.43) | `library/shiller-ie-data.md` |
| Anchor vs its own history | **~41, the 99th percentile** of the 145-year record; just below the 1999–2000 all-time-high cluster (43.2–44.2) | `library/shiller-ie-data.md`, 2026-08 [verified] |
| Dividend / distribution yield | ~1.2–1.3% gross (accumulated, not paid out); net of 15% US WHT ≈ 1.06% received | [partial — S&P factsheet queued] |

**What the anchor is worth here.** CAPE explains ~43% of 10-year-ahead real return variation and ~12% at 1 year — it is a decade instrument, not a timing tool. Critically, **it ranks decades well and levels them badly** (correlation 83–91%, but post-1985 out-of-sample level errors worse than the trailing average): use it to say this decade is likely worse than average, never to name the number. At today's 99th-percentile reading the anchor is at its *most* informative (signal concentrates in the tails), and what it says is that the record holds no good decade from a start this expensive. Per VAL-T2 this could be genuine expensiveness *or* a structural level-shift in CAPE's mean (accounting, buybacks, ~⅓ tech) — indistinguishable on the chart, so the base case is set conservatively and the bull case carries the "structural" reading.

## Expected return, decomposed

10-year annualised, **USD, real, before personal tax**. Terms move together across scenarios per VAL-P4 (a bear multiple is paired with bear growth, not cherry-picked). Each term is separately arguable and separately sourced.

| Term | Bear | Base | Bull | Basis |
|---|---|---|---|---|
| Starting yield (gross shareholder yield) | +2.3% | +2.8% | +3.3% | ~1.25% dividend [partial] + net buyback yield ~1.0/1.5/2.0% [unverified — no sourced series] |
| Real growth (real EPS/share) | +1.0% | +1.75% | +2.5% | Ibbotson–Chen US 1926–2000 base 1.75pp [verified]; bounded per `frameworks/sp500.md` |
| Valuation change | −5.0% | −2.0% | 0.0% | CAPE 41 → ~25 (bear) / ~33 (base) / holds (bull) over 10y. Reversion assumed *partial* within horizon |
| **Gross real return** | **−1.7%** | **+2.5%** | **+5.8%** | |
| Less: vehicle drag | −0.18% | −0.18% | −0.18% | Realised TD vs the *gross* index [computed from primary TD table + WHT]; the near-certain term |
| **Net-of-wrapper real (pre-tax)** | **−1.9%** | **+2.3%** | **+5.6%** | |
| Probability | 30% | 45% | 25% | Argued from the 99th-percentile start and the five-worst-starts record, not asserted |

**Probability-weighted net-of-wrapper real return: ≈ +1.8% per year over 10 years, pre personal tax.**
(0.30 × −1.9 + 0.45 × +2.3 + 0.25 × +5.6.)

**Cross-check against the empirical conditional record (VAL-P3 independence).** The absorbed Shiller file's *most-expensive CAPE quintile* delivered a 10-year forward real median of **+4.8%** (range −5.9% to +13.1%) [verified]. That quintile spans CAPE 18–44, so its median reflects *less* extreme starts than today's 41; conditioning tighter — the five most expensive starts ever were **all negative** (−2.55% to −4.59%) — pulls the honest centre **below** the quintile median and toward this table's base. The decomposition (+2.3%) is the more conservative lens; per VAL-P3, where two lenses diverge, the file names the conservative one rather than averaging. **These are two partially-independent reads (bottom-up terms vs empirical CAPE-conditioning) that bracket a modest, possibly-negative decade.**

**The vehicle drag, stated as its own line because it is the certain part.** ≈ **0.15–0.22%/yr** all-in vs the gross index (TER 0.07% + ~0.19% unrecovered US WHT − a few bp securities lending). Every other line in the table is a forecast with a wide distribution; this one is deducted whether the market rises or falls, and it is why the wrapper choice (VUAG vs the 0.03% SPYL vs the synthetic Invesco) is worth the research even though it moves the answer by only tens of basis points. Note the sign trap resolved in the thesis: the fund is *positive* against its stated NTR benchmark and mildly *negative* against the true gross index.

## Tax — a return driver, not an appendix (German resident, EUR base)

**This is research, not advice; the specifics need Francesco's *Steuerberater* to confirm.** Statutory figures pulled from the vehicle lens (which read the statute) and labelled accordingly.

- **Teilfreistellung 30%.** VUAG is an Aktienfonds (85% contractual equity quota [verified]), so 30% of income and gains are tax-free for a private investor. With Abgeltungsteuer 26.375%, the effective rate is ≈ **18.46%** of the *nominal* taxable amount [partial — statute read, rate arithmetic verified].
- **Vorabpauschale (accumulating wrapper).** For 2026: 0.70 × 3.20% Basiszins = 2.24% deemed base, less 30% = 1.568% taxable, × 26.375% ≈ **0.41% of start-of-year value**, owed in cash in Jan-2027 **with no distribution to fund it** [verified via the vehicle lens's reading of §18 InvStG + the 2026 BMF letter]. Crucially it is a **prepayment credited in full at disposal** (§19 InvStG), so the permanent cost is only the *time value* of paying early — **not** a recurring 0.41%/yr drag. Modelling it as an annual expense overstates it.
- **Why it belongs in the ranking:** the 18.46% effective rate applies to the *nominal* gain, so at 2.9% inflation it takes a larger bite of the *real* return than the headline suggests. Illustratively, on the base-case ~+2.3% real pre-tax (~+5.3% nominal), ~18.46% of the nominal gain ≈ **−1.0pp**, leaving an after-tax real base of **roughly +1.3%/yr** [illustrative, unverified — depends on holding period, the Basiszins path, and the €1,000 Sparer-Pauschbetrag]. The honest headline is the **pre-tax range above plus this mechanism**, not a single invented after-tax number.

## What the historical record says from here

The wealth-manager section — the reason the vault stores this. Computed natively on the S&P 500's own series (`scripts/exposure-history.py`, run 2026-08-23; the sp500 exposure is the one case where the long proxy *is* the exposure, so these are not a geographic substitution — only USD-not-EUR and price-only-pre-1980 caveats apply):

- **10-year annualised REAL total return** (VFINX, 1980–2026, CPI 2.9%, ~4.7 independent windows): worst **−7.3%**, p10 +0.7%, median **+8.9%**, p90 +13.0%, best +16.5%; **9% of windows ended below zero**.
- **Deep price-only history** (`^GSPC`, 1927–2026, ~9.9 windows, no dividends): worst 10y nominal −10.0%, median +7.5%; 11% below zero. Read for breadth/shape, not level.
- **These are overlapping windows, not independent observations**, and the real series is only ~4.7 independent 10-year windows — the distribution is thinner than the window count implies. The valuation-conditional read (what followed *from CAPE ~41 specifically*) is **not** in this script; it is supplied by `library/shiller-ie-data.md` (five-worst-starts all negative; most-expensive-quintile median +4.8%), which is why that source, not memory, carries the conditional claim.

**Drawdown record — the numbers that decide survivability** (nominal from the feed; real recoveries per the sp500 framework):

| Episode | Depth | Recovery |
|---|---|---|
| 1929 Depression (price only) | **−86.2%** | ~25y nominal price; ~15.5y in real total return |
| GFC 2007–09 (total return) | **−55.3%** | 4.9y |
| Dot-com 2000–02 | −47.5% | 6.1y |
| 1973–74 (price only) | −48.2% | 7.5y |

## Alternatives

An allocation is always against something.

| Alternative | Expected real (pre-tax, 10y) | Note |
|---|---|---|
| **Cash / dry powder** (the money's current home) | ~0 to +1% real if short rates > inflation | The base case clears cash, but by less than the historical equity premium — the extremeness of the start is the whole reason |
| **Nominal government bonds** | ~0.9% real long-run (verified via sibling), but starting yield is a far tighter predictor | Better if the horizon shortens or the drawdown table is unaffordable |
| **MSCI World / developed** (`developed-market-equity.md`) | Adds 28% ex-US; dilutes the US concentration and the 100% USD | The direct diversification alternative to *this* concentration |
| **Other S&P 500 wrappers** | Same exposure; the difference is drag | SPYL 0.03% (−~4bp/yr vs VUAG); Invesco synthetic (higher realised, more risk); CSPX a wash — see thesis peer table |

A fund whose expected real return does not clear cash plus a risk premium is not an allocation. VUAG's base case clears cash but the margin is thin — which argues for *sizing*, not *avoiding*.

## Allocation bands

Keyed to expected return and valuation percentile, not price (a fund has no fair value). `valuation-check`'s fund branch reads these mechanically against the recomputed net real return and drift-from-target.

| Action | Trigger | Reasoning |
|---|---|---|
| **ADD / INITIATE** | Expected net-of-wrapper real return above ~+4%/yr (10y), **or** CAPE back below ~28 (≈ below the ~75th percentile) | Below that valuation the forward distribution's centre lifts materially; today's ~41 does **not** meet this |
| **HOLD** | Expected net real between ~0% and ~+4%, CAPE 28–42 — **today's state** | Own as core beta, rebalance to target on drift; do not add aggressively at a 99th-percentile start |
| **TRIM / REBALANCE** | Drift beyond ~±5pp from target weight | Rebalancing is a rule, not a view (ASYM) |
| **EXIT** | An **exposure-level** kill switch (leave US large-cap) or a **vehicle-level** switch with no better wrapper available (switch funds) — see thesis. Never a price level or CAPE reading alone (ASYM-P1) | Exit is by thesis change, never by the quote |

## Update log

### 2026-08-23 — initial

Initial expected-return build. 10-year, USD, real: bear −1.9% / base +2.3% / bull +5.6% net-of-wrapper pre-tax, probability-weighted **≈ +1.8%/yr** — a deliberately sober number reflecting a 99th-percentile CAPE start. Decomposition (conservative) brackets the empirical Shiller conditional (+4.8% most-expensive-quintile median) from below; both point to a modest, possibly-negative decade. Vehicle drag ~0.15–0.22%/yr, the one near-certain term. Tax mechanism (30% Teilfreistellung → ~18.46% effective; Vorabpauschale a prepayment not a drag) stated with the pre-tax range as the honest headline. Allocation bands put today in **HOLD** (own as core beta, don't add aggressively here); ADD trigger needs CAPE < ~28 or expected real > ~+4%. All figures rest on a v1 `frameworks/sp500.md` bootstrapped in the same run — re-check on its first hand-refinement.
