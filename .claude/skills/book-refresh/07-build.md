# Step 7: build and verify

**Book slug:** `<slug>`. The caller must supply this.

## Goal

Build the PDF and EPUB from the updated manuscript, verify the output, and close the cycle by bumping `last_published`.

## Process

Before building, remove any legacy traceability comments from previous editions in the manuscript:

```bash
perl -pi -e 's/ ?<!-- F\d+(, ?F\d+)*( ?\([^)]*\))? -->//g; s/ ?<!-- consistency fix: [^>]*-->//g' books/<NNN>-<slug>/manuscript/*.md
```

The pattern matches single-ID, multi-ID, and annotated forms (a narrower pattern that skips the `(, ?F\d+)*` group leaves multi-ID comments such as `<!-- F1, F2 -->` behind, and those occur in this repo). Then verify `grep -rc '<!--' books/<NNN>-<slug>/manuscript/` returns zero for every file; if any comment remains, remove it before building. Manuscript files contain zero HTML comments at all times; traceability lives in this cycle's `.research/` artifacts, not in prose.

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
2. Read the previous edition date from the current `last_published` value in `books/<NNN>-<slug>/metadata.yaml`: at this point it still holds the previous edition's date, which is the `<old date>` for the grep. (On a re-run after the bump was already applied to the working tree, use `git diff HEAD -- books/<NNN>-<slug>/metadata.yaml | grep '^-.*last_published'`; if the bump is already committed, use `git log -p -- books/<NNN>-<slug>/metadata.yaml` and take the value from the commit preceding the bump.) Then run `grep -rn "Second Edition\|Third Edition\|<old date>" books/<NNN>-<slug>/manuscript/` and require zero hits, excepting occurrences in valid historical context (for example "founded in 2003").
3. Run the dash scans: `LC_ALL=C grep -rn -e $'\xe2\x80\x94' -e $'\xe2\x80\x93' books/<NNN>-<slug>/manuscript/` must return zero hits for both the em dash and the en dash characters in every chapter.
4. Read the opening pages of the PDF with the Read tool (`books/<NNN>-<slug>/output/<NNN>-<slug>.pdf`, pages 1 to 5). Confirm the title page contains no edition numbering and the frontmatter contains "current as of <Month Year>". Do not skip this step; if the PDF cannot be read, report the failure as a failure rather than marking the check passed. The fallback CLI path is `pdftotext <pdf> - | head -60`, only if native PDF reading is unavailable.
5. Run `unzip -p books/<NNN>-<slug>/output/<NNN>-<slug>.epub '*.xhtml' | grep -c '<!--'` and require zero, so no traceability comments ship in the EPUB (they leak verbatim without this check; the April 2026 palantir build shipped two).
6. Confirm the build script ran the manuscript checks (the gates section of `.Resources/quality-bar.md`) before compiling. If build.py reports gate failures, fix the listed lines and rebuild; the gate is not bypassed.

## Closing the cycle

After all verification checks pass, update `last_published` in `books/<NNN>-<slug>/metadata.yaml` to today's ISO date. This is the last edit of the cycle and the end-of-cycle bump that anchors the next research delta window. It happens only here, after both outputs verify, so an interrupted cycle never records a release that did not happen.

Then report the edition ready: the book, the edition label, the output file sizes, and the results of every verification check.

Then commit and push the edition as part of this step, never left to the user: `git add` exactly the book directory (manuscript, about.md, metadata.yaml, outputs, and this edition's `.research/` artifacts), commit with `<Book> <Month Year> edition refresh` plus the attribution footer `Co-Authored-By: Claude Code <noreply@anthropic.com>`, then `git push`. Stage nothing outside the book directory; unrelated working-tree changes stay untouched. After the push, `/publish-release <slug>` prepares the reader notification.

## Success criteria

- Build completes without errors.
- The manuscript checks gate passed.
- Both PDF and EPUB exist with non-zero size.
- No stale edition references remain in the manuscript.
- No em dashes, en dashes, or HTML comments remain in the manuscript, and the EPUB contains zero HTML comments.
- The title page and frontmatter were verified in the built PDF.
- `last_published` is updated to today's ISO date after both outputs verify.
- The edition is committed and pushed (the book directory plus this edition's `.research/` artifacts only, nothing else staged).

Report back with file sizes, the results of each verification check, confirmation of the `last_published` bump, confirmation of the edition commit and push, and the edition-ready summary.
