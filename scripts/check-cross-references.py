"""Repo integrity checker for the berkshire vault — the one pre-commit gate.

Eight check classes, all commit-blocking. Every one of them exists because a
specific failure is otherwise silent:

  1. CROSS-REFERENCES — markdown links and backticked paths resolve on disk.
  2. PERMANENT IDS      — every {PREFIX}-{P|M|T}{n} token resolves to exactly one
                          bold definition in the principle file that owns the
                          prefix. Dangling or mistyped citations are blocked.
  3. LIBRARY SCHEMA     — required frontmatter, non-empty "## Not captured",
                          per-takeaway locator + verification tag, 1:1:1 archive
                          pairing.
  4. GAP PARTITION      — for timed podcast/interview entries: the union of
                          takeaway + leftover locators must cover source-span
                          with no unaccounted stretch. Catches "silently dropped
                          a method mid-transcript" — which is not hypothetical,
                          it happened on the sibling vault's first real absorb.
  5. INDEX BIJECTION    — every library entry and principle file has exactly one
                          index row, and vice versa. Prefixes are unique.
  6. THESIS SHAPE       — post-cutover theses carry a "## Principles check" with
                          1-5 lines, resolvable IDs, and a legal verdict token
                          (or the exact sentinel).
  7. APPEND-ONLY        — staged journal entries and thesis Update logs may not
                          lose or rewrite existing dated lines. "Append-only" was
                          prose in a README until this check existed.
  8. EVIDENCE TAGS      — a principle claiming `well-supported` must actually
                          carry 3+ Voices lines with >=1 verified tier-1; a
                          `contested` one must carry a dissent. Catches tag/content
                          shear after a block move or split.

MODES
-----
    python scripts/check-cross-references.py            # working tree (manual use)
    python scripts/check-cross-references.py --staged   # staged content (pre-commit)

--staged is what the hook passes, and the distinction is load-bearing. Linting the
working tree at commit time means unrelated half-written work blocks commits it has
nothing to do with — which is how a lint gate teaches people to use --no-verify, and
how `absorb` would strand its own writes when the owner has a draft thesis open
elsewhere. Staged mode reads blobs from the index: exactly what is about to be
committed, nothing else.

Skipped everywhere: URLs, fragment-only links, template placeholders in braces,
and paths under .git/ .obsidian/ .claude/state|cache|logs/ library/_inbox/.
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# ---------------------------------------------------------------- configuration
# Section headings and enums are hoisted here on purpose: the lint couples to
# these exact strings, so a rename must land in the SAME commit that updates
# this block. (Lesson carried over from the sibling vault's schema lint.)

PRINCIPLES_DIR = "principles"
LIBRARY_DIR = "library"

LIBRARY_REQUIRED_FRONTMATTER = ("title", "type", "author", "published", "retrieved-from", "tags")
LIBRARY_TYPES = {
    "letter", "memo", "annual-report", "filing", "book", "article",
    "podcast", "interview", "annual-meeting-transcript", "dataset", "paper",
}
TIMED_TYPES = {"podcast", "interview", "annual-meeting-transcript"}
NOT_CAPTURED_HEADING = "## Not captured"
TAKEAWAYS_HEADING = "## Takeaways"

VERIFICATION_TAGS = {"verified", "partial", "unverified"}
EVIDENCE_LEVELS = {"emerging", "contested", "well-supported"}
RECORD_LEVELS = {"untested", "validated", "mixed"}

PRINCIPLES_CHECK_HEADING = "## Principles check"
VERDICT_TOKENS = {"ALIGNS", "TENSION", "VIOLATES"}
PRINCIPLES_CHECK_MAX_LINES = 5
SENTINEL_RE = re.compile(
    r"No stored principle bears on this situation \(reviewed:\s*([^)]+)\)", re.IGNORECASE
)
SENTINEL_MIN_SLUGS = 3

# Thesis Update-log headings that company-deep-dive actually writes. Keyed on the
# real strings, NOT on a skill name: an earlier draft of this gate looked for
# "— company-deep-dive", which no skill ever emits, so it would have passed
# everything forever while appearing to enforce.
DEEP_DIVE_LOG_RE = re.compile(
    r"^###\s+(\d{4}-\d{2}-\d{2})\s+[—-]\s+(initial thesis|deep-dive refresh)\b",
    re.IGNORECASE | re.MULTILINE,
)
# Set at Phase 5 completion (when company-deep-dive learned to write the section).
# Theses whose newest deep-dive entry predates this are grandfathered — the rule
# cannot apply retroactively to work written before the skill could satisfy it.
# The env override exists so scripts/test-lint.py can exercise this gate against a
# synthetic vault; never set it in normal use.
# The date the Principles check became mandatory: when the grafts landed in the
# skills that write theses. A thesis whose newest deep-dive entry predates this is
# grandfathered — NKE, ADBE and UNH were all written before the principles tier
# existed and cannot retroactively cite it; they acquire the section at their next
# refresh, which is when the skill will produce it.
#
# This sat at "2099-01-01" for two days, which grandfathered EVERY thesis past and
# future and made this whole check inert while reporting [OK]. It was caught by a
# deep-dive agent reading the source to get the section's shape right, not by the
# lint or the self-test. Sixth instance of this vault's signature failure: a gate
# that reports green while enforcing nothing. test-lint.py now fails if a
# placeholder-shaped far-future date ever reappears here.
PRINCIPLES_CHECK_CUTOVER = os.environ.get(
    "BERKSHIRE_PRINCIPLES_CUTOVER", "2026-07-28"
)

APPEND_ONLY_GLOBS = ("journal/*.md",)
UPDATE_LOG_HEADING = "## Update log"
# journal/_flagged.md is the one sanctioned in-place edit: active -> resolved
# rewrites a line by design (documented in the file's own header).
APPEND_ONLY_EXEMPT_INPLACE = {"journal/_flagged.md"}

# Frameworks and principles were append-only by CONVENTION only, with no gate at
# all — found the day this was added, when an Edit call inserted new learned-log
# entries above the file's last existing bullet instead of after it (caught and
# repaired by hand, nothing lost, but a future agent doing the same thing would
# silently reorder history with no lint to catch it).
#
# frameworks/*.md: append-only is scoped to ONE section, "## What I've learned
# over time" — the rest of a framework (KPIs, red flags, valuation logic) is
# meant to be rewritten as understanding improves; only the dated learning log
# is a historical record.
FRAMEWORK_LEARNED_HEADING = "## What I've learned over time"

# principles/*.md: unlike a framework, the ITEM BODIES (the rule statement,
# Voices lines, evidence/my-record tags) are legitimately rewritten in place —
# "Tiered autowrite (canonical)" makes a statement rewrite glance-confirm, not
# forbidden, and the audit-fix pass corrected several the same day this file was
# seeded. Only each item's own "- **Log:**" sub-list is the append-only evidence
# ledger. Checked as the flat set of every nested "  - " bullet in the file
# (verified against all six seeded files: every such bullet is a Log entry —
# Voices and My-record are single, unindented lines) rather than per-item, since
# set-membership already tolerates an item's Log block being reordered or a new
# item being inserted between two existing ones.
PRINCIPLE_LOG_LINE_RE = re.compile(r"^  - .+")

LINK_PATTERN = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")
BACKTICK_PATH_PATTERN = re.compile(r"`(\.{1,2}/[^`]+\.md|[a-zA-Z0-9_\-./]+/[a-zA-Z0-9_\-./]+\.md)`")
DATED_LINE_RE = re.compile(r"\d{4}-\d{2}-\d{2}")

SKIP_PREFIXES = (
    (".git",),
    (".obsidian",),
    (".claude", "state"),
    (".claude", "cache"),
    (".claude", "logs"),
    ("library", "_inbox"),
    ("library", "sources"),
)

EXEMPT_PATH_PARTS = ("_example", "_template.md")


# ------------------------------------------------------------------- file access
class Corpus:
    """Uniform access to either the working tree or the git index."""

    def __init__(self, staged: bool):
        self.staged = staged
        self._cache: dict[str, str] = {}
        self._paths: list[str] | None = None

    def _git(self, *args: str) -> str:
        out = subprocess.run(
            ["git", "-C", str(REPO_ROOT), *args],
            capture_output=True, text=True, encoding="utf-8", errors="replace",
        )
        return out.stdout

    def paths(self) -> list[str]:
        """Repo-relative posix paths of all .md files in scope."""
        if self._paths is not None:
            return self._paths
        if self.staged:
            names = [p for p in self._git("diff", "--cached", "--name-only", "--diff-filter=ACMR")
                     .splitlines() if p.endswith(".md")]
            # A staged commit must be linted in the context of the whole corpus:
            # an ID defined in an unmodified file still has to resolve. So take
            # HEAD's tree plus staged additions.
            head = [p for p in self._git("ls-tree", "-r", "--name-only", "HEAD").splitlines()
                    if p.endswith(".md")]
            names = sorted(set(head) | set(names))
        else:
            names = sorted(
                p.relative_to(REPO_ROOT).as_posix()
                for p in REPO_ROOT.rglob("*.md")
            )
        self._paths = [p for p in names if not self._skipped(p)]
        return self._paths

    @staticmethod
    def _skipped(rel: str) -> bool:
        parts = tuple(rel.split("/"))
        return any(parts[: len(pref)] == pref for pref in SKIP_PREFIXES)

    def read(self, rel: str) -> str:
        if rel in self._cache:
            return self._cache[rel]
        text = ""
        if self.staged:
            text = self._git("show", f":{rel}")
            if not text:  # not staged (unchanged file) -> read from HEAD
                text = self._git("show", f"HEAD:{rel}")
        else:
            path = REPO_ROOT / rel
            try:
                text = path.read_text(encoding="utf-8")
            except (OSError, UnicodeDecodeError):
                text = ""
        self._cache[rel] = text
        return text

    def read_head(self, rel: str) -> str:
        return self._git("show", f"HEAD:{rel}")

    def staged_md_paths(self) -> list[str]:
        if not self.staged:
            return []
        return [p for p in self._git("diff", "--cached", "--name-only", "--diff-filter=ACMR")
                .splitlines() if p.endswith(".md")]

    def exists(self, rel: str) -> bool:
        """Does this path exist as a file (in the relevant corpus)?"""
        if self.staged:
            if rel in set(self.paths()):
                return True
            out = self._git("cat-file", "-e", f":{rel}")  # noqa: F841 - exit code via stderr
            # cat-file -e writes nothing; fall back to ls-files for correctness
            listed = self._git("ls-files", "--", rel).strip()
            if listed:
                return True
            return (REPO_ROOT / rel).exists()
        return (REPO_ROOT / rel).exists()


def is_exempt(rel: str) -> bool:
    return any(part in rel for part in EXEMPT_PATH_PARTS)


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    out: dict[str, str] = {}
    for line in text[3:end].splitlines():
        if ":" in line and not line.strip().startswith("#"):
            k, v = line.split(":", 1)
            out[k.strip()] = v.split(" #")[0].strip().strip('"').strip("'")
    return out


def section(text: str, heading: str) -> str | None:
    """Body of a '## Heading' section, up to the next same-or-higher heading."""
    lines = text.splitlines()
    depth = len(heading) - len(heading.lstrip("#"))
    start = None
    for i, line in enumerate(lines):
        if line.strip().lower() == heading.lower():
            start = i + 1
            break
    if start is None:
        return None
    body: list[str] = []
    for line in lines[start:]:
        stripped = line.lstrip("#")
        d = len(line) - len(stripped)
        if line.startswith("#") and 0 < d <= depth:
            break
        body.append(line)
    return "\n".join(body)


# ------------------------------------------------------------------ check 1: refs
def is_skippable_target(target: str) -> bool:
    if target.startswith(("http://", "https://", "mailto:")):
        return True
    if target.startswith("#"):
        return True
    if "{" in target or "}" in target:
        return True
    return False


def extract_references(content: str) -> list[str]:
    refs: list[str] = []
    for _, target in LINK_PATTERN.findall(content):
        target = target.split("#", 1)[0].strip()
        # Links may be wrapped in <> and/or percent-encoded.
        if target.startswith("<") and target.endswith(">"):
            target = target[1:-1].strip()
        if target:
            refs.append(target)
    for target in BACKTICK_PATH_PATTERN.findall(content):
        refs.append(target.strip())
    return refs


def unquote(target: str) -> str:
    from urllib.parse import unquote as _u
    return _u(target)


def check_references(corpus: Corpus, errors: list[str]) -> int:
    checked = 0
    for rel in corpus.paths():
        content = corpus.read(rel)
        for target in extract_references(content):
            if is_skippable_target(target):
                continue
            checked += 1
            base = Path(rel).parent
            for cand in (base / target, Path(target), base / unquote(target), Path(unquote(target))):
                try:
                    norm = Path(*cand.parts).as_posix()
                    resolved = (REPO_ROOT / norm).resolve()
                    resolved.relative_to(REPO_ROOT)
                except ValueError:
                    continue
                candidate_rel = resolved.relative_to(REPO_ROOT).as_posix()
                if corpus.exists(candidate_rel) or resolved.exists():
                    break
            else:
                errors.append(f"{rel}: broken reference `{target}`")
    return checked


# ------------------------------------------------------------ check 2: unique IDs
def prefix_registry(corpus: Corpus) -> dict[str, str]:
    """Map PREFIX -> owning principle file, from frontmatter. The registry is what
    makes ID matching safe: only declared prefixes are ID-shaped, so tickers
    (BRK-B), filing items (8-K) and index names can never false-positive."""
    reg: dict[str, str] = {}
    for rel in corpus.paths():
        if not rel.startswith(f"{PRINCIPLES_DIR}/") or is_exempt(rel):
            continue
        fm = frontmatter(corpus.read(rel))
        pref = fm.get("prefix", "").strip()
        if pref:
            reg.setdefault(pref, rel)
    return reg


def check_ids(corpus: Corpus, errors: list[str]) -> int:
    reg = prefix_registry(corpus)
    if not reg:
        return 0
    id_re = re.compile(r"\b(" + "|".join(sorted(map(re.escape, reg))) + r")-([PMT])(\d+)\b")
    bold_re = re.compile(r"\*\*(" + "|".join(sorted(map(re.escape, reg))) + r")-([PMT])(\d+)\*\*")

    definitions: dict[str, list[str]] = {}
    references: dict[str, list[str]] = {}
    for rel in corpus.paths():
        if is_exempt(rel):
            continue
        text = corpus.read(rel)
        for pref, kind, num in bold_re.findall(text):
            tok = f"{pref}-{kind}{num}"
            definitions.setdefault(tok, []).append(rel)
            owner = reg[pref]
            if rel != owner:
                errors.append(
                    f"{rel}: bold-defines {tok}, but prefix {pref} is owned by {owner} "
                    f"(bold form is reserved for the owning file; cite plainly instead)"
                )
        for pref, kind, num in id_re.findall(text):
            references.setdefault(f"{pref}-{kind}{num}", []).append(rel)

    for tok, files in sorted(definitions.items()):
        owner_defs = [f for f in files if f == reg[tok.split("-")[0]]]
        if len(owner_defs) > 1:
            errors.append(f"{tok}: defined {len(owner_defs)} times in {owner_defs[0]} (must be unique)")

    for tok, files in sorted(references.items()):
        if tok not in definitions:
            where = ", ".join(sorted(set(files))[:3])
            errors.append(f"{tok}: referenced in {where} but never bold-defined in {reg[tok.split('-')[0]]}")
    return len(references)


# ------------------------------------------------- checks 3+4: library entries
LOCATOR_RE = re.compile(r"\((?:p\.?\s*\d+(?:\s*-\s*\d+)?|pp\.?\s*\d+\s*-\s*\d+|\d{1,2}:\d{2}(?::\d{2})?(?:\s*-\s*\d{1,2}:\d{2}(?::\d{2})?)?|§[^)]+|para\.?\s*\d+|[^)]*\bsec(?:tion)?\.?\s*[\w.]+)\)", re.IGNORECASE)
# A tag may carry a qualifier inside the bracket — `[partial — relayed from X, origin
# in Cites]` is better writing than a bare `[partial]` with the reason stranded in
# prose, and the tag stays machine-readable either way. Requiring the bracket to hold
# nothing but the word made the honest form of the label a lint failure.
TAG_RE = re.compile(r"\[(" + "|".join(VERIFICATION_TAGS) + r")(?:\s*[—\-–][^\]]*)?\]")
TIME_RE = re.compile(r"(\d{1,2}):(\d{2})(?::(\d{2}))?")


def to_seconds(stamp: str) -> int | None:
    m = TIME_RE.fullmatch(stamp.strip())
    if not m:
        return None
    a, b, c = m.group(1), m.group(2), m.group(3)
    if c is not None:
        return int(a) * 3600 + int(b) * 60 + int(c)
    return int(a) * 60 + int(b)


HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)


def top_level_bullets(body: str) -> list[str]:
    """Unindented bullets only, HTML comments stripped.

    A nested bullet belongs to the takeaway above it (the template's `*Texture:*`
    line), so it is not an independent claim needing its own locator and tag.
    """
    visible = HTML_COMMENT_RE.sub("", body)
    return [
        ln for ln in visible.splitlines()
        if ln[:1] in ("-", "*") and ln.strip() not in ("-", "*")
    ]


def bullet_lines(body: str) -> list[str]:
    """Bullets at any indent, with HTML comments stripped first.

    Templates and theses legitimately carry explanatory comments, and those
    comments contain dashed lists. Counting them as content made the Principles
    check's 5-line cap fire on a thesis whose visible section had two lines —
    i.e. the lint would have taught authors to write worse comments to appease it.
    """
    visible = HTML_COMMENT_RE.sub("", body)
    return [ln.strip() for ln in visible.splitlines() if ln.strip().startswith(("-", "*"))]


def check_library(corpus: Corpus, errors: list[str]) -> int:
    n = 0
    for rel in corpus.paths():
        if not rel.startswith(f"{LIBRARY_DIR}/") or is_exempt(rel):
            continue
        if Path(rel).name in ("README.md",):
            continue
        if len(Path(rel).parts) != 2:  # library/{slug}.md only
            continue
        n += 1
        text = corpus.read(rel)
        fm = frontmatter(text)
        for key in LIBRARY_REQUIRED_FRONTMATTER:
            if not fm.get(key):
                errors.append(f"{rel}: frontmatter missing required key `{key}`")
        typ = fm.get("type", "")
        if typ and typ not in LIBRARY_TYPES:
            errors.append(f"{rel}: type `{typ}` not one of {sorted(LIBRARY_TYPES)}")

        takeaways = section(text, TAKEAWAYS_HEADING)
        if takeaways is None:
            errors.append(f"{rel}: missing `{TAKEAWAYS_HEADING}`")
        else:
            # TOP-LEVEL bullets only. An indented sub-bullet is a continuation of its
            # parent takeaway — library/_template.md prescribes exactly that shape for
            # the required `*Texture:*` line — so demanding its own locator and tag made
            # the template's own form unlintable, and would have pushed authors to drop
            # the texture line rather than fight the gate.
            bullets = top_level_bullets(takeaways)
            if not bullets:
                errors.append(f"{rel}: `{TAKEAWAYS_HEADING}` is empty")
            for b in bullets:
                if not LOCATOR_RE.search(b):
                    errors.append(f"{rel}: takeaway lacks a locator: {b.strip()[:70]}")
                if not TAG_RE.search(b):
                    errors.append(f"{rel}: takeaway lacks a verification tag: {b.strip()[:70]}")

        leftovers = section(text, NOT_CAPTURED_HEADING)
        if leftovers is None:
            errors.append(f"{rel}: missing required `{NOT_CAPTURED_HEADING}` section")
        elif not leftovers.strip():
            errors.append(
                f"{rel}: `{NOT_CAPTURED_HEADING}` is empty — silent truncation reads as "
                f"'covered everything'; state what was skipped and why"
            )

        archive = fm.get("archive", "")
        if archive and not archive.lower().startswith("none"):
            slug = Path(rel).stem
            for chunk in archive.split(","):
                chunk = chunk.strip()
                if not chunk:
                    continue
                name = chunk.split("/")[-1]
                if name and not name.startswith(slug):
                    errors.append(
                        f"{rel}: archive `{name}` does not share the entry slug `{slug}` "
                        f"(1:1:1 pairing keeps locators addressable)"
                    )

        span = fm.get("source-span", "")
        if typ in TIMED_TYPES and not span:
            errors.append(
                f"{rel}: type `{typ}` requires `source-span` (use `untimed` when the "
                f"transcript carries no native timestamps)"
            )
        if span and span.strip().lower() != "untimed" and takeaways is not None:
            check_gap_partition(rel, span, takeaways, section(text, NOT_CAPTURED_HEADING) or "", errors)
    return n


GAP_BUFFER_SECONDS = 30
GAP_THRESHOLD_SECONDS = 6 * 60


def check_gap_partition(rel: str, span: str, takeaways: str, leftovers: str, errors: list[str]) -> None:
    """Union takeaway + leftover timestamp locators; fail on an unaccounted stretch.

    Constants (30s buffer / 6min threshold) are replay-tested in the sibling vault
    against the real incident that motivated them: a looser 90s/8min pair silently
    swallowed an 8:46 gap that contained a dropped five-question method. Do not
    'tidy' these numbers without re-running that replay.
    """
    m = re.search(r"(\d{1,2}:\d{2}(?::\d{2})?)\s*-\s*(\d{1,2}:\d{2}(?::\d{2})?)", span)
    if not m:
        return  # page-based or malformed span: nothing to interval-check
    start, end = to_seconds(m.group(1)), to_seconds(m.group(2))
    if start is None or end is None or end <= start:
        return
    marks: list[tuple[int, int]] = []
    for body in (takeaways, leftovers):
        for stamp in TIME_RE.finditer(body):
            sec = to_seconds(stamp.group(0))
            if sec is None:
                continue
            marks.append((max(start, sec - GAP_BUFFER_SECONDS), min(end, sec + GAP_BUFFER_SECONDS)))
    if not marks:
        errors.append(f"{rel}: source-span is timed but no timestamp locators found")
        return
    marks.sort()
    merged: list[list[int]] = [list(marks[0])]
    for lo, hi in marks[1:]:
        if lo <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], hi)
        else:
            merged.append([lo, hi])
    cursor = start
    for lo, hi in merged:
        if lo - cursor > GAP_THRESHOLD_SECONDS:
            errors.append(
                f"{rel}: unaccounted source stretch {cursor // 60}:{cursor % 60:02d}-"
                f"{lo // 60}:{lo % 60:02d} ({(lo - cursor) // 60}min) — no takeaway cites it and "
                f"`{NOT_CAPTURED_HEADING}` does not explain it"
            )
        cursor = max(cursor, hi)
    if end - cursor > GAP_THRESHOLD_SECONDS:
        errors.append(
            f"{rel}: unaccounted source stretch {cursor // 60}:{cursor % 60:02d}-"
            f"{end // 60}:{end % 60:02d} ({(end - cursor) // 60}min) at the end of the source"
        )


# --------------------------------------------------------- check 5: index rows
def index_rows(text: str) -> set[str]:
    """Slugs an index table actually LINKS to, from markdown or wiki links or an
    explicit .md filename.

    Deliberately NOT "any lowercase word in a cell": that heuristic read the Type
    column value `memo` as a slug and demanded a nonexistent library/memo.md —
    caught by scripts/test-lint.py. A lint that invents work blocks innocent
    commits and teaches --no-verify, so index rows must reference their file
    explicitly. (Linking also gives Obsidian real navigation, so this costs
    nothing.)
    """
    found: set[str] = set()
    for line in text.splitlines():
        if not line.strip().startswith("|"):
            continue
        for cell in line.strip().strip("|").split("|"):
            cell = cell.strip()
            for m in re.finditer(r"\[[^\]]*\]\(([^)]+)\)", cell):
                found.add(Path(m.group(1).split("#", 1)[0]).stem)
            for m in re.finditer(r"\[\[([^\]|#]+)", cell):
                found.add(Path(m.group(1).strip()).stem)
            bare = cell.strip("`").strip()
            if bare.endswith(".md"):
                found.add(Path(bare).stem)
    return found


def check_indexes(corpus: Corpus, errors: list[str]) -> None:
    paths = set(corpus.paths())
    for tier in (PRINCIPLES_DIR, LIBRARY_DIR):
        readme = f"{tier}/README.md"
        if readme not in paths:
            continue
        # Only the table under "## Index" is the index. A README legitimately holds
        # other tables — principles/README.md has a routing table naming
        # sectors/.../thesis.md and an alias table — and reading those as index rows
        # demanded a nonexistent principles/thesis.md (caught by test-lint.py).
        body = section(corpus.read(readme), "## Index")
        if body is None:
            errors.append(f"{readme}: no `## Index` section (the index is what makes routing trustworthy)")
            continue
        listed = index_rows(body)
        actual = {
            Path(p).stem for p in paths
            if p.startswith(f"{tier}/") and len(Path(p).parts) == 2
            and Path(p).name not in ("README.md",) and not is_exempt(p)
        }
        for slug in sorted(actual - listed):
            errors.append(f"{readme}: no index row for {tier}/{slug}.md")
        for slug in sorted(listed - actual):
            if slug in ("README", "_template"):
                continue
            errors.append(f"{readme}: index row `{slug}` has no matching {tier}/{slug}.md")

    reg: dict[str, list[str]] = {}
    for rel in sorted(paths):
        if rel.startswith(f"{PRINCIPLES_DIR}/") and not is_exempt(rel):
            pref = frontmatter(corpus.read(rel)).get("prefix", "").strip()
            if pref:
                reg.setdefault(pref, []).append(rel)
    for pref, files in sorted(reg.items()):
        if len(files) > 1:
            errors.append(f"prefix `{pref}` claimed by multiple files: {', '.join(files)}")


# -------------------------------------------------------- check 6: thesis shape
def check_thesis_shape(corpus: Corpus, errors: list[str]) -> None:
    for rel in corpus.paths():
        parts = Path(rel).parts
        if not (len(parts) == 5 and parts[0] == "sectors" and parts[2] == "companies"
                and parts[4] == "thesis.md"):
            continue
        if is_exempt(rel):
            continue
        text = corpus.read(rel)
        dates = [d for d, _ in DEEP_DIVE_LOG_RE.findall(text)]
        if not dates or max(dates) < PRINCIPLES_CHECK_CUTOVER:
            continue  # grandfathered: written before the skill could satisfy the rule
        body = section(text, PRINCIPLES_CHECK_HEADING)
        if body is None:
            errors.append(
                f"{rel}: deep-dive dated {max(dates)} is post-cutover but has no "
                f"`{PRINCIPLES_CHECK_HEADING}` section"
            )
            continue
        lines = bullet_lines(body)
        if not lines:
            errors.append(f"{rel}: `{PRINCIPLES_CHECK_HEADING}` is empty")
            continue
        if len(lines) > PRINCIPLES_CHECK_MAX_LINES:
            errors.append(
                f"{rel}: `{PRINCIPLES_CHECK_HEADING}` has {len(lines)} lines "
                f"(max {PRINCIPLES_CHECK_MAX_LINES} — scarcity forces selection)"
            )
        for ln in lines:
            sent = SENTINEL_RE.search(ln)
            if sent:
                slugs = [s.strip() for s in re.split(r"[,;]", sent.group(1)) if s.strip()]
                if len(slugs) < SENTINEL_MIN_SLUGS:
                    errors.append(
                        f"{rel}: sentinel names {len(slugs)} reviewed slug(s), "
                        f"needs >={SENTINEL_MIN_SLUGS} to evidence the sweep"
                    )
                continue
            if not any(tok in ln for tok in VERDICT_TOKENS):
                errors.append(
                    f"{rel}: principles-check line lacks a verdict token "
                    f"{sorted(VERDICT_TOKENS)}: {ln[:70]}"
                )


# --------------------------------------------------------- check 7: append-only
def check_append_only(corpus: Corpus, errors: list[str]) -> None:
    """Existing dated lines may not disappear or change.

    Only meaningful in staged mode (it diffs HEAD against what is being committed).
    """
    if not corpus.staged:
        return
    for rel in corpus.staged_md_paths():
        journalish = any(Path(rel).match(g) for g in APPEND_ONLY_GLOBS)
        thesis = Path(rel).name == "thesis.md"
        framework = Path(rel).parts[:1] == ("frameworks",) and Path(rel).name not in ("README.md", "_template.md")
        principle = Path(rel).parts[:1] == ("principles",) and Path(rel).name not in ("README.md", "_template.md")
        if not (journalish or thesis or framework or principle) or is_exempt(rel):
            continue
        head = corpus.read_head(rel)
        if not head.strip():
            continue  # new file
        new = corpus.read(rel)
        if rel in APPEND_ONLY_EXEMPT_INPLACE:
            continue
        if thesis:
            head_body, new_body = section(head, UPDATE_LOG_HEADING), section(new, UPDATE_LOG_HEADING)
            if head_body is None or new_body is None:
                continue
            head, new = head_body, new_body
        elif framework:
            head_body, new_body = section(head, FRAMEWORK_LEARNED_HEADING), section(new, FRAMEWORK_LEARNED_HEADING)
            if head_body is None or new_body is None:
                continue  # no learned-log section yet — nothing to protect
            head, new = head_body, new_body
        elif principle:
            # Scope to Log-entry lines only; item bodies above them may be
            # legitimately rewritten and must not trip this check.
            head = "\n".join(ln for ln in head.splitlines() if PRINCIPLE_LOG_LINE_RE.match(ln))
            new = "\n".join(ln for ln in new.splitlines() if PRINCIPLE_LOG_LINE_RE.match(ln))
        new_lines = set(new.splitlines())
        lost = [
            ln for ln in head.splitlines()
            if ln.strip() and DATED_LINE_RE.search(ln) and ln not in new_lines
        ]
        if lost:
            kind = "Log entry" if principle else "dated line"
            errors.append(
                f"{rel}: {len(lost)} existing {kind}(s) removed or rewritten — "
                f"append-only (write a new dated entry that corrects the old one instead). "
                f"First: {lost[0].strip()[:70]}"
            )


# ------------------------------------------------------- check 8: evidence tags
EVIDENCE_TAG_RE = re.compile(
    r"\[\s*evidence:\s*([a-z-]+)\s*\|\s*my record:\s*([a-z-]+)\s*\]", re.IGNORECASE
)
# The template's prescribed shape is `- **Voices:** **diverges** — ...`, so the mood
# marker is the SECOND bold token. An earlier version of this regex required it to be
# the first, and therefore matched zero voice lines in every correctly-formatted block:
# `contested` became impossible to claim, and the `well-supported` gate counted 0 voices
# for everything, so it would have fired on any legitimate promotion. Both directions
# wrong, and both invisible — the self-test's negative cases still passed, for the wrong
# reason. That is why test-lint.py now asserts the POSITIVE direction too: a check that
# only ever rejects is indistinguishable from a check that rejects everything.
VOICE_LINE_RE = re.compile(
    r"^\s*-\s+(?:\*\*Voices:?\*\*\s*)?\*\*(agrees|diverges|qualifies)\*\*",
    re.IGNORECASE | re.MULTILINE,
)


def check_evidence_tags(corpus: Corpus, errors: list[str]) -> None:
    for rel in corpus.paths():
        if not rel.startswith(f"{PRINCIPLES_DIR}/") or is_exempt(rel):
            continue
        if Path(rel).name == "README.md":
            continue
        text = corpus.read(rel)
        # Split into ### blocks so tags are evaluated against their own block.
        blocks = re.split(r"^###\s+", text, flags=re.MULTILINE)[1:]
        for block in blocks:
            title = block.splitlines()[0].strip() if block.splitlines() else "?"
            m = EVIDENCE_TAG_RE.search(block)
            if not m:
                errors.append(f"{rel}: block `{title[:50]}` has no [evidence: … | my record: …] tag")
                continue
            ev, rec = m.group(1).lower(), m.group(2).lower()
            if ev not in EVIDENCE_LEVELS:
                errors.append(f"{rel}: block `{title[:40]}` evidence `{ev}` not in {sorted(EVIDENCE_LEVELS)}")
            if rec not in RECORD_LEVELS:
                errors.append(f"{rel}: block `{title[:40]}` my-record `{rec}` not in {sorted(RECORD_LEVELS)}")
            voices = VOICE_LINE_RE.findall(block)
            verified = len(re.findall(r"\[verified\]", block))
            if ev == "well-supported" and (len(voices) < 3 or verified < 1):
                errors.append(
                    f"{rel}: block `{title[:40]}` claims well-supported but carries "
                    f"{len(voices)} voice line(s) / {verified} [verified] — promotion needs "
                    f"3+ independent primaries incl. one tier-1 (canonical: Maturity & tier-1)"
                )
            if ev == "contested" and not any(v.lower() == "diverges" for v in voices):
                errors.append(
                    f"{rel}: block `{title[:40]}` claims contested but has no **diverges** voice line"
                )


# ---------------------------------------------------------------------- driver
def main() -> int:
    ap = argparse.ArgumentParser(description="Repo integrity checks for the berkshire vault.")
    ap.add_argument("--staged", action="store_true",
                    help="lint staged content from the git index (what pre-commit uses)")
    args = ap.parse_args()

    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass

    corpus = Corpus(staged=args.staged)
    errors: list[str] = []

    n_files = len(corpus.paths())
    n_refs = check_references(corpus, errors)
    n_ids = check_ids(corpus, errors)
    n_lib = check_library(corpus, errors)
    check_indexes(corpus, errors)
    check_thesis_shape(corpus, errors)
    check_append_only(corpus, errors)
    check_evidence_tags(corpus, errors)

    mode = "staged" if args.staged else "working tree"
    print(f"Checked {n_files} files ({mode}): {n_refs} references, {n_ids} ID citations, "
          f"{n_lib} library entries.")

    if not errors:
        print("All checks pass. [OK]")
        return 0

    print(f"\n{len(errors)} problem(s):")
    for e in errors:
        print(f"  {e}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
