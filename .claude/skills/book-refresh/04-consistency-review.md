# Step 4: cross-chapter consistency review

**Book slug:** `<slug>`. The caller must supply this.

## Goal

After all chapters are updated, run a cross-chapter pass to catch contradictions, mismatched numbers, inconsistent terminology, and thesis drift, then run the quality bar. This is the safety net that the whole manuscript still hangs together as a single document and still earns its premium price.

## Inputs

1. Read all chapter files in `books/<NNN>-<slug>/manuscript/`. Read them in order: `00-frontmatter.md`, then `01-*.md` through the last chapter.
2. Read the research delta file: `books/<NNN>-<slug>/.research/<YYYY-MM>-delta.md`.
3. Read the changes file: `books/<NNN>-<slug>/.research/<YYYY-MM>-changes.md`.
4. Read `books/<NNN>-<slug>/.research/<YYYY-MM>-consistency-notes.md` if it exists; it lists cross-references step 3 flagged as fragile. Check those first.
5. Read `.Resources/voice.md` and `.Resources/quality-bar.md` before starting. Both files govern this phase.

### Role map

List `books/<NNN>-<slug>/manuscript/` and read each chapter file's H1 title. Before checking anything, write down the role map for this book: which file is the introduction, financials, market and competition, customers and use cases, technology, history, ethics and controversies, risk, outlook, and conclusion. Some books merge or split these roles (for example ethics and risk in one chapter); map what actually exists. Use these roles, not fixed chapter numbers, for every reference below. The number-to-topic mapping differs across the repo's books, so a hardcoded guess is wrong for most of them.

## What to check

### Financial figures

Any number that appears in multiple chapters must match. Common culprits:

- Revenue, margins, growth rates (often in the introduction's summary, the financials chapter, and the outlook chapter)
- Employee count, headcount growth (the introduction, the market chapter, the use-cases chapter)
- Stock price, valuation, market cap (the introduction, the financials chapter, the outlook chapter)
- Contract values, deal sizes (the market chapter, the use-cases chapter, the ethics or controversies chapter, the risk chapter)

If a figure changed in this edition, verify all references updated. If you find a mismatch, correct it and note the fix.

### Contract and customer names

The same customer, contract, or partnership may be referenced across chapters (the market chapter, the use-cases chapter, the ethics or controversies chapter). Check:

- Customer, agency, and partner name formatting is consistent throughout (for example, the same abbreviation and capitalization for a recurring customer or partner name, not one form in one chapter and another elsewhere).
- Contract names, program names, and product names are spelled the same way throughout.
- Dates align: if a contract is "announced in March 2025" in one chapter, another should not say "announced in early 2025" without the March specificity.

### Timelines and dates

Sequences of events must not contradict. Common issues:

- One chapter says "founded in year X" but another says "year Y founding"
- One chapter says "launched in 2022" but another says "2023 launch"
- Relative dates ("last quarter", "this year") that aged out

Check all date references. If a chapter uses a relative date like "last quarter" or "this year", replace it with an absolute date like "Q1 2026" so the book remains readable as the months pass.

### Thesis and outlook language

The outlook chapter (and the conclusion, when it is separate) carries the book's thesis and investment or strategic outlook. After updating facts in earlier chapters, the outlook may need rewording:

- If a key risk materialized, the outlook should reflect that reality, not treat it as hypothetical.
- If a growth driver accelerated or stalled, adjust the forward-looking language accordingly.
- Ensure the outlook chapter does not contradict specific facts stated in the earlier chapters.

### Terminology

Consistent terminology throughout:

- Product names: the book's established spelling and abbreviation of the subject's flagship products, used consistently (not a dotted or randomly expanded variant). Read the product names from metadata.yaml or the technology chapter at the start.
- Company descriptors: if the book describes the company one way in the introduction, do not switch to a different descriptor in a later chapter without reason.
- Section headings: sentence case throughout, no title case leaks.

## Quality bar pass

Run the per-book checklist in `.Resources/quality-bar.md` across the manuscript, then the per-chapter list on every chapter that was touched. At minimum verify: the numeric consistency gate (same fact, same value everywhere including frontmatter versus chapters; quarters sum to years; growth rates recompute from stated bases; an identical figure set under two different period labels is a contradiction), exactly one as-of-dated valuation snapshot with every prior-edition block deleted, the frontmatter house view matches the updated outlook chapter, the charter's banned phrase lists return zero hits, the cross-book scan returns zero hits, and the frontmatter passes the 300-word gate.

## Process

Read the manuscript straight through from frontmatter to final chapter. As you read, maintain a scratchpad of:

- Numbers you see and where they appear
- Dates that seem fragile (relative dates, "recent", "current")
- Claims that echo or contradict earlier chapters
- The fragile cross-references flagged by step 3

After the full read, resolve each inconsistency you flagged. For each fix:

- Edit the offending chapter directly.
- Append one line to `books/<NNN>-<slug>/.research/<YYYY-MM>-applied.md` under a `## consistency fixes` heading: `| <chapter file> | fix | what was changed and why |`.

Finally, strip every `<!-- ... -->` HTML comment from every manuscript file. They are working-layer artifacts and must never reach the build; they leak verbatim into the published EPUB.

Persist the review summary to `books/<NNN>-<slug>/.research/<YYYY-MM>-review.md`: the per-chapter quality bar verdicts, the verified-numbers table, the resolved falsifiers, the two premium-test answers, and an explicit final line `build blockers:` listing unresolved items or the word `none`. `/publish-release` gates on this file.

## Success criteria

- All financial figures that appear in multiple chapters are identical.
- All contract, customer, and product names use consistent spelling and formatting.
- All timeline references use absolute dates, not relative phrasing.
- The outlook chapter reflects the updated facts and contains no contradictions.
- No new em dashes, en dashes, title-case headings, or lowercase acronyms were introduced.
- The quality bar per-book checklist passed, or its unresolved items are recorded as build blockers in the report.
- Every fragile cross-reference from step 3's consistency notes is resolved or explicitly cleared.
- `grep -rc '<!--' books/<NNN>-<slug>/manuscript/` returns zero for every file.

Report back with a summary of inconsistencies found and fixed, the quality bar pass result, any unresolved build blockers, and the path of the persisted review file. If none found, report "no inconsistencies detected."
