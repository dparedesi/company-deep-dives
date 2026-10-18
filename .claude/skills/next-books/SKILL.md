---
name: next-books
description: Research and recommend which company deep-dive books to write next, based on search trends, news activity, investor interest, market disruption, and content gaps. Always uses a team of agents for deep parallel research. Use when the user says "what should the next book be", "recommend next books", "what companies are trending", "which company should I write about next", or wants strategic guidance on book selection.
---

# next-books

## Why?

Writing a deep-dive book is a major investment of research and creative work. Picking the right company matters: the book needs an audience actively searching for deep analysis. This skill runs exhaustive multi-angle research to identify which companies have the highest reader demand right now, then ranks them with clear justification.

## When to use

Use this skill when the user wants strategic guidance on what company to write about next. Triggers include "what should the next book be", "recommend next books", "what companies are trending", "which company should I write about next", "what should I write about", or any phrasing asking for book selection guidance.

## Quick start

1. `ls books/` and build the exclusion list (companies that already have books).
2. Phase 1 (`01-research-agents.md`): spawn 6 to 8 angle agents in waves of 3 to 5. Their files land in `.research/next-books/<YYYY-MM-DD>/` as `01-search-trends.md` through `08-wildcard.md`.
3. Phase 2 (`02-consolidate.md`): one agent scores and ranks all candidates into `09-consolidated-ranking.md` in the same directory.
4. Phase 3 (`03-report.md`): write `.research/next-books/<YYYY-MM-DD>-report.md`, the deliverable the user reads to decide the next book.
5. Phase 3 commits and pushes the run artifacts as its final step (see `03-report.md`). When the user picks a company, run `/create-book <company>`. This skill creates nothing else.

## Core requirement: team of agents

This skill MUST use a team of agents for research. Spawn 6 to 8 research agents, each covering a different angle of demand analysis. A single agent cannot produce the breadth and depth needed for confident recommendations.

Spawn the agents in waves of 3 to 5 rather than all at once; spawning 8 or more agents simultaneously frequently triggers API rate limits (429 errors).

Each agent writes only its own assigned file.

## The three-phase workflow

### Phase 1: parallel research (`01-research-agents.md`)

Spawn 6 to 8 research agents in waves, each covering a different angle:

1. **Search trends agent**: Google Trends data, search volume, most-searched public companies, rising queries
2. **News and media agent**: Companies dominating financial and tech news in the last 3 to 6 months
3. **Investor interest agent**: Highest retail interest (Reddit, Robinhood, StockTwits), institutional activity, analyst coverage
4. **Recent IPOs and SPACs agent**: Companies that recently went public or are about to, where people need foundational understanding
5. **Industry disruption agent**: Companies driving major shifts (AI, defense tech, space, fintech, energy) that attract curiosity
6. **Content gap agent**: What deep-dive content already exists (Leanpub, Amazon, Substack), where are the gaps
7. **Book performance agent**: If books already exist in this repo, analyze which ones get the most traction and why (news cycle, company momentum, topic freshness)
8. **Wildcard agent**: Unusual or counterintuitive picks that may not be obvious but have strong niche demand

Each agent writes findings to `.research/next-books/<YYYY-MM-DD>/<NN>-<domain>.md`.

### Phase 2: consolidation (`02-consolidate.md`)

One agent reads ALL research files from the current run's directory, identifies overlapping signals, and produces a consolidated ranking that tabulates the top 15 candidates (from a master list of at least 30 unique companies) with scores and justification. This agent also cross-references against existing books in the repo to avoid duplicates.

### Phase 3: report (`03-report.md`)

Generate a final recommendation report as a standalone markdown file. Includes:
- Top 5 to 7 recommended companies with detailed justification
- For each: why now, target audience, estimated search demand, content gap, and suggested angle
- A "watch list" of companies whose catalyst has not landed yet, with the catalyst to watch
- Summary table with quick comparison

The report follows the normative template in `03-report.md` exactly: same sections, same order, same columns. Output: `.research/next-books/<YYYY-MM-DD>-report.md`.

## Research tool strategy

Each agent should use **`mcp__duckduckgo__search`** as its primary search tool and **`mcp__duckduckgo__fetch_content`** to read result pages. Both are keyless with effectively no quota cap, so agents can run many queries without rationing.

The built-in web search tool is banned in this environment: it returns 400 errors, and an agent that tries it burns its turn on failing calls. Never list it as a fallback.

If duckduckgo is unavailable or unreliable for a particular query, agents should fall back to these MCP tools:

- `mcp__zai-web-search__web_search_prime` for web search
- `mcp__web_reader__webReader` for reading specific pages

Tell every spawned agent the tool order explicitly in its prompt. Do not assume a subagent knows the owner's global tool rules.

## Existing books check

Before starting research, read the list of existing books in the repo:

```bash
ls books/
```

Exclude any company that already has a book. These can appear in the report as "existing coverage" but should not be recommended as new books. Re-run this check every time the skill runs: the book set changes between runs, and a company recommended by a previous run may already have a book by now.

## Shared standards

Every phase that writes an artifact reads `.Resources/voice.md` (from the repo root) before writing and follows its register and hygiene rules; they apply to every generated file, not only book manuscripts. Money figures follow the house format everywhere: "$N billion", "$N million", "$N trillion", with the dollar sign attached.

After each phase, run the artifact gates on the files written so far: zero hits for an em dash (grep with `$'\xe2\x80\x94'`), an en dash (`$'\xe2\x80\x93'`), and non-Latin codepoints (the mixed-language defect class). Fix any hit before starting the next phase.

## Agent coordination rules

1. **Always use a team of agents for phase 1.** This is the heavy-lift phase.
2. **Spawn agents with default permissions.** Agents inherit the session's permission mode. If prompts become excessive, ask the user once to approve an allowlist for this skill (the search MCP tools listed above plus Write for `.research/next-books/**`).
3. **One active writer per file.** Each agent writes only its own assigned file. Never respawn an angle whose agent is still running.
4. **Phase 2 waits for phase 1.** Consolidation starts only after every spawned angle agent reaches a terminal state (see the handling section in `01-research-agents.md`).
5. **Phase 3 waits for phase 2.** The report is generated from the consolidated ranking.

## Output location

All artifacts live under `.research/next-books/` at the repo root (not inside any specific book folder). Each run gets its own dated directory, so a second run can never mix with or overwrite a previous run's files:

- Run directory: `.research/next-books/<YYYY-MM-DD>/` (create it if it does not exist)
- Inside it: `01-search-trends.md`, `02-news-media.md`, `03-investor-interest.md`, `04-recent-ipos.md`, `05-industry-disruption.md`, `06-content-gaps.md`, `07-book-performance.md`, `08-wildcard.md`, `09-consolidated-ranking.md`
- Final report: `.research/next-books/<YYYY-MM-DD>-report.md`

Phase 2 reads only files from the current run's directory; never mix files across run dates. If the skill runs twice on the same date, suffix the second run's label with -2 (and -3, and so on) in both the directory name and the report name, so `<YYYY-MM-DD>` throughout this skill reads as the run's suffixed label on same-day re-runs.
