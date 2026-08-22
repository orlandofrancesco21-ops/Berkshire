---
name: evaluate
description: Single-entry-point skill for "I want to look at TICKER" without orchestrating the three-step prerequisite chain manually. Determines the relevant industry and sector for the ticker, checks whether frameworks/{industry}.md and sectors/{sector}/primer.md already exist, runs framework-bootstrap and/or sector-primer inline if missing, then runs company-deep-dive. User-facing output is the deep-dive; intermediate artifacts (framework, primer) are written to disk for later refinement. Use when you want to evaluate a name and don't want to orchestrate the framework → primer → deep-dive sequence yourself. Routes funds to fund-deep-dive rather than company-deep-dive, resolving the exposure slug and bootstrapping the exposure lens inline first, exactly as the company path bootstraps a missing industry framework: an ETF is an exposure in a wrapper, not a business. Triggered by "evaluate X", "look at X", "let's look at X", "what about {TICKER}" (a ticker, not a general question), "I'm curious about X".
---

# evaluate

## When to use

You want to evaluate a name and don't want to think about whether the prerequisites are in place. Common phrasings:

- "Evaluate [TICKER]"
- "Let's look at [TICKER]"
- "What about [TICKER]"
- "I'm curious about [TICKER] — quick look"

This skill is a convenience wrapper. It does not replace the discipline of hand-editing frameworks and primers after they're generated — it just removes the friction of having to know what's missing before you can start. The first evaluation in a new sector is the most expensive (it bootstraps everything); subsequent evaluations in the same sector are fast because the framework and primer already exist.

## Inputs

- Ticker (with exchange suffix where relevant — `NKE`, `ASML.AS`, `RIO.L`)
- Optional: explicit industry hint if the obvious classification is wrong ("I want this evaluated as a luxury name, not generic apparel")

## Process

1. **Classify the ticker — first, is it a company or a fund?**

   If the ticker is an ETF, investment trust or any other pooled vehicle, this is a **fund** and the company path below does not apply: go to step 1f, which resolves the exposure, bootstraps the lens and hands off to `fund-deep-dive` — the skill that owns the funds tier and its two lenses (see "Funds tier (canonical)"). Signs you are looking at a fund rather than a business: it tracks a named index, it has an ISIN and a TER, its provider is an asset manager, or a lookup returns "ETF"/"Fund" as the quote type. When genuinely ambiguous, ask rather than guess — analysing a fund with the company skill produces a document about a business that does not exist.

   Otherwise this is a company. Determine:
   - Industry (the framework-level scope: "branded athletic footwear and apparel", "semiconductor equipment", "offshore drilling")
   - Sector slug (the more specific cut for the primer)

   Slugify both as lowercase-dashes. The right industry scope is narrow enough to be useful but broad enough to cover 5-10 names — "branded-athletic-footwear-and-apparel" not "global-consumer-discretionary"; "semiconductor-equipment" not "technology".

1f. **Fund path — resolve the exposure, bootstrap the lens, then hand off.** Steps 2-4 run `framework-bootstrap` inline when a company's lens is missing; the fund path does the same or it dead-ends the moment a fund arrives on an exposure nobody has written a framework for. That is the whole reason this step exists rather than a bare handoff.

   - **Resolve the exposure slug** against the exposure-slug registry in `frameworks/README.md`, matching on the **index the fund tracks** — from the rulebook or the fund's own documentation, never the product name. "Tracks MSCI World" is resolved by that registry, not by the words in the wrapper's name; a fund called "Global Leaders" may or may not be developed-market equity, and only the index says which.
   - **If no registered slug fits, do not stretch one.** A single-country, single-factor, sector or thematic index is a *different* exposure with different return drivers and different anchors, not a sub-case of a broad one. Propose the new slug and a one-line scope for it, and **ask before minting** — the registry is a taxonomy, and silently adding a row to it is the same too-much-autonomy that step 2's umbrella clause refuses on the navigator. Most funds hit no row today, so this is the expected path rather than the exception; the bootstrap run adds the row once the owner has assented.
   - **Bootstrap the missing lens.** Check `frameworks/{exposure-slug}.md`; if it is absent, run `framework-bootstrap {exposure-slug}` inline in **exposure mode**, which builds from `frameworks/_template-exposure.md` and adds the slug's row to the registry in the same run. Do not let it fall through to the industry template — an asset class is not an industry and that template asks the wrong questions of it. Then confirm `frameworks/etf-vehicle-mechanics.md` exists: it is universal and written once, so a missing one is bootstrapped once and never again.
   - Per "Concurrent orchestration (canonical)", a lens a peer invocation is concurrently writing counts as present: re-check rather than stopping at the first miss, read it fresh when it lands, and say in the handoff that it arrived mid-run so the thesis records what actually grounded it.
   - **Hand off to `fund-deep-dive`** with the ISIN (a bare ticker is an ambiguity, not an input — see that skill's Inputs), the resolved exposure slug, the horizon, and the allocation question. Its output, not this skill's, is what the user sees. Everything from step 2 down is the company path; skip it.

2. **Check for an existing framework.** Look for `frameworks/{industry-slug}.md`. Four cases:

   - **Exact match exists.** Use it as the lens. Continue to step 3.
   - **Umbrella framework exists (marker line `**Umbrella framework:** yes` at the top of the file — a Sub-sector navigator section alone does NOT make it an umbrella).** Identify the sub-sector this ticker belongs to from the navigator table. Then check whether the sub-framework exists. If yes, use it. If no, run `framework-bootstrap {sub-sector-slug}` inline.
   - **Related but not exact match exists** (e.g. you have `branded-consumer-apparel.md` but the ticker is athletic-specific). Use judgment — if the existing framework's lens fits, use it; if not, run `framework-bootstrap` for the narrower scope.
   - **Nothing exists.** Run `framework-bootstrap {industry-slug}` inline. The output is a v1 draft.

3. **Check for an existing sector primer.** Look for `sectors/{sector-slug}/primer.md`. If missing, run `sector-primer {sector-slug}` inline.

4. **Run `company-deep-dive`** on the ticker using the framework (or sub-framework, if step 2 went through the umbrella path) and primer just confirmed or created. The deep-dive's step 1 (existence check) and step 1b (umbrella check) will both pass, because a decision-grade framework now exists.

5. **In the user-facing output, lead with the deep-dive.** The framework and primer that were created (if any) are mentioned briefly but not foregrounded — the user asked about a company, not about infrastructure. Format:

   ```
   {TICKER} — evaluation

   {Deep-dive summary: thesis in 3 sentences, FV range, current price vs range, the one
   thing that worries you most, conviction level.}

   ---
   The one-page decision view is at sectors/{sector-slug}/companies/{TICKER}/ic-sheet.md.

   Infrastructure created during this evaluation (refine when you have time):
   - frameworks/{industry-slug}.md  ({"created v1 draft" / "already existed"})
   - sectors/{sector-slug}/primer.md  ({"created" / "already existed"})

   Recommended next: hand-edit the framework before relying on this thesis for any
   real decision. The auto-generated v1 is a starting point, not the answer.
   ```

## Output

The deep-dive summary, plus the brief infrastructure note. Same files-written confirmation as `company-deep-dive` itself.

On the fund path the output is `fund-deep-dive`'s, unchanged, with the same infrastructure note in the same register — naming the exposure slug that was resolved, `frameworks/{exposure-slug}.md` and `frameworks/etf-vehicle-mechanics.md` as created-v1-draft or already-existing, and carrying the same recommendation to hand-edit a v1 lens before any real allocation rests on it.

If the evaluation concludes PASS, the routing is identical to `company-deep-dive`: append to `watchlist.md` "Passed (with reason)" with a PASSED note in the thesis Update log.

## Notes

- This skill short-circuits the brief's "hand-edit between every step" discipline. That's the deliberate tradeoff. The output will be lower-quality than the manual three-step path because the framework and primer haven't been pressure-tested by the user before the deep-dive runs against them. Use the output as a starting point; hand-edit the framework before making any real decision.
- The first evaluation in a new sector pays the full bootstrap cost. The second evaluation in the same sector reuses the framework and primer — much faster. Over time, frameworks accumulate and `evaluate` collapses toward the speed of a bare `company-deep-dive`.
- If you find yourself running `evaluate` on names you don't actually intend to do work on, you're using the system as a screener. It's not a screener. Curiosity passes are fine occasionally; running this on 20 names a week is a sign you've slipped into screening behavior.
- The auto-generated framework gets a `framework-bootstrap` source tag in its "What I've learned over time" log. When you eventually hand-edit and refine it, append a dated entry noting the human pressure-test pass — that's the calibration data showing the framework went from v1-draft to v1-refined.
- If the umbrella framework has a Sub-sector navigator but no entry matches this ticker (e.g. a new sub-sector you hadn't anticipated), this skill should stop and ask — silently adding a new row to the navigator and bootstrapping against it is too much autonomy.
- The exposure slug is the fund path's equivalent of the industry scope, and it goes wrong the same way: too broad and the lens says nothing useful about what you are actually buying; too narrow and you are writing a framework per fund, which is a thesis with a framework's filename. One registered slug should serve every fund tracking that exposure, whoever wraps it.
- `evaluate` does not invoke `valuation-check` or `thesis-check` afterward. Those are monitoring skills for positions already held. The output of `evaluate` is a thesis + valuation that you then decide whether to act on (via `decision-log`) or pass on (auto-routed to watchlist).
