(() => {
  const reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const finePointer = window.matchMedia("(hover: hover) and (pointer: fine)").matches;

  // Refresh always lands at top; deep-link hashes still work on first visit
  if ("scrollRestoration" in history) history.scrollRestoration = "manual";
  const navType = performance.getEntriesByType("navigation")[0]?.type || "navigate";
  const isReload = navType === "reload";
  const forceTop = () => {
    window.scrollTo(0, 0);
    document.documentElement.scrollTop = 0;
    document.body.scrollTop = 0;
  };
  if (isReload) {
    if (location.hash) history.replaceState(null, "", location.pathname + location.search);
    forceTop();
    window.addEventListener("load", forceTop);
  } else if (!location.hash) {
    forceTop();
  }

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
    if (isReload) forceTop();
    ensureProgress();
    initBackToTop();
    splitTitles(document.querySelectorAll(".hero-title, .page-hero h1, .section-title"));
    initNav();
    initHeaderScroll();
    initProgress();
    initAiField();
    initTerminal();
    initMarquee();
    initMagnet();
    initFaq();
    document.documentElement.classList.add("js-ready");

    try {
      await loadScript("https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js");
      await loadScript("https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/ScrollTrigger.min.js");
      if (window.gsap && window.ScrollTrigger) window.gsap.registerPlugin(window.ScrollTrigger);
    } catch (_) {
      /* CSS fallbacks still work */
    }

    initWorkFilters();
    initSectionSpy();

    if (!reduced && window.gsap) {
      initPageIntro();
      initNavIntro();
      initHero();
      initPageHero();
      initReveal();
      initSectionTitles();
      initServiceBands();
      initCounters();
      initMarqueeGlow();
      initTiltCards();
      initFooter();
      initButtonShine();
      initHeroFloaters();
      initTitleUnderlines();
      initDockPulse();
      initLinkLift();
      initImageZoomHover();
      initWorkRail();
      initManifesto();
      initBento();
      if (finePointer) {
        initCursorSystem();
      }
    } else {
      document.querySelectorAll(".reveal, .reveal-child, .band-visual").forEach((el) => {
        el.style.opacity = "1";
        el.style.transform = "none";
        el.classList.add("is-in");
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

  function initBackToTop() {
    if (document.querySelector(".back-to-top")) return;
    let dock = document.querySelector(".sticky-dock");
    if (!dock) {
      dock = document.createElement("div");
      dock.className = "sticky-dock";
      dock.setAttribute("aria-label", "Quick actions");
      document.body.appendChild(dock);
    }
    const btn = document.createElement("button");
    btn.type = "button";
    btn.className = "back-to-top";
    btn.setAttribute("aria-label", "Back to top");
    btn.innerHTML = '<span aria-hidden="true">↑</span><span class="back-to-top-label">Top</span>';
    dock.prepend(btn);

    const toggle = () => {
      btn.classList.toggle("is-visible", window.scrollY > 420);
    };
    toggle();
    window.addEventListener("scroll", toggle, { passive: true });
    btn.addEventListener("click", () => {
      window.scrollTo({ top: 0, behavior: reduced ? "auto" : "smooth" });
    });
    initDockObscure(dock);
  }

  function initDockObscure(dock) {
    if (!dock || dock.dataset.obscureReady) return;
    dock.dataset.obscureReady = "1";

    const CONTENT =
      "a, button, p, h1, h2, h3, h4, li, label, summary, input, textarea, select, img, .btn, .work-card, .price-card, .bento-tile, .blog-card, .term-card, .faq-topic-card, .seo-chip, .service-chip, .nav-links, .nav-drop-toggle, table, td, th";

    const samplePoints = (rect) => [
      [rect.left + 12, rect.top + 12],
      [rect.left + rect.width / 2, rect.top + rect.height / 2],
      [rect.right - 12, rect.bottom - 12],
      [rect.left + 12, rect.bottom - 12],
      [rect.right - 12, rect.top + 12],
    ];

    const contentUnderDock = () => {
      const rect = dock.getBoundingClientRect();
      const prev = dock.style.pointerEvents;
      dock.style.pointerEvents = "none";
      let blocked = false;
      for (const [x, y] of samplePoints(rect)) {
        const el = document.elementFromPoint(x, y);
        if (el && el.closest(CONTENT)) {
          blocked = true;
          break;
        }
      }
      dock.style.pointerEvents = prev;
      return blocked;
    };

    const refresh = (e) => {
      const nearCorner =
        e &&
        e.clientX > window.innerWidth - 140 &&
        e.clientY > window.innerHeight - 180;

      if (e && e.target instanceof Element && e.target.closest(".sticky-dock")) {
        dock.classList.remove("is-obscured");
        return;
      }

      // Hovering real page content away from the dock corner → hide
      if (e && e.target instanceof Element && e.target.closest(CONTENT) && !nearCorner) {
        dock.classList.add("is-obscured");
        return;
      }

      // Content physically sitting under the dock buttons → hide
      if (contentUnderDock() && !nearCorner) {
        dock.classList.add("is-obscured");
        return;
      }

      dock.classList.remove("is-obscured");
    };

    window.addEventListener("pointermove", refresh, { passive: true });
    window.addEventListener("scroll", () => refresh(), { passive: true });
    window.addEventListener("resize", () => refresh());
    refresh();
  }

  function splitTitles(list) {
    list.forEach((title) => {
      if (!title || title.dataset.splitDone) return;
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
          const word = document.createElement("span");
          word.className = "word";
          const inner = document.createElement("span");
          if (node.classList && node.classList.contains("grad")) inner.className = "grad";
          inner.innerHTML = node.innerHTML;
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
      if (!open) {
        links.querySelectorAll(".has-dropdown.is-open").forEach((el) => {
          el.classList.remove("is-open");
          const btn = el.querySelector(".nav-drop-toggle");
          if (btn) btn.setAttribute("aria-expanded", "false");
        });
      }
    });
    links.querySelectorAll("a").forEach((a) =>
      a.addEventListener("click", () => {
        links.classList.remove("is-open");
        toggle.setAttribute("aria-expanded", "false");
        links.querySelectorAll(".has-dropdown.is-open").forEach((el) => el.classList.remove("is-open"));
      })
    );

    const closeDrops = (except) => {
      links.querySelectorAll(".has-dropdown").forEach((el) => {
        if (except && el === except) return;
        el.classList.remove("is-open", "is-hover");
        const b = el.querySelector(".nav-drop-toggle");
        if (b) b.setAttribute("aria-expanded", "false");
      });
    };

    links.querySelectorAll(".has-dropdown").forEach((item) => {
      const btn = item.querySelector(".nav-drop-toggle");
      if (!btn) return;

      // Desktop: open on hover without losing the menu in the gap
      item.addEventListener("pointerenter", () => {
        if (window.matchMedia("(max-width: 960px)").matches) return;
        closeDrops(item);
        item.classList.add("is-hover");
        btn.setAttribute("aria-expanded", "true");
      });
      item.addEventListener("pointerleave", () => {
        if (window.matchMedia("(max-width: 960px)").matches) return;
        item.classList.remove("is-hover");
        if (!item.classList.contains("is-open")) btn.setAttribute("aria-expanded", "false");
      });

      btn.addEventListener("click", (e) => {
        e.preventDefault();
        e.stopPropagation();
        const willOpen = !item.classList.contains("is-open");
        closeDrops(item);
        item.classList.toggle("is-open", willOpen);
        item.classList.toggle("is-hover", willOpen);
        btn.setAttribute("aria-expanded", willOpen ? "true" : "false");
      });
    });

    document.addEventListener("click", (e) => {
      if (e.target.closest(".has-dropdown") || e.target.closest(".nav-toggle")) return;
      closeDrops();
    });
  }

  function initNavIntro() {
    if (!window.gsap) return;
    const items = document.querySelectorAll(".nav-links > li");
    if (!items.length) return;
    gsap.from(items, {
      autoAlpha: 0,
      y: -10,
      duration: 0.55,
      stagger: 0.05,
      ease: "power3.out",
      delay: 0.15,
    });
    gsap.from(".logo", { autoAlpha: 0, x: -16, duration: 0.7, ease: "power3.out" });
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
    const pixels = hero.querySelectorAll(".pixel");
    const tl = gsap.timeline({ defaults: { ease: "power3.out" } });

    gsap.set(words, { yPercent: 115 });
    gsap.set([".hero-brand", ".hero-eyebrow", ".hero-sub", ".hero-cta .btn", ".hero-stage"], {
      autoAlpha: 0,
      y: 28,
    });
    gsap.set(pixels, { y: 18, autoAlpha: 0 });

    tl.to(".hero-brand", { autoAlpha: 1, y: 0, duration: 0.65 })
      .to(".hero-eyebrow", { autoAlpha: 1, y: 0, duration: 0.45 }, "-=0.3")
      .to(words, { yPercent: 0, duration: 0.8, stagger: 0.06 }, "-=0.2")
      .to(".hero-sub", { autoAlpha: 1, y: 0, duration: 0.55 }, "-=0.4")
      .to(".hero-cta .btn", { autoAlpha: 1, y: 0, stagger: 0.08, duration: 0.45 }, "-=0.3")
      .to(".hero-stage", { autoAlpha: 1, y: 0, duration: 0.85, ease: "power4.out" }, "-=0.55")
      .to(pixels, { autoAlpha: 1, y: 0, stagger: 0.05, duration: 0.4 }, "-=0.45");

    if (window.ScrollTrigger) {
      gsap.to(hero.querySelector(".hero-inner"), {
        y: 70,
        autoAlpha: 0.35,
        ease: "none",
        scrollTrigger: { trigger: hero, start: "top top", end: "bottom top", scrub: true },
      });
      gsap.to(".hero-mesh", {
        yPercent: 22,
        rotate: 8,
        ease: "none",
        scrollTrigger: { trigger: hero, start: "top top", end: "bottom top", scrub: true },
      });
      gsap.to(".hero-orb-a", {
        y: 90,
        x: 50,
        ease: "none",
        scrollTrigger: { trigger: hero, start: "top top", end: "bottom top", scrub: true },
      });
      gsap.to(".hero-orb-b", {
        y: -70,
        x: -40,
        ease: "none",
        scrollTrigger: { trigger: hero, start: "top top", end: "bottom top", scrub: true },
      });
      gsap.to("#ai-field", {
        opacity: 0.15,
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
    if (intro.length) gsap.set(intro, { autoAlpha: 0, y: 22 });

    if (kicker) tl.to(kicker, { autoAlpha: 1, y: 0, duration: 0.5 });
    tl.to(words, { yPercent: 0, duration: 0.85, stagger: 0.05 }, "-=0.15");
    if (sub) tl.to(sub, { autoAlpha: 1, y: 0, duration: 0.6 }, "-=0.4");
    if (cta) tl.to(cta, { autoAlpha: 1, y: 0, duration: 0.55 }, "-=0.35");
  }

  function initSectionTitles() {
    if (!window.gsap || !window.ScrollTrigger) return;
    gsap.utils.toArray(".section-title").forEach((title) => {
      const words = title.querySelectorAll(".word > span");
      if (!words.length) return;
      gsap.set(words, { yPercent: 110 });
      gsap.to(words, {
        yPercent: 0,
        duration: 0.85,
        stagger: 0.045,
        ease: "power3.out",
        scrollTrigger: { trigger: title, start: "top 88%" },
      });
    });
    gsap.utils.toArray(".section-kicker").forEach((el) => {
      gsap.from(el, {
        autoAlpha: 0,
        x: -18,
        duration: 0.6,
        ease: "power3.out",
        scrollTrigger: { trigger: el, start: "top 90%" },
      });
    });
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

    document
      .querySelectorAll(
        ".engage-grid, .trust-strip, .stats, .process-steps, .blog-grid, .outcome-grid, .industry-grid, .stack-grid, .price-grid, .promise-list, .seo-cloud"
      )
      .forEach((group) => {
        const kids = group.querySelectorAll(":scope > *");
        if (!kids.length) return;
        gsap.set(kids, { autoAlpha: 0, y: 30, scale: 0.98 });
        gsap.to(kids, {
          autoAlpha: 1,
          y: 0,
          scale: 1,
          duration: 0.75,
          stagger: { each: 0.07, from: "start" },
          ease: "power3.out",
          scrollTrigger: { trigger: group, start: "top 85%" },
        });
      });

    gsap.utils.toArray(".cta-band").forEach((el) => {
      gsap.from(el, {
        autoAlpha: 0,
        y: 48,
        scale: 0.97,
        duration: 1,
        ease: "power3.out",
        scrollTrigger: { trigger: el, start: "top 88%" },
      });
    });

    gsap.utils.toArray(".compare-wrap, .form, .faq").forEach((el) => {
      gsap.from(el, {
        autoAlpha: 0,
        y: 36,
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
      const visual = el.querySelector(".band-visual");
      const copy = el.querySelector("div:not(.band-visual)") || el.children[0];
      const fromX = i % 2 ? 64 : -64;

      gsap.from(copy, {
        x: fromX,
        autoAlpha: 0,
        duration: 1,
        ease: "power3.out",
        scrollTrigger: { trigger: el, start: "top 82%" },
      });

      ScrollTrigger.create({
        trigger: el,
        start: "top 80%",
        once: true,
        onEnter: () => visual && visual.classList.add("is-in"),
      });

      if (img) {
        gsap.fromTo(
          img,
          { scale: 1.2, yPercent: 10 },
          {
            scale: 1.02,
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
            duration: 1.8,
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

  function initMarqueeGlow() {
    if (!window.gsap || !window.ScrollTrigger) return;
    const marquee = document.querySelector(".marquee");
    if (!marquee) return;
    gsap.from(marquee, {
      autoAlpha: 0,
      y: 20,
      duration: 0.8,
      ease: "power3.out",
      scrollTrigger: { trigger: marquee, start: "top 95%" },
    });
  }

  function initTiltCards() {
    if (!finePointer || !window.gsap) return;
    const cards = document.querySelectorAll(
      ".engage-card, .price-card, .blog-card, .stat, .process-steps article, .outcome, .industry, .work-card"
    );
    cards.forEach((card) => {
      card.classList.add("tilt-card");
      card.addEventListener("pointermove", (e) => {
        const r = card.getBoundingClientRect();
        const x = (e.clientX - r.left) / r.width - 0.5;
        const y = (e.clientY - r.top) / r.height - 0.5;
        gsap.to(card, {
          rotateY: x * 8,
          rotateX: -y * 8,
          y: -4,
          duration: 0.35,
          ease: "power2.out",
          transformPerspective: 700,
        });
      });
      card.addEventListener("pointerleave", () => {
        gsap.to(card, {
          rotateY: 0,
          rotateX: 0,
          y: 0,
          duration: 0.55,
          ease: "power3.out",
        });
      });
    });
  }

  function initFooter() {
    if (!window.gsap || !window.ScrollTrigger) return;
    const footer = document.querySelector(".footer");
    if (!footer) return;
    gsap.from(".footer-grid > *", {
      autoAlpha: 0,
      y: 28,
      stagger: 0.08,
      duration: 0.75,
      ease: "power3.out",
      scrollTrigger: { trigger: footer, start: "top 90%" },
    });
  }

  function initFaq() {
    document.querySelectorAll(".faq details").forEach((d) => {
      d.addEventListener("toggle", () => {
        if (!d.open || !window.gsap || reduced) return;
        const p = d.querySelector("p");
        if (!p) return;
        gsap.fromTo(p, { autoAlpha: 0, y: 8 }, { autoAlpha: 1, y: 0, duration: 0.35, ease: "power2.out" });
      });
    });
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
      out.innerHTML = lines
        .map((l) => `<p class="line">${l.replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>")}</p>`)
        .join("");
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
          window.setTimeout(tick, 9 + Math.random() * 14);
        } else {
          p.innerHTML = html;
          i += 1;
          window.setTimeout(typeLine, 240);
        }
      };
      tick();
    };
    window.setTimeout(typeLine, 1100);
  }

  function initAiField() {
    const canvas = document.getElementById("ai-field");
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    if (!ctx) return;
    const colors = ["#3dff7a", "#3ad0ff", "#1a5cff", "#ffe566", "#ff9a1f"];
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
      const count = Math.max(32, Math.floor((w * h) / 22000));
      nodes = Array.from({ length: count }, () => ({
        x: Math.random() * w,
        y: Math.random() * h,
        vx: (Math.random() - 0.5) * 0.28,
        vy: (Math.random() - 0.5) * 0.28,
        r: 1.2 + Math.random() * 2,
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
          n.pulse += 0.018;
          const dx = mx - n.x;
          const dy = my - n.y;
          const d2 = dx * dx + dy * dy;
          if (d2 < 150000) {
            n.vx += dx * 0.000012;
            n.vy += dy * 0.000012;
          }
          if (n.x < 0 || n.x > w) n.vx *= -1;
          if (n.y < 0 || n.y > h) n.vy *= -1;
        }
        for (let j = i + 1; j < nodes.length; j++) {
          const m = nodes[j];
          const dx = n.x - m.x;
          const dy = n.y - m.y;
          const dist = Math.hypot(dx, dy);
          if (dist < 115) {
            ctx.strokeStyle = `rgba(58, 208, 255, ${0.16 * (1 - dist / 115)})`;
            ctx.lineWidth = 1;
            ctx.beginPath();
            ctx.moveTo(n.x, n.y);
            ctx.lineTo(m.x, m.y);
            ctx.stroke();
          }
        }
        const size = n.r + Math.sin(n.pulse) * 0.5;
        ctx.fillStyle = n.c;
        ctx.globalAlpha = 0.62;
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
    // Never magnet sticky dock buttons - they fight Top/Contact and stick to the cursor
    const buttons = [...document.querySelectorAll(".btn-magnet")];
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

  function initCursorSystem() {
    document.documentElement.classList.add("has-cursor");

    const wrap = document.createElement("div");
    wrap.className = "cursor-system";
    wrap.setAttribute("aria-hidden", "true");

    const ring = document.createElement("div");
    ring.className = "cursor-ring";
    const core = document.createElement("div");
    core.className = "cursor-core";
    wrap.appendChild(ring);
    wrap.appendChild(core);

    // Lagging circle chain = the "tail"
    const TAIL_N = 10;
    const tails = Array.from({ length: TAIL_N }, (_, i) => {
      const d = document.createElement("div");
      d.className = "cursor-tail";
      d.style.setProperty("--i", String(i));
      wrap.appendChild(d);
      return { el: d, x: window.innerWidth / 2, y: window.innerHeight / 2 };
    });

    // Extra spark particles for speed bursts
    const sparkColors = ["#3dff7a", "#3ad0ff", "#ffe566", "#ff9a1f"];
    const sparks = sparkColors.map((c) => {
      const d = document.createElement("div");
      d.className = "cursor-pixel";
      d.style.background = c;
      wrap.appendChild(d);
      return d;
    });

    document.body.appendChild(wrap);

    let mx = window.innerWidth / 2;
    let my = window.innerHeight / 2;
    let rx = mx;
    let ry = my;
    let cx = mx;
    let cy = my;
    let lastSpark = 0;
    let sparkI = 0;
    let lastX = mx;
    let lastY = my;
    let visible = false;

    const loop = () => {
      // Core snaps fastest, ring lags a touch, tail lags more (premium feel)
      cx += (mx - cx) * 0.42;
      cy += (my - cy) * 0.42;
      rx += (mx - rx) * 0.18;
      ry += (my - ry) * 0.18;
      core.style.transform = `translate3d(${cx}px, ${cy}px, 0)`;
      ring.style.transform = `translate3d(${rx}px, ${ry}px, 0)`;

      let px = rx;
      let py = ry;
      tails.forEach((node, i) => {
        const ease = 0.28 - i * 0.018;
        node.x += (px - node.x) * ease;
        node.y += (py - node.y) * ease;
        node.el.style.transform = `translate3d(${node.x}px, ${node.y}px, 0)`;
        px = node.x;
        py = node.y;
      });

      if (visible) {
        ring.style.opacity = "1";
        core.style.opacity = "1";
      }
      requestAnimationFrame(loop);
    };
    loop();

    window.addEventListener(
      "pointermove",
      (e) => {
        mx = e.clientX;
        my = e.clientY;
        visible = true;

        const dist = Math.hypot(mx - lastX, my - lastY);
        const now = performance.now();
        if (dist > 28 && now - lastSpark > 28) {
          lastSpark = now;
          lastX = mx;
          lastY = my;
          const spark = sparks[sparkI % sparks.length];
          sparkI += 1;
          spark.style.transform = `translate3d(${mx}px, ${my}px, 0) scale(1)`;
          spark.style.opacity = "0.85";
          if (window.gsap) {
            gsap.to(spark, {
              opacity: 0,
              scale: 0.2,
              duration: 0.55,
              ease: "power2.out",
              overwrite: true,
            });
          }
        }
      },
      { passive: true }
    );

    window.addEventListener("pointerleave", () => {
      visible = false;
      ring.style.opacity = "0";
      core.style.opacity = "0";
      tails.forEach((n) => {
        n.el.style.opacity = "0";
      });
    });
    window.addEventListener("pointerenter", () => {
      visible = true;
      tails.forEach((n) => {
        n.el.style.opacity = "";
      });
    });

    const hotSel = "a, button, .btn, .dock-btn, summary, .blog-card, .seo-chip, .nav-links a";
    document.querySelectorAll(hotSel).forEach((el) => {
      el.addEventListener("pointerenter", () => {
        wrap.classList.add("is-hot");
        ring.classList.add("is-hot");
      });
      el.addEventListener("pointerleave", () => {
        wrap.classList.remove("is-hot");
        ring.classList.remove("is-hot");
      });
    });

    // Keep native cursor on form fields for usability
    document.querySelectorAll("input, textarea, select").forEach((el) => {
      el.addEventListener("pointerenter", () => document.documentElement.classList.add("cursor-form"));
      el.addEventListener("pointerleave", () => document.documentElement.classList.remove("cursor-form"));
      el.addEventListener("focus", () => document.documentElement.classList.add("cursor-form"));
      el.addEventListener("blur", () => document.documentElement.classList.remove("cursor-form"));
    });
  }

  function initButtonShine() {
    document.querySelectorAll(".btn-primary, .dock-btn.quote").forEach((btn) => {
      btn.classList.add("has-shine");
    });
  }

  function initHeroFloaters() {
    const bg = document.querySelector(".hero-bg");
    if (!bg || bg.querySelector(".hero-floater")) return;
    for (let i = 0; i < 6; i++) {
      const f = document.createElement("span");
      f.className = "hero-floater";
      f.style.setProperty("--x", `${10 + i * 14}%`);
      f.style.setProperty("--y", `${18 + ((i * 17) % 60)}%`);
      f.style.setProperty("--d", `${6 + i * 1.4}s`);
      f.style.setProperty("--s", `${8 + (i % 3) * 6}px`);
      f.style.background = ["#3dff7a", "#3ad0ff", "#ffe566", "#ff9a1f", "#1a5cff", "#3dff7a"][i];
      bg.appendChild(f);
    }
    if (!window.gsap || !window.ScrollTrigger) return;
    gsap.to(".hero-floater", {
      y: "random(-40, 40)",
      x: "random(-30, 30)",
      duration: "random(4, 8)",
      repeat: -1,
      yoyo: true,
      ease: "sine.inOut",
      stagger: { each: 0.3, from: "random" },
    });
  }

  function initTitleUnderlines() {
    if (!window.gsap || !window.ScrollTrigger) return;
    document.querySelectorAll(".section-title").forEach((title) => {
      if (title.querySelector(".title-line")) return;
      const line = document.createElement("span");
      line.className = "title-line";
      title.appendChild(line);
      gsap.fromTo(
        line,
        { scaleX: 0 },
        {
          scaleX: 1,
          duration: 0.9,
          ease: "power3.out",
          scrollTrigger: { trigger: title, start: "top 85%" },
        }
      );
    });
  }

  function initDockPulse() {
    const dock = document.querySelector(".dock-btn.quote");
    if (!dock || !window.gsap) return;
    gsap.to(dock, {
      boxShadow: "0 14px 40px rgba(61,255,122,0.55)",
      duration: 1.4,
      yoyo: true,
      repeat: -1,
      ease: "sine.inOut",
    });
  }

  function initLinkLift() {
    if (!window.gsap || !finePointer) return;
    document.querySelectorAll(".nav-links a:not(.nav-cta), .footer a, .seo-chip").forEach((a) => {
      a.addEventListener("pointerenter", () => {
        gsap.to(a, { y: -2, duration: 0.25, ease: "power2.out", overwrite: "auto" });
      });
      a.addEventListener("pointerleave", () => {
        gsap.to(a, { y: 0, duration: 0.35, ease: "power3.out", overwrite: "auto" });
      });
    });
  }

  function initImageZoomHover() {
    if (!finePointer) return;
    document.querySelectorAll(".blog-card img, .post-cover img").forEach((img) => {
      const parent = img.parentElement;
      if (!parent) return;
      parent.addEventListener("pointerenter", () => {
        if (window.gsap) gsap.to(img, { scale: 1.06, duration: 0.7, ease: "power2.out" });
      });
      parent.addEventListener("pointerleave", () => {
        if (window.gsap) gsap.to(img, { scale: 1, duration: 0.8, ease: "power3.out" });
      });
    });
  }

  function initWorkRail() {
    const rail = document.getElementById("work-rail");
    if (!rail || !window.gsap || !window.ScrollTrigger) return;
    const cards = rail.querySelectorAll(".work-card");
    gsap.set(cards, { autoAlpha: 0, y: 40, rotate: 1.5 });
    gsap.to(cards, {
      autoAlpha: 1,
      y: 0,
      rotate: 0,
      duration: 0.85,
      stagger: 0.12,
      ease: "power3.out",
      scrollTrigger: { trigger: rail, start: "top 85%" },
    });

    // Drag-to-scroll feel on desktop
    if (!finePointer) return;
    let isDown = false;
    let startX = 0;
    let scrollLeft = 0;
    rail.addEventListener("pointerdown", (e) => {
      if (e.target.closest("a, button")) return;
      isDown = true;
      rail.classList.add("is-dragging");
      startX = e.pageX - rail.offsetLeft;
      scrollLeft = rail.scrollLeft;
    });
    window.addEventListener("pointerup", () => {
      isDown = false;
      rail.classList.remove("is-dragging");
    });
    rail.addEventListener("pointermove", (e) => {
      if (!isDown) return;
      e.preventDefault();
      const x = e.pageX - rail.offsetLeft;
      rail.scrollLeft = scrollLeft - (x - startX) * 1.15;
    });
  }

  function initManifesto() {
    if (!window.gsap || !window.ScrollTrigger) return;
    const title = document.querySelector(".manifesto-title");
    if (!title) return;
    gsap.from(".manifesto-metrics > div", {
      autoAlpha: 0,
      y: 24,
      stagger: 0.1,
      duration: 0.7,
      ease: "power3.out",
      scrollTrigger: { trigger: ".manifesto-metrics", start: "top 90%" },
    });
  }

  function initPageIntro() {
    if (sessionStorage.getItem("jb-intro") === "1") return;
    const wrap = document.createElement("div");
    wrap.className = "page-intro";
    wrap.setAttribute("aria-hidden", "true");
    wrap.innerHTML =
      '<div class="page-intro-mark">JB Software Solutions</div><div class="page-intro-bar"><span></span></div>';
    document.body.appendChild(wrap);
    const bar = wrap.querySelector(".page-intro-bar > span");
    const mark = wrap.querySelector(".page-intro-mark");
    const tl = gsap.timeline({
      onComplete: () => {
        sessionStorage.setItem("jb-intro", "1");
        wrap.remove();
      },
    });
    tl.from(mark, { autoAlpha: 0, y: 18, duration: 0.45, ease: "power3.out" })
      .to(bar, { width: "100%", duration: 0.7, ease: "power2.inOut" }, "-=0.1")
      .to(wrap, { autoAlpha: 0, duration: 0.45, ease: "power2.inOut" }, "+=0.15");
  }

  function initBento() {
    const bento = document.getElementById("bento");
    if (!bento || !window.gsap || !window.ScrollTrigger) return;
    const tiles = bento.querySelectorAll(".bento-tile");
    gsap.set(tiles, { autoAlpha: 0, y: 36 });
    gsap.to(tiles, {
      autoAlpha: 1,
      y: 0,
      duration: 0.8,
      stagger: 0.08,
      ease: "power3.out",
      scrollTrigger: { trigger: bento, start: "top 82%" },
    });
  }

  function initWorkFilters() {
    const filters = document.querySelectorAll(".work-filter");
    const rail = document.getElementById("work-rail");
    if (!filters.length || !rail) return;
    filters.forEach((btn) => {
      btn.addEventListener("click", () => {
        const key = btn.dataset.filter || "all";
        filters.forEach((b) => {
          b.classList.toggle("is-active", b === btn);
          b.setAttribute("aria-selected", b === btn ? "true" : "false");
        });
        rail.querySelectorAll(".work-card").forEach((card) => {
          const cat = card.dataset.cat || "all";
          const show = key === "all" || cat === "all" || cat === key;
          card.classList.toggle("is-filtered-out", !show);
        });
      });
    });
  }

  function initSectionSpy() {
    const ids = ["work", "capabilities", "services", "pricing-teaser", "market"];
    const present = ids
      .map((id) => document.getElementById(id))
      .filter(Boolean);
    if (present.length < 2) return;

    const spy = document.createElement("nav");
    spy.className = "section-spy";
    spy.setAttribute("aria-label", "Section navigation");
    present.forEach((el) => {
      const a = document.createElement("a");
      a.href = `#${el.id}`;
      a.title = el.id;
      a.dataset.spy = el.id;
      spy.appendChild(a);
    });
    document.body.appendChild(spy);

    const links = [...spy.querySelectorAll("a")];
    const setActive = (id) => {
      links.forEach((a) => a.classList.toggle("is-active", a.dataset.spy === id));
    };

    const pickActive = () => {
      const marker = window.innerHeight * 0.35;
      let current = present[0].id;
      present.forEach((el) => {
        const top = el.getBoundingClientRect().top;
        if (top <= marker) current = el.id;
      });
      // Near page bottom: lock to last section
      const doc = document.documentElement;
      const nearBottom = window.scrollY + window.innerHeight >= doc.scrollHeight - 80;
      if (nearBottom) current = present[present.length - 1].id;
      setActive(current);
    };

    pickActive();
    window.addEventListener("scroll", pickActive, { passive: true });
    window.addEventListener("resize", pickActive);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
