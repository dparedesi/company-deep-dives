# Phase 4: chapter writing

**Company name:** the user-provided name.
**Book folder:** `books/<NNN>-<slug>/`. Determined in phase 1.
**Chapter plan:** `books/<NNN>-<slug>/.research/chapter-plan.md`. Approved in phase 3.

## Goal

Write every chapter of the book. Each chapter should be a comprehensive, deeply researched, evidence-based analysis that reads like a continuous narrative, not a stitched-together research dump.

## Critical requirement: team of agents

This phase MUST use a team of agents. Spawn writing agents in parallel, each handling 2 to 3 chapters. A single agent cannot produce 80,000 to 150,000 words of sustained quality.

Use `mode: bypassPermissions` for all agents to prevent plan-approval blocking.

## Agent assignment strategy

1. Read the chapter plan from `books/<NNN>-<slug>/.research/chapter-plan.md`.
2. Assign chapters to agents to avoid dependencies. Principles:
   - Chapters that reference each other should be written by the same agent (if possible) or the referencing chapter should be written after the referenced one.
   - The introduction (chapter 1) and conclusion (final chapter) are usually written last because they synthesize the rest. Assign them to the agent that finishes first, or write them yourself after all other agents complete.
   - High-data chapters (financials, market, customers) can be written in parallel since they draw from different research files.
3. Target 2 to 3 chapters per agent.

## Agent prompt template

When spawning each writing agent, use this template:

```
You are a writing agent for a company deep-dive book. You are writing <NUMBER> chapters of a deep analytical book about <COMPANY NAME>.

## Your assigned chapters

<For each chapter, include from the chapter plan:>
- Chapter number and title
- Focus description
- Word target (8,000 to 15,000 words per chapter. This is aspirational: do not constrain or cut content to hit a lower number. Depth always wins over brevity.)
- Which research files to read for this chapter

## Research files

Read the research files in books/<NNN>-<slug>/.research/ that are relevant to your chapters. These contain the factual foundation. Draw specific numbers, dates, and claims from these files. Do not invent facts.

## Voice and style

Before writing, read these files to learn the book series voice:
- books/001-palantir/manuscript/00-frontmatter.md
- books/001-palantir/manuscript/01-chapter-1.md (first 200 lines)
- books/001-palantir/manuscript/04-chapter-4.md (first 200 lines)
- books/002-rocketlab/manuscript/00-frontmatter.md
- books/002-rocketlab/manuscript/01-chapter-1.md (first 200 lines)

Key style rules:
- No em dashes. Use colons, commas, parentheses, or separate sentences.
- Sentence-case headings (only first word and proper nouns capitalized).
- Acronyms uppercase: AI, NASA, CEO, IPO.
- Expanded acronyms: capitalize proper noun portions only.
- The tone is authoritative but accessible: evidence-based, multi-perspective, no hype, no doom.
- Seek truth, not bias. If the evidence is bullish, say so. If bearish, say so. Present the signals honestly.
- Write in continuous narrative prose. Use specific numbers, dates, and names. Avoid vagueness.
- Each chapter starts with # Title (H1 heading). No higher-level heading before it.
- The frontmatter file (00-frontmatter.md) has no H1 heading.

## Writing depth

This is not a blog post or a Wikipedia article. It is the deepest analysis the reader will find anywhere. Every claim should be supported by evidence. Every section should add new information or insight. If you find yourself writing generic observations ("the company faces many challenges"), stop and replace with specifics ("the company's customer concentration risk is acute: its top three clients account for 47% of revenue, up from 39% the prior year").

## Output

Write each chapter to its file:
- books/<NNN>-<slug>/manuscript/<NN>-<slugified-title>.md

Use a 2-digit prefix matching the chapter number (01, 02, 03...). Slugify the title for the filename (lowercase, hyphens, no special characters).

Each chapter file must:
- Start with # <Title> (H1 heading)
- Use ## <Subtitle> for major sections within the chapter
- Use ### <Subtitle> for subsections
- Run 8,000 to 15,000 words
- Read as a complete, self-contained analysis of its topic
- Draw specific facts from the research files
```

## Chapter file naming

Chapters are numbered starting at 01. The frontmatter is 00. Filenames use 2-digit prefix and slugified title:

```
00-frontmatter.md
01-introduction.md
02-genesis-and-evolution.md
03-the-technological-arsenal.md
04-business-model-and-financials.md
05-market-landscape.md
06-impact-and-use-cases.md
07-ethics-and-controversy.md
08-risk-analysis.md
09-future-outlook.md
10-conclusion.md
```

Adapt the names to the actual chapter plan. Keep the 2-digit prefix convention.

## After agents complete

Once all writing agents finish:

1. List all chapter files and check they exist with non-zero size.
2. Do a quick word count on each chapter. The 8,000 to 15,000 word target is aspirational; actual output often lands between 4,000 and 8,000 words. What matters is depth and specificity, not hitting a word count. Do not constrain the model to be brief.
3. If any chapter is significantly thin (below 3,000 words) or reads as superficial, note it for expansion.
4. Proceed to phase 5 (consistency review).

## Success criteria

- All chapter files exist in `books/<NNN>-<slug>/manuscript/`.
- Each chapter starts with an H1 heading.
- Each chapter targets 8,000 to 15,000 words (aspirational; depth over brevity, never constrain to be concise).
- Chapters draw specific facts from research files (no invented data).
- Writing conventions are followed (no em dashes, sentence-case headings, uppercase acronyms).
- The voice is consistent with the existing books in the repo.

Report back with a list of chapter files, their word counts, and any chapters that are under target.
