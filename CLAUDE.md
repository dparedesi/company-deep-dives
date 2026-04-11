# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

Book publishing system for analytical deep-dive books about companies. Markdown in, PDF + EPUB out. Published on Leanpub.

## Build commands

```bash
python scripts/build.py                  # Build all books
python scripts/build.py palantir         # Build specific book
python scripts/build.py palantir --pdf   # PDF only
python scripts/build.py palantir --epub  # EPUB only
python scripts/build.py --list           # List available books
```

Book slug comes from folder name: `001-palantir` -> `palantir`, `002-rocketlab` -> `rocketlab`.

Build must run from repo root (`scripts/build.py` resolves paths relative to its parent's parent).

**File naming:**
- Folders: `<NNN>-<slug>` (3-digit number, e.g., `003-spacex`)
- Chapters: `<NN>-<name>.md` (2-digit prefix, sorted alphabetically for ordering)
- Output: named after folder (e.g., `001-palantir.pdf`)

## Architecture

```
books/<NNN>-<slug>/          # Each book self-contained
  metadata.yaml              # Title, author, date, styling config
  cover-prompt.md            # Detailed prompt for AI cover image generation
  images/cover.jpg           # Cover
  manuscript/                # Markdown chapters, sorted alphabetically
    00-frontmatter.md        # Executive summary (no H1 heading)
    01-chapter-1.md          # Starts with # Chapter Title
    ...
  output/                    # Generated .pdf and .epub

scripts/build.py             # Pandoc wrapper: markdown -> PDF/EPUB
templates/book.typ           # Typst template for PDF (running headers, chapter pages, TOC)
templates/epub.css           # CSS for EPUB readers (night mode support built in)
.Resources/prompts/          # Workflow prompts for researching and updating chapters
```

**Build pipeline:** Pandoc reads sorted `.md` files -> applies Typst template (PDF) or CSS (EPUB) -> if cover exists, Typst compiles it to PDF and merges via macOS Automator tool (falls back to `qpdf`).

**Dependencies:** Pandoc, Typst (`brew install pandoc typst`), Python + PyYAML.

## Writing conventions

- **No em dashes** — use colons, commas, parentheses, or separate sentences
- **Sentence case for headings** — only first word and proper nouns capitalized
- **Acronyms uppercase** — AI, NASA, CEO, API, IPO
- **Expanded acronyms** — capitalize proper noun portions only: "National Aeronautics and Space Administration (NASA)"
- **Chapter files start with `# Title`** (H1) — this triggers page breaks in the Typst template
- **Frontmatter** (`00-frontmatter.md`) has no H1 heading

## Creating a new book

1. Create folder: `books/<NNN>-<slug>/` with `images/`, `manuscript/`, `output/` subdirs
2. Copy `metadata.yaml` from an existing book and update fields (title, author, date, description, colors)
3. Add `images/cover.jpg` for the cover page
4. Create `cover-prompt.md` with a detailed prompt for AI cover image generation (see existing books for format)
5. Create manuscript files with numbered prefixes: `00-frontmatter.md`, `01-chapter-1.md`, etc.
6. Chapter files start with `# Title` (H1); frontmatter has no H1
7. Run `python scripts/build.py <slug>`

## Updating an existing book

1. Edit manuscript files in `books/<NNN>-<slug>/manuscript/`
2. Update `metadata.yaml` if title, date, or description changes
3. Run `python scripts/build.py <slug>`
4. Output lands in `books/<NNN>-<slug>/output/`

## Cover image workflow

The PDF cover page renders at US Letter (8.5 x 11 inches, ratio 1:1.294). Image generators (ChatGPT, Gemini) rarely output this exact ratio. The cover must be fitted before building.

**Process:**

1. Generate the cover using the prompt in `cover-prompt.md`. Send it to ChatGPT, Gemini, or any image generator.
2. Pick the best result and place the file in `images/` (for example, `ChatGPT.png`, `Gemini.png`).
3. Check the image dimensions with `sips -g pixelWidth -g pixelHeight <file>`.
4. Calculate the target width for US Letter ratio: `target_width = height * 8.5 / 11`.
5. Pad the sides to reach the target width using ImageMagick with the correct background color:
   ```
   magick <input> -background "<HEX_COLOR>" -gravity center -extent <target_width>x<height> images/cover-padded.png
   ```
6. Convert to JPEG: `sips -s format jpeg images/cover-padded.png --out images/cover.jpg`.
7. Build and visually verify: `python scripts/build.py <slug>` then `open output/<NNN>-<slug>.pdf`.

**Getting the exact background color:** Image generators use a background color that may not match the hex in `metadata.yaml`. Ask the user to sample the exact color from the image using a color picker (for example, imagecolorpicker.com, macOS Digital Color Meter, or any eyedropper tool) and provide the hex code. Use that exact color for padding so the bars blend seamlessly.

**Key details:**
- Always pad (extend canvas), never stretch or crop. Stretching distorts the design; cropping loses content.
- ChatGPT consistently outputs 1024 x 1536 (2:3 ratio), which needs widening to ~1187 x 1536 for US Letter.
- The padding step is only needed for the PDF. The EPUB cover uses the original image directly via Pandoc's `--epub-cover-image`.
- Keep the original generator output file in `images/` alongside the processed `cover.jpg` for future reference.

## Troubleshooting

- **Missing chapters in output:** check that filenames have sequential numeric prefixes and end in `.md`
- **Cover not showing:** ensure `cover_image: cover.jpg` is set in `metadata.yaml` and the file exists in `images/`
- **PDF build fails:** verify Typst is installed (`brew install typst`); the script falls back to LaTeX if missing

## Monthly book refresh workflow

Use the `/book-refresh <slug>` skill to publish a new monthly edition of any deep-dive book. The skill handles research, per-chapter updates, consistency review, release notes, and build.

**Invocation:** `/book-refresh palantir` or `/book-refresh rocketlab`

**The six-step workflow:**

1. **Research delta** (`01-research-delta.md`): Deep research pass for everything material about the company since `last_published` in metadata.yaml. Uses MCP tools `mcp__zai-web-search__web_search_prime` and `mcp__web_reader__webReader`. Output: `books/<NNN>-<slug>/.research/<YYYY-MM>-delta.md`

2. **Fan out findings** (`02-fan-out-findings.md`): Transform research into per-chapter change list. Output: `books/<NNN>-<slug>/.research/<YYYY-MM>-changes.md`

3. **Update each chapter** (`03-update-chapter.md`): Apply change list to chapters in order of volatility (4, 5, 6, 7, 8, 9, 2, 3, 1, 10 for a 10-chapter book). Preserves voice and style.

4. **Consistency review** (`04-consistency-review.md`): Cross-chapter pass for contradictions in numbers, dates, contracts, thesis language, and terminology.

5. **Release notes** (`05-release-notes.md`): Generate "What's new in this edition" section for the about page from research and changes.

6. **Build**: Run `python scripts/build.py <slug>` to generate PDF and EPUB in `books/<NNN>-<slug>/output/`

**Metadata fields to bump each month:**

- `date: "<Month Year>"`: Human-readable edition label (for example, "April 2026")
- `last_published: "<YYYY-MM-DD>"`: ISO date of the previous edition (anchors the next research delta window)

**Edition model:** Date-based, not numbered. Use "April 2026 edition", never "Second Edition". Leanpub archives prior editions automatically.
