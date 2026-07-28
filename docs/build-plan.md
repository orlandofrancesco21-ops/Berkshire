# Build plan — berkshire research system

> Handoff brief written 2026-05. Captures the design intent, what's built, what's still to build, and in what order. If you (future Francesco, or a future Claude session) wonder *why* something was built or skipped, this is the answer.

## Status as of 2026-07-28 — the knowledge layer

Two tiers, two skills, one enforcement layer. The vault could produce knowledge and had nowhere to put knowledge that came from outside it; dropping an investor letter on it did nothing, and lessons that spanned industries had no home because `frameworks/` is industry-scoped.

**Built:**

- **`principles/`** — cross-industry investment principles, 48 items across six themes (VAL, ASYM, MOAT, CAPA, NARC, PROD), each with a permanent citable ID, attributed **Voices** (who agrees, who diverges, and the conditions each holds under), and two independent tags: `evidence:` (what the field supports) and `my record:` (what my own results show). Seeded from 41 candidates already latent in the frameworks, theses and the 2026-07-17 audit — every item carries a locator proving it was not invented.
- **`library/`** + **`sources.md`** — one distilled entry per absorbed source, locator-addressed and verification-labelled, with a mandatory non-empty `## Not captured` so silent truncation cannot read as full coverage. Raw sources archived to `library/sources/` (gitignored, mirrored off-machine).
- **`absorb`** and **`consult`** — the path in and the path out. Drop a file in `library/_inbox/` or paste a URL; absorb resolves, retrieves down a per-type ladder, passes a grounding gate, distills, fans out to the themes it genuinely touches, flags collisions with open theses, and commits. `consult` answers "what do big investors say about this kind of situation" from the stored corpus, with citations, and queues the gap rather than guessing when the corpus is silent.
- **Grafts into seven skills.** `company-deep-dive` gained the Principles check (in the thesis *and rendered in the chat output* — a section that only lands on disk does not answer the question while you are reading). `thesis-check` treats a principle tension as WATCH-max. `decision-log` carries the reliance stamp and a mirror checklist row. `post-mortem` grades the check against the realized outcome and owns `My record:`. Six skills were deliberately left untouched.
- **Enforcement.** `check-cross-references.py` now runs eight check classes against *staged* content; `test-lint.py` holds 37 planted-violation cases proving each fires; `check-cadence.py` is the clock, silent when healthy, wired at vault and user level.

**What the build actually taught, worth keeping:**

Five bugs were found in the enforcement layer itself, every one the same shape — **the gate contradicting the thing it was supposed to enforce.** A Type-column value read as a filename. A routing table read as an index. HTML-comment bullets counted toward a line cap. The template's own `*Texture:*` sub-bullet demanding its own locator. And the worst: `VOICE_LINE_RE` required the mood marker to be the first bold token while the template prescribes `- **Voices:** **diverges** —`, so it matched **zero** voice lines in every correctly-formatted block — making `contested` unreachable *and* `well-supported` unachievable, with the self-test's negative cases passing for the wrong reason.

That last one is the lesson: **a check that only ever rejects is indistinguishable from a check that rejects everything.** The evidence-tag cases now assert both directions, and every fix shipped with the regression case that would have caught it. It was found not by the lint or the tests but by a subagent that had formatted its file correctly, could not tag a dissent it had legitimately recorded, and wrote the reason into its Log rather than quietly downgrading its own work.

The corollary for the vault's own discipline: `scripts/test-lint.py` is not optional maintenance. Run it after touching the lint. A gate nobody has proven fires is a gate nobody should trust.

**Still open, deliberately:**

- **Fan-out of the first absorbed source.** The Marks memo is distilled and committed but changed no principle — the tier was being audit-corrected the same day, and interleaving new external voices with in-flight structural fixes would have muddied whether an item's support came from a primary source or its own earlier prose. Queued in `sources.md` with priority order.
- **Zero primary external sources in the tier.** Every Voices line but one is the owner's own analysis citing another file the owner wrote, so an `agrees` line is currently architectural rather than evidential. The files disclose this in their Open questions. `emerging` across the tier is an honest statement about what this vault has READ, not about what the field supports — and nothing promotes above it until primaries are absorbed (Buffett letters are first in the queue).
- **The interleaved-miss shape in distillation.** The unaccounted-span gap is closed structurally by interval math; a method dropped from *within* a segment that also produced a takeaway leaves no gap to detect. That is the independent second read's job, and its own limit is that nothing verifies the read was genuinely independent.
- **Autonomous scheduled runs.** Not built. The watchdog is the floor; the written trigger is rituals slipping twice inside six weeks despite nags firing.
- **`portfolio.md` TBD trade details** — owner-only, from brokerage records. Nags until filled.
- Deferred with written triggers: `spar`, `source-sweep` and its honesty probe, the full schema-lint port, generated indexes, a standalone glossary, `park`, a `projects/` tier, RAG.

## Status as of 2026-07-17

Everything in "Gaps to fill" 1-5 below is **built**: `thesis-check`, `portfolio-review`, `post-mortem` + `archive/_template.md`, `news-triage`, and the `earnings-prep`/`earnings-debrief` pair all exist in `.claude/skills/`. Two skills were added that this plan never listed: `evaluate` (single entry point chaining framework-bootstrap → sector-primer → company-deep-dive) and `decision-log` (same-day structured record of every position change). Gap 6 (`compare-within-sector`) remains deliberately deferred — its precondition (3+ deep dives in one sector) is unmet.

Of the "Smaller things to fix": journal structure is defined (`journal/README.md`), the quarterly passed-names skill exists (`watchlist-revisit`), and the framework write-back is explicit in `company-deep-dive`. Still genuinely open:

- `portfolio.md` → structured format (yml/csv) at 15+ positions.
- End-to-end relative-path verification with a real deep dive (mechanical link checking is covered by `scripts/check-cross-references.py`).

The historical sections below are kept as written for context — read them as history, not as a to-do list.

## Context: what this repo is and what we're optimizing for

This is a personal long-only, long-term, low-frequency investing research system. The user is Francesco — works in growth equity at Blume, this is his personal public-markets stack. Not a developer by background but comfortable in Claude Code + PowerShell on Windows.

Core principle: durable industry knowledge compounds across decisions. Frameworks are first-class IP. The right framework for evaluating businesses in a given sector beats faster generic analysis.

Three-layer architecture:

- `frameworks/` — industry-general playbooks (the IP that compounds across sectors)
- `sectors/` — sector primers + per-company deep dives and valuations
- `portfolio.md` + `watchlist.md` + `journal/` — ongoing state and monitoring

The bridge artifact that makes the system work is the pair `thesis.md` + `valuation.md` per company. The Analyst skills write them; the Portfolio Manager skills read them. There is no second source of truth.

Design rules that are non-negotiable:

- Thesis docs are append-only and dated. Never overwrite — old thinking matters for calibration.
- Fair value is always a range, never a point.
- Exit is never triggered by price alone — only by thesis change.
- Skills should be opinionated. Encode discipline into the tool so future-Francesco can't quietly drop it under emotional pressure.

## What's already built (and works conceptually)

- `framework-bootstrap` — generates new industry framework from `_template.md`
- `sector-primer` — produces `primer.md` + `value-chain.md` + `kpis.md` + `players.md`
- `company-deep-dive` — produces `thesis.md` + `valuation.md` per company
- `valuation-check` — reads thesis + valuation, recommends HOLD/TRIM/ADD/REVIEW/EXIT

Templates exist for: framework, sector (primer, value-chain, kpis, players), company (thesis, valuation), portfolio, watchlist.

## Gaps to fill — in priority order

1. **`thesis-check` skill** (highest priority — referenced twice by existing skills but doesn't exist). Pulls all material events since last thesis update (earnings, 8-Ks, insider transactions, material news, sell-side revisions if available). Single question: does anything trigger a kill switch written in `thesis.md`? Output: "thesis intact" OR "REVIEW: signal X potentially triggers kill switch Y." Appends a dated entry to the thesis log.
2. **`portfolio-review` skill.** Sweeps every position in `portfolio.md`, runs `valuation-check` + `thesis-check` on each, produces a single ranked digest: which names need attention, why, what action is implied. This is the Monday-morning ritual that makes the system usable as a portfolio manager and not just an analyst.
3. **`archive/` post-mortem template + skill.** When a position closes, write a structured post-mortem: entry thesis, what changed, return, what I'd do differently, what this teaches me. Highest-ROI artifact for calibration over a 5-year horizon. Currently `archive/` is an empty folder with no template.
4. **`news-triage` skill.** Daily or every-few-days pass over portfolio + watchlist. Filters news into ignore / log / flag-for-thesis-check. Most important output is suppression — "nothing material today" is a valid answer. Without this, the choice is read-everything (drowning) or read-nothing (blind).
5. **`earnings-prep` + `earnings-debrief` pair.** Earnings is the most predictable thesis-stress moment. `earnings-prep` reads the thesis 5 days before each holding's print, surfaces what to listen for based on kill switches. `earnings-debrief` reads the transcript afterward, appends to the thesis log.
6. **`compare-within-sector` skill.** Stack-rank multiple deep dives within a sector. Build when there's a real felt need — not before.

## Smaller things to fix while in the repo

- `journal/` is referenced in the workflow but has no structure or skill writing into it. Either define what lives there (weekly notes, decision log, both) or remove until defined.
- `portfolio.md` is a markdown table. Fine for now, but at 15+ positions migrate to `portfolio.yml` or `portfolio.csv` so concentration / sector / currency exposure checks can be programmatic.
- The `watchlist.md` "Passed" section is great — add a quarterly skill that flags passed names where the original reason has materially changed (price dropped, ownership changed, etc.).
- `company-deep-dive` should have an explicit final step writing back to `frameworks/{industry}.md`'s "What I've learned over time" section. Currently this is implicit; make it explicit.
- Cross-reference paths in templates use relative paths (e.g. `../../`-style climbs from a thesis file up to the sector primer or framework). When `thesis-check` and `portfolio-review` are added, verify these resolve correctly from each skill's working directory. Test with a real deep dive end-to-end before declaring done. Use `scripts/check-cross-references.py` to mechanically validate.

## MCPs needed for the monitoring skills

- **EDGAR** — `sec-edgar-mcp` is active in `.mcp.json` at the repo root (project MCP servers live there, not in `.claude/settings.json`). Free, no API key. Needed for 10-K/10-Q/8-K/Form 4 pulls in `thesis-check`.
- **yfinance** — used as Python library directly, no MCP needed. Current prices, historical multiples.
- **Web search** — built into Claude. Used for news triage and sell-side commentary.
- For non-US issuers, plug in additional sources as needed (Companies House UK, ESMA portals EU).

## What this system is not

- **Not a screener.** The user is not trying to scan 5,000 names. He's evaluating 10-20 names per year deeply.
- **Not a backtester.** No historical strategy simulation. Theses are forward-looking.
- **Not a trading system.** No order execution. Recommendations are advisory; the user acts manually.
- **Not a generic financial-research tool.** The framework lens is the entire point — generic deep dives without framework grounding are explicitly out of scope.

## Voice and structure for new skills

Match the existing four skills exactly. Frontmatter with `name` and `description`. Sections: When to use → Inputs → Process (numbered) → Output → Notes. Notes section is opinionated — encode the discipline, not just the mechanics. The "this is the skill that prevents emotional trading" line in `valuation-check` is the right register.

## Suggested order

Start with `thesis-check`. Run it on a real holding end-to-end before moving on. Then `portfolio-review`. Then the archive post-mortem template. Then `news-triage`. Then earnings pair. Stop and use the system for a quarter before building anything else.

## Shared rules

Definitions that more than one skill depends on. Skills should reference these by name rather than restating slightly different versions — drift between versions is how subtle bugs are born.

### Stale thesis (canonical)

A thesis is **stale** if any of the following are true:

- (a) The most recent dated entry in the Update log of `thesis.md` is more than **6 months** old.
- (b) The company has reported earnings since the most recent thesis or valuation update (i.e. the most recent Update log entry predates the most recent earnings release).
- (c) A prior `thesis-check` returned **REVIEW** within the last **90 days** and no `company-deep-dive` refresh has run since.

Skills that depend on this rule: `valuation-check` (step 2), `thesis-check` (step 7), `portfolio-review` (step 6), `decision-log` (discipline checklist). When any of these skills detect a stale thesis, the recommendation is `company-deep-dive` refresh — *not* a price-based action.

### Price and data sourcing (canonical)

Prices come from **yfinance** unless a skill states otherwise. Every written entry that quotes a price, multiple, or market-derived number must snapshot the **date, time, and currency** it was pulled at — a price without a timestamp is not evidence. News/headline references in journal entries carry their publication date. Skills that depend on this rule: `valuation-check`, `thesis-check`, `decision-log`, `earnings-prep`, `watchlist-revisit`, `post-mortem`, `news-triage`.

### Principles routing (canonical)

Three tiers hold knowledge, and the boundary between them is a test, not a taste:

| Scope | Home |
|---|---|
| Reasoning about one company | `sectors/{sector}/companies/{TICKER}/thesis.md` |
| Lessons true of one industry | `frameworks/{industry}.md` → "What I've learned over time" |
| Lessons true across industries | `principles/{theme}.md` |

**The test:** would this sentence survive with the ticker *and* the industry deleted? Only then does it belong in `principles/`. "Adobe's freemium pivot sacrificed ~$500M of ARR" is thesis-level. "Creative-software moats are file formats" is framework-level. "A beat-and-raise met with a selloff means the narrative is unresolved — do not read confirming fundamentals as a resolved debate" is principle-level.

Company-specific reasoning must never land in `principles/`; an external claim *about a holding* routes to `journal/_flagged.md`, never into a principle body. Skills that depend on this rule: `absorb`, `consult`, `company-deep-dive` (step 9b), `post-mortem` (step 9b), `watchlist-revisit`, `framework-bootstrap`.

### Permanent IDs and addressing (canonical)

Everything citable carries a permanent handle, so references survive edits, renames, and future splits.

- **Prefix:** each principle file declares `prefix:` in frontmatter — 3-5 uppercase letters, unique across `principles/`, mirrored in the `principles/README.md` index. As permanent as the scheme itself: never change one once items carry it.
- **Format:** `{PREFIX}-P{n}` (principle), `-M{n}` (mental model), `-T{n}` (trap). The kind letter is mandatory — it makes the citation self-describing and makes ticker collisions (`BRK-B`), filing items (`8-K`) and index names structurally unable to false-positive the lint.
- **Traps carry IDs** (a deliberate divergence from the RevOps vault, where traps are never cross-referenced): a thesis's Principles check and a post-mortem both need to write "matches ASYM-T2 (stale anchor)", and an unaddressable object can be neither cited nor lint-verified.
- **Definition:** an ID is bold-defined **exactly once**, in the file whose `prefix:` owns it (`**{PREFIX}-P1** — {rule}`). Everywhere else it is a plain reference. A bold foreign-prefix token is a lint error — including in this document, which is why the example above uses a placeholder prefix rather than a real one.
- **Permanence:** assigned at birth (n = one past the highest ever used in that file), never renumbered, never reused. Deleting an item leaves a gap; ordinals mean assignment order, not importance. On a file split, IDs travel with their blocks.
- **Enforcement:** `scripts/check-cross-references.py` resolves every ID-shaped token repo-wide against the registry built from `principles/*.md` frontmatter, so a dangling or mistyped citation is commit-blocking. Consequence: docs and examples use REAL IDs, never invented ones.

### Principle authority (canonical)

**Principles are advisory everywhere, always.** Maximum effect anywhere in the system: a WATCH-grade flag, a checklist line a human reads, or a citation. A principle can never trigger a verdict, block or force a trade, or fire a kill switch.

The kill switches written in `thesis.md` remain the only authoritative triggers, and exit is never triggered by price alone — nor by a principle. `thesis-check` may classify a principle-derived signal as **WATCH** and recommend the owner *write* a kill switch; it may never escalate one to REVIEW on its own. `decision-log`'s principles row is a mirror of what was considered, never a gate on what may be done.

This rule is the firewall against authority inversion — a stored generalization quietly acquiring veto power over a specific, better-informed judgment. Every skill that reads `principles/` cites this rule by name.

### Verification labels (canonical)

- `verified` = stated plainly in the PRIMARY artifact whose text was actually read.
- `partial` = some verified, some asserted without backing; also the **cap** for relays, secondary summaries, and ASR/auto-generated transcripts. A podcast guest reciting a Buffett figure is a relay — name the origin in `cites:`.
- `unverified` = memory, secondary recap, or unconfirmable — labeled inline, next to the figure.
- Never invent or interpolate a figure. Unconfirmed means **attribute the claim, not the number**.
- Upgrades (`unverified` → `verified`) happen only by re-fetching the original artifact, recorded as a dated line. A vault entry is never evidence for upgrading another vault entry.

### Evidence weighting (canonical)

When entries conflict, weight by what each source can actually know:

- **About my own process or record:** my post-mortems > my thesis/deep-dive hypotheses > any absorbed external claim. An investor's general rule does not outrank my own closed-position evidence about *me*.
- **About a company's facts:** the primary filing outranks any investor's characterization of it — including a famous one. A letter describing a business is commentary; the 10-K is the record.
- Absorbed entries answer "what does the field believe", not "what is true here".

### Maturity and tier-1 sources (canonical)

Each principle carries two independent tags: `evidence:` (what the field supports) and `my record:` (what my own results show). They move separately, and the interesting states are the mismatches — `well-supported | mixed` means respected investors agree and my trades do not, which is exactly the signal worth surfacing before sizing.

- **Promotion** to `well-supported`: 3+ **independent primary origins** including one tier-1. **Demotion**: 2+ independent contradicting primaries, or an explicit owner override — never one new source alone (a single source may add a named dissent to Voices instead).
- **Tier-1 (investing):** a primary artifact by a named practitioner with a long public capital-allocation record — Buffett/Munger shareholder letters, Marks memos, Graham/Fisher/Klarman books, named fund letters — or a primary dataset/filing. Interviews and podcasts are primary **only for that speaker's own views**; third-party commentary and summaries are secondary and cap at `partial`.
- **Recency, scoped deliberately:** figures and market-condition-dependent claims discount with age. Durable principles do **not** — a rule independently attested in 1987, 2008 and 2020 is *stronger* than one attested only last quarter; cross-time replication is upgrade evidence, not staleness. Naive across-the-board recency turns maturity into fashion-chasing. And recency never outranks verification: a `verified` 2015 figure beats an `unverified` 2026 one.
- Every tag change appends a dated line to the principle's own **Log**, which serves as the evidence ledger.

### Stale principle (canonical)

A principle is **stale** if any of these hold: its Log's newest entry is more than **6 months** old; an active flag in `journal/_flagged.md` touches it with no resolving edit; or its `my record:` line predates a post-mortem on a position the principle bears on. `consult` and `company-deep-dive` must surface staleness *before* citing, the way `valuation-check` surfaces a stale thesis. Coexists with — and is distinct from — the stale-thesis rule above.

### Tiered autowrite (canonical)

Default is **autowrite**: `absorb` writes and commits (scoped, local) without a prompt for additive, low-stakes, reversible changes — a new library entry and its index row, new attributed Voices takes, Log lines, `sources.md` queue rows.

**Glance-confirm** (one line, wait for a yes) for the high-consequence mutations: any `evidence:`/`my record:` promotion or demotion; a rewrite of existing principle/model/trap text; a **new principle file**; a new `journal/_flagged.md` contradiction; an open-question resolution; and **anything naming an open holding or watchlist entry** — the highest-consequence collision in this vault.

**Never autonomous:** thesis body writes, kill-switch changes, and `portfolio.md` **position rows** (adds, removes, sizing, cost basis) are owner-only. `portfolio.md`'s **derived columns** — Current weight, Total value, the Thesis-status mirror, Last reviewed — are sanctioned writes for `portfolio-review` alone: they are recomputed values that skill already owns, not decisions.

Commit discipline for autowrite: run the lint on what is about to be committed and fix in-context BEFORE committing; stage only the exact files the run wrote (**never `git add -A`**); **never `git commit --no-verify`**; commit locally with a message naming the source (local = revertibility, not backup). Precondition: `absorb` requires a clean tree **among the paths it writes** (`library/`, `principles/`, `sources.md`, `journal/_flagged.md`) and prints a loud warning about unrelated dirt rather than refusing — a strict whole-tree rule would make ingestion hostage to this vault's documented stranded-work habit, and `scripts/check-cadence.py` ages unrelated dirt separately. A diff confined to `sources.md`'s queue section is whitelisted (that is `consult`'s one write) and committed separately first. If `absorb`'s own paths are dirty at start, it offers **resume** (finish and commit the stranded run) or **revert** — never a bare refusal.

The lint is a schema gate, not a truth gate: it cannot catch a fabricated attributed take or a wrong `verified` label. The grounding gate, the periodic spot-audit, and `git revert` are the catches for those.

### Source archive and deep retrieval (canonical)

The distilled library entry is the citable record; the raw source behind it is **kept**, not discarded.

- `library/sources/{slug}.{txt,pdf}` holds the full source, sharing one slug with its entry (`library/{slug}.md`) — a 1:1:1 contract, lint-enforced. Gitignored like `library/_inbox/`: raw third-party material (investor letters, paid transcripts) is never committed, so durability comes from the mirror, not git. `python scripts/mirror-sources.py` copies the archive to `$BERKSHIRE_SOURCE_MIRROR` — which must be a **personal** location; there is deliberately no `$OneDrive` fallback, because on this machine that resolves to the employer's tenant and this repo is private by design.
- **The `.txt` is the canonical address space, and it is immutable.** Extracted once, at absorb time, by `python scripts/pdf-extract.py` (PyMuPDF; page breaks = form feeds; printed page N = the Nth segment, 1-based). Never re-extract over an existing `.txt` an entry already cites: a different tool or version shifts page boundaries and silently breaks every locator. If a `.txt` is lost but the PDF survives, re-extract and then re-verify the entry's cited figures before trusting its locators again.
- **Extractor choice is load-bearing.** `pdftotext -layout` silently under-extracts some PDFs (in the sibling vault: 281 characters from an 18-page report that PyMuPDF read as 12,446, tables included). A near-empty extraction reads as "this source is infographic-only" when the whole text layer was there — the grounding gate cannot see it, because a file genuinely exists on disk. So: PyMuPDF is primary, the script warns below ~200 chars/page, and low yield means **try another tool** (or render pages as images and read them visually). Any entry claiming content "was not retrievable" must name which extractors were tried.
- **Retrieval, not evidence.** Raw source text is a retrieval surface, never a citation source. A grep hit or page dump from `sources/` is a POINTER — it may be reported, explicitly labelled unabsorbed, but nothing enters a principle, thesis, flag, or decision from `sources/` directly. A hit that matters is promoted through `absorb`, which is what applies the grounding gate and verification caps. `consult`'s "never fill a gap from model memory" extends to "nor from unabsorbed raw text".
- **The deep-retrieval ladder** (cheapest rung that answers the question wins): (1) the principle block — pre-reconciled synthesis; (2) the library entry — exact figures, verification labels, locators; (3) `scripts/source-pages.py --grep "<regex>"` — page-addressed search across every archived source; (4) `scripts/source-pages.py <slug> <page|start-end>` — read only the cited span, never the whole document; (5) the PDF itself, for charts the text cannot carry.

### Distillation completeness (canonical)

A source is not absorbed when its theses are captured — it is absorbed when its *transferable content* is.

- **Five knowledge types, all swept:** claims/theses; **methods**; distinctions/profiles; heuristics; texture. Not just claims.
- **Store the move, not the label.** The method corollary of "store the rule, never the bare figure": a takeaway naming a framework, sequence, or play without its actual steps is unfinished. The steps ARE the knowledge.
- **Completeness is checked against the source, never from memory of the draft** — the draft looks complete by construction, so the check must operate on the raw text. For a source touching 3+ principle themes, use an independent second read before finalizing.
- **Roster sweep, evidence-backed:** read each principle file's `**Scope:**` line (not the index title — judging relevance from a title is how a squarely relevant theme gets skipped) and produce a source-anchored result per theme: a captured take with a locator, or "scanned {terms} — nothing". Substantive engagement earns a take; a passing mention does not.
- **Leftovers audit, persisted and linted:** the entry's required `## Not captured` section enumerates omitted segments with locators and reasons, so takeaway locators + leftovers account for the whole source span. Silent truncation reads as "covered everything" when it did not.
- **One texture line per takeaway** — a concrete mechanism or example, so takeaways stay copyable instead of becoming slogans.
- **Gap-partition check, mandatory for timed transcripts:** `source-span` states the total span (`"0:00-58:03"`); the lint merges every locator in Takeaways + Not-captured into intervals and fails on an unaccounted stretch over ~6 minutes. The 30s buffer / 6min threshold constants are replay-tested against a real incident in the sibling vault — a looser 90s/8min pair silently swallowed the very gap that contained a dropped five-question method. Do not "tidy" these numbers without re-running that replay. `source-span: untimed` is legal for owner-pasted transcripts with no native timestamps: interval math is skipped, paragraph locators are required instead, `## Not captured` must say why, and the entry is queued for priority in the next spot-audit — a lint whose passing condition demands data the source does not contain is a fabrication machine.

**The honest limit.** The unaccounted-span shape is closed structurally. The **interleaved-miss** shape is not: a method dropped from *within* a segment that also produced a captured takeaway leaves no gap to detect. No lint can see that; it is the independent second read's job, and that read's own limit is that nothing verifies it was genuinely independent. Also open: a locator that is present but wrong (the lint checks shape, not truth). The periodic spot-audit is the ongoing regression watch on both.

### Reliance stamp (canonical)

When a decision leans on a stored principle, `decision-log` writes `relied on {ID}@{YYYY-MM-DD}` — the ID plus the as-of date of the text relied upon. This is a greppable contract: it lets `absorb` mechanically find decisions resting on principle text that has since changed (reverse-notification), which is the only way a corpus that keeps growing can notify a decision that was already made.
