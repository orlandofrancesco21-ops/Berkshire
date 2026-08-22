#!/usr/bin/env python3
"""Cadence watchdog for the berkshire vault — the one thing here with a clock.

WHY. Every discipline in this vault is enforced by a skill that only runs when
invoked, and the README's ritual table has now failed twice: an 8-week silence
(May-Jul 2026, journal empty, two revisit dates blown through) and then 11 days
with the entire audit session's work stranded uncommitted. Prose cannot hold a
cadence. This script is read-only, prints nothing when healthy, and always exits 0
— it nags, it never blocks.

WIRED AT TWO LEVELS, deliberately:
  - vault level (Berkshire/.claude/settings.json) — full detail, every session.
  - user level (~/.claude/settings.json via the hook wrapper) — escalated items
    only, once a day, skipped when the session is already in the vault.
    Both documented silences involved ZERO Berkshire sessions, so a vault-scoped
    hook alone would have fired exactly zero times. The owner opens Claude Code
    near-daily for other repos; that is the only trigger verified to fire.

ANTI-HABITUATION is a design constraint, not a nicety: a check that prints a wall
of yellow every day trains the dismiss reflex and dies the same death as the prose
it replaced. Hence: silent when green, one line per breach, escalation only past
2x threshold, and every nag names the command that fixes it.

Checks (thresholds chosen against this vault's actual rituals):
  - news-triage        journal/{date}-triage.md newer than 5 days
                       (5, not 4: a Tue/Fri rhythm is exactly 4d apart, and a 4d
                       threshold false-fires every Tuesday morning on a healthy book)
  - portfolio-review   portfolio.md "Last reviewed" within 8 days
  - watchlist-revisit  watchlist.md "Last updated" within 95 days (quarterly)
  - source-sweep       sources.md "Last swept" within 35 days (once it exists)
  - open flags         journal/_flagged.md active flags older than 30 days, parsed
                       in THIS vault's grammar ("flagged {date}" with no "resolved"
                       on the line). The sibling vault greps a literal "UNRESOLVED"
                       token that never appears in these files — a ported check
                       would have matched nothing, forever, silently.
  - stale theses       held positions whose newest Update-log entry is >180 days old
                       (proxy for the canonical stale-thesis rule)
  - uncommitted work   dirty tree whose oldest modification is >7 days old — the
                       exact failure that stranded the 2026-07-17 audit
  - hooks wiring       core.hooksPath == .githooks, else the lint is silently OFF
  - portfolio TBDs     unresolved TBD share/cost fields (owner-only fix)
  - spot audit         >90 days since the last journal/{date}-spot-audit.md — the
                       verification-honesty probe; with one person as the entire
                       verification workforce, nothing else stops "verified" from
                       going decorative

Usage:
    python scripts/check-cadence.py                  # full report
    python scripts/check-cadence.py --user-level     # escalated only; skip if cwd is the vault
    python scripts/check-cadence.py --throttle 20    # at most once per 20 hours
    python scripts/check-cadence.py --force          # ignore throttle (manual check)
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import time
from datetime import date, datetime, timedelta
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TODAY = date.today()
STAMP = REPO_ROOT / ".claude" / "state" / "cadence-last-run"

DATE_RE = re.compile(r"(\d{4})-(\d{2})-(\d{2})")

# threshold days per check; a breach at >2x prints as escalated
TRIAGE_DAYS = 5
REVIEW_DAYS = 8
WATCHLIST_DAYS = 95
SWEEP_DAYS = 35
FLAG_DAYS = 30
THESIS_STALE_DAYS = 180
DIRTY_DAYS = 7
SPOT_AUDIT_DAYS = 90
NOVEL_EVAL_DAYS = 90

# Deliberate marker for "this value or behavior needs resolving before it can be
# trusted, and it may currently be silently wrong." Introduced 2026-07-31, after
# PRINCIPLES_CHECK_CUTOVER shipped as the literal placeholder "2099-01-01" with an
# in-code comment nobody re-read, and quietly disabled the vault's flagship
# enforcement gate for two days while it reported [OK]. That specific defect is
# fixed; this scanner exists so its shape can never ship silently again — a
# stale TODO is exactly as invisible as a gate that checks nothing, and this
# vault has now hit that pattern seven times.
#
# The literal string is namespaced (`TODO(vault):`, not bare `TODO`) so it can
# never collide with an ordinary comment or a human-directed note like
# journal/2026-07-17-decision.md's "TODO (Francesco): fill in the TBD fields" —
# that one is a request to a person and is already surfaced by the portfolio-TBD
# check above; this one is a request to whoever next touches the vault's own
# tooling, wherever it lives.
TODO_MARKER_RE = re.compile(r"TODO\(vault\):.*")
TODO_SCAN_GLOBS = ("*.py", "*.md")
TODO_SCAN_EXCLUDE_PARTS = {".git", ".obsidian", "_inbox", "sources"}
# Files that legitimately contain the literal marker string IN PROSE OR CODE
# describing the feature itself — this file's own docstrings, and the string
# constant its implementation matches against. Excluding them is narrow and
# justified (the file that spells out a sentinel cannot be scanned for it, the
# same way a spell-checker does not flag its own dictionary), unlike a broad
# "skip everything" exemption. Verified empirically: without this, the scanner's
# first-ever run self-flagged three times on its own comments and its own
# membership test, on the same day it was written.
TODO_SCAN_SELF_EXEMPT = {"scripts/check-cadence.py"}


class Nag:
    def __init__(self, text: str, fix: str = "", ratio: float = 1.0):
        self.text = text
        self.fix = fix
        self.ratio = ratio  # overdue / threshold; >2 escalates

    @property
    def escalated(self) -> bool:
        return self.ratio >= 2.0

    def render(self) -> str:
        prefix = "!! 2x OVERDUE" if self.escalated else "overdue"
        line = f"  - [{prefix}] {self.text}"
        return f"{line}\n      fix: {self.fix}" if self.fix else line


def parse_date(text: str) -> date | None:
    m = DATE_RE.search(text)
    if not m:
        return None
    try:
        return date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    except ValueError:
        return None


def parse_last_run(value: str) -> date | None:
    """'never' means never - even when trailing prose contains a date. portfolio.md
    literally reads 'never - positions backfilled 2026-07-17 during system audit',
    and a naive date-anywhere search reads that as a fresh review."""
    stripped = value.strip()
    if re.match(r"(?i)^never\b", stripped):
        return None
    return parse_date(value)


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return ""


def field(text: str, label: str) -> str | None:
    m = re.search(rf"\*\*{re.escape(label)}:\*\*(.*)", text)
    return m.group(1) if m else None


def git(*args: str) -> str:
    try:
        out = subprocess.run(["git", "-C", str(REPO_ROOT), *args],
                             capture_output=True, text=True, encoding="utf-8",
                             errors="replace", timeout=10)
        return out.stdout
    except (OSError, subprocess.SubprocessError):
        return ""


def age_nag(what: str, last: date | None, limit: int, fix: str, never_msg: str | None = None) -> Nag | None:
    if last is None:
        if never_msg is None:
            return None
        return Nag(never_msg, fix, ratio=2.0)
    days = (TODAY - last).days
    if days <= limit:
        return None
    return Nag(f"{what} last ran {last.isoformat()} ({days}d ago, limit {limit}d)",
               fix, ratio=days / limit)


def latest_journal(kind: str) -> date | None:
    jdir = REPO_ROOT / "journal"
    if not jdir.is_dir():
        return None
    dates = [d for p in jdir.glob(f"*-{kind}.md") if (d := parse_date(p.name))]
    return max(dates) if dates else None


def scan_todo_markers() -> list[Nag]:
    """Find every marker in the repo — see TODO_MARKER_RE's docstring comment
    above for why this exists. Reports file:line so it is a two-second fix, not
    a hunt."""
    hits: list[Nag] = []
    for glob in TODO_SCAN_GLOBS:
        for p in REPO_ROOT.rglob(glob):
            rel = p.relative_to(REPO_ROOT).as_posix()
            if rel in TODO_SCAN_SELF_EXEMPT:
                continue
            if any(part in TODO_SCAN_EXCLUDE_PARTS for part in p.relative_to(REPO_ROOT).parts):
                continue
            text = read(p)
            for i, line in enumerate(text.splitlines(), start=1):
                m = TODO_MARKER_RE.search(line)
                if m:
                    hits.append(Nag(f"{rel}:{i}: {m.group(0).strip()[:90]}",
                                    "resolve the marker, or say explicitly why it must wait",
                                    ratio=2.0))
    return hits


def latest_new_sector() -> date | None:
    """Date of the most recently ADDED framework or sector primer — i.e. the last
    time this vault was pointed at a name it had no lens for yet. sectors/_example/
    is scaffolding, not a real evaluation, and is excluded."""
    out = git("log", "--diff-filter=A", "--format=%ad", "--date=short", "--",
              "frameworks/*.md", "sectors/*/primer.md", ":(exclude)sectors/_example/*")
    dates = [d for ln in out.splitlines() if (d := parse_date(ln.strip()))]
    return max(dates) if dates else None


def collect() -> list[Nag]:
    nags: list[Nag] = []

    if git("config", "core.hooksPath").strip() != ".githooks":
        nags.append(Nag(
            "git hooks NOT wired on this machine - the pre-commit lint is OFF",
            "git config core.hooksPath .githooks", ratio=2.0))

    nags.append(age_nag("news-triage", latest_journal("triage"), TRIAGE_DAYS,
                        "run news-triage (a 'nothing material' entry takes two minutes)",
                        "news-triage has never run"))

    portfolio = read(REPO_ROOT / "portfolio.md")
    if portfolio:
        raw = field(portfolio, "Last reviewed")
        has_positions = bool(re.search(r"^\|\s*[A-Z][A-Z0-9.\-]{0,9}\s*\|", portfolio, re.MULTILINE))
        if has_positions:
            nags.append(age_nag("portfolio-review", parse_last_run(raw or ""), REVIEW_DAYS,
                                "run portfolio-review (stamps Last reviewed, keeps weights honest)",
                                "portfolio-review has never run while positions are open"))
        if re.search(r"\bTBD\b", portfolio):
            nags.append(Nag(
                "portfolio.md still has TBD share/cost fields - weights and concentration "
                "cannot be computed until they are filled",
                "fill shares / avg cost / trade date from brokerage records (owner-only)"))

    watchlist = read(REPO_ROOT / "watchlist.md")
    if watchlist:
        nags.append(age_nag("watchlist-revisit", parse_last_run(field(watchlist, "Last updated") or ""),
                            WATCHLIST_DAYS, "run watchlist-revisit (quarterly sweep of passed / waiting names)"))

    sources = read(REPO_ROOT / "sources.md")
    if sources:
        nags.append(age_nag("source-sweep", parse_last_run(field(sources, "Last swept") or ""),
                            SWEEP_DAYS, "review sources.md and absorb what is due"))

    flagged = read(REPO_ROOT / "journal" / "_flagged.md")
    for line in flagged.splitlines():
        stripped = line.strip()
        if not stripped.startswith("-") or "flagged" not in stripped.lower():
            continue
        if "resolved" in stripped.lower():
            continue
        d = parse_date(stripped)
        if not d:
            continue
        days = (TODAY - d).days
        if days > FLAG_DAYS:
            ticker = stripped.lstrip("- ").split(":", 1)[0][:12]
            nxt = ""
            m = re.search(r"next:\s*([a-z\-]+)", stripped)
            if m:
                nxt = f"run {m.group(1)} on {ticker}"
            nags.append(Nag(f"flag on {ticker} open since {d.isoformat()} ({days}d)",
                            nxt or "resolve or explicitly re-scope the flag", ratio=days / FLAG_DAYS))

    # Both tiers. The company glob is 5 parts, the funds glob is 3, and keying the
    # staleness clock to the company shape alone is exactly the failure the lint's
    # own position_doc() was written to fix on 2026-08-22 — reproduced here the
    # same day, in the sibling gate that commit did not open. A fund thesis could
    # have sat for years without ever nagging.
    theses = [(p, "company") for p in sorted(REPO_ROOT.glob("sectors/*/companies/*/thesis.md"))]
    theses += [(p, "fund") for p in sorted(REPO_ROOT.glob("funds/*/thesis.md"))]
    for thesis, variant in theses:
        rel = thesis.as_posix()
        if "_example" in rel or "_TICKER" in rel:
            continue
        ticker = thesis.parent.name
        if portfolio and not re.search(rf"^\|\s*{re.escape(ticker)}\s*\|", portfolio, re.MULTILINE):
            continue  # not held; watchlist names are swept quarterly instead
        entries = [d for d in (parse_date(ln) for ln in read(thesis).splitlines()
                               if ln.startswith("### ")) if d]
        if entries:
            skill = "fund-deep-dive" if variant == "fund" else "company-deep-dive"
            n = age_nag(f"{ticker} thesis", max(entries), THESIS_STALE_DAYS,
                        f"run {skill} refresh on {ticker} (canonical: stale thesis)")
            if n:
                nags.append(n)

    dirty = [ln for ln in git("status", "--porcelain").splitlines() if ln.strip()]
    if dirty:
        oldest = None
        for ln in dirty:
            rel = ln[3:].strip().strip('"').split(" -> ")[-1]
            p = REPO_ROOT / rel
            if p.is_file():
                mt = datetime.fromtimestamp(p.stat().st_mtime).date()
                oldest = mt if oldest is None or mt < oldest else oldest
        if oldest and (TODAY - oldest).days > DIRTY_DAYS:
            days = (TODAY - oldest).days
            nags.append(Nag(
                f"{len(dirty)} file(s) uncommitted, oldest modified {oldest.isoformat()} ({days}d ago) "
                f"- this is how the 2026-07-17 audit sat stranded",
                "review and commit (git status), or stash what is not wanted",
                ratio=days / DIRTY_DAYS))

    if (REPO_ROOT / "library").is_dir() and any((REPO_ROOT / "library").glob("*.md")):
        nags.append(age_nag("verification spot-audit", latest_journal("spot-audit"), SPOT_AUDIT_DAYS,
                            "re-check one random library entry against its archived source, or one "
                            "principle block against its own Voices/Log; write journal/{date}-spot-audit.md",
                            "verification spot-audit has never run (library entries exist)"))

    nags.extend(scan_todo_markers())

    # Past the initial build (2+ real sectors), nag if it has been a while since
    # the whole evaluate chain last ran against a name the vault had no lens for.
    # Every bug this vault's own build-plan status log records as "found by
    # dogfooding" (the cutover placeholder, the parallel-orchestration gaps) was
    # found this way — by real, unplanned use, not by any planted test case. This
    # turns that into a scheduled practice instead of something that only happens
    # when the owner happens to ask for a new name.
    real_sectors = [p for p in REPO_ROOT.glob("sectors/*/primer.md") if "_example" not in p.parts]
    if len(real_sectors) >= 2:
        n = age_nag("a full evaluate on an unfamiliar name", latest_new_sector(), NOVEL_EVAL_DAYS,
                    "run evaluate on a name outside every existing sector — that is how the "
                    "cutover-placeholder and parallel-orchestration bugs were actually found")
        if n:
            nags.append(n)

    return [n for n in nags if n]


def throttled(hours: float, force: bool) -> bool:
    if force or hours <= 0:
        return False
    try:
        if STAMP.exists() and (time.time() - STAMP.stat().st_mtime) < hours * 3600:
            return True
    except OSError:
        return False
    try:
        STAMP.parent.mkdir(parents=True, exist_ok=True)
        STAMP.write_text(datetime.now().isoformat(timespec="seconds"), encoding="utf-8")
    except OSError:
        pass
    return False


def main() -> int:
    ap = argparse.ArgumentParser(description="Cadence watchdog (never blocks; exit 0 always).")
    ap.add_argument("--user-level", action="store_true",
                    help="escalated breaches only; stay silent when cwd is inside the vault")
    ap.add_argument("--throttle", type=float, default=0,
                    help="report at most once per N hours (stamp in .claude/state/)")
    ap.add_argument("--force", action="store_true", help="ignore the throttle")
    args = ap.parse_args()

    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass

    if args.user_level:
        try:
            if REPO_ROOT == Path.cwd() or REPO_ROOT in Path.cwd().parents:
                return 0  # the vault's own hook covers this session in full detail
        except OSError:
            pass

    if throttled(args.throttle, args.force):
        return 0

    nags = collect()
    if args.user_level:
        nags = [n for n in nags if n.escalated]

    if not nags:
        if not args.user_level:
            print("berkshire cadence: nothing overdue.")
        return 0

    where = " (Berkshire vault)" if args.user_level else ""
    print(f"berkshire cadence{where} - {len(nags)} item(s) need attention:")
    for n in nags:
        print(n.render())
    return 0


if __name__ == "__main__":
    sys.exit(main())
