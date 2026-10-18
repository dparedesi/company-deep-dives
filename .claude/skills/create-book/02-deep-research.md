# Phase 2: deep research

**Company name:** the user-provided name. The caller must supply this.
**Book folder:** `books/<NNN>-<slug>/`. Determined in phase 1.

## Goal

Produce exhaustive, multi-domain research that forms the factual foundation of the entire book. This is not a quick overview. It is the deepest research pass possible, covering the company from every angle with specific numbers, dates, names, and sources.

## Critical requirement: team of agents

This phase MUST use a team of agents. Spawn research agents in parallel, each covering a different domain. A single agent cannot produce the volume and depth required for a comprehensive deep dive.

**Spawn in waves of 3 to 5 agents** rather than all 7-8 simultaneously. Spawning 8+ agents at once frequently triggers API rate limits (429 errors), causing agents to fail before completing their research. A practical pattern:
- Wave 1: financials, technology, market (3 agents)
- Wave 2: history, customers, ethics (3 agents)
- Wave 3: outlook plus any optional domain agents (2-3 agents)

Spawned agents inherit the session's permission mode; the Agent tool's `mode` parameter is deprecated and ignored, so do not pass it. Each agent writes only its own assigned research file.

## Agent assignments

Spawn these agents. Adjust the number based on the company's profile (some companies need more agents, some need fewer):

### Agent 1: Financial history
Research domain:
- Complete earnings history (quarterly and annual) for at least the last 3 to 5 years
- Revenue, gross margin, operating margin, net income, free cash flow
- Stock performance: IPO price, current price, all-time high, all-time low, market cap
- Valuation metrics: P/E, P/S, EV/EBITDA, Rule of 40
- Capital structure: debt, cash position, share count, dilution history
- Guidance vs actuals track record
- Analyst coverage: price targets, ratings distribution, consensus estimates

### Agent 2: Technology and products
Research domain:
- What the company builds and how it works (technical depth, not marketing copy)
- Core products and platforms, their technical architecture
- R&D spending and patent portfolio
- Technical differentiation: what makes their technology hard to replicate
- Engineering culture and hiring practices
- Open source contributions, developer community
- Product roadmap and upcoming launches
- Technical debt, known limitations, scalability challenges

### Agent 3: Market and competition
Research domain:
- Total addressable market (TAM), serviceable addressable market (SAM), serviceable obtainable market (SOM)
- Direct competitors and their market shares
- Indirect competitors and potential disruptors
- Competitive advantages (moats) and disadvantages
- Pricing strategy and positioning
- Analyst coverage and market research reports
- Industry trends and structural shifts
- Barriers to entry

### Agent 4: History, founding, and leadership
Research domain:
- Founding story: who, when, where, why, initial funding
- Key milestones and pivots in the company's history
- Executive team: CEO, CFO, CTO, COO backgrounds and track records
- Board of directors and notable investors
- Company culture, values, and organizational structure
- HQ locations, office footprint, remote work policy
- Employee count, growth rate, Glassdoor/Indeed sentiment
- Notable alumni and where they went

### Agent 5: Customers and use cases
Research domain:
- Named customers (as many as possible, with contract details if public)
- Customer concentration risk
- Deployment examples and case studies with specific outcomes
- Customer acquisition strategy and sales motion
- Net revenue retention, churn rates
- Partnership ecosystem and integrations
- Customer testimonials and public references
- Government/defense contracts (if applicable)

### Agent 6: Ethics, controversy, and risk
Research domain:
- Lawsuits, regulatory actions, and investigations
- Scandals, data breaches, and security incidents
- Ethical debates surrounding the company's work
- Societal impact: positive and negative
- Criticism from public figures, journalists, and competitors
- Employee activism, walkouts, or organized dissent
- Environmental, social, and governance (ESG) considerations
- Geopolitical risks and sanctions exposure

### Agent 7: Future outlook
Research domain:
- Analyst forecasts and consensus estimates (revenue, earnings for next 2 to 3 years)
- Strategic initiatives and growth vectors
- Upcoming catalysts: product launches, contract decisions, regulatory rulings
- Scenario analysis: bull, base, and bear cases from credible sources
- Long-term vision from leadership (public statements, investor letters)
- Industry disruption risks and opportunities
- M&A speculation and strategic options
- Blue sky opportunities and untapped markets

### Optional additional agents
Add if relevant to the company:
- Government contracts and public sector strategy
- Supply chain, manufacturing, and operations
- International expansion and geographic strategy
- Regulatory and compliance landscape
- Specific technology domain (AI, space, biotech, fintech)

## Research tool strategy

Each agent should use **mcp__duckduckgo__search** as the primary search tool and **mcp__duckduckgo__fetch_content** to read result pages. Both are keyless with effectively no quota cap, so agents can run many queries without rationing.

The native web search tool returns 400 errors in this environment. Never use it, and never list it as a fallback.

If duckduckgo is unavailable or unreliable for a particular query, agents should fall back to these MCP tools:

- `mcp__zai-web-search__web_search_prime` for web search
- `mcp__web_reader__webReader` for reading specific pages

Tell every spawned agent the tool order explicitly in its prompt. Do not assume a subagent knows the owner's global tool rules.

## Agent output format

Each agent writes its findings to a separate file in `books/<NNN>-<slug>/.research/`:

- `01-financials.md`
- `02-technology.md`
- `03-market.md`
- `04-history.md`
- `05-customers.md`
- `06-ethics-risk.md`
- `07-outlook.md`
- Additional agents use `08-<domain>.md`, `09-<domain>.md`, etc.

One file per domain, at the exact paths above; no other filenames belong in `.research/` root. Domain research files use only this numbering scheme; planning outputs live at their own exact paths (for example `chapter-plan.md`, never `09-chapter-plan.md`).

### Aggregate the claims register

After all domain agents finish, aggregate every load-bearing number (annual and quarterly financials, top contract values, flagship partnership dates and values, customer and developer counts, market share, valuation metrics) into `books/<NNN>-<slug>/.research/claims-register.md` with columns: metric, value, unit, period, source artifact, source URL or filing reference, as-of date, confidence. Every number that anchors an argument gets a row; writing and review phases cite register entries.

Each research file must follow this structure:

```markdown
# <Company name>: <Domain> research

Research date: <today's date>
Agent: <domain name>

---

## Overview

Two to four paragraphs summarizing the key findings in this domain. This is the executive summary for the domain.

---

## Detailed findings

### <Finding category 1>

<Specific facts with numbers, dates, and sources. Write in narrative prose, not bullet-point lists. Each paragraph should make a specific claim supported by evidence.>

**Source:** <URL or publication name>

### <Finding category 2>
...

---

## Key numbers

| Metric | Value | As of date | Source |
|--------|-------|------------|--------|
| Revenue | ... | ... | ... |
| ... | ... | ... | ... |

---

## Data gaps

List any questions that could not be answered with available sources. These are holes that may need manual research or primary source access. A number recorded as a data gap is unavailable downstream: no writing agent may supply it from memory or general knowledge, and flagging the gap in prose is the only permitted use.
```

## Agent prompt template

When spawning each agent, use this template (adapt the domain and file path):

```
You are a research agent for a company deep-dive book. Your domain: <DOMAIN>.

Company: <COMPANY NAME>

Your job is to produce the deepest, most comprehensive research on <COMPANY NAME>'s <DOMAIN> that is possible using web search. Be specific: use real numbers, real dates, real names. Do not guess. If you cannot confirm something, say so.

Write your findings to books/<NNN>-<slug>/.research/<NN>-<domain>.md following the structured format in .claude/skills/create-book/02-deep-research.md (read it first).

Research categories to cover:
<list from agent assignment above>

Use `mcp__duckduckgo__search` as your primary search tool and `mcp__duckduckgo__fetch_content` to read pages from results. Run at least 10 to 15 different queries to cover your domain thoroughly. If duckduckgo fails, fall back to `mcp__zai-web-search__web_search_prime` and `mcp__web_reader__webReader`. Never use the native web search tool: it returns 400 errors in this environment.

Be exhaustive. A good deep-dive book distinguishes itself by the depth of its research, not by having the same surface-level facts everyone else has.
```

## Success criteria

- All research files exist in `books/<NNN>-<slug>/.research/`.
- Each file follows the structured format (overview, detailed findings, key numbers table, data gaps).
- No file is a stub. Each domain file has substantial, specific content with real numbers and sources.
- Files reference specific sources (URLs, publication names, report titles).
- Data gaps are honestly reported where sources were insufficient.
- A claims register exists at `books/<NNN>-<slug>/.research/claims-register.md` covering every number that anchors an argument, with source and as-of date per row.
- Exactly one file per domain exists (no `-v2` siblings, no superseded duplicates left in place).
- Every data gap recorded in a research file is treated as unavailable downstream; no writing agent supplies such a number from memory or general knowledge.

Report back with a list of the research files created and a rough word count for each. Highlight any domains where research was thin and may need supplementation.

## Handling stuck or slow agents

Research agents can get stuck: search tools return errors, MCP tools hit rate limits, or the agent enters a loop. Practical guidance:

1. **No wall-clock triggers.** The output file for every agent is named before spawn: `books/<NNN>-<slug>/.research/<NN>-<domain>.md`. React to the agent's completion or failure signal, not to elapsed time; a slow agent is usually still working. When a task signal reports failure, or an agent reports completion, verify the artifact: the file exists, is non-empty, and is at least 3 KB. Retry only on a failure signal, or on completion without a usable artifact; silence alone is not a failure signal. Stop a failed agent with `TaskStop` if it still shows as active, then spawn exactly one replacement. The replacement writes to the exact same file path, overwriting the failed attempt's partial output; never invent sibling filenames such as `-v2` (a previous run produced `03-market-v2.md` this way, and downstream phases had no canonical marker for which version to trust).
2. **Do not wait for all agents to complete** before proceeding to phase 3 (chapter planning). If at least 5 of the 7 core domain research files (`01-financials.md` through `07-outlook.md`) are available, start the planning agent while the stragglers finish. The planner re-checks `.research/` before presenting its plan and incorporates files that arrived meanwhile (step 5 of `03-chapter-planning.md`). After the plan is approved, and before any writing agent spawns, confirm that every expected research file exists; wait for or retry any stragglers at that point.
3. **Accept variable quality.** Research files will range from 8 KB to 20 KB. That variance is fine. What matters is that each domain has enough material for the chapter planner and writers to work with.
4. **If a domain is genuinely thin** (the agent delivered less than 3 KB), note it. The chapter writing phase may need to supplement with inline research for that domain's chapters.
5. **Dedupe before phase 3.** List `books/<NNN>-<slug>/.research/`. If any domain exists in two versions despite the same-path rule, keep exactly one canonical version per domain (the more complete file, or a merge of the two), delete the other, and record the choice in the report-back.
