# Verification spot-audit — 2026-07-28

First run. Triggered by `scripts/check-cadence.py` the moment `library/` stopped being empty, which is the intended behaviour: the probe activates when there is something to audit.

**What this probe is for.** With one person as the entire verification workforce, nothing else stops a `verified` label from going decorative. The lint checks that a tag and a locator are *present*; it cannot check that the locator is *true*. This is the only thing that does.

## Target: `library/marks-2025-12-is-it-a-bubble.md`

Checked six cited locators against the archived canonical text (`library/sources/marks-2025-12-is-it-a-bubble.txt`, PyMuPDF extraction, 18 pages) by searching the cited page for the claim's own language.

| Locator | Claim | Result |
|---|---|---|
| p. 2 | Bubbles result from excessive optimism *applied to* developments, not from the developments | PASS — verbatim |
| p. 2 | Galbraith on "the extreme brevity of the financial memory" | PASS — verbatim |
| p. 6 | "Lottery-ticket thinking" is Marks's own term | PASS — verbatim, and confirmed as his coinage ("what I call") |
| p. 11 | The four-part debt test (proportion, asset quality, alternative liquidity, lender safety margin) | PASS — verbatim |
| p. 14 | Bubble-era p/e comparison showing today's leaders *lower* than 1998-2000 | PASS — the "half-off sale relative to its p/e 26 years ago" line is on the cited page |
| p. 15 | Templeton, 1987: those four words, but 20% of the time things really are different | PASS — verbatim, and the reflexive kicker is on the same page |

**Verdict: no discrepancy.** Every cited page carries the claim attributed to it, in the source's own language. Six of nineteen takeaways sampled.

## What this does not establish

- **Nothing about the twelve locators not sampled.** Six of nineteen is a probe, not a proof.
- **Nothing about the interleaved-miss shape.** This checks that what was written is *true*; it cannot check what was silently *dropped* from a page that also produced a captured takeaway. That gap is named honestly in "Distillation completeness (canonical)" and is the independent second read's job, not this probe's.
- **Nothing about the relay caps.** The eight entries in the memo's `## Cites` section are labelled `partial` because Marks is relaying them; verifying that he really wrote what the entry says he wrote does not verify the underlying claims. Those upgrade only by fetching the primary — Buffett's 1999 remarks, the Hobart/Huber book, the Perez book — which is a future absorb, not this audit.

## Next

Due again in ~90 days. Per the alternating design, the next probe should take a **principle block** rather than a library entry — checking an item's `evidence:` tag against its own Voices and Log lines, which is the other direction the corpus can drift.
