import { useEffect, useState } from 'react'
import { useReducedMotion } from 'framer-motion'

/**
 * off  = reduced motion
 * lite = phones / touch (keeps scroll reveals, drops heavy GPU loops)
 * full = fine pointer + wide viewport
 */
export default function useMotionTier() {
  const reduce = useReducedMotion()
  const [tier, setTier] = useState(() => (reduce ? 'off' : 'lite'))

  useEffect(() => {
    const sync = () => {
      if (reduce || window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
        setTier('off')
        return
      }
      const fine = window.matchMedia('(hover: hover) and (pointer: fine)').matches
      const wide = window.matchMedia('(min-width: 900px)').matches
      setTier(fine && wide ? 'full' : 'lite')
    }
    sync()
    const qs = [
      window.matchMedia('(hover: hover) and (pointer: fine)'),
      window.matchMedia('(min-width: 900px)'),
      window.matchMedia('(prefers-reduced-motion: reduce)'),
    ]
    qs.forEach((q) => q.addEventListener('change', sync))
    return () => qs.forEach((q) => q.removeEventListener('change', sync))
  }, [reduce])

  return tier
}
