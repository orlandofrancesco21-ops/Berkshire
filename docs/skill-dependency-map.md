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
| `absorb` | nothing strict — resolves, retrieves and grounds its own source. Needs `library/_template.md` + `principles/` to write into | a file in `library/_inbox/`; a queued row in `sources.md` | writes `library/{slug}.md` + index row; mints IDs / appends Voices + Log lines in `principles/`; drafts `journal/_flagged.md` entries on collision with an open thesis; surfaces decisions whose `relied on {ID}@` stamp predates a principle it changed; mirrors `library/sources/` |
| `consult` | `principles/` populated | the named ticker's `thesis.md` Principles check + active flags; `library/` entries; archived sources via `scripts/source-pages.py` | recommends `absorb` for a gap it cannot answer, and queues that gap in `sources.md` |
| `fund-deep-dive` | `frameworks/etf-vehicle-mechanics.md` (universal wrapper lens) + `frameworks/{exposure}.md` (asset-class lens); both required | provider annual report (authoritative for realised cost and tracking difference), KID/KIID, index methodology, holdings file, price/NAV history | writes `funds/{TICKER}/thesis.md` + `valuation.md` + `ic-sheet.md`; writes back to whichever lens learned something; routes the verdict to an allocation, the watchlist, or a pass |
| `compare-within-sector` (deferred) | 3+ `company-deep-dive`s in a single sector + a real felt need for the comparison | — | `decision-log` (the BUY that follows the pick) |

## Reading this table

- **Requires** = the precondition. If absent, the skill should stop and recommend the prior skill, not silently degrade.
- **Optional input from** = the skill works without these but produces better output when they're present.
- **Triggers / recommends** = what the skill suggests as the next step. None of the skills auto-invoke others — the user (or `portfolio-review` as the explicit aggregator) drives sequencing.

## State files in dependency order

Skills coordinate through three shared state files:

- **`portfolio.md`** — written by `decision-log` (BUY/ADD/TRIM) and `post-mortem` (EXIT removes the row); read by `portfolio-review`, `news-triage`, `decision-log`.
- **`watchlist.md`** — written by `company-deep-dive` (on PASS, appends to "Passed"); read by `news-triage`, `watchlist-revisit`, `decision-log`.
- **`sectors/{sector}/companies/{TICKER}/ic-sheet.md`** — the one-page derived decision view, per "IC sheet (canonical)". Written by `company-deep-dive` ONLY, regenerated whole on every run (fresh or refresh) — never appended, carries no log; the audit trail is thesis.md's Update log and the numbers reconcile to valuation.md. Read by anyone who wants the decision without the argument. Mandatory sibling for post-2026-08-22 deep-dives, lint-enforced (presence, required sections, dash ban).
- **`journal/_flagged.md`** — written by `news-triage` (news-derived flags) and `absorb` (a source contradicting an open thesis's reasoning, `next: thesis-check`); modified-in-place by `thesis-check`, `earnings-debrief` and `decision-log` (each resolves flags it acts on); read by `portfolio-review` (prioritizes flagged names) and `decision-log` (surfaces active flags at the moment of decision). Append-only at the line level — an active→resolved rewrite of one line is the single sanctioned in-place edit, and resolved entries stay in place for calibration.

Two further tiers were added 2026-07-28 and follow the same single-writer discipline:

- **`principles/`** — cross-industry principles with permanent IDs. **Voices lines and `evidence:` tags: `absorb` only.** **`My record:` lines: `post-mortem` only** (it is the only skill that sees a realized return). **Log lines:** `absorb`, `post-mortem`, `company-deep-dive` (step 9b) and `watchlist-revisit`, append-only and source-tagged. A rewrite of existing principle text is glance-confirm, never silent. Read by `consult`, `company-deep-dive` (step 3b), `thesis-check`, `decision-log`, `framework-bootstrap`.
- **`library/`** — one distilled entry per absorbed source. **Written by `absorb` only.** Read by `consult` and, through it, by anything asking what a source actually said. `library/_inbox/` and `library/sources/` are gitignored; durability comes from `scripts/mirror-sources.py`, not git.
- **`sources.md`** — the source watchlist and absorption queue. Written by `absorb` (clears rows it consumes, updates Last-absorbed and rotted access paths) and `consult` (appends a `wanted:` row for a gap it could not answer, and commits that single change so the file never sits dirty in a path `absorb` needs clean).

- **`funds/{TICKER}/`** — pooled vehicles (ETFs and the like), per "Funds tier (canonical)". **Written by `fund-deep-dive` only.** Three documents with the same contracts as a company folder: `thesis.md` append-only with the same Update-log headings, `valuation.md` canonical for the fund's return scenarios per VAL-P5, `ic-sheet.md` regenerated whole in the fund section variant. A top-level tier because a fund's peers are other funds tracking the same exposure, not the companies inside it. Identity is the ISIN, not the ticker.

If two skills appear to write to the same field, that's the bug — flag it and route the write through one skill only.
