# Step 3: update one chapter

**Book slug:** `<slug>`. The caller must supply this.

**Chapter:** `<NN>-<name>.md` (for example, `04-financials.md`, `05-customers.md`; numbers and names vary by book, use the actual files in the manuscript folder). The caller must supply this. The chapter may also be `00-frontmatter.md` (the frontmatter has no H1; its structure is bold labels and bullets).

## Goal

Apply the per-chapter change list from step 2 to a specific chapter file. Preserve voice, style, and structure while incorporating new facts and updating outdated claims.

## Inputs

1. Read the change list from step 2: `books/<NNN>-<slug>/.research/<YYYY-MM>-changes.md`. If it does not exist, stop and run step 2 first.
2. Read the target chapter file: `books/<NNN>-<slug>/manuscript/<NN>-<name>.md`.
3. Read `books/<NNN>-<slug>/metadata.yaml` to confirm the book title, date, and voice conventions.
4. Read `.Resources/voice.md` before editing. The chapter must keep its hook, dramatic question, and ending shape; an update that degrades the opening into roadmap or the ending into a summary has failed even if every fact landed.

## Process

Integrate new facts as narrative. Rewrite the affected passage so the new fact lives inside the standing story. Never prepend delta context, never add What changed or since-the-last-edition sections, and never re-paste the prior edition stat block into each updated chapter; later mentions cite or reference, they do not re-paste.

For each change line targeting this chapter in the changes file:

- **Add**: Insert the new fact in the most natural location. If the change file proposes a new subsection, add it with an H2 heading (`## New subsection title`) in sentence case. Write one to three sentences in the chapter's existing voice. If the target is `00-frontmatter.md`, do not add H2 headings; add new content as a bullet under the most fitting bold label.
- **Update**: Find the existing text near the indicated location. Replace the outdated fact with the new one. If the surrounding sentences need reflow to accommodate the new fact, edit them minimally to maintain flow.
- **Remove**: Cut the outdated sentence or paragraph. If removal creates a gap, smooth the surrounding text so the paragraph reads naturally.
- **Replace (snapshot)**: Delete the named prior block (valuation, dashboard) in full, then write the new block in its place, as-of dated inline. Never layer a new snapshot next to the old one. Process every item under the changes file's Stale blocks to delete the same way.

Never add HTML comments to the manuscript file. Traceability lives in the applied-changes ledger (below), not in the chapter file, and comments leak into the published EPUB.

After applying all changes, read the full chapter to check:

- The chapter still flows like a continuous document, not a patchwork of inserts.
- New facts integrate with the surrounding discussion; no jarring jumps in tone or detail level.
- Cross-references to other chapters still make sense. If one references a fact that changed, append a flag to `books/<NNN>-<slug>/.research/<YYYY-MM>-consistency-notes.md` as one line: `| <chapter file> | the cross-reference | why it may now be stale |` (create the file if it does not exist). Do not fix cross-chapter references here; step 4 consumes these notes and fixes them.
- No em dashes, sentence-case headings, acronyms uppercase per project conventions.

## Applied-changes ledger

After applying all changes, append one line per applied change to `books/<NNN>-<slug>/.research/<YYYY-MM>-applied.md` (create the file if missing; use one `## <chapter file>` section heading per chapter) in the form:

`| add/update/remove/replace | Fn | one-line summary of what was applied |`

This ledger is the working-layer traceability record for the cycle; step 6 reads it alongside the diff, and nothing from it ever enters the manuscript.

## Writing conventions

Strictly follow project `CLAUDE.md` conventions and `.Resources/voice.md`:

- **No em dashes**: use colons, commas, parentheses, or separate sentences.
- **Sentence case headings**: only first word and proper nouns capitalized.
- **Acronyms uppercase**: AI, NASA, CEO, API, IPO.
- **Expanded acronyms**: capitalize proper noun portions only.
- **Chapter files start with `# Title`**: H1 heading at the top.
- **New figures follow the charter's number rules**: house money format, a time anchor, and full precision exactly once per book.

## Success criteria

- The chapter file is modified on disk.
- Every change targeting this chapter from the changes file is applied, including every Stale blocks to delete item.
- The chapter reads as a coherent whole in the book's voice, with its hook, dramatic question, and ending shape intact.
- No new em dashes, title-case headings, or lowercase acronyms are introduced.
- Every applied change is recorded in `.research/<YYYY-MM>-applied.md` with its finding ID.
- Fragile cross-references are flagged to this cycle's consistency notes file.
- `grep -c '<!--' books/<NNN>-<slug>/manuscript/<NN>-<name>.md` returns 0: no HTML comments in the manuscript file.

Report back with the path to the modified chapter file and a count of changes applied (additions, updates, removals, replacements).
