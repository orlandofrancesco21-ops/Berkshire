---
name: sector-primer
description: Produce a structured sector primer document for a chosen sector. Reads the relevant industry framework from frameworks/ to ground the analysis, then surveys the value chain, key drivers, and most important players. Output is primer.md plus value-chain.md, kpis.md, and players.md in sectors/{sector}/. Use when starting fresh research on a sector before evaluating any specific company. Triggered by "sector-primer X", "let's do a primer on X", or "I want to research X sector".
---

# sector-primer

## When to use

The user wants to start a deep dive on a specific sector. The framework for the relevant industry already exists in `frameworks/`, OR they've just run `framework-bootstrap`. Common phrasings:

- "Let's do a sector primer on [sector]"
- "I want to research [sector] — full primer"
- "sector-primer [sector]"

## Inputs

- Sector name (more specific than industry — e.g. "European listed asset managers" not just "financials"; "offshore drillers" not just "energy")
- Optional: geographic focus, market cap range, particular subsector lens

## Process

1. **Identify the parent industry framework.** Check `frameworks/` for the relevant file. If none exists, stop and suggest `framework-bootstrap` first. The primer is meaningless without the framework lens.

2. **Create the sector folder.** `sectors/{sector-slug}/` if it doesn't exist. Slugify the name.

3. **Research breadth-first, then depth.** A serious primer should pull from at least 15-20 sources:
   - Recent industry reports (sell-side, consultancies, trade pubs)
   - Q&A sections of earnings transcripts for the top 5 players
   - Peer 10-Ks (especially the risk factors section)
   - News flow over the last 12 months
   - Regulatory filings if the sector is regulation-heavy
   - Long-form buy-side commentary if available
   - For Claude Code: spawn parallel subagents — one per top player to pull filings, one for industry reports, one for news. Don't serialize this.

4. **Write the four core files:**

   **`sectors/{sector}/primer.md`** — main document.
   - TL;DR (3-5 sentences with the sector thesis)
   - Industry structure (referencing the framework, not duplicating it)
   - What's changed in last 5 years
   - What's likely to change in next 5 years (with falsifiable signals)
   - Where economic profit pools sit
   - Key cycle indicators with current readings
   - Open questions

   **`sectors/{sector}/value-chain.md`**
   - Value chain map (stages, brief economics)
   - Who captures economics at each stage (revenue share vs profit share)
   - Moats by stage
   - Disintermediation risks
   - Vertical integration trends and whether they create or destroy value

   **`sectors/{sector}/kpis.md`** — pulled from the framework but tailored.
   - Operating KPIs with concrete top-quartile/median/bottom-quartile numbers from real companies in the space
   - Financial KPIs same format
   - Current valuation multiples vs 5y average and 10y range
   - Honest read on whether current numbers look mid-cycle / peak / trough

   **`sectors/{sector}/players.md`**
   - Tier 1: 5-7 must-understand names with positioning
   - Tier 2: worth tracking
   - Tier 3: niche but interesting
   - Recently public / pre-IPO worth watching

5. **Cross-reference between the files** where it helps the reader.

6. **Update the parent framework** if research surfaces something missing. Add a dated entry to the "What I've learned over time" section of `frameworks/{industry}.md`.

## Output

Four files written, plus a verbal summary:

- The 3 most important things you learned about the sector
- The 5-7 names worth doing a `company-deep-dive` on first, ranked
- 1-2 things you flagged but weren't fully confident about — for the user to pressure-test

## Notes

- A great primer makes the next 5 company analyses 3× faster. Don't rush. This is the highest-leverage phase.
- If the user already invests in this sector, ask upfront what their existing thesis is — incorporate it or challenge it explicitly.
- The TL;DR should be a thesis statement, not a description. "Cycle is mid-recovery, lowest-cost operators win, consensus underestimates X" beats "this is a sector that has cycles".
