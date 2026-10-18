# Phase 4: chapter writing

**Company name:** the user-provided name.
**Book folder:** `books/<NNN>-<slug>/`. Determined in phase 1.
**Chapter plan:** `books/<NNN>-<slug>/.research/chapter-plan.md`. Approved in phase 3, or completed via the autonomous-work exception.

## Goal

Write every chapter of the book. Each chapter should be a comprehensive, deeply researched, evidence-based analysis that reads like a continuous narrative, not a stitched-together research dump.

## Core principle: depth emerges from material, not from instructions

You cannot instruct an agent to "write 12,000 words" and get depth. You cannot instruct it to "cover 10 subtopics" and get substance. If the material supports 3 real topics, forcing 10 produces hallucination and padding. If the material supports 20, forcing 10 leaves the deepest analysis unwritten.

The correct approach is to discover what depth the research material actually supports, then spawn agents whose scope matches that depth. Narrow scope produces deep writing naturally. Broad scope produces summaries.

## The four-step workflow

### Step 1: Depth assessment (spawn assessment agents)

Spawn one depth-assessment agent per chapter. Each agent reads the chapter plan and all relevant research files, then answers one question: **based on what we actually have, what are the distinct, substantive topics this chapter can cover, and is there enough real material for each to warrant its own section?**

The assessment agent does NOT write any chapter content. It only produces a decomposition plan.

#### Assessment agent prompt template

```
You are a depth assessment agent for a company deep-dive book. You do NOT write chapters. You ONLY assess what depth the available research material supports.

## Your assignment
Chapter: <number and title from chapter plan>
Chapter focus: <description from chapter plan>
Research files to read:
- <list all relevant research files>

## Your job
1. Read EVERY research file listed above.
2. For this chapter's topic, identify every distinct, substantive subtopic where the research contains enough real material (specific facts, numbers, dates, quotes, events) to support a deep section of 1,500 to 5,000 words.
3. For each subtopic, honestly assess: is there enough real material here, or would a writer have to pad or speculate? If the material is thin, do NOT list it as a standalone section. It should be merged into a related section or mentioned briefly within one.
4. Group related subtopics that are individually thin but collectively substantive into combined sections.

## Output format

Write your assessment to books/<NNN>-<slug>/.research/assessment-<chapter-number>.md:

# Depth assessment: Chapter <number> - <title>

## Material review
<1-2 paragraphs summarizing what the research files actually contain for this chapter's topic>

## Recommended sections

### Section <N>.1: <topic>
- Research basis: <what specific material exists, with file references>
- Key facts available: <list the specific data points, events, names that the research provides>
- Depth potential: <shallow/moderate/deep - based on how much real material exists>
- Can this stand alone: <yes/no - if no, which section should it merge into?>

### Section <N>.2: <topic>
...

## Topics to mention briefly (not standalone sections)
<subtopics that have some material but not enough for a dedicated section>

## Topics to avoid (insufficient material)
<subtopics that would require speculation or padding>

## Estimated chapter depth
Based on available material, this chapter can support <number> substantive sections totaling approximately <estimated range> words of factual, evidence-based content.
```

#### Why this works
- The agent reads actual research, not a wish list.
- It distinguishes "we have real material here" from "this would be padding."
- Thin topics get merged or flagged, not forced into standalone sections.
- The number of sections emerges from the material, not from a hardcoded target.
- A chapter about CUDA with rich research might get 6 sections. A chapter about corporate governance with thin research might get 2.

### Step 2: Dynamic decomposition

After all assessment agents complete, read their outputs. For each chapter, create the final section decomposition based on their recommendations:

- Use the sections the assessment agent recommended.
- Merge any sections the agent flagged as too thin.
- Skip any topics the agent flagged as "insufficient material."
- Record the specific facts and research references for each section.

Write the final decomposition to `books/<NNN>-<slug>/.research/chapter-sections.md`.

### Step 3: Section writing (spawn one agent per section)

Spawn one section-writing agent per section from the decomposition. Each agent writes ONE narrow section. Because the scope is narrow and the material is known to exist (the assessment confirmed it), the agent naturally goes deep.

#### Section-writing agent prompt template

```
You are writing ONE section of a deep analytical book about <COMPANY NAME>. Your section covers a specific, narrow topic. Your job is to exhaust this topic using the available research material.

## Your section
Chapter: <chapter number and title>
Section: <section number and topic>
Output file: books/<NNN>-<slug>/.research/sections/<chapter>-<section>-<slug>.md
Research files: <specific files, from assessment>

## What the research contains
<Copy the "Key facts available" and "Research basis" from the depth assessment. This tells the agent exactly what material exists to work with.>

## How to write it
- Read the research files FIRST. Draw specific numbers, dates, and claims from research. Do not invent facts.
- Read `.Resources/voice.md` first and follow it exactly; it defines the voice, number formats, chapter engine, and banned patterns.
- Write in continuous narrative prose, not bullet points.
- Every paragraph should contain at least one specific fact (a number, a date, a name, a quote).
- If you catch yourself writing something generic ("the company grew rapidly"), replace it with specifics ("revenue grew 126% year-over-year, from approximately $26.9 billion to $60.9 billion between fiscal 2023 and fiscal 2024").
- Draw every number, date, and named event from the research files or the claims register (`books/<NNN>-<slug>/.research/claims-register.md`). If a number you want is not there, leave it out or flag the gap; never supply a value from memory or general knowledge.
- Every H2 section introduces a human decision before the number it produced, per the charter's chapter engine section.
- No em dashes. Use colons, commas, parentheses, or separate sentences.
- Sentence-case headings (only first word and proper nouns capitalized).
- Start with ## <section title> (H2, not H1).

## Depth guidance
You are writing ONE section, not an entire chapter. Go as deep as the material allows. If the research has 10 specific data points for your topic, use all 10. If it has 3, use those 3 deeply. Do not pad. Do not speculate beyond what the research supports. Write until you have exhausted the available material, then stop.

Write the section using the Write tool.
```

#### Why "write until you have exhausted the material, then stop" is the right instruction
- It ties output length to research depth, not an arbitrary number.
- For a section with rich research, "exhausting the material" produces 5,000+ words naturally.
- For a section with thin research, "exhausting the material" produces 1,500 words honestly.
- No padding, no hallucination, no arbitrary targets.

### Step 4: Assembly (spawn one agent per chapter)

Once all section-writing agents for a chapter complete, spawn one assembler agent per chapter.

#### Assembler agent prompt template

```
You are assembling one chapter of a deep analytical book from pre-written sections.

## Chapter details
Chapter number: <N>
Chapter title: <title>
Output file: books/<NNN>-<slug>/manuscript/<NN>-<slugified-title>.md
Section files (read ALL of these):
- books/<NNN>-<slug>/.research/sections/<N>-01-<slug>.md
- books/<NNN>-<slug>/.research/sections/<N>-02-<slug>.md
...

## Your job
1. Read every section file.
2. Assemble them into a coherent chapter with smooth transitions between sections.
3. Write the chapter opening in one of the three charter hook shapes defined in `.Resources/voice.md`; never a roadmap or setup paragraph.
4. Write the chapter ending so it turns a corner per the charter (a new fact that changes the stakes, a sharpened question, or a tension carried by a named actor or date); delete any section ending in a summary or disclaimer.
5. Remove any contradictions or repetitive passages between sections.
6. Fix writing convention violations (no em dashes, sentence-case headings).
7. The chapter starts with # <Title> (H1 heading).
8. Sections use ## <subtitle> (H2 headings).
9. Write the final assembled chapter to the output file using the Write tool.
10. Preserve every section's analytical depth, and compress padding: merge duplicated facts across sections, cut version-by-version chronologies down to the load-bearing milestones, and remove repeated stat blocks (`.Resources/quality-bar.md`, per-chapter numbers section, defines padding).

## Voice
Read `.Resources/voice.md` and conform the chapter to it.
```

## Spawning strategy

Spawn agents in waves, limiting each wave to 3 to 5 agents simultaneously to reduce API rate-limit risk. Spawning 8+ agents at once frequently triggers 429 errors that cause agents to fail before completing their work.

- **Wave 1:** Depth-assessment agents in waves of 3-5 (one per chapter, 8-12 total across 2-3 waves).
- **Wave 2:** Section-writing agents in waves of 3-5 (one per section, typically 25-50 total across 5-10 waves).
- **Wave 3:** As each chapter's sections all complete, spawn its assembler agent (these are lightweight and can go 2-3 at a time).

Spawned agents inherit the session's permission mode; the Agent tool's `mode` parameter is deprecated and ignored, so do not pass it. Each agent writes only its own assigned output file.

### Rate-limit fallback

If an agent hits a rate limit (429 error) and fails to complete:
1. Retry once with a fresh agent.
2. If the retry also fails, do the work directly (inline) rather than spawning another agent. The depth assessment, section writing, and assembly can all be done by the orchestrating agent if needed. This is slower but guaranteed to complete.

## After assembly completes

1. Before spawning an assembler agent for a chapter, verify every section file listed in `chapter-sections.md` for that chapter exists and is non-empty. Respawn any missing or empty section agents and wait for them to finish before assembling.
2. List all chapter files and verify they exist with non-zero size.
3. Do a word count on each chapter.
4. If any chapter lands below 70% of the low end of the assessment's estimated word range, compare it against the sum of its section files in `.research/sections/`. If sections were truncated during assembly, respawn the assembler for that chapter; if the sections themselves are thin, respawn those section agents.
5. Run the depth-quality audit (`04b-depth-quality-audit.md`) on every assembled chapter; it runs the per-chapter checklist in `.Resources/quality-bar.md` as its standard and writes `.research/quality-ch<NN>.md` per chapter.
6. Proceed to phase 5 (consistency review).

## Chapter file naming

Chapters are numbered starting at 01. The frontmatter is 00. Filenames use 2-digit prefix and slugified title. Adapt to the actual chapter plan.

## Writing conventions

- No em dashes. Use colons, commas, parentheses, or separate sentences.
- Sentence-case headings.
- Acronyms uppercase: AI, GPU, CEO, IPO.
- Expanded acronyms: capitalize proper noun portions only.
- The tone is authoritative but accessible: evidence-based, no hype, no doom.
- Seek truth, not bias.
- Every paragraph contains at least one specific fact.

## Success criteria

- All chapter files exist in `books/<NNN>-<slug>/manuscript/`.
- Each chapter starts with an H1 heading.
- Each chapter is assembled from sections that were validated by depth assessment.
- Section count varies per chapter based on available material (not a hardcoded number).
- Chapters draw specific facts from research files and the claims register (no invented data, no padding, no numbers from memory).
- Writing conventions are followed.
- The voice is consistent across chapters.
- Every chapter has a `.research/quality-ch<NN>.md` audit with all sections judged HONEST or minor padding; PADDED and UNSUPPORTED sections were rewritten, trimmed, or grounded before phase 5.

Report back with a list of chapter files, their word counts, and the assessment-to-actual variance for each chapter.
