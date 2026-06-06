import { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import { Mic, BookOpen, Globe, Users, Play, Pause, ChevronRight, Star } from 'lucide-react'

const Home = () => {
  const [isPlaying, setIsPlaying] = useState<number | null>(null)
  const [stats, setStats] = useState({
    stories: 0,
    languages: 0,
    contributors: 0,
    hours: 0
  })

  // Animate stats on load
  useEffect(() => {
    const targetStats = { stories: 1247, languages: 15, contributors: 89, hours: 340 }
    const duration = 2000
    const steps = 60
    const interval = duration / steps

    let step = 0
    const timer = setInterval(() => {
      step++
      const progress = step / steps
      setStats({
        stories: Math.floor(targetStats.stories * progress),
        languages: Math.floor(targetStats.languages * progress),
        contributors: Math.floor(targetStats.contributors * progress),
        hours: Math.floor(targetStats.hours * progress)
      })
      if (step >= steps) clearInterval(timer)
    }, interval)

    return () => clearInterval(timer)
  }, [])

  const featuredStories = [
    {
      id: 1,
      title: "The Wise Tortoise",
      language: "Swahili",
      languageCode: "swa",
      narrator: "Mzee Juma",
      duration: "4:32",
      category: "Folktale",
      image: "/story-1.jpg"
    },
    {
      id: 2,
      title: "Origin of the Luo",
      language: "Dholuo",
      languageCode: "luo",
      narrator: "Achieng Ochieng",
      duration: "8:15",
      category: "History",
      image: "/story-2.jpg"
    },
    {
      id: 3,
      title: "The Gourd of Wisdom",
      language: "Luganda",
      languageCode: "lug",
      narrator: "Namusisi Rose",
      duration: "6:20",
      category: "Proverb",
      image: "/story-3.jpg"
    }
  ]

  const languages = [
    { name: "Swahili", code: "swa", stories: 342, color: "bg-earth-500" },
    { name: "Luganda", code: "lug", stories: 189, color: "bg-forest-500" },
    { name: "Kinyarwanda", code: "kin", stories: 156, color: "bg-sunrise-500" },
    { name: "Kikuyu", code: "kik", stories: 98, color: "bg-earth-600" },
    { name: "Dholuo", code: "luo", stories: 87, color: "bg-forest-600" },
    { name: "Yoruba", code: "yor", stories: 76, color: "bg-sunrise-600" }
  ]

  return (
    <div className="space-y-12 animate-fade-in">
      {/* Hero Section */}
      <section className="relative bg-gradient-to-br from-earth-500 via-earth-600 to-earth-700 rounded-3xl overflow-hidden text-white p-8 md:p-12">
        <div className="absolute inset-0 opacity-10">
          <div className="absolute top-0 right-0 w-64 h-64 bg-sunrise-500 rounded-full blur-3xl" />
          <div className="absolute bottom-0 left-0 w-96 h-96 bg-forest-500 rounded-full blur-3xl" />
        </div>
        
        <div className="relative z-10 max-w-3xl">
          <h1 className="text-4xl md:text-6xl font-display font-bold mb-6 leading-tight">
            Where African Stories<br />
            <span className="text-sunrise-400">Live Forever</span>
          </h1>
          <p className="text-lg md:text-xl text-earth-100 mb-8 max-w-2xl">
            Preserve oral traditions, share cultural wisdom, and build AI that understands 
            African languages. Join thousands of storytellers across the continent.
          </p>
          <div className="flex flex-wrap gap-4">
            <Link to="/record" className="btn-secondary inline-flex items-center space-x-2 text-lg">
              <Mic className="w-5 h-5" />
              <span>Record a Story</span>
            </Link>
            <Link to="/stories" className="btn-outline border-white text-white hover:bg-white/10 inline-flex items-center space-x-2 text-lg">
              <BookOpen className="w-5 h-5" />
              <span>Explore Stories</span>
            </Link>
          </div>
        </div>

        {/* Floating Cards */}
        <div className="hidden lg:block absolute right-8 top-1/2 -translate-y-1/2 space-y-4">
          <div className="bg-white/10 backdrop-blur-md rounded-xl p-4 w-64 transform rotate-3 hover:rotate-0 transition duration-300">
            <div className="flex items-center space-x-3">
              <div className="w-10 h-10 bg-sunrise-500 rounded-full flex items-center justify-center">
                <Mic className="w-5 h-5 text-earth-900" />
              </div>
              <div>
                <p className="font-semibold">Just Recorded</p>
                <p className="text-sm text-earth-200">"The Hunter's Wisdom" - Igbo</p>
              </div>
            </div>
          </div>
          <div className="bg-white/10 backdrop-blur-md rounded-xl p-4 w-64 transform -rotate-2 hover:rotate-0 transition duration-300">
            <div className="flex items-center space-x-3">
              <div className="w-10 h-10 bg-forest-500 rounded-full flex items-center justify-center">
                <Globe className="w-5 h-5 text-white" />
              </div>
              <div>
                <p className="font-semibold">15 Languages</p>
                <p className="text-sm text-earth-200">And growing every day</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Stats Section */}
      <section className="grid grid-cols-2 md:grid-cols-4 gap-4">
        {[
          { label: 'Stories', value: stats.stories, icon: BookOpen },
          { label: 'Languages', value: stats.languages, icon: Globe },
          { label: 'Contributors', value: stats.contributors, icon: Users },
          { label: 'Hours of Audio', value: stats.hours, icon: Mic }
        ].map((stat, index) => (
          <div key={index} className="card text-center">
            <stat.icon className="w-8 h-8 mx-auto mb-2 text-earth-500" />
            <p className="text-3xl font-bold text-gray-900">{stat.value.toLocaleString()}</p>
            <p className="text-gray-600">{stat.label}</p>
          </div>
        ))}
      </section>

      {/* Featured Stories */}
      <section>
        <div className="flex items-center justify-between mb-6">
          <h2 className="text-2xl font-display font-bold text-gray-900">Featured Stories</h2>
          <Link to="/stories" className="text-earth-500 hover:text-earth-600 font-medium flex items-center space-x-1">
            <span>View All</span>
            <ChevronRight className="w-5 h-5" />
          </Link>
        </div>

        <div className="grid md:grid-cols-3 gap-6">
          {featuredStories.map((story) => (
            <div key={story.id} className="card group cursor-pointer hover:-translate-y-1 transition">
              <div className="relative aspect-video bg-gray-200 rounded-lg mb-4 overflow-hidden">
                <div className="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent" />
                <span className="language-badge absolute top-3 left-3">
                  {story.language}
                </span>
                <button
                  onClick={() => setIsPlaying(isPlaying === story.id ? null : story.id)}
                  className="absolute inset-0 flex items-center justify-center"
                >
                  <div className="w-14 h-14 bg-white/90 rounded-full flex items-center justify-center group-hover:scale-110 transition">
                    {isPlaying === story.id ? (
                      <Pause className="w-6 h-6 text-earth-600" />
                    ) : (
                      <Play className="w-6 h-6 text-earth-600 ml-1" />
                    )}
                  </div>
                </button>
                <span className="absolute bottom-3 right-3 text-white text-sm font-medium">
                  {story.duration}
                </span>
              </div>
              <h3 className="font-semibold text-lg mb-1 group-hover:text-earth-600 transition">
                {story.title}
              </h3>
              <p className="text-gray-600 text-sm mb-2">by {story.narrator}</p>
              <div className="flex items-center justify-between">
                <span className="text-xs text-gray-500 uppercase tracking-wide">{story.category}</span>
                <div className="flex items-center space-x-1 text-sunrise-500">
                  <Star className="w-4 h-4 fill-current" />
                  <span className="text-sm font-medium">4.9</span>
                </div>
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* Languages Section */}
      <section>
        <div className="flex items-center justify-between mb-6">
          <h2 className="text-2xl font-display font-bold text-gray-900">Supported Languages</h2>
          <Link to="/languages" className="text-earth-500 hover:text-earth-600 font-medium flex items-center space-x-1">
            <span>All Languages</span>
            <ChevronRight className="w-5 h-5" />
          </Link>
        </div>

        <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4">
          {languages.map((lang) => (
            <Link
              key={lang.code}
              to={`/languages/${lang.code}`}
              className="card p-4 text-center hover:shadow-lg transition group"
            >
              <div className={`w-12 h-12 ${lang.color} rounded-full mx-auto mb-3 flex items-center justify-center text-white font-bold text-lg group-hover:scale-110 transition`}>
                {lang.code.toUpperCase()}
              </div>
              <h3 className="font-semibold text-gray-900">{lang.name}</h3>
              <p className="text-sm text-gray-600">{lang.stories} stories</p>
            </Link>
          ))}
        </div>
      </section>

      {/* CTA Section */}
      <section className="bg-forest-500 rounded-2xl p-8 md:p-12 text-white text-center">
        <h2 className="text-3xl font-display font-bold mb-4">Have a Story to Share?</h2>
        <p className="text-lg text-forest-100 mb-8 max-w-2xl mx-auto">
          Every story matters. Record your oral traditions in your language and help preserve 
          African culture for future generations.
        </p>
        <div className="flex flex-wrap justify-center gap-4">
          <Link to="/record" className="bg-white text-forest-700 px-8 py-3 rounded-lg font-semibold hover:bg-forest-50 transition inline-flex items-center space-x-2">
            <Mic className="w-5 h-5" />
            <span>Start Recording</span>
          </Link>
          <Link to="/about" className="border-2 border-white text-white px-8 py-3 rounded-lg font-semibold hover:bg-white/10 transition">
            Learn More
          </Link>
        </div>
      </section>
    </div>
  )
}

export default Home
