// Professional Book Template for Typst
// =====================================
// Designed for trade paperback / modern book aesthetics

// Variables from Pandoc
#let book-title = "$title$"
#let book-author = "$author$"
#let book-date = "$date$"

// Color scheme
#let primary-color = rgb("#2c3e50")    // Dark blue-gray for headings
#let accent-color = rgb("#2c3e50")     // Same dark color (no bright blue)
#let muted-color = rgb("#7f8c8d")      // Gray for secondary text

// =========================================
// PAGE SETUP - Modern book margins
// =========================================
#set page(
  paper: "us-letter",
  margin: (
    // Modern book style margins
    inside: 1in,
    outside: 0.75in,
    top: 0.75in,
    bottom: 1in,
  ),
  // Running headers
  header: context {
    let page-num = counter(page).get().first()
    if page-num > 1 {
      set text(size: 8pt, fill: muted-color, style: "italic")
      if calc.odd(page-num) {
        // Odd pages: title on right
        h(1fr)
        book-title
      } else {
        // Even pages: author on left  
        book-author
        h(1fr)
      }
    }
  },
  // Page numbers
  footer: context {
    let page-num = counter(page).get().first()
    if page-num > 1 {
      set text(size: 10pt, fill: muted-color)
      h(1fr)
      [#page-num]
      h(1fr)
    }
  },
)

// =========================================
// TYPOGRAPHY
// =========================================
#set text(
  font: ("Libertinus Serif", "Linux Libertine", "Palatino", "Georgia"),
  size: 11pt,
  lang: "en",
)

#set par(
  leading: 0.7em,         // Line spacing
  first-line-indent: 1em, // Paragraph indent
  justify: true,
)

// Don't indent first paragraph after headings
#show heading: it => {
  it
  par(text(size: 0pt, ""))  // Reset indent
}

// =========================================
// HEADINGS - Chapter styling
// =========================================
#set heading(numbering: "1.1")

// Chapter headings (h1)
#show heading.where(level: 1): it => {
  pagebreak(weak: true)
  v(15%)  // Push down from top
  
  // Chapter number
  set text(size: 14pt, weight: "regular", fill: accent-color)
  if it.numbering != none {
    block[Chapter #counter(heading).display()]
  }
  
  v(0.5em)
  
  // Chapter title
  set text(size: 26pt, weight: "bold", fill: primary-color)
  block[#it.body]
  
  v(2em)
}

// Section headings (h2)
#show heading.where(level: 2): it => {
  v(1.5em)
  set text(size: 14pt, weight: "bold", fill: primary-color)
  it
  v(0.75em)
}

// Subsection headings (h3)
#show heading.where(level: 3): it => {
  v(1em)
  set text(size: 12pt, weight: "bold", fill: primary-color)
  it
  v(0.5em)
}

// Minor headings (h4)
#show heading.where(level: 4): it => {
  v(0.75em)
  set text(size: 11pt, weight: "bold", style: "italic", fill: primary-color)
  it
  v(0.25em)
}

// =========================================
// BLOCK ELEMENTS
// =========================================

// Block quotes
#show quote.where(block: true): it => {
  v(0.5em)
  block(
    inset: (left: 1.5em, right: 1em, y: 0.5em),
    stroke: (left: 2pt + accent-color),
  )[
    #set text(style: "italic", size: 10.5pt)
    #set par(first-line-indent: 0pt)
    #it.body
  ]
  v(0.5em)
}

// Code blocks
#show raw.where(block: true): it => {
  v(0.5em)
  block(
    fill: rgb("#f6f8fa"),
    stroke: 0.5pt + rgb("#e1e4e8"),
    inset: 12pt,
    radius: 4pt,
    width: 100%,
  )[
    #set text(font: ("Fira Code", "SF Mono", "Menlo", "Consolas"), size: 9pt)
    #it
  ]
  v(0.5em)
}

// Inline code
#show raw.where(block: false): it => {
  box(
    fill: rgb("#f0f0f0"),
    inset: (x: 3pt, y: 0pt),
    outset: (y: 3pt),
    radius: 2pt,
  )[
    #set text(font: ("Fira Code", "SF Mono", "Menlo"), size: 0.9em)
    #it
  ]
}

// Links
#show link: it => {
  set text(fill: accent-color)
  it
}

// =========================================
// LISTS
// =========================================
#set list(
  indent: 1.5em,
  body-indent: 0.5em,
  marker: ([•], [◦], [–]),
)

#set enum(
  indent: 1.5em,
  body-indent: 0.5em,
)

// =========================================
// TABLES
// =========================================
#set table(
  stroke: none,
  inset: 8pt,
  fill: (_, row) => if row == 0 { rgb("#f0f0f0") } else { none },
)

#show table.cell.where(y: 0): set text(weight: "bold")

// Add lines to tables
#show table: it => {
  set table(stroke: (x: none, y: 0.5pt + rgb("#ddd")))
  it
}

// =========================================
// HORIZONTAL RULES
// =========================================
#show line: it => {
  v(1em)
  align(center)[
    #box(width: 30%, line(length: 100%, stroke: 0.5pt + muted-color))
  ]
  v(1em)
}

// =========================================
// TABLE OF CONTENTS
// =========================================
$if(toc)$
#page[
  #v(10%)
  #align(center)[
    #text(size: 24pt, weight: "bold", fill: primary-color)[Contents]
  ]
  #v(1.5em)
  #outline(
    title: none,
    indent: 1.5em,
    depth: $toc-depth$,
  )
]
$endif$

// =========================================
// DOCUMENT CONTENT
// =========================================
$body$
