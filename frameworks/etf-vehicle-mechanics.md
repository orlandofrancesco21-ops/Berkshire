# ETF vehicle mechanics — evaluation framework

> Personal playbook for evaluating **the wrapper**, not the exposure. Every fund I ever own gets read through this file: it answers "given that I want exposure X, is THIS vehicle the right way to own it, and what does the wrapper cost me?" It is deliberately exposure-agnostic — it applies identically to a world-equity tracker, a EUR corporate-bond fund, and a gold ETC — which is why it is worth building once and properly.
> Written 2026-08-22, before any fund in this vault has been evaluated. Read the dated figures as calibration, not as current state.
> Append-only in "What I've learned over time". Refine every time a fund is evaluated.

**Last updated:** 2026-08-22
**Umbrella framework:** no — this is a **lens, not an industry**. It is decision-grade on the wrapper question alone and is never sufficient by itself: a fund deep dive requires this file **and** an exposure framework (`frameworks/{exposure-slug}.md`). Neither substitutes for the other.

---

## What this lens is

A fund is two decisions wearing one ticker. The first is *what exposure do I want and what will it return* — that is an asset-class question, and it lives in the exposure framework. The second is *what does it cost me to hold that exposure through this particular legal and operational structure* — and that is this file. The two are separable, they are decided by completely different evidence, and conflating them is the characteristic error of retail fund selection: people argue about whether to own world equities and then pick the wrapper off a league table sorted by TER.

The wrapper is where the certain money is. An exposure's expected return is a forecast with a wide distribution; the wrapper's drag is close to deterministic and it compounds every single year whether the exposure works or not. On a 20-year hold, 30 basis points a year of avoidable wrapper cost is roughly 6% of terminal wealth, and unlike the exposure return it is knowable in advance. That asymmetry — a *certain* drag paid against an *uncertain* return — is the reason this file exists and the reason wrapper work is the highest-return-per-hour research in fund investing. (No principle in `principles/` currently states that asymmetry; the ASYM items are about entry price and position size, not about certain costs. Logged as a candidate in Open questions rather than forced onto an existing ID.)

**The one sentence that matters:** two funds tracking the same index are a commodity, and in a commodity the only durable advantage is cost position (see MOAT-P4) — but the cost that decides the ranking is almost never the cost that is advertised.

## How to use this file

Order of operations for a fund deep dive:

1. **Establish identity first** (see "Share-class and listing multiplicity" below). ISIN, not ticker. Get this wrong and everything downstream is about a different fund.
2. **Run the exposure framework.** What is the honest expected real return of this asset class over the stated horizon, decomposed into starting yield + real growth + valuation change? That is not this file's job.
3. **Run this file** to produce the two subtraction terms — **costs** and **tax** — and the structural checks (viability, liquidity, index integrity, lending) that could invalidate the holding independently of whether the exposure works.
4. **Compare against the alternatives on the same exposure.** A fund's peer set is other wrappers on the same exposure. This file's output is only meaningful as a *relative* ranking plus an absolute drag number.

The governing numbers live in the fund's `valuation.md` scenario table and nowhere else (VAL-P5). Everything this file produces is an input to that table, never a second set of numbers that quietly competes with it.

## Vehicle-type navigator

Triage what you are actually looking at **before** applying anything below. Several rows here are not funds at all, and the differences are legal rather than cosmetic.

| Vehicle | What it legally is | Key wrapper risk | German tax treatment to check | Notes |
|---|---|---|---|---|
| **UCITS ETF** | An open-ended fund (Irish ICAV/plc, Lux SICAV) with an exchange listing, ring-fenced assets, UCITS diversification rules | Tracking drag, closure, index change | Aktienfonds / Mischfonds / Sonstige — drives Teilfreistellung | The default vehicle for a European investor and the case this file is written around |
| **UCITS index mutual fund** | Same fund law, no exchange listing; dealt at a single daily NAV | No intraday liquidity; platform-dependent access | Identical to the ETF equivalent | Removes spread and premium/discount entirely. Often the better wrapper for a pure buy-and-hold saver, and it is systematically overlooked because it has no ticker |
| **ETC / ETN (commodities, crypto)** | A **debt security**, not a fund. Often collateralised, sometimes physically backed, always an issuer claim | **Issuer/counterparty credit risk** — no fund ring-fencing in the UCITS sense | Usually *not* an investment fund for InvStG purposes; different regime entirely | The single most dangerous category to treat as "an ETF". A physically-backed gold ETC is a secured note, not a fund |
| **US-domiciled ETF (40-Act)** | US open-ended fund | Not purchasable by EU retail (PRIIPs); US estate-tax situs | US-situs asset; withholding at distribution, creditable | Covered below because the *comparison* matters even when the purchase is unavailable |
| **Actively managed ETF** | A fund with no index to track | Manager risk, no benchmark to compute TD against | Same as passive equivalent | Tracking difference is undefined here. The whole cost-measurement apparatus below degrades to "fees plus turnover" |
| **Leveraged / inverse ETP** | Daily-reset derivative product | Path dependency; guaranteed decay in choppy markets | Rarely an Aktienfonds | Out of scope for a long-only low-frequency vault. Named here so the exclusion is deliberate |

---

## 1. Cost, honestly measured

### TER is the advertised number; tracking difference is the real one

**TER (ongoing charges)** is a disclosed figure covering management fee, administration, custody, audit and — usually — the index licence. It excludes portfolio transaction costs, rebalancing costs, swap financing spreads, unrecoverable withholding tax, cash drag, and securities-lending economics. Every one of those excluded items is real money, and two of them (withholding tax and lending revenue) are routinely larger than the TER itself.

**Tracking difference (TD)** is the realised gap between the fund and its index over a stated period. It is the only number that captures everything, because it is measured after everything has happened.

**Vault sign convention, pinned here so it never has to be re-decided:**

> **TD = fund NAV total return − index total return. Negative TD is a cost. Positive TD means the fund beat its index.**

State the convention next to every TD figure written into a fund document, because **justETF and several providers use the opposite sign** (index minus fund, so their negative is good) (justETF and provider convention, observed 2026-08-22, partial). A sign error here inverts the entire cost ranking, and it is invisible when both funds are close to zero.

### What TD is made of

Build the expected TD from its parts *before* looking at the reported one. The residual between the two is the finding.

| Term | Sign | Typical magnitude driver |
|---|---|---|
| TER / ongoing charges | − | Disclosed |
| Unrecoverable withholding tax at fund level | − | **Index dividend yield × effective unrecovered rate** — see section 3 |
| Portfolio transaction and rebalancing costs | − | Index turnover, underlying spread, reconstitution frequency |
| Cash drag (dividends held between receipt and reinvestment) | − | Yield × average holding lag |
| Securities-lending revenue, net of the agent's share | + | Utilisation × lending spread × revenue split — see section 7 |
| Swap spread (synthetic funds) | ± | Negotiated; can be negative (counterparty pays the fund) |
| Sampling/optimisation error | ± | Zero-mean in theory, not in practice |
| Index-variant mismatch in the comparison itself | ± | See the withholding-assumption trap below |

Worked illustration, and note it is arithmetic on sourced inputs rather than a claim about any fund's performance: a physically replicating Irish S&P 500 UCITS ETF with a 0.07% TER (iShares Core S&P 500 UCITS ETF, IE00B5BMR087, justETF profile read 2026-08-22, partial) holding an index yielding ~1.05% gross (aggregator data, 2026-08-18, **unverified** — this is a secondary aggregator, not S&P DJI primary) suffers roughly 1.05% × 15% ≈ **16bp** of unrecoverable US withholding on top of the 7bp TER, for an expected drag of about **23bp** before lending revenue. A fund reporting materially better than −23bp is not free money: it is lending revenue, a favourable index-variant comparison, or a sampling bet. Find out which. A fund reporting materially worse has an unexplained leak.

Note what that arithmetic implies: **the withholding term scales with the dividend yield of the exposure, not with the fund's fee.** At the ~1.05% yield of 2026 the US-equity withholding drag is small relative to fee differences. On a high-dividend, value, REIT or emerging-market exposure yielding 3-4%, the same 15% costs 45-60bp and completely dominates the fee league table. **Cost ranking is exposure-dependent. Never carry a wrapper conclusion from a low-yield exposure to a high-yield one.**

### How to obtain the actual TD, in order of quality

1. **The fund's annual report.** This is the primary artifact and the disclosure is *mandatory*: an index-tracking UCITS's annual and half-yearly reports must state the tracking error at period end, the annual report must explain any divergence between anticipated and realised tracking error, and it "should also disclose and explain the annual tracking difference between the performance of the UCITS and the performance of the index tracked" (ESMA/2014/937, Guidelines on ETFs and other UCITS issues, para 11, dated 2014-08-01, read 2026-08-22, **verified**). The prospectus must additionally carry "information on the anticipated level of tracking error in normal market conditions" (same document, para 9(c), verified). If a fund document set does not contain these, that is itself a finding.
2. **Provider factsheet / website calendar-year table** of fund NAV return versus benchmark return. Same computation, more accessible, but the provider chooses the benchmark variant it compares to.
3. **Independent aggregators (justETF and similar).** Convenient, sign convention inverted, and a third-party series — anything keyed to it needs a named fallback (PROD-T3). Note as a live limitation of this vault: the BlackRock product page for the fund above returned **HTTP 403** to this session's fetch on 2026-08-22, so provider-level TD could not be read directly and no TD figure for any specific fund is asserted anywhere in this file.
4. **Compute it yourself** from fund NAV total-return series against the index total-return series. Only do this if you can obtain the *correct index variant* — see below.

### Why one year is noise, and how many years to use

A single year of TD is dominated by events that do not repeat: one large index reconstitution, one withholding-reclaim settlement landing in-period, one spike in lending demand for a squeezed constituent, one corporate action handled well or badly. **Use three years minimum and five where available, look at the year-by-year series rather than the average, and treat the dispersion as more informative than the mean** — a fund with a stable −9, −10, −11bp is a better-understood machine than one running −25, +14, −8bp to the same average.

Two hard gates before a TD series means anything:
- **The fund must be old enough.** Under three years there is no series, only a marketing chart. A fund whose displayed history predates its own inception is showing index history (see "When does the wrapper lie").
- **The comparison must be to the same index variant.** Price return, gross total return and net total return are three different series. This is where the largest silent error lives: **net-return index variants embed an assumed withholding treatment**, and where that assumption is worse than the fund's actual treaty position, the fund will appear to beat its index year after year with no skill whatsoever. An Irish fund paying 15% on US dividends compared against a net index constructed on a less favourable withholding assumption produces exactly this artifact. Establish which variant the provider is quoting before drawing a single conclusion. (Mechanism reasoned from the treaty rates in section 3; the specific withholding assumptions in any given index provider's net-return methodology were **not verified** in this build and must be read from the index methodology document at use time.)

### What a defensible TD range looks like

I will not invent a table of expected TD by asset class — the honest position on 2026-08-22 is that **this vault has no assembled TD dataset at all**, and a fabricated range here would be exactly the kind of number that becomes an anchor and outlives the conditions that produced it (PROD-P5). What is defensible now is the *construction method* above: build the expected drag from TER + yield × unrecovered withholding + a turnover allowance, subtract a lending estimate where lending is disclosed, and use that as the yardstick. The empirical range gets filled in as real funds are evaluated, and the first entries belong in "What I've learned over time".

## 2. Replication method

| Method | What the fund actually holds | Tracking effect | Counterparty risk | Withholding-tax effect |
|---|---|---|---|---|
| **Physical, full** | Every index constituent at index weight | Tightest; cost is transaction costs at rebalance | None from replication (lending may add some) | Pays the fund's treaty rate on every dividend, unrecoverable |
| **Physical, optimised/sampled** | A subset chosen to match risk characteristics | Adds basis risk that is zero-mean in theory and lumpy in practice | Same | Same |
| **Synthetic, unfunded swap** | A substitute basket of securities, plus a swap exchanging the basket's return for the index return | Mechanically very tight — the swap delivers the index by contract | Real: exposure to the swap counterparty between resets | **This is the point** — see below |

### Sampling: the check nobody runs

"Physical replication" on a factsheet does not mean full replication. The check is mechanical and takes two minutes: **download the fund's holdings file and count the positions, then compare to the index constituent count.** A broad developed-world or aggregate-bond fund holding materially fewer names than its index is optimised, and should say so. Then compare top-10 weights and sector weights against the index's published weights (which the index provider is required to publish — ESMA/2014/937 para 57, verified). Optimisation is not wrong; a bond aggregate index with tens of thousands of line items *cannot* be fully replicated. It is only wrong when it is undisclosed, or when the sampling is concentrated enough that the fund is quietly running an active bet.

### Synthetic replication and the withholding question

The mechanism, stated precisely: US withholding applies to dividends. A swap does not pay dividends — it pays a return. US tax law addressed this with the dividend-equivalent rules under section 871(m), which impose withholding on dividend-equivalent payments under equity derivatives — **but provide a safe harbour for contracts referencing a "qualified index"**. The regulation text has now been read, so the conditions can be stated rather than gestured at. Tested on the first business day of the calendar year (§1.871-15(l)(2)), an index qualifies only if it (i) "References 25 or more component securities"; (ii) references only long positions; (iii) references no single component above **15 percent** of the weighting; (iv) references no five or fewer components together above **40 percent** of the weighting; (v) "Is modified or rebalanced only according to publicly stated, predefined criteria"; (vi) "Did not provide an annual dividend yield in the immediately preceding calendar year from component underlying securities that is greater than **1.5 times the annual dividend yield of the S&P 500 Index** as reported for the immediately preceding calendar year"; and (vii) is traded through futures or option contracts on an SEC-registered national securities exchange, a CFTC-designated contract market, or a qualifying foreign board or exchange (Treas. Reg. §1.871-15(l)(2)-(3), full text read 2026-08-22, **verified**). Where the safe harbour applies, a synthetic fund can be delivered the index return **including the full gross dividend**, where a physical Irish fund receives 85% of it.

**Condition (vi) inverts this file's own argument, so read it before believing the headline.** Section 1 argues — correctly — that unrecovered withholding scales with the exposure's dividend yield and dominates the cost ranking on "a high-dividend, value, REIT or emerging-market exposure yielding 3-4%". But an index yielding 3-4% is yielding several times 1.5× the S&P 500's yield, fails condition (vi), and therefore **cannot use the safe harbour at all**. The synthetic route is structurally unavailable precisely where the withholding problem is largest. Synthetic replication is not a general answer to withholding drag; it is an answer available on broad, low-yield, derivative-covered indices — the S&P 500 and its close relatives — and it is absent from exactly the exposures where the arithmetic says the leak is worst. Condition (vii) narrows it further in the same direction: an index with no exchange-traded futures or options on it fails regardless of how it is built, which excludes most bespoke and niche indices.

Four honest qualifications, and they matter more than the headline:

- **The counterparty prices the advantage.** The swap spread is negotiated. The fund captures some of the withholding benefit; the bank captures the rest. The investor's share shows up in TD, not in a marketing claim — which is another reason TD is the only cost number that settles anything.
- **It is a regulatory arbitrage, not a structural property.** The qualified-index exception is a rule that has already been subject to repeated transitional relief and deferral. If it is narrowed, the advantage disappears **simultaneously for every synthetic US-equity fund**, which is a correlated regime event and not a fund-specific risk. Anything keyed to it needs to be written as an assumption with a named trigger, not as a permanent property of the vehicle (PROD-P3).
- **The test is re-run every year, and the headroom is not large.** Qualification is redetermined on the first business day of each calendar year against the *prior* year's yields, so an index can qualify one year and fail the next with no change to the fund and no announcement from it. On the ~1.05% S&P 500 yield used in section 1 (aggregator, unverified) the cap sits at roughly **1.6%**, and any index whose prior-year component yield exceeds that fails — a low bar for anything carrying meaningful non-US, value or small-cap content. The prior-year yields of the specific indices this vault might use were **not established** in this build. Treat the margin as an annual monitoring item with a number attached, not as a settled property of the wrapper.
- **Counterparty and collateral risk are real but bounded and disclosed.** UCITS caps OTC counterparty exposure (5%/10% of NAV depending on counterparty type, UCITS Directive Art 52(1) — **partial**, the directive text was not read directly), most synthetic ETFs reset far more frequently than the cap requires, and collateral must be diversified with a maximum exposure to any single issuer of 20% of NAV across aggregated baskets (ESMA/2014/937, section XII, read 2026-08-22, **verified**). The question to ask is not "is there counterparty risk" — it is *who is the counterparty, is it the fund's own parent bank, how often does exposure reset, what is the collateral, and who values it.*

### The German interaction that is easy to miss

Teilfreistellung requires the fund to be an **Aktienfonds**, defined as continuously investing **more than 50% of its Aktivvermögen in Kapitalbeteiligungen** *per its Anlagebedingungen* (§2(6) InvStG, read 2026-08-22, **verified**). A swap-based fund whose substitute basket is not equity, and whose investment terms do not commit to that threshold, can therefore hold pure equity exposure economically and still fail the equity-fund test. Many synthetic providers restructured their substitute baskets and investment terms precisely to qualify, but **it is fund-specific and it must be checked in the prospectus/Anlagebedingungen or in the provider's published German tax data, not assumed** (mechanism verified from the statute; any individual fund's status **unverified**). Losing a 30% partial exemption to save 15bp of withholding is a bad trade, and it is exactly the kind of trade that gets made by accident.

## 3. Domicile and withholding tax

**This is the biggest silent return driver available to a European investor, and it is decided before the first euro is invested.** Everything in this section is a framework for *what to check and why it matters*. None of it is tax advice, several items turn on facts specific to Francesco's situation, and every one of them needs confirmation from his own tax advisor before a euro moves.

### The three-layer structure

Tax on a fund holding hits in three places, and they are governed by different law:

1. **Source country → fund.** Withholding on dividends and interest paid by the underlying companies to the fund. Governed by the source country's law and its treaty with the **fund's domicile**. The investor's own residence is irrelevant here.
2. **Fund → investor.** Withholding by the fund's domicile on distributions to the holder.
3. **Investor's residence.** German income tax on the investor.

Layer 1 is the one that leaks, because for a European holder of a European fund it is generally **not recoverable at all** — there is no mechanism by which a German investor reclaims tax the Irish fund paid to the US.

### Ireland versus Luxembourg versus US domicile

- **Ireland (IE).** Irish-domiciled funds access the US-Ireland treaty, whose Article 10(2)(b) caps US tax on portfolio dividends at "**15 percent of the gross amount of the dividends in all other cases**" (US-Ireland income tax convention, general effective date 1998-01-01, treaty text read 2026-08-22, **verified**). Ireland levies no withholding on distributions to non-Irish-resident investors (widely stated, **not verified in this build** — check Irish Revenue guidance or the fund prospectus's tax section). Those two facts together are why Irish domicile is the European default for anything with US equity content.
- **Luxembourg (LU).** Luxembourg funds are generally reported as **not obtaining the reduced US treaty rate available to comparable Irish funds, and therefore suffering the 30% statutory rate on US-source dividends**. The locator is specific rather than general: Article 24(10) of the 1996 Convention provides that Luxembourg holding companies within the meaning of the Act of 31 July 1929 and the Decree of 17 December 1938, "or such other companies that enjoy a similar special fiscal treatment by virtue of the laws of Luxembourg, are not residents", and **Paragraph III.B of the Memorandum of Understanding** reads that phrase as including investment companies within the meaning of the **Act of 30 March 1988** — which is Luxembourg's undertakings-for-collective-investment law (CSSF document page, read 2026-08-22, **verified**). Not a treaty resident means no access to the Article 10(2)(b) 15% cap, hence the 30% statutory rate. (Art 24(10) and MoU para III.B are taken from a named practitioner special report — KPMG, *Tax Notes International*, 2008-07-21, PDF text extracted and read 2026-08-22 — so **partial**: neither the Convention text nor the Memorandum itself was read directly here. Note the locator that does *not* work: Senate Executive Report 105-8 was searched in full on 2026-08-22 and contains none of this.) **One caveat survives and it is not a formality:** the exclusion is drafted by reference to the 1988 Act, which the CSSF's own document page records as **repealed by the Law of 20 December 2002** (verified; the further succession to the Law of 17 December 2010 is secondary, **partial**). Whether the exclusion carries to funds constituted under the successor legislation is a question for the advisor — and either way, the fund's own annual report showing withholding actually suffered remains the per-fund confirmation. At the ~1.05% S&P 500 yield of August 2026 that gap is worth roughly 16bp a year on US equity content; at a 3% yield it is ~45bp. **Verify the domicile before, not after, comparing TERs** — the domicile difference can be several times the fee difference, and it is invisible on every screening tool that sorts by TER.
- **United States (US).** A US-domiciled fund holding US stocks suffers **no** fund-level withholding, and the 15% suffered by a German holder on distributions is generally creditable in Germany under the US-Germany treaty (**partial** — treaty text not read here). That makes US domicile arithmetically the most efficient wrapper for US equities for a German investor. It is nonetheless usually the wrong answer, for two reasons:
  - **Access.** US-domiciled ETFs do not produce a PRIIPs Key Information Document, so EU brokers are prohibited from executing them for retail clients — in force since 2018, with an exemption for clients categorised as professional under MiFID II (industry sources, read 2026-08-22, **partial**).
  - **US estate tax.** Shares in a US-domiciled fund are US-situs assets. An executor for a non-resident non-citizen decedent "must file an estate tax return, Form 706-NA … if the fair market value at death of the decedent's U.S.-situated assets exceeds **$60,000**" (IRS, "Some nonresidents with U.S. assets must file estate tax returns", read 2026-08-22, **verified**). Rates above that threshold are materially higher than most European investors expect and the estate-tax treaty position is a specialist question. Shares in an Irish-domiciled fund are *not* US-situs even when the fund holds nothing but US stocks (**partial** — the situs rule turns on the issuer's residence; confirm with the advisor). **This is the single strongest non-tax-rate argument for Irish domicile and it is invisible in every return comparison.**

### The German layer

Germany taxes fund holdings under the InvStG 2018 regime, and it has three moving parts a fund document must address.

**Teilfreistellung (partial exemption).** For an **Aktienfonds**, 30% of the Erträge are tax-free (the *Aktienteilfreistellung*) where the units are held in **Privatvermögen** by a natural person, rising to 60% for units in Betriebsvermögen and 80% for corporate investors (§20(1) InvStG, read 2026-08-22, **verified**). A **Mischfonds** gets half the equity rate, i.e. 15% for private assets (§20(2), verified). Real-estate funds get 60%, or 80% where the properties are foreign (§20(3), verified). The qualifying thresholds are structural, not economic: Aktienfonds requires **continuously more than 50%** of Aktivvermögen in Kapitalbeteiligungen per the Anlagebedingungen; Mischfonds requires **at least 25%** (§2(6) and §2(7) InvStG, verified). Note the second-order rule: a fund-of-funds counts an equity-fund holding as a Kapitalbeteiligung only to the extent of 51% of its value, and a mixed-fund holding at 25%, unless the terms provide for more (§2(8), verified). The Teilfreistellung is widely described as the legislature's lump-sum compensation for the fund-level foreign withholding that the investor can no longer credit — which, if right, means **it is the mechanism that partly offsets layer 1 above** (rationale **unverified**, not read from the statute; worth confirming because it changes how the two terms should be netted in a return decomposition rather than double-counted).

With Abgeltungsteuer at 25% plus the 5.5% solidarity surcharge = 26.375% (**partial**), the 30% exemption gives an effective rate of about **18.46%** on an equity fund's income and gains for a private investor — before church tax, which adds 8-9% of the tax where applicable (**partial**).

**Vorabpauschale (advance lump-sum taxation).** The mechanism that stops an accumulating fund from deferring tax forever. Base return = the redemption price at the start of the calendar year × **70% of the Basiszins**; the result is capped at the actual increase in redemption price over the year plus distributions, is never negative, is reduced pro rata by one twelfth for each full month before acquisition in the purchase year, and is deemed to accrue **on the first business day of the following calendar year** (§18 InvStG, read 2026-08-22, **verified**). The Basiszins is set annually by the BMF from Bundesbank yield-curve data on the first trading day of the year.

For 2026: "Die Deutsche Bundesbank hat hierfür auf den 2. Januar 2026 anhand der Zinsstrukturdaten einen Wert von **3,20 Prozent** … errechnet", and the 2026 Vorabpauschale is deemed to accrue on **4 January 2027** (BMF letter of 2026-01-13, GZ IV C 1 - S 1980/00230/012/001, PDF text extracted and read 2026-08-22, **verified**). The arithmetic that follows, computed 2026-08-22 on those verified inputs, for an accumulating equity fund in Privatvermögen with no capping and the allowance already used:

> 0.70 × 3.20% = **2.24%** deemed base return → less 30% Teilfreistellung = **1.568%** taxable → × 26.375% = **≈0.414% of the value at the start of 2026**, payable in early January 2027.

Two things about that number that are routinely got wrong in both directions:

- **It is a prepayment, not a permanent tax — and the statute makes it exactly neutral, not approximately so.** "Der Gewinn ist um die während der Besitzzeit angesetzten Vorabpauschalen zu vermindern" — the gain on disposal is reduced by the Vorabpauschalen already taxed during the holding period — and, the sentence that closes the arithmetic, "Die angesetzten Vorabpauschalen sind ungeachtet einer möglichen Teilfreistellung nach § 20 in voller Höhe zu berücksichtigen": they come off the gain **at full amount, notwithstanding any Teilfreistellung** (§19(1) Sätze 3 and 4 InvStG, read 2026-08-22, **verified**). Without Satz 4 a reader netting a 30% exemption on the Vorabpauschale and again on the reduced gain has to argue the legs cancel; with it the identity closes exactly. Written once so it never has to be re-derived — with tax rate *t*, exemption *f*, Vorabpauschalen *V* and raw gain *G*: tax over the life = *t*(1−*f*)·*V* during the holding period **+** *t*(1−*f*)·(*G* − *V*) on disposal = **_t_(1−_f_)·_G_**, identical to an otherwise equivalent fund that never had a Vorabpauschale. (Had only (1−*f*)·*V* been deductible, the holder would permanently overpay *t*(1−*f*)*f*·*V* — which is the version of the rule most people carry in their heads.) The permanent cost is therefore only the **time value of paying tax early**, not 41bp a year of drag. Modelling it as a recurring 41bp expense materially overstates the cost of accumulation.
- **It is regime-dependent, and 2026 is a high-Basiszins year.** The Basiszins was 3.20% for 2026 against 2.53% for 2025 (BMF letters, verified for 2026 / **partial** for 2025 via the 2026 letter's reference line). In years when the Basiszins was zero or negative the Vorabpauschale was nil and accumulation was a pure deferral. **The accumulating-versus-distributing answer therefore changes with the rate regime and must be re-derived, not inherited.**
- Practical mechanics worth checking with the advisor: the bank debits the tax from the settlement account in January, so an accumulating fund can create a **cash requirement with no cash inflow** — a real, if small, liquidity consideration for a fully invested portfolio.

**Distributing versus accumulating.** The Vorabpauschale is reduced by distributions made during the year (§18, verified), so the two converge in a high-rate regime and diverge in a low-rate one. Against that, the **Sparer-Pauschbetrag** of €1,000 for a single person (€2,000 for jointly assessed spouses), with actual Werbungskosten explicitly non-deductible (§20(9) EStG, read 2026-08-22, **verified**), is *use-it-or-lose-it annually* — which is an argument for realising *some* income each year if it would otherwise go unused. The decision rule is therefore not "accumulating always wins"; it is a three-way interaction between the Basiszins regime, the unused allowance, and the intended holding period.

**The standing caveat, stated plainly:** German and EU fund taxation is materially different from the US treatment most English-language fund commentary assumes, it is a real return driver rather than a footnote, and the specifics above — particularly anything touching a specific fund's Aktienfonds status, the netting of Teilfreistellung against fund-level withholding, treaty credits, and estate-tax exposure — **need Francesco's tax advisor to confirm before any of it is relied on for a decision.** This file encodes what to check and why it matters. It does not encode a tax position.

## 4. Structural viability and closure risk

Funds close. Globally, 2025 saw about **500 ETF closures against 2,759 new listings** (ETFGI press release via search, 2025-12, **partial**), and more than 85% of closures since 2021 have been funds under $50m of AUM, reaching about 92% in 2025 (Morningstar analysis via search, read 2026-08-22, **partial**, and US-weighted). Industry practitioners commonly cite $50-100m as the minimum viable size (**unverified** — commentary, not a disclosed provider policy).

Working thresholds for this vault, provisional and to be revised against real cases:

- **Below ~€50m: real closure risk.** Do not start a position without a specific reason.
- **€50-150m: watch.** Acceptable if the fund is over three years old, growing, and from a provider with a broad range.
- **Above ~€500m with a multi-year growth trend: structurally fine** on this axis.
- **Fund age under three years**: no TD history, no evidence of behaviour through a stress event, and a higher closure hazard. Not disqualifying; it is a reason to prefer the older sibling fund on the same index where one exists.

**What closure actually does to the holder, and why it is worse for a German investor than the English-language literature suggests.** The provider announces a termination date, the portfolio is liquidated, and holders receive cash at NAV. There is no capital loss in the naive sense. But:

- **It is a disposal at the provider's timing, not yours.** For a German private investor that crystallises the entire deferred gain, taxed at ~18.46% effective for an equity fund after Teilfreistellung, with previously taxed Vorabpauschalen credited (§19 InvStG, verified). **The deferral you were paying the wrapper to preserve is destroyed by a decision you had no part in.** On a long-held position this is by far the largest cost of closure and it does not appear in any closure-risk discussion written for a US audience.
- Redeployment costs a round-trip spread and possibly a worse entry.
- A merger into a successor fund may be tax-neutral under German rules where conditions are met (**unverified** — §23 InvStG territory; a specific question for the advisor, and a good one to settle in advance rather than in the four weeks a termination notice gives you).

**Provider concentration.** Holding every fund with one provider correlates closure policy, securities-lending policy, lending counterparty selection, and index-provider relationships. That is a real, if slow, concentration. It is not a reason to hold a worse fund; it is a reason to notice.

## 5. Liquidity and execution

### Why the fund's own volume matters far less than it looks

An ETF's shares are created and redeemed on demand: authorised participants deliver (or receive) the underlying basket in exchange for fund shares, which arbitrages the market price toward NAV. The consequence is the most counter-intuitive fact about ETFs and the one most often got wrong — **an ETF with trivial on-screen volume tracking a deeply liquid underlying is a liquid instrument, and an ETF with heavy on-screen volume tracking an illiquid underlying is not.** The relevant liquidity is the underlying's. Screening funds by average daily volume systematically selects for popularity rather than for tradability.

### When the mechanism breaks

It breaks when the arbitrage becomes hard or expensive: illiquid underlyings, closed underlying markets, and dealer withdrawal under stress. The documented episode is March 2020 in bond ETFs. The BIS Quarterly Review's study of bond ETF arbitrage records that "bond ETF prices deviated strongly from their NAVs" in March and April 2020, that "the tracking error of bond ETFs increased to above 200 basis points for some funds", that "extraordinary dysfunction of the market for US Treasuries resulted in deep discounts for ETFs investing in these securities", and attributes this to "impediments to the functioning of the arbitrage mechanism for bond ETFs" arising from the disconnect between creation baskets and actual holdings (BIS Quarterly Review, "The anatomy of bond ETF arbitrage", March 2021, read 2026-08-22, **verified**). Trade-press accounts of a ~5% discount on a large US investment-grade corporate bond ETF in the week to 2020-03-20, flipping to a ~3% premium after the Federal Reserve's 2020-03-23 announcement, are **unverified** here — the direction and rough magnitude are corroborated by the BIS piece; the specific decimals are not.

The interpretive point matters as much as the fact: **a discount to NAV is not automatically an ETF failure.** Corporate-bond NAVs are struck off dealer quotes that go stale in stress, so the ETF's traded price may be the *better* price discovery and the NAV the lagging number. That is genuinely reassuring for a holder who does not sell — and completely irrelevant to one who must. The rule that follows is about behaviour, not about the product: **never plan to raise cash from a fund whose underlying is illiquid, in the moment when everything is illiquid.**

### Execution rules

- **Limit orders always. Never a market order in an ETF.** The one non-negotiable.
- **Do not trade in the first or last ~15-30 minutes of the session.** At the open, underlying constituents have not all printed; at the close, market makers are managing inventory into the auction. Spreads are widest at both.
- **Do not trade when the underlying market is closed.** A US-equity UCITS ETF traded on a European venue at 09:05 CET is being priced off futures and hedging proxies, not off the underlying — the market maker charges for that uncertainty. Same for a Japan or Asia-Pacific fund traded in the European afternoon. The overlap window is the cheap window.
- **Treat the spread as a cost and amortise it over the horizon.** A 10bp round-trip spread on a 5-year hold is 2bp a year; on a position rebalanced quarterly it is 40bp a year. This reframes the whole cost question: **for a long-horizon holder TD dominates and spread is nearly irrelevant; for a frequent rebalancer the ranking can invert.** State the intended horizon before ranking wrappers.
- **Check premium/discount to iNAV before trading, and know the iNAV's limits.** Two requirements that are routinely merged into one and are not the same: a UCITS ETF "should disclose clearly in its prospectus, key investor information document and marketing communications the policy regarding portfolio transparency and where information on the portfolio may be obtained, including **where** the indicative net asset value, if applicable, **is published**" (ESMA/2014/937 para 17), while **how** the iNAV is calculated and **the frequency of calculation** must be disclosed "in its prospectus" — that one, and only that one (para 18) (read 2026-08-22, **verified**). Practical consequence: do not expect the iNAV calculation methodology in the KID. It is a prospectus item. But the iNAV is computed from the last prices of the underlyings — so **when the underlying market is closed, the iNAV is stale and the apparent premium or discount is an artifact.** A persistent one-sided deviation during the overlap window, by contrast, is a genuine signal about basket liquidity.

## 6. Index methodology, and the risk that it changes underneath you

### Who constructs it, and the incentives

Index providers (S&P DJI, MSCI, FTSE Russell, STOXX, Solactive and others) license the index to the fund, and the licence fee sits inside the TER. That produces a real and under-discussed dynamic: **part of the fee war between funds is a fee war between index providers**, and the cheapest funds often track a less-established provider's index. That is not disqualifying — it is a reason to read the methodology rather than assume the brand carries it.

UCITS law constrains what an index may be, and these are checkable primary rules rather than best practice. From ESMA/2014/937 (read 2026-08-22, **verified**):

- An index created and calculated at the request of one or a very limited number of market participants, to their specifications, "should not be considered as being an adequate benchmark of a market" (para 53). **The check for bespoke, provider-commissioned indices.**
- The prospectus "should disclose the rebalancing frequency and its effects on the costs within the strategy" (para 54).
- Indices rebalancing intra-day or daily do not satisfy the replicability requirement (para 55).
- The full calculation methodology must be disclosed, including constituents, calculation, rebalancing methodology, index changes and operational difficulties, free of charge (para 56); constituents **with their weightings** must be published (para 57).
- Selection and rebalancing must rest on "a set of pre-determined rules and objective criteria" (para 58).
- The provider must not accept payment from potential constituents for inclusion (para 59) and the methodology must not permit **backfilling** — retrospective changes to previously published index values (para 60).
- The UCITS must carry out documented due diligence on index quality (para 61).

If a fund's index fails any of these, either the index is not what it appears or the fund is not a UCITS. It is a fast, high-yield screen.

### Rebalancing and the front-running cost

Index changes are announced before they are effective, and index funds must trade at the reconstitution to stay tracking. That predictability is exploitable, and the cost falls on the fund. The magnitude is genuinely contested in the academic literature and **this vault has no sourced estimate** — inventing one would be worse than admitting the gap. What is observable without any external estimate: **compare the fund's TD in periods containing a major reconstitution against periods that do not.** If the drag concentrates there, the cost is real for this fund and this index, whatever the literature says. Prefer, other things equal, indices that rebalance less frequently and that use buffer zones around inclusion thresholds (buffers reduce turnover and reduce the predictability of the trade).

### Capping, and why a capped index is a different exposure

UCITS diversification limits constrain how concentrated a fund may be. An index-replicating UCITS may raise the single-issuer limit to 20% of assets, and to 35% for a single issuer where justified by exceptional market conditions in a market with a highly dominant issuer (UCITS Directive Art 53, **partial** — summarised from secondary sources; the directive text could not be read in this build and should be read before the limits are relied on). This is why capped index variants exist.

The consequence is a live decision, not a technicality: **a capped index is systematically underweight the largest constituents relative to the uncapped index.** In a market where a handful of names dominate — which is the condition that triggers capping in the first place — that is a large active bet, taken by default, that will look like brilliant risk management in one regime and like persistent underperformance in another. If the fund tracks a capped variant, **the exposure framework must underwrite the capped exposure, not the headline market**, and any comparison to a peer on the uncapped index is not a like-for-like wrapper comparison at all.

### Index redefinition — the silent exposure change

The methodology can change under you. Country reclassification (an emerging market promoted to developed, or the reverse), free-float rule changes, eligibility-criteria changes, a shift in the treatment of multiple share classes, or the fund switching index providers outright: each of these can change what you own without any transaction on your side, without a price signal, and without appearing in any performance report until after the fact.

Two defences, both mechanical:
- **At purchase**, read what the prospectus permits: can the fund change its index, on what notice, and with what shareholder rights? A fund that may substitute its index at the manager's discretion is a different object from one that may not.
- **On an ongoing basis**, monitor the index provider's methodology consultations for the specific index. This is a trigger keyed to a third-party publication, so per PROD-T3 it needs a named fallback — here the fallback is the fund's own annual report and the provider's shareholder notices, both of which will eventually carry the change even if the consultation is missed.

### What "the same index" means across providers

It usually does not mean the same thing. Broad developed-market indices from different providers differ in country classification (Korea's DM/EM status is the standing example — **partial**), in constituent count, in small-cap inclusion, in free-float treatment and in rebalancing schedule. Two funds both describing themselves as tracking "the world" can differ by hundreds of names and by several percent of country weight. **Peer comparison must be index-matched before it is wrapper-matched**, and where no index-matched peer exists, say so rather than comparing across indices and calling the difference wrapper quality.

## 7. Securities lending

### The rules

Two instruments govern this, and the file's first version cited only the older one. **ESMA/2014/937 sets what the fund may do**; **Regulation (EU) 2015/2365 (SFTR) sets what the fund must publish**, and the second is the one that turns most of a lending review from a negotiation into a retrieval.

From ESMA/2014/937 (read 2026-08-22, **verified**):

- "**All the revenues arising from efficient portfolio management techniques, net of direct and indirect operational costs, should be returned to the UCITS**" (para 29).
- The prospectus must disclose the policy on the direct and indirect costs that may be deducted from that revenue, "**These costs and fees should not include hidden revenue**", and must identify the entities paid and whether they are related parties of the management company or depositary (para 28). **That last clause is the one to actually use** — in the common case the lending agent is an affiliate of the fund manager, and the disclosure requirement means you can find out.
- "A UCITS should ensure that it is able at any time to recall any security that has been lent out or terminate any securities lending agreement into which it has entered" (para 30).
- Collateral must be diversified, with maximum exposure to a single issuer of **20% of NAV**, aggregated across counterparties, and must come from an entity independent of the counterparty and not highly correlated with it (section XII).

From **Regulation (EU) 2015/2365 (SFTR)** (EUR-Lex consolidated text read 2026-08-22, **verified**), which is the disclosure instrument and is directly applicable law rather than guidance:

- **Article 13** requires UCITS management companies and investment companies to inform investors of their use of SFTs and total return swaps "in the half-yearly and annual reports referred to in Article 68 of Directive 2009/65/EC" (Art 13(1)(a)), and that information "shall include the data provided for in Section A of the Annex" (Art 13(2)). Note *both* reports — this is a twice-yearly obligation, not an annual one.
- **Article 14** requires the UCITS prospectus to specify the SFTs and total return swaps the fund is authorised to use, with a clear statement that they are used, and to "include the data provided for in Section B of the Annex" (Art 14(1)-(2)).
- Article 13 has applied since **13 January 2017**; Article 14 from 13 July 2017 for undertakings established before 12 January 2016 (Art 33(2)).

Securities lending is an SFT, so every ETF that lends is inside this. The consequence for how this file is used is in "what to retrieve" below.

### The revenue split

iShares UCITS ETFs are reported to return **62.5% of lending income to the fund**, with BlackRock retaining 37.5% and bearing the operational costs of the programme (BlackRock product-page disclosure via search, read 2026-08-22, **partial** — the product page returned HTTP 403 to direct fetch, so this figure is relayed rather than read). Splits differ by provider and some providers return substantially all revenue net of direct costs. **The figure above is `partial` only because the report was not read, not because the number is unpublished** — since SFTR the split does not have to be relayed from a provider web page at all: Annex Section A requires the return and cost of each SFT type broken down between the fund, the manager and third parties in absolute terms and as a percentage of overall returns, in the fund's own half-yearly and annual reports. Going to the relayed figure when the mandated one exists is the retrieval failure this file's own posture warns about.

There is a genuine interpretive tension here worth naming rather than sliding past: ESMA says all revenue net of operational costs returns to the fund, and providers operate a percentage split characterised as the lending agent's fee for a service that includes indemnification against borrower default. Both statements can be true — a percentage fee is a way of pricing a cost — but the size of the split is not derived from measured costs, and ESMA has run supervisory work on UCITS costs and fees. **The right posture is to treat the split as a negotiated economic term to be compared across providers, not as a regulatory constant.**

### Why lending can make TD better than TER, and what to retrieve

Lending revenue is additive to fund return and shows up as a smaller (or positive) tracking difference. That is the honest explanation for most "the fund beat its index" claims. It is not free: it converts a small, continuous income stream into a small, discontinuous risk of loss on borrower default with imperfect collateral — a shape that looks excellent in every normal year and is tested only in the year that matters.

**Correcting the framing this file was first written with:** almost none of what follows is a request to a provider. It is a legal requirement in a document published twice a year, and going to look for it is a retrieval task. What to establish before crediting lending income in a return decomposition, with the line that already mandates it:

1. **Percentage on loan.** Annex Section A "Global data" requires "The amount of securities and commodities on loan as a proportion of total lendable assets", plus the amount engaged in each type of SFT and total return swap in absolute terms. Read the denominator carefully — *lendable assets*, not NAV — and note it is a reporting-date figure, so the average-versus-maximum picture is assembled from two documents: the Section B prospectus item requiring the **maximum and expected proportion of AUM** subject to SFTs supplies the ceiling the fund has reserved for itself. An average of a few percent against a prospectus ceiling of 20%+ is a different product from one where the two are close.
2. **The revenue split and the agent's identity.** Annex Section A "Data on return and cost" requires "Data on return and cost for each type of SFTs and total return swaps broken down between the collective investment undertaking, the manager of the collective investment undertaking and third parties (e.g. agent lender) in absolute terms and as a percentage of overall returns". Section B requires the prospectus to state the policy on sharing that return. ESMA/2014/937 para 28 makes the *related-party* question askable; SFTR makes the arithmetic published.
3. **Collateral composition, haircuts, and where collateral is held.** Annex Section A requires type and quality of collateral with maturity-tenor, currency and counterparty-country breakdowns, the "Ten largest collateral issuers across all SFTs and total return swaps", the "Top 10 counterparties of each type of SFTs", and, under safekeeping, the number and names of custodians with the amount each holds. Section B carries the acceptable-collateral and valuation policy. Equity collateral against equity loans behaves very differently from government-bond collateral in a correlated selloff, and the type-and-quality line is where that is visible.
4. **Whether the provider indemnifies the fund against borrower default**, and — this is the part that gets skipped — **whether that indemnity is a contractual obligation of a creditworthy entity or a stated policy.** **This is the one item on the list SFTR does not mandate**, which is precisely why it is the one that has to be asked for, and why an answer given in marketing language rather than contract language should be read as the answer.
5. **Whether cash collateral is reinvested**, and if so into what. Annex Section A requires the "Share of collateral received that is reused" against the maximum specified, and cash collateral reinvestment returns to the fund. This is the mechanism that turned securities lending into a loss centre for some funds in 2008.

The reframing changes what a gap means. Items 1, 2, 3 and 5 are not disclosures a provider may decline to make: a report published after 13 January 2017 that omits them is **non-compliant with a directly applicable EU Regulation**, which is a far harder finding than "the provider is not forthcoming" and is worth stating in those terms in a fund document. Item 4 is the genuine ask, and it is the one PROD-T3 covers — the absence of a metric the industry generally publishes is itself information.

## 8. Share-class and listing multiplicity — identity, and how to record it

The same fund routinely lists on several exchanges, in several currencies, under several tickers. Worked example, read 2026-08-22 (justETF profile, **partial**): the iShares Core S&P 500 UCITS ETF USD (Acc), **ISIN IE00B5BMR087**, trades as **SXR8** on XETRA, gettex and Stuttgart; as **CSPX** on the London Stock Exchange (USD line) and Euronext Amsterdam; as **CSSPX** on Borsa Italiana and SIX Swiss Exchange; and as **CSP1** on the LSE's GBX line. One fund, one ISIN, one NAV, four tickers, three currencies of quotation.

Two distinctions that are constantly conflated:

- **Trading currency is not currency exposure.** Buying the GBP line does not hedge anything. The fund's assets are US equities either way; the quotation currency changes nothing about the risk and only slightly about the FX cost of the trade.
- **Share class is a different fund for tax and identity purposes.** Accumulating and distributing classes of the same fund have **different ISINs**, different German tax treatment (see section 3), and different TDs. A currency-*hedged* class is a genuinely different exposure with its own cost (the hedge rolls, and its cost is the interest-rate differential, which is not in the TER).

### How this vault records fund identity

The architecture keys a fund's folder on a ticker (`funds/{TICKER}/`), and the ticker is the one attribute that is **not** unique. Recording rule, so the vault never ends up holding two folders for one fund:

- **The ISIN is the identity.** Every fund `thesis.md` opens with an **Identity block** carrying: ISIN (canonical), share-class type (Acc/Dist, hedged or not), domicile, legal structure, full name as it appears in the prospectus, the folder ticker chosen and why, and **every** known listing as `{ticker} — {exchange} — {currency}`.
- **The folder ticker is a label, not a key.** Prefer the primary/most-liquid European listing and say so in the block.
- **Before creating any fund folder, grep the repo for the ISIN.** If it appears, the fund already exists under another ticker; extend that folder rather than creating a second one.
- **Sibling classes get one folder, not two,** where the thesis is genuinely the same — with the class difference recorded in the Identity block and any tax or TD difference carried in `valuation.md`. Two folders for two share classes of one fund is a duplicate by another name.

This is the weakest joint in the current fund architecture and it deserves a mechanical gate rather than a convention (PROD-M1: when a step depends on remembering it under pressure, move it into a default that runs by itself). Flagged in Open questions as a proposed lint check: **one ISIN, one folder, repo-wide.**

## Wrapper KPIs

The metrics that actually decide a wrapper choice. Generic fund-screening fields are mostly noise here.

| Metric | What good looks like | What concerning looks like | Why it matters |
|---|---|---|---|
| **Tracking difference, 3-5 year series, year by year** | Small, stable, and explicable from its parts | Volatile, or better than the arithmetic floor with no lending to explain it | The only cost number that captures everything. Disclosure is mandatory in the annual report (ESMA/2014/937 para 11, verified) |
| **TD minus (TER + yield × unrecovered withholding)** | Near zero, or positive and explained by disclosed lending | Large negative residual | The unexplained leak. This is the diagnostic, not TD alone |
| **Domicile** | IE for anything with US content | LU for US-heavy exposure without a stated reason | Worth 15pp of the dividend yield per year, permanently and invisibly |
| **Aktienfonds status per the Anlagebedingungen** | Explicitly >50% Kapitalbeteiligungen | Silent, or a synthetic fund with a non-equity substitute basket | 30% Teilfreistellung (§20(1) InvStG, verified) dwarfs any plausible fee difference |
| **Fund AUM and its trajectory** | >€500m and growing | <€50m, or flat since launch, or step-shaped | Closure forces a taxable disposal at the provider's timing, not yours |
| **AUM concentration in one holder** | Broad; growth is smooth | A single step to most of the fund's size | A seed investor's exit closes the fund. The step in the AUM chart is the tell |
| **Fund age** | >3 years, ideally through a stress event | <3 years | No TD series exists below this. Any chart shown is index history |
| **Replication method and holdings count vs index count** | Stated, and the count matches the claim | "Physical" with a fraction of the constituents and no disclosure | Undisclosed optimisation is an undisclosed active bet |
| **Bid-ask spread, measured during underlying market hours** | Tight and stable; compare to the fund's own typical level | Wide, or only tight at certain hours | A round-trip cost. Amortise over the *intended* horizon before ranking |
| **Premium/discount to iNAV during the overlap window** | Oscillating around zero | Persistently one-sided | One-sided deviation says the creation/redemption basket is hard to source |
| **On-loan proportion and revenue split** | Present in the half-yearly and annual reports, modest, majority to the fund | **Absent** — which is a compliance failure, not a soft signal | Mandatory under SFTR Annex Section A (Art 13, verified). Explains a "good" TD and prices the risk taken to get it |
| **871(m) qualified-index headroom — synthetic funds only** | Prior-year index yield comfortably under 1.5× the S&P 500's prior-year yield, and exchange-traded futures or options exist on the index | At or near the cap, no listed derivatives, or never measured | Failing either test removes the whole withholding advantage at once, for every fund on that index (§1.871-15(l)(3)(vi)-(vii), verified) |
| **Index rebalancing frequency and buffer rules** | Quarterly or semi-annual, with buffers | Frequent, no buffers, or a bespoke index | Turnover is a cost and predictability is a cost |
| **Capping regime of the index** | Uncapped, or capped and deliberately chosen | Capped by default, unnoticed | A capped index is a different exposure and a large active bet |
| **Index-methodology change notices in the last 3 years** | None, or minor and disclosed | Reclassification, provider switch, eligibility rewrite | Your exposure can change with no transaction and no price signal |

## How the wrapper enters the expected-return decomposition

A fund's fair value is an **expected real return range over a stated horizon** (VAL-P1: a range, always, never a point), decomposed so each term is separately falsifiable:

> **Expected real return = starting yield + real growth + valuation change − costs − tax**

This file owns the last two terms and nothing else:

- **Costs** = the tracking-difference-based drag (which already contains TER, transaction costs, unrecovered fund-level withholding and lending revenue — do **not** add TER separately on top of TD, the double count is the most common arithmetic error in this decomposition), plus the amortised round-trip spread over the intended horizon.
- **Tax** = the investor-level German layer: the effective rate after Teilfreistellung applied to realised income and to the eventual gain, plus the time value of Vorabpauschale prepayments, **not** the Vorabpauschale itself treated as a recurring expense (§19 InvStG, verified).

Two honest methodological notes, because this is where a fund valuation is weakest:

- **The decomposition is one lens, not three.** VAL-P3 requires three or more genuinely independent lenses to cluster before acting. A yield-plus-growth-plus-rerating decomposition, a DCF of the same cash flows, and a "what does the current multiple imply" solve are one lens wearing three hats — the same for an index as for a company. The genuinely independent cross-checks available for a fund exposure are things like long-run realised real returns for the asset class, and a replacement/parity check against the alternative wrapper. **Any fund `valuation.md` should state plainly which lenses it actually has and whether they are independent, rather than manufacturing three.** This is a TENSION with VAL-P3, not a satisfaction of it, and should be written as such.
- **The starting-yield term inherits VAL-T1.** A yield computed on a peak-margin year or a trailing twelve months containing a special distribution is an unnormalized denominator, and it makes the whole decomposition wrong in a way the arithmetic will not reveal.

## When does the wrapper lie?

The analogue of the industry frameworks' "when does the multiple lie". Cases where the headline number misleads, roughly in order of how often they bite:

- **TER quoted without TD.** The advertised number excludes withholding tax, transaction costs and lending revenue — the three largest terms in several exposure classes. A fee league table is not a cost league table.
- **TD quoted with the opposite sign convention**, or against a different index variant than the one the peer fund is compared to. Both invert conclusions silently.
- **A "negative tracking difference" presented as manager skill.** It is lending revenue, a favourable net-index withholding assumption, or a sampling bet. There is no alpha in a mechanical tracker; there is only a cost that came out smaller than the sticker.
- **"Physical replication" that is heavily optimised.** The word is true and the picture it paints is not. Count the holdings.
- **A yield figure gross of withholding.** An index's dividend yield is not the yield the fund receives. For a physical Irish fund on US equities, subtract 15% before using it anywhere.
- **A distribution yield on a trailing twelve months containing a special distribution**, or a bond fund's distribution yield used where yield-to-maturity net of costs is the right forward number.
- **Backtested index history presented as fund history.** UCITS rules ban backfilling *published index values* (ESMA/2014/937 para 60, verified) but not the display of simulated index history in marketing material. A performance chart that starts before the fund's inception date is showing you an index, and indices have no transaction costs, no withholding leakage and no cash drag. **Check the inception date against the chart's left edge, every time.**
- **An AUM figure inflated by one seed investor.** A single institutional mandate can be most of a small fund. Read the AUM history for a step rather than a slope, and treat a fund whose size arrived in one day as a fund that can lose it in one day.
- **A promotional or waived fee.** "0.00% TER" is usually time-limited. Credit a fee level only against the actual charged history, not the announcement (CAPA-P2 in its wrapper form: claimed discipline is worth what the multi-year record says it is worth).
- **"Since inception" performance from a fund launched into a bull market.** A short window in one regime, presented as evidence about a machine that will be held across several.
- **A currency-hedged share class compared to the unhedged index.** The hedge cost is the interest-rate differential and it appears nowhere in the TER.
- **An ETC or ETN discussed as though it were a fund.** The wrapper is a debt claim on an issuer. Everything in this file about ring-fenced fund assets simply does not apply.

## Red flags

- **Domicile other than Ireland for an exposure with meaningful US dividend content, with no stated reason.** The default answer is 15% versus 30% of the dividend yield, permanently.
- **The fund's Aktienfonds status cannot be established from the prospectus, Anlagebedingungen, or the provider's German tax data.** A 30% partial exemption is too large to leave unverified.
- **A synthetic fund whose substitute basket is undisclosed**, or whose counterparty is an affiliate of the fund manager with no disclosed reset frequency.
- **A tax advantage that is a regulatory carve-out rather than a structural property** — the synthetic US-equity withholding case is the live example. It can be withdrawn for every affected fund at once.
- **AUM under €50m, or an AUM chart that is a step rather than a slope.**
- **Fund age under three years being compared on performance to a fund with a real record.**
- **An index created to a single sponsor's specification** (explicitly not an adequate benchmark under ESMA/2014/937 para 53, verified) — the tell is a bespoke index name that appears in exactly one fund.
- **An index whose full methodology, constituents and weights are not freely published** (paras 56-57, verified). This is a UCITS requirement; failure to meet it means something is wrong.
- **A prospectus permitting the manager to change the index at discretion** without a shareholder decision or a meaningful notice period.
- **Securities lending with an undisclosed split, an undisclosed maximum on-loan percentage, or cash-collateral reinvestment.**
- **Collateral correlated with the counterparty** — the independence requirement exists for a reason (ESMA/2014/937 section XII, verified).
- **A capped index adopted by default**, where the capping was never surfaced as an exposure decision.
- **Any wrapper decision made by sorting a screener on TER.** The most common failure and the one that produces the most confident wrong answers.
- **Any wrapper conclusion carried across exposures.** The right domicile, the right replication method and the right acc/dist choice all depend on the yield and the tax character of the underlying.

## Decision checklist

Executable mechanically by a fund deep dive. Every figure written down carries its source, date and verification label (PROD-P5).

**A. Identity**
1. ISIN recorded; repo grepped for it; no existing folder holds it.
2. Share class type (Acc/Dist/hedged), domicile, legal structure, full prospectus name recorded.
3. All known listings recorded as ticker/exchange/currency.

**B. Cost**
4. TER from the KID, dated.
5. TD obtained from the annual report where available; otherwise provider table; otherwise aggregator with the sign convention checked and the source labelled.
6. TD year-by-year for 3-5 years, not just the average; dispersion noted.
7. Index variant of the comparison identified (price / gross TR / net TR) and the net variant's withholding assumption checked.
8. Expected TD built from parts (TER + yield × unrecovered withholding + turnover allowance − lending estimate) and compared to reported. **Residual explained or flagged.**
9. Bid-ask spread observed during underlying market hours, and amortised over the intended holding horizon.

**C. Replication**
10. Method stated by the provider.
11. Holdings count compared to index constituent count; sampling identified.
12. If synthetic: counterparty identified, affiliation checked, reset frequency, collateral composition and haircut, and whether the withholding advantage rests on the 871(m) qualified-index safe harbour — recorded as an assumption with a trigger. **Test the two conditions that decide availability rather than assuming them: the index's prior-calendar-year dividend yield against 1.5× the S&P 500's for the same year, and the existence of exchange-traded futures or options on the index (§1.871-15(l)(3)(vi)-(vii)). Re-test annually — qualification is redetermined every January.** On a high-yield exposure, expect the answer to be that the route does not exist.

**D. Tax (all items to be confirmed by the tax advisor before reliance)**
13. Domicile and its treaty position on the fund's largest dividend-source country.
14. Aktienfonds / Mischfonds / other status, evidenced from the Anlagebedingungen or the provider's German tax data, and the resulting Teilfreistellung.
15. Acc vs Dist decision re-derived against the **current** Basiszins and the unused Sparer-Pauschbetrag — never inherited from a prior decision.
16. Vorabpauschale modelled as a prepayment (time value), not as a recurring expense — the netting is *exact*, because §19(1) Satz 4 InvStG deducts the Vorabpauschalen from the disposal gain in full, notwithstanding Teilfreistellung (verified). Do not carry a residual permanent cost.
17. Any US-situs exposure identified and the $60,000 estate-tax threshold considered.

**E. Structure**
18. AUM, its trajectory, and any evidence of single-holder concentration.
19. Fund age; whether it has traded through a stress event.
20. Provider concentration across the whole portfolio noted.
21. Closure consequence written out explicitly for this position: what a forced disposal would crystallise, at what effective rate.

**F. Index**
22. Index provider, methodology document located, rebalancing frequency and buffer rules.
23. Capping regime identified and, if capped, surfaced as an exposure decision to the exposure framework.
24. Methodology changes in the trailing three years; consultation monitoring set up with a named fallback (PROD-T3).
25. Whether the prospectus permits an index change, and on what terms.

**G. Lending**
26. On-loan proportion, revenue split, agent identity and related-party status, collateral policy, indemnity, cash-collateral reinvestment. **Retrieve items 1-3 and 5 from the half-yearly and annual reports (SFTR Art 13 + Annex Section A) and the ceiling from the prospectus (Art 14 + Annex Section B) before asking the provider anything. Record a missing Section A item as a compliance failure, not as a disclosure gap.** The indemnity (item 4) is the only one that is genuinely an ask.

**H. Output**
27. Costs and tax terms handed to `valuation.md` for the expected-return decomposition, with **no double-counting of TER on top of TD**.
28. Wrapper kill switches written with a threshold, a timeframe and an observable that is actually disclosed (PROD-P3) — candidates: AUM below a stated floor for two consecutive reports; TD deteriorating beyond a stated band for two consecutive years; index-methodology change; loss of Aktienfonds status; replication method change.
29. The rejected alternatives recorded with the reason and the condition that would change the answer (PROD-P6). **The passes are the larger half of the record.**

## Common bull-case archetypes

The stories that make an investor pick the wrong wrapper. Each has a documented ancestor; the trap is not restating one, it is acting on it without naming what it ignores.

- **"It has the lowest TER."** The single most common wrapper error. It ignores withholding, lending, spread and tax status — any of which can be several times the fee difference. Killed instantly by comparing TD instead.
- **"It's the biggest and most traded, so it's the most liquid."** Confuses the fund's secondary-market volume with the liquidity of its underlying. The creation/redemption mechanism means a small fund on a liquid underlying is fine, and a large fund on an illiquid underlying is not.
- **"It beats its index, so the manager is adding value."** There is no manager. It is lending revenue, an index-variant artifact, or a sampling bet — and each of those is a risk taken, not a skill demonstrated.
- **"Synthetic is dangerous."** A 2008-2011 European story that hardened into a reflex. Counterparty risk is real, bounded by UCITS limits, collateralised under diversification rules, and disclosed — and on some exposures the synthetic structure is materially cheaper after tax. The honest position is that synthetic replication trades a *disclosed and capped* counterparty risk for a *regulatory-carve-out-dependent* tax advantage. Both halves of that sentence need saying — as does *which* exposures: the qualified-index safe harbour's 1.5×-S&P-500 yield cap (§1.871-15(l)(3)(vi), verified) excludes high-yield indices outright, so the advantage exists on broad low-yield trackers and is unavailable exactly where withholding hurts most. The mirror-image error to "synthetic is dangerous" is **"synthetic is the answer to withholding"**, and it is the one this file was closer to making.
- **"Accumulating is always better for a German investor."** True when the Basiszins is near zero. Much weaker at 3.20%, and wrong outright when it leaves the €1,000 allowance unused. A rate-regime-dependent answer memorised as a rule.
- **"It's a UCITS, so it's safe."** UCITS constrains diversification, liquidity, counterparty exposure, collateral, index quality and disclosure. It says nothing whatever about whether the exposure is a good idea, and nothing about closure risk.

## Common bear-case archetypes

Which wrapper worries are genuine and which are noise.

- **Genuine: an AUM base that arrived in one step and could leave in one step.** The forced-disposal tax event is the real cost and it is not in any risk disclosure.
- **Genuine: an index provider consultation that would reclassify a country or rewrite eligibility.** Your exposure changes with no transaction on your side.
- **Genuine: an illiquid underlying plus a plan to sell into stress.** March 2020 is the documented case (BIS, verified), and the mechanism has not been repealed.
- **Genuine: the loss of a tax status** — Aktienfonds classification, or a withdrawal of the 871(m) qualified-index carve-out. Both are step changes, both are correlated across many funds, and neither shows up in performance until afterwards.
- **Noise: a discount to NAV in an illiquid segment, for a holder who is not selling.** The NAV may be the stale number, not the price.
- **Noise: a few basis points of TER difference between two funds on the same index, when TD is unavailable for one of them.** Ranking on a partial cost measure is worse than saying "could not establish".
- **Noise: a single bad TD year.** One reconstitution or one reclaim settlement. Look at the series.
- **Noise: securities lending as a category.** The question is the parameters, not the practice.

## Provider behaviour patterns

The wrapper analogue of the industry frameworks' "capital allocation patterns" — how the counterparty to your fee actually behaves.

- **Fee cuts are real and they are competitive, not generous.** They follow flows into a rival product on the same index. The observable is the charged fee history, not the announcement (CAPA-P2 in its wrapper form).
- **Providers launch far more funds than they can sustain and prune the tail.** 500 closures against 2,759 launches globally in 2025 (**partial**) is the base rate. A thematic or niche fund from a large provider is a call option the provider is holding, and you are short the strike.
- **Share-class engineering is a tell about who the fund is for.** A fund with an institutional class holding most of the assets and a retail class holding a sliver is a fund whose survival depends on a mandate you cannot see.
- **Lending economics are set at the provider level, not the fund level**, and they rarely change. It is a provider-selection variable more than a fund-selection one.
- **A provider that publishes tracking difference prominently is behaving differently from one that publishes only TER.** Not proof of anything, but it is a cheap signal about which number they expect to be judged on.
- **Index-provider relationships are an economic choice.** A provider moving a flagship fund to a cheaper index licence is cutting its own cost; whether it passes that on and whether the new index is the same exposure are two separate questions, and the second is the one that matters to the holder.

## Providers and sources worth tracking

| Source | What it gives | Limitation |
|---|---|---|
| **The fund's own annual report** | Tracking difference, tracking error, securities-lending detail, collateral, actual charges | Annual; often several months lagged |
| **KID / prospectus / Anlagebedingungen** | TER, anticipated tracking error, index-change permissions, Aktienfonds commitment, iNAV policy | Written to a template; the interesting facts are in the tax and EPM sections nobody reads |
| **Provider website factsheets** | AUM, holdings file, calendar-year fund-vs-benchmark, replication, lending policy | Provider chooses the benchmark variant. Fetching can be blocked (403 observed 2026-08-22) |
| **justETF and similar aggregators** | Fast cross-provider comparison, listings, TD series | Third-party series with an inverted TD sign convention. Needs a named fallback (PROD-T3) |
| **Index provider methodology documents** | Constituent rules, rebalancing, capping, consultations | Free publication is a UCITS requirement (ESMA/2014/937 paras 56-57, verified) — use it |
| **ESMA/2014/937 Guidelines on ETFs and other UCITS issues** | The rulebook this file's structural checks are built on: index quality, collateral, EPM conduct, iNAV and TD disclosure | 2014 guidance, not a Regulation; check for superseding instruments before relying on a paragraph number — SFTR has overtaken it on lending *reporting* |
| **Regulation (EU) 2015/2365 (SFTR), Art 13-14 and the Annex** | The mandatory securities-lending disclosure set: on-loan proportion, top-10 issuers and counterparties, collateral type/quality/maturity/currency/country, reuse and cash-collateral reinvestment, and the return-and-cost split between fund, manager and agent lender — in **both** the half-yearly and annual report, plus the prospectus items in Section B | Directly applicable law, so absence is non-compliance, not reticence. Applies to reports published from 13 January 2017. Says nothing about borrower-default indemnities |
| **InvStG 2018 and the annual BMF Basiszins letter** | Teilfreistellung, Vorabpauschale, disposal-gain adjustment, the year's Basiszins | German law changes; the Basiszins changes every January |
| **BIS / IOSCO / central-bank post-mortems of stress events** | The only rigorous evidence on how the arbitrage mechanism behaves when it matters | Retrospective by construction |

## Mental-model crossover risks

The assumptions from my other frameworks that **do not transfer here**. My existing frameworks are all single-business industry lenses — creative software, branded footwear, managed care, energy, memory semiconductors. Almost none of that machinery applies to a wrapper, and the danger is not that it misfires; it is that it stays silent and the silence gets read as a clean bill.

- **There is no business to analyse, and no management to grade.** Moat quality, capital allocation, incentive design, insider behaviour, competitive position — the entire apparatus that makes the company frameworks work has **no referent** in a wrapper decision. Do not go looking for it and do not manufacture it. The provider is a service counterparty, not an investee.
- **The peer set is other wrappers on the same exposure, never the companies inside the fund.** Comparing a world-equity ETF to the companies it holds is a category error; comparing it to another world-equity ETF on a *different* index is a subtler one (see "What 'the same index' means").
- **MOAT-P4 is the one principle that transfers cleanly, and it transfers hard.** Two funds on the same index are undifferentiated output, so cost position is the only durable advantage. But the cost curve here is TD-after-tax, not the advertised fee — which is exactly the "if you cannot state where it sits on the relevant cost curve, you do not yet have a view" test, applied to a wrapper.
- **A fund cannot be "wrong about a business", so kill switches must be re-conceived.** In a company thesis the kill switches watch the argument. For a fund, the wrapper switches watch **structural integrity** — AUM, TD drift, index redefinition, tax status, replication change — while the *exposure* switches live in the exposure framework and watch the asset class. Two different objects; write them in two clearly labelled groups, and do not let a wrapper switch masquerade as an investment view.
- **ASYM-P2 does not apply as written.** Its downside leg is the bear-case fair value from a company scenario table. A diversified fund has no idiosyncratic bear case of that kind — its downside is the exposure's bear real return, which comes from the exposure framework, not from anything in this file. Size a fund position against the exposure's drawdown history and the portfolio's total exposure to that asset class. Applying the 2:1 threshold mechanically to a fund is importing a company heuristic into a place where its inputs do not exist.
- **ASYM-P1 holds, and holds harder.** Exit only on thesis break, never on price. For a fund the "thesis" that can break is either the exposure case or the wrapper's integrity — and a drawdown in a broad index is the normal operation of the thing, not evidence about it.
- **NARC-M2 is the standing warning for this whole file.** Every heuristic imported from a company framework into a wrapper decision is a claim about a mechanism that mostly does not exist here. When you catch yourself asking "is this a good fund", check whether you mean "is this a good exposure" or "is this a good wrapper", because they have different answers and different evidence.
- **Do not run the Principles check expecting hits.** Most of `principles/` is about businesses, prices and management behaviour. A fund evaluation that surfaces two genuinely bearing principles has done well; one that surfaces eight has manufactured findings, which is worse than none.
- **The precision inverts relative to company work.** In a company thesis the numbers are estimates with wide error bars and the qualitative judgement carries the weight. In a wrapper analysis the numbers are close to knowable — a TER is exact, a treaty rate is exact, a statutory exemption is exact — and the judgement is mostly about which knowable numbers to go and get. **Effort here is retrieval, not inference.** That is a genuinely different research posture and it is why "could not establish" is a much more expensive answer in this file than in a company thesis: it usually means the document was not read, not that the fact is unknowable.
- **Currency: the base currency is EUR and the fund's quotation currency is irrelevant to it.** What matters is the currency of the underlying assets and whether the class is hedged. A GBP-quoted line of a USD-asset fund carries full USD exposure. This confusion is universal and it survives being explained.

## What I've learned over time

Append-only log.

- 2026-08-22 (framework-bootstrap, v1 — built before any fund was evaluated, so read this as a research design rather than as evidence): **the wrapper's cost terms are the only part of a fund decision that is close to deterministic, and they are the part universally decided by the least reliable number.** The advertised TER excludes the two terms that dominate several exposure classes — unrecoverable fund-level withholding tax, and securities-lending revenue — and European rules already mandate the better number: an index-tracking UCITS's annual report must "disclose and explain the annual tracking difference between the performance of the UCITS and the performance of the index tracked" (ESMA/2014/937 para 11, verified). The entire cost section of this file is therefore built on a disclosure that exists, is required, and is almost never used, which is an unusually cheap edge.
- 2026-08-22 (framework-bootstrap, v1 — the finding that most changed this file while writing it): **the withholding-tax term scales with the exposure's dividend yield, so the cost ranking of wrappers is exposure-dependent and cannot be carried across asset classes.** At the S&P 500's ~1.05% yield in August 2026 (aggregator, unverified) the Ireland-versus-Luxembourg domicile gap is worth ~16bp a year; on a 3-4% yielding value, REIT or emerging-market exposure the same rule costs 45-60bp and swamps every fee difference in the league table. This is why a fund deep dive must run this lens *against a specific exposure* and can never conclude "Irish physical is best" as a portable rule.
- 2026-08-22 (framework-bootstrap, v1 — German tax, the correction that matters most): **the Vorabpauschale is a prepayment, not a recurring expense, and modelling it as a 41bp annual drag is materially wrong.** For 2026 the arithmetic is 0.70 × 3.20% Basiszins = 2.24% deemed base return, less the 30% Aktienteilfreistellung, taxed at 26.375%, giving ~0.414% of the year-opening value payable in January 2027 (§18 InvStG and §20(1) InvStG verified; Basiszins verified from the BMF letter of 2026-01-13). But §19 InvStG reduces the gain on disposal by the Vorabpauschalen already taxed (verified), so the true permanent cost is only the time value on the early payment. Both errors are live in the popular literature — one side treats it as a recurring tax, the other ignores it entirely. Note also that it makes the accumulating-versus-distributing answer **rate-regime dependent**: near-zero in a zero-Basiszins year, materially different at 3.20%.
- 2026-08-22 (framework-bootstrap, v1 — the trap I expect to catch me first): **tracking-difference sign conventions are not standardised, and a comparison built on two sources with opposite conventions inverts silently.** This file pins the vault convention (fund minus index, so negative is a cost) and requires the convention to be stated next to every TD figure written into a fund document, because the error is undetectable when both funds sit near zero and catastrophic when they do not. The same shape of error lives in index variants: a fund compared against a *net* index whose withholding assumption is worse than the fund's own treaty position will appear to beat its benchmark year after year with no skill involved.
- 2026-08-22 (framework-bootstrap, v1 — honest gaps carried forward, so the next run does not assume they were closed): four things this build could not establish. (1) **No tracking-difference dataset of any kind** — the "defensible TD range by exposure class" the assignment asked for is deliberately absent rather than invented, and the provider page that would have supplied the first real series returned HTTP 403. (2) **No primary read of the UCITS Directive itself** — the Art 52 counterparty limits and the Art 53 index concentration relief (20%, and 35% for a dominant issuer) are carried at `partial` from secondary summaries and should be read before either is relied on. (3) **No primary read of the 871(m) regulation** — the qualified-index carve-out that the whole synthetic-replication tax argument rests on is sourced from practitioner commentary. (4) **No verification of any specific fund's German Aktienfonds status**, which is the single highest-value per-fund tax check in this file. All four are retrieval problems, not analysis problems, which is exactly the posture this lens predicts.
- 2026-08-22 (independent audit of v1, applied same day — four repairs, and the one that changes a recommendation): **the file's own diagnosis of where withholding hurts most identifies exactly the exposures where its proposed fix is legally unavailable.** §1.871-15(l)(3) was read in full this time rather than relayed from practitioner commentary, and the qualified-index safe harbour requires — alongside 25+ long components, the 15% single and 40% top-five weighting caps, predefined rebalancing, and listed futures or options — that the index "did not provide an annual dividend yield in the immediately preceding calendar year … greater than 1.5 times the annual dividend yield of the S&P 500 Index" (verified). A 3-4% yielding value, REIT or emerging-market index fails that cap outright. So synthetic replication is not a general answer to withholding drag; it is available on broad low-yield trackers and absent precisely where the leak is largest, and qualification is re-tested every January against the prior year's yields. **The general lesson for this vault: when a framework offers a fix for a problem it has just sized, read the fix's eligibility conditions before the fix's benefits.** Three smaller repairs from the same audit: the securities-lending section was built on ESMA/2014/937 alone and never named **SFTR** (Regulation (EU) 2015/2365), whose Art 13 has mandated the Annex Section A dataset — on-loan proportion, top-10 issuers and counterparties, collateral type/quality/maturity/currency/country, reuse, cash-collateral reinvestment, and the return-and-cost split between fund, manager and agent lender — in *every* half-yearly and annual report since 13 January 2017 (verified), which means the file was framing a retrieval task as a negotiation and treating a compliance failure as a soft signal; ESMA/2014/937 paras 17 and 18 had been merged, so the iNAV *calculation methodology* was wrongly said to be a KID item when para 18 puts it in the prospectus alone (verified); and §19(1) **Satz 4** InvStG was missing, which is the sentence that makes the Vorabpauschale prepayment net *exactly* rather than approximately — the netting identity is now written out so it is demonstrated rather than asserted (verified).
- 2026-08-22 (same audit — the finding that did not survive checking, recorded because a corrected locator is worth more than a corrected label): **the Luxembourg 30% claim was challenged as being locatable in the Notes to the 1996 Convention via Senate Executive Report 105-8, and it is not.** Sen. Ex. Rept. 105-8 was searched in full and contains none of it. The actual chain is **Article 24(10)** of the Convention — which *is* in the limitation-on-benefits article, contrary to the audit's premise — excluding 1929 holding companies "or such other companies that enjoy a similar special fiscal treatment", extended to investment companies within the meaning of the **Act of 30 March 1988** by **Paragraph III.B of the Memorandum of Understanding**, the 1988 Act being Luxembourg's undertakings-for-collective-investment law (CSSF, verified). The claim stays at `partial`, not `verified`: both provisions were read through a named practitioner report rather than from the Convention or the Memorandum themselves, and the 1988 Act was repealed by the Law of 20 December 2002, so whether the exclusion carries to funds under the successor law is genuinely open. **A `verified` label is about what was read, not about how confident the conclusion feels** — and an audit that is right about the substance can still be wrong about the citation, which is why the citation gets checked separately from the claim.

## Open questions

- **A wrapper-cost asymmetry principle.** A certain, compounding, knowable drag paid against an uncertain return is a distinct decision shape, and no item in `principles/` currently states it — the ASYM items address entry price and position size. Candidate for a new principle once a second instance shows the theme is real (per the "do not create a file for a single orphan idea" rule in `principles/README.md`). Parked deliberately rather than forced onto an existing ID.
- **ISIN-uniqueness lint.** The fund tier keys folders on ticker, and ticker is the one non-unique attribute of a fund. Proposed gate: one ISIN, one folder, repo-wide, checked mechanically from the Identity block. Until it exists this is a convention that depends on remembering it (PROD-M1 says that is not a fix).
- **Does Teilfreistellung actually compensate fund-level withholding, and if so how should the two be netted?** If the 30% exemption is the legislature's lump-sum offset for unrecoverable foreign withholding, then subtracting *both* the full withholding drag and applying the full effective rate double-counts. This changes the expected-return arithmetic and is currently unresolved. **Narrowed 2026-08-22:** the *Vorabpauschale* half of this question is settled by §19(1) Satz 4 InvStG (verified) — the Vorabpauschalen come off the disposal gain in full, notwithstanding Teilfreistellung, so the prepayment nets exactly and no residual permanent cost belongs in the decomposition. What remains open is the separate and larger question of whether Teilfreistellung is the legislature's lump-sum offset for unrecoverable **fund-level foreign withholding**. That one is unresolved and still needs the statute's rationale or the advisor.
- **Distributing funds and the Sparer-Pauschbetrag.** Is there a portfolio-level design in which one small distributing holding is deliberately used to consume the €1,000 allowance each year while the core stays accumulating? Plausible, unmodelled, and needs the advisor.
- **What is the right independence test for the valuation lenses on a fund?** VAL-P3 wants three genuinely independent lenses; a fund's decomposition is one lens with three terms. Until this is resolved, fund valuations should declare a failed cluster honestly rather than manufacture agreement.
- **Whether ESMA/2014/937 has been superseded in whole or part.** Every structural check in this file cites it. It dates from 2014, and a follow-up peer review exists. The paragraph numbers should be re-validated against current guidance before the next fund deep dive. **Partly answered 2026-08-22:** on the *reporting* of securities lending, SFTR is the later, stricter and higher-ranking instrument — Art 13 has required the Annex Section A dataset in both the half-yearly and annual report since 13 January 2017 (verified), against para 35's much thinner annual-report list. Treat SFTR as the operative source for lending disclosure. What could **not** be established is whether ESMA formally treats para 35 as superseded rather than merely overtaken; the Q&A and compliance-table search on 2026-08-22 found no such statement, so both are cited side by side rather than one being deleted. The rest of the guideline — index quality, collateral, iNAV, TD disclosure — is untouched by SFTR and the original question stands for those paragraphs.
- **No fund has been evaluated through this lens yet.** Everything above is a design; the first real fund will find the joints. The first three entries in "What I've learned over time" after a real evaluation are worth more than the rest of this file.
