import re, io

path = r"C:\Users\Sidhartha\Automation Projects\storm-market\.worktrees\root-docs-audit\LEARNINGS.md"
raw = open(path, "rb").read().decode("utf-8")
lines = raw.split("\r\n")
# raw ends with \r\n right after last content line -> split gives trailing "" element
assert lines[-1] == ""
lines = lines[:-1]  # drop trailing empty from final split

total_lines = len(lines)
assert total_lines == 1065, total_lines

# find all header line indices (0-based) matching "^## "
header_idx = [i for i, l in enumerate(lines) if l.startswith("## ")]

# preamble = lines[0:header_idx[0]]
preamble = lines[0:header_idx[0]]

# build sections: each section = lines[header_idx[k] : header_idx[k+1]] (or end)
sections = []
for k, hi in enumerate(header_idx):
    end = header_idx[k+1] if k+1 < len(header_idx) else total_lines
    sec_lines = lines[hi:end]
    header = sec_lines[0]
    m = re.search(r"(\d{4}-\d{2}-\d{2})", header)
    assert m, f"no date in header: {header}"
    date = m.group(1)
    sections.append({"header": header, "date": date, "lines": sec_lines})

print("total sections:", len(sections))

# block boundary: first section whose header is the "## ep3 v2 (2026-07-28)" line
boundary_header = "## ep3 v2 (2026-07-28)"
boundary_i = next(i for i, s in enumerate(sections) if s["header"] == boundary_header)
print("boundary section index:", boundary_i, sections[boundary_i]["header"])

A = sections[:boundary_i]      # already newest-first
B = sections[boundary_i:]      # oldest-first -> reverse it
B_rev = list(reversed(B))

combined = A + B_rev
# stable sort descending by date (Python sort is stable -> ties keep combined order)
combined_sorted = sorted(combined, key=lambda s: s["date"], reverse=True)

# sanity: multiset of headers unchanged
assert sorted(s["header"] for s in combined_sorted) == sorted(s["header"] for s in sections)
assert len(combined_sorted) == len(sections)

# verify monotonic non-increasing dates top to bottom
dates = [s["date"] for s in combined_sorted]
mono_ok = all(dates[i] >= dates[i+1] for i in range(len(dates)-1))
print("monotonic non-increasing:", mono_ok)

# Build the promoted-rules index block (present tense, no dates, pointer to header)
index_rules = [
    ("The ebook CTA is a must-keep contract: hook > CTA > payoff, landing 30\u201340% into runtime, from `config.yaml channel.cta`.",
     "the ebook CTA is a channel asset + a must-keep contract"),
    ("The 1440p HEVC file is the YouTube upload artifact; re-run the master gain/limiter step on any owner-supplied cut before the 2K upscale, never bit-copy its audio.",
     "1440p upload file is HEVC now"),
    ("mp4 surgery on a finished render uses h264_nvenc first, never libx264 \u2014 the quality gap doesn't survive YouTube's transcode at consumer-master bitrates.",
     "1440p upload tier + NVENC-first for mp4 surgery"),
    ("Convert GIFs before mounting (single-frame \u2192 PNG, animated \u2192 mp4); every mounted video needs an audio stream \u2014 mux silence into mute clips.",
     "ep6 render-failure ledger"),
    ("Audio slots longer than their file are silently truncated (WARN, not FAIL) \u2014 read the WARNs of a failed render; clip windows must never exceed the real clip length.",
     "ep6 render-failure ledger"),
    ("Batch every owner approval ask into ONE message, as early as possible \u2014 scattered mid-run checkpoints don't reliably land.",
     "ep6 owner rules + broadcast-geometry gotchas"),
    ("The hook must contain zero muted/mediocre elements \u2014 every beat is mid-action with its own audio.",
     "ep6 owner rules + broadcast-geometry gotchas"),
    ("Video-range black is Y=16, not 0 \u2014 threshold pillarbox/blanking detectors at \u226417, or use cropdetect.",
     "ep6 owner rules + broadcast-geometry gotchas"),
    ("Broadcast compilation reels have per-segment geometry \u2014 run cropdetect per cut window, never one blanket crop per reel.",
     "ep6 owner rules + broadcast-geometry gotchas"),
    ("Budget scripts on the previous episode's manifest wpm, then verify against the new manifest after the first full TTS run \u2014 probe-TTS only catches gross errors.",
     "ep6 TTS + sourcing"),
    ("Scene picking from long reels goes through contact sheets first \u2014 never per-frame agent probing.",
     "ep6 TTS + sourcing"),
    ("Scripts are written on the retention lattice (`references/script-scaling.md`) \u2014 read it before writing any script.",
     "ep5 kickoff: the retention lattice + script fact-QC layer"),
    ("Script fact-QC closes every `[verify]` marker before TTS runs; a conditional fact that fails verification gets cut, never softened.",
     "ep5 kickoff: the retention lattice + script fact-QC layer"),
    ("Every audio-carrying insert is transcribed in full before cut selection; the cut lands on the transcript's action/emotion peak.",
     "ep5 kickoff: the retention lattice + script fact-QC layer"),
    ("The hook has no black start \u2014 frame one is already mid-action, anchor audio already mid-transmission.",
     "ep5 kickoff: the retention lattice + script fact-QC layer"),
    ("The generator tripwire: any script that authors episode HTML (chooses cuts, holds, graphics, timings) is forbidden \u2014 delete it on sight.",
     "CHECKPOINT: revert to the ep2 method"),
    ("The full hook contract lives in DESIGN.md \u2014 apply it from episode scene one, don't rediscover it.",
     "ep2 hook rebuild + ship"),
    ("`--workers` must be pinned on every full render, never left on \"auto\".",
     "ep2 hook rebuild + ship"),
    ("Shipping while another session holds `.git/index.lock`: work from a `git worktree add`, never touch the main checkout.",
     "ep2 hook rebuild + ship"),
    ("Insert/AV cuts land on sentence boundaries via transcript, always \u2014 never mid-sentence.",
     "ep2 v1 owner review"),
    ("Verify each CUT, not just the source video \u2014 extract a frame from the cut itself and check chyrons/landmarks against the claimed event.",
     "ep2 v1 owner review"),
    ("The draft-proxy render (`--quality draft --crf 32 --fps 15 --workers 3`) is the mandatory review path; full-quality renders only after the owner approves the draft.",
     "draft-proxy render validated"),
    ("Cadence is reasoned per clip, never defaulted \u2014 any hold over ~8s needs a written reason; no visual repeats within an episode outside a flagged callback.",
     "owner review of ep1 v1"),
    ("The sync rule: the frame on screen must never contradict the narration (named entity / time-of-day / timestamp \u21d2 a matching or neutral visual).",
     "owner review of ep1 v1"),
    ("Never claim an editorial rule \"fixed\" from memory \u2014 re-run the lint/checks on the actual final file before claiming it.",
     "RCA: \"repeats fixed\" claim was FALSE"),
    ("Exhaust every static gate, then render once \u2014 a render is the last step, never a diagnostic tool.",
     "ep3 v3 \u2014 stop rendering to find things a script can find"),
    ("Run blackdetect on every render \u2014 the picture track can be empty while every static gate (lint, graphics_qc, hyperframes check) still passes.",
     "ep3 v3 \u2014 the defects no code gate was looking for"),
    ("`grep -o ' id=\"[^\"]*\"' index.html | sort | uniq -d` must print nothing before every render \u2014 duplicate element ids render black with no gate catching it.",
     "Duplicate element ids render BLACK"),
    ("`optimize_clips.py` must preserve audio and mux silence for mute clips; ffprobe every insert clip for an audio stream before rendering.",
     "optimize_clips.py strips audio and ignores bitrate"),
    ("Long renders launch via schtasks (or `run_hidden.vbs`), never harness background Bash \u2014 the reaped child tree dies silently mid-capture.",
     "Harness background tasks get reaped"),
    ("Stills run 3\u20136s max, always with motion; video beats may run up to 12\u201315s when the clip genuinely matches the narration.",
     "Owner pivot 2026-08-12"),
    ("The doctor rule: a known-below-spec deliverable means STOP before the render, state exactly what's broken, and wait \u2014 never render on a known defect.",
     "The doctor rule"),
    ("Count SOURCES, not cuts, when sourcing \u2014 assertion assets (broadcast pulls, official audio, survivor clips) beat another angle of the same b-roll.",
     "Sourcing doctrine for future episodes"),
    ("The full audio-mixdown scan (volumedetect on 30s windows) is a mandatory pre-render gate, not optional.",
     "Audio mixdown as a pre-render gate"),
    ("`scripts/audio_levels.py` is the gate for insert/narration/bed levels \u2014 run it before every mixdown build.",
     "Audio levels + media budget hardening"),
    ("No visible windows, ever \u2014 every scheduled/background command runs through `scripts/run_hidden.vbs`.",
     "No visible windows, ever"),
    ("The on-screen text rules (zone occupancy, one fact one instance, no decorative eyebrows, glass under text over footage) live in DESIGN.md \u2014 `overlap_check.mjs` v2 enforces them.",
     "ep6 draft v2 review \u2014 text collisions were a CHECKER false negative"),
    ("hyperframes 0.8.x opens visible console windows on this box \u2014 the pin stays 0.7.109 until an upstream version spawns ffmpeg/ffprobe hidden.",
     "ep6 ship"),
    ("Search `library/catalog-index.json` / `npx hyperframes catalog --query` before hand-authoring any graphic \u2014 MG library-first.",
     "ep6 ship"),
]
print("index rule count:", len(index_rules))
assert len(index_rules) <= 40

index_block_lines = []
index_block_lines.append("## Promoted rules index")
index_block_lines.append("")
index_block_lines.append("Standing rules still governing episode quality, compacted from the journal below. Each")
index_block_lines.append("line is a pointer, not a copy \u2014 find the full context by searching the journal for the")
index_block_lines.append("quoted section header.")
index_block_lines.append("")
for rule_text, header_phrase in index_rules:
    index_block_lines.append(f"- {rule_text} \u2192 \u00a7\u201c{header_phrase}\u201d")
index_block_lines.append("")

print("index block line count (incl heading/blank):", len(index_block_lines))

# Assemble final file
out_lines = []
out_lines.extend(preamble)
out_lines.extend(index_block_lines)
for s in combined_sorted:
    out_lines.extend(s["lines"])

out_text = "\r\n".join(out_lines) + "\r\n"

out_path = r"C:\Users\Sidhartha\Automation Projects\storm-market\.worktrees\root-docs-audit\.scratch_new_learnings.md"
open(out_path, "wb").write(out_text.encode("utf-8"))

# ---- verification ----
# 1) body content unchanged (multiset of section-body lines, ignoring order) matches original
orig_body_lines = []
for s in sections:
    orig_body_lines.extend(s["lines"])
new_body_lines = []
for s in combined_sorted:
    new_body_lines.extend(s["lines"])
print("orig body line count:", len(orig_body_lines))
print("new body line count:", len(new_body_lines))
print("body lines identical as multiset:", sorted(orig_body_lines) == sorted(new_body_lines))
print("body total char count orig:", sum(len(l) for l in orig_body_lines))
print("body total char count new:", sum(len(l) for l in new_body_lines))

print("preamble unchanged:", preamble == lines[0:header_idx[0]])

print("OLD total lines:", total_lines)
print("OLD total bytes:", len(raw.encode('utf-8')))
print("NEW total lines:", len(out_lines))
print("NEW total bytes:", len(out_text.encode('utf-8')))
