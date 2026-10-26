import useMotionTier from '../hooks/useMotionTier'

export default function ScrollMarquee({ items }) {
  const tier = useMotionTier()
  const doubled = [...items, ...items]
  if (tier === 'off') {
    return (
      <div className="marquee" aria-hidden="true">
        <div className="marquee-track" style={{ display: 'flex', gap: '2.5rem' }}>
          {items.map((t) => (
            <span key={t}>{t}</span>
          ))}
        </div>
      </div>
    )
  }

  return (
    <div className="scroll-marquees" aria-hidden="true">
      <div className="marquee marquee-scroll">
        <div
          className="marquee-track"
          style={{ display: 'flex', width: 'max-content', gap: '2.5rem', animationDuration: tier === 'lite' ? '40s' : '28s' }}
        >
          {doubled.map((t, i) => (
            <span key={`a-${t}-${i}`}>{t}</span>
          ))}
        </div>
      </div>
      {tier === 'full' && (
        <div className="marquee marquee-scroll marquee-reverse">
          <div
            className="marquee-track"
            style={{ display: 'flex', width: 'max-content', gap: '2.5rem', animationDuration: '38s', animationDirection: 'reverse' }}
          >
            {doubled.map((t, i) => (
              <span key={`b-${t}-${i}`}>{t}</span>
            ))}
          </div>
        </div>
      )}
    </div>
  )
}
