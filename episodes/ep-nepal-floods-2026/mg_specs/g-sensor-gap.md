# BRIEF — g-sensor-gap · A6 full payoff [PAY] · timeline: slope fails, gauge sees it late

## 0. What this graphic claims
Nepal's flood warning system measures rivers, not slopes. A slope that fails in 3 seconds gives a gauge nothing to
read until the mud is already in the water; in August the gauges nearest Langtang were swept away before warning
anyone. Before this storm, 49 of 77 districts were on flash flood alert. This is loop L6's close, the cta-hinge payoff.

## 1. SOURCE
factcheck-D#1: "authorities warned of possible flash floods in 49 of the country's 77 districts" (Al Jazeera, 27 Sep
2026), narration "forty nine of its seventy seven districts". factcheck-C#19: three stream gauges destroyed near
Langtang, one swept away 13 minutes after the collapse, before its next scheduled reading. factcheck-C#17: system
built for river floods, not moving mountainsides (Al Jazeera 19 Sep, ICIMOD quote).

## 2. DATUM, SCALE, ORIENTATION
Full-frame timeline, two horizontal tracks: SLOPE track y=420, RIVER GAUGE track y=620, both spanning x=200-1720.
RHS keeps clear of presenter corner (nothing enters x>=1600,y>=680).

## 3. GEOMETRY (px)
- Track lines: two horizontal lines y=420 and y=620, x 200-1720, stroke #5a768f 2px dashed, labels "SLOPE" (140,420)
  and "RIVER GAUGE" (140,620) 22px grey tracking3, left of the track never on it.
- Slope-fails mark: burst icon (small jagged star, #c0392b) at (600,420), pops in first; timeline tick label "SLOPE
  FAILS" below at (600,470) 19px #dfe7ee.
- Gauge-line: dashed flat segment x 200-1000 at y=620 (nothing to read), then curves upward (a short rising arc,
  quadratic path) from (1000,620) to (1300,540) once the slope-fails mark has already landed — visually the gauge
  reacts LATE and downstream of the slope mark's x position.
- Gauge-sees-it mark: green blip circle at (1300,540), tick label "GAUGE SEES IT" below at (1300,590) 19px #dfe7ee.
- Popfig stat (the [PAY] beat): centred lower area, AbrilFig 130px #d0121f "49 / 77" at (960,830) centred, sub 22px
  #93a3b2 tracking3 "DISTRICTS ON FLASH FLOOD ALERT" at (960,900) centred.

## 4. MUST BE TRUE
1. The "SLOPE FAILS" mark always lands strictly LEFT of the "GAUGE SEES IT" mark on the shared x-axis (the lag is the whole claim).
2. The gauge line stays flat/dashed (no reading) until after the slope-fails mark has already appeared.
3. The popfig reads "49 / 77" with sub "DISTRICTS ON FLASH FLOOD ALERT" — never "49 OF 77 DISTRICTS" run together in one line (16-char big-line cap).
4. Nothing sits in x>=1600,y>=680 (presenter keep-out) at any time.
5. Both track labels ("SLOPE", "RIVER GAUGE") are legible for the whole window.

## 5. PANEL TEXT (exact) and CUES
Text: "SLOPE" · "RIVER GAUGE" · "SLOPE FAILS" · "GAUGE SEES IT" · popfig "49 / 77" · sub "DISTRICTS ON FLASH FLOOD ALERT".
Cues (s, from "It measured rivers." sentence start, A6 open, 175 wpm est):
/* CUE "It measured rivers" @est 0.3 */ both track lines draw in (scaleX 0->1), labels reveal.
/* CUE "forty nine of its seventy seven districts on flash flood alert" @est 3.5 */ popfig "49 / 77" + sub slam in (power4.in), holds to 6.5.
/* CUE "river and rain gauges, which report when water rises" @est 9.0 */ popfig exits, gauge track re-emphasised (pulse).
/* CUE "A slope that fails in three seconds" @est 15.5 */ slope-fails burst mark pops at x=600, tick label reveals.
/* CUE "gives a river gauge nothing to read until the mud is already in the water" @est 18.5 */ gauge dashed segment pulses (still flat, "nothing to read").
/* CUE "the gauges nearest Langtang were swept away" @est 23.5 */ gauge line arcs up late at x=1000-1300, "GAUGE SEES IT" mark lands, gap between the two marks visibly reads.
Duration 27 s (tracks + marks exit x:660->1400 autoAlpha 0 at 26.4, 0.6 s power3.in).
