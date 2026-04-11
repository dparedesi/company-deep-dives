# Phase 5: consistency review

**Company name:** the user-provided name.
**Book folder:** `books/<NNN>-<slug>/`.

## Goal

Read the entire manuscript straight through and fix any inconsistencies across chapters. This is the cross-chapter pass that catches contradictions, terminology drift, and voice breaks that are invisible when chapters are written in isolation.

## Process

### 1. Read every chapter in order

Read `books/<NNN>-<slug>/manuscript/` files in filename order (00-frontmatter.md, then 01- through the final chapter). Read them sequentially, as a reader would.

### 2. Check for these categories of issues

#### Contradictory numbers
- Revenue, income, margin, and growth figures must match across all chapters.
- If Chapter 4 says "revenue of $4.48 billion" and Chapter 9 says "revenue of $4.5 billion", one of them is wrong.
- Market size estimates, customer counts, employee counts, and contract values must be consistent.

#### Inconsistent dates and timelines
- If one chapter says the company was "founded in 2003" and another says "founded in 2004", that is a contradiction.
- Product launch dates, IPO dates, and milestone dates must agree across chapters.

#### Terminology drift
- The same concept should be called the same thing everywhere. If one chapter says "artificial intelligence platform" and another says "AI platform", that is fine (abbreviation after first use). But if one says "ontological framework" and another says "data model" for the same thing, that needs harmonizing.
- Product names must be exact and consistent.

#### Thesis alignment
- The central thesis (stated in the frontmatter and introduction) should be supported, not contradicted, by the evidence in subsequent chapters.
- If the introduction claims the company has a "wide moat" but the risk chapter identifies "no meaningful barriers to entry", one or both need revising to reflect a more nuanced position.

#### Voice consistency
- All chapters should read as if written by the same author. Since multiple agents wrote chapters, voice drift is the most common issue.
- Watch for: sudden formality shifts, different paragraph lengths, different use of analogies or metaphors, different levels of technical depth.
- The voice should be authoritative, evidence-based, and accessible throughout.

#### Cross-references
- If one chapter says "as discussed in Chapter 4", verify that Chapter 4 actually discusses it.
- Verify that "as we will see in Chapter 8" type forward-references point to the right chapter.

### 3. Fix issues directly

For each issue found:

- If the fix is small (a number, a date, a word), edit the file directly.
- If the fix requires rewriting a paragraph or more, note the location and the issue, then fix it.
- If two chapters present different versions of the same fact, check the research files to determine which is correct, then update the wrong one.

### 4. Write a review summary

After fixing, write a brief summary of what was fixed to `books/<NNN>-<slug>/.research/consistency-review.md`:

```markdown
# Consistency review: <Book title>

Date: <today>

## Issues found and fixed
- <description of each fix with file and location>

## Issues requiring user attention
- <anything you are unsure about or that requires a judgment call>

## Confirmed consistent
- <areas you checked that were already consistent>
```

## Success criteria

- All chapters have been read in sequence.
- Contradictory numbers have been resolved (check research files for ground truth).
- Dates and timelines are consistent across chapters.
- Terminology is harmonized.
- The thesis is consistently supported throughout.
- Voice is uniform across chapters.
- Cross-references are accurate.
- A review summary has been written to `.research/consistency-review.md`.

Report back with the count of issues found and fixed, and any items that need user attention.
