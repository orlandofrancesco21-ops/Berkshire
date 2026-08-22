# Developed-market equity — asset-class exposure framework

> Personal playbook for forming and defending an **expected real return range** for broad developed-market equity, and for judging an allocation to it against its alternatives. This is the exposure almost any first ETF sits in, which is why it was built first.
> Written 2026-08-22, with the Shiller CAPE at 41.96 (2026-08-21) against a 1926-1984 mean of 14.6 — read every dated figure below as calibration, not as current state, and re-pull anything you are about to act on.
> Append-only in the learned log.

**Last updated:** 2026-08-22
**Exposure class:** listed equity, developed markets, large and mid cap, market-cap weighted
**Decision unit:** allocation over a stated horizon, against named alternatives — not a buy/pass on a business
**Default horizon:** **10 years.** This is not a preference. It is the only horizon at which the anchors below have measurable explanatory power, and the file refuses to quote an expected return without it.
**Umbrella framework:** no — decision-grade for a broad developed-market equity fund. Developed-market equity is one exposure with one return decomposition and one anchor family; it does not need a sub-exposure split. A *factor* or *single-country* fund is a different exposure and needs its own framework, not a sub-section of this one.

---

## Scope — what this exposure actually is

- **Index universe:** MSCI World is the reference index for this framework. FTSE Developed and S&P Developed BMI are near-substitutes with different country classifications and different small-cap treatment; where a fund tracks one of those, check the deltas rather than assuming this file's numbers carry over.
- **Selection rule:** large and mid cap across **23 developed-market countries**, covering approximately **85% of the free float-adjusted market capitalisation in each country** (MSCI World Index factsheet, as of 2026-07-31, verified).
- **Weighting:** free-float market cap. The mechanical consequence is worth stating plainly: the exposure buys more of whatever has already gone up. That is not a criticism — it is the reason the index has no turnover problem (2.95% over the last 12 months, same factsheet, verified) and no manager to be wrong. It is also why the concentration below is a *result*, not a decision anyone made.
- **Explicitly included:** Israel. Japan at 5.73%. Eleven sectors, of which Information Technology is 28.87%.
- **Explicitly excluded:** all emerging markets — which as of 2026 means **China, Taiwan, South Korea, India and Brazil are not in this exposure at all**; and **small caps**, which is the difference between the standard index and its IMI variant. A "World" fund holding zero Taiwanese semiconductors is the single most common surprise when a holder first opens the holdings list.
- **Reconstitution:** quarterly index reviews on MSCI's schedule; country classification (developed vs emerging) is decided by MSCI's own committee process on its own timetable, which makes the boundary of this exposure a **provider decision, not a market fact**.

### Label vs holdings

All figures from the MSCI World Index (USD) factsheet, as of 2026-07-31, verified — re-pull before acting, this drifts.

| What the label implies | What the index actually holds |
|---|---|
| "World" | **72.03% United States.** Japan 5.73%, UK 3.61%, Canada 3.41%, France 2.44%, all other 20 countries 12.78% combined |
| "Diversified across 1,282 companies" | **Top ten constituents = 26.41% of index weight.** NVIDIA 5.18%, Apple 5.07%, Microsoft 3.66%, Amazon 2.94%, Alphabet A+C 4.16% combined |
| "Broad market" | Large and mid cap only, ~85% of each country's free float. No small caps, no emerging markets |
| "Global equity risk" | For a EUR-based holder, ~72% of the exposure is USD-denominated assets. The currency position is real, unhedged by default, and nobody chose it |
| "A diversifier alongside my single stocks" | Francesco already holds NKE and ADBE. Both are US large caps inside this index. An allocation here is partly an *increase* in those two positions, not a hedge against them — quantify the overlap in the fund's own documents before calling it diversification |

**The one sentence that matters:** a developed-market index fund is a concentrated bet on large US companies wearing the word "World", and the concentration is at a level the yearbook data calls the highest US market concentration in 92 years (UBS/DMS Global Investment Returns Yearbook 2025 public summary, verified) — which does not make it wrong, but does mean the diversification argument for holding it has to be made on the numbers above rather than on the label.

## What drives long-run returns for this asset class

**The identity the valuation file will use.** Expected annualised real return over the horizon, in local terms, before the wrapper:

> **starting shareholder yield** (dividend yield + net buyback yield) **+ real growth in earnings per share + annualised change in the valuation multiple − fund costs − tax drag** (± currency, for a EUR-based holder)

The first three terms are an approximation of an accounting identity, not a model: they sum to the return by construction if the multiple term is measured on the same earnings definition as the yield. Everything that can be argued about lives inside the growth term and the multiple term. The last two terms are the only ones with a certain sign.

### What each term has historically contributed

The cleanest sourced decomposition available to this vault is Ibbotson and Chen's, for **US equities 1926-2000** (Yale ICF Working Paper 00-44, March 2002, verified — the PDF was read). Their identity reconstructs the 10.70% compounded annual nominal return as:

| Term | Contribution, US 1926-2000 | Can it repeat? |
|---|---|---|
| Income (dividend) return | **4.28 pp** | **No, not at this level.** MSCI World's dividend yield was 1.53% at 2026-07-31 (verified). The gap is the single largest reason a naive "equities return 7% real" assumption is unsafe today |
| Real earnings-per-share growth | **1.75 pp** | Bounded. It is per-share growth in the real economy, and Straehl and Ibbotson's follow-on work argues per-share payouts grew with productivity while aggregate payouts grew with GDP (Financial Analysts Journal 73(3), 2017 — abstract and summaries only, **partial**, the paper itself is paywalled and unread) |
| Change in the P/E multiple | **1.25 pp** | **No.** The P/E went from 10.22 at the start of 1926 to 25.96 at the end of 2000 (verified). A multiple cannot re-rate forever; this term is the one that borrows from the future |
| Inflation | 3.08 pp | Pass-through; strip it, this framework works in real terms |
| Reinvestment return | 0.20 pp | Small, and an artifact of the arithmetic |

That implies a **compounded real return of roughly 7.4% per year for US equities 1926-2000** (computed from the verified inputs above: 1.1070 / 1.0308 − 1). Two honest caveats, both load-bearing:

- **It is one country and it stops in 2000.** The global record is materially worse: the Global Investment Returns Yearbook 2025 puts the 1900-2024 annualised real return at **5.2% for world equities, 1.7% for bonds and 0.5% for bills** (Cambridge Judge Business School summary of the Yearbook, 2025, **partial** — this figure does not appear in the public summary PDF I read, so it is a secondary relay of a primary I could not obtain). The US-only numbers from the same source, read directly: nominal annualised 1900-2024 of **9.7% equities, 4.6% bonds, 3.4% bills, inflation 2.9%** (public summary, verified), which computes to about **6.6% real for US equities**.
- **The dividend term has partly migrated, not disappeared.** Buybacks now deliver a large share of what dividends used to. Shiller's own dataset added an alternative **total-return CAPE in September 2018 specifically to correct the earnings-per-share growth-rate bias caused by changing corporate distribution policy** (shillerdata.com, verified). Any decomposition that uses a bare dividend yield and a bare EPS growth rate on modern data is double-counting the shift. **Use shareholder yield, or use TR-CAPE, and say which.**

### Which term dominates when

Over ten years the yield and growth terms dominate and the multiple term is a swing factor. Over one year the multiple term is essentially the entire return. That asymmetry is the whole reason this framework insists on the horizon: it is the same identity producing a usable forecast at 10 years and noise at one.

## Valuation anchors and their honest track record

The core of this file. Explanatory power is stated with its sample, and **no anchor appears without the horizon at which it fails.**

| Anchor | Works at | Does NOT work at | Explanatory power (R²) | Sample | Source |
|---|---|---|---|---|---|
| **Shiller CAPE (P/E10)** | ~10 years | 1-3 years | **0.43** for 10-year-ahead real annualised returns | US, Jan 1926 - Jun 2012 | Vanguard 2012 (verified) |
| **Trailing 1-year P/E** | ~10 years | 1-3 years | **0.38** — statistically indistinguishable from CAPE | same | same (verified) |
| **Any smoothing between P/E1 and P/E15** | ~10 years | 1-3 years | R² **0.38 to 0.43**; the paper finds "no clear winner" | same | same (verified) |
| **Best of any signal at 1 year** | — | **1 year** | **0.12**, from a building-block model on trailing dividend yield and trend earnings growth. Most metrics near zero | same | same (verified) |
| **Fed Model** (earnings yield minus Treasury yield) | — | both | **0.16** at 10 years — worse than the earnings yield alone | same | same (verified) |
| **Trailing dividend yield alone** | — | both | explained **less than one-fifth** of 10-year returns | same | same (verified) |
| **Corporate profit margins, trend GDP growth, past returns** | — | both | near zero; the paper notes several popular signals correlated with future real returns **less well than rainfall** | same | same (verified) |
| **Starting yield, for nominal government bonds** (the contrast case, not this exposure) | 5-10 years | 1 year | correlation **0.81** US IG / **0.87** EUR IG at 5 years, vs **0.50 / 0.53** at 1 year | 1995-12-31 to 2025-05-31 | Janus Henderson, asset-manager article (**partial**) |

### Why bonds are far more predictable than equities, and why "valuation" is not one thing

This is the distinction the framework exists to hold, and it is mechanical rather than statistical.

A nominal government bond held to maturity has **every cash flow contractually fixed at purchase**. The starting yield to maturity *is* the return, up to reinvestment of coupons and default. Nothing has to be forecast. The residual uncertainty is a rounding error next to the signal, which is why the correlations above rise toward 0.9 as the holding period approaches the duration.

An equity fixes **nothing**. The buyer is forecasting an unknown stream of future earnings, an unknown payout policy, and — decisively — an unknown terminal multiple at which someone else will buy it. Two of the three terms in the decomposition above are forecasts, and the third (the multiple) is a forecast about other people's future forecasts. A CAPE reading is therefore not the equity analogue of a bond yield. It is a conditioning variable that shifts a wide distribution, and the width of that distribution is the finding, not a defect in the measurement.

The practical consequence: for a bond exposure, the starting yield can carry the expected-return range almost alone. For this exposure, the anchor sets the *centre* of the range and the historical dispersion sets the *width*, and the width is enormous.

## Historical return distribution

Point estimates are for people who have not read this section.

- **What CAPE explains, and what it leaves:** even conditioning on starting valuation, **approximately 60% of the historical variation in long-term real returns is unexplained** (Vanguard 2012, verified).
- **How wrong the point forecast has been:** in the same study, **about two-thirds of 10-year periods had realised returns that deviated from a 5-percentage-point band around the best-fit line** (verified). Read that twice. For a majority of history, the CAPE-implied forecast was wrong by more than 5pp per year, compounded over ten years.
- **Where the signal actually lives:** dropping the tails of the CAPE distribution and regressing only the **middle 50% of readings collapses the R² from 0.43 to 0.20** (verified). The anchor earns its keep at extremes and says comparatively little in the middle. Whether today's reading is an extreme is the first question to answer before quoting a range.
- **The distribution of annual outcomes:** in an average year, the real return on US equities was **8.5%**; the worst single year was 1931 and the best 1933 (UBS/DMS Yearbook 2025 public summary, verified). Across countries since 1900, the average standard deviation of **real** returns was **23.0% for equities**, 13.2% for bonds and 7.5% for bills (same source, verified).
- **Maximum drawdown, index level:** MSCI World fell **57.46%** from 2007-10-31 to 2009-03-09 (MSCI factsheet as of 2026-07-31, verified). That is the number a holder of this exact exposure actually lived through, in USD, nominal.

### Drawdown depth and time to recovery — in real terms

The four great US bear markets since 1900, from the Yearbook's public summary (verified). Recovery is measured in real terms, which is the only measure that matters to someone spending the money:

| Episode | Trough | Recovered | Underwater |
|---|---|---|---|
| Wall Street Crash | July 1932 | February 1945 | **15.5 years** |
| 1973-74 | October 1974 | — | **over 10 years in real terms** |
| Tech bubble | 2000-03 onward | July 2007 | **7.5 years**, peak to recovery |
| Global financial crisis | February 2009 | ~2013 | **4 years** |

The Yearbook's own conclusion on horizon is blunter than most allocation advice: **"much longer periods than 20 years are needed to understand trends in risk and return"** (public summary, verified). And the first quarter of this century has already underperformed the last one — global equities returned **3.5% real annualised since the start of 2000, with an equity risk premium over bills of 4.3%** (same source, verified), against the 5.2% long-run world figure.

**Sizing implication.** The historical record for this exposure contains a 57% index drawdown inside one holder's memory and a 15-year real recovery inside the sample that produces every long-run average quoted above. Size the allocation so that a second leg down is an opportunity to add rather than a reason to sell, and treat "it always recovers" as a statement whose supporting evidence includes a decade and a half of waiting (compare ASYM-T2, which says the same thing at single-stock level and understates it here, because an index cannot be replaced by a better idea the way a stock can). Principles are advisory throughout — see "Principle authority (canonical)".

## Regime and structural-change risks

Why the historical record may not repeat. Each with its direction of bias.

- **The CAPE's own mean has shifted, and nobody agrees why.** CAPE averaged **14.6 over 1926-1984**; since then it has **"defied mean reversion, having only once dropped below its long-run average"** (Davis, Aliaga-Díaz, Ahluwalia and Tolani, "Improving U.S. stock return forecasts: A fair-value CAPE approach", working paper read directly, published *Journal of Portfolio Management* 44(3), 2018 — verified). The current reading is **41.96 at 2026-08-21** against a full-series mean of 17.40 and median of 16.11, with an all-time high of 44.19 in December 1999 (multpl.com, **partial** — a secondary presentation of Shiller's data, not Shiller's file). If the level shift is structural, every historical CAPE-to-return regression is biased pessimistic today. If it is not, the current reading is within 5% of the dot-com peak. **This framework does not know which, and says so.**
- **Accounting changes in the denominator.** Siegel (2016) argues the secular rise in CAPE's trend is an artifact of **changes in accounting standards**, and proposes NIPA national-accounts earnings as the "E" instead (reported in the fair-value CAPE paper, verified as that paper's characterisation; Siegel's own paper unread, so the *claim* is verified and the *substance* is partial). Direction: makes reported CAPE look higher than a like-for-like historical comparison would.
- **Payout-policy shift, buybacks vs dividends.** Shiller's dataset added a total-return CAPE in September 2018 for exactly this reason (shillerdata.com, verified). Direction: a bare dividend yield understates shareholder return; a bare EPS series overstates growth if buybacks are ignored on one side. Both errors are live in casual analysis.
- **Index composition drift.** The MSCI World of 2026 is 28.87% Information Technology and 72% US (verified). Whatever the index was in 1990, it was not that. A historical average multiple for "the market" is an average of a differently-constituted thing, and applying it as a reversion target is a category error.
- **Survivorship and the one-country problem.** The single most cited long-run equity record — roughly 6.6% real, US, 1900-2024 — belongs to the most successful equity market of the period. The world number is 5.2% (partial). The Yearbook's database exists precisely because a US-only history is a survivor's history. **Direction: the headline figure most investors carry in their head is the best case, not the base case.** Note also that MSCI World's own published data before its 1986-03-31 launch is back-tested, which the factsheet states plainly (verified).
- **Concentration.** Top ten at 26.41% of the index and the ten largest companies globally at roughly a quarter of global equity value (verified). This is not by itself a forecast, but it means index-level returns now depend on a small number of outcomes to a degree the diversified historical record did not.

## Correlation and portfolio role

- **Role:** the growth engine. This exposure is not ballast and must never be sized as if it were.
- **Stock-bond correlation, long run:** **0.33 across countries and 0.19 in the US** (UBS/DMS Yearbook 2025 public summary, verified). The same source notes the correlation was negative from the late 1990s until 2021 and then was not — so the diversification benefit is real on the century-long average and **regime-dependent in the window a real allocation actually lives in**. Do not size a bond sleeve on the post-1998 correlation.
- **Overlap with what is already owned:** NKE and ADBE are both inside this index. The overlap is small in weight but the *factor* overlap (US large cap) is not. State the combined US large-cap exposure in the fund document rather than asserting diversification.
- **Currency:** ~72% USD for a EUR-based holder, unhedged by default. Over a 10-year horizon currency is closer to noise than to a return driver, but over the 1-3 year windows in which people actually judge themselves it can dominate. This is a genuine allocation decision (hedged vs unhedged share class) and it belongs in the fund document, informed by this weight.

## Alternatives to this exposure

The decision unit is an allocation *against alternatives*.

| Alternative | What it gets you that this does not | What it costs you | When it is the better call |
|---|---|---|---|
| **All-country (ACWI / global incl. EM)** | Adds ~10% emerging markets — Taiwan, China, Korea, India | More governance and expropriation risk; higher tracking cost | When the case rests on the exposure genuinely being "global" rather than on developed-market institutions |
| **All-country including small cap (IMI)** | The size premium, if it exists | Higher cost, more turnover, weaker evidence than the marketing implies | When the horizon is long enough that a factor tilt can be held through its underperformance |
| **Ex-US developed** | Removes the 72% US concentration deliberately | Gives up the market that produced the record every long-run average is built on | When the US concentration is the specific thing being managed |
| **Nominal government bonds** | A near-contractual expected return, per the predictability section above | Real returns of 0.9% annualised across 21 markets 1900-2024 (verified) — this is not a wealth-building asset | When the horizon is short, the money is spoken for, or the drawdown table above is unaffordable |
| **Holding more single stocks** | The chance to be right about something specific | Requires a research budget per name and produces the dispersion the index deliberately owns | When there is a genuine variant perception, per the IC sheet contract |
| **Cash** | Optionality, and a real return above zero when short rates exceed inflation | Almost certainly the worst 10-year outcome in the historical record | Only against a dated, named use for the money |

## When does the valuation anchor lie?

The failure modes of this file's own method, written by the person most likely to be fooled by them.

- **When the horizon is short.** The anchor is not a signal at one to three years, R² ~0.12 at best across every metric tested (verified). Quoting a CAPE-derived number as a reason to wait for a better entry is using a 10-year instrument as a timing tool, which the evidence does not support in either direction.
- **When the reading is in the middle of its distribution.** R² falls to 0.20 on the middle 50% of readings (verified). A mid-range CAPE is close to no information, and dressing it as a mild signal is worse than saying nothing. "Nothing relevant" is a valid output here as everywhere in this vault.
- **When the anchor's own out-of-sample record is worse than doing nothing.** Since roughly 1985, CAPE-based out-of-sample forecasts have had **larger average errors than simply using the trailing historical long-run average** (fair-value CAPE paper, verified). This is the strongest single argument against the method in this file and it is a primary-sourced one. The same paper reports that the **correlation** between predicted and realised 10-year returns has stayed high — 83% since 1960, 91% since 1985 — which resolves the apparent contradiction: the anchor **ranks decades well and levels them badly.** It knows which decade will be worse. It does not know by how much, and it has been persistently too pessimistic about the level.
- **When "expensive" has already persisted for a decade.** CAPE has dropped below its own long-run average only once since 1985 (verified). An investor who acted on "expensive" at any point in that span waited out most of a generation. This is VAL-T2's lesson at index level: name the *cause* of an elevated multiple before treating it as a forecast, because a structural cause and a cyclical one look identical on the chart.
- **When the denominator is not comparable.** Accounting-standard changes, buyback-driven EPS growth, and a 72%-US, 29%-technology index composition all mean today's numerator and denominator are not the same objects as the 1926 ones. See VAL-T1: a multiple is not information until the denominator is normalised, and at index level "normalised" is a much harder claim than at single-stock level.
- **When the multiple term is quietly doing all the work.** In any expected-return build, check what fraction of the projected return comes from assumed multiple change. Historically that term contributed 1.25pp of a ~7.4pp real return (verified). If a build has it contributing more than that, the build is a forecast about sentiment wearing the clothes of a valuation. Per VAL-P4, when the growth path and the exit multiple are linked, move them together rather than pretending they are independent.

## Red flags at exposure level

- **A single-point expected return.** VAL-P1 governs: the output is a range, and for a fund it is an expected-return range over a stated horizon, never a price target.
- **A long-run average quoted without its country.** "Equities return about 7% real" is a US number from the most successful market of the century. The world number is lower (partial, 5.2%).
- **A backtest that starts after 1985.** Every sample beginning in the last four decades contains the CAPE level shift and a bond bull market, and produces a flattering answer for both legs of a 60/40.
- **Diversification asserted from the constituent count.** 1,282 names with the top ten at 26.41% is a different object from 1,282 equally-weighted names.
- **A dividend yield used as the shareholder-yield term.** Understates the payout in the modern regime; the buyback migration is documented in Shiller's own data treatment (verified).
- **Treating the index provider's classification as a market fact.** Whether Korea is emerging or developed is a committee decision that changes what the fund holds without any business changing.
- **Reading a hedged share class as risk reduction without pricing the hedge.** The hedge has a carry cost tied to the rate differential and it is not free.
- **Any monitoring trigger keyed to a vendor series that could be discontinued or re-methodologised** — see PROD-T3. TrendForce-style dependence is not unique to industry frameworks; a CAPE series from a third-party website has the same fragility. Name the fallback next to the trigger or the trigger is decorative.

## Kill switches at exposure level

Per PROD-P3 a switch needs a threshold, a timeframe, and an observable that is actually published. At exposure level the honest set is small, and nothing here fires automatically — see "Principle authority (canonical)".

| Switch | Threshold | Timeframe | Observable, and where published | Fallback if the series dies |
|---|---|---|---|---|
| Concentration breaks the diversification premise | Top ten weight above ~35% of the index | Checked at each annual review | MSCI World factsheet, "Top 10 constituents", monthly | Compute from the fund's own published holdings file |
| The exposure stops being the thing that was bought | US country weight above ~80%, or a developed-to-emerging reclassification moving >2% of index weight | At MSCI's classification announcements | MSCI market classification review, annual June announcement | The fund's own country breakdown |
| The decomposition's yield term collapses | Shareholder yield (dividends + net buybacks) below ~2% while the multiple term is doing more than half the work in the current build | At each valuation refresh | Dividend yield from the index factsheet; buyback yield needs a source this vault does not yet have — **this switch is currently unusable and is written down as unusable** | None. Closing this is why the Damodaran and S&P buyback data are queued below |
| The wrapper stops delivering the exposure | Tracking difference persistently worse than the stated cost by more than ~0.20pp per year over 3 years | Annual | Fund's own annual report and index-vs-NAV series | Provider's published tracking data |

**Deliberately NOT switches here, so a future reader does not re-add them:** a drawdown of any depth (the historical table above makes clear that depth carries no information about what follows); CAPE crossing any particular level (0.20 R² in the middle of the distribution, and a documented 40-year one-way persistence); a bad year, or three; and any price level whatsoever. Exit is never triggered by price alone — that is a non-negotiable of this vault, not a preference of this file.

## What this framework does not cover

- **Wrapper mechanics.** Replication method (physical full / sampled / synthetic), UCITS domicile, accumulating vs distributing, securities lending and its revenue split, counterparty exposure, fund size and closure risk, spread and premium/discount, and tracking difference all live in the universal vehicle lens, [`frameworks/etf-vehicle-mechanics.md`](etf-vehicle-mechanics.md), which is read alongside this file on every fund deep-dive. Neither lens substitutes for the other: the best wrapper on a bad exposure is still a bad allocation, and a good exposure bought through a leaky wrapper gives back the premium it earned.
- **Any single fund's costs.** The cost term in the decomposition is generic here; it gets its value from the fund's own documents.
- **The tax rules themselves.** See below for what belongs here and what does not.

### Tax — what to check and why it matters, for a German-resident investor

**This is research, not advice.** Nothing in this section is settled, and the specifics must be confirmed by Francesco's *Steuerberater* before any of it is relied on for an allocation decision. It is written down because German fund taxation is materially different from the US treatment that dominates English-language investing writing, and because it is a real term in the return identity rather than a footnote.

What is genuinely a property of *this exposure* — and therefore belongs in this file rather than the vehicle lens:

- **The equity quota is what unlocks the partial exemption.** § 20 InvStG grants **30% of Erträge tax-free for an Aktienfonds held by a Privatanleger**, half that (15%) for a Mischfonds, and 60%/80% for domestic/foreign real-estate funds (statutory text at gesetze-im-internet.de, read directly, **verified**). A broad developed-market equity fund should qualify as an Aktienfonds; the qualifying threshold is a continuously-maintained Kapitalbeteiligungsquote defined elsewhere in the Act (commonly cited as 51%, **partial** — § 2 InvStG was not read). **What to check:** that the specific fund's prospectus states the equity quota and that the German depositary applies the Teilfreistellung automatically. A fund that drifts below the threshold silently loses 30% of its exemption.
- **Why it matters to the range:** the Teilfreistellung applies to the whole taxable amount, so it changes the *slope* of after-tax return, not a fixed offset. A build that models tax as a flat percentage of gains without it will be wrong in the same direction every year.

What is wrapper-and-jurisdiction mechanics, flagged here only so the fund document does not forget it (all **partial** — sourced from German tax-advisory sites, not from the statute or a BMF-Schreiben):

- **Vorabpauschale.** An annual advance lump-sum taxation of accumulating funds, computed as fund value × Basiszins × 0.7 and capped at the actual appreciation (§ 18 InvStG). The **Basiszins for 2026 is 3.20%**, with the tax withheld in January of the following year. This is the mechanism that makes a German accumulating ETF *not* fully tax-deferred, which is the single most common mistake carried over from US-centric writing.
- **Abgeltungsteuer** at 25% plus Solidaritätszuschlag (and church tax where applicable), against the Sparer-Pauschbetrag.
- **Direction of the effect:** tax reduces the compounding base every year, not just at exit, so its drag over a 10-year horizon is larger than a naive one-off calculation suggests.

**What could not be established:** the exact after-tax drag in percentage points for a specific fund and a specific holding period. It depends on distribution policy, the Basiszins path, and Francesco's personal allowance position. The framework's honest output is the *pre-tax* real return range plus a stated, sourced tax mechanism — not a single after-tax number invented to look precise.

## Mental-model crossover risks

The assumptions from this vault's five industry frameworks that do not transfer here. All five are single-business frameworks; importing their instincts into an asset class is the predictable failure — see NARC-M2.

- **Moat analysis is silent, and silence is not a clean bill.** There is no mechanism to name, no switching cost to credit, no cost curve to rank. An index owns the moats and the moatless together. In frameworks/memory-semiconductors.md the next-cohort lens went silent and that was explicitly recorded rather than read as a pass; the same discipline applies to the whole moat tier here.
- **Management quality does not exist as a variable.** What replaces it is index methodology and the classification committee — and those are worth roughly one paragraph of attention, not the research budget a CEO would get.
- **"Cheap" means something weaker.** At single-stock level a low multiple invites a search for the specific reason it is low, and that search can resolve. At index level there is no specific reason to find: the multiple is an aggregate whose components are moving in different directions, and the causal story is unverifiable by construction. Per VAL-T2, name the cause of a compression before acting — and accept that at index level you frequently cannot.
- **The range should be WIDER than a single-stock range, not narrower.** This is the most counter-intuitive item here and the one most likely to be got wrong. Diversification removes idiosyncratic dispersion from the *realised* outcome, which feels like precision. It does nothing about the dispersion of the *forecast*: 60% of 10-year variation unexplained, two-thirds of windows more than 5pp from the fit. A company deep-dive can reach a narrow range by understanding one business well; no amount of understanding narrows this one, because the residual is the market's future opinion of itself.
- **VAL-P3's three-independent-lenses rule is harder to satisfy here than it looks.** CAPE, trailing P/E, dividend yield and the building-block model are not four lenses; they share the same earnings series and largely the same mean-reversion assumption, and Vanguard's own comparison found them statistically indistinguishable (verified). A genuinely independent second lens has to come from somewhere else — Damodaran's implied-ERP approach solves for the discount rate that makes the index price equal the present value of expected cash flows (his 2025 figures: implied ERP 4.23%, earnings yield 3.97%, dividend yield 1.15%, T-bond 4.18%, giving an implied expected nominal return of roughly 8.4%; pages.stern.nyu.edu historical implied ERP page, read, verified) and is a real second lens because it is forward-looking and price-based rather than backward-looking and earnings-smoothed.
- **VAL-M1 does not apply.** There is no cyclical trough to normalise past at index level in the way a single cyclical business has one; smoothing is already what CAPE does, and stacking a second normalisation on top double-counts.
- **The kill-switch instinct mostly fails here.** PROD-P3's requirements are easy to satisfy for a company (a disclosed metric, a print date) and hard for an exposure. Most of what an investor wants to make a switch at index level is price, and price alone is never a trigger. Accept a shorter switch list rather than manufacturing observable-looking ones.

## Open questions

- **Does the vault believe the CAPE level shift is structural?** No position taken. The evidence for structural (accounting changes, real-rate conditioning, buyback migration, index composition) and the evidence for cyclical (a 41.96 reading within 5% of the December 1999 all-time high) are both live, and this file deliberately holds both. The fair-value CAPE approach is the most credible resolution found so far and it has not been replicated outside its authors' own institution as far as this vault has checked.
- **What is the actual net buyback yield for MSCI World, and where is it published?** Not established. Without it the shareholder-yield term is guesswork and one kill switch above is unusable.
- **Is there a published rolling-10-year real-return distribution for a developed-market (not US-only) index?** Not found. Every distribution figure in this file is US-only or country-average, which is exactly the survivorship problem the file warns about.
- **What is the empirically right way to combine a CAPE-implied range with a currency view for a EUR-based holder over 10 years?** Unresolved, and probably the most practically important open item.
- **This framework's own track record is n = 0.** It has never produced a range that has been graded against a realised outcome. Every claim about the method's reliability above is borrowed from published research on US data, not from this vault's experience. Treat the file as well-reasoned rather than validated, and say so in any fund document that leans on it.

## Sources to absorb

External evidence enters this vault through `absorb` and nowhere else, so this file's figures are only as good as the library behind it — and **`library/` currently holds one entry, none of it about this exposure.** Every number above is therefore sourced but *unabsorbed*: the retrieval was real, the distillation has not happened, and per "Source archive and deep retrieval (canonical)" retrieval is not evidence. The list below names exactly what would fix that, in priority order. **All five were queued in `sources.md` on 2026-08-22.**

| Source | Type | Access path | What it upgrades in this file | Queued |
|---|---|---|---|---|
| **Shiller, `ie_data.xls`** — monthly US price, dividends, earnings, CPI, rates from January 1871, plus CAPE and TR-CAPE | dataset | shillerdata.com / econ.yale.edu Shiller data page, free | Turns every CAPE figure from a secondary reading (multpl.com, partial) into a computed, verified number — including a real rolling-10-year distribution this vault could compute itself, and a TR-CAPE series that fixes the buyback bias | 2026-08-22 |
| **Vanguard 2012, Davis / Aliaga-Díaz / Thomas, "Forecasting stock returns: what signals matter, and what do they say now?"** | paper | PDF, free; already retrieved and read once for this file | The R² table is the single most load-bearing evidence here and currently lives only in this framework's prose. Absorbing it puts the figures in `library/` with locators and makes them citable from a fund's valuation file | 2026-08-22 |
| **Davis / Aliaga-Díaz / Ahluwalia / Tolani (2018), "Improving U.S. stock return forecasts: A fair-value CAPE approach"**, *Journal of Portfolio Management* 44(3) | paper | working-paper PDF free; journal version paywalled | The honest counter-case to this file's own method — the post-1985 out-of-sample failure and the rank-vs-level distinction. This is the source most likely to stop a bad allocation decision | 2026-08-22 |
| **Damodaran's data pages** — historical implied ERP (1960-2025) and the annual data update posts | dataset, article | pages.stern.nyu.edu, free, updated each January | The genuinely independent second valuation lens per VAL-P3, and an annually-refreshed one, which is what a 10-year framework needs to avoid rotting | 2026-08-22 |
| **UBS / DMS Global Investment Returns Yearbook** (Dimson, Marsh, Staunton) — full edition, not the public summary | annual-report | public summary free from UBS; full 294-page edition GBP 395 from London Business School; DMS data module GBP 4,000/yr | The global-versus-US record, the survivorship correction, and the drawdown/recovery table in full rather than the four episodes the summary shows. The paid tiers are almost certainly not worth it; the free summary should be absorbed and the gap recorded | 2026-08-22 |

A sixth row was queued the same day for a **gap with no identified source**: an index-level net buyback yield series for developed markets. Until one is found, the shareholder-yield term rests on a dividend yield alone, which the Shiller TR-CAPE documentation says is the wrong basis. A queued row naming a source that may not exist is the honest form — the alternative is the gap living only in this file's prose, where nothing sweeps it.

## What I've learned over time

Append-only log.

- 2026-08-22 (framework-bootstrap, v1 — the central finding): **CAPE ranks decades well and levels them badly, and conflating those two facts is how the anchor gets both oversold and dismissed.** The correlation between CAPE-predicted and realised 10-year US real returns has been 83% since 1960 and 91% since 1985, yet over the same later period the out-of-sample *forecast errors* were larger than simply using the trailing historical average (fair-value CAPE paper, verified). Both statements are true because correlation measures ordering and RMSE measures level, and CAPE's level relationship broke when its own mean shifted. The practical rule this yields: **use the anchor to say which decade is likely to be worse than another, never to say what number the next decade will print.**
- 2026-08-22 (framework-bootstrap, v1 — the finding that changes sizing): **the signal is concentrated in the tails.** Dropping the extreme readings and regressing only the middle 50% of CAPE observations cuts the R² from 0.43 to 0.20 (Vanguard 2012, verified). Combined with the finding that two-thirds of 10-year windows landed more than 5pp per year away from the fitted line, this means the honest output at a mid-range valuation is a *very* wide band, and the honest output at an extreme is a narrower one. The width of the range should therefore vary with where the reading sits in its own distribution — which is not how any retail expected-return table presents it.
- 2026-08-22 (framework-bootstrap, v1 — the crossover error worth writing down): **an index range must be WIDER than a single-stock range, and every instinct says the opposite.** Diversification removes idiosyncratic dispersion from the realised outcome, which feels like it should narrow the forecast. It does not: 60% of 10-year variation is unexplained by starting valuation, and the residual is the market's future opinion of itself, which no amount of research reduces. A company deep-dive can genuinely narrow its range by understanding the business better. This exposure cannot be understood better in that sense. Do not carry the "more diversified therefore more predictable" instinct across from the industry frameworks.
- 2026-08-22 (framework-bootstrap, v1 — honest gaps, so the next reader does not assume work was done): (1) **Nothing here has been through `absorb`.** Every figure was retrieved and read, and retrieval is not evidence in this vault; the five queued sources above are what closes it. (2) **No global rolling-return distribution was found** — every dispersion figure is US-only or a cross-country average, which is precisely the survivorship problem this file warns about, reproduced inside the file. (3) **No net buyback yield series** for the index, so the shareholder-yield term is incomplete and one kill switch is written down as unusable rather than quietly dropped. (4) **The German tax treatment is one statutory section deep** — § 20 InvStG was read; § 2's equity-quota definition, § 18's Vorabpauschale mechanics and every rate were taken from secondary German tax-advisory sites and are labelled partial. (5) **The method has never been graded**: n = 0 closed 10-year windows against a range this file produced.
