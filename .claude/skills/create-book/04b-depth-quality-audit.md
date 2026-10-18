# Phase 4b: depth-quality audit

**Company name:** the user-provided name.
**Book folder:** `books/<NNN>-<slug>/`. Determined in phase 1.
**Chapter sections decomposition:** `books/<NNN>-<slug>/.research/chapter-sections.md`. Written in phase 4 step 2.

## Goal

Verify, chapter by chapter, that every assembled chapter is grounded in the research material and meets the per-chapter quality bar, before the manuscript enters consistency review. This phase is the verification loop for phase 4's depth-assessment approach: it catches padding, unsupported claims, and missed research that the writing waves may have produced, and it forces remediation instead of letting thin sections through. This audit was first improvised during a real build (its outputs live in `books/004-nvidia/.research/quality-ch01.md` through `quality-ch10.md`); this file makes it a standing step so every future run repeats it.

## Inputs

- The assembled chapter files in `books/<NNN>-<slug>/manuscript/`.
- The research files that fed each chapter, per the research basis recorded in `books/<NNN>-<slug>/.research/assessment-<chapter-number>.md`.
- `books/<NNN>-<slug>/.research/chapter-sections.md` (the section decomposition).
- `books/<NNN>-<slug>/.research/claims-register.md` (provenance for load-bearing numbers).
- `.Resources/quality-bar.md` (the quality bar; its per-chapter checklist is the audit standard).
- `.Resources/voice.md` (the voice charter).

## Process

### 1. Audit one chapter at a time

For each assembled chapter, read the chapter and the research files that fed it. Do the audit yourself (inline), or spawn auditor agents in waves of 3 to 5, consistent with `04-chapter-writing.md`'s spawning strategy; each auditor handles exactly one chapter and writes exactly one audit file. Long runtimes are expected; verify artifacts, not clocks.

### 2. Judge every section against the research

For each section of the chapter, compare every factual claim against the research files and the claims register:

- **HONEST:** the section's claims trace to research material, and the research's depth is reflected in the prose.
- **PADDED:** the section stretches thin material with repetition, vagueness, or restated stat blocks.
- **UNSUPPORTED:** the section states specific claims (numbers, dates, events, quotations) with no basis in any research file or register row.

Also record, per section: missed material (real research facts the chapter failed to use, with file references) and padding detected (specific manuscript claims absent from the research, with line references).

### 3. Run the per-chapter quality bar

Run the per-chapter checklist in `.Resources/quality-bar.md` on the chapter (hook and engine, numbers, ending, craft and hygiene). Record pass or fail per checklist section, with the failing items named.

### 4. Write the audit file

Write `books/<NNN>-<slug>/.research/quality-ch<NN>.md` (one file per chapter, `<NN>` zero-padded to two digits):

```markdown
# Depth-quality audit: Chapter <N> - <title>

## Overall chapter verdict
- Total words: <count>
- Research utilization: <High | Medium | Low>
- Quality-bar per-chapter checklist: <pass | fail, with the failing items>
- Recommendation: <Acceptable | Needs work>

## Section-by-section assessment

### Section <N>.1: <title>
- Verdict: <HONEST | PADDED | UNSUPPORTED | minor padding>
- Missed material: <real research facts the section failed to use, with file references>
- Padding detected: <specific claims with no basis in the research files, with manuscript line references>
- Notes: <anything the remediation pass needs to know>

### Section <N>.2: <title>
...

## Chapter-level notes
<missed material and padding that cut across sections>
```

### 5. Remediate and re-audit

Every section judged PADDED or UNSUPPORTED must be rewritten or trimmed so each factual claim traces to a research file or register row: fix it inline, or respawn the section-writing agent and re-assemble the chapter. Re-audit the fixed sections and annotate their new verdicts in the audit file. A chapter is complete only when every section verdict is HONEST or minor padding. Phase 5 (consistency review) begins only after every chapter passes.

## Success criteria

- Every assembled chapter has a `books/<NNN>-<slug>/.research/quality-ch<NN>.md` audit file in the format above.
- Every section verdict is HONEST or minor padding; PADDED and UNSUPPORTED sections were rewritten, trimmed, or grounded, then re-audited.
- The per-chapter quality-bar checklist was run, and every unresolved item is recorded.
- No chapter proceeded to phase 5 before its audit passed.

Report back with one line per chapter: the verdict distribution, the research utilization, and whether remediation was needed.
