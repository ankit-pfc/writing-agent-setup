# SEO, AEO & Agent Skills Replication Guide

**Purpose:** This document provides a complete blueprint for replicating the SEO, Answer Engine Optimization (AEO), and agent skills system from the Sadhaka project to any new project with the same depth, relevance, and workflows.

**Last Updated:** 2026-03-09  
**Source Project:** opensadhaka.com (Sadhaka)

---

## Table of Contents

1. [Architecture Overview](#1-architecture-overview)
2. [Skills System](#2-skills-system)
3. [Workflows System](#3-workflows-system)
4. [Technical SEO Implementation](#4-technical-seo-implementation)
5. [LLM/AI Discovery Layer](#5-llmai-discovery-layer)
6. [Answer Engine Optimization (AEO)](#6-answer-engine-optimization-aeo)
7. [Indexing Infrastructure](#7-indexing-infrastructure)
8. [Content Strategy Framework](#8-content-strategy-framework)
9. [Analytics & Measurement](#9-analytics--measurement)
10. [Recurring Operations System](#10-recurring-operations-system)
11. [Step-by-Step Replication Checklist](#11-step-by-step-replication-checklist)

---

## 1. Architecture Overview

### Directory Structure

```
project-root/
├── .agents/
│   ├── skills/                    # Individual skill definitions
│   │   ├── seo-audit/
│   │   │   ├── SKILL.md           # Main skill file
│   │   │   └── references/        # Supporting reference docs
│   │   ├── answer-engine-optimization/
│   │   ├── llm-indexing/
│   │   ├── content-strategy/
│   │   └── [other-skills]/
│   └── workflows/                 # Multi-step workflow definitions
│       ├── answer-engine-optimization.md
│       └── seo-content-publishing.md
├── public/
│   └── .well-known/
│       └── brand-facts.json       # Machine-readable brand data
├── src/app/
│   ├── llms.txt/route.ts          # LLM discovery endpoint
│   ├── llms-full.txt/route.ts     # Extended LLM URL map
│   ├── brand-facts/page.tsx       # Human-readable brand facts
│   ├── robots.ts                  # Robots.txt with AI crawler rules
│   ├── sitemap.ts                 # Dynamic sitemap generation
│   └── api/
│       ├── indexnow/route.ts      # IndexNow key verification
│       └── indexnow/submit/route.ts # URL submission endpoint
└── plans/
    ├── seo-aeo-geo-status-scorecard.md
    ├── seo-recurring-operations-tracker.md
    └── seo-content-strategy-[project].md
```

### Key Concepts

| Concept | Definition |
|---------|------------|
| **Skill** | A single-purpose capability with specific triggers, instructions, and references |
| **Workflow** | A multi-step process that orchestrates multiple skills |
| **AEO** | Answer Engine Optimization - optimizing for AI assistants to cite/recommend |
| **GEO** | Generative Engine Optimization - making content retrievable by AI systems |
| **llms.txt** | A standard file for LLM crawlers to understand site structure |

---

## 2. Skills System

### 2.1 Skill File Structure

Every skill resides in `.agents/skills/{skill-name}/` and contains:

```
.agents/skills/{skill-name}/
├── SKILL.md              # Required: Main skill definition
└── references/           # Optional: Supporting documents
    ├── template.md
    ├── guide.md
    └── examples.md
```

### 2.2 SKILL.md Format

```markdown
---
name: skill-name
version: 1.0.0
description: When to use this skill. Include trigger phrases and keywords.
---

# Skill Title

You are an expert in [domain]. Your goal is to [objective].

## Initial Assessment

**Check for product marketing context first:**
If `.claude/product-marketing-context.md` exists, read it before asking questions.

[Additional context gathering steps...]

## Core Framework

### Priority Order
1. First priority area
2. Second priority area
3. Third priority area

### Detailed Sections

[Main skill content organized by topic...]

## Output Format

### Report Structure
- Executive Summary
- Detailed Findings
- Prioritized Action Plan

## References

- [Reference Name](references/file-name.md): Description

## Task-Specific Questions

1. Question about context?
2. Question about goals?

## Related Skills

- **related-skill-1**: When to use
- **related-skill-2**: When to use
```

### 2.3 Core SEO/AEO Skills to Replicate

#### SEO Audit Skill
**Location:** `.agents/skills/seo-audit/SKILL.md`

**Purpose:** Comprehensive SEO auditing for technical, on-page, and content issues.

**Key Sections:**
- Initial Assessment (context gathering)
- Audit Framework (Priority Order)
- Technical SEO Audit (Crawlability, Indexation, Speed, Mobile, Security)
- On-Page SEO Audit (Titles, Meta, Headings, Content, Images, Internal Links)
- Content Quality Assessment (E-E-A-T, Depth, Engagement)
- Common Issues by Site Type
- Output Format (Executive Summary, Findings, Action Plan)

**References to Include:**
- `references/aeo-geo-patterns.md` - Content patterns for AI optimization
- `references/ai-writing-detection.md` - Patterns to avoid in AI-generated content

#### Answer Engine Optimization Skill
**Location:** `.agents/skills/answer-engine-optimization/SKILL.md`

**Purpose:** Optimize content for AI assistants to cite and recommend.

**Key Sections:**
- Core Pillars of AEO (6 pillars)
- Execution Strategy (workflow reference)
- References to templates

**References to Include:**
- `references/brand-facts-template.md` - JSON structure for brand-facts.json

#### LLM Indexing Skill
**Location:** `.agents/skills/llm-indexing/SKILL.md`

**Purpose:** Set up LLM discoverability and fast indexing infrastructure.

**Key Sections:**
- LLM Discovery (llms.txt standard)
- Crawler Access (robots.txt for AI bots)
- Fast Indexing Infrastructure (IndexNow, Google Indexing API)
- Submitting to LLM Directories

**References to Include:**
- `references/llms-txt-template.md` - Template for llms.txt
- `references/llm-crawlers.md` - List of AI crawler user agents

#### Content Strategy Skill
**Location:** `.agents/skills/content-strategy/SKILL.md`

**Purpose:** Plan content that drives traffic, builds authority, and generates leads.

**Key Sections:**
- Searchable vs Shareable content
- Content Types (Use-Case, Hub/Spoke, Templates, Thought Leadership)
- Content Pillars and Topic Clusters
- Keyword Research by Buyer Stage
- Content Ideation Sources
- Prioritizing Content Ideas (scoring framework)
- Output Format

### 2.4 Skill Creation Best Practices

1. **Frontmatter is Critical**
   - `name`: Must match the directory name
   - `description`: Include trigger phrases for automatic skill selection

2. **Structure for LLM Consumption**
   - Use clear headings and bullet points
   - Include explicit "When to use" guidance
   - Reference other skills for handoffs

3. **Include Reference Files**
   - Templates for repetitive outputs
   - Checklists for validation
   - Examples for complex patterns

4. **Make Skills Composable**
   - Skills should be focused on one domain
   - Use "Related Skills" section for handoffs
   - Workflows orchestrate multiple skills

---

## 3. Workflows System

### 3.1 Workflow File Structure

Workflows reside in `.agents/workflows/` as single Markdown files:

```
.agents/workflows/
├── answer-engine-optimization.md
├── seo-content-publishing.md
└── [other-workflows].md
```

### 3.2 Workflow Format

```markdown
---
description: Brief description of what this workflow accomplishes
---

# Workflow Title

Use this workflow when [trigger conditions].

## Phase 1: [Phase Name]

1. Step one
2. Step two
3. Step three

## Phase 2: [Phase Name]

1. Step one
2. Step two

## Phase N: [Final Phase]

1. Final steps
2. Validation steps
```

### 3.3 Core Workflows to Replicate

#### Answer Engine Optimization Workflow
**Location:** `.agents/workflows/answer-engine-optimization.md`

**Phases:**
1. **Answer Intent Research** - Identify queries, map current AI responses
2. **Create the Answer Hub** - Structured recommendation page
3. **Create Brand-Facts Page** - Wikipedia-style neutral facts
4. **Machine-Readable Data** - brand-facts.json implementation
5. **Implement Specific Schema** - ItemList, FAQPage, Organization, Product
6. **Earning Third-Party Citations** - External validation strategy
7. **GPT Shopping Eligibility** - Product identifier setup

#### SEO Content Publishing Workflow
**Location:** `.agents/workflows/seo-content-publishing.md`

**Steps:**
1. **Research and Plan** - Intent analysis, competitor research, outline
2. **Set Keyword Strategy** - Primary, secondary, semantic keywords
3. **Implement Self-Improvement Loop** - lessons.md for continuous improvement
4. **Draft and Verify** - Content creation with validation checklist
5. **Autonomous SEO Fixing** - Direct fixes without hand-holding

---

## 4. Technical SEO Implementation

### 4.1 Robots.txt (robots.ts for Next.js)

**File:** `src/app/robots.ts`

```typescript
import { MetadataRoute } from "next";

export default function robots(): MetadataRoute.Robots {
  const baseUrl = "https://yourdomain.com";
  return {
    rules: [
      {
        userAgent: "*",
        allow: "/",
        disallow: ["/variant-*", "/admin", "/private"],
      },
      // Standard search crawlers
      { userAgent: "Googlebot", allow: "/" },
      { userAgent: "Bingbot", allow: "/" },
      // Social crawlers
      { userAgent: "Twitterbot", allow: "/" },
      { userAgent: "facebookexternalhit", allow: "/" },
      // AI/LLM crawlers (critical for AEO)
      { userAgent: "GPTBot", allow: "/" },
      { userAgent: "ClaudeBot", allow: "/" },
      { userAgent: "PerplexityBot", allow: "/" },
      { userAgent: "GoogleOther", allow: "/" },
      { userAgent: "anthropic-ai", allow: "/" },
      { userAgent: "cohere-ai", allow: "/" },
      { userAgent: "CCBot", allow: "/" },
    ],
    sitemap: [
      `${baseUrl}/sitemap.xml`,
      `${baseUrl}/llms.txt`,
      `${baseUrl}/llms-full.txt`,
    ],
  };
}
```

**Key Points:**
- Explicitly allow all major AI crawlers
- Include llms.txt in sitemap references
- Block test/variant pages from indexing

### 4.2 Sitemap (sitemap.ts for Next.js)

**File:** `src/app/sitemap.ts`

```typescript
import { MetadataRoute } from "next";

export default function sitemap(): MetadataRoute.Sitemap {
  const baseUrl = "https://yourdomain.com";
  
  // Group URLs by type for organized indexing
  const corePages = [/* ... */];
  const contentPages = [/* ... */];
  const programmaticPages = [/* ... */];
  
  return [
    ...corePages.map(url => ({
      url: `${baseUrl}${url}`,
      lastModified: new Date(),
      changeFrequency: 'weekly' as const,
      priority: 1,
    })),
    ...contentPages.map(url => ({
      url: `${baseUrl}${url}`,
      lastModified: new Date(),
      changeFrequency: 'monthly' as const,
      priority: 0.8,
    })),
    // ... more groups
  ];
}
```

**Best Practices:**
- Split into logical groups (core, content, programmatic)
- Set appropriate changeFrequency and priority
- Include all indexable URLs

### 4.3 Layout Metadata

**File:** `src/app/layout.tsx`

```typescript
export const metadata: Metadata = {
  metadataBase: new URL("https://yourdomain.com"),
  title: { default: "Site Name", template: "%s | Site Name" },
  description: "Site description",
  robots: {
    index: true,
    follow: true,
  },
  openGraph: {
    type: "website",
    locale: "en_US",
    url: "https://yourdomain.com",
    siteName: "Site Name",
  },
  twitter: {
    card: "summary_large_image",
  },
  verification: {
    google: process.env.NEXT_PUBLIC_GSC_VERIFICATION,
  },
  // Organization schema
  other: {
    "script:ld+json": JSON.stringify({
      "@context": "https://schema.org",
      "@type": "Organization",
      name: "Brand Name",
      url: "https://yourdomain.com",
      // ... more properties
    }),
  },
};
```

---

## 5. LLM/AI Discovery Layer

### 5.1 llms.txt Route

**File:** `src/app/llms.txt/route.ts`

```typescript
import { NextResponse } from "next/server";

export async function GET() {
  const content = `# Site Name

> Brief 1-2 sentence summary of what the site is about. This helps LLMs understand the context.

## Core Pages
- [Home](https://yourdomain.com): Main entry point
- [About](https://yourdomain.com/about): Company information
- [Features](https://yourdomain.com/features): Core product features

## Content Categories
- [Category 1](https://yourdomain.com/category1): Description
- [Category 2](https://yourdomain.com/category2): Description

## Key Resources
- [Resource 1](https://yourdomain.com/resource1): Description
- [Resource 2](https://yourdomain.com/resource2): Description

## Optional
- [Full URL List](https://yourdomain.com/llms-full.txt): Complete URL map
- [Brand Facts JSON](https://yourdomain.com/.well-known/brand-facts.json): Machine-readable data
`;

  return new NextResponse(content, {
    headers: {
      "Content-Type": "text/plain; charset=utf-8",
      "Cache-Control": "public, max-age=86400, s-maxage=86400, stale-while-revalidate=43200",
    },
  });
}
```

**llms.txt Format Requirements:**
1. Must start with H1 (site name)
2. Must have blockquote (>) with site summary
3. Use H2 headers to separate content categories
4. Use Markdown links: `- [Title](URL): Description`

### 5.2 llms-full.txt Route

**File:** `src/app/llms-full.txt/route.ts`

For larger sites, provide a flattened list of all URLs:

```typescript
import { NextResponse } from "next/server";

export async function GET() {
  // Generate from your data sources
  const urls = getAllSiteUrls();
  
  const content = `# Site Name - Full URL List

> Complete list of all indexed URLs on the site.

${urls.map(url => `- [${url}](${url})`).join('\n')}
`;

  return new NextResponse(content, {
    headers: {
      "Content-Type": "text/plain; charset=utf-8",
      "Cache-Control": "public, max-age=86400",
    },
  });
}
```

### 5.3 LLM Content API (Optional)

**File:** `src/app/api/llm-content/route.ts`

Provides structured markdown content for specific entities:

```typescript
import { NextRequest, NextResponse } from "next/server";

export async function GET(request: NextRequest) {
  const { searchParams } = new URL(request.url);
  const type = searchParams.get("type"); // e.g., "concept", "article"
  const slug = searchParams.get("slug");

  if (!type || !slug) {
    return NextResponse.json({ error: "Missing type or slug" }, { status: 400 });
  }

  // Fetch content and convert to markdown
  const content = await getMarkdownContent(type, slug);

  return new NextResponse(content, {
    headers: {
      "Content-Type": "text/markdown; charset=utf-8",
      "Cache-Control": "public, max-age=3600",
    },
  });
}
```

---

## 6. Answer Engine Optimization (AEO)

### 6.1 Brand Facts JSON

**File:** `public/.well-known/brand-facts.json`

```json
{
  "name": "Brand Name",
  "website": "https://yourdomain.com",
  "category": "Primary category description",
  "description": "1-2 sentence brand description",
  "primaryAudience": [
    "Audience segment 1",
    "Audience segment 2"
  ],
  "heroOffers": [
    {
      "id": "offer-1",
      "name": "Offer Name",
      "type": "offer type",
      "url": "https://yourdomain.com/offer",
      "description": "Offer description"
    }
  ],
  "contentCoverage": [
    "Topic area 1",
    "Topic area 2"
  ],
  "trustSignals": {
    "activeUsers": "X+",
    "rating": "X.X/5"
  },
  "socialProfiles": [
    "https://twitter.com/brand",
    "https://instagram.com/brand"
  ],
  "discoveryAssets": [
    "https://yourdomain.com/brand-facts",
    "https://yourdomain.com/llms.txt"
  ],
  "language": "en",
  "regionsServed": ["Global"],
  "lastUpdated": "2026-03-09"
}
```

### 6.2 Brand Facts Page

**File:** `src/app/brand-facts/page.tsx`

Create a human-readable version with:
- TL;DR summary
- Core facts (name, website, category, audience)
- Primary offerings
- Trust signals
- Knowledge areas covered
- Discovery assets
- FAQ section
- Schema markup (Organization, AboutPage, FAQPage)

**Key Schema Implementations:**

```typescript
const organizationSchema = {
  "@context": "https://schema.org",
  "@type": "Organization",
  name: "Brand Name",
  url: "https://yourdomain.com",
  description: "Brand description",
  sameAs: socialProfiles,
  knowsAbout: knowledgeAreas,
};

const faqSchema = {
  "@context": "https://schema.org",
  "@type": "FAQPage",
  mainEntity: faqItems.map(faq => ({
    "@type": "Question",
    name: faq.question,
    acceptedAnswer: {
      "@type": "Answer",
      text: faq.answer,
    },
  })),
};
```

### 6.3 Answer Hub Pages

For recommendation-style queries, create structured pages:

**URL Pattern:** `/guides/best-[category]-[year]` or `/best-[category]-for-[use-case]`

**Required Sections:**
1. **TL;DR** (60-90 words, neutral, factual, recommendation-style)
2. **Ranked List** (5-7 options with justifications)
3. **Comparison Table** (specs, features, pricing)
4. **How to Choose** (3-5 practical bullets)
5. **FAQ Section** (5-8 questions from Answer Intent Map)
6. **Citations** (5+ authoritative external sources)
7. **CTA** (link to your product)

### 6.4 AEO Content Patterns

Include these patterns in content (from `references/aeo-geo-patterns.md`):

| Pattern Type | Use Case | Structure |
|-------------|----------|-----------|
| Definition Block | "What is X?" | 1-sentence definition + expansion + context |
| Step-by-Step Block | "How to X" | Numbered steps with clear actions |
| Comparison Table | "X vs Y" | Feature comparison with bottom line |
| Pros/Cons Block | "Is X worth it?" | Balanced evaluation with verdict |
| FAQ Block | Topic pages | Question + direct answer (50-100 words) |
| Listicle Block | "Best X" | Numbered items with justifications |

---

## 7. Indexing Infrastructure

### 7.1 IndexNow Key Verification

**File:** `src/app/api/indexnow/route.ts`

```typescript
import { NextResponse } from "next/server";

export const dynamic = "force-dynamic";

export async function GET() {
  const key = process.env.INDEXNOW_KEY;

  if (!key) {
    return new NextResponse("INDEXNOW_KEY not configured", { status: 404 });
  }

  return new NextResponse(key, {
    headers: {
      "Content-Type": "text/plain; charset=utf-8",
      "Cache-Control": "no-store, max-age=0",
    },
  });
}
```

**Next.config Rewrite:**

```typescript
// next.config.ts
const nextConfig = {
  async rewrites() {
    const key = process.env.INDEXNOW_KEY;
    if (!key) return [];
    
    return [
      {
        source: `/${key}.txt`,
        destination: '/api/indexnow',
      },
    ];
  },
};
```

### 7.2 IndexNow Submission Endpoint

**File:** `src/app/api/indexnow/submit/route.ts`

```typescript
import { NextRequest, NextResponse } from "next/server";

export const dynamic = "force-dynamic";

const INDEXNOW_PROVIDERS = [
  { name: "bing", endpoint: "https://www.bing.com/indexnow" },
  { name: "yandex", endpoint: "https://yandex.com/indexnow" },
];

export async function POST(request: NextRequest) {
  // 1. Validate auth (optional)
  // 2. Extract URLs from payload
  // 3. Normalize and validate URLs
  // 4. Submit to each provider
  // 5. Return results with Search Console links

  const key = process.env.INDEXNOW_KEY;
  const siteOrigin = process.env.NEXT_PUBLIC_SITE_URL;
  
  const payload = await request.json();
  const urls = payload.urls || [payload.url];
  
  const results = [];
  for (const url of urls) {
    const providerResults = await Promise.all(
      INDEXNOW_PROVIDERS.map(provider => submitToProvider(url, key, provider))
    );
    results.push({ url, providers: providerResults });
  }

  return NextResponse.json({
    submittedUrls: urls.length,
    results,
    searchConsole: {
      requestIndexingLinks: urls.map(url => ({
        url,
        inspectUrl: buildSearchConsoleInspectUrl(url),
      })),
    },
  });
}
```

### 7.3 Environment Variables Required

```bash
# .env
INDEXNOW_KEY=your-min-8-char-alphanumeric-key
INDEXNOW_SUBMIT_TOKEN=optional-auth-token-for-submission
NEXT_PUBLIC_SITE_URL=https://yourdomain.com
GSC_PROPERTY=sc-domain:yourdomain.com
NEXT_PUBLIC_GSC_VERIFICATION=your-verification-code
```

---

## 8. Content Strategy Framework

### 8.1 Content Pillars

Define 3-5 core content pillars:

1. **Product-led**: Problems your product solves
2. **Audience-led**: What your ICP needs to learn
3. **Search-led**: Topics with search volume
4. **Competitor-led**: What competitors rank for

### 8.2 Pillar Structure

```
Pillar Topic (Hub)
├── Subtopic Cluster 1
│   ├── Article A
│   ├── Article B
│   └── Article C
├── Subtopic Cluster 2
│   ├── Article D
│   └── Article E
└── Subtopic Cluster 3
    └── Article F
```

### 8.3 Keyword Research by Stage

| Stage | Modifiers | Example |
|-------|-----------|---------|
| Awareness | "what is", "how to", "guide" | "What is Vedanta" |
| Consideration | "best", "top", "vs", "alternatives" | "Best meditation style" |
| Decision | "pricing", "reviews", "demo" | "Sadhaka reviews" |
| Implementation | "templates", "tutorial", "setup" | "How to start japa" |

### 8.4 Content Scoring Framework

| Factor | Weight | Questions |
|--------|--------|-----------|
| Customer Impact | 40% | Frequency? Pain point intensity? LTV? |
| Content-Market Fit | 30% | Product alignment? Unique insights? |
| Search Potential | 20% | Volume? Competition? Trends? |
| Resources | 10% | Expertise available? Research needed? |

---

## 9. Analytics & Measurement

### 9.1 Key Events to Track

**SEO Content Events:**
- `seo_article_read` - Article engagement
- `cta_click` - Call-to-action clicks
- `path_explore` - Topic/path exploration

**Conversion Funnel Events:**
- `[product]_start` - Entry point
- `[product]_complete` - Completion
- `[product]_email_capture` - Lead capture
- `[product]_result_view` - Result viewing
- `[product]_result_share` - Social sharing

### 9.2 KPI Dashboard

| Metric | Target Direction | Tracking Method |
|--------|-----------------|-----------------|
| Organic Sessions | ↑ MoM | GA4 |
| Indexed Pages | ↑ | GSC |
| Avg CTR | ↑ | GSC |
| Keywords in Top 10 | ↑ | GSC/Ahrefs |
| Conversion Rate | ↑ | GA4 |
| Email Capture Rate | ↑ | GA4 |

---

## 10. Recurring Operations System

### 10.1 Operating Cadence

**Weekly (Execution):**
- [ ] Publish 2-3 SEO articles/pages
- [ ] Add internal links from 3+ existing pages
- [ ] Verify metadata for new pages
- [ ] Validate schema output
- [ ] Submit URLs to IndexNow + GSC
- [ ] Review analytics events
- [ ] Review top 10 organic pages

**Monthly (Optimization):**
- [ ] Refresh underperforming pages (CTR < 2%, position 11-30)
- [ ] Add 4-6 spoke pages
- [ ] Audit sitemap/robots consistency
- [ ] Validate llms.txt output
- [ ] Check broken links
- [ ] Compare month-over-month performance

**Quarterly (Strategic):**
- [ ] Re-prioritize keyword clusters
- [ ] Expand proven templates
- [ ] Review conversion paths
- [ ] Update tracker

### 10.2 Publishing Runbook

For every new page:
- [ ] Complete metadata and canonical
- [ ] Add content analytics instrumentation
- [ ] Add internal links from related pages
- [ ] Include in sitemap
- [ ] Verify production build
- [ ] Submit to IndexNow
- [ ] Request indexing in GSC

### 10.3 Validation Payload Structure

```json
{
  "run_id": "uuid",
  "job_key": "seo_weekly_publish",
  "status": "completed",
  "started_at": "ISO-8601",
  "finished_at": "ISO-8601",
  "artifacts": {
    "published_urls": ["..."],
    "indexnow_submissions": [{"url": "...", "ok": true}],
    "quality_scores": [{"url": "...", "score": 8.4}]
  },
  "checks": {
    "content_generated": true,
    "quality_threshold_met": true,
    "metadata_valid": true,
    "schema_valid": true,
    "sitemap_contains_url": true,
    "indexing_submitted": true
  },
  "errors": [],
  "summary": "2 pages published, all checks passed"
}
```

---

## 11. Step-by-Step Replication Checklist

### Phase 1: Skills & Workflows Setup

- [ ] Create `.agents/skills/` directory
- [ ] Create `seo-audit/SKILL.md` with full framework
- [ ] Create `seo-audit/references/aeo-geo-patterns.md`
- [ ] Create `answer-engine-optimization/SKILL.md`
- [ ] Create `answer-engine-optimization/references/brand-facts-template.md`
- [ ] Create `llm-indexing/SKILL.md`
- [ ] Create `llm-indexing/references/llms-txt-template.md`
- [ ] Create `llm-indexing/references/llm-crawlers.md`
- [ ] Create `content-strategy/SKILL.md`
- [ ] Create `.agents/workflows/answer-engine-optimization.md`
- [ ] Create `.agents/workflows/seo-content-publishing.md`

### Phase 2: Technical SEO Foundation

- [ ] Create `src/app/robots.ts` with AI crawler rules
- [ ] Create `src/app/sitemap.ts` with URL groups
- [ ] Update `src/app/layout.tsx` with metadata and schema
- [ ] Verify GSC verification meta tag

### Phase 3: LLM Discovery Layer

- [ ] Create `src/app/llms.txt/route.ts`
- [ ] Create `src/app/llms-full.txt/route.ts`
- [ ] Optionally create `src/app/api/llm-content/route.ts`
- [ ] Submit to llmstxt.site and directory.llmstxt.cloud

### Phase 4: AEO Implementation

- [ ] Create `public/.well-known/brand-facts.json`
- [ ] Create `src/app/brand-facts/page.tsx` with schemas
- [ ] Identify answer hub page opportunities
- [ ] Create first answer hub page

### Phase 5: Indexing Infrastructure

- [ ] Generate IndexNow key (8+ alphanumeric chars)
- [ ] Add `INDEXNOW_KEY` to environment
- [ ] Create `src/app/api/indexnow/route.ts`
- [ ] Add rewrite in `next.config.ts`
- [ ] Create `src/app/api/indexnow/submit/route.ts`
- [ ] Test key verification URL
- [ ] Test submission endpoint

### Phase 6: Content Strategy

- [ ] Define 3-5 content pillars
- [ ] Create pillar hub pages
- [ ] Identify quick-win keywords
- [ ] Create content backlog
- [ ] Set up article template with schema

### Phase 7: Analytics & Operations

- [ ] Implement tracking events
- [ ] Create KPI dashboard/snapshot template
- [ ] Create recurring operations tracker
- [ ] Define validation payload contract
- [ ] Set up execution log

### Phase 8: Validation

- [ ] Verify `/robots.txt` renders correctly
- [ ] Verify `/sitemap.xml` renders correctly
- [ ] Verify `/llms.txt` renders correctly
- [ ] Verify `/.well-known/brand-facts.json` renders
- [ ] Verify `/brand-facts` page renders with schema
- [ ] Test IndexNow submission
- [ ] Validate GA4 events in DebugView
- [ ] Run first SEO audit with new skills

---

## Appendix A: File Templates

### A.1 Minimal SKILL.md Template

```markdown
---
name: skill-name
version: 1.0.0
description: Trigger phrases and use cases for this skill.
---

# Skill Name

You are an expert in [domain]. Your goal is to [objective].

## Initial Assessment

[Context gathering steps]

## Core Framework

### Priority Order
1. First priority
2. Second priority

## Output Format

[Expected output structure]

## References

- [Reference](references/file.md): Description

## Related Skills

- **related-skill**: When to use
```

### A.2 Minimal Workflow Template

```markdown
---
description: What this workflow accomplishes
---

# Workflow Title

Use this workflow when [trigger conditions].

## Phase 1: [Name]

1. Step one
2. Step two

## Phase 2: [Name]

1. Step one
2. Step two

## Validation

- [ ] Checklist item 1
- [ ] Checklist item 2
```

---

## Appendix B: Quick Reference

### B.1 LLM Crawlers to Allow

| User-Agent | Company |
|------------|---------|
| GPTBot | OpenAI |
| ChatGPT-User | OpenAI |
| ClaudeBot | Anthropic |
| anthropic-ai | Anthropic |
| PerplexityBot | Perplexity |
| GoogleOther | Google |
| cohere-ai | Cohere |
| CCBot | Common Crawl |

### B.2 Schema Types by Page Type

| Page Type | Schema Types |
|-----------|--------------|
| Article | Article, FAQPage, BreadcrumbList |
| Product | Product, AggregateRating, Offer |
| Category | ItemList, CollectionPage |
| Brand Facts | Organization, AboutPage, FAQPage |
| Answer Hub | ItemList, FAQPage, HowTo |

### B.3 IndexNow Providers

| Provider | Endpoint |
|----------|----------|
| Bing | https://www.bing.com/indexnow |
| Yandex | https://yandex.com/indexnow |

---

## Appendix C: Troubleshooting

### C.1 llms.txt Not Rendering
- Check route handler returns `Content-Type: text/plain`
- Verify route is at `/llms.txt/route.ts` (App Router)
- Check for middleware blocking the route

### C.2 IndexNow Key Not Verifying
- Verify `INDEXNOW_KEY` environment variable is set
- Check rewrite in `next.config.ts`
- Test `/api/indexnow` directly
- Ensure key is exactly 8+ alphanumeric characters

### C.3 Schema Not Appearing
- Verify JSON-LD is in `<script type="application/ld+json">`
- Check for JSON syntax errors
- Use Google Rich Results Test to validate

### C.4 AI Crawlers Not Indexing
- Verify robots.ts explicitly allows AI user agents
- Check that llms.txt is referenced in sitemap array
- Submit to LLM directories

---

*End of Replication Guide*