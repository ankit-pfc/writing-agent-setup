"use client"

import { useState, useEffect } from "react"
import { PlayCircle, FileText, CheckCircle2, RotateCw, XCircle, LayoutDashboard, Settings, Search, PenTool, Edit3, Sparkles, Upload, MessageSquare } from "lucide-react"

import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { Badge } from "@/components/ui/badge"

const API_BASE_URL = "http://localhost:8000/api"

// Pipeline stage definitions with icons and colors
const STAGES = {
  pending: { label: "Pending", icon: RotateCw, color: "bg-zinc-500", textColor: "text-zinc-700" },
  brief: { label: "Brief", icon: FileText, color: "bg-blue-500", textColor: "text-blue-700" },
  research: { label: "Research", icon: Search, color: "bg-cyan-500", textColor: "text-cyan-700" },
  writing: { label: "Writing", icon: PenTool, color: "bg-amber-500", textColor: "text-amber-700" },
  editing: { label: "Editing", icon: Edit3, color: "bg-orange-500", textColor: "text-orange-700" },
  revision: { label: "Revision", icon: RotateCw, color: "bg-purple-500", textColor: "text-purple-700" },
  seo_optimization: { label: "SEO", icon: Sparkles, color: "bg-indigo-500", textColor: "text-indigo-700" },
  published: { label: "Published", icon: CheckCircle2, color: "bg-emerald-500", textColor: "text-emerald-700" },
  failed: { label: "Failed", icon: XCircle, color: "bg-red-500", textColor: "text-red-700" },
}

interface Pipeline {
  id: string
  topic: string
  page_type: string
  status: string
  revision_count?: number
  max_revisions?: number
  content?: string
  metadata_json?: {
    total_score?: number
    status?: string
    feedback?: string
    dimension_1_depth?: number
    dimension_3_voice?: number
    dimension_6_exclusion_safety?: number
    seo_score?: {
      score?: number
      grade?: string
    }
    revision_feedback?: string
  }
  seo_output?: {
    optimization_summary?: {
      meta_title_length?: number
      internal_links_added?: number
      schema_type?: string
      aeo_blocks_added?: number
    }
    meta_tags?: {
      title?: string
      description?: string
    }
  }
  created_at?: string
  updated_at?: string
}

export default function Dashboard() {
  const [topic, setTopic] = useState("")
  const [pageType, setPageType] = useState("blog_post")
  const [isSubmitting, setIsSubmitting] = useState(false)
  const [pipelines, setPipelines] = useState<Pipeline[]>([])
  const [selectedPipeline, setSelectedPipeline] = useState<Pipeline | null>(null)

  const fetchPipelines = async () => {
    try {
      const res = await fetch(`${API_BASE_URL}/pipelines`)
      if (res.ok) {
        const data = await res.json()
        setPipelines(data)
      }
    } catch (e) {
      console.error("Failed to fetch pipelines", e)
    }
  }

  useEffect(() => {
    fetchPipelines()
    const interval = setInterval(fetchPipelines, 3000)
    return () => clearInterval(interval)
  }, [])

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    if (!topic.trim()) return

    setIsSubmitting(true)
    try {
      const res = await fetch(`${API_BASE_URL}/generate`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ topic, page_type: pageType })
      })

      if (res.ok) {
        setTopic("")
        fetchPipelines()
      } else {
        console.error("Generation failed", await res.text())
      }
    } catch (error) {
      console.error("Network error", error)
    } finally {
      setIsSubmitting(false)
    }
  }

  const getStatusBadge = (status: string) => {
    const stage = STAGES[status as keyof typeof STAGES] || STAGES.pending
    const Icon = stage.icon
    const isAnimating = ["writing", "editing", "revision", "research", "brief", "seo_optimization"].includes(status)

    return (
      <Badge variant="secondary" className={`${stage.color} text-white`}>
        <Icon className={`w-3 h-3 mr-1 ${isAnimating ? "animate-spin" : ""}`} />
        {stage.label}
      </Badge>
    )
  }

  const getStageProgress = (status: string) => {
    const stageOrder = ["pending", "brief", "research", "writing", "editing", "revision", "seo_optimization", "published"]
    const currentIndex = stageOrder.indexOf(status)
    const progress = ((currentIndex + 1) / stageOrder.length) * 100
    return Math.min(progress, 100)
  }

  return (
    <div className="min-h-screen bg-zinc-50 text-zinc-950 font-sans">
      <header className="sticky top-0 z-30 flex items-center h-16 px-6 border-b border-zinc-200 bg-white shadow-sm">
        <div className="flex items-center gap-2 font-bold text-lg tracking-tight">
          <LayoutDashboard className="w-5 h-5 text-indigo-600" />
          Content Agent CMS
        </div>
        <div className="ml-auto flex items-center gap-4">
          <Badge variant="outline" className="bg-indigo-50 text-indigo-700 border-indigo-200">
            Phase 2 Active
          </Badge>
          <Button variant="ghost" size="sm" className="hidden md:flex">
            <Settings className="w-4 h-4 mr-2" />
            Agent Config
          </Button>
        </div>
      </header>

      <main className="container mx-auto p-6 grid grid-cols-1 lg:grid-cols-12 gap-6">
        {/* Left Column - Submission Form */}
        <div className="lg:col-span-4 space-y-6">
          <Card className="border-indigo-100 shadow-indigo-100/20">
            <CardHeader className="bg-gradient-to-br from-indigo-50 to-white rounded-t-xl border-b border-indigo-50">
              <CardTitle className="text-xl">New Pipeline</CardTitle>
              <CardDescription>Initiate an autonomous content generation.</CardDescription>
            </CardHeader>
            <CardContent className="pt-6">
              <form onSubmit={handleSubmit} className="space-y-4">
                <div className="space-y-2">
                  <Label htmlFor="topic">Topic / Keyword</Label>
                  <Input
                    id="topic"
                    placeholder="e.g. Best meditation for beginners"
                    value={topic}
                    onChange={(e) => setTopic(e.target.value)}
                    required
                    className="focus-visible:ring-indigo-500"
                  />
                </div>

                <div className="space-y-2">
                  <Label htmlFor="type">Page Type</Label>
                  <select
                    id="type"
                    className="flex h-10 w-full rounded-md border border-zinc-200 bg-white px-3 py-2 text-sm focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-indigo-500"
                    value={pageType}
                    onChange={(e) => setPageType(e.target.value)}
                  >
                    <option value="blog_post">Blog Post</option>
                    <option value="glossary_term">Glossary Term</option>
                    <option value="comparison">Comparison Guide</option>
                    <option value="how_to">How-To Guide</option>
                  </select>
                </div>

                <Button
                  type="submit"
                  disabled={isSubmitting || !topic.trim()}
                  className="w-full bg-indigo-600 hover:bg-indigo-700 text-white shadow-md shadow-indigo-200 transition-all"
                >
                  {isSubmitting ? (
                    <><RotateCw className="w-4 h-4 mr-2 animate-spin" /> Starting...</>
                  ) : (
                    <><PlayCircle className="w-4 h-4 mr-2" /> Generate Content</>
                  )}
                </Button>
              </form>
            </CardContent>
          </Card>

          {/* Pipeline Stages Legend */}
          <Card>
            <CardHeader className="pb-3">
              <CardTitle className="text-sm font-medium">Pipeline Stages</CardTitle>
            </CardHeader>
            <CardContent className="grid grid-cols-2 gap-2 text-xs">
              {Object.entries(STAGES).map(([key, stage]) => {
                const Icon = stage.icon
                return (
                  <div key={key} className="flex items-center gap-2">
                    <div className={`w-2 h-2 rounded-full ${stage.color}`} />
                    <Icon className="w-3 h-3 text-zinc-500" />
                    <span className="text-zinc-600">{stage.label}</span>
                  </div>
                )
              })}
            </CardContent>
          </Card>
        </div>

        {/* Right Column - Kanban / List */}
        <div className="lg:col-span-8 flex flex-col gap-4">
          <div className="flex items-center justify-between">
            <h2 className="text-xl font-semibold tracking-tight">Active Pipelines</h2>
            <Badge variant="outline" className="px-3 py-1 font-medium bg-white shadow-sm">
              {pipelines.length} Total
            </Badge>
          </div>

          <div className="grid grid-cols-1 gap-4">
            {pipelines.length === 0 ? (
              <div className="text-center py-16 px-4 bg-white rounded-xl border border-zinc-200 shadow-sm">
                <FileText className="w-12 h-12 text-zinc-300 mx-auto mb-3" />
                <h3 className="text-lg font-medium text-zinc-900">No active pipelines</h3>
                <p className="text-zinc-500 text-sm mt-1">Start a new generation on the left to see it appear here.</p>
              </div>
            ) : (
              pipelines.map((p) => (
                <Card
                  key={p.id}
                  className={`overflow-hidden bg-white/50 backdrop-blur-sm transition-shadow hover:shadow-md border-zinc-200 cursor-pointer ${selectedPipeline?.id === p.id ? 'ring-2 ring-indigo-500' : ''}`}
                  onClick={() => setSelectedPipeline(p)}
                >
                  <div className="flex flex-col gap-4 p-5">
                    {/* Header Row */}
                    <div className="flex items-start justify-between">
                      <div className="flex-1 space-y-2">
                        <div className="flex items-center gap-3">
                          <h3 className="font-semibold text-lg text-zinc-900 line-clamp-1" title={p.topic}>
                            {p.topic}
                          </h3>
                          {getStatusBadge(p.status)}
                        </div>
                        <div className="flex items-center gap-3 text-sm text-zinc-500">
                          <span className="capitalize px-2 py-0.5 bg-zinc-100 rounded-md text-xs font-medium">
                            {p.page_type.replace("_", " ")}
                          </span>
                          <span className="font-mono text-xs text-zinc-400">ID: {p.id.split('-')[0]}</span>
                          {p.revision_count !== undefined && p.revision_count > 0 && (
                            <span className="text-purple-600 text-xs">
                              Rev {p.revision_count}/{p.max_revisions || 3}
                            </span>
                          )}
                        </div>
                      </div>
                    </div>

                    {/* Progress Bar */}
                    <div className="w-full bg-zinc-100 rounded-full h-1.5">
                      <div
                        className={`h-1.5 rounded-full transition-all duration-500 ${p.status === 'failed' ? 'bg-red-500' :
                            p.status === 'published' ? 'bg-emerald-500' : 'bg-indigo-500'
                          }`}
                        style={{ width: `${getStageProgress(p.status)}%` }}
                      />
                    </div>

                    {/* Scorecard Grid */}
                    {p.metadata_json && p.metadata_json.total_score !== undefined && (
                      <div className="grid grid-cols-2 md:grid-cols-5 gap-2">
                        <div className="bg-indigo-50/50 p-2 rounded flex flex-col items-center justify-center text-center">
                          <span className="text-[10px] uppercase font-bold text-indigo-500 tracking-wider">Quality</span>
                          <span className="text-lg font-black text-indigo-700">{p.metadata_json.total_score}</span>
                        </div>
                        <div className="bg-zinc-50 p-2 rounded flex flex-col items-center justify-center text-center">
                          <span className="text-[10px] uppercase font-bold text-zinc-500 tracking-wider">Safety</span>
                          <span className="text-sm font-semibold text-zinc-700">{p.metadata_json.dimension_6_exclusion_safety}/10</span>
                        </div>
                        <div className="bg-zinc-50 p-2 rounded flex flex-col items-center justify-center text-center">
                          <span className="text-[10px] uppercase font-bold text-zinc-500 tracking-wider">Depth</span>
                          <span className="text-sm font-semibold text-zinc-700">{p.metadata_json.dimension_1_depth}/10</span>
                        </div>
                        <div className="bg-zinc-50 p-2 rounded flex flex-col items-center justify-center text-center">
                          <span className="text-[10px] uppercase font-bold text-zinc-500 tracking-wider">Voice</span>
                          <span className="text-sm font-semibold text-zinc-700">{p.metadata_json.dimension_3_voice}/10</span>
                        </div>
                        {p.metadata_json.seo_score && (
                          <div className="bg-emerald-50/50 p-2 rounded flex flex-col items-center justify-center text-center">
                            <span className="text-[10px] uppercase font-bold text-emerald-500 tracking-wider">SEO</span>
                            <span className="text-sm font-semibold text-emerald-700">{p.metadata_json.seo_score.grade || '-'}</span>
                          </div>
                        )}
                      </div>
                    )}

                    {/* SEO Output Summary */}
                    {p.seo_output && p.seo_output.optimization_summary && (
                      <div className="text-xs text-zinc-500 flex flex-wrap gap-3 pt-2 border-t border-zinc-100">
                        <span>Title: {p.seo_output.optimization_summary.meta_title_length} chars</span>
                        <span>Links: {p.seo_output.optimization_summary.internal_links_added}</span>
                        <span>Schema: {p.seo_output.optimization_summary.schema_type}</span>
                        <span>AEO: {p.seo_output.optimization_summary.aeo_blocks_added} blocks</span>
                      </div>
                    )}

                    {/* Feedback indicator */}
                    {p.metadata_json?.revision_feedback && (
                      <div className="flex items-center gap-2 text-xs text-purple-600 bg-purple-50 px-2 py-1 rounded">
                        <MessageSquare className="w-3 h-3" />
                        <span className="truncate">{p.metadata_json.revision_feedback}</span>
                      </div>
                    )}

                    {/* Action Button */}
                    {p.content && (
                      <div className="flex justify-end pt-2 border-t border-zinc-100">
                        <Button variant="outline" size="sm" className="relative group">
                          <FileText className="w-4 h-4 mr-2" />
                          View Draft
                          {p.status === 'published' && (
                            <span className="absolute -top-1 -right-1 w-2 h-2 rounded-full bg-emerald-500" />
                          )}
                        </Button>
                      </div>
                    )}
                  </div>
                </Card>
              ))
            )}
          </div>
        </div>
      </main>

      {/* Selected Pipeline Detail Modal (simplified - shows content) */}
      {selectedPipeline && selectedPipeline.content && (
        <div className="fixed inset-0 bg-black/50 z-50 flex items-center justify-center p-4" onClick={() => setSelectedPipeline(null)}>
          <Card className="max-w-4xl w-full max-h-[80vh] overflow-hidden" onClick={e => e.stopPropagation()}>
            <CardHeader className="flex flex-row items-center justify-between">
              <div>
                <CardTitle>{selectedPipeline.topic}</CardTitle>
                <CardDescription>{selectedPipeline.page_type.replace('_', ' ')} • {selectedPipeline.status}</CardDescription>
              </div>
              <Button variant="ghost" size="sm" onClick={() => setSelectedPipeline(null)}>✕</Button>
            </CardHeader>
            <CardContent className="overflow-auto max-h-[60vh]">
              <pre className="whitespace-pre-wrap text-sm text-zinc-700 font-sans">
                {selectedPipeline.content}
              </pre>
            </CardContent>
          </Card>
        </div>
      )}
    </div>
  )
}