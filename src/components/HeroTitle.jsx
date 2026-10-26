function Words({ text, start = 0 }) {
  return text.split(' ').map((w, i) => (
    <span key={`${w}-${i}`} className="hero-word">
      <span style={{ '--i': start + i }}>{w}</span>
    </span>
  ))
}

export default function HeroTitle() {
  return (
    <h1 className="hero-title">
      <Words text="Your Vision. Our Code." />
      <span className="grad">
        <Words text="Limitless Possibilities." start={4} />
      </span>
    </h1>
  )
}
