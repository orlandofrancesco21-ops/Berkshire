---
name: thesis-check
description: For a held position (or watchlist name with an existing thesis), pull every material event since the last thesis update and ask one question — does anything trigger a kill switch written in thesis.md? Reads thesis.md and the relevant industry framework. Output is "thesis intact" or "REVIEW: signal X potentially triggers kill switch Y" with a dated entry appended to the thesis update log. Use when an earnings release lands, when a position has dropped or rallied sharply, when portfolio-review flags a name, or as a standalone gut-check before adding/trimming. Triggered by "thesis-check X", "is the X thesis still intact", "X just reported, run a thesis-check".
---

# thesis-check

## When to use

Either invoked directly on a single name, or by `portfolio-review` across all positions. Common phrasings:

- "Thesis-check [TICKER]"
- "Is the [TICKER] thesis still intact?"
- "[TICKER] just reported — run thesis-check"
- "Something feels off on [TICKER], check the thesis"

This is the skill that separates noise from signal. The whole point is to stress-test the specific, falsifiable kill switches written in `thesis.md` — not to re-do the original analysis. If you find yourself re-arguing the bull case, you're doing the wrong skill. Run `company-deep-dive` instead.

## Inputs

- Ticker (with exchange suffix where applicable — `ASML.AS`, `RIO.L`, `MSFT`)
- Optional: a specific event to investigate (e.g. "thesis-check ASML.AS focused on the latest earnings")

## Process

1. **Locate the company files.** Find `sectors/{sector}/companies/{TICKER}/thesis.md` and `valuation.md`. If `thesis.md` doesn't exist, stop — there's no thesis to check. Suggest `company-deep-dive` first.

2. **Read the kill switches.** Open `thesis.md` and extract:
   - The "What would change my mind" section (bull-case kill switches AND bear-case kill switches)
   - The most recent dated entry in the Update log — this is the "since when" boundary
   - The Conviction level (a check on a 5-conviction name should be more rigorous than on a 2)

   Also read `frameworks/{industry}.md` "Red flags specific to this industry" — these are kill switches the user may not have explicitly written into the thesis but the framework says to watch for. Treat them as additional candidate triggers.

3. **Establish the lookback window.** Default: from the date of the most recent Update log entry to today. If that's < 30 days, extend back to 90 days — short windows miss slow-developing signals.

4. **Pull material events in the window.** For US issuers, via EDGAR MCP if configured:
   - All 8-Ks filed (Items 1.01, 1.02, 2.02, 2.06, 5.02, 5.07, 7.01, 8.01 are the ones that usually matter)
   - The most recent 10-Q or 10-K filed in the window (if any)
   - Form 4 insider transactions — flag any sales > $1M or any meaningful buys
   - Recent earnings transcript if the company reported in the window

   For non-US issuers, equivalents (annual report, half-year report, ad-hoc announcements, director dealings).

   For all issuers:
   - Web search for material news in the window (acquisitions, divestitures, regulatory actions, key personnel changes, major contract wins/losses, competitor moves that affect the thesis)
   - Sell-side estimate revisions if surfaceable via search (direction matters more than magnitude — three downgrades is a signal, one is noise)
   - Price action: any single-day move > 8% deserves to be understood, not just observed

   For Claude Code: parallelize this. One subagent per data source.

5. **Map events to kill switches.** This is the only step that matters. For every material event surfaced in step 4, ask: does this event move the needle on a kill switch named in `thesis.md`?

   - **Direct trigger:** the event maps cleanly to a kill switch ("management's pricing discipline collapsed" was a kill switch; the company just announced a 15% list-price cut). This is REVIEW.
   - **Partial trigger:** the event is in the neighborhood of a kill switch but doesn't fully meet it ("revenue concentration in top customer > 40%" was a kill switch; new disclosure puts it at 37% up from 31%). This is WATCH — flag but don't escalate yet.
   - **Adjacent noise:** the event is real but doesn't map to any written kill switch. Note it for context, do not escalate. If you find yourself wanting to escalate on something that isn't a kill switch, the right answer is to add a new kill switch to the thesis — not to override the discipline now.
   - **Framework-level red flag:** an event that triggers a generic red flag from the framework but is not in `thesis.md`. Treat as WATCH and recommend the user explicitly add (or reject) it as a kill switch.

6. **Produce the verdict.** Exactly one of:
   - **THESIS INTACT** — no kill switch triggered, no framework red flag triggered. Material events surfaced are either neutral or thesis-confirming.
   - **WATCH** — at least one partial trigger or framework-level red flag. Not yet a REVIEW, but the next event in this direction probably is.
   - **REVIEW** — at least one direct kill-switch trigger. The thesis as written is in question. Recommend a full `company-deep-dive` refresh before any sizing change.

7. **Append a dated entry to `thesis.md` Update log.** Append only — never edit prior entries. Format:

   ```
   ### YYYY-MM-DD — thesis-check
   - Verdict: {THESIS INTACT / WATCH / REVIEW}
   - Lookback window: {date} → {date}
   - Material events surfaced:
     - {event 1} — maps to: {kill switch / framework red flag / noise}
     - {event 2} — maps to: ...
   - Kill switches triggered (direct): {list, or "none"}
   - Kill switches triggered (partial): {list, or "none"}
   - Framework red flags triggered: {list, or "none"}
   - Recommended next action: {none / monitor / re-deep-dive}
   ```

8. **Do not modify the thesis body.** Kill switches, bull case, bear case, conviction — these are the user's calls. If the recommendation is REVIEW, the user runs `company-deep-dive` and decides whether to rewrite. Never silently rewrite the thesis.

9. **Resolve the flag, if any.** If `journal/_flagged.md` exists and this ticker has an active flag with `next: thesis-check`, mark it resolved. Update the line to:

   ```
   - {TICKER}: flagged {flag-date}, resolved {today} ({verdict}) — was: {short reason}
   ```

   Do not delete the line — keeping resolved entries in place preserves the calibration trail (which flags led to which verdicts over time).

## Output

A single verdict block, in this exact shape:

```
{TICKER} — thesis-check
Lookback: {date} → {date}
Verdict: {THESIS INTACT / WATCH / REVIEW}

Material events:
  - {one-line summary of each event with date}

Kill switches triggered:
  - Direct: {list or "none"}
  - Partial: {list or "none"}
  - Framework-level: {list or "none"}

Next action: {none / monitor next earnings / run company-deep-dive}
Reasoning: {one to three sentences}
```

If invoked from `portfolio-review`, return the same block — the caller will aggregate.

## Notes

- The kill switches in `thesis.md` are the only authoritative source of truth. If something feels wrong but doesn't map to a written kill switch, the answer is to *write a new kill switch*, not to escalate. Suppressed signals you can't articulate are how generic deep dives get reborn.
- Be willing to return THESIS INTACT when nothing has actually broken, even if the stock is down 30%. Price action is not a kill switch. This skill exists partly to give you permission to ignore noise.
- Conversely, be willing to return REVIEW when a kill switch is clearly hit, even if the stock is up 30%. Asymmetric in both directions.
- Insider sales are often noise (tax, diversification, options vesting); insider *buys* are almost never noise. Weight accordingly.
- One downgrade is noise. Three downgrades clustered in two weeks is a signal — usually that the sell-side is catching up to something operational. Investigate the something.
- If you cannot find any material events in the lookback window, that itself is a finding. Note it explicitly ("no 8-Ks, no Form 4 activity, no material news, no analyst revisions") rather than producing a vague INTACT.
- This skill does not change positions. It produces a verdict. Acting on REVIEW means running `company-deep-dive` first, *then* deciding. Acting on WATCH means doing nothing until the next event lands.
- Apply the canonical stale-thesis rule in `docs/build-plan.md` (Shared rules). If the thesis is stale by that definition, recommend a `company-deep-dive` refresh in parallel with this check — a stale thesis is hard to check against.
