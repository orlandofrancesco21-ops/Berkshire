---
theme: process-discipline
prefix: PROD
updated: 2026-07-28
---
# Process discipline

**Scope:** The rules that govern my own behaviour rather than any company's — decision logging and its timing, monitoring cadence and the cost of gaps in it, pre-committing evaluation criteria before scheduled events, writing kill switches that can actually be graded and keeping them alive as disclosure changes, and maintaining the calibration record (passes, backfills, old wrong entries). Not here: what to conclude about a business, how to price one, or when to act on a price — those are the other principle files.

## Principles

### PROD-P1 — Pre-commit the criteria before the event

**PROD-P1** — When a thesis-stressing event has a known date (a print, a rate notice, a court milestone), write the confirms-if / refutes-if criteria and translate each kill switch into an observable that event will actually produce, before it happens; a grade produced without pre-committed criteria is hindsight-contaminated and has to open by saying so rather than pass as analysis.
`[evidence: emerging | my record: validated]` (as-of 2026-07-28)

- **Voices:** **agrees** — Owner's own analysis, `README.md` monitoring-cadence table (earnings-prep row) 2026-05 [unverified]: each kill switch becomes a specific print observable and each bull/bear point a confirms-if/refutes-if binary, committed *before* the print (holds when: the event has a known date — an unscheduled shock offers no pre-commitment window, and the honest substitute is to timestamp the reaction and label it reactive rather than to fabricate a prep after the fact)
- **Voices:** **qualifies** — Owner's own analysis, the three backfilled 2026-07-17 earnings-debriefs 2026-07-17 [unverified]: a print can still be graded with no prep on file, directly against the written kill switches, provided the debrief flags the gap in its first line and discounts its own confidence (holds when: falsifiable switches exist; with neither prep nor gradeable switches a debrief is narrative, not calibration, and should not be counted as one)
- **My record:** 2026-07-17 — validated by failure. Three prints landed in the 2026-05 to 2026-07 window (two holdings, one watchlist name) and no earnings-prep one-pager was produced for any of them; all three debriefs were backfilled roughly three to five weeks late and each opens with a process note stating elevated hindsight-contamination risk (`journal/2026-07-17-triage.md`, plus the 2026-07-17 debrief entries in the NKE, ADBE and UNH thesis update logs).
- **Log:**
  - 2026-07-28 — minted from `README.md` monitoring-cadence table (earnings-prep / earnings-debrief rows) and the "no earnings-prep one-pager was ever produced for this print" process notes in the 2026-07-17 debriefs.

### PROD-P2 — Log the decision the same day, or label it reconstruction

**PROD-P2** — Every position change gets its decision record the same day, carrying price, size, the verdicts relied on, and the reasoning as it actually stood; anything written later is reconstruction subject to recall bias, must be labelled as such, and must mark unrecoverable fields unknown rather than filling them with zero or a plausible number.
`[evidence: emerging | my record: validated]` (as-of 2026-07-28)

- **Voices:** **agrees** — Owner's own analysis, `journal/README.md` "Rules" 2026-05 [unverified]: decisions are not optional and are written at the time of the decision, not after — without it you wonder a year later why you bought something and have no answer (holds when: the record exists for calibration, which is always the case here; the same-day rule is about capturing reasoning, so it is not satisfied by a broker confirmation or a tax lot)
- **Voices:** **qualifies** — Owner's own analysis, `journal/2026-07-17-decision.md` backfill note 2026-07-17 [unverified]: a late backfill still beats no record, provided it is labelled reconstruction and downstream reads treat size and cost basis as unknown rather than zero (holds when: the trade facts can still be recovered from a statement; where they cannot, the discipline checklist records the failure instead of inventing the fields)
- **My record:** 2026-07-17 — validated by failure. Two BUYs executed somewhere inside the 2026-05-20 to 2026-07-17 window were never logged at the time; `journal/2026-07-17-decision.md` carries both with trade date, size and price as TBD, both discipline checklists showing same-day logging FAILED, and both reasoning blocks marked reconstruction. Position size and cost basis remain unknown, which is what blocks any position-versus-fair-value read on either name.
- **Log:**
  - 2026-07-28 — minted from `journal/README.md` "Rules" (decisions are not optional) and the backfill note heading `journal/2026-07-17-decision.md`.

### PROD-P3 — Kill switches must be falsifiable and keyed to a forward event

**PROD-P3** — A kill switch is only usable if it names a threshold, a timeframe, and an observable the company actually discloses, and is keyed to something that has not yet happened; audit the written set against current disclosure and the forward calendar every time the thesis is touched. A rewrite for falsifiability must restate, in the same entry, the signal the old switch was watching — so whether the rewrite narrowed the watch is settled against a written record now, not against recollection at the next grading.
`[evidence: emerging | my record: validated]` (as-of 2026-07-28)

- **Voices:** **agrees** — Owner's own analysis, `docs/build-plan.md` "Design rules that are non-negotiable" 2026-05 [unverified]: exit is never triggered by price alone, only by thesis change — which puts the entire weight of the exit decision on whether the written switches can be tested at all (holds when: the switch is meant to drive action; a genuinely qualitative concern is better written as a watch-item than dressed in a fake threshold that will be graded literally later)
- **Voices:** **qualifies** — Owner's own analysis, the 2026-07-17 kill-switch maintenance entries 2026-07-17 [unverified]: rewriting for falsifiability is a maintenance pass, not a thesis change — the underlying signals being watched should survive the rewrite unchanged, and if restating a switch quietly narrows what it watches, that is a thesis edit masquerading as housekeeping (holds when: a disclosed proxy for the original signal exists)
- **My record:** 2026-07-17 — validated. The system audit had to rewrite three UNH switches (one keyed to a CMS rate notice that had already resolved before the thesis was written, one with no threshold or timeframe at all, one open-ended) and three ADBE switches keyed to metrics the company does not separately disclose. Both sets were written at initiation in 2026-05 and none had ever been graded before the audit.
- **Log:**
  - 2026-07-28 — minted from the 2026-07-17 "kill-switch maintenance (system audit)" entries in the UNH and ADBE thesis update logs.
  - 2026-07-28 — audit correction: the qualifies line's counter-condition ("if restating a switch quietly narrows what it watches, that is a thesis edit masquerading as housekeeping") had the same defect as PROD-T2's — a judgment call at rewrite time with nothing to test it against. Added one falsifiable clause to the statement: the rewrite must restate the original signal in the same entry, so a maintenance entry that does not is in violation on its face. This was the second item under the "unviolatable hedge" finding, which named only PROD-T2 explicitly; picked on structure, not on the file conceding it.

### PROD-P4 — Correct by appending, never by editing

**PROD-P4** — When an entry turns out to be wrong, append a new dated entry that says so and leave the original standing; the wrong entry is the only surviving record of how the reasoning actually ran, and overwriting it destroys the calibration data the correction exists to create.
`[evidence: emerging | my record: untested]` (as-of 2026-07-28)

- **Voices:** **agrees** — Owner's own analysis, `docs/build-plan.md` "Design rules that are non-negotiable" and `journal/README.md` "Rules" 2026-05 [unverified]: records are append-only by file — if you got something wrong, write a new dated entry saying so; old thinking matters (holds when: the artifact is a record of reasoning; skill-written outputs are append-only at the file level too, so "tidying up" a triage or review output is the same violation)
- **Voices:** **qualifies** — Owner's own analysis, the 2026-07-17 system audit 2026-07-17 [unverified]: appending is not sufficient where the stale text is what another skill reads — a wrong figure inside a thesis body needs the dated correction *and* a pointer at the read site, or the append is archaeology while the error stays live (holds when: another file or skill consumes the value; for pure narrative reasoning the append alone is enough)
- **My record:** 2026-07-28 — untested in the way that matters: nothing in the vault has yet been wrong enough to create the urge to quietly fix it. The 2026-07-17 audit did append rather than edit, including a same-day correction carried as an appended paragraph inside the ADBE kill-switch-maintenance entry — but appending was cheap there, since the text being corrected was hours old.
- **Log:**
  - 2026-07-28 — minted from `docs/build-plan.md` "Design rules that are non-negotiable" (first rule) and `journal/README.md` "Rules" (append-only by file).

### PROD-P5 — A market number without its snapshot is not evidence

**PROD-P5** — Any price, multiple, or market-derived figure written down carries the date, time, and currency it was pulled at, and any news reference carries its publication date; an undated number silently becomes an anchor that outlives the conditions that produced it.
`[evidence: emerging | my record: untested]` (as-of 2026-07-28)

- **Voices:** **agrees** — Owner's own analysis, `docs/build-plan.md` "Price and data sourcing (canonical)" 2026-05 [unverified]: prices come from a named source and every written entry snapshots date, time and currency — a price without a timestamp is not evidence (holds when: the figure does work in a decision, a band, or a comparison; a rounded price used as narrative colour still needs the date but not the minute)
- **My record:** 2026-07-28 — untested: the vault's own entries mostly comply, and no decision here has yet been shown to go wrong from an undated figure. The closest live instance is a watchlist entry trigger written at initiation against a fair value that has since drifted, which is a stale-anchor problem rather than a missing-snapshot one — so this rule has not yet been paid for.
- **Log:**
  - 2026-07-28 — minted from `docs/build-plan.md` "Shared rules" → "Price and data sourcing (canonical)".

### PROD-P6 — Log the passes, with a reason and a revisit trigger

**PROD-P6** — Every name evaluated and declined gets a dated row with the reason for passing and the condition that would make it interesting again, and that table gets swept on a fixed cadence; the passes are the larger half of the decision record and the only way to learn whether the reasons you decline on are any good.
`[evidence: emerging | my record: untested]` (as-of 2026-07-28)

- **Voices:** **agrees** — Owner's own analysis, `README.md` "Workflow" step 3 and `watchlist.md` "Passed (with reason)" 2026-05 [unverified]: names that don't make the cut get logged with the reason, because pattern recognition compounds on what you historically pass on, and the same file's monitoring-cadence table puts a quarterly `watchlist-revisit` sweep over that table (holds when: the pass followed real work — logging every name glanced at and dropped floods the table and destroys the signal the sweep is looking for; when the revisit condition names an observable and not only a price level, since a price-only trigger is exactly what goes stale as the fair value it was derived from drifts, see ASYM-T1; and when the sweep stays a check on whether the pass reason still holds rather than a standing invitation to re-litigate — a pass that has to be re-defended every quarter quietly becomes a reason to buy)
- **My record:** 2026-07-28 — untested and, so far, unpracticed: the `watchlist.md` "Passed (with reason)" table has no rows. The one researched-and-declined name to date sits under "Researched, waiting for entry" with a price trigger instead, and the quarterly sweep of the passed names has never run. The calibration dataset this rule exists to build does not yet exist.
- **Log:**
  - 2026-07-28 — minted from `README.md` "Workflow" step 3 and the `watchlist.md` "Passed (with reason)" section header, plus the quarterly `watchlist-revisit` row of the `README.md` monitoring-cadence table for the fixed-cadence sweep clause. It belongs here because it is a rule about maintaining my own record, not about when to act on a price. [Corrected 2026-07-28: this line previously read "Extracted under the asymmetry theme in the seed brief and moved here". No move ran — the asymmetry twin was minted independently and stayed live, so the line documented a de-duplication that had not happened.]
  - 2026-07-28 — corrected the mint line above, which falsely claimed the rule had been moved out of the asymmetry theme. Editing it rather than only appending is the narrow exception PROD-P4 does not cover: the sentence was not wrong reasoning worth preserving, it was a false statement about the vault's own structure, and leaving it standing would have kept telling a future reader the duplicate was already resolved.
  - 2026-07-28 — audit merge: the asymmetry file's third principle ordinal (prefix ASYM, principle number 3 — "the pass log is calibration data") is retired as a duplicate of this item — same rule, minted the same day from the identical locator pair, with near-identical my-record text. Two permanent IDs for one behaviour could have been cited by a thesis Principles check as two independent supports, manufacturing exactly the false consensus this vault exists to prevent. This item survives because it is behavioural and already carried the fixed-cadence sweep the asymmetry version omitted. Both of the retired item's distinct conditions are folded into the agrees line above: the revisit trigger must be an observable rather than only a price level, and the pass log stays a record rather than a queue. The second was carried across deliberately though the finding named only the first — dropping a genuine counter-condition during a merge is the "narrowing what it watches under cover of housekeeping" failure PROD-P3 warns about.

## Mental models

### PROD-M1 — A repeated process failure is a design failure

**PROD-M1** — When the same lapse recurs, read it as evidence that the step depends on remembering it under pressure, and move the step into an opinionated default that runs by itself; resolving to try harder is not a fix, and a discipline that lives only as intention is the first thing dropped in a drawdown.
`[evidence: emerging | my record: mixed]` (as-of 2026-07-28)

- **Voices:** **agrees** — Owner's own analysis, `docs/build-plan.md` "Design rules that are non-negotiable" (fourth rule) and "Voice and structure for new skills" 2026-05 [unverified]: skills should be opinionated — encode the discipline into the tool so future-me cannot quietly drop it under emotional pressure (holds when: the discipline is general enough to encode; over-encoding converts judgment calls into box-ticking, which is why a stored principle stays advisory and never gates a decision — see "Principle authority (canonical)" in `docs/build-plan.md`)
- **Voices:** **qualifies** — Owner's own analysis, `README.md` "Keeping the rituals honest" 2026-07 [unverified]: encoding a discipline inside a tool does nothing if nothing makes the tool run — a periodic ritual needs a trigger outside my attention, such as booking the next print date the day the previous debrief lands (holds when: the step is periodic; event-driven steps can instead be encoded as a precondition inside the skill that consumes their output)
- **My record:** 2026-07-17 — mixed. Every discipline that ran behaved as designed: the debriefs graded switches against their letter and intent, and the decision log surfaced its own same-day failure as a checklist line rather than hiding it. What the encoding could not do was start itself — the skills existed for the whole eight-week silence while the journal stayed empty. Encoded discipline is necessary here and demonstrably not sufficient.
- **Log:**
  - 2026-07-28 — minted from `docs/build-plan.md` "Design rules that are non-negotiable" (fourth rule), restated as a lens rather than the seed's rule form, with the counter-evidence taken from `README.md` "Keeping the rituals honest".

## Traps

### PROD-T1 — Burst-then-silence

**PROD-T1** — The monitoring failure mode is rhythm, not laziness: a heavy research sprint is followed by silence, and the silence is where written triggers go un-actioned — so read process health off the elapsed time since the last dated entry, never off how much work the last sprint produced.
`[evidence: emerging | my record: validated]` (as-of 2026-07-28)

- **Voices:** **agrees** — Owner's own analysis, `README.md` "Keeping the rituals honest" 2026-07 [unverified]: the pattern to guard against is heavy research sprint then nothing until something hurts; the minimum viable cadence is a twice-weekly triage whose usual output is "nothing material", a review every Monday even on a tiny book, prep before every print, and a quarterly watchlist sweep (holds when: positions or live entry triggers exist; a fully cash book with an empty watchlist genuinely needs no cadence, and running the ritual anyway is how it becomes theatre)
- **My record:** 2026-07-17 — validated, with a measured cost. Roughly eight weeks of silence from 2026-05-08 to 2026-07-17 (journal empty, two revisit dates blown through — `README.md` "Keeping the rituals honest", 2026-07, unverified) let a holding trade through its own written ADD band on what the debrief describes as a ~20% drawdown, with no debrief on file; the debrief records it as an un-actioned ADD signal flagged for calibration and explicitly not actioned retroactively (ADBE 2026-07-17 earnings-debrief, "Price reaction", unverified against a price series).
- **Log:**
  - 2026-07-28 — minted from `README.md` "Keeping the rituals honest" and the "Price reaction" paragraph of the ADBE 2026-07-17 earnings-debrief. The seed candidate's separate clause about "nothing material today" being the cheap two-minute output is folded into the agrees line rather than kept as its own item.

### PROD-T2 — A mis-specified threshold fires a false signal

**PROD-T2** — A switch can breach its own letter while the business improves, or sit silent while it deteriorates, whenever the threshold was written against the wrong seasonality or the wrong base; grade letter and intent separately, and where they disagree, recalibrate before the next event instead of acting on the letter. Recalibration is only available against a discriminator written down in advance: when the switch is set, name the observable that would show the threshold was mis-specified — a seasonality or base-effect artefact, identifiable without reference to which way the surprise went — and the observable that would instead show the business genuinely changing. A discriminator produced for the first time at grading is not a recalibration case, and the switch stands as written.
`[evidence: emerging | my record: validated]` (as-of 2026-07-28)

- **Voices:** **agrees** — Owner's own analysis, the 2026-07-17 earnings-debrief kill-switch gradings 2026-07-17 [unverified]: a ratio ceiling set without reference to which quarter is seasonally lowest, and a margin threshold written against a revenue base inconsistent with the disclosed earnings seasonality, both fire mechanically on an improving business — do not let a mis-specified threshold generate a false kill signal (holds when: the divergence is traceable to the specification; when letter and intent disagree because the business genuinely changed, that is the switch working and "recalibrating" it is rationalization)
- **My record:** 2026-07-17 — validated. Two UNH bull-side switches graded neutral on intent while breaching, or being arithmetically certain to breach, their letter: a medical-cost-ratio ceiling confounded by quarterly seasonality, and an operating-margin threshold written against a revenue base the company's disclosed earnings profile cannot reach. Both were written at initiation on 2026-05-21 and the defect surfaced only at the first grading, eight weeks later — see the 2026-07-17 earnings-debrief in `sectors/us-managed-care-and-health-services/companies/UNH/thesis.md`.
- **Log:**
  - 2026-07-28 — minted from the kill-switch grading section of the UNH 2026-07-17 earnings-debrief.
  - 2026-07-28 — audit correction: the counter-condition (recalibrate a mis-specified threshold, never one whose breach is the business changing) named the distinction without giving a test, which left the trap able to excuse any inconvenient fire — a gap the file's own Open questions already conceded. Added one falsifiable clause: the discriminating observable must be written when the switch is set, so a switch with no pre-registered discriminator cannot be recalibrated at all. The rule itself is unchanged.

### PROD-T3 — The observable dies before the trigger does

**PROD-T3** — Companies consolidate segments and retire metrics, which silently kills any trigger keyed to a disclosure rather than to a signal; every metric-keyed switch needs a named fallback proxy, and the disappearance of a metric management used to promote is itself information, not a gap to route around.
`[evidence: emerging | my record: validated]` (as-of 2026-07-28)

- **Voices:** **agrees** — Owner's own analysis, the 2026-07-17 kill-switch maintenance and its same-day correction 2026-07-17 [unverified]: two observables chosen in a morning falsifiability pass were already dead on arrival because the segment they keyed on had been consolidated two quarters earlier, and had to be corrected the same day against the surviving disclosures (holds when: the signal you care about survives the disclosure change and a proxy exists; where no proxy does, say so and re-weigh conviction rather than keeping a switch that can never fire)
- **My record:** 2026-07-17 — validated within hours. The audit rewrote ADBE's bull-case switches for falsifiability in the morning against segment-level ARR metrics, and the debrief run the same day found those metrics discontinued since Q1 FY26; one switch is graded "NOT GRADEABLE AS WRITTEN" and the entry carries the fix as an appended same-day paragraph. A surviving clause now treats the absence of a previously-touted disclosure for two or more quarters as a trigger in its own right.
- **Log:**
  - 2026-07-28 — minted from the same-day correction in the 2026-07-17 kill-switch-maintenance entry and the "dead on arrival" / "NOT GRADEABLE AS WRITTEN" gradings in the ADBE thesis update log.

### PROD-T4 — The thesis can be stale on the day it is written

**PROD-T4** — Depth of work is no protection against a months-old announcement nobody looked for: sweep leadership changes and corporate events across at least the trailing two quarters before finalizing a thesis, because a conviction leg resting on facts that were already public and already false contaminates every decision taken downstream of it.
`[evidence: emerging | my record: validated]` (as-of 2026-07-28)

- **Voices:** **agrees** — Owner's own analysis, `journal/2026-07-17-decision.md` calibration note on the second backfilled BUY 2026-07-17 [unverified]: the thesis was written without registering a CEO-transition announcement made two months earlier, and named as successor an executive who left weeks later — the buy inherited that blind spot (holds when: the missed fact bears on a conviction leg; not every unnoticed press release is a process failure, and treating it as one produces a sweep so wide it stops getting run)
- **My record:** 2026-07-17 — validated. The management-quality section of the ADBE thesis written 2026-05-20 described the CEO as incumbent with succession merely a watch-item, two months after a transition announcement dated 2026-03-12, and named the CFO as successor-in-waiting; that CFO left on 2026-06-15 (both dates per the ADBE 2026-07-17 earnings-debrief citing an Adobe leadership release and the Q2 print, unverified — the primary filings have not been read here). The debrief calls the section stale on the day it was written; it was one of the three legs of a conviction 4, and the decision entry records that the BUY inherited it.
- **Log:**
  - 2026-07-28 — minted from the CEO-transition kill-switch grading in the ADBE 2026-07-17 earnings-debrief and the ADBE calibration note in `journal/2026-07-17-decision.md`.

## Open questions

- Every item here rests on the owner's own analysis of his own record. That is the correct hierarchy for claims about my process under the evidence-weighting rule in `docs/build-plan.md`, but it also means nothing in this file has been pressure-tested against how disciplined investors actually run cadence, decision journals, and pass logs. The first absorbed letter, memo, or interview touching investment process routes here.
- What is the honest promotion test for `my record: validated` when a rule has only ever been observed *failing*? PROD-P1 and PROD-P2 carry validated on the strength of documented costs, not of the rule working — weaker evidence than a rule observed on both sides, and the tag does not currently distinguish the two.
- PROD-T2's counter-condition (recalibrate a mis-specified threshold, but never a threshold whose breach is the business changing) now has a procedural test — the discriminator must be pre-registered when the switch is set — but that only closes the escape hatch prospectively. Every switch currently written was set without one, so the whole existing set is un-recalibratable under the rule as it now stands. Whether the honest answer is to grandfather them, or to pre-register discriminators for the existing switches at the next maintenance pass, is unresolved.
- The minimum viable cadence in `README.md` was written after the failure it describes and has not yet survived a quarter. Untested: whether a twice-weekly triage would have caught the un-actioned ADD band at all, or whether a price-level alert is the only thing that catches a band breach between rituals.
- No rule here covers what happens when a *sequence* of small process debts compounds — a missed prep leading to a late debrief leading to an ungraded switch. Each item above is written as an isolated lapse, which is not how the eight-week silence actually unfolded.
