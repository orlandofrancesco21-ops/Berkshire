---
name: news-triage
description: Daily (or every-few-days) pass over portfolio and watchlist names. Filters incoming news into three buckets — ignore, log, flag-for-thesis-check. The most important output is suppression: "nothing material today" is a valid and frequent answer. Without this skill, the only choices are read-everything (drowning) or read-nothing (blind). Writes the daily output to journal/{YYYY-MM-DD}-triage.md. Triggered by "news-triage", "morning triage", "what's happening on the book today", "anything I need to read".
---

# news-triage

## When to use

Daily, weekly, or whenever you feel the urge to "check in" on the market. Common phrasings:

- "News-triage"
- "Morning triage"
- "Anything I need to read on my names today?"
- "What's happened on the book this week?"

This is the skill that defends your attention. Without it, you read 30 headlines and act on the one with the most alarming verb. With it, you read a 5-bullet digest that says — most days — "nothing material, get back to work."

## Inputs

- Optional: lookback window (default 24h for daily, 7d for weekly)
- Optional: scope — `portfolio` (default), `watchlist`, `both`

## Process

1. **Load the universe.** Read `portfolio.md` (and `watchlist.md` if scoped). Extract every ticker.

2. **Pull news per name.** For each ticker in the window, gather:
   - Wire-service headlines (Bloomberg, Reuters, FT, WSJ — whatever's accessible via web search)
   - Company press releases (search company IR pages or corporate news feeds)
   - 8-K filings or equivalents (the EDGAR MCP if configured for US issuers)
   - Sector-level news that touches the name's framework drivers (rare but matters when it lands)

   For Claude Code: parallelize — one subagent per ticker.

3. **Classify every item into one of three buckets.** Be strict — the bias is toward IGNORE.

   **IGNORE** (most items end here):
   - Price commentary ("Stock up 3% on no news")
   - Analyst initiations/maintained ratings
   - Generic sector pieces with no name-specific content
   - Awards, conference appearances, IR roadshows
   - Insider transactions < $1M unless pattern-significant
   - Macro commentary unless it directly maps to a thesis driver

   **LOG** (context-worthy, not action-worthy):
   - Earnings dates announced
   - Management commentary at conferences (not new disclosures)
   - Sector M&A activity that affects competitive positioning
   - Sell-side analyst changes (note them but don't escalate unless 3+ in cluster)
   - Insider buys of any size (buys are signal, sales are usually noise)

   **FLAG** (potentially material — recommend `thesis-check`):
   - 8-K filings on Items 1.01 / 1.02 / 2.02 / 2.06 / 5.02 (material agreements, terminations, results, impairments, exec departures)
   - Pre-announcements of earnings (negative or positive)
   - Regulatory actions (investigations, settlements, license actions)
   - Acquisitions / divestitures the company is party to
   - Loss of a top-5 customer
   - Cluster of 3+ analyst downgrades within two weeks
   - Any news that maps directly to a kill switch written in the name's `thesis.md`

4. **Write the daily output** to `journal/{YYYY-MM-DD}-triage.md`. Format:

   ```
   # News triage — {YYYY-MM-DD}

   Lookback: {date} → {date}
   Scope: portfolio ({N names}) + watchlist ({M names})

   ## FLAGS — read these
   - {TICKER}: {one-line summary} → recommend thesis-check
   - {TICKER}: {one-line summary} → recommend thesis-check

   ## LOG — for context only, no action
   - {TICKER}: {one-line summary}
   - {TICKER}: {one-line summary}

   ## IGNORED — {count} headlines suppressed
   ({short note on whether anything seemed borderline}

   ## Nothing on
   {tickers with no news activity — confirms the silence is real, not a data gap}
   ```

5. **If there are zero FLAGs and zero LOGs**, write that explicitly:

   ```
   # News triage — {YYYY-MM-DD}
   Nothing material across portfolio + watchlist. {N} headlines suppressed.
   ```

   This is a common and correct output. Do not invent flags to justify the skill running.

6. **Do not run `thesis-check` from here.** Recommend it. The user (or `portfolio-review`) runs `thesis-check` deliberately, not as a side effect of news scanning.

## Output

The journal file path, plus a one-line summary to the chat:

```
{date}: {N} FLAGs, {M} LOGs, {K} IGNOREd. Written to journal/{YYYY-MM-DD}-triage.md.
```

If there are FLAGs, also surface them inline in the chat for immediate attention — the user shouldn't have to open the file to see what needs action.

## Notes

- The default failure mode of this skill is over-flagging. If you find yourself producing 5+ FLAGs per day across a 10-name portfolio, something is wrong — either you own too many names, you're too sensitive, or the news pipeline is being noisy. Recalibrate.
- The second failure mode is under-flagging — declaring INTACT silence when the company actually filed a material 8-K you missed. Mitigate by always checking EDGAR directly (or the local equivalent) for filings in the window, not just headline news.
- One downgrade is noise. Three downgrades in two weeks is signal. Same for upgrades — clustered estimate revisions almost always mean the sell-side is catching up to an operational reality.
- Insider sales are usually noise (tax, diversification, vesting). Insider *buys* are almost never noise. Asymmetric weighting.
- Macro news is almost always IGNORE for this system. The book is long-term and bottom-up. If "Fed raises rates 25bps" goes into FLAG, the discipline is broken.
- If the same name keeps generating LOGs week after week without any FLAG, that's its own signal — usually the sector is in motion and a fresh `sector-primer` pass is overdue.
- The journal file is append-only by date — you'll naturally end up with one file per day you run this. That's the point. The history is the calibration data for future-you.
