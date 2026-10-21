import { useRef } from 'react'
import {
  motion,
  useMotionTemplate,
  useMotionValue,
  useSpring,
} from 'framer-motion'
import useMotionTier from '../hooks/useMotionTier'

export default function TiltCard({
  children,
  className = '',
  max = 10,
  glare = true,
  as: Tag = motion.div,
  ...rest
}) {
  const tier = useMotionTier()
  const fancy = tier === 'full'
  const ref = useRef(null)
  const rx = useMotionValue(0)
  const ry = useMotionValue(0)
  const gx = useMotionValue(50)
  const gy = useMotionValue(50)
  const srx = useSpring(rx, { stiffness: 220, damping: 22 })
  const sry = useSpring(ry, { stiffness: 220, damping: 22 })
  const glareBg = useMotionTemplate`radial-gradient(420px circle at ${gx}% ${gy}%, rgba(61,255,122,0.22), transparent 55%)`

  const onMove = (e) => {
    if (!fancy || !ref.current) return
    const r = ref.current.getBoundingClientRect()
    const px = (e.clientX - r.left) / r.width
    const py = (e.clientY - r.top) / r.height
    ry.set((px - 0.5) * max * 2)
    rx.set((0.5 - py) * max * 2)
    gx.set(px * 100)
    gy.set(py * 100)
  }

  const onLeave = () => {
    rx.set(0)
    ry.set(0)
  }

  const { style: restStyle, ...restProps } = rest

  return (
    <Tag
      ref={ref}
      className={`tilt-card ${className}`.trim()}
      onPointerMove={fancy ? onMove : undefined}
      onPointerLeave={fancy ? onLeave : undefined}
      style={{
        rotateX: fancy ? srx : 0,
        rotateY: fancy ? sry : 0,
        transformStyle: fancy ? 'preserve-3d' : undefined,
        transformPerspective: fancy ? 1000 : undefined,
        ...restStyle,
      }}
      {...restProps}
    >
      {children}
      {glare && fancy && (
        <motion.span className="tilt-glare" style={{ background: glareBg }} aria-hidden="true" />
      )}
    </Tag>
  )
}
