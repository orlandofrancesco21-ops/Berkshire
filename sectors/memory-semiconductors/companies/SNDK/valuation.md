# SNDK — valuation

Companion to `thesis.md`. **This file is canonical for SNDK's scenario numbers per VAL-P5** — any range quoted elsewhere reconciles to the table below or declares itself a different object.

**Last updated:** 2026-07-30
**Framework:** `../../../../frameworks/memory-semiconductors.md`
**Sector:** `../../primer.md`

**Data sourcing:** price and market-derived multiples from a single yfinance pull, **2026-07-30 18:37 local, USD**, per "Price and data sourcing (canonical)". Balance-sheet and income-statement figures from SanDisk's Form 10-Q for the quarter ended **2026-04-03** (filed 2026-05-01) and Form 10-K for FY2025 (filed 2025-08-21), `verified`. Guidance from the Form 8-K earnings release of 2026-04-30, `verified`. Consensus estimates from the yfinance analyst tables pulled 2026-07-30, corroborated independently against stockanalysis.com as of 2026-07-23.

---

## Primary valuation framework

**Price to book value — but against a *forward* book, not the reported one. And P/E is not a secondary lens here; it has no valid domain at all.**

The framework is explicit and this name is the reason it is worth saying twice. At a memory trough the earnings denominator is negative and P/E does not exist; at a memory peak a mid-single-digit forward P/E is the **signature of the top**, not a valuation argument. On 2026-07-30 SNDK trades at 5.87x forward earnings, MU at 5.56x, SK hynix around 5.2x and Samsung around 5-7x (the first two `verified`, the Korean figures commentary and `unverified`). That is not four independent cheapness signals — it is **one consensus forecast of one peak year, quoted four times**. Micron peaked in May 2018 at a forward P/E of roughly 4-5x and then fell ~56% *while earnings were still rising* (commentary, `unverified`). VAL-T1 in its purest available form: a low multiple on peak earnings and a high multiple on trough earnings are the same mistake, and the trap fires whenever the multiple is the first thing you look at.

So the primary lens is P/B — with the framework's correction, which is the single most useful idea in the file and runs *opposite* to the usual stale-denominator trap. Everywhere else in this vault a stale book understates a compounder. **Here, at a peak, book value compounds faster than the price falls**, so the trailing P/B is stale in the other direction:

| Book value per share | Basis | P/B at 1,249.44 |
|---|---|---|
| **$93.09** | reported equity $13,777M ÷ 148.1M shares, 2026-04-03 (`verified`) | **13.42x** |
| **$126.63** | + fiscal Q4 2026 at the guide midpoint (~$31.50 non-GAAP EPS × ~158M diluted ≈ $4,977M) | **9.87x** |
| **$284.30** | + FY2027 at *my base case* ($170 EPS), net of $3.0bn of buyback | **4.39x** |
| **$329.30** | + FY2027 at *consensus* ($212.95 EPS), net of $3.0bn of buyback | **3.79x** |

SanDisk would earn between 1.9x and 2.4x its entire current book value in a single fiscal year. So 13.4x book is no more evidence of overvaluation than Micron's 0.81x was evidence of cheapness in February 2016 — both are stale denominators. **Anchor on the post-peak-year book, and be explicit that the anchor only exists if the peak year is actually delivered.**

Two adjustments the framework does not make and this name requires:

- **Use tangible book.** Goodwill is **$4,994M — 36% of the $13,777M equity base** — a legacy of Western Digital's 2016 SanDisk acquisition, and it has already been written down twice ($671M in FY2023, $1,830M in the quarter ended 2025-03-28, `verified`). Goodwill on a commodity manufacturer that has impaired it twice in three years is not book value you can underwrite through a trough. The trough multiples below are applied to book **less goodwill**.
- **There is no replacement-cost floor here, and that is a structural finding rather than a modelling choice.** The framework's second cross-check is EV against the cost of rebuilding installed capacity — $15-20bn+ and 2-3 years for a greenfield DRAM fab (`unverified`) — and it is the anchor that has repeatedly caught fab-owning incumbents at troughs. **SanDisk owns no fab.** Net PP&E is $649M. Its productive capacity is a 49.9% interest in equipment held by three JV entities inside buildings **Kioxia owns**, and it is contractually barred from building its own (10-Q Note 10 and S-3ASR 2026-02-17, `verified`). An asset floor requires the company to own the asset. What SanDisk has instead is the mirror image: $6,543M of Flash Ventures commitments, $993M of lease guarantees, $856M of prepaid building depreciation still to be credited and a $1.2bn payment owed to Kioxia over 2026-2029. Its balance sheet understates its capital intensity and overstates its flexibility, in the same breath.

## Current state

| Metric | Current (2026-07-30) | 5y average | 10y range | Sector peers (2026-07-30) |
|---|---|---|---|---|
| Price | **1,249.44** | n/a — 17 months of history | n/a. 52-week 40.10 – 2,354.39; first bar 36.00 on 2025-02-13 | MU 856.97 · WDC 523.46 · STX 838.53 |
| Market cap | $185.0bn | n/a | n/a | MU $967.9bn · STX $189.7bn · WDC $180.4bn |
| Enterprise value | **~$181.5bn** (recomputed) | n/a | n/a | vendor field reports $146.9bn — **understated by ~$34bn, do not use** |
| Forward P/E (FY2027 cons.) | **5.87x** | n/a | n/a | MU 5.56x · WDC 27.82x · STX 15.05x |
| Trailing P/E | 42.70x | n/a | n/a | meaningless — TTM contains two loss quarters |
| P/B (reported) | **13.42x** | n/a | n/a | MU ~9.6x. MU troughs ~0.81x (2016-02), 0.97x (2019-05), 1.32x (2023-02) — `unverified` |
| P/B (post-FY27 consensus book) | **3.79x** | n/a | n/a | — |
| EV / TTM revenue | **13.76x** | n/a | n/a | recomputed; vendor field says 11.14x |
| EV / TTM GAAP operating income | **33.8x** ($5,370M TTM) | n/a | n/a | — |
| EV / annualised Q3 FY26 operating income | **11.0x** ($4,111M × 4) | n/a | n/a | the honest run-rate multiple |
| EV / annualised Q4 FY26 guided revenue | **5.67x** ($8.0bn × 4) | n/a | n/a | — |
| TTM gross margin | 56.04% | — | FY23 7.1% · FY24 16.1% · FY25 30.1% | latest quarter **78.4%**; Q4 guide 78.9-80.9% |
| GAAP operating income | TTM **+$5,370M** | — | **FY23 -$2,035M · FY24 -$468M · FY25 -$1,377M** | three straight loss years |

**Read on current state — and three vendor-data corrections that have to be made before any of this is usable.** The framework's "when does the multiple lie?" list fires on this name in four of its five modes simultaneously, which is unusual enough to be worth stating as the headline finding of this valuation.

1. **The "impossible" operating margin is a period mismatch, and the GAAP figure is real.** The vendor reports operating margin 69.98% *above* gross margin 56.04%. The first is the **latest quarter alone, normalised**; the second is **trailing twelve months**. Both reconcile exactly: TTM gross profit ($498M + $687M + $1,541M + $4,662M) ÷ TTM revenue ($1,901M + $2,308M + $3,025M + $5,950M) = 7,388 / 13,184 = **56.04%**; and (operating income $4,111M + $46M loss on debt extinguishment + $7M separation costs) ÷ $5,950M = **69.98%**. The filed GAAP figure for the quarter is **operating income $4,111M on revenue $5,950M = 69.1%**, and it closes arithmetically as 78.4% gross margin less $498M of opex (8.4% of revenue) with **no joint-venture income involved at all** — SanDisk's equity-method Flash Ventures result is a **loss** ($58M in 9M FY26, $74M in FY2025) and sits in *Other income (expense)*, below the operating line. TTM GAAP operating margin is **40.7%**. Do not quote 70% as a run-rate; do not attribute it to the JV.
2. **The vendor's annual "operating income" row is not GAAP and is wrong by more than a billion dollars.** It reconciles to the filings only after adding back the impairment and separation charges: FY2025 filed **-$1,377M** + $1,830M impairment + $67M separation + $21M termination − $34M divestiture gain = **+$507M** (the vendor's "+0.51bn"). Same for FY2023 (−$2,035M + $671M + $69M = −$1,295M) and FY2024 (−$468M + $40M = −$428M). **The filed record is three consecutive years of GAAP operating losses.**
3. **The vendor's enterprise value is understated by ~$34bn.** $185.0bn market cap − $3.735bn cash + $0.21bn debt = **~$181.5bn**, against a reported $146.9bn. Every EV multiple derived from the vendor field is ~24% too low. (Note the $3,735M cash is the 2026-04-03 balance and **$972M left the building on 2026-04-08** for the Nanya subscription.)

And on the peer row: **WDC and STX are not NAND comparables.** Western Digital and SanDisk split in February 2025 — WDC kept HDD — and both HDD names are a two-player oligopoly with no fab and entirely different supply economics. The genuinely informative thing in that row is the *spread*: the market capitalises HDD earnings at **three to five times** the multiple it gives memory earnings, on businesses feeding the same AI-storage demand. That is not an arbitrage. It is the market stating that it does not believe memory's current earnings repeat and does believe HDD's do.

## Fair value range

The valuation turns on two things and only two: **what SanDisk earns in fiscal 2027** (the year ending ~2027-07-02, which sits mostly *ahead* of TrendForce's 2H27 NAND crossover — a timing point the bulls are right about), and **what multiple of the resulting book value the market pays once the peak year is in the rear-view mirror**. Per VAL-P4 those two move together across the cases: the earnings path and the multiple that path earns are causally linked here through the same variable — whether the sufficiency ratio holds.

Book build, common to all three cases: reported equity $13,777M (2026-04-03) + fiscal Q4 2026 at the guide midpoint ($31.50 non-GAAP × ~158M diluted ≈ $4,977M) = **$18,754M entering FY2027**. Share count held at 148.1M throughout, because a $6.0bn buyback at these prices retires only 4.8M shares against roughly 9M of diluted equity-comp overhang — the two roughly cancel, which is itself the point (CAPA-M1).

| Scenario | FY2027 EPS | End-FY2027 tangible BVPS | Multiple applied | **Fair value** | Prob. |
|---|---|---|---|---|---|
| **Bear** — momentum rolls faster than consensus, NAND sufficiency turns positive on TrendForce's 2H27 schedule, ASPs fall through cost in FY2028, Flash Ventures under-utilisation charges return, goodwill impaired a third time | **$110** (30% below the *lowest* of 21 estimates) | **$197.9** (equity $34,304M less $4,994M goodwill; $1.5bn buyback) | **1.0x** — the low end of memory's 0.8-1.3x trough band, because SanDisk is pure NAND, owes half of JV fixed costs regardless of output, and has no fab to floor the value | **$200** | 40% |
| **Base** — FY2027 delivers well but below consensus because contract-price momentum has already collapsed from +70-75% to +10-15% QoQ; the cycle then rolls on the historical 6-8-quarter clock; normalised through-cycle EPS ~$30-38 | **$170** | **$250.6** (equity $42,104M less goodwill; $3.0bn buyback) | **1.6x** — above trough, below the ~1.93x 10-year median, reflecting a genuinely re-based datacenter revenue floor | **$400** | 40% |
| **Bull** — the AI-inference demand shift plus contracted LTAs genuinely re-base the trough: gross margin settles in a new 45-55% band instead of going negative, normalised EPS ~$130, and the market pays a normal cyclical multiple on that normalised number | **$213** (consensus mean delivered) | $295.6 | **12x normalised EPS of $130** = $1,560, cross-checked at **5.3x** post-FY27 tangible book | **$1,560** | 20% |

**Fair value range: $200 (bear) — $400 (base) — $1,560 (bull).**

**Probability-weighted fair value: ~$552** (0.40 × 200 + 0.40 × 400 + 0.20 × 1,560).

**Current price vs range:** 1,249.44 is **6.2x the bear case, 3.1x the base case, 2.3x the probability-weighted value, and 0.80x the bull case**. Upside to base: **−68%**. Upside to bull: **+24.9%**. Downside to bear: **−84.0%**. On ASYM-P2's standardised basis — upside to base over downside to bear, from the current price, off this table — the reward-to-risk ratio is **negative**; even stretching the numerator to the bull case, which that item forbids, gives about **0.3:1** against a 2:1 threshold for a starting position.

**Three things this table is honestly saying.**

- **The bull case is roughly today's price.** That is not a coincidence and it is the cleanest summary of the setup: at 1,249.44 the market is paying, today, for the outcome in which a nine-time-repeating commodity cycle does not repeat. The bull case here is already generous — it assumes SanDisk durably earns **$130 a share**, roughly $19bn of net income a year, against a company whose *total revenue* in FY2025 was $7.36bn and whose GAAP operating line was negative in each of FY2023, FY2024 and FY2025. It implies **5.3x post-peak-year tangible book**, which the framework says is squarely in "you are underwriting a regime change" territory. That is coherent — the bull *is* underwriting a regime change — but it should be named as such rather than smuggled in as a multiple.
- **The range is not decision-grade, and the valuation says so rather than averaging it away.** $200 to $1,560 is a **7.8x spread** against VAL-P3's provisional cluster tolerance of roughly 1.33x. Per that rule, a failed cluster does not forbid acting; it forbids calling the lenses agreed, and requires naming which is conservative and why. **The trough-book lens is the conservative one and it is the one carrying the evidence**: nine cycles in forty years, Micron's own P/B trough series, and this company's own three loss years ending fourteen months ago. The bull lens rests on customer agreements less than a year old whose **price mechanics are not disclosed in any primary document**, and on a supply-discipline claim the industry's own forecaster contradicted on 2026-07-21 and again on 2026-07-30.
- **A range this wide still produces a clean decision, because the price is outside it in one direction.** Every case except the bull sits 68-84% below the market. The width matters for what you would pay *if* you were buying; it does not create ambiguity about whether to buy here.

**What the current price embeds, solved backwards.** This is the framework's third cross-check and the least escapable number in the file. At an enterprise value of **~$181.5bn**:

| If the market is paying | then normalised operating income must be | i.e. normalised EPS of about |
|---|---|---|
| 8x EV/EBIT | $22.7bn/yr | **$146** |
| 10x EV/EBIT | $18.1bn/yr | **$117** |
| 12x EV/EBIT | $15.1bn/yr | **$98** |

Set against: **TTM GAAP operating income $5,370M**, and filed GAAP operating income of **−$2,035M / −$468M / −$1,377M** in FY2023 / FY2024 / FY2025. Put the other way round: at ~11x EV/EBIT, today's price requires SanDisk to sustain **its single best quarter ever, annualised, indefinitely** ($4,111M × 4 = $16.4bn; EV/that = 11.0x). Not grow from it — *sustain* it, through the capacity wave the industry has already announced.

## Sensitivity

Only two variables move the answer, and per VAL-P4 they are not independent — they are two readings of the same underlying question, which is whether the NAND sufficiency ratio holds. A third row is included because it is the one input that could genuinely re-rate the whole table and is answerable on a known date.

| Variable | Bear | Base | Bull | FV impact |
|---|---|---|---|---|
| **FY2027 EPS** (consensus $212.95; range $154.28–$396.08 across 21 analysts) | $110 | $170 | $213 | ~$50-60 of tangible BVPS per $60 of EPS; at a constant multiple, ~$95 of FV per $60 of EPS in the base case |
| **Exit multiple of post-FY27 tangible book** (memory troughs 0.8-1.3x; MU 10-yr median ~1.93x) | 1.0x | 1.6x | 5.3x | **dominant.** Each 0.5x on the base case is ~$125 of fair value. The whole bear-to-bull span is far more multiple than earnings |
| **LTA price mechanic** — floor / index / volume-only (**not disclosed**) | volume-only; customers take the bits and refuse the price | volume plus a partial floor on ~1/3 of bits | a firm price floor on >1/3 of FY2027 bits, rising toward 50% | binary. A genuine disclosed floor moves the *bear* case most — it is what stops trough gross margin going negative, and it is the difference between a 1.0x and a 1.3-1.5x trough multiple |

**The dominant variable is the multiple, not the earnings.** Even taking the bull's $213 of FY2027 EPS at face value, the fair value swings from **$296** (1.0x tangible book) to **$1,560** (12x normalised earnings) depending only on what the market decides the normalised number is. That is what it means to say P/E has no valid domain here: at the peak, the earnings are nearly a known quantity and the *multiple* is the entire debate. And this is precisely NARC-M1 — the multiple prices what consensus currently believes about the story, and 21 analysts marking FY2027 up **86% in 90 days, 6 up and 0 down over 30 days, while the stock halved**, is the market and the sell side holding opposite positions on the same earnings.

## Cross-checks

Three lenses, chosen to interrogate genuinely different inputs rather than to be one forecast wearing three hats (VAL-P3's holds-when). The fourth — the framework's EV/replacement-cost anchor — is **unavailable for this name**, and that absence is a finding.

- **(1) Normalised mid-cycle earnings, run downward** (VAL-M1, inverted for a peak). Framework rule: at the trough normalise up, at the peak normalise **down**, and write down what "normal" is assumed to be because that assumption *is* the valuation. My assumption: a normalised year for SanDisk is revenue of **$18-25bn** — well above the $7.36bn of FY2025 because the Datacenter re-basing is real, well below the $49.87bn of FY2027 consensus — at a **35-45% gross margin**, against a cited sustainable commodity-DRAM band of 55-70% (`unverified`) and a NAND-only normal that the framework says is lower still. That gives $27-48 of normalised EPS. At the framework's 8-15x on normalised memory earnings: **$220-720**. This lens brackets the bear and base cases and sits an order of magnitude below the price. It agrees with the primary lens.
- **(2) Implied expectations, solved backwards** — the table above. At ~$181.5bn of EV the price requires **$98-146 of permanent normalised EPS**. Independent of the first lens because it interrogates the *price* rather than a forecast. It agrees with nothing on this page except the bull case, and it is the number that makes the bull case legible: the bull is not "earnings are good," it is "$117 a share is the new normal."
- **(3) The framework's own working P/B rule, applied without adjustment.** "Sub-1.2x book is where memory has historically been buyable; above ~3x book you are underwriting a regime change; above 10x you are not doing valuation." At 13.42x reported book SNDK is in the third bucket; at 3.79x post-FY27 consensus book it is in the second. **Both readings are on the same day and neither is wrong** — which is the framework's point about forward book, and also the reason this cross-check is a sanity check rather than a valuation.
- **(4) Replacement cost — unavailable, and the reason matters.** For a fab owner this is the trough anchor: installed capacity has an unambiguous rebuild cost and the market has repeatedly priced incumbents below it. **SanDisk has $649M of net PP&E and no fab.** Its capacity is 49.9% of equipment inside Kioxia's buildings, held through JVs it cannot consolidate, on a non-compete that forbids it from building its own. There is no rebuild cost to anchor to, only an obligation schedule — $6,543M of Flash Ventures commitments, $993M of lease guarantees, $856M of prepaid building depreciation outstanding, $1.2bn owed to Kioxia over 2026-2029. **The asset-based floor that works for Micron does not exist for SanDisk, and its absence removes the one lens that has historically caught memory at the bottom.**
- **(5) The sell-side, as a datapoint about what the argument actually is.** 22-23 analysts, mean target **$2,217.77**, median $2,250, high $3,169, low $1,000, 15 Strong Buy / 3 Buy / 4 Hold / 1 Sell (yfinance 2026-07-30, corroborated at stockanalysis.com 2026-07-23). The mean target is **10.4x FY2027 consensus EPS** — so the sell side is *not* arguing for a re-rating; it is arguing that the peak earnings are real and deserve an ordinary cyclical multiple. **The entire gap between my bull case ($1,560) and the street ($2,218) is whether you capitalise $213 of peak EPS at 10x or a normalised $130 at 12x.** That is the debate in one sentence, and the framework's answer — that applying any P/E to a memory peak year is VAL-T1 with the label filed off — is why my number is the lower one.

**Do the cross-checks cluster? No — and this is recorded as a failure, not reconciled away.** Lenses (1) and (3) support $200-720. Lens (2) supports the price only if $117 of EPS is permanent. VAL-P3's tolerance is ~1.33x; the spread is 7.8x. Naming the conservative lens as that rule requires: **lens (1), normalised mid-cycle earnings, is the conservative one**, because its assumption ("normal" is $18-25bn of revenue at 35-45% gross margin) is *already* far more generous than anything this asset has produced in ten years, and it still lands at a fifth of the current price.

## Hold / trim / add bands

This is the table `valuation-check` reads on price moves. **There is no position** — the deep-dive verdict is PASS — so the HOLD row describes the range, not an endorsement.

| Action | Price band | Reasoning |
|---|---|---|
| **ADD / INITIATE** | **< $400**, and only with all three conditions below | At or below base-case fair value, i.e. ≤1.6x post-FY2027 tangible book. **Conditions: (a)** the FY2027 book has actually been *reported*, not forecast — verify equity in a filed balance sheet, because today's base case rests on a book value that only exists if the peak year arrives; **(b)** the LTA price mechanic has been disclosed as a floor or an index rather than volume alone; **(c)** NAND sufficiency still negative, or the issuer-disclosed proxy holding (ASP/GB flat-to-up with exabytes compounding). First tranche 1-2%, not the 3-4% the same conviction buys elsewhere in this vault — ASYM-T2 and the framework's crossover section both cap memory sizing below the vault default |
| **HOLD** | $400 – $1,560 | Nominally inside the fair value range — but the range is **7.8x wide and fails VAL-P3's cluster tolerance**, so this band carries no information. Treat it as "the valuation cannot discriminate here", not as a hold recommendation. At 1,249.44 the stock is inside this band and the verdict is still PASS, because upside to base is −68% |
| **TRIM** | > $1,560 | Above the bull-case fair value, which itself already requires a regime change — normalised EPS of $130 and 5.3x post-peak-year tangible book |
| **EXIT** | n/a — price-independent | Requires a thesis kill switch per `thesis.md`, never a price level (ASYM-P1). Specifically: two consecutive quarters of ASP/GB down QoQ in SanDisk's own MD&A; Flash Ventures under-utilisation charges reappearing in the related-party note; GAAP gross margin below 55%; or the exabyte/ASP decomposition disappearing from MD&A for two quarters (PROD-T3 — the metric's disappearance is itself the trigger) |

**Current price 1,249.44 (2026-07-30) → do not initiate.** Not because the price fell 46% and might fall further, and not because of the drawdown — ASYM-P1 forbids reading a price move as a signal in either direction. Because the reward-to-risk from here, computed off this table, is negative.

## Update log

### 2026-07-30 — initial valuation

Price 1,249.44 USD (yfinance, 2026-07-30 18:37 local), one session off a 1,015.89 capitulation low struck 2026-07-29 after a 56.5% peak-to-trough fall in 34 calendar days from 2,335.00 on 2026-06-25, then +23.4% in a single session. **The reference price is not a settled level and this band is written against a violently two-way tape** — that is a stated limitation of every percentage on this page, not a caveat.

Primary lens is price to *forward* tangible book per the framework, because at a memory peak the trailing book is a stale denominator in the opposite direction from the usual trap and P/E has no valid domain at either end of the cycle. Fair value **$200 / $400 / $1,560**, probability-weighted **~$552** at 40/40/20. Price sits at 6.2x bear, 3.1x base, 2.3x PWFV, 0.80x bull. Reward-to-risk on ASYM-P2's standardised base-over-bear basis is **negative**.

Cross-checks fail VAL-P3's cluster tolerance by 7.8x and the failure is recorded rather than averaged; normalised mid-cycle earnings is named the conservative lens. The framework's EV/replacement-cost anchor is **unavailable for this name** — SanDisk has $649M of net PP&E, no fab, and 49.9% of equipment inside buildings Kioxia owns — which removes the one lens that has historically caught memory at a bottom and is the reason the bear case cannot be floored on assets.

Three vendor-data corrections applied before anything was built: enterprise value recomputed at ~$181.5bn against a reported $146.9bn (~24% understatement flowing through every EV multiple); the "impossible" 69.98% operating margin resolved as a latest-quarter normalised figure quoted against a trailing-twelve-month gross margin, reconciling to four significant figures with the filed GAAP margin at 69.1% and **no JV income involved**; and the vendor's annual operating-income row shown to be non-GAAP, with the filed record being three consecutive years of operating losses.

Two dates set this file's shelf life: fiscal Q4 and full-year 2026 report **2026-08-05**, Investor Day **2026-08-13**. The single item that would most move this table is a disclosure at either event of whether the $41.6bn of remaining performance obligations carries a **price floor or only a volume commitment** — it moves the *bear* case most, because it is what determines whether trough gross margin goes negative again. Re-run this valuation after both.
