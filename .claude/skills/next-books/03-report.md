# Phase 3: final report

## Goal

Generate a polished, actionable recommendation report from the consolidated ranking. This is the deliverable the user reads to decide which book to write next.

## Input

- `.research/next-books/<RUN>/09-consolidated-ranking.md` from phase 2, the current run. `<RUN>` is the run's date label, plus a numeric suffix on same-day re-runs (see SKILL.md, output location).
- All phase 1 research files in `.research/next-books/<RUN>/` for reference and citation.

## Output

Write the final report to `.research/next-books/<YYYY-MM-DD>-report.md` (use today's date; see SKILL.md for the same-day re-run suffix).

## Timing rules

Market timing around company events (an expected IPO window, an earnings catalyst, a product cycle) may be discussed as a market fact, with sources. Never attach a writing-duration or publication-cycle estimate to any recommendation: no months of research, no writing-cycle durations, no target publication quarters, no start dates. Describe scope concretely instead (number of chapters, revenue streams, segments, filings to cover) and let the owner judge timing.

## Report structure

```markdown
# Next book recommendations

Report date: <today's date>
Existing books: <list from ls books/>

---

## Executive summary

3 to 5 sentences on the macro picture: which themes generated the most corroborated demand signals, with counts from the angle files, what kind of companies are attracting the most interest, and the single strongest recommendation.

---

## Top recommendations

### 1. <Company name> (<Ticker>)

**Why now:** One paragraph on timing and catalyst.
**Demand signals:** 3 to 5 bullet points with specific evidence (search volume, news events, investor activity, content gaps). Every bullet cites an angle file by number or a URL.
**Target reader:** Who buys this book and why.
**Suggested angle:** What makes this book different from anything else available.
**Information availability:** High/medium/low (depth of public filings, earnings-call transcripts, and disclosure history available to support the deep dive).
**Confidence:** High/medium/low (based on how many research angles agreed).

### 2. <Company name> (<Ticker>)
(continue through top 5 to 7)

---

## Comparison matrix

| Company | Demand | Gap | Timing | Complexity | Confidence |
|---------|--------|-----|--------|------------|------------|
| ... | High/Med/Low | Wide/Narrow | Now/Soon/Later | High/Med/Low | High/Med/Low |

---

## Watch list

Companies that are gaining momentum but need a specific catalyst before they become top picks. Include what to watch for.

| Company | Current score | What would push it higher |
|---------|---------------|--------------------------|
| ... | ... | ... |

---

## Thematic insights

What the research revealed about reader demand patterns:
- Which sectors attract the most deep-dive interest
- What kind of company stories resonate (turnarounds, disruptors, controversials, compounders)
- Whether timing matters more than topic (news-driven vs evergreen)
- Geographic and demographic patterns in search interest

---

## Methodology note

Brief note on how the research was conducted: number of agents, angles covered, sources consulted, limitations.

---

## Full source list

Aggregate all sources from all research files into a single deduplicated list.
```

## Normative requirements

The structure above is normative, not advisory. Before finishing, verify every item:

1. Use exactly the sections in the template above, in that order, with those exact heading names. Do not add, rename, or reorder sections. Do not append a separate final-recommendation section; the single strongest recommendation belongs in the executive summary.
2. The Top recommendations section must contain 5, 6, or 7 numbered entries (### 1. through ### N.). Fewer than 5 fails this phase. The consolidated ranking always provides detailed analysis for 7 candidates, so 7 entries is the default.
3. Every numbered entry must include all six labeled fields from the template: Why now, Demand signals (3 to 5 bullets, each citing an angle file by number or a URL), Target reader, Suggested angle, Information availability (high/medium/low), and Confidence (high/medium/low).
4. The comparison matrix must have exactly the columns Company | Demand | Gap | Timing | Complexity | Confidence, with the cell vocabularies shown in the template (High/Med/Low, Wide/Narrow, Now/Soon/Later).
5. The watch list must have exactly the columns Company | Current score | What would push it higher. The promoting catalyst is the content of the third column; there is no timeline column.
6. Reference research files by repo-relative path (for example `.research/next-books/<RUN>/01-search-trends.md`), never absolute paths.
7. Follow the repo writing conventions: no em or en dashes anywhere, sentence case for headings, acronyms expanded on first use. Register follows `.Resources/voice.md` (from the repo root), which applies to generated files too, not only book manuscripts.
8. No hype adjectives (perpetual, perfect, ultimate, fever pitch, and phrases like "the dominant investment narrative of the decade"). Every factual claim about demand, numbers, or market data must cite an angle file (by number) or a URL. Replace vague heat language with counts, for example: "AI infrastructure appeared in 5 of the top 7 candidates and was flagged as a high or critical demand signal in 4 of 8 angle files."

## Success criteria (machine-checkable)

- The report's ## headings are exactly the template's sections, in order.
- The Top recommendations section has 5, 6, or 7 numbered entries, each containing all six labeled fields.
- The comparison matrix header row is exactly: Company | Demand | Gap | Timing | Complexity | Confidence.
- The watch list header row is exactly: Company | Current score | What would push it higher.
- grep for "/Users/" in the report file returns nothing (no absolute paths).
- grep for an em dash (`$'\xe2\x80\x94'`) or an en dash (`$'\xe2\x80\x93'`) in the report file returns nothing.
- grep for each banned hype word (perpetual, perfect, ultimate, fever pitch) returns nothing.
- Every factual claim cites an angle file number or a URL.
- No effort, duration, or publication-cycle estimates appear anywhere in the report.
- Money figures use the form "$N billion" with the dollar sign attached, never the spelled-out pattern.

## Final step: commit and push

Commit and push the run artifacts as part of this phase, never left to the user: `git add` exactly the dated run directory and the report file under `.research/next-books/`, commit with `Next-books selection research <run label>` (the suffixed label, for example `2026-10-18-2`, on same-day re-runs) plus the attribution footer `Co-Authored-By: Claude Code <noreply@anthropic.com>`, then `git push`. Stage nothing outside `.research/next-books/`. If the push fails, report the failure and the local commit hash and stop; do not force-push.

Report back with the report path, the number of entries in Top recommendations, confirmation that every normative check and every grep gate passed, and the commit hash of the pushed run.
