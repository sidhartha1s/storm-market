# El Reno v4b: bakes the two ambience stems the composition mounts as sx-mus-bed-a and sx-mus-bed-b.
# Why a bake: an <audio> element plays at one fixed volume, and this script's bed has to drop out, thin to
# rain and come back on named words (edit_script.md Picture notes). The times below are the editor's choices,
# set by hand against words.json; this file is their one home. It writes audio only, never episode HTML.
# Sources (all claim-free, assets/sfx/provenance.md): the DeAPI dark-ambient score, the owner-pack pulse
# drone (hook), the self-made rain loop, the public-domain waver siren.
# usage: python3 episodes/ep4-el-reno/bake_beds.py     (run from the repo root or anywhere; paths are absolute)
import subprocess
from pathlib import Path

EP = Path(__file__).resolve().parent
SFX = EP.parent.parent / "assets" / "sfx"
OUT = EP / "media" / "beds"
SCORE, DRONE = SFX / "deapi" / "score-act1-darkambient.mp3", SFX / "owner-2026-08-13" / "freesound_community-industrial-pulse-drone-27456.mp3"
RAIN, SIREN = SFX / "rain-loop.mp3", SFX / "03_tornado_siren_waver.ogg"

# (episode second, gain). Straight lines between points; before the first and after the last point the gain holds.
BED = [  # the score. 1 = full bed
    (17.5, 0), (21, 1),                                   # in under the title, as the hook drone leaves
    (56.8, 1), (58.3, .45), (72.6, .45), (74, 1),         # I1-S3: thins to rain over the flood count
    (147.9, 1), (148.7, 0),                               # I1-S8: out on the last word
    (162, 0), (164, 1),                                   # A1-S1: back under the last sentence
    (249.8, 1), (249.92, 0), (250.95, 0), (252.5, 1),     # A1-S6: silence on "cut out", one second
    (283.9, 1), (284.6, .6), (287.7, .6), (288.5, 1),     # A1-S8: low under the three-second hold
    (326.3, 1), (327, .7), (335.9, .7), (336.5, 0),       # Paul clip 2, then the act blackout
    (337.45, 0), (338.6, 1),
    (402.4, 1), (403, .5), (411.6, .5), (412.2, .7), (421.9, .7), (422.6, 1),   # A2-S3 thins; Paul clip 3
    (517.9, 1), (518.4, 0), (521.06, 0), (523, 1),        # A2-S11: out on the question, back after the blackout
    (547.9, 1), (548.67, 0),                              # the TV crew's sequence carries no bed
    (573.02, 0), (575, .75),                              # A3-S5: back in, lower than before
    (637, .75), (637.5, 0), (645.9, 0), (646.8, .75),     # A3-S8: everything out under the counter
    (684.9, .75), (685.4, 0), (686.1, 0), (687, .75),     # A3-S10: silence after the three names
    (698, .75), (698.6, .6), (707.5, .6), (708.2, .75),   # Paul clip 4
    (737.6, .75), (738.6, .4), (750.9, .4), (751.66, 0),  # A3-S14: thins to rain; out at the ad's blackout
    (778.07, 0), (780, .85),                              # Act 4 opens after the ad
    (833.2, .85), (834.2, .4), (838.25, .4), (838.6, 0), (841, 0), (842.5, .85),   # A4-S4: water, then silence after "survived"
    (1063.2, .85), (1063.6, 0), (1065.58, 0), (1067.5, .85),                         # A4-S16: out on "Why not?"
    (1263.6, .85), (1268.6, 1.5), (1268.94, 1.5), (1269.1, 0),                       # A5-S12: rises under the last sentence, stops with it
    (1280.21, 0), (1282, .8), (1323.5, .8), (1327.3, 0),                             # the close
]
DRONE_ENV = [(0, 0), (.8, 1), (17.5, 1), (21, 0)]         # hook: low drone from 0:00
RAIN_ENV = [  # the rain loop is about 10 dB quieter than the score, so its full level is above 1
    (56.5, 0), (58.3, 3), (72.6, 3), (74.2, 0),           # I1-S3 flood water
    (315.5, 0), (317, 2.2), (325.5, 2.2), (327, 0),       # A1-S11 the wall of rain
    (362.6, 0), (364.5, 2.2), (383, 2.2), (384.5, 0),     # A2-S2 rain fills the ring
    (480.6, 0), (482, 2.2), (497, 2.2), (498.5, 0),       # A2-S10 inside the rain
    (737.6, 0), (739, 3), (750.9, 3), (751.66, 0),        # A3-S14 thins to rain
    (826.9, 0), (828.5, 2.5), (838.25, 2.5), (838.6, 0),  # A4-S4 water
    (845.26, 0), (847, 1.5), (879.5, 1.5), (881, 0),      # A4-S5 and A4-S6 the drain
    (986.5, 0), (988, 1.5), (999, 1.5), (1000, 0),        # A4-S12 windshield
]
SIRENS = [  # (episode second the siren file starts, its envelope)
    (150.08, [(150.08, 0), (151.5, .8), (161.5, .8), (164.5, 0)]),   # A1-S1 warnings going out
    (784.8, [(784.8, 0), (786.3, .8), (792.5, .8), (795, 0)]),       # A4-S1 "When the tornado sirens sounded"
]
STEMS = [("elreno-bed-a.mp3", 0.0, 751.66, 0.0), ("elreno-bed-b.mp3", 778.07, 1327.38, 200.0)]   # name, from, to, where in the score loop it starts


def expr(points, shift):
    """Piecewise-linear gain as an ffmpeg expression of t (stem time = episode time minus shift)."""
    pts = [(t - shift, g) for t, g in points]
    out = f"{pts[0][1]}"
    for (t0, g0), (t1, g1) in zip(pts, pts[1:]):
        if g1 != g0:
            out += f"+({g1 - g0:.4f})*clip((t-({t0:.3f}))/{t1 - t0:.3f},0,1)"
    return out


def start_gain(points, at):
    """Gain at a stem's first second, so a stem that begins mid-envelope starts at the right level."""
    g = points[0][1]
    for (t0, g0), (t1, g1) in zip(points, points[1:]):
        if at >= t1: g = g1
        elif at > t0: g = g0 + (g1 - g0) * (at - t0) / (t1 - t0)
    return g


OUT.mkdir(parents=True, exist_ok=True)
loop = OUT / "_score-loop.mp3"   # the 168 s score crossfaded onto itself three times: 8 copies, seams 3 s
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(SCORE), "-filter_complex",
                "[0]asplit=8[a][b][c][d][e][f][g][h];[a][b]acrossfade=d=3[ab];[c][d]acrossfade=d=3[cd];[e][f]acrossfade=d=3[ef];[g][h]acrossfade=d=3[gh];"
                "[ab][cd]acrossfade=d=3[abcd];[ef][gh]acrossfade=d=3[efgh];[abcd][efgh]acrossfade=d=3", "-b:a", "192k", str(loop)], check=True)
for name, t0, t1, loop_at in STEMS:
    dur = t1 - t0
    def vol(points):
        pts = [(t0, start_gain(points, t0))] + [p for p in points if p[0] > t0]
        return f"volume=eval=frame:volume='{expr(pts, t0)}'"
    cmd = ["ffmpeg", "-v", "error", "-y", "-ss", f"{loop_at}", "-i", str(loop), "-stream_loop", "-1", "-i", str(RAIN), "-i", str(DRONE)]
    chains = [f"[0]aformat=sample_rates=44100:channel_layouts=stereo,{vol(BED)}[bed]", f"[1]aformat=sample_rates=44100:channel_layouts=stereo,{vol(RAIN_ENV)}[rain]",
              f"[2]aformat=sample_rates=44100:channel_layouts=stereo,{vol(DRONE_ENV)}[drone]"]
    mix = ["[bed]", "[rain]", "[drone]"]
    for start, env in SIRENS:
        if t0 <= start < t1:
            cmd += ["-i", str(SIREN)]
            n = (len(cmd) - 6) // 2 - 1 + 0   # index of the input just added
            n = sum(1 for c in cmd if c == "-i") - 1
            chains.append(f"[{n}]aformat=sample_rates=44100:channel_layouts=stereo,adelay={int((start - t0) * 1000)}:all=1,{vol(env)}[s{n}]")
            mix.append(f"[s{n}]")
    graph = ";".join(chains) + ";" + "".join(mix) + f"amix=inputs={len(mix)}:normalize=0:duration=longest,atrim=0:{dur:.3f},alimiter=limit=0.9"
    subprocess.run(cmd + ["-filter_complex", graph, "-t", f"{dur:.3f}", "-b:a", "192k", str(OUT / name)], check=True)
    print(name, "seconds", round(dur, 2))
