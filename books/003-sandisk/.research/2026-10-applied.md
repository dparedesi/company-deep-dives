# Sandisk Corporation applied changes: October 2026

One line per applied change, per step 3 of the book-refresh cycle. Generated from the chapter agents' structured returns plus the orchestrator's frontmatter and introduction passes.

## 05-commodity-cycle.md

| gate-fix | lint | Line 3: pro forma revenue "$7.355 billion" became "approximately $7.4 billion" and net loss "$1.64 billion" became "approximately $1.6 billion" (two-decimal aggregate gate). |
| gate-fix | lint | Line 103: same two-value fix in the 2023 downturn section. |
| gate-fix | lint | Line 165: "**Revenue of $7.355 billion.**" became "**Revenue of approximately $7.4 billion.**". |
| gate-fix | lint | Line 167: "**Net loss of $1.64 billion.**" became "**Net loss of approximately $1.6 billion.**". |

## 06-market-position.md

| gate-fix | lint | Verified no two-decimal billions and no spelled-out money introduced; all new aggregates follow the conversion policy (approximately $23.1 billion, $68.9 billion, $38.9 billion, roughly $21 billion, approximately $9.0 billion, approximately $4.9 billion, approximately $17 billion, roughly $274 billion); lint reports zero hits for manuscript/06-market-position.md. |

## 10-future-outlook.md

| gate-fix | lint | Fixed all 18 'Koxia' misspellings to Kioxia (charter: one canonical spelling) |
| gate-fix | lint | Replaced the CJK fragment at old line 173 (as新兴需求源的发展速度不确定。) with English prose |
| gate-fix | lint | Two-decimal money fixes at old lines 5, 17, 43, 83, 185: $7.355 billion became approximately $7.4 billion, $1.64 billion became approximately $1.6 billion (four occurrences), each now with a fiscal-year anchor |
| gate-fix | lint | Retired the old bear-band contradiction inside the scorecard: below $6 billion (this chapter) and below $5 billion (frontmatter) each cited exactly once, both bands retired everywhere else |
| gate-fix | lint | Heading case normalized to sentence case across touched sections (old 'Multi-Scenario Outlook for 2030' heading rebuilt as 'Three scenarios for the contracted decade' per the sanctioned scenario rebuild) |
| gate-fix | lint | Zero lint hits in this file: no em or en dashes, no CJK, no HTML comments, no spelled-out money, no two-decimal aggregates, no banned phrases |

## 08-spin-off.md (The Spin-Off and Re-Emergence), The SanDisk Paradox, October 2026 edition update

| gate-fix | lint | Former line 13: $7.355 billion became approximately $7.4 billion; 'net income ... negative $1.64 billion' became 'a net loss of approximately $1.6 billion in 2025' |
| gate-fix | lint | Former line 19: $9.52 billion became $9.5 billion (WD HDD revenue, 2025) |
| gate-fix | lint | Former line 31: pro forma net loss $1.64 billion became approximately $1.6 billion |
| gate-fix | lint | Former line 73: $7.355 billion became approximately $7.4 billion for 2025 |
| gate-fix | lint | Former line 75: $1.64 billion became approximately $1.6 billion |
| gate-fix | lint | Former lines 107 and 139 equivalents: all new and retained money figures follow the conversion policy natively ($9.0 billion, $20.2 billion, $11.4 billion, $1.2 billion, per-share prices exact) |
| gate-fix | lint | lint_manuscript.py sandisk: zero hits in 08-spin-off.md after edits (remaining 14 hits are in 00-frontmatter, 09, 10, about.md, owned by other steps) |

## 03-toshiba-jv.md (The Toshiba Joint Venture and Manufacturing Logic)


## 04-product-strategy.md (Sandisk, October 2026 edition)

| gate-fix | lint | None required: 04-product-strategy.md had zero lint hits before and after editing (pre-existing book hits are in 00-frontmatter, 05, 07, 08, 09, 10, and about.md, owned by other steps). |
| gate-fix | lint | Verified by scan: no em or en dashes, no HTML comments, no CJK or Cyrillic codepoints, no spelled-out money, no two-decimal aggregates in the billions; unit prices kept exact ($429.99) and money formats follow the conversion policy (approximately $5.2 billion, approximately $200). |

## 07-wd-acquisition.md

| gate-fix | lint | Line 172: '$7.355 billion in pro forma revenue' to 'Approximately $7.4 billion in pro forma revenue (fiscal 2025)' |
| gate-fix | lint | Line 173: '-$1.64 billion in pro forma net loss' to 'A pro forma net loss of approximately $1.6 billion the same year' |
| gate-fix | lint | Line 179: '$9.52 billion in 2025 revenue' to '$9.5 billion in fiscal 2025 revenue' |

## 00-frontmatter.md

| replace | F42, F43, F44, F45, F57, F58, F59, F60-F64 | Rebuilt frontmatter: claim-first overview opening (replacing book-description opening), key-findings bullets updated to FY2026 actuals, Q2 2026 shares, JV-through-2034, WD stake severance; Act III thesis rewritten around the contracted decade; future outlook section rebuilt with the scored April scenarios, new base 45 / bull 30 / bear 25 framework, house view, risk-reward verdict at $1,299.30, and dated falsifiers |
| update | F5, F6, F7, F8 | Commodity-cycle bullet now carries the FY2026 frame: approximately $20.2 billion revenue, approximately $11.4 billion GAAP net income, NBM contracted bits |
| update | F23, F25 | Market-position bullet now cites Q2 2026 revenue-basis shares and YMTC third in bits |
| update | F1, F3, F4, F32 | JV and WD bullets corrected: Sandisk holds the 49.9 percent Flash Ventures interests, extended to 2034; WD equity stake under 1 percent by mid-2026 |
| update | F52 | Ethics bullet adds the April 2026 Sanriku earthquake live test |
| gate-fix | lint | House view added (was a missing-house-view gate hit); all aggregates converted to one-decimal format |

## 01-introduction.md

| none | | No step-3 edit required: chapter contains no false JV-ownership claims and its structure holds; the edition-date line is step 5's |

## 02-founding-vision.md

| none | | No changes this edition |

## 09-ethics-risk.md

| update | F52, F63 | Earthquake live-test passage: April 20, 2026 Sanriku quake per Kioxia's official statement (JMA magnitude 7.5, no Kitakami damage, production normal), spot quotes briefly paused |
| rewrite | F2, F30 | Kioxia ownership paragraph rewritten: listed December 2024 (TSE Prime, 285A), Bain out July 2026, Toshiba near 14 percent, SK Hynix convertible-bond vehicle largest holder; geopolitical framing inverted |
| add | F22 | New section on the 2026 allocation choice and who paid for it (retail disappearance, consumer DDR5 up roughly 500 percent, NBM locking the priority in) |
| add | F49, F26 | China risk passage: YMTC third in bits under sanctions, STAR IPO, largest-by-2027 aim; CXMT density claim and the October rout; export controls reframed as slowed-not-stopped |
| add | F55 | Tariff paragraph: 15 percent baseline on Japanese imports, Section 232 spared NAND, broader chip tariffs live into 2027 |
| add | F53, F54 | New section on the optics of a boom: Kfar Saba cuts, pre-planned insider sales framed exactly |
| update | charter | Ranked top three risks by likelihood times impact closing the structural-risks run |
| update | F5-F8, F23-F25 | Brief 2026 cites with Chapter 5 pointer; Q2 2026 share anchors replace Q3 2025 |
| fix | F1 | False WD-50-percent claim in the spin-off section corrected (Sandisk holds the 49.9 percent interests) |
| gate-fix | lint | Lines 77, 81, 121, 157: two-decimal billions converted to one-decimal prints |

