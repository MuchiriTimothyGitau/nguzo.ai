import { useState } from 'react'
import { Link, useLocation } from 'react-router-dom'
import { Mic, BookOpen, Globe, Info, Menu, X, Home } from 'lucide-react'

interface LayoutProps {
  children: React.ReactNode
}

function Layout({ children }: LayoutProps) {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false)
  const location = useLocation()

  const navItems = [
    { path: '/', label: 'Home', icon: Home },
    { path: '/record', label: 'Record', icon: Mic },
    { path: '/stories', label: 'Stories', icon: BookOpen },
    { path: '/languages', label: 'Languages', icon: Globe },
    { path: '/about', label: 'About', icon: Info },
  ]

  const isActive = (path: string) => location.pathname === path

  return (
    <div className="min-h-screen flex flex-col bg-gray-50">
      {/* Header */}
      <header className="bg-earth-500 text-white shadow-lg sticky top-0 z-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between h-16">
            {/* Logo */}
            <Link to="/" className="flex items-center space-x-2 hover:opacity-90 transition">
              <div className="w-10 h-10 bg-sunrise-500 rounded-full flex items-center justify-center">
                <span className="text-earth-900 font-bold text-lg">H</span>
              </div>
              <div className="hidden sm:block">
                <h1 className="text-xl font-display font-bold">Hadithi</h1>
                <p className="text-xs text-earth-100">African Oral Traditions</p>
              </div>
            </Link>

            {/* Desktop Nav */}
            <nav className="hidden md:flex items-center space-x-1">
              {navItems.map((item) => (
                <Link
                  key={item.path}
                  to={item.path}
                  className={`flex items-center space-x-1 px-4 py-2 rounded-lg transition-all ${
                    isActive(item.path)
                      ? 'bg-earth-600 text-white'
                      : 'text-earth-100 hover:bg-earth-600 hover:text-white'
                  }`}
                >
                  <item.icon className="w-4 h-4" />
                  <span className="text-sm font-medium">{item.label}</span>
                </Link>
              ))}
            </nav>

            {/* Mobile Menu Button */}
            <button
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
              className="md:hidden p-2 rounded-lg hover:bg-earth-600 transition"
              aria-label="Toggle menu"
            >
              {mobileMenuOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
            </button>
          </div>
        </div>

        {/* Mobile Nav */}
        {mobileMenuOpen && (
          <div className="md:hidden bg-earth-600 border-t border-earth-700">
            <div className="px-4 py-2 space-y-1">
              {navItems.map((item) => (
                <Link
                  key={item.path}
                  to={item.path}
                  onClick={() => setMobileMenuOpen(false)}
                  className={`flex items-center space-x-3 px-4 py-3 rounded-lg transition-all ${
                    isActive(item.path)
                      ? 'bg-earth-500 text-white'
                      : 'text-earth-100 hover:bg-earth-500'
                  }`}
                >
                  <item.icon className="w-5 h-5" />
                  <span className="font-medium">{item.label}</span>
                </Link>
              ))}
            </div>
          </div>
        )}
      </header>

      {/* Main Content */}
      <main className="flex-1 max-w-7xl mx-auto w-full px-4 sm:px-6 lg:px-8 py-6">
        {children}
      </main>

      {/* Bottom Mobile Nav (Dock) */}
      <nav className="md:hidden fixed bottom-0 left-0 right-0 bg-white border-t border-gray-200 safe-area-inset-bottom z-50">
        <div className="flex justify-around items-center py-2">
          {navItems.map((item) => (
            <Link
              key={item.path}
              to={item.path}
              className={`flex flex-col items-center space-y-1 px-3 py-2 rounded-lg transition-all ${
                isActive(item.path)
                  ? 'text-earth-500'
                  : 'text-gray-400 hover:text-earth-400'
              }`}
            >
              <item.icon className="w-6 h-6" />
              <span className="text-xs font-medium">{item.label}</span>
            </Link>
          ))}
        </div>
      </nav>

      {/* Spacer for mobile bottom nav */}
      <div className="md:hidden h-20" />

      {/* Footer */}
      <footer className="bg-earth-800 text-earth-100 py-8 hidden md:block">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div>
              <h3 className="text-lg font-display font-semibold text-white mb-4">Hadithi</h3>
              <p className="text-sm text-earth-300">
                Preserving African oral traditions through community-driven AI.
              </p>
            </div>
            <div>
              <h4 className="font-semibold text-white mb-4">Quick Links</h4>
              <ul className="space-y-2 text-sm">
                <li><Link to="/record" className="hover:text-white transition">Record Story</Link></li>
                <li><Link to="/stories" className="hover:text-white transition">Browse Stories</Link></li>
                <li><Link to="/languages" className="hover:text-white transition">Languages</Link></li>
              </ul>
            </div>
            <div>
              <h4 className="font-semibold text-white mb-4">Connect</h4>
              <p className="text-sm text-earth-300">
                Built with ❤️ for African communities.
              </p>
            </div>
          </div>
          <div className="mt-8 pt-8 border-t border-earth-700 text-center text-sm text-earth-400">
            © 2026 Hadithi - African Native Oral LLM Project
          </div>
        </div>
      </footer>
    </div>
  )
}

export default Layout
