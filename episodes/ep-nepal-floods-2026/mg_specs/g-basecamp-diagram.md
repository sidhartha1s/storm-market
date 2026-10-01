# BRIEF — g-basecamp-diagram · A3 open (Himlung base camp, avalanche path) · SCHEMATIC

## 0. What this graphic claims
Himlung base camp sat at the foot of the massif with a fixed rope climbing toward Camp 1; the avalanche came down
the face and crossed the camp. Everything on screen serves that one shape: high face -> rope -> camp -> slide path.

## 1. SOURCE
No published cross-section exists for this camp (owner brief: "SCHEMATIC, NOT TO SCALE"). Numbers that ARE confirmed
and must appear correctly: 16 at base camp = 2 climbing guides + 14 kitchen/support staff (factcheck-B#14, factcheck-D#3);
UAE climbing-school group due in Kathmandu Oct 1 (factcheck-A#2, factcheck-B#15); Himlung sold as "a first big
Himalayan climb" / training peak (factcheck-B#13).

## 2. DATUM, SCALE, ORIENTATION
Diagram stage = left 1180 x 1080 (x 0-1180). RHS panel 1180-1920 (740px), gradient rail per tokens.md.
Base/foot line y = 830 (ground). Apex y = 150. No real elevation scale — schematic only, caption says so.

## 3. GEOMETRY (px)
- Massif silhouette: apex (700,150); left ridge to (230,830); right ridge to (1170,830); base line y=830, x 150-1180.
  Rock fill gradient #4a5560 -> #2a3644, snow cap near apex (#dfe7ee wedge, top 80px).
- Camp: 5 tent triangles (amber #d8a13a), x = 380/440/500/560/620, y 790-822 (base at 822, apex 22px up).
- Fixed rope: dashed line #f2f5f8 (dash 8 6) from (500,788) to Camp-1 marker (830,430); marker = 14px ring + label
  "CAMP 1" at (850,420), diagram-label tier, left of line never on it.
- Avalanche path: polygon (700,230)-(760,230)-(650,780)-(380,780), fill rgba(223,231,238,0)->rgba(223,231,238,.55)
  gradient top-to-bottom, crossing directly over the tent cluster (x 380-650).
- Caption "SCHEMATIC, NOT TO SCALE" at (96,1010), small tier, grey.

## 4. MUST BE TRUE
1. Camp 1 marker sits above and right of the tent cluster, joined to it by the dashed rope line only (no other path touches it).
2. The avalanche wedge's top edge starts above y=230 (near the face, not the camp) and its base fully covers the tent x-range (380-650).
3. Exactly 5 tent icons, all inside x 350-650, never overlapping the rope line.
4. RHS stat row reads 16 total / 2 guides / 14 kitchen-support (not any other split).
5. "DUE OCT 1" appears, never a different date.
6. "SCHEMATIC, NOT TO SCALE" is legible for the whole window.

## 5. PANEL TEXT (exact) and CUES
RHS panel: eyebrow "HIMLUNG HIMAL · NEPAL'S FAR NORTH" · serif sub italic "a first big Himalayan climb" · row "16"/"AT
BASE CAMP" · row "2"/"CLIMBING GUIDES" · row "14"/"KITCHEN & SUPPORT" · note "UAE CLIMBING SCHOOL · DUE OCT 1".
Cues (s, from A3 paragraph start, 175 wpm est):
/* CUE "Himlung Himal stands in Nepal's far north" @est 0.3 */ massif + eyebrow reveal, slow drift starts (whole window).
/* CUE "a practice run before peaks like Everest" @est 8.9 */ serif sub reveals.
/* CUE "Guides carry up the tents and fix the ropes" @est 14.4 */ tents fade in, rope line draws.
/* CUE "sixteen workers were at base camp" @est 21.6 */ Camp 1 marker pops, row "16/AT BASE CAMP" reveals.
/* CUE "two climbing guides and fourteen kitchen and support staff" @est 24.7 */ rows "2" and "14" stagger in.
/* CUE "due in Kathmandu on October first" @est 32.5 */ "UAE CLIMBING SCHOOL · DUE OCT 1" note reveals.
/* CUE "Then snow and rock came down onto the camp" @est 37.0 */ avalanche wedge slides down over tents, panel note pulses once, hold to exit.
Duration 40 s (panel exits x:660->1400 autoAlpha 0 at 39.4, 0.6 s power3.in).
