# docs/

Design notes for the system itself — not investing notes. Read these when onboarding (yours or a fresh Claude session) or before making structural changes.

| File | What it contains |
|---|---|
| [`build-plan.md`](build-plan.md) | The handoff brief: design intent, what's built, gaps in priority order, MCPs needed, scope boundaries, and the canonical Shared rules (e.g. the stale-thesis definition) that more than one skill depends on. |
| [`skill-dependency-map.md`](skill-dependency-map.md) | What each skill requires, optional inputs, and what it triggers next. Documents the three shared state files (`portfolio.md`, `watchlist.md`, `journal/_flagged.md`) and the writer-skill for each. |

## Conventions for `docs/`

- This folder is for **system design** (how the skills coordinate, what rules they share, why something was built or deferred). Investing knowledge lives in `frameworks/` and `sectors/`.
- Files here are append-only at the section level. If a Shared rule changes, update it in place (and document the change in the file's own history) — don't fork it across multiple definitions.
- Keep this index up to date when adding new files.
