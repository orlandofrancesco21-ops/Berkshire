"""Cross-reference checker for the berkshire repo.

Walks every .md file in the repo, extracts markdown links and frontmatter file
references, resolves them relative to the source file's location, and reports
any that don't exist on disk.

Run manually after structural edits:
    python scripts/check-cross-references.py

Exits 0 if all references resolve, non-zero if any are broken.

Skipped:
    - URLs (http://, https://, mailto:)
    - Fragment-only links (#section)
    - Template placeholders containing braces like {TICKER}, {industry}
    - Files inside .git/, .obsidian/, .claude/state/, .claude/cache/, .claude/logs/
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# Match markdown links: [text](path) and reference-style frontmatter: **Field:** `path`
LINK_PATTERN = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")
BACKTICK_PATH_PATTERN = re.compile(r"`(\.{1,2}/[^`]+\.md|[a-zA-Z0-9_\-./]+/[a-zA-Z0-9_\-./]+\.md)`")

SKIP_DIRS = {".git", ".obsidian", "state", "cache", "logs"}


def is_skippable_target(target: str) -> bool:
    """Return True if the link target is not a local file we should check."""
    if target.startswith(("http://", "https://", "mailto:")):
        return True
    if target.startswith("#"):
        return True
    # Template placeholders — anything with curly braces is a pattern, not a real path
    if "{" in target or "}" in target:
        return True
    return False


def iter_markdown_files(root: Path):
    for path in root.rglob("*.md"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        yield path


def extract_references(content: str) -> list[str]:
    """Return all candidate file references in a markdown file."""
    refs: list[str] = []
    for _, target in LINK_PATTERN.findall(content):
        # Strip any anchor fragment from the target
        target = target.split("#", 1)[0].strip()
        if target:
            refs.append(target)
    for target in BACKTICK_PATH_PATTERN.findall(content):
        refs.append(target.strip())
    return refs


def main() -> int:
    broken: list[tuple[Path, str, Path]] = []
    files_checked = 0
    refs_checked = 0

    for md_file in iter_markdown_files(REPO_ROOT):
        files_checked += 1
        try:
            content = md_file.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            print(f"WARN: could not decode {md_file}, skipping")
            continue

        for target in extract_references(content):
            if is_skippable_target(target):
                continue
            refs_checked += 1
            # Try resolving relative to the source file first (handles
            # template-style ../../X.md links). Fall back to repo-root
            # (handles skills that say "journal/_flagged.md" meaning the
            # repo-root path, not a sibling of the SKILL.md file).
            source_relative = (md_file.parent / target).resolve()
            repo_relative = (REPO_ROOT / target).resolve()

            resolved = None
            for candidate in (source_relative, repo_relative):
                try:
                    candidate.relative_to(REPO_ROOT)
                except ValueError:
                    continue
                if candidate.exists():
                    resolved = candidate
                    break

            if resolved is None:
                # Report against the source-relative resolution (more
                # informative for the typical case)
                broken.append((md_file, target, source_relative))

    print(f"Checked {refs_checked} references across {files_checked} files.")

    if not broken:
        print("All references resolve. [OK]")
        return 0

    print(f"\n{len(broken)} broken reference(s):")
    for source, target, resolved in broken:
        rel_source = source.relative_to(REPO_ROOT)
        try:
            rel_resolved = resolved.relative_to(REPO_ROOT)
        except ValueError:
            rel_resolved = resolved
        print(f"  {rel_source}: `{target}` -> {rel_resolved} (not found)")
    return 1


if __name__ == "__main__":
    sys.exit(main())
