# Phase 6: about page and metadata

**Company name:** the user-provided name.
**Book folder:** `books/<NNN>-<slug>/`.

## Goal

Generate all Leanpub-facing content: the about page fields, final metadata, and the frontmatter (executive summary). These must reflect the actual content of the finished manuscript.

## Process

### 1. Read the manuscript

Read the full manuscript to extract the key facts, thesis, and themes for the about page. At minimum, read:

- `books/<NNN>-<slug>/manuscript/00-frontmatter.md` (may still be empty from phase 1)
- `books/<NNN>-<slug>/manuscript/01-<first-chapter>.md` (introduction, to capture the hook and thesis)
- `books/<NNN>-<slug>/manuscript/<NN>-<financials-chapter>.md` (to pull the latest financial data)
- `books/<NNN>-<slug>/manuscript/<NN>-<final-chapter>.md` (conclusion, for the synthesis)

Also read `books/<NNN>-<slug>/.research/chapter-plan.md` to understand the intended thesis.

### 2. Write the frontmatter (00-frontmatter.md)

The frontmatter is the executive summary that opens the book. It has no H1 heading. It should:

- Open with a hook: a provocative or surprising statement about the company.
- State the book's thesis in 2 to 3 sentences.
- List the key findings (6 to 10 bullet points) with specific numbers and facts from the manuscript.
- Close with a paragraph on what makes this analysis different from others.

Read existing frontmatter files (`books/001-palantir/manuscript/00-frontmatter.md`, `books/002-rocketlab/manuscript/00-frontmatter.md`) to match the format and depth.

### 3. Populate about.md fields

Update `books/<NNN>-<slug>/about.md` with:

#### Book Title and Subtitle
Review the working title from metadata.yaml and refine it based on what the manuscript actually argues. The title must:

1. Include the company name for discoverability (readers search for the company).
2. Be catchy and memorable, not generic. Avoid words like "Story", "Journey", "Rise", "Tale".
3. Capture something specific about this company. The word or phrase after the company name should evoke the thesis or the company's distinctive quality.
4. Vary in structure from other books in the repo. Do not default to "The <Company> <Noun>" every time. Examples of different structures:
   - "The Palantir Enigma" (article + company + evocative noun)
   - "Rocket Lab: The Small Launch Revolution" (company + colon + tagline)
   - "SpaceX and the Reusable Future" (company + "and the" + thematic phrase)
   - "Anduril's Defense" (company possessive + thematic word)

If the working title from phase 1 already meets these criteria, keep it. If the manuscript revealed a stronger angle, rename accordingly.

#### About the Book
Write a comprehensive description (see `books/001-palantir/about.md` for length and depth). This should:
- Open with why this company matters.
- State what the book covers.
- List 4 to 6 bullet highlights of what readers will find inside.
- Include specific numbers from the manuscript (revenue, growth rates, market cap, etc.).
- End with who should read this book and why.
- Include "current as of <Month Year>" to anchor the data freshness.
- No em dashes.

#### Teaser text
One or two sentences that appear on the Leanpub book page. Should hook the reader with a question or surprising fact. Include "current as of <Month Year>".

#### Meta description
SEO description under 160 characters. Include key topics and the freshness date.

#### Table of contents HTML
Generate from the actual chapter titles in the manuscript:

```html
<p>Overview</p>
<p>Chapter 1: <title></p>
<p>Chapter 2: <title></p>
...
```

Use `&amp;` for ampersands in HTML.

#### What's new in this edition
Since this is the first edition, write: "This is the first edition, published <Month Year>."

### 4. Finalize metadata.yaml

Update `books/<NNN>-<slug>/metadata.yaml`:

- `title` and `subtitle`: confirm they match about.md (update if the about page refined them).
- `date`: current month and year.
- `last_published`: today's ISO date.
- `description`: a one-paragraph description for the book's metadata (shorter than the About section).
- `keywords`: 6 to 10 tags including the company name, industry, and key themes.
- `pdf.colors`: confirm the primary and accent colors fit the company's theme.

### 5. Verify title consistency

The book title must be identical in:
- `metadata.yaml` title field
- `about.md` Book Title section
- `00-frontmatter.md` (if the title appears)
- Manuscript chapter 1 (if the title appears)

If any of these disagree, reconcile them.

## Writing conventions

- No em dashes in any about.md text.
- Sentence-case headings.
- No edition numbering anywhere.
- The tone in about.md should be authoritative and enticing, not salesy.

## Success criteria

- `00-frontmatter.md` is populated with a hook, thesis, key findings, and differentiation.
- `about.md` has all Leanpub fields populated (title, subtitle, about, teaser, meta description, TOC HTML, release notes).
- `metadata.yaml` is finalized with correct title, date, description, and keywords.
- All financial numbers in about.md match the manuscript.
- No em dashes, no edition numbering, sentence-case headings.
- Title is consistent across metadata.yaml, about.md, and frontmatter.

Report back with a summary of what was populated and any fields where you made a judgment call that the user should review.
