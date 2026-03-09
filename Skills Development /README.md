# Content Writing Skill Architecture

A layered system for production-grade content generation across all writing contexts. One foundational skill, five specialized subskills.

---

## Architecture Overview

```
content-writing-core/          ← Foundational. Always active.
│   Universal clarity rules, audience calibration,
│   research standards, quality gates, banned phrases
│
├── web-content-writing/       ← Blogs, guides, evergreen articles
│       Digital reading behavior, headline mechanics,
│       H2 architecture, formatting, meta elements
│
├── seo-geo-writing/           ← Search + LLM citation optimization
│       Keyword integration, GEO/AEO structure,
│       E-E-A-T signals, FAQ design, schema markup,
│       LLM-indexable formatting (2026 standards)
│
├── marketing-copywriting/     ← Email, ads, product copy, campaigns
│       Awareness ladder, AIDA/PAS/PASTOR frameworks,
│       objection handling, social proof architecture
│
├── landing-page-writing/      ← Conversion pages, single-goal CRO
│       Hero mechanics, value proposition clarity,
│       CTA design, pricing copy, page length decisions
│
└── news-writing/              ← Journalism, press releases, announcements
        Inverted pyramid, AP style, attribution rules,
        objectivity standards, press release structure
```

---

## How to Invoke

### Single task (most common)
> "Write a blog post about X"
→ Invoke: `content-writing-core` + `web-content-writing`

> "Write an SEO article about X for both Google and AI citation"
→ Invoke: `content-writing-core` + `web-content-writing` + `seo-geo-writing`

> "Write a landing page for X"
→ Invoke: `content-writing-core` + `marketing-copywriting` + `landing-page-writing`

> "Write a press release for X"
→ Invoke: `content-writing-core` + `news-writing`

> "Write email copy for X campaign"
→ Invoke: `content-writing-core` + `marketing-copywriting`

### Combined tasks
> "Write a full-funnel content piece — SEO article that drives to a landing page"
→ Invoke: `content-writing-core` + `web-content-writing` + `seo-geo-writing` (for article)
→ Then: `content-writing-core` + `marketing-copywriting` + `landing-page-writing` (for page)

### Character content
> "Write a Sādhak X thread about abhyāsa"
→ Invoke: `sadhak-writing` (which inherits from `writing-masterclass`)
→ `content-writing-core` principles apply but character skill takes precedence on voice/vocabulary

---

## Skill Combination Rules

| Primary task | Core | Web | SEO/GEO | Mktg Copy | Landing | News |
|---|---|---|---|---|---|---|
| Blog / article | ✅ | ✅ | Optional | — | — | — |
| SEO + GEO optimized | ✅ | ✅ | ✅ | — | — | — |
| Email campaign | ✅ | — | — | ✅ | — | — |
| Ad copy | ✅ | — | — | ✅ | — | — |
| Landing page | ✅ | — | — | ✅ | ✅ | — |
| Press release | ✅ | — | — | — | — | ✅ |
| News article | ✅ | — | — | — | — | ✅ |
| Product description | ✅ | — | Optional | ✅ | — | — |
| Knowledge base / FAQ | ✅ | ✅ | ✅ | — | — | — |
| Thought leadership | ✅ | ✅ | Optional | — | — | — |

---

## Relationship to Character Skills

The character skills (Sādhak, Eitan Lev) and the writing masterclass operate alongside this architecture, not inside it.

| Skill | Primary focus | Relationship to this architecture |
|---|---|---|
| `writing-masterclass` | Ankit's voice synthesis + master style library | Peer of content-writing-core — provides the voice layer |
| `sadhak-writing` | Sādhak character for X/Twitter | Overrides voice/vocabulary from core; quality gates from core still apply |
| `eitan-lev-writing` | Eitan Lev character for X/Twitter | Same as above |

When generating character content, character skills take precedence on voice, vocabulary, and structure. The universal quality gates from `content-writing-core` still apply.

---

## File Structure

```
content-skills/
├── README.md                          ← This file
├── core/
│   └── SKILL.md                       ← content-writing-core
├── web-content/
│   └── SKILL.md                       ← web-content-writing
├── seo-geo/
│   └── SKILL.md                       ← seo-geo-writing
├── marketing-copywriting/
│   └── SKILL.md                       ← marketing-copywriting
├── landing-page/
│   └── SKILL.md                       ← landing-page-writing
└── news-writing/
    └── SKILL.md                       ← news-writing
```
