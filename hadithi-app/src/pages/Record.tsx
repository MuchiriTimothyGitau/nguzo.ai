import { useState, useRef } from 'react'
import { Mic, StopCircle, Play, Pause, Trash2, Save, Languages } from 'lucide-react'

const Record = () => {
  const [isRecording, setIsRecording] = useState(false)
  const [audioBlob, setAudioBlob] = useState<Blob | null>(null)
  const [recordingTime, setRecordingTime] = useState(0)
  const [language, setLanguage] = useState('')
  const [title, setTitle] = useState('')
  const [category, setCategory] = useState('')
  const mediaRecorderRef = useRef<MediaRecorder | null>(null)
  const chunksRef = useRef<Blob[]>([])

  const languages = [
    { code: 'swa', name: 'Swahili' },
    { code: 'lug', name: 'Luganda' },
    { code: 'kin', name: 'Kinyarwanda' },
    { code: 'kik', name: 'Kikuyu' },
    { code: 'luo', name: 'Dholuo' },
    { code: 'yor', name: 'Yoruba' }
  ]

  const categories = [
    'Folktale',
    'History',
    'Proverb',
    'Song',
    'Poetry',
    'Personal Story',
    'Cultural Practice'
  ]

  const startRecording = async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true })
      const mediaRecorder = new MediaRecorder(stream)
      mediaRecorderRef.current = mediaRecorder
      chunksRef.current = []

      mediaRecorder.ondataavailable = (e) => {
        if (e.data.size > 0) {
          chunksRef.current.push(e.data)
        }
      }

      mediaRecorder.onstop = () => {
        const blob = new Blob(chunksRef.current, { type: 'audio/webm' })
        setAudioBlob(blob)
      }

      mediaRecorder.start()
      setIsRecording(true)
      
      // Start timer
      const timer = setInterval(() => {
        setRecordingTime(prev => prev + 1)
      }, 1000)

      // Store timer to clear later
      ;(mediaRecorder as any).timer = timer
    } catch (err) {
      console.error('Error accessing microphone:', err)
      alert('Could not access microphone. Please check permissions.')
    }
  }

  const stopRecording = () => {
    if (mediaRecorderRef.current) {
      mediaRecorderRef.current.stop()
      mediaRecorderRef.current.stream.getTracks().forEach(track => track.stop())
      clearInterval((mediaRecorderRef.current as any).timer)
      setIsRecording(false)
    }
  }

  const formatTime = (seconds: number) => {
    const mins = Math.floor(seconds / 60)
    const secs = seconds % 60
    return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`
  }

  const handleSave = () => {
    if (!audioBlob || !title || !language) {
      alert('Please fill in all required fields and record audio')
      return
    }
    // TODO: Upload to server
    console.log('Saving story:', { title, language, category, audioBlob })
    alert('Story saved! (Demo mode - not actually uploaded)')
    
    // Reset
    setAudioBlob(null)
    setTitle('')
    setLanguage('')
    setCategory('')
    setRecordingTime(0)
  }

  return (
    <div className="max-w-2xl mx-auto space-y-6 animate-fade-in">
      <div className="text-center mb-8">
        <h1 className="text-3xl font-display font-bold text-gray-900 mb-2">Record a Story</h1>
        <p className="text-gray-600">Share your oral traditions with the world</p>
      </div>

      {/* Recording Interface */}
      <div className="card">
        <div className="flex flex-col items-center space-y-6">
          {/* Recording Button */}
          <div className="relative">
            {isRecording && (
              <div className="absolute inset-0 bg-red-500 rounded-full animate-ping opacity-20" />
            )}
            <button
              onClick={isRecording ? stopRecording : startRecording}
              className={`w-24 h-24 rounded-full flex items-center justify-center transition-all ${
                isRecording
                  ? 'bg-red-500 hover:bg-red-600 shadow-lg shadow-red-500/30'
                  : 'bg-earth-500 hover:bg-earth-600 shadow-lg shadow-earth-500/30'
              }`}
            >
              {isRecording ? (
                <StopCircle className="w-10 h-10 text-white" />
              ) : (
                <Mic className="w-10 h-10 text-white" />
              )}
            </button>
          </div>

          {/* Timer */}
          <div className="text-center">
            <p className={`text-4xl font-mono font-bold ${isRecording ? 'text-red-500' : 'text-gray-400'}`}>
              {formatTime(recordingTime)}
            </p>
            <p className="text-sm text-gray-500 mt-1">
              {isRecording ? 'Recording...' : audioBlob ? 'Recording complete' : 'Tap to start'}
            </p>
          </div>

          {/* Audio Preview */}
          {audioBlob && (
            <div className="w-full bg-gray-100 rounded-lg p-4">
              <audio controls className="w-full">
                <source src={URL.createObjectURL(audioBlob)} type="audio/webm" />
              </audio>
              <button
                onClick={() => {
                  setAudioBlob(null)
                  setRecordingTime(0)
                }}
                className="mt-2 text-red-500 text-sm flex items-center space-x-1 hover:text-red-600"
              >
                <Trash2 className="w-4 h-4" />
                <span>Delete and re-record</span>
              </button>
            </div>
          )}
        </div>
      </div>

      {/* Story Details Form */}
      <div className="card space-y-4">
        <h2 className="text-xl font-semibold text-gray-900">Story Details</h2>
        
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">
            Title *
          </label>
          <input
            type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            placeholder="e.g., The Wise Tortoise"
            className="input-field"
          />
        </div>

        <div className="grid md:grid-cols-2 gap-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              <Languages className="w-4 h-4 inline mr-1" />
              Language *
            </label>
            <select
              value={language}
              onChange={(e) => setLanguage(e.target.value)}
              className="input-field"
            >
              <option value="">Select language</option>
              {languages.map((lang) => (
                <option key={lang.code} value={lang.code}>
                  {lang.name}
                </option>
              ))}
            </select>
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Category
            </label>
            <select
              value={category}
              onChange={(e) => setCategory(e.target.value)}
              className="input-field"
            >
              <option value="">Select category</option>
              {categories.map((cat) => (
                <option key={cat} value={cat}>
                  {cat}
                </option>
              ))}
            </select>
          </div>
        </div>

        {/* Consent Checkbox */}
        <div className="bg-forest-50 border border-forest-200 rounded-lg p-4">
          <label className="flex items-start space-x-3">
            <input type="checkbox" className="mt-1 w-4 h-4 text-forest-500 rounded" />
            <span className="text-sm text-gray-700">
              I confirm that I have the right to share this story, and I consent to it being 
              used for AI training and cultural preservation purposes. I understand I can 
              request deletion at any time.
            </span>
          </label>
        </div>

        <button
          onClick={handleSave}
          disabled={!audioBlob || !title || !language}
          className="btn-primary w-full flex items-center justify-center space-x-2 disabled:opacity-50"
        >
          <Save className="w-5 h-5" />
          <span>Save Story</span>
        </button>
      </div>

      {/* Tips */}
      <div className="bg-sunrise-50 border border-sunrise-200 rounded-xl p-4">
        <h3 className="font-semibold text-earth-900 mb-2">Recording Tips</h3>
        <ul className="text-sm text-gray-700 space-y-1 list-disc list-inside">
          <li>Find a quiet space with minimal background noise</li>
          <li>Speak clearly and at a moderate pace</li>
          <li>Keep your phone about 6 inches from your mouth</li>
          <li>Pause between sentences for better audio quality</li>
          <li>Stories can be 1-30 minutes long</li>
        </ul>
      </div>
    </div>
  )
}

export default Record
