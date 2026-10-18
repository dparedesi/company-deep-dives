# Business Model, Financial Performance & Health

## Palantir's core business model: software, services, and solutions

Palantir Technologies operates primarily as an enterprise software company, generating the vast majority of its revenue through the sale of subscriptions to its core platforms, Gotham, Foundry, and increasingly, the Artificial Intelligence Platform (AIP), along with associated services. The model is designed to embed Palantir's technology deeply within client operations, fostering long-term relationships and significant expansion potential.

**Revenue Streams:**

* **Software Subscriptions:** This is the primary and most strategic revenue source. Clients subscribe to Palantir's platforms, which can be deployed in various environments:
  * **Palantir Cloud:** Palantir hosts and manages the software in its own secure cloud environment, providing it as a Software-as-a-Service (SaaS) offering. This includes ongoing operations and maintenance (O&M).
  * **Customer-Hosted Environments (On-Premises or Private Cloud):** Clients can deploy Palantir's software within their own data centers or private cloud infrastructure. Palantir provides the software license and ongoing O&M. This flexibility, managed by Apollo, is crucial for many government and security-conscious commercial clients.
  * **Apollo as a Product:** Increasingly, Palantir offers Apollo itself as a commercial product, allowing customers to manage their own software applications with the same robust, multi-environment capabilities.
* **Professional Services:** While Palantir emphasizes its identity as a software product company, professional services have historically played a significant role, particularly in the initial "Acquire" and "Expand" phases of customer engagement. These services include:
  * **Platform Implementation & Integration:** Assisting clients in deploying the platforms and integrating them with their existing complex IT landscapes and data sources.
  * **Use Case Development & Customization:** Working with clients to identify high-impact use cases and configure/extend the platforms to meet specific operational needs.
  * **Training & Support:** Providing training for client personnel and ongoing technical support.
    The strategic intent is for software subscription revenue to constitute the dominant portion of total revenue, with services facilitating adoption and maximizing the value derived from the software, rather than being a primary profit center in itself.

**Customer Segments:** Palantir reports its revenue across two main customer segments:

* **Government:** This includes agencies of the United States federal government (Department of War, intelligence agencies, civilian agencies like HHS and CDC), as well as non-US governments (primarily allies). This segment has historically provided the bedrock of Palantir's revenue and is characterized by large, long-term contracts.
* **Commercial:** This includes enterprises across a wide range of industries such as manufacturing, energy, finance, healthcare, automotive, pharmaceuticals, and supply chain logistics. This segment, particularly in the US, has become the primary engine of growth in recent years.

By FY 2024, Palantir generated approximately $2.9 billion in revenue, with 55% from government customers and 45% from commercial clients, and two-thirds of revenue coming from the United States. This mix illustrates the company's dual engine: an entrenched government franchise and a rapidly scaling commercial business. The strategy is now unambiguously "software first, services as enabler," and the model has proved it can scale to multiple billions with high margins.

**AIP Revenue Mechanics**

AIP monetization combines classic enterprise licensing with usage-based billing for AI compute. Customers typically contract for platform access (Foundry, AIP, and often Gotham or Apollo) then pay for AI inference and agentic workflows based on compute usage, measured in tokens and compute-seconds. In practice, this looks like solution bundles: AIP for insurance underwriting, for hospital operations, or for retail store optimization, often layered on fixed platform commitments plus variable usage. AIP is increasingly packaged as vertical solutions (insurance, healthcare, manufacturing, retail) with pre-built workflows and ontologies, which makes the business model more solution-based than generic platform licenses.

The vertical packaging strategy represents a meaningful evolution from Palantir's earlier generic platform approach. Pre-built workflows and industry-specific ontologies reduce implementation time and accelerate the path to first value. Rather than selling a generic platform that requires extensive customization, Palantir now offers tailored solutions for specific industries, allowing faster deployment and clearer ROI demonstration. This shift has proven particularly effective in accelerating commercial adoption, as prospects can more easily envision how AIP would apply to their specific operational challenges.

Annual contract values for AIP deployments vary significantly by customer size and segment, but several patterns emerge from disclosed deals. Large commercial customers often start in the low seven figures for initial AIP deployments, with expansion contracts reaching eight figures as use cases proliferate across the enterprise. Government AIP contracts, while less numerous, tend to be larger and longer in duration, reflecting the procurement cycles and mission-critical nature of the work. The shift to consumption-based pricing with AIP creates a different revenue profile compared to traditional multi-year fixed contracts. Rather than recognizing revenue evenly over a contract term, Palantir now recognizes revenue that fluctuates with customer usage. This creates variability quarter to quarter but also enables faster revenue capture as customers accelerate their AI adoption.

Compute margins represent a critical economic consideration for AIP that differs from traditional software. Unlike pure software products where incremental costs are minimal, AI inference requires GPU compute that Palantir must purchase from cloud providers. The spread between what Palantir charges customers for compute and what it pays to hyperscalers constitutes a critical margin lever. Management has indicated that compute margins remain healthy even as AIP scales, partly because customers pay for outcomes rather than raw GPU hours. The ability to package compute within vertical solutions rather than selling raw inference as a commodity contributes to margin preservation. Customers pay for outcomes, underwriting automation or factory optimization, rather than for GPU hours directly. This outcome-based pricing insulates Palantir from the commoditization pressure that affects infrastructure providers.

The fixed-fee component of AIP contracts, typically tied to platform access, further stabilizes margins by providing a baseline of high-margin software revenue that is not correlated with compute costs. Large commercial customers often start in the low seven figures for initial AIP deployments, with expansion contracts reaching eight figures as use cases proliferate. Government AIP contracts tend to be larger and longer in duration, reflecting the procurement cycles and mission-critical nature of the work.

**AIP Pricing Tiers and Token-Based Economics**

Palantir has structured AIP pricing into distinct tiers that align with customer maturity and deployment scale. The entry-level AIP Spark offering provides organizations with a lower-friction path to experimentation, allowing teams to prototype AI workflows without committing to substantial platform contracts. As deployments prove successful and scale to production use cases, customers typically migrate to AIP Enterprise, which includes broader platform access, higher compute quotas, and expanded support. The largest enterprises and government agencies often negotiate custom engagements that combine multiple platforms with dedicated engineering resources and tailored service level agreements.

The token-based pricing model creates a direct correlation between usage intensity and revenue. Each AI inference operation, whether retrieving documents from a knowledge base, executing agentic workflows, or generating recommendations, consumes tokens that are billed to the customer account. This model aligns Palantir's economics with the value delivered, as customers actively using the platform pay proportionally more than those with dormant deployments. The consumption-based approach also creates expansion dynamics where successful implementations naturally drive increased usage and therefore revenue, creating a virtuous cycle within accounts.

**Marquee AIP Deployments**

To understand how the business model translates into real-world impact, consider two examples that illustrate the "land, then expand into workflows" pattern:

* Walgreens scaled an AIP/Foundry deployment from 10 stores to 4,000 in approximately eight months, reducing task times by roughly 30% and automating hundreds of billions of micro-decisions per day across store operations.
* AIG rebuilt its underwriting process on AIP, effectively multiplying underwriter capacity with reported productivity gains of two to five times, transforming a historically manual and time-intensive process into an AI-augmented workflow.

These deployments exemplify how initial platform adoption expands into mission-critical operational infrastructure, driving the high average revenue per customer and strong net retention rates that define Palantir's financial profile.

**AIP Boot Camp Economics**

The relationship between boot camps and revenue conversion operates as the primary engine of Palantir's commercial go-to-market motion. Boot camps function as both lead generation and product demonstration, compressing what traditionally required months of evaluation into days of intensive work. Prospects arrive with actual datasets and leave with working workflows, a dramatic departure from the slide-ware demos that characterize much of enterprise software sales. This product-led approach shortens sales cycles and improves conversion rates because prospects experience value rather than hearing about it.

The boot camp model also scales more efficiently than Palantir's traditional high-touch consulting approach. Rather than deploying Forward Deployed Engineers for months-long engagements, a single boot camp can serve multiple prospective customers simultaneously. The capital efficiency of this model is reflected in Palantir's sales and marketing economics, with revenue growth outpacing sales investment as the boot camp motion matures.

Boot camps operate as loss leaders in many cases, requiring Palantir to invest engineering time and compute resources before any contract is signed. The conversion rate from boot camp to paying customer is not disclosed, but the correlation between funnel activity and US commercial revenue growth suggests the funnel is efficient. US commercial revenue grew 93% year over year in Q2 2025, 121% in Q3 2025, and then 133% in Q1 2026 and 149% in Q2 2026, periods during which the funnel kept accelerating. Once converted, AIP customers often follow a familiar pattern: initial deployment in a single business unit or use case, followed by expansion to additional departments and workflows as value is demonstrated.

The funnel itself has evolved faster than the revenue it produces. By the Q2 2026 earnings call, Palantir had stopped headlining a boot camp count entirely; the quarterly counters of the 2023 and 2024 era, 324 and then 660, are dashboard history now. The motion runs through Agent Camps, per-customer conversion events that precede contracts, and through a new Sovereignty Bootcamp format that management said "exploded" with attendance from chief executives and operational leads, including partners that had gone dormant. Where the original boot camp converted one use case at a time, the Sovereignty Bootcamp sells the stack underneath an entire government or enterprise: models, data, and the hardware they run on, owned rather than rented.

The efficiency gains from the boot camp model represent a meaningful structural improvement in Palantir's go-to-market economics. Under the traditional consulting-heavy model, customer acquisition costs were substantial as Forward Deployed Engineers spent months on initial implementations before revenue materialized. Boot camps compress this timeline dramatically, with prospects often committing to six or seven-figure contracts within weeks of their initial workshop. This shortened sales cycle improves cash collection dynamics and reduces the working capital burden of supporting pre-revenue engagements.

## The "Acquire, Expand, Scale" go-to-market flywheel

Palantir's go-to-market (GTM) strategy, especially for large enterprise and government clients, has traditionally revolved around a three-phase model designed for deep engagement and long-term value creation:

* **Acquire Phase:** This initial phase focuses on getting a foothold in a new client organization. It often involves:
  * Pilot projects or proof-of-concept deployments on specific, high-value problems.
  * Significant upfront investment from Palantir, including the deployment of highly skilled Forward Deployed Engineers (FDEs) who work closely with the client.
  * Palantir may operate at a loss or minimal revenue during this phase, prioritizing demonstrated value and building trust over immediate financial return. The goal is to prove indispensable.
* **Expand Phase:** Once initial value is demonstrated and trust is established, the focus shifts to expanding Palantir's footprint within the organization. This involves:
  * Rolling out the platform to more users, departments, or business units.
  * Integrating additional data sources and tackling more complex use cases.
  * Revenue from the client begins to grow substantially. Contribution margins may still be developing as the scope of work increases.
* **Scale Phase:** In this mature phase, Palantir's platform becomes deeply embedded in the client's core operations, often becoming a critical piece of their infrastructure.
  * The platform is utilized extensively across the organization, driving significant operational efficiencies or new capabilities.
  * Revenue per customer is typically very high, and contribution margins are strong as the initial heavy investment in acquisition and customization is leveraged across a larger, recurring revenue stream.
  * Switching costs for the client become very high, leading to "sticky" long-term relationships.

**Evolution of GTM: AIP Boot Camps as the Core Commercial Motion**

Palantir's five-day AIP boot camps have evolved from an experimental tactic into the central pillar of the commercial go-to-market playbook. These intensive, short-duration (one to five days) workshops invite potential and existing customers to bring their own data and business problems to rapidly build and test AI-powered solutions using AIP.

* **Product-Led, Not Slide-Ware:** Prospects arrive with their actual datasets. Forward Deployed Engineers and product teams work alongside customer teams to build working workflows in days rather than months, demonstrating tangible value before any contract is signed.
* **Impact on Commercial Acceleration:** Management repeatedly credits boot camps and their descendants, the Agent Camps, with the surge in US commercial revenue, which grew 93% year over year in Q2 2025, 121% in Q3 2025, 133% in Q1 2026, and 149% in Q2 2026. The rapid ramp in US commercial customer count and remaining deal value traces directly back to this motion.
* **A Second Pillar, Sovereign AI:** Since 2026 the go-to-market has run on two engines. Boot camps convert commercial customers one workflow at a time; the sovereign AI stack, the Sovereign AI Operating System with NVIDIA reference architectures and certified modular data center partners, sells national-scale ownership of models, data, and hardware. Karp put the attribution plainly in the Q2 2026 earnings release: "demand for AI sovereignty has now been unleashed... The sovereign AI revolution makes us very optimistic." The same release raised FY2026 revenue guidance to approximately $8.2 billion, 82 percent growth, and sovereign demand was a named reason.
* **Scalable Deep Engagement:** Boot camps represent a shift towards more product-led growth while preserving Palantir's "deep engagement" DNA. They drastically reduce time to value, shorten sales cycles, and generate qualified leads and expansion opportunities more efficiently than the traditional high-touch consulting model.

## Deconstructing the cost structure

Palantir's cost structure reflects its dual identity as a high-growth software company with significant R&D needs and a historical element of intensive client engagement.

* **Cost of Revenue:**
  * Primarily consists of salaries, stock-based compensation (SBC), and benefits for personnel involved in providing ongoing operations and maintenance (O&M) for its platforms and delivering professional services.
  * Also includes third-party cloud hosting costs (for example, AWS, Azure, GCP) for Palantir's SaaS offerings, allocated overhead (like facilities and IT), and other direct costs associated with customer deployments.
  * Palantir has focused on improving its gross margin by productizing its offerings and managing hosting costs, aiming for software-like gross margins (which have consistently exceeded 80% in recent periods).
* **Operating Expenses:**
  * **Sales & Marketing (S&M):** Historically, S&M expenses were very high as a percentage of revenue, reflecting long and complex sales cycles, the cost of FDEs in the "Acquire" phase, and early investments in building out a direct sales force (which began in earnest around 2018-2019). With the success of AIP Boot Camps and a maturing commercial sales motion, the S&M margin (S&M as a % of revenue) is expected to decrease over time as revenue scales.
  * **Research & Development (R&D):** Palantir invests heavily in R&D to innovate and enhance its core platforms (Gotham, Foundry, Apollo, AIP), develop new features, and stay at the forefront of AI and data analytics. This is crucial for maintaining its technological differentiation. As revenue grows, R&D as a percentage of revenue is expected to provide leverage.
  * **General & Administrative (G&A):** Includes costs for executive management, finance, legal, human resources, and other corporate functions. Stock-based compensation has historically been a significant component of G&A.
* **Stock-Based Compensation (SBC):**
  * A notable aspect of Palantir's financials, particularly around the time of its IPO and in the initial years as a public company. SBC has been a significant expense impacting GAAP profitability.
  * While a non-cash expense (affecting net income but not directly impacting free cash flow), it does contribute to shareholder dilution.
  * Palantir has been working to manage SBC levels more predictably, and its impact as a percentage of revenue has been declining.
  * In FY 2024, stock-based compensation increased by approximately $216 million versus 2023, partly due to a $115.8 million one-time acceleration on market-vesting stock appreciation rights. A large portion of reported SBC in 2024 reflects one-off acceleration of legacy awards rather than the run-rate compensation structure for new hires, which somewhat distorts GAAP margins in the short term.

**SBC deep dive: the 2024 acceleration and insider selling**

Stock-based compensation has been a defining feature of Palantir's financial structure, reflecting both its Silicon Valley roots and the competitive landscape for engineering and data science talent. In the pre-IPO period, Palantir relied heavily on employee stock options and RSUs to attract talent while remaining private, creating substantial overhang that later manifested as SBC expense after the direct listing. As revenue has accelerated, dilution has become a shrinking side of the equation: equity grants continue, but the compensation structure has become more predictable and the expense is growing far slower than the top line.

**2024 One-Time Acceleration Event:**

The year 2024 marked a notable inflection in SBC reporting. The $216 million increase versus 2023 included a significant one-time component: $115.8 million in acceleration expense related to market-vesting stock appreciation rights. These awards, typically granted to executives and key employees, vest based on stock price performance rather than time. When Palantir's stock price surged in 2024, these awards accelerated, creating a one-time expense that does not reflect the ongoing run-rate compensation structure. This dynamic is important for investors to understand, as the 2024 SBC figure likely overstates the recurring compensation expense relative to future periods.

The market-vesting SARs acceleration represents a quirk of Palantir's compensation structure that emerged during the pre-IPO period. As a private company, Palantir used these performance-based awards to align employees with long-term value creation. The substantial stock price appreciation following the AIP launch triggered accelerated vesting, creating a temporary spike in SBC expense that is not expected to recur at similar magnitude.

**10b5-1 Trading Plans and Insider Selling Patterns:**

Insider ownership remains significant at approximately 6-7% of shares outstanding, with founders and early investors maintaining substantial positions. This alignment of management and shareholder interests is often viewed positively by long-term investors. However, insider selling activity through 2026 drew investor attention. CEO Alex Karp's 10b5-1 trading plan, with a ceiling of approximately $1.2 billion, represents a planned diversification strategy, but it operates at a time when the stock trades at premium valuations.

A 10b5-1 trading plan is a pre-arranged plan for selling stocks that allows corporate insiders to sell shares at a predetermined time, allowing them to avoid accusations of trading on nonpublic information. These plans are typically established during periods when the insider is not in possession of material nonpublic information and are designed to provide liquidity for diversification or estate planning purposes. However, the timing and scale of Palantir insider selling has drawn scrutiny from investors.

**Detailed Insider Selling Activity:**

The trailing twelve months through October 11, 2026 put the scale beyond debate: insiders sold $868.71 million of stock, 5.89 million shares across nine insiders, with zero open-market purchases on the other side of the ledger. Peter Thiel's $289.7 million sale of 2 million shares on March 2, 2026 was the largest single line, and Karp added an $86 million sale on August 20, six insiders sold roughly $95 million in August alone, and Stephen Cohen, Shyam Sankar, Ryan Taylor, and Matthew Glazer all participated across the period.

The breadth of insider selling across multiple executives, rather than being concentrated in a single individual, contributed to investor concerns about whether management viewed the stock valuation as sustainable. While such selling can reflect normal diversification and pre-planned trading programs, and much of Karp's August sale covered tax withholding on vesting RSUs, the scale at a premium valuation has drawn investor attention as a potential risk signal. The company's strong free cash flow generation provides flexibility to fund both organic growth and shareholder returns even with ongoing SBC, but investors will continue to monitor the balance between employee compensation needs and shareholder dilution.

**Balance Sheet Strength:** At the end of FY2025, Palantir maintained approximately $7.2 billion in cash, equivalents, and short-term US Treasuries with only approximately $229 million in debt. By Q2 2026 the position had grown to $9.2 billion, with more than $2.1 billion of adjusted free cash flow generated in the first half of 2026 alone and no evidence of equity issuance diluting the source of the build.

**Operating Leverage Emerging**

The cost structure that once made Palantir look like a consulting-heavy hybrid now increasingly behaves like a mature software company. In Q2 2025, the company reported approximately $1.0 billion in quarterly revenue (a milestone first), with GAAP operating margin around 27%, adjusted operating margin approximately 46%, and Rule of 40 around 94. By Q3 2025, GAAP operating margin reached roughly 33% and GAAP net income margin approximately 40%, with Rule of 40 above 110. For the full year FY2025, the company delivered gross margins of approximately 82%, EBIT margins near 32%, and net income margins of approximately 36%. Then 2026 broke the scale of the comparison: Q1 2026 printed a Rule of 40 of 145, and Q2 2026 printed 155, the twelfth consecutive quarterly expansion, on 93 percent revenue growth with a 47 percent GAAP operating margin and a 62 percent adjusted operating margin. Palantir is combining hypergrowth revenue with GAAP operating margins most software companies never reach at any growth rate, a level usually reserved for the strongest cloud franchises at a fraction of this growth.

## Financial performance review: the journey to profitability and growth

Palantir's financial narrative is one of transformation from a high-growth, loss-making private entity to a publicly traded company demonstrating sustainable profitability and accelerating growth. The AIP-driven commercial re-acceleration in 2024 and 2025 represents a pivotal chapter in this story.

### From $595 million to $4.5 billion: the revenue journey

Palantir's revenue trajectory from fiscal year 2018 through fiscal year 2025 represents one of the more remarkable growth stories in enterprise software. The journey from $595 million in annual revenue to approximately $4.5 billion spans seven years and encompasses three distinct phases: steady pre-IPO expansion, post-listing deceleration as the company navigated public market scrutiny, and a dramatic post-2023 re-acceleration driven by artificial intelligence platform adoption.

**Historical Revenue Growth:**

* 2018: $595 million
* 2019: $743 million (25% year over year)
* 2020: Approximately $1.1 billion (47% year over year)
* 2021: Approximately $1.5 billion (41% year over year)
* 2022: Approximately $1.9 billion (24% year over year)
* 2023: Approximately $2.2 billion (17% year over year)
* 2024: $2.9 billion (approximately 29% year over year)
* 2025: Approximately $4.5 billion, roughly 56% year over year growth versus 2024, exceeding a guidance range of approximately $4.4 billion after three consecutive raises.

The pre-IPO period established the foundation. In fiscal year 2018, Palantir generated approximately $595 million in revenue. The following year, 2019, revenue reached $743 million, representing 25 percent year-over-year growth. This period was characterized by deep government contract penetration and the early stages of commercial expansion. The company was still private, operating with the luxury of focusing on long-term contract development rather than quarterly earnings guidance. Government revenue dominated this period, with the United States military and intelligence community providing the bedrock of recurring revenue through multi-year contracts for Gotham deployments.

Fiscal year 2020 marked a significant inflection point. Revenue reached approximately $1.1 billion, representing 47 percent year-over-year growth and pushing Palantir past the billion-dollar annual revenue milestone. This was the year Palantir completed its direct listing on the New York Stock Exchange in September 2020, at a $7.25 reference price. The pandemic year proved unexpectedly favorable for Palantir as government agencies sought data integration capabilities for crisis response and commercial enterprises accelerated digital transformation initiatives.

The post-IPO period began with continued momentum. Fiscal year 2021 delivered approximately $1.5 billion in revenue, 41 percent growth over 2020. This growth rate, while robust, represented a deceleration from the prior year's 47 percent, a pattern that would concern investors in subsequent years. Government revenue continued to provide stability, with large defense and intelligence agency renewals underpinning the top line. Commercial revenue began gaining traction but faced headwinds as Palantir rebuilt its direct sales force and adjusted to public company operating cadences.

Fiscal year 2022 marked the low point of Palantir's growth trajectory. Revenue reached approximately $1.9 billion, representing 24 percent year-over-year growth. This further deceleration from 41 percent to 24 percent raised questions about whether Palantir could sustain expansion as its government contracts matured and commercial execution proved challenging. Government revenue grew but at a measured pace, while commercial revenue faced macroeconomic headwinds including rising interest rates and enterprise caution on large software commitments.

Fiscal year 2023 proved to be the inflection point that reversed this narrative. Revenue reached approximately $2.2 billion, representing 17 percent year-over-year growth. While this represented yet another deceleration from the prior year's 24 percent, the more significant story was on the profitability line. Palantir achieved its first full year of GAAP profitability with $210 million in net income. More importantly, 2023 marked the launch of the Artificial Intelligence Platform (AIP) in April, a product introduction that would catalyze the growth re-acceleration to follow.

Fiscal year 2024 demonstrated the first fruits of the AIP strategy. Revenue reached $2.9 billion, representing 29 percent year-over-year growth. This marked the first acceleration in annual growth since going public, reversing the multi-year deceleration pattern. Net income reached $462 million, a 120 percent increase over 2023 and representing a 16 percent net margin. The government segment generated approximately $1.6 billion, or 55 percent of total revenue, while commercial reached approximately $1.3 billion, or 45 percent.

Fiscal year 2025 delivered the full flowering of the AIP-driven transformation. Revenue reached approximately $4.5 billion, representing 56 percent year-over-year growth. This marked the highest growth rate since going public and occurred from a much larger base, defying conventional scaling dynamics. Net income reached $1.6 billion, a 253 percent increase over 2024 and representing a 36 percent net margin. The Rule of 40 exceeded 100, a level typically achieved only by the most exceptional software franchises. Free cash flow reached approximately $2.1 billion, representing a 47 percent margin.

**What makes this trajectory noteworthy is not merely the compound growth rate but the way growth accelerated rather than decelerated as the revenue base expanded.** In 2025, Palantir achieved 56 percent year-over-year growth from a multi-billion dollar base, its highest growth rate since going public and a figure that defies the typical scaling dynamics where growth slows as companies mature. The compound annual growth rate from 2020 through 2025 approximates 33 percent, placing Palantir among the top-tier growth companies in enterprise software. The 17 percent growth in 2023 represented a low point, followed by 29 percent in 2024 and 56 percent in 2025, a pattern of accelerating growth from an expanding base that is rare in enterprise software.

**The quarterly progression reveals the accelerating momentum more precisely.** In the first quarter of 2023, Palantir generated approximately $491 million in revenue with modest year-over-year growth. By the fourth quarter of 2023, quarterly revenue reached approximately $608 million. The April 2023 AIP launch began showing results in the second half of the year. In the first quarter of 2024, revenue reached approximately $634 million. The second quarter of 2024 delivered approximately $678 million. The third quarter of 2024 reached approximately $726 million. The fourth quarter of 2024 achieved approximately $826 million, with GAAP net income of $79 million representing a 10 percent margin and US revenue up 52 percent year over year.

The acceleration intensified in 2025. The first quarter of 2025 delivered approximately $875 million in revenue. The second quarter of 2025 marked a milestone with approximately $1.0 billion in quarterly revenue, the first time Palantir achieved a billion-dollar revenue quarter. GAAP operating margin reached approximately 27 percent, adjusted operating margin approximately 46 percent, and Rule of 40 around 94. GAAP earnings per share reached $0.13 with record net income. The third quarter of 2025 demonstrated further acceleration with approximately $1.2 billion in quarterly revenue. GAAP operating margin reached approximately 33 percent, GAAP net income margin approximately 40 percent, and Rule of 40 above 110.

Then 2026 made the 2025 acceleration look like a warm-up. The first quarter of 2026, reported May 4, delivered approximately $1.6 billion in revenue, up 85 percent year over year and the fastest growth since the 2020 direct listing. US commercial revenue rose 133 percent to $595 million, and total US revenue rose 104 percent to approximately $1.3 billion, the first triple-digit US growth since the direct listing. The second quarter, reported August 3, delivered approximately $1.9 billion, up 93 percent, with US commercial up 149 percent to $764 million and US government up 90 percent to $809 million. GAAP net income crossed $1 billion in a single quarter for the first time, approximately $1.1 billion at a 55 percent margin, and adjusted free cash flow crossed the same line at approximately $1.2 billion. First-half 2026 revenue reached approximately $3.6 billion, up 89 percent, an acceleration curve that runs from 63 percent growth in Q3 2025 to 85 to 93 percent in the first half of 2026, eleven straight quarters of accelerating growth.

**Revenue Guidance Evolution:**

Palantir's approach to revenue guidance has evolved from conservatism to increasing confidence as the AIP growth engine matured. In fiscal year 2023, guidance was cautious as the company navigated the post-IPO transition and the early stages of AIP launch. By 2024, guidance began reflecting the emerging momentum, with management raising expectations throughout the year as boot camp conversions exceeded internal projections. The 2025 guidance evolution proved particularly telling. Management initially provided a range that was ultimately exceeded, then proceeded to raise guidance three separate times during the year as AIP demand continued to surprise to the upside.

Fiscal 2026 compressed the pattern into a single year. The initial guide on February 2, 2026 was approximately $7.2 billion. The May 4 raise took it to approximately $7.7 billion. The August 3 raise took it to approximately $8.2 billion, 82 percent growth for the full year, alongside US commercial guidance of at least $3.4 billion, up 134 percent, and adjusted free cash flow guidance of $4.5 to $4.7 billion, itself raised twice from an initial $3.9 to $4.1 billion.

The scorecard against the Street is one-sided. In April 2026, analyst consensus for FY2026 revenue stood at approximately $7.3 billion; two reported quarters later, the company's own guide was approximately $8.2 billion, meaning April's consensus ran roughly 12 percent low, and the August raise was the third consecutive quarterly raise. The same chase is running ahead of 2027: FY2027 consensus has moved from approximately $10.4 billion toward roughly $11.9 billion, with consensus EPS of $2.35, up from $2.09 ninety days earlier.

The pattern of conservative guidance followed by raises and beats has contributed to investor confidence and multiple expansion. When management consistently under-promises and over-delivers, the market rewards the reliability of execution by applying higher valuation multiples. However, this dynamic also creates expectations for continued outperformance, raising the bar for future quarters. Any failure to maintain the guidance raise and beat pattern could trigger multiple compression even if absolute performance remains strong.

### Segment revenue dynamics: government and commercial evolution

The government versus commercial split evolution tells a strategic story. In the early years, government revenue dominated, often exceeding 60 percent of total revenue. This reflected Palantir's origins in defense and intelligence work, with Gotham deployments across the Department of Defense, intelligence agencies, and civilian agencies like Health and Human Services and the Centers for Disease Control and Prevention. Government revenue provided stability through long-term contracts, high security clearances, and mission-critical deployments that created significant switching costs. However, government growth was inherently constrained by budget cycles, procurement processes, and the finite nature of defense spending.

**Government:** Remains a large and stable contributor. For FY 2024, government revenue was approximately $1.6 billion (55% of total). For FY 2025, government revenue reached approximately $2.5 billion, maintaining roughly 55% of total revenue. The segment re-accelerated in 2026: US government revenue grew 84 percent in Q1 and 90 percent in Q2, reaching $809 million in the quarter. The obligations data shows how much runway remains. As of October 2026, the Army's consolidated enterprise agreement had obligated 17 percent of its $10 billion ceiling, approximately $1.8 billion, roughly 12 percent of the way through its ten-year performance period, against a US government business already running at $809 million per quarter. Budget-line visibility is arriving as well: the Pentagon's fiscal 2027 request includes more than $2 billion for CJADC2 efforts centered on the Maven Smart System, putting Palantir's flagship program inside the appropriations text rather than surviving on periodic task orders.

The strategic pivot toward commercial revenue gained urgency as Palantir prepared for its public listing and investors sought growth beyond the government franchise. Commercial revenue represented the primary growth vector but proved challenging to scale initially.

**Commercial:** The primary growth engine, driven by AIP adoption. For FY 2024, commercial revenue was approximately $1.3 billion (45% of total). For FY 2025, commercial revenue reached approximately $2.0 billion, maintaining roughly 45% of total revenue while growing faster than government.

**US Commercial: The Main Rocket**

US commercial has become the standout segment, with the boot camp funnel and its Agent Camp descendants translating directly into customer acquisition and revenue growth:

* Q2 2025: US commercial revenue grew 93% year over year to $306 million.
* Q3 2025: US commercial revenue surged 121% year over year to approximately $397 million, representing around three-quarters of total commercial revenue that quarter.
* Full-year 2025: US commercial reached approximately $1.4 billion, at least 104% year over year growth.
* Q1 2026: US commercial revenue grew 133% to $595 million, on 615 US commercial customers and net dollar retention of 150 percent.
* Q2 2026: US commercial revenue grew 149% to $764 million, on a record $2.1 billion of US commercial total contract value booked in the quarter, up 153 percent, $6.2 billion of US commercial remaining deal value, up 124 percent, 653 customers, and net dollar retention of 157 percent.

The AIP boot camp model, intensive workshops where prospective customers brought their own data and business problems to build working AI workflows in days rather than months, proved to be the breakthrough. This product-led motion dramatically shortened sales cycles and demonstrated tangible value before contract signature. The 2026 bookings records carry a named deal ladder behind them: a multinational technology company converted to a three-year expansion worth nearly $370 million in Q2 2026, a global asset manager signed a $35 million three-year deal, a nonprofit health system converted a pilot into $37 million of total contract value, and a global software company signed a $15 million five-month contract right after an Agent Camp. Expansion, not just acquisition, is doing the heavy lifting: the 150 and then 157 percent net dollar retention prints mean the installed base alone added half again to its revenue in a year.

**International commercial revenue has faced relative headwinds.** While the United States commercial segment has delivered triple-digit growth, international commercial has lagged. This reflects several factors including more stringent data sovereignty regulations in Europe, different procurement cultures in Asia-Pacific, and the concentration of Palantir's go-to-market resources in the domestic market. By Q2 2026 the United States accounted for 81 percent of total revenue, leaving international at roughly $362 million for the quarter, growing around one-third as fast as the US: international commercial revenue rose 26 percent year over year in Q2 2026 while US commercial rose 149 percent. Management has indicated international commercial expansion as a priority, but the execution has proven more challenging than the domestic surge.

**International vs Domestic: Geographic Revenue Split Evolution**

The geographic distribution of Palantir's revenue tells an important story about where the company has succeeded and where challenges remain. The United States has consistently delivered the strongest growth, driven by both government spending on defense and intelligence platforms and the surge in commercial AIP adoption. By 2025, the US accounted for roughly two-thirds of total revenue, up from roughly 60% in earlier years, and by Q2 2026 the share had reached 81 percent, a concentration level that makes the entire financial story an American story.

European commercial growth has faced structural headwinds that extend beyond simple execution challenges. The General Data Protection Regulation (GDPR) and various national data sovereignty laws create complexity for cloud-based AI platforms that process sensitive corporate information. European enterprises, particularly in financial services and healthcare, often prefer on-premises deployments that require more complex implementation. Additionally, European procurement cultures tend to be more risk-averse and committee-driven, extending sales cycles compared to the more rapid decision-making typical of US enterprises.

Asia-Pacific presents a different set of challenges. While government opportunities exist, particularly among US allies seeking to modernize defense capabilities, commercial adoption has been slower. Cultural differences in data sharing, strong local cloud incumbents, and varying regulatory approaches to AI have created a more complex expansion environment. Palantir has made investments in the region, but revenue contribution remains modest relative to North America and Europe.

The concentration of growth in the US market creates both opportunity and risk. On the positive side, the US commercial market represents the largest single enterprise software market globally, and Palantir's early success there creates a defensible position. The government franchise provides additional stability and cross-selling opportunities. However, geographic concentration also creates vulnerability if US economic conditions deteriorate or if defense spending faces headwinds. Diversifying international commercial growth remains a strategic priority but one that has proven difficult to execute.

### The path to profitability: from losses to strong margins

The path to profitability represents a parallel narrative to the revenue journey. From 2019 through 2022, Palantir posted substantial annual losses of approximately $1.2 billion in 2020, $520 million in 2021, and $374 million in 2022. These losses reflected heavy investment in research and development, sales and marketing, and the pre-IPO compensation structure that included significant stock-based compensation.

**Profitability Inflection:**

Palantir achieved its first full year of GAAP operating profitability in 2023, and the trajectory has steepened since:

* 2023: $210 million in net income (first full year of GAAP profitability), representing approximately 9.4% net margin
* 2024: $462 million in net income, representing a 120% year-over-year increase and 16.1% net margin
* 2025: $1.6 billion in net income, representing a 253% increase over 2024 and 36.4% net margin

Operating margins tell the story of operating leverage. Operating margins turned positive in 2023 at approximately 5.4 percent, expanded to approximately 10.8 percent in 2024, and reached approximately 32 percent in 2025. This rapid margin expansion reflects the fixed-cost nature of software businesses where incremental revenue flows largely to the bottom line. The profitability transition was achieved without sacrificing growth investment. R&D spending increased from $387 million (2021) to $508 million (2024), while sales and marketing investment continued to expand.

**Quarterly profitability milestones:**

* Q4 2024: GAAP net income of $79 million (10% margin), with US revenue up 52% year over year.
* Q2 2025: GAAP earnings per share of $0.13 and record net income, with Rule of 40 around 94.
* Q3 2025: GAAP net income of approximately $476 million (40% margin) and Rule of 40 above 110.
* Q1 2026: GAAP net income of $871 million (53% margin), GAAP earnings per share of $0.34, adjusted earnings per share of $0.33 against $0.28 expected.
* Q2 2026: GAAP net income above $1 billion in a quarter for the first time, approximately $1.1 billion at a 55% margin, with adjusted earnings per share of $0.41 against $0.35 expected.

The company is no longer in the "profit optional" phase. By Q2 2026, Palantir was delivering 93 percent revenue growth while converting 55 cents of every revenue dollar into GAAP net income, a combination with no precedent among large enterprise software players.

### Free cash flow generation

Free cash flow generation has paralleled the profitability transformation. After declining from $321 million in 2021 to $184 million in 2022 due to working capital movements, free cash flow reached $697 million in 2023, $1.1 billion in 2024, and approximately $2.1 billion in 2025. The 2025 free cash flow represents a 47 percent margin, placing Palantir among the most profitable software companies globally. Operating cash flow followed a similar trajectory, reaching approximately $2.1 billion in 2025 with operating cash flow as a percentage of revenue expanding from 22 percent in 2021 to 48 percent in 2025.

The consistency between operating cash flow and free cash flow demonstrates that Palantir generates cash with minimal capital expenditure requirements, typical of enterprise software companies. Capital expenditures have remained modest, ranging from $13-40 million annually.

**Quarterly free cash flow:**

* Q2 2025: Adjusted free cash flow of approximately $569 million (57% margin).
* FY 2025 Guidance: After Q2 2025, management raised adjusted free cash flow guidance to approximately $1.8 to $2.0 billion. Following Q3 2025, guidance moved up again to $1.9 to $2.1 billion for the full year.
* Q1 2026: Adjusted free cash flow of $925 million (57% margin).
* Q2 2026: Adjusted free cash flow of approximately $1.2 billion (63% margin), the first quarter above $1 billion, bringing first-half 2026 adjusted free cash flow above $2.1 billion.
* FY 2026 Guidance: Adjusted free cash flow of $4.5 to $4.7 billion, raised twice from an initial $3.9 to $4.1 billion.

Free cash flow and operating cash are now comfortably ahead of equity-based compensation, a meaningful milestone for a company that historically relied heavily on stock-based compensation.

### Rule of 40 performance

Rule of 40 performance provides a composite view of growth and margin efficiency, and Palantir has emerged as an exceptional performer on this metric. The Rule of 40 calculates revenue growth rate plus profit margin, typically using free cash flow margin or adjusted EBITDA margin. Scores above 40 indicate healthy software companies, while scores above 60 indicate exceptional performers.

Palantir's Rule of 40 score has accelerated from approximately 55 in 2023 to above 100 in 2025, and then out of the chart's range entirely: 145 in Q1 2026 and 155 in Q2 2026, the twelfth consecutive quarterly expansion. In Q2 2025 the score stood at approximately 94, built from 48 percent revenue growth plus a 46 percent adjusted operating margin. A year later, growth alone, at 93 percent, exceeded what most companies on the chart manage on growth plus margin combined.

Achieving such scores at multi-billion dollar revenue scale is unusual, as most software companies see their Rule of 40 scores decline as they grow larger. Palantir's improving score at increasing scale suggests strong competitive positioning and widening moats. The Rule of 40 performance also validates the AIP strategy, demonstrating that the shift to consumption-based pricing has not compromised margins. Palantir is combining growth rates typical of early-stage companies with margins typical of mature software franchises, a combination that defines top-tier software businesses.

## Key customer metrics and operational efficiency

**Customer Count Growth:** Particularly strong in the US commercial segment, reflecting the success of AIP boot camps, Agent Camps, and the product-led motion. US commercial customer count has expanded from approximately 100 at AIP's launch to 653 by Q2 2026, a six-fold increase, and total customer count reached 1,007 in Q1 2026, up 31 percent year over year. International commercial customer growth has lagged, contributing to the relative underperformance of international commercial revenue compared to US commercial. Government customer count has grown more slowly, which is expected given the longer sales cycles and smaller total addressable market of government agencies versus commercial enterprises.

**Net Dollar Retention (NDR):** A key SaaS metric indicating revenue growth from existing customers, and one where Palantir's reported figures have outrun the standard playbook. A healthy enterprise software figure sits near 110 to 120 percent. Palantir stopped describing a typical range as growth accelerated: the company-reported figure was 150 percent in Q1 2026 and 157 percent in Q2 2026, meaning the existing customer base alone generated half again more revenue year over year before any new customer acquisition counted. Palantir does not disclose a segment breakdown of the metric, so commercial-versus-government splits circulating in analyst commentary are estimates, not company data.

The scale of that retention number changes what land-and-expand means here. At 157 percent, expansion inside the installed base compounds faster than most software companies grow in total. The AIG deployment exemplifies the mechanism, with the insurer rebuilding its underwriting process on AIP and effectively multiplying underwriter capacity with reported productivity gains of two to five times. Such transformative deployments create their own expansion momentum as successful use cases catalyze adoption across additional business units, and the deep data integration underneath them creates switching costs that hold regardless of customer type.

**Customer Concentration:** Concentration has improved significantly over Palantir's history. In the early years, a small number of government contracts represented a substantial portion of revenue. By 2025, no single customer accounted for more than 3% of total revenue, according to company disclosures. This diversification reduces risk and provides more predictable revenue as individual contract renewals or losses have diminished impact on overall results.

The top 10 customers now represent a smaller percentage of revenue than in the early 2020s, even as absolute customer count has grown. Government revenue concentration remains higher than commercial concentration given the nature of defense and intelligence contracting, where individual programs can reach hundreds of millions of dollars. However, even within government, Palantir has broadened its customer base across more agencies and international allies, mitigating the risk associated with any single government budget cycle. Commercial revenue concentration has decreased particularly rapidly as the customer base expanded from approximately 100 to more than 650 customers in the US alone. The growth in customer count combined with stable or increasing average deal size indicates that Palantir is successfully penetrating smaller mid-market customers while maintaining its presence among large enterprises.

**Deal Value by Segment and Size:**

Significant deal momentum has emerged, with large contracts becoming more frequent as AIP deployments scale. Deal sizes vary substantially by customer segment and deployment scope. Government contracts typically range from tens of millions to hundreds of millions of dollars for multi-year implementations spanning multiple agencies or extensive military programs. These contracts often include classified work requiring specialized facilities and cleared personnel, creating barriers to entry for competitors.

Commercial deal sizes show more variance. Large enterprises undertaking digital transformations often commit to eight-figure contracts as they roll out AIP across multiple business units and geographies. Mid-market companies typically start in the six to low seven-figure range for initial deployments, with expansion opportunities as use cases prove successful. The distribution of deal sizes creates a healthy revenue mix where commercial customers provide growth and volume while government customers provide stability and high-value contracts.

Average deal size has been increasing as AIP deployments expand in scope. Initial boot camp conversions might generate contracts in the hundreds of thousands, but successful implementations often lead to expansion contracts three to five times larger as additional workflows are automated and more business units adopt the platform. This expansion dynamic, reflected in the strong NDR metrics, drives increasing average revenue per customer over time.

**Notable Churn:** BP, the energy giant, represents a publicly cited customer loss when the company ended its Palantir engagement in 2023 following a multi-year deployment. The BP case illustrates several risk factors: high pricing can become difficult to justify during corporate cost-cutting, and some customers may attempt to build internal capabilities rather than paying for external platforms. The energy sector has also developed competing platforms that can siphon away potential customers. However, BP appears to be an exception rather than the rule. Palantir's disclosed churn rates remain significantly below typical SaaS benchmarks, with many customers maintaining relationships for five, seven, or even ten years. The combination of deep data integration, custom ontologies, and mission-critical workflows creates substantial switching costs that protect against churn. Even when customers reduce spending or pause expansions, existing relationships often continue rather than ending completely. The government customer base shows particularly low churn given the mission-critical nature of defense and intelligence work, where changing platforms would require re-certification and substantial operational disruption.

**Average Revenue Per Customer:** High, especially for top-tier clients, reflecting the deep integration of Palantir's platforms into customer operations. The average government deal size significantly exceeds the average commercial deal size, with individual government contracts often reaching tens or hundreds of millions of dollars.

## Balance sheet strength and cash flow analysis

Palantir maintains a fortress balance sheet that provides substantial strategic flexibility.

**Cash Position:** At Q2 2026, the company held $9.2 billion in cash, equivalents, and short-term US Treasuries against approximately $229 million in debt, up from approximately $7.2 billion at the end of FY2025.

The balance sheet has strengthened alongside revenue growth. Cash and short-term investments grew from approximately $2.6 billion in 2021 to $2.7 billion in 2022, $3.7 billion in 2023, $5.2 billion in 2024, and approximately $7.2 billion in 2025, then jumped to $9.2 billion by mid-2026 as first-half adjusted free cash flow above $2.1 billion poured in faster than the company could redeploy it; no equity issuance stands behind the build. This represents more than a 250 percent increase in cash position over five years, providing substantial strategic flexibility for acquisitions, buybacks, or continued investment. The company has maintained a conservative capital structure with minimal debt. Short-term debt has remained consistently low at approximately $45 million, while long-term debt has declined from $220 million (2021) to $183 million (2025). Total debt-to-equity ratio stands at approximately 6%, indicating minimal financial leverage.

Total assets have grown from approximately $3.3 billion (2021) to $8.9 billion (2025), reflecting the accumulation of cash and investments. Shareholders' equity has expanded from approximately $2.3 billion to $7.4 billion over the same period. The equity growth reflects both retained earnings (which have turned from cumulative deficits to strong positive territory) and the company's consistent profitability.

A notable feature of Palantir's balance sheet is its low capital intensity. Net property, plant and equipment has remained consistently around $230-270 million, despite significant revenue growth. This reflects the cloud-native nature of the platform and Palantir's strategy of leveraging public cloud infrastructure rather than owning data centers.

**Capital Allocation:**

Capital allocation remains conservative. Palantir has been buying back a modest amount of stock, with repurchases in the tens of millions per quarter during 2024 and 2025. At the same time, the company reinvests the vast majority of excess cash into short-dated US Treasuries, building a large financial asset base. This approach stabilizes the balance sheet but leaves open questions about whether more aggressive buybacks, dividends, or strategic acquisitions are warranted. The company has significant optionality but has not yet signaled a shift toward aggressive capital return.

One new instrument appeared in 2026: customer equity. A June 24, 2026 securities filing showed Palantir holding a reported 7.4 percent stake in Surf Air Mobility, the regional airline whose SurfOS operating system it powers, a stake taken alongside the platform deal rather than as a financial investment. If the pattern repeats, Palantir would be partially taking payment for its software in its customers' upside, a business model development worth watching; the Surf Air figure awaits confirmation against the SEC filing itself.

## Valuation considerations: the premium for growth and AI leadership

Palantir's stock valuation reflects the market's assessment of its position as an AI infrastructure leader, but the magnitude of the premium has made it one of the most debated names in the software sector. This chapter owns the business case on each side; the market multiples themselves live in Chapter 8, which holds the book's only valuation snapshot, dated October 16, 2026, when the stock closed at $186.03 with a market capitalization of $447 billion after a first half that erased 34 percent and an August-to-October rally that set records before correcting.

By any traditional metric, the valuation is extreme even by high-growth software standards. The market is effectively pricing Palantir as an AI infrastructure winner on par with the major hyperscalers. The achievement of GAAP profitability in 2023 and the 2025 to 2026 growth acceleration gave the multiples an earnings base to stand on, and the October 2026 snapshot in Chapter 8 works through what the price implies operationally. The debate this section settles is whether the business underneath can earn its way into those multiples.

**The Bull Case:**

* AIP is setting the agenda in enterprise AI, with boot camps, Agent Camps, vertical solutions, and reference customers across retail, healthcare, insurance, and manufacturing demonstrating real-world value creation.
* Revenue growth has re-accelerated to 85 and then 93 percent year over year in the first half of 2026 while the company converts 55 percent of revenue into GAAP net income, with a record $2.1 billion US commercial bookings quarter behind it.
* Sovereign AI has opened a second growth pillar beside the boot camp engine, one that sells national-scale infrastructure rather than single use cases, and the August 2026 guidance raise to approximately $8.2 billion is its first receipt.
* The combination of government stability and commercial hypergrowth creates a diversified revenue base with multiple expansion vectors.
* Deep technical moats (Ontology, Apollo, security certifications) create switching costs that protect the installed base.
* Rule of 40 performance at 155 in Q2 2026 places Palantir alone among software franchises at this scale.

**The Bear Case:**

* Valuation is priced for perfection, with multiple commentators arguing there is no rational reason to own the stock besides momentum at current levels.
* Heavy reliance on US government contracts exposes the company to macro uncertainty around defense budgets, even as commercial grows; the US is now 81 percent of revenue, concentrating both engines in one political system.
* Insider selling has a scale beyond the old diversification story: $868.71 million sold across nine insiders in the twelve months through October 11, 2026, with zero open-market purchases. While such selling can reflect pre-planned programs, and part of Karp's sale covered tax withholding, the scale and breadth at a premium valuation reads as a risk signal.
* International commercial growth, up just 26 percent in Q2 2026 against 149 percent in the US, raises questions about global scalability.
* AI commoditization could pressure pricing if competitors offer similar capabilities at lower cost.
* The compute margin structure could face pressure if hyperscaler GPU pricing increases or if customers demand more transparent pricing.

**A Valuation Sanity Check:**

A simple way to think about Palantir's valuation is to translate the premium multiple into operational expectations. At the October 16, 2026 price, the market is effectively underwriting that the 2026 acceleration, 93 percent growth with a 55 percent net margin, persists for years rather than normalizing, that the Rule of 40 stays far above 40, and that sovereign AI and the boot camp engine together keep compounding bookings at the record pace of Q2 2026. Any wobble in those metrics, or a slowdown in US commercial momentum, can drive sharp multiple compression, as the October selloff demonstrated in miniature. Chapter 8's October snapshot works the other direction: which of the book's scenarios the market price sits closest to, and what would have to be true for the price to be cheap.

## October 2026 snapshot

With two quarters of fiscal 2026 reported, the financial picture is no longer an inflection point; it is a company outrunning its own guidance:

* **Revenue:** Approximately $4.5 billion in FY2025 (56% growth) as history; first-half 2026 revenue of approximately $3.6 billion, up 89 percent; FY2026 guidance of approximately $8.2 billion, raised twice, with US commercial guided to at least $3.4 billion, up 134 percent.
* **Revenue mix:** The US at 81 percent of Q2 2026 revenue, with US commercial growing 149 percent and international commercial 26 percent.
* **Profitability:** First quarter above $1 billion of GAAP net income (Q2 2026, 55% margin); Rule of 40 at 155, the twelfth consecutive quarterly expansion.
* **Cash position:** $9.2 billion in cash and Treasuries at Q2 2026, against approximately $229 million in debt.
* **Free cash flow:** More than $2.1 billion of adjusted free cash flow in the first half of 2026; FY2026 guidance of $4.5 to $4.7 billion.
* **Next test:** The November 2 Q3 report, where Street consensus of roughly $2.2 billion already sits above the company's own guide, and management has warned of an expense ramp.

**Summary of Financial Trajectory:**

Palantir has successfully navigated a challenging path from a pioneering, mission-driven private company to a publicly traded entity demonstrating increasing financial discipline and a clear trajectory towards sustainable, profitable growth. The US commercial segment, powered by AIP, is currently its main growth engine. Strong gross margins, improving operating leverage, and robust free cash flow generation paint a picture of improving financial health. The ability to translate its technological prowess into consistent, scalable, and profitable growth across both its commercial and government segments globally will ultimately determine its long-term financial success and market standing.

The revenue journey reveals three strategic insights. First, the government franchise provided a stable foundation that funded commercial expansion without requiring external capital. Second, the AIP product launch coincided with enterprise AI adoption readiness, creating a timing advantage. Third, the boot camp go-to-market model proved highly effective at converting AI interest into deployed contracts, particularly in the United States market. The result is a company that transformed from unprofitable growth to profitable growth while simultaneously accelerating revenue expansion from a multi-billion dollar base. The first reading on whether the acceleration holds arrives November 2, against a Street bar already above the company's own guide.
