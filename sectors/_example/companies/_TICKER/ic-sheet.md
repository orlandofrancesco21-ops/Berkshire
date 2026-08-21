# {TICKER} IC sheet

<!--
CONTRACT (lint-enforced where starred; see "IC sheet (canonical)" in docs/build-plan.md)

*  This file is a DERIVED VIEW. company-deep-dive regenerates it whole on every
   run, fresh or refresh. It is never appended to and it carries no log. The
   audit trail lives in thesis.md's Update log; the numbers reconcile to
   valuation.md, which is canonical per VAL-P5. If this sheet and those files
   disagree, this sheet is wrong.
*  No em-dashes or en-dashes anywhere in this file. Hyphens, colons, periods.
   Short declarative bullets. This is a deliberate style firewall: the deep
   documents argue, this sheet informs.
*  Every figure carries its as-of date. A price without a date is not a number.
*  One page. A senior reader gets verdict, price vs value, the variant
   perception, and the kill switches in under five minutes. If a section needs
   more than its bullet budget, the overflow belongs in thesis.md.
-  Nothing appears here that is not in thesis.md or valuation.md. The sheet
   summarizes the decision; it never introduces new analysis, new numbers, or
   softer adjectives than the source documents earned.
-->

| | |
|---|---|
| Verdict | {BUY x% / WATCH / PASS}, conviction {1-5} |
| Price | {x.xx CCY, YYYY-MM-DD} |
| Fair value | {bear} / {base} / {bull}, probability-weighted {pwfv} |
| Price vs base case | {+/-x%} |
| Reward-to-risk | {base-over-bear from current price, per ASYM-P2} |
| Next dated event | {event, YYYY-MM-DD} |
| Deep docs | `./thesis.md`, `./valuation.md`, both as-of {YYYY-MM-DD} |

## Executive summary

- {What the company is, in one line a non-specialist can parse.}
- {The call and the single number that carries it.}
- {The one thing that would most change the answer, and when it arrives.}
- {3 to 6 bullets total. This section alone must be able to run the IC discussion.}

## Business

- {What it sells, to whom, and how the money is made.}
- {Structural position: share, cost position, what it owns and does not own.}
- {2 to 4 bullets.}

## Bull case

1. {Numbered. Each bullet is one load-bearing claim with its key figure and as-of date.}
2. {...}

## Bear case

1. {Numbered. Steelmanned. The strongest version, not the convenient one.}
2. {...}

## Variant perception: where we differ from the market

<!-- Required section. If the vault's valuation method or conclusion differs
     from how the market prices this name, this section says so plainly and
     defends it. If we agree with the market, say that instead; do not
     manufacture contrarianism. -->

- What the market pays for: {the market's method and what it implies, stated fairly}.
- What we anchor on instead: {our method}.
- Why: {the argument, 1 to 3 bullets, evidence not adjectives}.
- The strongest case against us: {steelman of the market's view}.
- What proves us wrong, and when: {observable + date}.

## Valuation

- Method: {primary lens and why it fits this business; one line on what was rejected and why}.
- Scenarios (reconciles to `./valuation.md`, which is canonical):

| Scenario | Key assumption | Fair value | Probability |
|---|---|---|---|
| Bear | {...} | {...} | {...} |
| Base | {...} | {...} | {...} |
| Bull | {...} | {...} | {...} |

- What the current price embeds: {solved backwards, one bullet}.

## Kill switches, short form

- {Observable + threshold + where it is disclosed. Full definitions live in thesis.md.}
- {...}

## Sizing

- {Current size and the conditions under which it changes. Cite the asymmetry basis.}

## What we do not know

- {The gaps that bound the conviction, stated without hedging language.}
