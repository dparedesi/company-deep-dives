# Phase 1: setup

**Company name:** the user-provided name (for example, "SpaceX", "Stripe", "Anduril"). The caller must supply this.

## Goal

Create the book folder structure and starter files so that subsequent phases have a working directory to write into.

## Process

### 1. Determine slug and folder number

- Slug: lowercase, hyphenated. "SpaceX" becomes "spacex", "Rocket Lab" becomes "rocketlab", "Palantir Technologies" becomes "palantir". Strip common suffixes like "Technologies", "Inc", "Corp", "Ltd".
- Folder number: list existing `books/` directories, find the highest NNN, increment by 1. Pad to 3 digits (for example, `003`).
- Folder path: `books/<NNN>-<slug>/`

### 2. Create directory structure

```
books/<NNN>-<slug>/
  metadata.yaml
  about.md
  images/
    cover.jpg
  manuscript/
    00-frontmatter.md
  output/
  .research/
```

### 3. Create metadata.yaml

Copy the metadata.yaml from `books/001-palantir/metadata.yaml` as a template. Update:

- `title`: A working title. Use the pattern "The <Company> <Something>" or a distinctive phrase. This is a placeholder; the user may change it later.
- `subtitle`: A working subtitle that captures the core thesis angle. Placeholder.
- `date`: Current month and year (for example, "April 2026").
- `last_published`: Today's ISO date.
- `description`: A one-paragraph placeholder describing the book's scope.
- `keywords`: Company name and 5 to 7 relevant tags.
- `pdf.colors.primary` and `pdf.colors.accent`: Choose colors that fit the company's brand or theme.

Do not change: `author`, `toc`, `toc_depth`, `number_sections`, `pdf` layout settings, `fonts`, `epub.chapter_level`, `publisher`, `rights`.

### 4. Copy a placeholder cover

Copy the cover from any existing book (for example, `books/001-palantir/images/cover.jpg`) to `books/<NNN>-<slug>/images/cover.jpg`. The user will replace this with a proper cover later.

### 5. Create about.md

Write an about.md with all the standard Leanpub field headers, populated with placeholders:

```markdown
## Book Title:
<working title>

## Subtitle:
<working subtitle>

## About the Book:
<placeholder: will be populated in phase 6>

## Teaser text:
<placeholder>

## Meta description:
<placeholder>

## Table of contents HTML:
<placeholder: will be populated after chapter plan is approved>

## What's new in this edition
This is the first edition.
```

### 6. Create empty frontmatter

Write `books/<NNN>-<slug>/manuscript/00-frontmatter.md` with just a blank line. This will be populated in phase 6.

### 7. Create cover prompt

Write `books/<NNN>-<slug>/cover-prompt.md` with a detailed prompt for an image generation agent to create the book cover. The prompt should include:

- **Book title and subtitle** from the working metadata.
- **Visual concept** derived from the company's theme and industry. Think about what visual metaphor captures this company's story (cycles, networks, growth trajectories, disruption, etc.).
- **Color palette** using the primary and accent colors from metadata.yaml. Specify hex codes and describe how they should be used (dominant background vs accent highlights).
- **Composition** describing layout: title placement, central visual element, subtitle and author name placement.
- **Typography guidance**: serif for title (elegant, modern), sans-serif for subtitle and author. No italics on the title.
- **Mood**: authoritative, analytical, clean, minimal. This is a serious deep-dive, not a lightweight business book.
- **What to avoid**: company logos (trademark risk), product photos, generic stock imagery (globes, handshakes, arrows), more than 3 colors, gradients/gloss effects.
- **Reference style**: think Princeton University Press or MIT Press. Clean, geometric, confident, restrained.
- **Technical specs**: US Letter ratio (8.5 x 11 inches, which is 1:1.294). Request this explicitly. In pixels at 150 DPI: 1275 x 1650. Generators will likely ignore the exact ratio, so plan for a dimension fix step.
- **Cover dimension fix**: After the user provides the generated image, check its actual dimensions with `sips -g pixelWidth -g pixelHeight`. If the ratio does not match US Letter (1:1.294), pad the sides using ImageMagick: `magick <input> -background "<HEX_COLOR>" -gravity center -extent <target_width>x<height> cover-padded.png`. Calculate target width as `height * 8.5 / 11`. The background color must match the image's actual background exactly. Ask the user to sample it with a color picker and provide the hex code. Then convert to JPEG: `sips -s format jpeg cover-padded.png --out images/cover.jpg`. Never stretch or crop.
- **One-sentence summary** at the end.

Read `books/003-sandisk/cover-prompt.md` as an example of the expected depth and format.

## Success criteria

- `books/<NNN>-<slug>/` exists with all subdirectories.
- `metadata.yaml` is valid YAML with correct author, date, and working title.
- `about.md` exists with all Leanpub field headers.
- `images/cover.jpg` exists (placeholder).
- `manuscript/00-frontmatter.md` exists.
- `cover-prompt.md` exists with a complete, detailed image generation prompt.
- `.research/` and `output/` directories exist.

Report back with the folder path and the assigned NNN number.
