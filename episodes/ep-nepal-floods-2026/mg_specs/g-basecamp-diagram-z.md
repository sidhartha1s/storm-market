# BRIEF — g-basecamp-diagram-z · Z close, fades to the single camp · SCHEMATIC

## 0. What this graphic claims
The full camp thins to one tent as the episode closes: "the guides and cooks who went up first were the ones on the
mountain... Pasang Bhote was among the first two they reached." One remaining camp icon carries the closing beat
under the returning name card (name card itself is an index.html overlay, not part of this file).

## 1. SOURCE
Reuses g-basecamp-diagram geometry. No new numbers; closing beat, not a new claim.

## 2. DATUM, SCALE, ORIENTATION
Same stage as g-basecamp-diagram. Dawn palette carried over from g-basecamp-diagram-a6 (continuity cut).

## 3. GEOMETRY (px)
Starts identical to g-basecamp-diagram-a6's end state (massif, 5 tents, rope line, Camp-1 marker, avalanche wedge).
Over the fade: 4 of 5 tents (440/500/560/620) fade to 0, rope line + Camp-1 marker fade to 0, avalanche wedge dims
to 15% opacity (context, not gone). One tent (x=380) stays, gains a soft glow (radial highlight behind it).

## 4. MUST BE TRUE
1. Exactly one tent icon is fully visible by the end (the one at x=380); all other camp elements are gone (autoAlpha 0).
2. The massif silhouette itself never disappears (it is the constant backdrop for the closing card).
3. Something drifts for the entire window (no static hold past the fade).
4. No new number or label is introduced (silent visual, narration carries the words).

## 5. PANEL TEXT (exact) and CUES
No panel text (RHS stays clear for the name card mounted by index.html). Cues:
/* CUE "(Z chapter open, continuous from the a6 hold)" @est 0.0 */ tl.set to a6 end-state, visible.
/* CUE "the ones on the mountain" @est 1.2 */ rope line + Camp-1 marker fade out, 0.6 s.
/* CUE "Pasang Bhote was among the first two" @est 3.0 */ 4 tents fade out 0.7 s stagger 0.1, remaining tent glow ramps in.
/* CUE "under fresh snow" @est 6.5 */ avalanche wedge dims to 15%, whole-window drift continues (scale 1.0->1.03).
Duration 8.0 s. No hard exit (cuts to g-outro on the episode timeline, per Picture line).
