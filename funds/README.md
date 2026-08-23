# Funds

Pooled vehicles — ETFs, and anything else where you buy an exposure rather than a business. One folder per fund: `funds/{TICKER}/` holding `thesis.md`, `valuation.md` and `ic-sheet.md`.

This is a top-level tier rather than a folder inside `sectors/` for one reason: a fund's peer set is **other funds tracking the same exposure**, not the companies inside it. A world-equity tracker has no sector.

Canonical rule: "Funds tier" in [`../docs/build-plan.md`](../docs/build-plan.md). Written by `fund-deep-dive` only.

## Identity is the ISIN

The same fund lists on several exchanges, in several currencies, under different tickers — and distributing and accumulating share classes are genuinely different objects with different tax treatment. The folder is named for the primary listing's ticker because humans need something to type; `thesis.md` carries the ISIN, domicile, currency, share class and the exact index.

Two folders for one fund is a research error. Before creating a folder, search the existing ones for the ISIN.

## Two lenses

A company deep-dive reads an industry framework plus a sector primer. A fund deep-dive reads:

| Lens | File | Scope |
|---|---|---|
| **Vehicle** | [`../frameworks/etf-vehicle-mechanics.md`](../frameworks/etf-vehicle-mechanics.md) | Universal. Cost, replication, domicile and withholding tax, size and closure risk, liquidity, index methodology, securities lending. Written once, used by every fund. |
| **Exposure** | `../frameworks/{exposure}.md` | Per asset class. What drives long-run returns, which valuation anchors have predictive power and over what horizon, the historical distribution of outcomes. |

Both are required, and they fail independently. **"Right exposure, wrong vehicle" is a common and actionable finding** — it means switch funds, not avoid the asset class. Conflating the two produces the wrong action.

## What a fund valuation outputs

Not a fair value. A fund is not cheap or expensive the way a business is: you cannot buy it below intrinsic value, and no management team exists to close a gap. The output is an **expected real return over an explicit horizon**, decomposed so each term can be argued and falsified on its own:

```
starting yield + real growth + valuation change − costs − tax
```

The wrapper's cost is the one term that is nearly certain while every other is a forecast. That asymmetry is why it deserves disproportionate research effort, and why a few basis points compound into real money over a decade.

Bands are **allocation** bands keyed to expected return and valuation percentile. Price bands are a company construct.

## Instruments

Three scripts. Each answers a different question and none substitutes for another.

- **`python scripts/exposure-history.py {TICKER} --cpi {rate}`** — the REALISED distribution: rolling returns over the horizon that matters, drawdown depth, and time to recovery. Reports how many windows are genuinely independent, because overlapping windows are the standard way this table misleads. Nominal without `--cpi`. Run it on the exposure framework's **history proxy**, never on the fund's own ticker: a fund younger than one cycle cannot show you its own worst case.
- **`python scripts/valuation-conditional.py [--horizon N] [--buckets 5]`** — the VALUATION-CONDITIONAL distribution: what forward real returns actually followed from a given starting multiple, computed from the archived Shiller dataset ([`../library/shiller-ie-data.md`](../library/shiller-ie-data.md)). Defaults to an expanding percentile basis, so each month is ranked only against what an investor standing there could have known. **US large-cap only** — it is the wrong series for a world or European exposure, and the output says so.
- **`python scripts/fund-metrics.py {TICKER} [...] --benchmark {B} --benchmark-variant {net-tr|gross-tr|price} --currency EUR`** — the OBJECTIVE COMPARISON against a benchmark: alpha and beta with t-statistics, R-squared, tracking error, information ratio, Sortino, up and down capture, correlations, all on the common overlapping period. Owned by [`compare-funds`](../.claude/skills/compare-funds/SKILL.md); the benchmark-selection rules and the practical question of which series the free feed actually carries live in [`../frameworks/fund-evaluation.md`](../frameworks/fund-evaluation.md).

**On the valuation-conditional question, which this section previously recorded as not built:** it is built, and the two paths named as ways to close it were both taken. `absorb` grew a dataset rung, the lint's locator forms grew sheet, column, row and date-range addresses, the dataset was archived and distilled into a citable entry, and the derived script reads it. What remains genuinely open is coverage, not capability — the archived series is US large-cap, so a European or world exposure still has no valuation-conditional evidence in this vault and a fund valuation on one must say so rather than borrowing the US numbers.

Read all three against their own honesty guards rather than around them. Each script refuses to answer in at least one situation — too few independent windows, a price-index benchmark, a currency it cannot resolve — and a refusal is the output, not an obstacle.

## The honest caution about a fund's track record

The most prominent number on any factsheet is trailing performance, and it is the least useful. A fund with a superb trailing decade has, all else equal, a **worse** forward expected return, because part of that return was multiple expansion that has already happened and cannot happen twice. Backtested index history is not fund history and is never a track record.
