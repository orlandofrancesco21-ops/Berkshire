---
name: consult
description: The read side of the knowledge layer — a 30-second, citation-backed answer to "what do serious investors say about this kind of situation?", drawn only from what the vault actually holds. Normalizes the question through the alias table in principles/README.md, routes by its Index to specific principle blocks, and returns each rule with its permanent ID, the attributed Voices (who, source and year, verification label, holds-when conditions), both maturity tags, and any named divergence — surfacing staleness before citing rather than after. When the question names a ticker it also reads that company's thesis.md "Principles check" and any active flags in journal/_flagged.md touching it, because "what do investors say about this situation" is usually really "about MY situation". Read-only except for one sanctioned write: a question the corpus cannot answer becomes a `wanted:` row in the sources.md queue, committed on its own. Advises, never decides — it does not write principles, does not write theses, does not recommend trades, and does not absorb sources (it offers; you invoke absorb). "The corpus holds nothing on this" is a complete answer. Triggered by "what do investors say about X", "what does the vault hold on X", "consult on X", "quick check on X", "is there a principle for this", "who disagrees with that", "do I have anything on X", or a ticker plus "what would a serious investor make of this situation".
---

# consult

## When to use

- "What do big investors say about a quality name compressing for three years?" — thirty seconds before you act on it.
- "Quick check: do I hold anything on buybacks at a premium multiple?"
- "Consult on NKE" — the stored principles that bear on a name you own, plus its open flags.
- Anything where the time budget is one screen, not a deep dive. If the question is really "should I buy this", that is `valuation-check` and `thesis-check`; consult supplies the principles those decisions are weighed against, and nothing more.

Not for: writing to `principles/`, refreshing a thesis, or absorbing a source. Consult offers the absorb; you invoke it.

## Inputs

- The question, however phrased. A ticker is optional and changes the run (step 2).
- Nothing else. Consult reads the vault as committed; it pulls no live market data.

## Process

1. **Normalize, then route by index — never sweep the tree.**
   - Map the question's terms through the alias table in `principles/README.md` first. "Adjusted FCF" and "distributable cash" are filed under owner earnings; "payoff ratio" under reward-to-risk; "thesis breaker" under kill switch. One glance at the table, not a study — but skip it and you will conclude the vault is silent on material it holds under its own name.
   - Read the Index table, then open the `**Scope:**` line of each candidate file before deciding it is irrelevant. Judge from the index title alone and a squarely relevant theme gets skipped — the same reason `absorb`'s roster sweep reads scope lines, per "Distillation completeness (canonical)".
   - Descend to the specific named blocks. Read those blocks plus that file's Open questions; do not read six principle files end to end because the question was vague. "A great business that has been getting cheaper for two years" routes to `principles/asymmetry-entry-exit.md` and lands on ASYM-T2 — one file, one block, not a tree walk.
   - Ambiguous scope: use the boundary calls in `principles/README.md` ("the multiple is too low" splits VAL / NARC / ASYM depending on what is being asked), pick the closest, and name the alternative in one clause. Do not stop to ask.

2. **If the question names a ticker, read the owner's own situation too.**
   - That company's `thesis.md` "Principles check" section — the verdict lines (`ALIGNS | TENSION | VIOLATES {ID}`) already written against this name, or the sentinel saying no stored principle bore on it.
   - Active flags in `journal/_flagged.md` touching the ticker. An external claim *about a holding* never lands in a principle body — it routes to the flag file, per "Principles routing (canonical)" — so for a specific claim about a specific name, the flag is often the only place the corpus holds it.
   - The newest dated entry in the thesis Update log. If the thesis is stale per "Stale thesis (canonical)", say so before quoting its Principles check: those lines are a record of past reasoning, not the current read, and the recommendation is a `company-deep-dive` refresh.

3. **Check staleness before citing, not after.** Run every block you are about to cite against "Stale principle (canonical)" — its Log date, the flag file, and its `my record:` line are the three inputs. A stale block is still citable: cite it with `[stale: {which of the three conditions fired}]` attached to the ID, the way `valuation-check` surfaces a stale thesis before recommending on it. Citing a stale principle silently is how a superseded rule keeps its authority.

4. **Answer, with the three registers kept apart.** Lead with the direct answer in two or three lines, then the citations. Per item:
   - The ID and the rule as written, both tags (`[evidence: … | my record: …]`) and the as-of date. Cite by permanent ID per "Permanent IDs and addressing (canonical)" so the answer stays traceable after the file is edited or split, and give the as-of date so `decision-log` can write `relied on {ID}@{date}` if this answer drives an action — per "Reliance stamp (canonical)".
   - The attributed Voices: who, source and year, verification label, and the `holds when` conditions. **The conditions are the whole value.** An unconditioned rule is a slogan, and a slogan is what gets misapplied to the one situation it was never about. Cap at the 2-3 most divergent takes plus a count ("4 voices, splitting on franchise durability — the rest are in the file").
   - Any **diverges** line, always. A named disagreement beats a false consensus: present both poles and say what distinguishes the cases — which is normally the holds-when conditions, not the strength of conviction.
   - Surface a tag mismatch unprompted. `well-supported | mixed` means respected investors agree and your own trades do not, and that belongs in front of you before sizing, per "Maturity and tier-1 sources (canonical)".

   Three registers, never blended:

   | Register | What it is | Where it comes from |
   |---|---|---|
   | Attributed | what a named investor said | a Voices line, with its verification label |
   | Vault's own | what your own analysis concluded | principle statement text, framework or thesis reasoning with no external voice behind it |
   | My record | what your actual results show | the `My record:` line, written by `post-mortem` |

   When two registers conflict, resolve by what each source can actually know, per "Evidence weighting (canonical)" — and state which way it resolved rather than presenting the conflict as a tie. A named investor's general rule losing to your own closed-position evidence is a normal, correct outcome of this step. Never invent or interpolate a figure: unconfirmed means attribute the claim, not the number ("Verification labels (canonical)"). Consult quotes no live price; a market figure it repeats from a vault file carries that file's snapshot, per "Price and data sourcing (canonical)".

5. **Deep retrieval when the block is not enough.** Walk the ladder in `CLAUDE.md`, cheapest rung that answers the question wins — and stop at the rung that answers it.
   - Rung 2, the library entry: exact figures with locators. Read its `## Not captured` before concluding the source is silent on the topic — that section exists so a deliberate omission does not read as absence.
   - Rung 3, one grep: `python scripts/source-pages.py --grep "owner earnings"`. Rung 4 reads only the cited span.
   - **Grep hits are pointers, never evidence.** Report one as `unabsorbed pointer — {slug} p.N` and offer the absorb; do not paraphrase raw source text into the answer, per "Source archive and deep retrieval (canonical)". One grep, not a deep read — speed is the contract, and a pointer is enough to decide whether the absorb is worth an afternoon.

6. **Name the gap, then queue it — the one sanctioned write.** If the corpus does not hold the answer, say exactly that. Never fill the hole from model memory, and never from unabsorbed raw text. Then append one row to the "Queued for absorption" table in `sources.md`:

   ```
   | wanted: {the question, as asked} | {source type, or blank if unknown} | {what it would settle} | 2026-07-28 | consult |
   ```

   Queue rows are autowrite per "Tiered autowrite (canonical)". Commit that one change on its own:

   ```
   python scripts/check-cross-references.py
   git add sources.md
   git commit -m "sources: queue wanted — {short question}"
   ```

   Stage that one path explicitly and take the rest of the commit discipline from "Tiered autowrite (canonical)". Committing it is not tidiness: a diff confined to the queue section is whitelisted for exactly this reason, and an uncommitted `sources.md` sits dirty in a path `absorb` needs clean, so the next ingestion run opens on a resume-or-revert prompt instead of on the source. The row is the anti-rediscovery mechanism — the same gap should not be found again next quarter with no record that it was already found.

   An empty answer still owes evidence of the sweep: name the themes actually scanned, the way a thesis sentinel must name the slugs it reviewed.

## Output

One screen. Length scales with the question, never with the size of the corpus.

```
{question} — consult

{The direct answer, 2-3 lines. What the stored principles hold and what decides between them.}

{ID} — {rule as written} [evidence: … | my record: …] (as-of {date}) [stale: …]
  agrees — {Who}, {source year} [verified]: {take} (holds when: {conditions})
  diverges — {Who}, {source year} [partial]: {take} (holds when: {conditions})
{ID} — {…}

Vault's own: {conclusions with no external voice behind them, marked as such}
My record: {post-mortem evidence — or "untested: no closed position bears on this"}
On {TICKER}: {Principles-check lines + active flags, with thesis staleness if any}
Gap: {what the corpus does not hold} → queued in sources.md ({date}) · absorb {suggested source}?
```

Nothing relevant is a complete run, not a failed one:

```
{question} — consult
The corpus holds nothing on this. Scanned: {theme slugs, with what was searched in each}.
Queued as `wanted: {question}` in sources.md ({date}), committed. Closest adjacent material: {ID or "none"}.
```

## Notes

- **This is the skill that prevents a manufactured consensus.** The failure it exists to stop is specific: one blog post, two of your own hunches and a half-remembered Buffett line get blended into "investors generally hold that…", and a real decision leans on it. Keeping attributed, vault's-own, and my-record visibly separate is the entire defense. If an answer cannot say which register a claim came from, that claim does not go in the answer.
- **Consult advises. It never decides.** Per "Principle authority (canonical)", principles are advisory everywhere, always. The output says what the stored rules and named investors hold and what conditions decide between them; it never says "so don't buy it", never blocks or forces a trade, and never fires a kill switch — the kill switches in `thesis.md` are the only authoritative triggers. A stored generalization acquiring veto power over a specific, better-informed judgment is authority inversion, and this skill is the surface where that would happen first.
- "The corpus holds nothing on this" is a first-class output and will be a frequent one early. A fluent improvised answer wearing the vault's authority is strictly worse than a blank: the blank gets queued and closed, the improvisation gets cited six months later as though it had a source.
- **Divergence is the product, not a defect.** Two named investors contradicting each other, with their conditions attached, is more useful than either alone — the conditions are what tell you which case you are actually in. Never smooth a real conflict into a summary. Where the corpus genuinely holds no through-line, say the theme is contested and hand over both poles.
- Conditions or nothing. A Voices line quoted without its `holds when` is a fortune cookie, and it will be applied confidently to the one situation it was never about.
- Never quote a figure the block does not carry. If the number matters and only the claim is stored, say the claim is stored and the number is not — then offer the absorb that would settle it. Filling in a plausible figure is unrecoverable: it reads exactly like a verified one afterwards.
- Speed is a feature with teeth. If the answer is running past a screen, it has stopped being a consult — either the question was a deep dive in disguise (hand it to `company-deep-dive`) or the routing was lazy and read whole files instead of blocks.
- Surface `well-supported | mixed` every time it appears, even when the question did not ask. The field agreeing while your own record disagrees is the most decision-relevant state the corpus can be in, and it is invisible unless something says it out loud.
- Consult never writes to `principles/`. Wanting to — because the answer feels one sentence short of a rule — means the next run should be `absorb`, which is what applies the grounding gate and the verification caps. The queue row is how that want survives the session.
