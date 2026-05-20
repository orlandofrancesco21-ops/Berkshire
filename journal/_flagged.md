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

<!-- Example entries (delete once real flags exist):
- AAPL: flagged 2026-05-01 — 8-K Item 5.02 (CFO departure) → next: thesis-check
- MSFT: flagged 2026-04-28, resolved 2026-04-30 (THESIS INTACT) — was: cluster of 3 downgrades in 10d
-->
