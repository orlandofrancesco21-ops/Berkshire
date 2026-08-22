# {TICKER} IC sheet

<!--
FUND VARIANT of the IC sheet. Same contract as the company sheet (see
"IC sheet (canonical)" in docs/build-plan.md): a derived view regenerated whole
on every run, no log, nothing originates here, hyphens only and no em- or
en-dashes anywhere, every figure dated, one page.

The section set differs because the object differs: a fund has no Business and
no per-name Sizing decision. It has an Exposure, a Vehicle, and an Allocation
against alternatives. The lint enforces this variant's headings.
-->

| | |
|---|---|
| Verdict | {ALLOCATE x% / WATCH / PASS}, conviction {1-5} |
| Fund | {ISIN}, {domicile}, {distributing or accumulating} |
| Index | {exact index tracked} |
| Price / NAV | {x.xx CCY, YYYY-MM-DD} |
| Expected net real return | {bear} / {base} / {bull} over {horizon}, weighted {w.w%} |
| Cost | TER {x.xx%}, realised tracking difference {y.yy%} over {N} years |
| All-in annual drag | {x.xx% to y.yy%: TER + unrecovered withholding + turnover, less lending; per the vehicle assessment} |
| Alternative | {the next best way to own this exposure, and its cost} |
| Next dated event | {annual report / index review / fee change, YYYY-MM-DD — for a fund this is never an earnings date} |
| Deep docs | `./thesis.md`, `./valuation.md`, both as-of {YYYY-MM-DD} |

## Executive summary

- {What the fund holds, in one line a non-specialist can parse.}
- {The allocation call and the single number that carries it.}
- {The starting valuation and what the record says follows from it.}
- {The one thing that would most change the answer, and when it arrives.}

## Exposure

- {What is actually inside, versus what the name implies. Concentration and country or sector skew.}
- {Why this asset class, at this starting point.}

## Vehicle

- {Cost: TER versus realised tracking difference, and which is the honest number.}
- {Replication, domicile, withholding tax, size and closure risk, spread, securities lending.}
- {Why this wrapper rather than the alternatives that track the same index.}

## Case for

1. {Numbered. Each is one load-bearing claim with its key figure and as-of date.}

## Case against

1. {Steelmanned. Include what the starting valuation implies about forward returns.}

## Variant perception: where we differ from the market

- What the market prices: {stated fairly}.
- What we anchor on instead: {method}, and why.
- The strongest case against us: {steelman}.
- What proves us wrong, and when: {observable plus date}.

## Expected return

- Decomposition (reconciles to `./valuation.md`, which is canonical):

| Term | Bear | Base | Bull |
|---|---|---|---|
| Starting yield | | | |
| Real growth | | | |
| Valuation change | | | |
| Less costs and tax | | | |
| **Net real** | | | |

- Historical outcomes from comparable starting points: {range, and the worst realised case}.
- Drawdown record: {depth, duration, time to recovery}.

## Kill switches

- Exposure-level: {the asset-class case is broken}.
- Vehicle-level: {this wrapper is broken while the exposure may be fine. Action is a switch, not an exit}.

## Allocation

- {Target percentage, role (core beta or satellite tilt), what it displaces, correlation to existing holdings, currency and whether hedged, rebalancing bands.}

## What we do not know

- {The gaps that bound the conviction, stated without hedging language.}
