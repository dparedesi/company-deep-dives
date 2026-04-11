# Step 3: update one chapter

**Book slug:** `<slug>`. The caller must supply this.

**Chapter:** `<NN>-<name>.md` (for example, `04-financials.md`, `05-customers.md`). The caller must supply this.

## Goal

Apply the per-chapter change list from step 2 to a specific chapter file. Preserve voice, style, and structure while incorporating new facts and updating outdated claims.

## Inputs

1. Read the change list from step 2: `books/<NNN>-<slug>/.research/<YYYY-MM>-changes.md`. If it does not exist, stop and run step 2 first.
2. Read the target chapter file: `books/<NNN>-<slug>/manuscript/<NN>-<name>.md`.
3. Read `books/<NNN>-<slug>/metadata.yaml` to confirm the book title, date, and voice conventions.

## Process

For each change line targeting this chapter in the changes file:

- **Add**: Insert the new fact in the most natural location. If the change file proposes a new subsection, add it with an H2 heading (`## New subsection title`) in sentence case. Write one to three sentences in the chapter's existing voice. Cite the finding ID from the changes file in a trailing comment `<!-- Fn -->` so traceability is preserved.
- **Update**: Find the existing text near the indicated location. Replace the outdated fact with the new one. If the surrounding sentences need reflow to accommodate the new fact, edit them minimally to maintain flow. Add a trailing comment `<!-- Fn (updated) -->`.
- **Remove**: Cut the outdated sentence or paragraph. If removal creates a gap, smooth the surrounding text so the paragraph reads naturally. Add a trailing comment `<!-- Fn (removed) -->`.

After applying all changes, read the full chapter to check:

- The chapter still flows like a continuous document, not a patchwork of inserts.
- New facts integrate with the surrounding discussion; no jarring jumps in tone or detail level.
- Cross-references to other chapters still make sense (if they reference facts that changed, note them for step 4 but do not fix them yet; step 4 is the cross-chapter consistency pass).
- No em dashes, sentence-case headings, acronyms uppercase per project conventions.

## Writing conventions

Strictly follow project `CLAUDE.md` conventions:

- **No em dashes**: use colons, commas, parentheses, or separate sentences.
- **Sentence case headings**: only first word and proper nouns capitalized.
- **Acronyms uppercase**: AI, NASA, CEO, API, IPO.
- **Expanded acronyms**: capitalize proper noun portions only.
- **Chapter files start with `# Title`**: H1 heading at the top.

## Success criteria

- The chapter file is modified on disk.
- Every change targeting this chapter from the changes file is applied.
- The chapter reads as a coherent whole in the book's voice.
- No new em dashes, title-case headings, or lowercase acronyms are introduced.
- All finding IDs are traceable via HTML comments.

Report back with the path to the modified chapter file and a count of changes applied (additions, updates, removals).
