---
title: Stock Market Data Used in "Irrational Exuberance" (ie_data.xls)
type: dataset
author: Robert J. Shiller
published: 2026-08
retrieved-from: https://shillerdata.com/ — the versioned workbook link on that page
retrieval-path: rung 1, author's own data page. The VERSIONED link is the only current one — the plain `shillerdata.com/downloads/ie_data.xls` path and the econ.yale.edu mirror both served copies years stale when checked 2026-08-22 (ending 2024-09 and 2023-09). Fetched with `curl -L -o`; an HTML-oriented fetch returns the landing page, not the workbook.
source-span: sheet Data, rows 8-1875 — 1868 monthly observations, 1871-01 to 2026-08; sheet Disclaimer is one cell
archive: sources/shiller-ie-data.xls
extraction: pandas.read_excel via xlrd, 2026-08-23 — 2 sheets, Data 1877x22, header spans rows 1-7 so every locator below is a positional column address
tags: [valuation-discipline, narrative-and-cycle-models, process-discipline]
talking-book: no
---

**One-line:** The 155-year monthly record of US large-cap price, dividends, earnings, CPI and long rates behind CAPE — the primary file, so every valuation figure computed from it is verified rather than read off someone else's chart.

**Why it matters to my process/portfolio:** Every CAPE number in `frameworks/developed-market-equity.md` previously rested on a secondary rendering (multpl.com, capped `partial`). This file replaces the whole class of them with computed figures, and it is what `scripts/valuation-conditional.py` reads. It also answers the one question a starting-valuation argument always turns on — what actually followed from readings like today's — with the record rather than with a remembered statistic. It is US large-cap only, which is a limit worth stating every time it is used.

## Takeaways

- **Two sheets. `Data` carries 1,868 monthly rows, 22 columns, with a header block spanning rows 1-7 across merged cells — so it must be read positionally, by column address, not by header name.** Column map, which is the whole retrieval key: A date, B S&P Comp price, C dividend, D earnings, E CPI, F date fraction, G long rate GS10, H real price, I real dividend, **J real total return price**, K real earnings, L real TR scaled earnings, **M CAPE**, O TR CAPE, Q excess CAPE yield, R/S bond returns, T 10-year annualised stock real return, U bonds, V excess. (sheet Data, rows 1-7) [verified]
  - *Texture:* N and P are empty spacer columns. Reading by header name silently shifts every address by one or two.
- **The date column is `YYYY.MM` and January is the trap: as a float, January is `.01` and October is `.10`, which are different numbers and need no special case.** The intuition that a trailing zero is lost applies to the printed string, not to the stored float, and "fixing" it is what breaks January. (sheet Data, col A, 1871-01 to 2026-08) [verified]
  - *Texture:* This cost a real bug in this vault. A `.1 means October` special case fired on all 156 Januaries and relabelled them October, so the tool announced a record starting 1871-10 for a series that starts 1871-01, and its month counter sorted Jan 1872 nine months after Feb 1872. Column F, `Date Fraction` = year + (month - 0.5)/12, is unambiguous and settles it in one line.
- **CAPE and TR CAPE start ten years after the price series, in 1881-01, because they need a decade of trailing real earnings first.** 1,748 values against 1,868 price rows. Any join that assumes the two series are coextensive silently drops or misaligns the first decade. (sheet Data, col M and col O, 1881-01 to 2026-08) [verified]
- **For forward-return work use column J, `Real Total Return Price`, never column H, `Real Price`.** H excludes dividends; over a century the difference is most of the return, and a decomposition built on H understates real equity returns by roughly the dividend yield compounded. (sheet Data, col H and col J, 1871-01 to 2026-08) [verified]
- **The file already contains Shiller's own 10-year annualised real stock return in column T, which makes it a free correctness check on any forward-return code written against it.** (sheet Data, col T, 1871-01 to 2016-08) [verified]
  - *Texture:* Checked: this vault's own computation from column J agrees with column T to 0.000000 across all 1,628 overlapping months. That check is the reason the conditional-distribution figures below are quotable at all — without it they are one indexing error away from fiction. Note T ends 2016-08, ten years short of the data, because the last decade has no completed window.
- **The most recent months are partly estimated, and the file says so in a footer row most readers never scroll to.** As of this copy: the August price is the 1 August close rather than a month-end, October 2025 / July / August CPI are estimated, and the August GS10 is the 31 July value. (sheet Data, row 1876) [verified]
  - *Texture:* Worse, the input series stop before the outputs do: earnings (col D) end 2026-03 and dividends (col C) end 2026-06, while CAPE (col M) runs to 2026-08. So the headline "today's CAPE" rests on estimated recent earnings and estimated CPI. Quote it to two significant figures, not four, and never treat the last few months as settled.
- **`Excess CAPE Yield` (col Q) is Shiller's own answer to "but low rates justify the multiple", and its construction is reconstructible from the file: ECY = 1/CAPE − (GS10 − trailing 10-year CPI inflation).** Verified by reconstruction against all 1,748 published values, max absolute difference 0.000000. Latest reading 0.0097. (sheet Data, col Q, 1881-01 to 2026-08) [verified]
  - *Texture:* The real-yield leg uses realised trailing inflation, not an expectations measure — so ECY moves when the past decade's inflation is revised into the window, not only when the market reprices. That is a property to state when citing it, not a flaw.
- **Conditional distribution computed from this file, expanding-basis quintiles, 10-year forward real total return: cheapest quintile (CAPE 4.8-15.4) median +9.0%, range -4.2% to +20.0%; most expensive quintile (CAPE 18.0-44.2) median +4.8%, range -5.9% to +13.1%. Seven independent decades behind each.** (sheet Data, col J and col M, 1881-01 to 2016-08) [verified]
  - *Texture:* The gap between the cheapest and most expensive quintile medians is 4.2 points a year. The spread *inside* the most expensive quintile is 19 points. Starting valuation moves the centre of the distribution and barely narrows it, which is exactly why the output is a range to argue inside rather than a forecast.
- **The five most expensive starting months in the entire 145-year record all produced NEGATIVE real returns over the following decade.** CAPE 43.2 to 44.2, clustered 1999-07 to 2000-04, delivering -2.55% to -4.59% real per year for ten years. The worst was not the highest reading. (sheet Data, col M and col T, 1999-07 to 2000-04) [verified]
  - *Texture:* Today's 41.18 sits just below that cluster, at the 99th percentile on both the expanding and the full-sample basis. The honest reading is not "therefore -3%": it is that the record contains no example of a decade starting this expensive that ended well, and only five examples at all.

## Not captured

- **Columns B, C, E, G, I, K, L, R, S, U, V** — documented in the map above but not distilled. They are inputs to the derived series that matter here, or bond-side series with no current use in this vault. Addresses recorded so a later question does not require rediscovering the layout.
- **Shiller's methodology documentation on shillerdata.com and in *Irrational Exuberance* itself** — not read. So this entry says nothing about how the pre-1926 series was reconstructed, how the S&P predecessor indices were spliced, or why TR CAPE was introduced. `frameworks/developed-market-equity.md` already carries the September 2018 TR-CAPE provenance from the website; that claim is not re-derived here and this entry is not evidence for it.
- **The `Disclaimer` sheet** — read in full, one paragraph. Shiller disclaims accuracy and completeness and states he is not a registered investment adviser. No data, no methodology, nothing citable beyond that.
- **The exact versioned filename of the workbook downloaded** — not recorded at fetch time, which is a provenance gap in this entry rather than in the file. The next refresh should record it, because the plain path serves a stale copy and "shillerdata.com" alone does not identify which vintage produced these numbers. The sha256 of the archived copy begins `71c3636da5269b07`, which pins *this* file even if the URL is lost.
- **Any non-US, small-cap, or non-equity content** — there is none. This is the S&P 500 and its spliced predecessors. It is the wrong series for a world or European exposure, and the most likely way to misuse it.

## Fan-out

**Deliberately deferred, and this is the honest state.** No principle file was updated from this dataset. This entry was written to close a gap the fund-analytics audit found — a dataset archived and already being read by a script, with no citable entry behind it — and fanning it into `principles/` in the same pass would mix a retrospective fix with new principle evidence. A queue row is left in `sources.md`.

What this dataset is queued to change, in priority order:

- **VAL** — the strongest fit. Every valuation item that leans on "high multiples imply lower forward returns" can move from asserted to computed, with the important qualifier attached: the effect is real in the centre of the distribution and weak at the edges, and the within-bucket spread is wider than the between-bucket gap. The five-worst-starts finding is the single most usable figure in the file.
- **NARC** — the 1999-2000 cluster is the cycle-model case study with the outcome attached rather than the narrative. It is also a genuine constraint on cycle reasoning: five observations, one episode.
- **PROD** — the process items gain the column-T self-check as a named method: when a dataset ships a derived series, recompute it and compare before quoting anything else from the file.

Also pending: `frameworks/developed-market-equity.md` carries CAPE figures sourced to multpl.com at `partial`. They can now be recomputed from this file and relabelled `verified`, with the numbers restated to whatever this file actually says.
