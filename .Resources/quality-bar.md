# Quality bar

The premium test, operationalized. One question judges every chapter and every book: would a discerning reader pay a premium for this because it is the definitive, to-go reference on this company? One companion question sets the height of the bar: what in this chapter would make that reader put the book down?

How this file is used: writers self-check with the per-chapter list before submitting. Consistency review runs the per-book list across the whole manuscript. The gates section blocks builds mechanically. Voice rules live in `.Resources/voice.md` (the voice charter); this file references them, and other files must not restate them.

## Per-chapter checklist

Run for every chapter, at writing time and again during consistency review. Before anything else: would a discerning reader pay a premium for this chapter as the definitive treatment of its slice of the company? If the answer is uncertain, the chapter needs a sharper question or deeper material; more words will not produce it.

### Hook and engine

- The opening sentence is a scene (a date, a place, a person, an event) in one of the three charter hook shapes, and the first three paragraphs contain zero roadmap, methodology, market taxonomy, returning-reader language, or book-description.
- The chapter's central dramatic question is stated in the first two paragraphs, specific to this company and this chapter, with the stakes named, and the ending resolves or sharpens it.
- At least one dated, dramatized decision moment with named actors; where sources cannot support reconstruction, the chapter says so and stages the stakes.
- At least one sourced quotation of 40 or more characters that is speech, and at least one named decision-maker with agency in every H2 section, introduced before the number the decision produced.
- Zero consulting frameworks as headings, bullet lists, or repeated templates, and competitor subsections are each structured differently.
- No changelog padding: no stretch of more than five consecutive paragraphs each naming a different version or release, and every kept milestone carries an argument.

### Numbers

- Money in the charter format everywhere, and zero hits for the spelled-out pattern.
- No false precision: at most one decimal on aggregates above $1 billion, hedges on estimates, and market projections rounded to a magnitude the reader can hold.
- Every material number carries a time anchor in the same sentence or clause, and the chapter's three largest numbers have translation frames.
- Nothing repeated: no exact figure repeated verbatim from another chapter, no projection stated twice within one chapter, and no stat block re-pasted.
- Everything reconciles: growth rates recompute from stated bases, quarters sum to years, segments sum to totals, and the same fact carries the same value everywhere.

### Ending

- The last two paragraphs turn a corner (a new fact that changes the stakes, a sharpened question, or a tension carried by a named actor or date) and contain zero summary, disclaimer, uplift boilerplate, and fence-sitting.

### Craft and hygiene

- Sentence rhythm in the charter band (a manuscript-wide average of 16 to 22 words per sentence, and this chapter between 14 and 24), with at most one one-line dramatic paragraph per section.
- Zero em dashes, zero en dashes, zero escaped punctuation, zero non-Latin codepoints, zero HTML comments, and zero internal pipeline markers.
- One canonical spelling per entity, verified with a near-duplicate alias scan over entities appearing more than 10 times.
- Chapter length within 2.5 times the book's median chapter length.

## Per-book checklist

Run during consistency review, before the build.

### Frontmatter

- Opens with a claim about the company, with zero book-description opening.
- Full structure present: the edition-currency line, key findings with "(see Chapter N)" pointers, the central thesis with a three-part mechanism, and base, bull, and bear with key variables.
- House view present: the most likely scenario, probability weights or an explicit confidence level, and a one-sentence risk-reward verdict at the current market price.
- Zero banned boilerplate from the charter's list, and a minimum of 300 words; an empty or skeletal frontmatter blocks publication.

### Conviction

- Every named thesis has a falsifier section with at least one dated or numeric falsifier.
- The scenario chapter states a most probable outcome in concrete operational terms.
- The bear case has its strongest form: the causal bridge sentence plus quantitative multiple-compression math.
- The risk chapter ranks a top three by likelihood times impact, with reasons.
- Any analyst consensus cited is answered with the book's own position (above, below, or in line, with a reason) and its own scenario-implied value.
- Every valuation discussion includes the sanity check translation, and the current price is placed against the book's own scenarios.
- Every dated, binary thesis milestone carries the book's own credibility assessment of management's timeline.
- Zero verdict-dissolving phrases in the outlook, conclusion, and investor sections.

### Register and one author

- Zero hits for the charter's register violations and self-praise scans.
- At most one reader covenant, in the introduction, in the "What this book is not" form.
- Sentence-case headings throughout, and headings name stakes, moments, or mechanisms.
- The voice test: read the opening page of three chapters chosen at random against the charter; a reader who finished another book in this series must hear the same author.
- Zero cross-book references: no series or companion language, and no valuation comps against sibling-book subjects. Sibling subjects appear only as plain market context.

### Reliability

- Every load-bearing number is traceable to a research artifact with a named source and an as-of date, through a claims register or equivalent delta finding IDs; a number with no provenance does not ship.
- The numeric consistency gate passed: same fact, same value everywhere including the frontmatter, no duplicate figure sets under two different period labels, and no coexisting valuation snapshots.
- Exactly one valuation snapshot, as-of dated inline, and every prior-edition block deleted.
- Cumulative dashboard metrics (adoption counts, cumulative outcome totals, program counters) re-pulled with the new as-of date inline.
- Attribution honesty: "according to company disclosures" and "announced in YYYY" appear only with a named source in the research, the book's own analytic models are labeled as estimates with the reasoning shown, and source qualifiers survive copying.
- Edition currency: prices, multiples, and return figures re-verified this cycle, and the release notes state what was re-verified versus carried forward.
- When a prior edition exists: its scenario forecasts and the company's guidance-versus-actuals are scored in the research delta, and expired milestones are resolved in the outlook chapter.

### Iteration continuity (refresh and remediation editions)

An edition is an iteration, never a replacement. A reader who owned the previous edition must recognize the book they bought and feel it got sharper, not swapped for a new one.

- The chapter set, order, and H1 titles are unchanged unless a structural change was sanctioned and recorded in the changes file.
- Existing scenes, reconstructions, and arguments that still hold are kept and improved in place, never discarded and re-drafted from zero.
- Prose changes are surgical: a section is rewritten only when a new fact, a gate hit, or a bar failure demands it. Style-only rewrites of passages that already meet the charter are forbidden.
- The diff is part of the review: report the changed-line ratio per chapter. Any chapter where most lines changed carries a recorded justification (sanctioned structural change, bar-mandated rebuild, or a factual correction cascade that forced new prose).
- Remediation editions may legitimately touch more than a normal monthly refresh, but section by section, not book-wide: the editor names which bar failure each rewrite serves.

## Gates: what blocks a build

Mechanical scans run as part of the build, with zero tolerance and no judgment calls. Any hit fails the build with the exact file and line listed:

- U+2013 and U+2014 anywhere; CJK, Hangul, or Cyrillic codepoints; escaped punctuation (a backslash immediately before punctuation); HTML comments.
- The spelled-out money pattern, and two-decimal aggregates in the billions.
- The charter's banned phrase lists (self-praise, report-speak, verdict-dissolving).
- A frontmatter that is missing the house view or that is under 300 words.

## Put-it-down triggers

The fastest ways to lose a premium reader. Each one is a documented failure mode of this series, and each one is a stop-the-press event:

- An internal contradiction the reader can catch (the same quarter at two values, the same milestone at two dates).
- A misspelled partner or entity name anywhere in the book.
- An untranslated fragment, an escaped artifact, or a pipeline marker in the prose.
- A number that cannot be true against the book's own stated bases.
- A fence-sit ending after a chapter promised a judgment.
- An opening that describes the book instead of making a claim about the company.
- Evidence-free specifics stated as fact ("typically 115 to 120 percent").

## How to run it

- Writer self-check: the per-chapter list, at writing time, before submitting.
- Consistency review: the per-book list across the whole manuscript, then the per-chapter list on every chapter that was touched.
- Build gates: automated, fail closed, exact hits with file and line reported.
- Review output is specific: the file, the line, and the fix. "Looks good" is not an acceptable review result.

