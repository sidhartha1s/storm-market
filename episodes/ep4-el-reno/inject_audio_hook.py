#!/usr/bin/env python3
"""One-shot injector: hook picture, cards (track 3), music/SFX beds, grade CSS,
master volume/card timeline. Idempotent-guarded: refuses if marker already present."""
import io, sys

P = 'index.html'
h = io.open(P, encoding='utf-8').read()
if 'EP4-AUDIO-INJECT' in h:
    sys.exit('already injected')

# ---- 1. a7-s3 radar chronological order fix (0000 -> 0014 -> 0018) ----
h = h.replace('id="a7-s3-ktlx-ref-0014utc-1914cdt-jun1-1" data-start="1901.91"',
              'id="a7-s3-ktlx-ref-0000utc-1900cdt-jun1-1" data-start="1901.91"')
h = h.replace('id="i-a7-s3-ktlx-ref-0014utc-1914cdt-jun1-1" src="media/radar/ktlx-ref-0014utc-1914cdt-jun1.png"',
              'id="i-a7-s3-ktlx-ref-0000utc-1900cdt-jun1-1" src="media/radar/ktlx-ref-0000utc-1900cdt-jun1.png"')
h = h.replace('id="a7-s3-ktlx-ref-0018utc-1918cdt-jun1-1" data-start="1911.91"',
              'id="a7-s3-ktlx-ref-0014utc-1914cdt-jun1-1" data-start="1911.91"')
h = h.replace('id="i-a7-s3-ktlx-ref-0018utc-1918cdt-jun1-1" src="media/radar/ktlx-ref-0018utc-1918cdt-jun1.png"',
              'id="i-a7-s3-ktlx-ref-0014utc-1914cdt-jun1-1" src="media/radar/ktlx-ref-0014utc-1914cdt-jun1.png"')
h = h.replace('id="a7-s3-ktlx-ref-0000utc-1900cdt-jun1-1" data-start="1929.91"',
              'id="a7-s3-ktlx-ref-0018utc-1918cdt-jun1-1" data-start="1929.91"')
h = h.replace('id="i-a7-s3-ktlx-ref-0000utc-1900cdt-jun1-1" src="media/radar/ktlx-ref-0000utc-1900cdt-jun1.png"',
              'id="i-a7-s3-ktlx-ref-0018utc-1918cdt-jun1-1" src="media/radar/ktlx-ref-0018utc-1918cdt-jun1.png"')

# ---- 2. CSS: broadcast grade + cards ----
CSS = """
  .grade-bc video { filter: brightness(0.88) saturate(0.72) contrast(1.1) sepia(0.12); }
  .placecard { position:absolute; left:0; right:0; bottom:180px; text-align:center; z-index:6; }
  .placecard .pc-place { display:table; margin:0 auto; font-family:'Arial Black',Arial,sans-serif; font-weight:900; font-size:58px; color:#f2f5f8; letter-spacing:2px; background:rgba(5,8,12,0.66); padding:10px 42px; text-shadow:0 3px 26px rgba(0,0,0,0.9); }
  .placecard .pc-date { display:table; margin:10px auto 0; font-family:Georgia,serif; font-style:italic; font-size:30px; color:#d8a13a; background:rgba(5,8,12,0.66); padding:8px 30px; }
"""
h = h.replace('  .clip { position:absolute; inset:0; }', '  .clip { position:absolute; inset:0; }' + CSS)

# ---- 3. Hook picture (track 1), before the A0-S2 windows ----
HOOK = """<!-- EP4-AUDIO-INJECT -->
<!-- ── A0 HOOK (0–28s): siren spine; two gated unmuted broadcast pulls; radar blooms ── -->
<section class="clip grade-bc" id="a0-hook-kfor-very-close-call-1" data-start="2.0" data-duration="4.0" data-track-index="1" data-owner-gate="pending"><video id="v-a0-hook-kfor-very-close-call-1" src="media/broadcast/kfor-sutton-very-close-call-hookcut.mp4" data-start="2.0" data-duration="4.0"></video></section>
<section class="clip" id="a0-hook-wxgov-radar-loop-1" data-start="6.0" data-duration="6.0" data-track-index="1"><img id="i-a0-hook-wxgov-radar-loop-1" src="media/weathergov/wxgov-radar-loop-elreno.gif"></section>
<section class="clip grade-bc" id="a0-hook-twc-bettes-suv-toss-1" data-start="12.0" data-duration="3.5" data-track-index="1" data-owner-gate="pending"><video id="v-a0-hook-twc-bettes-suv-toss-1" src="media/broadcast/twc-bettes-suv-toss-hookcut.mp4" data-start="12.0" data-duration="3.5"></video></section>
<section class="clip" id="a0-hook-ktlx-ref-2233utc-1733cdt-1" data-start="15.5" data-duration="6.0" data-track-index="1"><img id="i-a0-hook-ktlx-ref-2233utc-1733cdt-1" src="media/radar/ktlx-ref-2233utc-1733cdt.png"></section>
<section class="clip" id="a0-hook-ktlx-ref-2251utc-1751cdt-1" data-start="21.5" data-duration="6.5" data-track-index="1"><img id="i-a0-hook-ktlx-ref-2251utc-1751cdt-1" src="media/radar/ktlx-ref-2251utc-1751cdt.png"></section>

"""
h = h.replace('<!-- PICTURE WINDOWS: authored per act below this line -->',
              '<!-- PICTURE WINDOWS: authored per act below this line -->\n\n' + HOOK)

# ---- 4. Track 3 cards + Track 5 beds ----
TAIL = """<!-- ======== TRACK 3 — TITLES/CARDS ======== -->
<section class="clip" id="c-dateplace" data-start="0.5" data-duration="7.0" data-track-index="3">
  <div class="placecard"><div class="pc-place">EL RENO, OKLAHOMA</div><div class="pc-date">MAY 31, 2013 · 6:03 PM</div></div>
</section>
<section class="clip" id="c-moore" data-start="97.5" data-duration="7.0" data-track-index="3">
  <div class="placecard"><div class="pc-place">MOORE, OKLAHOMA</div><div class="pc-date">MAY 20, 2013 · ELEVEN DAYS EARLIER</div></div>
</section>
<!-- ======== TRACK 5 — MUSIC/SFX BEDS (volumes driven on master tl; every bed dies INTO its blackout) ======== -->
<audio id="sfx-siren" src="media/sfx/03_tornado_siren_waver.ogg" data-start="0" data-duration="28.5" data-volume="0" data-bed="1"></audio>
<audio id="bgm-a0" src="media/music/m-dread-2x.mp3" data-start="30" data-duration="63.06" data-volume="0" data-bed="1"></audio>
<audio id="bgm-a1" src="media/music/m-neutral-2x.mp3" data-start="95.56" data-duration="219.86" data-volume="0" data-bed="1"></audio>
<audio id="bgm-a2a" src="media/music/m-dread-2x.mp3" data-start="317.42" data-duration="177.11" data-volume="0" data-bed="1" data-callback="dread returns for the left-turn act"></audio>
<audio id="bgm-a2b" src="media/music/m-dread-5x.mp3" data-start="496.53" data-duration="497.81" data-volume="0" data-bed="1"></audio>
<audio id="bgm-a4" src="media/music/m-tense-3x.mp3" data-start="997.34" data-duration="309.75" data-volume="0" data-bed="1"></audio>
<audio id="bgm-a5" src="media/music/m-somber-2x.mp3" data-start="1309.09" data-duration="173.21" data-volume="0" data-bed="1"></audio>
<audio id="bgm-a6" src="media/music/m-neutral-3x.mp3" data-start="1484.3" data-duration="247.52" data-volume="0" data-bed="1" data-callback="neutral underscore for lessons act"></audio>
<audio id="bgm-a7" src="media/music/m-somber-2x.mp3" data-start="1734.32" data-duration="206.58" data-volume="0" data-bed="1" data-callback="somber returns for the reckoning"></audio>
<audio id="bgm-a8" src="media/music/m-hopeful-1x.mp3" data-start="1943.9" data-duration="21.19" data-volume="0" data-bed="1"></audio>
<audio id="sfx-rain" src="media/sfx/01_rain_street_medium.mp3" data-start="1309.09" data-duration="45.0" data-volume="0" data-bed="1"></audio>
"""
h = h.replace('<!-- ======== TRACK 3 — TITLES/CARDS ======== -->\n', '')
h = h.replace('<!-- ======== TRACK 5 — MUSIC/SFX BEDS: editorial choice, authored below ======== -->', TAIL)

# ---- 5. Master timeline: bed volumes + card entrances ----
TL = """<script>
(function() {
  const tl = gsap.timeline({ paused: true });
  /* siren spine: in over 2s, duck under both unmuted pulls, swell, die before narration */
  tl.to("#sfx-siren", { volume: 0.5, duration: 2.0 }, 0.0);
  tl.to("#sfx-siren", { volume: 0.22, duration: 0.5 }, 1.8);   /* duck under KFOR pull */
  tl.to("#sfx-siren", { volume: 0.5, duration: 0.6 }, 6.1);
  tl.to("#sfx-siren", { volume: 0.22, duration: 0.5 }, 11.8);  /* duck under TWC pull */
  tl.to("#sfx-siren", { volume: 0.55, duration: 1.0 }, 15.6);  /* swell over the bloom */
  tl.to("#sfx-siren", { volume: 0.0, duration: 3.0 }, 25.0);   /* gone before a0-s2 speaks */
  /* beds: 2s in, die INTO each blackout dip (out ends at dip start) */
  tl.to("#bgm-a0",  { volume: 0.10, duration: 2.0 }, 30.5);
  tl.to("#bgm-a0",  { volume: 0.0,  duration: 1.0 }, 92.06);   /* bo-a0 @93.06 */
  tl.to("#bgm-a1",  { volume: 0.16, duration: 2.0 }, 96.0);
  tl.to("#bgm-a1",  { volume: 0.0,  duration: 1.0 }, 314.42);  /* bo-a1 @315.42 */
  tl.to("#bgm-a2a", { volume: 0.16, duration: 2.0 }, 317.9);
  tl.to("#bgm-a2a", { volume: 0.0,  duration: 1.0 }, 493.53);  /* bo-width @494.53 */
  tl.to("#bgm-a2b", { volume: 0.16, duration: 2.0 }, 497.0);
  tl.to("#bgm-a2b", { volume: 0.10, duration: 0.8 }, 691.6);   /* duck under a2-broadcast pull */
  tl.to("#bgm-a2b", { volume: 0.16, duration: 0.8 }, 702.2);
  tl.to("#bgm-a2b", { volume: 0.0,  duration: 1.0 }, 993.34);  /* bo-twistex @994.34 */
  tl.to("#bgm-a4",  { volume: 0.16, duration: 2.0 }, 997.8);
  tl.to("#bgm-a4",  { volume: 0.0,  duration: 1.0 }, 1306.09); /* bo-a4 @1307.09 */
  tl.to("#bgm-a5",  { volume: 0.16, duration: 2.0 }, 1309.6);
  tl.to("#bgm-a5",  { volume: 0.0,  duration: 1.0 }, 1481.3);  /* bo-a5 @1482.3 */
  tl.to("#bgm-a6",  { volume: 0.16, duration: 2.0 }, 1484.8);
  tl.to("#bgm-a6",  { volume: 0.0,  duration: 1.0 }, 1730.82); /* bo-reckoning @1731.82 */
  tl.to("#bgm-a7",  { volume: 0.16, duration: 2.0 }, 1734.8);
  tl.to("#bgm-a7",  { volume: 0.0,  duration: 1.0 }, 1939.9);  /* bo-close @1940.9 */
  tl.to("#bgm-a8",  { volume: 0.14, duration: 2.0 }, 1944.4);
  tl.to("#bgm-a8",  { volume: 0.0,  duration: 1.5 }, 1963.4);  /* end of comp */
  /* rain under the flood act (source mean -29.7 dB; 0.85 = audible bed) */
  tl.to("#sfx-rain", { volume: 0.85, duration: 3.0 }, 1310.0);
  tl.to("#sfx-rain", { volume: 0.0,  duration: 3.0 }, 1351.0);
  /* cards: rise + settle, exit before window end */
  tl.fromTo("#c-dateplace .placecard", { autoAlpha: 0, y: 26 }, { autoAlpha: 1, y: 0, duration: 0.6, ease: "power3.out" }, 0.7);
  tl.to("#c-dateplace .placecard", { autoAlpha: 0, y: -14, duration: 0.5, ease: "power2.in" }, 6.8);
  tl.fromTo("#c-moore .placecard", { autoAlpha: 0, y: 26 }, { autoAlpha: 1, y: 0, duration: 0.6, ease: "power3.out" }, 97.7);
  tl.to("#c-moore .placecard", { autoAlpha: 0, y: -14, duration: 0.5, ease: "power2.in" }, 103.8);
  window.__timelines["ep4-el-reno"] = tl;
})();
</script>
"""
h = h.replace('<script>window.__timelines = window.__timelines || {};</script>',
              '<script>window.__timelines = window.__timelines || {};</script>\n' + TL)

io.open(P, 'w', encoding='utf-8').write(h)
print('injected OK')
