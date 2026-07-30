# Memory semiconductors — KPIs and benchmarks

Concrete numbers from the actual companies and from the industry's supply/demand data, as of **2026-07-30**. Prices and multiples from the yfinance pull of 2026-07-30 18:37 local, USD, per "Price and data sourcing (canonical)". Verification labels per "Verification labels (canonical)".

**Read this page in the order it is written.** The industry table comes first because in memory the industry variable *causes* the company P&L, not the other way round — the income statement is the last place the cycle shows up, and by then the multiple has already moved (NARC-P2).

---

## 1. Industry KPIs — these lead everything

No quartiles here: these are single industry-wide series. Good/concerning is what a stock-picker actually needs.

| Metric | Good reading | Concerning reading | Current (2026-07-30) | Why it matters |
|---|---|---|---|---|
| **Bit supply growth vs bit demand growth**, by product | Demand exceeds supply by 3pp+ | Supply exceeds demand by 2pp+ | DRAM 2026: demand mid-30s% vs supply 16% (IDC via commentary, `partial`). NAND percentages **not obtainable** — TrendForce withholds them | The single causal variable. Demand is a *rate*; supply is a *step function* — a fab lands all at once. A 4-5pp gap is the difference between +85% gross margin and -33% |
| **Sufficiency ratio** (TrendForce supply/demand balance) | Negative (deficit) and getting more negative | Positive and rising | **DRAM -1% to -2% (2026), widening in 2027. NAND 4-5% deficit 2026, turns POSITIVE 2H 2027** (`verified`, TrendForce 2026-07-21 and 2026-07-30) | The cleanest single number in the sector, and it is currently telling you DRAM and NAND diverge |
| **Contract price momentum — the 2nd derivative** | Accelerating or stable | Decelerating for 2+ consecutive quarters | DRAM +43-48% → +93-98% → +58-63% → **+13-18%e**. NAND +55-60% → +70-75% → **+10-15%e** (`partial`) | **Both have decelerated for two quarters.** Equities discount the second derivative, not the level. Absolute price peaks historically land 2-4 quarters after momentum peaks |
| Supplier inventory (weeks) | 3-5 (tight) | >10 | **3-5** | Tight — but low inventory *at a price peak* is a top signature, not a bottom one. It is what causes the spike that triggers the capex |
| **OEM / distributor inventory (weeks)** | 2-5 | >10, or rising while prices decelerate | **7-9, up from 2-4** (`unverified`, commentary) | Normal is ~8; the post-COVID glut peaked at **31+**. The metric closest to firing |
| Fab utilisation | ~95-100% | <70%; ~50% is the floor seen in real downturns | Flash Ventures "historically ~100%"; **Kioxia's Yokkaichi Fab7 and Kitakami Fab2 reportedly ~50%** (`partial`) | The reported 50% matters more than any new-fab announcement: bit supply can be added by filling existing shells with tools, no groundbreaking required |
| **Industry capex in absolute dollars, YoY, at peak margin** | Flat or down | Up 20%+ | **SK hynix 2026 guided +50% to ≥$31bn (2026-07-29)**; Micron FY2026 ~$25-27bn, raised from an $18bn plan; DRAM industry $53.7bn (2025) → $61.3bn (2026e); NAND $21.1bn → $22.2bn | The industry's oldest tell, and it fired three weeks ago. Grade claimed discipline only against a full cycle of actual data (CAPA-P2) |
| Capex / **mid-cycle** sales | 25-35% | >40%, or rising while prices decelerate | Micron Q3 FY26 looks like a benign 17% ($7.1bn/$41.5bn) — against FY2025 revenue it is ~19% **per quarter** | **This ratio lies harder at the peak than any other memory metric**, because the denominator is a bubble. Always compute it against mid-cycle revenue (VAL-M1's logic applied to a ratio) |
| HBM share of DRAM wafer input | Rising | Falling | 19% (2025) → **~22-23% (2026e)**; HBM wafer capacity +29% YoY vs commodity DRAM +10% (`partial`) | DRAM's supply-destruction valve. NAND has no equivalent — the asymmetry in one metric |
| Chinese share of bit output | Flat | Rising | NAND → **~19% by 2027** (`verified`); CXMT DRAM ~350k WSPM by end-2026, ~25k below Micron (`unverified`) | A producer indifferent to the price at which it clears breaks every "supply discipline" argument, which implicitly assumes all producers maximise profit |
| Layer count / node transition status | Leading or on schedule | A missed transition | Kioxia/SanDisk 10th-gen (reported 332-layer) in production at Kitakami Fab2 from early July 2026, **~59% higher bit density per unit area** vs 218-layer (`partial`); SK hynix 321L in MP; Samsung ~430L targeted 2027 | A cost-down that becomes a *price*-down the moment the deficit closes. Hybrid bonding is the 2027 battleground |
| Downstream unit demand | Growing | Contracting | Smartphones **-15-20% YoY 2026**, notebooks **-10%**, servers **+17%** (TrendForce 2026-07-21) | Elasticity is already visible. Samsung's own mobile division lost money on the price in Q2 2026 (`partial`) |

## 2. Company operating KPIs

Sample is the four names in the current peer pull plus what is disclosed for the Korean players. Quartile framing is strained on n=4-6 — read the columns as *best / representative / worst observed*, not as a distribution.

| Metric | Best observed | Representative | Worst observed | Source / date |
|---|---|---|---|---|
| **Exabytes shipped, YoY** — the KPI that separates price from volume | MU (not separately disclosed) | SNDK Datacenter **+160%** | **SNDK total FLAT; Edge -10%; Consumer -40%** | SNDK 10-Q q/e 2026-04-03, `verified` |
| **ASP per gigabyte, YoY** | SNDK Edge +343% | SNDK total **+248%** | SNDK Consumer +139% | Same, `verified` |
| GAAP gross margin, latest reported quarter | **MU 84.6%** (q/e 2026-05-28, `partial`) | SNDK 78.4% (q/e 2026-04-03, `verified`) | SNDK was **22.5%** five quarters earlier (q/e 2025-03-28) | Issuer filings/releases |
| GAAP operating margin, latest quarter | **MU 80.4%** (`partial`) | **SNDK 69.1%** = $4,111M / $5,950M (`verified`, 10-Q) | SK hynix **-67%** in Q1 2023 (`partial`) | See note below on the yfinance artefact |
| Trough gross margin, this cycle's prior down-leg | — | SNDK FY2023 **7.1%**, FY2024 16.1%, FY2025 30.1% (`verified`, FY2025 10-K) | **Micron -32.7%** in a FY2023 quarter (`partial`) | The number that defines the downside |
| Revenue concentration | SNDK: no customer >10% in FY2025 or FY2024; top 10 = 40% of revenue (`verified`) | — | SNDK had one customer at 15% in FY2023 | FY2025 10-K |
| Sales incentive & marketing / gross revenue | SNDK **12%** (Q3 FY26) | — | SNDK **19%** (Q3 FY25) | 10-Q, `verified` — they stopped discounting; the first thing to reverse |
| Under-utilisation charges | Zero | SNDK $11M in 9M FY26 | SNDK $24M in the prior-year periods | 10-Q Note 10, `verified` — SanDisk *deliberately* restricted its share of JV utilisation in 1H FY26, then ran flat out |

**Two mandatory warnings on this table:**

1. **Do not quote a ~70% operating margin as a run-rate for anything.** It is one quarter, and it sits on a base of 22.5% gross margin five quarters earlier. The 69.1% figure *is* the filed GAAP number (SanDisk 10-Q, quarter ended 2026-04-03) and 78.4% gross minus $498M of opex closes to it arithmetically without any JV contribution — the yfinance "impossible" reading of `operatingMargins` 69.98% above `grossMargins` 56.04% is a **period mismatch**, not an accounting anomaly: 69.98% is the latest quarter normalised, 56.04% is trailing twelve months. Two independent reconciliations landed on the same answer to four significant figures. TTM operating margin is **41.6%**.
2. **Do not use yfinance's annual operating-income row for SanDisk as GAAP.** SEC-filed `OperatingIncomeLoss` is **FY2023 -$2,035M, FY2024 -$468M, FY2025 -$1,377M** — three straight GAAP *operating* loss years, not the "+$0.51bn in FY2025" a data vendor reports after reclassifying the ~$1.83bn FY2025 goodwill impairment below the line. Per "Evidence weighting (canonical)", the primary filing outranks any characterisation of it, including a data vendor's.

## 3. Company financial KPIs

| Metric | Best observed | Representative | Worst observed | Source / date |
|---|---|---|---|---|
| Net cash / (net debt) | **SNDK: $3,735M cash, $0 long-term debt** at 2026-04-03; $1.5bn revolver fully undrawn; $2.0bn Term Loan B retired in full 2026-03-04 (`verified`) | MU cash+investments $30.2bn vs LT debt $5.14bn (`partial`) | Micron burned **-$5.45bn of FCF** in FY2023 | The real test is not leverage at peak — it is how many quarters of trough cash burn the pile funds |
| Off-balance-sheet obligations | — | **SNDK: $12,793M total committed cash requirements, of which $6,543M Flash Ventures; $993M of JV lease guarantees; $1.2bn owed Kioxia 2026-29** (`verified`) | — | "Zero debt" is a much narrower claim than it sounds in a JV-based NAND business |
| Operating cash flow | SNDK **$4,545M in 9M FY26** (vs -$10M prior-year 9M); MU $25.39bn in one quarter (`partial`) | — | SNDK FY2023-25: three loss years | |
| Reported capex — **and why it misleads** | SNDK $134M in 9M FY26 → FCF ~$4.41bn | MU $7.1bn in a single quarter | — | SanDisk's fab capital runs through JV loans, lease guarantees and prepaid building depreciation, **not** the PP&E line. Reading $134M as asset-light is the single most common error available on this name |
| Cash tax vs book tax | — | **SNDK: $117M cash taxes paid against $638M expense**; non-current income tax payable $131M → $783M in nine months (`verified`) | — | FCF conversion should worsen even if earnings hold. An earnings-quality flag, not a fraud flag |
| Goodwill / equity | — | **SNDK: $4,994M = 36% of $13,777M equity**, already impaired twice ($671M FY2023, $1,830M FY2025) | — | `verified`, 10-Q |
| Buyback discipline | — | SNDK **$6.0bn authorised 2026-04-30** ≈ 3.2% of a $185.0bn cap, against a ~6% diluted-vs-basic share wedge (157M vs 148M) | — | CAPA-P1: grade a repurchase by the multiple executed at and the shares actually retired. A memory buyback at 13x book is value destruction regardless of dollars returned. CAPA-M1: net return is gross repurchase minus SBC issuance |
| Insider behaviour | **SNDK CEO Goeckeler holds 509,903 shares (~$637M at 1,249.44) with zero open-market sales** — every disposition code F tax withholding (`verified`, Forms 4, 2026-05-11 to 2026-07-02) | CFO Visoso 165,058, no sales | CTO sold 2,000 at ~$1,755; CLO sold 600 at $1,736 and 600 at $2,088; CAO sold 2,446 at $1,426 | Trivial second-tier trimming, nothing from CEO or CFO. CAPA-M3's converse — no insider-exit signal |

## 4. Valuation multiples (current)

| Name | Fwd P/E | Trailing P/E | P/B | EV / TTM revenue | EV / TTM EBITDA |
|---|---|---|---|---|---|
| **SNDK** | 5.84-5.87 | 42.6 | **13.4** | **13.7x** | **32.1x** |
| **MU** | 5.56 | 19.3 | 9.58 | 10.5x | 13.9x |
| WDC (HDD) | **27.8** | 31.2 | 24.9 | 15.1x | 45.4x |
| STX (HDD) | **15.1** | 3,624 | 171.0 | 15.6x | 42.4x |

All 2026-07-30, `verified` from the yfinance pull **except** that the EV-based columns are **recomputed**: yfinance's `enterpriseValue` field is not reconcilable to market cap + debt − cash for any of the four names, understating SNDK by ~$34bn (146.9B reported vs ~$181bn reconciled), MU by ~$130bn, WDC by ~$20bn, STX by ~$17bn. **The brief's EV/Revenue 11.14 and EV/EBITDA 26.09 for SNDK are both ~24% too low. Use the recomputed figures.**

**Sector median / 5y average / 10y range: mostly not obtainable, and saying so is the honest answer.**

- SNDK has **~17 months of price history** (first bar 2025-02-13 at 36.00, when-issued) and GAAP-negative earnings for most of it. There is no 5-year average and no 10-year range. Any substitute is a construct and must be labelled one.
- The only long clean series is Micron's, and it could not be verified this session (macrotrends returned HTTP 403). Reported **MU trough P/B: 0.81 (2016-02-29), 0.97 (2019-05-31), 1.32 (2023-02-28), 10-year median ~1.93x — all `unverified`.** The *magnitude* is safe; the decimals are not.
- Working rule, minted from Micron's series alone and therefore explicitly provisional: **memory has historically been buyable below ~1.2x book; above ~3x book you are underwriting a permanent regime change; above 10x you are not doing valuation.** Replace this the first time a second name's full-cycle P/B series is assembled.

### Why P/E has no valid domain in this sector

At the trough the denominator is negative and P/E does not exist. At the peak it is a mid-single-digit number on peak earnings. **It is unusable at one end and actively misleading at the other.** SNDK at 5.87x, MU at 5.56x, SK hynix ~5.2x and Samsung ~5-7x are not five cheapness signals; they are one consensus forecast of a peak year, quoted five times. Micron peaked in May 2018 at ~$64 on a ~4-5x forward P/E and fell ~56% to ~$28 by December 2018 **while earnings were still rising** (`unverified`, commentary). This is VAL-T1 in its purest available form.

### What the forward P/E actually embeds — the arithmetic a screen hides

SNDK FY2027 consensus (21 analysts, yfinance 2026-07-30, corroborated by stockanalysis.com as of 2026-07-23):

| | Mean | Low | High |
|---|---|---|---|
| EPS | **212.95** | 154.28 | 396.08 |
| Implied P/E at 1,249.44 | **5.87x** | 8.10x | 3.15x |
| Revenue | $49.87bn | $38.18bn | $80.91bn |

- The mean requires 212.95 × 148.1M shares = **~$31.5bn of net income on $49.87bn of revenue — a 63.2% net margin** — and there is no margin lever left, since Q4 FY26 is already guided at 79-81% gross margin. The entire increment must come from price × volume.
- Against the Q4 FY26 guided EPS midpoint of ~$31.50 (annualising to ~$126, i.e. **~9.9x**), consensus needs earnings a further **~69% above the June-quarter run-rate, held for a full year**.
- **The FY2027 consensus rose 86% in 90 days** (114.38 → 175.38 → 188.88 → 212.60 → 212.95) with **6 upward revisions and 0 downward in the last 30 days** — while the stock halved. Estimates chased realised spot pricing in a straight line and not one analyst cut. That is the textbook late-cycle configuration, and it means **the market is voting against its own consensus**.
- **TrendForce's NAND crossover (2H 2027) lands inside the fiscal year the estimate covers** (SanDisk's FY2027 ends ~July 2027). Consensus assumes peak conditions hold right through the quarter the industry's own forecaster says the shortage ends.

### The P/B anchor, and the trap inside it

P/B is the right primary lens here (VAL-P2 — pick the multiple from what the denominator means for the business; for a commodity manufacturer that is replacement capital, not earnings). **But naive P/B fails at a peak in the opposite direction to the way P/E fails**, because book compounds faster than price falls:

| SNDK book value per share | P/B at 1,249.44 |
|---|---|
| Now (Q3 FY26 balance sheet), 93.09 | **13.42x** |
| + Q4 FY26 consensus EPS 34.52 → 127.60 | 9.79x |
| **+ FY27 consensus EPS 212.95 → 340.55** | **3.67x** |

SanDisk would earn **2.3x its entire current book value in FY2027 alone** if consensus is right. So 13.4x book is a stale denominator in the other direction, exactly as 0.81x was in 2016. The honest anchor is post-FY27 book:

| Multiple of post-FY27 book (340.55) | Implied price | vs 1,249.44 |
|---|---|---|
| 0.8x (2016 trough, `unverified`) | 272 | -78% |
| 1.0x | 341 | -73% |
| 1.3x (2023 trough, `unverified`) | 443 | -65% |
| 2.0x (mid-cycle) | 681 | -45% |
| **3.67x (today)** | **1,249** | 0% |

Today's price is **3.67x forward book — above every historical trough anchor and above a normal mid-cycle multiple, on a book value that only exists if the peak year is actually delivered.** That framing is far more decision-useful than "5.87x forward earnings," and it is the single most useful line on this page.

### EV / replacement cost — the third independent lens

Greenfield DRAM fab: **$15-20bn+ for 100-200k wafer starts/month, 2-3 years to build** (`unverified`, trade/analyst estimates). This is the honest trough anchor — at the bottom, installed capacity has an unambiguous rebuild cost and the market has repeatedly priced incumbents below it. It is also the *bear* anchor at the top: SNDK's reconciled EV of ~$181bn sits against a NAND fab base it half-owns through a JV, inside buildings owned by its partner.

VAL-P3 wants three genuinely independent lenses. **A DCF, an FCF yield and an EBITDA multiple all driven off one price forecast are one lens counted three times** — the standard memory mistake. The three that are actually independent here are: (a) normalised mid-cycle earnings on a stated normal gross margin, (b) multiple of post-recovery book against historical trough/mid-cycle P/B, (c) EV against replacement cost of capacity.

## What's normal vs what's stretched

**Peak, on every reading that is not a P/E.**

- **Gross margins ~25pp above prior-peak precedent.** The cited sustainable commodity-DRAM band is 55-70% and the 2018 peak was ~60% (`unverified`); current prints are 78-86%. Mean reversion here does not require a demand collapse — only normalisation.
- **Momentum has rolled in both products** while the *level* is still rising. That combination — rising prices, collapsing rate of increase, inventory building at the OEM — is the specific configuration that has preceded every prior top.
- **The supply response is announced but not landed.** 2-3 years decision-to-first-wafer means today's announcements are the 2028-29 problem; the 2027 problem was decided in 2024-25 and is arriving on schedule.
- **The cycle is ~36 months old trough-to-peak against ~30 months for the 2018 supercycle** (`unverified`) — already ~20% past the prior precedent.
- **Positioning was crowded going in.** Q1 2026 13Fs (positions as of 2026-03-31, i.e. *before* the June peak): SNDK hedge-fund holders 114 vs 75 the prior quarter; MU 154 vs 137; Tepper and Druckenmiller both opened SNDK (`unverified`, secondary). Stale, and part of the bear case rather than a reason to follow.

**Genuinely not stretched:**

- **Balance sheets.** Net cash across the complex, no refinancing risk, no covenant risk, no dilution risk. This is the one respect in which the industry enters a peak in unrecognisable shape versus 2018 or 2000, and it changes how deep the *trough* has to go before distress selling starts.
- **The DRAM supply constraint.** Sufficiency negative and widening into 2027, with an EUV gate and a self-reinforcing HBM valve. That leg of the bull case is intact and is the reason the sector deserves ongoing work rather than a pass.

**What the three cases imply for a valuation range — and why the range is not yet decision-grade.** Running the cases separately, per VAL-P1 (act on a range) and VAL-P4 (the earnings path and the multiple that path earns must move together — a bull case that assumes both 213 of EPS *and* a re-rating is double-counting):

| Case | Logic | Implied SNDK band |
|---|---|---|
| Cycle rolls on the historical timetable | Normalise the denominator (VAL-M1); apply the historical trough-to-mid P/B band of 0.8-2.0x to post-FY27 book | **272-681** |
| Peak is durable but earns a cyclical multiple | ~10x a normalised 100-120 EPS. Note this is also almost exactly the sell side's own position: a mean target of ~2,218 against FY27 EPS of 212.95 is **10.4x forward** — the analysts are arguing the earnings are real, not that the multiple re-rates | **1,000-1,200** |
| Regime change (contracted, oligopolistic, AI-structural) | 212.95 is a run-rate rather than a peak; ~10x | **~2,130** |

**That spread is roughly 272 to 2,130 — an 8x range, and it fails VAL-P3's cluster tolerance by an enormous margin.** The correct response is not to average it away. It is to name which lens is conservative and why: the trough-book lens is supported by every prior cycle; the regime-change lens rests on contract structures less than a year old that have never been tested through a down-leg. **The band cannot honestly be narrowed to decision width today**, and the observable that would narrow it is whether the LTA price floors hold when spot rolls — which nobody can know before the first down-quarter.
