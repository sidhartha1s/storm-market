# g-a5-11-panel · A5-S7 (Paul on camera) · standard · Sonnet 5.5 high
Shared rules: `_list.md` "Shared rules". Base: `g-a5-4-pages` (same two pages, scaled). Panel shape: mg-quickref "RHS stat panel". Why a panel on a Paul clip: `_list.md` change 8 (owner 26 Oct 26, paul-clips.md "No props, ever").

## 0. Claim
Side by side: the 1900 report has telephones and merchants; the ride appears only later, and no one else is known to have backed it up.

## 1. Source
Report lines: sources-cline.md §3. Ride later, uncorroborated: sources-cline.md §4; "not known to have corroborated" (fact-check a5-r1 rows 29 to 30).

## 2. Datum, scale, orientation
Overlay comp, transparent root, over `ins-paul-5` (not generated; timed to the TTS stand-in `audio/a5-s7.wav`). The panel goes on the side away from Paul's face in the start frame; default RIGHT. Paul is never composited over the graphic: the panel is a card over his frame, not a cut-out.

## 3. Geometry (px)
- Panel: `right:0; top:0; bottom:0; width:820px`, RHS gradient `linear-gradient(270deg, rgba(6,9,13,0.94) 72%, rgba(6,9,13,0))`, padding 90px 96px 0 170px.
- Inside, two pages side by side, each 260 x 340 (g-a5-4's pages at 0.42 scale), tops at 260, left page x 1190, right page x 1494, gap 44 (the gap stays empty).
- Tags above them, Arial Black 900 26 px `#f2f5f8`: "SEPT 1900" over the left page, "LATER" over the right.
- On the left page the two report lines are lit (telephone, Strand street), bar per shared rule, scaled; a short label under the page: "TELEPHONE · MERCHANTS" Arial 700 22 px `#93a3b2`.
- Under the right page: "RIDE · NOT KNOWN TO BE BACKED" Arial 700 22 px `#93a3b2`.
- Panel title top: "THE TWO ACCOUNTS" Arial Black 900 52 px `#f2f5f8` at top 140 (big tier).
- Panel text stays above y 680 (pages end at 600, labels by 660): circle off anyway (full-frame Paul clip).
- Popfig after the panel leaves, centred x 960 y 470: big "1900 → LATER", sub "THE REPORT · THE RIDE".

## 4. Must be true in the picture
1. Paul's face is never covered: read the start frame; if his face sits right of x 1100, mirror the panel to the left and say so.
2. Left = report (SEPT 1900), right = later telling.
3. No text says "nobody saw it" or "no other survivor backed it" without "known".
4. The popfig is never on screen with the panel (panel out complete before popfig in).
5. Nothing covers the logo bug at (1740, 900) (the panel gradient may pass over it only if the bug stays visible; if not, end the panel at bottom 760 px).

## 5. Text and cues (a5-s7.words.json, segment 5.64 s; retime to the clip's own transcript once generated)
- 0.00 ("Put" 0.00): panel slides in `x:660 -> 0, 0.7 s power3.out`.
- 0.58 ("side" 0.58) /* SIDE BY SIDE @0.58 */: pages in left then right, 0.2 s apart; tags with them.
- 1.04 ("side," 1.04): left page bars draw (both lines, 0.3 s apart); its label in.
- 2.06 ("ride" 2.06) /* LATER @3.04 */: right page brightens; its label in at 3.90 ("no").
- 4.94 ("have" 4.94): panel out `x:980, autoAlpha 0, 0.6 s power3.in`, done by 5.54.
- 5.50 ("up." 5.50) /* POPFIG @5.50 */: popfig in; holds 1.0 s land time (host end = 5.64 + 1.0, or the clip end if shorter: then the popfig starts 1.0 s before the clip end and the panel leaves before it).

## Motion for the whole window
Pages float y ±3; Paul himself moves in the clip.

## Exit
Popfig out (scale 0.92, autoAlpha 0, 0.45 s) ending on the clip's end.

## Footage under it
`ins-paul-5` (Paul at an empty desk, hands empty), mounted on track 1 for the whole host.
