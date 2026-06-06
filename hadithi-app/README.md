# Hadithi App

A Progressive Web App (PWA) for preserving and sharing African oral traditions.

## Features

- **Record Stories**: Audio recording interface with metadata
- **Browse Stories**: Search, filter, and listen to oral traditions
- **Language Support**: 15+ African languages with visual indicators
- **Mobile-First**: Responsive design with mobile navigation
- **PWA**: Installable app that works offline
- **Ethical Framework**: Built-in consent and community governance

## Tech Stack

- React 18 + TypeScript
- Vite (fast build tool)
- Tailwind CSS (styling)
- React Router (navigation)
- Lucide React (icons)
- Vite PWA Plugin (PWA capabilities)

## Getting Started

### Prerequisites

- Node.js 18+ 
- npm or yarn

### Installation

```bash
# Navigate to app directory
cd hadithi-app

# Install dependencies
npm install

# Start development server
npm run dev
```

The app will open at `http://localhost:3000`

### Build for Production

```bash
npm run build
```

Output will be in `dist/` directory.

## Project Structure

```
hadithi-app/
├── src/
│   ├── components/
│   │   └── Layout.tsx          # Main layout with navigation
│   ├── pages/
│   │   ├── Home.tsx            # Landing page with stats
│   │   ├── Record.tsx          # Audio recording interface
│   │   ├── Stories.tsx         # Story browser with filters
│   │   ├── Languages.tsx       # Language directory
│   │   └── About.tsx           # About page
│   ├── App.tsx                 # Main app with routes
│   ├── main.tsx                # Entry point
│   └── index.css               # Global styles
├── index.html                  # HTML template
├── vite.config.ts              # Vite configuration
├── tailwind.config.js          # Tailwind customization
└── package.json                # Dependencies
```

## Pages

### Home (`/`)
- Hero section with CTA
- Animated statistics
- Featured stories carousel
- Language showcase
- Call-to-action for contributors

### Record (`/record`)
- Audio recording interface using Web Audio API
- Timer display
- Audio preview with playback
- Metadata form (title, language, category)
- Consent checkbox
- Recording tips

### Stories (`/stories`)
- Search functionality
- Filter by language and category
- Story cards with metadata
- Audio player interface (simulated)
- Empty state with clear filters

### Languages (`/languages`)
- Grid of supported languages
- Speaker counts
- Story counts per language
- Contributor counts
- Status badges (Active/Growing/Beta)
- Request new language CTA

### About (`/about`)
- Mission statement
- Feature highlights
- How it works (4-step process)
- Partner logos
- Contact information

## Design System

### Colors
- **Primary**: Earth brown (#8B4513)
- **Secondary**: Sunrise gold (#FFD700)
- **Accent**: Forest green (#228B22)
- **Background**: Light gray (#F9FAFB)

### Typography
- **Display**: Poppins (headings)
- **Body**: Inter (text)

### Components
- `btn-primary`: Earth background, white text
- `btn-secondary`: Sunrise background, dark text
- `btn-outline`: Bordered buttons
- `card`: White card with shadow
- `input-field`: Styled form inputs
- `language-badge`: Language indicator pill

## Customization

### Adding a New Language

1. Update `languages` array in `src/pages/Languages.tsx`
2. Add to filter options in `src/pages/Stories.tsx`
3. Update recording options in `src/pages/Record.tsx`

### Adding Stories

Stories are currently hardcoded in `src/pages/Stories.tsx`. Connect to a backend API by:

1. Replacing the `stories` array with API calls
2. Implementing authentication if needed
3. Adding loading states

## PWA Features

The app is configured as a PWA with:
- Web App Manifest
- Service Worker for offline caching
- Icons for different devices
- Theme color support

Users can "Add to Home Screen" on mobile devices.

## Browser Support

- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Development Notes

### Audio Recording
Uses native Web Audio API and MediaRecorder. Requires HTTPS in production for microphone access.

### Routing
Client-side routing with React Router. Works with GitHub Pages or Netlify with proper redirects.

### Styling
Tailwind CSS with custom configuration:
- Custom colors (earth, sunrise, forest)
- Custom fonts (Poppins, Inter)
- Custom animations (fade-in, slide-up)

## Deployment

### Netlify
1. Connect GitHub repo
2. Build command: `npm run build`
3. Publish directory: `dist`
4. Add `_redirects` file for SPA routing

### Vercel
1. Import GitHub repo
2. Framework preset: Vite
3. Build command: `npm run build`
4. Output directory: `dist`

### GitHub Pages
Update `vite.config.ts` with `base: '/your-repo-name/'`

## Next Steps

1. Connect to backend API for data persistence
2. Implement actual audio upload
3. Add user authentication
4. Create user profiles
5. Add story transcription interface
6. Implement search with backend
7. Add offline audio caching

## License

MIT License - See parent project for details.

---

Built with ❤️ for African communities.
