# 📚 Company Deep Dives

In-depth analytical books about innovative companies — their technology, strategy, market position, and future outlook. Each book is a comprehensive deep dive that goes beyond surface-level summaries to uncover novel insights and connections.

## 📖 Published Books

| # | Title | Author | Chapters |
|---|-------|--------|----------|
| 001 | **The Palantir Enigma** — *Forging Operational Sovereignty in a Data-Driven World* | Daniel Paredes | 10 |
| 002 | **The Rocket Lab Story and the Future of Space** — *Māhia to Mars* | Daniel Paredes | 11 |

## ✨ Features

- **Markdown-based authoring** — Write your books in plain Markdown
- **PDF generation** — Professional typography using Typst templates
- **EPUB generation** — E-reader compatible books with custom CSS styling
- **Cover image support** — Automatic cover page integration
- **Table of contents** — Auto-generated TOC for both formats
- **Chapter numbering** — Configurable section numbering
- **Metadata-driven** — YAML configuration for each book

## 🏗️ Project Structure

```
company-deep-dives/
├── books/
│   └── <book-id>/
│       ├── metadata.yaml      # Book configuration
│       ├── images/
│       │   └── cover.jpg      # Cover image
│       ├── manuscript/
│       │   ├── 00-frontmatter.md
│       │   ├── 01-chapter-1.md
│       │   └── ...
│       └── output/
│           ├── <book-id>.pdf
│           └── <book-id>.epub
├── scripts/
│   └── build.py               # Build automation script
├── templates/
│   ├── book.typ               # Typst template for PDF
│   └── epub.css               # CSS styles for EPUB
└── README.md
```

## 🚀 Quick Start

### Prerequisites

Install the required tools:

```bash
# Install Pandoc (document converter)
brew install pandoc

# Install Typst (for PDF generation)
brew install typst

# Install Python dependencies
pip install pyyaml
```

### Building Books

```bash
# Build all books (PDF + EPUB)
python scripts/build.py

# Build a specific book
python scripts/build.py palantir
python scripts/build.py rocketlab

# Build only PDF
python scripts/build.py palantir --pdf

# Build only EPUB
python scripts/build.py palantir --epub

# List available books
python scripts/build.py --list
```

## 📝 Creating a New Book

1. **Create the book directory:**

```bash
mkdir -p books/003-mybook/{images,manuscript,output}
```

2. **Create `metadata.yaml`:**

```yaml
# Book Metadata
title: "Your Book Title"
subtitle: "An Optional Subtitle"
author: "Your Name"
date: "2025"
language: en

# Cover Image (relative to images/ folder)
cover_image: cover.jpg

# Table of Contents
toc: true
toc_depth: 3

# Chapter Numbering
number_sections: true

# PDF Styling
pdf:
  paper_size: "us-letter"
  font_size: "11pt"
  colors:
    primary: "#2c3e50"
    accent: "#3498db"

# EPUB Styling
epub:
  chapter_level: 1

# Book Description
description: |
  A brief description of your book for metadata purposes.

# Keywords
keywords:
  - keyword1
  - keyword2
```

3. **Add your manuscript files** in `manuscript/`:
   - `00-frontmatter.md` — Executive summary, preface, etc.
   - `01-chapter-1.md` — First chapter
   - `02-chapter-2.md` — Second chapter
   - etc.

4. **Add a cover image** (optional):
   - Place `cover.jpg` in the `images/` folder

5. **Build your book:**

```bash
python scripts/build.py mybook
```

## 🎨 Templates

### PDF Template (`templates/book.typ`)

The Typst template provides:
- Professional book margins (inside/outside for binding)
- Running headers with title and author
- Elegant chapter title pages
- Configurable typography (Libertinus Serif by default)
- Page numbers

### EPUB Stylesheet (`templates/epub.css`)

The EPUB CSS provides:
- Clean, readable typography
- Styled headings with accent colors
- Proper paragraph indentation
- Responsive tables and code blocks
- Blockquote styling

## 📋 Build Output

After building, you'll find the generated files in each book's `output/` directory:

- `<book-id>.pdf` — High-quality PDF with cover
- `<book-id>.epub` — E-reader compatible EPUB

## 🔧 Technical Details

### Build Process

1. **PDF Generation:**
   - Pandoc converts Markdown to PDF using Typst as the PDF engine
   - Cover image is compiled separately and merged with content
   - Uses macOS PDF merge tools (with qpdf fallback)

2. **EPUB Generation:**
   - Pandoc converts Markdown directly to EPUB
   - Custom CSS styling is applied
   - Cover image is embedded in the EPUB

### Supported Features

- ✅ Markdown (CommonMark + Pandoc extensions)
- ✅ Images and figures
- ✅ Tables
- ✅ Code blocks with syntax highlighting
- ✅ Blockquotes
- ✅ Footnotes
- ✅ Cross-references
- ✅ Math equations (LaTeX syntax)

## 📄 License

This project and its contents are proprietary. All rights reserved.

---

*Built with ❤️ using Pandoc and Typst*
