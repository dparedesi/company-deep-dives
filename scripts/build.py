#!/usr/bin/env python3
"""
Book Build System
=================
A Python script to build PDF and EPUB books from Markdown using Pandoc.

Usage:
    python scripts/build.py                    # Build all books
    python scripts/build.py palantir          # Build specific book
    python scripts/build.py palantir --pdf    # Build only PDF
    python scripts/build.py palantir --epub   # Build only EPUB
    python scripts/build.py --list            # List available books
"""

import argparse
import os
import subprocess
import sys
import yaml
from pathlib import Path
from datetime import datetime
import re

# Configuration
BOOKS_DIR = Path(__file__).parent.parent / "books"
TEMPLATES_DIR = Path(__file__).parent.parent / "templates"
DEFAULT_AUTHOR = "Daniel Paredes"

# Month name to number mapping
MONTH_MAP = {
    'january': '01', 'february': '02', 'march': '03', 'april': '04',
    'may': '05', 'june': '06', 'july': '07', 'august': '08',
    'september': '09', 'october': '10', 'november': '11', 'december': '12'
}


def convert_to_iso_date(date_str: str) -> str:
    """Convert human-readable date to ISO format for EPUB compatibility.
    
    Examples:
        "December 2025" -> "2025-12"
        "2025" -> "2025"
        "2025-12-01" -> "2025-12-01" (already ISO)
    """
    if not date_str:
        return ""
    
    date_str = date_str.strip()
    
    # Already ISO format (YYYY-MM-DD or YYYY-MM or YYYY)
    if re.match(r'^\d{4}(-\d{2})?(-\d{2})?$', date_str):
        return date_str
    
    # Try "Month YYYY" format (e.g., "December 2025")
    match = re.match(r'^(\w+)\s+(\d{4})$', date_str, re.IGNORECASE)
    if match:
        month_name = match.group(1).lower()
        year = match.group(2)
        if month_name in MONTH_MAP:
            return f"{year}-{MONTH_MAP[month_name]}"
    
    # Try to extract just the year
    year_match = re.search(r'\d{4}', date_str)
    if year_match:
        return year_match.group()
    
    return ""


def find_books() -> dict[str, Path]:
    """Find all books in the books directory."""
    books = {}
    if not BOOKS_DIR.exists():
        return books
    
    for book_dir in sorted(BOOKS_DIR.iterdir()):
        if book_dir.is_dir() and (book_dir / "metadata.yaml").exists():
            # Use folder name as book key (e.g., "001-palantir" -> "palantir")
            book_key = book_dir.name.split("-", 1)[-1] if "-" in book_dir.name else book_dir.name
            books[book_key] = book_dir
    
    return books


def load_metadata(book_dir: Path) -> dict:
    """Load book metadata from YAML file."""
    metadata_file = book_dir / "metadata.yaml"
    if metadata_file.exists():
        with open(metadata_file, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    return {}


def get_chapter_files(book_dir: Path) -> list[Path]:
    """Get all chapter markdown files in order."""
    manuscript_dir = book_dir / "manuscript"
    if not manuscript_dir.exists():
        return []
    
    # Get all .md files and sort them
    md_files = sorted(manuscript_dir.glob("*.md"))
    return md_files


def check_pandoc() -> bool:
    """Check if Pandoc is installed."""
    try:
        result = subprocess.run(
            ["pandoc", "--version"],
            capture_output=True,
            text=True
        )
        return result.returncode == 0
    except FileNotFoundError:
        return False


def check_typst() -> bool:
    """Check if Typst is installed (for PDF generation)."""
    try:
        result = subprocess.run(
            ["typst", "--version"],
            capture_output=True,
            text=True
        )
        return result.returncode == 0
    except FileNotFoundError:
        return False


def build_pdf(book_dir: Path, metadata: dict, use_typst: bool = True) -> bool:
    """Build PDF from markdown files."""
    chapter_files = get_chapter_files(book_dir)
    if not chapter_files:
        print(f"  ⚠️  No chapter files found in {book_dir / 'manuscript'}")
        return False
    
    output_dir = book_dir / "output"
    output_dir.mkdir(exist_ok=True)
    
    # Output filename - use book directory name for simplicity (avoids special char issues)
    output_file = output_dir / f"{book_dir.name}.pdf"
    content_file = output_dir / "content_temp.pdf"
    
    # Check for cover image
    cover_image = metadata.get("cover_image")
    cover_path = None
    if cover_image:
        cover_path = book_dir / "images" / cover_image
        if not cover_path.exists():
            print(f"  ⚠️  Cover image not found: {cover_path}")
            cover_path = None
    
    # Build Pandoc command for content
    cmd = ["pandoc"]
    
    # Add all chapter files
    cmd.extend([str(f) for f in chapter_files])
    
    # Output to content file (will merge with cover later)
    if cover_path:
        cmd.extend(["-o", str(content_file)])
    else:
        cmd.extend(["-o", str(output_file)])
    
    # Metadata
    if metadata.get("title"):
        cmd.extend(["--metadata", f"title={metadata['title']}"])
    if metadata.get("author"):
        cmd.extend(["--metadata", f"author={metadata['author']}"])
    if metadata.get("date"):
        cmd.extend(["--metadata", f"date={metadata['date']}"])
    
    # PDF engine
    if use_typst:
        cmd.extend(["--pdf-engine=typst"])
        # Use custom book template
        template_file = TEMPLATES_DIR / "book.typ"
        if template_file.exists() and template_file.stat().st_size > 0:
            cmd.extend(["--template", str(template_file)])
    else:
        # Fallback to LaTeX with basic styling
        cmd.extend([
            "--pdf-engine=xelatex",
            "-V", "geometry:margin=1in",
            "-V", "fontsize=11pt",
            "-V", "documentclass=book",
        ])
    
    # Table of contents
    if metadata.get("toc", True):
        cmd.append("--toc")
        cmd.extend(["--toc-depth", str(metadata.get("toc_depth", 3))])
    
    # Number sections
    if metadata.get("number_sections", True):
        cmd.append("--number-sections")
    
    print(f"  📄 Building PDF: {output_file.name}")
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"  ❌ PDF build failed:")
            print(f"     {result.stderr}")
            return False
        
        # If we have a cover, merge it with the content
        if cover_path:
            print(f"  🖼️  Adding cover image...")
            
            # Create cover PDF using Typst
            cover_pdf = output_dir / "cover_temp.pdf"
            cover_typ = output_dir / "cover_temp.typ"
            
            # Copy cover image to output dir for Typst to find it
            import shutil
            temp_cover = output_dir / cover_path.name
            shutil.copy(cover_path, temp_cover)
            
            # Write a simple Typst file for the cover (use just filename since it's in same dir)
            cover_typst_content = f'''#set page(margin: 0pt, width: 8.5in, height: 11in)
#image("{cover_path.name}", width: 100%, height: 100%, fit: "cover")
'''
            cover_typ.write_text(cover_typst_content)
            
            # Compile cover to PDF - use just filenames since we're running from output dir
            cover_result = subprocess.run(
                ["typst", "compile", "cover_temp.typ", "cover_temp.pdf"],
                capture_output=True, text=True,
                cwd=str(output_dir)  # Run from output dir so paths work
            )
            
            if cover_result.returncode != 0:
                print(f"  ⚠️  Cover generation failed, using content only")
                print(f"     {cover_result.stderr}")
                content_file.rename(output_file)
            else:
                # Verify cover PDF was created
                if not cover_pdf.exists():
                    print(f"  ⚠️  Cover PDF not found, using content only")
                    content_file.rename(output_file)
                else:
                    # Merge cover + content using macOS Automator tool
                    try:
                        merge_result = subprocess.run(
                            ["/System/Library/Automator/Combine PDF Pages.action/Contents/MacOS/join",
                             "-o", str(output_file), str(cover_pdf), str(content_file)],
                            capture_output=True, text=True
                        )
                        if merge_result.returncode != 0:
                            # Fallback: try qpdf if available
                            merge_result = subprocess.run(
                                ["qpdf", "--empty", "--pages", str(cover_pdf), str(content_file), "--", str(output_file)],
                                capture_output=True, text=True
                            )
                            if merge_result.returncode != 0:
                                print(f"  ⚠️  PDF merge failed, using content only")
                                content_file.rename(output_file)
                    except Exception as e:
                        print(f"  ⚠️  PDF merge failed ({e}), using content only")
                        content_file.rename(output_file)
            
            # Cleanup temp files
            for temp_file in [cover_typ, cover_pdf, content_file, temp_cover]:
                if temp_file.exists():
                    temp_file.unlink()
        
        print(f"  ✅ PDF created: {output_file}")
        return True
    except Exception as e:
        print(f"  ❌ Error building PDF: {e}")
        return False


def build_epub(book_dir: Path, metadata: dict) -> bool:
    """Build EPUB from markdown files."""
    chapter_files = get_chapter_files(book_dir)
    if not chapter_files:
        print(f"  ⚠️  No chapter files found in {book_dir / 'manuscript'}")
        return False
    
    output_dir = book_dir / "output"
    output_dir.mkdir(exist_ok=True)
    
    # Output filename - use book directory name for simplicity
    output_file = output_dir / f"{book_dir.name}.epub"
    
    # Build Pandoc command
    cmd = ["pandoc"]
    
    # Add all chapter files
    cmd.extend([str(f) for f in chapter_files])
    
    # Output
    cmd.extend(["-o", str(output_file)])
    
    # Metadata
    if metadata.get("title"):
        cmd.extend(["--metadata", f"title={metadata['title']}"])
    if metadata.get("author"):
        cmd.extend(["--metadata", f"author={metadata['author']}"])
    if metadata.get("date"):
        # EPUB requires ISO date format (YYYY-MM-DD or YYYY-MM or YYYY)
        # Convert human-readable dates like "December 2025" to "2025-12"
        date_str = metadata['date']
        epub_date = convert_to_iso_date(date_str)
        if epub_date:
            cmd.extend(["--metadata", f"date={epub_date}"])
    if metadata.get("language"):
        cmd.extend(["--metadata", f"lang={metadata['language']}"])
    
    # EPUB-specific options
    css_file = TEMPLATES_DIR / "epub.css"
    if css_file.exists():
        cmd.extend(["--css", str(css_file)])
    
    # Cover image
    cover_image = metadata.get("cover_image")
    if cover_image:
        cover_path = book_dir / "images" / cover_image
        if cover_path.exists():
            cmd.extend(["--epub-cover-image", str(cover_path)])
    
    # Table of contents
    if metadata.get("toc", True):
        cmd.append("--toc")
        cmd.extend(["--toc-depth", str(metadata.get("toc_depth", 3))])
    
    # Split chapters
    cmd.extend(["--epub-chapter-level", "1"])
    
    print(f"  📚 Building EPUB: {output_file.name}")
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"  ❌ EPUB build failed:")
            print(f"     {result.stderr}")
            return False
        print(f"  ✅ EPUB created: {output_file}")
        return True
    except Exception as e:
        print(f"  ❌ Error building EPUB: {e}")
        return False


def build_book(book_key: str, book_dir: Path, build_pdf_flag: bool = True, build_epub_flag: bool = True) -> bool:
    """Build a single book."""
    print(f"\n📖 Building: {book_key}")
    print(f"   Directory: {book_dir}")
    
    metadata = load_metadata(book_dir)
    if not metadata:
        print(f"  ⚠️  No metadata.yaml found, using defaults")
        metadata = {"title": book_key, "author": DEFAULT_AUTHOR}
    
    # Check for chapters
    chapters = get_chapter_files(book_dir)
    print(f"   Found {len(chapters)} chapter(s)")
    
    success = True
    use_typst = check_typst()
    
    if build_pdf_flag:
        if not use_typst:
            print("  ℹ️  Typst not found, falling back to LaTeX for PDF")
        if not build_pdf(book_dir, metadata, use_typst):
            success = False
    
    if build_epub_flag:
        if not build_epub(book_dir, metadata):
            success = False
    
    return success


def list_books():
    """List all available books."""
    books = find_books()
    if not books:
        print("No books found. Create a book in the 'books/' directory with a metadata.yaml file.")
        return
    
    print("\n📚 Available books:\n")
    for key, path in books.items():
        metadata = load_metadata(path)
        title = metadata.get("title", key)
        author = metadata.get("author", "Unknown")
        chapters = len(get_chapter_files(path))
        print(f"  • {key}")
        print(f"    Title: {title}")
        print(f"    Author: {author}")
        print(f"    Chapters: {chapters}")
        print()


def main():
    parser = argparse.ArgumentParser(
        description="Build books from Markdown to PDF and EPUB",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument(
        "book",
        nargs="?",
        help="Book to build (e.g., 'palantir'). If not specified, builds all books."
    )
    parser.add_argument(
        "--pdf",
        action="store_true",
        help="Build only PDF"
    )
    parser.add_argument(
        "--epub",
        action="store_true",
        help="Build only EPUB"
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List available books"
    )
    
    args = parser.parse_args()
    
    # Check Pandoc
    if not check_pandoc():
        print("❌ Pandoc is not installed!")
        print("   Install with: brew install pandoc")
        sys.exit(1)
    
    if args.list:
        list_books()
        return
    
    # Determine what to build
    build_pdf_flag = args.pdf or (not args.pdf and not args.epub)
    build_epub_flag = args.epub or (not args.pdf and not args.epub)
    
    books = find_books()
    
    if not books:
        print("❌ No books found!")
        print(f"   Make sure you have books in: {BOOKS_DIR}")
        print("   Each book needs a metadata.yaml file.")
        sys.exit(1)
    
    if args.book:
        # Build specific book
        if args.book not in books:
            print(f"❌ Book '{args.book}' not found!")
            print(f"   Available books: {', '.join(books.keys())}")
            sys.exit(1)
        
        success = build_book(args.book, books[args.book], build_pdf_flag, build_epub_flag)
    else:
        # Build all books
        print("🚀 Building all books...")
        success = True
        for key, path in books.items():
            if not build_book(key, path, build_pdf_flag, build_epub_flag):
                success = False
    
    print("\n" + "=" * 50)
    if success:
        print("✅ Build complete!")
    else:
        print("⚠️  Build completed with some errors")
        sys.exit(1)


if __name__ == "__main__":
    main()
