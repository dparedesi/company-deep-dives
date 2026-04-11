# Step 4: cross-chapter consistency review

**Book slug:** `<slug>`. The caller must supply this.

## Goal

After all chapters are updated, run a cross-chapter pass to catch contradictions, mismatched numbers, inconsistent terminology, and thesis drift. This is the safety net that the whole manuscript still hangs together as a single document.

## Inputs

1. Read all chapter files in `books/<NNN>-<slug>/manuscript/`. Read them in order: `00-frontmatter.md`, then `01-*.md` through the last chapter.
2. Read the research delta file: `books/<NNN>-<slug>/.research/<YYYY-MM>-delta.md`.
3. Read the changes file: `books/<NNN>-<slug>/.research/<YYYY-MM>-changes.md`.

## What to check

### Financial figures

Any number that appears in multiple chapters must match. Common culprits:

- Revenue, margins, growth rates (often in Ch 1 summary, Ch 4 financials, Ch 9 outlook)
- Employee count, headcount growth (Ch 1, Ch 5, Ch 6)
- Stock price, valuation, market cap (Ch 1, Ch 4, Ch 9)
- Contract values, deal sizes (Ch 5, Ch 6, Ch 8)

If a figure changed in this edition, verify all references updated. If you find a mismatch, correct it and note the fix.

### Contract and customer names

The same customer, contract, or partnership may be referenced across chapters (Ch 5 customers, Ch 6 use cases, Ch 8 controversies). Check:

- Company name formatting is consistent (for example, "Department of Defense" not "DOD" in one place and "DoD" in another).
- Contract names, program names, and product names are spelled the same way throughout.
- Dates align: if a contract is "announced in March 2025" in Ch 5, Ch 6 should not say "announced in early 2025" without the March specificity.

### Timelines and dates

Sequences of events must not contradict. Common issues:

- Ch 2 says "founded in 2003" but Ch 5 says "2004 founding"
- Ch 6 says "launched in 2022" but Ch 8 says "2023 launch"
- Relative dates ("last quarter", "this year") that aged out

Check all date references. If a chapter uses a relative date like "last quarter" or "this year", replace it with an absolute date like "Q1 2026" so the book remains readable as the months pass.

### Thesis and outlook language

The final chapter (often Ch 10 or the last numbered chapter) contains the book's thesis and investment or strategic outlook. After updating facts in earlier chapters, the outlook may need rewording:

- If a key risk materialized, the outlook should reflect that reality, not treat it as hypothetical.
- If a growth driver accelerated or stalled, adjust the forward-looking language accordingly.
- Ensure the outlook chapter does not contradict specific facts stated in Ch 4 through 9.

### Terminology

Consistent terminology throughout:

- Product names: for example, "AIP" not "A.I.P." or "Artificial Intelligence Platform" randomly.
- Company descriptors: if the book refers to "data operations company" in Ch 1, do not switch to "data analytics company" in Ch 6 without reason.
- Section headings: sentence case throughout, no title case leaks.

## Process

Read the manuscript straight through from frontmatter to final chapter. As you read, maintain a scratchpad of:

- Numbers you see and where they appear
- Dates that seem fragile (relative dates, "recent", "current")
- Claims that echo or contradict earlier chapters

After the full read, resolve each inconsistency you flagged. For each fix:

- Edit the offending chapter directly.
- Add a comment `<!-- consistency fix: <what and why> -->` so the change is traceable.

## Success criteria

- All financial figures that appear in multiple chapters are identical.
- All contract, customer, and product names use consistent spelling and formatting.
- All timeline references use absolute dates, not relative phrasing.
- The outlook chapter reflects the updated facts and contains no contradictions.
- No new em dashes, title-case headings, or lowercase acronyms were introduced.

Report back with a summary of inconsistencies found and fixed. If none found, report "no inconsistencies detected."
