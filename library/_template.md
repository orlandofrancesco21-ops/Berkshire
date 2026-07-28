---
title: {exact title of the source}
type: {letter|memo|annual-report|filing|book|article|podcast|interview|annual-meeting-transcript|dataset|paper}
author: {who wrote or spoke it}
published: {YYYY-MM or YYYY-MM-DD}
retrieved-from: {URL, or "owner-provided" for material dropped in _inbox/}
retrieval-path: {which rung of the ladder actually worked — so a rotted path is visible next time}
source-span: {"0:00-58:03" for timed audio | "pp.1-24" for documents | untimed}
archive: {sources/{slug}.txt, sources/{slug}.pdf — or "none — {why, and the re-fetch path}"}
extraction: {tool + date, e.g. "pdf-extract.py (PyMuPDF) 2026-07-28" — provenance for every locator below}
tags: [{principle theme slugs this source actually touches}]
talking-book: {yes|no}
---

**One-line:** {one sentence — becomes the index row in README.md}

**Why it matters to my process/portfolio:** {1-3 lines. Not a summary — the reason this is in the vault. If you cannot state it, the source probably should not have been absorbed.}

<!--
SCHEMA NOTES (starred items are lint-enforced; canon in docs/build-plan.md
"Distillation completeness", "Verification labels", "Source archive and deep retrieval")

*  Every Takeaways bullet carries a (locator) AND a [verification tag].
*  `## Not captured` is REQUIRED and must be non-empty.
*  `source-span` is required for podcast/interview/annual-meeting-transcript.
   Timed spans get interval-checked: takeaway + leftover locators must cover the
   span with no unaccounted stretch over ~6 minutes. Use `untimed` when the
   transcript has no native timestamps — then use paragraph/section locators and
   say why in Not captured. Never invent timestamps to satisfy the check.
*  `archive:` filenames share this entry's slug (1:1:1: entry / .txt / .pdf).

SWEEP FIVE KNOWLEDGE TYPES, not just claims:
   claims/theses · METHODS · distinctions/profiles · heuristics · texture
   "Store the move, not the label": a takeaway naming a framework or sequence
   without its actual steps is unfinished. The steps ARE the knowledge.

talking-book: yes when the author is discussing a position they hold. Their claims
about that specific name are talking a book — cap at directional, and say so in the
takeaway. Their general reasoning is still usable.
-->

## Takeaways

- {The claim, method, or distinction — with its conditions, not just its headline} ({locator}) [{verified|partial|unverified}]
  - *Texture:* {one line — the concrete mechanism or example that makes this copyable rather than a slogan}

## Not captured

- {segment} ({locator}) — {why it was skipped: colour, off-topic, already held, promotional}

## Cites

{Claims this source RELAYS from somewhere else. Name the origin; a relay caps at
`partial` no matter how confident the speaker sounds. Delete the section if the
source relays nothing.}

- {claim} — originally from {origin, year} ({locator here}) [partial]

## Fan-out

{What this source changed in `principles/`, written by absorb. Makes the entry
auditable: an entry that changed nothing anywhere is either a weak source or a
weak absorb, and either way that should be visible.}

- {PREFIX}-{K}{n} — {new item minted | Voices line added | evidence tag changed from X to Y}
- {or: "no principle updates — {why: already held, too company-specific, below the bar}"}
