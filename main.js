(() => {
  const reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const finePointer = window.matchMedia("(hover: hover) and (pointer: fine)").matches;

  const loadScript = (src, ms = 4000) =>
    new Promise((resolve, reject) => {
      if (window.gsap && src.includes("gsap.min.js")) {
        resolve();
        return;
      }
      if (window.ScrollTrigger && src.includes("ScrollTrigger")) {
        resolve();
        return;
      }
      if ([...document.scripts].some((s) => s.src.includes(src.split("/").pop()))) {
        resolve();
        return;
      }
      const el = document.createElement("script");
      el.src = src;
      const timer = window.setTimeout(() => reject(new Error("timeout " + src)), ms);
      el.onload = () => {
        window.clearTimeout(timer);
        resolve();
      };
      el.onerror = () => {
        window.clearTimeout(timer);
        reject(new Error("fail " + src));
      };
      document.head.appendChild(el);
    });

  async function boot() {
    ensureProgress();
    // Never block first paint / copy on CDN. Split + chrome first.
    splitTitles();
    initNav();
    initHeaderScroll();
    initProgress();
    initAiField();
    initTerminal();
    initMarquee();
    initMagnet();
    document.documentElement.classList.add("js-ready");

    try {
      await loadScript("https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js");
      await loadScript("https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/ScrollTrigger.min.js");
      if (window.gsap && window.ScrollTrigger) window.gsap.registerPlugin(window.ScrollTrigger);
    } catch (_) {
      /* CSS fallbacks still work */
    }

    if (!reduced && window.gsap) {
      initHero();
      initPageHero();
      initReveal();
      initServiceBands();
      initCounters();
      if (finePointer) initCursorTrail();
    } else {
      document.querySelectorAll(".reveal, .reveal-child").forEach((el) => {
        el.style.opacity = "1";
        el.style.transform = "none";
      });
    }
  }

  function ensureProgress() {
    if (document.querySelector(".progress-bar")) return;
    const bar = document.createElement("div");
    bar.className = "progress-bar";
    bar.setAttribute("aria-hidden", "true");
    document.body.prepend(bar);
  }

  function splitTitles() {
    document.querySelectorAll(".hero-title, .page-hero h1").forEach((title) => {
      if (title.dataset.splitDone) return;
      const nodes = [...title.childNodes];
      title.textContent = "";
      nodes.forEach((node) => {
        if (node.nodeType === Node.TEXT_NODE) {
          node.textContent.split(/(\s+)/).forEach((part) => {
            if (!part) return;
            if (/^\s+$/.test(part)) {
              title.appendChild(document.createTextNode(part));
              return;
            }
            const word = document.createElement("span");
            word.className = "word";
            const inner = document.createElement("span");
            inner.textContent = part;
            word.appendChild(inner);
            title.appendChild(word);
          });
        } else if (node.nodeType === Node.ELEMENT_NODE) {
          const el = node;
          const word = document.createElement("span");
          word.className = "word";
          const inner = document.createElement("span");
          if (el.classList && el.classList.contains("grad")) {
            inner.className = "grad";
          }
          inner.innerHTML = el.innerHTML;
          word.appendChild(inner);
          title.appendChild(word);
        }
      });
      title.dataset.splitDone = "1";
    });
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

  function initHeaderScroll() {
    const header = document.querySelector(".site-header");
    if (!header) return;
    const onScroll = () => {
      header.classList.toggle("is-scrolled", window.scrollY > 24);
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  function initProgress() {
    const bar = document.querySelector(".progress-bar");
    if (!bar) return;
    const update = () => {
      const doc = document.documentElement;
      const max = doc.scrollHeight - window.innerHeight;
      const p = max > 0 ? (window.scrollY / max) * 100 : 0;
      bar.style.width = `${p}%`;
    };
    update();
    window.addEventListener("scroll", update, { passive: true });
    window.addEventListener("resize", update);
  }

  function initHero() {
    if (!window.gsap) return;
    const hero = document.querySelector(".hero");
    if (!hero) return;

    const words = hero.querySelectorAll(".hero-title .word > span");
    const tl = gsap.timeline({ defaults: { ease: "power3.out" } });

    gsap.set(words, { yPercent: 110 });
    gsap.set([".hero-eyebrow", ".hero-sub", ".hero-cta .btn", ".hero-stage", ".hero-chip"], {
      autoAlpha: 0,
      y: 24,
    });

    tl.to(".hero-eyebrow", { autoAlpha: 1, y: 0, duration: 0.6 })
      .to(words, { yPercent: 0, duration: 0.95, stagger: 0.06 }, "-=0.25")
      .to(".hero-sub", { autoAlpha: 1, y: 0, duration: 0.7 }, "-=0.45")
      .to(".hero-cta .btn", { autoAlpha: 1, y: 0, stagger: 0.1, duration: 0.55 }, "-=0.4")
      .to(".hero-stage", { autoAlpha: 1, y: 0, duration: 0.85 }, "-=0.35")
      .to(".hero-chip", { autoAlpha: 1, y: 0, stagger: 0.08, duration: 0.5 }, "-=0.55");

    if (window.ScrollTrigger) {
      gsap.to(".hero-mesh", {
        yPercent: 18,
        ease: "none",
        scrollTrigger: { trigger: hero, start: "top top", end: "bottom top", scrub: true },
      });
      gsap.to(".hero-orb-a", {
        y: 80,
        x: 40,
        ease: "none",
        scrollTrigger: { trigger: hero, start: "top top", end: "bottom top", scrub: true },
      });
      gsap.to(".hero-orb-b", {
        y: -60,
        x: -30,
        ease: "none",
        scrollTrigger: { trigger: hero, start: "top top", end: "bottom top", scrub: true },
      });
    }
  }

  function initPageHero() {
    if (!window.gsap) return;
    const hero = document.querySelector(".page-hero");
    if (!hero || document.querySelector(".hero")) return;

    const words = hero.querySelectorAll("h1 .word > span");
    const tl = gsap.timeline({ defaults: { ease: "power3.out" } });
    const kicker = hero.querySelector(".section-kicker");
    const sub = hero.querySelector(":scope > .container > p, :scope > div > p");
    const cta = hero.querySelector(".hero-cta");
    gsap.set(words, { yPercent: 115 });
    const intro = [kicker, sub, cta].filter(Boolean);
    if (intro.length) gsap.set(intro, { autoAlpha: 0, y: 20 });

    if (kicker) tl.to(kicker, { autoAlpha: 1, y: 0, duration: 0.5 });
    tl.to(words, { yPercent: 0, duration: 0.85, stagger: 0.05 }, "-=0.15");
    if (sub) tl.to(sub, { autoAlpha: 1, y: 0, duration: 0.6 }, "-=0.4");
    if (cta) tl.to(cta, { autoAlpha: 1, y: 0, duration: 0.55 }, "-=0.35");
  }

  function initReveal() {
    if (!window.gsap || !window.ScrollTrigger) {
      document.querySelectorAll(".reveal, .reveal-child").forEach((el) => {
        el.style.opacity = "1";
        el.style.transform = "none";
      });
      return;
    }

    gsap.utils.toArray(".reveal").forEach((el) => {
      gsap.to(el, {
        autoAlpha: 1,
        y: 0,
        duration: 0.9,
        ease: "power3.out",
        scrollTrigger: { trigger: el, start: "top 88%" },
      });
    });

    document.querySelectorAll(".engage-grid, .trust-strip, .stats, .process-steps, .blog-grid, .outcome-grid, .industry-grid, .stack-grid, .price-grid, .promise-list").forEach((group) => {
      const kids = group.querySelectorAll(":scope > *");
      if (!kids.length) return;
      gsap.set(kids, { autoAlpha: 0, y: 28 });
      gsap.to(kids, {
        autoAlpha: 1,
        y: 0,
        duration: 0.75,
        stagger: 0.08,
        ease: "power3.out",
        scrollTrigger: { trigger: group, start: "top 85%" },
      });
    });

    gsap.utils.toArray(".cta-band").forEach((el) => {
      gsap.from(el, {
        autoAlpha: 0,
        y: 40,
        scale: 0.98,
        duration: 0.9,
        ease: "power3.out",
        scrollTrigger: { trigger: el, start: "top 88%" },
      });
    });
  }

  function initServiceBands() {
    if (!window.gsap || !window.ScrollTrigger) return;
    gsap.utils.toArray(".service-band").forEach((el, i) => {
      const img = el.querySelector(".band-visual img");
      const fromX = i % 2 ? 56 : -56;
      gsap.from(el, {
        x: fromX,
        autoAlpha: 0,
        duration: 1,
        ease: "power3.out",
        scrollTrigger: { trigger: el, start: "top 82%" },
      });
      if (img) {
        gsap.fromTo(
          img,
          { scale: 1.18, yPercent: 8 },
          {
            scale: 1.04,
            yPercent: 0,
            ease: "none",
            scrollTrigger: {
              trigger: el,
              start: "top bottom",
              end: "bottom top",
              scrub: true,
            },
          }
        );
      }
    });
  }

  function initCounters() {
    if (!window.gsap || !window.ScrollTrigger) return;
    document.querySelectorAll("[data-count]").forEach((el) => {
      const end = Number(el.getAttribute("data-count")) || 0;
      const suffix = el.getAttribute("data-suffix") || "";
      const obj = { v: 0 };
      const parent = el.closest(".stat");
      ScrollTrigger.create({
        trigger: el,
        start: "top 90%",
        once: true,
        onEnter: () => {
          if (parent) parent.classList.add("is-on");
          gsap.to(obj, {
            v: end,
            duration: 1.7,
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
      out.innerHTML = lines.map((l) => `<p class="line">${l.replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>")}</p>`).join("");
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
      const plain = raw.replace(/\*\*/g, "");
      let c = 0;
      const tick = () => {
        c += 1;
        p.textContent = plain.slice(0, c);
        if (c < plain.length) {
          p.innerHTML = p.textContent + '<span class="cursor"></span>';
          window.setTimeout(tick, 10 + Math.random() * 16);
        } else {
          p.innerHTML = html;
          i += 1;
          window.setTimeout(typeLine, 260);
        }
      };
      tick();
    };
    window.setTimeout(typeLine, 700);
  }

  function initAiField() {
    const canvas = document.getElementById("ai-field");
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    if (!ctx) return;
    const colors = ["#3dff7a", "#3ad0ff", "#1a5cff", "#ffe566"];
    let w = 0;
    let h = 0;
    let nodes = [];
    let mouse = { x: 0.55, y: 0.4 };
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
      const count = Math.max(28, Math.floor((w * h) / 26000));
      nodes = Array.from({ length: count }, () => ({
        x: Math.random() * w,
        y: Math.random() * h,
        vx: (Math.random() - 0.5) * 0.22,
        vy: (Math.random() - 0.5) * 0.22,
        r: 1.2 + Math.random() * 1.8,
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
          n.pulse += 0.015;
          const dx = mx - n.x;
          const dy = my - n.y;
          const d2 = dx * dx + dy * dy;
          if (d2 < 140000) {
            n.vx += dx * 0.00001;
            n.vy += dy * 0.00001;
          }
          if (n.x < 0 || n.x > w) n.vx *= -1;
          if (n.y < 0 || n.y > h) n.vy *= -1;
        }
        for (let j = i + 1; j < nodes.length; j++) {
          const m = nodes[j];
          const dx = n.x - m.x;
          const dy = n.y - m.y;
          const dist = Math.hypot(dx, dy);
          if (dist < 110) {
            ctx.strokeStyle = `rgba(58, 208, 255, ${0.14 * (1 - dist / 110)})`;
            ctx.lineWidth = 1;
            ctx.beginPath();
            ctx.moveTo(n.x, n.y);
            ctx.lineTo(m.x, m.y);
            ctx.stroke();
          }
        }
        const size = n.r + Math.sin(n.pulse) * 0.45;
        ctx.fillStyle = n.c;
        ctx.globalAlpha = 0.55;
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
    const colors = ["#3dff7a", "#3ad0ff", "#ffe566", "#ff9a1f"];
    const pool = colors.map((c) => {
      const d = document.createElement("div");
      d.className = "cursor-pixel";
      d.style.background = c;
      document.body.appendChild(d);
      return d;
    });
    let i = 0;
    let last = 0;
    window.addEventListener(
      "pointermove",
      (e) => {
        const now = performance.now();
        if (now - last < 32) return;
        last = now;
        const el = pool[i % pool.length];
        i += 1;
        el.style.transform = `translate(${e.clientX}px, ${e.clientY}px)`;
        el.style.opacity = "0.75";
        if (window.gsap) {
          gsap.to(el, { opacity: 0, duration: 0.45, overwrite: true });
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
