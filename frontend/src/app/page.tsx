"use client"

import { useState, useEffect } from "react"
import { PlayCircle, FileText, CheckCircle2, RotateCw, XCircle, LayoutDashboard, Settings } from "lucide-react"

import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { Badge } from "@/components/ui/badge"

const API_BASE_URL = "http://localhost:8000/api"

export default function Dashboard() {
  const [topic, setTopic] = useState("")
  const [pageType, setPageType] = useState("blog_post")
  const [isSubmitting, setIsSubmitting] = useState(false)
  const [pipelines, setPipelines] = useState<any[]>([])

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
    switch (status) {
      case "published": return <Badge variant="success" className="bg-emerald-500"><CheckCircle2 className="w-3 h-3 mr-1" /> Published</Badge>
      case "failed": return <Badge variant="destructive" className="bg-red-500"><XCircle className="w-3 h-3 mr-1" /> Failed</Badge>
      case "writing": return <Badge variant="warning" className="bg-amber-500 text-white"><RotateCw className="w-3 h-3 mr-1 animate-spin" /> Writing</Badge>
      case "editing": return <Badge variant="warning" className="bg-orange-500 text-white"><RotateCw className="w-3 h-3 mr-1 animate-spin" /> Editing</Badge>
      case "revision": return <Badge variant="warning" className="bg-blue-500 text-white"><RotateCw className="w-3 h-3 mr-1 animate-spin" /> Revision</Badge>
      default: return <Badge variant="secondary"><RotateCw className="w-3 h-3 mr-1 animate-spin" /> {status}</Badge>
    }
  }

  return (
    <div className="min-h-screen bg-zinc-50 text-zinc-950 font-sans">
      <header className="sticky top-0 z-30 flex items-center h-16 px-6 border-b border-zinc-200 bg-white shadow-sm">
        <div className="flex items-center gap-2 font-bold text-lg tracking-tight">
          <LayoutDashboard className="w-5 h-5 text-indigo-600" />
          Content Agent CMS
        </div>
        <div className="ml-auto flex items-center gap-4">
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
        </div>

        {/* Right Column - Kanban / List */}
        <div className="lg:col-span-8 flex flex-col gap-4">
          <div className="flex items-center justify-between">
            <h2 className="text-xl font-semibold tracking-tight">Active Pipelines</h2>
            <Badge variant="outline" className="px-3 py-1 font-medium bg-white shadow-sm">
              {pipelines.length} In Progress
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
                <Card key={p.id} className="overflow-hidden bg-white/50 backdrop-blur-sm transition-shadow hover:shadow-md border-zinc-200">
                  <div className="flex flex-col md:flex-row gap-4 p-5">
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
                      </div>

                      {/* Show scorecard if metadata exists and it has score */}
                      {p.metadata_json && p.metadata_json.total_score !== undefined && (
                        <div className="mt-4 pt-4 border-t border-zinc-100 grid grid-cols-2 md:grid-cols-4 gap-2">
                          <div className="bg-indigo-50/50 p-2 rounded flex flex-col items-center justify-center text-center">
                            <span className="text-[10px] uppercase font-bold text-indigo-500 tracking-wider">Overall Score</span>
                            <span className="text-lg font-black text-indigo-700">{p.metadata_json.total_score || "N/A"}</span>
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
                        </div>
                      )}
                    </div>

                    {p.content && (
                      <div className="w-full md:w-32 flex flex-col justify-center border-t md:border-t-0 md:border-l border-zinc-100 pt-4 md:pt-0 md:pl-4">
                        <Button variant="outline" size="sm" className="w-full relative group">
                          View Draft
                          <span className="absolute right-0 w-2 h-2 mr-2 rounded-full bg-emerald-500 animate-pulse" />
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
    </div>
  )
}
