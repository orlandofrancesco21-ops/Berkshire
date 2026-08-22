---
name: thesis-check
description: For a held position (or watchlist name with an existing thesis), pull every material event since the last thesis update and ask one question — does anything trigger a kill switch written in thesis.md? Reads thesis.md and the relevant industry framework, resolving the position through both tiers — sectors/{sector}/companies/{TICKER}/ and funds/{TICKER}/. For a fund it reads the vehicle and exposure lenses instead, and tests the exposure-level and vehicle-level kill switches separately, because a vehicle break is a fund switch rather than an exit. Output is "thesis intact" or "REVIEW: signal X potentially triggers kill switch Y" with a dated entry appended to the thesis update log. Use when a position has dropped or rallied sharply, when portfolio-review flags a name, or as a standalone gut-check before adding/trimming. For post-earnings analysis use earnings-debrief instead — running both on the same print creates duplicate thesis-log entries. Triggered by "thesis-check X", "is the X thesis still intact".
---

# thesis-check

## When to use

Either invoked directly on a single name, or by `portfolio-review` across all positions. Common phrasings:

- "Thesis-check [TICKER]"
- "Is the [TICKER] thesis still intact?"
- "Something feels off on [TICKER], check the thesis"

**Not for post-earnings analysis.** "[TICKER] just reported" routes to `earnings-debrief`, which grades the print against the pre-committed `earnings-prep` criteria and can itself recommend a thesis-check afterward. Running both directly on the same print creates duplicate thesis-log entries.

This is the skill that separates noise from signal. The whole point is to stress-test the specific, falsifiable kill switches written in `thesis.md` — not to re-do the original analysis. If you find yourself re-arguing the bull case, you're doing the wrong skill. Run `company-deep-dive` instead.

## Inputs

- Ticker (with exchange suffix where applicable — `ASML.AS`, `RIO.L`, `MSFT`)
- Optional: a specific event to investigate (e.g. "thesis-check ASML.AS focused on the latest earnings")

## Process

1. **Locate the position's files.** Two tiers hold positions, so try both, in this order — the same lookup the lint's own `position_doc()` performs: `sectors/{sector}/companies/{TICKER}/`, then `funds/{TICKER}/`. Either way you want `thesis.md` and `valuation.md`. If neither tier has a `thesis.md`, stop — there's no thesis to check. Suggest `company-deep-dive` first, or `fund-deep-dive` if the ticker is a pooled vehicle.

   A hit in `funds/` puts this run on the **fund branch**, which is flagged at each step below. It changes which lenses you read (step 2), which events count (step 4), and how many verdicts come out (step 6) — but not what this skill is for: the kill switches as written are still the only authoritative triggers.

2. **Read the kill switches.** Open `thesis.md` and extract:
   - The "What would change my mind" section (bull-case kill switches AND bear-case kill switches)
   - The most recent dated entry in the Update log — this is the "since when" boundary
   - The Conviction level (a check on a 5-conviction name should be more rigorous than on a 2)

   Also read `frameworks/{industry}.md` "Red flags specific to this industry" — these are kill switches the user may not have explicitly written into the thesis but the framework says to watch for. Treat them as additional candidate triggers.

   **Fund branch.** The thesis's "What would change my mind" is already split into **Exposure-level** and **Vehicle-level** switches; keep them split from here on, and record which side each candidate trigger belongs to. There is no industry framework: read both lenses instead — `frameworks/etf-vehicle-mechanics.md` for the wrapper and `frameworks/{exposure-slug}.md` for the asset class (the thesis names the slug). Each has its own red flags, and which lens a red flag came from decides which of the two verdicts in step 6 it feeds. Conviction is likewise two statements rather than one number; weight the check against whichever of the two it belongs to.

   Also read the thesis's own `## Principles check` section, if present — any principle marked TENSION or VIOLATES at write-time is a standing watch item. If an event in this window bears on one, classify it exactly like a framework-level red flag: **WATCH**, and recommend the owner add (or explicitly reject) a written kill switch. Never REVIEW, never a trigger — "Principle authority (canonical)" in `docs/build-plan.md` (Shared rules) makes principles advisory everywhere, and the Notes below hold that the kill switches in `thesis.md` are the only authoritative source of truth; a principle-derived signal that could escalate would invert both. This section lives inside `thesis.md`, so it costs no extra read. Finding that no stored principle bears on the window is a normal result, not a gap to fill.

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

   **Fund branch — a fund files none of the above, and looking for 8-Ks on an ETF returns a clean sweep that means nothing.** The events that exist here are:
   - **Vehicle-level:** the annual report if one landed in the window (the fund's print, per `fund-deep-dive` step 0), a TER or fee-cap change, realized tracking difference drifting from what the thesis assumed, AUM or share-class size moving toward a closure threshold, a share-class merger or closure notice, a change of index or a methodology review by the sponsor, a replication-method or securities-lending policy change, a domicile or tax-treatment change, a provider merger.
   - **Exposure-level:** what the exposure framework says actually drives this asset class — the anchor it names and where that anchor now sits, and any structural change it lists as a regime risk. Not the fund's quote, and not a drawdown: the exposure frameworks name drawdown depth as deliberately *not* a switch.
   - Provider disclosures are the source for the vehicle side, and PROD-P3's rule holds — a switch keyed to something nobody publishes cannot fire.

   For Claude Code: parallelize this. One subagent per data source.

5. **Map events to kill switches.** This is the only step that matters. For every material event surfaced in step 4, ask: does this event move the needle on a kill switch named in `thesis.md`?

   - **Direct trigger:** the event maps cleanly to a kill switch ("management's pricing discipline collapsed" was a kill switch; the company just announced a 15% list-price cut). This is REVIEW.
   - **Partial trigger:** the event is in the neighborhood of a kill switch but doesn't fully meet it ("revenue concentration in top customer > 40%" was a kill switch; new disclosure puts it at 37% up from 31%). This is WATCH — flag but don't escalate yet.
   - **Adjacent noise:** the event is real but doesn't map to any written kill switch. Note it for context, do not escalate. If you find yourself wanting to escalate on something that isn't a kill switch, the right answer is to add a new kill switch to the thesis — not to override the discipline now.
   - **Framework-level red flag:** an event that triggers a generic red flag from the framework but is not in `thesis.md`. Treat as WATCH and recommend the user explicitly add (or reject) it as a kill switch.

   **Fund branch: map to the right side, and never let one side borrow the other's evidence.** Every mapped event carries a side — exposure or vehicle — taken from the switch it hit, not from how serious it feels. A widened tracking difference is vehicle even if the exposure is also down; a change in what drives the asset class is exposure even if this wrapper tracks it perfectly. The one genuinely cross-cutting case is a *forced* closure or merger of the share class: it is vehicle-level and it is a taxable event, so it maps to a switch and to a cost, not to a view about the asset class.

6. **Produce the verdict.** Exactly one of:
   - **THESIS INTACT** — no kill switch triggered, no framework red flag triggered. Material events surfaced are either neutral or thesis-confirming.
   - **WATCH** — at least one partial trigger or framework-level red flag. Not yet a REVIEW, but the next event in this direction probably is.
   - **REVIEW** — at least one direct kill-switch trigger. The thesis as written is in question. Recommend a full `company-deep-dive` refresh before any sizing change.

   **Fund branch — two verdicts, in two sentences, never blended into one.** Return an **exposure verdict** and a **vehicle verdict**, each using the same three tokens. Per "Funds tier (canonical)" the two lenses fail independently and imply different actions: an exposure REVIEW puts holding the asset class at all in question; a vehicle REVIEW says *this wrapper* is broken while the exposure may be fine, and its action is a **fund switch** — `fund-deep-dive` on the exposure to name the substitute — not an exit. The headline verdict is the worse of the two, and it always says which lens fired. The moment they blend, a fixable cost problem starts arguing about macro, and a wrapper that should have been swapped instead becomes a debate about whether to own the asset at all.

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
   - Principle tensions touched: {list, or "none"}
   - Recommended next action: {none / monitor / re-deep-dive}
   ```

   On the fund branch, same heading token, with the two lenses kept apart:

   ```
   ### YYYY-MM-DD — thesis-check
   - Exposure verdict: {THESIS INTACT / WATCH / REVIEW}
   - Vehicle verdict: {THESIS INTACT / WATCH / REVIEW}
   - Lookback window: {date} → {date}
   - Material events surfaced:
     - {event 1} — side: {exposure / vehicle} — maps to: {kill switch / framework red flag / noise}
   - Exposure kill switches triggered (direct / partial): {list, or "none"}
   - Vehicle kill switches triggered (direct / partial): {list, or "none"}
   - Framework red flags triggered: {list with the lens each came from, or "none"}
   - Principle tensions touched: {list, or "none"}
   - Recommended next action: {none / monitor / fund-deep-dive refresh / fund switch — name the substitute question}
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

For a fund, the same block with `Verdict:` replaced by two lines — `Exposure verdict:` and `Vehicle verdict:` — the kill-switch list split the same way, and a next action that distinguishes a refresh from a fund switch.

If invoked from `portfolio-review`, return the same block — the caller will aggregate. On the fund branch it takes the worse of the two verdicts into its matrix and carries the lens that fired into the reason column, so do not pre-collapse them here.

## Notes

- The kill switches in `thesis.md` are the only authoritative source of truth. If something feels wrong but doesn't map to a written kill switch, the answer is to *write a new kill switch*, not to escalate. Suppressed signals you can't articulate are how generic deep dives get reborn.
- Be willing to return THESIS INTACT when nothing has actually broken, even if the stock is down 30%. Price action is not a kill switch. This skill exists partly to give you permission to ignore noise.
- Conversely, be willing to return REVIEW when a kill switch is clearly hit, even if the stock is up 30%. Asymmetric in both directions.
- Insider sales are often noise (tax, diversification, options vesting); insider *buys* are almost never noise. Weight accordingly.
- One downgrade is noise. Three downgrades clustered in two weeks is a signal — usually that the sell-side is catching up to something operational. Investigate the something.
- If you cannot find any material events in the lookback window, that itself is a finding. Note it explicitly ("no 8-Ks, no Form 4 activity, no material news, no analyst revisions") rather than producing a vague INTACT.
- This skill does not change positions. It produces a verdict. Acting on REVIEW means running `company-deep-dive` first, *then* deciding. Acting on WATCH means doing nothing until the next event lands.
- Apply the canonical stale-thesis rule in `docs/build-plan.md` (Shared rules). If the thesis is stale by that definition, recommend a `company-deep-dive` refresh in parallel with this check — a stale thesis is hard to check against. On the fund branch the refresh skill is `fund-deep-dive`, and that rule's clause (b) reads against the fund's annual report rather than an earnings release; `fund-deep-dive` step 0 owns that mapping.
- A fund almost never returns a *symmetric* result. The vehicle side moves on disclosures that arrive on a schedule and can be checked mechanically; the exposure side moves on almost nothing between annual reports. So the common honest output here is INTACT / INTACT with a note that nothing was published in the window — and the second-most common is a vehicle WATCH on a drag that widened while the exposure did not move at all. If both sides move together every quarter, one of them is being read off the price.
