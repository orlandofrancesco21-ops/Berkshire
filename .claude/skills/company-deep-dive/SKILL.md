---
name: company-deep-dive
description: Produce a full long-form analysis of a single company, grounded in the relevant industry framework and sector primer. Reads frameworks/{industry}.md and sectors/{sector}/primer.md as context — assumes both already exist (for the auto-bootstrapping entry point that creates missing prerequisites, use the evaluate skill instead). Output is thesis.md and valuation.md in sectors/{sector}/companies/{TICKER}/; also handles the refresh of an existing thesis. Triggered by "deep dive on X", "company-deep-dive X", "refresh the X thesis", or "deep-dive X for the Y book".
---

# company-deep-dive

## When to use

The user wants to evaluate a specific company seriously — not a screen, not a quick look. Common phrasings:

- "Deep dive on [TICKER]"
- "Run company-deep-dive on [name]"
- "Let's evaluate [TICKER] for the [sector] book"

## Inputs

- Ticker (with exchange suffix where applicable — `ASML.AS`, `RIO.L`, `MSFT`)
- Sector folder it belongs in (must already exist; if not, stop and suggest `sector-primer` first)

## Process

0. **Determine mode: fresh or REFRESH.** If `sectors/{sector}/companies/{TICKER}/thesis.md` already exists, this run is a **REFRESH**, not a fresh write. In refresh mode:
   - Read the existing `thesis.md` and `valuation.md` in full before pulling any new data. The old thinking is calibration data, not something to discard.
   - **Preserve the Update log verbatim.** Every prior dated entry stays exactly as written — the first entry is the original bull case and `post-mortem` depends on it.
   - Rewrite the body sections in place (summary, bull case, bear case, capital allocation, management, kill switches, conviction, sizing logic) to reflect current reality.
   - Append a dated entry `### YYYY-MM-DD — deep-dive refresh` to the Update log summarizing *what changed and why* — which bull/bear points strengthened or died, any kill-switch rewording, conviction moves with reasoning.
   - Apply the same rules to `valuation.md`: rewrite scenario tables and bands in place, preserve and append to its update history.
   Fresh mode (no existing thesis.md) proceeds from the templates as described below.

1. **Confirm context exists.** Check that `sectors/{sector}/` and `frameworks/{industry}.md` both exist. If not, stop and ask the user to run the appropriate prior skill.

1b. **Check whether the framework is an umbrella.** Look for the marker line near the top of `frameworks/{industry}.md`: `**Umbrella framework:** yes` means triage-only, *explicitly* not decision-grade. (The presence of a "Sub-sector navigator" section does **not** by itself make a framework an umbrella — decision-grade frameworks may keep a navigator as triage context. The marker is the only signal. A framework with no marker line is treated as decision-grade.) If the marker says yes, do not proceed using the umbrella alone:
   - Identify which sub-sector this company belongs to from the navigator table (e.g. ASML.AS in the semis umbrella is "semiconductor equipment"; CEG in the energy umbrella is "Nuclear IPP").
   - Check whether `frameworks/{sub-sector-slug}.md` exists.
   - If yes: use the sub-framework as the **primary** lens for this deep-dive. The umbrella stays as supplementary context (cross-cutting principles, cycle position, regulatory backdrop).
   - If no: stop and recommend `framework-bootstrap {sub-sector-slug}` first. Do not attempt to deep-dive against an umbrella alone — the result will be a generic analysis, not framework-grounded.

   This enforces the discipline that umbrella frameworks aren't decision-grade. They're navigators.

2. **Load the lens.** Read both the operative framework (sub-framework if step 1b applied, otherwise the single industry framework) and `sectors/{sector}/primer.md` before doing anything else. The framework determines what questions matter for this company. Don't apply a generic deep-dive template.

3. **Pull the data:**
   - Latest 10-K and last 4 10-Qs (or 20-F / annual reports for non-US issuers)
   - Last 4 earnings transcripts (read prepared remarks AND Q&A — the Q&A is where signal lives)
   - Insider transactions (Form 4 for US issuers, equivalents elsewhere)
   - Long-term price + valuation multiple history (yfinance or similar)
   - Recent news (last 6-12 months)
   - Competitor filings for the same period (for read-through on industry conditions)

   For Claude Code: parallelize this. One subagent per data source.

4. **Write `sectors/{sector}/companies/{TICKER}/thesis.md`.** Use the template in `sectors/_example/companies/_TICKER/thesis.md`. Key sections:
   - One-sentence summary of what the business does
   - The bull case (3-5 framework-grounded points)
   - The bear case (3-5 framework-grounded points — take this seriously)
   - Capital allocation track record (5-year table with concrete dollar amounts: FCF, buybacks, dividends, M&A, capex)
   - Management quality assessment (tenure, ownership, comp structure, communication quality)
   - What would change my mind (specific, falsifiable signals — both bull-case kill switches and bear-case kill switches)
   - Conviction level (1-5) with explicit reasoning
   - Position sizing logic

5. **Run the valuation inline.** The valuation must use the multiples specified in `frameworks/{industry}.md` — not a generic DCF unless the framework calls for one.

6. **Write `sectors/{sector}/companies/{TICKER}/valuation.md`** using the template. Key outputs:
   - Primary valuation framework per the industry framework
   - Current state vs 5y average vs 10y range
   - Fair value range (low / base / high — never a point)
   - Sensitivity table on the 2-3 variables that matter most
   - Cross-checks
   - Hold / trim / add bands (this is what `valuation-check` reads)

7. **Save model code if you build any** to `sectors/{sector}/companies/{TICKER}/model.py`. It should be re-runnable with new inputs next quarter. (Ad-hoc scratch material can live in `sectors/{sector}/companies/{TICKER}/notes/` — no skill reads or writes it; it's human working space.)

8. **Date the thesis entry.** First entry under "Update log" should be dated today and summarize the initial write-up.

9. **Write back to the framework.** Append a dated entry to `frameworks/{industry}.md` under "What I've learned over time" with anything this deep-dive surfaced that *wasn't already in the framework*. The framework is the IP that compounds — every deep-dive should leave it richer than it found it. Format:

   ```
   - YYYY-MM-DD ({TICKER} deep-dive): {one or two sentences on what was new — a metric the framework hadn't named, a red flag pattern not previously captured, a valuation quirk specific to this archetype, etc.}
   ```

   The ` deep-dive` source tag distinguishes these from `post-mortem` entries, which are higher-signal (calibrated by actual returns). Future-you reading the log should be able to weight them differently.

   If the deep-dive surfaced nothing new beyond the existing framework, write that explicitly: `- YYYY-MM-DD ({TICKER} deep-dive): no framework-level updates — existing framework captured everything material.` Honest negatives are also calibration data.

   Do not silently rewrite other parts of the framework. New insights go in this append-only section. Restructuring the framework body is a separate, deliberate decision.

10. **Route the verdict to the watchlist or portfolio.** A deep-dive ends in one of three routings:

    **BUY-worthy** — hand off to the user for a decision; if they act, `decision-log` records it and updates `portfolio.md`.

    **WAIT (great business, wrong price)** — the most common non-BUY, non-PASS outcome. Append the company to `watchlist.md` under **"Researched, waiting for entry"** with: today's date, the fair value range, and an **explicit entry trigger** (a price level and/or a named event — "below $X" or "post-{event} clarity"). Append a dated entry to the thesis Update log: `### YYYY-MM-DD — WAIT` with the trigger. `watchlist-revisit` sweeps this section quarterly.

    **PASS (not confident enough to recommend)** — still a valid output; the work has value.
    - Append the company to `watchlist.md` under **"Passed (with reason)"**, filling every column of that table: today's date, a one-line reason (the specific bear-case or framework gap that drove the pass), and **"Revisit when"** (the specific condition that would reopen the question).
    - Do **not** delete `thesis.md` or `valuation.md` from `sectors/{sector}/companies/{TICKER}/` — they remain the source material for any future re-evaluation by `watchlist-revisit` (the quarterly re-evaluation skill).
    - Append a dated entry to the company's `thesis.md` Update log: `### YYYY-MM-DD — PASS` followed by `See watchlist.md. Reason: {short reason}.` (Dated heading format, same as every other Update-log entry — log parsers rely on one convention.)
    - The next `watchlist-revisit` sweep will check whether the reason for passing has materially changed.

    If `watchlist-revisit` re-opened this name and this deep-dive resolves it, also update or remove the company's existing watchlist row so it appears in exactly one section.

## Output

Files written, plus a verbal summary:

- The thesis in 3 sentences
- Fair value range (range, never a point)
- Current price vs that range
- The one thing that worries you most
- Recommended conviction level

## Notes

- This is a serious analysis. 30-50 hours of equivalent human work. Spend the tokens.
- Don't be afraid to say "I'm not confident enough to recommend." A pass is a valid output. Save the analysis to the watchlist.passed section if so.
- Append-only: every future update to the thesis adds a dated entry. Never overwrite.
- The bear case is where most analyses fail. Steelman it. If the bear case feels weak, you haven't worked it hard enough.
