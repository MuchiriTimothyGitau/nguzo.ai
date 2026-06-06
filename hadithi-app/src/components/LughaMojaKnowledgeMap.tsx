// LughaMoja Knowledge Map Component
// Extracted from version 1.0 - Visual learning progress tracker

import { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'

interface Concept {
  id: string
  name: string
  description: string
  mastery: number
  prerequisites: string[]
}

interface LughaMojaKnowledgeMapProps {
  language: string
  concepts?: Concept[]
}

const LughaMojaKnowledgeMap = ({ language, concepts: propConcepts }: LughaMojaKnowledgeMapProps) => {
  const [concepts, setConcepts] = useState<Concept[]>([])
  const [loading, setLoading] = useState(true)

  // Default concepts for African language learning
  const defaultConcepts: Concept[] = [
    { id: '1', name: 'Basic Greetings', description: 'Hello, goodbye, thank you', mastery: 85, prerequisites: [] },
    { id: '2', name: 'Numbers 1-10', description: 'Counting basics', mastery: 70, prerequisites: ['1'] },
    { id: '3', name: 'Family Terms', description: 'Mother, father, sibling words', mastery: 60, prerequisites: ['1'] },
    { id: '4', name: 'Common Verbs', description: 'Go, come, eat, drink', mastery: 45, prerequisites: ['1', '2'] },
    { id: '5', name: 'Tonal Basics', description: 'High and low tones', mastery: 30, prerequisites: ['1'] },
    { id: '6', name: 'Past Tense', description: 'Talking about yesterday', mastery: 20, prerequisites: ['4'] },
    { id: '7', name: 'Future Tense', description: 'Talking about tomorrow', mastery: 15, prerequisites: ['4'] },
    { id: '8', name: 'Proverbs', description: 'Wisdom sayings', mastery: 10, prerequisites: ['3', '4', '5'] },
  ]

  useEffect(() => {
    // Simulate loading from IndexedDB or API
    setTimeout(() => {
      setConcepts(propConcepts || defaultConcepts)
      setLoading(false)
    }, 500)
  }, [propConcepts])

  if (loading) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-earth-500"></div>
      </div>
    )
  }

  const getMasteryColor = (mastery: number) => {
    if (mastery >= 80) return '#22c55e' // green-500
    if (mastery >= 50) return '#eab308' // yellow-500
    return '#ef4444' // red-500
  }

  const getMasteryLabel = (mastery: number) => {
    if (mastery >= 80) return 'Mastered'
    if (mastery >= 50) return 'In Progress'
    return 'Needs Work'
  }

  return (
    <div className="space-y-6">
      {/* Legend */}
      <div className="card p-4">
        <div className="flex flex-wrap items-center gap-4 text-sm">
          <span className="font-medium text-gray-700">Mastery Levels:</span>
          <div className="flex items-center gap-2">
            <div className="w-4 h-4 rounded-full bg-red-500"></div>
            <span>Needs Work (0-49%)</span>
          </div>
          <div className="flex items-center gap-2">
            <div className="w-4 h-4 rounded-full bg-yellow-500"></div>
            <span>In Progress (50-79%)</span>
          </div>
          <div className="flex items-center gap-2">
            <div className="w-4 h-4 rounded-full bg-green-500"></div>
            <span>Mastered (80-100%)</span>
          </div>
        </div>
      </div>

      {/* Visual Map */}
      <div className="card p-6 overflow-x-auto">
        <h3 className="text-lg font-semibold mb-4">{language} Learning Path</h3>
        <svg className="w-full" viewBox="0 0 800 400" style={{ minHeight: '400px' }}>
          {/* Draw connections */}
          {concepts.map((concept, idx) => {
            const x = 100 + (idx % 4) * 200
            const y = 80 + Math.floor(idx / 4) * 160
            
            return concept.prerequisites.map(prereqId => {
              const prereqIdx = concepts.findIndex(c => c.id === prereqId)
              if (prereqIdx === -1) return null
              
              const prereqX = 100 + (prereqIdx % 4) * 200
              const prereqY = 80 + Math.floor(prereqIdx / 4) * 160
              
              return (
                <line
                  key={`${prereqId}-${concept.id}`}
                  x1={prereqX}
                  y1={prereqY + 40}
                  x2={x}
                  y2={y - 40}
                  stroke="#d1d5db"
                  strokeWidth="2"
                  markerEnd="url(#arrowhead)"
                />
              )
            })
          })}
          
          {/* Arrow marker */}
          <defs>
            <marker id="arrowhead" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
              <polygon points="0 0, 10 3, 0 6" fill="#d1d5db" />
            </marker>
          </defs>

          {/* Draw nodes */}
          {concepts.map((concept, idx) => {
            const x = 100 + (idx % 4) * 200
            const y = 80 + Math.floor(idx / 4) * 160
            const color = getMasteryColor(concept.mastery)
            
            return (
              <g key={concept.id} className="cursor-pointer hover:opacity-80 transition">
                <circle cx={x} cy={y} r="40" fill={color} opacity="0.2" />
                <circle cx={x} cy={y} r="35" fill={color} />
                <text x={x} y={y} textAnchor="middle" dominantBaseline="middle" className="fill-white font-bold text-sm">
                  {concept.mastery}%
                </text>
                <text x={x} y={y + 55} textAnchor="middle" className="fill-gray-700 text-xs font-medium">
                  {concept.name.length > 15 ? concept.name.substring(0, 15) + '...' : concept.name}
                </text>
              </g>
            )
          })}
        </svg>
      </div>

      {/* Concept List */}
      <div className="card">
        <h3 className="text-lg font-semibold mb-4">Concept Details</h3>
        <div className="grid gap-3">
          {concepts.map(concept => (
            <div
              key={concept.id}
              className="flex items-center justify-between p-4 border border-gray-200 rounded-lg hover:border-earth-400 transition"
            >
              <div className="flex-1">
                <div className="flex items-center gap-3">
                  <div 
                    className="w-10 h-10 rounded-full flex items-center justify-center text-white font-bold text-sm"
                    style={{ backgroundColor: getMasteryColor(concept.mastery) }}
                  >
                    {concept.mastery}%
                  </div>
                  <div>
                    <div className="font-semibold">{concept.name}</div>
                    <div className="text-sm text-gray-600">{concept.description}</div>
                  </div>
                </div>
              </div>
              <div className="text-right">
                <span className={`text-xs px-2 py-1 rounded-full ${
                  concept.mastery >= 80 ? 'bg-green-100 text-green-700' :
                  concept.mastery >= 50 ? 'bg-yellow-100 text-yellow-700' :
                  'bg-red-100 text-red-700'
                }`}>
                  {getMasteryLabel(concept.mastery)}
                </span>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}

export default LughaMojaKnowledgeMap
