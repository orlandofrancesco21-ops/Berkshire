# Frameworks

Industry-specific evaluation playbooks. **The IP that compounds.**

## How to use

- One file per industry. Slugified filename: `banks.md`, `mining.md`, `offshore-drilling.md`, `saas-vertical.md`.
- Start from `_template.md`. Don't deviate from the structure unless you have a reason — consistency makes cross-framework comparison easier.
- Refine after every deep dive. The "What I've learned over time" section is the most valuable one over a 5-year horizon.

## When to create a new framework

When you're about to evaluate a name in an industry you don't yet have a framework for. Run `framework-bootstrap` to generate a draft, then hand-edit before using it for any real decision.

## When to split or merge

- **Split** when one framework is being stretched across genuinely different businesses (e.g. "tech" → split into "vertical SaaS", "ad-supported consumer", "semis-equipment").
- **Merge** rarely. If you're tempted, the answer is usually that one of the frameworks is just underdeveloped.

## Template sections worth knowing about

Two sections in `_template.md` are easy to skim past but deserve deliberate attention:

- **Sub-sector navigator (optional).** Keep this section if the framework covers an umbrella industry — financials, energy, industrials, healthcare — that spans genuinely different business models with different KPIs and valuation lenses. The navigator triages what kind of business you're actually looking at before you apply any framework, and `company-deep-dive` will require the matching sub-framework to exist before proceeding. Delete the section if the framework is for a single coherent business type (e.g. "offshore drilling" — no sub-sectors needed).
- **Mental-model crossover risks (required).** The assumptions that *don't* transfer from your other frameworks into this one. Every framework needs this, even if short, because the most reliable analytical mistakes come from importing heuristics that worked elsewhere ("scale wins", "recurring revenue is stable", "network effects compound") into industries where they don't. If your other frameworks are software and this is heavy industry — or vice versa — that section is where you write the warnings to your future self.
