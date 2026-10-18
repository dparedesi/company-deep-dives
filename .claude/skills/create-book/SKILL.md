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

## Shared standards

Every phase that writes, edits, assembles, or reviews manuscript prose reads `.Resources/voice.md` (the voice charter) before touching prose, and follows it exactly. Phase 4b and phase 5 additionally read `.Resources/quality-bar.md` (the quality bar) and run it as their review passes, and phase 7 enforces its gates through the build. Both files are the single source of truth for voice and quality; phase prompts reference them by path and never restate their rules.

## The seven-phase workflow

Run these phases in order. Each numbered file under `.claude/skills/create-book/` is a self-contained prompt; invoke them by reading the file and following its instructions.

### Phase 1: Setup (`01-setup.md`)
Create the book folder with standard structure. Copy metadata.yaml from an existing book. Create empty about.md with Leanpub field headers. Create a cover-prompt.md with a detailed image generation prompt. Use a placeholder cover. Takes a company name (for example, "SpaceX") and determines the slug and folder number.

### Phase 2: Deep research (`02-deep-research.md`)
**Team of agents, in waves.** Spawn the 5 to 8 research agents in waves of 3 to 5 (see `02-deep-research.md` for the wave pattern and the rate-limit rationale), each covering a different domain (financials, technology, market, history, customers, ethics, outlook, and company-specific domains). Each agent writes findings to its own file in `.research/`; retries overwrite the same domain file, never `-v2` siblings. Retry on a failure signal or on completion without a usable artifact, not on a timer. After all domains finish, aggregate the load-bearing numbers into the claims register.

### Phase 3: Chapter planning (`03-chapter-planning.md`)
A single planning agent reads ALL research output and designs a chapter structure that fits this specific company. Proposes 8 to 12 chapters with titles and descriptions. Presents the plan to the user for approval before proceeding. If the user has explicitly authorized autonomous work (for example, "keep working non-stop" or "don't wait for me"), skip the approval and proceed directly.

### Phase 4: Chapter writing (`04-chapter-writing.md`)
**Team of agents.** After the user approves the chapter plan, spawn writing agents using the depth assessment approach. Depth assessment agents determine what each chapter can cover based on available research material, then section-writing agents write narrow, deep sections. Chapter length emerges from the material, not from word count targets.

### Phase 4b: Depth-quality audit (`04b-depth-quality-audit.md`)
**Runs after assembly.** Audit every assembled chapter against the research that fed it and the per-chapter checklist in `.Resources/quality-bar.md`, writing `.research/quality-ch<NN>.md` per chapter. PADDED and UNSUPPORTED sections are rewritten, trimmed, or grounded before phase 5 begins.

### Phase 5: Consistency review (`05-consistency-review.md`)
Read all chapters straight through yourself, inline (no sub-agent), checking for contradictory numbers, inconsistent terminology, thesis alignment, and voice consistency, then run the quality bar in `.Resources/quality-bar.md` as the review pass. Fix issues directly.

### Phase 6: About page and metadata (`06-about-and-metadata.md`)
Generate all Leanpub fields in about.md. Finalize metadata.yaml. Write the frontmatter with executive summary and key findings.

### Phase 7: Build (`07-build.md`)
Run `python scripts/build.py <slug>` from the repo root. Verify PDF and EPUB output and that the manuscript-check gates passed. Commit and push the new book directory as the final step (repo-style message with attribution footer; stage nothing outside the book directory).

## Generalization

This skill takes a company name as input. Everywhere a path appears, substitute the folder number and slug:

- Manuscript chapters: `books/<NNN>-<slug>/manuscript/<NN>-<name>.md`
- Metadata: `books/<NNN>-<slug>/metadata.yaml`
- About page: `books/<NNN>-<slug>/about.md`
- Frontmatter: `books/<NNN>-<slug>/manuscript/00-frontmatter.md`
- Research artifacts: `books/<NNN>-<slug>/.research/`
- Build output: `books/<NNN>-<slug>/output/`

Nothing in this skill is hardcoded to any specific company. The slug, folder number, and company identity come from user input and metadata.yaml. Follow `.Resources/voice.md` for the voice; do not copy any existing book's structure or prose.

## Artifacts produced

The exact output filename per phase. Downstream phases locate artifacts by these exact paths:

- Phase 1: `books/<NNN>-<slug>/` with `metadata.yaml`, `about.md` (placeholder scaffold), `cover-prompt.md`, `images/cover.jpg` (placeholder), `manuscript/00-frontmatter.md` (empty), and `.research/` and `output/` directories.
- Phase 2: `books/<NNN>-<slug>/.research/01-financials.md` through `07-outlook.md`, extra domains as `08-<domain>.md`, `09-<domain>.md`, and so on, plus `.research/claims-register.md`.
- Phase 3: exactly one approved plan, `books/<NNN>-<slug>/.research/chapter-plan.md`. Never leave a numbered draft plan (for example `09-chapter-plan.md`) in the same directory.
- Phase 4: per-chapter `.research/assessment-<chapter-number>.md`, the consolidated `.research/chapter-sections.md`, per-section `.research/sections/<chapter>-<section>-<slug>.md`, and the assembled `manuscript/<NN>-<slug>.md` per chapter.
- Phase 4b: `.research/quality-ch<NN>.md` per chapter.
- Phase 5: `.research/consistency-review.md`.
- Phase 6: `manuscript/00-frontmatter.md` populated, `about.md` populated, `metadata.yaml` finalized.
- Phase 7: `output/<NNN>-<slug>.pdf` and `output/<NNN>-<slug>.epub`.

This map applies to new books built with this skill. Pre-existing books use different vocabularies (001 and 002 predate the skill, 003 used an earlier whole-chapter version, 004 added its quality audits ad hoc); do not rename existing artifacts.

## Agent coordination rules

1. **Always use teams of agents for phases 2 and 4.** These are the heavy-lift phases where parallelism is essential. A single agent cannot produce the volume and depth required.
2. **Spawned agents inherit the session's permission mode.** The Agent tool's `mode` parameter is deprecated and ignored; do not pass it. What matters for an uninterrupted run is file discipline: each agent writes only its own assigned file.
3. **Each agent writes only its own assigned file.** Never have two agents write to the same file simultaneously. One exception: a retry agent for a failed domain reuses and overwrites the same domain file path, so exactly one file per domain survives and no `-v2` siblings appear.
4. **Coordinate through the task list.** Create tasks for each phase and assign them to agents. Track completion via TaskUpdate.
5. **Join after each phase.** Wait for all agents in a phase to complete before starting the next phase, with one exception: chapter planning (phase 3) may start once at least 5 of the 7 core domain research files (`01-financials.md` through `07-outlook.md`) exist in `books/<NNN>-<slug>/.research/`, while the remaining agents finish; the planner re-checks the directory before presenting the plan. Before spawning any phase 4 writing agent, verify that every expected research file exists; if any are still missing, wait for those agents or spawn retries. The chapter plan must be approved by the user before writing begins, unless the user has authorized autonomous work.

## Writing conventions

Respect writing conventions in project `CLAUDE.md`:

- No em dashes. Use colons, commas, parentheses, or separate sentences.
- Sentence-case headings. Only the first word and proper nouns are capitalized.
- Acronyms uppercase: AI, NASA, CEO, API, IPO.
- Expanded acronyms: capitalize proper noun portions only. "National Aeronautics and Space Administration (NASA)".
- Chapter files start with `# Title` (H1).
- Frontmatter (`00-frontmatter.md`) has no H1 heading.
- Learn the voice from `.Resources/voice.md`; do not imitate any existing book manuscript, because older books carry documented voice regressions.
