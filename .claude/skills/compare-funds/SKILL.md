---
name: compare-funds
description: Compare two or more funds (ETFs, index funds, active funds) against each other and against a deliberately chosen benchmark, and answer whether any of them is actually good — where "good" means faithful and cheap for a passive fund, and a residual distinguishable from luck for an active one. Runs on the common overlapping history via scripts/fund-metrics.py, reads the output against frameworks/fund-evaluation.md and the wrapper lens, separates the part of any gap explained by fees from the part attributed to a manager, and reports rather than files. READ-AND-REPORT by default: output is a comparison table plus a verdict in chat, and a file is written only when the comparison is the substance of an allocation decision. Triggered by "compare X and Y", "compare-funds X Y Z", "which of these funds is better", "is this fund actually good", "is this manager any good", "X or Y for the {exposure} sleeve", "does this active fund beat its benchmark", or "should I switch from X to Y".
---

# compare-funds

## When to use

The owner is holding two or more funds side by side and wants to know which one to own, or whether a single fund is worth its fee at all. Common phrasings:

- "Compare [fund A] and [fund B]"
- "Is [active fund] actually good, or is it just the index?"
- "Which of these three should I hold for the [exposure] sleeve?"
- "Should I switch from [fund A] to [fund B]?"
- "This fund is up 14% a year — is that skill?"

Not this skill: a full allocation case on one fund (`fund-deep-dive`, which owns `thesis.md`, `valuation.md` and `ic-sheet.md`), ranking companies inside a sector (`compare-within-sector`), or deciding *what exposure to own* — that question is settled before this one, and step 1 will hand it back if it has not been.

The precondition is weaker than `fund-deep-dive`'s deliberately: this skill runs on candidates that do not yet have vault documents, because the most useful comparison is often the one that decides which fund is worth deep-diving. What it does **not** do is let a comparison stand in for that dive.

## Inputs

- **Two or more funds, by ISIN** — or enough to resolve one. A bare ticker is an ambiguity, not an input, per "Funds tier (canonical)": the same fund lists on several exchanges under different tickers, and the distributing and accumulating classes are different objects. If the owner gave tickers, resolve them and say what you resolved them to before running anything.
- **The question being asked**, in one of three shapes, because they need different benchmarks: *which of these do I own* (fund selection), *is this manager earning the fee* (active assessment), or *should I switch out of what I hold* (replacement). If it is a replacement, name the incumbent — a comparison with no named alternative is a rating, not a decision.
- **The intended holding period.** Cost differences compound over it and a track record is judged against it. A three-year answer and a twenty-year answer differ on the same funds.
- **A benchmark, if the owner has one in mind** — recorded as an input, then tested in step 3 rather than accepted. His benchmark and the analytically right one are separate objects and both get written down.

## Process

1. **Establish that the funds are comparable at all — before any data is pulled.** This step decides whether the rest of the process is even measuring what the owner thinks it is.

   - **Identity, per "Funds tier (canonical)":** ISIN, share class (accumulating or distributing), listing and trading currency, the fund's own base currency, and hedged or unhedged. Two share classes of the same fund are a tax and cash-flow question, not a manager question, and this skill says so and stops rather than manufacturing a performance argument between them.
   - **Exposure.** Resolve each fund to an exposure slug through the registry in `frameworks/README.md`, matching on **the index it actually tracks** (or, for an active fund, on the mandate in the prospectus and what the holdings file shows it actually owns — where the two disagree, the holdings win per "Evidence weighting (canonical)").
   - **If the funds track different indices, this is not a fund comparison.** It is an exposure decision wearing a fund-selection costume, and the fee comparison it produces will be answering a question nobody asked. Say so plainly, and **split the question in two**: which exposure, settled first through `fund-deep-dive` on the exposure lens (or `framework-bootstrap` if the slug has no framework); then which vehicle inside the winning exposure, which is this skill. Report the split as the finding. It is a complete and frequent output of step 1, and running the metrics anyway produces a number that looks like an answer.
   - **Active against passive is a legitimate comparison and a specific one.** The tracker is the null hypothesis, not a peer: the question is whether the active fund's fee bought something the tracker could not deliver, and that framing carries through to step 6.
   - **Currency.** Every series must be measured in one currency, stated. Comparing a EUR-listed line against a USD-listed one measures the euro, not the manager.

2. **Load the lenses, before touching the data.** Three files, in this order:
   - `frameworks/etf-vehicle-mechanics.md` — the universal wrapper lens. It owns cost, replication, domicile and withholding, closure risk, liquidity, index methodology and securities lending, and it is what makes a *passive* verdict possible at all: for a passive fund, good means faithful and cheap, and that verdict is already fully specified there.
   - `frameworks/fund-evaluation.md` — the statistical lens on active management: benchmark selection, the decomposition into beta, factor exposures, costs and residual, and the significance thresholds this skill quotes rather than restates. If it is being written concurrently, per "Concurrent orchestration (canonical)" re-check rather than stopping at the first miss, read it **fresh** when it lands, and say in the report that the lens arrived mid-run.
   - `frameworks/{exposure-slug}.md` — the asset-class lens, for what drives returns in this exposure and what a normal outcome distribution looks like in it. The umbrella rule carries over unchanged: a framework marked `**Umbrella framework:** yes` is triage-only, and a comparison run against an umbrella alone is triage, and says so.

   **The one case where the exposure lens is not required:** when every fund in the comparison tracks the *same index in the same variant*, the exposure cancels out of the ranking and the comparison is a pure wrapper question that the vehicle lens answers alone. Say explicitly that the run is scoped to the wrapper, and say what it therefore cannot tell him — nothing here argues that the exposure is worth owning. That is the only exemption, and it does not extend to two funds tracking merely *similar* indices, where the small-cap or country-classification delta is exactly what the comparison would otherwise attribute to the manager.

   Do not apply a remembered fund-comparison checklist. These three files exist to replace it, and the ratios in step 5 mean different things in different asset classes.

3. **Choose the benchmark deliberately, and write down why — before the metrics run.** Per the benchmark section of `frameworks/fund-evaluation.md`, which owns the selection rules. What this step owns is the discipline around them:

   - **Two benchmarks get recorded, separately.** (a) The fund's **own prospectus benchmark** — what it is contractually measured against, what its factsheet quotes, and what its fee is justified by. (b) The **analytically right** one — the cheapest investable combination that reproduces the exposure the fund actually runs, from the holdings file rather than the name.
   - **Where those two differ, that difference is frequently the entire finding.** A fund benchmarked against a broad index while running a small-cap or value or single-country book will show alpha that is factor exposure with a fee attached, and a fund benchmarked against a peer-group average is being measured against a survivor set (see Notes). Name which is happening.
   - **The benchmark must be investable, in the comparison currency, and in the correct return variant.** Net or gross total return, never a price index: comparing an accumulating NAV to a price index manufactures alpha roughly equal to the dividend yield, and this vault has the same warning written into `fund-deep-dive` step 4 for the same reason.
   - **Benchmark choice is committed before the output is read.** Choosing it afterwards, or trying a second one because the first was unflattering, is picking the answer. If a second benchmark genuinely belongs in the analysis — an active fund with a mandate that spans two exposures is the real case — declare both up front and report both results, including the one that disagrees.

4. **Align the periods, and state the window in the same breath as every number derived from it.** Every figure in this comparison runs on the **common overlapping history** of all the funds and the benchmark. `scripts/fund-metrics.py` aligns to that period and says so in its output; quote that line rather than restating it from intent.

   - State the window as dates **and** as length in years **and** as the observation count. All three, because the third is what step 5's significance test actually consumes.
   - **Where one fund is younger than the others, say what that costs.** The comparison inherits the shortest history, so the whole run is judged on that fund's window: a three-year common window may contain no drawdown at all, in which case a manager whose entire claim is downside protection cannot be evaluated in it, and the up/down capture numbers are describing one regime. Write that as a limitation on the verdict, not as a caveat under it.
   - **Do not repair a short window.** Not by splicing a predecessor share class, not by chaining a merged fund's history, and never by extending with the index's backtest — backtested history has no spread, no cash drag, no withholding and no redemptions, and it was selected in part because it looked good. A short record is a fact about the evidence, and the honest response is a weaker verdict.
   - Comparing a three-year fund's trailing return against a fifteen-year fund's is the most common silent error in fund comparison, and it is silent precisely because both numbers are correctly computed.

5. **Run `scripts/fund-metrics.py` and read the output against `frameworks/fund-evaluation.md`.**

   ```
   python scripts/fund-metrics.py {TICKER} {TICKER2} [...] --benchmark {BENCHMARK} --rf {rate} --years {N}
   ```

   - **State the risk-free rate with its source and date.** It is an input to Sharpe, to Sortino and to the CAPM regression, and changing it changes the ranking. An undated rate is an anchor that outlives the conditions that produced it (PROD-P5), and every figure carried into the report is stamped per "Price and data sourcing (canonical)" and labelled per "Verification labels (canonical)".
   - **Every alpha reported carries its t-statistic, its R-squared and its observation count. An alpha without all three does not get quoted** — not in the table, not in the verdict, not in passing in the chat summary. The thresholds for calling a residual distinguishable from luck belong to `frameworks/fund-evaluation.md`; cite them, do not re-derive them here.
   - **Read R-squared first, before alpha.** A low R-squared means the benchmark does not explain what this fund does, so the alpha computed against it is not a measurement of skill — it is a measurement of the wrong comparison. That routes back to step 3, and the run should say so rather than reporting the alpha with a hedge attached.
   - **Read the risk numbers as an owner, not as a scorecard.** Max drawdown and, more importantly, **time to recovery** decide whether a position can be held through the bad case; tracking error and information ratio say whether a fund is doing what it claims; up/down capture says where the return was earned, and an asymmetric capture pattern that appears only in a window containing one direction is not a pattern.
   - Volatility, Sharpe and Sortino rank funds only against funds running the same exposure. Across exposures they rank asset classes, which is a different question and one this skill has already refused in step 1.

6. **Separate cost from skill — and do the cost half first.** This is the step that decides how much of any performance gap is even available to be attributed to a manager.

   - Take the **all-in annual drag** for each fund as a range, built term by term exactly as `fund-deep-dive` step 4 specifies — that step owns the term list and the sourcing rules, and a second copy of them here is a second version to drift from. Each term carries its own source, date and verification label; where a term genuinely cannot be established, widen the range and name the document that would close it, rather than narrowing it with an assumption.
   - **Compute the cost difference between the funds in basis points per year, and compound it over the owner's stated horizon.** Then state, in one sentence, how much of the observed performance gap the fee difference alone explains — before a word is written about the manager.
   - **The ordering is the discipline, not a formatting preference.** Cost differences are near-certain, known forward, and recur every year in every market. Alpha differences are measured backward and are usually not statistically distinguishable from zero. Reversing the order lets a gap that is arithmetic get narrated as judgment.
   - For an active fund the fee is charged against the benchmark's return whether or not the manager beats it, so the hurdle is the fee and the hurdle recurs. A residual that is positive but smaller than the fee is a fund that earned money for its manager.
   - Where a fund's R-squared is high and its active share low, the fee is being charged for exposure the benchmark supplies. Say that in cost terms, since it is a cost finding, not a skill finding.

7. **Correlation and portfolio fit.** Read the script's correlation matrix — the funds against each other, against the benchmark, and against what `portfolio.md` already holds.

   - **Two funds correlated at 0.98 over the common window are one decision, not two**, and the choice between them collapses onto cost and tax. That is a result, and it is the most common one in a single exposure.
   - **Correlation is not a constant and it rises when it hurts.** The number that matters for an allocation is the one measured in the drawdown, not the full-sample one; if the common window from step 4 contains no drawdown, the diversification claim is untested and must be reported as untested rather than as low.
   - **Overlap is computed from the holdings files, not from names.** Two differently-named funds can be 70% the same securities. This is the same rule `fund-deep-dive` applies in its allocation logic, for the same reason.
   - State the role each candidate would play — core beta or satellite tilt — and what it displaces, per "Funds tier (canonical)". Target weights and rebalance bands are `portfolio.md`'s, and this skill does not set them.

8. **The verdict, in one of four registers.** Say which, say on what evidence, and say whether the evidence is strong enough to support the choice at all:

   - **PREFER {TICKER}** — one fund wins on evidence that survives step 5's significance test or on a cost gap large enough to decide it. State the margin and which of the two it rests on.
   - **INDISTINGUISHABLE — choose on cost.** The funds cannot be separated on the available record, so the decision is made on the terms that are knowable: all-in drag, tax treatment, and closure risk. This is a **first-class verdict and the most frequent one**, not a failure to conclude, and it is written as an answer rather than as an apology.
   - **NOT COMPARABLE — split the question**, from step 1. Different exposures, and the exposure question goes first.
   - **INSUFFICIENT RECORD.** The window is too short or too single-regime for any verdict, including the cost one, to be safe. Name what would close it, and since more history is a date, name the date.

   Where the verdict leads to sizing, sizing follows ASYM-P2's asymmetry basis exactly as everywhere else, with the qualification `fund-deep-dive` records: for a diversified fund the bear leg is a drawdown rather than a permanent loss, so the binding constraint is the drawdown depth and the time to recovery from step 5, written in as numbers.

   **What this skill may never do:** switch a holding on performance alone. ASYM-P1 holds on a fund as it holds on a company — a fund is exited or replaced when a written kill switch in its `thesis.md` fires, and a comparison is not a kill switch. A comparison that argues for replacing a held fund routes to a `fund-deep-dive` refresh on the incumbent and a fresh `fund-deep-dive` on the substitute; it does not decide.

9. **Decide whether anything is written, and where — the boundary is narrow on purpose.**

   **Default: nothing is written.** This is a read-and-report skill. The comparison table and the verdict go to the chat, and that is the whole output. A comparison run to decide what to research next leaves no file behind.

   **A file is written only when this comparison is the substance of an allocation decision** — it changed, or deliberately confirmed, what will actually be held. Then exactly one of:

   - **Append to the relevant fund's `funds/{TICKER}/thesis.md` Update log**, heading `### YYYY-MM-DD — fund comparison`, verbatim: what was compared, the window, the verdict, and the one or two figures it rests on. Append-only, per the non-negotiable and the lint that enforces it. **Never** use the headings `— initial thesis` or `— deep-dive refresh`: those two strings are what the lint keys the Principles-check and IC-sheet gates on, so borrowing one claims a deep dive that did not happen and switches on gates this run does not satisfy — the vault's signature failure shape, in its most tempting form.
   - **Or a dated note under `funds/{TICKER}/notes/`** when the comparison is long enough to be its own artifact. That folder is unlinted human working space: no skill reads it, nothing cites it, and it carries no log and no schema. It is **not** a new document tier and must never be referenced as though a later run could rely on it.

   **What this skill never writes:** a fund folder that did not exist, any body section of `thesis.md`, `valuation.md` or `ic-sheet.md` (`fund-deep-dive` only, per "Funds tier (canonical)" and "IC sheet (canonical)"), `portfolio.md` position rows (owner-only per "Tiered autowrite (canonical)"), or a `watchlist.md` row for a fund that has not been deep-dived. Any expected-return figure quoted from a fund's `valuation.md` is quoted, never revised: that file is canonical for it per VAL-P5, and a second live set of numbers is a bug.

   **Lens-level findings are reported, not filed.** If the comparison taught the vehicle or exposure framework something durable, name it in the report and hand it to the `fund-deep-dive` run that acts on the comparison, which owns that write-back. A read-and-report skill does not open an append-only framework log.

## Output

A comparison table and a verdict, written to the chat. The table has one row per fund and carries, at minimum:

- ISIN, share class, currency, hedged or not, and the index or mandate
- All-in annual drag, as a range, with the ongoing charge shown separately from it
- Annualised return and volatility over the common window, with the window restated in the header
- Sharpe, Sortino, max drawdown and time to recovery
- Tracking error and information ratio against the chosen benchmark
- CAPM alpha and beta, each with t-statistic, R-squared and observation count in the same cell as the figure
- Up and down capture
- Correlation to each other fund and to the relevant existing holding

Then, in prose:

- **The benchmark, and why it was chosen** — plus the fund's own prospectus benchmark where it differs, and what that difference does to the alpha
- **The window, its length, its observation count, and what the shortest history costs the comparison**
- **The cost half of the gap and the skill half**, in that order, with the fee difference compounded over the stated horizon
- **The correlation read**, including whether the diversification claim was testable in this window at all
- **The verdict** in one of step 8's four registers, and the observable that would change it
- **What is not known** — every term that could not be established, and the document that would close each one

## Notes

- **A fund's trailing return is the least useful number on its factsheet and the most prominent one.** Part of any strong trailing decade was multiple expansion that has already happened and is now the starting valuation; all else equal, that fund has a *worse* forward expected return, not a better one. Trailing performance enters this analysis as an input to tracking difference and as evidence about the vehicle. It is never evidence about the exposure, and it is never the verdict.
- **The wrong benchmark can manufacture alpha or destroy it outright, and it does so silently.** Benchmark choice is an analytical decision made before the numbers are seen, not an administrative field copied off a factsheet. A fund measured against an index it does not resemble produces a number that is arithmetically correct and analytically meaningless — and it is the single easiest way for this skill to produce a confident wrong answer.
- **Most track records are too short to distinguish skill from luck, and pretending otherwise is the failure mode of this entire exercise.** Ten years of monthly data is a small sample for a residual that size. So the honest output of many comparisons is "cannot tell — pick the cheaper one", and that sentence is a conclusion. Writing a hedged preference instead, because a verdict feels more useful than a null, converts noise into a decision the owner then has to live with.
- **The funds available to compare today are the ones that survived.** Poor funds are closed or merged into better ones and their records leave the databases with them, so any peer-relative conclusion — a quartile rank, a "beats the average fund" claim, a peer-group benchmark — is flattered by an amount nobody can quote for this specific comparison. Treat peer-relative evidence as weaker than benchmark-relative evidence, always, and never build a verdict on it alone.
- **A cheap fund tracking the right exposure beats a brilliant fund tracking the wrong one, over any horizon that matters.** The exposure question is therefore settled before the fund question, and step 1 hands it back rather than absorbing it. Two lenses, two verdicts, per "Funds tier (canonical)" — "right exposure, wrong vehicle" is a fund switch, and "wrong exposure, excellent vehicle" is a decision this skill must refuse to launder.
- **For a passive fund the entire question is faithfulness and cost, and it is already answered.** Do not import active machinery to dress it up: an alpha t-statistic on an index tracker is measuring tracking difference with extra steps, and the wrapper lens measures that directly and better.
- **Cost is the one number known forward.** Everything else in the table is a backward-looking estimate with an error bar; the ongoing charge and the spread are deducted whether the market rises or falls, and they are the same next year. That asymmetry is why step 6 runs cost first and why a comparison that ends on cost has ended on its firmest ground, not its weakest.
- **Correlation is a regime statistic pretending to be a constant.** Quoted full-sample, it is at its most reassuring exactly where it is least reliable; the pair that decorrelates in calm markets and converges in a crash has told you nothing you can size against. If the common window contains no crash, say the number is untested rather than low.
- **Where sizing follows, it follows ASYM-P2's asymmetry basis** — computed one way, off the canonical table in the fund's `valuation.md`, and stated. What a fund changes is which risk the ratio stands in for: the constraint becomes the drawdown distribution and time to recovery, so those go in as numbers and the position is sized to be one the owner can hold through and add into.
- **The comparison is not a document tier.** Its natural output is a paragraph in the chat and, at most, a dated line in a thesis that already exists. Every instinct to give it a home of its own — a compare file, a rankings table, a scorecard that gets refreshed — is an instinct to create a second set of live numbers alongside `valuation.md`, and this vault has one rule about two live sets of numbers.
