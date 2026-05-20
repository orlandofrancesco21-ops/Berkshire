---
name: portfolio-review
description: Sweep every position in portfolio.md, run valuation-check and thesis-check on each, and produce a single ranked digest — which names need attention this week, why, and what action is implied. This is the Monday-morning ritual that turns the analyst output (thesis + valuation files) into a portfolio manager workflow. Reads portfolio.md, every position's thesis.md and valuation.md, and the relevant frameworks. Output is one digest, not 12 separate reports. Use weekly or before any portfolio-level decision (rebalance, cash deployment, sector tilt). Triggered by "portfolio-review", "run the Monday review", "sweep the book".
---

# portfolio-review

## When to use

Either invoked weekly (the standing ritual) or before a portfolio-level decision. Common phrasings:

- "Portfolio-review"
- "Run the Monday review"
- "Sweep the book — what needs attention?"
- "Anything I should be acting on this week?"

This is the skill that turns the system from a research workbench into a portfolio. Without it, theses sit unread between earnings and decisions get made on whichever name happens to be on your mind that morning. With it, the system tells *you* which name to focus on.

## Inputs

- None required. Default scope is every position in `portfolio.md`.
- Optional: `--watchlist` to also sweep `watchlist.md` (useful before deploying cash).
- Optional: `--sector {slug}` to scope to one sector.

## Process

1. **Load the universe.** Read `portfolio.md`. Extract every position: ticker, sector folder, conviction level, position size, entry date. If a position lacks a `sectors/{sector}/companies/{TICKER}/thesis.md` file, flag it — every position must have a thesis on file or it shouldn't be a position.

   Also read `journal/_flagged.md` (if present) — the shared state file `news-triage` writes to. Note any portfolio tickers with active flags, the date flagged, and the recommended follow-on skill. These are the names this review should prioritize, even if their `thesis-check` returns INTACT.

2. **Run thesis-check on every position.** Use the `thesis-check` skill's full process for each name. For Claude Code: parallelize — one subagent per ticker. Collect each verdict (THESIS INTACT / WATCH / REVIEW).

3. **Run valuation-check on every position.** Same pattern. Collect each recommendation (HOLD / TRIM / ADD / REVIEW / EXIT).

4. **Cross-reference the two verdicts.** The combined verdict matrix:

   | thesis-check | valuation-check | Combined action |
   |---|---|---|
   | INTACT | HOLD | HOLD — no action |
   | INTACT | ADD | ADD candidate — confirm position sizing |
   | INTACT | TRIM | TRIM candidate — confirm position sizing |
   | WATCH | HOLD | MONITOR — next event likely to escalate |
   | WATCH | ADD/TRIM | DEFER price action — resolve the WATCH first |
   | REVIEW | any | RE-DEEP-DIVE — do not act on price until thesis refreshed |
   | INTACT | REVIEW | RE-DEEP-DIVE — valuation logic is stale |

   The matrix is deliberately asymmetric: thesis status dominates valuation status. A REVIEW verdict on either axis suppresses price-based action.

5. **Rank by urgency.** Sort positions in this order:
   1. REVIEW combined verdicts (every one — these need a deep-dive refresh)
   2. Names with active flags in `journal/_flagged.md` even if INTACT (news-triage surfaced something; investigate before declaring no-action)
   3. WATCH combined verdicts (every one — these are next quarter's REVIEWs)
   4. ADD candidates with high conviction (4-5) — capital deployment opportunities
   5. TRIM candidates — risk management
   6. ADD candidates with lower conviction (1-3) — usually defer to higher-conviction ADDs
   7. Plain HOLD (everything else) — collapse into a single line

6. **Compute portfolio-level metrics.** Independent of name-by-name verdicts, report:
   - Total position count
   - Top 5 concentration (% of portfolio)
   - Sector concentration (any > 35%?)
   - Currency exposure (any single non-base currency > 30%?)
   - Cash level
   - Stale theses, per the canonical stale-thesis rule in `docs/build-plan.md` (Shared rules)

7. **Write the digest** to `journal/{YYYY-MM-DD}-review.md`. Format below.

8. **Do not modify any thesis or valuation files.** This skill aggregates; it does not write to per-company files. The per-company appends already happened when `thesis-check` and `valuation-check` ran in steps 2 and 3.

## Output

A single digest, in this exact shape:

```
Portfolio review — {YYYY-MM-DD}

Action items (top of mind this week):
1. {TICKER} — {combined verdict} — {one-sentence reason}
2. {TICKER} — {combined verdict} — {one-sentence reason}
...

Portfolio metrics:
- Positions: N
- Top 5 concentration: X%
- Sector concentration: {sector A X%, sector B Y%}
- Currency exposure: {breakdown}
- Cash: X%
- Stale theses (per canonical rule): {list or "none"}

Full sweep:
| Ticker | Thesis | Valuation | Combined | Reason |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

Stale-thesis flags:
- {TICKER}: last update YYYY-MM-DD — recommend company-deep-dive refresh
```

## Notes

- The point of this skill is suppression. Most weeks, the action items section should be short — 0-2 names. If it's consistently 6+, either you own too many names, you're being too sensitive in `thesis-check`, or your kill switches are too tight.
- Don't act on the digest the moment it lands. Sleep on REVIEW verdicts. The discipline is "the digest tells me where to focus this week," not "the digest tells me to trade today."
- A stale thesis (per the canonical rule) is not automatically a REVIEW. It just means the next REVIEW or major event triggers a `company-deep-dive` refresh. Don't refresh every thesis on a calendar — refresh when something changed.
- Sector concentration > 35% in one industry is fine if it's deliberate (a sector you've worked hard on). It's a problem if it's accidental drift. The skill flags; you decide.
- If two consecutive reviews produce the same WATCH on the same name without new information, that's a signal the WATCH should either escalate to REVIEW or be downgraded to INTACT. Don't leave names parked in WATCH forever.
- This skill is the right place to ask "do I own too many names?" If you can't recall each thesis from memory while reading the digest, you own too many.
