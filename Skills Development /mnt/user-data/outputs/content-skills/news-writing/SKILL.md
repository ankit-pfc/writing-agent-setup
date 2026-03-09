---
name: news-writing
description: >
  Subskill for news and journalism-style writing — breaking news, press releases, news articles, 
  event reports, product announcements written in journalistic style, and any content where 
  timeliness, factual precision, and the inverted pyramid structure apply.
  Invoke alongside content-writing-core.
  Use for: news articles, press releases, product/company announcement posts, event reports, 
  industry news roundups, executive Q&As written in news style, research summaries.
  Do NOT use for: opinion pieces or thought leadership (use web-content-writing + writing-masterclass), 
  marketing copy (use marketing-copywriting), or evergreen SEO content (use seo-geo-writing).
version: 1.0
parent: content-writing-core
---

# News Writing

Builds on content-writing-core. All core rules apply. This skill adds the journalism layer — the standards, structures, and precision conventions of professional news writing.

**Core principle of news writing:**  
Tell the reader what happened, who it involves, why it matters, and what comes next — in that order, at that level of precision, with verifiable facts only. Opinion has its own section; it doesn't belong in a news report.

---

## 1. The Inverted Pyramid

The foundational structure of all news writing. Most important information at the top. Supporting details follow. Background and context at the bottom.

```
┌─────────────────────────────────────────────┐
│            THE LEAD (Lede)                  │
│  Who, What, When, Where, Why — the core    │
│  of the story in 1–2 sentences              │
├─────────────────────────────────────────────┤
│           KEY DETAILS                       │
│  Essential context, most important facts    │
│  Quotes that advance the story              │
├─────────────────────────────────────────────┤
│         SUPPORTING INFORMATION              │
│  Secondary facts, additional quotes         │
│  Related developments                       │
├─────────────────────────────────────────────┤
│          BACKGROUND / CONTEXT               │
│  History, definition, broader significance  │
│  (Most expendable — cut from the bottom up) │
└─────────────────────────────────────────────┘
```

**Why this structure:** Editors cut from the bottom. Readers leave from the bottom. The story must survive any truncation point.

---

## 2. The Lead (Lede)

The lead is the most important sentence in a news article. It must:
- State the most newsworthy fact
- Answer as many of the 5 W's as possible (Who, What, When, Where, Why)
- Be one sentence, rarely two
- Be 25–40 words maximum

### 2.1 Lead Types

**Summary Lead (default):** States the news directly.
> Anthropic released Claude 4 on Tuesday, adding real-time web search and an extended 200,000-token context window to its flagship AI assistant.

**Delayed Lead (for features, analysis, longer pieces):** Opens with context or scene, delays the news one sentence.
> For three years, the question was whether AI assistants could replace search. On Tuesday, Anthropic made its answer clear.

**Rule:** Use summary leads for breaking news and announcements. Use delayed leads only for longer features where scene-setting serves the story.

### 2.2 Lead Bans

- Starting with a quote ("According to the company...")
- Starting with a question ("Have you ever wondered...?")
- Starting with the company name or a proper noun before the news (buries the lead)
- Embedding the news in a long preamble
- "Recently," "Today," "Now" as the first word (vague)

---

## 3. The 5 W's and H

Every news story covers these. Not necessarily in a single sentence, but all within the first two paragraphs:

| Element | Question | News example |
|---|---|---|
| Who | Who is involved? | The company / the person / the organization |
| What | What happened? | The event, announcement, development |
| When | When did it happen? | Date, time — always specific |
| Where | Where did it happen? | Location, platform, jurisdiction |
| Why | Why did it happen? | Cause, motivation, stated reason |
| How | How did it happen? | Mechanism, process (often in body, not lede) |

---

## 4. Attribution and Sourcing

### 4.1 Attribution Rules

In journalism, every non-obvious fact has an attribution. The reader must be able to evaluate the quality of every claim by knowing its source.

**Attribution formats:**
- Named source on the record: "According to Ankit Sharma, the company's CTO..."
- Named source with title: "Dr. Priya Mehta, professor of AI ethics at IIT Delhi, said..."
- Named document: "According to the company's earnings release..."
- On-background source (unnamed, with descriptor): "A person familiar with the matter said..."
- Official statement: "In a statement, the company said..."

**Never:** "Sources say" without any descriptor. "Experts believe" without naming them. "Reports suggest" without linking to the reports.

### 4.2 Direct Quotes

Quotes in news stories serve specific jobs:
- To convey a person's position in their own words
- To add human voice to a factual report
- To present contested claims attributed to their speaker (not as verified fact)

**Quote rules:**
- Never change the meaning of a quote when editing it
- "[sic]" for factual errors in the original
- Brackets [ ] for editorial insertions that clarify without changing meaning
- Quotes that simply restate what the text already says = cut them. Every quote must add something the paraphrase doesn't.
- Attribution goes at the first natural pause in a long quote, or at the end for short ones
- "Said" is the neutral attribution verb. Use "said" by default. Only use "argued," "claimed," "alleged" when the characterization is appropriate.

### 4.3 Source Hierarchy

1. Primary sources: official statements, direct interviews, original documents, official data
2. Secondary sources: coverage by credible news organizations, expert commentary
3. Unnamed/background sources: permitted when primary source is unavailable; must include a descriptor and reason for anonymity
4. Social media posts: attribute carefully — they can be deleted. Screenshot and archive.

---

## 5. News Writing Style Conventions

### 5.1 Tense

- **Past tense for reported events:** "The company announced..." not "The company announces..."
- **Present tense for standing facts:** "The company employs 2,000 people."
- **Future tense for stated intentions:** "The company plans to launch in Q3."

### 5.2 Numbers

- **Spell out one through nine.** Use numerals for 10 and above.
- **Exception:** Percentages always numerals (5%, not five percent), money always numerals ($3 million)
- **Large numbers:** "$4.2 million" not "$4,200,000." "2.3 billion" not "2,300,000,000."
- **Ages:** Always numerals. "She is 34."
- **Dates:** Month + Day + Year. "March 12, 2026." Not "12th of March."

### 5.3 Titles and Names

- **Full name on first reference.** Title before name: "Chief Executive Ankit Sharma" or "Ankit Sharma, chief executive."
- **Last name only on subsequent references** (AP style): "Sharma said..."
- **Capitalize formal titles before names.** Lowercase after: "President Biden" but "Joe Biden, president of the United States."

### 5.4 Objectivity and Fairness

- **Both sides of a contested issue** must be represented in the same article, with proportional weight
- **Label opinion clearly.** Analysis and commentary must be identified as such
- **No advocacy language** in news reporting. "The company claims" is more neutral than "the company says" — use "says" unless the claim is contested
- **Loaded language ban in news:** "shocking," "outrageous," "stunning," "slammed," "blasted" — these are opinions, not descriptions

---

## 6. Press Releases — Special Rules

Press releases are a hybrid: written by PR, formatted in news style, intended for journalists to republish or adapt.

### 6.1 Press Release Structure
```
FOR IMMEDIATE RELEASE (or embargo date)
[Date, City] — [Headline]
[Sub-headline]
[Lead paragraph — the news, 5 W's]
[Expansion — context and key details]
[Quote from executive — forward-looking, not just announcing]
[Boilerplate description of company]
[Contact information]
```

### 6.2 Press Release Rules

- The headline must be newsworthy, not marketing copy. "Company Launches New Product" is weak. "Anthropic Releases First AI System With Built-In Constitutional Alignment Layer" is news.
- The lead paragraph should function as a standalone news brief
- The executive quote must say something substantive — not repeat what the paragraphs already say
- Boilerplate ("About [Company]") is always the last paragraph
- No exclamation marks, no superlatives, no marketing language in the news sections

---

## 7. Headlines in News Writing

News headlines differ from web content and marketing headlines:

**News headline rules:**
- State what happened, not what might interest you about it
- Active verb preferred: "Anthropic Releases..." not "New AI Tool Released By Anthropic"
- Present tense for recent events (creates immediacy): "Startup Raises $50M" not "Startup Raised $50M"
- Attribute opinion or contested claims: "Study Links X to Y" not "X Causes Y"
- Avoid ambiguity — news headlines should be immediately clear
- Maximum 10–12 words for print/web news

**Headline bans in news:**
- Question headlines: "Will AI Replace Writers?" (This is commentary, not news)
- Clickbait: "You Won't Believe What This Startup Just Did"
- Misleading: Don't overstate the significance of the story
- Vague: "Big Changes Coming to Tech Industry"

---

## 8. News Writing Quality Gates

In addition to core quality gates:

**Gate N1 — The Lead Test**
Does the first sentence answer at least Who, What, and When? If not — rewrite the lead.

**Gate N2 — The Attribution Test**
Find every non-obvious factual claim. Is each one attributed to a named, verifiable source? Unnamed claims must be flagged.

**Gate N3 — The Inverted Pyramid Test**
If you cut the last third of the article, does the essential story survive? If important information is only in the bottom — restructure.

**Gate N4 — The Objectivity Test**
Find every adjective and adverb. Is each one factual ("a 40% drop") or editorial ("a shocking drop")? Remove or replace editorial characterizations with factual ones.

**Gate N5 — The Quote Audit**
For each direct quote: (a) Is it attributed correctly? (b) Does it add something the paraphrase doesn't? (c) Is the attribution verb appropriate? Remove or paraphrase quotes that fail any of these.

**Gate N6 — The Fairness Test**
If the story involves a contested claim or negative coverage of a named person or organization: has their position or response been sought and included? If not — note it explicitly ("[Company] did not respond to a request for comment").
