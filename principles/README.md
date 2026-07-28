# Principles

Cross-industry investment principles — **the layer that outlives any single holding.**

`frameworks/` holds what is true of an industry. This holds what is true of *investing*: how to read a price, when asymmetry justifies size, what management behaviour signals, how narratives and cycles move, and the process rules that stop me from repeating my own mistakes. It is also where **named investors' views** live, attributed and conditioned — so a company evaluation can say what the field believes about the situation in front of it, not just what I believe.

## Routing

Which tier does a lesson belong to? The test: **would this sentence survive with the ticker *and* the industry deleted?**

| Scope | Home |
|---|---|
| Reasoning about one company | `sectors/{sector}/companies/{TICKER}/thesis.md` |
| True of one industry | `frameworks/{industry}.md` → "What I've learned over time" |
| True across industries | here |

An external claim *about a holding* is not a principle — it routes to [journal/_flagged.md](../journal/_flagged.md). Canonical rule: "Principles routing" in [docs/build-plan.md](../docs/build-plan.md).

## Index

| Theme | Prefix | Scope in one line |
|---|---|---|
| [Valuation discipline](valuation-discipline.md) | VAL | Turning a price into a decision: ranges, normalized denominators, the right multiple, cross-check clustering |
| [Asymmetry, entry and exit](asymmetry-entry-exit.md) | ASYM | When to act: reward-to-risk thresholds, exit discipline, entry anchors, windows of mispricing |
| [Business quality and moats](business-quality-and-moats.md) | MOAT | What makes a franchise durable, how moats are actually tested, and how they end |
| [Capital allocation signals](capital-allocation-signals.md) | CAPA | Reading management by what they do with cash — buybacks, M&A, incentives, disclosure |
| [Narrative and cycle models](narrative-and-cycle-models.md) | NARC | How stories and cycles move prices independently of fundamentals |
| [Process discipline](process-discipline.md) | PROD | The rules that govern my own behaviour: logging, cadence, calibration, honest negatives |

Boundary calls that come up repeatedly:

- **Management quality** → CAPA, unless the point is about the *durability of the business itself*, which is MOAT.
- **"The multiple is too low"** → VAL if the question is what the price implies; NARC if the question is why the market believes it; ASYM if the question is whether to buy.
- **"I keep doing this to myself"** → PROD. Behavioural failures are process failures.

## ID rules (summary — canon lives in docs/build-plan.md)

`{PREFIX}-P{n}` principle · `-M{n}` mental model · `-T{n}` trap. Bold-defined exactly once, in the file whose `prefix:` owns it; cited plainly everywhere else. Born once, never renumbered, never reused — gaps are normal and mean an item was deleted. Every ID-shaped token in the repo must resolve, or the commit is blocked.

Cite them: a thesis writes `ALIGNS|TENSION|VIOLATES {ID} — {why}`; `decision-log` stamps `relied on {ID}@{as-of}`; a framework cites inline `(see {ID})`.

## Terms and aliases

Normalized before dedupe and routing, so the same idea does not get stored twice under two names. `absorb` appends rows as it meets new synonyms.

| Canonical term | Aliases seen in the wild | Note |
|---|---|---|
| Owner earnings | free cash flow, adjusted FCF, distributable cash | Definitions differ materially — always check what the source subtracts for maintenance capex |
| ROIC | ROCE, ROIIC, cash-on-cash return | ROIIC (incremental) answers a different question than ROIC (average); do not merge |
| Moat | durable competitive advantage, economic castle, franchise | |
| Margin of safety | discount to intrinsic value, downside cushion | |
| Normalized earnings | mid-cycle earnings, through-cycle EPS, steady-state earnings | |
| Reward-to-risk | asymmetry, upside/downside skew, payoff ratio | |
| Kill switch | disconfirming evidence, thesis breaker, exit trigger | This vault's term is kill switch; only `thesis.md` holds authoritative ones |

## Two axes, moving separately

Each item carries `evidence:` (what the field supports: emerging / contested / well-supported) and `my record:` (what my own results show: untested / validated / mixed). The mismatches are the point — `well-supported | mixed` means respected investors agree and my trades do not, and that belongs in front of me *before* I size the next position. Promotion and demotion follow "Maturity and tier-1 sources (canonical)"; every change appends a dated Log line.

## When to split or merge

**Split** when one file is carrying two genuinely different decision contexts (e.g. VAL growing a distinct "special situations" cluster with its own rules). IDs travel with their blocks — that is what makes a split mechanical rather than a migration. **Merge** rarely: the urge usually means one file is simply underdeveloped.

Do not create a seventh file for a single orphan idea. Park it in the closest file's Open questions until a second and third instance show the theme is real.
