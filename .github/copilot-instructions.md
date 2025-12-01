# Copilot Instructions for Company Deep Dives

## Project Overview

This is a **book publishing system** for creating analytical deep-dive books about companies. Content is authored in Markdown and compiled to PDF (via Typst) and EPUB (via Pandoc).

## Architecture

```
books/<NNN>-<bookname>/     # Each book in numbered folder
├── metadata.yaml           # Book configuration (title, author, TOC settings)
├── images/cover.jpg        # Cover image (required for cover pages)
├── manuscript/             # Markdown content (sorted alphabetically)
│   ├── 00-frontmatter.md   # Executive summary, preface
│   ├── 01-chapter-1.md     # Chapters numbered sequentially
│   └── ...
└── output/                 # Generated PDF and EPUB files

scripts/build.py            # Python build automation
templates/book.typ          # Typst template for PDF styling
templates/epub.css          # CSS for EPUB reader styling
```

## Build Commands

```bash
python scripts/build.py                  # Build all books (PDF + EPUB)
python scripts/build.py <bookname>       # Build specific book (e.g., palantir)
python scripts/build.py <bookname> --pdf # PDF only
python scripts/build.py <bookname> --epub # EPUB only
python scripts/build.py --list           # List available books
```

Book names are derived from folder names: `001-palantir` → use `palantir`

## Creating a New Book

1. Create folder: `books/<NNN>-<name>/` with `images/`, `manuscript/`, `output/` subdirs
2. Copy `metadata.yaml` from existing book and update fields
3. Add `images/cover.jpg` for cover page
4. Create manuscript files with numbered prefixes (`00-`, `01-`, `02-`, etc.)
5. Use `# Title` (H1) for chapter headings—triggers page breaks in PDF

## Key Conventions

### File Naming
- **Folders**: `<3-digit-number>-<slug>` (e.g., `003-spacex`)
- **Chapters**: `<2-digit-number>-<name>.md` sorted alphabetically for ordering
- **Output**: Uses folder name (e.g., `001-palantir.pdf`)

### Metadata (metadata.yaml)
Required fields: `title`, `author`, `date`, `cover_image: cover.jpg`
Optional: `subtitle`, `toc: true`, `toc_depth: 3`, `number_sections: true`
See `books/001-palantir/metadata.yaml` for full example.

### Content Style
- Frontmatter file (`00-frontmatter.md`) contains executive summary (no H1)
- Chapter files start with `# Chapter Title` which becomes the TOC entry
- Use standard Markdown: tables, code blocks, blockquotes, footnotes, images

### Writing Conventions
- **Never use em dashes (—)**. Use colons, commas, parentheses, or separate sentences instead
- **Use sentence case for headings**: Capitalize only the first word and proper nouns
  - ✅ `# The future of commercial space` 
  - ✅ `## How Rocket Lab disrupted the industry`
  - ❌ `# The Future of Commercial Space`
- **Acronyms stay uppercase**: AI, NASA, CEO, API, IPO
- **Expanded acronyms**: Capitalize proper noun portions only
  - ✅ "Artificial intelligence platform (AIP)"
  - ✅ "National Aeronautics and Space Administration (NASA)"

### Template Customization
- **PDF styling**: Edit `templates/book.typ` (Typst syntax)
- **EPUB styling**: Edit `templates/epub.css`
- Color scheme uses `#2c3e50` (primary) across both templates

## Dependencies

- **Pandoc** (required): `brew install pandoc`
- **Typst** (PDF engine): `brew install typst`
- **Python + PyYAML**: `pip install pyyaml`
- macOS uses built-in PDF merge tools; falls back to `qpdf` if needed

## Troubleshooting

- **Missing chapters**: Check filename prefixes are sequential and end in `.md`
- **Cover not showing**: Ensure `cover_image: cover.jpg` in metadata and file exists
- **PDF build fails**: Verify Typst is installed; script falls back to LaTeX if missing
