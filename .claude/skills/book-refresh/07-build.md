# Step 7: build and verify

**Book slug:** `<slug>`. The caller must supply this.

## Goal

Build the PDF and EPUB from the updated manuscript and verify the output.

## Process

Run the build from the repo root:

```bash
python scripts/build.py <slug>
```

This generates:
- `books/<NNN>-<slug>/output/<NNN>-<slug>.pdf`
- `books/<NNN>-<slug>/output/<NNN>-<slug>.epub`

## Verification

After the build succeeds:

1. Confirm both files exist in the output directory and have non-zero file size.
2. Grep the manuscript for common issues:
   - `grep -r "Second Edition\|Third Edition" books/<NNN>-<slug>/manuscript/` should return zero hits.
   - `grep -r "<old date>" books/<NNN>-<slug>/manuscript/` using the previous edition date should return zero hits (unless the old date appears in valid historical context, like "founded in 2003").
3. Spot-check the PDF (if possible): confirm the title page does not contain edition numbering and the frontmatter says "current as of <Month Year>".

## Success criteria

- Build completes without errors.
- Both PDF and EPUB exist with non-zero size.
- No stale edition references remain in the manuscript.
- The frontmatter reflects the new edition date.

Report back with file sizes and confirmation of the verification checks.
