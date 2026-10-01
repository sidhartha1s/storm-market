// grain.js — unified film layer: seeded grain canvas + vignette + dust specks.
// PROVEN implementation from demo-joplin-90 (2026-07-22): timeline-driven, deterministic,
// GSAP-based (rAF/WAAPI versions drift under the seek-by-frame capture engine — don't revert).
//
// Usage inside a composition (after the GSAP timeline `tl` exists):
//   <div id="vignette"></div><canvas id="grain" width="480" height="270"></canvas>  (untimed, last in root)
//   CSS: #vignette{position:absolute;inset:0;z-index:90;pointer-events:none;
//          background:radial-gradient(ellipse at 50% 50%,transparent 52%,rgba(0,0,0,.5) 100%)}
//        #grain{position:absolute;inset:0;width:100%;height:100%;z-index:91;
//          pointer-events:none;opacity:.11;mix-blend-mode:overlay}
//        .dust{position:absolute;z-index:92;pointer-events:none;border-radius:50%;
//          background:rgba(255,255,255,.32);filter:blur(1.2px)}
//   JS:  filmLayer(tl, DUR);   // DUR = composition duration in seconds

function filmLayer(tl, DUR, root = document.getElementById("root")) {
  const gcv = document.getElementById("grain"), gctx = gcv.getContext("2d");
  const gimg = gctx.createImageData(gcv.width, gcv.height);
  function mulberry32(a) {
    return function () {
      a |= 0; a = (a + 0x6D2B79F5) | 0;
      let t = Math.imul(a ^ (a >>> 15), 1 | a);
      t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }
  let lastSeed = -1;
  function paintGrain(timeSec) {
    const seed = Math.floor(timeSec * 12); // reseed ~12x/s
    if (seed === lastSeed) return;
    lastSeed = seed;
    const rnd = mulberry32(seed + 7), d = gimg.data;
    for (let i = 0; i < d.length; i += 4) {
      const v = 128 + (rnd() - 0.5) * 210;
      d[i] = d[i + 1] = d[i + 2] = v; d[i + 3] = 255;
    }
    gctx.putImageData(gimg, 0, 0);
  }
  const gdrv = { t: 0 };
  tl.to(gdrv, { t: DUR, duration: DUR, ease: "none", onUpdate: () => paintGrain(gdrv.t) }, 0);

  for (let i = 0; i < 6; i++) {
    const s = document.createElement("div");
    s.className = "dust";
    const size = 2 + (i % 3) * 2;
    s.style.width = s.style.height = size + "px";
    s.style.left = ((i * 137) % 90 + 4) + "%";
    s.style.top = ((i * 61) % 80 + 5) + "%";
    root.appendChild(s);
    const cycle = 9 + i * 1.7;
    tl.fromTo(s, { x: 0, y: 0, opacity: 0 },
      { x: 40 + i * 13, y: 120 + i * 29, opacity: 0.5, duration: cycle, ease: "none",
        repeat: Math.max(0, Math.floor(DUR / cycle) - 1), yoyo: true }, 0);
  }
}
