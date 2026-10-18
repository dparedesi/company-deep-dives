# Phase 2: consolidation

## Goal

Read ALL research files from the current run and produce a consolidated, scored ranking of candidate companies. Identify overlapping signals (a company that appears across multiple angles is a stronger pick) and eliminate weak candidates.

## Input

- All phase 1 files in the current run's directory: `.research/next-books/<RUN>/01-search-trends.md` through `08-wildcard.md`. `<RUN>` is the run's date label, plus a numeric suffix on same-day re-runs (see SKILL.md, output location).
- The existing-books list from `ls books/`, to remove covered companies.

Read only files from the current run's directory. Never mix files across run dates: a file from an earlier run's directory is stale demand signal, even if the current run is missing its counterpart.

## Process

1. Read every research file produced by the parallel agents in this run.
2. Build a master list of all companies mentioned across all files.
3. For each company, count how many angles it appeared in (per the membership rule below) and aggregate the evidence.
4. Map demand signals to dimension scores (per the mapping below).
5. Score each company using the scoring framework below.
6. Rank by composite score.
7. Recompute every row against the formula, then write the consolidated ranking to `.research/next-books/<RUN>/09-consolidated-ranking.md`.

## Scoring framework

Score each candidate company on five dimensions, each on a 1 to 5 scale with the anchors below. Levels 2 and 4 are defined; use them when the evidence sits between the odd anchors rather than defaulting to 3 or 5:

| Dimension | Weight | 1 (low) | 2 (below medium) | 3 (medium) | 4 (below high) | 5 (high) |
|-----------|--------|---------|-------------------|-------------|----------------|----------|
| Search demand | 25% | Minimal search interest | Occasional queries, flat or declining trend | Moderate queries | Sustained high queries or a clearly rising trend | Very high search volume |
| News momentum | 20% | Rarely in news | Occasional coverage, no running story | Regular coverage | Frequent coverage with a live running story | Dominating headlines |
| Investor interest | 20% | Niche following | Modest retail or institutional interest, not both | Moderate retail and institutional | Strong retail interest plus visible institutional activity | Viral retail plus institutional |
| Content gap | 20% | Good current books exist | Several books, most still current, at least one strong | Some coverage, outdated | Only weak or fragmentary coverage | Zero deep-dive content |
| Narrative potential | 15% | Boring story | Some interesting dynamics, little tension | Interesting dynamics | Strong tension or transformation underway | Compelling, polarizing story |

**Mapping from phase 1 signals:** phase 1 files report demand signal strength as high, medium, or low. Map high = 5, medium = 3, low = 1. First normalize non-standard labels from phase 1 (for example "very high", "maximum", "critical", "medium-high") to high, medium, or low, and note the normalization in the methodology section.

**Composite score** = weighted average across all dimensions: `0.25*search + 0.20*news + 0.20*investor + 0.20*gap + 0.15*narrative`.

**Angle membership** (for the Angles column and the signal bonus): a company appears in an angle only if it is a numbered top candidate or an extended-list entry in that angle's file. Passing mentions, exclusion headers, and name-drops inside another company's entry do not count. For each angle counted, cite the file number and section (for example: 05, top candidates, entry 3).

**Signal bonus:** if a company appears in 4 or more research angles (counted per the membership rule above), add +0.5 to the composite score. Multi-angle consensus is the strongest signal.

**Scale:** the composite ranges from 1.0 to 5.5: 5.0 is the weighted maximum, and the signal bonus adds up to 0.5. Report composite as X.X/5.5 in the table, the detailed sections, and the watch list.

**Rounding:** compute the weighted average exactly, add the bonus, then round once to one decimal, rounding halves up. One rounding pass, after the bonus.

**Worked example:** Search 4, News 5, Investor 4, Content gap 5, Narrative 5, Angles 7 gives `0.25*4 + 0.20*5 + 0.20*4 + 0.20*5 + 0.15*5 = 4.55`, plus the 0.5 signal bonus (7 angles >= 4) = 5.05/5.5.

**Verification loop:** after building the table, recompute every row against the formula, fix mismatches, and show the arithmetic inline for the top 7 before writing the file.

**Existing book penalty:** if the company already has a book in this repo, mark it as "existing coverage" and remove it from ranking. Note it separately as validation that the skill is working correctly.

## Output format

Write the ranking in direct plain English, following the register and hygiene rules in `.Resources/voice.md` (from the repo root), which apply to research files too, not only book manuscripts. Write to `.research/next-books/<RUN>/09-consolidated-ranking.md`:

```markdown
# Consolidated ranking: next book candidates

Consolidation date: <today's date>
Run: <RUN label>

---

## Methodology

Brief description of how files were combined and scored, including any label normalization and the angle-membership rule applied.

---

## Top 15 candidates

| Rank | Company | Ticker | Composite | Search | News | Investor | Content gap | Narrative | Angles |
|------|---------|--------|-----------|--------|------|----------|-------------|-----------|--------|
| 1 | ... | ... | 5.1 | 5 | 4 | 5 | 4 | 5 | 7/8 |
| 2 | ... | ... | ... | ... | ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |

---

## Detailed analysis for top 7

### 1. <Company name> (<Ticker>) - Score: X.X/5.5

**Composite evidence from research** (cite file and section for each line):
- Search trends (01, top candidates, entry N): <summary of what agent 1 found>
- News coverage (02, extended list, entry N): <summary of what agent 2 found>
- Investor interest (03, top candidates, entry N): <summary of what agent 3 found>
- Content gap (06, top candidates, entry N): <summary of what agent 6 found>

**Why this company NOW:** <2 to 3 sentences on timing>

**Reader profile:** <who buys this book>

**Suggested angle:** <what makes this book unique>

**Risks:** <why this might NOT work as a book>

---

## Watch list (catalyst not landed yet)

Companies that scored well but lack immediate catalyst. List the catalyst that would promote each into the top picks.

---

## Existing coverage validation

Companies already covered in this repo that appeared in research (confirms the repo is on the right track).

---

## Data gaps

Questions that could not be answered from available research.
```

## Success criteria

- Every phase 1 file in the current run's directory is read and incorporated (no files from other runs).
- The master list built during the process contains at least 30 unique companies, from which the top 15 are tabulated.
- Top 15 are scored with specific evidence, and every row recomputes exactly against the formula (weighted average, bonus, single rounding pass); the arithmetic is shown inline for the top 7.
- Angle counts follow the membership rule and cite file and section for each angle counted.
- Top 7 have detailed narrative analysis.
- No existing repo books appear in the candidate ranking.
- The watch list names the promoting catalyst for each company.
- The artifact gates pass: zero hits for an em dash (`$'\xe2\x80\x94'`), an en dash (`$'\xe2\x80\x93'`), and non-Latin codepoints; no hype adjectives; money figures in the form "$N billion" with the dollar sign attached.

Report back with the run directory path, the count of candidates scored, the top 3 composite scores with their arithmetic, and confirmation that every row recomputed against the formula and the artifact gates passed.
