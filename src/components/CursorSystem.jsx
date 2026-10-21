import { useEffect, useRef } from 'react'

const TAIL_N = 10
const SPARK_COLORS = ['#3dff7a', '#3ad0ff', '#ffe566', '#ff9a1f']
const HOT_SEL =
  'a, button, .btn, .dock-btn, summary, .blog-card, .seo-chip, .nav-links a, .bento-tile, .work-card, .price-card, .service-chip, .magnetic'

function closestHot(t) {
  return t?.closest?.(HOT_SEL)
}

function isFormField(t) {
  return t?.closest?.('input, textarea, select, [contenteditable="true"]')
}

export default function CursorSystem() {
  const wrapRef = useRef(null)

  useEffect(() => {
    const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches
    const fine = window.matchMedia('(hover: hover) and (pointer: fine)').matches
    if (reduced || !fine) return undefined

    const wrap = wrapRef.current
    if (!wrap) return undefined

    document.documentElement.classList.add('has-cursor')

    const ring = wrap.querySelector('.cursor-ring')
    const core = wrap.querySelector('.cursor-core')
    const tailEls = [...wrap.querySelectorAll('.cursor-tail')]
    const sparks = [...wrap.querySelectorAll('.cursor-pixel')]

    const tails = tailEls.map((el) => ({
      el,
      x: window.innerWidth / 2,
      y: window.innerHeight / 2,
    }))

    let mx = window.innerWidth / 2
    let my = window.innerHeight / 2
    let rx = mx
    let ry = my
    let cx = mx
    let cy = my
    let lastSpark = 0
    let sparkI = 0
    let lastX = mx
    let lastY = my
    let visible = false
    let raf = 0
    let alive = true
    let hotDepth = 0

    const loop = () => {
      if (!alive) return
      cx += (mx - cx) * 0.42
      cy += (my - cy) * 0.42
      rx += (mx - rx) * 0.18
      ry += (my - ry) * 0.18
      core.style.transform = `translate3d(${cx}px, ${cy}px, 0)`
      ring.style.transform = `translate3d(${rx}px, ${ry}px, 0)`

      let px = rx
      let py = ry
      tails.forEach((node, i) => {
        const ease = 0.28 - i * 0.018
        node.x += (px - node.x) * ease
        node.y += (py - node.y) * ease
        node.el.style.transform = `translate3d(${node.x}px, ${node.y}px, 0)`
        px = node.x
        py = node.y
      })

      if (visible) {
        ring.style.opacity = '1'
        core.style.opacity = '1'
      }
      raf = requestAnimationFrame(loop)
    }
    raf = requestAnimationFrame(loop)

    const setHot = (on) => {
      wrap.classList.toggle('is-hot', on)
      ring.classList.toggle('is-hot', on)
    }

    const onMove = (e) => {
      mx = e.clientX
      my = e.clientY
      visible = true

      const dist = Math.hypot(mx - lastX, my - lastY)
      const now = performance.now()
      if (dist > 28 && now - lastSpark > 28) {
        lastSpark = now
        lastX = mx
        lastY = my
        const spark = sparks[sparkI % sparks.length]
        sparkI += 1
        spark.style.transition = 'none'
        spark.style.transform = `translate3d(${mx}px, ${my}px, 0) scale(1)`
        spark.style.opacity = '0.85'
        requestAnimationFrame(() => {
          spark.style.transition = 'opacity 0.55s ease, transform 0.55s ease'
          spark.style.opacity = '0'
          spark.style.transform = `translate3d(${mx}px, ${my}px, 0) scale(0.2)`
        })
      }
    }

    const onLeave = () => {
      visible = false
      ring.style.opacity = '0'
      core.style.opacity = '0'
      tails.forEach((n) => {
        n.el.style.opacity = '0'
      })
    }

    const onEnter = () => {
      visible = true
      tails.forEach((n) => {
        n.el.style.opacity = ''
      })
    }

    const onOver = (e) => {
      if (isFormField(e.target)) {
        document.documentElement.classList.add('cursor-form')
      }
      if (closestHot(e.target)) {
        hotDepth += 1
        setHot(true)
      }
    }

    const onOut = (e) => {
      if (isFormField(e.target) && !isFormField(e.relatedTarget)) {
        document.documentElement.classList.remove('cursor-form')
      }
      if (closestHot(e.target) && !closestHot(e.relatedTarget)) {
        hotDepth = Math.max(0, hotDepth - 1)
        if (hotDepth === 0) setHot(false)
      }
    }

    window.addEventListener('pointermove', onMove, { passive: true })
    window.addEventListener('pointerleave', onLeave)
    window.addEventListener('pointerenter', onEnter)
    document.addEventListener('pointerover', onOver)
    document.addEventListener('pointerout', onOut)

    return () => {
      alive = false
      cancelAnimationFrame(raf)
      window.removeEventListener('pointermove', onMove)
      window.removeEventListener('pointerleave', onLeave)
      window.removeEventListener('pointerenter', onEnter)
      document.removeEventListener('pointerover', onOver)
      document.removeEventListener('pointerout', onOut)
      document.documentElement.classList.remove('has-cursor', 'cursor-form')
    }
  }, [])

  return (
    <div className="cursor-system" ref={wrapRef} aria-hidden="true">
      <div className="cursor-ring" />
      <div className="cursor-core" />
      {Array.from({ length: TAIL_N }, (_, i) => (
        <div key={i} className="cursor-tail" style={{ '--i': i }} />
      ))}
      {SPARK_COLORS.map((c) => (
        <div key={c} className="cursor-pixel" style={{ background: c }} />
      ))}
    </div>
  )
}
