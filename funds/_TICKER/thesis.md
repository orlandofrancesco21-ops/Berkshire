# {TICKER} — fund thesis

> Append-only. Date every update. Old thinking matters.

**Created:** YYYY-MM-DD
**Last updated:** YYYY-MM-DD
**Vehicle lens:** `../../frameworks/etf-vehicle-mechanics.md`
**Exposure lens:** `../../frameworks/{exposure-slug}.md`

## Identity

The ISIN is the identity; the ticker is not. Fill every row before analysing anything — a share class you did not check is a fund you did not analyse.

| | |
|---|---|
| ISIN | {IE00...} |
| Primary listing / ticker | {exchange, ticker, currency} |
| Other listings | {same fund, other tickers — list them so a future search finds this file} |
| Domicile | {IE / LU / US / ...} |
| Share class | {distributing / accumulating} |
| Index tracked | {exact index name and version} |
| Provider | {...} |
| Inception | {YYYY-MM-DD — fund inception, NOT index backtest start} |
| TER / actual tracking difference | {x.xx% / y.yy% over N years, sourced} |
| Fund size | {AUM, currency, as-of date} |

**Data sourcing:** {which figures come from the KID/KIID, which from the annual report — authoritative for realised costs, securities-lending revenue and tracking difference — which from the provider factsheet, which from price history. Every figure carries a date and a verification label per "Verification labels (canonical)".}

---

## What this fund actually holds

{The exposure in plain terms, then the gap between the label and the holdings. Concentration: top-10 weight, largest single name, sector and country skew, effective number of holdings. A "world" fund that is 70% one country is a different object from what its name implies, and this section is where that gets said.}

## The case for the exposure

{Why own this asset class at all, at this starting point. Grounded in the exposure framework, not in recent performance. Numbered points.}

## The case against the exposure

{Steelmanned. The strongest version, including what the starting valuation implies and what the historical record says about outcomes from here.}

## Vehicle assessment

{Against the vehicle framework's checklist. This section replaces "capital allocation track record" and "management quality", which do not exist for a fund. Cost (TER vs realised tracking difference), replication method and its consequences, domicile and withholding tax, size and closure risk, spread and liquidity, securities lending, index methodology and change risk. State the alternatives: which other funds track this exposure, and why this one — or why not.}

## What would change my mind

Two kinds, and they imply different actions. Per PROD-T3, key each to a disclosure the provider or index actually publishes.

**Exposure-level** — these would say the asset-class case is broken:
- {observable + threshold + where it is disclosed}

**Vehicle-level** — these would say *this wrapper* is broken while the exposure may be fine. The action is a fund switch, not an exit:
- {TER increase, tracking difference degrading beyond {x}bp for {n} periods, AUM below {threshold}, index methodology change, domicile or tax treatment change, securities-lending policy change, provider merger}

## Principles check

{1-5 lines, same contract as a company thesis: verdict token + resolvable ID + attribution + the fact of THIS situation that engages it. Or the sentinel. Note MOAT and CAPA rarely bear on a fund — do not manufacture a moat line for an index; the sentinel exists for genuine non-applicability.}

## Conviction

**Level (1-5):** {n}

{Reasoning. Must answer every VIOLATES line above. For a fund, conviction is about the exposure case and the vehicle's fitness — it is not the allocation, which follows below.}

## Allocation logic

{The decision unit. What percentage, in what role (core beta or satellite tilt), against what alternative, over what horizon. What it displaces or duplicates in the existing portfolio, and its correlation to what is already held. Currency exposure and whether it is hedged. Rebalancing bands. Sizing follows ASYM-P2's asymmetry basis; what a fund changes is that the binding constraint is the drawdown distribution and time-to-recovery, not permanent loss of a single business.}

## Update log

### YYYY-MM-DD — initial thesis

{Same heading convention as a company thesis, deliberately: one convention across both tiers, and the shape gate keys on it.}
