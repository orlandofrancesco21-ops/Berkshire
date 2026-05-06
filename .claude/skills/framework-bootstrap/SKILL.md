---
name: framework-bootstrap
description: Generate a new industry evaluation framework from scratch. Use when starting research on a sector for which no framework file exists in frameworks/. The output is a draft framework document covering industry structure, what makes a great business, industry-specific KPIs, valuation logic, red flags, and common archetypes — opinionated and useful for stock-picking, not a generic encyclopedia entry. Triggered by phrases like "build a framework for X", "framework-bootstrap X", or starting research on a new sector.
---

# framework-bootstrap

## When to use

The user is starting research on a new industry and `frameworks/{industry-slug}.md` does not exist yet. Common phrasings:

- "Let's build a framework for [industry]"
- "I want to research [industry] — start with the framework"
- "framework-bootstrap [industry]"

Before running, check whether a framework already exists for this industry. If yes, suggest refining the existing one rather than creating a duplicate.

## Inputs

- Industry name (e.g. "offshore drilling", "specialty chemicals", "European listed banks")
- Optional: lens the user wants emphasized (e.g. "focus on cyclical dynamics", "I care most about capital allocation")

## Process

1. **Read `frameworks/_template.md`** as the starting structure. The output must follow this template exactly — it's not optional. Consistency across frameworks is what makes them comparable.

2. **Ask one grounding question** (if the user hasn't already answered it): "Do you have an existing thesis or angle on this industry, or is this a clean-slate exploration?" This frames the rest of the work.

3. **Research deeply.** Spend tokens here. Sources to draw from:
   - Recent sell-side industry primers
   - Long-form articles from quality buy-side investors writing on this space
   - 10-K risk factor language across 3-5 large players (this reveals what management actually thinks matters)
   - Trade publications and industry associations
   - Recent earnings transcripts to hear how operators talk about the business

4. **Fill in each section opinionatedly.** Avoid generic statements ("companies make money by selling products"). The user already knows generic — they need framework-level insight that isn't in a Wikipedia article.

5. **Industry-specific KPIs section is the most important.** Produce 5-10 metrics that actually matter for this industry, with concrete benchmarks for "good" vs "concerning". If the right metric is non-obvious (P/NAV for miners, combined ratio for insurance, NIM for banks, Rule of 40 for SaaS), make sure it's explicitly called out.

6. **Valuation framework section must be specific.** State which multiple is primary and why generic multiples may mislead. Include historical ranges with sources.

7. **Red flags section needs 5+ industry-specific items.** Things that would NOT show up in a generic financial-statement scan. This is where industry expertise lives.

8. **Write the output to `frameworks/{industry-slug}.md`.** Slugify the name (lowercase, dashes, no spaces).

## Output

A complete framework file. Then verbally summarize for the user:

- The 3 most important industry-specific KPIs
- The primary valuation multiple and its historical range
- The 2-3 red flags they should pressure-test against any name they consider in this space

End with: "Initial draft saved to `frameworks/{industry-slug}.md`. The framework gets sharper as you study specific names — refine this file every time you do a deep dive."

## Notes

- This is a v1 framework. It will be wrong in places. The user will refine it over time — that's the design.
- Cite sources where possible but don't over-cite. The framework is the user's POV, not a literature review.
- If the industry is obviously different from the user's existing frameworks (e.g. their other frameworks are all software but this is heavy industry), flag any mental-model crossover risks explicitly.
