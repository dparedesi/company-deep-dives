---
name: book-refresh
description: Publish a new monthly or quarterly edition of an existing deep-dive book in books/<NNN>-<slug>/. Use when the user says "refresh the <book> book", "new edition", "publish an update", "roll the book forward", "bring it current", or mentions a monthly, quarterly, or periodic refresh of any existing book in this repo. Handles the research delta, per-chapter updates, consistency review, metadata bumps, release notes, and build. Not for creating a new book (that is /create-book).
argument-hint: <slug>
---

# book-refresh

**Why?** A deep-dive book starts going stale the day it ships: prices move, quarters print, contracts land, theses break. Without a repeatable pipeline, each book decays toward uselessness and ad-hoc updates drift into internal contradictions. This skill turns a published book into a living, dated edition through a windowed research delta, chapter-level updates, and a consistency pass, without rewriting what already works.

## When to use this skill

Use this skill when the user asks to publish a new edition of any deep-dive book in `books/<NNN>-<slug>/`. Triggers include "refresh the Palantir book", "new edition of Rocket Lab", "publish an update", "bring the Nvidia book current", or any phrasing that implies rolling the book forward to a new monthly (or quarterly) cut. The skill is book-agnostic: it takes a slug like `palantir` or `rocketlab` as input and operates on the corresponding `books/<NNN>-<slug>/` directory. Creating a brand-new book is a different skill (`/create-book`).

## The edition model

Editions are **date-based**, not numbered. A new release is "April 2026 edition", never "Third Edition". The book identity (title, subtitle) does not encode an edition number and must never be changed to add one.

Two `metadata.yaml` fields anchor the edition:

- `date: "<Month Year>"`: human-readable edition label (for example, `"April 2026"`). Updated every refresh, in step 5, because step 6 needs the new label.
- `last_published: "<YYYY-MM-DD>"`: ISO date of the previous release. This is the delta window anchor that the research step uses to decide what to look for. It is updated at the very end of the cycle, in step 7, only after the build verifies, so an interrupted cycle never records a release that did not happen.

Leanpub's built-in version history archives prior editions for readers, so nothing in the book's title, subtitle, frontmatter, or about page needs to reference "First Edition", "Second Edition", or earlier release dates. If you find that language, strip it.

## Cadence

Default cadence is **monthly**. The skill works for any cadence: it reads `last_published` from metadata and treats everything since that date as the delta window, so quarterly or ad-hoc refreshes work identically. Step 1 measures the window in days and confirms with the user before sweeping a window that exceeds 95 days.

## Shared standards

Every step that writes or edits manuscript prose reads `.Resources/voice.md` (the voice charter) before editing, and follows it exactly. Step 4 additionally reads `.Resources/quality-bar.md` (the quality bar) and runs it as its review pass. Both files are the single source of truth for voice and quality; step prompts reference them by path and never restate their rules. The project `CLAUDE.md` writing conventions (no em dashes, sentence-case headings, acronyms uppercase, chapter files start with an H1, frontmatter has no H1) stay in force alongside both files.

## Pre-flight (run before step 1)

Verify the book is refreshable. Two checks, in order:

1. **Metadata fields.** `books/<NNN>-<slug>/metadata.yaml` must have `last_published` as an ISO date (`YYYY-MM-DD`) and `date` in `"<Month Year>"` format (for example `"April 2026"`).
2. **About page.** `books/<NNN>-<slug>/about.md` must exist and contain all seven Leanpub field headers: `## Book Title:`, `## Subtitle:`, `## About the Book:`, `## Teaser text:`, `## Meta description:`, `## Table of contents HTML:`, `## What's new in this edition`. No field may contain placeholder text.

If either check fails, repair before continuing:

- **Missing or malformed `last_published`**: ask the user for the ISO date of the last real published edition and write it in. If `date` is not in `"<Month Year>"` format, set it to the current `<Month Year>`. If the user cannot supply the date, stop and report that the book is not refreshable. Do not guess.
- **Missing, incomplete, or placeholder-containing `about.md`**: create or rebuild it in two passes. First, create the file with the seven headers using the structure in `.claude/skills/create-book/01-setup.md` step 5. Second, populate every field with real content following `.claude/skills/create-book/06-about-and-metadata.md` section 3: title and subtitle from `metadata.yaml`; About the Book, Teaser text, and Meta description written from the manuscript, using `books/001-palantir/about.md` as the format and depth reference; Table of contents HTML generated from the actual chapter H1 titles (`&amp;` for ampersands). The What's new section may say "This is the first tracked edition, published <Month Year>." since step 6 regenerates it. Then run the title consistency check from `06-about-and-metadata.md` section 5: the `metadata.yaml` title must equal the about.md Book Title.

Report all repairs performed, then continue with step 1.

## The seven-step workflow

Run these steps in order for each refresh. Each numbered file under `.claude/skills/book-refresh/` is a self-contained prompt; invoke them by reading the file and following its instructions with the book slug filled in.

1. **Research delta** (`01-research-delta.md`): one consolidated web-research pass for everything material about the book's subject since `last_published`, including resolving expired thesis milestones, scoring the prior edition's forecasts, and re-pulling valuation and dashboard numbers. Output goes to `books/<NNN>-<slug>/.research/<YYYY-MM>-delta.md`.
2. **Fan out findings** (`02-fan-out-findings.md`): turn the research file into a per-chapter change list at `books/<NNN>-<slug>/.research/<YYYY-MM>-changes.md`, including explicit deletions of superseded blocks. Structural change proposals are flagged for the user, never applied silently.
3. **Update each chapter** (`03-update-chapter.md`): apply the change list to one chapter at a time, in the standing story's narrative voice, so updates land as narrative inside the existing prose rather than as delta markers (per the charter's edition refresh rule). Determine chapter ordering dynamically (see below).
4. **Consistency review** (`04-consistency-review.md`): cross-chapter pass for contradictions (numbers, dates, contract values, thesis language, terminology), then the quality-bar pass from `.Resources/quality-bar.md`.
5. **Metadata and framing update** (`05-metadata-framing.md`): update `metadata.yaml`, `about.md`, and `00-frontmatter.md` to reflect the new edition date. Strip any edition-numbering language.
6. **Release notes** (`06-release-notes.md`): regenerate the "What's new in this edition" section in `about.md` from the research file, the changes file, and the git diff of the manuscript.
7. **Build** (`07-build.md`): run `python scripts/build.py <slug>` from the repo root, verify the output, then bump `last_published` after both outputs verify. The step then commits and pushes the edition as one commit (the book directory plus this edition's `.research/` artifacts, repo-style message with attribution footer, nothing else staged). After the push, `/publish-release <slug>` prepares the reader notification.

### Chapter ordering (step 3)

Do not hardcode chapter numbers. Instead, read each chapter's H1 title and determine ordering by volatility:

- **High volatility** (update first): chapters covering financials, market/competition, use cases, ethics, risk, and future outlook. These move every month.
- **Medium volatility**: chapters covering technology/products, history/leadership.
- **Low volatility** (update last): introduction, conclusion, frontmatter. These mostly need cross-reference fixes after the main chapters move.

Read the chapter titles at the start of step 3 and order accordingly. The number-to-topic mapping differs across the repo's books, so any fixed numeric order is wrong for most of them. Adapt for books with different chapter structures.

## Generalization

This skill takes a book slug as input. Everywhere a path appears, substitute the folder number and slug:

- Manuscript chapters: `books/<NNN>-<slug>/manuscript/<NN>-<name>.md`
- Metadata: `books/<NNN>-<slug>/metadata.yaml`
- About page: `books/<NNN>-<slug>/about.md`
- Frontmatter: `books/<NNN>-<slug>/manuscript/00-frontmatter.md`
- Research artifacts: `books/<NNN>-<slug>/.research/` (create if missing), including the monthly delta, changes, applied ledger, consistency notes, and the claims register
- Build output: `books/<NNN>-<slug>/output/`

Nothing in this skill is hardcoded to Palantir or any specific book. If a prompt needs the book subject (company name, focus area), read it from `books/<NNN>-<slug>/metadata.yaml` at the start of the step. Wherever a chapter is referenced by role (financials, outlook, ethics), locate the actual file by its H1 title in the current book, never by a fixed number.
