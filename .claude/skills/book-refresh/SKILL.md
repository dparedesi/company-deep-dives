---
name: book-refresh
description: Publish a new monthly edition of a deep-dive book in books/<NNN>-<slug>/. Use when the user says "refresh the <book> book", "new edition", "publish an update", or mentions monthly/quarterly refresh of a book in this repo. Handles research, per-chapter updates, consistency review, metadata bumps, and build.
argument-hint: <slug>
---

# book-refresh

## When to use this skill

Use this skill when the user asks to publish a new edition of any deep-dive book in `books/<NNN>-<slug>/`. Triggers include "refresh the Palantir book", "new edition of Rocket Lab", "publish an update", or any phrasing that implies rolling the book forward to a new monthly (or quarterly) cut. The skill is book-agnostic: it takes a slug like `palantir` or `rocketlab` as input and operates on the corresponding `books/<NNN>-<slug>/` directory.

## The edition model

Editions are **date-based**, not numbered. A new release is "April 2026 edition", never "Third Edition". The book identity (title, subtitle) does not encode an edition number and must never be changed to add one.

Two `metadata.yaml` fields anchor the edition:

- `date: "<Month Year>"`: human-readable edition label (for example, `"April 2026"`). Updated every refresh.
- `last_published: "<YYYY-MM-DD>"`: ISO date of the previous release. This is the delta window anchor that the research step uses to decide what to look for. Updated every refresh, at the end of the cycle, to the release date of the new edition.

Leanpub's built-in version history archives prior editions for readers, so nothing in the book's title, subtitle, frontmatter, or about page needs to reference "First Edition", "Second Edition", or earlier release dates. If you find that language, strip it.

## Cadence

Default cadence is **monthly**. The skill works for any cadence: it reads `last_published` from metadata and treats everything since that date as the delta window, so quarterly or ad-hoc refreshes work identically.

## The seven-step workflow

Run these steps in order for each refresh. Each numbered file under `.claude/skills/book-refresh/` is a self-contained prompt; invoke them by reading the file and following its instructions with the book slug filled in.

1. **Research delta** (`01-research-delta.md`): one consolidated web-research pass for everything material about the book's subject since `last_published`. Output goes to `books/<NNN>-<slug>/.research/<YYYY-MM>-delta.md`.
2. **Fan out findings** (`02-fan-out-findings.md`): turn the research file into a per-chapter change list at `books/<NNN>-<slug>/.research/<YYYY-MM>-changes.md`.
3. **Update each chapter** (`03-update-chapter.md`): apply the change list to one chapter at a time. Determine chapter ordering dynamically (see below).
4. **Consistency review** (`04-consistency-review.md`): cross-chapter pass for contradictions (numbers, dates, contract values, thesis language) and fix any drift.
5. **Metadata and framing update** (`05-metadata-framing.md`): update `metadata.yaml`, `about.md`, and `00-frontmatter.md` to reflect the new edition date. Strip any edition-numbering language.
6. **Release notes** (`06-release-notes.md`): regenerate the "What's new in this edition" section in `about.md` from the research file, the changes file, and the git diff of the manuscript.
7. **Build** (`07-build.md`): run `python scripts/build.py <slug>` from the repo root. Verify the output.

### Chapter ordering (step 3)

Do not hardcode chapter numbers. Instead, read each chapter's H1 title and determine ordering by volatility:

- **High volatility** (update first): chapters covering financials, market/competition, use cases, ethics, risk, and future outlook. These move every month.
- **Medium volatility**: chapters covering technology/products, history/leadership.
- **Low volatility** (update last): introduction, conclusion, frontmatter. These mostly need cross-reference fixes after the main chapters move.

Read the chapter titles at the start of step 3 and order accordingly. For a typical 10-chapter company deep dive, the order is usually: financials, market, use cases, ethics, risk, outlook, history, technology, introduction, conclusion. Adapt for books with different chapter structures.

## Generalization

This skill takes a book slug as input. Everywhere a path appears, substitute the folder number and slug:

- Manuscript chapters: `books/<NNN>-<slug>/manuscript/<NN>-<name>.md`
- Metadata: `books/<NNN>-<slug>/metadata.yaml`
- About page: `books/<NNN>-<slug>/about.md`
- Frontmatter: `books/<NNN>-<slug>/manuscript/00-frontmatter.md`
- Research artifacts: `books/<NNN>-<slug>/.research/` (create if missing)
- Build output: `books/<NNN>-<slug>/output/`

Nothing in this skill is hardcoded to Palantir or any specific book. If a prompt needs the book subject (company name, focus area), read it from `books/<NNN>-<slug>/metadata.yaml` at the start of the step.

## Writing conventions reminder

Respect writing conventions in project `CLAUDE.md`: no em dashes, sentence-case headings, acronym rules, chapter files start with `# Title`, frontmatter has no H1.
