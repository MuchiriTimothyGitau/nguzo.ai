import { Routes, Route } from 'react-router-dom'
import Layout from './components/Layout'
import Home from './pages/Home'
import Record from './pages/Record'
import Stories from './pages/Stories'
import Languages from './pages/Languages'
import About from './pages/About'

function App() {
  return (
    <Layout>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/record" element={<Record />} />
        <Route path="/stories" element={<Stories />} />
        <Route path="/languages" element={<Languages />} />
        <Route path="/about" element={<About />} />
      </Routes>
    </Layout>
  )
}

export default App
