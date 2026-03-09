# Content Agent CMS

> An AI-powered content generation system with specialized agents, deterministic quality enforcement, and SEO optimization.

A multi-agent architecture that transforms topics into publication-ready content through orchestrated pipelines. The system combines LLM-powered creativity with deterministic quality gates, exclusion scanning, and SEO optimization.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Agent System](#agent-system)
- [Pipeline Workflow](#pipeline-workflow)
- [Knowledge Store](#knowledge-store)
- [API Reference](#api-reference)
- [Installation](#installation)
- [Configuration](#configuration)
- [Frontend Dashboard](#frontend-dashboard)
- [Project Structure](#project-structure)
- [Development Phases](#development-phases)

---

## Overview

Content Agent CMS is designed for organizations that need to produce high-quality, SEO-optimized content at scale. Unlike simple LLM wrappers, this system uses:

- **Specialized Agents**: Each agent has a specific role (Orchestrator, Researcher, Writer, Editor, SEO Specialist)
- **Deterministic Quality Gates**: Regex-based exclusion scanning ensures content safety
- **10-Dimension Quality Scorecard**: Multi-faceted evaluation of generated content
- **Structured Knowledge Store**: JSON-based rules engine (not vector RAG) for predictable behavior
- **Human-in-the-Loop**: Multiple autonomy modes from full control to auto-publish

### Key Features

- 🤖 **Multi-Agent Pipeline**: Orchestrated workflow with specialized agents
- 📊 **Quality Scorecard**: 10-dimension evaluation with weighted scoring
- 🛡️ **Exclusion Scanner**: Fail-closed regex patterns for content safety
- 🔍 **SEO Optimization**: On-page, schema, AEO/GEO, and internal linking
- 📝 **Content Rules Engine**: Per-page-type requirements (word count, sections, tone)
- 🔄 **Revision Loops**: Automatic writer-editor feedback cycles
- 🎛️ **Mission Control Dashboard**: Real-time pipeline monitoring

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     FRONTEND (Next.js)                          │
│                   Mission Control Dashboard                      │
└─────────────────────────────┬───────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                     API LAYER (FastAPI)                          │
│  /api/generate  /api/pipelines  /api/feedback  /api/knowledge   │
└─────────────────────────────┬───────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    AGENT ORCHESTRATION                           │
│                                                                  │
│  ORCHESTRATOR ──► RESEARCHER ──► WRITER ◄──► EDITOR             │
│        │              │            │            │                │
│        │              │            │            ▼                │
│        │              │            │     SEO SPECIALIST          │
│        │              │            │            │                │
│        ▼              ▼            ▼            ▼                │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                  KNOWLEDGE STORE                         │    │
│  │  content_rules | exclusions | link_map | seo_guidance   │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    DATA LAYER (SQLite)                           │
│   Pipeline | FeedbackEntry | ContentDraft | SEOOptimized        │
└─────────────────────────────────────────────────────────────────┘
```

---

## Agent System

### 1. Orchestrator Agent

The strategic brain of the pipeline. Analyzes requests and configures the workflow.

**Responsibilities:**
- Creates structured content briefs
- Configures pipeline based on topic and page type
- Advances pipeline stages
- Manages revision loop decisions

**File:** `backend/app/agents/orchestrator.py`

```python
# Example: Creating a content brief
brief = orchestrator.create_content_brief(pipeline)
# Returns: topic, page_type, target_audience, content_requirements, 
#          seo_requirements, quality_thresholds, pipeline_config
```

### 2. Researcher Agent

Gathers structured knowledge for content creation using deterministic retrieval.

**Responsibilities:**
- Retrieves content rules for page type
- Identifies internal linking opportunities
- Prepares SEO guidance
- Assembles research bundle for Writer

**File:** `backend/app/agents/researcher.py`

### 3. Writer Agent

The sole content producer. Assembles dynamic prompts and calls the LLM.

**Responsibilities:**
- Builds system prompt from SOUL.md + skills + knowledge
- Injects deterministic SEO boundaries
- Generates content draft
- Handles different page types (blog, glossary, comparison, how-to)

**File:** `backend/app/agents/writer.py`

**Supported Page Types:**
| Type | Min Words | Max Words | Required Sections |
|------|-----------|-----------|-------------------|
| `blog_post` | 1,500 | 3,000 | introduction, body, faq |
| `glossary_term` | 800 | 1,500 | definition, explanation, examples |
| `comparison` | 1,200 | 2,500 | overview, key_differences, table |
| `how_to` | 1,000 | 2,000 | prerequisites, steps, tips |
| `x_thread` | 150 | 500 | hook, development, close |

### 4. Editor Agent

Quality gate with dual-pass evaluation: deterministic + qualitative.

**Responsibilities:**
- Scans for exclusion violations (regex patterns)
- Scores content on 10-dimension quality scorecard
- Triggers revision loops if score < 8.0
- Automatic rejection on exclusion violations

**File:** `backend/app/agents/editor.py`

**10-Dimension Quality Scorecard:**

| Dimension | Weight | Description |
|-----------|--------|-------------|
| Content Depth | 15% | Word count, comprehensiveness |
| Factual Accuracy | 15% | Citations, technical correctness |
| Voice Consistency | 10% | Brand voice adherence |
| SEO Structure | 10% | H1/H2/H3 hierarchy, keywords |
| AEAD Compliance | 10% | AEO blocks, GEO patterns |
| **Exclusion Safety** | 15% | Zero violations (binary pass/fail) |
| AI Detection Risk | 10% | Avoiding AI writing markers |
| Uniqueness | 5% | Original content percentage |
| Readability | 5% | Natural flow, grade level |
| E-E-A-T Signals | 5% | Expert attribution, credentials |

**Scoring Rules:**
- Score ≥ 8.0 → Approve → SEO Specialist
- Score 6.0-7.9 → Revision → Back to Writer (max 3 loops)
- Score < 6.0 → Reject → Flag for re-briefing
- **Any exclusion violation = automatic rejection**

### 5. SEO Specialist Agent

Applies comprehensive SEO optimization to approved content.

**Responsibilities:**
- Generates meta tags (title, description)
- Applies internal linking from link_map.json
- Creates JSON-LD schema markup
- Adds AEO (Answer Engine Optimization) blocks
- Implements GEO (Generative Engine Optimization) patterns

**File:** `backend/app/agents/seo_specialist.py`

**SEO Score Components:**
- Meta Tags: 30 points (title ≤60 chars, description ≤160 chars)
- Internal Links: 20 points (≥3 links recommended)
- Schema Markup: 25 points (JSON-LD + FAQ schema)
- AEO Blocks: 25 points (definitions, FAQs, steps, tables)

---

## Pipeline Workflow

### Pipeline States

```
pending → brief → research → writing → editing → revision → seo_optimization → published
                                                                    ↓
                                                                  failed
```

### Pipeline State Object

```python
class ContentPipeline(BaseModel):
    id: str
    status: Literal["pending", "brief", "research", "writing", "editing", 
                    "revision", "seo_optimization", "published", "failed"]
    topic: str
    page_type: str
    content_brief: Optional[Dict]
    research_bundle: Optional[Dict]
    content: Optional[str]
    metadata_json: Optional[Dict]  # Quality scores
    seo_output: Optional[Dict]
    revision_count: int = 0
    max_revisions: int = 3
    feedback_entries: List[FeedbackEntry]
    created_at: datetime
    updated_at: datetime
```

### Autonomy Modes

| Mode | Human Gates | Use Case |
|------|-------------|----------|
| **Mode 1: Full Control** | Every stage gated | Building trust in pipeline |
| **Mode 2: Review Final** | Review final output only | Proven pipeline quality |
| **Mode 3: Approval Queue** | Batch approval of auto-generated | Scaling production |
| **Mode 4: Full Auto** | Auto-publish if score ≥ threshold | Mature, calibrated pipeline |

---

## Knowledge Store

The Knowledge Store uses **structured JSON** (not vector RAG) for deterministic, predictable behavior.

### Structure

```
knowledge/
├── raw/                          # Source markdown files
│   ├── content-rules.md
│   ├── exclusions.md
│   └── keyword-strategy.md
└── parsed/                       # Parsed JSON for agents
    ├── content_rules.json        # Per-page-type requirements
    ├── exclusions.json           # Banned words + regex patterns
    └── link_map.json             # Internal linking map
```

### Content Rules (`content_rules.json`)

Defines requirements for each page type:

```json
{
  "page_type": "blog_post",
  "min_words": 1500,
  "max_words": 3000,
  "required_sections": ["introduction", "body", "faq"],
  "min_internal_links": 3,
  "faq_count": "5-10"
}
```

### Exclusions (`exclusions.json`)

Fail-closed scanning patterns:

```json
{
  "banned_words": ["vibe", "manifest", "leverage", "synergy"],
  "regex_patterns": [
    "\\bvibe[s]?\\b",
    "\\bquantum\\b(?!\\s+(?:mechanics|physics))",
    "\\bthis is your sign\\b"
  ],
  "hook_pattern_bans": ["Have you ever wondered why"],
  "close_pattern_bans": ["Drop a comment", "Follow for more"]
}
```

### Link Map (`link_map.json`)

Internal linking opportunities:

```json
[
  {"concept": "meditation", "canonical_url": "/guides/meditation"},
  {"concept": "mindfulness", "canonical_url": "/practices/mindfulness"}
]
```

### KnowledgeStore API

```python
from app.knowledge.store import KnowledgeStore

store = KnowledgeStore(data_dir="knowledge/parsed")

# Get content rules for a page type
rules = store.get_content_rules("blog_post")

# Get compiled exclusion patterns
patterns = store.get_exclusion_patterns()

# Find internal link targets in text
links = store.get_internal_link_targets("Learn about meditation and mindfulness")
```

---

## API Reference

### Base URL

```
http://localhost:8000/api
```

### Endpoints

#### Start Generation

```http
POST /api/generate
Content-Type: application/json

{
  "topic": "Best meditation for beginners",
  "page_type": "blog_post",
  "max_revisions": 3
}
```

**Response:**
```json
{
  "pipeline_id": "550e8400-e29b-41d4-a716-446655440000",
  "status": "pending",
  "message": "Pipeline started in background. Poll /api/status/{pipeline_id} for updates."
}
```

---

#### Get Pipeline Status

```http
GET /api/status/{pipeline_id}
```

**Response:**
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "topic": "Best meditation for beginners",
  "page_type": "blog_post",
  "status": "published",
  "revision_count": 1,
  "max_revisions": 3,
  "content": "# Best Meditation for Beginners\n\n...",
  "metadata_json": {
    "total_score": 8.5,
    "dimension_1_depth": 9,
    "dimension_6_exclusion_safety": 10
  },
  "seo_output": {
    "meta_tags": {
      "title": "Best Meditation for Beginners | Complete Guide",
      "description": "Learn the fundamentals of meditation..."
    },
    "optimization_summary": {
      "meta_title_length": 45,
      "internal_links_added": 4,
      "schema_type": "BlogPosting",
      "aeo_blocks_added": 3
    }
  },
  "created_at": "2026-09-03T18:00:00",
  "updated_at": "2026-09-03T18:05:00"
}
```

---

#### List All Pipelines

```http
GET /api/pipelines
```

**Response:**
```json
[
  {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "topic": "Best meditation for beginners",
    "page_type": "blog_post",
    "status": "published",
    "revision_count": 1,
    "created_at": "2026-09-03T18:00:00",
    "updated_at": "2026-09-03T18:05:00"
  }
]
```

---

#### Submit Feedback

```http
POST /api/feedback
Content-Type: application/json

{
  "pipeline_id": "550e8400-e29b-41d4-a716-446655440000",
  "stage": "editing",
  "feedback_type": "edit",
  "original_content": "Original paragraph...",
  "edited_content": "Revised paragraph...",
  "comment": "Simplified the language for better readability"
}
```

---

#### Advance Pipeline Stage

```http
POST /api/advance/{pipeline_id}?next_stage=seo_optimization
```

---

#### Delete Pipeline

```http
DELETE /api/pipelines/{pipeline_id}
```

---

#### Health Check

```http
GET /health
```

**Response:**
```json
{
  "status": "ok"
}
```

---

## Installation

### Prerequisites

- Python 3.10+
- Node.js 18+
- SQLite (included)

### Backend Setup

```bash
# Navigate to backend
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend Setup

```bash
# Navigate to frontend
cd frontend

# Install dependencies
npm install

# Run development server
npm run dev
```

### Environment Variables

Create a `.env` file in the backend directory:

```env
# LLM Configuration
ANTHROPIC_API_KEY=your_api_key_here
LLM_MODEL=claude-3-5-sonnet-20241022

# Database
DATABASE_URL=sqlite:///./content_agents.db

# Knowledge Store
KNOWLEDGE_DATA_DIR=../knowledge/parsed
```

---

## Configuration

### Agent Configuration

Each agent has a `SOUL.md` file defining its personality and constraints:

```
workspace/agents/
  writer/SOUL.md          # Voice, tone, hard constraints
  editor/SOUL.md          # Scoring calibration
  seo_specialist/SOUL.md  # SEO preferences
```

### Skills System

Agent prompt templates are stored as markdown:

```
skills/
  writer/
    blog_post.md          # Blog post template
    glossary_term.md      # Glossary page template
    comparison.md         # Comparison page template
  editor/
    base.md               # Quality scorecard
    exclusion_rules.md    # Exclusion patterns
  seo_specialist/
    on_page.md            # On-page SEO rules
    schema.md             # JSON-LD templates
    aeo.md                # Featured snippet optimization
```

---

## Frontend Dashboard

The Mission Control Dashboard provides real-time pipeline monitoring.

### Features

- **Pipeline Kanban**: Visual status of all pipelines
- **Quality Scorecard**: 10-dimension scores at a glance
- **SEO Metrics**: Meta tags, links, schema, AEO blocks
- **Content Preview**: Modal view of generated content
- **Stage Progress**: Visual progress bar through pipeline stages

### Pages

| Route | Description |
|-------|-------------|
| `/` | Pipeline kanban dashboard |
| `/workspace/[id]` | Content workspace for a pipeline |
| `/agents` | Agent configuration panel |
| `/history` | Pipeline history and analytics |

---

## Project Structure

```
content-agents-cms/
├── backend/
│   ├── app/
│   │   ├── main.py                 # FastAPI app entry point
│   │   ├── agents/
│   │   │   ├── base.py             # BaseAgent class
│   │   │   ├── orchestrator.py     # Strategic planning
│   │   │   ├── researcher.py       # Knowledge retrieval
│   │   │   ├── writer.py           # Content generation
│   │   │   ├── editor.py           # Quality scoring
│   │   │   └── seo_specialist.py   # SEO optimization
│   │   ├── api/routes/
│   │   │   ├── generate.py         # Pipeline endpoints
│   │   │   └── knowledge.py        # Knowledge endpoints
│   │   ├── knowledge/
│   │   │   ├── parser.py           # Markdown → JSON parser
│   │   │   ├── store.py            # Knowledge query methods
│   │   │   └── models.py           # Pydantic models
│   │   ├── models/
│   │   │   └── pipeline.py         # Pipeline state model
│   │   ├── schemas/
│   │   │   └── generate.py         # Request/response schemas
│   │   ├── services/
│   │   │   ├── pipeline_service.py # Pipeline orchestration
│   │   │   ├── llm_client.py       # LLM API client
│   │   │   └── memory_service.py   # Agent memory
│   │   ├── db/
│   │   │   ├── database.py         # SQLAlchemy setup
│   │   │   └── models.py           # DB models
│   │   └── core/
│   │       └── config.py           # App configuration
│   ├── knowledge/
│   │   ├── raw/                    # Source markdown
│   │   └── parsed/                 # JSON knowledge files
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── app/
│   │   │   ├── page.tsx            # Dashboard home
│   │   │   ├── layout.tsx          # Root layout
│   │   │   └── globals.css         # Global styles
│   │   └── components/ui/          # UI components
│   ├── package.json
│   └── next.config.ts
├── skills/                         # Agent prompt templates
├── workspace/agents/               # Agent SOUL.md files
└── README.md
```

---

## Development Phases

### Phase 1: Core Loop ✅
- [x] Project scaffolding (FastAPI + Next.js + SQLite)
- [x] Knowledge parser and store
- [x] Writer Agent with dynamic prompts
- [x] Editor Agent with 10-dimension scoring
- [x] API endpoints for generation
- [x] Frontend dashboard

### Phase 2: Full Pipeline (In Progress)
- [x] Orchestrator Agent
- [x] Researcher Agent
- [x] SEO Specialist Agent
- [x] Pipeline service orchestration
- [x] Revision loops (Writer ↔ Editor)
- [ ] Human-in-the-loop gates
- [ ] Feedback storage and analysis

### Phase 3: Publishing + Memory (Planned)
- [ ] Publisher Agent (GitHub API integration)
- [ ] Video Script Agent
- [ ] Agent memory system (MEMORY.md + daily logs)
- [ ] Feedback synthesizer for agent calibration

### Phase 4: Autonomous + Monitoring (Planned)
- [ ] Monitor Agent (GSC/GA4 tracking)
- [ ] Heartbeat system for scheduled generation
- [ ] Approval queue for batch review
- [ ] Auto-publish with quality guardrails

---

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## License

This project is licensed under the MIT License.

---

## Acknowledgments

- Built with [FastAPI](https://fastapi.tiangolo.com/) and [Next.js](https://nextjs.org/)
- UI components from [shadcn/ui](https://ui.shadcn.com/)
- LLM integration designed for [Anthropic Claude](https://www.anthropic.com/)