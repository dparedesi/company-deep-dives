# Voice charter

The single source of truth for the narrative voice of every book in this repository. Any agent that writes, edits, assembles, or reviews manuscript prose reads this file first, before writing a word, and follows it exactly. Skills reference the charter by path (`.Resources/voice.md`, from the repo root); they never restate its rules. It composes with the project CLAUDE.md writing conventions (no em dashes, sentence-case headings, acronyms uppercase, chapter files start with an H1, frontmatter has no H1), which stay in force. Quality and reliability gates live in `.Resources/quality-bar.md`.

The goal: every book reads like one author wrote it. A discerning reader who finishes one book and opens another must hear the same person. The register is a factual company analysis that reads like a bestseller: scenes, decisions, numbers that land, and a judgment the reader can disagree with.

## Who the author is on the page

An impersonal analytic author who evaluates companies and takes positions.

- "We" appears sparingly, and only for analytic stance and verdicts ("we present three scenarios"; "we land on the base case"). Never "I". The reader is addressed only to set boundaries, never chatted up.
- The book speaks to exactly one audience: the discerning reader evaluating the company. Never management ("strategic recommendations for the internal team"), never audience segments ("potential investors", "tailored to meet the informational needs of").
- Register: "this book" and "this analysis". Never "this report", "this document", "hereinafter referred to as", parenthetical legal disclaimers, or AI-generation disclosures.
- The book never describes its own depth, comprehensiveness, novelty, or effort. Any sentence that claims effort gets deleted; the effort reaches the reader as scene detail, number anchoring, and falsification frameworks.
- One short reader-covenant section per book is allowed, in the "What this book is not" form: direct refusals about the reader's interests, zero self-praise, zero legalese.
- Dry humor at low density is welcome, usually at an industry's or a product's expense (a chip that "earned the nickname '3D decelerator' from reviewers"; a name already claimed by a toilet paper manufacturer's trademark). Structural metaphors stay close to ones the companies themselves use ("AI factories", "who buys the shovels").

## Sentence and rhythm

- Manuscript-wide average sentence length: 16 to 22 words. No chapter average outside 14 to 24. Compute it with a script; do not eyeball it.
- The cadence is comma-heavy and mechanism-forward: subject, verb, mechanism, consequence. Stack clauses with commas, colons, parentheses, and occasional semicolons for paired judgments. Never with dashes of any kind.
- Explicit enumeration is a house habit: "First... Second... Third..." for argumentative moves.
- One-line dramatic paragraphs are allowed in narrative chapters, at most one per section ("What they did not have was a name.").
- No report connectives: "Having dissected X, we now turn to Y", "The following section examines", "as we saw above". Sections advance by argument, and the argument names what comes next and why it matters.

## Numbers

- Money is always "$N billion", "$N million", "$N trillion", with the dollar sign attached to the number ("approximately $4.48 billion"). The spelled-out pattern "N billion dollars" is banned everywhere, including the about page and release notes.
- Per-share and unit prices stay exact at any magnitude ("$207.52"). Aggregates above $1 billion get at most one decimal place, and "approximately" when the number is an estimate. Two-decimal precision on multi-billion aggregates ("215.94 billion") is false precision and is banned.
- Market-research projections get rounded to a magnitude the reader can hold ("roughly half a trillion by the early 2030s"). Never "$448.60 billion by 2030", and never the same projection stated twice.
- Every material number carries a time anchor in the same sentence or clause: a fiscal year or a calendar date ("$1.63 billion in profit in 2025").
- The house number move: state the fact, then translate it into a frame the reader can feel. Models: "The drive offered 20 MB of capacity at a price of approximately $1,000. In modern terms, this translates to roughly $50,000 per gigabyte in today's dollars." "A GPU that cost a few hundred dollars could outperform a CPU cluster that cost hundreds of thousands of dollars." Each chapter translates at least its three largest numbers.
- A headline number enters the book once, at full precision. Later mentions cite it briefly at the same value or refer to it by meaning ("the reversal year", "the flagship contract"); a stat block never gets re-pasted across chapters.
- The same fact carries the same value, unit, and date anchor everywhere, frontmatter included.
- Growth rates recompute from their stated bases. If a quarter grew 262 percent year over year, the prior-year quarter printed in the same book must support it.

## How chapters open

The first sentence of every chapter is a scene: a specific date, a place, a named person, or a specific company event. Roadmap and report framing are banned from the first three paragraphs of any file, including the frontmatter. One of three hook shapes opens each chapter, varied across the book:

1. Dated anomaly cold open. A specific date, a strange fact held for two or three sentences, then a plain-language payoff line, then a uniqueness claim, then the promise of explanation. Model: "On February 24, 2025, a company called Sandisk Corporation began trading on the NASDAQ stock exchange under the ticker symbol SNDK." Payoff: "The reason was simple: SNDK was the same ticker that SanDisk Corporation had used from its November 1995 initial public offering until its acquisition by Western Digital in May 2016." Uniqueness: "No other major technology company has completed a full founding-to-IPO-to-acquisition-to-independence cycle within four decades."
2. Decision under stakes. A named person, at a specific moment, with the options as they appeared then, and what hung on the outcome. The model is the fraud-ring opening: a persistent Russian fraud abuser whose patterns proved impossible to stop, the system named after him, and the losses that fell from nearly 10 percent of transaction volume to less than 0.5 percent.
3. Transformation sentence. From X in year A to Y in year B, with the interval named, and why the change was improbable. Model: "from over $1 billion in annual losses (2020) to $1.63 billion in profit (2025), a complete reversal in five years".

Banned in the first three paragraphs of any file: addressing returning readers, listing what the chapter covers, methodology, market taxonomy (TAM, SAM, SOM), book-description language, and any "What changed" or edition-delta framing.

## How chapters end

Endings turn a corner: a new fact that changes the stakes, a sharpened version of the chapter's question, or a concrete forward-looking tension carried by a named actor or date. The final chapter of the book ends on its largest unresolved tension, framed as a choice between two possible futures. Model: "whether SanDisk's story becomes a case study in corporate resilience or another example of how structural realities of the semiconductor industry eventually overwhelm even the most determined independent companies."

Banned endings: summaries of what the chapter covered, generic uplift ("still being written", "actively building pieces of the future"), logistics disclaimers ("readers should verify data against the most recent sources"), self-reference to the analysis, and fence-sitting truisms ("lies somewhere in the middle", "it remains to be seen", "warrants close observation", "will likely contain elements from across these scenarios").

## The chapter engine

- One central dramatic question per chapter, specific to this company and this chapter, stated explicitly in the first two paragraphs, with the stakes named (what happens to the company if each answer wins), and resolved or sharpened by the end. Example for a competition chapter: "will operational AI stay a standalone market or become a feature of cloud platforms, and can the incumbent survive the second answer?"
- Every H2 section introduces a human decision before the number it produced: who chose, when, the options as they appeared then, and the consequence. At least one named decision-maker with agency per section, and at least one sourced direct quotation of 40 or more characters that is speech (a said, wrote, or testified line) per chapter.
- Every contract, product launch, reversal, or strategic decision covered in a chapter is dramatized at least once as a reconstructed decision moment: the date, who was in the room, the options weighed, what was turned down, and how it resolved. Model: "Cohen fixed software bugs in real time during demos to government clients while Karp distracted the client with conversation."
- Where the sources cannot support reconstruction, the book says so explicitly and stages the stakes instead: what each party wanted, and what the outcome decided for them. A decision never gets flattened into a fact about consolidation.
- Consulting frameworks dissolve into thesis prose. TAM, SAM, SOM, SWOT, and Porter's Five Forces never appear as headings, bullet lists, or repeated templates. Each becomes one argued paragraph inside a section organized around a question. Competitor subsections are each structured differently: a deal story, a mechanism, a constraint, a counterfactual.
- No changelog padding. No section enumerates version-by-version or year-by-year release chronologies; compress to three to five load-bearing milestones, each with an argument attached.
- Chapter length discipline: no chapter longer than roughly 2.5 times the book's median chapter length; compress or split chapters that exceed it.
- Transitions: each section picks up the previous section's conclusion as its opening tension. Chapters hand forward by question: the tension one chapter ends on is the question the next chapter opens with.

## Certainty and conviction

- The author owns a house view. The frontmatter states which scenario the author assigns as most likely, approximate probability weights or an explicit confidence level for all three, and a one-sentence verdict on risk-reward at the current market price.
- Scenario chapters commit: a "most probable outcome" stated in concrete operational terms, then falsification triggers the reader can track, named observables with at least one dated or numeric trigger ("sustained 50 percent or higher commercial growth").
- Every named thesis is paired with its falsifier: observable developments that would prove it wrong. Naming failure in advance is what makes conviction credible, so every thesis gets one.
- The bear case is steelmanned with a causal bridge sentence ("the bear case does not require the company to fail; it merely requires it to succeed at a slightly slower pace than the most optimistic projections") plus quantitative multiple math showing the price path under bear assumptions. A flat taxonomy of worries does not count as a bear case.
- When analyst consensus or price targets appear, the book states its own position relative to them (above, below, or in line, with a reason) and presents its own scenario-implied value. Consensus aggregation is freely available elsewhere and adds nothing.
- Every valuation discussion includes a sanity check translation: what the current multiple implies operationally (growth rate, margin, duration), and which of the book's own scenarios the current market price is closest to. Model: "At current prices, the market is effectively underwriting sustained revenue growth near or above 30 percent for many years."
- When a uniform verdict is not defensible, commit asymmetrically by segment: "locked in as X under conservative scenarios, while Y remains contested".
- Risks are ranked. State a top three by assessed likelihood multiplied by impact, with a sentence on why each sits where it does.
- Any dated, binary milestone that anchors the thesis (a first launch, a certification, a profitability date) gets the book's own credibility assessment of management's timeline. Restating the target as fact is a failure.

## Headings and structure

- Sentence case for every heading: only the first word and proper nouns are capitalized. Acronyms stay uppercase (AI, GPU, IPO).
- Headings name stakes, moments, or mechanisms. The register to replicate: "The Sega moment and the $5 million lifeline". Promise-line titles for book parts name stakes (the flash pioneer years, the undoing, the re-emergence) instead of topics.
- No consulting framework names in headings. No escaped punctuation inside headings.
- The frontmatter follows the refined structure: an opening claim about the company, the edition-currency line ("This edition is current as of April 2026"), "Key findings" bullets with "(see Chapter N)" pointers, "The central thesis" with a three-part mechanism, "Future outlook and key variables" with base, bull, and bear, and the house view. Banned boilerplate, zero exceptions: "exceptionally comprehensive", "Unprecedented insight", "synergistic triad", "Key findings & core conclusions", "novel insights and connections".

## What never appears

- Em dashes and en dashes, in prose, bullets, comments, and captions. Use commas, colons, parentheses, or separate sentences.
- Report-speak: "this report", "this document", "hereinafter referred to as", consulting-audience framing, dual-audience prefaces, parenthetical legal disclaimers, AI-generation disclosures, and recommendations addressed to company management.
- Self-praise and process talk: "unprecedented", "exceptionally comprehensive", "novel insights", "the most thorough publicly available", "we aim", "unprecedented depth", methodology lists, objectives sections, and conclusions that catalog their own insights.
- Verdict-dissolving phrases: "it remains to be seen", "the story is still being written", "lies somewhere in the middle", "warrants close observation", "investment decisions should carefully weigh", "will likely contain elements from across these scenarios".
- False precision, spelled-out money ("N billion dollars"), and two-decimal aggregates in the billions.
- Cross-book references: no series, companion volumes, sibling subjects, or valuation comps against companies that are the subjects of other books in this repository. A sibling subject may appear only as unavoidable market context (a supplier, a competitor), named plainly, with zero language implying a series or a shared author.
- Pipeline artifacts: HTML comments, escaped punctuation (a stray backslash before periods, ampersands, or hyphens, the signature of a docs-app export), untranslated fragments in any language, and inconsistent entity spellings. One canonical spelling per entity, enforced across the whole book (Kioxia, never Koxia).
- Returning-reader language: "What changed", "returning readers", "since the last edition". Edition refreshes enter the standing story as narrative. The change log lives on the about page.

## Example pairs

Bad and good, with the reason in one line.

### Openings

Bad: "This book offers an exceptionally comprehensive and in-depth analysis of the company, moving beyond readily available summaries to uncover novel insights and connections."

Good: "On February 24, 2025, a company called Sandisk Corporation began trading on the NASDAQ stock exchange under the ticker symbol SNDK."

Why: the bad version describes and praises the book; the good version stages a dated anomaly the reader wants explained.

### Money

Bad: "Revenue grew from 5.01 billion dollars in fiscal 2016 to 215.94 billion dollars in fiscal 2026."

Good: "Revenue grew from approximately $5.0 billion in fiscal 2016 to $216 billion in fiscal 2026, a 43x increase."

Why: the bad version breaks the house format twice and adds false precision; the good version carries the format, a hedge, and a translation in one line.

### Conviction

Bad: "The answer, as with most questions about technology markets, lies somewhere in the middle."

Good: "The bear case does not require the company to fail; it merely requires it to succeed at a slightly slower pace than the most optimistic projections."

Why: the bad version dissolves the verdict the reader paid for; the good version gives the downside its strongest, most likely form.

### Decision moments

Bad: "The agreement consolidates roughly 75 separate contracts under a single framework, validating the platform."

Good: "Cohen fixed software bugs in real time during demos to government clients while Karp distracted the client with conversation."

Why: the bad version records an outcome and editorializes; the good version stages people acting under pressure, which is what a reader remembers.

