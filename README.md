# Personal investing research system

A structured workspace for long-only, long-term, low-frequency investing. Built around the principle that **durable industry knowledge compounds across decisions** — the right framework for evaluating businesses in a given sector beats faster generic analysis.

> Design rationale, gap list, and build history live in [`docs/build-plan.md`](docs/build-plan.md). Read that file before making structural changes to the system.

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
│   ├── _template.md         # blank template for new frameworks
│   └── README.md            # framework conventions
├── sectors/                 # active sector research, with companies inside
│   └── _example/            # template structure for a new sector
├── portfolio.md             # current holdings + conviction
├── watchlist.md             # names being researched
├── journal/                 # time-stamped append-only context (triage / review / decision / notes)
│   └── README.md            # journal filename conventions and rules
├── archive/                 # closed positions — post-mortems
│   └── _template.md         # post-mortem template
├── docs/                    # design notes
│   └── build-plan.md        # handoff brief; gap list; rationale
└── .claude/
    └── skills/              # reusable Claude skills that read/write the above
        ├── framework-bootstrap/
        ├── sector-primer/
        ├── company-deep-dive/
        ├── valuation-check/
        ├── thesis-check/
        ├── portfolio-review/
        ├── news-triage/
        ├── earnings-prep/
        ├── earnings-debrief/
        └── post-mortem/
```

## Workflow

**Starting a new sector deep-dive:**

1. If no framework exists for the industry, run `framework-bootstrap`.
2. Run `sector-primer` to produce the primer and supporting docs.
3. Hand-edit. Pressure-test. Add what's missing.

**Evaluating companies:**

1. Run `company-deep-dive` on each candidate; the sector primer + framework are the lens.
2. Compare the candidates side-by-side.
3. The winner gets a thesis and valuation file in `sectors/{sector}/companies/{TICKER}/`. Names that don't make the cut get logged to `watchlist.md` "Passed (with reason)" — pattern recognition compounds on what you historically pass on.

**Monitoring (low-frequency, deliberate):**

| Cadence | Skill | What it does |
|---|---|---|
| Daily / every few days | `news-triage` | Scans portfolio + watchlist for material events. Default output is suppression — "nothing material today" is the right answer most days. |
| Weekly (Monday ritual) | `portfolio-review` | Runs `thesis-check` + `valuation-check` per position, cross-references the two, produces a ranked digest of names needing attention. |
| 5-7d before each holding's print | `earnings-prep` | Translates each kill switch into a specific print observable and each bull/bear point into a "confirms if / refutes if" binary — committed *before* the print. |
| Within 48h after each print | `earnings-debrief` | Grades reality against the prep. Verdict drives whether to do nothing, monitor, run `thesis-check`, or run `company-deep-dive`. |
| Ad-hoc when a name is in question | `thesis-check` and/or `valuation-check` | Stress-test against written kill switches; check price vs. fair value range. |
| On any position close | `post-mortem` | Within 30 days of exit. Reads the full thesis log, distills 1-3 lessons, writes back to the framework. The highest-ROI artifact in the system over a 5-year horizon. |

## Conventions

- One folder per sector under `sectors/`. Slugified name (e.g. `offshore-drilling/`).
- One folder per company under `sectors/{sector}/companies/{TICKER}/`.
- Tickers use exchange suffix where relevant (`ASML.AS`, `RIO.L`, etc.).
- Thesis docs are append-only and dated. Old thinking matters — never overwrite.
- Fair value is always a **range**, never a point. Point estimates are fake precision.

## Skills

Each skill lives in `.claude/skills/{skill-name}/SKILL.md`. The full set:

- `framework-bootstrap` — generates a new industry framework from `frameworks/_template.md`.
- `sector-primer` — produces a structured sector primer with supporting files.
- `company-deep-dive` — full company analysis grounded in the relevant framework + sector primer; writes `thesis.md` and `valuation.md`.
- `valuation-check` — current price vs fair value band; HOLD / TRIM / ADD / REVIEW / EXIT recommendation.
- `thesis-check` — pulls material events since last thesis update; verdict against written kill switches (THESIS INTACT / WATCH / REVIEW).
- `portfolio-review` — sweeps every position; runs the per-name skills; produces a ranked weekly digest.
- `news-triage` — daily/weekly pass; filters into IGNORE / LOG / FLAG; defaults to suppression.
- `earnings-prep` — pre-commits criteria before each print so the post-print analysis isn't rationalization.
- `earnings-debrief` — grades the print against the prep; recommends next action.
- `post-mortem` — written within 30 days of every exit; writes back to the framework's lessons section.

Explicitly **deferred** (stub at `.claude/skills/compare-within-sector/SKILL.md.deferred`):

- `compare-within-sector` — stack-rank multiple deep dives within a sector. Build when there's a real felt need — typically after 3+ deep dives in one sector when a single name needs to be picked. Not before.

## Reading and editing

The repo is plain markdown — read or edit it in any markdown-aware tool. Recommended interface: **[Obsidian](https://obsidian.md/)**. The single source of truth is always the files on disk; Obsidian is just a viewer/editor over them. Open the repo folder as an Obsidian vault and you get wikilinks (cross-doc navigation between framework ↔ sector primer ↔ thesis ↔ valuation), backlinks (which other docs reference this one), a graph view of how the corpus connects, and a fast editor without leaving the markdown format the skills require.

**Setup:** install Obsidian → "Open folder as vault" → point at this repo's folder. Add Dataview as the one community plugin worth installing — it lets `portfolio.md` render as a live table querying frontmatter from each thesis file. `.obsidian/` is `.gitignored` so each machine has its own vault config (theme, plugins, layout) without polluting commits.

**Why Obsidian and not Notion / Cursor / GitHub web:** Obsidian wins on a personal markdown corpus because the files stay canonical and the skills can read what you've written. Notion fights the system — Notion blocks aren't markdown, two-way sync is lossy, and skills can't read it. Cursor or VS Code work as editors but aren't built for cross-doc reading. The GitHub web UI is fine for reading on mobile but awkward for editing.

## Data sources

This system assumes free-tier access to:

- **SEC EDGAR** — via the [`edgartools` Python library](https://github.com/dgunning/edgartools) or its [MCP server](https://www.edgartools.io/edgartools-mcp-for-sec-filings/). No API key needed. Required for `thesis-check`, `news-triage`, and `earnings-debrief` to pull 10-K / 10-Q / 8-K / Form 4 filings reliably on US issuers.
- **Yahoo Finance** — via `yfinance` (Python library, no MCP needed). Prices, basic fundamentals, multiples, and historical data. Used by `valuation-check`, `earnings-prep`, `post-mortem`, and `watchlist-revisit`.
- **Web search** — built into Claude. Used by `news-triage`, `sector-primer`, `framework-bootstrap`, `earnings-debrief` (for transcripts), and `watchlist-revisit`.

Configure MCPs in `.claude/settings.json`. See `.claude/settings.example.json` for the pattern.

### Gaps and future upgrades

- **Earnings transcripts.** There is no free, no-API-key transcript MCP at this writing. Fallback is web search to investor-relations pages or to public previews on Motley Fool, Seeking Alpha, or company-hosted PDFs. `earnings-debrief` is the most affected skill — accept that transcript quality will vary until a clean source is wired.
- **News.** Web search is sufficient for `news-triage`'s default cadence. A Bloomberg-, Reuters-, or FT-grade news MCP would be a future upgrade — particularly useful for catching adverse news inside the 24-72h window where reaction matters.
- **Non-US filings.** EDGAR covers US issuers only. The gaps you'll feel first:
  - **UK** — Companies House for filings and ownership; LSE RNS for ad-hoc announcements.
  - **EU** — ESMA-registered storage portals for each jurisdiction (BaFin for Germany, AMF for France, CONSOB for Italy, CNMV for Spain).
  - **Canada** — SEDAR+.
  - **Australia** — ASX announcements platform.
  - **Japan** — TDnet / EDINET.
  - **Brazil, India, others** — respective securities regulator portals.

  These can be wired as separate MCPs when you start covering non-US names seriously. Until then, web search to the relevant regulator's portal is the fallback.

## Security

This repo is intended to be **private**. It will contain your positions, cost basis, and conviction calls. The `.gitignore` blocks the obvious sensitive files (env, keys, cached data, local-only files), but the responsibility is on you to keep this repo private.

If you ever want to share specific frameworks publicly, fork them out into a separate public repo — never make this one public.

## Maintenance

- After the first real deep dive completes, copy a redacted version into `sectors/_example/` as a worked example. Templates are easier to follow with one filled-in example than with placeholders alone.
- Run `scripts/check-cross-references.py` periodically to verify markdown links between files still resolve. It walks the repo and reports any broken paths.
