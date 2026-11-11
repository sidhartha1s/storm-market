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
The whole run holds the heavy lock (render_busy.heavy_lock), so no TTS, e2e or other render runs between two acts and
no other run restages the act file while this one waits; each act's render.cmd passes through on HEAVY_LOCK_TOKEN.
render.cmd writes render_<mode>_done.marker after EVERY act and the audio pass: poll render_acts_<out-basename>_done.marker
instead, which holds this run's exit code (0 only once the concat is checked) and is deleted when the run starts.
"""
import hashlib
import html as html_lib
import json
import math
import os
import re
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
import render_busy  # noqa: E402

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


def _set_attr(tag, name, value):
    """The start tag with attribute name set to value: replaced where it is, else added before the tag's close."""
    pat = re.compile(r"""\s%s=(?:(["']).*?\1|[^\s"'>]+)""" % re.escape(name), re.S)
    new = f' {name}="{html_lib.escape(value)}"'  # HTMLParser hands values back unescaped
    return pat.sub(lambda m: new, tag, count=1) if pat.search(tag) else re.sub(r"\s*/?>$", lambda m: new + m.group(0), tag, count=1)


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
    """index.html as a composition of frames [fa, fb): times shifted by fa/fps, everything outside it parked and
    hidden (audible media on the act's edges)."""
    p = _Timed(html)
    a, dur = fa / fps, (fb - fa) / fps
    total = float(p.root["attrs"]["data-duration"])
    edits = []  # (start, end, replacement), applied back to front
    for el in p.els:
        s, e = _span(el)
        audible = el["tag"] == "audio" or (el["tag"] == "video" and "muted" not in el["attrs"]
                                           and el["attrs"].get("data-has-audio", "true") == "true")
        if _needs_trim(el) and s < a < e and el["tag"] != "audio":
            raise SystemExit(f"render_acts: #{el['attrs'].get('id')} starts before the act at {a:.3f} s; "
                             "that seam is not clean")
        tag = html[el["start"]:el["tag_end"]]
        if e <= a or s >= a + dur:
            # Nothing outside the act is dropped. hyperframes decides from the whole compiled page whether to open its
            # browser probe (any media without data-start, scripted volume, ...), and the probe sweeps the root
            # timeline (video visibility 0 to the end at 0.1 s, audio windows at 1/fps, events suppressed, then 0),
            # leaving every graphic's timeline initialised and rewound. Dropping the sub-composition that triggers it
            # (Moore: g-a3-tiles' radar video has no data-start) left graphics in their authored state: PR 223
            # defects 1 and 2. Parked elements are hidden so they never paint (defect 3). Audible media parks on
            # the act's first or last frame, where the audio sweep rewinds or finishes this act's graphics as the
            # single render's sweep does from before or after the act.
            if audible and s < total:
                start = 0.0 if e <= a else dur - 1 / fps
                tag = _set_attr(tag, "data-duration", repr(1 / fps))
            else:  # the runtime does not honour a negative data-start: park past the act's end
                start = dur + 1 if e <= a else s - a
            css = el["attrs"].get("style", "").strip().rstrip(";")
            tag = _set_attr(_set_attr(tag, "style", (css + "; " if css else "") + "display: none !important"),
                            "data-act-parked", "")
        else:
            start = max(s - a, 0.0)  # one running through the seam starts at 0 with the rest of its length
            if s < a and el["tag"] == "audio":
                # starts on the audio sweep's first sample inside the act, so every sample lands where the single
                # render's does; its sound moves with it
                start = math.ceil((a - s) * fps - 1e-9) / fps + s - a
                if start >= e - a:  # it ends before that sample: keep a real length, the sweep sees it at 0
                    start = 0.0
                tag = _set_attr(tag, "data-media-start", repr(float(el["attrs"].get("data-media-start", 0)) + a + start - s))
            if s < a and "data-duration" in el["attrs"]:
                tag = _set_attr(tag, "data-duration", repr(e - a - start))
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
    edits.append((body_end, body_end, POST % {"id": json.dumps(root["attrs"]["data-composition-id"]), "a": a}))
    out = html
    for s, e, rep in sorted(edits, key=lambda x: (x[0], x[1]), reverse=True):
        out = out[:s] + rep + out[e:]
    return out


LOCAL_REF = re.compile(r'''(?:src|href|data-composition-src)=["']([^"'#:]+)["']|url\(["']?([^"')#:]+)''')


PARKED = re.compile(r"<[^>]*\sdata-act-parked=[^>]*>")
# hyperframes' probeRequiresBrowser triggers that a sub-composition can carry (producer probeStage.ts)
PROBE_TRIGGERS = (r"<(?:video|audio)\b(?![^>]*\sdata-start=)[^>]*>", r"\.\s*volume\s*=",
                  r"\b(?:gsap|tl|timeline|tween)\s*\.\s*(?:to|fromTo|set)\s*\([\s\S]{0,2000}\bvolume\s*:",
                  r"""\bcreateElement\s*\(\s*["'`](?:video|audio)["'`]\s*\)""", r"\bnew\s+(?:Audio|Video)\s*\(")


def _local_files(base, text):
    """Every local file text references, and the files those html/css files reference in turn."""
    seen, todo = set(), [(base, text)]
    while todo:
        base, text = todo.pop()
        for m in LOCAL_REF.finditer(text):
            path = (base / (m.group(1) or m.group(2)).strip()).resolve()
            if path in seen or not path.is_file():
                continue
            seen.add(path)
            if path.suffix in (".html", ".css"):
                todo.append((path.parent, path.read_text(encoding="utf-8", errors="replace")))
    return seen


def fingerprint(staged, ep, mode, fps):
    """Everything that decides an act's pixels: the slice and every local file its own elements load, by content
    (optimize_clips.py rewrites media in place, so a name alone is not enough). What parked elements load counts
    only through the hyperframes probe triggers it carries, so a fix in another act keeps this act reusable.
    shortcut: audio inside a parked sub-composition is neither moved to the act's edge nor hashed; no episode
    mounts audio in a graphic today, revisit if one does."""
    h = hashlib.sha256()
    for part in (mode, str(fps), os.environ.get("RENDER_CRF", ""), RENDER_CMD.read_bytes().decode("utf-8"), staged):
        h.update(part.encode("utf-8"))
    own = _local_files(ep, PARKED.sub("", staged))
    for path in sorted(own):
        h.update(str(path.relative_to(ep.resolve()) if path.is_relative_to(ep.resolve()) else path).encode("utf-8"))
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(1 << 20), b""):
                h.update(chunk)
    parked = [x.read_text(encoding="utf-8", errors="replace") for x in _local_files(ep, "".join(PARKED.findall(staged)))
              - own if x.suffix in (".html", ".js")]
    h.update(repr([any(re.search(t, x) for x in parked) for t in PROBE_TRIGGERS]).encode("utf-8"))
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
    if render_preflight.stamp_refusal(ep):  # before the basename is claimed; each act's render.cmd checks it again
        raise SystemExit(7)
    old = json.loads((renders / "acts" / reuse / "plan.json").read_text()) if reuse else {"acts": []}
    old_by_key = {(x["frames"][0], x["frames"][1], x["fingerprint"]): x["file"] for x in old["acts"]}
    pieces.mkdir(parents=True)  # claims the basename before the wait for the lock
    marker = ep / f"render_acts_{base}_done.marker"
    marker.unlink(missing_ok=True)
    try:
        with render_busy.heavy_lock(f"render_acts {slug} {mode} {base}"):
            render_all(slug, mode, ep, fps, html, acts, old_by_key, pieces, out)
    except BaseException:
        marker.write_text("1\n")
        raise
    marker.write_text("0\n")


def render_all(slug, mode, ep, fps, html, acts, old_by_key, pieces, out):
    base, renders = pieces.name, out.parent
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
            log = (pieces / f"act{i:02d}.log").read_text(encoding="utf-8", errors="replace")  # render.cmd's copy
            if "NVIDIA" not in log:  # verify_render.sh's GPU check, which would otherwise see only the audio pass
                raise SystemExit(f"render_acts: act{i:02d} did not render on the NVIDIA GPU; see {pieces / f'act{i:02d}.log'}")
        got = video_frames(path)
        if got != fb - fa:
            raise SystemExit(f"render_acts: act{i:02d} has {got} frames, expected {fb - fa}")
        plan["acts"].append({"frames": [fa, fb], "fingerprint": fp, "file": path})
        (pieces / "plan.json").write_text(json.dumps(plan, indent=1))
    run_render(slug, mode, f"acts/{base}/audio", "index.html", {"RENDER_FPS": str(AUDIO_FPS)})
    # verify_render.sh reads these beside the output: the act fps, not the 1 fps pass's; the audio pass's log, as before
    (renders / f"{base}.fps").write_text(f"{fps}\n")
    (renders / f"{base}.log").write_bytes((pieces / "audio.log").read_bytes())
    listing = pieces / "concat.txt"
    listing.write_text("".join(f"file '{Path(x['file']).as_posix()}'\n" for x in plan["acts"]))
    total = acts[-1][1]
    subprocess.run(["ffmpeg", "-v", "error", "-n", "-f", "concat", "-safe", "0", "-i", str(listing),
                    "-i", str(pieces / "audio.mp4"), "-map", "0:v", "-map", "1:a", "-c", "copy",
                    "-t", repr(total / fps), "-movflags", "+faststart", str(out)], check=True)
    got = video_frames(out)
    audio = float(subprocess.run(["ffprobe", "-v", "error", "-select_streams", "a:0", "-show_entries", "stream=duration",
                                  "-of", "csv=p=0", str(out)], capture_output=True, text=True, check=True).stdout)
    if got != total or audio < (total - 1) / fps:
        raise SystemExit(f"render_acts: {out.name} has {got} frames and {audio:.3f} s of sound, expected {total} frames")
    print(f"OK {out} ({total} frames, {len(acts)} acts)")


if __name__ == "__main__":
    main(sys.argv[1:])
