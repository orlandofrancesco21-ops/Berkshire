---
name: evaluate
description: Single-entry-point skill for "I want to look at TICKER" without orchestrating the three-step prerequisite chain manually. Determines the relevant industry and sector for the ticker, checks whether frameworks/{industry}.md and sectors/{sector}/primer.md already exist, runs framework-bootstrap and/or sector-primer inline if missing, then runs company-deep-dive. User-facing output is the deep-dive; intermediate artifacts (framework, primer) are written to disk for later refinement. Use when you want to evaluate a name and don't want to orchestrate the framework → primer → deep-dive sequence yourself. Triggered by "evaluate X", "look at X", "let's look at X", "what about X", "I'm curious about X".
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

1. **Classify the ticker.** A quick web lookup to determine:
   - Industry (the framework-level scope: "branded athletic footwear and apparel", "semiconductor equipment", "offshore drilling")
   - Sector slug (the more specific cut for the primer)

   Slugify both as lowercase-dashes. The right industry scope is narrow enough to be useful but broad enough to cover 5-10 names — "branded-athletic-footwear-and-apparel" not "global-consumer-discretionary"; "semiconductor-equipment" not "technology".

2. **Check for an existing framework.** Look for `frameworks/{industry-slug}.md`. Four cases:

   - **Exact match exists.** Use it as the lens. Continue to step 3.
   - **Umbrella framework exists (has a "Sub-sector navigator" section).** Identify the sub-sector this ticker belongs to from the navigator table. Then check whether the sub-framework exists. If yes, use it. If no, run `framework-bootstrap {sub-sector-slug}` inline.
   - **Related but not exact match exists** (e.g. you have `branded-consumer-apparel.md` but the ticker is athletic-specific). Use judgment — if the existing framework's lens fits, use it; if not, run `framework-bootstrap` for the narrower scope.
   - **Nothing exists.** Run `framework-bootstrap {industry-slug}` inline. The output is a v1 draft.

3. **Check for an existing sector primer.** Look for `sectors/{sector-slug}/primer.md`. If missing, run `sector-primer {sector-slug}` inline.

4. **Run `company-deep-dive`** on the ticker using the framework (or sub-framework, if step 2 went through the umbrella path) and primer just confirmed or created. The deep-dive's step 1b will pass because the framework now exists.

5. **In the user-facing output, lead with the deep-dive.** The framework and primer that were created (if any) are mentioned briefly but not foregrounded — the user asked about a company, not about infrastructure. Format:

   ```
   {TICKER} — evaluation

   {Deep-dive summary: thesis in 3 sentences, FV range, current price vs range, the one
   thing that worries you most, conviction level.}

   ---
   Infrastructure created during this evaluation (refine when you have time):
   - frameworks/{industry-slug}.md  ({"created v1 draft" / "already existed"})
   - sectors/{sector-slug}/primer.md  ({"created" / "already existed"})

   Recommended next: hand-edit the framework before relying on this thesis for any
   real decision. The auto-generated v1 is a starting point, not the answer.
   ```

## Output

The deep-dive summary, plus the brief infrastructure note. Same files-written confirmation as `company-deep-dive` itself.

If the evaluation concludes PASS, the routing is identical to `company-deep-dive`: append to `watchlist.md` "Passed (with reason)" with a PASSED note in the thesis Update log.

## Notes

- This skill short-circuits the brief's "hand-edit between every step" discipline. That's the deliberate tradeoff. The output will be lower-quality than the manual three-step path because the framework and primer haven't been pressure-tested by the user before the deep-dive runs against them. Use the output as a starting point; hand-edit the framework before making any real decision.
- The first evaluation in a new sector pays the full bootstrap cost. The second evaluation in the same sector reuses the framework and primer — much faster. Over time, frameworks accumulate and `evaluate` collapses toward the speed of a bare `company-deep-dive`.
- If you find yourself running `evaluate` on names you don't actually intend to do work on, you're using the system as a screener. It's not a screener. Curiosity passes are fine occasionally; running this on 20 names a week is a sign you've slipped into screening behavior.
- The auto-generated framework gets a `framework-bootstrap` source tag in its "What I've learned over time" log. When you eventually hand-edit and refine it, append a dated entry noting the human pressure-test pass — that's the calibration data showing the framework went from v1-draft to v1-refined.
- If the umbrella framework has a Sub-sector navigator but no entry matches this ticker (e.g. a new sub-sector you hadn't anticipated), this skill should stop and ask — silently adding a new row to the navigator and bootstrapping against it is too much autonomy.
- `evaluate` does not invoke `valuation-check` or `thesis-check` afterward. Those are monitoring skills for positions already held. The output of `evaluate` is a thesis + valuation that you then decide whether to act on (via `decision-log`) or pass on (auto-routed to watchlist).
