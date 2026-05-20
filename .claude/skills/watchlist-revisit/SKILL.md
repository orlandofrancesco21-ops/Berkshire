---
name: watchlist-revisit
description: Quarterly sweep over watchlist.md — specifically the "Passed (with reason)" and "Researched, waiting for entry" sections. For each name, pull current price, multiples, recent news, and insider activity; compare to the original reason for passing or waiting; flag names where that reason has materially changed (price dropped through entry trigger, founder ownership reversed, competitive position shifted, etc.). The point is to surface when your own past judgment has been overtaken by reality. Pattern recognition compounds on what you historically pass on. Writes to journal/{date}-watchlist-revisit.md. Triggered by "watchlist-revisit", "revisit the passed list", "quarterly watchlist sweep", "anything I passed on worth re-evaluating".
---

# watchlist-revisit

## When to use

Quarterly, or whenever you've recently re-evaluated the framework and want to check whether old PASS decisions still hold under the new lens. Common phrasings:

- "Revisit watchlist"
- "Quarterly watchlist sweep"
- "Anything on the passed list worth re-evaluating?"
- "Watchlist-revisit [TICKER]" (single name)

This is the skill that defends against the most expensive mistake in long-horizon investing: passing on a name at the wrong moment, then never re-checking because the original reason for passing felt permanent. Reasons that *were* permanent in 2020 are often not permanent in 2026. The skill forces the comparison.

## Inputs

- None required (default: sweep the whole `watchlist.md`)
- Optional: ticker to revisit just one name

## Process

1. **Read `watchlist.md`** in full. Extract every entry from:
   - **"Researched, waiting for entry"** — full thesis exists; just waiting for price or trigger.
   - **"Passed (with reason)"** — evaluated and declined; reason logged.

   Ignore the "Researching now" and "On the radar" sections — those don't have a prior reason to compare against.

2. **For each name in scope, pull current data.** Parallelize with subagents if running across the full list:
   - Current price (yfinance)
   - Current value of whatever multiple was the basis for the original reason (e.g. if passed at "30x P/E too expensive", pull current P/E)
   - Material news in the last 90 days (web search + EDGAR if US issuer)
   - Insider activity in the last 90 days (Form 4 for US; equivalents elsewhere) — especially buys
   - Major shareholder changes (top-5 holder shifts via 13F-type filings where available)

3. **For each name, compare current state to the original reason.** This is the only step that matters. Examples of patterns that flip a PASS into FLAG:

   | Original reason | What flips it |
   |---|---|
   | "Too expensive — 30x P/E" | Now 12-15x (without obvious deterioration in business) |
   | "Founder sold his entire stake" | Founder or family back in materially |
   | "Customer concentration > 50% in single name" | Concentration now < 30% |
   | "Pre-FCF, capital cycle question" | First positive FCF year delivered + balance sheet de-risked |
   | "Hostile regulator" | Regulator changed / new ruling resolved the overhang |
   | "Capital allocation track record poor" | New CFO + new buyback at depressed prices |
   | "Cyclical peak" | Trough delivered + counter-cyclical capex in place |

   For "waiting for entry" names: the comparison is simpler — has the entry trigger fired? (Price below $X, multiple compressed to Y, catalyst event occurred, etc.)

4. **Produce per-name verdicts:**
   - **STILL VALID** — original reason for passing/waiting still holds. No action.
   - **FLAG** — the reason for passing/waiting has materially changed. Recommend `company-deep-dive` refresh.
   - **TRIGGER FIRED** (waiting-for-entry only) — the buy trigger has fired. Recommend `decision-log` (BUY/ADD) with a fresh `valuation-check` first to confirm the FV range hasn't drifted.

5. **Write the output** to `journal/{YYYY-MM-DD}-watchlist-revisit.md`. Format:

   ```
   # Watchlist revisit — {YYYY-MM-DD}

   Scope: {N} names from "Passed", {M} names from "Researched, waiting for entry"

   ## FLAGGED — reason for passing/waiting has changed
   - {TICKER}: passed {original-date}. Original reason: {X}. Now: {Y}. → recommend company-deep-dive refresh.
   - ...

   ## TRIGGER FIRED — entry trigger reached on waiting-list name
   - {TICKER}: waiting for {trigger}. Now {state}. → recommend valuation-check, then decision-log if confirmed.

   ## STILL VALID — no change
   - ({collapsed count}, e.g. "8 of 12 passed names: original reason still holds.")
   ```

6. **Do not modify `watchlist.md` directly.** This skill produces FLAGs; the user (or a follow-on `company-deep-dive`) decides whether to move a name from "Passed" back to "Researching now". Silently moving names between sections corrupts the calibration trail.

## Output

A ranked list of flagged + trigger-fired names with recommended next actions, restated in chat. Plus the journal file path.

If nothing has changed materially across the whole watchlist: `Watchlist revisit — {date}: no flags. {N} names re-verified.` This is the most common output when run on cadence, and that's fine — the skill exists to confirm absence as much as to surface presence.

## Notes

- The most valuable output of this skill, over years, is the pattern that emerges from your PASS decisions. If `watchlist-revisit` repeatedly FLAGs the same kind of pass ("I always pass on cyclicals at the trough — and they always compound"), that's a framework-level lesson. Write it to the relevant framework's "What I've learned over time" section.
- Don't conflate "the reason changed" with "I should buy now." The skill surfaces the question; `company-deep-dive` answers it. A FLAG is permission to re-evaluate, not a recommendation to act.
- Run quarterly, not monthly. Monthly is too frequent — most pass reasons that hold for a quarter hold for a year. Monthly creates the temptation to chase prior PASSes that have rallied without re-doing the analytical work.
- "Stock dropped 30%" is rarely a flip on its own — price alone is not a reason. Pair it with whatever was the actual reason for passing. ("Passed because too expensive at 30x" + "now at 12x" = legitimate flip. "Passed because founder sold" + "now down 30%" = unrelated; pass still valid.)
- Resolved FLAGs (i.e. names that have been re-deep-dived after a flip and either bought or passed again) should be re-added to the appropriate `watchlist.md` section by the deep-dive that resolves them. This skill doesn't track flag-resolution state — the per-section position in `watchlist.md` is the state.
