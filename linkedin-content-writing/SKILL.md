---
name: linkedin-content-writing
version: 1.0.0
description: >
  Standalone LinkedIn content writing skill for topic discovery, topic suggestion,
  user topic selection, and post planning/execution using current LinkedIn format
  and engagement strategy. Invoke when the user asks for LinkedIn thought
  leadership posts, founder/operator posts, personal brand growth posts, or
  LinkedIn content calendars. Built on content-writing-core and informed by
  search-growth-system principles.
invoke_with: content-writing-core
recommended_companions: search-growth-system
---

# LinkedIn Content Writing Skill

This skill is a complete operating flow for LinkedIn content:

1. discover topics from live web signals (via MCP web search),
2. suggest ranked topic options,
3. ask user to choose/refine topic,
4. plan the content before drafting,
5. produce LinkedIn-native post output for 2026 reading behavior.

---

## 1) Dependencies and Inputs

### Required
- `audience` (who this post is for)
- `objective` (awareness, credibility, inbound leads, hiring, newsletter growth, etc.)

### Recommended
- `niche/domain`
- `personal POV` or operating experience
- `offer/context` (if conversion-oriented)

### MCP Requirement
This skill expects access to an MCP web-search tool (e.g., Tavily/Brave/SerpAPI MCP).

Preferred MCP tool capabilities:
- keyword/news search with recency filters,
- result snippets + source URLs,
- optional domain filtering,
- optional query refinement support.

If MCP is unavailable, fall back to:
- internal knowledge,
- prior user context,
- and clearly state: “topic suggestions are non-live and not web-validated.”

### MCP Tool Contract (Recommended)
If you are implementing a custom MCP server, expose tools similar to:
- `search_topic_signals(query, audience, timeframe)`
- `collect_source_snippets(query, max_results)`
- `research_topic_angle(topic, audience, objective)`

Any equivalent naming is fine if behavior is the same.

---

## 2) Core Behavior Sequence (Mandatory)

### Step A — Topic Discovery (Web + Context)
Use MCP search to collect:
- trend shifts,
- high-friction pain points,
- recurring buyer/operator questions,
- contrarian narratives,
- recent market conversations.

Generate a **Topic Radar** table:
- topic
- why-now signal
- relevance to target audience
- content angle
- confidence (high/medium/low)

### Step B — Suggest Topic List
Return 5–10 topic options ranked by:
1. audience relevance,
2. uniqueness of angle,
3. expected engagement quality,
4. business/brand fit.

For each topic provide:
- one-line angle,
- best post type (story / framework / contrarian / case note),
- estimated engagement potential.

### Step C — Ask for Topic Selection
Always ask the user to:
- pick one topic, or
- merge two topics, or
- request a tighter niche.

Do not draft full content before topic confirmation unless the user explicitly asks.

### Step D — Content Planning Before Writing
After topic confirmation, produce a **LinkedIn Content Plan**:
- target reader persona
- awareness level (Schwartz)
- single core claim
- hook options (3)
- evidence/proof blocks
- structure choice
- CTA/comment strategy
- optional repurposing notes

### Step E — Draft in LinkedIn-Native Format
Write the post using:
- hard hook in line 1,
- short line breaks,
- one core idea,
- specific observations,
- practical takeaway,
- clean close (engagement prompt without bait).

---

## 3) Voice and Tone System

## Voice Base (from content-writing-core)
- Clarity first
- Specificity over abstraction
- Peer-to-peer stance
- No corporate jargon
- No guru posture

### Influence Blend (Default)
- Paul Graham: clear contrarian reasoning
- Morgan Housel: story → principle mechanics
- Orwell: plain language discipline
- Dan Koe: hook and scroll architecture

### Tone Rules
- calm conviction, not hype
- direct, non-performative
- analytical + human
- no inflated claims

### Banned Patterns
- “In today’s fast-paced world…”
- vague “thought leader” platitudes
- engagement bait (“agree?”, “thoughts?”, “comment YES”)
- generic AI phrasing without lived specificity

---

## 4) LinkedIn 2026 Format and Engagement Rules

### Structural Defaults
- 1 strong opening line before fold
- 8–20 short lines for readability
- 1 idea per post
- 1 closing action
- 0–3 emojis (only if voice-fit)
- 3–5 hashtags max (optional, only relevant)

### High-Performing Post Types
1. **Operator Story** — real incident → lesson → framework
2. **Contrarian Insight** — common belief → reframe → evidence
3. **Field Note** — what changed recently in market/workflow
4. **Mini Framework** — 3-part model with practical use
5. **Mistake Debrief** — what failed, what changed, what now works

### Engagement Strategy (Non-Bait)
- ask a specific professional question at close
- invite counterexamples, not validation
- seed 1st comment with extra context/checklist
- prioritize save-worthy specificity over reach-bait

---

## 5) Planning Output Template

When asked to plan, return this format:

```md
## LinkedIn Topic Plan
- Topic:
- Audience:
- Objective:
- Why now (web signals):

## Core Claim
-

## Hook Options (3)
1.
2.
3.

## Structure
- Type:
- Outline:

## Evidence Blocks
- Data/observation:
- Story/proof:
- Optional citation/source direction:

## Engagement Close
- CTA/comment prompt:
- First comment seed:
```

---

## 6) Draft Output Modes

When generating content, support:
- **Mode A:** One polished LinkedIn post
- **Mode B:** 3 post variants (different hooks)
- **Mode C:** Weekly 5-post plan
- **Mode D:** One post + carousel outline + comment strategy

---

## 7) Guardrails

- Never generate fake metrics/case studies.
- Mark uncertain claims as hypotheses.
- Do not write broad advice without audience context.
- Keep one-post/one-idea discipline.
- If no web data is available, disclose it explicitly.

---

## 8) Prompting Contract (How to run this skill)

1. Discover and rank topics via MCP web search.
2. Ask user to select/refine topic.
3. Build a content plan first.
4. Then draft LinkedIn post in current platform style.

If user asks directly for writing without topic research, skip Step 1 but state the tradeoff.

---

## 9) Related Skills and Sources

- **content-writing-core**: baseline writing quality and voice discipline
- **search-growth-system**: evidence-first discovery, prioritization, and operating rigor
- Other specialized writing agents/skills may be used for research support, but this skill owns LinkedIn output formatting and engagement strategy.
