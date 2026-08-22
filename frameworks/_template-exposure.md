# {Exposure} — asset-class exposure framework

> Personal playbook for forming and defending an **expected-return range** for an asset-class exposure, and for judging an allocation to it against its alternatives.
> Append-only in the learned log. Refine every time a fund tracking this exposure is deep-dived, and every time a realized 10-year window closes on a range this file produced.

**Last updated:** YYYY-MM-DD
**Exposure class:** {equity | nominal government bonds | inflation-linked bonds | credit | listed real assets | commodities | cash}
**Decision unit:** allocation over a stated horizon, against named alternatives — **not** a buy/pass on a business
**Default horizon:** {the horizon at which this exposure's anchors have measurable predictive power — state it here and never quote an expected return without it}
**Umbrella framework:** no <!-- Same marker line, same literal string, as frameworks/_template.md — `fund-deep-dive` keys on it exactly as `company-deep-dive` does, so an exposure framework must carry it or the gate silently reads absence as "not umbrella". Set to "yes — triage only; sub-exposure framework required before any fund deep dive" for a genuinely umbrella asset class (e.g. "fixed income", where government bonds, credit and inflation-linked have different return drivers, different anchors and different predictability). The marker, NOT the presence of a Sub-exposure navigator, is what the skills read. -->

<!-- Optional — delete this section for a single coherent exposure. Use it when the framework spans asset classes whose return decomposition or anchor differs, either as a true umbrella (marker = yes) or as triage context in a decision-grade file.

## Sub-exposure navigator

| Sub-exposure | What it is | Return decomposition | Primary anchor | Horizon the anchor works at |
|---|---|---|---|---|
|  |  |  |  |  |
-->


<!--
SCHEMA NOTES — the parallel of frameworks/_template.md for an ASSET CLASS.

WHY THIS TEMPLATE EXISTS AT ALL. The industry template asks "what makes a great
business here" and "how do good operators allocate capital". Both questions are
meaningless for an exposure: there is no operator, no moat, no capital-allocation
decision to grade. An index has no management team to be wrong about. Everything
that makes the industry template useful — the sub-sector navigator, the KPI table,
the bull/bear archetypes — is about dispersion BETWEEN businesses, and an exposure
deliberately owns the dispersion rather than betting on it. Forcing an asset class
into the industry template produces a document that looks complete and answers
nothing.

THE ONE JOB. Every section below exists to serve exactly one question:
  *How do I form a defensible expected-return range for this exposure over a
   stated horizon, and what has that method's track record actually been?*
A section that does not feed the range or its error bars does not belong here.

WHAT THE LINT ENFORCES (scripts/check-cross-references.py, run from the repo root):
*  Append-only on "## What I've learned over time" — existing dated lines may
   never be removed or rewritten. Everything ABOVE that heading is meant to be
   rewritten as understanding improves; only the log is a historical record.
*  Every ID-shaped token resolves. Real principle IDs only (registered prefixes
   are listed in principles/README.md) — an invented one BLOCKS THE COMMIT. The
   placeholder form {PREFIX}-P{n} used in this template carries no digits and is
   therefore lint-invisible, which is why templates use it and real files do not.
*  Every markdown link and every backticked path must resolve on disk. Do not
   backtick a path to a file that does not exist yet; name it in plain prose
   instead until it does.

WHAT THE LINT CANNOT ENFORCE, AND THEREFORE MATTERS MOST:
-  Every figure carries source + date + a verification label — verified (the
   primary artifact was read) / partial (secondary, relay, or asset-manager
   marketing) / unverified (memory or unconfirmable). See "Verification labels
   (canonical)" in docs/build-plan.md. A remembered statistic dressed as a fact
   is the single worst thing that can enter this tier, because an exposure
   framework's whole output is a number.
-  "Could not establish" is a finished answer. An anchor with no sourced track
   record is written down AS an anchor with no sourced track record.
-  Every anchor's row states the horizon at which it WORKS and the horizon at
   which it does NOT. An anchor quoted without its failure horizon is a
   forecast pretending to be a fact.

VOICE. Same register as the industry frameworks: opinionated, specific, willing
to say "this is well-reasoned rather than proven". Encode the discipline into the
file so future-Francesco cannot quietly drop it under pressure.

RELATIONSHIP TO THE OTHER LENSES. A fund deep-dive reads TWO frameworks: this
one (the EXPOSURE lens — what the holdings are worth over the horizon) and
frameworks/etf-vehicle-mechanics.md (the universal VEHICLE lens: wrapper
mechanics, replication, domicile, tracking difference, securities lending, tax
wrapper). Neither substitutes for the other: the best fund tracking a bad
exposure is still a bad allocation, and a good exposure bought through a bad
wrapper leaks the premium it earned.

OWNERSHIP: written by framework-bootstrap; refined by a fund deep-dive's
write-back into the learned log. Nothing company-specific ever lands here, and
nothing fund-specific either — a wrapper's expense ratio belongs in that fund's
own documents, not in the exposure framework. See "Principles routing
(canonical)"; the test is whether the sentence survives with the TICKER and the
PROVIDER deleted.
-->

---

## Scope — what this exposure actually is

The gap between the label and the holdings, stated first, because everything downstream is arithmetic on the holdings and rhetoric on the label.

- **Index universe:** {the specific index or indices this framework covers — name them, do not say "the market"}
- **Selection rule:** {how a security gets in: domicile, size, liquidity, free float, classification}
- **Weighting:** {market cap / free-float cap / equal / fundamental — and what that mechanically implies about what the exposure buys more of as prices move}
- **Explicitly included:** {the things a reader would not expect to be in here}
- **Explicitly excluded:** {the things the label implies but the index does not hold — small caps, a whole country classified elsewhere, a whole asset type}
- **Rebalancing and reconstitution:** {cadence, and who decides}

### Label vs holdings

The concentration table. Fill it from the index provider's own current factsheet, dated, and re-pull it rather than trusting this copy — it drifts.

| What the label implies | What the index actually holds (as of {date}, {source}, {verified/partial}) |
|---|---|
| {e.g. "global"} | {e.g. "N% one country"} |
| {e.g. "diversified"} | {e.g. "top ten = N% of index weight"} |
| {e.g. "broad"} | {e.g. "N constituents, large and mid only"} |

**The one sentence that matters:** {state, in one sentence, the thing about this exposure that a reader who only knows the label would get wrong.}

## What drives long-run returns for this asset class

The return decomposition, written as an identity so every term is separately falsifiable and separately monitorable. This is the skeleton the fund's valuation file will fill in.

**Identity:** {e.g. real return = starting yield + real growth of the yielding quantity + change in valuation multiple − costs − tax. Write the version that is actually true for THIS asset class, and say plainly whether it is an accounting identity or an approximation.}

| Term | What it is | Historical contribution | Source, date, label | Can it repeat? |
|---|---|---|---|---|
| {term} | {definition} | {pp per year} | {source} | {yes / bounded / no — and why} |

- **Which term dominates over the default horizon, and which dominates over one year.** They are usually different terms, and confusing the two is how a long-horizon allocation gets judged on a short-horizon outcome.
- **Which term is bounded.** At least one term in most decompositions cannot compound forever (a multiple cannot rise without limit; a yield cannot fall below zero indefinitely). Name it and say what happens when it stops.
- **Which terms are subtractions the investor controls.** Cost and tax are the only terms with a certain sign. Say so.

## Valuation anchors and their honest track record

The heart of the file. One row per anchor, and **no row is allowed without its failure horizon.**

| Anchor | Works at | Does NOT work at | Explanatory power | Sample | Source, date, label |
|---|---|---|---|---|---|
| {anchor} | {horizon} | {horizon} | {R², correlation, or "not sourceable"} | {period, market} | {source} {[verified/partial/unverified]} |

### Why this asset class has the predictability it has

Not "valuation works" — *why* it works here, mechanically, and how that mechanism compares with the other asset classes in this vault. The predictability of an asset class is a property of how contractual its cash flows are, not of how popular its valuation ratio is. State:

- **How much of the terminal payoff is contractually fixed at purchase.** This is the whole difference between a bond and an equity, and it is the reason a single number can be a near-complete forecast for one and a weak conditional distribution for the other. Do not treat "valuation" as one thing across asset classes.
- **What has to be forecast that is not fixed.** Every unfixed term is a source of forecast error, and the error compounds with the horizon rather than cancelling.
- **What ends the mean reversion.** The anchor assumes something reverts. Name the something, and name the conditions under which it stops reverting.

## Historical return distribution

Point estimates are for people who have not read this section. What a wealth manager must hold in mind while sizing.

- **Rolling real returns over the default horizon:** {best, worst, median, and the width of the middle 80% — with source and period}
- **Worst realised outcome ever recorded, and where:** {the number, the market, the window}
- **Drawdown depth and time to recovery:** {the named episodes, with trough dates and recovery dates — in REAL terms, because nominal recovery flatters}
- **The longest stretch of negative real return:** {years}
- **What the distribution looks like conditioned on a starting valuation like today's:** {or state plainly that the vault cannot compute this yet, and what would let it}

**Sizing implication.** One or two sentences translating the numbers above into how much of this exposure can be held without being forced to sell it. This is the sentence the owner will actually reread.

## Regime and structural-change risks

Why the historical record may not repeat. Each entry states the mechanism, the direction of the bias, and whether it makes the historical record too optimistic or too pessimistic.

- **Accounting and measurement changes:** {do the historical and current versions of the denominator mean the same thing?}
- **Index composition drift:** {has the thing being measured changed identity over the sample?}
- **Sector and country mix shift:** {and whether the anchor's historical level is comparable across the mix}
- **Payout-policy shift:** {buybacks vs dividends, or coupon vs capital structure — where a shift silently breaks a per-share growth series}
- **Survivorship and single-country bias:** {the difference between one country's history and the global record; which of the two this framework's headline numbers come from}
- **Structural level shift in the anchor itself:** {has the anchor's own mean moved, and is the evidence for that a mechanism or just recent data?}

## Correlation and portfolio role

What this exposure is FOR, against the owner's existing holdings — not in the abstract.

- **Role:** {growth engine / ballast / inflation hedge / liquidity}
- **Correlation with the other exposures held, and the regime in which that correlation breaks:** {number, source, and the named episode where it failed}
- **What it overlaps with that is already owned:** {an exposure bought alongside single stocks in the same index is partly a bigger position in those stocks, not a diversifier — quantify it}
- **Currency:** {what the exposure's currency exposure actually is, in the owner's base currency, and whether that is a deliberate bet}

## Alternatives to this exposure

The decision unit is an allocation *against alternatives*, so the alternatives are part of the framework, not part of the fund document.

| Alternative | What it gets you that this does not | What it costs you | When it is the better call |
|---|---|---|---|
|  |  |  |  |

## When does the valuation anchor lie?

The exposure-level analogue of the industry frameworks' "when does the multiple lie". The failure modes of this file's own method, written by the person most likely to be fooled by them.

- {The state in which the anchor reads cheap and is not}
- {The state in which the anchor reads expensive and is not}
- {The measurement artifact that shifts the anchor without changing anything real}
- {The horizon at which the anchor is simply not a signal, quoted anyway}
- {The composition change that makes the historical level of the anchor non-comparable to today's}

## Red flags at exposure level

Things that look fine in a generic allocation write-up and signal real trouble here. The non-obvious ones are the valuable ones.

-
-
-

## Kill switches at exposure level

Per PROD-P{n}, a switch is only usable if it names a threshold, a timeframe, and an **observable that is actually published**. At exposure level the honest set is small, and it is mostly about the *thesis for holding the exposure* rather than about price — see "Principle authority (canonical)": nothing here fires automatically, and price alone never triggers anything.

| Switch | Threshold | Timeframe | Observable, and where it is published | Named fallback if the series dies |
|---|---|---|---|---|
|  |  |  |  |  |

**What is deliberately NOT a switch here:** {drawdown depth, a valuation level crossing a line, an anchor turning "expensive" — say which of these were considered and rejected, and why, so a future reader does not re-add them.}

## What this framework does not cover

The boundary, stated so a fund deep-dive does not assume this file answered a question it never asked.

- **Wrapper mechanics** — replication method, domicile, accumulating vs distributing, tracking difference, securities lending, counterparty risk, closure and merger risk. Those live in the universal vehicle framework, [`frameworks/etf-vehicle-mechanics.md`](etf-vehicle-mechanics.md), which is read alongside this one on every fund deep-dive.
- **Any single fund's costs.** An expense ratio is a fund fact; the *cost term in the decomposition* is generic here and gets its actual value from the fund document.
- **Tax.** The identity above carries a tax term because tax is a real return driver, not a footnote. The **rules** that populate it are wrapper- and jurisdiction-specific and live with the vehicle lens; what belongs here is only which parts of THIS exposure's return are taxed differently from each other (income vs capital, for instance), because that is a property of the asset class. Whatever this file or any other in the vault says about tax is research, not advice, and specifics need the owner's tax advisor to confirm.

## Mental-model crossover risks

The assumptions from the **industry** frameworks in this vault that do not transfer to an exposure. Required section, even if short — the owner's other frameworks are all single-business frameworks, and importing their instincts into an asset class is the predictable failure. Be specific.

- **Moat analysis is silent here, and silence is not a clean bill.** There is no mechanism to name, no switching cost to credit, no cost curve to rank. A diagnostic that is simply inapplicable must not be read as "passed" (compare the way an inapplicable lens was handled in frameworks/memory-semiconductors.md).
- **Management quality does not exist as a variable.** {And what replaces it, if anything: index methodology, provider governance, the committee that decides classification.}
- **{The stock-level habit that produces the worst error here}** (see NARC-M{n}: an assumption carried in from the last thing you studied).
- **{What "cheap" means differently at index level than at stock level}**
- **{Whether the range should be wider or narrower than a single-stock range, and why}**

## Open questions

Genuinely unresolved things about this exposure. Candidates for the next absorb, and citable as known gaps rather than guessed at.

- {question}

## Sources to absorb

External evidence enters this vault through `absorb` and nowhere else, so a framework's numbers are only as good as the library behind it. This section names **exactly** which sources would upgrade this file's figures from remembered or secondary to `verified`, in priority order, and states what each one specifically fixes. Queue them in `sources.md` and say here that they are queued — an unqueued list is a wish.

| Source | Type | Access path | What it upgrades in this file | Queued |
|---|---|---|---|---|
|  |  |  |  | {YYYY-MM-DD / no} |

## What I've learned over time

Append-only log. Write back after every fund deep-dive in this exposure, and — the high-signal entry this tier exists for — every time a 10-year window closes on a range this file produced, so the method gets graded by an outcome rather than by its own plausibility.

Entries are tagged by source skill so future-you can weight them appropriately.

- YYYY-MM-DD ({TICKER} fund deep-dive): one or two sentences on what was new.
- YYYY-MM-DD (range post-mortem, {window}): what the file predicted for the window that just closed, what actually happened, and which term of the decomposition was wrong.
