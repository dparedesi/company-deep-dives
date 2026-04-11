# Step 1: research delta

**Book slug:** `<slug>` (for example, `palantir`, `rocketlab`). The caller must supply this.

## Goal

Produce a comprehensive, tagged list of material developments about the book's subject since the previous edition. This is the single source of truth the rest of the refresh cycle consumes.

## Inputs

1. Read `books/<NNN>-<slug>/metadata.yaml`. Extract:
   - `title` and `subtitle`: tells you the book's subject and framing thesis.
   - `last_published`: ISO date of the previous edition. This is the delta window start.
   - `description`: tells you what the current edition already covers (do not re-research those facts as if new).
2. Read `books/<NNN>-<slug>/manuscript/00-frontmatter.md` to confirm the book's thesis and the key findings it currently emphasizes.
3. List the chapter files under `books/<NNN>-<slug>/manuscript/` to learn the chapter count and the topic of each chapter (use the H1 title in each file). You will tag findings by chapter number.

If `last_published` is missing, stop and ask the user what delta window to use. Do not guess.

## Research scope

Delta window: `last_published` through today's date. Cover everything material to the book's subject that happened in that window. Categories to sweep (adapt to the book's subject; these are typical for a company deep dive):

- **Financial**: earnings reports, revenue, guidance, margins, cash flow, stock price moves, valuation shifts, analyst revisions.
- **Contract and customer**: new or expanded customer wins, losses, renewals, government contracts, international deals.
- **Product**: launches, roadmap changes, deprecations, major releases, technical shifts.
- **Market and competitive**: competitor moves, market structure changes, platform shifts, pricing pressure, new entrants.
- **Leadership and people**: executive changes, board moves, notable hires, departures, public statements from leadership.
- **Regulatory and policy**: rulings, enforcement actions, new laws affecting the subject, lobbying, policy shifts.
- **Controversy and risk**: lawsuits, scandals, outages, security incidents, ethical debates.
- **Black-swan and context**: anything outside normal categories that materially affects the book's thesis (geopolitical events, sudden partnerships, acquisitions).

Search for each category explicitly. Do not rely on one broad query.

## Search tools

Use **WebSearch** (the built-in tool) as the primary search method. It is available in every Claude Code instance and requires no setup.

If WebSearch returns errors, empty results, or is unreliable for a particular query, fall back to these MCP tools if they are available in the current environment:

- `mcp__zai-web-search__web_search_prime` for web search
- `mcp__web_reader__webReader` for reading specific pages

Do not treat MCP tools as required. The skill must work with WebSearch alone.

## Output format

Write the findings to `books/<NNN>-<slug>/.research/<YYYY-MM>-delta.md` where `<YYYY-MM>` is the current month. Create the `.research/` directory if it does not exist.

Structure each finding as a narrative block with a header, not a field-by-field form. This format gives the next step (fan-out) more context to work with:

```markdown
# <Book subject> delta research: <Month Year>

Delta window: <last_published> through <today>.

---

## F1: <short descriptive title>
**Type:** financial | contract | product | market | leadership | regulatory | controversy | risk | black-swan
**Chapters:** <list of chapter numbers>
**Confidence:** high | medium | low
**Date:** <ISO date or range>

One to three sentences describing what happened and why it matters for the book. Include specific numbers, names, and dates. If the finding affects how a chapter should be updated, say so explicitly (for example, "the revenue guidance in Chapter 4 should be updated from X to Y").

**Source:** <URL or description of where you found this>

---

## F2: ...
```

Number findings sequentially (F1, F2, ...). Aim for completeness over brevity: if a finding is material and recent, include it even if it might overlap with another. The fan-out step resolves overlaps.

After all findings, include:

1. A **summary table** mapping chapters to findings (which chapters have how many findings).
2. A **data gaps and verification needs** section noting any findings with low confidence or that need primary source verification before inclusion in the manuscript.

## Success criteria

- The file exists at `books/<NNN>-<slug>/.research/<YYYY-MM>-delta.md`.
- Every finding has type, chapters, confidence, date, and source.
- Every major category listed above has either findings or an explicit "no material developments" note.
- No finding predates `last_published`.
- No finding is a restatement of something already in the current manuscript (spot-check by reading a relevant chapter before recording the finding).

Report back with the path to the research file and a one-line summary of what the delta window produced (rough count of findings per category).
