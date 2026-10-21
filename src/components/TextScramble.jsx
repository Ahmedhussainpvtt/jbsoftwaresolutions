import { useEffect, useRef, useState } from 'react'
import { useInView, useReducedMotion } from 'framer-motion'

const GLYPHS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#$%&*'

export default function TextScramble({ text, className = '', as: Tag = 'span', trigger = true }) {
  const reduce = useReducedMotion()
  const ref = useRef(null)
  const inView = useInView(ref, { once: true, amount: 0.7 })
  const [out, setOut] = useState(reduce || !trigger ? text : '')

  useEffect(() => {
    if (reduce || !trigger || !inView) {
      if (reduce) setOut(text)
      return
    }
    let frame = 0
    const total = Math.max(18, text.length * 2)
    let id
    const run = () => {
      frame += 1
      const progress = frame / total
      setOut(
        text
          .split('')
          .map((ch, i) => {
            if (ch === ' ' || ch === '.' || ch === ',') return ch
            if (i / text.length < progress) return text[i]
            return GLYPHS[(Math.random() * GLYPHS.length) | 0]
          })
          .join(''),
      )
      if (frame < total) id = requestAnimationFrame(run)
      else setOut(text)
    }
    id = requestAnimationFrame(run)
    return () => cancelAnimationFrame(id)
  }, [inView, text, reduce, trigger])

  return (
    <Tag ref={ref} className={className}>
      {out || text}
    </Tag>
  )
}
