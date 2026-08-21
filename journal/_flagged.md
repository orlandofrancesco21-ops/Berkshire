# Active flags

Shared state file, and **canon for flag state** — anything that mirrors it (a principle's `My record:` line, a review digest) is a copy, and when they disagree this file wins.

Written by `news-triage` (news-derived flags) and by `absorb` (when an external source contradicts the reasoning in an open thesis). Resolved — never deleted — by `thesis-check`, `earnings-debrief`, or `decision-log` when a decision acts on the flagged name. Read by `portfolio-review`, which prioritizes flagged names, and by `decision-log`, which surfaces active flags at the moment of decision.

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
- SNDK: flagged 2026-08-22 — the PASS's revisit trigger fired on 2026-08-05: SanDisk disclosed that the NBM contracts carry price floors and ceilings ($93.9bn minimum contracted revenue at floor pricing, ~1/2 of FY2027 bits, $16.5bn of guarantees; Q4 FY2026 deck p.11, reaffirmed at the 2026-08-13 Investor Day — deck-level disclosure, the audited 10-K says only "fixed and variable components", and the floor LEVEL is undisclosed). By the thesis's own pre-commitment "bear point 5 collapses and the base case moves materially". Also: FY2026 printed GAAP operating income +$12,389M ending the three-year loss streak, $4.5bn of buyback executed in fiscal Q4 at ~15x book, an FY2028-30 model of ~80% GM / 100% excess-cash return was guided, and the price (1,596.08, 2026-08-21) now sits above the old bull-case fair value of 1,560. Zero of eight bull-case kill switches fired. Both docs are stale per "Stale thesis (canonical)" clause (b) → next: company-deep-dive
