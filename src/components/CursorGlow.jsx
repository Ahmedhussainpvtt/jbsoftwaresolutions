import { useEffect } from 'react'
import { motion, useMotionValue, useSpring, useReducedMotion } from 'framer-motion'

export default function CursorGlow() {
  const reduce = useReducedMotion()
  const x = useMotionValue(-200)
  const y = useMotionValue(-200)
  const sx = useSpring(x, { stiffness: 140, damping: 22, mass: 0.4 })
  const sy = useSpring(y, { stiffness: 140, damping: 22, mass: 0.4 })

  useEffect(() => {
    if (reduce) return undefined
    const onMove = (e) => {
      x.set(e.clientX - 180)
      y.set(e.clientY - 180)
    }
    window.addEventListener('pointermove', onMove, { passive: true })
    return () => window.removeEventListener('pointermove', onMove)
  }, [reduce, x, y])

  if (reduce) return null

  return (
    <motion.div
      className="cursor-glow"
      aria-hidden="true"
      style={{ x: sx, y: sy }}
    />
  )
}
