---
name: decision-log
description: Capture a portfolio decision (BUY / SELL / TRIM / ADD / EXIT / PASS) the moment it happens, with structured supporting context pulled from thesis.md, valuation.md, and recent journal entries. Writes journal/{date}-decision.md with the action, size, price, fair-value-range-at-time-of-decision, the verdicts that informed the call, and a mandatory reasoning section. Also updates portfolio.md for BUY/ADD/SELL/EXIT actions. The bridge between research artifacts and actual position history — without it, future-you can't reconstruct why anything was bought or sold. Triggered by "log decision X buy", "I just bought X — log it", "decision-log: trimmed X 30%".
---

# decision-log

## When to use

Every time you transact. Common phrasings:

- "Log decision: bought [TICKER]"
- "Decision-log [TICKER] buy 4% at $X"
- "I just trimmed [TICKER] 30% — log it"
- "Pass on [TICKER] — log it" (for watchlist names you've decided not to pursue)

This is the skill that makes the journal discipline actually work. The journal is the bridge between what the research said and what you actually did — without per-decision entries written at the time, that bridge collapses into recall bias within a year. Run this skill **the same day** you transact, not "later this week."

## Inputs

- Ticker
- Action — one of: `BUY` / `SELL` / `TRIM` / `ADD` / `EXIT` / `PASS`
- Size — optional. Either % of portfolio (e.g. "3%"), absolute amount, or "full" for EXIT. If omitted, the skill will prompt.
- Price — optional. Defaults to current price via yfinance if not provided.

## Process

1. **Pull current price** from yfinance if not provided. Snapshot it in the entry — even if approximate, future-you will want a price.

2. **Locate and read the supporting files.** For any ticker that's been deep-dived:
   - `sectors/{sector}/companies/{TICKER}/thesis.md` — extract current conviction level, most recent `thesis-check` verdict, most recent `valuation-check` verdict (look in the Update log).
   - `sectors/{sector}/companies/{TICKER}/valuation.md` — extract current fair value range (low / base / high).

   If no thesis exists (a PASS on a name you haven't deep-dived, or a BUY without prior analysis — which is itself a red flag), note that explicitly in the entry. A BUY without a thesis-on-file deserves a loud `WARNING: no thesis on file at time of buy` in the decision entry.

3. **Pull recent context from `journal/`.** Within the last 7 days:
   - Read the most recent `journal/{date}-review.md` and `journal/{date}-triage.md` if present.
   - Extract any FLAG, action item, or recommendation involving this ticker.
   - Include in the supporting context block.

4. **Read `journal/_flagged.md`** for any active flag on this ticker. If present, surface it — an active flag at the moment of a BUY/ADD is a discipline question; an active flag at the moment of SELL/EXIT is expected.

5. **Write `journal/{YYYY-MM-DD}-decision.md`.** If a decision file for today already exists (multiple decisions same day), append a new entry rather than overwriting. Format:

   ```
   ## {TICKER} — {ACTION}
   **Time:** YYYY-MM-DD HH:MM (local)
   **Size:** {% of portfolio or absolute or "full"}
   **Price:** ${X}
   **FV range at decision:** ${low} – ${high} (last updated {date in valuation.md})
   **Position vs FV:** {% above/below base}

   **Supporting verdicts (from per-company files):**
   - Conviction (from thesis.md): {1-5}
   - Most recent thesis-check: {verdict, date}
   - Most recent valuation-check: {verdict, date}

   **Recent journal signals:**
   - {pull-through from review/triage/flagged.md or "none"}

   **Reasoning (mandatory — fill before clicking trade):**
   {Two sentences minimum. Why this action, why now, what would have stopped you.}

   **Discipline check:**
   - [ ] Thesis is not stale (per canonical rule in docs/build-plan.md)
   - [ ] No active flag in journal/_flagged.md, OR flag has been resolved by a thesis-check/earnings-debrief
   - [ ] FV range was updated within last 6 months OR a fresh valuation-check was just run
   - [ ] For BUY: a written thesis exists on file
   - [ ] For SELL/EXIT: the trigger maps to a written kill switch, a valuation hit, or a stated portfolio-level reason (no "I just felt like it")
   ```

6. **Update `portfolio.md` if applicable:**
   - `BUY` — add a new row with ticker, sector, today's date, cost basis (price × size), weight, conviction (pulled from thesis), thesis status (pulled from most recent thesis-check)
   - `ADD` — increase weight on existing row; do not change conviction unless the user explicitly requests
   - `TRIM` — decrease weight on existing row
   - `SELL` (partial) — same as TRIM
   - `EXIT` — do *not* remove the row from `portfolio.md` here. Confirm with the user that `post-mortem` should run, which will remove the row in its own step 11.
   - `PASS` — do not touch `portfolio.md` and do not write to `watchlist.md` either. `watchlist.md` is the write-territory of `company-deep-dive` (which appends to "Passed (with reason)" when a serious deep-dive concludes PASS). A `decision-log PASS` action records the decision in `journal/` only — it's the lightweight "I considered this and moved on" log. If the PASS is serious enough that the name should sit on the watchlist for future revisit, run `company-deep-dive` and let it write through the proper channel.

7. **Restate the reasoning back to the user in chat.** This is the verbal commitment that pairs with the written one. If the reasoning sounds weak when restated aloud, that's a signal — the user can still abort the action.

## Output

The decision entry as written to `journal/{YYYY-MM-DD}-decision.md`, restated in chat. Plus confirmation of any `portfolio.md` / `watchlist.md` updates. Plus, for `EXIT`, an explicit prompt: "Position closed. Run `post-mortem` now or within 30 days."

## Notes

- The reasoning section is not optional. If you can't articulate the why in two sentences before the trade, the decision isn't ready. The skill exists partly to enforce this gate — if running it feels annoying right before a trade, that's the skill working.
- "Price went up" / "Price went down" are not reasons. They're observations. The reason is what changed about the thesis, the valuation, or the portfolio's risk profile.
- Same-day, not "I'll log it later this week." Recall bias corrupts the reasoning within 24 hours.
- Resolved flags can be cited as the reason for a SELL/EXIT (e.g. "thesis-check returned REVIEW on YYYY-MM-DD, deep-dive refresh confirmed the kill switch, exiting per discipline"). Unresolved flags at the time of a BUY are a discipline failure — log them anyway, with the failure noted.
- The `Discipline check` checklist is not a gate that blocks the trade — it's a mirror. If three of five boxes are unchecked at the moment of a BUY, you're trading on instinct. That's allowed (this isn't a trading system) but the journal should be honest about it.
- Over time, the decision log + post-mortem corpus is what reveals patterns in your own behavior (e.g. "I always trim winners early and ride losers", or "I PASS on names that later compound 5×"). Without this skill writing the inputs, those patterns stay invisible.
