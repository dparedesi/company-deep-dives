---
name: create-book
description: Create a brand new company deep-dive book from scratch. Use when the user says "create a book about <company>", "new book", "write about <company>", or wants to start a deep-dive analysis of a company that does not yet have a book in this repo. Handles research with a team of agents, chapter planning, parallel chapter writing, consistency review, about page generation, and build.
argument-hint: <company-name>
---

# create-book

## Why?

Creating a company deep dive from scratch requires exhaustive research, thoughtful structure, and sustained voice across 80,000 to 150,000 words. A single agent cannot do this well. This skill orchestrates teams of agents for research and writing, producing a book that seeks truth through evidence, not bias.

## When to use

Use this skill when the user wants to create a brand new analytical deep-dive book about a technology company. Triggers include "create a book about SpaceX", "write about Anduril", "new deep dive on Stripe", or any phrasing that implies starting a book that does not yet exist in this repo.

If the book already exists, use `/book-refresh <slug>` instead.

## Core philosophy

The books in this repo seek truth, not a bias. The goal is the deepest, most factual, most comprehensive analysis humanly possible. Not generic pros/cons lists. Not fence-sitting neutrality. A genuine effort to surface the real signals.

If the evidence is bullish, say so. If bearish, say so. Usually it is a mix of signals across different dimensions, and the book should lay them all out with specificity and depth so the reader walks away feeling "this person actually did the work."

## The seven-phase workflow

Run these phases in order. Each numbered file under `.claude/skills/create-book/` is a self-contained prompt; invoke them by reading the file and following its instructions.

### Phase 1: Setup (`01-setup.md`)
Create the book folder with standard structure. Copy metadata.yaml from an existing book. Create empty about.md with Leanpub field headers. Create a cover-prompt.md with a detailed image generation prompt. Use a placeholder cover. Takes a company name (for example, "SpaceX") and determines the slug and folder number.

### Phase 2: Deep research (`02-deep-research.md`)
**Team of agents.** Spawn 5 to 8 research agents in parallel, each covering a different domain (financials, technology, market, history, customers, ethics, outlook, and company-specific domains). Each agent writes findings to `.research/`. Use `mode: bypassPermissions` for all agents. If an agent has not delivered output after 20 minutes, spawn a retry agent for that domain.

### Phase 3: Chapter planning (`03-chapter-planning.md`)
A single planning agent reads ALL research output and designs a chapter structure that fits this specific company. Proposes 8 to 12 chapters with titles and descriptions. Presents the plan to the user for approval before proceeding. If the user has explicitly authorized autonomous work (for example, "keep working non-stop" or "don't wait for me"), skip the approval and proceed directly.

### Phase 4: Chapter writing (`04-chapter-writing.md`)
**Team of agents.** After the user approves the chapter plan, spawn writing agents. Each agent handles 2 to 3 chapters, reads relevant research and the voice from existing books. Target 8,000 to 15,000 words per chapter. Use `mode: bypassPermissions` for all agents.

### Phase 5: Consistency review (`05-consistency-review.md`)
One agent reads all chapters straight through, checking for contradictory numbers, inconsistent terminology, thesis alignment, and voice consistency. Fixes issues directly.

### Phase 6: About page and metadata (`06-about-and-metadata.md`)
Generate all Leanpub fields in about.md. Finalize metadata.yaml. Write the frontmatter with executive summary and key findings.

### Phase 7: Build (`07-build.md`)
Run `python scripts/build.py <slug>` from the repo root. Verify PDF and EPUB output.

## Generalization

This skill takes a company name as input. Everywhere a path appears, substitute the folder number and slug:

- Manuscript chapters: `books/<NNN>-<slug>/manuscript/<NN>-<name>.md`
- Metadata: `books/<NNN>-<slug>/metadata.yaml`
- About page: `books/<NNN>-<slug>/about.md`
- Frontmatter: `books/<NNN>-<slug>/manuscript/00-frontmatter.md`
- Research artifacts: `books/<NNN>-<slug>/.research/`
- Build output: `books/<NNN>-<slug>/output/`

Nothing in this skill is hardcoded to any specific company. The slug, folder number, and company identity come from user input and metadata.yaml. Read existing books in the repo to learn the voice but do not copy their structure rigidly.

## Agent coordination rules

1. **Always use teams of agents for phases 2 and 4.** These are the heavy-lift phases where parallelism is essential. A single agent cannot produce the volume and depth required.
2. **Use `mode: bypassPermissions`** for all spawned agents. Research and writing agents get stuck in plan-approval loops otherwise.
3. **Each agent writes to its own file.** Never have two agents write to the same file simultaneously. Use separate research files per domain and separate chapter files per agent.
4. **Coordinate through the task list.** Create tasks for each phase and assign them to agents. Track completion via TaskUpdate.
5. **Join after each phase.** Wait for all agents in a phase to complete before proceeding to the next phase. Research must finish before chapter planning. Chapter plan must be approved before writing begins.

## Writing conventions

Respect writing conventions in project `CLAUDE.md`:

- No em dashes. Use colons, commas, parentheses, or separate sentences.
- Sentence-case headings. Only the first word and proper nouns are capitalized.
- Acronyms uppercase: AI, NASA, CEO, API, IPO.
- Expanded acronyms: capitalize proper noun portions only. "National Aeronautics and Space Administration (NASA)".
- Chapter files start with `# Title` (H1).
- Frontmatter (`00-frontmatter.md`) has no H1 heading.
- Learn the voice from existing books in `books/001-palantir/manuscript/` and `books/002-rocketlab/manuscript/`.
