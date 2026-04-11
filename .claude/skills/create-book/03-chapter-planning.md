# Phase 3: chapter planning

**Company name:** the user-provided name.
**Book folder:** `books/<NNN>-<slug>/`. Determined in phase 1.

## Goal

Read all research output from phase 2 and design a chapter structure that fits this specific company. The structure should be organic to the subject, not a rigid template applied to every book.

## Process

### 1. Read all research files

Read every file in `books/<NNN>-<slug>/.research/`. You need the full picture before designing the structure. Do not skim; read thoroughly.

### 2. Identify the company's story arc

Based on the research, determine what makes this company unique:

- What is the central tension or question that defines this company?
- What are the 3 to 5 themes that keep appearing across multiple research domains?
- What would a reader most want to understand about this company?
- What is surprising or counterintuitive about this company?

These themes become the backbone of the chapter structure.

### 3. Design the chapter structure

Every deep-dive book in this repo should cover these areas (but the order, emphasis, and number of chapters dedicated to each should vary by company):

- **Introduction**: Hook the reader. What is the central enigma or tension?
- **History and genesis**: Origin story, founding, early years, key pivots.
- **Technology and products**: What they build, how it works, technical depth.
- **Business model and financials**: How they make money, financial performance, unit economics.
- **Market and competition**: Competitive landscape, positioning, moats.
- **Customers and use cases**: Who uses it, how, and with what results.
- **Ethics, controversy, and societal impact**: The hard questions.
- **Risk analysis**: What could go wrong, what keeps investors up at night.
- **Future outlook**: Where is this going? Bull, base, bear scenarios.
- **Conclusion**: Synthesis, unanswered questions, final assessment.

This is a guideline, not a template. Some companies warrant two chapters on technology. Some need a dedicated chapter on regulation. Some deserve a chapter on their founder's philosophy. Let the research drive the structure.

Target 8 to 12 chapters. Aim for coverage that is comprehensive but not padded. Each chapter should have a clear reason to exist.

### 4. Write the chapter plan

Create a file at `books/<NNN>-<slug>/.research/chapter-plan.md` with this structure:

```markdown
# Chapter plan: <Book title>

## Central thesis
<One paragraph: what is this book arguing or revealing?>

## Story arc
<One paragraph: how does the book flow from start to finish? What is the narrative journey?>

---

## Chapter 1: <title in sentence case>
**Focus:** <one sentence on what this chapter covers>
**Word target:** <8,000 to 15,000 words>
**Research domains feeding this chapter:** <list which research files>

<One paragraph describing what this chapter will cover, the key questions it answers, and how it fits into the overall arc.>

## Chapter 2: <title>
...

---

## Notes on structure
<Explain why you chose this particular order and emphasis. What makes it right for this company?>
```

### 5. Present to the user

Print the chapter plan to the conversation. Show each chapter's title and one-sentence description. Then ask the user for approval before proceeding to phase 4.

Use AskUserQuestion with the chapter plan summarized. The user may:
- Approve as-is
- Request chapter additions, removals, or reordering
- Request different emphasis on certain topics
- Suggest a different title for the book

Wait for explicit approval before proceeding.

## Adaptive structure examples

These are examples of how structure varies by company, not templates to copy:

**A defense tech company** might warrant: two chapters on government contracts and procurement, a chapter on ethics that is longer than most, a chapter on the founder's political philosophy.

**A consumer tech company** might warrant: a chapter on product design philosophy, a chapter on supply chain and manufacturing, shorter ethics section but longer competition section.

**A fintech company** might warrant: a chapter on regulation across jurisdictions, a chapter on the financial system it is disrupting, heavy emphasis on unit economics and risk.

The structure must serve the subject, not the other way around.

## Success criteria

- A chapter plan file exists at `books/<NNN>-<slug>/.research/chapter-plan.md`.
- The plan covers 8 to 12 chapters.
- Every research domain is represented in at least one chapter.
- The plan includes a central thesis, story arc, and per-chapter descriptions.
- The structure is adaptive to the company, not a rigid template.
- The user has approved the plan before phase 4 begins.

Report back with the chapter plan summary and confirmation of user approval.
