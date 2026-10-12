#!/usr/bin/env bash
# Post-render verification. Usage: verify_render.sh <episode-dir> <render-basename> <draft|full>
# The mode is the one passed to render.cmd and is required: it picks the log (render_<mode>.log)
# and the frame rate the file must have. The file name says neither.
# Everything here reads the finished mp4 — the checks that do not need pixels already ran
# before the render (sweep_episode.py, blank_scan.mjs, beat_density.py, graphics_qc.mjs).
set -u
if [ $# -ne 3 ] || { [ "$3" != draft ] && [ "$3" != full ]; }; then
  echo "usage: verify_render.sh <episode-dir> <render-basename> <draft|full>"; exit 1
fi
EP="$1"; BASE="$2"; MODE="$3"
MP4="$EP/renders/$BASE.mp4"
[ -f "$MP4" ] || { echo "MISSING $MP4"; exit 1; }
FAIL=0

echo "=== gpu (owner 2026-09-15: capture must run on the dedicated GPU, never the Intel iGPU) ==="
LOG="$EP/render_$MODE.log"
PROBES=$(grep -ao 'browserGpuMode probe.*' "$LOG" 2>/dev/null | cut -c1-160)
echo "${PROBES:-no probe line in $LOG}"
# one probe line per capture worker; every one of them must name NVIDIA
if [ -z "$PROBES" ] || printf '%s\n' "$PROBES" | grep -qv NVIDIA; then
  echo "FAIL: a capture worker did not run on the NVIDIA GPU (run scripts/render_busy.py --launch to pin, then re-render)"; exit 2
fi

echo
echo "=== composition truth (index.html #root — the spec this render must match) ==="
COMPOUT=$(python3 - "$EP/index.html" <<'PYEOF'
import re, sys
h = open(sys.argv[1], encoding="utf-8", errors="replace").read()
m = re.search(r'<div[^>]*\bid="root"[^>]*>', h)
if not m:
    print("MISSING")
else:
    tag = m.group(0)
    def attr(name):
        mm = re.search(name + r'="([^"]+)"', tag)
        return mm.group(1) if mm else None
    vals = [attr(n) for n in ("data-width", "data-height", "data-duration", "data-fps")]
    print("MISSING" if None in vals else " ".join(vals))
PYEOF
)
echo "$COMPOUT"
if [ "$COMPOUT" = "MISSING" ] || [ -z "$COMPOUT" ]; then
  echo "FAIL: could not read data-width/height/duration/fps off #root in $EP/index.html — cannot verify without the spec"
  COMP_W=0; COMP_H=0; COMP_DUR=0; COMP_FPS=0
  FAIL=1
else
  read -r COMP_W COMP_H COMP_DUR COMP_FPS <<< "$COMPOUT"
fi

# The frame rate this render must have. A final matches the composition. A draft is a proxy
# rendered at the rate render.cmd launched it with (RENDER_FPS included) and recorded in render_draft.fps.
EXPECT_FPS="$COMP_FPS"
if [ "$MODE" = draft ]; then
  EXPECT_FPS=$(tr -d ' \t\r\n' < "$EP/render_draft.fps" 2>/dev/null)
  if [ -z "$EXPECT_FPS" ]; then
    echo "FAIL: $EP/render_draft.fps is missing or empty — this draft predates the check or never reached the render step, so its frame rate cannot be verified"
    exit 1
  fi
fi

echo
echo "=== artifact vs composition (duration/resolution/audio must match the composition, fps the ==="
echo "=== $MODE rate $EXPECT_FPS — a truncated, downgraded or muted render used to exit 0 here) ==="
PROBE=$(ffprobe -v error -show_entries format=duration,size,bit_rate \
        -show_entries stream=codec_name,codec_type,width,height,r_frame_rate,nb_frames \
        -of default=noprint_wrappers=1 "$MP4")
echo "$PROBE"
HAS_AUDIO=$(ffprobe -v error -select_streams a -show_entries stream=codec_type -of csv=p=0 "$MP4")
# Passed as an argv string, never a /tmp file: this python runs as a native Windows exe (no
# MSYS path translation for text read from a heredoc), so a bash-side /tmp/... path that
# ffmpeg/grep resolve fine is simply not there when a plain open() asks for it.
if ! python3 - "$COMP_W" "$COMP_H" "$COMP_DUR" "$EXPECT_FPS" "$HAS_AUDIO" "$PROBE" <<'PYEOF'
import re, sys
comp_w, comp_h, comp_dur, expect_fps, has_audio, probe = sys.argv[1:7]
probe = probe.replace("\r\n", "\n")  # ffprobe is a native console app; bash keeps its \r
def field(name):
    m = re.search(rf'^{name}=(.+)$', probe, re.MULTILINE)
    return m.group(1).strip() if m else None
dur, w, h, rfr = field("duration"), field("width"), field("height"), field("r_frame_rate")
if comp_w == "0":
    print("SKIP: no composition truth to check dimensions/duration/fps against")
    sys.exit(1)
ok = True
if dur is None or abs(float(dur) - float(comp_dur)) > 0.5:
    print(f"FAIL: duration {dur}s != composition {comp_dur}s (off by more than 0.5s)")
    ok = False
if w != comp_w or h != comp_h:
    print(f"FAIL: resolution {w}x{h} != composition {comp_w}x{comp_h}")
    ok = False
if rfr:
    n, d = rfr.split("/")
    fps = round(float(n) / float(d))
    if str(fps) != expect_fps:
        print(f"FAIL: fps {fps} != expected {expect_fps}fps (a draft shipped as the final, or a render at the wrong rate?)")
        ok = False
if not has_audio.strip():
    print("FAIL: no audio stream in the render")
    ok = False
if ok:
    print(f"OK: {w}x{h} @ {rfr} ({float(dur):.1f}s), audio present — matches the composition")
sys.exit(0 if ok else 1)
PYEOF
then
  FAIL=1
fi

echo
echo "=== black (1.5s+), silence (2s+) and freeze (6s+) spans: FAIL only outside a declared ==="
echo "=== blackout section or CTA dip (silence: also holds and the CTA body) ==="
# Owner's duration table (CLAUDE.md "Chapter blackout"): 1.5s+ of black is dead air, a bug. A
# declared <section class="blackout"> (bo-void, bo-close) and the CTA dips are black, silent and
# still on purpose, so black/freeze/silence inside them are exempt. A declared hold and the CTA body
# may be quiet (silence exempt) but must still show a live picture: black or frozen there is a
# defect (CLAUDE.md: a long hold keeps something alive; a CTA that fails to decode renders black).
BLACK_RAW=$(ffmpeg -hide_banner -nostats -i "$MP4" -vf "blackdetect=d=1.5:pix_th=0.10" -an -f null - 2>&1)
SILENCE_RAW=$(ffmpeg -hide_banner -nostats -i "$MP4" -af "silencedetect=n=-50dB:d=2" -f null - 2>&1)
FREEZE_RAW=$(ffmpeg -hide_banner -nostats -i "$MP4" -vf "freezedetect=n=-58dB:d=6" -an -f null - 2>&1)
VID_DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$MP4")
if ! python3 - "$EP" "$VID_DUR" "$BLACK_RAW" "$SILENCE_RAW" "$FREEZE_RAW" <<'PYEOF'
import re, sys
from pathlib import Path

ep, vid_dur = sys.argv[1], float(sys.argv[2])
raws = {k: v.replace("\r\n", "\n") for k, v in zip(("black", "silence", "freeze"), sys.argv[3:6])}
html = (Path(ep) / "index.html").read_text(encoding="utf-8", errors="replace")

# Declared windows: the same structural markers lint_timeline.py sanctions a narration gap
# against (declared hold, chapter blackout) plus the CTA insert padded by config.yaml dip_in/out.
def sections(cls):
    return [(float(a), float(a) + float(b)) for a, b in re.findall(
        r'<section\b[^>]*class="[^"]*\b' + cls + r'\b[^"]*"[^>]*data-start="([\d.]+)"'
        r'[^>]*data-duration="([\d.]+)"', html)]
picture_ok = sections("blackout")                 # black and freeze allowed only here
quiet_ok = picture_ok + sections("hold")          # silence also allowed in holds and the CTA

cta = re.search(r'<video\b[^>]*src="[^"]*cta/[^"]*"[^>]*>', html)
if cta:
    tag = cta.group(0)
    def attr(name):
        m = re.search(name + r'="([^"]+)"', tag)
        return float(m.group(1)) if m else None
    cs, cd = attr("data-start"), attr("data-duration")
    if cs is not None and cd is not None:
        dip_in = dip_out = 1.0
        cfg = Path(ep).resolve().parent.parent / "config.yaml"
        if cfg.exists():
            ctxt = cfg.read_text(encoding="utf-8", errors="replace")
            m_in, m_out = re.search(r'dip_in:\s*([\d.]+)', ctxt), re.search(r'dip_out:\s*([\d.]+)', ctxt)
            if m_in: dip_in = float(m_in.group(1))
            if m_out: dip_out = float(m_out.group(1))
        picture_ok += [(cs - dip_in, cs), (cs + cd, cs + cd + dip_out)]
        quiet_ok.append((cs - dip_in, cs + cd + dip_out))

TOL = 0.5  # detector edges can land a touch outside the declared window
fail = False
for kind, raw in raws.items():
    starts = [float(x) for x in re.findall(kind + r'_start:\s*([\d.]+)', raw)]
    ends = [float(x) for x in re.findall(kind + r'_end:\s*([\d.]+)', raw)]
    if len(ends) == len(starts) - 1:
        ends.append(vid_dur)  # still open at end of file (a closing blackout)
    if len(starts) != len(ends):
        print(f"FAIL: {len(starts)} {kind}_start vs {len(ends)} {kind}_end lines, could not pair every span")
        fail = True
        continue
    windows = quiet_ok if kind == "silence" else picture_ok
    bad = [(ss, se) for ss, se in zip(starts, ends)
           if not any(ws - TOL <= ss and se <= we + TOL for ws, we in windows)]
    if bad:
        print(f"FAIL: {len(bad)} {kind} span(s) outside any declared window allowed for {kind}:")
        for ss, se in bad:
            print(f"    {ss:.2f}s - {se:.2f}s")
        fail = True
    else:
        print(f"OK: {len(starts)} {kind} span(s), all inside a declared window" if starts else f"OK: no {kind} spans")
sys.exit(1 if fail else 0)
PYEOF
then
  FAIL=1
fi

echo
echo "=== pop scan (single-frame diff spikes, downscaled 180x180 gray, sampled at the render's own ==="
echo "=== fps — CPU-light) — REPORT only: every other check above FAILs, this one deliberately does ==="
echo "=== not, because an intentional quick cut/flash-edit can trip the same signature (see ==="
echo "=== scripts/pop_scan.py module docstring for why) ==="
if [ -z "$EXPECT_FPS" ] || [ "$EXPECT_FPS" = "0" ]; then
  echo "SKIP: no expected fps available to sample at"
else
  ffmpeg -hide_banner -v error -i "$MP4" -vf "fps=$EXPECT_FPS,scale=180:180,format=gray" -f rawvideo - \
    | python3 "$(dirname "$0")/pop_scan.py" --fps "$EXPECT_FPS"
  POP_FFMPEG_RC=${PIPESTATUS[0]}
  if [ "$POP_FFMPEG_RC" != 0 ]; then
    echo "SKIP: ffmpeg failed to decode frames for pop scan (exit $POP_FFMPEG_RC) — not run, not clean"
  fi
fi

echo
if [ "$FAIL" != 0 ]; then
  echo "verify_render FAIL — see FAIL lines above; do not ship this render"
  exit 4
fi
echo "verify_render clean"
