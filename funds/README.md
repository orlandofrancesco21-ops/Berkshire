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

- `python scripts/exposure-history.py {TICKER}` — realised rolling-return distributions, drawdown depth and time-to-recovery. Reports how many windows are genuinely independent, because overlapping windows are the standard way this table misleads.
- What it cannot do: tell you what returns followed a given *starting valuation*.

**That capability is NOT YET BUILT, and this section says so rather than describing it as an absorb away.** It needs decades of valuation history, which is a time series rather than a document — and the vault's ingestion stack is text-only: `absorb` archives `.txt` and `.pdf`, the lint's locator forms are pages, timestamps, paragraphs and statutory sections, and `source-pages.py` globs `*.txt`. A spreadsheet has no rung. So a queued Shiller-style dataset currently has no defined landing.

Two ways to close it, neither done: add a dataset rung to `absorb` (archive the raw file, define a series locator convention such as `(sheet Data, col K, 1871-2026)`, extend the locator pattern), or build the derived artifact — a script that takes an absorbed series and reports realised forward 10-year real returns bucketed by starting-valuation decile — and cite that instead of a queue row. Until one exists, a fund valuation states the valuation-conditional question as an open gap rather than answering it.

## The honest caution about a fund's track record

The most prominent number on any factsheet is trailing performance, and it is the least useful. A fund with a superb trailing decade has, all else equal, a **worse** forward expected return, because part of that return was multiple expansion that has already happened and cannot happen twice. Backtested index history is not fund history and is never a track record.
