#!/usr/bin/env python3
"""Self-test for check-cross-references.py — proves every gate actually FIRES.

WHY THIS EXISTS. A lint that passes is indistinguishable from a lint that checks
nothing. Two gates in this vault's design were caught, before shipping, keyed to
strings no skill ever writes ("— company-deep-dive" as an Update-log tag) or
tokens this vault's files never contain (RevOps' "UNRESOLVED" flag marker). Both
would have reported green forever while enforcing nothing — the precise failure
mode the enforcement layer exists to prevent. So each check gets a planted
violation and must reject it.

Every case runs against a synthetic vault in a temp dir (its own git repo), so the
real vault is never touched.

Usage:
    python scripts/test-lint.py           # run all cases
    python scripts/test-lint.py -v        # show lint output per case
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
LINT = "scripts/check-cross-references.py"

# A minimal but valid vault: one principle file, one library entry + index rows,
# one grandfathered thesis. Each case mutates a copy of this.
CLEAN: dict[str, str] = {
    "principles/README.md": """# Principles

## Index

| Theme | Prefix | File | Scope |
|---|---|---|---|
| Valuation | VAL | [valuation-discipline](valuation-discipline.md) | What price pays for |
""",
    "principles/valuation-discipline.md": """---
theme: valuation-discipline
prefix: VAL
updated: 2026-07-28
---
# Valuation discipline

**Scope:** What a price implies, and when a multiple lies.

## Principles

### VAL-P1 — Fair value is a range
**VAL-P1** — Express fair value as a scenario range; a point estimate is fake precision.
`[evidence: emerging | my record: untested]` (as-of 2026-07-28)
- **Voices:** **agrees** — Owner, self, 2026 [unverified]: written into the vault's canon (holds when: always)
- **My record:** 2026-07-28 — canon since inception.
- **Log:**
  - 2026-07-28 — minted from docs/build-plan.md
""",
    "library/README.md": """# Library

## Index

| Entry | Type | Author |
|---|---|---|
| [marks-memo](marks-memo.md) | memo | Howard Marks |
""",
    "library/marks-memo.md": """---
title: A Memo
type: memo
author: Howard Marks
published: 2026-01
retrieved-from: https://example.com/memo
tags: [valuation-discipline]
archive: sources/marks-memo.txt
---
**One-line:** Cheapness on fear differs from cheapness on impairment.

## Takeaways
- Distinguish price falling on sentiment from price falling on earnings power (p. 3) [verified]

## Not captured
- Closing anecdote (pp. 8-9) — colour, no transferable rule
""",
    "sectors/x/companies/AAA/thesis.md": """# AAA — thesis

## What would change my mind
- Nothing yet.

## Conviction
3

## Update log

### 2026-05-20 — initial thesis
Written before the principles layer existed.
""",
    "journal/2026-05-20-decision.md": """# Decisions — 2026-05-20

- 2026-05-20 — BUY AAA, starter size.
""",
}


def build(tmp: Path, files: dict[str, str]) -> None:
    (tmp / "scripts").mkdir(parents=True, exist_ok=True)
    shutil.copy(REPO_ROOT / LINT, tmp / LINT)
    for rel, body in files.items():
        p = tmp / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(body, encoding="utf-8", newline="\n")


def git(tmp: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(tmp), *args],
                          capture_output=True, text=True, encoding="utf-8", errors="replace")


def run_lint(tmp: Path, staged: bool, env_extra: dict[str, str] | None = None) -> tuple[int, str]:
    env = {**os.environ, **(env_extra or {})}
    cmd = [sys.executable, str(tmp / LINT)] + (["--staged"] if staged else [])
    out = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8",
                         errors="replace", env=env, cwd=str(tmp))
    return out.returncode, out.stdout + out.stderr


def case(name: str, mutate, expect_fail: bool, needle: str = "",
         staged: bool = False, env: dict[str, str] | None = None,
         commit_first: bool = False):
    return dict(name=name, mutate=mutate, expect_fail=expect_fail, needle=needle,
                staged=staged, env=env, commit_first=commit_first)


def edit(rel: str, new: str):
    def _m(files: dict[str, str]) -> None:
        files[rel] = new
    return _m


def append(rel: str, extra: str):
    def _m(files: dict[str, str]) -> None:
        files[rel] = files[rel] + extra
    return _m


def replace(rel: str, old: str, new: str):
    def _m(files: dict[str, str]) -> None:
        assert old in files[rel], f"fixture drift: {old!r} not in {rel}"
        files[rel] = files[rel].replace(old, new)
    return _m


def noop(files: dict[str, str]) -> None:
    return None


def add_episode(body: str):
    """Write library/ep.md AND its index row, so gap-rule cases can only fail on
    the gap rule."""
    def _m(files: dict[str, str]) -> None:
        files["library/ep.md"] = body
        files["library/README.md"] = files["library/README.md"] + "| [ep](ep.md) | podcast | Some Host |\n"
    return _m


# A legitimate non-index table in a README. principles/README.md really carries a
# routing table naming sectors/.../thesis.md and an alias table; reading those as
# index rows demanded a nonexistent principles/thesis.md.
ROUTING_TABLE = """
## Routing

| Scope | Home |
|---|---|
| One company | sectors/x/companies/AAA/thesis.md |
"""

# A Principles check whose HTML comment contains a dashed rules list. The visible
# section is ONE line, so the 5-line cap must not fire. Counting comment lines as
# bullets would have taught authors to write worse comments to appease the lint.
COMMENTED_CHECK = """## Principles check

<!-- rules:
     - max 5 lines, hard cap
     - every line must cite a fact from THIS thesis
     - ALIGNS only where it changes sizing or conviction, max 2
     - TENSION and VIOLATES always permitted
     - the sentinel is a legitimate complete output
-->

- **TENSION VAL-P1** (self, 2026): fair value stated as a point here, not a range.
"""

# The library template's own prescribed shape: an indented `*Texture:*` sub-bullet
# under a takeaway, and a verification tag carrying a qualifier inside the bracket.
# Both were once lint failures — the gate contradicted the template it enforces.
TEMPLATE_SHAPED_ENTRY = """---
title: A Memo
type: memo
author: Howard Marks
published: 2026-01
retrieved-from: https://example.com/memo
tags: [valuation-discipline]
archive: sources/marks-memo.txt
---
**One-line:** Cheapness on fear differs from cheapness on impairment.

## Takeaways
- Distinguish price falling on sentiment from price falling on earnings power (p. 3) [verified]
  - *Texture:* the 1973 case, where both happened to the same names nine months apart
- A relayed claim caps at partial however confident the speaker (p. 7) [partial - relayed via a newsletter; origin in Cites]

## Not captured
- Closing anecdote (pp. 8-9) — colour, no transferable rule
"""

PODCAST_TIMED = """---
title: An Episode
type: podcast
author: Some Host
published: 2026-02
retrieved-from: https://example.com/ep
source-span: "0:00-40:00"
tags: [valuation-discipline]
---
**One-line:** Talk.

## Takeaways
- A claim (1:00) [verified]

## Not captured
- Intro banter (0:00-0:30) — no content
"""

CASES = [
    # -- baseline -----------------------------------------------------------
    case("clean vault passes", noop, expect_fail=False),

    # -- 1. cross-references ------------------------------------------------
    case("broken markdown link", append("principles/README.md", "\nSee [gone](nope.md)\n"),
         expect_fail=True, needle="broken reference"),

    # -- 2. permanent IDs ---------------------------------------------------
    case("dangling ID citation", append("library/marks-memo.md", "\nSupports VAL-P9.\n"),
         expect_fail=True, needle="VAL-P9"),
    case("foreign-prefix bold definition",
         append("library/marks-memo.md", "\n**VAL-P2** — squatting on the owner's namespace.\n"),
         expect_fail=True, needle="bold-defines"),
    case("duplicate ID definition",
         append("principles/valuation-discipline.md",
                "\n### VAL-P1 — duplicate\n**VAL-P1** — same ID twice.\n"
                "`[evidence: emerging | my record: untested]` (as-of 2026-07-28)\n"),
         expect_fail=True, needle="defined 2 times"),
    case("valid ID citation passes",
         append("library/marks-memo.md", "\nCorroborates VAL-P1.\n"), expect_fail=False),

    # -- 3. library schema --------------------------------------------------
    case("library entry missing Not captured",
         replace("library/marks-memo.md", "## Not captured\n- Closing anecdote (pp. 8-9) — colour, no transferable rule\n", ""),
         expect_fail=True, needle="Not captured"),
    case("takeaway without locator",
         replace("library/marks-memo.md", "(p. 3) [verified]", "[verified]"),
         expect_fail=True, needle="lacks a locator"),
    case("takeaway without verification tag",
         replace("library/marks-memo.md", "(p. 3) [verified]", "(p. 3)"),
         expect_fail=True, needle="verification tag"),
    case("missing required frontmatter key",
         replace("library/marks-memo.md", "author: Howard Marks\n", ""),
         expect_fail=True, needle="missing required key"),
    case("archive slug mismatch",
         replace("library/marks-memo.md", "archive: sources/marks-memo.txt",
                 "archive: sources/some-other-name.txt"),
         expect_fail=True, needle="does not share the entry slug"),

    case("template-shaped entry passes: indented texture, qualified tag",
         edit("library/marks-memo.md", TEMPLATE_SHAPED_ENTRY), expect_fail=False),
    case("an untagged TOP-LEVEL takeaway is still caught",
         edit("library/marks-memo.md",
              TEMPLATE_SHAPED_ENTRY.replace("(p. 3) [verified]", "(p. 3)")),
         expect_fail=True, needle="verification tag"),

    # -- 4. gap partition ---------------------------------------------------
    # These three share an indexed ep.md so the ONLY possible error is the gap
    # rule itself — otherwise "untimed passes" would pass for the wrong reason
    # (a missing index row) and prove nothing about interval math being skipped.
    case("podcast without source-span",
         add_episode(PODCAST_TIMED.replace('source-span: "0:00-40:00"\n', "")),
         expect_fail=True, needle="requires `source-span`"),
    case("timed podcast with unaccounted stretch",
         add_episode(PODCAST_TIMED),
         expect_fail=True, needle="unaccounted source stretch"),
    case("timed podcast with full coverage passes",
         add_episode(PODCAST_TIMED.replace(
             "## Not captured\n- Intro banter (0:00-0:30) — no content\n",
             "## Not captured\n- Banter and sponsor reads (0:00-0:30, 2:00, 7:00, 12:00, 17:00, "
             "22:00, 27:00, 32:00, 37:00, 40:00) — no transferable content\n")),
         expect_fail=False),
    case("untimed podcast skips interval math",
         add_episode(PODCAST_TIMED.replace('"0:00-40:00"', "untimed")),
         expect_fail=False),

    # -- 5. index bijection / prefixes --------------------------------------
    case("non-index table is not read as index rows",
         append("principles/README.md", ROUTING_TABLE), expect_fail=False),
    case("README without an Index section is rejected",
         edit("principles/README.md", "# Principles\n\nNo index here.\n"),
         expect_fail=True, needle="no `## Index` section"),
    case("library entry with no index row",
         edit("library/orphan.md", CLEAN["library/marks-memo.md"].replace(
             "archive: sources/marks-memo.txt", "archive: sources/orphan.txt")),
         expect_fail=True, needle="no index row"),
    case("duplicate prefix across principle files",
         edit("principles/other.md", CLEAN["principles/valuation-discipline.md"]
              .replace("theme: valuation-discipline", "theme: other")
              .replace("### VAL-P1 — Fair value is a range", "### VAL-P7 — Other")
              .replace("**VAL-P1** —", "**VAL-P7** —")),
         expect_fail=True, needle="claimed by multiple files"),

    # -- 6. thesis shape ----------------------------------------------------
    case("pre-cutover thesis is grandfathered", noop, expect_fail=False,
         env={"BERKSHIRE_PRINCIPLES_CUTOVER": "2026-07-01"}),
    case("post-cutover thesis without Principles check",
         replace("sectors/x/companies/AAA/thesis.md", "### 2026-05-20 — initial thesis",
                 "### 2026-07-20 — deep-dive refresh"),
         expect_fail=True, needle="no `## Principles check`",
         env={"BERKSHIRE_PRINCIPLES_CUTOVER": "2026-07-01"}),
    case("post-cutover thesis with valid Principles check",
         lambda f: (
             replace("sectors/x/companies/AAA/thesis.md", "### 2026-05-20 — initial thesis",
                     "### 2026-07-20 — deep-dive refresh")(f),
             replace("sectors/x/companies/AAA/thesis.md", "## Conviction",
                     "## Principles check\n- **TENSION VAL-P1** (self, 2026): FV stated as a point here.\n\n## Conviction")(f),
         ),
         expect_fail=False, env={"BERKSHIRE_PRINCIPLES_CUTOVER": "2026-07-01"}),
    case("Principles check over the line cap",
         lambda f: (
             replace("sectors/x/companies/AAA/thesis.md", "### 2026-05-20 — initial thesis",
                     "### 2026-07-20 — deep-dive refresh")(f),
             replace("sectors/x/companies/AAA/thesis.md", "## Conviction",
                     "## Principles check\n" + "".join(
                         f"- **ALIGNS VAL-P1** (self): line {i}.\n" for i in range(6)
                     ) + "\n## Conviction")(f),
         ),
         expect_fail=True, needle="max 5", env={"BERKSHIRE_PRINCIPLES_CUTOVER": "2026-07-01"}),
    case("sentinel with too few reviewed slugs",
         lambda f: (
             replace("sectors/x/companies/AAA/thesis.md", "### 2026-05-20 — initial thesis",
                     "### 2026-07-20 — deep-dive refresh")(f),
             replace("sectors/x/companies/AAA/thesis.md", "## Conviction",
                     "## Principles check\n- No stored principle bears on this situation "
                     "(reviewed: valuation-discipline, process-discipline)\n\n## Conviction")(f),
         ),
         expect_fail=True, needle="reviewed slug", env={"BERKSHIRE_PRINCIPLES_CUTOVER": "2026-07-01"}),
    case("verdict line without a verdict token",
         lambda f: (
             replace("sectors/x/companies/AAA/thesis.md", "### 2026-05-20 — initial thesis",
                     "### 2026-07-20 — deep-dive refresh")(f),
             replace("sectors/x/companies/AAA/thesis.md", "## Conviction",
                     "## Principles check\n- Broadly consistent with value investing principles.\n\n## Conviction")(f),
         ),
         expect_fail=True, needle="verdict token", env={"BERKSHIRE_PRINCIPLES_CUTOVER": "2026-07-01"}),

    case("HTML comment bullets do not count toward the line cap",
         lambda f: (
             replace("sectors/x/companies/AAA/thesis.md", "### 2026-05-20 — initial thesis",
                     "### 2026-07-20 — deep-dive refresh")(f),
             replace("sectors/x/companies/AAA/thesis.md", "## Conviction",
                     COMMENTED_CHECK + "\n## Conviction")(f),
         ),
         expect_fail=False, env={"BERKSHIRE_PRINCIPLES_CUTOVER": "2026-07-01"}),

    # -- 7. append-only (staged mode only) ----------------------------------
    case("removing a dated journal line is blocked",
         edit("journal/2026-05-20-decision.md", "# Decisions — 2026-05-20\n\n(nothing here now)\n"),
         expect_fail=True, needle="append-only", staged=True, commit_first=True),
    case("appending a dated journal line is allowed",
         append("journal/2026-05-20-decision.md", "- 2026-05-21 — ADD AAA.\n"),
         expect_fail=False, staged=True, commit_first=True),
    case("rewriting a thesis Update-log line is blocked",
         replace("sectors/x/companies/AAA/thesis.md",
                 "### 2026-05-20 — initial thesis", "### 2026-05-20 — revised history"),
         expect_fail=True, needle="append-only", staged=True, commit_first=True),

    # -- 8. evidence tags ---------------------------------------------------
    # BOTH directions, deliberately. A regex bug once made these two negative cases
    # pass for the wrong reason: the voice-line pattern matched nothing at all, so
    # every block counted zero voices. Rejecting correctly while also rejecting
    # everything valid is indistinguishable from working, unless the positive case
    # is asserted too.
    case("well-supported without three voices",
         replace("principles/valuation-discipline.md",
                 "[evidence: emerging | my record: untested]",
                 "[evidence: well-supported | my record: untested]"),
         expect_fail=True, needle="well-supported"),
    case("well-supported WITH three voices and a verified source passes",
         replace("principles/valuation-discipline.md",
                 "`[evidence: emerging | my record: untested]` (as-of 2026-07-28)\n"
                 "- **Voices:** **agrees** — Owner, self, 2026 [unverified]: written into the vault's canon (holds when: always)",
                 "`[evidence: well-supported | my record: untested]` (as-of 2026-07-28)\n"
                 "- **Voices:** **agrees** — Howard Marks, Oaktree memo, 2025 [verified]: scenario ranges over points (holds when: outcomes are genuinely distributional)\n"
                 "- **Voices:** **agrees** — Owner, self, 2026 [unverified]: written into the vault's canon (holds when: always)\n"
                 "- **Voices:** **qualifies** — Aswath Damodaran, blog, 2024 [partial]: a range wide enough to be safe can be too wide to act on (holds when: the range spans the decision threshold)"),
         expect_fail=False),
    case("contested without a dissenting voice",
         replace("principles/valuation-discipline.md",
                 "[evidence: emerging | my record: untested]",
                 "[evidence: contested | my record: untested]"),
         expect_fail=True, needle="diverges"),
    case("contested WITH a dissenting voice passes",
         replace("principles/valuation-discipline.md",
                 "`[evidence: emerging | my record: untested]` (as-of 2026-07-28)",
                 "`[evidence: contested | my record: untested]` (as-of 2026-07-28)\n"
                 "- **Voices:** **diverges** — Some Practitioner, letter, 2024 [unverified]: a point estimate forces a decision a range lets you dodge (holds when: the mandate requires a single number)"),
         expect_fail=False),
    case("block without an evidence tag",
         replace("principles/valuation-discipline.md",
                 "`[evidence: emerging | my record: untested]` (as-of 2026-07-28)\n", ""),
         expect_fail=True, needle="no [evidence"),
    case("unknown evidence level",
         replace("principles/valuation-discipline.md",
                 "[evidence: emerging |", "[evidence: rock-solid |"),
         expect_fail=True, needle="not in"),
]


def check_no_placeholder_cutover():
    """The cutover constant must be a real date, not a far-future placeholder.

    It shipped as "2099-01-01", which grandfathered every thesis in the vault and
    made the Principles-check gate inert while the lint still reported [OK]. No
    planted-violation case could catch it: the fixture theses are correctly
    post-cutover under any sane value, so the suite stayed green. The defect was in
    the CONSTANT, not the logic, so this asserts on the constant directly.
    """
    src = (REPO_ROOT / LINT).read_text(encoding="utf-8")
    m = re.search(r'BERKSHIRE_PRINCIPLES_CUTOVER"\s*,\s*"(\d{4})-(\d{2})-(\d{2})"', src)
    if not m:
        return "could not find the PRINCIPLES_CHECK_CUTOVER default in the lint source"
    if int(m.group(1)) > date.today().year + 1:
        return (f"cutover default is {m.group(1)}-{m.group(2)}-{m.group(3)} - a far-future "
                "placeholder grandfathers every thesis and makes the check inert")
    return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--verbose", action="store_true")
    args = ap.parse_args()

    passed = failed = 0
    for c in CASES:
        files = dict(CLEAN)
        with tempfile.TemporaryDirectory(prefix="berkshire-lint-test-") as td:
            tmp = Path(td)
            if c["staged"]:
                build(tmp, files)
                git(tmp, "init", "-q")
                git(tmp, "config", "user.email", "t@t")
                git(tmp, "config", "user.name", "t")
                git(tmp, "add", "-A")
                git(tmp, "commit", "-q", "-m", "base")
                c["mutate"](files)
                for rel, body in files.items():
                    p = tmp / rel
                    p.parent.mkdir(parents=True, exist_ok=True)
                    p.write_text(body, encoding="utf-8", newline="\n")
                git(tmp, "add", "-A")
            else:
                c["mutate"](files)
                build(tmp, files)

            code, out = run_lint(tmp, staged=c["staged"], env_extra=c["env"])

        did_fail = code != 0
        ok = did_fail == c["expect_fail"]
        if ok and c["expect_fail"] and c["needle"]:
            ok = c["needle"].lower() in out.lower()
        status = "PASS" if ok else "FAIL"
        want = "reject" if c["expect_fail"] else "accept"
        print(f"[{status}] {c['name']} (expected {want}, exit {code})")
        if not ok or args.verbose:
            for line in out.strip().splitlines():
                print(f"        {line}")
        passed += ok
        failed += not ok

    problem = check_no_placeholder_cutover()
    if problem:
        print(f"[FAIL] constant guard: {problem}")
        failed += 1
    else:
        print("[PASS] constant guard: cutover is a real date, not a placeholder")

    print(f"\n{passed}/{passed + failed} cases pass.")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
