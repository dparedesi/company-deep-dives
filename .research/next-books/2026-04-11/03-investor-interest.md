# Next books research: investor and retail interest
Research date: 2026-04-11
Agent: investor interest
Excludes: Palantir (001-palantir), Rocket Lab (002-rocketlab), SanDisk (003-sandisk)

---

## Methodology

Four primary data sources were scraped on 2026-04-11:

1. **ApeWisdom** (apewisdom.com): Top 100 most-mentioned stocks across Reddit (r/wallstreetbets, r/stocks, r/investing, r/options, r/stockmarket). Provides mention counts and upvote totals. Captures real-time retail sentiment.
2. **Finviz most active** (finviz.com): Stocks sorted by absolute trading volume across 2 pages (40 stocks). Captures institutional + retail trading intensity.
3. **Finviz high relative volume screener**: Stocks with price >$10 and relative volume >2x, sorted by volume. Identifies momentum names with unusual activity.
4. **StockAnalysis most shorted** (stockanalysis.com): 100 most-shorted stocks by short % of float. High short interest signals controversy and bull/bear debate intensity.

Supplementary earlier data from Yahoo Finance trending tickers, MSN Money most active, and Seeking Alpha was also incorporated from a parallel research pass.

Limitations: Robinhood most-held list, 13F institutional filing aggregators, and options flow data were unavailable due to client-side rendering, paywalls, or API failures. Multiple WebSearch calls returned API errors. Some mcp__zai-web-search queries returned empty results.

---

## Top candidates (1-5 with full detail)

### 1. NVIDIA (NVDA)

**Demand signal:** high

**Why now:** Epicenter of the AI infrastructure buildout. Every earnings report is a market-moving event. Retail and institutional investors alike obsess over data center revenue guidance. The stock trades at extreme volume (407M shares/day was the single highest on Finviz most active) and dominates financial media coverage.

**Evidence:**
- #1 most active stock by volume on Finviz (407M shares, April 2026)
- 18 Reddit mentions with 1,328 upvotes in 24 hours (ApeWisdom)
- Dedicated leveraged ETFs (NVDL, NVDU) signal massive retail derivatives demand
- Constant analyst coverage with frequent price target revisions

**Reader profile:** AI-curious investors who want to understand the full stack: CUDA moat, data center economics, competitive threats from AMD/custom silicon, and whether the valuation is justified.

**Suggested angle:** "The AI Pickaxe" -- NVIDIA as the toll collector on the AI boom. Focus on whether the moat is real or whether custom silicon (Google TPU, Amazon Trainium, AMD MI300) erodes it. Every investor has an opinion; a deep-dive gives them the ammunition.

---

### 2. Tesla (TSLA)

**Demand signal:** high

**Why now:** Perpetual controversy machine. Bull/bear divide is as wide as any stock in the market. Robotaxi launch timeline, energy storage growth, and political overtones keep it in constant discussion.

**Evidence:**
- 115M shares daily volume (Finviz most active, #13 overall)
- 10 Reddit mentions with 903 upvotes in 24 hours (ApeWisdom)
- Multiple dedicated leveraged ETFs (TSL, TSLL, TSLT)
- Consistently among the most-discussed stocks on every retail platform

**Reader profile:** Investors who either love or hate Tesla and want a rigorous, ideology-free analysis. Both bulls (robotaxi, Optimus, energy) and bears (valuation, competition, Musk distraction) need the same factual foundation.

**Suggested angle:** "More than cars" -- Tesla as an energy, AI, and robotics company that happens to make vehicles. The bull case is the optionality; the bear case is that none of the optionality is proven. A balanced deep-dive is exactly what the market lacks.

---

### 3. Intel (INTC)

**Demand signal:** high

**Why now:** The defining turnaround story in semiconductors. Pat Gelsinger's departure and new leadership direction, foundry business ramp, and question of whether Intel can compete with TSMC. High volume and high debate.

**Evidence:**
- 138M shares daily volume (Finviz most active, #4 overall)
- 13 Reddit mentions with 1,339 upvotes in 24 hours (ApeWisdom)
- Deep value narrative attracting both value and contrarian investors
- Government CHIPS Act funding adds policy dimension

**Reader profile:** Contrarian and value investors looking at the most debated turnaround in tech. Also attracts semiconductor industry enthusiasts.

**Suggested angle:** "The comeback" -- whether Intel's foundry pivot can work, the economics of IDM 2.0, and whether this is a value trap or the trade of the decade. Nobody is neutral on Intel.

---

### 4. CoreWeave (CRWV)

**Demand signal:** high

**Why now:** Brand new IPO (March 2026), AI infrastructure pure-play, immediately shot to the top of most-active lists. The "NVIDIA of cloud" narrative is driving massive retail interest. This is the freshest story on the list.

**Evidence:**
- 83M shares daily volume (Finviz, #17 most active overall)
- 7 Reddit mentions with 2,300+ upvotes in 24 hours (ApeWisdom)
- $53.6B market cap within weeks of IPO
- Direct NVIDIA partnership (largest GPU cloud customer)

**Reader profile:** Investors chasing the next AI infrastructure winner. Wants to understand whether CoreWeave is a sustainable business or a leveraged GPU rental operation that collapses if demand slows.

**Suggested angle:** "The GPU landlord" -- CoreWeave's debt-fueled GPU acquisition model, dependence on NVIDIA, and whether cloud AI compute is a commodity or a moat. First-mover advantage in a brand new category.

---

### 5. Super Micro Computer (SMCI)

**Demand signal:** high

**Why now:** Accounting scandal, delayed filings, potential Nasdaq delisting, then dramatic recovery. The ultimate "is it fixed or not?" story. Extreme controversy drives extreme interest.

**Evidence:**
- 100M shares daily volume (Finviz most active, #16 overall)
- Among most-discussed stocks on Reddit for months running
- Dedicated leveraged ETFs exist (SMCU)
- Short interest remains elevated despite recovery

**Reader profile:** Investors who want to understand the server/HPC infrastructure layer and whether SMCI's accounting issues are fatal or a buying opportunity. High-risk, high-reward seekers.

**Suggested angle:** "Built to last or built to break?" -- The only company that can rival Dell/HPE in AI server deployments, but with a clouded governance history. Is the discount warranted?

---

## Extended list (6-25 with one-line justifications)

| # | Company | Ticker | Justification |
|---|---------|--------|---------------|
| 6 | Hims & Hers Health | HIMS | 32% short interest, $9.1B mcap, telehealth-to-compounding-pharma disruptor with fierce FDA/regulatory debate |
| 7 | Microsoft | MSFT | 100 Reddit mentions (#4 overall), enterprise AI infrastructure leader, Copilot revenue is the next earnings catalyst |
| 8 | ServiceNow | NOW | 44 Reddit mentions, $86.8B mcap, enterprise AI workflow adoption story, 58M shares daily volume |
| 9 | SoundHound AI | SOUN | 28% short interest, $5.7B mcap, voice AI narrative play with extreme retail following |
| 10 | MicroStrategy | MSTR | Bitcoin proxy with dedicated leveraged ETFs (MSTU), constant debate over premium to BTC holdings |
| 11 | Applied Digital | APLD | 32% short interest, $8B mcap, data center and AI cloud play attracting both growth and short sellers |
| 12 | Snowflake | SNOW | $41.9B mcap, 23M shares daily volume, cloud data platform pivoting to AI, high-profile CEO transition |
| 13 | Cloudflare | NET | $58.8B mcap, 13.7M shares daily volume, AI inference at the edge narrative, profitability turning point |
| 14 | Lucid Motors | LCID | 28% short interest, $5.7B mcap, EV challenger with Saudi backing, perpetual survival debate |
| 15 | Marvell Technology | MRVL | $112.4B mcap, 41M shares daily volume, custom silicon/AI networking play, high analyst coverage |
| 16 | Upstart | UPST | 34% short interest, $3.6B mcap, AI-driven lending platform, rate-cycle sensitivity creates bull/bear split |
| 17 | C3.ai | AI | 31% short interest, $2B mcap, pure-play enterprise AI, constant debate over whether revenue growth justifies valuation |
| 18 | Etsy | ETSY | 29% short interest, $5.6B mcap, marketplace turnaround story, activist investor involvement |
| 19 | Astera Labs | ALAB | $25.4B mcap, 10.9M shares daily volume, semiconductor connectivity for AI data centers, recent IPO momentum |
| 20 | TeraWulf | WULF | $5.4B mcap, high short interest, AI data center infrastructure play (nuclear-powered mining pivot) |
| 21 | Fastly | FSLY | 38.6M shares daily volume (-21.69% single-day drop), edge computing with extreme volatility attracting traders |
| 22 | CrowdStrike | CRWD | Cybersecurity leader with 42M+ volume sessions, AI-powered endpoint protection, Microsoft competition debate |
| 23 | Coinbase | COIN | Only public pure-play crypto exchange, Bitcoin ETF custody revenue, cycle-dependent but extreme retail interest |
| 24 | Dell Technologies | DELL | +21.93% on earnings, AI server demand flowing through, classic "old tech finds new life" narrative |
| 25 | Meta Platforms | META | 20 Reddit mentions, Llama open-source AI strategy, AR/metaverse investment debate, massive retail base |

---

## Sources consulted

1. ApeWisdom - Top 100 Reddit stocks (apewisdom.com/all) - scraped 2026-04-11
2. Finviz - Most active stocks screener, sorted by volume (finviz.com/screener.ashx?v=111&ft=4&o=-volume) - scraped 2026-04-11
3. Finviz - High relative volume screener, price >$10, rel vol >2x (finviz.com/screener.ashx?v=111&f=sh_price_o10,sh_relvol_o2&ft=4&o=-volume) - scraped 2026-04-11
4. StockAnalysis - Most shorted stocks (stockanalysis.com/list/most-shorted-stocks/) - scraped 2026-04-11
5. Yahoo Finance - Trending tickers (finance.yahoo.com/trending-tickers/) - accessed 2026-04-11
6. MSN Money - Most active stocks (msn.com/en-us/money/markets) - accessed 2026-04-11
7. Seeking Alpha - Market news and trending topics (seekingalpha.com/market-news) - accessed 2026-04-11
8. MarketBeat - Most followed stocks (marketbeat.com/stocks/most-followed/) - accessed 2026-04-11 (category page)

---

## Notes on data quality and limitations

- ApeWisdom data is a 24-hour snapshot; mention counts fluctuate daily but the top 20 names are remarkably stable week over week
- Finviz volume data is intraday and reflects a single trading session; however, the most-active list is consistent across multiple checks
- StockAnalysis short interest data updates semi-monthly; figures are approximate for mid-April 2026
- No direct access to Robinhood popularity rankings (client-side rendered), 13F institutional filing databases (paywalled), or options flow data (UnusualWhales paywalled)
- Reddit mention counts exclude private subreddits and Discord communities, which are significant for some stocks (GME, AMC)
- Several WebSearch API calls returned error 400; some mcp__zai-web-search queries returned empty results, limiting breadth of supplementary sources
