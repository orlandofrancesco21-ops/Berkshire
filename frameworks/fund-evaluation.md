# Fund evaluation — is this manager or strategy actually adding anything?

> Personal playbook for the **third** lens on a fund. The wrapper lens (`frameworks/etf-vehicle-mechanics.md`) asks *is this a good container*. The exposure lens (`frameworks/{exposure-slug}.md`) asks *is this asset class worth owning*. This file asks the question neither of them can: **is this manager or this strategy delivering something a cheap combination of index funds could not have delivered — and can I tell that apart from luck?**
> Written 2026-08-23, before any fund in this vault has been evaluated through it. Read the dated figures as calibration, not as current state.
> Append-only in "What I've learned over time". Refine every time a fund is evaluated.

**Last updated:** 2026-08-23
**Umbrella framework:** no — this is a **lens, not an industry**, like the wrapper lens. It is decision-grade on the skill question alone and never sufficient by itself: a fund deep dive still requires the wrapper lens and an exposure framework. Neither substitutes for the other.

---

## What this lens is, and why "is it a good fund" is two different questions

For a **passive** fund, good means *faithful and cheap*. There is no manager, no skill claim, and no residual to test — there is a rulebook, a replication method, and a cost that shows up as tracking difference. That question is fully owned by the wrapper lens and is already built. This file's contribution to a passive fund is its **faithfulness half** (tracking error, R-squared against the stated index, up/down capture symmetry, correlation to the exposure the fund claims to give) and nothing else. A passive fund evaluated through the skill half of this file will produce a manufactured finding, which is worse than none.

For an **active** fund, good means the manager delivered something a cheap combination of index funds could not have. That is a **statistical claim about a residual**, not a performance table. The whole method is: decompose the realised return into benchmark beta, factor exposures, costs and a residual — then ask whether the residual is distinguishable from luck at a stated confidence, with a stated number of observations. If it is not, the honest output is "could not establish", and per PROD-P6 that is a pass with a reason, not a verdict.

**The one sentence that matters:** almost every fund evaluation that goes wrong goes wrong in one of exactly two places — the **wrong benchmark**, or **too little data** — and both of them fail in the flattering direction, so neither announces itself.

Those two failure modes get sections 1 and 3, at the front, before any ratio is computed. They are not caveats at the end. A caveat at the end of a document is a thing the reader has already stopped reading.

### How this lens interacts with the other two

Three lenses, three verdicts, and they are genuinely separable — a fund can be a good strategy in a bad wrapper, a bad strategy in an excellent wrapper, or the right exposure reached the wrong way. The actions differ, so the verdicts must stay in separate sentences from the first draft onward, exactly as "Funds tier (canonical)" already requires for the first two.

| Lens | Question | Failure it detects | Action when it fails |
|---|---|---|---|
| Exposure (`frameworks/{exposure-slug}.md`) | Is this asset class worth owning at today's starting point? | Bad asset class, or bad starting valuation | Do not own the exposure. No wrapper and no manager fixes this |
| Wrapper (`frameworks/etf-vehicle-mechanics.md`) | Given the exposure, is this container faithful, cheap, tax-efficient and structurally sound? | Leaky, closure-prone or tax-wrong container | **Fund switch.** Same exposure, different ISIN. Not a view on the asset |
| Skill (this file) | Given the exposure and the container, is the manager adding a residual I could not buy cheaply? | Factor beta sold as alpha; a record too short to support the claim | **Replace the active fund with the factor combination that explains it**, or with the plain index fund. Also not a view on the asset |

The interaction that is easy to miss and expensive: **the skill verdict and the wrapper verdict use the same raw material and answer different questions.** A negative tracking difference on a passive fund is a *cost* finding for the wrapper lens. A negative alpha on an active fund is a *skill* finding for this one. The arithmetic is nearly identical and the conclusions route to different actions. Say which lens a number is doing work for, every time.

And the ordering rule: **run the exposure lens first, the wrapper lens second, this one third.** A manager whose alpha is real and whose exposure is a bad asset class at a bad price is still a bad allocation. Skill is a modifier on an exposure decision, never a substitute for one.

## 1. Benchmark selection comes first

The benchmark is not an administrative field. It **is** the definition of the residual, and every number downstream — alpha, information ratio, tracking error, up/down capture, active share — is defined relative to it. Get it wrong and the entire evaluation measures a style tilt and calls it skill.

The mechanism is not subtle: a mid-cap growth fund measured against a large-cap blend index earns or loses whatever the mid-cap-growth-versus-large-cap-blend spread was over the window, before the manager does anything at all. Over 2010-2020 that spread flattered nobody; over 1990-2009 it did the reverse. The manager did not change.

**This is not a theoretical worry — it is the documented explanation of the single most cited manager-selection metric in the industry.** Frazzini, Friedman and Pomorski re-ran Cremers and Petajisto's own sample and found the active-share result was a benchmark composition effect: "Sorting funds on active share is equivalent to sorting on benchmark type," and after controlling for benchmark differences, "we found no significant relationship between the active share measure and fund returns" (*Deactivating Active Share*, Financial Analysts Journal Vol 72 No 2, March/April 2016, PDF text extracted and read 2026-08-23, **verified**). A whole literature, an industry rule of thumb and a generation of manager-selection processes rested on a benchmark artifact. Assume the same is true of any new predictor until it has been re-run inside benchmarks.

### The selection method

Match the fund's **actual holdings and realised factor profile**, not its marketing category. In order:

1. **Start from the holdings file, not the category label.** Market-cap distribution, sector weights, country weights, and the number of names. "Global equity" and "European small-cap value" are both categories that hundreds of very different portfolios sit inside.
2. **Take the prospectus benchmark as a hypothesis and test it.** Regress the fund's excess return on the candidate benchmark's excess return and read three things: **beta**, **R-squared**, and the **residual (tracking-error) volatility**. This is what `python scripts/fund-metrics.py {TICKER} --benchmark {TICKER}` produces, and it produces the t-statistic on alpha at the same time, which section 3 makes mandatory.
3. **Judge the fit on R-squared, and judge the honesty of the label on beta.** A stated benchmark that produces a low R-squared is not the fund's benchmark, whatever the prospectus says. A beta materially away from 1.0 against the fund's own stated benchmark means the fund is running a leverage or defensiveness tilt that will masquerade as alpha in any rising or falling market respectively — CAPM alpha already strips this, which is exactly why the raw excess return does not.
4. **Test at least two rival benchmarks and report all of them.** One benchmark produces a number; three produce a *range*, and the width of that range is the honest uncertainty in the alpha estimate before any statistics are done. If the alpha's sign flips across defensible benchmarks, there is no alpha finding — there is a benchmark-selection finding, and it should be written as one.
5. **Beware the fund whose style drifts.** SPIVA measures this directly and the number is worse than most people expect: over 15 years, only **43.77%** of all domestic equity funds that survived still carried the same style classification they started with, and over 20 years **47.70%** (SPIVA U.S. Scorecard Mid-Year 2025, Report 2, data as of 2025-06-30, PDF extracted and read 2026-08-23, **verified**). A single fixed benchmark applied across a 15-year record is, more likely than not, the wrong benchmark for part of it. Run the regression on sub-periods and look at whether beta and R-squared are stable. **A rolling beta that trends is a style drift, and it is a finding about the manager, not noise in the estimate.**

### When no clean benchmark exists

Say so, and use a blend. The honest answer for a genuinely unusual mandate is a **blended benchmark** — a weighted combination of investable indices chosen to match the fund's actual exposures — with the weights stated, dated, and justified from the holdings file rather than fitted to maximise or minimise the alpha.

Two rules that keep a blend honest:

- **Fix the weights from holdings, not from the return regression.** Weights chosen to maximise R-squared are an in-sample fit and will absorb genuine alpha along with genuine beta. State the holdings-derived weights first; if a return-fitted blend disagrees materially, that disagreement is itself the finding (usually: the fund's realised exposure differs from its stated one).
- **A blend is a *self-built* benchmark, and per ESMA's own reasoning about bespoke indices in the wrapper lens, an index built to one participant's specification is a weak benchmark of a market.** The defence is publishing the recipe: write the constituents and weights into `valuation.md` so a later run grades the *same* blend rather than quietly re-fitting one.

**And where even a blend cannot be defended, the correct output is that this fund's performance is not measurable and therefore its skill claim is not assessable.** That is a complete answer. It routes to PASS with a reason, not to a softer verdict computed off a benchmark nobody believes.

## 2. The return decomposition — the analytical core

Walk the ladder. Each rung absorbs a source of return that is **separately purchasable at low cost**, and the residual after each rung is what remains unexplained.

| Rung | Model | What it absorbs | What the residual then means |
|---|---|---|---|
| 0 | Raw total return | Nothing | A number with no information content whatsoever about skill |
| 1 | Return minus benchmark | The market's own return | Excess return. Still contains every systematic tilt the fund runs |
| 2 | CAPM: `r_f + β(r_m − r_f)` | Market beta — leverage and defensiveness | **Jensen's alpha.** The residual after being paid for market risk |
| 3 | Fama-French 3: adds SMB, HML | Size and value tilts | Alpha after size and value. Most "value manager alpha" dies here |
| 4 | Carhart 4: adds momentum (UMD/MOM) | Momentum | Alpha after momentum. Most "growth momentum manager alpha" dies here |
| 5 | Fama-French 5: adds RMW (profitability), CMA (investment) | Quality and conservative-investment tilts | Alpha after the five. Most "quality compounder manager alpha" dies here |

Factor return series for every rung are available free and primary from the **Ken French data library**, which publishes *Fama/French 3 Factors*, *Fama/French 5 Factors (2x3)*, and the *Momentum Factor (Mom)* at monthly and daily frequency, plus **Developed, Developed ex US, European, Japanese, Asia Pacific ex Japan and North American** regional variants of the 3- and 5-factor sets and momentum, and an Emerging 5-factor set (Ken French data library page read 2026-08-23, **verified**). The regional sets matter here: a EUR-base investor evaluating a European fund against US factors is running section 1's error in a second dimension.

### The finding that matters, and how to recognise it in a regression output

**When a manager's apparent alpha shrinks toward zero as factors are added, you are not buying skill. You are paying active fees for factor beta you could buy cheaply.** The pattern is completely mechanical and it looks like this:

- Excess return over benchmark: **+2.8% a year**, and this is the number on the factsheet.
- CAPM alpha: **+2.1%**, t = 1.2. Some of it was beta above 1 in a rising market.
- FF3 alpha: **+0.6%**, t = 0.4, and the **HML loading is +0.45 with a t of 4.8**.
- Carhart alpha: **+0.3%**, t = 0.2.

*(Illustrative arithmetic showing the shape to look for — **not** any fund's figures, and it is deliberately not sourced to one, because inventing a fund's numbers to make a point is the exact failure "Verification labels (canonical)" exists to prevent.)*

The diagnostic is **not** the size of the final alpha. It is the pair of facts that (a) alpha fell substantially as factors entered, and (b) a factor loading is large **and statistically strong** while the alpha is small and statistically weak. That combination says the return has a name, the name is a factor, and the factor is purchasable through a cheap systematic fund. Read the loadings' t-statistics, not just the alpha's — a loading is estimated far more precisely than a mean, so factor exposures are the *reliable* half of the regression output and alpha is the unreliable half.

Three refinements that prevent the wrong conclusion from the right regression:

- **A significant factor loading is not by itself a criticism.** If the fund is *sold* as a value fund and its HML loading is +0.45, it is doing what it said. The criticism is the **fee**: the correct comparison is then this fund against a cheap systematic value fund with the same loading, not against the plain market index. That comparison is the actual decision, and it belongs in the wrapper lens's peer table with the factor fund named as a peer.
- **A negative loading matters as much as a positive one.** Persistent negative SMB (a large-cap tilt) inside a fund benchmarked to a small-cap index is section 1's error wearing a different hat.
- **Do not stop at FF5 and call it complete.** Quality, low-volatility, betting-against-beta, and liquidity factors are not in FF5, and a fund loading on one of them will show an unexplained residual that looks like alpha under this ladder. Say what the ladder *cannot* absorb rather than treating rung 5 as the end of the world.

The vault's script contract gives rungs 0-2 directly: `python scripts/fund-metrics.py {TICKER} [TICKER2 ...] --benchmark {TICKER} [--rf 4.0] [--years N]` returns annualised return and volatility, Sharpe, Sortino, max drawdown and recovery, tracking error, information ratio, **CAPM alpha and beta with t-statistics and R-squared**, up/down capture, and a correlation matrix, aligned to the series' **common overlapping period** — which it states, and which section 3 makes the reader read before anything else. **Rungs 3-5 are not in the script as of 2026-08-23.** Until they are, any alpha this vault quotes from the script is a *CAPM* alpha, must be labelled as such, and must carry the sentence that it has not been adjusted for size, value, momentum, profitability or investment. Quoting a CAPM alpha as though it were a factor-adjusted one is this section's headline error committed by the tooling rather than by the analyst.

## 3. The statistical-power problem, stated in years

This is the section that separates an honest evaluation from a plausible one.

### The relationship

For a fund with annualised alpha *α* and annualised tracking error *TE* against its benchmark, the information ratio is **IR = α / TE**, and the t-statistic on the estimated alpha over *N* years of data is

> **t = IR × √N**

because the standard error of the annualised alpha estimate is TE / √N. Inverting: the record length required for a given alpha to clear a given t-hurdle is

> **N = (t_hurdle / IR)²**

Three thresholds are worth carrying, and they answer three different questions:

- **t ≥ 1.96** — the conventional 5% two-sided significance level. `N = 3.84 / IR²`. This is the length at which the point estimate *would* be significant **if the realised IR equals the true IR**, which is the coin landing exactly on its expectation.
- **80% power** — the length at which you would actually *detect* a true alpha of that size 80% of the time. `N = 7.85 / IR²`, roughly **double** the previous column. This is the honest number for the question "how long before I could tell", and it is almost never the one quoted.
- **t ≥ 3.0** — the hurdle appropriate when the fund was selected out of a screened universe rather than examined in isolation, because a 5% threshold applied to 100 candidates yields 5 false positives by construction. `N = 9 / IR²`.

### The worked table

Years of monthly data required, computed 2026-08-23 from the formulae above (**arithmetic on a stated relationship, not an empirical result** — the inputs are hypothetical alpha/TE pairs chosen to span the plausible range):

| Alpha (ann.) | Tracking error (ann.) | IR | Years for t ≥ 1.96 | Years for 80% power | Years for t ≥ 3.0 |
|---|---|---|---|---|---|
| 4.0% | 4.0% | 1.00 | 3.8 | 7.8 | 9.0 |
| 3.0% | 4.0% | 0.75 | 6.8 | 14.0 | 16.0 |
| **2.0%** | **4.0%** | **0.50** | **15.4** | **31.4** | **36.0** |
| 1.5% | 3.0% | 0.50 | 15.4 | 31.4 | 36.0 |
| 2.0% | 6.0% | 0.33 | 34.6 | 70.6 | 81.0 |
| 1.0% | 4.0% | 0.25 | 61.5 | 125.6 | 144.0 |
| 2.0% | 8.0% | 0.25 | 61.5 | 125.6 | 144.0 |
| 0.5% | 2.0% | 0.25 | 61.5 | 125.6 | 144.0 |

**A 2% alpha at 4% tracking error — a genuinely good active manager — needs about 15 years to reach conventional significance and about 31 years to be reliably detectable.** That is the number to remember.

Read the same relationship from the other end, which is the form that actually bites in practice:

| Record length | True IR needed for t ≥ 1.96 | Equivalent alpha at 4% TE | at 6% TE |
|---|---|---|---|
| 3 years | 1.13 | 4.53% | 6.79% |
| **5 years** | **0.88** | **3.51%** | **5.26%** |
| 10 years | 0.62 | 2.48% | 3.72% |
| 15 years | 0.51 | 2.02% | 3.04% |
| 20 years | 0.44 | 1.75% | 2.63% |
| 30 years | 0.36 | 1.43% | 2.15% |

**The uncomfortable conclusion, stated plainly: most fund track records in existence are too short to support the claim being made about them, and a five-year record is nearly always insufficient.** A five-year window can only establish skill for a manager with a *true* sustained information ratio near 0.88 — 3.5% of alpha a year at 4% tracking error, every year, as a population parameter rather than a realised outcome. Sustained IRs at that level are not a normal feature of the fund universe; a five-year record that appears to show one is far more likely to be a lucky draw from a low-IR distribution than a genuine high-IR manager, simply because there are vastly more of the former.

### Two corollaries that surprise people

- **Monthly data does not rescue a short record, and daily data does not either.** The precision of an estimated *mean* depends on the calendar span of the sample, not on how finely it is sliced. Merton's result is that the standard error of an expected-return estimate is not reduced by sampling more frequently within a fixed period — volatility can be pinned down from high-frequency data, drift cannot (Merton, "On Estimating the Expected Return on the Market: An Exploratory Investigation", *Journal of Financial Economics* 8, 1980, pp. 323-361; the specific statement relayed from search summaries after the primary PDF returned a 404 and an SSRN mirror returned HTTP 403 on 2026-08-23, **unverified**, and it is doing real work here so it should be read before the next fund evaluation leans on it). The practical consequence stands regardless of the citation: `--years N` in the metrics script is the binding constraint on what can be concluded, and no sampling choice relaxes it.
- **The published evidence says the noise swamps the signal in the cross-section.** Fama and French report that the average OLS standard error of individual-fund alpha estimates — "the average imprecision of α estimates" — is **0.28% per month (3.4% per year)**, while the standard deviation of *true* alpha across the whole active universe is about **1.25% per year** ("Luck versus Skill in the Cross-Section of Mutual Fund Returns", *Journal of Finance* 65(5), October 2010, pp. 1915-1947, sample January 1984 to September 2006, PDF text extracted and read 2026-08-23, **verified**). **The typical measurement error is roughly 2.7 times the entire cross-sectional spread of the thing being measured** (3.4 / 1.25, computed 2026-08-23). Note honestly what inflates that average: their panel admits funds with as few as eight months of returns, so short-lived funds pull the mean standard error up. The direction of the point is unaffected and the magnitude is the right order.

### The vault rule this section mints

> **Every alpha this vault ever quotes carries a t-statistic and the number of observations, in the same sentence as the alpha.** An alpha without both is not a finding; it is a number. This applies in `thesis.md`, in `valuation.md`, in `ic-sheet.md` and in any chat output. Where the t-statistic is below the hurdle, write "not distinguishable from zero at N years" rather than reporting the point estimate as though it were the conclusion.

This is PROD-P5's discipline extended from prices to statistics, and it should become a mechanical gate rather than a convention — PROD-M1 says a step that depends on remembering it under pressure is not fixed. Logged in Open questions as a proposed lint.

## 4. The ratios — what each is for, and where each lies

Every ratio below is a summary statistic, which means it is a *compression* of the return series and therefore has a specific thing it cannot see. Know the blind spot before quoting the number. All of these come out of the metrics script; none of them is a verdict.

**Sharpe ratio** — excess return over the risk-free rate, divided by total volatility. The right measure for a **standalone** portfolio held on its own, because it prices total risk. Good reading: higher than the benchmark's own Sharpe over the *same* window, which is the comparison almost nobody makes.
- *Cannot see:* the shape of the distribution. It assumes risk is symmetric and fully described by standard deviation.
- *How it is gamed:* by selling tail risk. Goetzmann, Ingersoll, Spiegel and Welch show the Sharpe ratio "may be manipulated with option-like strategies", derive the strategy that maximises it, and state the consequence directly — "Expected returns being held constant, high Sharpe ratio strategies are, by definition, strategies that generate regular modest profits punctuated by occasional crashes" ("Sharpening Sharpe Ratios", NBER Working Paper 9116, August 2002, PDF extracted and read 2026-08-23, **verified**; note the paper's own "Preliminary: please do not quote" marker on the working-paper version). Covered-call writing, short-volatility overlays, illiquid marks that smooth reported returns, and credit strategies whose losses arrive all at once all raise Sharpe without adding anything. **A high Sharpe plus negative skew plus a short record is the signature of a strategy that has not yet met its bad year, not of a good one.**
- *Also misread:* the risk-free rate is not a rounding error. The script's `--rf` default must be stated with its date; a Sharpe computed at 4% cash against one computed at 0% cash are different numbers about the same fund.

**Sortino ratio** — excess return over *downside* deviation only. The right measure when the return distribution is genuinely asymmetric and upside volatility is not the risk being managed.
- *Cannot see:* it still says nothing about the benchmark. A fund with a great Sortino that simply owns a rising asset class has demonstrated nothing about the manager.
- *How it is gamed:* through the two free parameters nobody states. The **minimum acceptable return** (zero? the risk-free rate? the benchmark?) and the **denominator convention** (divide the sum of squared shortfalls by the total number of periods, or only by the count of down periods?) both move the answer materially and are chosen by whoever is presenting. **Sortino is only comparable across funds when both conventions are stated.** Record which the script uses next to the figure.

**Information ratio** — alpha over tracking error. **The right ratio for judging an active manager against a benchmark**, because it prices exactly the risk the manager chose to take relative to the mandate, and because it is the direct input to the power arithmetic in section 3 (t = IR × √N).
- *Good reading:* sustained above ~0.5 over a long window is genuinely strong. Above 1.0 over a long window is exceptional and should be interrogated for a data problem, a benchmark mismatch, or an illiquidity mark before it is believed.
- *Cannot see:* everything section 1 covers. IR is defined by the benchmark, so a wrong benchmark produces a confidently wrong IR.
- *How it is gamed:* by shrinking the denominator. A closet indexer with 1.5% tracking error and 0.5% alpha posts an IR of 0.33 that looks respectable, on a portfolio that is 95% index at active fees — and section 3's table says that IR needs ~35 years to prove itself. **Always read IR alongside the absolute tracking error and the fee.** An IR is a ratio; the money is in the numerator.

**Calmar ratio** — annualised return over maximum drawdown. Useful precisely because max drawdown is the risk measure that matches how a real holder actually fails: by selling at the bottom.
- *Cannot see:* anything but a single worst episode. It is one observation, and it is the most sample-dependent statistic on this list.
- *How it is misread:* a fund launched after the last crisis has a small max drawdown because it did not exist for the bad window. This is the same inception-date artifact the wrapper lens documents for `scripts/exposure-history.py`, and it applies identically here. **A Calmar computed over a period containing no crisis is not a risk measure.** State the window and whether it contains a drawdown regime.

**Up-capture and down-capture** — the fund's average return in periods when the benchmark rose, and when it fell, each as a percentage of the benchmark's.
- *Good reading:* up-capture above 100 with down-capture below 100 is the shape genuine skill produces. Both above or both below 100 usually means a beta bet, not skill — a fund with 115/115 is levered, and a fund with 85/85 is defensive, and neither has added anything a cash blend could not.
- *Cannot see:* asymmetry that is a **timing artifact of the window**. A fund holding cash through a period that happened to fall shows brilliant down-capture and has demonstrated nothing repeatable.
- *How it is gamed:* by the choice of period (monthly versus quarterly up/down periods can flip the reading) and by the number of down periods in the sample. **Read the count of down periods.** A down-capture computed on six observations is a story about six months.

**R-squared** — the fraction of the fund's return variance explained by the benchmark. Its main job here is section 1's job: it tells you whether the benchmark is the right one.
- *Good reading:* for a passive fund, very high (near-total) — anything else is a replication or index-variant problem for the wrapper lens. For an active fund, high enough that the benchmark is credible, low enough that the manager is doing something.
- *Cannot see:* direction or magnitude. A fund can have a very high R-squared and a large negative alpha.
- *How it is misread:* a **low** R-squared is routinely sold as evidence of independent thinking. It is equally consistent with tracking a different asset class, and it makes every other statistic on this list less reliable, because alpha and IR are both defined against a benchmark that explains little. **Low R-squared should widen the error bars on the skill claim, not strengthen it.**

**Correlation** — see section 5, because its job is a portfolio question and not a manager question.

## 5. Correlation and the portfolio question

Correlation is the one measure on this list that is **not** about the fund. It decides whether the fund adds anything **at portfolio level**, regardless of its standalone merit — and a fund with genuine, statistically established alpha that correlates near-perfectly with something already owned adds almost nothing but fees.

The metrics script produces a correlation matrix across every ticker passed to it in one call, over their common overlapping period. Use it that way: pass the candidate fund **and the existing holdings** together, not the candidate alone.

### Correlation is not beta, and conflating them is a real error

Correlation measures the **tightness** of the relationship; beta measures its **slope and scale**. Two funds can both correlate 0.95 with an index and have betas of 0.6 and 1.5 — identical co-movement, wildly different magnitudes of exposure. Mechanically, beta = correlation × (fund volatility / benchmark volatility), so a high correlation with a low beta is a *diversifier of magnitude*, not of direction.

The decision consequence: **correlation answers "will this fall at the same time"; beta answers "how far will it fall".** A portfolio built on correlation alone will be surprised by magnitude, and one built on beta alone will be surprised by timing. R-squared is the square of the correlation with a single benchmark, which is why sections 1 and 5 keep meeting.

### Correlation instability, and why it fails exactly when it is needed

Historical correlation is an average across regimes and it is **not stable across them**. The specific empirical shape matters: it is not that correlations rise when markets are volatile — it is that they rise when markets are *falling*. Longin and Solnik, using extreme value theory on the tails of the joint distribution, "reject the null hypothesis of multivariate normality for the negative tail, but not for the positive tail", and conclude that "correlation is not related to market volatility per se but to the market trend. Correlation increases in bear markets, but not in bull markets" ("Extreme Correlation of International Equity Markets", *Journal of Finance* 56(2), 2001, pp. 649-676, PDF text extracted and read 2026-08-23, **verified**).

Read that carefully, because the naive version is wrong in a way that matters: a high-volatility rally does **not** produce the correlation spike. The diversification a full-sample correlation matrix promises is a diversification that is systematically *absent in the drawdown it was bought for*. Three operational rules follow:

- **Compute correlation over the drawdown sub-periods separately**, not only over the full sample, and quote both. Where the sub-period sample is too small to be meaningful, say so rather than skipping it.
- **Discount any diversification claim resting on a full-sample correlation.** The honest posture is that the correlation you will actually experience in the bad state is higher than the number in the table, by an amount this vault has not yet measured.
- **A correlation-based allocation argument is a claim about a future regime, and per PROD-P3 it needs an observable and a threshold if it is going to be a kill switch at all.** "Correlation rose" is not a kill switch. "Trailing 36-month correlation to the core holding above X for two consecutive quarterly reviews" is.

### The portfolio decision rule this section produces

A fund earns portfolio space on one of two grounds, and the write-up must say which:

1. **It is a better version of an exposure already wanted** — cheaper, more faithful, or with an established residual. Here correlation to the incumbent should be *high*; that is the point, and the case is a switch.
2. **It is a genuinely different exposure or return stream.** Here correlation should be low, *and* the low correlation must survive the drawdown sub-period test, *and* the exposure itself must clear the exposure lens on its own merits. Low correlation to something bad is not a reason to own it.

Anything that is neither is a fee increase. Overlap must be computed from the holdings files rather than asserted from names, exactly as the `fund-deep-dive` skill already requires for the allocation step — two "global equity" funds can share most of their weight, and a correlation of 0.98 between them is a fact about the same stocks being owned twice.

## 6. Active share and holdings-based measures

Returns-based analysis (sections 2-4) infers what a fund does from what it earned. Holdings-based analysis reads what it actually owns. The second sees things the first cannot:

- **Closet indexing**, directly and immediately, rather than inferred from a low tracking error after three years of data. This is the genuine contribution, and it is a **fee** finding rather than a skill finding.
- **Concentration and position sizing** — how much of the active risk sits in how few names.
- **Turnover and holding period**, which price the transaction costs the return series has already silently paid.
- **Style drift as it happens**, rather than a year later in a rolling regression. Given the 43.77% fifteen-year style-consistency figure in section 1, this is worth more than it sounds.
- **Overlap with what is already owned**, which is section 5's portfolio question answered without waiting for a correlation series to accumulate.

**Active share** is the headline holdings measure: one-half the sum of the absolute differences between the fund's weights and the benchmark's, running from 0 (identical to benchmark) to 1 (no overlap at all) (definition read from *Deactivating Active Share*, 2016, **verified**). It requires the **full holdings file and the benchmark's full constituent weights, at the same date** — which for a UCITS is retrievable, since index constituents and weights must be published, but which is genuinely laborious and must be repeated over time to mean anything. A single-date active share is a snapshot of a portfolio that may have been positioned for the disclosure.

### The honest state of the evidence

Cremers and Petajisto (2009) and Petajisto (2013) reported that high-active-share funds outperform their benchmarks and proposed a rule of thumb that funds below 60% active share should be avoided as closet indexers. Frazzini, Friedman and Pomorski re-ran **the same sample and methodology** and found: high-active-share funds are predominantly benchmarked to small- and mid-cap indices which did poorly over the 1990-2009 sample; "there is no reliable statistical evidence that high-active-share and low-active-share funds have returns that are different from each other"; and "for a given benchmark, there is no reliable statistical evidence that high-active-share funds outperform low-active-share funds". Their conclusion: active share "does not reliably predict performance and … investors who rely on it to identify skilled managers may reach erroneous conclusions" (all quotes *Deactivating Active Share*, FAJ 72(2), 2016, read 2026-08-23, **verified**).

Notably, the original authors had already published the mechanism: "The standard non-benchmark-adjusted Carhart alphas show no significant relationship with active share. The reason behind this is that the benchmark indexes of the highest active share funds have large negative Carhart alphas, while the benchmarks of the lowest active share funds have large positive alphas" (Cremers and Petajisto 2009, **quoted within** *Deactivating Active Share* — a relay, so `partial` per "Verification labels (canonical)"; the origin paper was not read here).

**The vault's position, and it is a position rather than a summary:** active share is a good measure of *how much active risk is being taken* and therefore an excellent input to the question "**is this fee proportionate to the activity**". It is not evidence about skill. Frazzini and co-authors reach the same split themselves — "although active share may not be useful for predicting outperformance, it may well be useful for evaluating costs. Fees matter, and we believe they should be in line with the active risk" (verified). Use it that way and nowhere else:

> **Fee per unit of active risk = ongoing charge ÷ active share.** A fund charging 0.90% with 30% active share is charging roughly 3.0% on the part of the portfolio that is actually active, and paying an index fund's job to be done at thirty times an index fund's price for the other 70%. That is an arithmetic finding, not a forecast, and it is available on day one — which makes it more useful than any alpha estimate the record can support.

This is MOAT-P4 in its fund form: where the output is undifferentiated (the 70% that is the index), the only durable advantage is cost position. And the reflex to assert skill from outcomes with no mechanism named is MOAT-T1 transplanted — a manager's edge asserted from high past returns, high star ratings and high AUM, with no described mechanism by which the edge is generated, is the same defect as a moat asserted from its own outcomes. **Delete the trailing returns from the pitch and see whether an edge is still described.** In most cases nothing is left.

## 7. The base rate

This is the prior any single fund must argue against. It is not an argument that active management is impossible; it is the frequency with which the claim has turned out to be true, and a single fund's evidence must be strong enough to move a prior this unfavourable.

### SPIVA — the survivorship-corrected record

All figures below are from SPIVA scorecards, whose methodology explicitly corrects the three biases that make ordinary peer comparisons flatter than reality (SPIVA U.S. Scorecard Mid-Year 2025, data as of 2025-06-30, PDF extracted and read 2026-08-23, **verified**):

- **Survivorship bias correction:** "SPIVA Scorecards account for the entire opportunity set — not just the survivors — thereby eliminating survivorship bias", using "the opportunity set available at the beginning of the period as the denominator".
- **Apples-to-apples comparison:** each category measured against a benchmark appropriate to it, which is section 1's rule applied at industry scale.
- **Asset-weighted as well as equal-weighted returns**, because equal weighting lets a tiny fund count as much as a very large one.
- Fund returns are **net of fees, excluding loads**.

**Percentage of active US funds underperforming their benchmark** (Report 1a, absolute return):

| Category | Benchmark | 5 yr | 10 yr | 15 yr | 20 yr |
|---|---|---|---|---|---|
| All Domestic Funds | S&P Composite 1500 | 88.32% | 90.31% | 92.52% | 93.81% |
| All Large-Cap Funds | S&P 500 | 86.91% | 85.98% | 88.29% | 91.03% |
| All Mid-Cap Funds | S&P MidCap 400 | 73.54% | 76.84% | 83.72% | 88.81% |
| All Small-Cap Funds | S&P SmallCap 600 | 61.60% | 78.42% | 85.41% | 87.81% |

**And on a risk-adjusted basis it is worse, not better** (Report 1b): All Large-Cap Funds **98.16%** at 15 years and **96.17%** at 20 years; All Domestic Funds **97.71%** and **96.84%**. The commonly heard defence — "they underperform on return but take less risk" — is not supported by the risk-adjusted table, which is the one nobody quotes.

**For a EUR-base investor the numbers are worse still**, and this is the relevant set for this vault (SPIVA Europe Scorecard Mid-Year 2025, Report 1a, data as of 2025-06-30, PDF extracted and read 2026-08-23, **verified**):

| Euro-denominated category | Benchmark | 5 yr | 10 yr |
|---|---|---|---|
| Global Equity | S&P World | 94.75% | **98.22%** |
| U.S. Equity | S&P 500 | 96.35% | 97.21% |
| Europe Equity | S&P Europe 350 | 91.78% | 94.48% |
| Eurozone Equity | S&P Eurozone BMI | 92.54% | 96.31% |
| Emerging Markets Equity | S&P/IFCI Composite | 79.88% | 90.48% |

Global equity is "the largest active category by both the number of funds and collective assets under management" for euro-denominated funds (verified), and it is the worst row in the table over ten years.

### Survivorship — the correction that makes published peer comparisons flatter than reality

Funds that fail disappear, and they disappear *because* they failed. Any peer-group ranking, star rating, or "top decile over 10 years" table computed on funds that exist today has silently deleted the losers from the denominator. The size of the deletion:

- **US equity funds, 10-year survivorship: 63.81%. 15-year: 50.90%. 20-year: 37.29%** (SPIVA U.S. Mid-Year 2025, Report 2, verified). **Over 20 years, roughly five of every eight funds that existed at the start are gone.**
- **European funds are worse:** 10-year survival of **58%** for all equity funds and **54%** for all fixed income, and the report notes these are worse than the extrapolation of recent attrition would predict — "over 10 years, a similar attrition rate would result in survival rates of 62% and 69%, respectively, versus the observed 10-year survival rates of 58% and 54%" (SPIVA Europe Mid-Year 2025, verified).

A ten-year peer comparison built on survivors is therefore a comparison among the ~60% that lived. The 40% that did not are the part of the distribution the fund being evaluated is being asked to prove it is not in.

### Persistence — and the finding that goes past "weak"

Of the **512** domestic equity funds in the **top quartile** as of December 2020, the percentage still in the top quartile was 5.27% after one year and **0.00% after two, three and four years** — a zero that repeats across All Large-Cap (162 funds), All Mid-Cap (65), All Small-Cap (127) and All Multi-Cap (130) (U.S. Persistence Scorecard Year-End 2024, Report 2, data as of 2024-12-31, PDF extracted and read 2026-08-23, **verified**).

Lowering the bar to the **top half** does not rescue it. Over the same five consecutive twelve-month periods: All Domestic Funds **4.21%**, All Large-Cap **2.42%**, All Mid-Cap **0.76%**, All Small-Cap **2.79%**, All Multi-Cap **5.32%** — against the **6.25%** a coin would deliver, a figure the report itself computes as "50%*50%*50%*50% = 6.25%, or 1/16" (same source, verified).

**Persistence is not merely weak; on this measure it is below chance.** One honest qualification that the flattering reading of this statistic omits: a fund that is merged or liquidated cannot remain in the top half, so attrition mechanically pushes the observed rate below the coin-flip benchmark. The correct conclusion is therefore *not* "past winners systematically lose"; it is that **past top-half membership plus a real-world survival hazard together offer less than a coin flip**, which is the number an actual investor experiences. State it that way.

A later edition is reported to show only 0.46% of top-quartile domestic equity funds from 2021 remaining top quartile through December 2025, with zero mid-cap funds doing so (U.S. Persistence Scorecard Year-End 2025, relayed via search-result summaries on 2026-08-23; the S&P primary PDF and article page both returned **HTTP 403** to this session and no secondary article could be fetched either — **unverified**, carried only as directionally consistent with the verified 2024 edition, and to be re-fetched before it is quoted anywhere else).

### The theoretical reason the base rate looks like this

It is not that managers are unskilled. It is **arithmetic**. Fama and French state the constraint: "passive investors get passive returns, that is, they have zero α … This means active investment must also be a zero sum game — aggregate α is zero before costs … After costs, that is, in terms of net returns to investors, active investment must be a negative sum game" (2010, verified; the point is attributed there to Sharpe's arithmetic of active management). Their empirical result matches: the value-weight portfolio of active US equity funds is close to the market portfolio, so its net alpha is negative by about the amount of fund expenses, and "true α in net returns to investors is negative for most if not all active funds, **including funds with strongly positive α estimates for their entire histories**" (verified, emphasis added).

The tail is not empty, but it is thin and it is measured **gross**: with a true-alpha standard deviation of 1.25% a year, "about one-sixth of funds have true gross return α greater than 1.25% per year … and only about 2.4% have true α greater than 2.50% per year" (verified). Those are before-cost numbers. The fee is what stands between the sixth and the investor.

Two live qualifications, recorded so this section is not read as settled: Harvey and Liu (*Journal of Finance* 77(3), June 2022, pp. 1921-1966) argue the Fama-French bootstrap **undersamples** and therefore fails to reject a zero-alpha null even when some funds do generate economically large risk-adjusted returns, while the Kosowski et al. (2006) approach over-rejects (**partial** — abstract and summaries read via search on 2026-08-23, the paper itself not read). And every figure above is *mutual funds*; the base rate for active ETFs, for institutional share classes with materially lower fees, and for non-equity asset classes is a different question this file has not sourced.

## 8. When does the measure lie?

Cases where the headline number misleads, roughly in order of how often they bite.

- **The benchmark is wrong.** The single largest source of false skill findings and false failure findings alike. It is invisible in every output, because every output is denominated in it. Section 1 exists for this.
- **The benchmark is right but the window is not.** A style's good decade is a manager's good decade. Report the benchmark's own return over the window next to the fund's, so the reader can see how much of the story is the asset class.
- **The record is too short and nobody said so.** A three- or five-year alpha reported without a t-statistic is the default state of the industry. Section 3's rule is the answer.
- **The alpha is CAPM alpha presented as factor-adjusted alpha.** Rungs 3-5 of section 2's ladder are where most apparent alpha actually dies, and the vault's script does not run them as of 2026-08-23.
- **The series does not start where you think.** The metrics script aligns to the **common overlapping period** across every ticker passed to it, so adding a young fund to a comparison silently truncates the history of every other one — and truncates away the crisis, which is where the interesting differences live. **Read the stated common period before reading any number computed on it.** This is the same inception-date artifact the wrapper lens documents for the exposure-history script, arriving through a different door.
- **Survivorship, at every level.** In the peer group, in the star rating, in the category average, in the "funds like this returned X" claim. If the source did not say how it handled dead funds, it did not handle them.
- **Backfill and incubation bias.** A firm launches several strategies quietly, publishes the track record of the one that worked, and the published inception date is real while the selection is not. The tell is a fund whose record predates its public availability, or a strategy with a "simulated" or "representative account" segment spliced onto the front.
- **Sharpe on a short-volatility strategy.** Regular modest profits punctuated by occasional crashes is the *definition* of the Sharpe-maximising shape (verified, section 4). A high Sharpe with negative skew and no crisis in the sample is not a risk measurement.
- **Smoothed returns from illiquid or stale-marked holdings.** Understated volatility inflates Sharpe, understates beta, understates correlation and understates drawdown, all at once and all in the flattering direction. The diagnostic is significant **autocorrelation** in the monthly return series, which is not something the metrics script reports as of 2026-08-23. Where holdings are private, unlisted, or thinly traded, treat every risk statistic as a lower bound.
- **Fees measured at the wrong share class.** Institutional and retail classes of the same strategy can differ by more than the entire alpha under discussion. Match the share class actually purchasable — the wrapper lens's ISIN discipline applies here identically.
- **Alpha reported gross.** The only alpha that matters to a holder is net of everything, including the ongoing charge, transaction costs, and the entry spread amortised over the intended horizon.
- **A ratio quoted without its convention.** Sortino without its minimum acceptable return and denominator convention, tracking error without its frequency, Calmar without its window. Each is a different number under a different convention, and the presenter picks.
- **Selection out of a screened universe, priced at a 5% threshold.** If the fund arrived by ranking a database, the t-hurdle is not 1.96. Section 3's third column applies.
- **The manager changed.** A ten-year record under three portfolio managers is three records. Check the tenure of the person running it against the length of the record being quoted — this is PROD-T4's shape (a months-old announcement nobody looked for) applied to a fund.
- **Assets grew.** A strategy that worked at €200m may not work at €8bn, and the record was earned at the smaller size. The past return was generated by a fund that no longer exists in the relevant sense.
- **The multiple-hypothesis problem inside a single fund.** Running six benchmarks, four windows and three ratios and reporting the flattering combination is the same statistical sin as screening a database. Fix the benchmark and the window **before** computing, and report every specification run.

## 9. Decision checklist

Executable mechanically by a fund evaluation. Every figure carries source, date and a verification label per "Verification labels (canonical)" and PROD-P5.

**A. Classify first**
1. Passive or active? If passive, run **section A + the faithfulness half of E only**, and route the cost question to the wrapper lens. Do not run the skill sections on an index tracker.
2. Fee, share class matched to what is actually purchasable, and stated annually.

**B. Benchmark (do this before computing anything)**
3. Holdings file obtained; cap distribution, sector and country weights read.
4. Prospectus benchmark recorded as a **hypothesis**.
5. At least two rival benchmarks identified from the holdings, not from the category label.
6. Regression run against each: beta, R-squared, residual volatility. Best-fitting benchmark named, and the alpha reported under **all** of them.
7. If no clean benchmark exists: blended benchmark constructed from holdings-derived weights, weights written into `valuation.md` so a later run grades the same blend. If no defensible blend exists, **stop and record that skill is not assessable.**
8. Sub-period stability of beta and R-squared checked; style drift reported if present.

**C. Decomposition**
9. `python scripts/fund-metrics.py {TICKER} --benchmark {BENCHMARK} --rf {rate} --years {N}` run; the **common overlapping period the script reports** is read and quoted before any figure from it is used.
10. CAPM alpha, its t-statistic, R-squared and beta recorded together. **Labelled explicitly as CAPM alpha, not factor-adjusted alpha.**
11. Where factor data is obtained (Ken French library, matched to the fund's **region**): FF3, Carhart 4 and FF5 alphas and loadings recorded, each with its t-statistic. Where it is not obtained, the gap is stated, not glossed.
12. Alpha decay across rungs documented. If alpha falls materially while a factor loading is large and strongly significant, the finding is **factor beta at active fees** and it is written in those words.
13. Factors the ladder cannot absorb named (quality, low-vol, liquidity, betting-against-beta) so the residual is not over-claimed.

**D. Statistical power**
14. IR computed; required years for t ≥ 1.96, for 80% power, and for t ≥ 3.0 computed from section 3's formulae and compared to the **actual record length**.
15. Verdict stated in one of exactly three forms: *established at N years*, *suggestive but under-powered*, or **not distinguishable from zero at N years**.
16. Whether the fund was selected out of a screened universe recorded, and the t-hurdle set accordingly.
17. Manager tenure checked against record length. AUM at the start of the record versus today recorded.

**E. Ratios and behaviour**
18. Sharpe, Sortino, IR, Calmar, up/down capture, max drawdown and time-to-recovery recorded, each with its window, its convention and its risk-free rate.
19. Benchmark's **own** Sharpe and drawdown over the identical window recorded alongside, so the comparison is like-for-like.
20. Return skew and any evidence of return smoothing (autocorrelation, illiquid marks) checked before any Sharpe is credited.
21. Count of down periods in the up/down capture calculation recorded.

**F. Holdings-based**
22. Active share computed where holdings and index weights allow; date stamped; repeated over time where the data supports it.
23. **Fee per unit of active risk = ongoing charge ÷ active share** computed and stated. This is the day-one finding that does not need a track record.
24. Turnover and implied transaction costs noted.

**G. Portfolio**
25. Correlation matrix run with the candidate **and** every existing holding in the same call.
26. Correlation recomputed over drawdown sub-periods; both quoted; the gap between them treated as the honest error on any diversification claim.
27. Beta to the core holding computed separately from correlation to it, and both reported.
28. Overlap computed from holdings files, never asserted from names.

**H. Output**
29. Skill verdict written **in its own sentence**, separate from the wrapper verdict and the exposure verdict.
30. Every alpha quoted carries its t-statistic and N, per the rule minted in section 3.
31. Kill switches written per PROD-P3 with threshold, timeframe and an observable that is actually published — candidates: manager departure; AUM crossing a stated level; style drift beyond a stated factor-loading band for two consecutive annual reviews; fee per unit of active risk above a stated ceiling. Note that **an alpha threshold is a bad kill switch**, because section 3 says the measurement will not resolve inside the timeframe any switch would use. Switches on a fund's *skill* case should key on inputs (manager, mandate, size, fee), not on the residual.
32. The passes recorded with the reason and the condition that would change the answer (PROD-P6). The alternative that wins is named with its ISIN.

## Mental-model crossover risks

The assumptions from my other frameworks that **do not transfer here** — and, unusually for this vault, several that transfer from the *company* frameworks and are actively useful, which is worth naming because the wrapper lens's blanket warning does not apply to this file.

- **This is the one fund lens where the company frameworks' machinery partly works, and the wrapper lens's blanket "there is no business to analyse" does not carry over.** An active manager *is* an agent making decisions, so MOAT-T1's shape (an advantage asserted from its own outcomes with no mechanism named), CAPA-P2's shape (credit claimed discipline only against a full cycle of actual data, never against the pitch), and NARC-T2's shape (an operator doubling down on the thesis their career was built on) all have real referents. Import them deliberately. But import them as *shapes*, not as the company checklist — there is still no balance sheet, no capex, no repurchase to grade.
- **The precision inverts twice.** The wrapper lens notes that its numbers are close to knowable and its work is retrieval. Company work is the opposite: wide error bars, judgement carries the weight. **This file is a third thing** — the numbers are computable to arbitrary decimal places and *simultaneously* almost devoid of information, because the estimator is imprecise even when the arithmetic is exact. That combination is uniquely dangerous, because it produces confident-looking output with no confidence behind it. NARC-M2's warning applies directly: an assumption carried in from the last kind of analysis you did is a claim, not a fact.
- **A track record is not a fundamental.** In company work, past financials are *evidence about the business* and are read as such. A fund's past return is evidence about a **random variable with a large standard error**, and per the note already in the `fund-deep-dive` skill, a great trailing return implies a *worse* forward expected return where it came from multiple expansion. Do not read a return history the way a 10-K is read.
- **VAL-T1's habit transfers, and the denominator here is the benchmark.** A stock is not cheap until the denominator is normalised; a fund is not skilled until the benchmark is right. It is the same error in a different variable, and the *habit* of anchoring on a ratio before checking what is underneath it is what carries the damage across.
- **VAL-P3's independence test bites harder here than anywhere.** Sharpe, Sortino, IR, Calmar and up/down capture computed on **one return series against one benchmark** are one lens wearing five hats. They are not five confirming views; they are five transformations of the same numbers, and they will agree with each other by construction. Genuinely independent lenses on a skill claim are: the returns-based regression, the **holdings-based** analysis (different data entirely), and the **fee-versus-active-risk** arithmetic (needs no history at all). Say which of the three you actually have.
- **ASYM-P1 holds and its meaning changes.** Exit only on thesis break, never on price. For an active fund the thesis that can break is the *skill* case, and section 3 says the skill case will almost never break on the evidence inside a normal holding period. That is not a licence to hold forever; it is why the kill switches key on **inputs** — the manager, the mandate, the size, the fee — rather than on the residual.
- **ASYM-P2 does not apply as written**, for the reason the wrapper lens already gives: a diversified fund's downside is a drawdown distribution, not a permanent loss of a single business, and its bear leg comes from the exposure framework. Nothing in this file changes that.
- **A high star rating or a peer-group quartile is a survivorship-corrupted ranking, not a measurement.** "Evidence weighting (canonical)" applies with unusual force: the survivorship-corrected primary (SPIVA, CRSP-based) outranks any commercial rating built on funds that still exist.
- **Do not run the Principles check expecting hits**, per the note already in "Funds tier (canonical)". The themes that genuinely bear on a skill evaluation are PROD (process, kill switches, figure discipline), NARC (narrative and imported assumptions) and VAL (denominators, lens independence). MOAT and CAPA bear only through the *shapes* named in the first bullet, and stretching them into citations is a manufactured finding.

## What I've learned over time

Append-only log.

- 2026-08-23 (framework-bootstrap, v1 — built before any fund was evaluated with it, so read this as a research design rather than as evidence): **the two failure modes that make a fund evaluation worthless are both flattering, which is why they survive review.** A wrong benchmark and an under-powered record both tend to produce a *positive-looking* answer, and neither leaves a trace in the output — every ratio is silently denominated in the benchmark, and no ratio carries its own standard error. That is the structural reason this file puts benchmark selection and statistical power in front of the ratios instead of behind them. The single most persuasive piece of evidence for that ordering is not an argument but a case: the entire published relationship between active share and outperformance turned out to be a benchmark composition effect, replicated on the original authors' own sample, and it had already been sold to the industry as a manager-selection rule (Frazzini, Friedman and Pomorski, FAJ 2016, verified).
- 2026-08-23 (framework-bootstrap, v1 — the number that most changed this file while writing it): **a 2% alpha at 4% tracking error needs about 15 years to reach conventional significance and about 31 years to be reliably detectable, and a five-year record can only establish skill for a manager with a true information ratio near 0.88.** Computed 2026-08-23 from t = IR × √N. Almost every fund marketed on a three- or five-year record is therefore making a claim its data cannot support, and the flattering half of the industry's evidence base consists of exactly those records. The published cross-sectional evidence agrees from the other direction: Fama and French put the average imprecision of individual-fund alpha estimates at 3.4% a year against a true-alpha standard deviation of 1.25% a year (verified), so the typical measurement error is roughly 2.7 times the entire spread of the thing being measured.
- 2026-08-23 (framework-bootstrap, v1 — the base rate, and the version of it that applies to this vault): **for a EUR-base investor the active record is worse than the US headline numbers that dominate English-language commentary.** Euro-denominated Global Equity funds — the largest active category by both fund count and assets — underperformed the S&P World over ten years at a rate of **98.22%**, and euro-denominated U.S. Equity funds underperformed the S&P 500 at **97.21%** (SPIVA Europe Mid-Year 2025, verified). Two supporting facts that make published peer comparisons flatter than reality: European equity funds' observed ten-year survival is **58%**, worse than the extrapolation of recent attrition would predict (verified); and of 512 US top-quartile domestic equity funds as of December 2020, **0.00%** were still top quartile two, three and four years later, while top-*half* five-year persistence came in **below** the 6.25% a coin would deliver (U.S. Persistence Scorecard Year-End 2024, verified). The honest reading of that last one is not that winners systematically lose — it is that attrition is inside the number, and a fund that is liquidated cannot remain in the top half.
- 2026-08-23 (framework-bootstrap, v1 — the finding that is available on day one and needs no track record): **fee divided by active share is the one skill-adjacent number that is knowable rather than estimated.** A fund charging 0.90% with 30% active share is charging about 3.0% on the genuinely active portion and index-fund work at thirty times index-fund prices on the rest. This is the file's version of the wrapper lens's central insight — that the certain, computable term deserves more analytical effort than the uncertain, forecast one — and it survives every objection the statistical sections raise, because it is arithmetic on two disclosed figures rather than an inference from a noisy series. Frazzini and co-authors reach the same split from the other side: active share is useless for predicting performance and useful for evaluating cost (verified).
- 2026-08-23 (framework-bootstrap, v1 — honest gaps carried forward, so the next run does not assume they were closed): six things this build could not do. (1) **No factor regressions were run on any fund**, and `scripts/fund-metrics.py` as contracted delivers CAPM only — rungs 3-5 of the ladder in section 2 are described but not tooled, which means any alpha the vault quotes today is a CAPM alpha and must be labelled one. (2) **No autocorrelation / return-smoothing diagnostic exists** in the script contract, so the illiquid-marks failure mode in section 8 is named but not detectable with current tooling. (3) **The U.S. Persistence Scorecard Year-End 2025 could not be read** — the S&P PDF and article page both returned HTTP 403 and two secondary articles also 403'd, so the 0.46% figure is `unverified` and the verified persistence evidence in this file is the 2024 edition. (4) **The Merton (1980) sampling-frequency result is `unverified`** — two mirrors failed (404 and 403) and it is load-bearing for the "monthly data does not rescue a short record" claim. (5) **Cremers and Petajisto (2009) was read only through its critic**, which is a relay and caps at `partial`; the original should be read before the active-share section is relied on in an argument with someone who has read it. (6) **The whole base rate is mutual funds**; active ETFs, cheap institutional classes and non-equity asset classes are a different question and this file does not answer it. Note the pattern in gaps 3, 4 and 5 — the wrapper lens hit the same HTTP 403 wall on provider pages, and **paywalled or bot-blocked primaries are now a recurring, structural limitation on this vault's fund work rather than an incident.**

## Open questions

- **An alpha-carries-its-t-statistic lint.** Section 3 mints a vault rule that every alpha quoted anywhere carries a t-statistic and an observation count. Right now that is a convention, and PROD-M1's whole point is that a convention depending on memory under pressure is not a fix. Proposed gate: any line in `funds/` containing an alpha figure must carry a t-statistic and an N within the same sentence. Not built; the shape of the regex and the false-positive rate are unexamined.
- **Should `scripts/fund-metrics.py` grow rungs 3-5?** The Ken French library publishes the needed series free, in the right regional variants, at monthly frequency (verified). The argument against is scope creep and a dependency on an external file whose format can change — PROD-T3's shape. The argument for is that section 2 is the analytical core of this file and is currently un-runnable. Unresolved; decide against a real fund rather than in the abstract.
- **What is the right t-hurdle for this vault specifically?** A private investor evaluating one fund he found deliberately is not running a 5,000-fund screen, so the multiple-testing correction that justifies t ≥ 3.0 may be too harsh. But the fund almost certainly reached his attention *because* it performed well, which is a selection effect wearing a disguise. The honest position is that the effective hurdle is somewhere between 1.96 and 3.0 and depends on how the fund was found — and that "how did this fund come to my attention" should therefore be a recorded field in any fund evaluation. Not currently in any template.
- **How much does the drawdown-conditional correlation actually rise?** Section 5 establishes the direction from primary evidence (Longin and Solnik, verified) and has **no magnitude at all** for the exposures this vault holds. Until that is measured, every diversification claim here carries an unquantified error in the unfavourable direction. A candidate first measurement: recompute the correlation matrix over the 2007-2009 and 2020 windows for the portfolio's actual holdings, and record the gap.
- **Is there a principle here?** Two candidate sentences survive the "delete the ticker, the industry and the asset class" test in "Principles routing (canonical)": *a claim that cannot be distinguished from luck with the data available is not evidence, however large the point estimate*, and *when a measure's denominator is chosen by the person being measured, the measure is about the choice.* Both are close to PROD territory and neither has a second instance yet. Parked deliberately, per the orphan-idea rule in `principles/README.md`, rather than forced onto an existing ID.
- **The `frameworks/README.md` "three kinds of file" table now has four kinds**, and this file is the fourth — a lens that is neither an industry playbook, nor an exposure lens, nor the vehicle lens. The registry row and the table update are an **outstanding write-back** owned by whoever runs the next single-threaded pass, per "Concurrent orchestration (canonical)"; it was not applied inline because that file may be being written concurrently.
- **No fund has been evaluated through this lens yet.** Everything above is a design. The first three entries in "What I've learned over time" written after a real evaluation will be worth more than the rest of this file.
