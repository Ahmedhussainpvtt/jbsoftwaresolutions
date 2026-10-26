import useMotionTier from '../hooks/useMotionTier'

const ALL = Array.from({ length: 18 }, (_, i) => ({
  id: i,
  left: `${(i * 17 + 7) % 94}%`,
  top: `${(i * 23 + 11) % 88}%`,
  size: 3 + (i % 5),
  dur: 4.5 + (i % 7) * 0.7,
  delay: (i % 9) * 0.35,
  rise: -28 - (i % 5) * 4,
}))

export default function FloatingBits() {
  const tier = useMotionTier()
  if (tier === 'off') return null

  const bits = tier === 'full' ? ALL : ALL.slice(0, 6)

  return (
    <div className="floating-bits" aria-hidden="true">
      {bits.map((b) => (
        <span
          key={b.id}
          className="floating-bit"
          style={{
            left: b.left,
            top: b.top,
            width: b.size,
            height: b.size,
            '--fb-dur': `${b.dur * (tier === 'lite' ? 1.35 : 1)}s`,
            '--fb-delay': `${b.delay}s`,
            '--fb-rise': `${b.rise}px`,
          }}
        />
      ))}
    </div>
  )
}
