# g-a5-4-princeton: Princeton, Charney, the machine (A5-S4)
Builder: Sonnet 5.5, high effort. Depth: standard. Read `references/mg-quickref.md` and `learnings/mg.md` first.
Start from: popfig and glass parts of `references/editing-patterns/ep6-glasscard-popfig-bfmg.html`; `library/inhouse/snippets/cards.css` `.popfig`, `.namecard`, `.srclab` (copy values, not class names). Prefix every id/class `a54-`.
Sits over: nothing. Full-frame comp on track 2; its ground is the photo below.
Asset: `media/candidates/a5/A5-S4_c2_von-neumann-oppenheimer-ias-1952.jpg` (1500 x 1125, CC BY 4.0, Jeremy Norman Collection of Images; provenance verified Y; picks.md pick). Orchestrator copies it to `media/a5/ias-machine-1952.jpg` and adds the CC BY credit to the description. Mount that path only.

## 0. Claim
Around 1950 in Princeton, New Jersey, a team led by Jule Charney set out to forecast weather with arithmetic on an electronic computer. The picture is the kind of machine they meant; it is not Charney and not the 1950 run.

## 1. Source
- `factcheck/a5-r2.md` row 18 (NOAA: "a group of theoretical meteorologists at the Institute of Advanced Study in Princeton, New Jersey. The group was headed by Jule Charney."), rows 19, 21, 22 (chips "PRINCETON, NEW JERSEY", "JULE CHARNEY" confirmed).
- Photo: IAS machine, dated 10 June 1952, two named men in front (Oppenheimer, von Neumann). The 1950 one-day forecast ran on ENIAC (row 21), so the photo is labelled with its own year.

## 2. Datum, scale, orientation
- Crop: machine only, NO FACE in any frame. Faces sit at about source x 620 to 1160, y 200 to 470; bodies from x 475 rightwards. Use the left rack column only: crop box 430 x 242 source px (16:9), x 40 to 470. Scale = 1920 / 430 = 4.465. Screen = ((src_x - crop_x) × 4.465, (src_y - crop_y) × 4.465).
- Pan: crop_y from 140 (tube racks) at 0.00 to 818 (drum cylinders, bottom-left) at the end, ease none (crop_x fixed at 40). Implement as an img 1500 x 1125 scaled 4.465 inside a 1920 x 1080 clip, translated by -crop × 4.465.
- Grade: `.archgrade` filter; a 0.25 dim layer under text.

## 3. Geometry (px)
- Popfig: big "PRINCETON" AbrilFig 150 px `#d0121f`, `.pf-big` shadow, centred x 960, block top y 330 (about 960 px wide, inside x 96 to 1824); sub "NEW JERSEY" Arial 700 32 px `#e8e3d8`, `.pf-sub` shadow, 12 px under.
- Name card (text only, no photo slot): "JULE CHARNEY" Arial Black 900 64 px `#f2f5f8`, centred, bottom 150 (`.namecard .nc-name` values), on a glass pill (tokens.md glass surface, radius 28, padding 10 x 42) since it sits over a moving photo; sub line "Meteorology group, Princeton" Georgia italic 32 px `#e8c56a`, 10 px under, same pill.
- Source line (bottom-left, left 110, bottom 60), Arial 700 20 px `#c8d3e0`, glass pill: "Photo: IAS computer, Princeton, 1952 · Source: AMS".
- Tiers: 150/64 (big), 32 (mid), 20 (small).

## 4. Must be true in the picture
1. No human face or head is visible in any frame of the pan (check the first frame, the last frame and 3 between). A face under "JULE CHARNEY" = FIX: it would name the wrong man.
2. The name card and popfig never show at the same time (one reading target).
3. "1952" appears only in the source line; no "1950" anywhere on screen (the spoken 1950 forecast was not on this machine).
4. Text-safe margins hold; corner x >= 1600, y >= 680 holds no text (name card pill must end left of x 1600 if it reaches y 680: centred 64 px "JULE CHARNEY" is about 560 px wide, x 680 to 1240, fine).
5. Popfig is bare Abril with shadow, no card.

## 5. Panel text (exact) and cues
Text: `PRINCETON` · `NEW JERSEY` · `JULE CHARNEY` · `Meteorology group, Princeton` · `Photo: IAS computer, Princeton, 1952 · Source: AMS`
Cues from `audio/a5-s4.words.json`:
- 0.00: photo crop on at crop_y 140, pan running (ease none to the end).
- 0.60: source line in (`fromTo` autoAlpha 0, x -20 to 0, 0.4 s).
- 1.12 "Princeton,": big line in (`fromTo` autoAlpha 0, scale 1.25 to 1, 0.45 s, back.out(1.6)). `/* PRINCETON @1.12 */`
- 1.84 "New": sub in (`fromTo` autoAlpha 0, y 18 to 0, 0.4 s, power3.out). `/* NEW JERSEY @1.84 */`
- 2.20 to 3.10: popfig float y 0 to -8.
- 3.10: popfig exits (`to` autoAlpha 0, y -40, scale 0.96, 0.5 s, power3.in), gone by 3.60.
- 3.78 "Jule": name pill in (`fromTo` autoAlpha 0, y 30 to 0, 0.5 s, power3.out). `/* JULE @3.78 */`
- 4.00 "Charney": sub line in (`fromTo` autoAlpha 0, y 12 to 0, 0.35 s). `/* CHARNEY @4.00 */`
- 4.50 to 8.80: name pill float y 0 to -6, sine.inOut.
- 8.80: name card exits (`to` y 30, autoAlpha 0, 0.5 s, power3.in). `/* WORKED @8.34 */`
- 9.30 to 17.88: photo pan alone (picture carries "electronic computer", "Could a machine...", "In 1950..."). Something moves every second (the pan).
- 17.88 to 18.40: land, fade-through to black 0.4 s at the end (full-frame scene end, not a hard vanish).
Host: data-start = A5-S4 audio start, duration 18.40 s. Root `id="g-a5-4-princeton-root"`.

## 6-8
Contract, tools, done line and receipt: `references/mg-brief-template.md` §6, §7, §7a, §8. Done line 7: composite frames at 1.5, 5.0 and 15.0 s and read every one for faces.
Fallback (picture line's own): if the 4.465x crop reads as mush on the frame read, replace the photo with a self-made line drawing of a 1950s room-sized computer (reels and panels), keep every text and cue, and change the source line to "Source: AMS". Report which one shipped.
Must not: CSS @keyframes, `id="root"`, a name card over any person.
