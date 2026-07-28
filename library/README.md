# Library

One distilled entry per absorbed external source. **The entry is the citable record; the raw source is a retrieval surface.**

Written only by `absorb`. Nothing else writes here — an entry appears when a source has passed the grounding gate, been distilled with locators, and had its takeaways fanned out to whichever principle themes it actually touches.

## How material gets in

| Input | What to do |
|---|---|
| A file (PDF, saved article, transcript, notes) | Drop it in `_inbox/` and say "absorb" |
| A URL | "absorb {url}" |
| Something you heard but don't have | Say so — `absorb` with no arguments offers to queue it in [../sources.md](../sources.md) |

One source per run, end to end. Never batched: a batch is where the completeness pass quietly degrades.

## Index

| Entry | Type | Author | Published | Themes | One-line |
|---|---|---|---|---|---|
| [Is It a Bubble?](marks-2025-12-is-it-a-bubble.md) | memo | Howard Marks (Oaktree) | 2025-12-09 | NARC, VAL, CAPA, MOAT, ASYM | A cycle specialist's anatomy of how bubbles form, why the good ones are still bubbles, and why a transformative technology and a profitable investment are different questions. |

Every entry needs exactly one row here and vice versa; the lint enforces the bijection, so a hand-added row pointing nowhere blocks the commit.

## Verification labels

Canonical definitions live in [../docs/build-plan.md](../docs/build-plan.md) ("Verification labels"). In short:

- `verified` — stated plainly in the primary artifact whose text was actually read.
- `partial` — partly backed; also the **cap** for relays, secondary summaries, and auto-generated transcripts.
- `unverified` — memory or unconfirmable, labelled inline next to the figure.

Never invent or interpolate a figure. Unconfirmed means attribute the claim, not the number. An upgrade happens only by re-fetching the original, recorded as a dated line — and a vault entry is never evidence for upgrading another vault entry.

## `_inbox/` and `sources/` are gitignored

`_inbox/` is the drop folder. `sources/` is the archive: the canonical extracted `.txt` (immutable — locators address it) plus the original binary, sharing the entry's slug.

Neither is committed. Third-party material carries copyright and the text is bulky, so **durability comes from the mirror, not from git**: `python scripts/mirror-sources.py` copies the archive to `$BERKSHIRE_SOURCE_MIRROR`, which must be a personal location. There is deliberately no OneDrive fallback — on this machine that variable points at the employer's tenant, and this vault is private by design.

**Also exclude both folders in Obsidian** (Settings → Files & Links → Excluded files). Gitignore hides them from git, not from the quick switcher, search, or graph — a 60,000-character transcript in the search index makes the vault worse to use. Repeat this step on any new machine.

## Reading an entry

`## Takeaways` is what the source actually gives you, each line locator-addressed so it can be checked. `## Not captured` is the honest inventory of what was skipped and why — read it before concluding the source has nothing on a topic. `## Fan-out` says what changed in `principles/`, so an entry that moved nothing is visible as such.

To go deeper than the entry, follow the deep-retrieval ladder in [../CLAUDE.md](../CLAUDE.md) — and remember that raw text from `sources/` is a pointer, never a citation.
