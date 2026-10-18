# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

Book publishing system for analytical deep-dive books about companies. Markdown in, PDF + EPUB out. Published on Leanpub.

## North star

The long-term goal is an autonomous book producer and maintainer whose output passes one test: would a discerning reader pay a premium because this is the definitive, most reliable, most compelling book on this company? Every skill change, chapter edit, and review pass in this repo is judged against that test, not just against internal consistency.

- **One author.** Every book must read like the same person wrote it: same voice, same care, same depth. The canonical voice is defined in `.Resources/voice.md` (the voice charter); read it before writing or editing any manuscript prose.
- **Books never reference each other.** Readers are not collectors. What is shared is the voice, never cross-marketing.
- **Bestseller storytelling, factual rigor.** Chapters hook, build tension, and pull the reader forward. Executives and engineers appear as characters with agency, not names attached to events. Factual claims stay traceable to research artifacts.
- **Conviction over fence-sitting.** Present bullish, bearish, and neutral theses with their best evidence, then land on a defensible house view with named falsifiers. Never dissolve into "it remains to be seen".
- **Depth compounds across editions.** Each edition raises the bar: more primary-source grounding, sharper theses, better narrative. The reader should feel the accumulated effort from first version to every iteration.
- **Quality bar is explicit.** The premium test is operationalized as checklists in `.Resources/quality-bar.md`. Writers write to it, reviewers review against it.

Improvements to skills and manuscripts are not mechanical rule-patching. Detecting and correcting drift is necessary but never sufficient; the goal is that no reader can tell a machine wrote it.

## Build commands

```bash
python scripts/build.py                  # Build all books
python scripts/build.py palantir         # Build specific book
python scripts/build.py palantir --pdf   # PDF only
python scripts/build.py palantir --epub  # EPUB only
python scripts/build.py --list           # List available books

python scripts/lint_manuscript.py        # Quality gates, all books (report mode exits 0)
python scripts/lint_manuscript.py palantir  # Quality gates for one book
```

Builds run the quality gates (`.Resources/quality-bar.md`, "Gates" section) before compiling and fail closed, listing every hit with file and line. `--skip-lint` bypasses the gates; use it only before a book has been remediated to the bar.

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

scripts/build.py             # Pandoc wrapper: markdown -> PDF/EPUB, runs quality gates first
scripts/lint_manuscript.py   # Quality-bar gates: mechanical scans, fail closed
templates/book.typ           # Typst template for PDF (running headers, chapter pages, TOC)
templates/epub.css           # CSS for EPUB readers (night mode support built in)
.Resources/voice.md          # Voice charter: single source of truth for the narrative voice
.Resources/quality-bar.md    # Quality bar: premium test, checklists, and build gates
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

Use the `/create-book <company>` skill. It runs the full pipeline: setup, team-based deep research in waves, chapter planning with user approval, depth-assessed parallel writing, a depth-quality audit, consistency review against the quality bar, about page generation, build, and commit-and-push. The manual steps below document the underlying conventions:

1. Create folder: `books/<NNN>-<slug>/` with `images/`, `manuscript/`, `output/` subdirs
2. Copy `metadata.yaml` from an existing book and update fields (title, author, date, description, colors)
3. Add `images/cover.jpg` for the cover page
4. Create `cover-prompt.md` with a detailed prompt for AI cover image generation (see existing books for format)
5. Create manuscript files with numbered prefixes: `00-frontmatter.md`, `01-chapter-1.md`, etc.
6. Chapter files start with `# Title` (H1); frontmatter has no H1
7. Run `python scripts/build.py <slug>`

## Updating an existing book

For a new edition, use `/book-refresh <slug>` (next section). Manual edits are for quick fixes; note that the build gates still apply.

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

**Getting the exact background color:** Image generators use a background color that may not match the hex in `metadata.yaml` `pdf.colors.primary`. Do NOT assume the metadata color matches. Instead:
1. Check if `cover_bg_color` exists in `metadata.yaml`. If so, use it directly.
2. If not, ask the user to sample the exact color from the image using a color picker (for example, imagecolorpicker.com, macOS Digital Color Meter, or any eyedropper tool) and provide the hex code.
3. After sampling, **store it in `metadata.yaml`** as `cover_bg_color: "<HEX>"` so the cover can be regenerated later without re-sampling.

**Key details:**
- Always pad (extend canvas), never stretch or crop. Stretching distorts the design; cropping loses content.
- ChatGPT consistently outputs 1024 x 1536 (2:3 ratio), which needs widening to ~1187 x 1536 for US Letter.
- The padding step is only needed for the PDF. The EPUB cover uses the original image directly via Pandoc's `--epub-cover-image`.
- Keep the original generator output file in `images/` alongside the processed `cover.jpg` for future reference.

## Troubleshooting

- **Build blocked by quality gates:** run `python scripts/lint_manuscript.py <slug>` for the full hit list with file and line; the gates are defined in `.Resources/quality-bar.md`
- **Missing chapters in output:** check that filenames have sequential numeric prefixes and end in `.md`
- **Cover not showing:** ensure `cover_image: cover.jpg` is set in `metadata.yaml` and the file exists in `images/`
- **PDF build fails:** verify Typst is installed (`brew install typst`); the script falls back to LaTeX if missing

## Monthly book refresh workflow

Use the `/book-refresh <slug>` skill to publish a new edition of any deep-dive book. It runs a pre-flight (metadata fields and about.md completeness, repairing what it can), then seven steps, each a self-contained prompt in `.claude/skills/book-refresh/`:

1. **Research delta** (`01-research-delta.md`): everything material since `last_published`, plus scoring the prior edition's forecasts and re-pulling valuation and dashboard numbers. Output: `books/<NNN>-<slug>/.research/<YYYY-MM>-delta.md`
2. **Fan out findings** (`02-fan-out-findings.md`): per-chapter change list at `.research/<YYYY-MM>-changes.md`; structural change proposals are flagged for the user, never applied silently
3. **Update each chapter** (`03-update-chapter.md`): apply changes chapter by chapter in the standing narrative voice; ordering is dynamic, by volatility read from H1 titles (financials, market, risk first; introduction and conclusion last), never hardcoded chapter numbers
4. **Consistency review** (`04-consistency-review.md`): contradictions pass plus the quality bar; the review persists to `.research/<YYYY-MM>-review.md`, which `/publish-release` gates on
5. **Metadata and framing** (`05-metadata-framing.md`): edition-date fields in metadata.yaml, about.md, and frontmatter
6. **Release notes** (`06-release-notes.md`): regenerates "What's new in this edition" in about.md
7. **Build** (`07-build.md`): build with the quality gates, verify outputs, bump `last_published` only after both outputs verify, then commit and push the edition as one commit

**Metadata anchors:** `date: "<Month Year>"` is the edition label; `last_published: "<YYYY-MM-DD>"` is the delta window anchor, bumped only at the end of step 7 after the build verifies.

**Edition model:** date-based, never numbered ("April 2026 edition", never "Third Edition"). Leanpub archives prior editions automatically.

**Editions iterate, never replace:** refreshes preserve chapter structure, existing scenes and arguments that still hold, and the book's voice; the quality bar's iteration-continuity section governs the diff.

**Publication:** after the push, `/publish-release <slug>` verifies the build and the persisted review, fixes stale facts in about.md, generates the reader email, and commits and pushes its changes. The Leanpub notify step itself is manual. First editions never run `/publish-release`.

**Staleness pre-flight:** when any pipeline skill runs, scan `books/*/metadata.yaml` and report books whose `last_published` is more than 35 days in the past or missing; the pipeline exists to keep every book current.

## Next-book selection workflow

Use the `/next-books` skill to research which company to write about next. It spawns 6 to 8 angle agents in waves using duckduckgo MCP search, consolidates a scored ranking, and writes a normative-template report to `.research/next-books/<YYYY-MM-DD>-report.md` (each run in its own dated directory), then commits and pushes the run. When you pick a company, it hands off to `/create-book`.
