---
name: publish-release
description: Prepare a book for Leanpub publication after a refresh. Use when the user says "publish", "release notes", "notify readers", "send to Leanpub", or wants the email notification for a new book edition. Verifies the build is current and the quality bar passed, fixes stale facts in the about page fields, then generates concise email-ready release notes to paste into Leanpub's "Notify Readers" form. Runs after /book-refresh; never for a first edition.
argument-hint: <slug>
---

# publish-release

**Why?** After a refresh, nobody else owns the stale facts on the about page, and announcing an edition before verifying the build and the quality bar risks emailing readers something other than what the manuscript now says.

## When to use

Use this skill after `/book-refresh <slug>` has completed and the book is built. It runs from the second edition onward, never for a first edition: Leanpub's "Notify Readers" form emails existing readers, and a first upload has none. Input 1 stops a first edition before any work begins.

This skill does three things:

1. **Verifies the edition is publishable**: the refresh cycle passed the quality bar, and the built PDF and EPUB are no older than any source file (the pre-publish gate and step 0).
2. **Updates stale facts in `about.md`** (quarters, guidance figures, headline numbers, table of contents entries) so they reflect the latest manuscript. Edition-date fields belong to book-refresh step 5 (see the ownership section below).
3. **Generates email-ready release notes** to paste into Leanpub's "Notify Readers" form.

## Ownership of about.md

- create-book phase 6 creates every section.
- book-refresh step 5 owns the edition-date fields: the "current as of <Month Year>" and "Current to" phrases, edition labels, and the edition date in the What's-new heading.
- book-refresh step 6 owns the "What's new in this edition" section.
- This skill owns stale facts in the other sections: About the Book, Teaser text, Meta description, and Table of contents HTML. It also owns the reader email.

If an edition-date field is stale, flag it in the report with the corrected text instead of editing it; book-refresh step 5 owns it.

## Inputs

1. Verify `books/<NNN>-<slug>/about.md` exists (`ls books/<NNN>-<slug>/about.md`). If it is missing, stop and tell the user: this book has no Leanpub about page yet; generate one first via create-book's phase 6 step, then rerun this skill. Otherwise read all sections. If the "What's new in this edition" section reads "This is the first edition..." (create-book's phase 6 writes exactly this sentence for a new book, optionally followed by the publication month), stop as well: this skill notifies existing readers after a refresh, and a first upload has none. Tell the user to run it from the second edition onward, right after each `/book-refresh <slug>`.
2. Read `books/<NNN>-<slug>/metadata.yaml` to get the edition date and book title.
3. Read `books/<NNN>-<slug>/manuscript/00-frontmatter.md` for the latest key financial data and thesis language. If it is empty or a stub, pull the key data from the financials chapter (input 4) and flag the empty frontmatter in the final report so it can be backfilled.
4. Locate the financials chapter dynamically, then skim it to pull the most current numbers. Read each chapter's first heading, for example `grep -m1 '^# ' books/<NNN>-<slug>/manuscript/*.md`. Pick the chapter covering financial performance (revenue, margins, segment results, balance sheet, market capitalization). Judge by H1 title, by filename (for example `05-financial-ascent.md`), or, when titles are evocative, by skimming the `## ` subheadings of shortlisted chapters (look for sections like Revenue Growth, Gross Margin, Segment Revenue, Balance Sheet). Do not assume a fixed chapter number: chapter 04 is financials only for Palantir, and in the other books it holds technology or product content. Pull the numbers from that chapter plus `00-frontmatter.md` (input 3).

## Pre-publish gate

Before generating release notes, verify the refresh cycle passed the quality bar:

1. Confirm the persisted consistency review `books/<NNN>-<slug>/.research/<YYYY-MM>-review.md` (written by book-refresh step 4) records no unresolved build blockers. If the file is missing, ask the user to confirm the consistency review passed before continuing.
2. Confirm `books/<NNN>-<slug>/manuscript/00-frontmatter.md` contains the house view section required by `.Resources/quality-bar.md`.

If either is missing, stop and tell the user to rerun the book-refresh consistency review first. The gate lives in `.Resources/quality-bar.md`.

## Step 0: verify the build is current

Release notes tell readers what the new edition contains, so the built artifacts must include every source change before anything is written or announced.

1. Confirm both artifacts exist and are non-empty: `books/<NNN>-<slug>/output/<NNN>-<slug>.pdf` and `books/<NNN>-<slug>/output/<NNN>-<slug>.epub`. If either is missing or zero bytes, stop before step 1 and tell the user to run `python scripts/build.py <slug>` from the repo root, then re-run this skill.
2. From the repo root, list every build input newer than either artifact:

   ```bash
   find books/<NNN>-<slug>/manuscript books/<NNN>-<slug>/metadata.yaml books/<NNN>-<slug>/images templates/book.typ templates/epub.css scripts/build.py scripts/lint_manuscript.py -type f \( -newer books/<NNN>-<slug>/output/<NNN>-<slug>.pdf -o -newer books/<NNN>-<slug>/output/<NNN>-<slug>.epub \) -print 2>/dev/null
   ```

   Empty output means the build is current. Any listed file means at least one delivered format is stale. Ties (equal mtime) count as current.
3. If any file is listed, stop before step 1 and tell the user: "The built PDF and EPUB in `output/` do not include the latest changes to: [list the files]. Run `python scripts/build.py <slug>` from the repo root, then re-run this skill." Do not update `about.md` and do not print release notes until the user confirms the build ran.

Do not include `about.md` in the comparison. Its content is not a build input for the artifacts (the lint scans it, but step 1's edits follow the same voice rules the lint enforces), and step 1 edits it, so including it would always report staleness.

This check complements the What's-new guard in step 2: an empty or placeholder "What's new" section means the refresh never ran (run `/book-refresh <slug>`); a populated section with stale or missing artifacts means the refresh ran without a finished build (run `python scripts/build.py <slug>`).

## Step 1: update about.md fields

The about page has these sections that may contain stale data after a refresh:

- **About the Book** (`## About the Book:`): The main description paragraph. Check for outdated references like old quarter results ("Q3 2025"), old guidance figures ("guided to approximately X"), or old dates. Update to the latest actuals from the manuscript. Do NOT rewrite the whole description; only update the specific facts that are stale.
- **Teaser text** (`## Teaser text:`): The one-liner that appears on the book's Leanpub page. Update any stale facts (quarters, guidance figures, headline numbers).
- **Meta description** (`## Meta description:`): The SEO description. Update any stale facts.
- **Table of contents HTML** (`## Table of contents HTML:`): Rebuild it from the actual manuscript H1 titles rather than trusting the stored HTML. List the chapter titles in file order with `grep -m1 '^# ' books/<NNN>-<slug>/manuscript/*.md` (note: `00-frontmatter.md` yields no H1 and maps to the fixed leading entry `<p>Overview</p>`). Compare both the chapter count and each title against the current entries. If the count differs or any title differs, for whatever reason (drift from an earlier edition, a rename, or an error at creation), regenerate the full HTML list from the H1 titles: keep `<p>Overview</p>` as the first entry, then one `<p>Chapter N: <title></p>` per chapter file in sorted filename order, where N comes from the file's numeric prefix (01- means Chapter 1) and `<title>` is the H1 text with any leading `Chapter N:` or `Chapter N -` prefix removed, markdown escapes unescaped (for example `\-` becomes `-`), and ampersands encoded as `&amp;`. Examples: an H1 of `# Chapter 5: The Fastest Five Trillion in History` becomes `<p>Chapter 5: The Fastest Five Trillion in History</p>`; an H1 of `# Market Landscape & Strategic Positioning` in a file numbered `05-` becomes `<p>Chapter 5: Market Landscape &amp; Strategic Positioning</p>`. If the stored HTML already matches both count and titles exactly, leave it unchanged and say so in the report. Separator-style differences between the stored list and the H1s (for example stored hyphens where H1s use colons) count as drift and trigger the full regeneration; do not preserve the stored separator style.
- **What's new in this edition** (`## What's new in this edition`): Already regenerated by book-refresh step 6. Do not touch it. The only exception: if a specific number or date in a bullet contradicts the manuscript or the financials chapter, fix only the contradicting fact and report the fix in your output.

Rules for updates:

- Only change facts that are stale. Do not rewrite for style.
- Pull numbers from the manuscript (frontmatter and financials chapter), not from memory or assumptions.
- Maintain the existing voice and tone. Number formats follow `.Resources/voice.md`.
- No em dashes, no edition numbering.

## Step 2: generate Leanpub release notes email

The about page's "What's new" section is comprehensive and chapter-referenced. The Leanpub email needs to be shorter, punchier, and reader-facing. Transform it into an email that makes a reader want to update.

Rules:

- Lead with the edition date and a one-line hook.
- Group into three to five short bullets maximum. Merge related items.
- No chapter references (readers don't care about internal structure).
- Use the money format from `.Resources/voice.md`: approximately $4.5 billion, never "4.5 billion dollars" and never "$4.5B".
- No jargon, no finding IDs, no HTML comments.
- Keep total length under 200 words. Leanpub emails work best when they're brief.
- Before printing, run `wc -w` on the drafted text and count the bullets. If the text exceeds 200 words or there are more than five bullets, merge or cut until both checks pass, then print.
- End with a one-line call to action ("Update your copy to get the latest analysis.")

If the "What's new in this edition" section is empty, contains TODO or placeholder text, or its edition month is older than the `date` field in `metadata.yaml`, book-refresh step 6 has not run: stop and tell the user to run `/book-refresh <slug>` first.

## Output

First, report what was updated in `about.md` (list the specific fields changed with before/after snippets).

Also report any core input that was missing or empty (`about.md`, `00-frontmatter.md`, or the financials chapter), so the owner can repair the manuscript before the next edition.

Then print the release notes text to the conversation:

```
## Release notes to paste into Leanpub

<Month Year> edition of <Book Title>

<one-line hook>

<3-5 bullets>

<call to action>
```

After printing, remind the user:

1. Copy the release notes text above.
2. Copy updated fields from `about.md` into the corresponding Leanpub settings fields (About the Book, Teaser text, Meta description, Table of contents).
3. Go to Leanpub > your book > Notify Readers.
4. Paste into the Release Notes field.
5. Click "Notify your readers that your book has been updated."
6. This sends an email and bell notification to all readers (unless they disabled it). Leanpub recommends doing this only once or twice a month.

Then commit and push the changes made in this run, never left to the user: `git add` exactly the book's about.md (plus any book file this run fixed), commit with `<Book> <Month Year> edition publish prep` plus the attribution footer `Co-Authored-By: Claude Code <noreply@anthropic.com>`, then `git push`. Stage nothing outside the book directory.

## Success criteria

- The pre-publish gate passed: `.research/<YYYY-MM>-review.md` recorded no unresolved build blockers (or the user confirmed it), and `00-frontmatter.md` contains the house view section.
- Both `output/<NNN>-<slug>.pdf` and `output/<NNN>-<slug>.epub` were confirmed to exist and to be no older than any file in `manuscript/`, `metadata.yaml`, `images/`, `templates/book.typ`, `templates/epub.css`, `scripts/build.py`, and `scripts/lint_manuscript.py` before any `about.md` edit or release-notes output. A stale or missing build stopped the skill instead of triggering a reader notification.
- All stale facts in `about.md` are updated to match the current manuscript; stale edition-date fields are flagged for book-refresh step 5, not edited.
- Release notes text is printed to the conversation.
- Release notes pass a word count of 200 or fewer (`wc -w`) and a bullet count of three to five, with no chapter references, finding IDs, HTML comments, or banned money forms ("4.5 billion dollars", "$4.5B").
- Every bullet reflects a real change from the about page.
- Any missing or empty core input (`about.md`, `00-frontmatter.md`, or the financials chapter) was reported.
- The changes are committed and pushed, and the user has clear instructions for the manual Leanpub steps.
- A first edition was stopped at input 1 with the second-edition-onward explanation.
