(() => {
  const reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const finePointer = window.matchMedia("(hover: hover) and (pointer: fine)").matches;

  const loadScript = (src) =>
    new Promise((resolve, reject) => {
      if ([...document.scripts].some((s) => s.src.includes(src.split("/").pop()))) {
        resolve();
        return;
      }
      const el = document.createElement("script");
      el.src = src;
      el.onload = resolve;
      el.onerror = reject;
      document.head.appendChild(el);
    });

  async function boot() {
    try {
      await loadScript("https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js");
      await loadScript("https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/ScrollTrigger.min.js");
      if (window.gsap && window.ScrollTrigger) window.gsap.registerPlugin(window.ScrollTrigger);
    } catch (_) {
      /* CSS fallbacks still work */
    }

    initNav();
    initAiField();
    initTerminal();
    initMarquee();
    initMagnet();
    if (!reduced) {
      initReveal();
      initCounters();
      initHero();
      if (finePointer) initCursorTrail();
    } else {
      document.querySelectorAll(".reveal").forEach((el) => {
        el.style.opacity = "1";
        el.style.transform = "none";
      });
    }
  }

  function initNav() {
    const toggle = document.querySelector(".nav-toggle");
    const links = document.querySelector(".nav-links");
    if (!toggle || !links) return;
    toggle.addEventListener("click", () => {
      const open = links.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    links.querySelectorAll("a").forEach((a) =>
      a.addEventListener("click", () => {
        links.classList.remove("is-open");
        toggle.setAttribute("aria-expanded", "false");
      })
    );
  }

  function initHero() {
    if (!window.gsap) return;
    const tl = gsap.timeline({ defaults: { ease: "power3.out" } });
    tl.from(".hero-brand", { y: 30, autoAlpha: 0, duration: 0.8 })
      .from(".hero-title", { y: 40, autoAlpha: 0, duration: 0.9 }, "-=0.45")
      .from(".hero-sub", { y: 24, autoAlpha: 0, duration: 0.7 }, "-=0.5")
      .from(".hero-cta .btn", { y: 18, autoAlpha: 0, stagger: 0.1, duration: 0.55 }, "-=0.4")
      .from(".ai-proof", { y: 28, autoAlpha: 0, duration: 0.8 }, "-=0.35");
  }

  function initReveal() {
    if (!window.gsap || !window.ScrollTrigger) {
      document.querySelectorAll(".reveal").forEach((el) => {
        el.style.opacity = "1";
        el.style.transform = "none";
      });
      return;
    }
    gsap.utils.toArray(".reveal").forEach((el) => {
      gsap.to(el, {
        autoAlpha: 1,
        y: 0,
        duration: 0.85,
        ease: "power3.out",
        scrollTrigger: { trigger: el, start: "top 88%" },
      });
    });
    gsap.utils.toArray(".service-band").forEach((el, i) => {
      gsap.from(el, {
        x: i % 2 ? 40 : -40,
        autoAlpha: 0,
        duration: 0.9,
        ease: "power3.out",
        scrollTrigger: { trigger: el, start: "top 85%" },
      });
    });
  }

  function initCounters() {
    if (!window.gsap || !window.ScrollTrigger) return;
    document.querySelectorAll("[data-count]").forEach((el) => {
      const end = Number(el.getAttribute("data-count")) || 0;
      const suffix = el.getAttribute("data-suffix") || "";
      const obj = { v: 0 };
      ScrollTrigger.create({
        trigger: el,
        start: "top 90%",
        once: true,
        onEnter: () => {
          gsap.to(obj, {
            v: end,
            duration: 1.6,
            ease: "power2.out",
            onUpdate: () => {
              el.textContent = Math.round(obj.v) + suffix;
            },
          });
        },
      });
    });
  }

  function initMarquee() {
    const track = document.querySelector(".marquee-track");
    if (!track || track.dataset.cloned) return;
    track.innerHTML = track.innerHTML + track.innerHTML;
    track.dataset.cloned = "1";
  }

  function initTerminal() {
    const el = document.querySelector(".ai-terminal[data-lines]");
    if (!el) return;
    let lines = [];
    try {
      lines = JSON.parse(el.getAttribute("data-lines") || "[]");
    } catch (_) {
      lines = [];
    }
    const out = el.querySelector(".term-out");
    if (!out || !lines.length) return;
    if (reduced) {
      out.innerHTML = lines.map((l) => `<p class="line">${l}</p>`).join("");
      return;
    }
    let i = 0;
    const typeLine = () => {
      if (i >= lines.length) return;
      const p = document.createElement("p");
      p.className = "line";
      out.appendChild(p);
      const raw = lines[i];
      const html = raw
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>");
      let plain = raw.replace(/\*\*/g, "");
      let c = 0;
      const tick = () => {
        c += 1;
        const slice = plain.slice(0, c);
        const rebuilt = html.includes("<strong>")
          ? raw
              .replace(/&/g, "&amp;")
              .replace(/</g, "&lt;")
              .replace(/>/g, "&gt;")
              .replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>")
              .slice(0, Math.min(html.length, c + (raw.length - plain.length)))
          : slice;
        p.innerHTML = rebuilt + (c < plain.length ? '<span class="cursor"></span>' : "");
        if (c < plain.length) {
          window.setTimeout(tick, 12 + Math.random() * 18);
        } else {
          p.innerHTML = html;
          i += 1;
          window.setTimeout(typeLine, 280);
        }
      };
      tick();
    };
    typeLine();
  }

  function initAiField() {
    const canvas = document.getElementById("ai-field");
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    if (!ctx) return;
    const colors = ["#ff4d4d", "#ff9a1f", "#ffe566", "#3dff7a", "#2ecbff", "#1a4fd8"];
    let w = 0;
    let h = 0;
    let nodes = [];
    let mouse = { x: 0.5, y: 0.35 };
    let raf = 0;

    const resize = () => {
      const parent = canvas.parentElement;
      w = parent.clientWidth;
      h = parent.clientHeight;
      const dpr = Math.min(window.devicePixelRatio || 1, 2);
      canvas.width = w * dpr;
      canvas.height = h * dpr;
      canvas.style.width = w + "px";
      canvas.style.height = h + "px";
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      const count = Math.max(36, Math.floor((w * h) / 18000));
      nodes = Array.from({ length: count }, () => ({
        x: Math.random() * w,
        y: Math.random() * h,
        vx: (Math.random() - 0.5) * 0.35,
        vy: (Math.random() - 0.5) * 0.35,
        r: 1.5 + Math.random() * 2.2,
        c: colors[(Math.random() * colors.length) | 0],
        pulse: Math.random() * Math.PI * 2,
      }));
    };

    const draw = () => {
      ctx.clearRect(0, 0, w, h);
      const mx = mouse.x * w;
      const my = mouse.y * h;
      for (let i = 0; i < nodes.length; i++) {
        const n = nodes[i];
        if (!reduced) {
          n.x += n.vx;
          n.y += n.vy;
          n.pulse += 0.02;
          const dx = mx - n.x;
          const dy = my - n.y;
          const d2 = dx * dx + dy * dy;
          if (d2 < 160000) {
            n.vx += dx * 0.000015;
            n.vy += dy * 0.000015;
          }
          if (n.x < 0 || n.x > w) n.vx *= -1;
          if (n.y < 0 || n.y > h) n.vy *= -1;
        }
        for (let j = i + 1; j < nodes.length; j++) {
          const m = nodes[j];
          const dx = n.x - m.x;
          const dy = n.y - m.y;
          const dist = Math.hypot(dx, dy);
          if (dist < 120) {
            ctx.strokeStyle = `rgba(46, 203, 255, ${0.18 * (1 - dist / 120)})`;
            ctx.beginPath();
            ctx.moveTo(n.x, n.y);
            ctx.lineTo(m.x, m.y);
            ctx.stroke();
          }
        }
        const size = n.r + Math.sin(n.pulse) * 0.6;
        ctx.fillStyle = n.c;
        ctx.globalAlpha = 0.75;
        ctx.fillRect(n.x - size, n.y - size, size * 2, size * 2);
        ctx.globalAlpha = 1;
      }
      if (!reduced) raf = requestAnimationFrame(draw);
    };

    resize();
    draw();
    window.addEventListener("resize", () => {
      cancelAnimationFrame(raf);
      resize();
      draw();
    });
    window.addEventListener(
      "pointermove",
      (e) => {
        mouse.x = e.clientX / window.innerWidth;
        mouse.y = e.clientY / window.innerHeight;
      },
      { passive: true }
    );
  }

  function initMagnet() {
    if (!finePointer || reduced) return;
    const buttons = [...document.querySelectorAll(".dock-btn, .btn-magnet")];
    if (!buttons.length) return;

    const CATCH = 90;
    const BREAK = 130;
    const PULL_RATIO = 0.45;
    const active = new Map();
    let pointerX = 0;
    let pointerY = 0;
    let frame = 0;

    const rest = () => ({ x: 0, y: 0, sx: 1, sy: 1, angle: 0 });
    const apply = (el, state) => {
      el.style.setProperty("--tx", `${state.x.toFixed(2)}px`);
      el.style.setProperty("--ty", `${state.y.toFixed(2)}px`);
      el.style.setProperty("--stretch-x", state.sx.toFixed(3));
      el.style.setProperty("--stretch-y", state.sy.toFixed(3));
      el.style.setProperty("--pull-angle", `${state.angle.toFixed(2)}deg`);
    };

    const release = (el, entry) => {
      if (!entry.pulling) return;
      entry.pulling = false;
      entry.target = rest();
      el.classList.remove("is-pulling");
      el.classList.add("is-snapping");
      entry.state = rest();
      apply(el, entry.state);
      clearTimeout(entry.snapTimer);
      entry.snapTimer = setTimeout(() => {
        el.classList.remove("is-snapping");
        entry.state = rest();
        apply(el, entry.state);
        active.delete(el);
      }, 560);
    };

    const tick = () => {
      let busy = false;
      active.forEach((entry, el) => {
        const ease = entry.pulling ? 0.28 : 0.22;
        entry.state.x += (entry.target.x - entry.state.x) * ease;
        entry.state.y += (entry.target.y - entry.state.y) * ease;
        entry.state.sx += (entry.target.sx - entry.state.sx) * ease;
        entry.state.sy += (entry.target.sy - entry.state.sy) * ease;
        entry.state.angle = entry.target.angle;
        apply(el, entry.state);
        const settled =
          !entry.pulling &&
          Math.abs(entry.state.x) < 0.2 &&
          Math.abs(entry.state.y) < 0.2 &&
          Math.abs(entry.state.sx - 1) < 0.01;
        if (!settled) busy = true;
      });
      frame = busy ? requestAnimationFrame(tick) : 0;
    };

    const startLoop = () => {
      if (!frame) frame = requestAnimationFrame(tick);
    };

    const centerOf = (el, entry) => {
      if (entry && entry.pulling) return { x: entry.originX, y: entry.originY };
      const rect = el.getBoundingClientRect();
      return { x: rect.left + rect.width / 2, y: rect.top + rect.height / 2 };
    };

    window.addEventListener(
      "pointermove",
      (e) => {
        pointerX = e.clientX;
        pointerY = e.clientY;
        let nearest = null;
        let nearestDist = Infinity;
        buttons.forEach((el) => {
          const c = centerOf(el, active.get(el));
          const dist = Math.hypot(pointerX - c.x, pointerY - c.y);
          if (dist < nearestDist) {
            nearestDist = dist;
            nearest = el;
          }
        });
        buttons.forEach((el) => {
          const entry = active.get(el) || {
            pulling: false,
            state: rest(),
            target: rest(),
            originX: 0,
            originY: 0,
            snapTimer: 0,
          };
          const c = centerOf(el, entry);
          const dx = pointerX - c.x;
          const dy = pointerY - c.y;
          const dist = Math.hypot(dx, dy);
          if (el === nearest && dist < CATCH) {
            if (!entry.pulling) {
              entry.pulling = true;
              entry.originX = c.x;
              entry.originY = c.y;
              el.classList.add("is-pulling");
              el.classList.remove("is-snapping");
            }
            const pull = Math.min(dist, BREAK) * PULL_RATIO;
            const ang = (Math.atan2(dy, dx) * 180) / Math.PI;
            entry.target = {
              x: Math.cos((ang * Math.PI) / 180) * pull,
              y: Math.sin((ang * Math.PI) / 180) * pull,
              sx: 1 + Math.min(dist, BREAK) / 400,
              sy: 1 - Math.min(dist, BREAK) / 700,
              angle: ang * 0.04,
            };
            if (dist > BREAK) release(el, entry);
            active.set(el, entry);
            startLoop();
          } else if (entry.pulling) {
            release(el, entry);
            active.set(el, entry);
            startLoop();
          }
        });
      },
      { passive: true }
    );
  }

  function initCursorTrail() {
    const colors = ["#ff4d4d", "#ff9a1f", "#ffe566", "#3dff7a", "#2ecbff"];
    const pool = colors.map((c) => {
      const d = document.createElement("div");
      d.className = "cursor-pixel";
      d.style.background = c;
      document.body.appendChild(d);
      return d;
    });
    let i = 0;
    window.addEventListener(
      "pointermove",
      (e) => {
        const el = pool[i % pool.length];
        i += 1;
        el.style.transform = `translate(${e.clientX}px, ${e.clientY}px)`;
        el.style.opacity = "0.9";
        if (window.gsap) {
          gsap.to(el, { opacity: 0, duration: 0.55, overwrite: true });
        } else {
          el.style.transition = "opacity 0.55s";
          requestAnimationFrame(() => {
            el.style.opacity = "0";
          });
        }
      },
      { passive: true }
    );
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
