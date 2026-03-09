# 🧠 Content Agent CMS — Unified Architecture

> Merges the Writing Masterclass building plan patterns (OpenClaw, SOUL.md, skills-as-markdown, heartbeat, feedback loops) with an SEO content pipeline (8 specialized agents, pSEO/GEO/AEO knowledge, exclusion enforcement). One system for all content generation across any project or agent.

---

## How the Two Systems Map Together

| Building Plan Concept | SEO Pipeline Equivalent | Resolution |
|---|---|---|
| Orchestrator | Mission Planner | **Merge → Orchestrator** does both: picks what to write (strategic planning) AND configures the pipeline per piece |
| Research Agent | Researcher | **Same** — structured knowledge retrieval, not RAG |
| Writer Agent | Content Writer | **Same** — sole content producer, system prompt assembled per-request |
| Editor Agent | Quality Checker | **Merge → Editor** does quality scoring (10-dimension scorecard) AND exclusion/AI-detection checks |
| Platform Agents (Twitter, LinkedIn, Newsletter) | SEO Specialist | **Both exist** — SEO Specialist is a "platform agent" for Google (on-page, schema, AEO/GEO). Twitter/LinkedIn/Newsletter agents are separate verticals for distribution |
| — | Publisher | **Added** — GitHub-as-CMS commit/deploy agent |
| — | Video Script Agent | **Added** — script + storyboard only, controlled imagination |
| — | Monitor | **Added** — GSC/GA4 performance tracking feeds back to Orchestrator |

### Final Agent Lineup: 8 Agents

```
ORCHESTRATOR (strategic planning + pipeline config)
    → RESEARCHER (knowledge retrieval + source gathering)
        → WRITER (sole content producer)
            ↔ EDITOR (quality scoring + revision loops)
                → SEO SPECIALIST ("Google platform agent")
                    → PUBLISHER (GitHub commit + deploy)
                    → VIDEO SCRIPT AGENT (storyboard + narration)
                → PLATFORM AGENTS (Twitter, LinkedIn, Newsletter — future)
    ← MONITOR (performance → feeds back to Orchestrator)
```

---

## OpenClaw Patterns Applied to SEO Pipeline

### 1. SOUL.md — Agent Personality Files

Each agent has a `SOUL.md` defining its persona, constraints, and style. These are the identity anchors — they don't change between runs.

```
workspace/agents/
  orchestrator/SOUL.md
  researcher/SOUL.md
  writer/SOUL.md
  editor/SOUL.md
  seo_specialist/SOUL.md
  publisher/SOUL.md
  video_script/SOUL.md
  monitor/SOUL.md
```

#### Writer SOUL.md (excerpt)

```markdown
# Writer Agent — SOUL

## Identity
You are the primary Content Writer. You write for readers who want depth without academic jargon. Your voice is warm, guiding, authoritative but modern — like a wise friend walking beside someone on their path.

## Voice
- Clarity over cleverness — always choose clear over creative
- Active over passive — "Krishna teaches Arjuna" not "Arjuna is taught by Krishna"
- Specific over vague — "practiced by Shaiva monks in Kashmir since the 9th century"
- One idea per section — logical flow, not information dump
- Benefits language — "why this matters to your practice" not structural descriptions

## Hard Constraints
- NEVER use em dashes (—). Use commas, colons, or parentheses
- NEVER use: delve, leverage, utilize, robust, seamless, transformative, cutting-edge
- NEVER open with: "In today's...", "In the ever-evolving...", "Let's delve..."
- NEVER close with: "In conclusion...", "By [doing X] you can [achieve Y]..."
- ZERO medical claims — no "cures", "treats", "heals"
- ZERO copyrighted translations reproduced in full
- ALL Sanskrit includes both Devanagari + IAST transliteration

## Quality Floor
- Word count: meet minimum for page type (see content-rules.md)
- Internal links: minimum 3 per piece, descriptive anchor text
- FAQ section: 5-10 questions matching "People Also Ask" phrasing
- Heading hierarchy: exactly one H1, then H2→H3 (no skipping)
```

#### Video Script Agent SOUL.md

```markdown
# Video Script Agent — SOUL

## Identity
You are a visual storyteller for the brand's YouTube channel. You translate detailed content into narrated video scripts with image storyboards. You have a gift for making complex topics feel cinematic and alive.

## Creative Range
You ARE allowed to:
- Use vivid imagery and scene-setting ("Picture the battlefield at dawn...")
- Create atmospheric descriptions for slide visuals
- Use storytelling hooks and narrative tension
- Employ metaphor, analogy, and poetic language appropriate to the tradition
- Build emotional arcs across 5-8 minute scripts
- Create "you are there" moments that transport the viewer

You are NOT allowed to:
- Fabricate historical events or attribute false quotes to sages
- Embellish theological claims beyond what the source texts support
- Break character with modern slang or anachronistic references
- Make medical/curative claims (same exclusions as Writer)
- Use copyrighted translations or imagery descriptions
- Add dramatic interpretations where the texts are clear and specific

## Format
- Image layover + audio narration (no face camera)
- 5-8 minutes target duration (300-480 seconds)
- 10-15 slides with transition notes
- Full narration script per slide (TTS-ready or voiceover-ready)

## Guardrails
- Every creative embellishment must be traceable to a source text or tradition
- When imagining a scene, use "The tradition describes..." not "This is what happened..."
- Sanskrit pronunciation must be correct (provide IAST for TTS)
- All claims stay within exclusions.md boundaries
- Factual accuracy is non-negotiable — imagination applies to delivery, not content
```

### 2. MEMORY.md — Learned Preferences

```
workspace/agents/
  writer/
    MEMORY.md              # Curated: voice preferences, anti-patterns learned from feedback
  editor/
    MEMORY.md              # Scoring calibration: what "good" means for brand content
    memory/
  seo_specialist/
    MEMORY.md              # Keywords that worked, SERP features won, linking patterns
    memory/
  video_script/
    MEMORY.md              # Narration styles that got engagement, pacing patterns
    memory/
```

**Two-layer retrieval:**
1. `MEMORY.md` always loaded into context (<200 lines, curated)
2. Daily logs indexed with BM25 (SQLite FTS5), queried only when relevant

**Memory flush:** Before context compaction, agent persists durable findings to `MEMORY.md`.

### 3. Skills-as-Markdown — Agent Prompt Templates

```
skills/
  orchestrator.md                 # How to analyze request + configure pipeline
  research/
    base.md                       # How to build a research brief
    seo_knowledge.md              # SEO-specific retrieval rules (what keywords, what competitors)
  writer/
    base.md                       # Base writer instructions
    blog_post.md                  # Blog post content template + requirements
    product_page.md               # Product/Service page template
    article.md                    # Long-form article template
    comparison.md                 # Comparison page template
    glossary_term.md              # Glossary/Definition page template
    how_to.md                     # Step-by-step guide template
    founder_story.md              # Brand/founder story template
  editor/
    base.md                       # Quality scorecard (10 dimensions)
    exclusion_rules.md            # Exclusion patterns to scan for
    ai_detection.md               # AI writing markers to catch
    content_rules.md              # Minimum requirements per page type
  seo_specialist/
    on_page.md                    # Title, meta, headings, keyword density
    schema.md                     # JSON-LD structured data rules
    aeo.md                        # Featured snippet optimization
    geo.md                        # AI citation optimization (GEO)
    internal_linking.md           # linkMap.json injection rules
    off_page_tasks.md             # Video briefs, social posts, backlink opps
  video_script/
    base.md                       # Script structure + storyboard format
    youtube_seo.md                # Title, description, tags, timestamps
    narration_style.md            # Pacing, tone, pronunciation guide
  publisher/
    github_flow.md                # Branch, commit, PR, merge workflow
    ci_validation.md              # What the GitHub Action checks
  monitor/
    gsc_tracking.md               # What to query from Search Console
    anomaly_detection.md          # When to alert (not indexed after 7d, etc.)
```

**Why markdown, not code:**
- Editable without code changes — tweak agent behavior by editing a file
- Version-controllable — `git diff` shows prompt evolution
- Feedback loop updates _these files_ — when user calibrates an agent, the skill file changes
- Selective injection: only load relevant skills per pipeline turn (<2000 tokens per injection)

### 4. Pipeline State Object

Single shared `ContentPipeline` state object (persisted to DB):

```python
class ContentPipeline(BaseModel):
    id: str
    status: Literal["brief", "research", "writing", "editing", "revision",
                     "seo_optimization", "publishing", "video_scripting",
                     "published", "failed"]
    content_brief: ContentBrief
    research_bundle: Optional[ResearchBundle]
    draft: Optional[ContentDraft]
    editor_scores: Optional[QualityScore]  # 10-dimension scorecard
    revision_count: int = 0
    max_revisions: int = 3
    seo_output: Optional[SEOOptimizedContent]
    video_task: Optional[VideoScriptTask]
    video_script: Optional[VideoScript]
    published_url: Optional[str]
    feedback_entries: list[FeedbackEntry] = []
    created_at: datetime
    updated_at: datetime
```

Each agent reads current state → does work → appends output. Orchestrator advances the `status` field. **Explicit pipeline, fully debuggable** — no event-driven indirection.

### 5. Four Autonomy Modes

| Mode | Human Gates | Use Case |
|------|-------------|----------|
| **Mode 1: Full Control** | Every stage gated | Launch state — building trust in the pipeline |
| **Mode 2: Review Final** | Pipeline runs until SEO output → user reviews final only | Proven pipeline quality |
| **Mode 3: Approval Queue** | Heartbeat creates pipelines on schedule → batch approval | Scaling content production |
| **Mode 4: Full Auto** | Auto-publish if quality score > threshold → alerts only for low scores | Mature pipeline with calibrated quality |

### 6. Heartbeat (Phase 4)

```markdown
# HEARTBEAT.md

## Schedule
- Every Monday 9am: Generate 5 glossary term pages (next unfinished in sequence)
- Every Wednesday 9am: Generate 2 blog posts (next from priority list)
- Every Friday 9am: Generate 1 comparison article (next from gap analysis)
- First of month: Run Monitor → weekly performance report

## Pending
- [ ] Glossary: terminology batch A (5 items)
- [ ] Blog: industry trends, how-to guide
- [ ] Comparison: Product A vs Product B

## Quality Threshold
- Auto-publish if editor score ≥ 8.0/10
- Queue for review if 6.0-7.9
- Reject + alert if < 6.0
```

### 7. Feedback Loop

```
Capture → Store → Synthesize → Recommend → Apply
```

1. **Capture**: Every human edit, approval, or rejection stored with stage context + diff
2. **Store**: `FeedbackEntry` linked to pipeline ID + stage + what changed
3. **Synthesize**: Periodically, Claude analyzes accumulated feedback for patterns ("user consistently prefers shorter introductions on Sanskrit vocab pages")
4. **Recommend**: System generates config adjustment proposals (changes to skill files or MEMORY.md)
5. **Apply**: User approves adjustments → skill file or SOUL.md updated → all future content reflects the learning

---

## Knowledge Store (Structured, Not Vector)

SEO knowledge is structured and finite — deterministic retrieval beats fuzzy search.

```
knowledge/
  seo/
    exclusions.json              # Parsed from exclusions.md
    content_rules.json           # Parsed from content-rules.md (min words, required sections)
    keyword_clusters.json        # From seo-content-strategy.md
    competitor_patterns.json     # From competitor research
    link_map.json                # Canonical URL map for internal linking
    meta_templates.json          # Title/description formulas per page type
    schema_templates.json        # JSON-LD templates per page type
  content/
    principles.json              # From Writing Masterclass Blueprint
    techniques/                  # Hook, structure, rhythm, persuasion patterns
    voice/
      brand_voice.json           # Voice DNA for the specific brand
      style_tags.json            # Modifier tags
    vocabulary/
      power_words.json
      transitions.json
      anti_patterns.json         # AI writing markers to avoid (from ai-writing-detection.md)
  aeo_geo/
    definition_blocks.json       # AEO pattern templates
    step_by_step_blocks.json
    comparison_table_blocks.json
    faq_blocks.json
    citation_blocks.json         # GEO patterns for AI citation
    evidence_sandwich.json
    voice_search_patterns.json
```

**`KnowledgeStore` class** loads all JSON at startup (<2MB). Query methods:
- `get_content_rules(page_type)` → min words, required sections
- `get_exclusion_patterns()` → regex array for fail-closed scanning
- `get_keywords(cluster, priority)` → target keywords for a content brief
- `get_meta_template(page_type)` → title/description formula
- `get_aeo_patterns(query_type)` → definition/step/table/faq blocks
- `get_geo_citation_pattern(domain)` → spiritual content citation template
- `get_anti_patterns()` → AI writing markers to avoid
- `get_internal_link_targets(concepts[])` → URLs from linkMap.json

---

## Editor: 10-Dimension Quality Scorecard

Adapted from building plan's quality scorecard for SEO content:

| Dimension | Weight | What It Measures |
|-----------|--------|-----------------|
| 1. **Content Depth** | 15% | Word count, comprehensiveness, answers search intent |
| 2. **Factual Accuracy** | 15% | Citations accurate, technical claims correct, balanced evidence |
| 3. **Voice Consistency** | 10% | Matches brand voice (SOUL.md), appropriate tone and cadence |
| 4. **SEO Structure** | 10% | H1/H2/H3 hierarchy, keyword in first 100 words, internal links |
| 5. **AEAD Compliance** | 10% | AEO blocks present (definition, FAQ, steps), GEO citation patterns |
| 6. **Exclusion Safety** | 15% | Zero medical claims (if applicable), zero copyright violations, zero defamation |
| 7. **AI Detection Risk** | 10% | No flagged words/phrases/patterns, varied sentence lengths |
| 8. **Uniqueness** | 5% | ≥40% unique content (not template swapped), original analysis |
| 9. **Readability** | 5% | Natural flow, reads well aloud, appropriate grade level for audience |
| 10. **E-E-A-T Signals** | 5% | Primary citations, expert attribution, author credentials |

**Scoring rules:**
- Score 1-10 per dimension → weighted total
- ≥ 8.0 → approve → SEO Specialist
- 6.0-7.9 → revision request → back to Writer (max 3 loops)
- < 6.0 → reject → flag to Orchestrator for re-briefing

**Dimension 6 (Exclusion Safety) is binary:** ANY exclusion violation = automatic score 0 on this dimension = overall fail regardless of other scores.

---

## Adjusted Project Structure

```
content-agents-cms/
  backend/
    app/
      main.py
      config.py
      api/routes/
        generate.py              # POST /api/generate
        pipelines.py             # Pipeline CRUD + stage advancement
        knowledge.py             # GET /api/knowledge/*
        agents.py                # Agent configs + status
        feedback.py              # Feedback CRUD + synthesis
      agents/
        base.py                  # BaseAgent class (loads SOUL.md + skills)
        orchestrator.py          # Strategic planning + pipeline config
        researcher.py            # Knowledge retrieval + source synthesis
        writer.py                # Content generation (sole producer)
        editor.py                # Quality scoring (10 dimensions) + exclusion checks
        seo_specialist.py        # On-page, schema, AEO/GEO, internal linking
        publisher.py             # GitHub API commit/PR/merge
        video_script.py          # Script + storyboard generation
        monitor.py               # GSC/GA4 querying + anomaly detection
      knowledge/
        parser.py                # Markdown sources → structured JSON
        store.py                 # Loads JSON, deterministic query methods
        models.py                # Pydantic models for knowledge objects
      memory/
        store.py                 # File-based MEMORY.md + daily logs
        search.py                # BM25 over daily logs (FTS5)
        compaction.py            # Context compaction + flush
      models/
        database.py              # SQLAlchemy models
        schemas.py               # Pydantic request/response schemas
        pipeline.py              # ContentPipeline state model
      services/
        pipeline_service.py      # Pipeline orchestration logic
        feedback_service.py      # Feedback capture + synthesis
        memory_service.py        # Memory R/W abstraction
        voice_config_service.py  # Config evolution (baseline + overrides + adjustments)
        heartbeat.py             # Scheduled pipeline creation (Phase 4)
      db/
        session.py, migrations/
    knowledge/                   # Source + parsed knowledge files
    tests/

  workspace/                     # Agent workspaces (file-based memory)
    agents/
      orchestrator/SOUL.md, MEMORY.md, memory/
      researcher/SOUL.md, MEMORY.md, memory/
      writer/SOUL.md, MEMORY.md, memory/
      editor/SOUL.md, MEMORY.md, memory/
      seo_specialist/SOUL.md, MEMORY.md, memory/
      publisher/SOUL.md, MEMORY.md, memory/
      video_script/SOUL.md, MEMORY.md, memory/
      monitor/SOUL.md, MEMORY.md, memory/

  skills/                        # Agent prompt templates (markdown)
    orchestrator.md
    research/base.md, seo_knowledge.md
    writer/
      core/SKILL.md              # Foundation: clarity, audience, research, rules
      web-content/SKILL.md       # Blogs, guides, articles
      seo-geo/SKILL.md           # Search + LLM citation
      marketing/SKILL.md         # Email, ads, campaigns
      landing-page/SKILL.md      # Conversion pages
      news/SKILL.md              # Journalism, press releases
    editor/base.md, exclusion_rules.md, ai_detection.md, content_rules.md
    seo_specialist/on_page.md, schema.md, aeo.md, geo.md,
                   internal_linking.md, off_page_tasks.md
    video_script/base.md, youtube_seo.md, narration_style.md
    publisher/github_flow.md, ci_validation.md
    monitor/gsc_tracking.md, anomaly_detection.md

  frontend/                      # Mission Control Dashboard
    app/
      page.tsx                   # Pipeline kanban (home)
      workspace/[pipelineId]/page.tsx  # Content workspace
      agents/page.tsx            # Agent configuration
      history/page.tsx           # History + analytics
    components/
      pipeline-card.tsx, pipeline-kanban.tsx, content-editor.tsx
      quality-scorecard.tsx, voice-weight-editor.tsx
      agent-status-card.tsx, feedback-form.tsx
      video-script-viewer.tsx    # Script + storyboard preview
      seo-metrics-panel.tsx      # GSC data display

  HEARTBEAT.md                   # Autonomous schedule (Phase 4)
```

---

## Phased Build Order (Adjusted)

### Phase 1: Core Loop — Topic → Content → Score

**Goal:** Type a topic + pick a page type → get generated content with quality score.

| Step | What | Key Files |
|------|------|-----------|
| 1 | Project scaffolding — FastAPI + Poetry, Next.js + Tailwind, SQLite + SQLAlchemy | `pyproject.toml`, `main.py`, `config.py` |
| 2 | Knowledge parser — `content-rules.md`, `exclusions.md`, `seo-content-strategy.md`, `competitor-research.md` → structured JSON | `knowledge/parser.py`, `knowledge/models.py` |
| 3 | Knowledge store — loads JSON, query methods with filtering | `knowledge/store.py` |
| 4 | Writer Agent — builds system prompt from SOUL.md + skill file + knowledge store, calls Claude | `agents/writer.py`, `agents/base.py` |
| 5 | Editor Agent — 10-dimension quality scoring + exclusion scan | `agents/editor.py` |
| 6 | API — `POST /api/generate`, `GET /api/knowledge/techniques` | `api/routes/generate.py` |
| 7 | Frontend — input form, generate, content card + scorecard | `frontend/app/page.tsx` |

### Phase 2: Full Pipeline + Feedback

| Step | What |
|------|------|
| 1 | DB schema — `ContentPipeline`, `ContentOutput`, `FeedbackEntry` |
| 2 | Orchestrator — receives request, creates brief, configures pipeline |
| 3 | Researcher — separate from Writer, outputs `ResearchBundle` |
| 4 | Revision loop — Editor ↔ Writer (up to 3 loops) |
| 5 | SEO Specialist — on-page optimization, schema, AEO/GEO, internal linking |
| 6 | Human-in-the-loop gates at each stage |
| 7 | Pipeline Kanban dashboard + content workspace |
| 8 | Feedback storage — all edits linked to pipeline + stage |

### Phase 3: Publishing + Video + Memory

| Step | What |
|------|------|
| 1 | Publisher Agent — GitHub API integration (branch → commit → PR → merge) |
| 2 | CI validation GitHub Action (content-rules, exclusions, AI detection, build test) |
| 3 | Video Script Agent — script + storyboard generation |
| 4 | Agent memory system — MEMORY.md + daily logs + BM25 search |
| 5 | Feedback synthesizer — pattern detection → config recommendations |
| 6 | Agent config panel + History view in frontend |

### Phase 4: Autonomous + Monitoring (Heartbeat)

| Step | What |
|------|------|
| 1 | Monitor Agent — GSC API + GA4 queries, anomaly detection |
| 2 | Heartbeat system — scheduled pipeline creation from `HEARTBEAT.md` |
| 3 | Approval queue — batch review for heartbeat-generated content |
| 4 | Mode 2 (review final only) → Mode 3 (approval queue) |
| 5 | Quality guardrails for auto-publish |
| 6 | Performance analytics dashboard — trends, keyword tracking, agent effectiveness |

---

## Key Differences from Original Building Plan

| Aspect | Building Plan (Generic) | Content CMS Adaptation |
|--------|------------------------|-------------------|
| **Platform Agents** | Twitter, LinkedIn, Newsletter | Added: SEO Specialist (on-page/schema/AEO/GEO), Publisher (GitHub-as-CMS), Video Script Agent |
| **Knowledge Store** | Writing Masterclass Blueprint (principles, masters, techniques) | Added: `exclusions.json`, `content_rules.json`, `keyword_clusters.json`, `competitor_patterns.json`, `link_map.json`, `aeo_geo/` patterns |
| **Editor Scorecard** | 10 generic writing quality dimensions | Dimensions 5-7 are SEO-specific: AEAD compliance, exclusion safety, AI detection risk |
| **Pipeline stages** | Research → Writing → Editing → Platform | Research → Writing → Editing → SEO Optimization → Publishing → Video Scripting |
| **Writer skill overlays** | social.md, long_form.md, sales.md, thought_leadership.md | blog_post.md, product_page.md, article.md, comparison.md, glossary_term.md, how_to.md, founder_story.md |
| **Autonomy target** | Auto-publish to social media | Auto-commit to GitHub → Vercel deploy → GSC indexing ping |
| **Monitor** | Not in original plan | Added: GSC/GA4 performance tracking feeds data back to Orchestrator for content gap analysis |
