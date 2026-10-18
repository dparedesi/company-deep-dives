# Step 2: fan out findings per chapter

**Book slug:** `<slug>`. The caller must supply this.

## Goal

Transform the research delta file into a per-chapter change list that step 3 can apply mechanically. One section per chapter, each listing concrete edits with source citations, plus the explicit deletions and structural flags that keep the book from accumulating stale blocks or silently drifting structure.

## Inputs

1. Read the research delta file from step 1: `books/<NNN>-<slug>/.research/<YYYY-MM>-delta.md`. If it does not exist, stop and run step 1 first.
2. List `books/<NNN>-<slug>/manuscript/` to get the full inventory. Treat `00-frontmatter.md` as the frontmatter (executive summary; it has no H1; its structure is bold labels and bullets such as "**Overview**" and "**Key findings**"). Read the H1 title of each numbered chapter file so you know each chapter's focus.
3. Skim each chapter file and the frontmatter to learn its current structure and the facts already stated. Do not rewrite; you only need enough context to decide what each finding replaces, adds to, or leaves alone.

### Validate the delta file before processing

For every finding block `## Fn`, confirm:

- `**Type:**` is one of financial, contract, product, market, leadership, regulatory, controversy, risk, black-swan (never `add` or `update`).
- `**Chapters:**` is present and lists chapter numbers, optionally with the `frontmatter` tag.
- `**Confidence:**` is exactly one of `high`, `medium`, `low` (no compounds, no annotations).
- `**Date:**` is present.
- `**Source:**` is present and contains a URL or an outlet name plus article title.

If any block fails any check, do not proceed to fan-out. Repair the delta file first: look up the missing source and add the `**Source:**` line. If the source cannot be recovered, set the finding's `**Source:**` line to `Source: not recoverable; see Data gaps`, downgrade its `**Confidence:**` to `low`, and add a matching entry under the delta file's `## Data gaps and verification needs` section. Continue only after every block passes all five checks.

## Process

For each finding `Fn` in the delta file, look at its `**Chapters:**` list. For each chapter (or `frontmatter`) listed:

- Decide the operation: **add**, **update**, **remove**, or **replace (snapshot)**.
  - **Add**: the chapter does not currently mention the topic and should.
  - **Update**: the chapter has an older version of this fact (older number, older date, older framing) that needs replacing.
  - **Remove**: a prior statement is now false or misleading and must be cut. Rare but possible.
  - **Replace (snapshot)**: delete the existing valuation or dashboard block and write the new as-of-dated block in its place. Any addition that leaves the prior edition block in place is an error; order deletions explicitly and never rely on additions alone.
- Identify the target location inside the chapter as precisely as you can: section name, nearby sentence, or paragraph topic. If the chapter does not have a natural home for the finding, propose a new subsection title (sentence case). For frontmatter targets, the location vocabulary is its bold labels and bullets, not subsections, since the frontmatter carries no headings.
- Write the new or updated text in one or two sentences. Do not draft full paragraphs here; step 3 handles voice and expansion.
- Cite the finding by ID (`F3`, `F7`) so step 3 can trace back to the source.

A single finding can produce edits in multiple chapters. A single chapter can absorb edits from many findings.

### Artifact conflict reconciliation

When two research artifacts disagree on a value, count, or date, name the winner with the reason (fresher, better sourced, more specific), correct the losing value in the base research file itself, and record the resolution in the changes file. Only the winner reaches the manuscript or the claims register.

### Claims register maintenance

Extend `books/<NNN>-<slug>/.research/claims-register.md` with this cycle's findings and mark each row re-verified or carried forward. If no register exists, create one from this cycle's findings plus the book's current headline numbers. Every load-bearing number that will appear in the manuscript should have a row with its value, period, source, and as-of date.

### Structural changes

If a finding opens a domain no existing chapter covers (decide by reading every H1 title), do not create or renumber chapters silently. Record it in the changes file under "## Structural change proposals" with a suggested new chapter title and which existing chapters absorb overflow, and flag it in your report back. The user decides. If the user approves a renumber, update cross-references and the about.md Table of contents HTML in the same change.

## Output format

Write the change list to `books/<NNN>-<slug>/.research/<YYYY-MM>-changes.md`. Structure:

```markdown
# <Book subject> per-chapter changes: <Month Year>

Source research: `<YYYY-MM>-delta.md`

## Frontmatter (00-frontmatter.md)

[include this section only when at least one finding is tagged frontmatter; edits use the same add/update/remove/replace line format with finding IDs, targeting the bold labels and bullets]

## Chapter 1: <title>

- **Add** (F3): in the section on "<section>", note that <one-line fact>. Source: F3.
- **Update** (F7): replace the revenue figure near "<nearby sentence>" with <new figure>. Source: F7.
- **Remove** (F12): the claim about <X> near "<nearby sentence>" is now outdated; cut or rewrite to reflect that <Y>. Source: F12.
- **Replace (snapshot)** (F11): delete the valuation block dated <old as-of> near "<nearby sentence>" and write the new one, as-of dated <date>. Source: F11.

## Chapter N: <title>

- (no changes this edition)

## Stale blocks to delete

[required section; list every prior-edition block superseded by this cycle's facts (old valuation snapshots, old dashboard counters, resolved-milestone framing), with its location, so step 3 deletes rather than accumulates]

## Dropped findings

[findings decided non-material for the book, one line of reasoning each]
```

Every chapter gets a section, even if there are no changes (write "no changes this edition"). Include a Frontmatter section whenever the delta file tags any finding `frontmatter`. This lets step 3 run the loop without having to re-check the research file.

## Success criteria

- The file exists at `books/<NNN>-<slug>/.research/<YYYY-MM>-changes.md`.
- The delta file passed the format validation before processing.
- Every chapter in the manuscript has a section in the changes file, plus a Frontmatter section when the delta tags any finding `frontmatter`.
- Every change line names the operation (add, update, remove, replace snapshot), references a finding ID from the delta file, and points to a target location inside the chapter.
- Every superseded valuation or dashboard block appears under Stale blocks to delete.
- Every load-bearing number carried into the manuscript has a claims-register row.
- No finding from the delta file is silently dropped. If a finding is decided to be non-material for the book, note it at the bottom under a "## Dropped findings" section with one line of reasoning.

Report back with the path to the changes file, a brief per-chapter count of edits planned, and any structural change proposals.
