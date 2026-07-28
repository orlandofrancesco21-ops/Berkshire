---
name: post-mortem
description: When a position closes, write a structured post-mortem to archive/. Reads the closed position's thesis.md and valuation.md including the full update log, computes the actual return, and produces a candid post-mortem using archive/_template.md. The highest-ROI artifact in the entire system over a 5-year horizon — every closed position teaches something, and the lessons compound. Also writes the lesson back into the relevant framework's "What I've learned over time" section, and — for a lesson that survives deleting the ticker *and* the industry — into `principles/`, where it grades the entry thesis's Principles check against the realized outcome and updates the item's `My record:` line, the one field this skill alone writes. Use when you exit a position, never later than 30 days after exit. Triggered by "post-mortem on X", "I sold X — write the post-mortem", "close out X".
---

# post-mortem

## When to use

Every time a position closes — winner or loser. Common phrasings:

- "Post-mortem on [TICKER]"
- "I sold [TICKER] — write the post-mortem"
- "Close out [TICKER]"

The non-negotiable rule: this skill runs within 30 days of exit, while the decision is still fresh. After that, hindsight bias corrupts the analysis and the lesson is half-lost.

The hardest cases to write are wins. Losses force introspection; wins encourage narrative. Write the win post-mortem with the same discipline as the loss — *which specific point was right, and how would I know it again?*

## Inputs

- Ticker
- Exit date (default: today)
- Exit price (default: pull current price)

## Process

1. **Locate the company files.** Find `sectors/{sector}/companies/{TICKER}/thesis.md` and `valuation.md`. Read the entire thesis including every update log entry — old thinking is the raw material for this exercise.

2. **Read `archive/_template.md`** as the starting structure. The output must follow this template.

3. **Compute returns.** Pull historical prices via yfinance from entry date to exit date.
   - Absolute return (price + dividends, in the holding currency)
   - IRR (annualized)
   - Return vs sector benchmark (sector ETF if available, or peer median)
   - Return vs broad index (S&P 500 for US, FTSE 100 for UK, STOXX 600 for EU, etc.)
   - Currency contribution if foreign

4. **Classify the outcome.** Pick one: WIN / LOSS / NEUTRAL. Defined by the bar set at entry (in the original thesis "Position sizing logic"), not by the sign of the return. A flat name where the thesis said "compound at 12% annually" is a LOSS, not a NEUTRAL.

5. **Reconstruct the entry thesis honestly.** Find the first dated entry in the Update log — that's the original bull case. Do not edit for hindsight. The point is to capture what you thought *then*, so you can compare to what actually happened.

6. **Identify the primary exit reason.** Pick one of:
   - KILL_SWITCH_TRIGGERED — a specific written kill switch fired (best case for system calibration — the discipline worked)
   - VALUATION_HIT — price reached or exceeded the top of the fair value range and no thesis-positive change justified expanding it
   - THESIS_INVALIDATED — the thesis broke but no specific kill switch was written. This is a framework failure — the kill switch should have been there. Note this loudly.
   - PORTFOLIO_REBALANCE — position size or sector exposure forced the exit, independent of the name's own thesis
   - SECTOR_VIEW_CHANGED — broader industry view shifted, not the specific company

   Cite the trigger event with a date.

7. **Write the three diagnostic sections** with discipline:
   - **What I got right** — 1-3 *specific* bull-case points that played out. Cite the original thesis.
   - **What I got wrong** — 1-3 specific points where the thesis was wrong. Be honest. "I underestimated X" is fine; "the market was wrong" is not.
   - **What was unknowable** — the 1-2 things that broke the thesis but couldn't have been seen at entry with reasonable diligence. Bar is high — "I didn't see it" doesn't qualify.

7b. **Grade the entry thesis's `## Principles check`.** That section was written at entry against stored principles; a realized return is the only thing that can score it. Grade each line, and write the grade down in the diagnostic section it bears on, carrying the permanent ID so the grade stays greppable per "Permanent IDs and addressing (canonical)":
   - **PREDICTIVE** — a VIOLATES or TENSION line named what actually went wrong. Quote it verbatim. If the position was taken anyway, say what overrode it: an advisory flag that was read and dismissed is a different failure from one that was never written.
   - **MISSED** — a trap that was already in the store fired, and the check never cited it. Name the ID. Least comfortable finding in the exercise and the most valuable one, so look for it deliberately instead of waiting for it to surface.
   - **IRRELEVANT** — an ALIGNS line turned out to have nothing to do with the outcome. Say so. An ALIGNS line that did no work is not support, it is padding.
   - **NOTHING TO GRADE** — the thesis predates the section, or it carried the sentinel and the outcome bears that out. A complete answer; do not manufacture a grade to have something to say.

   The grade is a record, not a verdict. It cannot move the outcome classification (step 4) or the exit reason (step 6): principles are advisory everywhere, per "Principle authority (canonical)", and the kill switches in `thesis.md` remain the only authoritative triggers.

8. **Distill 1-3 lessons.** These are the artifacts that compound. Each lesson should be (a) concrete, (b) generalizable beyond this one name, (c) actionable — in the framework if it is industry-specific, in `principles/` if it survives deleting the ticker *and* the industry (step 9b), routed per "Principles routing (canonical)". Example: "Capital allocators with a buyback-at-any-price habit destroy value in cyclicals" is a lesson. "I should be more careful" is not.

9. **Update the framework.** Append every lesson to `frameworks/{industry}.md` "What I've learned over time" section. Use the post-mortem source tag — these entries are higher-signal than deep-dive entries (calibrated by actual returns) and the tag preserves that distinction in the log. Format:

   ```
   - YYYY-MM-DD ({TICKER} post-mortem, {WIN/LOSS/NEUTRAL}): {lesson — one or two sentences}
   ```

   Also consider:
   - Should a new kill switch be added to the framework's red flags section?
   - Should "what good looks like" be revised for any KPI?
   - Should the historical valuation range be revised?

   Make those edits in `frameworks/{industry}.md` and note them in the post-mortem's "Framework / principles updates triggered" section.

9b. **Write back to `principles/`** — for any lesson that passed the cross-industry test in step 8. This is the vault's highest-grade evidence: the only place a stored principle meets a realized return.

   - **Find the item the closed position bears on** — by ID from the grades in step 7b, or through the Index and `**Scope:**` lines in `principles/README.md`. Append a dated calibration line to that item's **Log**:

     ```
     - YYYY-MM-DD ({TICKER} post-mortem, WIN|LOSS|NEUTRAL): {what the outcome showed}
     ```

     Then update its **My record:** line to say what the closed position showed, dated. The Log line is the ledger entry recording that change.
   - **Never mint a second item for a lesson an existing item already covers.** IDs are permanent per "Permanent IDs and addressing (canonical)", so a near-duplicate is permanent too, and from then on each copy gets cited half the time. If nothing covers the lesson, park it in the closest file's **Open questions** with the date and ticker; a genuinely new item or a new file is glance-confirm per "Tiered autowrite (canonical)".
   - **This skill is the sole writer of `My record:` lines in `principles/`.** No other skill touches that field. Ownership ambiguity is exactly what the vault's "if two skills write the same field, that's the bug" rule exists to prevent.
   - **You may move `my record:` (untested → validated | mixed). You may not touch `evidence:`.** The two tags are independent axes: `evidence:` tracks external support and moves only under "Maturity and tier-1 sources (canonical)" — one closed position is not a new primary origin. Per "Evidence weighting (canonical)", about the owner's own record his post-mortems outrank any absorbed external claim, so a `well-supported | mixed` mismatch is the signal to surface before the next sizing decision, not a contradiction to be settled in the famous investor's favour.
   - **"No stored principle bears on this outcome" is a complete result.** Say it and move on — but say it, because skipping the step silently is not the same thing: per "Stale principle (canonical)" an item whose `my record:` line predates a post-mortem on a position it bears on is thereby stale.

10. **Write the post-mortem** to `archive/{exit-YYYY-MM}-{TICKER}.md`. Filename uses **exit** year-month so the archive sorts by when the lesson was learned, not by when the position was opened. The `Entry: YYYY-MM` field in the frontmatter preserves the original entry context for sequencing.

11. **Remove the position from `portfolio.md`.** Do not delete the thesis or valuation files — they stay in `sectors/{sector}/companies/{TICKER}/` as the source material for the post-mortem and for future re-evaluation. Append a dated entry to the company's `thesis.md` Update log: `### YYYY-MM-DD — EXIT` followed by `See archive/{filename}.md.` (dated-heading format, same convention as every other Update-log entry).

12. **Write a `CLOSED.md` marker.** Create `sectors/{sector}/companies/{TICKER}/CLOSED.md` with a single line:

    ```
    Closed: YYYY-MM-DD. See archive/{exit-YYYY-MM}-{TICKER}.md
    ```

    The marker means future browsing of the sector folder (in `ls`, Obsidian, GitHub) immediately distinguishes live positions from closed ones without having to open `thesis.md` to find the EXITED note.

## Output

Confirmation of:
- File written: `archive/{exit-YYYY-MM}-{TICKER}.md`
- Framework updated: `frameworks/{industry}.md` ({N lessons appended, M kill switches added})
- Principles updated: `principles/{theme}.md` ({IDs} — Log line plus `My record:`), or "none — no stored principle bore on this outcome"
- Portfolio updated: position removed from `portfolio.md`
- Thesis log updated: exit note appended

Plus the 1-3 lessons, restated, so they land at the top of the user's attention before the conversation closes.

## Notes

- The post-mortem on a winner is the harder skill. Wins generate "I knew it" narrative; the work is to identify the *specific* reason it worked, not the comforting story. Reread the original thesis word-by-word — most "I knew" claims aren't actually in the thesis.
- Do not write a post-mortem in the same week you exit a hot loser. You'll be too angry to be useful. Wait two weeks, write then.
- If the lesson is "this name was idiosyncratic, no framework update needed," that's a valid conclusion — but be honest about it. Most losses contain at least one framework-level lesson.
- Filename convention is `{exit-YYYY-MM}-{TICKER}.md` (exit-year-month) so the archive sorts by when the lesson was learned. The frontmatter `Entry: YYYY-MM` field preserves entry-context for sequencing.
- If you find yourself unwilling to write the post-mortem, that's a signal — usually that the loss was discipline-related (you knew, you didn't act). Write it anyway. Especially that one.
- No lint can score whether a Principles check was *insightful* — the gate checks shape only: line count, resolvable IDs, a legal verdict token. Step 7b is the only feedback loop that ever grades the content, and it runs exactly once per closed position. Skip it and the section decays into boilerplate: three comfortable ALIGNS lines nobody ever checked against an outcome.
- post-mortem alone writes `My record:` in `principles/`. `absorb` adds Voices and moves `evidence:`; only a closed position can say what my own record shows.
- The lessons section is where the entire system pays for itself. A 5-year journal of these is the real IP. Treat it accordingly.
