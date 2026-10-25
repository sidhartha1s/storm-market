#!/usr/bin/env python3
"""Render an episode act by act, so a fix re-renders only the act it touched (skeptic finding 4, owner sk_4 26 Oct 26).

hyperframes 0.8.185 has no local frame-range render, so each act is its own staged composition: a copy of index.html
whose timing is shifted to start at the act. Seams sit in the middle of the chapter blackouts (`section.blackout`),
cut on a frame. Picture is rendered per act (its audio is discarded); the sound comes from ONE pass over the whole
composition at 1 fps (the mix does not depend on the frame rate), so beds that cross a seam stay one mix.
Every render goes through scripts\\render.cmd (preflight, render_busy, stream gate) with RENDER_COMPOSITION set.

Usage (launch hidden: wscript scripts\\run_hidden.vbs python3 scripts\\render_acts.py ...):
  python3 scripts/render_acts.py <slug> <draft|full> <out-basename> [--reuse <older-basename>] [--plan]
Each act lands in renders/acts/<out-basename>/actNN.mp4 with a fingerprint of everything that decides its pixels
(staged slice, the sub-compositions it mounts, render.cmd, mode, fps). With --reuse, an act whose fingerprint matches
the older run's is taken from there instead of rendered. Output: renders/<out-basename>.mp4. Nothing is overwritten.
--plan prints the seams and exits.
"""
import hashlib
import json
import os
import re
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
RENDER_CMD = SCRIPTS / "render.cmd"
STAGE_NAME = "_act_tmp.html"  # the next plain render.cmd run sweeps _*_tmp.html
AUDIO_FPS = 1
FRAME_EPS = 1e-3  # hyperframes durationToFrameCount: within 1e-3 of a whole frame rounds, else ceil
MEDIA_TAGS = {"audio", "video"}
VOID_TAGS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}


def mode_fps(mode):
    """The fps render.cmd uses for this mode (its _FPS defaults, RENDER_FPS overrides); test_render_acts pins them."""
    return int(os.environ.get("RENDER_FPS") or {"draft": 15, "full": 30}[mode])


def frame_count(duration, fps):
    raw = duration * fps
    return round(raw) if abs(raw - round(raw)) <= FRAME_EPS else int(raw) + 1


class _Timed(HTMLParser):
    """Every element inside the root carrying data-start, with its source span and nesting."""

    def __init__(self, html):
        super().__init__(convert_charrefs=False)
        self.lines = [0]
        for line in html.splitlines(keepends=True):
            self.lines.append(self.lines[-1] + len(line))
        self.stack, self.els, self.root = [], [], None
        self.feed(html)

    def _off(self):
        line, col = self.getpos()
        return self.lines[line - 1] + col

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        start = self._off()
        tag_end = start + len(self.get_starttag_text())
        el = {"tag": tag, "attrs": a, "start": start, "tag_end": tag_end, "end": tag_end, "children": 0}
        if self.stack:
            self.stack[-1]["children"] += 1
        if self.root is None and "data-composition-id" in a and "data-duration" in a:
            self.root = el
        elif self.root is not None and "data-start" in a:
            el["parent"] = next((p for p in reversed(self.stack) if p in self.els), None)
            self.els.append(el)
        if tag not in VOID_TAGS:
            self.stack.append(el)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID_TAGS:
            self.stack.pop()

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i]["tag"] == tag:
                for el in self.stack[i:]:
                    el["end"] = self._off() + len(f"</{tag}>")
                del self.stack[i:]
                return

    def handle_data(self, data):
        if self.stack and data.strip():
            self.stack[-1]["children"] += 1


def _span(el):
    s = float(el["attrs"]["data-start"])
    d = el["attrs"].get("data-duration")
    return s, (s + float(d)) if d else float("inf")


def _needs_trim(el):
    """Media and sub-composition hosts cannot start before the act: their source offset would have to move."""
    return el["tag"] in MEDIA_TAGS or "data-composition-src" in el["attrs"]


def plan_acts(html, fps):
    """Frame ranges [start, end) per act. A blackout's middle frame is a seam unless media or a host spans it."""
    p = _Timed(html)
    total = frame_count(float(p.root["attrs"]["data-duration"]), fps)
    cuts, skipped = [], []
    for el in p.els:
        if el["tag"] == "audio" or "blackout" not in el["attrs"].get("class", "").split():
            continue
        s, e = _span(el)
        cut = round((s + e) / 2 * fps)
        spanning = [o["attrs"].get("id", o["tag"]) for o in p.els
                    if o["tag"] != "audio" and _needs_trim(o) and _span(o)[0] < cut / fps < _span(o)[1]]
        (skipped if spanning else cuts).append((cut, el["attrs"].get("id"), spanning))
    edges = [0] + sorted({c for c, _, _ in cuts if 0 < c < total}) + [total]
    return list(zip(edges, edges[1:])), skipped


PRE = """<script>/* render_acts: authored scripts read the original times */
document.querySelectorAll("[data-act-src-start]").forEach(function (el) {
  el.setAttribute("data-start", el.getAttribute("data-act-src-start")); });
</script>
"""
POST = """<script>/* render_acts: back to act time; the root timeline's children move to act time */
document.querySelectorAll("[data-act-src-start]").forEach(function (el) {
  el.setAttribute("data-start", el.getAttribute("data-act-start")); });
(function () {
  var A = %(a)r, tl = window.__timelines && window.__timelines[%(id)s];
  if (!tl) return;
  var kids = tl.getChildren(false, true, true), done = [], later = [];
  kids.forEach(function (c) {
    var s = c.startTime(), e = s + c.totalDuration();
    if (s >= A) { later.push(c); return; }
    tl.remove(c);
    if (e <= A) { done.push(c); return; }
    var d = gsap.timeline({ paused: true });  // spans the seam: play it from A on
    d.add(c, 0);
    tl.add(d.tweenFromTo(A - s, e - s, { duration: e - A, ease: "none", immediateRender: true }), 0);
  });
  // GSAP shifts every child when one starts before 0, so finished ones apply their end state once, in order
  done.sort(function (x, y) { return x.endTime() - y.endTime(); })
      .forEach(function (c) { c.totalTime(c.totalDuration(), true); });
  later.forEach(function (c) { c.startTime(c.startTime() - A); });
})();
</script>
"""


def slice_html(html, fa, fb, fps):
    """index.html as a composition of frames [fa, fb): times shifted by fa/fps, media and hosts outside it dropped."""
    p = _Timed(html)
    a, dur = fa / fps, (fb - fa) / fps
    edits = []  # (start, end, replacement), applied back to front
    dropped = []
    for el in p.els:
        if any(d["start"] <= el["start"] < d["end"] for d in dropped):
            continue
        s, e = _span(el)
        if el["tag"] == "audio" or (_needs_trim(el) and (e <= a or s >= a + dur)):
            dropped.append(el)
            edits.append((el["start"], el["end"], ""))
            continue
        if _needs_trim(el) and s < a:
            raise SystemExit(f"render_acts: #{el['attrs'].get('id')} starts before the act at {a:.3f} s; "
                             "that seam is not clean")
        # the runtime does not honour a negative data-start: an element over before the act parks past its end,
        # one running through the seam starts at 0 with the rest of its length
        start = dur + 1 if e <= a else max(s - a, 0.0)
        tag = html[el["start"]:el["tag_end"]]
        if s < a < e and "data-duration" in el["attrs"]:
            tag = re.sub(r'\bdata-duration="[^"]*"', f'data-duration="{e - a!r}"', tag, count=1)
        new = re.sub(r'\bdata-start="[^"]*"', f'data-start="{start!r}" data-act-start="{start!r}" '
                     f'data-act-src-start="{el["attrs"]["data-start"]}"', tag, count=1)
        edits.append((el["start"], el["tag_end"], new))
    root = p.root
    root_tag = re.sub(r'\bdata-duration="[^"]*"', f'data-duration="{dur!r}"', html[root["start"]:root["tag_end"]], count=1)
    edits.append((root["start"], root["tag_end"], root_tag))
    first_script = html.find("<script", root["tag_end"])
    body_end = html.rfind("</body>")
    if first_script < 0 or first_script > body_end:
        first_script = body_end
    edits.append((first_script, first_script, PRE))
    edits.append((body_end, body_end, POST % {"id": json.dumps(root["attrs"]["data-composition-id"]),
                                              "a": a, "b": a + dur, "dur": dur}))
    out = html
    for s, e, rep in sorted(edits, key=lambda x: (x[0], x[1]), reverse=True):
        out = out[:s] + rep + out[e:]
    return out


LOCAL_REF = re.compile(r'''(?:src|href|data-composition-src)=["']([^"'#:]+)["']|url\(["']?([^"')#:]+)''')


def fingerprint(staged, ep, mode, fps):
    """Everything that decides an act's pixels: the slice and every local file it or its mounts load, by content
    (optimize_clips.py rewrites media in place, so a name alone is not enough)."""
    h = hashlib.sha256()
    for part in (mode, str(fps), os.environ.get("RENDER_CRF", ""), RENDER_CMD.read_bytes().decode("utf-8"), staged):
        h.update(part.encode("utf-8"))
    seen, todo = set(), [(ep, staged)]
    while todo:
        base, text = todo.pop()
        for m in LOCAL_REF.finditer(text):
            path = (base / (m.group(1) or m.group(2)).strip()).resolve()
            if path in seen or not path.is_file():
                continue
            seen.add(path)
            if path.suffix in (".html", ".css"):
                todo.append((path.parent, path.read_text(encoding="utf-8", errors="replace")))
    for path in sorted(seen):
        h.update(str(path.relative_to(ep.resolve()) if path.is_relative_to(ep.resolve()) else path).encode("utf-8"))
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(1 << 20), b""):
                h.update(chunk)
    return h.hexdigest()[:16]


def run_render(slug, mode, base, composition, extra_env=None):
    env = dict(os.environ, RENDER_COMPOSITION=composition, **(extra_env or {}))
    rc = subprocess.run(["cmd", "/c", str(RENDER_CMD), slug, mode, base], env=env,
                        creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0)).returncode
    if rc:
        raise SystemExit(f"render_acts: render.cmd {slug} {mode} {base} exited {rc}; see the episode's render_{mode}*.log")


def video_frames(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-count_packets",
                          "-show_entries", "stream=nb_read_packets", "-of", "csv=p=0", str(path)],
                         capture_output=True, text=True, check=True).stdout
    return int(out.strip())


def main(argv):
    args = [x for x in argv if not x.startswith("--")]
    reuse = argv[argv.index("--reuse") + 1] if "--reuse" in argv else None
    if reuse:
        args.remove(reuse)
    if len(args) != 3 or args[1] not in ("draft", "full"):
        raise SystemExit(__doc__)
    slug, mode, base = args
    ep = SCRIPTS.parent / "episodes" / slug
    fps = mode_fps(mode)
    html = (ep / "index.html").read_text(encoding="utf-8")
    acts, skipped = plan_acts(html, fps)
    for cut, bo, spanning in skipped:
        print(f"seam skipped at {bo} (frame {cut}): spanned by {', '.join(spanning)}")
    for i, (fa, fb) in enumerate(acts, 1):
        print(f"act{i:02d}: frames {fa}-{fb} ({fa / fps:.3f}-{fb / fps:.3f} s)")
    if "--plan" in argv:
        return
    renders = ep / "renders"
    out = renders / f"{base}.mp4"
    pieces = renders / "acts" / base
    if out.exists() or pieces.exists():
        raise SystemExit(f"render_acts: {out.name} or acts/{base} exists; never overwritten, pick a new basename")
    old = json.loads((renders / "acts" / reuse / "plan.json").read_text()) if reuse else {"acts": []}
    old_by_key = {(x["frames"][0], x["frames"][1], x["fingerprint"]): x["file"] for x in old["acts"]}
    pieces.mkdir(parents=True)
    plan = {"mode": mode, "fps": fps, "acts": []}
    for i, (fa, fb) in enumerate(acts, 1):
        staged = slice_html(html, fa, fb, fps)
        fp = fingerprint(staged, ep, mode, fps)
        hit = old_by_key.get((fa, fb, fp))
        if hit:
            print(f"act{i:02d}: unchanged, reused {hit}")
            path = hit
        else:
            (ep / STAGE_NAME).write_text(staged, encoding="utf-8")
            run_render(slug, mode, f"acts/{base}/act{i:02d}", STAGE_NAME)
            path = str(pieces / f"act{i:02d}.mp4")
            log = (ep / f"render_{mode}.log").read_text(encoding="utf-8", errors="replace")
            (pieces / f"act{i:02d}.log").write_text(log, encoding="utf-8")  # the next render overwrites the episode log
            if "NVIDIA" not in log:  # verify_render.sh's GPU check, which would otherwise see only the audio pass
                raise SystemExit(f"render_acts: act{i:02d} did not render on the NVIDIA GPU; see {pieces / f'act{i:02d}.log'}")
        got = video_frames(path)
        if got != fb - fa:
            raise SystemExit(f"render_acts: act{i:02d} has {got} frames, expected {fb - fa}")
        plan["acts"].append({"frames": [fa, fb], "fingerprint": fp, "file": path})
        (pieces / "plan.json").write_text(json.dumps(plan, indent=1))
    run_render(slug, mode, f"acts/{base}/audio", "index.html", {"RENDER_FPS": str(AUDIO_FPS)})
    (ep / f"render_{mode}.fps").write_text(f"{fps}\n")  # verify_render.sh checks the output against this, not the 1 fps pass
    listing = pieces / "concat.txt"
    listing.write_text("".join(f"file '{Path(x['file']).as_posix()}'\n" for x in plan["acts"]))
    total = acts[-1][1]
    subprocess.run(["ffmpeg", "-v", "error", "-n", "-f", "concat", "-safe", "0", "-i", str(listing),
                    "-i", str(pieces / "audio.mp4"), "-map", "0:v", "-map", "1:a", "-c", "copy",
                    "-t", repr(total / fps), "-movflags", "+faststart", str(out)], check=True)
    got = video_frames(out)
    if got != total:
        raise SystemExit(f"render_acts: {out.name} has {got} frames, expected {total}")
    print(f"OK {out} ({total} frames, {len(acts)} acts)")


if __name__ == "__main__":
    main(sys.argv[1:])
