---
name: absorb
description: The ingestion path — turns ONE external source (shareholder letter, memo, filing, article, podcast, book chapter, fund letter, or a DATASET such as a long-history price/valuation series or a macro table) into a distilled library entry plus the principle updates it actually earns, end to end, then commits locally. Three equally first-class input modes: a URL; a description ("the latest Marks memo", "that Buffett letter about float") resolved by web search into candidates to pick from; or a file already dropped in library/_inbox/. Retrieves down a per-type ladder, archives the raw text into library/sources/ and passes the grounding gate before distilling anything, writes library/{slug}.md with locator-addressed and verification-tagged takeaways plus a non-empty Not-captured audit, fans out to every principles/ theme whose Scope line the source genuinely touches (minting permanent IDs, or appending attributed Voices and dated Log lines), greps portfolio.md / watchlist.md / theses for collisions and drafts a journal/_flagged.md entry when a source contradicts an open thesis, checks for decisions resting on principle text it changed, updates the indexes and the sources.md queue, mirrors the archive, then lints, stages only its own files and commits. One source per run, never batched. Triggered by "absorb {url}", "absorb the latest Marks memo", "absorb this letter/memo/filing/podcast/article", "drop this in the library", "add this to the vault", a pasted link, a file left in _inbox/, or a bare "absorb" with no argument — which offers the _inbox/ contents, the sources.md queue, and the chance to queue something you only heard about.
---

# absorb

## When to use

- **A URL:** "absorb this", "add this memo to the library."
- **A description:** "the latest Marks memo", "that Buffett letter about float", "the Damodaran post on terminal value" — resolved by search into candidates you pick from, then retrieved without further prompting.
- **A dropped file:** anything saved into `library/_inbox/` — a letter PDF, a saved article, a pasted transcript, a book chapter. Retrieval is skipped entirely.
- **Nothing in hand:** bare `absorb` offers the `_inbox/` contents, the `sources.md` queue, and "is there something you heard about that should go in the queue?" That queue row is the capture channel between hearing a podcast in the car and being at the desk. Use it — an unqueued source is a source that evaporates.

Friction target: URL in, committed out, zero prompts for a plain investor letter. One source per run, end to end. **Never batched** — several items dropped at once get processed one at a time, and say so before starting with the first. A batch is where the completeness pass quietly degrades into skimming.

What absorb does **not** do, ever:

- **Never writes a thesis.** No `sectors/**/thesis.md` body, no kill switches. A source that bears on a holding produces a flag, not a thesis edit.
- **Never writes `portfolio.md` position rows**, and never makes a buy/sell/trim recommendation. Absorbed material answers "what does the field believe", not "what should I do with my money" — per "Evidence weighting (canonical)".
- **Never absorbs the owner's own thinking.** Own knowledge goes to `journal/{date}-notes.md`, a `decision-log` entry, or a thesis via `company-deep-dive`. `library/` is external evidence under verification labels — nothing else.

## Inputs

- The source: a URL, a description, or an `_inbox/` filename. None of the three is the "real" mode.
- Optional: themes the owner already thinks it maps to — checked against `**Scope:**` lines, never assumed.
- Optional: "show me first", which gates every write in this run instead of only the high-consequence tier.

## Process

### 0. Precondition, and the interrupted-run protocol

Check only the paths this skill writes: `git status --porcelain library principles sources.md journal/_flagged.md`.

- **Its own paths clean:** proceed.
- **Unrelated dirt elsewhere in the tree** (a half-written thesis, a draft primer): print a loud one-line warning naming the dirty files and **proceed anyway**. Per "Tiered autowrite (canonical)" — a whole-tree cleanliness rule would make ingestion hostage to this vault's documented stranded-work habit, `--staged` linting means that work cannot break this commit, and `scripts/check-cadence.py` ages unrelated dirt on its own clock.
- **A diff confined to `sources.md`'s queue section:** whitelisted (that is `consult`'s one sanctioned write). Commit it separately first, then proceed on a clean footing.
- **Its own paths dirty:** a previous run was interrupted. Offer two options via AskUserQuestion and never a bare refusal — **RESUME** (read what is already written, work out which step it died on, finish and commit it) or **REVERT** (`git checkout -- library principles sources.md journal/_flagged.md`, then start clean). Refusing here is how a stranded half-entry becomes permanent.

### 1. Resolve the source

- **URL given:** fetch once. State title, author, publication date and type in one line, then proceed. No confirmation prompt — this is the zero-friction path.
- **Description given:** WebSearch, then present up to 3 candidates via AskUserQuestion. Each card carries the canonical URL, publish date, author/speaker and length — **all scraped from the candidate pages, never from model memory.** Model memory produces plausible-looking letters that do not exist. The owner picks; retrieval then runs autonomously.
- **`_inbox/` file given:** identify it from the file itself (title, author, date, type — ask only if genuinely ambiguous). **Skip step 2 entirely**; the step 3 grounding gate is satisfied by the file, but still run the identity and length sanity checks — the common failures here are a truncated download and the wrong file with the right name.
- **It is a dataset** (a long-history price/valuation series, a macro table, an ERP series): retrieve **the file itself, never the page describing it.** The download link on the publisher's data page is the source; the page's prose about it is a description, and a table someone else has rendered into HTML — multpl.com for Shiller's CAPE — is a *presentation* of the dataset, which is the thing absorbing it is meant to replace. State the file name, format, publisher and the vintage or "last updated" stamp the provider prints: a dataset has a vintage the way a letter has a date, and the same URL fetched six months apart is two sources, not one.
- **Only recaps found:** if search surfaces third-party summaries of the described source (a newsletter write-up, an SEO blog), say so plainly and offer either the secondary artifact **explicitly labelled secondary** (figures cap at `partial` per "Verification labels (canonical)") or a deeper rung of step 2. Never distill a recap as if it were the source.
- **It is the owner's own thinking:** stop and say so. Route to `journal/` or a thesis, per the "What absorb does not do" list above.

### 2. Retrieve — the ladder, cheapest rung first

Work down the ladder for the type and record which rung actually worked in the entry's `retrieval-path` frontmatter — that is how a rotted path becomes visible next time instead of being rediscovered next quarter. When a rung listed in `sources.md`'s access-path column has rotted, fix that row in step 6.

**Shareholder letters (Buffett/Berkshire):** `berkshirehathaway.com/letters/letters.html` — direct HTML or PDF, no paywall, full archive back to 1977.

**Marks memos:** `oaktreecapital.com/insights/memos` — direct PDF, ungated.

**Filings (10-K, 10-Q, 8-K, 13F, Form 4):** the `edgartools` MCP first (wired in `.mcp.json`), then the issuer's IR page for non-US or older documents.

**Articles:** plain fetch of the individual post URL, never the homepage (homepages serve excerpts). Bot-blocked → curl with a desktop user agent to the scratchpad. "[Content truncated]" means long, not gated → curl and strip tags locally. Genuinely paywalled → owner paste or `_inbox/` drop; never summarize a paywalled piece from its teaser.

**Podcasts / interviews / annual-meeting Q&A:** (1) the first-party episode page for metadata and the true runtime; (2) a transcript site — re-search rather than trusting a rung that worked last quarter; (3) `yt-dlp --write-auto-subs --sub-langs en --skip-download {url}` where a video exists; (4) owner paste. Auto-generated transcripts cap at `partial`.

**Books / long reports:** owner-supplied PDF into `library/_inbox/`. Finite high-density corpora (Poor Charlie's Almanack, Daily Journal Q&A) are absorbed in chapters, not whole — one chapter is one run.

**Datasets (long-history series, macro tables, provider data pages):** (1) the author's or institution's own data page, downloading the file it links — Shiller's `ie_data.xls` at shillerdata.com, Damodaran's series at pages.stern.nyu.edu, a central-bank or statistical-office release; (2) the institutional archive or the university mirror where the personal page has rotted; (3) owner drop into `library/_inbox/`. Never reconstruct a series from a third-party rendering of it, and never from a chart: a site republishing someone else's series is a relay that caps at `partial` per "Verification labels (canonical)", and reading numbers off a plotted line is inventing figures with extra steps. Fetch with `curl -L -o` rather than a text fetch — a spreadsheet pulled through an HTML-oriented fetcher arrives corrupted or as the landing page, and the step 3 parse check is what catches it.

**Explicit failure exit.** Every rung exhausted → append a queue row to `sources.md` and stop cleanly:

```
| wanted: transcript for {source} | {type} | absorb failed every retrieval rung ({rungs tried}) | {YYYY-MM-DD} | absorb |
```

Then say precisely which rungs failed and what would unblock it (a paste, an `_inbox/` drop, a `yt-dlp` install). **Never a half-entry.** An entry written without its source is indistinguishable from one written from memory six months later.

### 3. Ground — the gate

Nothing is distilled until all of these hold. Cite "Source archive and deep retrieval (canonical)".

- **The raw text exists as a FILE** at `library/sources/{slug}.txt`, sharing the entry's slug (1:1:1, lint-enforced). Never memory-only. A PDF is kept alongside as `library/sources/{slug}.pdf`; an `_inbox/` binary is moved there, not copied.
- **Length above the per-type floor:** letter / memo / report / filing > 5k chars, transcript > 15k chars, article > 2k chars. Below the floor is a retrieval failure wearing a success costume.
- **Identity check:** the claimed author or speaker plus 2-3 topic keywords from step 1 actually appear in the raw text.
- **Transcripts:** word count against runtime at ~130-150 wpm. Under ~80% coverage means the transcript is partial — record the uncovered range in `## Not captured` and cap its figures at `partial`.
- **PDFs: extract ONCE**, with `python scripts/pdf-extract.py {in.pdf} library/sources/{slug}.txt`. That `.txt` is the immutable address space every locator points into — never re-extract over one an entry already cites. Below ~200 chars/page the **EXTRACTOR** failed, not the source: try another tool, or render the pages as images and read them visually. Never write "content not retrievable" without naming which extractors were tried.

- **Datasets: the archive is the raw file, and the gate is that it PARSES and matches what the publisher claims.** The archive path is `library/sources/{slug}.{csv,xlsx,xls}`, saved **exactly as downloaded** — never opened-and-re-saved, never tidied — per "Source archive and deep retrieval (canonical)". The length floor and the identity check do not transfer, so these are their analogue and all four hold before anything is distilled: (a) the file opens with a plain pandas read and its sheet names are the ones the entry will cite; (b) the columns the entry will address exist, under the names the provider documents; (c) the **row count and the first and last dates match the coverage the source advertises** — a page saying "monthly from 1871" against a file whose last row is 2019 is a stale or truncated download, this path's version of the JS shell; (d) two or three values spot-checked against figures the provider prints in its own prose. A silently truncated CSV is the dataset form of the 281-character extraction: a real file genuinely exists on disk, so only the check catches it. Record sheet, rows, date range, and the tool and date in `extraction:`, the way a PDF records its extractor — that line is the provenance for every locator below it.

Gate fails → stop. Say which rungs and which extractors were tried, and offer the paste/drop path. The failure this prevents is the worst one available: a cookie wall or JS shell comes back and a fluent, plausible, entirely fictional entry gets written and committed. Distilled-from-vibes must be structurally impossible, not merely discouraged.

### 4. Distill into the library entry

Write `library/{slug}.md` from `library/_template.md`. Sweep all five knowledge types per "Distillation completeness (canonical)" — claims/theses, **methods**, distinctions/profiles, heuristics, texture — and obey its "store the move, not the label" rule: a takeaway naming a framework, screen or sequence without its actual steps is unfinished. The steps are the knowledge.

- Every takeaway carries a **locator** (page, section, paragraph, or timestamp) and a **verification tag**, per "Verification labels (canonical)". Every takeaway also carries **one texture line** — the concrete mechanism or example that keeps it copyable instead of a slogan.
- Figures live inside the takeaway with their source and date, tagged. A takeaway that is only a number is not finished, and **an unconfirmed figure means attribute the claim, not the number.**
- Relayed claims go in `## Cites` naming the origin and cap at `partial` — a letter reciting someone else's study is not independent support.
- `source-span` is required for `podcast`, `interview` and `annual-meeting-transcript`. Get the true runtime from the first-party page: an entry that stops the span at 40:00 on a 58:03 episode quietly exempts the tail from the gap-partition lint forever. `untimed` is legal for an owner-pasted transcript with no native timestamps — then use paragraph locators, say why in `## Not captured`, and expect priority in the next spot-audit. **Never invent a timestamp to satisfy the check.**
- `## Not captured` is required and non-empty: each omitted segment with its locator and a one-line reason (promotional, off-topic, colour, already held). Takeaway locators plus leftovers should account for the whole source span.
- Set `talking-book: yes` when the author is discussing a position they hold. Their claims about that name are directional only; their general reasoning still transfers.
- `tags:` lists the theme slugs this source genuinely touches — the fan-out audit and the reverse-notification both run off it, so an untagged take is invisible to the tooling.
- **For `type: dataset`,** follow the dataset clause of "Distillation completeness (canonical)": one takeaway per **series**, not one per topic, each carrying its locator in the dataset form — `(sheet Data, col K, 1881-01 to 2026-07)` — its verification tag, and its **units, base and currency**, with the texture line saying what the series is actually for and what shape it comes in (`monthly, so a 10-year forward window is 120 rows`). Name the transformations the series supports, since those are what the vault came for. `## Not captured` carries coverage, methodology and known revisions instead of skipped segments. `source-span` is the file's own extent (`"1871-01 to 2026-07, 1,867 rows"`) and is not interval-checked — the gap-partition math is for timed audio. **A figure is not verified by living in a spreadsheet.** The label follows the SOURCE exactly as it does everywhere else: a series its publisher computed from its own primary collection is `verified`; a series a third party **assembled from other people's data** is `partial` unless the underlying is itself primary and named in `## Cites`; and any column the compiler imputed, spliced or backfilled is `partial` at best regardless of who published it, with the treatment written into the methodology gap. A dataset file is the most authoritative-*looking* artifact this vault ingests, which is exactly why the cap matters.

**Second read, for any source touching 3+ themes.** Re-read the RAW TEXT independently and diff the result against your draft — ideally via a subagent handed only `library/sources/{slug}.txt`, the five knowledge types, and the themes' `**Scope:**` lines, and explicitly **not** your draft. A same-pass "did I get everything?" reproduces the original miss, because the draft looks complete by construction. Be honest about what this buys: per "Distillation completeness (canonical)" it closes the unaccounted-span shape and does **not** close the interleaved-miss shape — a method dropped from inside a segment that also produced a captured takeaway leaves no gap for any lint to find.

### 5. Fan out to `principles/`

Normalize the source's terms through the alias table in `principles/README.md` first — the same idea arriving under a second name is how a concept gets stored twice. A genuinely new synonym earns an alias row (additive, autowrite).

Then, for **every** theme, read its `**Scope:**` line in the file itself — **not** the index title. Judging relevance from a title is exactly how a squarely relevant theme gets skipped. Produce a source-anchored result for each one, no exceptions: either a captured take with its locator, or an explicit "scanned {terms} — nothing". Substantive engagement earns a take; a passing mention does not. Do not manufacture spread across the roster.

Per theme the source does touch:

- **Item already exists** → append an attributed Voices line in the template's shape (`**agrees**` / `**diverges**` / `**qualifies**`, who, source and year, verification tag, and the `holds when:` conditions) plus a dated Log line naming this entry. **Corroboration is content** — record agreement, not only clashes. Same person repeating a view years apart is cross-time replication and strengthens; the same person having *changed* their view is supersession — record the new take, note the old, and do not count it as corroboration.
- **Genuinely new** → mint the next free ID per "Permanent IDs and addressing (canonical)": n = one past the highest ever used in that file, bold-defined once in the file whose `prefix:` owns it, kind letter mandatory. Statements are conditional and falsifiable ("when X, do Y because Z") — if it cannot be violated it is not a rule and does not get an ID.
- Keep Voices takes **qualitative — no bare figures.** The number lives in the library entry with its locator and tag; a figure on a Voices line reads as a citation it does not have.
- **Never write the My-record line.** That field is `post-mortem`'s alone.
- Every touched file gets a Log line and a refreshed `updated:` date — that is also what clears the file under "Stale principle (canonical)".

**Write tiers**, per "Tiered autowrite (canonical)": a new item inside an existing file, new Voices lines, Log lines, alias rows and the library entry are **autowrite**. A **new principle file** is glance-confirm — one line, wait for a yes. Any `evidence:` or `my record:` change follows "Maturity and tier-1 sources (canonical)" and is glance-confirm: promotion needs 3+ independent primary origins including one tier-1, demotion needs 2+ contradicting primaries or an explicit owner override, and one new source alone never demotes — it adds a named dissent instead. Check the shape before committing: the lint fails `well-supported` without 3+ Voices lines and at least one `[verified]`, and `contested` without a `**diverges**` line.

**Collision check.** Grep the live book for what this source touches:

```
git grep -nE "{TICKER}|{situation}" -- portfolio.md watchlist.md sectors
```

A source that contradicts the *reasoning* of an open thesis gets a `journal/_flagged.md` entry in that file's own grammar — read its header for the exact line format, name **both** the principle ID and the thesis it collides with, and give `next:` a defined value (`thesis-check`):

```
- {TICKER}: flagged {YYYY-MM-DD} — {source} contradicts the {leg} of the thesis; cites {PREFIX}-P{n} — see library/{slug}.md ({locator}) → next: thesis-check
```

This is **glance-confirm and the highest-consequence write in this vault** — anything naming an open holding or watchlist entry is. And it stays advisory: per "Principle authority (canonical)" the flag can produce at most a WATCH-grade signal and a recommendation that the owner *write* a kill switch. A principle can never trigger a verdict, block a trade, or fire a kill switch; the kill switches in `thesis.md` are the only authoritative triggers. Note also "Principles routing (canonical)": a claim *about a holding* routes to the flag, never into a principle body.

**A dataset fans out differently, and mostly not into `principles/`.** Run the roster sweep anyway and expect most themes to return an honest "scanned {terms} — nothing": a series is evidence, not a claim, and minting a principle out of a table is manufacturing. What a dataset changes is what the vault can now **compute**, so its fan-out record is about consumers rather than themes. Grep for the figures it supersedes — the ones currently resting on a secondary presentation of this same data:

```
git grep -nE "{series name}|{secondary source's name or domain}" -- frameworks sectors funds library
```

Each hit is a `partial` figure that can now be recomputed from the primary. None of them is absorb's to rewrite: framework files, fund documents and theses belong to other skills, and a concurrently-running peer may be holding one per "Concurrent orchestration (canonical)". List them in `## Fan-out`, leave a `sources.md` queue row naming the file, the series and the consuming document, and say the same in the summary — an absorbed dataset whose consumers were never told is a capability nobody knows they have, which is how the same secondary figure gets re-cited for another year.

**Reverse-notification.** Grep `journal/` for `relied on {ID}@` stamps (per "Reliance stamp (canonical)") whose as-of date predates any principle text you changed this run, and surface them in the summary. Do not edit those entries — `journal/` is append-only. This is the only mechanism by which a growing corpus can notify a decision that was already made.

### 6. Index, state files, mirror

- Append the entry's row to `library/README.md`'s `## Index` table as a **link**, not a bare slug — the lint reads links, and the bijection is commit-blocking in both directions.
- New principle file → add its `## Index` row in `principles/README.md` (theme link, prefix, the `**Scope:**` line verbatim). Items added to an existing file need no index change; that table carries no counts.
- Clear this source's queue row from `sources.md` if it had one, and update the matching Recurring row's **Last absorbed** date. A recurring source whose Last-absorbed says "never" forever is a lie in that table. Fix any access path that rotted during this run.
- `python scripts/mirror-sources.py`. `library/sources/` is gitignored, so the commit does **not** back up the raw source — this is the only step that does, and skipping it is how a pasted transcript becomes unrecoverable. It copies whatever extension it finds, so an archived dataset is covered; a dataset is also the material that needs it most, because providers republish revised vintages **in place at the same URL** and the vintage an entry's locators address stops being downloadable without warning.

### 7. Commit and summarize

1. `python scripts/check-cross-references.py` and fix every finding **in-context**, while you still hold the source. Then stage and re-run with `--staged`, which is what the hook runs.
2. Stage only the exact files this run wrote, by explicit path. **Never `git add -A`** — it sweeps unrelated work into a commit labelled for this source. Never stage `library/sources/` or `library/_inbox/`; the entry's `archive:` and `extraction:` frontmatter is their committed record.
3. Commit locally, message naming the source. **Never `--no-verify`** — a failing hook means fix the content. Local commit only: this is revertibility, not backup.
4. Print the summary below.

**Minimal absorb — the degraded mode, named on purpose.** Grounding gate → library entry (locators, verification tags, non-empty `## Not captured`) → index row → scoped commit. Skips fan-out, the collision check and the mirror, and leaves a `fan-out-pending` row in `sources.md`'s queue for a catch-up run. Use it when the owner is in a hurry, or when the queue has been backing up across sweeps — that backlog is the honest signal that the full pipeline is too heavy for the moment, and a named degraded mode is what keeps the answer from being "absorb nothing". Say out loud that this is minimal absorb, so nobody later reads a fan-out-free entry as a source that touched no theme.

## Output

Autowrite runs print nothing until the end. Only the high-consequence tier interrupts, one line each. Then:

```
absorbed: {title} — {author}, {published} ({type})
retrieval: rung {n} ({what worked}) · extraction: {tool, chars, chars/page} · span: {source-span}
files: library/{slug}.md · library/README.md · {principle files} · {sources.md | journal/_flagged.md}
principles: minted {IDs} · voices added {IDs} · evidence tags changed {ID: X → Y}
themes scanned, nothing found: {slugs}
flags raised: {flagged.md line, or none}
decisions resting on changed principle text: {relied-on stamps, or none}
not captured: {every leftover with its locator and reason}
commit: {short-sha} — revert with `git revert {short-sha}`
```

The full Not-captured list goes in the summary, not just in the file. That is what makes "covered everything" checkable rather than asserted.

If the run stopped early, say exactly where: which retrieval rungs failed, or which grounding check failed and which extractors were tried, or which of its own paths were dirty and whether the owner chose resume or revert. A clean stop with a queue row is a good outcome. A half-entry is not.

## Notes

- This is the skill that stops knowledge from evaporating. The failure it exists to prevent is not a bad entry — it is the podcast heard in the car in March that no longer exists in April. That is why the bare-`absorb` queue row is a first-class output and not an afterthought: capture beats quality at the moment of encounter, and the queue is where the two get reconciled.
- The grounding gate is the load-bearing wall of the entire vault. Everything downstream — principles, flags, the deep-retrieval ladder, a thesis citing a principle — inherits its trust from "the raw text was on disk and was read". One entry written from a JS shell poisons a corpus that has no way to detect it, because the entry will read *better* than the honest ones. Fluency is not evidence.
- A low extraction yield is a broken tool, never an empty source. This vault has the receipt: 281 characters from an 18-page report whose tables another extractor read in full. The gate cannot catch it, because a file genuinely exists on disk — only your suspicion can.
- **"Nothing relevant" is a first-class output.** A source that legitimately touches one theme should produce one take and five honest "scanned {terms} — nothing" lines. Spreading a thin source across six themes to look thorough is the one failure mode that damages the corpus faster than skipping it entirely, because every future `consult` inherits the padding as if it were evidence.
- An entry that changed nothing anywhere is a real result — record it in `## Fan-out` and say which: the source was weak, the ground was already held, or it sat below the bar. Do not mint a principle to justify the run having happened.
- Absorbed external claims never outrank the owner's own record about the owner. Per "Evidence weighting (canonical)": a post-mortem beats a thesis hypothesis beats a famous investor's general rule, and the primary filing beats any investor's characterization of a company — including a celebrated one. A letter describing a business is commentary; the 10-K is the record.
- Never let a source with prestige skip a step. A Buffett letter is tier-1 for *promotion* purposes and gets exactly the same locators, verification tags and Not-captured audit as a blog post. Reverence is how unverified figures enter a vault.
- The lint is a schema gate, not a truth gate. It cannot see a fabricated attributed take or a wrongly-confident `verified`. Those are caught by the grounding gate, the periodic spot-audit, and `git revert` on the summary you just printed — which is precisely why the summary lists every take and every ID it touched.
- The glance-confirm tier is short on purpose. It exists for the three writes that are damaging *and* hard to spot later: a new principle file, an evidence-tag change, and a flag naming an open holding. Everything else is additive and reversible, and prompting for it would train the owner to stop reading the prompts.
