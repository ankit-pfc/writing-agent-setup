# Writing Agent System — Implementation Plan & Task Tracker

> This document maps the phased build-out of the multi-system writing agent architecture with the Sādhak validation as the primary vertical slice. Skills and asset files are the core — architecture, API, and UI are the scaffolding.

---

## Project Overview

**Goal:** Build a multi-agent writing system where:
- Research agents track discourse, trends, and cultural signals
- Writing agents generate character-accurate content (Sādhak, Eitan Lev, LinkedIn voice)
- Editing agents apply exclusions, quality gates, and tone calibration
- SEO agents handle keyword strategy, schema, and meta optimization
- Human stays in the loop for quality control and cultural evolution

**Primary validation target:** Sādhak character on X/Twitter  
**Reason:** Most complete asset library, clearest audience, fastest feedback loop

---

## Asset Inventory Status

| Asset | Status | Location |
|---|---|---|
| Sādhak Writing Mechanics (SKILL.md) | ✅ Complete | skills/sadhak-writing/SKILL.md |
| Eitan Lev Writing Mechanics (SKILL.md) | ✅ Complete | skills/eitan-lev-writing/SKILL.md |
| Writing Masterclass Core (SKILL.md) | ✅ Complete | skills/writing-masterclass/SKILL.md |
| Character Bible (Sādhak) | ✅ Complete | assets/character-bible.md |
| Content Rules | ✅ Complete | assets/content-rules.md |
| Exclusions | ✅ Complete | assets/exclusions.md |
| Keyword Strategy | ⚠️ Stub created | assets/keyword-strategy.md |
| Competitor Research | 🔴 Missing | Needs external input |
| Link Map | 🔴 Missing | Needs external input |
| Schema / Meta Templates | 🔴 Missing | Needs external input |
| Eitan Lev Character Bible | ⚠️ Partial | In skill file; needs full bible |
| TPOT Lingo Research (live) | ⚠️ Partial | In skill file; needs monthly update |

---

## Phase Structure

### Phase 0 — Preflight ✅ (Current)
Asset preparation and knowledge mapping.

**Deliverables:**
- [x] Sādhak Writing SKILL.md
- [x] Eitan Lev Writing SKILL.md
- [x] Writing Masterclass Core SKILL.md
- [x] character-bible.md (Sādhak)
- [x] content-rules.md
- [x] exclusions.md
- [ ] keyword-strategy.md (stub ready, needs research input)
- [ ] competitor-research.md
- [ ] link-map.md
- [ ] schema-meta-templates.md

**Blocking:** Phase 1 cannot start without the keyword strategy and schema templates if SEO is a Phase 1 priority. For X-only content, Phase 1 can start now.

---

### Phase 1 — Sādhak Validation (Vertical Slice)
**Goal:** Demonstrate end-to-end generation quality for one character, one platform.  
**Scope:** X/Twitter only. No SEO. No Eitan Lev. No LinkedIn.

**Milestone 1.1 — Prompt Asset Mapping**
- [ ] Extract system prompt from SKILL.md (Sādhak)
- [ ] Build prompt template per mode (5 modes × 1 template each)
- [ ] Build validation checklist prompt (for editing agent)
- [ ] Test: Generate 10 tweets per mode → human review against quality gates

**Milestone 1.2 — Writing Agent (Single Character)**
- [ ] Build single-agent writing flow: input (topic + mode) → output (tweet/thread)
- [ ] Implement banned vocabulary check (automatic)
- [ ] Implement hook pattern validation (rule-based or LLM-judge)
- [ ] Human review interface: approve / reject / edit with annotation

**Milestone 1.3 — Research Agent (Cultural Awareness)**
- [ ] Build TPOT/discourse tracker: monitor specified accounts, flag new terms
- [ ] Weekly report format: "Currently Alive" / "Currently Dead" updates
- [ ] Human review gate: proposed updates to skill file require approval
- [ ] Integration: approved updates auto-update the living layer in SKILL.md

**Milestone 1.4 — Quality Loop**
- [ ] Annotated feedback from human review feeds back into prompt refinement
- [ ] Collect 50+ annotated outputs (approved/rejected/edited)
- [ ] First calibration: where is the agent failing consistently?
- [ ] Skill file update based on findings

**Success criteria for Phase 1:**
- 70%+ of generated tweets/threads pass all 5 quality gates without human edit
- Research agent correctly identifies 3+ discourse shifts in first 30 days
- Human reviewer time < 10 min per batch of 20 outputs

---

### Phase 2 — Second Character + LinkedIn Voice
**Dependency:** Phase 1 validation complete  
**Goal:** Extend to Eitan Lev (X) and LinkedIn (Ankit voice)

**Milestone 2.1 — Eitan Lev Activation**
- [ ] Build full Eitan Lev character bible (separate from skill file)
- [ ] Prompt asset mapping for Eitan (same process as Milestone 1.1)
- [ ] Cross-character contamination check: do the voices stay distinct?
- [ ] Test: Generate 20 outputs. Can a reader identify the character without being told?

**Milestone 2.2 — LinkedIn Writing Agent**
- [ ] Map LinkedIn voice synthesis from writing-masterclass SKILL.md
- [ ] Template builder: 3 LinkedIn templates (Build-in-Public, Counterintuitive Principle, Postmortem)
- [ ] Context-aware: agent knows which of Ankit's ventures is being featured
- [ ] Human review interface for LinkedIn (higher stakes than X — longer review time expected)

**Milestone 2.3 — Multi-Character Router**
- [ ] Single input interface: select character + platform + topic + mode
- [ ] Routes to appropriate skill file + prompt template
- [ ] Ensures no cross-character contamination in the prompt stack

---

### Phase 3 — SEO + Long-Form + PR Agents
**Dependency:** Phase 2 complete, keyword strategy and schema documents ready

**Milestone 3.1 — SEO Agent**
- [ ] Keyword strategy document complete (external input required)
- [ ] Schema / meta template library complete
- [ ] Agent generates meta titles, descriptions, schema markup from content
- [ ] Link map integration: internal linking suggestions

**Milestone 3.2 — Long-Form Writing Agent**
- [ ] Essay structure templates from writing-masterclass SKILL.md
- [ ] Multi-section generation with coherence checking
- [ ] Output formats: Markdown, Substack-ready, app (Sanatan Rising) ready

**Milestone 3.3 — Ad Copy / PR Agent**
- [ ] Context: which product, which audience, which stage (launch / growth / re-engagement)
- [ ] Templates from Context Module 3.3 (Sales Copy) and 3.4 (PR)
- [ ] Ankit voice validation (does this sound like the writing masterclass voice?)

---

### Phase 4 — Evolution Protocol + Feedback Architecture
**Dependency:** All agents running, 90+ days of data

**Milestone 4.1 — Living Skill File Updates**
- [ ] Monthly cadence: review Cultural Awareness Layer in both character skill files
- [ ] Human review interface for proposed changes to core skill files
- [ ] Version control for skill files: every change tracked with rationale

**Milestone 4.2 — Performance Learning Loop**
- [ ] Content performance tracking (engagement quality, not just quantity)
- [ ] Mapping performance data back to: which hook type, which mode, which topic
- [ ] Agent calibration based on performance data

**Milestone 4.3 — Character Evolution**
- [ ] Identify when a character's voice needs to shift (not the banned words — the sensibility)
- [ ] Process: human input → proposed change → skill file update → A/B test
- [ ] "Cannot change" list enforced (see SKILL.md Section 5.4 evolution rules)

---

## Missing External Inputs — Required Before Full Phase 1

These documents are referenced in the system architecture but require external research input that cannot be generated from existing conversations:

### 1. keyword-strategy.md
**What's needed:**
- Primary keyword clusters for Sādhak content (Sanskrit terms + English bridges)
- Search intent mapping: who is searching for this, what are they looking for
- Long-tail keyword opportunities in the spiritual-tech-neuroscience intersection
- X/Twitter hashtag strategy (if any — the character is currently hashtag-free)
- SEO priority: the app vs. X content (different strategies)

**Source:** Keyword research tool output (Ahrefs, SEMrush, or equivalent) + human editorial input

### 2. competitor-research.md
**What's needed:**
- Accounts in the Sādhak discourse ecosystem (direct — similar voices)
- Accounts in the adjacent space (spiritual + neuroscience, spiritual + tech)
- What they do well — the gap the character fills
- What vocabulary/topics they've saturated
- Their posting patterns and engagement quality

**Source:** Manual X research + social analytics tool output

### 3. link-map.md
**What's needed:**
- Content clusters and how they link (for app SEO)
- Core content → supporting content architecture
- Which X threads should link to which app content
- Cross-platform content journey: X → app → newsletter → app (for Sanatan Rising)

**Source:** Content audit once initial pieces are live

### 4. schema-meta-templates.md
**What's needed:**
- Article schema for app/blog content
- FAQ schema for Sanskrit term explanation posts
- Person schema for character/author
- Meta title and description templates by content type
- Open Graph templates for X link previews

**Source:** Technical SEO input + platform specs

---

## Architecture Notes

### Recommended Stack (for reference — architecture is outside this skill's scope)
- **Prompt orchestration:** LangChain or direct Anthropic API calls
- **Skill file storage:** Flat files in version-controlled repo (not a database — files are read directly into prompts)
- **Human review interface:** Simple Next.js UI with approve/reject/edit + annotation
- **Research agent data:** Twitter API (for discourse tracking) + Exa for broader web
- **Feedback loop storage:** Postgres — annotated outputs with metadata

### Skill File Integration Pattern
Skills are injected directly into system prompts. The pattern is:

```
SYSTEM PROMPT =
  [Character Identity — 3-5 sentences from character-bible.md]
  + [Voice Signature — from SKILL.md Section 1]
  + [Banned Vocabulary — from exclusions.md, full list]
  + [Bridge Mechanics — from SKILL.md Section 2.1]
  + [Hook Patterns — from SKILL.md Section 3.3, priority order]
  + [Mode Instructions — from SKILL.md Section 4, current mode only]
  + [Cultural Awareness Snapshot — from SKILL.md Section 5.1-5.2]
```

USER PROMPT = topic + mode + any additional context

**Note:** The full SKILL.md is NOT injected — only the relevant sections per call. This manages context window efficiently and avoids prompt bloat.

---

## Review Cadence

| Review | Frequency | Owner |
|---|---|---|
| Content quality gate review | Per batch (before publishing) | Human |
| Cultural Awareness Layer update | Monthly | Human + Research Agent |
| Skill file calibration | Every 6 weeks | Human (based on performance data) |
| Exclusions list update | Monthly | Human |
| Character evolution check | Quarterly | Human |
| Architecture review | Per phase completion | Tech lead |
