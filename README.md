# Personal investing research system

A structured workspace for long-only, long-term, low-frequency investing. Built around the principle that **durable industry knowledge compounds across decisions** — the right framework for evaluating businesses in a given sector beats faster generic analysis.

> Design rationale, gap list, and build history live in [`docs/build-plan.md`](docs/build-plan.md). Read that file before making structural changes to the system.

## Architecture

Three phases, each producing durable artifacts the next phase reads:

1. **Sector research** (`sectors/`) — weeks per sector. Output: primer, value chain, KPIs, players.
2. **Company analysis** (`sectors/{sector}/companies/{TICKER}/`) — days per name. Output: thesis, valuation, model.
3. **Portfolio monitoring** (`portfolio.md`, `journal/`) — continuous, low-noise. Output: position decisions.

Each company folder carries three documents: `thesis.md` (the argument, append-only log), `valuation.md` (the numbers, canonical), and `ic-sheet.md` — a one-page IC-memo view in plain bullets that a senior reader digests in under five minutes, regenerated from the other two on every deep-dive. Read the sheet first; open the deep documents where you want the reasoning.

Two cross-cutting knowledge tiers sit above all three phases, and they are the personal IP — the part that compounds:

- **`frameworks/`** — industry-specific evaluation playbooks. What is true of *an industry*.
- **`principles/`** — cross-industry investment principles with permanent citable IDs, each carrying attributed investor voices (who agrees, who diverges, and the conditions each holds under) and two independent tags: what the field supports, and what my own record shows. What is true of *investing*.

The routing test between them, and against a company thesis: would this sentence survive with the ticker **and** the industry deleted? Only then is it a principle. Canonical rule: "Principles routing" in [`docs/build-plan.md`](docs/build-plan.md).

Feeding `principles/` is [`library/`](library/README.md) — one distilled entry per absorbed external source (letter, memo, filing, podcast, book chapter), each takeaway locator-addressed and verification-labelled. Drop a file in `library/_inbox/` or paste a URL and run `absorb`; it retrieves, archives the raw source, distills, and fans what it learned out to whichever principles it actually touches.

## Folder map

```
.
├── principles/              # cross-industry investment principles (the IP that spans industries)
│   ├── _template.md         # blank template — ID rules, two-axis tags, Voices shape
│   └── README.md            # routing, index, alias table, split/merge rules
├── library/                 # one distilled entry per absorbed external source
│   ├── _inbox/              # DROP ZONE — put a PDF/article/transcript here, then run absorb
│   ├── sources/             # raw archive (gitignored; mirrored off-machine)
│   ├── _template.md         # entry schema
│   └── README.md            # how material gets in, verification labels
├── sources.md               # recurring sources + the absorption queue
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
│   ├── build-plan.md        # handoff brief; build history; rationale
│   ├── skill-dependency-map.md  # which skill reads/writes which file
│   └── README.md            # docs index
├── scripts/
│   ├── check-cross-references.py  # THE pre-commit gate — 8 check classes
│   ├── test-lint.py               # planted-violation cases proving each gate fires
│   ├── check-cadence.py           # the clock: session-start nag, silent when healthy
│   ├── pdf-extract.py             # PDF -> canonical page-addressed text (PyMuPDF)
│   ├── source-pages.py            # page-addressed search/read over the archive
│   └── mirror-sources.py          # off-machine backup of the gitignored archive
├── .mcp.json                # project MCP servers (edgartools)
└── .claude/
    └── skills/              # reusable Claude skills that read/write the above
        ├── evaluate/            # single-entry-point for "look at TICKER" (chains the three below)
        ├── framework-bootstrap/
        ├── sector-primer/
        ├── company-deep-dive/
        ├── valuation-check/
        ├── thesis-check/
        ├── portfolio-review/
        ├── news-triage/
        ├── earnings-prep/
        ├── earnings-debrief/
        ├── decision-log/
        ├── watchlist-revisit/
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
| Quarterly | `watchlist-revisit` | Sweeps "Passed (with reason)" and "Researched, waiting for entry" names; flags where the original pass/wait reason has materially changed. |
| On every position change | `decision-log` | Same-day structured record of BUY / ADD / TRIM / SELL / EXIT / PASS with the supporting verdicts; updates `portfolio.md`. Decisions are not optional. |
| On any position close | `post-mortem` | Within 30 days of exit. Reads the full thesis log, distills 1-3 lessons, writes back to the framework. The highest-ROI artifact in the system over a 5-year horizon. |

## Conventions

- One folder per sector under `sectors/`. Slugified name (e.g. `offshore-drilling/`).
- One folder per company under `sectors/{sector}/companies/{TICKER}/`.
- Tickers use exchange suffix where relevant (`ASML.AS`, `RIO.L`, etc.).
- Thesis docs are append-only and dated. Old thinking matters — never overwrite.
- Fair value is always a **range**, never a point. Point estimates are fake precision.

## Skills

Each skill lives in `.claude/skills/{skill-name}/SKILL.md`. The full set:

- `absorb` — **the ingestion path.** One external source per run: resolve (URL / description / dropped file) → retrieve down a per-type ladder → archive the raw text and pass the grounding gate → distill into `library/{slug}.md` with locators and verification tags → fan out to every principle theme it genuinely touches → flag any collision with an open thesis → lint, stage its own files, commit. Zero prompts for a plain investor letter.
- `consult` — **the read side.** "What do big investors say about this kind of situation?" Routes through the alias table and index to the relevant principle blocks, answers with IDs, attributed voices, verification labels and the conditions each view holds under — and when the corpus does not hold the answer, says so and queues the gap in `sources.md` rather than filling it from memory.
- `evaluate` — single-entry-point for "I want to look at TICKER" — chains framework-bootstrap → sector-primer → company-deep-dive automatically if prerequisites are missing. Use this when you don't want to orchestrate the three-step prereq chain yourself.
- `framework-bootstrap` — generates a new industry framework from `frameworks/_template.md`.
- `sector-primer` — produces a structured sector primer with supporting files.
- `company-deep-dive` — full company analysis grounded in the relevant framework + sector primer; writes `thesis.md` and `valuation.md`. Stops if prerequisites are missing — for the auto-bootstrapping convenience path, use `evaluate`.
- `valuation-check` — current price vs fair value band; HOLD / TRIM / ADD / REVIEW / EXIT recommendation.
- `thesis-check` — pulls material events since last thesis update; verdict against written kill switches (THESIS INTACT / WATCH / REVIEW).
- `portfolio-review` — sweeps every position; runs the per-name skills; produces a ranked weekly digest.
- `news-triage` — daily/weekly pass; filters into IGNORE / LOG / FLAG; defaults to suppression.
- `earnings-prep` — pre-commits criteria before each print so the post-print analysis isn't rationalization.
- `earnings-debrief` — grades the print against the prep; recommends next action.
- `decision-log` — captures every position change (BUY / ADD / TRIM / SELL / EXIT / PASS) the same day it happens, with the verdicts that informed it; updates `portfolio.md`. The bridge between research artifacts and actual position history.
- `watchlist-revisit` — quarterly sweep of "Passed" and "waiting for entry" names; flags where the original reason to pass or wait has been overtaken by reality.
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

Project-scoped MCP servers are configured in **`.mcp.json` at the repo root** (Claude Code does not read `mcpServers` from `.claude/settings.json`). The active config wires `edgartools`; see `.mcp.json.example` for placeholder patterns for future sources.

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
- `scripts/check-cross-references.py` verifies markdown links between files still resolve. It runs automatically as a **pre-commit hook** (`.githooks/pre-commit`). One-time setup on each new clone/machine: `git config core.hooksPath .githooks`. Bypass in an emergency with `git commit --no-verify`.

### Keeping the rituals honest

The monitoring cadence table above is the system's heartbeat, and prose alone has now failed to hold it **twice**: an 8-week silence (May-Jul 2026 — journal empty, two revisit dates blown through), and then 11 days during which the entire 2026-07-17 audit sat uncommitted. The failure mode is burst-then-silence: heavy research sprint, then nothing until something hurts.

So the guard is no longer a paragraph. `scripts/check-cadence.py` runs at session start and reports what is actually overdue — news-triage past 5 days, portfolio-review past 8, watchlist-revisit past 95, an open flag past 30, a held thesis past 180, **and a dirty tree whose oldest change is more than a week old** (that last one is the exact failure that stranded the audit). It also nags while `portfolio.md` still carries TBD trade details, and every ~90 days asks for one verification spot-audit.

Three design choices make it survive contact with a busy owner:

- **It is silent when healthy.** A check that prints a wall of yellow every day trains the dismiss reflex and dies the same death as the prose it replaced.
- **It is wired at user level too**, not just in this vault. Both documented silences involved *zero* Berkshire sessions — a vault-scoped hook would have fired exactly zero times. Any Claude Code session on this machine surfaces escalated items, once a day, and stays quiet inside the vault where the fuller report already runs.
- **Every nag names the command that fixes it**, which turns it from guilt into a button.

Minimum viable cadence if time is short: `news-triage` twice a week ("nothing material" takes two minutes and is the usual answer); `portfolio-review` every Monday, even on a tiny book; `earnings-prep` before every print, with the next report date calendared the day the previous debrief lands (`earnings-debrief` now prompts for exactly that); `watchlist-revisit` in the first week of each quarter.

Autonomous scheduled runs — having Claude execute news-triage and the Monday review unattended — are deliberately **not** built yet. The watchdog above is the floor; if rituals still slip twice inside six weeks despite nags firing, that is the trigger to add the scheduler, and to have it stamp a last-run date this same script then watches (so a dead scheduler is caught by the same mechanism that catches a skipped ritual).

### Restore on a new machine

1. `git config core.hooksPath .githooks` — otherwise the pre-commit gate is silently off. (`check-cadence.py` detects and nags about this.)
2. Set `BERKSHIRE_SOURCE_MIRROR` — the backup target for `library/sources/`. It must **not** be the Synera OneDrive; there is deliberately no default, so an unset mirror fails loudly instead of quietly leaking a private archive into company storage. Currently `C:\Users\FrancescoOrlando\Repo\Berkshire-source-archive`.

   Use PowerShell, **not** `setx`: `setx VAR "C:\path"` stores the quote characters as part of the value, and the script then hunts for a directory literally named `"C:\path"`. That is not hypothetical — it failed exactly that way here on the first attempt.

   ```powershell
   [Environment]::SetEnvironmentVariable('BERKSHIRE_SOURCE_MIRROR', 'C:\your\path', 'User')
   ```

   Be honest about what the current location buys: a local folder protects the archive against loss *from the vault* — a bad `git clean`, a deleted working copy, a re-clone — but **not** against disk failure or losing the machine. Point it at something replicated when convenient. The raw sources are the one artifact here that git does not protect, which is the whole reason this step exists.
3. In Obsidian: Settings → Files & Links → Excluded files → add `library/_inbox/` and `library/sources/`. Gitignore hides them from git, not from the quick switcher, search, or graph.
4. `pip install pymupdf yfinance` if absent, and confirm `uvx` is available for the `edgartools` MCP.
5. Sanity check: `python scripts/test-lint.py` (expect all cases passing) and `python scripts/check-cadence.py`.
