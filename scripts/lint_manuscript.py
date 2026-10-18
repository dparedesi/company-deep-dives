#!/usr/bin/env python3
"""
Manuscript Quality Gates
========================
Mechanical enforcement of .Resources/quality-bar.md ("Gates: what blocks a build").
Zero tolerance, no judgment calls: any hit fails the build with the exact file and line.

Usage:
    python scripts/lint_manuscript.py palantir           # Lint one book, fail closed
    python scripts/lint_manuscript.py palantir --report  # Report hits, always exit 0
    python scripts/lint_manuscript.py                    # Lint all books
"""

import argparse
import re
import sys
from pathlib import Path

BOOKS_DIR = Path(__file__).parent.parent / "books"

# Scanned files: manuscript/*.md plus about.md (money and artifact rules apply there too).
def scan_files(book_dir: Path) -> list[Path]:
    files = sorted((book_dir / "manuscript").glob("*.md"))
    about = book_dir / "about.md"
    if about.exists():
        files.append(about)
    return files


# Codepoint gates: em dash, en dash, CJK, Hangul, Cyrillic.
FORBIDDEN_CODEPOINTS = [
    ("em dash (U+2014)", re.compile("\u2014")),
    ("en dash (U+2013)", re.compile("\u2013")),
    ("CJK codepoint", re.compile("[\u4e00-\u9fff]")),
    ("Hangul codepoint", re.compile("[\uac00-\ud7a3]")),
    ("Cyrillic codepoint", re.compile("[\u0400-\u04ff]")),
]

# Artifact gates: escaped punctuation (docs-app export signature), HTML comments.
ESCAPED_PUNCTUATION = re.compile(r"\\[.,;:!?'\"()\[\]{}\-]")
HTML_COMMENT = re.compile(r"<!--")

# Money gates per the voice charter (.Resources/voice.md, "Numbers").
SPELLED_OUT_MONEY = re.compile(r"\b(?:billion|million|trillion)\s+dollars\b", re.IGNORECASE)
TWO_DECIMAL_AGGREGATE = re.compile(r"\$?\d[\d,]*\.\d{2,}\s*(?:billion|trillion)\b", re.IGNORECASE)

# Banned phrases: self-praise, report-speak, verdict-dissolving, returning-reader framing.
BANNED_PHRASES = [
    "exceptionally comprehensive",
    "unprecedented insight",
    "unprecedented depth",
    "novel insights",
    "synergistic triad",
    "key findings & core conclusions",
    "moving beyond readily available summaries",
    "the most thorough publicly available",
    "this report",
    "this document",
    "hereinafter referred to as",
    "it remains to be seen",
    "story is still being written",
    "lies somewhere in the middle",
    "warrants close observation",
    "will likely contain elements from across these scenarios",
    "only time will tell",
    "more questions than answers",
    "returning readers",
    "before diving into",
]
BANNED_PHRASE_PATTERNS = [(p, re.compile(re.escape(p), re.IGNORECASE)) for p in BANNED_PHRASES]

# Frontmatter gates: house view present, minimum substance.
HOUSE_VIEW = re.compile(r"house view|most likely scenario|we land on", re.IGNORECASE)
FRONTMATTER_MIN_WORDS = 300

MAX_HITS_SHOWN = 200


def lint_file(path: Path, rel: str) -> list[str]:
    hits = []
    text = path.read_text(encoding="utf-8")
    lines = text.split("\n")

    for lineno, line in enumerate(lines, 1):
        for name, pattern in FORBIDDEN_CODEPOINTS:
            if pattern.search(line):
                hits.append(f"{rel}:{lineno}: {name}: {line.strip()[:100]}")
        if ESCAPED_PUNCTUATION.search(line):
            hits.append(f"{rel}:{lineno}: escaped punctuation: {line.strip()[:100]}")
        if HTML_COMMENT.search(line):
            hits.append(f"{rel}:{lineno}: HTML comment: {line.strip()[:100]}")
        if SPELLED_OUT_MONEY.search(line):
            hits.append(f"{rel}:{lineno}: spelled-out money: {line.strip()[:100]}")
        if TWO_DECIMAL_AGGREGATE.search(line):
            hits.append(f"{rel}:{lineno}: two-decimal aggregate in the billions: {line.strip()[:100]}")
        for phrase, pattern in BANNED_PHRASE_PATTERNS:
            if pattern.search(line):
                hits.append(f"{rel}:{lineno}: banned phrase ({phrase}): {line.strip()[:100]}")

    return hits


def lint_frontmatter(book_dir: Path) -> list[str]:
    fm = book_dir / "manuscript" / "00-frontmatter.md"
    if not fm.exists():
        return [f"manuscript/00-frontmatter.md: missing frontmatter file"]
    text = fm.read_text(encoding="utf-8")
    hits = []
    if not HOUSE_VIEW.search(text):
        hits.append("manuscript/00-frontmatter.md: no house view (most likely scenario, probability or confidence, verdict) found")
    word_count = len(text.split())
    if word_count < FRONTMATTER_MIN_WORDS:
        hits.append(f"manuscript/00-frontmatter.md: frontmatter under {FRONTMATTER_MIN_WORDS} words ({word_count})")
    return hits


def run_lint(book_dir: Path, report_only: bool = False) -> tuple[bool, list[str]]:
    """Lint one book directory. Returns (passed, hits)."""
    hits = []
    for f in scan_files(book_dir):
        rel = str(f.relative_to(book_dir))
        hits.extend(lint_file(f, rel))
    hits.extend(lint_frontmatter(book_dir))
    return (len(hits) == 0, hits)


def main():
    parser = argparse.ArgumentParser(
        description="Quality-bar gates for book manuscripts (see .Resources/quality-bar.md)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("book", nargs="?", help="Book to lint (e.g., 'palantir'). If not specified, lints all books.")
    parser.add_argument("--report", action="store_true", help="Report hits but always exit 0 (does not gate anything)")
    args = parser.parse_args()

    if not BOOKS_DIR.exists():
        print("No books directory found.")
        sys.exit(1)

    book_dirs = {}
    for d in sorted(BOOKS_DIR.iterdir()):
        if d.is_dir() and (d / "metadata.yaml").exists():
            book_dirs[d.name.split("-", 1)[-1] if "-" in d.name else d.name] = d

    if args.book:
        if args.book not in book_dirs:
            print(f"Book '{args.book}' not found. Available: {', '.join(book_dirs)}")
            sys.exit(1)
        targets = {args.book: book_dirs[args.book]}
    else:
        targets = book_dirs

    any_failed = False
    total_hits = 0
    for key, d in targets.items():
        passed, hits = run_lint(d)
        total_hits += len(hits)
        if passed:
            print(f"✅ {key}: gates passed ({len(scan_files(d))} files)")
        else:
            any_failed = True
            print(f"❌ {key}: {len(hits)} gate hit(s) across {len(scan_files(d))} files")
            for h in hits[:MAX_HITS_SHOWN]:
                print(f"   {h}")
            if len(hits) > MAX_HITS_SHOWN:
                print(f"   ... and {len(hits) - MAX_HITS_SHOWN} more")

    if args.report:
        print(f"\nReport mode: {total_hits} hit(s) total (not gating).")
        sys.exit(0)

    if any_failed:
        print("\nQuality gates failed. The build is blocked until every hit is fixed.")
        print("See .Resources/quality-bar.md (Gates) and .Resources/voice.md (banned lists).")
        sys.exit(1)
    print("\nAll quality gates passed.")


if __name__ == "__main__":
    main()
