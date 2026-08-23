# VUAG — fund thesis

> Append-only. Date every update. Old thinking matters.

**Created:** 2026-08-23
**Last updated:** 2026-08-23
**Vehicle lens:** `../../frameworks/etf-vehicle-mechanics.md`
**Exposure lens:** `../../frameworks/sp500.md`

## Identity

The ISIN is the identity; the ticker is not. VUAG (GBP line, LSE) and VUAA (every other listing) are the **same fund**.

| | |
|---|---|
| ISIN | **IE00BFMXXD54** |
| Primary listing / ticker | LSE, **VUAG**, GBP (the GBP line); LSE USD line is **VUAA** |
| Other listings | VUAA — LSE (USD), Xetra (EUR), Borsa Italiana (EUR), Bolsa Mexicana (MXN). One ISIN, five listings, three quotation currencies |
| Domicile | **Ireland** (Vanguard Funds plc — an Irish UCITS plc, not an ICAV) |
| Share class | **Accumulating** (distributing sibling is VUSA, IE00B3XXRP09, same 0.07% OCF) |
| Index tracked | **S&P 500 — Net Total Return variant** (SPTR500N). The NTR index deducts a 30% withholding assumption on dividends; this matters below |
| Provider | Vanguard (Vanguard Group (Ireland) Ltd, manager; BBH depositary) |
| Inception | **2019-05-14** (this accumulating class; the distributing class dates to 2012) — ~7.3 years of live NAV history, comfortably past the 3-year gate |
| TER / actual tracking difference | **TER 0.07%** [KID 2026-03-24, verified]. Realised TD **positive vs its NTR benchmark**: +0.29 / +0.20 / +0.16 / +0.24 / +0.18 / +0.15% for 2020–2025 [factsheet 2026-07-31, verified]. Against the true *gross* index the all-in drag is ≈ **0.15–0.22%/yr** — see Vehicle assessment |
| Fund size | **USD 86.0bn** total fund; **USD 34.2bn** this Acc class [factsheet 2026-07-31, verified]. No closure risk on any axis |

**Data sourcing:** TER, replication, benchmark variant, domicile, legal structure, Acc status, inception, AUM, the 2020–2025 year-by-year tracking record, all listings, and German Aktienfonds status are all **[verified]** from Vanguard's own KID (2026-03-24) and factsheet (2026-07-31). Market price VUAG.L **108.88 GBP, 2026-08-22, yfinance [verified]** (NAV is struck in USD; the GBP figure is the GBP line's market price). The securities-lending revenue split could **not** be read from a primary source (the 8.5MB annual report defeated extraction) — carried as a gap, not invented. Dividend/buyback yields are **[partial]** (aggregator/derived, not S&P DJI primary — the S&P 500 factsheet is queued in `sources.md`).

---

## What this fund actually holds

The S&P 500 — the ~500 largest US companies, free-float market-cap weighted, chosen by the S&P Dow Jones **Index Committee** (a discretionary committee, not a pure rules engine: GAAP-profitability screen, float minimum, committee timing). Full physical replication, 504 holdings versus 503 index constituents [factsheet 2026-06-30, verified] — genuinely full replication, not sampled-and-labelled-physical.

The gap between the label and the holdings, per `frameworks/sp500.md`:

- **"500 companies" is not "diversified".** The top ten are roughly the high-30s% of index weight (needs the current S&P factsheet to pin — **[partial]**, queued), materially more concentrated than MSCI World's top-ten 26.41% [verified], because this is the pure-US mega-cap core those same names sit inside. The direction — a record-high concentration — is not in doubt; the exact number is.
- **~One-third Information Technology** by GICS, and more once the mega-cap platforms in Communication Services / Consumer Discretionary are counted by economic character (**[partial]**, queued).
- **100% US, 100% USD.** For a EUR-based holder the entire currency position is USD, unhedged. Higher than a World fund's ~72%.
- **Already-owned overlap:** NKE and ADBE (held) are both S&P 500 constituents. The *weight* overlap is small; the *factor* overlap (US large cap) is total. An allocation here is more US-large-cap beta stacked on two US-large-cap single names — quantify against `portfolio.md` once its share/cost fields are filled (currently TBD).

## The case for the exposure

1. **It is the core growth engine of a long-only equity book, and the cheapest, most-studied way to own US large-cap productivity.** Over the full record US large-cap equity compounded ~7.4% real (1926–2000 Ibbotson–Chen decomposition, verified via `frameworks/sp500.md`) — the single most successful equity market of the century.
2. **The wrapper is excellent** (see Vehicle assessment): 0.07% TER, full physical, Irish-domiciled so US dividend withholding is capped at the 15% treaty rate, $86bn and growing, and it *beats* its stated benchmark net of fees. On the part of the analysis that is knowable rather than forecast, this fund is close to best-in-class.
3. **German tax efficiency is real and structural:** classified as an **Aktienfonds** with a contractual 85% minimum equity quota [Vanguard DE page, verified], so it qualifies for the 30% Teilfreistellung — a benefit that dwarfs any plausible fee difference between it and its peers.
4. **For a decade-plus holder, cost certainty beats valuation timing.** CAPE is not a 1–3 year timing tool (R² ~0.12); the durable edge in a commodity wrapper is cost position (MOAT-P4), and this fund has it.

## The case against the exposure

Steelmanned, and this is the load-bearing half of the document:

1. **The starting valuation is at a historic extreme.** Shiller CAPE ~41 (2026-08, `library/shiller-ie-data.md`, verified), the **99th percentile** of the 145-year record. The five most expensive starting months ever recorded (CAPE 43.2–44.2, clustered 1999–2000) **all produced negative real returns over the following decade** (−2.55% to −4.59%/yr). Today's reading sits just below that cluster. The record contains **no example of a decade starting this expensive that ended well** — and only five examples at all.
2. **Conditioning on valuation lowers the centre and barely narrows the width.** The most-expensive CAPE quintile delivered a 10-year forward real median of **+4.8%** with a range of −5.9% to +13.1% (computed from the absorbed Shiller file, verified). The term decomposition (below) is more conservative still, at ~+2.5% real base. The honest 10-year expected real return is **modest and genuinely could be negative** — not the ~7% most holders carry in their heads.
3. **Record concentration means the outcome now rests on a handful of mega-caps** to a degree the diversified historical drawdown record did not, so the tail may be *worse* than history shows. Marks' Dec-2025 "Is it a bubble?" (`library/marks-2025-12-is-it-a-bubble.md`, absorbed) is the on-point reading.
4. **There is no ex-US ballast.** Unlike a World fund, this exposure cannot be defended by pointing at a lower world number — it *is* the survivor market, priced as if its exceptional century is guaranteed to repeat.
5. **The drawdown record is brutal and lived-through:** −55% in the GFC (recovered ~5y), −86% price / ~15.5y *real* recovery in 1929–45, −48% in 1973–74. A holder must be sized to hold and add through that, not to sell into it.

## Vehicle assessment

*(This section replaces the company thesis's "capital allocation" and "management quality" sections, which do not exist for an index fund — the index committee is the only "manager," and it gets one paragraph, not a research budget.)*

**Vehicle verdict: SOUND for a 10-year hold.** This is a well-built, cheap, large, tax-efficient wrapper. The finding is not a wrapper problem; it is that a marginally cheaper physical clone exists and a higher-realized-return (but riskier) synthetic clone exists.

**All-in annual drag: ≈ 0.15% to 0.22%/yr** vs the true *gross* S&P 500 total-return index, built from separately-sourced terms:
- TER **0.07%** [verified].
- Unrecovered US withholding ≈ 15% × ~1.25% dividend yield ≈ **0.19%** [WHT rate verified from the US–Ireland treaty via the vehicle lens; yield partial].
- Index turnover/rebalance: a few bp (S&P 500 is low-turnover).
- Less securities-lending credit: a few bp (fund lends; split **not established** from primary — widen the range for it).
- **Cross-check from the primary record:** the fund beats its *net-total-return* benchmark by +0.15 to +0.29%/yr (2020–2025). That benchmark embeds a 30% WHT assumption (≈ −0.375%), so versus the true gross index the fund runs ≈ **−0.18%/yr** — consistent with the bottom-up build. **State the sign carefully:** positive vs the NTR benchmark (the fund's WHT beats the benchmark's assumption), mildly negative vs the economic gross index.

**Replication:** full physical, 504/503 names — tightest method, no counterparty risk. **Domicile:** Ireland — the correct domicile for US-equity content (15% treaty WHT vs Luxembourg's 30%; and Irish-fund shares are not US-situs, sidestepping US estate tax). **Size/closure:** $86bn fund, $34bn class, growing — structurally fine. **Liquidity:** deeply liquid underlying; trade with limit orders during US-market overlap hours only.

**Peer table** — the peer set is other S&P 500 wrappers, never the companies inside:

| Fund | ISIN | Class | TER | Replication | Domicile | AUM | Realised TD | Verdict vs VUAG |
|---|---|---|---|---|---|---|---|---|
| **VUAG** (this) | IE00BFMXXD54 | Acc | 0.07% | Physical full | IE | $86.0bn | +0.15–0.29% vs NTR | — |
| iShares Core (CSPX/SXR8) | IE00B5BMR087 | Acc | 0.07% | Physical full | IE | $158bn | +0.16% vs index (2025) | **Wash** — structural twin, same fee/design |
| SPDR (SPYL) | IE000XZSV718 | Acc | **0.03%** | Physical full | IE | (SPDR umbrella) | +0.20% ann. vs NTR | **~4bp/yr cheaper**, but Acc class young (Oct-2023) and smaller |
| Invesco (SPXS) | IE00B3YCGJ38 | Acc | 0.05% + ~0.07% swap ≈ 0.12% | **Synthetic** | IE | $57bn | **+0.3 to +0.5%/yr** vs NTR | **Higher realised net return** via 871(m) full-gross-dividend capture, at the cost of swap-counterparty risk + a correlated regulatory-arbitrage risk |
| Amundi | LU1681048804 | Acc | 0.15% | Synthetic | LU | €6.75bn | +0.2–0.5% vs NTR | **Dominated** — highest fee, LU domicile; the synthetic advantage is eaten by cost |

**Named best alternative(s):** none *strictly* dominates VUAG. **SPDR SPYL** (0.03%, physical, Irish) is the cost-minimal clone — ~4bp/yr cheaper, worth ~0.4% of terminal wealth over a decade, against the cost of a younger, smaller Acc class. **Invesco SPXS** has delivered the highest *realised* net return, but its edge is a US regulatory arbitrage (§1.871-15 qualified-index safe harbour) that can vanish for every synthetic US-equity fund at once, plus swap-counterparty risk — a different risk profile, not a free lunch. **VUAG vs iShares CSPX is a genuine wash.**

## What would change my mind

Two kinds, different actions (PROD-P3: each keyed to a published observable).

**Exposure-level** — the asset-class case is broken (action: leave US large-cap, not switch funds):
- A methodology change to the S&P 500's selection rule (e.g. dropping the GAAP-profitability screen) — observable in the S&P methodology PDF.
- Shareholder yield (dividends + net buybacks) falling below ~2% while the return build leans on multiple expansion for more than half of it — **currently unusable as a hard switch** because no net-buyback-yield series is sourced (queued).
- Note per ASYM-P1 / the sp500 framework: **no CAPE level, no drawdown depth, and no price is a kill switch.** Exit is never triggered by price alone.

**Vehicle-level** — *this wrapper* is broken while the exposure is fine (action: switch funds, a taxable event to weigh):
- TER increase, or realised tracking difference degrading beyond ~0.15pp/yr worse than the stated cost for 3 consecutive years — Vanguard factsheet / annual report.
- AUM falling below ~€500m with a sustained downtrend (far off today) — factsheet.
- Loss of Aktienfonds status / the 85% equity quota — Vanguard German tax data.
- An S&P 500 index-provider or methodology change, or a share-class merger/closure notice.

## Principles check

- **ALIGNS VAL-P1** — the output is an expected-real-return *range* over a stated horizon, never a point; this file and `valuation.md` refuse a single number.
- **TENSION VAL-T2** — a valuation percentile above history can be composition change (accounting, buybacks, ~⅓ tech) rather than genuine expensiveness, and the two are indistinguishable on the chart. This thesis *asserts* mostly-expensive (hence the conservative base case) while flagging that if the CAPE level shift is structural, the bear case is too harsh. What would show it: a decade of realised returns landing in the upper half of the conditional band.
- **ALIGNS ASYM-P2** (holds-when: the ratio treats a drawdown and a permanent loss as the same thing scaled) — for a diversified index the bear leg genuinely *is* a drawdown, not permanent loss, so the binding sizing constraint is drawdown depth and time-to-recovery, written into Allocation logic as numbers.
- **ALIGNS MOAT-P4** — two funds tracking the same index are a commodity, and the only durable edge is cost position; the vehicle assessment is decided on cost/structure, not narrative.

## Conviction

**Level (1-5):** 3

Two verdicts, deliberately not blended:
- **Exposure (moderate, ~3/5):** owning US large-cap as core equity beta over 10+ years is sound, but at a 99th-percentile CAPE the 10-year expected real return is modest (~+1.8%/yr pre-tax, probability-weighted, net of wrapper) with a real probability of a negative decade. This answers the case-against's VALUATION challenge not by dismissing it but by *sizing for it* — the conviction is in owning the exposure, not in the entry point being good.
- **Vehicle (high, ~5/5):** VUAG is a sound, cheap, large, tax-efficient wrapper. The only refinements are a ~4bp cheaper physical clone (SPYL) and a higher-realised-return synthetic (Invesco) whose extra return buys extra risk.

The binding constraint is the exposure/valuation, not the wrapper — which is why the blended number is 3 and not 5.

## Allocation logic

The decision unit. Owner is **deploying a specific cash amount, 10-year horizon**, into a **core equity-beta** role.

- **Role:** core beta, rebalanced back to target (not a satellite tilt to be re-argued on drift).
- **What it displaces:** cash / dry powder. It duplicates, in factor terms, the US-large-cap exposure already held via NKE and ADBE — quantify the combined US-large-cap weight once `portfolio.md`'s TBD share/cost fields are filled; until then, treat the addition as *increasing*, not diversifying, US-large-cap concentration.
- **Currency:** 100% USD, unhedged, for a EUR base. Over 10 years currency is closer to noise than a return driver, but it does most of its work in the drawdown — a EUR holder can experience a US-market fall *and* a USD fall together. No defensible directional FX expectation; carried as a ±band, not hedged (the hedge's carry cost is a real annual number that would eat much of the wrapper's cheapness).
- **Sizing, written as numbers per ASYM-P2:** the historical record for this exact exposure contains a **−55% drawdown recovered in ~5 years and an −86% price fall that took ~15 years to recover in real terms.** Size the position so that a **50%+ drawdown lasting a decade is an outcome you can hold through and *add* into**, not one that forces a sale. Concretely: the position should be small enough that a halving of it does not threaten a dated cash need and does not exceed your tolerance for a multi-year underwater hold.
- **Entry, given a lump at a 99th-percentile CAPE:** lump-sum investing has the higher *expected* return (time in market, and CAPE does not time 1–3 year entries). But phasing the cash over ~6–12 tranches is a defensible **regret-minimiser** whose expected-return cost is small and whose benefit is behavioural — it makes the drawdown-tolerance sizing above easier to actually live. This is a behavioural choice, explicitly **not** a claim that valuation lets you time the entry.
- **Target weight:** an owner risk decision (depends on total equity target and risk tolerance, which this run does not have). The system's input is: own it as core beta, size it for the drawdown record above, and prefer VUAG or the ~4bp-cheaper SPYL as the wrapper.

## Update log

### 2026-08-23 — initial thesis

Fresh deep-dive via `evaluate` → `fund-deep-dive`, prompted by "evaluate etf VUAG". Exposure lens `frameworks/sp500.md` was **bootstrapped in the same run** (v1, un-pressure-tested) and the exposure-slug `sp500` minted with the owner's assent — so the exposure figures here rest on a v1 framework and should be re-checked when it is hand-refined. Original allocation case: **own the S&P 500 as core equity beta over 10 years through VUAG, a SOUND and tax-efficient wrapper, but sized for a 99th-percentile-CAPE starting point** where the probability-weighted 10-year expected real return is ~+1.8%/yr pre-tax (net of wrapper) with a genuine chance of a negative decade. Vehicle SOUND; cost-minimal clone SPYL (0.03%) and higher-realised-return synthetic Invesco (871(m)) both named. Verdict routed ALLOCATE-as-core-beta with sizing/entry discipline as the binding constraint, not the wrapper choice. Securities-lending split and current S&P concentration figures are open gaps (queued in `sources.md`).
