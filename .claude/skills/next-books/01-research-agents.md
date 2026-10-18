# Phase 1: parallel research agents

## Goal

Produce exhaustive, multi-angle research on which companies have the highest demand for deep-dive analysis right now. This is not a quick overview. It is a thorough investigation of search trends, news cycles, investor behavior, content gaps, and market dynamics.

## Inputs

- The existing-books list from `ls books/` (the exclusion list; see SKILL.md).
- The run label for this run: today's date, plus a numeric suffix on same-day re-runs (see SKILL.md, output location). Every file in this phase writes into `.research/next-books/<RUN>/`.

## Critical requirement: team of agents

This phase MUST use a team of agents. Spawn 6 to 8 research agents, in waves of 3 to 5, each covering a different angle. Each agent writes only its own assigned file: one agent per angle file, one active writer at a time.

Before spawning, check which books already exist:

```bash
ls books/
```

Pass this list to every agent so they know which companies are already covered.

## Agent assignments

### Agent 1: search trends and query demand

Research domain:
- Google Trends: which public tech/defense/industrial companies have rising search interest in the last 3 to 6 months
- Most-searched companies on financial platforms (Yahoo Finance, Google Finance, Bloomberg)
- Rising "deep dive", "analysis", "stock analysis" queries tied to specific companies
- Search volume estimates for company name + "analysis", company name + "deep dive", company name + "book"
- Companies where public interest spiked recently and has not faded (sustained interest, not one-day spikes)
- Regional search patterns: which companies are trending globally vs US-only

### Agent 2: news and media coverage

Research domain:
- Companies dominating financial and tech news headlines in the last 3 to 6 months
- Major news events: earnings surprises, product launches, lawsuits, regulatory actions, CEO changes
- Media narrative framing: which companies have compelling stories that attract readers
- Frequency of coverage: how often the company appears in major outlets (WSJ, NYT, TechCrunch, Bloomberg, Reuters, FT)
- Documentary, podcast, and long-form content about specific companies (signals reader appetite)
- Controversial or polarizing companies that generate strong opinions (these drive book sales)

### Agent 3: investor and retail interest

Research domain:
- Most-discussed companies on retail investor platforms (Reddit r/wallstreetbets, r/stocks, r/investing; StockTwits; X/Twitter finfluencers)
- Robinhood/retail broker most-held stocks and trending tickers
- Institutional investor activity: 13F filings, hedge fund concentration, activist positions
- Analyst coverage breadth: companies with the most analyst reports, upgrades/downgrades
- Earnings call attendance and transcript interest
- Options market activity as a proxy for interest
- Companies with passionate bull/bear debates (these attract deep-dive readers)

### Agent 4: recent IPOs, SPACs, and newly public companies

Research domain:
- Companies that went public in the last 12 to 18 months where investors still need foundational understanding
- Upcoming IPOs generating buzz (pre-IPO research demand)
- Companies that IPO'd and then had dramatic price action (up or down) attracting attention
- Direct listings and their unique dynamics
- SPACs that actually delivered interesting businesses
- Lockup expirations and secondary offering catalysts
- Companies transitioning from "startup" to "public company" narrative

### Agent 5: industry disruption and thematic interest

Research domain:
- Companies driving or benefiting from AI adoption (infrastructure, chips, applications)
- Defense tech and government contractor momentum (following Palantir's trajectory)
- Space economy: launch, satellites, communications
- Clean energy and energy transition companies
- Fintech disruption: payments, lending, crypto infrastructure
- Biotech and healthcare innovation
- Supply chain reshoring and advanced manufacturing
- Identify thematic clusters where multiple companies are hot but one or two stand out

### Agent 6: content gap analysis

Research domain:
- Search Leanpub, Amazon Kindle, and Google Books for existing deep-dive books on major tech/defense/industrial companies
- Identify companies with ZERO or WEAK deep-dive coverage (the gap)
- Check Substack for popular deep-dive series and which companies they cover
- Look for companies where the only available content is superficial (investor relations pages, Wikipedia) vs substantive analysis
- Identify companies where existing books are outdated: published more than 24 months ago, or predating the company's most recent major business-model shift, platform transition, or revenue-segment change
- Check podcast landscape for companies that are discussed frequently but lack written deep dives

### Agent 7: book performance analysis

Research domain:
- Analyze the books already in this repo: what do their subjects have in common?
- For existing books with traction, what external factors drove interest?
- Cross-reference: if Palantir is getting traction, what similar companies might benefit from the same tailwind?
- Look at "related searches" and "people also search for" patterns around existing book subjects
- Identify companies in the same orbit as existing book subjects (same sector, same investor base, same narrative)
- Check if any existing book subjects have competitor companies that readers would naturally want to compare

### Agent 8: wildcard and contrarian picks

Research domain:
- Companies that are NOT obvious picks but have strong niche followings
- Niche industrial or B2B companies with cult-like investor bases (e.g., ASML, Constellation Software, Comfort Systems)
- Companies undergoing dramatic transformations (turnarounds, pivots, spinoffs)
- Companies with fascinating founding stories or CEO personalities that make for compelling narrative
- International companies gaining US investor attention (TSMC, BYD, Mercado Libre)
- "Boring" businesses with incredible financial metrics that value investors obsess over
- Companies at the intersection of multiple hot themes (e.g., AI + defense, space + manufacturing)

## Query craft

Each agent runs at least 10 to 15 distinct queries, varying intent, not just company names: gap questions, site-scoped searches, platform-specific signals, and contrarian probes. Seed patterns per angle:

| Angle | Seed queries |
|-------|--------------|
| 1 Search trends | "<company> stock analysis" search volume; "most searched companies" Google Trends this month; "<company> deep dive" rising queries |
| 2 News and media | "most covered companies in tech news this month"; "<company> earnings surprise coverage"; site:reuters.com <company> |
| 3 Investor interest | "most discussed stocks on wallstreetbets this month"; "Robinhood top held stocks"; "StockTwits trending tickers" |
| 4 Recent IPOs | "recent tech IPOs last 12 months"; "upcoming IPOs generating buzz"; "best performing newly public companies" |
| 5 Industry disruption | "AI infrastructure companies driving adoption"; "defense tech companies momentum"; "space economy companies to watch" |
| 6 Content gaps | "best books on <company>"; site:leanpub.com <company> deep dive; "<company> book" Goodreads |
| 7 Book performance | "companies similar to <existing subject>"; "people also search for <existing subject>"; "<existing subject> competitors deep dive" |
| 8 Wildcard | "underrated companies with cult followings"; "boring businesses with incredible margins"; "companies undergoing dramatic turnarounds" |

Corroborate before claiming: a demand claim backed by a single source is unverified. Label single-source claims as unverified in the artifact or drop them.

## Agent prompt template

When spawning each agent, use this template:

```
You are a research agent identifying which companies have the highest demand for deep-dive analysis books. Your research angle: <ANGLE>.

Existing books already in the repo (EXCLUDE these from recommendations):
<list from ls books/>

Your job is to identify 15 to 25 companies that rank highest for your specific angle. Be specific: use real data, real search trends, real news events. Do not guess. If you cannot confirm something, say so.

For each company, provide:
1. Company name and ticker
2. Why they rank for your angle (specific evidence)
3. Estimated demand signal strength (high/medium/low)
4. Key catalyst or reason readers would seek a deep dive NOW

Write your findings to .research/next-books/<RUN>/<NN>-<domain>.md following the structured format below.

Search tools: use `mcp__duckduckgo__search` as your primary search tool and `mcp__duckduckgo__fetch_content` to read pages from results. Run at least 10 to 15 different queries to cover your angle thoroughly, including the seed patterns for your angle. If duckduckgo fails for a query, fall back to `mcp__zai-web-search__web_search_prime` and `mcp__web_reader__webReader`. Never use the built-in web search tool; it returns 400 errors in this environment.

Corroborate before claiming: a demand claim backed by a single source is unverified. Label single-source claims as unverified or drop them.

Voice: before writing, read .Resources/voice.md (from the repo root) and follow its register and hygiene rules; they apply to research files too, not only book manuscripts. In practice that means no em or en dashes, no hype language, sentence case headings, and money figures in the form "$N billion" with the dollar sign attached.

Be exhaustive. The quality of the final recommendation depends entirely on the depth of your research.
```

## Agent output format

Each agent writes findings to `.research/next-books/<RUN>/<NN>-<domain>.md`:

```markdown
# Next books research: <angle>

Research date: <today's date>
Agent: <angle name>

---

## Methodology

Brief description of search queries used and sources consulted.

---

## Top candidates

### 1. <Company name> (<Ticker>)

**Demand signal:** <high/medium/low>
**Why now:** <specific catalyst or reason>
**Evidence:**
- <specific data point with source>
- <specific data point with source>
- <specific data point with source>

**Reader profile:** Who would buy a deep-dive book on this company
**Suggested angle:** What makes this book different from available content

### 2. <Company name> (<Ticker>)
...

---

## Extended list

Brief entries for companies ranked 6 to 25 with one-line justification each.

---

## Sources

List all URLs and publications consulted.
```

The format matters downstream: phase 2 counts an angle for a company only when the company appears as a numbered top candidate or an extended-list entry, so keep those two sections complete and explicit.

## Success criteria

- All angle files for the angles actually spawned exist in the current run's directory.
- Each file follows the structured format (methodology, top candidates, extended list, sources).
- Each file identifies 15 to 25 companies with specific evidence.
- Each file cites at least 5 distinct sources with URLs or publication names (this is the quality floor used in the handling section below).
- Single-source demand claims are labeled unverified or dropped.
- No duplicates with existing books in the repo.
- The artifact gates pass: zero hits for an em dash (`$'\xe2\x80\x94'`), an en dash (`$'\xe2\x80\x93'`), and non-Latin codepoints across the run directory's files.

Report back with the run directory path, the angle files created with their company counts, any angle that fell below the quality floor and how it was resolved, and confirmation that the artifact gates passed.

## Handling stuck, failed, or weak agents

Files from previous runs sit in their own dated directories and never mix with this run's; only files inside the current run's directory count.

1. **No wall-clock triggers.** Distinguish slow from failed by checking task status, not elapsed time. Long runtimes are expected when search tools return errors and agents fall back to MCP tools; a long-running agent is not a failed agent.
2. **Check stragglers after the others finish.** If an angle's agent is still running, wait for it; never spawn a second agent for an angle that already has a running agent. If an agent failed or exited without writing its file, stop it (TaskStop) if it still shows as active, then spawn exactly one replacement for that angle with the same prompt, writing to the same `.research/next-books/<RUN>/<NN>-<domain>.md` path. One active writer per file at all times.
3. **Quality floor.** An angle file is usable only if it identifies at least 15 companies and cites at least 5 distinct sources with URLs or publication names. If a written file falls below the floor, respawn that angle once with sharper queries; if the second attempt also falls below, keep the better of the two files and add a "thin coverage" note at the top so phase 2 discounts it.
4. **Phase 2 gate.** Start phase 2 only when every angle file for the angles actually spawned (6 to 8 per the spawn instruction) exists and meets the quality floor. If fewer than 5 usable files remain after the single respawn pass per missing angle, stop and ask the user to choose: respawn the missing angles again, proceed with partial coverage while naming the absent angles, or abort. Only the user's explicit choice may start phase 2 with fewer than 5 usable files.

Every angle must reach a terminal state (finished, failed and stopped, or respawned once) before consolidation begins, so phase 2 never reads a file that is still being written.
