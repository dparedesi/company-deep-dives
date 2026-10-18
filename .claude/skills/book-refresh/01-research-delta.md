# Step 1: research delta

**Book slug:** `<slug>` (for example, `palantir`, `rocketlab`). The caller must supply this.

## Goal

Produce a comprehensive, tagged list of material developments about the book's subject since the previous edition. This is the single source of truth the rest of the refresh cycle consumes, so its provenance has to be complete: every finding carries its own source, and every format field uses the controlled vocabulary below.

## Inputs

1. Read `books/<NNN>-<slug>/metadata.yaml`. Extract:
   - `title` and `subtitle`: tells you the book's subject and framing thesis.
   - `last_published`: ISO date of the previous edition. This is the delta window start.
   - `description`: tells you what the current edition already covers (do not re-research those facts as if new).
2. Read `books/<NNN>-<slug>/manuscript/00-frontmatter.md` to confirm the book's thesis, the key findings it currently emphasizes, and the scenario forecasts and dated milestones the previous edition committed to.
3. List the chapter files under `books/<NNN>-<slug>/manuscript/` and read each file's H1 title. You will tag findings with the chapter numbers of this book as they exist on disk today, resolved from this inventory at runtime, plus the optional tag `frontmatter` (see Output format).

If `last_published` is missing, derive a candidate anchor before asking: (1) the "current as of" date inside the `description` field, (2) the date of the last manuscript-touching commit via `git log -1 --format=%cI -- books/<NNN>-<slug>/manuscript/`. Present the candidate and its provenance to the user for confirmation, then write the confirmed value into `last_published` in metadata.yaml before starting the research sweep. Do not proceed on an unconfirmed anchor.

## Research scope

### Window length

Compute the window length in days from `last_published` through today and state it in your report back. If the window exceeds 95 days, tell the user the cadence lapsed and confirm they want a full-window sweep rather than a recent-months focus. For windows exceeding two months, add a `**Materiality:**` line to each finding (thesis-changing, material, or minor), cap minor findings at the top 10 by relevance, and cover every earnings report inside the window; a long window usually contains two or more.

### Categories to sweep

Cover everything material to the book's subject that happened in the delta window. Sweep each category explicitly; do not rely on one broad query:

- **Financial**: earnings reports, revenue, guidance, margins, cash flow, stock price moves, valuation shifts, analyst revisions.
- **Contract and customer**: new or expanded customer wins, losses, renewals, government contracts, international deals.
- **Product**: launches, roadmap changes, deprecations, major releases, technical shifts.
- **Market and competitive**: competitor moves, market structure changes, platform shifts, pricing pressure, new entrants.
- **Leadership and people**: executive changes, board moves, notable hires, departures, public statements from leadership.
- **Regulatory and policy**: rulings, enforcement actions, new laws affecting the subject, lobbying, policy shifts.
- **Controversy and risk**: lawsuits, scandals, outages, security incidents, ethical debates.
- **Black-swan and context**: anything outside normal categories that materially affects the book's thesis (geopolitical events, sudden partnerships, acquisitions).

### Six mandatory sweeps

Beyond the categories above, run these six sweeps every cycle. They exist because certain classes of number and claim systematically rot or expire between editions:

- **Thesis state**: resolve every dated milestone from the prior edition that expired in the window (first launches, certifications, award decisions, profitability dates): did it happen, slip, or fail? The outlook chapter must reflect the resolution.
- **Prior-forecast scorecard**: score the previous edition's scenario forecasts, falsifiers, and the company's guidance versus actuals.
- **Valuation re-snapshot**: re-pull stock price, all-time high, market cap, and multiples as of today; the refresh replaces the old snapshot wholesale.
- **Dashboard metrics**: re-pull cumulative counters (adoption counts, cumulative outcome totals, program counters) with their new as-of dates; these understate systematically if carried forward.
- **Flagged verification**: re-verify any prior finding marked medium or low confidence before it stays asserted in prose.
- **Primary sources**: for load-bearing numbers, prefer the earnings release, the 10-K or 10-Q, or the contract announcement over aggregators.

## Search tools

Use **`mcp__duckduckgo__search`** as the primary search tool for every query category, and **`mcp__duckduckgo__fetch_content`** to read the full content of result pages (press releases, filings, coverage). Both are keyless with effectively no quota cap, so run as many queries as the sweep needs.

If duckduckgo is unavailable or unreliable for a particular query, fall back to, in order:

- `mcp__zai-web-search__web_search_prime` for web search
- `mcp__web_reader__webReader` for reading specific pages

That is the complete chain. Do not route around it, and do not waste queries retrying a tool that is already returning errors for this environment.

## Output format

Write the findings to `books/<NNN>-<slug>/.research/<YYYY-MM>-delta.md` where `<YYYY-MM>` is the current month. Create the `.research/` directory if it does not exist.

Structure each finding as a narrative block with a header, not a field-by-field form. This format gives the next step (fan-out) more context to work with:

```markdown
# <Book subject> delta research: <Month Year>

Delta window: <last_published> through <today>.

---

## F1: <short descriptive title>
**Type:** financial | contract | product | market | leadership | regulatory | controversy | risk | black-swan
**Chapters:** <list of chapter numbers, and optionally `frontmatter`>
**Confidence:** high | medium | low
**Date:** <ISO date or range>
**Supersedes:** <prior finding or manuscript claim this finding replaces> (optional)

One to three sentences describing what happened and why it matters for the book. Include specific numbers, names, and dates. If the finding affects how a chapter should be updated, say so explicitly (for example, "the revenue guidance in the financials chapter should be updated from X to Y").

**Source:** <URL or description of where you found this>

---

## F2: ...
```

Number findings sequentially (F1, F2, ...). Tag a finding with `frontmatter` (alone or alongside chapter numbers) when it affects the executive summary in 00-frontmatter.md, for example its key findings bullets or the "current as of" framing. Aim for completeness over brevity: if a finding is material and recent, include it even if it might overlap with another. The fan-out step resolves overlaps.

### Validate before writing

Before writing the file, validate every finding block against the template. A block passes only if it has all six required elements:

1. A `## Fn: <short descriptive title>` header with sequential numbering.
2. A `**Type:**` line whose value is exactly one of: financial, contract, product, market, leadership, regulatory, controversy, risk, black-swan. Never `add`, `update`, or `remove`; those are step 2 operations, not finding categories.
3. A `**Chapters:**` line listing the affected chapter numbers, plus `frontmatter` where relevant.
4. A `**Confidence:**` line whose value is exactly one of `high`, `medium`, `low`. No compounds (for example `medium-high`) and no parenthetical annotations; if the confidence needs qualification, explain it in the narrative sentences or the Data gaps section, not in the field value.
5. A `**Date:**` line with an ISO date or range.
6. A `**Source:**` line containing a URL, or the outlet name plus article title. A single `Sources:` line at the top of the file does not substitute for per-finding Source lines.

Fix any block that fails before writing the file.

After all findings, include:

1. A **summary table** mapping chapters to findings (which chapters have how many findings).
2. A **data gaps and verification needs** section noting any findings with low confidence or that need primary source verification before inclusion in the manuscript.

## Success criteria

- The file exists at `books/<NNN>-<slug>/.research/<YYYY-MM>-delta.md`.
- Every finding block passes the six-element validation above.
- Every major category and all six mandatory sweeps have either findings or an explicit "no material developments" note.
- Every dated thesis milestone from the prior edition that expired in the window has a resolution finding.
- Valuation and dashboard numbers are re-pulled with their new as-of dates, not carried forward.
- No finding predates `last_published`.
- No finding is a restatement of something already in the current manuscript (spot-check by reading a relevant chapter before recording the finding).

Report back with the path to the research file, the window length in days, and a one-line summary of what the delta window produced (rough count of findings per category).
