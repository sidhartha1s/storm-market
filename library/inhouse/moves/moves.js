/* ============================================================================
   The Warning Hour: move library (moves.js)
   Motion building blocks extracted from the showcase MG g-tanker-throw.html (demo-mg-showcase,
   GSAP 3.14.2). The host page loads gsap + DrawSVGPlugin + CustomEase + SplitText and calls
   gsap.registerPlugin(DrawSVGPlugin, CustomEase, SplitText) before any move runs.
   Contract: move(tl, targets, at, opts) adds tweens to ONE paused timeline and returns handles.
   Deterministic: seeded mulberry32 only; no Math.random, Date or requestAnimationFrame.
   Per-frame work goes through onFrame(): one onUpdate per timeline, fired after every child tween
   has rendered, so any seek order gives the same frame. Drive the timeline with tl.time() or
   tl.progress(); tl.seek() suppresses onUpdate by default.
   GATE: beat_density.py counts only literal tl.<call>(..., <number>) in the composition source.
   Positions inside moves are at-relative, so the gate cannot see them (README "Gates").
   ============================================================================ */
(function (root) {
  'use strict';
  const G = () => root.gsap;
  const SVGNS = 'http://www.w3.org/2000/svg';

  /* mulberry32: same generator as the showcase. rng(seed)() -> [0, 1). */
  function rng(seed) {
    let s = seed | 0;
    return function () {
      s = s + 0x6D2B79F5 | 0;
      let t = Math.imul(s ^ s >>> 15, 1 | s);
      t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t;
      return ((t ^ t >>> 14) >>> 0) / 4294967296;
    };
  }

  function mk(tag, parent, css, svg) {
    const el = svg ? root.document.createElementNS(SVGNS, tag) : root.document.createElement(tag);
    if (css) el.style.cssText = css;
    parent.appendChild(el);
    return el;
  }

  /* onFrame: the single per-frame hub. Installs tl's onUpdate once; every move that writes per
     frame registers here, in call order (camera first, then bodies, then finish). Throws if the
     timeline already has a foreign onUpdate, so two per-frame writers can never fight.
     renderNow(tl) paints frame tl.time() once at build end, as the showcase does. */
  const HUBS = new WeakMap();
  function onFrame(tl, fn) {
    let list = HUBS.get(tl);
    if (!list) {
      if (tl.eventCallback('onUpdate')) throw new Error('moves.onFrame: timeline already has an onUpdate; route per-frame work through MOVES.onFrame');
      list = [];
      HUBS.set(tl, list);
      tl.eventCallback('onUpdate', function () { const t = tl.time(); for (const f of list) f(t); });
    }
    list.push(fn);
  }
  function renderNow(tl) { const t = tl.time(); for (const f of HUBS.get(tl) || []) f(t); }

  /* Named CustomEases from the showcase: 'drag' (wind-carried flight), 'slam' (popfig hit). */
  const EASES = { drag: 'M0,0 C0.16,0.3 0.4,0.56 0.6,0.72 0.78,0.86 0.9,0.96 1,1', slam: 'M0,0 C0.5,0 0.7,0.4 0.82,0.7 0.9,0.9 0.96,1 1,1' };
  const made = new Set();
  function ease(name) {
    if (!EASES[name]) return name;
    if (!root.CustomEase) throw new Error('moves: CustomEase is not loaded; the host must load and register it');
    if (!made.has(name)) { root.CustomEase.create('mv-' + name, EASES[name]); made.add(name); }
    return 'mv-' + name;
  }

  /* Text must never ride the camera. Throws when a text element sits inside the rig's shake root. */
  function assertHud(rig, el, who) {
    if (rig && rig.shakeEl.contains(el)) throw new Error('moves.' + who + ': text is inside the camera rig and would ride shake and drift; mount it on the HUD layer');
  }

  /* cameraRig: one camera proxy {fx, fy, z} (world point at screen centre, zoom) drives every depth layer.
     els: { shake: element wrapping all world layers, layers: [[el, depth], ...] } depth 0.4 bg, 1 world, 1.4 fg.
     opts: { fx, fy, z, w: 1920, h: 1080, drift: 1 (handheld sum-of-sines scale, 0 locks it), roll: 0.15 deg }.
     Returns rig { cam, sh, shakeEl }; animate it with camMove and shake. HUD text stays OUTSIDE els.shake.
     Gate: adds no tweens; its per-frame write lives in the onFrame hub (continuous drift, never idle). */
  function cameraRig(tl, els, o) {
    o = Object.assign({ fx: 960, fy: 540, z: 1, w: 1920, h: 1080, drift: 1, roll: 0.15 }, o);
    const cx = o.w / 2, cy = o.h / 2;
    const rig = { cam: { fx: o.fx, fy: o.fy, z: o.z }, sh: { x: 0, y: 0, r: 0 }, shakeEl: els.shake };
    for (const [el] of els.layers) el.style.transformOrigin = '0 0';
    onFrame(tl, function (t) {
      const c = rig.cam, d = o.drift;
      const dx = d * (4 * Math.sin(0.9 * t) + 2.2 * Math.sin(2.3 * t + 1.2));
      const dy = d * (3 * Math.sin(1.1 * t + 0.5) + 1.6 * Math.sin(2.9 * t + 2.1));
      for (const [el, p] of els.layers) {
        const z = 1 + (c.z - 1) * p, fx = cx + (c.fx - cx) * p, fy = cy + (c.fy - cy) * p;
        el.style.transform = 'translate(' + (cx - fx * z + dx * p) + 'px,' + (cy - fy * z + dy * p) + 'px) scale(' + z + ')';
      }
      els.shake.style.transform = 'translate(' + rig.sh.x + 'px,' + rig.sh.y + 'px) rotate(' + (rig.sh.r + o.roll * d * Math.sin(0.7 * t)) + 'deg)';
    });
    return rig;
  }

  /* camMove: push-in (z up) or pull-back (z down) and reframe, one literal tween on the camera proxy.
     opts: { fx, fy, z, duration: 1.7, ease: 'power2.out' }. A long sine.inOut move is the cheapest
     way to keep a hold alive. Gate: one tl.to on a proxy; never overlap two camMoves in time. */
  function camMove(tl, rig, at, o) {
    o = Object.assign({ duration: 1.7, ease: 'power2.out' }, o);
    tl.to(rig.cam, { fx: o.fx, fy: o.fy, z: o.z, duration: o.duration, ease: o.ease }, at);
  }

  /* shake: seeded, decaying impulse on the shake root (translate + a little roll).
     opts: { amp: 24 px, hits: 9, decay: 0.7 per hit, duration: 0.6, seed: 7, roll: 0.05 deg per px }.
     Small amp (4 to 8) for thunder or a derail, 20 to 30 for a landing. Ends exactly at rest.
     Gate: one keyframed tl.to on a proxy; impulses must not overlap (the later one owns sh). */
  function shake(tl, rig, at, o) {
    o = Object.assign({ amp: 24, hits: 9, decay: 0.7, duration: 0.6, seed: 7, roll: 0.05 }, o);
    const R = rng(o.seed), kf = [];
    for (let i = 0; i < o.hits; i++) {
      const a = o.amp * Math.pow(o.decay, i);
      kf.push({ x: (R() - 0.5) * 2 * a, y: (R() - 0.5) * 2 * a, r: (R() - 0.5) * a * o.roll });
    }
    kf.push({ x: 0, y: 0, r: 0 });
    tl.to(rig.sh, { keyframes: kf, duration: o.duration, ease: 'none' }, at);
  }

  /* arcThrow: a body on a true parabola (x linear in u, y quadratic) with tumble, anticipation squash
     before `at`, landing squash + elastic spring and settle, speed-driven directional blur, ghost trail.
     els: { pos (translate, carries filter url(#blur)), rot, sq (CSS transform-origin at the base), art
     (cloned for ghosts), ghostWrap, blur (feGaussianBlur), trailClip (clip rect for trail paths) }.
     opts: { x0, y0, x1, y1, apex px, duration, ease: 'drag', r0, spin deg, ox, oy (body centre), ghosts: 3 }.
     Returns { fly (driver {u}), st (tween st.r for rocking), pose(u), land }. Gate: literal tl.to calls. */
  function arcThrow(tl, els, at, o) {
    o = Object.assign({ apex: 420, duration: 1.65, ease: 'drag', r0: 0, spin: 352, settle: 10, tilt: -12,
      ox: 75, oy: 39, ghosts: 3, gap: 0.028, blur: 0.005, blurMax: 9 }, o);
    const D = o.duration, ez = ease(o.ease), E = G().parseEase(ez);
    const fly = { u: 0 }, st = { r: 0, lift: 0, set: 0 };
    const pose = (u) => ({ x: o.x0 + (o.x1 - o.x0) * u, y: o.y0 + (o.y1 - o.y0) * u - 4 * o.apex * u * (1 - u) });
    const uAt = (t) => E(Math.min(1, Math.max(0, (t - at) / D)));
    /* anticipation: the wind grabs it */
    tl.to(st, { lift: -10, r: o.tilt, duration: 0.3, ease: 'power2.out' }, at - 0.32);
    tl.to(els.sq, { scaleY: 0.9, scaleX: 1.05, duration: 0.18, ease: 'power2.in' }, at - 0.18);
    tl.to(els.sq, { scaleY: 1.06, scaleX: 0.96, duration: 0.14, ease: 'power2.out' }, at);
    tl.to(els.sq, { scaleY: 1, scaleX: 1, duration: 0.4, ease: 'sine.out' }, at + 0.14);
    /* flight */
    tl.to(fly, { u: 1, duration: D, ease: ez }, at);
    tl.to(st, { lift: 0, duration: 0.3 }, at);
    /* landing: squash, spring, settle */
    tl.to(els.sq, { scaleY: 0.72, scaleX: 1.16, duration: 0.07, ease: 'power2.out' }, at + D);
    tl.to(els.sq, { scaleY: 1, scaleX: 1, duration: 0.7, ease: 'elastic.out(1.1,0.35)' }, at + D + 0.07);
    tl.to(st, { set: 1, duration: 0.6, ease: 'back.out(3)' }, at + D);

    const ghosts = [];
    if (els.ghostWrap && els.art) for (let i = 0; i < o.ghosts; i++) {
      const g = els.art.cloneNode(true);
      g.removeAttribute('id');
      g.querySelectorAll('[id]').forEach((n) => n.removeAttribute('id'));
      g.style.cssText = 'position:absolute;left:0;top:0;opacity:0;transform-origin:' + o.ox + 'px ' + o.oy + 'px';
      els.ghostWrap.appendChild(g);
      ghosts.push(g);
    }
    onFrame(tl, function (t) {
      const u = fly.u, P = pose(u);
      els.pos.style.transform = 'translate(' + (P.x - o.ox) + 'px,' + (P.y - o.oy + st.lift) + 'px)';
      els.rot.style.transform = 'rotate(' + (o.r0 + st.r + o.spin * u + o.settle * st.set) + 'deg)';
      if (els.trailClip) els.trailClip.setAttribute('width', String(P.x));
      const on = u > 0.02 && u < 0.985 ? 1 : 0;
      ghosts.forEach((g, i) => {
        const ug = Math.max(0, u - o.gap * (i + 1)), Q = pose(ug);
        g.style.opacity = String(on * (0.3 - i * 0.09));
        g.style.transform = 'translate(' + (Q.x - o.ox) + 'px,' + (Q.y - o.oy) + 'px) rotate(' + (o.r0 + st.r + o.spin * ug) + 'deg)';
      });
      if (els.blur) { /* blur follows screen-axis speed, sampled from the same ease: seek-safe */
        const h = 1 / 60, A = pose(uAt(t - h)), B = pose(uAt(t + h));
        const sx = Math.min(o.blurMax, Math.abs(B.x - A.x) / (2 * h) * o.blur), sy = Math.min(o.blurMax, Math.abs(B.y - A.y) / (2 * h) * o.blur);
        els.blur.setAttribute('stdDeviation', sx.toFixed(2) + ' ' + sy.toFixed(2));
      }
    });
    return { fly, st, pose, land: at + D };
  }

  /* arcPath: SVG d for the same parabola, for a dashed trail clipped by els.trailClip. */
  function arcPath(o) {
    const apex = o.apex == null ? 420 : o.apex;
    return 'M' + o.x0 + ',' + o.y0 + ' Q' + (o.x0 + o.x1) / 2 + ',' + ((o.y0 + o.y1) / 2 - 2 * apex) + ' ' + o.x1 + ',' + o.y1;
  }

  /* counter: HUD number tied to a driver proxy (e.g. arcThrow's fly.u), written once per frame.
     el: the counter block; opts: { driver, key: 'u', to, format(v), final (exact text at u >= 1), text
     (child that holds digits), punchAt (landing punch), rig (asserts el is not in the camera) }.
     Gate: literal set/fromTo for the reveal, set + to for the punch; text write is per frame. */
  function counter(tl, el, at, o) {
    o = Object.assign({ key: 'u', to: 100, format: (v) => String(Math.floor(v)), text: el, punchAt: null, rig: null }, o);
    assertHud(o.rig, el, 'counter');
    const final = o.final == null ? o.format(o.to) : o.final;
    tl.set(el, { autoAlpha: 0 }, 0);
    tl.fromTo(el, { autoAlpha: 0, y: 20 }, { autoAlpha: 1, y: 0, duration: 0.3, ease: 'power3.out' }, at);
    if (o.punchAt != null) {
      tl.set(el, { scale: 1.18 }, o.punchAt);
      tl.to(el, { scale: 1, duration: 0.5, ease: 'elastic.out(1,0.4)' }, o.punchAt);
    }
    onFrame(tl, function () { const u = o.driver[o.key]; o.text.textContent = u >= 1 ? final : o.format(o.to * u); });
  }

  /* slamFig: red popfig slams in (scale 1.9 to 1, 'slam' ease), holds, slides up and out.
     opts: { hold: 1.0, scale: 1.9, rig }. Returns the time the exit ends.
     Gate: fromTo reveal, autoAlpha:0 exit; never tl.from. */
  function slamFig(tl, el, at, o) {
    o = Object.assign({ hold: 1.0, scale: 1.9, rig: null }, o);
    assertHud(o.rig, el, 'slamFig');
    tl.set(el, { autoAlpha: 0 }, 0);
    tl.fromTo(el, { autoAlpha: 0, scale: o.scale }, { autoAlpha: 1, scale: 1, duration: 0.35, ease: ease('slam') }, at);
    tl.to(el, { autoAlpha: 0, y: -30, duration: 0.3, ease: 'power2.in' }, at + 0.35 + o.hold);
    return at + 0.65 + o.hold;
  }

  /* dustPuff: seeded soft dust clouds that bloom out and up from a ground point, then thin away.
     wrap: world-layer container; opts: { x, y (ground), n: 34, seed: 475, spread: 120, reach: 420,
     rise: 150, color: '150,140,125' }. Gate: per puff one set + two literal to calls, exits autoAlpha:0. */
  function dustPuff(tl, wrap, at, o) {
    o = Object.assign({ n: 34, seed: 475, spread: 120, reach: 420, rise: 150, color: '150,140,125' }, o);
    const R = rng(o.seed);
    for (let i = 0; i < o.n; i++) {
      const d = mk('div', wrap, 'position:absolute;left:0;top:0;width:90px;height:90px;margin:-45px 0 0 -45px;border-radius:50%;opacity:0;' +
        'background:radial-gradient(circle, rgba(' + o.color + ',0.55), rgba(' + o.color + ',0.18) 45%, rgba(0,0,0,0) 70%)');
      const x0 = o.x + (R() - 0.5) * o.spread, dx = (R() - 0.25) * o.reach, dy = -(30 + R() * o.rise), s = 0.8 + R() * 2.2, dur = 1.6 + R() * 1.8;
      tl.set(d, { x: x0, y: o.y, scale: 0.3, autoAlpha: 0.75 + R() * 0.25 }, at);
      tl.to(d, { x: x0 + dx, y: o.y + dy, scale: s, duration: dur, ease: 'power3.out' }, at);
      tl.to(d, { autoAlpha: 0, duration: dur * 0.8, ease: 'power1.in' }, at + dur * 0.35);
    }
  }

  /* debrisBurst: seeded chips kicked up on a ballistic hop (rise power2.out, fall power2.in) with spin.
     opts: { x, y (ground), n: 14, seed: 476, reach: 360, color: '#6d7a86' }.
     Gate: literal set/to calls per chip, exit autoAlpha:0 after they come to rest. */
  function debrisBurst(tl, wrap, at, o) {
    o = Object.assign({ n: 14, seed: 476, reach: 360, color: '#6d7a86' }, o);
    const R = rng(o.seed);
    for (let i = 0; i < o.n; i++) {
      const c = mk('div', wrap, 'position:absolute;left:0;top:0;width:7px;height:4px;opacity:0;background:' + o.color);
      const dx = (R() - 0.3) * o.reach, up = 60 + R() * 150, dur = 0.55 + R() * 0.45;
      tl.set(c, { x: o.x + (R() - 0.5) * 60, y: o.y - 4, autoAlpha: 1, rotation: 0 }, at);
      tl.to(c, { x: '+=' + dx, rotation: (R() - 0.5) * 900, duration: dur, ease: 'none' }, at);
      tl.to(c, { y: o.y - 4 - up, duration: dur * 0.45, ease: 'power2.out' }, at);
      tl.to(c, { y: o.y + 2, duration: dur * 0.55, ease: 'power2.in' }, at + dur * 0.45);
      tl.to(c, { autoAlpha: 0, duration: 0.6 }, at + dur + 0.6);
    }
  }

  /* impactRing: a flat ground ellipse (SVG <ellipse>) that snaps on small and expands out to nothing.
     opts: { rx: 260, ry: 22, duration: 0.9 }. Gate: set + to, exits autoAlpha:0. */
  function impactRing(tl, ring, at, o) {
    o = Object.assign({ rx: 260, ry: 22, duration: 0.9 }, o);
    tl.set(ring, { autoAlpha: 0 }, 0);
    tl.set(ring, { autoAlpha: 0.9, attr: { rx: 20, ry: 3 } }, at);
    tl.to(ring, { autoAlpha: 0, attr: { rx: o.rx, ry: o.ry }, duration: o.duration, ease: 'power2.out' }, at);
  }

  /* rain: seeded slanted streaks that wrap around the frame, positions a pure function of t.
     layer: full-frame container (inside the shake root, outside parallax layers); opts: { n: 70, seed,
     w: 2200, h: 1240, vmin: 1100, vmax: 1800 px/s, slant: 0.36 (dx per dy), len: 64, alpha: 0.16 }.
     Gate: no tweens, continuous per-frame motion for the whole window. */
  function rain(tl, layer, o) {
    o = Object.assign({ n: 70, seed: 20250620, w: 2200, h: 1240, vmin: 1100, vmax: 1800, slant: 0.36, len: 64, alpha: 0.16 }, o);
    const R = rng(o.seed), deg = -Math.atan(o.slant) * 180 / Math.PI, drops = [];
    for (let i = 0; i < o.n; i++) {
      const el = mk('div', layer, 'position:absolute;left:0;top:0;width:2px;height:' + o.len + 'px;border-radius:1px;' +
        'background:linear-gradient(180deg, rgba(190,208,226,0), rgba(190,208,226,' + o.alpha + '))');
      const d = { el, x: R() * o.w, y: R() * o.h, v: o.vmin + R() * (o.vmax - o.vmin) };
      el.style.opacity = String(0.35 + R() * 0.65);
      drops.push(d);
    }
    onFrame(tl, function (t) {
      for (const d of drops) {
        const yy = ((d.y + t * d.v) % o.h) - 70, xx = ((d.x + t * d.v * o.slant) % o.w) - 140;
        d.el.style.transform = 'translate(' + xx + 'px,' + yy + 'px) rotate(' + deg + 'deg)';
      }
    });
  }

  /* lightning: full-frame sky flash; flickers on and off, ends on a peak, decays.
     flash: overlay placed BEHIND the world layers (backlights the scene, never washes text).
     opts: { flickers: 2, decay: 0.3 }. Gate: fromTo with repeat (gate counts repeats), exit autoAlpha:0. */
  function lightning(tl, flash, at, o) {
    o = Object.assign({ flickers: 2, decay: 0.3 }, o);
    tl.set(flash, { autoAlpha: 0 }, 0);
    tl.fromTo(flash, { autoAlpha: 0 }, { autoAlpha: 1, duration: 0.05, ease: 'none', yoyo: true, repeat: o.flickers * 2 - 2 }, at);
    tl.to(flash, { autoAlpha: 0, duration: o.decay, ease: 'power2.out' }, at + (o.flickers * 2 - 1) * 0.05);
  }

  /* measureDraw: DrawSVG a ruler, ticks, leader or threshold line from 0% to 100%, staggered, then
     fade in its labels. paths: [<path|line>]; opts: { duration: 0.7, stagger: 0.1, ease: 'power2.inOut',
     labels: element or null, labelDelay: 0.4 }. Gate: set at literal 0, then tl.to per path. */
  function measureDraw(tl, paths, at, o) {
    o = Object.assign({ duration: 0.7, stagger: 0.1, ease: 'power2.inOut', labels: null, labelDelay: 0.4 }, o);
    tl.set(paths, { drawSVG: '0%' }, 0);
    paths.forEach((p, i) => tl.to(p, { drawSVG: '100%', duration: o.duration, ease: o.ease }, at + i * o.stagger));
    if (o.labels) {
      tl.set(o.labels, { autoAlpha: 0 }, 0);
      tl.fromTo(o.labels, { autoAlpha: 0, y: 8 }, { autoAlpha: 1, y: 0, duration: 0.4 }, at + o.labelDelay);
    }
  }

  /* bandCompare: equal reference bands laid end to end (1x, 2x, 3x ...) growing left to right, each
     labelled. g: SVG <g> in the world layer; opts: { x0, y, unit px, count, h: 12, gap: 4, labelY,
     color: '#d8121f', labelColor: '#ff5a5f', stagger: 0.18 }. The caller picks count; the band total may
     overshoot the measured mark, so the copy must say "nearly". Gate: set at 0, tl.to / fromTo per band. */
  function bandCompare(tl, g, at, o) {
    o = Object.assign({ h: 12, gap: 4, color: '#d8121f', labelColor: '#ff5a5f', stagger: 0.18, font: 'AbrilFig,Georgia', size: 26 }, o);
    const labelY = o.labelY == null ? o.y + 44 : o.labelY, rects = [], labels = [];
    for (let i = 0; i < o.count; i++) {
      const r = mk('rect', g, null, true);
      r.setAttribute('x', o.x0 + i * o.unit + o.gap / 2); r.setAttribute('y', o.y);
      r.setAttribute('width', o.unit - o.gap); r.setAttribute('height', o.h); r.setAttribute('fill', o.color);
      const t = mk('text', g, null, true);
      t.setAttribute('x', o.x0 + (i + 0.5) * o.unit); t.setAttribute('y', labelY); t.setAttribute('text-anchor', 'middle');
      t.setAttribute('font-family', o.font); t.setAttribute('font-size', o.size); t.setAttribute('fill', o.labelColor);
      t.textContent = (i + 1) + '×';
      rects.push(r); labels.push(t);
    }
    tl.set(rects, { scaleX: 0, transformOrigin: '0% 50%' }, 0);
    tl.set(labels, { autoAlpha: 0 }, 0);
    rects.forEach((r, i) => tl.to(r, { scaleX: 1, duration: 0.3, ease: 'power2.out' }, at + i * o.stagger));
    labels.forEach((t, i) => tl.fromTo(t, { autoAlpha: 0, y: 8 }, { autoAlpha: 1, y: 0, duration: 0.25 }, at + 0.1 + i * o.stagger));
    return { rects, labels };
  }

  /* kineticText: SplitText word stagger (rise + flip up from rotationX -70), with a settle-hold guarantee:
     throws unless every word has settled at least minHold seconds before exitAt. Give el CSS perspective.
     opts: { exitAt (required), minHold: 1.0, stagger: 0.12, duration: 0.5, ease: 'back.out(1.6)', rig }.
     Returns { words, settled }. Gate: initial set at literal 0, one staggered tl.to; never tl.from. */
  function kineticText(tl, el, at, o) {
    o = Object.assign({ minHold: 1.0, stagger: 0.12, duration: 0.5, ease: 'back.out(1.6)', rig: null }, o);
    if (o.exitAt == null) throw new Error('moves.kineticText: exitAt is required (the settle-hold guarantee needs it)');
    assertHud(o.rig, el, 'kineticText');
    const words = new root.SplitText(el, { type: 'words' }).words;
    const settled = at + (words.length - 1) * o.stagger + o.duration;
    if (o.exitAt - settled < o.minHold) throw new Error('moves.kineticText: words settle at ' + settled.toFixed(2) + ' s but exit at ' + o.exitAt + ' s; hold is under ' + o.minHold + ' s');
    tl.set(el, { autoAlpha: 1 }, 0);
    tl.set(words, { autoAlpha: 0, y: 46, rotationX: -70, transformOrigin: '50% 100%' }, 0);
    tl.to(words, { autoAlpha: 1, y: 0, rotationX: 0, duration: o.duration, stagger: o.stagger, ease: o.ease }, at);
    return { words, settled };
  }

  /* finishLayer: seeded film grain (N canvas tiles cycled at fps), vignette, depth-of-field blur per layer.
     els: { grain: <canvas> (any size, CSS-stretched), vig: full-frame div, dof: [[layerEl, px], ...] }.
     opts: { seed: 99, tiles: 6, fps: 24, amount: 120, opacity: 0.14, vignette: 0.62 }. Stack grain and
     vignette ABOVE the world and BELOW the HUD so small text is never noised. Gate: no tweens; grain per frame. */
  function finishLayer(tl, els, o) {
    o = Object.assign({ seed: 99, tiles: 6, fps: 24, amount: 120, opacity: 0.14, vignette: 0.62 }, o);
    for (const [el, px] of els.dof || []) el.style.filter = 'blur(' + px + 'px)';
    if (els.vig) els.vig.style.background = 'radial-gradient(ellipse 75% 70% at 50% 50%, rgba(0,0,0,0) 55%, rgba(0,0,0,' + o.vignette + ') 100%)';
    if (!els.grain) return;
    const cv = els.grain, ctx = cv.getContext('2d'), R = rng(o.seed), tiles = [];
    cv.style.mixBlendMode = 'overlay';
    cv.style.opacity = String(o.opacity);
    for (let k = 0; k < o.tiles; k++) {
      const im = ctx.createImageData(cv.width, cv.height), a = im.data;
      for (let p = 0; p < a.length; p += 4) { const v = 128 + (R() + R() - 1) * o.amount; a[p] = a[p + 1] = a[p + 2] = v; a[p + 3] = 255; }
      tiles.push(im);
    }
    let last = -1;
    onFrame(tl, function (t) {
      const f = Math.floor(t * o.fps) % tiles.length;
      if (f !== last) { ctx.putImageData(tiles[f], 0, 0); last = f; }
    });
  }

  /* cleanExit: HUD slides up and out (autoAlpha:0, staggered), optional camera push past the subject,
     optional fade to black. Also usable mid-composition to retire one HUD block (hud only).
     els: { hud: [el], rig, black }; opts: { dy: -60, push: {fx, fy, z} }. Returns the end time.
     Gate: literal tl.to exits with autoAlpha:0; never a hard cut or opacity-only vanish. */
  function cleanExit(tl, els, at, o) {
    o = Object.assign({ dy: -60, push: null }, o);
    let end = at + 0.45 + 0.05 * Math.max(0, els.hud.length - 1);
    tl.to(els.hud, { y: '+=' + o.dy, autoAlpha: 0, duration: 0.45, ease: 'power3.in', stagger: 0.05 }, at);
    if (els.rig && o.push) { tl.to(els.rig.cam, { fx: o.push.fx, fy: o.push.fy, z: o.push.z, duration: 0.7, ease: 'power3.in' }, at); end = Math.max(end, at + 0.7); }
    if (els.black) {
      tl.set(els.black, { autoAlpha: 0 }, 0);
      tl.to(els.black, { autoAlpha: 1, duration: 0.5, ease: 'power2.in' }, at + 0.18);
      end = Math.max(end, at + 0.68);
    }
    return end;
  }

  const MOVES = { rng, onFrame, renderNow, ease, cameraRig, camMove, shake, arcThrow, arcPath, counter, slamFig,
    dustPuff, debrisBurst, impactRing, rain, lightning, measureDraw, bandCompare, kineticText, finishLayer, cleanExit };
  root.MOVES = MOVES;
  if (typeof module === 'object' && module.exports) module.exports = MOVES;
})(typeof window !== 'undefined' ? window : globalThis);
