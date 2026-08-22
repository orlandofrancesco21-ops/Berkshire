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

1. **Load the universe.** Read `portfolio.md`. Extract every position: ticker, sector folder, conviction level, position size, entry date. Resolve each position's documents through both tiers, in this order — the same lookup the lint's own `position_doc()` performs: `sectors/{sector}/companies/{TICKER}/`, then `funds/{TICKER}/`. A position is an orphan only if **neither** tier holds a `thesis.md`; flag those, because every position must have a thesis on file or it shouldn't be a position.

   An allocated fund with a thesis in `funds/{TICKER}/` is a fully documented position and is never flagged. It has no sector folder by design — per "Funds tier (canonical)" a fund's peer set is other funds on the same exposure, so an S&P 500 tracker has no sector to sit in, and a sweep that reads a missing sector folder as a missing thesis would flag the vault's own correct output every Monday.

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
   | WATCH | REVIEW | RE-DEEP-DIVE — both axes are wobbling |
   | REVIEW | any | RE-DEEP-DIVE — do not act on price until thesis refreshed |
   | INTACT | REVIEW | RE-DEEP-DIVE — valuation logic is stale |
   | any | EXIT | ESCALATE — sleep on it, then `decision-log` discussion; EXIT is never executed from a sweep |

   The matrix is deliberately asymmetric: thesis status dominates valuation status. A REVIEW verdict on either axis suppresses price-based action.

   **Funds enter the same matrix, but `thesis-check` returns two verdicts for them.** Take the worse of the exposure and vehicle verdicts into the matrix, and carry the lens that fired into the reason column — because the implied action differs and the matrix cannot see it: an exposure REVIEW is a RE-DEEP-DIVE on the asset class, a **vehicle** REVIEW is a fund switch (`fund-deep-dive` to name the substitute), and neither is an EXIT. Per "Funds tier (canonical)" the two never collapse into one number. A fund's ADD/TRIM likewise comes from `valuation-check`'s allocation bands and its drift-from-target-weight rule, not from a price against a fair value, so a TRIM row on a fund may be a rebalancing rule firing rather than a view — say which in the reason column.

5. **Rank by urgency.** Sort positions in this order:
   1. REVIEW combined verdicts (every one — these need a deep-dive refresh)
   2. Names with active flags in `journal/_flagged.md` even if INTACT (news-triage surfaced something; investigate before declaring no-action)
   3. WATCH combined verdicts (every one — these are next quarter's REVIEWs)
   4. ADD candidates with high conviction (4-5) — capital deployment opportunities
   5. TRIM candidates — risk management
   6. ADD candidates with lower conviction (1-3) — usually defer to higher-conviction ADDs
   7. Plain HOLD (everything else) — collapse into a single line

6. **Compute portfolio-level metrics — from current prices, not the stored weights.** The `Current weight` column in `portfolio.md` is only as fresh as the last sweep; recompute it now. For each position: shares (from `portfolio.md`) × current price (yfinance, per the canonical price-sourcing rule in `docs/build-plan.md` Shared rules), converted to the base currency declared at the top of `portfolio.md`. Total portfolio value = sum of position values + Cash line. Then report:
   - Total position count
   - Top 5 concentration (% of portfolio)
   - Sector concentration (any > 35%?). Funds have no sector: report each under its exposure slug on its own line, and never bucket one into a sector because of what it happens to hold. Where a fund's holdings genuinely overlap a directly-held name, that is an overlap finding for `fund-deep-dive`'s allocation logic, computed from the holdings file — not something to assert here from names.
   - Currency exposure (any single non-base currency > 30%?)
   - Cash level
   - Stale theses, per the canonical stale-thesis rule in `docs/build-plan.md` (Shared rules)

7. **Write the recomputed numbers back to `portfolio.md`.** This is the one file this skill updates: the `Current weight` column per position, the `Total portfolio value` line, the Concentration check section (each figure dated today), the `Thesis status` column from today's verdicts, and the `Last reviewed` date. If the book is empty, just set `Last reviewed` and state that explicitly.

8. **Write the digest** to `journal/{YYYY-MM-DD}-review.md`. Format below.

9. **Do not modify any thesis or valuation files.** This skill aggregates; per-company writes already happened when `thesis-check` and `valuation-check` ran in steps 2 and 3. `portfolio.md` (step 7) is the only file this skill updates directly.

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
- This skill is the right place to ask "do I own too many names?" If you can't recall each thesis from memory while reading the digest, you own too many. Count funds separately when you ask it: one broad tracker is one decision, not five hundred, and folding it into the name count makes a deliberately simple book look unmanageable.
- A sweep that flags a correctly-documented position is worse than one that misses a real problem, because it trains the reader to skim the flag list. The orphan check in step 1 is the one most likely to do that — it fires on a *missing document*, and a document living in the other tier is not missing.
