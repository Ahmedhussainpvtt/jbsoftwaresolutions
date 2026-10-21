import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter } from 'react-router-dom'
import { HelmetProvider } from 'react-helmet-async'
import App from './App.jsx'

const rawBase = import.meta.env.BASE_URL || '/'
const basename = rawBase.replace(/\/$/, '') || undefined

// GitHub Pages often serves the project root without a trailing slash.
// React Router then fails to match path="/". Normalize before mount.
if (basename && window.location.pathname === basename) {
  window.history.replaceState(null, '', `${basename}/`)
}

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <HelmetProvider>
      <BrowserRouter basename={basename}>
        <App />
      </BrowserRouter>
    </HelmetProvider>
  </StrictMode>,
)
