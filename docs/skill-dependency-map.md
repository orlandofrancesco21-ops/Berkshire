# Skill dependency map

What each skill needs before it can run, what optional inputs it consumes, and what it recommends / triggers afterward. Use this when onboarding (yours or a fresh Claude session) — saves repeated discovery from skill text.

| Skill | Requires | Optional input from | Triggers / recommends |
|---|---|---|---|
| `evaluate` | nothing — checks and bootstraps prerequisites internally | — | runs `framework-bootstrap` (if missing) + `sector-primer` (if missing) + `company-deep-dive` end-to-end. Recommends hand-edit pass on auto-generated framework. |
| `framework-bootstrap` | — (creates `frameworks/{industry}.md` from `_template.md`) | — | `sector-primer` |
| `sector-primer` | `frameworks/{industry}.md` exists | — | `company-deep-dive` on top candidates |
| `company-deep-dive` | `frameworks/{industry}.md` + `sectors/{sector}/primer.md`. If framework has a "Sub-sector navigator" section, also requires `frameworks/{sub-sector}.md` (umbrellas aren't decision-grade) | — | writes thesis + valuation; on PASS appends to `watchlist.md`; appends to framework's "What I've learned" |
| `valuation-check` | thesis + valuation on file (a prior `company-deep-dive`) | — | `thesis-check` (if REVIEW), `company-deep-dive` (if thesis is stale per canonical rule), `decision-log` (if user acts on the result) |
| `thesis-check` | thesis on file | `journal/_flagged.md` flags written by `news-triage` | `company-deep-dive` (if REVIEW); marks resolved flags in `journal/_flagged.md` |
| `portfolio-review` | `portfolio.md` populated | `journal/_flagged.md` (prioritizes flagged names) | runs `thesis-check` + `valuation-check` internally; writes digest to `journal/{date}-review.md` |
| `news-triage` | `portfolio.md` + `watchlist.md` populated | — | recommends `thesis-check` or `earnings-debrief`; writes new flags to `journal/_flagged.md` and per-day file to `journal/{date}-triage.md` |
| `earnings-prep` | thesis + valuation on file | upcoming earnings calendar | `earnings-debrief` after the print |
| `earnings-debrief` | thesis on file (and ideally an `earnings-prep` entry to grade against) | — | `thesis-check` or `company-deep-dive` depending on verdict; marks resolved flags in `journal/_flagged.md` |
| `post-mortem` | thesis + valuation on file (a closed position) | — | appends to framework's "What I've learned" (post-mortem tag); writes `archive/{exit-YYYY-MM}-{TICKER}.md` + `CLOSED.md` marker; removes row from `portfolio.md` |
| `decision-log` | nothing strict — reads thesis if present and warns if not | recent `journal/{date}-review.md` or `journal/{date}-triage.md`; `journal/_flagged.md` | `post-mortem` (if action was SELL or EXIT); updates `portfolio.md` for BUY/ADD/TRIM |
| `watchlist-revisit` | `watchlist.md` populated (specifically "Passed" and "Researched, waiting for entry" sections) | — | `company-deep-dive` refresh on FLAGGED names; `valuation-check` + `decision-log` on TRIGGER FIRED names |
| `compare-within-sector` (deferred) | 3+ `company-deep-dive`s in a single sector + a real felt need for the comparison | — | `decision-log` (the BUY that follows the pick) |

## Reading this table

- **Requires** = the precondition. If absent, the skill should stop and recommend the prior skill, not silently degrade.
- **Optional input from** = the skill works without these but produces better output when they're present.
- **Triggers / recommends** = what the skill suggests as the next step. None of the skills auto-invoke others — the user (or `portfolio-review` as the explicit aggregator) drives sequencing.

## State files in dependency order

Skills coordinate through three shared state files:

- **`portfolio.md`** — written by `decision-log` (BUY/ADD/TRIM) and `post-mortem` (EXIT removes the row); read by `portfolio-review`, `news-triage`, `decision-log`.
- **`watchlist.md`** — written by `company-deep-dive` (on PASS, appends to "Passed"); read by `news-triage`, `watchlist-revisit`, `decision-log`.
- **`journal/_flagged.md`** — written by `news-triage` (new flags); modified-in-place by `thesis-check` and `earnings-debrief` (resolve flags); read by `portfolio-review` (prioritizes flagged names) and `decision-log` (surfaces active flags at moment of decision). Append-only at the line level — resolved entries stay in place for calibration.

If two skills appear to write to the same field, that's the bug — flag it and route the write through one skill only.
