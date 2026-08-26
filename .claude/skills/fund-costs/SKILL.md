---
name: fund-costs
description: Price what a fund or a whole portfolio actually costs, from the PRIIPs KID rather than from a factsheet or a remembered figure. Resolves each holding by ISIN down a measured retrieval ladder (issuer KID by URL, a folder of downloaded KIDs, fondsweb), parses the full cost block including entry charges and performance fees, and reports a weighted household cost with explicit coverage - naming every ISIN it could not resolve instead of treating it as free. READ-AND-REPORT by default; it writes nothing unless the portfolio is the owner's own and he asks. Triggered by "what am I paying", "what's the TER", "price this portfolio", "how much are these funds costing", "what are the fees on X", "is this fund expensive", or a dropped set of KID PDFs or a broker holdings export.
---

# fund-costs

## When to use

Any question of the shape *what does this actually cost me*, about one fund or a whole book. Common phrasings:

- "What am I paying on this portfolio?"
- "What's the TER on [fund]?"
- "Price these for me" + a holdings export or a folder of KIDs
- "Is this fund expensive for what it does?"

**Why this gets its own skill:** cost is the only term in a fund's expected return that is close to certain. Everything else — return, volatility, whether a manager has skill — is a forecast with a wide interval, and on a fund under three years old is not answerable at all. The cost is knowable today, to two decimal places, from a document the manufacturer is legally required to publish. Treating it as a footnote inverts the confidence ordering.

Not this skill: judging whether the cost is *worth it* (`fund-deep-dive`), comparing funds against a benchmark (`compare-funds`), or anything about the exposure. This one answers *how much*, not *whether*.

## Inputs

- **ISINs.** Not fund names. Per "Funds tier (canonical)", identity is the ISIN — and the reason is arithmetic, not pedantry: **ongoing costs vary more between share classes of one fund than between funds.** Measured on one real portfolio, same day: Invesco Sustainable Allocation A 1.30% / C 0.90% / Z 0.80% / S 0.71%; Allianz Global FRN Plus AT 0.61% / IT 0.32% / P2 0.28% / WT 0.24%. A figure taken from a sibling class is a wrong number wearing a right one's clothes. If given names or broker abbreviations, resolve them and **show the resolution before running anything**.
- **Position values**, if a portfolio-level answer is wanted. Without them there is no weighted average, only a list.
- **Optionally a folder of KID PDFs** the owner has already downloaded — the highest-provenance rung, and the fallback for funds no public source carries.

## Process

1. **Resolve every holding to an ISIN and show the mapping.** Broker labels are abbreviations (`CORE FAM PARK E EU A`, `INV P EU H INC FAM A`) and several expand to funds with near-identical names in different classes. State what each resolved to and let the owner correct it before any number is quoted.

2. **Run the ladder.**

   ```
   python scripts/kid-fetch.py {ISIN} [{ISIN} ...] --kid-dir {folder} --json costs.json
   ```

   The script's own docstring documents each rung and what it was measured at. In short: issuer KID by URL and local KID PDFs are **primary**; fondsweb is secondary but was exact on every fund it covered; anything unreached is reported **unresolved**, never zero.

3. **Route the unresolved by hand rather than dropping them.** Two rungs exist that a script cannot walk, and both are worth the minute they take:
   - **investing.com** carries the Italian-distributed funds fondsweb misses, and blocks scripted requests while answering an agent fetch. Try `it.investing.com/funds/{isin}` before giving up.
   - **fundsquare** serves real KID PDFs but needs a per-provider key in the URL, so it is a manual lookup.
   - Failing both, ask the owner to download the KID. It is two clicks in most banking portals, and it is primary evidence.

4. **Read what the cost block says beyond the headline.** The ongoing figure is not the whole cost and the script surfaces the rest:
   - **Entry charges** are quoted as a MAXIMUM ("fino a un massimo del 3,0%", "questa è la cifra massima"). Whether it was actually applied is in the owner's transaction history, not the KID. Say which you know.
   - **Performance fees** are a live term, not boilerplate. One fund in a recent real portfolio carried *up to 15% of returns* while its ongoing figure looked ordinary.
   - **Transaction costs** are inside the PRIIPs ongoing total and are an estimate that varies with turnover.

5. **Weight it, and state coverage as a number.** Report the weighted average, the euro figure per year, and **what fraction of the portfolio the figure actually covers**. Where holdings are unpriced, say how the blend moves across their plausible range — if the answer is robust to the gap, that is worth more than a falsely precise average. Per "No silent caps", an unpriced holding is named, never quietly excluded.

6. **Separate the parked money from the invested money.** A large cash or money-market sleeve drags the blended cost down and makes an expensive book look cheap. Report both: the blend, and the cost of the part that is actually invested. On a recent real portfolio the blend was 1.13% while the invested half cost 1.67%.

7. **Add the costs the funds do not contain.** Ongoing fund costs are only part of what leaves the account. Also state, where they apply: the advisory or platform fee (a separate monthly debit, not netted from NAV — and sometimes fully rebated, which only the transaction history shows), and statutory charges such as Italy's 0.20%/yr *imposta di bollo* on securities accounts.

## Output

A table — ISIN, ongoing, entry max, performance fee, source rung, value held, cost per year — then:

- **The weighted household cost**, in percent and in euros per year, with coverage stated.
- **The unresolved list**, named.
- **Anything the ongoing figure hides**: performance fees, entry maxima, a parking sleeve flattering the blend.
- **The comparison that makes it mean something**: the cost against the portfolio's own gross yield where it is bond-heavy, or against a cheap index alternative for the same exposure.

Read-and-report. This skill writes no vault document. If the portfolio is the owner's own and he asks for it filed, that routes to `fund-deep-dive` for a real position, or to a note he owns. **A portfolio belonging to someone else is quarantined and goes nowhere near the vault's own tiers** — one gitignored folder per subject, never committed, never cited from a vault document, personal identifiers stripped on the way in. The lint enforces all three. The quarantine directory carries its own README stating the contract; this skill deliberately does not link to it, because a committed path pointing at gitignored material both dangles on every other clone and publishes a subject's name to the remote.

## Notes

- **A missing figure is not a zero.** The single most damaging output this skill could produce is a clean-looking average computed over the funds that happened to resolve. The script refuses to do it; do not do it in prose either.
- **The KID beats the factsheet, and both beat memory.** The KID is the regulated document with a defined cost methodology. A factsheet's "TER" may exclude transaction costs and will not mention performance fees.
- **A thin PDF extraction means the extractor failed**, not that the fund has no costs. Inherited from `pdf-extract.py`, which exists because that mistake was nearly written into an entry once.
- **Costs are certain; conclusions from them are not.** A high fee is a strong argument, not a verdict — an expensive fund can still be the right holding. That judgement belongs to `fund-deep-dive`, and this skill hands it the number rather than the answer.
