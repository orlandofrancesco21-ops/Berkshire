# Frameworks

Evaluation playbooks. **The IP that compounds.**

## Three kinds of file in this folder

The folder started as one file per industry and is no longer that. Read this table before assuming which template a file follows.

| Kind | What it is | Starts from | Written by | Read by |
|---|---|---|---|---|
| **Industry playbook** | one file per industry — a set of competing businesses, where the analysis is about the dispersion *between* operators | `_template.md` | `framework-bootstrap`, industry mode | `company-deep-dive`, and the sector skills |
| **Exposure lens** | one file per asset class — no operator, no moat, no capital-allocation decision to grade; the output is an expected-return range over a stated horizon | `frameworks/_template-exposure.md` | `framework-bootstrap`, exposure mode | `fund-deep-dive` |
| **The vehicle lens** | exactly one file, `frameworks/etf-vehicle-mechanics.md` — wrapper mechanics, replication, domicile, tracking difference, securities lending, tax wrapper. Universal: it applies whatever the fund holds | nothing — it is hand-written once and **never bootstrapped**, because there is no second one to be consistent with | hand-edited | `fund-deep-dive`, alongside the exposure lens |

A fund deep-dive reads **two** of these: the exposure lens for what the holdings are worth, and the vehicle lens for what the wrapper does to that. Neither substitutes for the other — the best fund tracking a bad exposure is still a bad allocation, and a good exposure bought through a leaky wrapper gives back the premium it earned.

## Exposure-slug registry

`fund-deep-dive` resolves a fund to an exposure through this table. Match on the **index the fund actually tracks**, not on the product name.

| Index family the fund tracks | Exposure slug | Status |
|---|---|---|
| MSCI World, FTSE Developed, S&P Developed BMI — developed markets, large and mid cap, market-cap weighted | `developed-market-equity` | live |
| MSCI World IMI, FTSE Developed All Cap — the same universe **plus small caps** | none yet | near-substitute, not the same exposure: check the small-cap delta or bootstrap it |
| MSCI ACWI, FTSE All-World — developed **plus emerging** | none yet | bootstrap |
| S&P 500 (and its exact trackers: VUAG/VUSA, CSPX, SXR8, VOO, SPY, IVV) | `sp500` | live — US large-cap, committee-selected, single-country. Deliberately **not** `developed-market-equity` |
| MSCI USA, Russell 1000, and any other single-country large-cap index | none yet | a *different* single-country index from the S&P 500 (rules-based, different count) — bootstrap its own, do not route to `sp500` |
| Any factor, sector or thematic index | none yet | different exposure, different anchor; bootstrap |

**When no row fits — and today most funds hit no row — stop rather than stretching the nearest one.** Run `framework-bootstrap` in exposure mode and add the row. Two indices share a slug only if they share a return decomposition *and* an anchor; differing country classification or small-cap treatment is a delta to check inside one framework, but a different asset class is a different file. Whoever creates an exposure framework adds its row here in the same run, or the framework is an orphan no fund deep-dive can find.

## How to use

- One file per industry, or per asset-class exposure. Slugified filename: `banks.md`, `mining.md`, `offshore-drilling.md`, `saas-vertical.md`, `developed-market-equity.md`.
- Start from the right template — `_template.md` for an industry, `frameworks/_template-exposure.md` for an exposure. Don't deviate from the structure unless you have a reason — consistency makes cross-framework comparison easier.
- Refine after every deep dive. The "What I've learned over time" section is the most valuable one over a 5-year horizon. For an exposure the highest-signal entry is a realized 10-year window closing on a range the file produced.

## When to create a new framework

When you're about to evaluate a name in an industry you don't yet have a framework for, or a fund in an exposure you don't yet have one for. Run `framework-bootstrap` to generate a draft, then hand-edit before using it for any real decision.

## When to split or merge

- **Split** when one framework is being stretched across genuinely different businesses (e.g. "tech" → split into "vertical SaaS", "ad-supported consumer", "semis-equipment").
- **Merge** rarely. If you're tempted, the answer is usually that one of the frameworks is just underdeveloped.

## Template sections worth knowing about

Two sections in `_template.md` are easy to skim past but deserve deliberate attention. Both carry over to `frameworks/_template-exposure.md` under the exposure names ("Sub-exposure navigator", same `Umbrella framework:` marker line read the same way) — and the exposure template adds a third, the **history proxy** field, which names the ticker `scripts/exposure-history.py` is actually run on and why it is not the fund's own.

- **Sub-sector navigator (optional).** Keep this section if the framework spans several related business models — either a true umbrella industry (financials, energy, industrials) or a decision-grade framework that still benefits from triage context (e.g. managed care). Whether `company-deep-dive` requires a matching sub-framework before proceeding is governed by the **`Umbrella framework:`** marker line at the top of the file (`yes` = triage only, sub-framework required; `no` = decision-grade, navigator is context). Delete the section entirely if the framework is for a single coherent business type (e.g. "offshore drilling" — no sub-sectors needed).
- **Mental-model crossover risks (required).** The assumptions that *don't* transfer from your other frameworks into this one. Every framework needs this, even if short, because the most reliable analytical mistakes come from importing heuristics that worked elsewhere ("scale wins", "recurring revenue is stable", "network effects compound") into industries where they don't. If your other frameworks are software and this is heavy industry — or vice versa — that section is where you write the warnings to your future self.
