# SNDK — investment thesis

> Append-only. Date every update. Old thinking matters.

**Created:** 2026-07-30
**Last updated:** 2026-08-22 (refresh)
**Sector:** `../../primer.md`
**Framework:** `../../../../frameworks/memory-semiconductors.md`

**Data sourcing:** prices and market-derived figures from yfinance pulled 2026-08-21 22:36-22:41 UTC (official close of 2026-08-21), USD, per "Price and data sourcing (canonical)". Company figures from SEC filings read directly (FY2026 10-K filed 2026-08-17; Q4 FY2026 8-K and earnings deck 2026-08-05; prior filings per the initial entry) and from the **Q3 and Q4 FY2026 earnings-call transcripts, read in full** (fool.com, cross-checked against a second host) — the transcript gap named in the initial thesis is closed. The Investor Day (2026-08-13) rests on its official press release plus secondary coverage, `partial`; its full transcript sits behind Seeking Alpha's paywall. Scenario numbers are canonical in `valuation.md` per VAL-P5.

---

## What the business does

SanDisk sells NAND flash memory — and, functionally, nothing else. Enterprise and client SSDs, embedded flash, and retail cards across three end markets: Datacenter (25.4% of FY2026 revenue and the only place bits grow), Edge (60.1%), Consumer (14.5%). It owns no fab. Its entire manufacturing base is a 49.9% interest in three JV entities ("Flash Ventures") held with Kioxia across eight fabs at Yokkaichi and Kitakami: **Kioxia owns the buildings**, each parent takes about half the output at cost plus a small markup, SanDisk owes half of all JV fixed costs regardless of output taken, must fund ~half of JV capex when JV cash flow is short, and is contractually **barred from manufacturing flash itself**. All three JVs now co-terminate 2034-12-31, extended 2026-01-29 alongside a $1.2bn payment to Kioxia over 2026-2029 for "continued availability of supply" (10-K Note 10, `verified`). Separated from Western Digital 2025-02-21.

What changed in FY2026 is not the structure but the *commercial regime*: revenue $20,248M (+175%, on a 53-week year), and more than half of forward volume is now sold under multi-year "New Business Model" agreements the 10-K says are "expected to become our predominant way of doing business." Read against the framework's navigator, SanDisk is still the purest listed expression of commodity NAND plus enterprise SSD — the two structurally worst rows — but it is now that asset **with a contracted book bolted on**, and the whole investment question is which of those two facts dominates.

## The bull case

Framework-grounded, each point load-bearing, updated for what is now verified.

1. **Datacenter is real volume in a price-driven year.** FY2026 Datacenter revenue $5,153M (+437%) on exabytes up "almost 120%" with revenue/GB up "almost 150%" (10-K MD&A, `verified`); fiscal Q4 alone $2,977M, +103% QoQ (8-K, `verified`). Datacenter bits went from 25% of the portfolio in fiscal Q3 to 38% exiting FY2026 (Q3/Q4 calls, `verified`). The AI-inference buyer funds storage from an accelerator budget — the least price-elastic customer NAND has ever had.

2. **The contracted book now has verified floors, quantified margins, and scale.** CFO, Q4 call, verbatim: NBM pricing "include[s] both fixed and variable elements with a variable portion subject to floors and ceilings"; "we expect attractive margins even at floor pricing"; and in Q&A, NBM gross margin confirmed at "around 80%... there is some upside as prices continue to go up" (`verified`, transcript). Total minimum contracted revenue **$93.9bn at floor pricing** across 8 customers; RPO $59.8bn at year-end, $91.1bn including two post-quarter signings ($31.3bn, 10-K subsequent events, `verified`); **>50% of FY2027 bits and ~2/3 of FY2028 bits committed** (Q4 call, `verified` — slightly stronger than the deck's "~1/2"). Terms hardened fast: at the Q3 call management refused any margin target; one quarter later it named ~80%. The framework's trait #7 — selling forward at the top trades peak upside for trough survival — executed at industry-first scale.

3. **The balance sheet and the print.** Zero debt, $4,762M cash, revolver undrawn; FY2026 GAAP operating income **+$12,389M** after three consecutive loss years; FCF $11,494M (10-K, `verified`). Q4 GAAP gross margin 84.6%.

4. **Management guided a three-year model that, if real, ends the cycle as a phenomenon**: FY2028-30 revenue growth mid-to-high teens consistent with bit growth, non-GAAP GM ~80%, operating margin ~75%, adjusted FCF margin ~50%, and **100% of excess cash returned** (Investor Day release 2026-08-13, `verified` from the PR; the model's basis is management's own). Kioxia — the JV partner whose capex is SanDisk's supply — reaffirmed ¥470bn/yr average capex for FY2026-28 on 2026-08-03 and announced an ¥800bn buyback instead of new fabs (`partial`).

5. **Supply-side discipline was tested in Q&A and held.** Pushed by Morgan Stanley to accelerate capex while competitors pivot fabs to DRAM, management declined: "we continue to execute the plan that we had" — FY2027 capex ~6% of revenue, bit growth deliberately trimmed to mid-teens to hold NBM inventory buffers (Q4 call, `verified`). That is the opposite of the peak-capex reflex that has broken every prior cycle.

## The bear case

Steelmanned, and still the case with the deeper evidence base. Updated where the record moved.

1. **FY2026's revenue was price.** +175% revenue on mid-teens exabyte growth; Edge bits up only high-single-digits with revenue/GB up ~180%; Consumer bits *down* mid-teens (10-K MD&A, `verified`). Elasticity is already visible where the buyer can refuse. Prices this far above cost have summoned supply nine times in forty years.

2. **The supply response is assembling — from outside the discipline club.** TrendForce's standing forecast (2026-07-21, reaffirmed 07-30, no newer release as of 2026-08-22): NAND supply outgrows demand in 2027, balance turns 2H27, Chinese suppliers ~19% of global bits by 2027. YMTC reached **14% global shipment share in Q2 2026 — #3, ahead of Kioxia** — with a third Wuhan fab expected in production by end-2026 (`partial`, Counterpoint). Q4 2026 contract-price momentum is converging (TrendForce, direction only). And SanDisk was the **slowest-growing of the top five NAND vendors in Q2** (+50.7% QoQ vs Micron's +99.2%, `partial`) — the JV is monetizing this cycle less aggressively than peers. Management's own claim that bits stay on allocation "beyond calendar year 2027" (Q4 call, `verified` as a statement) is now in explicit, dated disagreement with the industry's forecaster.

3. **The floor regime is disclosed in decks, not in the audited record — and the cushion shrinks under audit.** The 10-K never uses the words "floor," "ceiling," or "minimum pricing"; its language is "pricing mechanisms consisting of fixed and variable components... supported by financial guarantees" (`verified`). The deck's $16.5bn of guarantees resolves, in the audited filing, to **$5.0bn of third-party collateral accessible only on default or breach, $1.5bn of refundable customer deposits, and $1.24bn of contract liabilities — ~$7.7bn identifiable**, against $93.9bn of claimed minimums. The risk factor concedes guarantees "may not fully offset such lost revenue depending on... when during the contract term the customer's failure to perform were to occur," and **discloses no renegotiation mechanics at all** (`verified`). No analyst on either call obtained the floor level, the fixed/variable split, or a customer name.

4. **The cycle is this company's own filed record, and the fixed-cost machine runs both ways.** GAAP operating losses of $2,035M / $468M / $1,377M in FY2023-25; gross margin as low as 7.1%. Flash Ventures under-utilisation charges, audited: **$249M (FY2024), $75M (FY2025), $11M (FY2026)** (10-K Note 10 — correcting the initial thesis, whose "$24M in 9M FY25" was FY2025's *inventory write-down*, a different line). Goodwill of $4,994M — 36% of equity — has been impaired twice. Half of JV fixed costs are owed regardless of output; total material cash requirements $11,760M including $6,559M of Flash Ventures commitments and now $5,892M of Nanya DRAM purchase commitments through FY2031 (`verified`).

5. **FY2026's cash and earnings quality carries one-offs the multiple is capitalizing.** ~$4.0bn of FY2026 operating cash flow was NBM customer deposits/advances and unpaid taxes; cash taxes paid were $146M against $1,584M of expense, with a **~$1.4bn catch-up due in FY2027** and 15% CAMT from FY2027 (10-K, `verified`). The Nanya stake added an $808M unrealized, non-operating gain to net income. The 53-week year flattered every YoY rate. And receivables concentrated sharply: three customers now hold ~19%, 12% and 10% of the $4.7bn AR book (`verified`) — the contracted book concentrates counterparty risk even while no customer crosses 10% of revenue.

6. **The price is paying for the model, not the print.** The market sold the record Q4 (−10% over two sessions, with Citi, Evercore and Wells cutting targets into it) and then bought the Investor Day model (+22% over two sessions). FY2028 consensus — where the upgrades landed — spans **$173 to $361 of EPS** across 19 analysts. At 1,596.08 the price embeds, solved backwards at 8x EV/EBIT with 15-21% tax, permanent EPS of $154-166: **fiscal Q4 annualized, forever** (valuation.md cross-check 1).

## Capital allocation track record

Eighteen months public. The table's FY2023-25 rows remain carve-out blanks (see initial entry). What is new is that the record now contains **decisions at scale**, and they grade both ways:

- **The buyback went from press release to $4.5bn executed in one quarter** — 2.836M shares at ~$1,512 average (10-K, `verified`), roughly 14x reported and **~20x tangible book**, near all-time-high prices, with pace described only as "very consistent" and no price-sensitivity discipline stated when asked (Q4 call, `verified`). A further $14bn was authorized 2026-08-05 ($15.5bn remaining). CAPA-P1 judges a repurchase by the multiple paid, and its energy-framework dissent says the top-of-cycle instrument is distribution, not repurchase. Management chose repurchase and explicitly deprioritized dividends as "less tax efficient" (Q4 call). This is the single largest capital decision in the company's short life, and it is a peak-multiple purchase of its own stock — defensible only under the bull case's own premise that the cycle is over.
- **Debt retirement (FY2026) remains the one unambiguously correct move.** Term Loan B settled 2026-03-04 from cash.
- **Nanya**: $970M remitted 2026-04-08, marked at $1,777M at year-end (locked up three years), plus $5.9bn of DRAM purchase commitments — a supply hedge that is also a top-of-its-own-cycle purchase with a coupon of obligations attached.
- **Tax catch-up ahead**: FY2027 operating cash flow inherits ~$1.4bn of FY2026's accrued-but-unpaid taxes; FY2026 FCF is not the run rate.

**Read: still unknown-not-clean per CAPA-P2 — but no longer for lack of data points.** The points now exist; what does not exist is a downturn to grade them against.

## Management quality

Transcripts for Q3 and Q4 FY2026 read in full — the gap the initial thesis carried is closed. What they show:

- **Direct on mechanics, disciplined on disclosure.** Management answered structure questions precisely (fixed/variable term shape, guarantee custody, release timing) and refused, consistently, the floor level, the split percentages, and customer names — across twelve analysts on the Q4 call, nobody extracted them. The two hardest questions (Bernstein on whether the light Q1 guide reflects conservatism; Morgan Stanley on accelerating capex) received process answers, not numbers.
- **The pricing-power arc is visible across one quarter**: Q3, "I do not think we are there yet to talk about a target"; Q4, NBM margins "around 80%" with upside capture. Terms hardened as the queue lengthened — customers "coming back for the second round of NBMs a quarter in" (Q4 call, `verified`).
- **Insider posture shifted from "no exit signal" to "orderly exit plans."** 10b5-1 plans adopted in fiscal Q4: CEO Goeckeler up to 124,192 shares (~24% of his 509,903, expires 2027-09-30), CFO Visoso up to 11,000, CTO Ilkbahar up to 6,270 (after cancelling a prior plan unsold) (10-K Item 9B, `verified`). Since 2026-07-02 the only filed sales are the CLO's 600 shares at $2,088 and 600 at $1,162. Plans are not sales, and the sizes are moderate — but the direction of stated intent changed, and the initial thesis's "no open-market sale" line is now dated. WDC's residual ~1.7M shares are being monetized by end of calendar 2026 (`verified`) — a known, finite overhang.
- **Comp**: the maxed-out Launch Grants remain the plan of record; no replacement mega-grant appears in the 10-K (Part III defers to the unfiled proxy). Alignment still rests on the CEO's holding, now with a sale plan attached to ~a quarter of it.
- The Goeckeler line that best captures the register of the moment: "I feel like I've finally gotten to the starting line of where the real value creation is going to happen" (Investor Day, `partial`).

## What would change my mind

Rewritten for the next window: the Q1 FY2027 print (~early November 2026; the quarterly exabyte/ASP-per-GB decomposition returns with the Q1 10-Q — the FY2026 10-K disclosed it only annually) and the FY2026 proxy. Per PROD-P1, written before the events; per PROD-T3, keyed to issuer disclosures with third-party series as corroboration only.

**Bull-case kill switches** — any one says the case for ever owning this is broken:

- **ASP per gigabyte down QoQ in MD&A for two consecutive quarters** with exabyte growth insufficient to hold revenue flat. (The first down-ASP quarter is not a kill — it is the floor regime's first real test, and per the bear-side switch below it may *strengthen* the case if margins hold.)
- **Flash Ventures under-utilisation charges reappear in the related-party note in any quarter, at any amount.** FY2026's audited figure was $11M; the clean baseline is now zero.
- **GAAP gross margin below 55% in any quarter through FY2027.** With >50% of bits contracted at ~80% NBM margins, a blended print below 55% arithmetically requires either a spot collapse beyond the FY2023 experience or the floors not performing as described — either kills the bull case as stated. (Below 65% in any quarter: WATCH, not a kill.)
- **Any NBM customer dispute, renegotiation, termination, or guarantee draw disclosed, at any size.** The regime's first crack is the switch; the 10-K discloses no renegotiation mechanics, so any appearance of them is new information by definition.
- **Kioxia guides average capex above ~¥470bn/yr, or announces any new fab or shell-fill with stated production before 2029** in a primary release. Reaffirmed at exactly that level 2026-08-03 — not fired.
- **The exabyte/ASP decomposition disappears from quarterly MD&A for two consecutive quarters** (PROD-T3: the metric's disappearance is itself the trigger).
- **Any equity issuance, a drawn revolver, or suspension of the remaining $15.5bn authorization.**

**Bear-case kill switches** — any one says the bear case is wrong and NAND has genuinely re-based:

- ~~Floor pricing disclosed on at least a third of FY2027 bits~~ — **FIRED 2026-08-05** (deck + Q4 call: floors and ceilings, >50% of FY2027 bits, $93.9bn minimum; graded in the 2026-08-22 update entry). The successor switch: **the floor LEVEL disclosed, in any document, at a level implying blended gross margin ≥40% in a spot collapse.** That is the remaining half of the original unknown.
- **A full quarter of ASP/GB down QoQ in MD&A with GAAP gross margin held above 65%** — the floor observed working, not just described.
- **Exabytes +15% YoY for two consecutive quarters with ASP/GB flat or down** — real volume growth at normalizing prices.
- **GAAP gross margin ≥50% for four consecutive quarters including at least one down-ASP quarter** — the framework's "new higher band" test, unchanged.

## Principles check

Routed by `**Scope:**` line via `../../../../principles/README.md`; all six themes read 2026-08-22. Advisory only per "Principle authority (canonical)". Staleness per "Stale principle (canonical)": no file stale; the open SNDK flag (journal/_flagged.md, 2026-08-22) is the flag this refresh discharges.

- VIOLATES VAL-P3 — Owner's own framework, `valuation-discipline.md`, cluster tolerance ~1.33x — the refreshed lenses span **$475 to $2,200, a 4.6x spread** (improved from July's 7.8x, still a recorded failure); the conservative lens is named in valuation.md and the Conviction section answers this line.
- ALIGNS VAL-T1 — Owner's own analysis, framework "When does the multiple lie?" sections — the market price equals **fiscal Q4's EBIT annualized in perpetuity at 8x** (valuation.md cross-check 1, with tax); a 7.45x forward P/E on peak-year consensus remains the top's signature, not a bargain, and naming the denominator is still what sets the verdict.
- TENSION CAPA-P1 — Owner's own analysis, `capital-allocation-signals.md`, judge a repurchase by the multiple paid — **$4.5bn executed at ~$1,512/share, roughly 20x tangible book, at a cycle peak**, with management stating pace-consistency and no price discipline when asked; CAPA-P1's standing energy dissent says the top-of-cycle instrument is distribution, not repurchase, and management chose repurchase while deprioritizing dividends.
- TENSION MOAT-P4 — Owner's own analysis, `business-quality-and-moats.md` — cost-per-bit rank is still not separable from Kioxia's fabs and no supplier discloses it; the item's precondition for a quality view remains permanently unmeetable here; unchanged from July and unaffected by the print.
- TENSION NARC-P1 — Owner's own analysis, `narrative-and-cycle-models.md`, confirming fundamentals do not resolve a narrative — the market **sold the record print (−10% in two sessions, three target cuts into it) and bought the management model (+22% in two sessions a week later)**; the debate moved from this year's earnings to the FY2028-30 model, which is not falsifiable before FY2028.

## Conviction

**Level (1-5): 2** (raised from 1; PASS stands)

**Why 2 and not 1.** The initial conviction 1 carried two binding gaps: no transcript ever read, and a valuation whose single most-moving input (floor existence) was unknown. Both closed. The transcripts are read; the floors exist, at verified scale, with an ~80% NBM margin quantified by the CFO in Q&A; and the trough anchor the bear case rests on is now verified from primary filings rather than borrowed unverified. The evidence base under this thesis is categorically better than it was on 2026-07-30.

**Why 2 and not 3, and why the verdict is still PASS.** First, the price: fair value is $475 / $875 / $2,200, probability-weighted ~$1,090 (valuation.md, canonical). At 1,596.08 the upside to base is **−45%** and the ASYM-P2 numerator is **negative** — there is no size at which the standardized reward-to-risk supports entry, so the franchise debate never reaches the sizing question. Second, the VIOLATES line answered rather than obeyed: the 4.6x lens spread means the range is still not decision-grade; the conservative lens (distributions plus a 9x terminal on normalized-down earnings) is the only one resting entirely on verified history — memory bottoms near 1.0x book, and no NAND long-term agreement has ever been tested through a collapse. The bull lens rests on a management model announced nine days ago and a floor whose level is a secret. Third, the two facts that moved *against* the name since July: YMTC at #3 with new bits arriving before 2029, and the largest capital decision of the company's life being a ~20x-tangible-book repurchase with stated indifference to price.

**What is genuinely stronger on the bull side, said plainly.** The floor disclosure was the bear's best single risk and it landed against the bear. Zero of eight bull-side switches fired at a print that beat its own guide by ~25%. Kioxia chose a buyback over fabs. If the FY2028-30 model is even approximately real, today's price is cheap — our bull case now sits at the street's mean target, and the street's mean is +33% above the close. The honest statement of the position: **this went from "priced beyond even the regime-change case" in July to "priced between the base and the regime-change case" in August.** That narrows the miss if the PASS is wrong, and the PASS is likelier to be wrong here than it was three weeks ago. It stands anyway, because a negative reward-to-risk at the current price is not a judgment call under this vault's rules.

**What I still do not know, because it bounds the above:** the floor level (nowhere, including the audited 10-K); whether floors survive a tested downturn (contracts <2 years old, identifiable audited cushion ~$7.7bn against $93.9bn of minimums); the Investor Day Q&A (paywalled transcript — the one remaining unread primary); and SanDisk's own trough behavior under the NBM regime, which has no precedent to measure.

## Position sizing logic

**0%.** Unchanged. Entry requires all three, per valuation.md's bands: price below the $875 base case; the floor level disclosed **or** one full quarter of ASP/GB down with gross margin held (the floor observed, not described); no NBM dispute on record. First tranche capped at 1-2% per ASYM-T2 and the framework's memory cap — this industry has produced −81.7% and −98.2% drawdowns and one 21.5-year recovery, and SanDisk remains the structurally worse half of a two-industry sector. The distance to a defensible entry compressed from ~70% below the July price to ~45% below today's plus one disclosure; that is what the fired switch bought, and it is not enough to act on.

## Update log

### 2026-07-30 — initial thesis

Initial write-up. Price 1,249.44 USD (yfinance, 2026-07-30 18:37 local); market cap $185.0bn; 148.1M shares; net cash. Stock is +2,780% over one year, -46% from its 2,354.39 high, and **one session off a 1,015.89 capitulation low struck 2026-07-29** — the reference price is not a settled level and the fair value band is written against a violently two-way tape.

Thesis: SanDisk is the purest listed NAND asset, in the sub-sector the framework rates structurally worst, at a moment when its revenue is up 251% year over year on **flat exabytes and ASP per gigabyte up 248%**. Three consecutive years of GAAP operating losses ended fourteen months ago. The industry's own forecaster published, nine days before this write-up, that NAND supply growth outpaces demand in 2027 with the balance turning positive in 2H27. The bull case — Datacenter mix, a $41.6bn contracted book, zero debt and $4.4bn of nine-month free cash flow — is real and is priced several times over.

Fair value **$200 / $400 / $1,560** (bear/base/bull), probability-weighted ~$552, built on price-to-forward-book with normalised mid-cycle earnings and a solved-backwards implied-expectations lens as cross-checks. `valuation.md` is canonical for these numbers per VAL-P5. The lenses fail VAL-P3's cluster tolerance by a wide margin and the valuation says so rather than averaging it away. Conviction **1**. Size **0%**.

Two data-integrity findings that bear on anything built off vendor data for this name, both reconciled to the filings: (1) the reported operating margin of 69.98% sitting *above* a 56.04% gross margin is a **period mismatch**, not a business anomaly — the first is the latest quarter normalised, the second is trailing twelve months, and the GAAP figure (operating income $4,111M on revenue $5,950M = **69.1%**) reconciles as 78.4% gross margin less 8.4% opex with no JV income involved; the equity-method Flash Ventures result is a **loss** ($58M in 9M FY26) and sits below the operating line anyway. (2) The vendor's annual "operating income" row is **not GAAP** — it reconciles to the filed figures only after adding back the $1,830M impairment, separation and termination costs and netting a divestiture gain, so FY2025's "+$0.51bn" is a filed operating **loss of $1,377M**. Vendor enterprise value is understated by ~$34bn (reported $146.9bn against ~$181.5bn reconciled from market cap less cash plus debt), so every EV multiple derived from it is ~24% too low.

Principles check run against all six themes: 1 VIOLATES (VAL-P3, cluster failure), 1 ALIGNS (VAL-T1, and it is what sets the verdict), 3 TENSION (MOAT-P4 cost-curve position unknowable through the JV; CAPA-P2 seventeen months is not a record; PROD-T3 leading series are third-party and had to be re-keyed to issuer disclosure).

Known gaps carried, not netted out: no earnings-call transcript read for any of the last four quarters (the `company-deep-dive` step-3 requirement is unmet); no Kioxia filing read; the NBM contracts' price mechanics unestablished; no absolute exabyte or cost-per-bit data exists in public disclosure. Fiscal Q4/FY2026 reports **2026-08-05** and the Investor Day is **2026-08-13**, so this document is stale within a week by construction — the kill switches are written as pre-print criteria per PROD-P1 for exactly that reason.

---

### 2026-07-30 — PASS

See `../../../../watchlist.md`. Reason: purest expression of the structurally worst memory sub-sector, priced at 3.1x base-case fair value and 2.3x probability-weighted fair value, on peak-cycle earnings that follow three consecutive years of GAAP operating losses; reward-to-risk is negative on ASYM-P2's standardised base-over-bear basis, and the valuation lenses fail VAL-P3's cluster tolerance by 7.8x, so the range is not decision-grade in either direction. Revisit condition is written as an observable rather than a price alone, per PROD-P6: **the first quarter in which SanDisk's own MD&A reports ASP per gigabyte down quarter-over-quarter** — that is the quarter the LTA price mechanics become observable and the untested question in this thesis gets its answer — or a disclosed contractual price floor at the 2026-08-13 Investor Day or in the FY2026 10-K.

---

### 2026-08-22 — deep-dive refresh

Refresh mandated by the fired revisit trigger (flag of 2026-08-22, discharged by this entry). Price 1,596.08 (official close 2026-08-21; note the initial entry's 1,249.44 was an intraday snapshot — the official 2026-07-30 close was 1,279.96; official closes hereafter). Transcript gap closed: Q3 and Q4 FY2026 calls read in full; Investor Day still rests on its PR plus secondary coverage.

**Pre-commitments graded.** Zero of eight bull-case kill switches fired: ASP/GB rose again in Q4 (two-thirds of sequential growth was price, one-third volume), GAAP GM 84.6%, under-utilisation zero incremental in Q4 (audited FY2026 total $11M), no equity issued, buyback executed. One of five bear-case switches fired, and it was the pre-named highest-value unknown: **NBM floors and ceilings disclosed 2026-08-05** — $93.9bn minimum at floor pricing, >50% of FY2027 bits, ~2/3 of FY2028, NBM GM "around 80%" per the CFO in Q&A. Per the initial entry's own pre-commitment, bear point 5 collapsed and the base case moved materially. Caveats that survive: the floor LEVEL is disclosed nowhere (the audited 10-K never says "floor"); the deck's $16.5bn guarantee figure resolves to ~$7.7bn identifiable in the 10-K; no renegotiation mechanics disclosed.

**Corrections to the record** (bodies rewritten; originals preserved above per append-only): the FY2025 under-utilisation figure is $75M audited full-year — the initial thesis's "$24M in 9M FY25" was FY2025's inventory write-down, a different line. The Micron trough P/B staircase (0.81/0.97/1.32) did not survive primary verification: corrected troughs ~0.80-0.82x (2016), ~1.03x (2019), ~1.06-1.07x (2022-12); SNDK's own standalone trough ~1.0x tangible. The consensus "$264.72" circulating in the vault's own 2026-08-22 flag discussion is the **FY2028** mean, not FY2027 — FY2027 consensus is $214.10, essentially unchanged since 07-30.

**New facts weighed**: FY2026 10-K (equity $15,736M, TBVPS $73.36, cash $4,762M, zero debt, FCF $11,494M with ~$4.0bn of NBM deposits and unpaid taxes inside it, ~$1.4bn tax catch-up due FY2027, 53-week year); $4.5bn buyback executed at ~$1,512 avg (~20x tangible book) + $14bn new authorization; 100%-excess-cash-return policy; FY2028-30 model (~80% GM, ~75% OM, ~50% FCF margin); Kioxia capex reaffirmed ¥470bn/yr (kill switch not fired) and buying back its own stock; YMTC at 14% share, #3, third fab producing end-2026; SNDK slowest top-5 grower in Q2; CEO/CFO/CTO 10b5-1 sale plans adopted; AR concentration 19/12/10%; Nanya $808M unrealized gain plus $5.9bn DRAM commitments.

**Verdict**: fair value re-based to **$475 / $875 / $2,200**, PWFV ~$1,090 at 30/45/25 (valuation.md canonical; weights argued there; roughly half the base-case move is a stated method change from retained-forward-book to distributions-plus-terminal, forced by the payout policy). **PASS stands; conviction 1 → 2; size 0%.** Upside to base −45%, ASYM-P2 numerator negative. Principles check re-run: VAL-P3 VIOLATES (4.6x spread, improved from 7.8x), VAL-T1 ALIGNS, CAPA-P1 TENSION (the ~20x-tangible-book repurchase is now a live instance, replacing CAPA-P2's nothing-to-audit line), MOAT-P4 TENSION (unchanged), NARC-P1 TENSION (the beat was sold, the model was bought — the narrative moved to FY2028-30 and is unfalsifiable before then). Next window: Q1 FY2027 print (~Nov 2026), where the quarterly ASP/GB decomposition returns.
