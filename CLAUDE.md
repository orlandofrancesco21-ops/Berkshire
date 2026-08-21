# Working in this vault

Personal long-only, long-term, low-frequency public-markets research system. Plain markdown, read in Obsidian, operated by the skills in `.claude/skills/`. Private repo — it holds positions, cost basis, and conviction calls.

**Read [docs/build-plan.md](docs/build-plan.md) "Shared rules" before any structural change.** Those rules are canonical and are referenced *by name* from skills, never restated — restating is how versions drift apart.

## The four tiers

| Tier | Holds | Written by |
|---|---|---|
| `principles/` | Cross-industry investment principles + attributed investor voices | `absorb`, `post-mortem`, `company-deep-dive`, `watchlist-revisit` |
| `frameworks/` | Industry-specific evaluation playbooks | `framework-bootstrap`, `company-deep-dive` |
| `sectors/` | Sector primers, per-company `thesis.md` + `valuation.md` | `sector-primer`, `company-deep-dive` |
| `library/` | One distilled entry per absorbed external source | `absorb` only |

State files: `portfolio.md` (positions), `watchlist.md` (names), `sources.md` (sources to absorb), `journal/` (dated triage / review / decision / post-mortem entries), `journal/_flagged.md` (open flags — canon for flag state).

## Non-negotiables

- **Thesis docs and journal entries are append-only and dated.** Never rewrite an existing dated line — write a new one that corrects it. Enforced by the pre-commit gate, not just convention.
- **Fair value is always a range**, never a point.
- **Exit is never triggered by price alone** — only by thesis change. Nor by a principle.
- **Principles are advisory.** A stored principle can produce a WATCH flag or a checklist line. It can never trigger a verdict, block a trade, or fire a kill switch — the kill switches in `thesis.md` are the only authoritative triggers. See "Principle authority (canonical)".
- **Never invent a figure.** Unconfirmed means attribute the claim, not the number. Verification labels are canonical.
- **"Nothing relevant" is always a valid output.** Suppression is a feature — `news-triage` exists to say "nothing material today", and a Principles check may legitimately find that no stored principle bears on a situation. Manufactured findings are worse than none.

## Enforcement (what will block a commit)

`python scripts/check-cross-references.py` — one gate, eight check classes: broken links, unresolvable `{PREFIX}-{P|M|T}{n}` citations, library schema (locators, verification tags, non-empty `## Not captured`, archive pairing), podcast gap-partition interval math, index bijection, thesis Principles-check shape, append-only violations (now covering `journal/`, `thesis.md`, `frameworks/*.md`'s learned-log, and each `principles/*.md` item's own `Log:`), evidence-tag consistency. Runs `--staged` from `.githooks/pre-commit` (it checks what is being committed, not your working tree).

`python scripts/test-lint.py` — planted-violation cases proving each gate actually fires, in **both** directions where a gate can reject, plus one case that renders the REAL `principles/_template.md` (not a hand-typed paraphrase of it) and asserts it passes. **Run this after touching the lint.** A gate that silently checks nothing is this vault's documented failure mode, seven times over now — including a cutover constant left at a placeholder value that grandfathered every thesis for two days while reporting `[OK]`. A check that only ever rejects is indistinguishable from a check that rejects everything; a fixture that quietly drifted from the template it's supposed to mirror is the same failure one step removed.

`python scripts/check-cadence.py` — the clock. Runs at session start (and at user level for any session on this machine, once a day, escalated items only). Silent when healthy. Never blocks. Also scans the repo for `TODO(vault)`-with-a-colon markers (an unresolved value that may currently be silently wrong — this is how the cutover placeholder should have been caught the day it shipped, not two days later; this sentence avoids writing the literal marker because the scanner would flag its own documentation, which it did, on 2026-08-22) and nags if it has been >90 days since `evaluate` last ran on a name outside every existing sector — every recent bug here was found by exercising the system on something genuinely new, not by any planted test.

Skills may be orchestrated one at a time (the common case) or in parallel by a parent agent — see "Concurrent orchestration (canonical)" in docs/build-plan.md if you are running `company-deep-dive` or `sector-primer` outside `evaluate`'s own sequential default.

One-time setup on a new clone: `git config core.hooksPath .githooks`, and set `BERKSHIRE_SOURCE_MIRROR` to a personal location for the source archive (must NOT be the Synera OneDrive). Use PowerShell's `[Environment]::SetEnvironmentVariable(...)`, **not** `setx` — `setx` stores the quote characters as part of the value. Full step in the README's "Restore on a new machine".

## Deep retrieval — cheapest rung that answers the question wins

1. The principle block in `principles/` — pre-reconciled synthesis, plus what named investors say.
2. The library entry — exact figures with verification labels and locators.
3. `python scripts/source-pages.py --grep "<regex>"` — page-addressed search across every archived source.
4. `python scripts/source-pages.py <slug> <page|start-end>` — read only the cited span, never the whole document.
5. The PDF itself — for charts the text layer cannot carry.

**Retrieval is not evidence.** A grep hit in `library/sources/` is a pointer. Nothing enters a principle, thesis, flag, or decision from raw source text directly — it goes through `absorb`, which is what applies the grounding gate and the verification caps. Never fill a gap from model memory either: say what is missing and offer to absorb the source that would close it.

## Conventions

- Tickers use an exchange suffix where relevant (`ASML.AS`, `RIO.L`).
- Prices come from `yfinance` unless stated otherwise, and every quoted price carries date, time, and currency.
- Sector and theme folders/files are slugified (`offshore-drilling`, `valuation-discipline`).
- Real IDs only in docs and examples — every ID-shaped token is resolved by the lint, so a citation to an ID that no principle file defines blocks the commit — which is why the examples in this file and in the canonical rules use placeholder prefixes.
