# Step 2: fan out findings per chapter

**Book slug:** `<slug>`. The caller must supply this.

## Goal

Transform the research delta file into a per-chapter change list that step 3 can apply mechanically. One section per chapter, each listing concrete edits with source citations.

## Inputs

1. Read the research delta file from step 1: `books/<NNN>-<slug>/.research/<YYYY-MM>-delta.md`. If it does not exist, stop and run step 1 first.
2. List `books/<NNN>-<slug>/manuscript/` to get the full chapter inventory. Read the H1 title of each chapter file (`01-chapter-1.md` through the last) so you know each chapter's focus.
3. Skim each chapter file to learn its current structure and the facts already stated. Do not rewrite; you only need enough context to decide what each finding replaces, adds to, or leaves alone.

## Process

For each finding `Fn` in the delta file, look at its `Affected chapters` list. For each chapter listed:

- Decide the operation: **add**, **update**, or **remove**.
  - **Add**: the chapter does not currently mention the topic and should.
  - **Update**: the chapter has an older version of this fact (older number, older date, older framing) that needs replacing.
  - **Remove**: a prior statement is now false or misleading and must be cut. Rare but possible.
- Identify the target location inside the chapter as precisely as you can: section name, nearby sentence, or paragraph topic. If the chapter does not have a natural home for the finding, propose a new subsection title (sentence case).
- Write the new or updated text in one or two sentences. Do not draft full paragraphs here; step 3 handles voice and expansion.
- Cite the finding by ID (`F3`, `F7`) so step 3 can trace back to the source.

A single finding can produce edits in multiple chapters. A single chapter can absorb edits from many findings.

## Output format

Write the change list to `books/<NNN>-<slug>/.research/<YYYY-MM>-changes.md`. Structure:

```markdown
# <Book subject> per-chapter changes: <Month Year>

Source research: `<YYYY-MM>-delta.md`

## Chapter 1: <title>

- **Add** (F3): in the section on "<section>", note that <one-line fact>. Source: F3.
- **Update** (F7): replace the revenue figure near "<nearby sentence>" with <new figure>. Source: F7.

## Chapter 2: <title>

- **Remove** (F12): the claim about <X> near "<nearby sentence>" is now outdated; cut or rewrite to reflect that <Y>. Source: F12.

...

## Chapter N: <title>

- (no changes this edition)
```

Every chapter gets a section, even if there are no changes (write "no changes this edition"). This lets step 3 run the loop without having to re-check the research file.

## Success criteria

- The file exists at `books/<NNN>-<slug>/.research/<YYYY-MM>-changes.md`.
- Every chapter in the manuscript has a section in the changes file.
- Every change line names the operation (add, update, remove), references a finding ID from the delta file, and points to a target location inside the chapter.
- No finding from the delta file is silently dropped. If a finding is decided to be non-material for the book, note it at the bottom under a "## Dropped findings" section with one line of reasoning.

Report back with the path to the changes file and a brief per-chapter count of edits planned.
