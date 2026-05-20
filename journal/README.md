# journal/

Append-only, time-stamped context that doesn't belong inside a company's `thesis.md`. Three file types live here, distinguished by filename suffix:

## Filename convention

```
{YYYY-MM-DD}-{type}.md
```

Where `type` is one of:

| Suffix | Written by | Contents |
|---|---|---|
| `triage` | `news-triage` skill | Daily/weekly news-triage output (FLAGs, LOGs, IGNORE counts). |
| `review` | `portfolio-review` skill | Weekly portfolio sweep — ranked action items, metrics, full-sweep table. |
| `decision` | Human (you) | A decision you made: buy / sell / trim / add / no-action with reasoning. Written *at* the time of the decision, not after. |
| `notes` | Human (you) | Free-form weekly reflection. Optional. Useful for capturing things that don't fit anywhere else but you want to be able to grep later. |

Examples:

- `2026-05-18-triage.md` — Monday morning news triage
- `2026-05-20-review.md` — Wednesday portfolio review
- `2026-05-21-decision.md` — "Trimmed ASML 30% on valuation, reasoning: ..."
- `2026-05-24-notes.md` — Weekend reflection on sector positioning

## Rules

- **Append-only by file.** Never edit an old journal entry. If you got something wrong, write a new dated entry that says so.
- **One file per event.** Don't try to consolidate a triage and a decision into the same file — they're different things on different cadences.
- **Decisions are not optional.** Every position change gets a `decision` entry the same day. The decision log is the bridge between research artifacts and actual portfolio history. Without it, you'll wonder why you bought something a year later and have no answer.
- **Skill-written files are also append-only at the file level.** `news-triage` and `portfolio-review` each produce one file per run. Don't manually edit their output to "tidy it up" — that breaks the calibration data.

## What does NOT go here

- Company-specific reasoning → goes in `sectors/{sector}/companies/{TICKER}/thesis.md` Update log
- Framework-level lessons → go in `frameworks/{industry}.md` "What I've learned over time"
- Position metadata → goes in `portfolio.md`

If you're not sure where to write something, the heuristic is: *would I want to find this when researching company X six months from now?* If yes, write it in the company file. *Would I want to find it when reviewing my decisions over Q3?* Write it here.

## Retention

Keep everything. The journal is the raw calibration material for the post-mortem skill and for future framework refinement. Disk is cheap; lost context isn't recoverable.
