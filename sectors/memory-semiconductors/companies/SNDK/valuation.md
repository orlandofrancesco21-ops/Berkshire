# SNDK — valuation

Companion to `thesis.md`. **This file is canonical for SNDK's scenario numbers per VAL-P5** — any range quoted elsewhere reconciles to the table below or declares itself a different object.

**Last updated:** 2026-08-22 (refresh; initial valuation 2026-07-30)
**Framework:** `../../../../frameworks/memory-semiconductors.md`
**Sector:** `../../primer.md`

**Data sourcing:** price and market data from yfinance pulled 2026-08-21 22:36-22:41 UTC (close of 2026-08-21), USD, per "Price and data sourcing (canonical)". Company figures from the FY2026 10-K (filed 2026-08-17, KPMG unqualified), the Q4 FY2026 8-K and earnings deck (2026-08-05), and the Q3/Q4 FY2026 earnings-call transcripts (fool.com, cross-checked against a second host), all read directly — `verified`. The Investor Day (2026-08-13) rests on the official press release plus secondary coverage — `partial`; its full transcript exists only behind Seeking Alpha's paywall. Consensus from yfinance analyst tables, 2026-08-21.

---

## Primary valuation framework

**Distributions received plus a terminal multiple on normalized earnings — a method change from the initial valuation, forced by a disclosed policy.**

The 2026-07-30 valuation anchored on *forward tangible book*: the peak year's earnings compound the book, and a trough multiple on that bigger book floors the value. That construction assumed retention. On 2026-08-13 management committed to returning **100% of excess cash** (Investor Day release, `verified` from the official PR), and in fiscal Q4 it executed $4.5bn of buyback at an average ~$1,512/share (10-K) — roughly **20x tangible book**. Under full payout via repurchase far above book, forward tangible BVPS does not compound; it *shrinks* (equity falls by dollars spent while the share count falls by only dollars-over-price). The peak year now reaches the owner as distributions, not as book. So the anchor becomes: **PV of the distributions the peak years deliver, plus a terminal value at a normalized multiple once the cycle (or its absence) is revealed.** Forward tangible book survives as the bear-case floor input, not as the primary lens.

P/E remains without a valid domain at either end of the cycle (VAL-T1): trailing 21.6x and forward 7.45x on FY2027 consensus are the same peak, quoted twice.

**The trough anchor, now verified — and corrected.** The prior file applied Micron trough P/B of 0.81x / 0.97x / 1.32x with decimal precision while labelling the series unverified. It has now been recomputed from primary filings and unadjusted price history (EDGAR XBRL + yfinance, 2026-08-22):

| Trough | Price basis | Equity basis | P/B | P/TBV |
|---|---|---|---|---|
| MU 2016-02-11 | close 9.69 / low 9.45 | Q1 FY2016 10-Q | **0.80-0.82** | 0.84-0.86 |
| MU 2019 (Jan/May lows) | close 31.00-32.61 | Q1/Q2 FY2019 10-Qs | **~1.03** | ~1.08 |
| MU 2022-12 (actual cycle low) | close 48.43-48.88 | FY2022 10-K / Q1 FY2023 10-Q | **~1.06-1.07** | ~1.10 |
| SNDK 2025-04 (its own standalone low) | close 29.62 / low 27.89 | 10-Q q/e 2025-03-28 | 0.44-0.47 | **~0.97-1.03** |

The prior 0.97x (2019) and 1.32x (2023) do not reproduce from any trough price against any adjacent balance sheet; the rising staircase was a data artifact. The prior file's "40.10" SNDK price appears to be back-solved from a 1.4x-tangible claim rather than traded. **The defensible floor evidence is: memory bottoms near 1.0x book (tangible ~1.0-1.1x), with one 0.8x episode in 2016.** The bear case below uses 1.0x tangible.

## Current state

| Metric | Current (2026-08-21) | Notes |
|---|---|---|
| Price | **1,596.08** | official close; +24.7% vs the 2026-07-30 close of 1,279.96. Realized vol ~140% annualized — any single close is a noisy anchor |
| Market cap | $233.7bn | 146,419,001 shares (10-K cover, 2026-08-07; yfinance agrees exactly) |
| Enterprise value | **~$228.9bn** (hand: cap − $4,762M cash + $0 debt) | vendor field now within 0.4% — but hand-compute remains the rule here |
| Trailing P/E | 21.6x | FY2026 GAAP EPS $73.76 — meaningful for the first time |
| Forward P/E | **7.45x** on FY2027 consensus $214.10 | the vendor's forwardPE of 6.03x is the **FY2028** mean ($264.72) — label carefully; a prior vault note misread it as FY2027 |
| P/B / P/TBV | 14.85x / **21.8x** | equity $15,736M; TBV $10,742M ($73.36/sh) after stripping $4,994M goodwill |
| EV / FY2026 revenue | 11.3x | revenue $20,248M (+175%; note FY2026 was a 53-week year) |
| EV / FY2026 GAAP EBIT | 18.5x | EBIT $12,389M — first profitable year after FY2023-25 losses |
| EV / Q4-annualized EBIT | **8.1x** | Q4 EBIT $7,037M × 4 = $28.1bn — the multiple the bulls are actually quoting |
| FY2027 consensus | rev $48.96bn, EPS $214.10 (20 analysts, $187-238) | essentially unchanged since 07-30 ($212.95); the June-July revision wave has stopped |
| FY2028 consensus | EPS $264.72 (19 analysts, **$173-361**) | this is where post-Investor-Day upgrades landed; the spread is the debate |
| Street targets | mean $2,126, median $2,100 (23 analysts) | = 9.9x FY2027 / 8.0x FY2028 consensus EPS |

**Balance-sheet and cash-flow reads that bound everything below (all 10-K, `verified`):** cash $4,762M, zero debt, revolver undrawn. FY2026 FCF of $11,494M **overstates steady state**: ~$4.0bn of OCF was NBM customer deposits/advances (+$1,374M refund liabilities, +$1,217M contract liabilities) and unpaid taxes (+$1,370M payable). Cash taxes paid were $146M against $1,584M of expense — a **~$1.4bn tax catch-up is due in FY2027**, and the company expects to be subject to 15% CAMT from FY2027. The Nanya stake contributed an $808M unrealized non-operating gain to FY2026 net income.

## Fair value range

The valuation turns on one question with two dates: **does the NBM floor regime survive its first tested downturn** — and the first test cannot arrive before the spot half of the book rolls, which TrendForce's standing forecast places in 2H27 (supply outgrowing demand in 2027) while management claims allocation "beyond calendar year 2027". What is now *verified* about the regime (Q4 call + 10-K): floors and ceilings exist; **>50% of FY2027 bits and ~2/3 of FY2028 bits are committed**; RPO $59.8bn entirely NBM, $91.1bn including two post-quarter signings; NBM gross margin "around 80%" (CFO, Q&A). What is **not** verified: the floor level (disclosed nowhere, including the audited 10-K, which never uses the word "floor"); and the guarantee cushion — the deck's $16.5bn against the 10-K's identifiable $5.0bn third-party collateral (accessible only on default) + $1.5bn refundable deposits + $1.24bn advances, with the risk factor conceding guarantees "may not fully offset" lost revenue and disclosing **no renegotiation mechanics at all**.

Method per scenario: PV of distributed peak-year earnings (the 100%-payout policy makes distributions the carrier), plus a terminal multiple on normalized EPS once the regime is revealed, discounted ~2 years at 10% (owner convention). Share count 146.4M drifting to ~143-145M on continued repurchase. Normalized-EPS builds are stated inline — per VAL-M1 the "normal" assumption *is* the valuation.

| Scenario | The story, and the build | **Fair value** | Prob. |
|---|---|---|---|
| **Bear** — the floor level proves low and the regime partially fails its first test: spot half rolls from FY2027 H2 (TrendForce crossover; YMTC's third fab in production), one or more NBM customers dispute or renegotiate rather than eat above-market floors, FY2028 spot gross margin goes negative. FY2027 EPS ~$150 (below the lowest of 20 estimates — the bear assumes what no analyst models, as before), ~$130 distributed; FY2028 ~$40. Normalized: revenue ~$22bn at ~40% GM → EPS ~$43; terminal 9x = ~$390. PV ≈ $155 distributions + $320 terminal | **$475** | 30% |
| **Base** — the floors hold as written through the first downturn but the cycle still cycles above them: FY2027 EPS ~$190 (Q1 guide $44-46 annualizes to ~$180; consensus $214 assumes no H2 fade), FY2028 ~$150. Normalized: revenue ~$30bn at ~50% GM (the NBM half at ~80% floors the blend far above the pre-NBM 35-45% normal) → EPS ~$80; terminal 9x = $720. PV ≈ $280 distributions + $595 terminal | **$875** | 45% |
| **Bull** — the FY2028-30 model is real: ~80% GM sustained, mid-teens bit growth, ~50% FCF margin, all of it returned. FY2027 $214, FY2028 $265 delivered; normalized EPS ~$220 at 10x = $2,200 terminal. PV ≈ $390 distributions + $1,820 terminal. Note what this is: **our bull now sits almost exactly at the street's mean target ($2,126)** — the market's base case is our regime-change case | **$2,200** | 25% |

**Fair value range: $475 (bear) — $875 (base) — $2,200 (bull). Probability-weighted: ~$1,090.**

**Current price vs range:** 1,596.08 = 3.4x bear, 1.8x base, **1.46x probability-weighted**, 0.73x bull. Upside to base: **−45%**. Upside to bull: **+38%**. Downside to bear: **−70%**. On ASYM-P2's standardized basis — upside to base over downside to bear, from the current price — the numerator is **still negative**. The verdict logic is unchanged even though every case moved up.

**Why the whole table moved up from $200/$400/$1,560 — two drivers, separated honestly.** (1) *Facts*: the floor disclosure (the exact event the old sensitivity table said moves the bear most), the ~80% NBM margin confirmed in Q&A, >50%/two-thirds bit coverage, a Q1 FY2027 guide whose midpoint annualizes to ~$180 of EPS, and Kioxia reaffirming capex discipline. (2) *Method*: the switch from retained-forward-book to distributions-plus-terminal, forced by the payout policy — under the old method the same base assumptions would have produced roughly $300-400, so **roughly half the base-case increase is method, not evidence**. Stated per PROD-P1 so the next refresh can grade which driver aged well.

**The weights, argued rather than asserted this time.** Bear 40%→30%: the single event the old bear most feared (no floors at all) is off the table — but only the floor's *existence* is verified, not its level, and not its survivability; YMTC is adding bits before 2029 from outside the discipline club; Q4 2026 contract-price momentum is converging (TrendForce). Base 40%→45%: the contracted book now carries the base case mechanically for two fiscal years. Bull 20%→25%: zero of eight bull-side kill switches fired at the print; Kioxia chose a buyback over fabs; but the bull still requires a nine-time-repeating cycle not to repeat, on contracts younger than two years, with the floor level a secret — 25% is as far as unverified "attractive margins" can carry it.

## Sensitivity

| Variable | Bear | Base | Bull | FV impact |
|---|---|---|---|---|
| **Floor level** (undisclosed) | low; renegotiated in the downturn | holds; blend floors GM ~50% normalized | holds with upside capture | **dominant, binary, and still invisible.** Its disclosure date is unknown; its first market test arrives with the spot roll |
| **Normalized EPS** (post-regime-reveal) | ~$43 | ~$80 | ~$220 | ~$9 of FV per $1 of normalized EPS at 9x through the terminal |
| **Terminal multiple** | 9x | 9x | 10x | each 1x on the base = ~$65 of FV; the bear's floor cross-check is 1.0x tangible book (~$73/sh), which a 9x multiple on $43 sits comfortably above |
| **FY2027 delivery vs guide** | $150 | $190 | $214+ | secondary — ~19% of RPO (~$11.4bn) is already scheduled into FY2027 revenue; the year is substantially pre-sold |

## Cross-checks

- **(1) Implied expectations, solved backwards — now with tax** (the prior version was computed at zero tax, overstating implied EPS 15-21%). At EV $228.9bn: 8x EV/EBIT requires permanent EBIT of $28.6bn — **almost exactly Q4 FY2026 annualized ($28.1bn), forever** — i.e. permanent EPS of $154-166 at 15-21% tax. 10x requires $123-133. 12x requires $103-111. FY2027 consensus ($214) sits above every cell, which is the cleanest possible statement that the market is pricing cycle *duration*, not next year's number. Against my normalized builds: the price sits between the base ($80) and bull ($220) normals — consistent with the 1.46x PWFV reading.
- **(2) Trough tangible book as the bear floor.** 1.0x current TBVPS is ~$73. The bear case's terminal ($390) sits far above it because even a partially-failed NBM regime is assumed to leave normalized earnings positive; a bear that assumes *full* regime failure and a classic trough would revisit ~$75-150. That worse-than-bear case is real but requires the floors to be near-worthless — assigned to the tail inside the 30%, not modelled separately.
- **(3) The street, as a datapoint about the argument.** Mean target $2,126 = 9.9x FY2027 / 8.0x FY2028 consensus. The sell side is not arguing for a re-rating; it is arguing the peak is the new normal — same debate as 07-30, one leg higher. The tell that conviction there is thinner than the targets suggest: three firms **cut** targets into the post-print selloff on 08-06 (Citi 2500→2100, Evercore 3100→2800, Wells 1620→1400) before the Investor Day reversed sentiment (+22% in two sessions).
- **Do the lenses cluster? No.** $475 to $2,200 is a 4.6x spread against VAL-P3's ~1.33x tolerance — better than July's 7.8x, still a recorded failure. The conservative lens is the bear construction (distributions plus 9x on normalized-down earnings): it is the only one whose key input (memory bottoms near 1.0x book; NAND LTAs have never survived a tested collapse) rests entirely on verified history rather than on management characterizations.

## Hold / trim / add bands

**There is no position** — the verdict remains PASS. Bands describe the range, not an endorsement.

| Action | Price band | Reasoning |
|---|---|---|
| **ADD / INITIATE** | **< $875**, with conditions | At or below base-case fair value, and only with: (a) the floor LEVEL disclosed, or one full quarter of MD&A data showing ASP/GB down with gross margin held (the floor observed working); (b) no NBM dispute or renegotiation disclosed; (c) first tranche 1-2% per ASYM-T2 and the framework's memory cap |
| **HOLD** | $875 – $2,200 | Inside a range that fails VAL-P3's cluster tolerance by 4.6x — this band carries limited information. At 1,596.08 the stock is inside it and the verdict is still PASS, because upside to base is −45% |
| **TRIM** | > $2,200 | Above a bull case that already assumes the cycle is abolished |
| **EXIT** | n/a — price-independent | Kill switches per `thesis.md` only (ASYM-P1) |

**Current price 1,596.08 (2026-08-21) → do not initiate.** Reward-to-risk on the standardized basis is negative. The distance to a defensible entry is no longer 70% (it was, in July); it is ~45% plus one disclosure. That is what three weeks of verified facts bought.

## Update log

### 2026-07-30 — initial valuation

Price 1,249.44 USD (yfinance, 2026-07-30 18:37 local), one session off a 1,015.89 capitulation low struck 2026-07-29 after a 56.5% peak-to-trough fall in 34 calendar days from 2,335.00 on 2026-06-25, then +23.4% in a single session. **The reference price is not a settled level and this band is written against a violently two-way tape** — that is a stated limitation of every percentage on this page, not a caveat.

Primary lens is price to *forward* tangible book per the framework, because at a memory peak the trailing book is a stale denominator in the opposite direction from the usual trap and P/E has no valid domain at either end of the cycle. Fair value **$200 / $400 / $1,560**, probability-weighted **~$552** at 40/40/20. Price sits at 6.2x bear, 3.1x base, 2.3x PWFV, 0.80x bull. Reward-to-risk on ASYM-P2's standardized base-over-bear basis is **negative**.

Cross-checks fail VAL-P3's cluster tolerance by 7.8x and the failure is recorded rather than averaged; normalised mid-cycle earnings is named the conservative lens. The framework's EV/replacement-cost anchor is **unavailable for this name** — SanDisk has $649M of net PP&E, no fab, and 49.9% of equipment inside buildings Kioxia owns — which removes the one lens that has historically caught memory at a bottom and is the reason the bear case cannot be floored on assets.

Three vendor-data corrections applied before anything was built: enterprise value recomputed at ~$181.5bn against a reported $146.9bn (~24% understatement flowing through every EV multiple); the "impossible" 69.98% operating margin resolved as a latest-quarter normalised figure quoted against a trailing-twelve-month gross margin, reconciling to four significant figures with the filed GAAP margin at 69.1% and **no JV income involved**; and the vendor's annual operating-income row shown to be non-GAAP, with the filed record being three consecutive years of operating losses.

Two dates set this file's shelf life: fiscal Q4 and full-year 2026 report **2026-08-05**, Investor Day **2026-08-13**. The single item that would most move this table is a disclosure at either event of whether the $41.6bn of remaining performance obligations carries a **price floor or only a volume commitment** — it moves the *bear* case most, because it is what determines whether trough gross margin goes negative again. Re-run this valuation after both.

### 2026-08-22 — refresh

Refresh mandated by the fired revisit trigger (journal/_flagged.md, 2026-08-22): the floor disclosure the prior entry named as the single most valuation-moving item landed on 2026-08-05 and was reaffirmed 2026-08-13. Price 1,596.08 (close 2026-08-21). New range **$475 / $875 / $2,200**, PWFV **~$1,090** at 30/45/25; verdict unchanged at PASS because upside-to-base remains −45% and the ASYM-P2 numerator remains negative.

Material changes and their reasons: (1) **method** — primary lens moved from retained-forward-tangible-book to distributions-plus-terminal, forced by the 100%-excess-cash-return policy and $4.5bn of Q4 buyback at ~$1,512/share; roughly half the base-case increase is this method change, stated so the next refresh can grade it. (2) **The trough P/B series was recomputed from primaries and corrected**: MU troughs are ~0.80-0.82x (2016, verified), ~1.03x (2019) and ~1.06-1.07x (2022-12) — the prior 0.97x/1.32x do not reproduce and the rising staircase was an artifact; SNDK's own standalone trough was 0.44-0.47x reported / ~1.0x tangible. The prior file's "40.10" price point appears back-solved, not traded. (3) **Implied-expectations table rebuilt with explicit tax** (prior version was zero-tax, overstating implied EPS by 15-21%); at today's EV, 8x EV/EBIT = Q4-run-rate-forever. (4) Consensus labelling corrected: yfinance forwardEps ($264.72) is the FY2028 mean; FY2027 consensus is $214.10 and has moved only +0.5% since 07-30 — a prior vault note misread the field. (5) FY2026 FCF flagged as overstating steady state (~$4.0bn of NBM deposits and unpaid taxes inside OCF; ~$1.4bn tax catch-up due FY2027; 15% CAMT from FY2027; 53-week year). (6) The prior reference price 1,249.44 was an intraday snapshot; the official 2026-07-30 close was 1,279.96 — future entries use official closes.

Grading the prior entry per PROD-P1: its pre-commitment was specific (floor disclosure moves the bear most) and correct in direction; its bear multiple (1.0x) was consistent with the corrected trough series; its 1.32x-anchored pieces and the unverified staircase were not, and are retired. What remains unverified after the refresh: the floor LEVEL (nowhere, including the audited 10-K, which never says "floor"); the deck's $16.5bn guarantee figure against the 10-K's identifiable ~$7.7bn of collateral, deposits and advances; and any renegotiation mechanics (the 10-K discloses none).
