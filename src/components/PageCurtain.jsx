import { useEffect, useState } from 'react'
import { useLocation } from 'react-router-dom'
import { AnimatePresence, motion } from 'framer-motion'
import useMotionTier from '../hooks/useMotionTier'

/** Full-bleed route wipe on desktop only. Mobile gets a quick fade flash. */
export default function PageCurtain() {
  const { pathname } = useLocation()
  const tier = useMotionTier()
  const [burst, setBurst] = useState(null)
  const first = useState(() => ({ current: true }))[0]

  useEffect(() => {
    if (tier === 'off') return
    if (first.current) {
      first.current = false
      return
    }
    const id = pathname + String(Date.now())
    setBurst(id)
    const ms = tier === 'full' ? 780 : 320
    const t = setTimeout(() => setBurst(null), ms)
    return () => clearTimeout(t)
  }, [pathname, tier, first])

  if (tier === 'off') return null

  const full = tier === 'full'

  return (
    <AnimatePresence>
      {burst && (
        <motion.div
          key={burst}
          className={`page-curtain${full ? '' : ' is-lite'}`}
          aria-hidden="true"
          initial={full ? { clipPath: 'inset(0 0 100% 0)' } : { opacity: 0 }}
          animate={
            full
              ? {
                  clipPath: ['inset(0 0 100% 0)', 'inset(0 0 0% 0)', 'inset(100% 0 0% 0)'],
                }
              : { opacity: [0, 0.55, 0] }
          }
          exit={{ opacity: 0 }}
          transition={
            full
              ? { duration: 0.72, times: [0, 0.42, 1], ease: [0.76, 0, 0.24, 1] }
              : { duration: 0.28, times: [0, 0.4, 1], ease: 'easeOut' }
          }
        >
          {full && (
            <>
              <span className="page-curtain-shine" />
              <span className="page-curtain-grid" />
              <span className="page-curtain-label">JB</span>
            </>
          )}
        </motion.div>
      )}
    </AnimatePresence>
  )
}
