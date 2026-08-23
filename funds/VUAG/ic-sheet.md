# VUAG IC sheet

| | |
|---|---|
| Verdict | ALLOCATE as core beta, size for drawdown; today sits in the HOLD band (do not add aggressively). Conviction 3 |
| Fund | IE00BFMXXD54, Ireland, accumulating |
| Index | S&P 500 Net Total Return (SPTR500N), full physical replication |
| Price / NAV | 108.88 GBP (VUAG.L market price; NAV in USD), 2026-08-22 |
| Expected net real return | bear -1.9% / base +2.3% / bull +5.6% over 10 years, weighted +1.8% per year (pre personal tax, net of wrapper) |
| Cost | TER 0.07% (2026-03-24). Realised tracking difference positive vs its NTR benchmark, +0.15% to +0.29% per year 2020 to 2025 |
| All-in annual drag | 0.15% to 0.22% per year vs the gross index: TER 0.07% plus ~0.19% unrecovered US withholding, less a few bp securities lending |
| Alternative | SPDR SPYL (IE000XZSV718), 0.03%, physical, Irish: ~4bp per year cheaper, younger Acc class. Invesco SPXS synthetic: higher realised return, more risk |
| Next dated event | Fund annual report, period end 2026-06-30, expected around Q4 2026 (a fund print, not an earnings date) |
| Deep docs | `./thesis.md`, `./valuation.md`, both as-of 2026-08-23 |

## Executive summary

- Owns the 500 largest US companies, cap weighted, through a cheap full-physical Irish wrapper.
- The call: own it as core equity beta over 10 years, but size for the drawdown record and do not add aggressively at today's valuation. The single number: weighted +1.8% real per year, pre-tax, over 10 years.
- Starting valuation is extreme: Shiller CAPE ~41 (2026-08), the 99th percentile of 145 years. The five most expensive starts ever recorded all produced negative real decades.
- What would most change the answer: the CAPE reading falling below ~28, or the fund's annual report showing tracking or cost degradation. The next fund print lands around Q4 2026.

## Exposure

- What is inside: ~500 US large caps, committee selected, ~one third Information Technology, top ten roughly high-30s% of weight (partial, S&P factsheet queued). More concentrated than MSCI World's top ten of 26.41% (2026-07-31).
- 100% US, 100% USD for a EUR-based holder, unhedged. No ex-US ballast.
- Why this asset class: the core growth engine of a long-only book and the most studied, cheapest way to own US large-cap productivity, which compounded ~7.4% real over 1926 to 2000.

## Vehicle

- Cost: TER 0.07% (2026-03-24). The honest number is the realised tracking difference, which is positive against the fund's stated NTR benchmark and about -0.18% per year against the true gross index. All-in drag 0.15% to 0.22% per year.
- Full physical (504 holdings vs 503 constituents, 2026-06-30), Ireland domicile (15% US treaty withholding, not US-situs for estate tax), USD 86.0bn fund and USD 34.2bn class (2026-07-31), no closure risk, Aktienfonds with an 85% equity quota so the 30% Teilfreistellung applies. Securities-lending split not established from a primary source (gap).
- Why this wrapper: none strictly dominates it. SPDR SPYL is ~4bp per year cheaper but its Acc class is young. Invesco synthetic has beaten the index by more via the 871(m) gross-dividend route, at the cost of counterparty and regulatory-arbitrage risk. iShares CSPX is a wash.

## Case for

1. Cheapest, most studied way to own US large-cap productivity; TER 0.07% (2026-03-24), full physical, deeply liquid.
2. Excellent wrapper on the knowable part of the analysis: beats its net-TR benchmark net of fees every year 2020 to 2025.
3. German tax efficient: Aktienfonds, 85% equity quota, 30% Teilfreistellung (Vanguard DE page, 2026).
4. Over a decade, cost certainty beats valuation timing; CAPE does not time 1 to 3 year entries.

## Case against

1. CAPE ~41 (2026-08) is the 99th percentile; the five most expensive starts ever all gave negative real decades (-2.55% to -4.59%).
2. Conditioning on valuation lowers the centre and barely narrows the width: most-expensive quintile 10-year real median +4.8%, range -5.9% to +13.1%.
3. Record concentration means the outcome rests on a handful of mega-caps to a degree the historical drawdown record did not.
4. No ex-US ballast: this is the survivor market priced as if its exceptional century repeats.
5. Drawdown record: -55% (GFC, 2007 to 2009), -86% price with ~15.5y real recovery (1929 to 1945).

## Variant perception: where we differ from the market

- What the market prices: US large-cap earnings compounding at roughly their historical pace, with the current multiple sustained.
- What we anchor on instead: the 10-year valuation-conditional record (Shiller CAPE, `library/shiller-ie-data.md`), which puts the forward real return below the long-run average from a 99th-percentile start.
- The strongest case against us: the CAPE mean has structurally shifted (accounting, buybacks, ~one third tech), so historical reversion is the wrong base rate (VAL-T2). We hold this as a live possibility, which is why the bull case carries no valuation drag.
- What proves us wrong, and when: a decade of realised returns landing in the upper half of the conditional band; observable only at the 10-year mark, which is why sizing, not timing, is the response now.

## Expected return

- Decomposition (reconciles to `./valuation.md`, which is canonical):

| Term | Bear | Base | Bull |
|---|---|---|---|
| Starting yield | +2.3% | +2.8% | +3.3% |
| Real growth | +1.0% | +1.75% | +2.5% |
| Valuation change | -5.0% | -2.0% | 0.0% |
| Less costs and tax | -0.18% (wrapper); personal tax ~18.46% effective, see valuation.md | -0.18% | -0.18% |
| **Net real (pre personal tax)** | **-1.9%** | **+2.3%** | **+5.6%** |

- Historical outcomes from comparable starting points: most-expensive CAPE quintile 10-year real median +4.8%, range -5.9% to +13.1%; the five most expensive starts ever were all negative.
- Drawdown record: -55.3% (2007 to 2009, recovered 4.9y); -86.2% price (1929, ~15.5y real recovery); -47.5% (2000 to 2002, 6.1y).

## Kill switches

- Exposure-level (leave US large-cap): an S&P 500 selection-rule methodology change; shareholder yield below ~2% while multiple expansion carries the return build (currently unusable, no buyback series sourced). Never a CAPE level or price alone.
- Vehicle-level (switch funds, a taxable event): TER rise; tracking difference more than ~0.15pp per year worse than stated cost for 3 years; AUM below ~EUR 500m with a downtrend; loss of Aktienfonds status; index or share-class change.

## Allocation

- Target percentage: an owner risk decision (needs total equity target and risk tolerance, not supplied). System input: own as core beta, size for the drawdown record.
- Role: core beta, rebalanced to target. Displaces cash; duplicates in factor terms the US large-cap already held via NKE and ADBE (quantify once portfolio.md TBD fields are filled).
- Currency: 100% USD, unhedged; no directional FX view; carried as a band, does its work in the drawdown.
- Sizing: small enough that a 50%+ drawdown lasting a decade can be held through and added into, not sold into.
- Entry: lump-sum has the higher expected return; phasing the cash over ~6 to 12 tranches is a defensible regret-minimiser at a 99th-percentile start, on behavioural grounds, not because valuation times the entry.
- Rebalancing band: ~+/-5pp from target.

## What we do not know

- The current S&P 500 top-ten weight and sector weights to the decimal (S&P factsheet queued; concentration figures are partial).
- The securities-lending revenue split (the annual report defeated extraction; gap flagged).
- The net buyback yield series, so the shareholder-yield term is part estimate and one exposure kill switch is unusable.
- The exact after-tax drag, which depends on holding period, the Basiszins path, and the annual allowance; needs the tax advisor.
- Whether CAPE's elevated mean is structural or cyclical; the vault takes no position and holds both.
