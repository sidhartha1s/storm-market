/* ============================================================================
   The Warning Hour — overlay chrome snippet library (helpers.js)
   COPY the functions you need into the episode's index.html <script> block —
   do not link this file from a composition. Verbatim-consolidated from the
   shipped GSAP timelines (ep6 most-evolved; popIn variant compared against
   ep5/ep2). All of these assume a paused `gsap.timeline()` in scope as `tl`.
   ============================================================================ */

/* ---- Ken Burns helper: every still moves (ep6). Call once per still with its
   timeline offset `at` (seconds) and duration `dur`; from/to scale + x/y in px. ---- */
function kb(sel, at, dur, fromScale, toScale, fromX, toX, fromY, toY) {
  tl.fromTo(sel, { scale: fromScale, x: fromX, y: fromY },
    { scale: toScale, x: toX, y: toY, duration: dur, ease: "none" }, at);
}
// example: kb("#kb-leveebreak", 151.42, 5.54, 1.02, 1.14, 0, -14, 0, -9);

/* ---- card pop-in on the spoken cue (ep6). Cards are track-3 mounted; the hard
   unmount at the end of the section's data-duration window IS the exit — no
   explicit fade-out is needed for these. For a card that must exit mid-window
   (e.g. before the next beat lands), pair this with an explicit
   tl.to(sel, { autoAlpha: 0, y: -12, duration: 0.4, ease: "power2.in" }, exitAt). ---- */
function popIn(sel, at) {
  tl.fromTo(sel, { autoAlpha: 0, y: 16, scale: 1.12 }, { autoAlpha: 1, y: 0, scale: 1, duration: 0.4, ease: "power3.out" }, at);
}
// batch-call pattern (ep6): an array of "selector|atSeconds" strings, split and dispatched:
//   ["#p-src-betsy|80.3","#p-q-washing|140.8", ...].forEach(function(spec) {
//     const parts = spec.split("|");
//     popIn(parts[0], parseFloat(parts[1]));
//   });

/* ---- older popIn variant (ep5/ep2) — pop-ins the whole family of card classes found
   inside a section wrapper at once, rather than one sel per card. Prefer the ep6 single-sel
   popIn above for new work (it's the more-evolved, per-card-controllable version); this
   variant is kept for reference since some cards are still authored this way. ---- */
function popInFamily(sel, at) {
  tl.fromTo(sel + " .popup, " + sel + " .lt, " + sel + " .quotecard, " + sel + " .dispatchlab, " + sel + " .namecard, " + sel + " .srclab, " + sel + " .polaroid",
    { autoAlpha: 0, y: 18 }, { autoAlpha: 1, y: 0, duration: 0.45, ease: "power2.out" }, at);
}

/* ---- date match-cut stamp: slam in (contract vocabulary), slide-fade out at
   window end (ep6). `hold` is the on-screen duration in seconds. ---- */
function stamp(sel, at, hold) {
  tl.fromTo(sel, { scale: 2.6, autoAlpha: 0 }, { scale: 1, autoAlpha: 1, duration: 0.35, ease: "power4.in" }, at);
  tl.to(sel, { autoAlpha: 0, y: -26, duration: 0.25, ease: "power2.in" }, at + hold - 0.25);
}
// example: stamp("#st-d2", 83.08, 3.2);

/* ---- simple staggered reveal for multi-element designed cards (ep6). `y` defaults to 14px. ---- */
function reveal(sel, at, y) {
  tl.fromTo(sel, { autoAlpha: 0, y: (y || 14) }, { autoAlpha: 1, y: 0, duration: 0.5, ease: "power2.out" }, at);
}
// stagger a card's lines: reveal(".cl-head", 488.8); reveal(".cl-1", 489.2); reveal(".cl-2", 490.8);

/* ---- slow drift so a designed card's background never sits static (ep6). ---- */
function drift(sel, at, dur) {
  tl.fromTo(sel, { scale: 1.0, transformOrigin: "center" }, { scale: 1.03, duration: dur, ease: "none" }, at);
}
// example: drift("#c-nocar-dark", 508.2, 5.9);

/* ---- counter roll-up idiom (ep6) — animates a plain-object value and writes it into
   a target element's textContent every tick, formatted with thousands separators.
   Use for "the toll reached N" type reveals timed to the spoken number. ---- */
function counterRollUp(targetElId, toValue, at, dur) {
  const o = { v: 0 };
  tl.to(o, {
    v: toValue, duration: dur || 2.2, ease: "power2.out",
    onUpdate: function () {
      const el = document.getElementById(targetElId);
      if (el) el.textContent = Math.round(o.v).toLocaleString("en-US");
    }
  }, at);
}
// example (ep6, "the 10,000 counts up as the line is spoken"):
//   counterRollUp("rf-count", 10000, 528.2, 2.2);

/* ---- pillarbox blur-fill: for every .contain-wrap, clone its <img> into a blurred
   cover-fit backdrop copy behind the sharp contain-fit original (ep6). Run once before
   building the timeline, not inside it — this mutates the DOM, it isn't animated. ---- */
function wirePillarboxBlurfill() {
  document.querySelectorAll(".contain-wrap").forEach(function (w) {
    const im = w.querySelector("img"); if (!im) return;
    const bg = im.cloneNode(); bg.removeAttribute("id"); bg.className = "blurfill";
    w.insertBefore(bg, im);
  });
}

/* ---- log-space camera zoom: a plain linear scale tween on a push/pull-out over ~1.5x reads
   as decelerating even at ease:"none" — scale is exponential, not additive, so a 1->4x move
   is already at scale 2 by 50% of the TIME but that's only 33% of the way through the visual
   "zoom" (log(2)/log(4)); the eye reads a fast start, a long slow crawl. Interpolate in LOG
   space instead so perceived zoom speed is constant. Use for any camera push/pull-out over
   ~1.5x; a smaller move is fine as a plain fromTo (mg-quickref "Motion and exits"). ---- */
function logLerpScale(fromScale, toScale, t) {
  return Math.exp(Math.log(fromScale) + (Math.log(toScale) - Math.log(fromScale)) * t);
}
function logZoom(sel, at, dur, fromScale, toScale, ease) {
  const o = { t: 0 };
  tl.fromTo(o, { t: 0 }, {
    t: 1, duration: dur, ease: ease || "none",
    onUpdate: function () { gsap.set(sel, { scale: logLerpScale(fromScale, toScale, o.t) }); }
  }, at);
}
// example: logZoom("#cam-push", 120.4, 3.2, 1, 4, "power1.inOut");
if (typeof module !== "undefined") module.exports = { logLerpScale }; // node self-check only; harmless in a <script> tag
