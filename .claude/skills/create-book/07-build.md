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

1. **Manuscript checks gate**: The build script runs manuscript checks (the gates section of `.Resources/quality-bar.md`) before compiling. If build.py reports gate failures, fix the listed lines and rebuild; the gate is not bypassed. If the installed build script does not run the gates, run the gates section of `.Resources/quality-bar.md` yourself across the manuscript and treat any hit as a failure before proceeding.

2. **File existence and size**: Confirm both PDF and EPUB exist with non-zero file size. For a first edition of 80,000 to 150,000 words, expect the PDF to be 1.5 to 3.0 MB and the EPUB to be 500 KB to 1.5 MB.

3. **No em dashes or en dashes**: Grep the manuscript and about.md for both dash characters (the em dash, U+2014, and the en dash, U+2013, written here by byte sequence):
   ```bash
   LC_ALL=C grep -rn -e $'\xe2\x80\x94' -e $'\xe2\x80\x93' books/<NNN>-<slug>/manuscript/ books/<NNN>-<slug>/about.md
   ```
   This should return zero hits for both characters in both locations. If any hit appears, replace the dash with a comma, colon, parentheses, or two separate sentences, then rebuild.

4. **No edition numbering**: Grep for numbered editions:
   ```bash
   grep -ri "first edition\|second edition\|third edition\|1st edition\|2nd edition" books/<NNN>-<slug>/manuscript/
   ```
   This should return zero hits (unless "first edition" appears in the about.md release notes section).

5. **Chapter ordering**: Confirm the chapter files sort correctly and the table of contents in about.md matches the actual chapter files.

6. **Title page**: Confirm metadata.yaml has a valid title, subtitle, and author.

### 3. If the build fails

Read the error output. Common failures:
- **Manuscript checks failed**: the output lists each hit with file and line; the scans are defined in `.Resources/quality-bar.md`, gates section. Fix the listed lines and rebuild.
- **Typst not installed**: Run `brew install typst`.
- **Missing cover**: Confirm `images/cover.jpg` exists.
- **Empty manuscript**: Confirm chapter files have content.
- **Invalid YAML**: Validate metadata.yaml syntax.

Fix the issue and rebuild.

## Success criteria

- Build completes without errors.
- Both PDF and EPUB exist with reasonable file sizes.
- The manuscript checks gate passed.
- No em dashes or en dashes in the manuscript or about.md.
- No edition numbering in the manuscript.
- Chapter ordering matches the about.md table of contents.
- Title, subtitle, and author are correct in the PDF.
- The new book directory is committed and pushed, with nothing staged outside it (repo-style message with attribution footer).

Report back with file sizes and confirmation of all verification checks.

## Commit the edition

Commit and push the new book as the final action of this phase, never left to the user: `git add` exactly the new book directory (including `.research/`, about.md, metadata.yaml, cover images, and output/), commit with `Add <Company> deep-dive book: <Title>` plus the attribution footer `Co-Authored-By: Claude Code <noreply@anthropic.com>`, then `git push`. Stage nothing outside the book directory.

## Next steps after build

The book is now ready for the user to:

1. Review the manuscript for accuracy and voice.
2. Skip `/publish-release <slug>` for a first edition: it exists to notify existing readers after a refresh, and its stop condition rejects first-edition release notes. Run it from the second edition onward, right after each `/book-refresh <slug>`.
3. Upload to Leanpub using the fields in about.md.
4. Replace the placeholder cover with a real cover image.
