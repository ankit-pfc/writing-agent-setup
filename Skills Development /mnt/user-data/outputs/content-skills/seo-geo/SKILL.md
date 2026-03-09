---
name: seo-geo-writing
description: >
  Subskill for search-optimized and LLM-indexable content writing. Covers both traditional SEO 
  (Google, Bing rankings) and GEO/AEO (Generative Engine Optimization — getting cited by ChatGPT, 
  Perplexity, Claude, Gemini in AI-generated responses). Invoke alongside content-writing-core and 
  web-content-writing. This skill adds: keyword integration, topical authority architecture, E-E-A-T 
  signals, semantic structure, FAQ and schema patterns, and LLM-specific formatting conventions.
  Use for: any content intended to rank in search OR be cited by AI engines.
  GEO and SEO are not in conflict — GEO is an extension of SEO.
version: 1.0
parent: content-writing-core
companion: web-content-writing
---

# SEO + GEO Writing

Builds on content-writing-core and web-content-writing. All parent rules apply. This skill adds the search and AI-citation optimization layer — how to write content that both ranks in Google and gets cited as a source by LLMs like ChatGPT, Claude, Perplexity, and Gemini.

**Core mental model:**  
SEO = "Help search engines find and rank this page."  
GEO = "Help LLMs understand, trust, and cite this page in their answers."  
Both reward the same thing: clear, structured, authoritative, specific content.

---

## 1. The GEO/LLM Paradigm Shift

Traditional SEO optimizes for position in a ranked list of links. GEO optimizes for citation frequency in AI-generated responses. Key differences:

| Dimension | Traditional SEO | GEO / LLM Optimization |
|---|---|---|
| Goal | Rank #1 for target keyword | Be cited across many relevant AI responses |
| Ranking signal | Keywords, backlinks, CTR | Clarity, completeness, authority, structure |
| User behavior | Click through to website | May receive answer without clicking |
| Success metric | Organic traffic, position | AI citation share, mention frequency |
| Content structure | Keyword density, headers | Modular sections, direct answers, schema |
| Freshness | Crawl recency | dateModified schema, explicit recency signals |

Both strategies share the same foundation: high-quality, accurate, well-structured, authoritative content. GEO rewards those properties more aggressively.

---

## 2. Keyword Strategy — Integration Rules

### 2.1 Keyword Placement (SEO)

| Location | Rule |
|---|---|
| Title / H1 | Primary keyword, as close to the front as natural |
| First 100 words | Primary keyword used once, naturally |
| H2s | 1–2 H2s should contain primary or secondary keywords |
| Body | Primary keyword: 1–2 uses per 500 words. Never force. |
| Meta title | Primary keyword first 50 characters |
| Meta description | Primary keyword once, naturally |
| Image alt text | Descriptive, includes keyword where natural |
| URL slug | Primary keyword in slug |

### 2.2 Semantic Coverage (GEO)

LLMs don't just scan for keywords — they evaluate topical completeness. A page about "vipassanā meditation" should naturally cover: technique, origins, benefits, how it differs from other meditation types, common challenges. **If the page answers sub-questions the reader would logically have, it ranks and gets cited better.**

**Semantic coverage protocol:**
1. Identify the primary topic
2. List 8–12 questions someone researching this topic would have
3. Ensure the content answers at least 6–8 of them, either as sections or within the body

### 2.3 Keyword Bans
- Never repeat a keyword awkwardly to hit density targets
- Never use exact-match keywords in unnatural sentence constructions
- Never stuff keywords into H2s at the cost of headline clarity
- Never use keyword variants (LSI) at the expense of accurate terminology

---

## 3. Content Architecture for LLM Citation

LLMs use RAG (Retrieval-Augmented Generation) — they break queries into sub-questions, retrieve relevant passages, and synthesize answers. This means:

**Each section must be able to stand alone as an answer.** LLMs don't always read the full article — they extract the most relevant section. Every major section should be self-contained: it states its claim, supports it, and can be understood without requiring context from other sections.

### 3.1 The Answer-First Structure

For any section addressing a specific question:
```
[Question (as H2 or H3 — phrased as the user would ask it)]
[Direct answer — 1-2 sentences that fully answer the question]
[Context and development — 2-4 sentences of supporting detail]
[Optional: example, data point, or source citation]
```

This mirrors the way LLMs extract and present information. When your content is structured this way, it becomes the natural pull source.

### 3.2 TL;DR and Summary Blocks

For long-form content, include a 40–60 word TL;DR block near the top:
```
**TL;DR:** [The single most important thing this article establishes, stated in 1-2 sentences.]
```

LLMs treating the content as a RAG source will frequently pull from this block. It also improves featured snippet chances.

### 3.3 Modular Section Design

Each major section should:
- Begin with a direct statement (not a transition from the previous section)
- Include at least one specific, citable data point or named source
- Use consistent terminology throughout (LLMs reward terminological consistency — it signals subject mastery)
- End cleanly (not trail into the next section)

---

## 4. E-E-A-T Signals (Experience, Expertise, Authoritativeness, Trustworthiness)

Google and LLMs both weight E-E-A-T signals heavily. These are content-level signals, not just technical signals.

### 4.1 Experience Signals
- First-hand observations, personal data, case studies from actual experience
- "In our testing of X across 6 months..." vs. "Experts suggest..."
- Original insights that can only come from having done the thing

### 4.2 Expertise Signals
- Correct technical vocabulary used with precision
- Nuance — acknowledging where the topic gets complicated
- Explicit limitations of the advice ("This approach works when X; it doesn't work when Y")
- Citing named sources (not just "studies show")

### 4.3 Authority Signals
- Author bio with relevant credentials or experience (on the page)
- Outbound links to authoritative sources (.edu, .gov, peer-reviewed, reputable journalism)
- Internal linking to a content cluster that demonstrates breadth on the topic
- Third-party mentions and citations (this requires off-page strategy, but content quality drives it)

### 4.4 Trustworthiness Signals
- Dates visible — when was this written, when was it last updated?
- No sponsored content presented as editorial without disclosure
- Acknowledging uncertainty where uncertainty exists ("As of March 2026, this is the current understanding — this field is evolving")
- Sources cited in-text, not just a reference list at the bottom

---

## 5. FAQ Section Design

FAQ sections are among the highest-value GEO elements. LLMs and AI Overviews extract directly from well-structured FAQ content.

### 5.1 FAQ Rules

- 6–10 questions per FAQ section
- Questions must be phrased as a real user would search or ask (conversational, complete sentences)
- Each answer: 40–80 words, standalone, complete
- Questions progress from basic to complex, or general to specific
- No duplicate coverage of what's already in the main body — FAQs should add, not repeat
- FAQ schema markup should accompany this section (see Section 6)

### 5.2 FAQ Question Patterns That Get Cited

| Pattern | Example |
|---|---|
| What is [X]? | What is generative engine optimization? |
| How does [X] work? | How does LLM citation selection work? |
| What is the difference between [X] and [Y]? | What is the difference between SEO and GEO? |
| When should I [do X]? | When should I use structured data markup? |
| What are the [benefits/risks/steps] of [X]? | What are the main GEO ranking factors? |
| Is [X] still [valid/relevant/effective]? | Is keyword density still a ranking factor? |
| How long does [X] take? | How long does it take for GEO changes to show results? |

---

## 6. Schema Markup Reference

Schema tells LLMs and search engines what your content *means*. Content types and their recommended schema:

| Content Type | Schema Type | Key Properties |
|---|---|---|
| Blog post / Article | `Article` | headline, author, datePublished, dateModified, image |
| FAQ section | `FAQPage` + `Question` + `Answer` | Each Q&A pair as acceptedAnswer |
| How-to content | `HowTo` | steps, estimatedCost, totalTime |
| Product page | `Product` | name, description, price, review |
| Person / Author | `Person` | name, jobTitle, affiliation, sameAs |
| Organization | `Organization` | name, url, logo, contactPoint |
| Event | `Event` | name, startDate, location, organizer |

**Critical for GEO:** `dateModified` in Article schema signals freshness — update it every time you substantially revise content.

---

## 7. Technical GEO Checklist

These are technical requirements for content to be LLM-crawlable and citable:

- [ ] Content is server-side rendered (not behind JavaScript that AI crawlers can't execute)
- [ ] Page is not blocked by robots.txt for major AI crawlers (GPTBot, ClaudeBot, PerplexityBot)
- [ ] Important content is not behind login, paywall, or interactive form
- [ ] `llms.txt` file exists at root to guide AI crawlers (analogous to robots.txt for LLMs)
- [ ] Schema markup implemented and validated
- [ ] dateModified updated on each substantial revision
- [ ] Sitemap updated and submitted when new content goes live
- [ ] Page loads in under 3 seconds (AI crawlers also penalize slow pages)
- [ ] HTTPS (TLS) — AI crawlers don't crawl HTTP

---

## 8. Recency and Freshness Signals

LLMs preferentially select current information — content from the last 1–2 years ranks higher for citation than older material on the same topic.

**Freshness writing patterns:**
- Include the year in content where it adds specificity: "As of 2026, the most widely-cited approach is..."
- Update statistics with their year: "A 2025 Gartner study found..." not "A recent study found..."
- When covering evolving topics, explicitly acknowledge currency: "This reflects the state as of Q1 2026 — this space is changing rapidly."
- Implement update timestamps on the page — visible to readers and readable by crawlers

---

## 9. Internal Linking for Topical Authority

Strengthening internal linking demonstrates topic authority to both search engines and LLMs evaluating whether to trust a domain.

**Topical cluster structure:**
```
Pillar page (comprehensive coverage of main topic)
├── Cluster article 1 (deep dive on sub-topic A)
├── Cluster article 2 (deep dive on sub-topic B)
├── Cluster article 3 (deep dive on sub-topic C)
└── FAQ page (answers the questions all of the above generate)
```

Every cluster article links back to the pillar. The pillar links out to all cluster articles. This signals to LLMs that your domain is the authoritative hub for this topic.

---

## 10. SEO/GEO Quality Gates

In addition to core and web-content quality gates:

**Gate S1 — The Standalone Section Test**
Take any section out of context. Can it stand as a complete answer to the question it addresses? If not — add the missing context.

**Gate S2 — The Specificity-Source Test**
Every statistic, percentage, or named finding has a source named inline. No naked numbers.

**Gate S3 — The FAQ Coverage Test**
Have 6–10 genuine questions a real person would ask about this topic been addressed — either in the body or in the FAQ section?

**Gate S4 — The Schema Check**
Appropriate schema markup exists and has been validated. dateModified is current.

**Gate S5 — The Terminology Consistency Test**
Pick the 3 most important terms in the article. Are they used consistently throughout? Or do synonyms create ambiguity? LLMs reward terminological precision — it signals domain mastery.
