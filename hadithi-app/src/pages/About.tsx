import { Heart, Users, Globe, BookOpen, Mic, Shield } from 'lucide-react'

const About = () => {
  return (
    <div className="space-y-8 animate-fade-in">
      {/* Hero */}
      <section className="text-center py-8">
        <h1 className="text-4xl font-display font-bold text-gray-900 mb-4">
          About Hadithi
        </h1>
        <p className="text-xl text-gray-600 max-w-2xl mx-auto">
          Preserving African oral traditions through community-driven AI and ethical storytelling.
        </p>
      </section>

      {/* Mission */}
      <section className="bg-earth-500 rounded-2xl p-8 text-white">
        <h2 className="text-2xl font-display font-bold mb-4">Our Mission</h2>
        <p className="text-lg text-earth-100 leading-relaxed">
          Hadithi (Swahili for "story") is dedicated to preserving and celebrating African oral 
          traditions. We believe every language, every story, and every voice matters. By combining 
          community-driven data collection with cutting-edge AI, we're building technology that 
          understands and respects African languages — not retrofitting English models, but creating 
          AI from the ground up for African tongues.
        </p>
      </section>

      {/* Features Grid */}
      <section className="grid md:grid-cols-3 gap-6">
        {[
          {
            icon: Mic,
            title: "Record & Share",
            description: "Easily record oral traditions in your language and share them with the world."
          },
          {
            icon: Globe,
            title: "15+ Languages",
            description: "Supporting Swahili, Luganda, Kinyarwanda, Kikuyu, Dholuo, Yoruba, and more."
          },
          {
            icon: Shield,
            title: "Ethical AI",
            description: "Community data sovereignty with transparent consent and benefit-sharing."
          },
          {
            icon: BookOpen,
            title: "Cultural Preservation",
            description: "Protecting endangered languages and oral traditions for future generations."
          },
          {
            icon: Users,
            title: "Community First",
            description: "Built with communities, not for them. Community boards govern data use."
          },
          {
            icon: Heart,
            title: "Free Forever",
            description: "Open source and free for communities. No paywalls for cultural heritage."
          }
        ].map((feature, index) => (
          <div key={index} className="card">
            <feature.icon className="w-10 h-10 text-earth-500 mb-4" />
            <h3 className="font-semibold text-lg mb-2">{feature.title}</h3>
            <p className="text-gray-600 text-sm">{feature.description}</p>
          </div>
        ))}
      </section>

      {/* How It Works */}
      <section className="card">
        <h2 className="text-2xl font-display font-bold text-gray-900 mb-6">How It Works</h2>
        <div className="space-y-6">
          {[
            {
              step: 1,
              title: "Record",
              description: "Use your phone to record stories, songs, or oral histories in your language."
            },
            {
              step: 2,
              title: "Share",
              description: "Upload with metadata and consent information. Stories are reviewed for quality."
            },
            {
              step: 3,
              title: "Preserve",
              description: "Stories are archived and used to train AI models that understand your language."
            },
            {
              step: 4,
              title: "Empower",
              description: "AI tools help document, translate, and share your culture with the world."
            }
          ].map((item) => (
            <div key={item.step} className="flex items-start space-x-4">
              <div className="w-10 h-10 bg-earth-500 rounded-full flex items-center justify-center text-white font-bold shrink-0">
                {item.step}
              </div>
              <div>
                <h3 className="font-semibold text-lg">{item.title}</h3>
                <p className="text-gray-600">{item.description}</p>
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* Partners */}
      <section className="card text-center">
        <h2 className="text-xl font-semibold mb-4">Supported By</h2>
        <p className="text-gray-600 mb-6">
          Hadithi is part of the African Native Oral LLM project, working with communities, 
          researchers, and organizations across the continent.
        </p>
        <div className="flex flex-wrap justify-center gap-4 text-sm text-gray-500">
          <span className="px-4 py-2 bg-gray-100 rounded-full">Masakhane</span>
          <span className="px-4 py-2 bg-gray-100 rounded-full">LINGUA Africa</span>
          <span className="px-4 py-2 bg-gray-100 rounded-full">Community Partners</span>
        </div>
      </section>

      {/* Contact */}
      <section className="bg-forest-500 rounded-2xl p-8 text-white text-center">
        <h2 className="text-2xl font-display font-bold mb-4">Get Involved</h2>
        <p className="text-forest-100 mb-6">
          Want to contribute stories, add a language, or partner with us?
        </p>
        <div className="flex flex-wrap justify-center gap-4">
          <a 
            href="mailto:hello@hadithi.africa" 
            className="bg-white text-forest-700 px-6 py-3 rounded-lg font-semibold hover:bg-forest-50 transition"
          >
            Contact Us
          </a>
          <a 
            href="https://github.com/your-org/hadithi" 
            className="border-2 border-white text-white px-6 py-3 rounded-lg font-semibold hover:bg-white/10 transition"
          >
            GitHub
          </a>
        </div>
      </section>
    </div>
  )
}

export default About
