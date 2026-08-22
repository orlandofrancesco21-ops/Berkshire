---
name: framework-bootstrap
description: Generate a new evaluation framework from scratch, in one of two modes. INDUSTRY mode (a set of competing businesses) produces a draft covering industry structure, what makes a great business, industry-specific KPIs, valuation logic, red flags, and common archetypes — opinionated and useful for stock-picking, not a generic encyclopedia entry. EXPOSURE mode (an asset class) produces the lens a fund deep-dive needs: the return decomposition, the valuation anchors with the horizon each works and fails at, and the historical return and drawdown distribution. Use when starting research on a sector or an asset class for which no framework file exists in frameworks/. Triggered by phrases like "build a framework for X", "framework-bootstrap X", "build a framework for {asset class}", or starting research on a new sector or a new exposure.
---

# framework-bootstrap

## When to use

The user is starting research on a new industry or a new asset-class exposure and `frameworks/{slug}.md` does not exist yet. Common phrasings:

- "Let's build a framework for [industry]"
- "I want to research [industry] — start with the framework"
- "framework-bootstrap [industry]"
- "Build a framework for [asset class]" — developed-market equity, nominal government bonds, gold
- `fund-deep-dive` stopped because the exposure framework for a fund's asset class does not exist

Before running, check whether a framework already exists for this industry or exposure. If yes, suggest refining the existing one rather than creating a duplicate. For an exposure, check `frameworks/README.md`'s exposure-slug registry before inventing a slug — a fund deep-dive resolves its exposure through that table, and a second slug for the same asset class splits the lens in two.

## Inputs

- Industry name (e.g. "offshore drilling", "specialty chemicals", "European listed banks") **or** exposure name (e.g. "developed-market equity", "EUR investment-grade credit")
- Optional: lens the user wants emphasized (e.g. "focus on cyclical dynamics", "I care most about capital allocation")

## Process

1. **Branch first: is this an INDUSTRY or an EXPOSURE?** An **industry** is a set of competing businesses, and the analysis is about the dispersion *between* operators. An **exposure** is an asset class, where there is no operator, no moat and no capital-allocation decision to grade — the analysis is about a defensible expected-return range over a stated horizon, and the exposure deliberately owns the dispersion rather than betting on it. "European listed banks" is an industry; "developed-market equity", "nominal government bonds", "gold" are exposures. Ask if it is genuinely ambiguous rather than guessing — the wrong branch produces a document that looks complete and answers nothing.

   - **INDUSTRY → read `frameworks/_template.md`** as the starting structure. The output must follow this template exactly — it's not optional. Consistency across frameworks is what makes them comparable. Steps 5-7 apply as written.
   - **EXPOSURE → read `frameworks/_template-exposure.md`** instead, and follow it just as exactly, for the same reason. It exists because the industry template's central questions ("what makes a great business here", "how do good operators allocate capital") are meaningless for an asset class — an index has no management team to be wrong about. Steps 5-7 are replaced by step 5e.

2. **Ask one grounding question** (if the user hasn't already answered it): "Do you have an existing thesis or angle on this industry, or is this a clean-slate exploration?" This frames the rest of the work.

3. **Research deeply.** Spend tokens here. Sources to draw from:
   - Recent sell-side industry primers
   - Long-form articles from quality buy-side investors writing on this space
   - 10-K risk factor language across 3-5 large players (this reveals what management actually thinks matters)
   - Trade publications and industry associations
   - Recent earnings transcripts to hear how operators talk about the business
   - **In exposure mode the top five bullets mostly do not apply.** Substitute: the index provider's own methodology document and current factsheet (the rulebook is the mandate, the product name is marketing); long-run return datasets and the primary research on the anchor's track record, including the papers arguing the anchor has *failed*; and the paper or dataset that would let a rolling-return distribution be computed rather than remembered. A 10-K is not a source about an asset class.
   - `principles/` — the cross-industry principles that bear on this industry (start from the index in `principles/README.md`), cited inline by ID inside the sections the template already has: "Mental-model crossover risks" and "Red flags specific to this industry" (in exposure mode, "Red flags at exposure level"). Inline deliberately — step 1's template-exact rule means a new principles section here would make every existing framework non-conforming, so do not "improve" this into one. Advisory only, per "Principle authority (canonical)"; finding that nothing stored bears on a new industry is a valid result.

4. **Fill in each section opinionatedly.** Avoid generic statements ("companies make money by selling products"). The user already knows generic — they need framework-level insight that isn't in a Wikipedia article.

5. *(industry mode)* **Industry-specific KPIs section is the most important.** Produce 5-10 metrics that actually matter for this industry, with concrete benchmarks for "good" vs "concerning". If the right metric is non-obvious (P/NAV for miners, combined ratio for insurance, NIM for banks, Rule of 40 for SaaS), make sure it's explicitly called out.

6. *(industry mode)* **Valuation framework section must be specific.** State which multiple is primary and why generic multiples may mislead. Include historical ranges with sources.

7. *(industry mode)* **Red flags section needs 5+ industry-specific items.** Things that would NOT show up in a generic financial-statement scan. This is where industry expertise lives.

5e. *(exposure mode — replaces steps 5-7)* **Three sections carry the whole file, and each one has a discipline the file is not allowed to drop.**
   - **The return decomposition is the skeleton.** Write the identity that is actually true for *this* asset class, term by term, and say plainly whether it is an accounting identity or an approximation. Each term gets its historical contribution with a source, and a verdict on whether it can repeat. Name the bounded term — at least one term in most decompositions cannot compound forever — and name the terms whose sign is certain because the investor pays them (cost, tax). Say which term dominates over the default horizon and which dominates over one year; they are different terms, and confusing them is how a long-horizon allocation gets judged on a short-horizon outcome.
   - **Valuation anchors, each with the horizon at which it works AND the horizon at which it fails.** No row without its failure horizon — an anchor quoted without one is a forecast pretending to be a fact. State explanatory power with its sample, and go looking for the evidence *against* the anchor as hard as for it; the out-of-sample record is usually worse than the in-sample fit and is the finding most likely to stop a bad allocation. Then explain *why* this asset class has the predictability it has, mechanically: how much of the terminal payoff is contractually fixed at purchase is the whole difference between a bond and an equity, and "valuation" is not one thing across asset classes.
   - **The historical return and drawdown distribution, not a point estimate.** Rolling returns over the default horizon — best, worst, median, and the width of the middle 80% — plus drawdown depth and time to recovery *in real terms*, and the longest stretch of negative real return. This section also names the **history proxy** the instrument runs on (`scripts/exposure-history.py`), with the date the price feed actually starts, what the proxy substitutes for, how it differs, and which way that biases the distribution. Most funds tracking an exposure are younger than one cycle, so running the instrument on the fund's own ticker produces a handful of independent windows dressed as hundreds; the proxy is how that is avoided once, here, rather than badly in every fund document.

8. **Write the output to `frameworks/{slug}.md`.** Slugify the name (lowercase, dashes, no spaces). In exposure mode, add the slug to the exposure-slug registry in `frameworks/README.md` with the index families it covers — an exposure framework that a fund deep-dive cannot resolve to is an orphan.

## Output

A complete framework file. Then verbally summarize for the user.

In industry mode:

- The 3 most important industry-specific KPIs
- The primary valuation multiple and its historical range
- The 2-3 red flags they should pressure-test against any name they consider in this space

In exposure mode:

- The return decomposition in one line, and which term is doing most of the work
- The primary anchor, its explanatory power, and the horizon at which it is not a signal at all
- The worst realised outcome and the longest real recovery in the record, because that is the number that decides sizing

End with: "Initial draft saved to `frameworks/{slug}.md`. The framework gets sharper as you study specific names — refine this file every time you do a deep dive." In exposure mode the refinement trigger is a fund deep-dive in that exposure, and the high-signal one is a realized 10-year window closing on a range the file produced.

## Notes

- This is a v1 framework. It will be wrong in places. The user will refine it over time — that's the design.
- Cite sources where possible but don't over-cite. The framework is the user's POV, not a literature review.
- If the industry is obviously different from the user's existing frameworks (e.g. their other frameworks are all software but this is heavy industry), flag any mental-model crossover risks explicitly.
