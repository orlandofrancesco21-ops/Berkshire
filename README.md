# Personal investing research system

A structured workspace for long-only, long-term, low-frequency investing. Built around the principle that **durable industry knowledge compounds across decisions** — the right framework for evaluating businesses in a given sector beats faster generic analysis.

## Architecture

Three phases, each producing durable artifacts the next phase reads:

1. **Sector research** (`sectors/`) — weeks per sector. Output: primer, value chain, KPIs, players.
2. **Company analysis** (`sectors/{sector}/companies/{TICKER}/`) — days per name. Output: thesis, valuation, model.
3. **Portfolio monitoring** (`portfolio.md`, `journal/`) — continuous, low-noise. Output: position decisions.

A cross-cutting **frameworks library** (`frameworks/`) holds industry-specific evaluation playbooks that apply across all phases. This is the personal IP — the stuff that compounds.

## Folder map

```
.
├── frameworks/              # industry-specific evaluation playbooks (the IP)
│   └── _template.md         # blank template for new frameworks
├── sectors/                 # active sector research, with companies inside
│   └── _example/            # template structure for a new sector
├── portfolio.md             # current holdings + conviction
├── watchlist.md             # names being researched
├── journal/                 # weekly notes, decision log, news triage
├── archive/                 # closed positions, retired theses
└── .claude/
    └── skills/              # reusable Claude skills that read/write the above
        ├── framework-bootstrap/
        ├── sector-primer/
        ├── company-deep-dive/
        └── valuation-check/
```

## Workflow

**Starting a new sector deep-dive:**

1. If no framework exists for the industry, run `framework-bootstrap`.
2. Run `sector-primer` to produce the primer and supporting docs.
3. Hand-edit. Pressure-test. Add what's missing.

**Evaluating companies:**

1. Run `company-deep-dive` on each candidate; the sector primer + framework are the lens.
2. Compare the candidates side-by-side.
3. The winner gets a thesis and valuation file in `sectors/{sector}/companies/{TICKER}/`.

**Monitoring (low-frequency, deliberate):**

1. Earnings-driven: when a holding reports, re-read the thesis and append what changed.
2. Weekly: a news triage pass produces `journal/{date}.md`.
3. Quarterly: run `valuation-check` on every position. Hold / trim / add / exit.

## Conventions

- One folder per sector under `sectors/`. Slugified name (e.g. `offshore-drilling/`).
- One folder per company under `sectors/{sector}/companies/{TICKER}/`.
- Tickers use exchange suffix where relevant (`ASML.AS`, `RIO.L`, etc.).
- Thesis docs are append-only and dated. Old thinking matters — never overwrite.
- Fair value is always a **range**, never a point. Point estimates are fake precision.

## Skills

Each skill lives in `.claude/skills/{skill-name}/SKILL.md`. The starter set:

- `framework-bootstrap` — generates a new industry framework from scratch.
- `sector-primer` — produces a structured sector primer with supporting files.
- `company-deep-dive` — full company analysis, grounded in the relevant framework.
- `valuation-check` — current price vs fair value band, with hold/trim/add/exit recommendation.

Add more (`compare-within-sector`, `thesis-check`, `news-triage`, `portfolio-review`) as patterns emerge from your workflow. Don't pre-build skills you haven't yet felt the need for.

## Data sources

This system assumes free-tier access to:

- **SEC EDGAR** — via the [`edgartools` Python library](https://github.com/dgunning/edgartools) or its [MCP server](https://www.edgartools.io/edgartools-mcp-for-sec-filings/). No API key needed.
- **Yahoo Finance** — via `yfinance` for prices and basic fundamentals.
- **Web search** — built into Claude.

Configure MCPs in `.claude/settings.json`. See `.claude/settings.example.json` for the pattern.

For non-US filings, plug in additional data sources as needed (Companies House for UK, ESMA-registered filing portals for EU).

## Security

This repo is intended to be **private**. It will contain your positions, cost basis, and conviction calls. The `.gitignore` blocks the obvious sensitive files (env, keys, cached data, local-only files), but the responsibility is on you to keep this repo private.

If you ever want to share specific frameworks publicly, fork them out into a separate public repo — never make this one public.
