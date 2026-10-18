# Step 6: generate release notes

**Book slug:** `<slug>`. The caller must supply this.

## Goal

Generate the "What's new in this edition" section for the book's about page. This section tells readers what changed since the previous edition. Pull from the research findings, the applied changes, and the actual manuscript diff.

Ownership: this step owns the What's new in this edition section of about.md and regenerates it wholesale. create-book/06 created every section; book-refresh/05 owns the edition-date fields; publish-release owns stale facts in the other sections plus the reader email. Do not touch the other sections.

## Inputs

1. Read the research delta file: `books/<NNN>-<slug>/.research/<YYYY-MM>-delta.md`.
2. Read the changes file: `books/<NNN>-<slug>/.research/<YYYY-MM>-changes.md`.
3. Read the about page: `books/<NNN>-<slug>/about.md`.
4. Read `books/<NNN>-<slug>/metadata.yaml` to get the current edition date.
5. Read the actual manuscript changes. Run `git diff HEAD --stat -- books/<NNN>-<slug>/manuscript/` for a per-file overview, then `git diff HEAD -- books/<NNN>-<slug>/manuscript/` and read the per-file hunks. Also run `git status --short -- books/<NNN>-<slug>/manuscript/` to catch untracked new chapter files. The diff against HEAD is the authoritative record of what this edition actually changed.

## Process

Review the research and changes files, then the manuscript diff, to identify the most significant updates. Use the diff in two ways. First, verification: check that each change line you plan to describe has a corresponding hunk in the diff. A change line with no hunk means step 3 skipped it or step 2 deferred it, so do not claim it in the notes. Second, coverage: scan the diff for significant edits the changes file does not capture, notably consistency fixes from step 4 and date-context updates to the frontmatter, introduction, and conclusion from step 5, and include them when they matter to a reader.

If the diff is empty, determine which case you are in. Either the edition was already committed: run `git log --oneline -3 -- books/<NNN>-<slug>/manuscript/` and read the latest edition commit with `git show <commit> --stat -- books/<NNN>-<slug>/manuscript/` to recover what changed. Or this cycle genuinely produced no manuscript changes: write a short note saying this edition refreshes framing and consistency with few material developments, and do not invent bullets from research findings that never landed.

Group what remains by importance and theme. Release notes should be concise and reader-facing: emphasize what matters to a reader deciding whether to update, not every minor edit.

Organize into these sections (adapt to the actual changes; omit empty sections):

- **Major developments**: black-swan events, transformative deals, product launches that materially change the thesis.
- **Financial updates**: earnings, guidance, stock moves that affect the investment or strategic outlook.
- **Market and competitive**: new rivals, market structure shifts, pricing pressure.
- **Product and technology**: major releases, deprecations, technical shifts.
- **Leadership and organizational**: executive changes, strategic pivots.
- **Risk and controversy**: lawsuits, scandals, regulatory actions that affect risk assessment.

Each bullet should be one to two sentences, written for a general reader (not an insider). Avoid jargon where possible. If a finding affects a specific chapter, note it in parentheses: "(Chapter 4)", using that chapter's number in this book's manuscript. Numbers and money follow the number rules in `.Resources/voice.md` in every bullet.

## Output format

Write the release notes to `books/<NNN>-<slug>/about.md`. Find the existing "What's new in this edition" section (or create it if it does not exist) and replace it with:

```markdown
## What's new in this edition

This <Month Year> edition incorporates developments through <Month D, YYYY>. Major updates include:

### Major developments

- Bullet on the most significant change.

### Financial updates

- Bullet on earnings, revenue, guidance shifts, or stock performance.

### Market and competitive

- Bullet on competitor moves, market structure, pricing.

### Product and technology

- Bullet on launches, deprecations, technical shifts.

### Leadership and organizational

- Bullet on executive changes, strategic pivots.

### Risk and controversy

- Bullet on lawsuits, scandals, regulatory actions.
```

If a section has no updates, omit it. The final release notes should be five to fifteen bullets total; fewer is better.

## Date language

The first sentence must state the edition month and year (matching `date` in metadata.yaml) and the specific cutoff date, in the exact form "This <Month Year> edition incorporates developments through <Month D, YYYY>." Do not use the phrase "current as of" in this section; that phrase belongs to the description paragraphs handled in step 5.

## Success criteria

- `books/<NNN>-<slug>/about.md` is updated with a new "What's new in this edition" section.
- The section leads with the edition month and year and the specific developments-through date.
- Every bullet reflects a real change visible in the manuscript diff, whether or not it originated in the changes file.
- No bullet mentions findings that were dropped in step 2, or changes with no corresponding diff hunk.
- The section is concise (five to fifteen bullets) and reader-facing.
- Every number in every bullet follows the number rules in `.Resources/voice.md`.

Report back with the path to the updated about page and a count of bullets in the release notes.
