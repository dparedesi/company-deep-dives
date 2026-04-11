# Phase 7: build and verify

**Book slug:** `<slug>`. Determined in phase 1.

## Goal

Build the PDF and EPUB from the manuscript and verify the output is correct.

## Process

### 1. Run the build

From the repo root:

```bash
python scripts/build.py <slug>
```

This generates:
- `books/<NNN>-<slug>/output/<NNN>-<slug>.pdf`
- `books/<NNN>-<slug>/output/<NNN>-<slug>.epub`

### 2. Verify output

After the build succeeds:

1. **File existence and size**: Confirm both PDF and EPUB exist with non-zero file size. For a first edition of 80,000 to 150,000 words, expect the PDF to be 1.5 to 3.0 MB and the EPUB to be 500 KB to 1.5 MB.

2. **No em dashes**: Grep the manuscript for em dashes:
   ```bash
   grep -r '—' books/<NNN>-<slug>/manuscript/
   ```
   This should return zero hits.

3. **No edition numbering**: Grep for numbered editions:
   ```bash
   grep -ri "first edition\|second edition\|third edition\|1st edition\|2nd edition" books/<NNN>-<slug>/manuscript/
   ```
   This should return zero hits (unless "first edition" appears in the about.md release notes section).

4. **Chapter ordering**: Confirm the chapter files sort correctly and the table of contents in about.md matches the actual chapter files.

5. **Title page**: Confirm metadata.yaml has a valid title, subtitle, and author.

### 3. If the build fails

Read the error output. Common failures:
- **Typst not installed**: Run `brew install typst`.
- **Missing cover**: Confirm `images/cover.jpg` exists.
- **Empty manuscript**: Confirm chapter files have content.
- **Invalid YAML**: Validate metadata.yaml syntax.

Fix the issue and rebuild.

## Success criteria

- Build completes without errors.
- Both PDF and EPUB exist with reasonable file sizes.
- No em dashes in the manuscript.
- No edition numbering in the manuscript.
- Chapter ordering matches the about.md table of contents.
- Title, subtitle, and author are correct in the PDF.

Report back with file sizes and confirmation of all verification checks.

## Next steps after build

The book is now ready for the user to:

1. Review the manuscript for accuracy and voice.
2. Run `/publish-release <slug>` to prepare Leanpub publication (though for a first edition, the about.md should already be complete from phase 6).
3. Upload to Leanpub using the fields in about.md.
4. Replace the placeholder cover with a real cover image.
