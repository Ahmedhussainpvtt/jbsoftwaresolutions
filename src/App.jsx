import { Routes, Route, useLocation, Navigate, useParams } from 'react-router-dom'
import { motion } from 'framer-motion'
import Header from './components/Header'
import Footer from './components/Footer'
import Dock from './components/Dock'
import CursorSystem from './components/CursorSystem'
import ScrollProgress from './components/ScrollProgress'
import ScrollToTop from './components/ScrollToTop'
import PageCurtain from './components/PageCurtain'
import Aurora from './components/Aurora'
import Home from './pages/Home'
import ServicePage from './pages/ServicePage'
import {
  About,
  Pricing,
  Contact,
  BlogHub,
  Privacy,
  Terms,
  NotFound,
} from './pages/SimplePage'
import { FaqHub, FaqTopic } from './pages/FaqPages'
import { GlossaryHub, GlossaryTerm } from './pages/GlossaryPages'
import { getService } from './data/services'
import { pageVariants } from './motion'
import './styles.css'
import './motion-extras.css'

function ServiceRoute() {
  const { slug } = useParams()
  const clean = (slug || '').replace(/\/$/, '')
  if (!getService(clean)) return <Navigate to="/" replace />
  return <ServicePage slug={clean} />
}

export default function App() {
  const location = useLocation()

  return (
    <>
      <ScrollToTop />
      <ScrollProgress />
      <CursorSystem />
      <Aurora />
      <PageCurtain />
      <Header />
      <motion.main
        key={location.pathname}
        variants={pageVariants}
        initial="initial"
        animate="animate"
      >
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="about" element={<About />} />
          <Route path="about/" element={<About />} />
          <Route path="pricing" element={<Pricing />} />
          <Route path="pricing/" element={<Pricing />} />
          <Route path="contact" element={<Contact />} />
          <Route path="contact/" element={<Contact />} />
          <Route path="faq" element={<FaqHub />} />
          <Route path="faq/" element={<FaqHub />} />
          <Route path="faq/:slug" element={<FaqTopic />} />
          <Route path="faq/:slug/" element={<FaqTopic />} />
          <Route path="blog" element={<BlogHub />} />
          <Route path="blog/" element={<BlogHub />} />
          <Route path="glossary" element={<GlossaryHub />} />
          <Route path="glossary/" element={<GlossaryHub />} />
          <Route path="glossary/:slug" element={<GlossaryTerm />} />
          <Route path="glossary/:slug/" element={<GlossaryTerm />} />
          <Route path="privacy" element={<Privacy />} />
          <Route path="privacy/" element={<Privacy />} />
          <Route path="terms" element={<Terms />} />
          <Route path="terms/" element={<Terms />} />
          <Route path="services/:slug" element={<ServiceRoute />} />
          <Route path="services/:slug/" element={<ServiceRoute />} />
          <Route path="*" element={<NotFound />} />
        </Routes>
      </motion.main>
      <Footer />
      <Dock />
    </>
  )
}
