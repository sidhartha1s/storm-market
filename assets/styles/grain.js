// grain.js — unified film layer: animated grain + vignette + drifting dust specks.
// JS/WAAPI only (CSS @keyframes would disable hyperframes fast-capture).
// Usage: <script src="grain.js"></script> then grainLayer(rootEl, {opacity:0.10, dust:6})
function grainLayer(root, opts = {}) {
  const opacity = opts.opacity ?? 0.10;
  const dustCount = opts.dust ?? 6;

  // vignette
  const vig = document.createElement("div");
  Object.assign(vig.style, {
    position: "absolute", inset: "0", pointerEvents: "none", zIndex: 90,
    background: "radial-gradient(ellipse at 50% 50%, transparent 55%, rgba(0,0,0,0.42) 100%)",
  });
  root.appendChild(vig);

  // grain canvas — noise reseeded ~15x/s, seeded from the timeline clock so a frame
  // renders identically wherever it is captured (chunk workers seek independently)
  const cv = document.createElement("canvas");
  cv.width = 480; cv.height = 270; // upscaled by CSS => coarse filmic grain
  Object.assign(cv.style, {
    position: "absolute", inset: "0", width: "100%", height: "100%",
    pointerEvents: "none", zIndex: 91, opacity: String(opacity), mixBlendMode: "overlay",
  });
  root.appendChild(cv);
  const ctx = cv.getContext("2d");
  const img = ctx.createImageData(cv.width, cv.height);
  function mulberry32(a) {
    return function () {
      a |= 0; a = (a + 0x6D2B79F5) | 0;
      let t = Math.imul(a ^ (a >>> 15), 1 | a);
      t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }
  let lastSeed = -1;
  function paint() {
    const t = document.timeline.currentTime || 0;
    const seed = Math.floor(t / 66); // ~15fps reseed
    if (seed !== lastSeed) {
      lastSeed = seed;
      const rnd = mulberry32(seed);
      const d = img.data;
      for (let i = 0; i < d.length; i += 4) {
        const v = 128 + (rnd() - 0.5) * 220;
        d[i] = d[i + 1] = d[i + 2] = v; d[i + 3] = 255;
      }
      ctx.putImageData(img, 0, 0);
    }
    requestAnimationFrame(paint);
  }
  requestAnimationFrame(paint);

  // dust specks — soft blurred dots drifting down-right, WAAPI
  for (let i = 0; i < dustCount; i++) {
    const s = document.createElement("div");
    const size = 2 + (i % 3) * 2;
    Object.assign(s.style, {
      position: "absolute", zIndex: 92, pointerEvents: "none",
      width: size + "px", height: size + "px", borderRadius: "50%",
      background: "rgba(255,255,255,0.35)", filter: "blur(1px)",
      left: (i * 137) % 100 + "%", top: (i * 61) % 100 + "%",
    });
    root.appendChild(s);
    s.animate(
      [
        { transform: "translate(0,0)", opacity: 0 },
        { opacity: 0.5, offset: 0.2 },
        { transform: `translate(${40 + i * 13}px, ${120 + i * 29}px)`, opacity: 0 },
      ],
      { duration: 9000 + i * 1700, iterations: Infinity, delay: i * 800, easing: "linear" }
    );
  }
}
