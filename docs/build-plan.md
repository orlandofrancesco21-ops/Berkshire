# Build plan — berkshire research system

> Handoff brief written 2026-05. Captures the design intent, what's built, what's still to build, and in what order. If you (future Francesco, or a future Claude session) wonder *why* something was built or skipped, this is the answer.

## Context: what this repo is and what we're optimizing for

This is a personal long-only, long-term, low-frequency investing research system. The user is Francesco — works in growth equity at Blume, this is his personal public-markets stack. Not a developer by background but comfortable in Claude Code + PowerShell on Windows.

Core principle: durable industry knowledge compounds across decisions. Frameworks are first-class IP. The right framework for evaluating businesses in a given sector beats faster generic analysis.

Three-layer architecture:

- `frameworks/` — industry-general playbooks (the IP that compounds across sectors)
- `sectors/` — sector primers + per-company deep dives and valuations
- `portfolio.md` + `watchlist.md` + `journal/` — ongoing state and monitoring

The bridge artifact that makes the system work is the pair `thesis.md` + `valuation.md` per company. The Analyst skills write them; the Portfolio Manager skills read them. There is no second source of truth.

Design rules that are non-negotiable:

- Thesis docs are append-only and dated. Never overwrite — old thinking matters for calibration.
- Fair value is always a range, never a point.
- Exit is never triggered by price alone — only by thesis change.
- Skills should be opinionated. Encode discipline into the tool so future-Francesco can't quietly drop it under emotional pressure.

## What's already built (and works conceptually)

- `framework-bootstrap` — generates new industry framework from `_template.md`
- `sector-primer` — produces `primer.md` + `value-chain.md` + `kpis.md` + `players.md`
- `company-deep-dive` — produces `thesis.md` + `valuation.md` per company
- `valuation-check` — reads thesis + valuation, recommends HOLD/TRIM/ADD/REVIEW/EXIT

Templates exist for: framework, sector (primer, value-chain, kpis, players), company (thesis, valuation), portfolio, watchlist.

## Gaps to fill — in priority order

1. **`thesis-check` skill** (highest priority — referenced twice by existing skills but doesn't exist). Pulls all material events since last thesis update (earnings, 8-Ks, insider transactions, material news, sell-side revisions if available). Single question: does anything trigger a kill switch written in `thesis.md`? Output: "thesis intact" OR "REVIEW: signal X potentially triggers kill switch Y." Appends a dated entry to the thesis log.
2. **`portfolio-review` skill.** Sweeps every position in `portfolio.md`, runs `valuation-check` + `thesis-check` on each, produces a single ranked digest: which names need attention, why, what action is implied. This is the Monday-morning ritual that makes the system usable as a portfolio manager and not just an analyst.
3. **`archive/` post-mortem template + skill.** When a position closes, write a structured post-mortem: entry thesis, what changed, return, what I'd do differently, what this teaches me. Highest-ROI artifact for calibration over a 5-year horizon. Currently `archive/` is an empty folder with no template.
4. **`news-triage` skill.** Daily or every-few-days pass over portfolio + watchlist. Filters news into ignore / log / flag-for-thesis-check. Most important output is suppression — "nothing material today" is a valid answer. Without this, the choice is read-everything (drowning) or read-nothing (blind).
5. **`earnings-prep` + `earnings-debrief` pair.** Earnings is the most predictable thesis-stress moment. `earnings-prep` reads the thesis 5 days before each holding's print, surfaces what to listen for based on kill switches. `earnings-debrief` reads the transcript afterward, appends to the thesis log.
6. **`compare-within-sector` skill.** Stack-rank multiple deep dives within a sector. Build when there's a real felt need — not before.

## Smaller things to fix while in the repo

- `journal/` is referenced in the workflow but has no structure or skill writing into it. Either define what lives there (weekly notes, decision log, both) or remove until defined.
- `portfolio.md` is a markdown table. Fine for now, but at 15+ positions migrate to `portfolio.yml` or `portfolio.csv` so concentration / sector / currency exposure checks can be programmatic.
- The `watchlist.md` "Passed" section is great — add a quarterly skill that flags passed names where the original reason has materially changed (price dropped, ownership changed, etc.).
- `company-deep-dive` should have an explicit final step writing back to `frameworks/{industry}.md`'s "What I've learned over time" section. Currently this is implicit; make it explicit.
- Cross-reference paths in templates use relative paths (e.g. `../../`-style climbs from a thesis file up to the sector primer or framework). When `thesis-check` and `portfolio-review` are added, verify these resolve correctly from each skill's working directory. Test with a real deep dive end-to-end before declaring done. Use `scripts/check-cross-references.py` to mechanically validate.

## MCPs needed for the monitoring skills

- **EDGAR** — the `sec-edgar-mcp` pattern in `.claude/settings.example.json` should be activated. Free, no API key. Needed for 10-K/10-Q/8-K/Form 4 pulls in `thesis-check`.
- **yfinance** — used as Python library directly, no MCP needed. Current prices, historical multiples.
- **Web search** — built into Claude. Used for news triage and sell-side commentary.
- For non-US issuers, plug in additional sources as needed (Companies House UK, ESMA portals EU).

## What this system is not

- **Not a screener.** The user is not trying to scan 5,000 names. He's evaluating 10-20 names per year deeply.
- **Not a backtester.** No historical strategy simulation. Theses are forward-looking.
- **Not a trading system.** No order execution. Recommendations are advisory; the user acts manually.
- **Not a generic financial-research tool.** The framework lens is the entire point — generic deep dives without framework grounding are explicitly out of scope.

## Voice and structure for new skills

Match the existing four skills exactly. Frontmatter with `name` and `description`. Sections: When to use → Inputs → Process (numbered) → Output → Notes. Notes section is opinionated — encode the discipline, not just the mechanics. The "this is the skill that prevents emotional trading" line in `valuation-check` is the right register.

## Suggested order

Start with `thesis-check`. Run it on a real holding end-to-end before moving on. Then `portfolio-review`. Then the archive post-mortem template. Then `news-triage`. Then earnings pair. Stop and use the system for a quarter before building anything else.

## Shared rules

Definitions that more than one skill depends on. Skills should reference these by name rather than restating slightly different versions — drift between versions is how subtle bugs are born.

### Stale thesis (canonical)

A thesis is **stale** if any of the following are true:

- (a) The most recent dated entry in the Update log of `thesis.md` is more than **6 months** old.
- (b) The company has reported earnings since the most recent thesis or valuation update (i.e. the most recent Update log entry predates the most recent earnings release).
- (c) A prior `thesis-check` returned **REVIEW** within the last **90 days** and no `company-deep-dive` refresh has run since.

Skills that depend on this rule: `valuation-check` (step 2), `thesis-check` (step 7), `portfolio-review` (step 6). When any of these skills detect a stale thesis, the recommendation is `company-deep-dive` refresh — *not* a price-based action.
