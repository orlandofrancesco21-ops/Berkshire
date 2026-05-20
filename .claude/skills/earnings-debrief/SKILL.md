---
name: earnings-debrief
description: After a portfolio holding reports, read the press release and transcript (prepared + Q&A), compare reality to the earnings-prep one-pager produced beforehand, and append a structured debrief to the thesis log. For each kill switch and each bull/bear case point, mark CONFIRMED / REFUTED / NEUTRAL with the specific evidence. The output is the input to thesis-check — if anything material flipped, this skill recommends running thesis-check (or company-deep-dive in extreme cases). Use within 48h of every print. Triggered by "earnings-debrief X", "X just reported — debrief", "run the post-earnings on X".
---

# earnings-debrief

## When to use

Within 48 hours of every print for every position. Common phrasings:

- "Earnings-debrief [TICKER]"
- "[TICKER] just reported — debrief"
- "Run the post-earnings on [TICKER]"

48h is a deliberate window. Within 24h you're still emotional about the price reaction; after 72h you've already integrated the news and the debrief becomes hindsight narrative. The middle is the calibration zone.

## Inputs

- Ticker
- Optional: explicit transcript URL or paste (default: pull via web search)

## Process

1. **Locate the prep.** Read `sectors/{sector}/companies/{TICKER}/thesis.md`. Find the most recent `earnings-prep` entry. If none exists, flag this — you reported on a name without prep — and produce the debrief anyway but note the gap loudly.

2. **Pull the print materials.**
   - Press release (revenue, margins, EPS, KPIs, guidance changes)
   - Full transcript — *both* prepared remarks AND Q&A. The Q&A is where signal lives; do not skip it.
   - 8-K (or equivalent) filed alongside the print — sometimes contains material disclosures not in the press release
   - Price reaction (intraday and the 1-3 day move). Note it; do not weight it heavily.

3. **Grade each kill switch.** For every kill-switch observable written in the prep:
   - **TRIGGERED** — the observable fired. Cite the specific transcript line or KPI.
   - **PARTIAL** — the observable moved toward the kill switch but didn't fully fire.
   - **NEUTRAL** — no movement.
   - **REVERSED** — the observable moved *away* from the kill switch (anti-trigger).

4. **Grade each bull/bear case point.** For every "confirms if / refutes if" pair:
   - **CONFIRMED** — confirmation criterion met.
   - **REFUTED** — refutation criterion met.
   - **NEUTRAL** — neither met clearly.
   - **MIXED** — partial confirmation on some dimensions, partial refutation on others. Spell out which.

5. **Check the Q&A questions.** For each of the 3 questions written in the prep:
   - Did an analyst ask it? (If not, why not — was it answered in prepared remarks instead?)
   - What did management answer? Note the answer verbatim or near-verbatim.
   - Was the answer evasive, direct, or different from prior calls?

6. **Check guidance vs. the prep's prediction.** Did the company:
   - Maintain prior guidance?
   - Raise / lower?
   - Withdraw?
   - Stay silent on a number they typically give?

   Compare to the pattern flagged in the prep (sandbagger / overpromiser / honest).

7. **Identify anything material that wasn't in the prep.** This is the hardest part — what did the print surface that you didn't anticipate? New disclosure, surprise capital allocation move, regulatory development mentioned, customer concentration shift, etc. Write these down without judgement; they may trigger a kill switch you hadn't written.

8. **Verdict.** Pick exactly one:
   - **THESIS INTACT** — no kill switch triggered, bull/bear net neutral or confirming, no material unanticipated disclosure.
   - **MONITOR** — partial triggers, mixed grades, or one unanticipated disclosure worth tracking. No immediate action; revisit at next print or news event.
   - **RUN THESIS-CHECK** — at least one direct trigger or one material unanticipated disclosure that maps to a framework red flag. Run `thesis-check` before any sizing decision.
   - **RUN COMPANY-DEEP-DIVE** — multiple triggers, or the print revealed the thesis is structurally different from what was written. The thesis needs to be re-written, not just re-checked.

9. **Append the debrief to `thesis.md` Update log.** Format:

   ```
   ### YYYY-MM-DD — earnings-debrief (print date YYYY-MM-DD)

   Headline: {one-line — beat/miss/inline + the most important non-obvious data point}

   Kill switch grades:
   - {switch}: {TRIGGERED / PARTIAL / NEUTRAL / REVERSED} — {evidence}
   - {switch}: ...

   Bull case grades:
   - {point}: {CONFIRMED / REFUTED / NEUTRAL / MIXED} — {evidence}

   Bear case grades:
   - {point}: {CONFIRMED / REFUTED / NEUTRAL / MIXED} — {evidence}

   Q&A check:
   1. {question} — {asked? / answered with: ...}
   2. ...

   Guidance:
   - Action: {maintained / raised / lowered / withdrawn / silent}
   - Vs prior pattern: {consistent / inconsistent with sandbagger/overpromiser/honest baseline}

   Unanticipated disclosures:
   - {item}: {framework red flag? / new candidate kill switch? / noise?}

   Price reaction (24h): {±X%} — noted, not weighted.

   Verdict: {THESIS INTACT / MONITOR / RUN THESIS-CHECK / RUN COMPANY-DEEP-DIVE}
   Recommended next action: {none / monitor / thesis-check / deep-dive refresh}
   ```

10. **Do not modify the thesis body.** Even if the print clearly broke the thesis, this skill only grades and recommends. The actual re-write happens in `company-deep-dive`.

## Output

The verdict block, restated to the chat so it lands before the conversation closes:

```
{TICKER} earnings debrief — {date}
Verdict: {THESIS INTACT / MONITOR / RUN THESIS-CHECK / RUN COMPANY-DEEP-DIVE}
Key takeaway: {one sentence}
Next action: {none / monitor / thesis-check / deep-dive refresh}
```

## Notes

- The prep is the contract. If "bear case refutes if X" is in the prep and the print delivers X, the bear case is REFUTED — even if your gut wants to find a reason to keep worrying. Trust the pre-commitment. If the criterion was wrong, fix it before the next print, not now.
- Q&A is where signal lives. If management dodged a key question, that itself is a data point — usually a partial trigger on whatever the question was about.
- Price reactions are noted but not weighted. A name that beats and drops is not automatically a refute; a name that misses and rallies is not automatically a confirm. The market's near-term read is sometimes useful, often noise.
- Unanticipated disclosures are the place where new kill switches get born. If the print revealed something you didn't think to watch for, ask: should this be a kill switch going forward? If yes, the user adds it to thesis.md manually — this skill does not silently rewrite the kill-switch list.
- "RUN COMPANY-DEEP-DIVE" should be rare — once every 1-2 years per name at most. Use it only when the print revealed the business is structurally different (a major segment divestment, a CEO change with strategy reset, a fundamental customer-mix shift). Don't escalate to deep-dive for ordinary quarterly variance.
- If you find yourself producing THESIS INTACT verdicts on a name through 4 consecutive prints while the stock has fallen 40%, the framework or the thesis is probably wrong — even though the discipline says hold. Run `company-deep-dive` voluntarily and see if a written-fresh thesis still believes the bull case. Discipline isn't stubbornness.
- Pair earnings-prep + earnings-debrief or run neither. Running prep without debrief wastes the prep. Running debrief without prep is just storytelling.
