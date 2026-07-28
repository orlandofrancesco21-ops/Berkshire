#!/usr/bin/env python3
"""Mirror library/sources/ to an off-machine location, because git does not cover it.

`library/sources/` is gitignored on purpose (confidentiality stamps + binary
size), so the raw PDFs and canonical extracted text have NO remote copy from
git. The distilled entries survive in git; the sources do not. This script is
the durability step the build plan refers to.

This is not hypothetical. The sibling RevOps vault lost an owner-pasted Spotify
transcript before its archive layer existed — in-app only, not re-fetchable.
Investor letters and podcast transcripts are the hardest artifacts to re-retrieve,
so prevention only holds if the archive is actually mirrored.

TARGET MUST BE SET EXPLICITLY — $BERKSHIRE_SOURCE_MIRROR or --dest. There is
deliberately NO $OneDrive fallback (RevOps has one; this vault must not). On this
machine $OneDrive resolves to the EMPLOYER's tenant ("OneDrive - Synera GmbH"), so
a fallback would silently back a private investment archive — positions, cost
basis, conviction calls — up to company-controlled storage, and would tie source
durability to continued employment. README's security note is explicit that this
repo is private and stays private. Failing loudly is correct: an unset mirror is
an unfinished setup step, never a silent default.

Set it once, persistently (Windows):
    setx BERKSHIRE_SOURCE_MIRROR "D:\\personal\\Berkshire-source-archive"
then open a NEW shell — setx does not affect the current one.

ADDITIVE BY DEFAULT: copies new and newer files, never deletes from the mirror.
A file vanishing locally must not silently vanish from the backup too. Pass
--prune only when you deliberately want the mirror to match local exactly.

Usage:
    python scripts/mirror-sources.py              # mirror to $BERKSHIRE_SOURCE_MIRROR
    python scripts/mirror-sources.py --dry-run    # show what would copy
    python scripts/mirror-sources.py --dest PATH  # explicit target
"""

from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCES = REPO_ROOT / "library" / "sources"
ENV_VAR = "BERKSHIRE_SOURCE_MIRROR"
SKIP = {".gitkeep"}


def resolve_dest(explicit: str | None) -> Path | None:
    """Explicit --dest, else $BERKSHIRE_SOURCE_MIRROR. No fallback by design —
    see the module docstring (an employer-OneDrive default would leak a private
    investment archive into company storage)."""
    if explicit:
        return Path(explicit)
    env = os.environ.get(ENV_VAR)
    if env:
        return Path(env)
    return None


def main() -> int:
    ap = argparse.ArgumentParser(description="Mirror the local source archive off-machine.")
    ap.add_argument("--dest", help="explicit mirror target directory")
    ap.add_argument("--dry-run", action="store_true", help="report actions, copy nothing")
    ap.add_argument("--prune", action="store_true",
                    help="also DELETE mirror files with no local counterpart (off by default)")
    args = ap.parse_args()

    dest = resolve_dest(args.dest)
    if dest is None:
        print(
            f"No mirror target — the source archive is NOT backed up.\n"
            f"  Set a PERSONAL location (not the Synera OneDrive), once:\n"
            f'      setx {ENV_VAR} "D:\\personal\\Berkshire-source-archive"\n'
            f"  then open a new shell. Or pass --dest PATH for a one-off run.",
            file=sys.stderr,
        )
        return 2
    if not SOURCES.is_dir():
        print(f"{SOURCES} does not exist — nothing to mirror.", file=sys.stderr)
        return 2

    local = {p.name: p for p in SOURCES.iterdir() if p.is_file() and p.name not in SKIP}
    if not args.dry_run:
        dest.mkdir(parents=True, exist_ok=True)
    existing = {p.name: p for p in dest.iterdir() if p.is_file()} if dest.is_dir() else {}

    copied = skipped = 0
    for name, src in sorted(local.items()):
        tgt = dest / name
        if name in existing and existing[name].stat().st_mtime >= src.stat().st_mtime \
                and existing[name].stat().st_size == src.stat().st_size:
            skipped += 1
            continue
        print(f"{'would copy' if args.dry_run else 'copy'}: {name} ({src.stat().st_size:,} bytes)")
        if not args.dry_run:
            shutil.copy2(src, tgt)
        copied += 1

    orphans = sorted(set(existing) - set(local))
    for name in orphans:
        if args.prune:
            print(f"{'would delete' if args.dry_run else 'delete'}: {name} (no local counterpart)")
            if not args.dry_run:
                (dest / name).unlink()
        else:
            print(f"mirror-only (kept, use --prune to remove): {name}")

    print(f"\nmirror: {dest}")
    print(f"{copied} copied, {skipped} already current, {len(orphans)} mirror-only")
    return 0


if __name__ == "__main__":
    sys.exit(main())
