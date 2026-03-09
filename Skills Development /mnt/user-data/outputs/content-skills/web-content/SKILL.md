---
name: web-content-writing
description: >
  Subskill for web content — blog posts, articles, evergreen guides, how-to content, and thought 
  leadership pieces published on websites. Invoke alongside content-writing-core. 
  Handles: scannable structure, digital reading behavior, internal linking signals, headline mechanics, 
  meta elements, and the formatting rules that make web content perform. 
  Use for: blog posts, knowledge base articles, FAQ pages, pillar content, evergreen guides.
  Do NOT use alone for pure SEO/GEO optimization (use seo-geo-writing), sales copy (use marketing-copywriting), 
  or news articles (use news-writing).
version: 1.0
parent: content-writing-core
---

# Web Content Writing

Builds on content-writing-core. All core rules apply. This skill adds the web-specific layer: how digital readers actually read, how to structure for skimmability without sacrificing depth, and how to format for both humans and content systems.

---

## 1. How Web Readers Actually Read

F-pattern and Z-pattern reading are well-documented. Web readers:
- Read the headline and first sentence of each paragraph
- Scan H2s and H3s to map the article before committing
- Drop off significantly after the first scroll
- Return to sections non-linearly based on their specific need

**Implication for writing:**
- Every H2 must communicate standalone value
- First sentence of every paragraph must carry the full weight of that paragraph's claim
- Nothing critical can appear only in the middle of a paragraph
- The article must work as a skim AND as a full read

---

## 2. Headline and Title Mechanics

### 2.1 Title Architecture

A strong web content title contains:
- **Clarity** about what the reader will learn
- **Specificity** that signals depth ("5 types" is stronger than "types of")
- **Relevance signal** for the right audience
- **Optional: recency signal** ("2026 guide") for fast-moving topics

**Title formulas by content type:**

| Type | Formula | Example |
|---|---|---|
| How-to | How to [Achieve Outcome] [Modifier] | How to Build a Content Calendar Without Burnout |
| Listicle | [Number] [Thing] That [Benefit/Consequence] | 7 Content Structures That Reduce Bounce Rate |
| Definitive guide | The [Adjective] Guide to [Topic] | The Practical Guide to Long-Form SEO Content |
| Question | [Natural Question the Reader Actually Has]? | Does Publishing Frequency Still Matter in 2026? |
| Comparison | [Option A] vs [Option B]: [Deciding Factor] | Blog vs Newsletter: Which Builds Audience Faster? |

### 2.2 Headline Rules
- Maximum 60–65 characters for SEO display (meta title)
- Front-load the most important keyword
- No clickbait — the article must deliver what the headline promises
- No "the ultimate guide" unless the content is genuinely comprehensive

### 2.3 H2 and H3 Structure

H2s are the skeleton. A reader skimming H2s should understand the article's full argument without reading a word of body text.

**H2 test:** Read only the H2s in sequence. Do they tell a coherent story? If not — restructure.

**H3s:** Sub-points within an H2. They should be parallel in structure where possible (all questions, or all noun phrases, not mixed).

**H2 bans:**
- "Introduction" as an H2 (implied)
- "Conclusion" as an H2 (write a real closing section)
- Vague H2s: "More Information," "Additional Considerations," "Other Points"

---

## 3. Formatting for Digital Reading

### 3.1 Paragraph Length
- 2–4 sentences per paragraph for body content
- 1-sentence paragraphs are permitted for emphasis — but used sparingly
- Single-sentence subheadings followed by a single-sentence paragraph = formatting abuse

### 3.2 Lists and Bullets
- Use when items are genuinely parallel and enumerable
- Minimum 3 items, maximum 8 before considering a table or sub-sections
- Each bullet must be one consistent grammatical structure
- Never use bullets to replace paragraphs that need to be argued, not listed
- **Bullet ban:** Starting every bullet with "This" or "It" (lazy)

### 3.3 Bold and Emphasis
- Bold for the most important phrase in a paragraph — the thing someone skimming should catch
- Maximum one bolded phrase per paragraph
- Never bold full sentences
- Italics for titles, foreign terms, or a single word of specific emphasis

### 3.4 Tables
- Use when comparing 3+ items across 2+ dimensions
- Use when the relationship between items is best communicated as a grid
- Never use a table for content that flows naturally as prose

### 3.5 Images and Media
- Every image needs a specific, descriptive alt text (not "image of man smiling")
- Caption images when they require context
- Don't use stock photos that add nothing. Use images that explain something the text can't.

---

## 4. Article Architecture

### 4.1 The Introduction — 3-Part Structure

The introduction has one job: earn the reader's continued attention by proving this piece is worth their time.

```
[Hook — the specific thing that makes this relevant right now]
[Stakes — what the reader gains or avoids by reading this]
[Scope — exactly what this article covers and doesn't]
```

**Introduction length:** 80–150 words. No longer.

**Introduction bans:**
- Starting with a dictionary definition ("According to Merriam-Webster...")
- Starting with a generic trend statement ("Content marketing is growing rapidly...")
- Promising things the article doesn't deliver
- Recapping what the reader already knows just to fill the introduction

### 4.2 The Body — Section Architecture

Each body section follows:
```
[H2 — standalone claim or topic label]
[Opening sentence — the point of this section stated directly]
[Development — 2-4 paragraphs proving or developing the point]
[Optional H3s — only if the section has 3+ genuine sub-points]
[Transition (optional) — a sentence linking this section to the next]
```

### 4.3 The Closing Section

The close is not a summary. Options:
- **The implication close:** What does all of this mean for the reader going forward?
- **The action close:** Specific next step, stated directly
- **The question close:** Leave the reader with a genuine open question (for thought leadership)
- **The synthesis close:** Draw a non-obvious connection across the sections

**Never:** "In conclusion, we've seen that..." — rewrite as if you're saying one last useful thing, not finishing an essay.

---

## 5. Internal Linking Strategy

For web content that lives in a content ecosystem:

- **3–5 internal links per article** for blog/article content
- Link to content that genuinely deepens understanding — not for linking's sake
- Anchor text = descriptive phrase (not "click here" or "this article")
- Link placement: within body paragraphs at the moment of relevance, not at the end as a list
- Pillar pages get linked from multiple cluster articles — not the other way around

---

## 6. Meta Elements

### 6.1 Meta Title
- 50–60 characters
- Primary keyword near the front
- Matches the intent of what the page actually delivers
- Can differ slightly from the on-page H1 title

### 6.2 Meta Description
- 140–155 characters
- Contains the primary keyword naturally
- Tells the reader what they get, not what the page is about
- Includes a soft CTA where natural ("Learn how," "Find out," "See why")
- Not a sentence fragment

### 6.3 URL Slug
- Lowercase, hyphens, no special characters
- 3–6 words: `/how-to-build-content-calendar`
- Matches the topic, not the full title
- No dates in the slug (unless the content is inherently dated, like a year-in-review)

---

## 7. Content Freshness and Maintenance

Web content ages. Evergreen doesn't mean permanent.

**Update triggers:**
- Statistics are more than 2 years old
- A tool, platform, or method referenced has changed significantly
- A new development makes a claim outdated
- The content ranks but traffic is declining (signal: intent drift)

**Update conventions:**
- Add "Updated [Month Year]" below the title when substantially revised
- Update the dateModified in schema markup
- Don't delete — update in place to preserve backlinks and authority

---

## 8. Web Content Quality Gates

In addition to core quality gates:

**Gate W1 — The H2 Skim Test**
Read only the H2s in sequence. Do they tell a coherent story? If not, restructure.

**Gate W2 — The Paragraph Opening Test**
Read only the first sentence of each paragraph. Does the article make sense? If not — rewrite paragraph openers.

**Gate W3 — The Introduction Delivery Test**
Does the introduction promise something specific? Does the article deliver it? If there's a gap — rewrite the intro or expand the content.

**Gate W4 — The Closing Test**
Does the closing add something new? Or does it repeat what came before? If it repeats — rewrite.

**Gate W5 — The Specificity Scan**
Search for: many, often, some, usually, most, research, experts. Replace each with a specific source or remove.
