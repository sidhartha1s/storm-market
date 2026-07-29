#!/usr/bin/env bash
# Post-render verification. Usage: verify_render.sh <episode-dir> <render-basename>
# Everything here reads the finished mp4 — the checks that do not need pixels already ran
# before the render (sweep_episode.py, blank_scan.mjs, beat_density.py, graphics_qc.mjs).
set -u
EP="$1"; BASE="$2"
MP4="$EP/renders/$BASE.mp4"
[ -f "$MP4" ] || { echo "MISSING $MP4"; exit 1; }

echo "=== artifact ==="
ffprobe -v error -show_entries format=duration,size,bit_rate \
        -show_entries stream=codec_name,width,height,r_frame_rate,nb_frames \
        -of default=noprint_wrappers=1 "$MP4"

echo
echo "=== black spans (d>=0.4s, pix_th 0.10) ==="
ffmpeg -hide_banner -i "$MP4" -vf "blackdetect=d=0.4:pix_th=0.10" -an -f null - 2>&1 \
  | grep -a "black_start" | sed 's/.*black_start/black_start/' | tee /tmp/_black.txt
echo "black spans: $(wc -l < /tmp/_black.txt)"

echo
echo "=== silent spans (audio dropout, -50dB for 2s+) ==="
ffmpeg -hide_banner -i "$MP4" -af "silencedetect=n=-50dB:d=2" -f null - 2>&1 \
  | grep -a "silence_start" | tail -20

echo
echo "=== freeze detection (no visible change for 6s+) ==="
ffmpeg -hide_banner -i "$MP4" -vf "freezedetect=n=-58dB:d=6" -an -f null - 2>&1 \
  | grep -a "freeze_start" | tail -20
