#!/usr/bin/env bash
# Post-render verification. Usage: verify_render.sh <episode-dir> <render-basename>
# Everything here reads the finished mp4 — the checks that do not need pixels already ran
# before the render (sweep_episode.py, blank_scan.mjs, beat_density.py, graphics_qc.mjs).
set -u
EP="$1"; BASE="$2"
MP4="$EP/renders/$BASE.mp4"
[ -f "$MP4" ] || { echo "MISSING $MP4"; exit 1; }
FAIL=0

echo "=== gpu (owner 2026-09-15: capture must run on the dedicated GPU, never the Intel iGPU) ==="
LOG="$EP/render_full.log"; [ "$BASE" != "${BASE%draft*}" ] && LOG="$EP/render_draft.log"
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

echo
echo "=== artifact vs composition (duration/fps/resolution/audio must match — a truncated, ==="
echo "=== downgraded or muted render used to exit 0 here) ==="
ffprobe -v error -show_entries format=duration,size,bit_rate \
        -show_entries stream=codec_name,codec_type,width,height,r_frame_rate,nb_frames \
        -of default=noprint_wrappers=1 "$MP4" | tee /tmp/_probe.txt
HAS_AUDIO=$(ffprobe -v error -select_streams a -show_entries stream=codec_type -of csv=p=0 "$MP4")
if ! python3 - "$COMP_W" "$COMP_H" "$COMP_DUR" "$COMP_FPS" "$HAS_AUDIO" <<'PYEOF'
import re, sys
comp_w, comp_h, comp_dur, comp_fps, has_audio = sys.argv[1:6]
probe = open("/tmp/_probe.txt", encoding="utf-8", errors="replace").read()
def field(name):
    m = re.search(rf'^{name}=(.+)$', probe, re.MULTILINE)
    return m.group(1) if m else None
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
    if str(fps) != comp_fps:
        print(f"FAIL: fps {fps} != composition {comp_fps}fps (a draft mastered by mistake?)")
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
echo "=== black spans (d>=0.4s, pix_th 0.10) ==="
ffmpeg -hide_banner -i "$MP4" -vf "blackdetect=d=0.4:pix_th=0.10" -an -f null - 2>&1 \
  | grep -a "black_start" | sed 's/.*black_start/black_start/' | tee /tmp/_black.txt
echo "black spans: $(wc -l < /tmp/_black.txt)"
# Owner's own duration table (CLAUDE.md "Chapter blackout"): 0.6-0.9s = chapter break,
# 1.0-1.3s = dramatic punctuation (the CTA's dip_in/dip_out, config.yaml, land here), 1.5s+ =
# dead air — a bug, not a style. Gate on that threshold, never on the raw span COUNT: chapter
# blackouts are intentional and their count varies per episode, so "zero black" would fail
# every real episode.
LONGEST_BLACK=$(grep -oa 'black_duration:[0-9.]*' /tmp/_black.txt | cut -d: -f2 | sort -g | tail -1)
if [ -n "$LONGEST_BLACK" ] && python3 -c "import sys; sys.exit(0 if float('$LONGEST_BLACK') >= 1.5 else 1)"; then
  echo "FAIL: a ${LONGEST_BLACK}s black span is dead air (owner threshold: 1.5s+), not a chapter break"
  FAIL=1
fi

echo
echo "=== silent spans (audio dropout, -50dB for 2s+) ==="
ffmpeg -hide_banner -i "$MP4" -af "silencedetect=n=-50dB:d=2" -f null - 2>&1 \
  | grep -a "silence_start" | tee /tmp/_silence.txt | tail -20
if [ -s /tmp/_silence.txt ]; then
  echo "FAIL: $(wc -l < /tmp/_silence.txt) silence span(s) of 2s+ at -50dB or below — a dropped narration segment or dead audio"
  FAIL=1
fi

echo
echo "=== freeze detection (no visible change for 6s+) ==="
ffmpeg -hide_banner -i "$MP4" -vf "freezedetect=n=-58dB:d=6" -an -f null - 2>&1 \
  | grep -a "freeze_start" | tee /tmp/_freeze.txt | tail -20
if [ -s /tmp/_freeze.txt ]; then
  echo "FAIL: $(wc -l < /tmp/_freeze.txt) frozen span(s) of 6s+ — a frozen clip"
  FAIL=1
fi

echo
if [ "$FAIL" != 0 ]; then
  echo "verify_render FAIL — see FAIL lines above; do not ship this render"
  exit 4
fi
echo "verify_render clean"
