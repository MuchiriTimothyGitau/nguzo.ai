import { useState } from 'react'
import { Play, Pause, Search, Filter, Clock, User, Tag } from 'lucide-react'

const Stories = () => {
  const [searchQuery, setSearchQuery] = useState('')
  const [selectedLanguage, setSelectedLanguage] = useState('all')
  const [selectedCategory, setSelectedCategory] = useState('all')
  const [playingId, setPlayingId] = useState<number | null>(null)

  const stories = [
    {
      id: 1,
      title: "The Wise Tortoise",
      language: "Swahili",
      languageCode: "swa",
      narrator: "Mzee Juma",
      duration: "4:32",
      category: "Folktale",
      description: "A story about wisdom and patience from the Swahili coast.",
      dateAdded: "2026-05-01"
    },
    {
      id: 2,
      title: "Origin of the Luo",
      language: "Dholuo",
      languageCode: "luo",
      narrator: "Achieng Ochieng",
      duration: "8:15",
      category: "History",
      description: "The ancient story of how the Luo people came to Kenya.",
      dateAdded: "2026-04-28"
    },
    {
      id: 3,
      title: "The Gourd of Wisdom",
      language: "Luganda",
      languageCode: "lug",
      narrator: "Namusisi Rose",
      duration: "6:20",
      category: "Proverb",
      description: "A Baganda tale about the value of wisdom over strength.",
      dateAdded: "2026-04-25"
    },
    {
      id: 4,
      title: "The Hunter's Song",
      language: "Kikuyu",
      languageCode: "kik",
      narrator: "Wanjiku Kamau",
      duration: "3:45",
      category: "Song",
      description: "Traditional hunting song from central Kenya.",
      dateAdded: "2026-04-20"
    },
    {
      id: 5,
      title: "Rwanda Creation Myth",
      language: "Kinyarwanda",
      languageCode: "kin",
      narrator: "Ndayisaba Jean",
      duration: "12:30",
      category: "History",
      description: "The origin story of the Rwandan people.",
      dateAdded: "2026-04-15"
    },
    {
      id: 6,
      title: "The Clever Hare",
      language: "Swahili",
      languageCode: "swa",
      narrator: "Mwangi Peter",
      duration: "5:10",
      category: "Folktale",
      description: "A trickster tale featuring the clever hare Sungura.",
      dateAdded: "2026-04-10"
    }
  ]

  const languages = ['all', 'Swahili', 'Dholuo', 'Luganda', 'Kikuyu', 'Kinyarwanda']
  const categories = ['all', 'Folktale', 'History', 'Proverb', 'Song', 'Poetry']

  const filteredStories = stories.filter(story => {
    const matchesSearch = story.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
                         story.narrator.toLowerCase().includes(searchQuery.toLowerCase())
    const matchesLanguage = selectedLanguage === 'all' || story.language === selectedLanguage
    const matchesCategory = selectedCategory === 'all' || story.category === selectedCategory
    return matchesSearch && matchesLanguage && matchesCategory
  })

  return (
    <div className="space-y-6 animate-fade-in">
      <div className="text-center mb-8">
        <h1 className="text-3xl font-display font-bold text-gray-900 mb-2">Stories</h1>
        <p className="text-gray-600">Explore oral traditions from across Africa</p>
      </div>

      {/* Search and Filters */}
      <div className="card space-y-4">
        <div className="relative">
          <Search className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
          <input
            type="text"
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            placeholder="Search stories, narrators..."
            className="input-field pl-12"
          />
        </div>

        <div className="flex flex-wrap gap-4">
          <div className="flex items-center space-x-2">
            <Filter className="w-4 h-4 text-gray-500" />
            <select
              value={selectedLanguage}
              onChange={(e) => setSelectedLanguage(e.target.value)}
              className="input-field py-2 w-40"
            >
              <option value="all">All Languages</option>
              {languages.slice(1).map(lang => (
                <option key={lang} value={lang}>{lang}</option>
              ))}
            </select>
          </div>

          <select
            value={selectedCategory}
            onChange={(e) => setSelectedCategory(e.target.value)}
            className="input-field py-2 w-40"
          >
            <option value="all">All Categories</option>
            {categories.slice(1).map(cat => (
              <option key={cat} value={cat}>{cat}</option>
            ))}
          </select>
        </div>
      </div>

      {/* Results Count */}
      <p className="text-sm text-gray-500">
        Showing {filteredStories.length} of {stories.length} stories
      </p>

      {/* Stories Grid */}
      <div className="grid md:grid-cols-2 gap-4">
        {filteredStories.map((story) => (
          <div key={story.id} className="card hover:shadow-lg transition group">
            <div className="flex items-start justify-between mb-3">
              <div>
                <h3 className="font-semibold text-lg text-gray-900 group-hover:text-earth-600 transition">
                  {story.title}
                </h3>
                <p className="text-sm text-gray-500">{story.description}</p>
              </div>
              <span className="language-badge">{story.language}</span>
            </div>

            <div className="flex items-center space-x-4 text-sm text-gray-600 mb-4">
              <span className="flex items-center space-x-1">
                <User className="w-4 h-4" />
                <span>{story.narrator}</span>
              </span>
              <span className="flex items-center space-x-1">
                <Clock className="w-4 h-4" />
                <span>{story.duration}</span>
              </span>
              <span className="flex items-center space-x-1">
                <Tag className="w-4 h-4" />
                <span>{story.category}</span>
              </span>
            </div>

            <button
              onClick={() => setPlayingId(playingId === story.id ? null : story.id)}
              className="btn-primary w-full flex items-center justify-center space-x-2"
            >
              {playingId === story.id ? (
                <>
                  <Pause className="w-5 h-5" />
                  <span>Pause</span>
                </>
              ) : (
                <>
                  <Play className="w-5 h-5" />
                  <span>Listen</span>
                </>
              )}
            </button>
          </div>
        ))}
      </div>

      {filteredStories.length === 0 && (
        <div className="text-center py-12">
          <p className="text-gray-500">No stories found matching your criteria.</p>
          <button
            onClick={() => {
              setSearchQuery('')
              setSelectedLanguage('all')
              setSelectedCategory('all')
            }}
            className="text-earth-500 hover:text-earth-600 mt-2"
          >
            Clear filters
          </button>
        </div>
      )}
    </div>
  )
}

export default Stories
