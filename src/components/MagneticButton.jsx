import { useRef } from 'react'
import { motion, useMotionValue, useSpring, useReducedMotion } from 'framer-motion'
import { Link } from 'react-router-dom'

const MotionLink = motion.create(Link)

export default function MagneticButton({
  to,
  href,
  children,
  className = 'btn btn-primary',
  strength = 0.42,
  type = 'button',
  style,
}) {
  const reduce = useReducedMotion()
  const ref = useRef(null)
  const x = useMotionValue(0)
  const y = useMotionValue(0)
  const sx = useSpring(x, { stiffness: 380, damping: 18, mass: 0.28 })
  const sy = useSpring(y, { stiffness: 380, damping: 18, mass: 0.28 })

  const onMove = (e) => {
    if (reduce || !ref.current) return
    const r = ref.current.getBoundingClientRect()
    x.set((e.clientX - (r.left + r.width / 2)) * strength)
    y.set((e.clientY - (r.top + r.height / 2)) * strength)
  }

  const onLeave = () => {
    x.set(0)
    y.set(0)
  }

  const shared = {
    ref,
    className,
    style: { x: sx, y: sy, display: 'inline-flex', ...style },
    onPointerMove: onMove,
    onPointerLeave: onLeave,
    whileHover: reduce
      ? undefined
      : {
          scale: 1.07,
          boxShadow: '0 12px 40px rgba(61, 255, 122, 0.35)',
        },
    whileTap: { scale: 0.94 },
  }

  if (to) {
    return (
      <MotionLink to={to} {...shared}>
        {children}
      </MotionLink>
    )
  }
  if (href) {
    return (
      <motion.a href={href} {...shared}>
        {children}
      </motion.a>
    )
  }
  return (
    <motion.button type={type} {...shared}>
      {children}
    </motion.button>
  )
}
