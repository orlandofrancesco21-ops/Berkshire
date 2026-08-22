# Active flags

Shared state file, and **canon for flag state** — anything that mirrors it (a principle's `My record:` line, a review digest) is a copy, and when they disagree this file wins.

Written by `news-triage` (news-derived flags) and by `absorb` (when an external source contradicts the reasoning in an open thesis). Resolved — never deleted — by `thesis-check`, `earnings-debrief`, or `decision-log` when a decision acts on the flagged name, or by `company-deep-dive` when a refresh discharges a flag that routed to it. Read by `portfolio-review`, which prioritizes flagged names, and by `decision-log`, which surfaces active flags at the moment of decision.

## Format

Active flag:
```
- {TICKER}: flagged {YYYY-MM-DD} — {short reason} → next: {thesis-check | earnings-debrief | valuation-check | company-deep-dive | owner-review}
```

Resolved flag (preserved for calibration):
```
- {TICKER}: flagged {YYYY-MM-DD}, resolved {YYYY-MM-DD} ({verdict}) — was: {short reason}
```

## Rules

- Append-only at the file level. Skills may *update* a line (active → resolved) but must not delete it.
- Multiple flags on the same ticker over time are kept as separate lines, not collapsed.
- Filename starts with `_` so it sorts to the top of `journal/` listings.
- This file is committed to the repo so flag state travels across machines.

## Active and resolved flags

(populated by `news-triage` and `absorb`; resolved by `thesis-check`, `earnings-debrief` or `decision-log`)

`next: owner-review` means no skill can dispose of it — it needs a human judgment call.

- ADBE: flagged 2026-07-17 — Q2 FY26 debrief triggered CEO-transition kill switch (Narayen stepping down, announced 2026-03-12, no successor; CFO Durn exited 2026-06-15); conviction 4 needs re-weighing with the management leg impaired → next: thesis-check
- NKE: flagged 2026-07-28 — recorded reward-to-risk in thesis.md "Conviction" (~2:1) does not reconcile with its own valuation.md scenario table, which yields roughly 1.3:1 on base-over-bear from the price of record; the paragraph quoted a restated target band rather than the table. A sizing-basis discrepancy, not a thesis break — but the starting-size decision rested on the flattered figure. Surfaced by the ASYM-P2 basis fix, which standardized how the ratio is computed → next: valuation-check
- ADBE: flagged 2026-07-28 — recorded reward-to-risk in thesis.md "Conviction" (3:1 to 4:1, read as a step-up case) does not reconcile with its own valuation.md scenario table, which yields roughly 2.5:1 on base-over-bear; the numerator was widened toward the bull case. On the basis the vault now standardizes on this clears the starting threshold only, not the step-up threshold → next: valuation-check
- SNDK: flagged 2026-08-22, resolved 2026-08-22 (company-deep-dive refresh: PASS re-affirmed, conviction 1→2, FV re-based to $475/$875/$2,200 PWFV ~$1,090, entry conditions rewritten in watchlist.md) — was: the PASS's revisit trigger fired 2026-08-05 (NBM price floors disclosed, >50% of FY2027 bits, $93.9bn minimum; floor LEVEL still undisclosed and the deck's $16.5bn guarantees resolve to ~$7.7bn identifiable in the audited 10-K); both docs stale per "Stale thesis (canonical)" clause (b)
