---
name: earnings-prep
description: 5-7 days before a portfolio holding reports, read thesis.md and valuation.md to produce a one-page earnings preview — what each kill switch would look like at this print, what each bull/bear case point needs to confirm or refute, where last quarter's guidance vs consensus sits, and the 3 questions to listen for in Q&A. The point is to walk into the call with prepared answers rather than reactive emotion. Reads thesis.md, valuation.md, and the relevant industry framework. Output is a one-pager appended to the thesis log under a draft heading. Use proactively before every print for every position. Triggered by "earnings-prep X", "X reports next week — prep me", "earnings-prep all".
---

# earnings-prep

## When to use

5-7 days before a portfolio holding reports. Common phrasings:

- "Earnings-prep [TICKER]"
- "[TICKER] reports next week — prep me"
- "Earnings-prep all — what's coming up?"
- "Run earnings-prep on everything reporting this month"

This is the skill that converts earnings from emotional events into instrumented ones. The discipline: decide *before* the print what you'd need to see to change your mind. After the print, you compare reality to the prepared template rather than to your post-hoc rationalization.

## Inputs

- Ticker (or `all` to scan upcoming earnings for the whole portfolio)
- Optional: explicit earnings date (default: pull from yfinance or company IR page)

## Process

1. **Locate upcoming earnings.** For a single name, pull the next earnings date. For `all`, scan every position in `portfolio.md` and identify any reporting within 14 days. Sort by date.

2. **Locate the company files.** Read `sectors/{sector}/companies/{TICKER}/thesis.md` and `valuation.md` in full. If they don't exist, stop — there's no thesis to prep against.

3. **Extract the kill switches.** Every entry in "What would change my mind" — bull AND bear. For each, write the specific observable that would trigger it at *this* print. Example:
   - Kill switch: "Pricing discipline breaks (list price cut > 5% in a quarter)"
   - Print observable: "Watch ASP/unit, pricing commentary in prepared remarks, and any list-price changes disclosed in 8-K filings during the quarter."

4. **Extract the bull/bear case points.** For each, identify what this print should confirm or refute. Frame as a binary if possible:
   - Bull case: "AI demand is structural, not cyclical"
   - This print confirms if: "Backlog grows sequentially AND management raises FY guidance AND no hyperscaler commentary about pull-ins"
   - This print refutes if: "Backlog falls sequentially OR FY guide cut OR explicit pull-in language from a top-3 customer"

5. **Pull last 4 quarters' guidance vs delivered.** From transcripts or yfinance. Surface:
   - Guidance issued at each prior print (revenue, margin, EPS, or industry-specific KPIs)
   - Actual delivered at the following print
   - Pattern: chronic sandbagger / chronic overpromiser / honest broker
   - This quarter's published guidance and current consensus

6. **Identify the Q&A questions.** The 3 questions you would ask if you were on the call, derived from the kill switches and bull/bear points. These are the questions analysts may or may not ask — write them down so you can check post-call whether they got asked and answered.

7. **Pull recent context.** In the 30 days before the print:
   - Any 8-K filings (or equivalents)
   - Material competitor news (peer earnings, peer pre-announcements)
   - Insider activity
   - Sell-side estimate revisions in the run-up — direction and magnitude

8. **Append the prep to `thesis.md` Update log.** Format:

   ```
   ### YYYY-MM-DD — earnings-prep (for print on YYYY-MM-DD)

   Kill switches — what to watch for:
   - {kill switch}: {specific print observable}
   - {kill switch}: {specific print observable}

   Bull case — confirms if / refutes if:
   - {point}: confirms if {X}, refutes if {Y}
   - {point}: confirms if {X}, refutes if {Y}

   Bear case — confirms if / refutes if:
   - {point}: confirms if {X}, refutes if {Y}

   Guidance track record (last 4Q):
   - {Q}: guided X, delivered Y ({beat/miss/inline})
   - Pattern: {sandbagger / overpromiser / honest}

   This quarter:
   - Company guidance: {published or none}
   - Consensus: {revenue / margin / EPS / KPI}
   - Estimate revisions in last 30d: {direction, magnitude}

   Questions to listen for in Q&A:
   1. {question}
   2. {question}
   3. {question}

   Recent context (last 30d):
   - {bullet, only if material}
   ```

9. **Do not predict the print.** This skill is not "guess the beat/miss." It's "decide what the result would mean *before* you see it." Saying "I expect a beat" is out of scope and corrupts the post-print analysis.

## Output

Confirmation of:
- Print date
- File updated: `sectors/{sector}/companies/{TICKER}/thesis.md`
- The questions-to-listen-for list, restated in the chat so they're top-of-mind

For `all` mode: a calendar table of upcoming prints + a confirmation per name. Run the full prep on each.

## Notes

- The point is pre-commitment. If you don't write "bear case refutes if X" before the print, you'll rationalize X after the print. The skill enforces the commitment.
- "Beat consensus by Y%" is not a thesis criterion. Frame everything in terms of kill switches and framework drivers, not Street estimates. Beats can come with refuted theses; misses can come with confirmed ones.
- A chronic sandbagger that "beats and raises" every quarter is conveying less signal than a chronic honest broker that exactly hits its number. Calibrate guidance reads to the pattern.
- If the 3 Q&A questions are easy to write, the thesis is probably well-formed. If you struggle to write 3, the thesis is vague — fix the thesis, not the prep.
- Earnings-prep is wasted effort on names where you wouldn't act on the result regardless. If you're holding a 5-conviction long-duration name through whatever the print says, just say so and skip the prep. Be honest about that — false rigour is worse than no rigour.
- After the print, `earnings-debrief` reads this prep and grades reality against it. The two skills are a pair — running prep without later debrief defeats the purpose.
