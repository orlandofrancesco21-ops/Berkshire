# Sources

Where investment knowledge comes from. **Not** `watchlist.md` — that tracks companies; this tracks reading.

**Last swept:** never — created 2026-07-28 (one source absorbed the same day, outside a sweep)

Two tables. **Recurring sources** are the ones worth checking on a cadence (they publish, reliably, and they are worth reading when they do). **Queued for absorption** is everything waiting — things heard about, gaps `consult` could not answer, and recurring items that came due.

## Recurring sources

Tier-1 means a primary artifact by a named practitioner with a long public capital-allocation record — the sources that can promote a principle's evidence tag. Interviews and podcasts are primary only for that speaker's own views.

| Source | Type | Tier | Cadence | Access path | Last absorbed | Notes |
|---|---|---|---|---|---|---|
| Berkshire Hathaway shareholder letters (Buffett) | letter | 1 | annual, late Feb | berkshirehathaway.com/letters/letters.html — direct PDF/HTML, no paywall | never | The full archive back to 1977 is public. Worth absorbing historical ones deliberately, not just the newest: cross-time replication is what promotes a principle. |
| Berkshire annual meeting Q&A | annual-meeting-transcript | 1 | annual, early May | CNBC's Buffett Archive (transcribed); Berkshire posts the webcast | never | Transcript quality varies; cap ASR-derived figures at partial. |
| Howard Marks memos (Oaktree) | memo | 1 | roughly monthly | oaktreecapital.com/insights/memos — direct PDF at `/docs/default-source/memos/{slug}.pdf`, ungated, verified 2026-07-28 | 2025-12-09 ("Is It a Bubble?") | The most concentrated source on cycles and narrative-vs-fundamentals in public writing. |
| Munger — Poor Charlie's Almanack / Daily Journal Q&A | book, transcript | 1 | none (closed corpus) | owner-provided PDF into `_inbox/` | never | Finite and high-density: absorb in chapters, not whole. |
| Damodaran (Musings on Markets) | article | 2 | irregular, ~monthly | aswathdamodaran.blogspot.com | never | Strongest on valuation mechanics and where multiples mislead; usually shows its arithmetic, so figures are often `verified`. |
| Selected fund quarterly letters | letter | 1-2 | quarterly | per-manager IR pages | never | Set `talking-book: yes` — a manager discussing a position they hold is talking a book. Their general reasoning still transfers. |
| Investing podcasts (to be chosen) | podcast | 2 | weekly-ish | transcript site or yt-dlp; owner paste as fallback | never | Pick 1-2 deliberately rather than subscribing broadly. Note the access path that worked — free transcript sites rot fast. |

## Queued for absorption

Rows land here from three places: the owner mentioning something, `consult` hitting a question the vault cannot answer (`wanted:` rows), and `absorb` failing every retrieval rung (`wanted: transcript for …`).

| What | Type | Why queued | Added | Origin |
|---|---|---|---|---|
| Fan-out of "Is It a Bubble?" to NARC / CAPA / MOAT / VAL / ASYM | memo (already absorbed) | Entry is distilled and committed; principle fan-out was deferred because the tier was being audit-corrected the same day. Priority order and what each theme gains are written in the entry's Fan-out section. | 2026-07-28 | absorb (deferred step 5) |
| Buffett/Berkshire letters — start with one from a bubble year (1999 or 2000) | letter | Would put a second independent tier-1 voice against the same cycle material this memo covers, which is what "Maturity and tier-1 sources" needs for any promotion above `emerging`. Cross-time replication is upgrade evidence. | 2026-07-28 | build plan (Phase 7 validation batch) |
| An investing podcast, to exercise the timed-transcript path | podcast | Nothing has tested the gap-partition interval check against a real transcript with native timestamps. The check is replay-tested against the sibling vault's incident but not against a source in this one. | 2026-07-28 | build plan (Phase 7 validation batch) |

## Notes

- **The queue is the honest signal.** If items sit here across three sweeps without being absorbed, the pipeline is too heavy — fall back to the minimal-absorb mode (grounding gate → library entry → index row → commit, with a `fan-out-pending` row left here) rather than letting the queue become a graveyard.
- **A recurring source that never gets absorbed is a lie in this table.** Either absorb it or move it out of Recurring.
- Access paths are recorded because they rot: free transcript sites disappear, IR pages reorganize. When a path breaks, update the row rather than rediscovering it next quarter.
