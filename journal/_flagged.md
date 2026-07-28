# Active flags

Shared state file written by `news-triage` and read by `portfolio-review`. Entries are added when news-triage produces a FLAG and resolved (not deleted) when the corresponding follow-on skill (`thesis-check` or `earnings-debrief`) runs against the ticker.

## Format

Active flag:
```
- {TICKER}: flagged {YYYY-MM-DD} — {short reason} → next: {thesis-check | earnings-debrief}
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

(populated by `news-triage`; resolved by `thesis-check` or `earnings-debrief`)

- ADBE: flagged 2026-07-17 — Q2 FY26 debrief triggered CEO-transition kill switch (Narayen stepping down, announced 2026-03-12, no successor; CFO Durn exited 2026-06-15); conviction 4 needs re-weighing with the management leg impaired → next: thesis-check
