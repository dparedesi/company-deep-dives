# Step 5: generate release notes

**Book slug:** `<slug>`. The caller must supply this.

## Goal

Generate the "What's new in this edition" section for the book's about page. This section tells readers what changed since the previous edition. Pull from the research findings, the applied changes, and the actual manuscript diff.

## Inputs

1. Read the research delta file: `books/<NNN>-<slug>/.research/<YYYY-MM>-delta.md`.
2. Read the changes file: `books/<NNN>-<slug>/.research/<YYYY-MM>-changes.md`.
3. Read the about page: `books/<NNN>-<slug>/about.md`.
4. Read `books/<NNN>-<slug>/metadata.yaml` to get the current edition date.

## Process

Review the research and changes files to identify the most significant updates. Group them by importance and theme. Release notes should be concise and reader-facing: emphasize what matters to a reader deciding whether to update, not every minor edit.

Organize into these sections (adapt to the actual changes; omit empty sections):

- **Major developments**: black-swan events, transformative deals, product launches that materially change the thesis.
- **Financial updates**: earnings, guidance, stock moves that affect the investment or strategic outlook.
- **Market and competitive**: new rivals, market structure shifts, pricing pressure.
- **Product and technology**: major releases, deprecations, technical shifts.
- **Leadership and organizational**: executive changes, strategic pivots.
- **Risk and controversy**: lawsuits, scandals, regulatory actions that affect risk assessment.

Each bullet should be one to two sentences, written for a general reader (not an insider). Avoid jargon where possible. If a finding affects a specific chapter, note it in parentheses: "(Chapter 4)".

## Output format

Write the release notes to `books/<NNN>-<slug>/about.md`. Find the existing "What's new in this edition" section (or create it if it does not exist) and replace it with:

```markdown
## What's new in this edition

This <Month Year> edition incorporates developments through <date>. Major updates include:

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

Use "current as of <Month Year>" in the first sentence, where <Month Year> matches the `date` field in `metadata.yaml`. For example: "This April 2026 edition incorporates developments through April 11, 2026."

## Success criteria

- `books/<NNN>-<slug>/about.md` is updated with a new "What's new in this edition" section.
- The section leads with the edition month and year and a "current as of" date.
- Every bullet reflects a real change from the research or changes file.
- No bullet mentions findings that were dropped in step 2.
- The section is concise (five to fifteen bullets) and reader-facing.

Report back with the path to the updated about page and a count of bullets in the release notes.
