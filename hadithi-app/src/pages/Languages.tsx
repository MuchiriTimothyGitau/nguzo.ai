import { Mic, BookOpen, Users, Headphones } from 'lucide-react'

const Languages = () => {
  const languages = [
    {
      name: "Swahili",
      nativeName: "Kiswahili",
      code: "swa",
      speakers: "200M+",
      region: "East Africa",
      stories: 342,
      contributors: 45,
      color: "bg-earth-500",
      status: "Active"
    },
    {
      name: "Luganda",
      nativeName: "Luganda",
      code: "lug",
      speakers: "8M",
      region: "Uganda",
      stories: 189,
      contributors: 28,
      color: "bg-forest-500",
      status: "Active"
    },
    {
      name: "Kinyarwanda",
      nativeName: "Kinyarwanda",
      code: "kin",
      speakers: "12M",
      region: "Rwanda, DRC",
      stories: 156,
      contributors: 22,
      color: "bg-sunrise-500",
      status: "Active"
    },
    {
      name: "Kikuyu",
      nativeName: "Gĩkũyũ",
      code: "kik",
      speakers: "6.6M",
      region: "Kenya",
      stories: 98,
      contributors: 15,
      color: "bg-earth-600",
      status: "Growing"
    },
    {
      name: "Dholuo",
      nativeName: "Dholuo",
      code: "luo",
      speakers: "4.2M",
      region: "Kenya, Tanzania",
      stories: 87,
      contributors: 12,
      color: "bg-forest-600",
      status: "Growing"
    },
    {
      name: "Yoruba",
      nativeName: "Yorùbá",
      code: "yor",
      speakers: "40M",
      region: "Nigeria, Benin",
      stories: 76,
      contributors: 18,
      color: "bg-sunrise-600",
      status: "Beta"
    },
    {
      name: "Igbo",
      nativeName: "Igbo",
      code: "ibo",
      speakers: "27M",
      region: "Nigeria",
      stories: 43,
      contributors: 9,
      color: "bg-earth-400",
      status: "Beta"
    },
    {
      name: "Amharic",
      nativeName: "አማርኛ",
      code: "amh",
      speakers: "32M",
      region: "Ethiopia",
      stories: 34,
      contributors: 7,
      color: "bg-forest-400",
      status: "Coming Soon"
    }
  ]

  return (
    <div className="space-y-6 animate-fade-in">
      <div className="text-center mb-8">
        <h1 className="text-3xl font-display font-bold text-gray-900 mb-2">Languages</h1>
        <p className="text-gray-600">African languages supported by Hadithi</p>
      </div>

      {/* Stats Overview */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
        <div className="card text-center">
          <Globe className="w-8 h-8 mx-auto mb-2 text-earth-500" />
          <p className="text-2xl font-bold">15</p>
          <p className="text-sm text-gray-600">Languages</p>
        </div>
        <div className="card text-center">
          <BookOpen className="w-8 h-8 mx-auto mb-2 text-forest-500" />
          <p className="text-2xl font-bold">1,247</p>
          <p className="text-sm text-gray-600">Stories</p>
        </div>
        <div className="card text-center">
          <Users className="w-8 h-8 mx-auto mb-2 text-sunrise-500" />
          <p className="text-2xl font-bold">89</p>
          <p className="text-sm text-gray-600">Contributors</p>
        </div>
        <div className="card text-center">
          <Headphones className="w-8 h-8 mx-auto mb-2 text-earth-500" />
          <p className="text-2xl font-bold">340</p>
          <p className="text-sm text-gray-600">Hours</p>
        </div>
      </div>

      {/* Language Grid */}
      <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-4">
        {languages.map((lang) => (
          <div key={lang.code} className="card hover:shadow-lg transition group">
            <div className="flex items-start justify-between mb-4">
              <div className="flex items-center space-x-3">
                <div className={`w-14 h-14 ${lang.color} rounded-xl flex items-center justify-center text-white font-bold text-lg`}>
                  {lang.code.toUpperCase()}
                </div>
                <div>
                  <h3 className="font-semibold text-lg text-gray-900">{lang.name}</h3>
                  <p className="text-sm text-gray-500">{lang.nativeName}</p>
                </div>
              </div>
              <span className={`px-2 py-1 rounded-full text-xs font-medium ${
                lang.status === 'Active' ? 'bg-green-100 text-green-700' :
                lang.status === 'Growing' ? 'bg-blue-100 text-blue-700' :
                lang.status === 'Beta' ? 'bg-yellow-100 text-yellow-700' :
                'bg-gray-100 text-gray-600'
              }`}>
                {lang.status}
              </span>
            </div>

            <div className="space-y-2 text-sm">
              <div className="flex justify-between">
                <span className="text-gray-500">Speakers:</span>
                <span className="font-medium">{lang.speakers}</span>
              </div>
              <div className="flex justify-between">
                <span className="text-gray-500">Region:</span>
                <span className="font-medium">{lang.region}</span>
              </div>
              <div className="flex justify-between">
                <span className="text-gray-500">Stories:</span>
                <span className="font-medium">{lang.stories}</span>
              </div>
              <div className="flex justify-between">
                <span className="text-gray-500">Contributors:</span>
                <span className="font-medium">{lang.contributors}</span>
              </div>
            </div>

            <button className="btn-outline w-full mt-4 text-sm">
              View Stories
            </button>
          </div>
        ))}
      </div>

      {/* CTA */}
      <div className="bg-earth-500 rounded-2xl p-8 text-white text-center">
        <h2 className="text-2xl font-display font-bold mb-2">Don't see your language?</h2>
        <p className="text-earth-100 mb-6">
          We're constantly adding new languages. Help us prioritize by requesting yours.
        </p>
        <button className="bg-white text-earth-600 px-6 py-3 rounded-lg font-semibold hover:bg-earth-50 transition">
          Request Language
        </button>
      </div>
    </div>
  )
}

export default Languages
