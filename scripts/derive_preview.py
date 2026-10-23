"""derive_preview.py (SKETCH, not implemented; design: docs/design/preview-render.md).

Stage a gitignored preview page that renders one time window of an episode at a small viewport.
Usage (the render.cmd `preview` branch, not yet written):
    python3 scripts/derive_preview.py <episode-dir> <window-spec> [height]
Writes <ep>/_preview_tmp.html and <ep>/_preview_tmp.html.json, prints "t0 t1 out-basename".

Never writes index.html or compositions/*.html. Content-blind: reads only tag, id, the time attributes, whether
data-composition-src is present, and byte spans; writes only time attributes, whole-element drops, the root's size
and duration, one stage wrapper div and one fixed injected script. Both self-checks run on every call, so a derive that ever needs to know
what a beat means fails on its own output.
"""
from __future__ import annotations

import sys
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Literal

PAGE = "_preview_tmp.html"            # render.cmd's `del /q _*_tmp.html` already sweeps it before every draft/full
MANIFEST = PAGE + ".json"
Height = Literal[360, 540, 720, 1080]  # 360 is the owner's ask; 1080 = window only, no stage wrapper

# The time attributes the plan models. Any other time-like data-* on a timed element is a refusal, never a guess.
MODELED = ("data-start", "data-end", "data-duration", "data-media-start", "data-playback-start")


class DeriveError(Exception):
    """A refusal at the boundary. The message names the element id and attribute; render.cmd logs it."""


@dataclass(frozen=True)
class Window:
    """Episode seconds. Invariant 0 <= t0 < t1 <= duration. Built only by parse_window or snap_t0."""
    t0: float
    t1: float


class Kind(Enum):
    MEDIA = "media"   # <video>/<audio>: the producer schedules them node-side from attributes; trimmable
    HOST = "host"     # data-composition-src: a sub-composition cannot be trimmed, so t0 snaps to its start
    CLIP = "clip"     # any other element with data-start: start/duration editable


@dataclass(frozen=True)
class Timed:
    """One ROOT-page element with a numeric data-start (sub-composition files are never parsed).
    Invariants: start >= 0; HOST always has an end; tag_span = start tag, elem_span = whole element."""
    kind: Kind
    id: str
    start: float
    end: float | None
    media_start_attr: Literal["data-media-start", "data-playback-start"] | None
    media_start: float
    tag_span: tuple[int, int]
    elem_span: tuple[int, int]


@dataclass(frozen=True)
class Root:
    """The single page-level [data-composition-id]. A second one is a refusal."""
    comp_id: str
    duration: float
    tag_span: tuple[int, int]


@dataclass(frozen=True)
class PreviewPlan:
    """The whole decision as data; apply_plan only turns it into text.
    Invariants: edits and drops never overlap; window.t0 <= requested.t0 (snapped left, never right);
    the injected block carries exactly window.t0 and window.t1."""
    requested: Window
    window: Window
    height: Height
    edits: tuple[tuple[tuple[int, int], str, str], ...]   # (tag_span, attribute, new value)
    drops: tuple[tuple[int, int], ...]                     # elem_spans fully outside the window
    injected: str
    kept_files: tuple[str, ...]                            # media + comps still referenced: the manifest


@dataclass(frozen=True)
class StagedPreview:
    page: Path
    manifest: Path
    window: Window
    out_basename: str   # "<slug>-preview-<t0>-<t1>": owner timestamp on the preview + t0 = episode time


# ---- boundary: parse into domain types, refuse what the plan does not model ----

def parse_window(spec: str, rows: list[dict], duration: float) -> Window:
    """'all' | 'a3' (act token, from timeline.json row-id prefixes: id grammar, not meaning) | 'mm:ss-mm:ss' |
    '552-830.5'. Clamps t1 to duration; refuses t0 >= t1."""
    raise NotImplementedError


def read_root(html: str) -> Root:
    raise NotImplementedError


def read_timed(html: str) -> list[Timed]:
    """Every root-page element with data-start, in document order (html.parser offsets). Refuses a non-numeric
    time attribute, a HOST without data-duration, data-playback-rate, or any time-like attribute outside MODELED."""
    raise NotImplementedError


# ---- pure core ----

def snap_t0(t0: float, timed: list[Timed]) -> float:
    """Move t0 left until no HOST straddles it. Terminates: strictly decreasing over a finite set; 0 is safe."""
    raise NotImplementedError


def plan_preview(root: Root, timed: list[Timed], requested: Window, height: Height) -> PreviewPlan:
    """Interval arithmetic only, with w = (snap_t0(requested.t0), requested.t1):
    drop end <= w.t0 or start >= w.t1; kept elements shift data-start/data-end by -w.t0; MEDIA straddling w.t0
    gets start 0 and media-start += w.t0 - start; anything straddling w.t1 is cut to w.t1; root data-duration =
    w.t1 - w.t0; height < 1080 sets root data-width = 1920*h/1080, data-height = h and wraps the root's children
    in stage_open(height)."""
    raise NotImplementedError


def preview_block(comp_id: str, window: Window, height: Height) -> str:
    """The fixed clock shim, first in <head> (window [14, 20] on demo-pin matched the whole render, 23 Oct 26):
    <script>window.__timelines = new Proxy({}, {set(o,k,v){ if(k===ID && v && !v.__hfPreview){
      const outer = gsap.timeline({paused:true}); outer.add(v.tweenFromTo(T0, T1, {ease:"none"}), 0);
      outer.__hfPreview = true; v = outer; } o[k] = v; return true; }});</script>
    Below 1080 the root's children are also wrapped in the stage div (see stage_open), never `html{zoom}`:
    zoom drew only the top-left 213x120 px."""
    raise NotImplementedError


def stage_open(height: Height) -> str:
    """'<div id="hf-preview-stage" style="position:absolute; left:0; top:0; width:1920px; height:1080px;
    transform:scale(h/1080); transform-origin:0 0">', inserted right after the root's start tag and closed right
    before its end tag. One wrapper, so GSAP's inline transforms on clips never meet it. Empty string at 1080."""
    raise NotImplementedError


def apply_plan(html: str, plan: PreviewPlan) -> str:
    """Apply drops and edits from the end of the text backwards (spans stay valid), then insert the block."""
    raise NotImplementedError


# ---- self-checks, run inside stage_preview on every call ----

def assert_content_blind(original: str, derived: str, plan: PreviewPlan) -> None:
    """Reverse exactly the plan and require byte equality with the original."""
    raise NotImplementedError


def assert_identity(html: str) -> None:
    """Window 'all' at 1080 changes nothing but the injected block. Also the committed unit test on demo-pin."""
    raise NotImplementedError


# ---- shell ----

def stage_preview(ep: Path, spec: str, height: Height = 360) -> StagedPreview:
    """Read index.html (never write it), plan, apply, self-check, write PAGE and MANIFEST. Idempotent."""
    raise NotImplementedError


def main(argv: list[str]) -> int:
    """<episode-dir> <window-spec> [height]. Exit 2 with the DeriveError message on a refusal."""
    raise NotImplementedError


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
