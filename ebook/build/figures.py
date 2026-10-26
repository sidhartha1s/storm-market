#!/usr/bin/env python3
"""figures.py — original, code-drawn diagrams for The Storm-Ready Home.

Every figure is inline SVG (or, where the content is a text comparison, plain HTML boxes
built from book.css's own component classes), self-contained, print-safe, and drawn to a
fixed height so paginate.mjs can measure it exactly like any other atomic block. No raster
images, no external fonts, no stock art, no AI imagery — see manuscript/P8-credits.md.

Colour and type come from book.css's :root variables via var(...) rather than hard-coded
hex, so a figure never forks the palette (`figures.py` is loaded into pages that already
carry book.css — the variables are always in scope).

Usage:
    from figures import render_figure, FIGURES
    html = render_figure("safe-room-plan")   # -> one <figure>...</figure> string

FIGURES is the manifest paginate.mjs / blocks_pipeline.py needs to resolve a
`«FIG: id»` marker to HTML, and that this module's own preview harness
(figures_preview.py) walks to build a full proof set. Each entry:
    id             — the token used in a manuscript «FIG: id» marker
    number         — sequential figure number as it prints ("Figure 4")
    caption        — the figcaption sentence (no "Figure N —" prefix; render_figure adds it)
    justification  — one line: what this figure does that the prose next to it cannot
    file           — manuscript file the anchor lives in
    protection     — protection number(s) the figure illustrates, for cross-reference

No number appears in any figure below unless it is already published, cited prose
elsewhere in this same manuscript (see the justification/source note on each render
function) — nothing here is estimated or approximated for the sake of a nicer picture.

Figures 14 on are the large-print set for older readers (senior review 2026-10-27): drawn
in points (viewBox width 342 = the 4.76in content width, so 1 unit = 1pt at print size),
system serif, nothing under 11pt. Figures 25-28 are the one exception to "no raster": they
point at art/illustrations/<id>.png, and render_figure raises if that file is missing.
"""
from pathlib import Path

ART_DIR = Path(__file__).parent / "art" / "illustrations"

# ---------------------------------------------------------------------------
# shared constants — book.css custom properties, referenced live (never hex-forked)
# ---------------------------------------------------------------------------
INK = "var(--ink)"
INK_SOFT = "var(--ink-soft)"
INK_MUTE = "var(--ink-mute)"
RULE = "var(--rule)"
PAPER = "var(--paper)"
AMBER = "var(--amber)"
AMBER_BG = "var(--amber-bg)"
ALERT = "var(--alert)"
SANS = "'Segoe UI', Arial, sans-serif"


def _svg(viewbox, height_in, label, body):
    """Wrap an SVG body. Fixed height + width:auto (centered) is the sample.html
    convention (Figures 23.1 / 74.1 in build/sample.html) — it gives paginate.mjs a
    deterministic box regardless of the figure's internal viewBox units."""
    return (f'<svg viewBox="0 0 {viewbox[0]} {viewbox[1]}" '
            f'style="height:{height_in}in;width:auto;margin:0 auto;display:block" '
            f'role="img" aria-label="{label}">{body}</svg>')


def _figure(number, caption, inner_html):
    return (f'<figure><b class="fignum" style="display:none">{number}</b>{inner_html}'
            f'<figcaption><b>Figure {number}</b> — {caption} Original diagram.</figcaption>'
            f'</figure>')


def _text(x, y, s, size=8, weight=400, color=INK_MUTE, anchor="start", family=SANS, italic=False):
    style = "italic" if italic else "normal"
    return (f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" '
            f'font-weight="{weight}" font-style="{style}" '
            f'text-anchor="{anchor}" style="fill:{color}">{s}</text>')


def _label_dot(x, y, r=3, color=AMBER):
    return f'<circle cx="{x}" cy="{y}" r="{r}" style="fill:{color}"/>'


# ---------------------------------------------------------------------------
# Figure 1 — Safe room selection (Protection 23) — MANDATORY, sold by name
# ---------------------------------------------------------------------------
def fig_safe_room_plan():
    body = f'''
    <rect x="6" y="6" width="328" height="116" stroke-width="2.5" style="fill:none;stroke:{INK}"/>
    <line x1="118" y1="6" x2="118" y2="78" stroke-width="1.6" style="stroke:{INK}"/>
    <line x1="118" y1="78" x2="232" y2="78" stroke-width="1.6" style="stroke:{INK}"/>
    <line x1="232" y1="6" x2="232" y2="78" stroke-width="1.6" style="stroke:{INK}"/>
    <line x1="232" y1="40" x2="334" y2="40" stroke-width="1.6" style="stroke:{INK}"/>
    <rect x="118" y="40" width="114" height="38" stroke-width="2" style="fill:{AMBER_BG};stroke:{AMBER}"/>
    {_text(175, 63, "SAFE ROOM", size=10, weight=700, color=AMBER, anchor="middle")}
    <g stroke-width="2.4" style="stroke:{ALERT}">
      <line x1="30" y1="6" x2="66" y2="6"/><line x1="84" y1="6" x2="108" y2="6"/>
      <line x1="6" y1="52" x2="6" y2="88"/><line x1="334" y1="60" x2="334" y2="96"/>
      <line x1="150" y1="122" x2="190" y2="122"/><line x1="248" y1="122" x2="286" y2="122"/>
    </g>
    {_text(60, 30, "bedroom", size=8)}
    {_text(280, 28, "kitchen", size=8, anchor="end")}
    {_text(280, 104, "living", size=8, anchor="end")}
    {_text(46, 104, "garage", size=8)}
    <g transform="translate(6,140)">
      <line x1="0" y1="0" x2="18" y2="0" stroke-width="2.4" style="stroke:{ALERT}"/>
      {_text(24, 3, "exterior window or door — the safe room touches none", size=7.6)}
    </g>
    '''
    return _figure(1, "Floor plan of a safe-room choice: an interior room carved from the "
                   "center of the house, walled on every side by other rooms, with no "
                   "exterior wall and no window (red) of its own.",
                   _svg((360, 160), 1.35, "Floor plan showing an interior safe room with zero exterior walls", body))


# ---------------------------------------------------------------------------
# Figure 2 — The three rooms (Form 12; serves Protections 23, 26, 29)
# ---------------------------------------------------------------------------
def fig_three_rooms():
    # Every rule below is inline (no <style> block, no CSS classes, no SVG <marker>/<defs>
    # outside an <svg> wrapper) and every card gets an explicit fixed height rather than
    # relying on flex cross-axis stretch — both were found, on inspection of the first
    # render, to be fragile under Chrome's headless layout at this box size.
    CARD_H = "1.6in"

    def card(title, icon_svg, lines, accent):
        items = "".join(
            f'<div style="font-size:7.2pt;line-height:1.32;color:{INK_SOFT};margin-bottom:2pt">{ln}</div>'
            for ln in lines
        )
        return (
            f'<div style="flex:1 1 0;box-sizing:border-box;height:{CARD_H};overflow:hidden;'
            f'border:.75pt solid {accent};padding:6pt 7pt;background:#fff;font-family:{SANS}">'
            f'<div style="margin-bottom:3pt">{icon_svg}</div>'
            f'<div style="font-size:7.4pt;font-weight:700;letter-spacing:.03em;'
            f'text-transform:uppercase;margin-bottom:4pt;color:{accent}">{title}</div>'
            f'{items}</div>'
        )

    icon_safe = (
        f'<svg viewBox="0 0 40 40" style="width:26px;height:26px;display:block">'
        f'<rect x="4" y="4" width="32" height="32" stroke-width="2.5" style="fill:none;stroke:{INK}"/>'
        f'<rect x="13" y="13" width="14" height="14" stroke-width="2.5" style="fill:{AMBER_BG};stroke:{AMBER}"/>'
        f'</svg>'
    )
    icon_warm = (
        f'<svg viewBox="0 0 40 40" style="width:26px;height:26px;display:block">'
        f'<rect x="4" y="14" width="32" height="22" stroke-width="2.5" style="fill:none;stroke:{INK}"/>'
        f'<circle cx="20" cy="8" r="6" stroke-width="2" style="fill:none;stroke:{ALERT}"/>'
        f'<g stroke-width="1.6" style="stroke:{ALERT}">'
        f'<line x1="20" y1="0" x2="20" y2="2"/>'
        f'<line x1="10" y1="4" x2="12" y2="6"/>'
        f'<line x1="30" y1="4" x2="28" y2="6"/>'
        f'</g></svg>'
    )
    icon_cool = (
        f'<svg viewBox="0 0 40 40" style="width:26px;height:26px;display:block">'
        f'<rect x="4" y="10" width="32" height="26" stroke-width="2.5" style="fill:none;stroke:{INK}"/>'
        f'<path d="M2 18 L14 18 L10 14 M14 18 L10 22" stroke-width="1.6" style="fill:none;stroke:{AMBER}"/>'
        f'<path d="M38 28 L26 28 L30 24 M26 28 L30 32" stroke-width="1.6" style="fill:none;stroke:{AMBER}"/>'
        f'</svg>'
    )

    cards = (
        card("Safe room &middot; P23", icon_safe,
             ["Lowest floor.", "Zero exterior walls.", "No picture windows.", "For: wind, minutes"], ALERT)
        + card("Warm room &middot; P26", icon_warm,
               ["Interior, small.", "South window for daytime sun.", "Body heat does the rest.",
                "For: cold outage, days"], AMBER)
        + card("Cooling room &middot; P29", icon_cool,
               ["Lowest floor, north side.", "Fewest windows, cross-flow.",
                "Fans exhaust; don't aim at you.", "For: heat outage, days"], INK_SOFT)
    )
    inner = (f'<div style="display:flex;gap:8pt;box-sizing:border-box;height:{CARD_H}">'
             f'{cards}</div>')
    return (f'<figure>{inner}'
            f'<figcaption><b>Figure 2</b> — One house, three different best rooms. The room that '
            f'protects you from wind is not the room that keeps you warm, which is not the room '
            f'that keeps you cool &mdash; the criteria conflict on purpose. Original diagram.</figcaption>'
            f'</figure>')


# ---------------------------------------------------------------------------
# Figure 3 — Shut-off literacy (Protection 35)
# ---------------------------------------------------------------------------
def fig_utility_shutoffs():
    body = f'''
    <path d="M20 90 L140 20 L260 90 Z" stroke-width="2" style="fill:none;stroke:{INK}"/>
    <rect x="40" y="90" width="200" height="90" stroke-width="2.2" style="fill:none;stroke:{INK}"/>
    <line x1="40" y1="140" x2="240" y2="140" stroke-width="1.2" stroke-dasharray="3,3" style="stroke:{INK_MUTE}"/>
    {_text(244, 137, "main floor", size=7, color=INK_MUTE)}
    {_text(244, 176, "basement / crawlspace", size=7, color=INK_MUTE)}
    <rect x="330" y="150" width="26" height="26" stroke-width="1.6" style="fill:none;stroke:{INK}"/>
    {_text(343, 168, "P", size=9, weight=700, anchor="middle")}
    {_text(322, 195, "electrical panel", size=7.4, anchor="end")}
    <line x1="330" y1="163" x2="240" y2="163" stroke-width="1.4" stroke-dasharray="2,2" style="stroke:{AMBER}"/>
    <circle cx="16" cy="130" r="7" stroke-width="2" style="fill:none;stroke:{ALERT}"/>
    {_text(16, 133, "G", size=8, weight=700, anchor="middle", color=ALERT)}
    {_text(2, 112, "gas shut-off,", size=7.4, color=ALERT)}
    {_text(2, 121, "wrench hangs here", size=7.4, color=ALERT)}
    <line x1="20" y1="123" x2="40" y2="128" stroke-width="1.2" stroke-dasharray="2,2" style="stroke:{ALERT}"/>
    <circle cx="66" cy="180" r="7" stroke-width="2" style="fill:none;stroke:{AMBER}"/>
    {_text(66, 183, "W", size=7, weight=700, anchor="middle", color=AMBER)}
    {_text(66, 205, "water main shut-off", size=7.4, anchor="middle", color=AMBER)}
    '''
    return _figure(3, "Three shut-offs, three different places in the same house. Find and "
                   "label all three before you need one — locations vary by house; this shows "
                   "the pattern, not your address.",
                   _svg((360, 220), 1.55, "House cross-section marking the gas, water main, and electrical shut-offs", body))


# ---------------------------------------------------------------------------
# Figure 4 — The water heater as a reserve (Protection 4)
# ---------------------------------------------------------------------------
def fig_water_heater_drawoff():
    def step(n, x, y, text_lines):
        t = "".join(_text(x + 15, y + 3 + i * 9.5, ln, size=7.2) for i, ln in enumerate(text_lines))
        return (f'<circle cx="{x}" cy="{y}" r="8" style="fill:{AMBER}"/>'
                f'{_text(x, y + 3, str(n), size=8.5, weight=700, color=PAPER, anchor="middle")}{t}')

    body = f'''
    <rect x="196" y="34" width="74" height="150" rx="8" stroke-width="2.4" style="fill:none;stroke:{INK}"/>
    <path d="M212 34 v-14 h-14" stroke-width="1.6" style="stroke:{INK};fill:none"/>
    <rect x="184" y="12" width="12" height="12" stroke-width="1.6" style="fill:none;stroke:{INK}"/>
    {_text(180, 10, "cold inlet valve", size=6.8, anchor="end")}
    <path d="M256 34 v-12 h30" stroke-width="1.6" style="stroke:{INK};fill:none"/>
    <rect x="288" y="16" width="10" height="10" stroke-width="1.4" style="fill:none;stroke:{INK}"/>
    {_text(302, 24, "hot tap opened", size=6.8)}
    {_text(302, 33, "elsewhere", size=6.8)}
    <rect x="224" y="184" width="18" height="10" stroke-width="1.6" style="fill:none;stroke:{INK}"/>
    <path d="M233 194 v10 h20" stroke-width="1.6" style="stroke:{INK};fill:none"/>
    {_text(233, 216, "drain valve", size=6.8, anchor="middle")}
    {_text(233, 225, "&rarr; clean container", size=6.8, anchor="middle")}
    {_text(233, 245, "gas pilot / breaker off at the base first", size=6.8, color=INK_MUTE, anchor="middle")}
    {step(1, 30, 24, ["kill the energy &mdash;", "gas pilot or breaker"])}
    {step(2, 30, 66, ["shut the cold-water", "inlet at the tank"])}
    {step(3, 30, 108, ["open a hot tap", "elsewhere, to admit air"])}
    {step(4, 30, 150, ["draw from the drain", "valve into a container"])}
    {step(5, 30, 192, ["do not refill or", "re-energize until safe"])}
    <line x1="40" y1="24" x2="184" y2="18" stroke-width="1" stroke-dasharray="2,2" style="stroke:{INK_MUTE}"/>
    <line x1="40" y1="66" x2="196" y2="70" stroke-width="1" stroke-dasharray="2,2" style="stroke:{INK_MUTE}"/>
    <line x1="40" y1="108" x2="288" y2="21" stroke-width="1" stroke-dasharray="2,2" style="stroke:{INK_MUTE}"/>
    <line x1="40" y1="150" x2="224" y2="188" stroke-width="1" stroke-dasharray="2,2" style="stroke:{INK_MUTE}"/>
    '''
    return _figure(4, "The five-step draw-off sequence in order, and where each valve is on the "
                   "tank — a conventional water heater holds forty to eighty gallons of potable "
                   "water most households never think to use.",
                   _svg((380, 260), 1.85, "Water heater schematic showing the five-step draw-off sequence", body))


# ---------------------------------------------------------------------------
# Figure 5 — Garage door bracing (Protection 74)
# ---------------------------------------------------------------------------
def fig_garage_door_pressure():
    body = f'''
    <g>
      <rect x="14" y="34" width="150" height="70" stroke-width="2" style="fill:#f2efe9;stroke:{INK}"/>
      <path d="M14 34 L89 10 L164 34" stroke-width="2" style="fill:none;stroke:{INK}"/>
      <rect x="36" y="58" width="106" height="46" stroke-width="1.4" style="fill:#fff;stroke:{INK}"/>
      <g stroke-width="1.6" style="stroke:{INK_MUTE}"><line x1="0" y1="74" x2="30" y2="74"/><line x1="0" y1="88" x2="30" y2="88"/></g>
      {_text(89, 118, "braced &mdash; 16 ft door holds", size=7.6, anchor="middle")}
      {_text(89, 127, "pressure stays outside", size=7.6, anchor="middle")}
    </g>
    <g>
      <rect x="214" y="34" width="150" height="70" stroke-width="2" style="fill:#f2efe9;stroke:{INK}"/>
      <path d="M210 30 L289 4 L368 30" stroke-width="2.4" style="fill:none;stroke:{ALERT}"/>
      <path d="M240 58 l106 0 l-16 46 l-74 0z" stroke-width="1.6" style="fill:{AMBER_BG};stroke:{ALERT}"/>
      <g stroke-width="1.8" style="stroke:{ALERT}">
        <line x1="268" y1="98" x2="268" y2="66"/><line x1="289" y1="100" x2="289" y2="62"/><line x1="310" y1="98" x2="310" y2="66"/>
      </g>
      {_text(289, 118, "breached &mdash; wind fills house,", size=7.6, anchor="middle", color=ALERT)}
      {_text(289, 127, "roof loaded from inside", size=7.6, anchor="middle", color=ALERT)}
    </g>
    '''
    return _figure(5, "A double garage door is sixteen feet of unsupported sheet metal. Braced "
                   "or rated (left), the wind stays outside. Breached (right), it pressurizes "
                   "the house and loads the roof deck from underneath.",
                   _svg((380, 138), 1.15, "Comparison of a braced versus breached garage door under wind load", body))


# ---------------------------------------------------------------------------
# Figure 6 — Ember-resistant vents / Zone 0, and defensible space (P76, P77)
# ---------------------------------------------------------------------------
def fig_defensible_space_zones():
    body = f'''
    <rect x="10" y="52" width="34" height="34" stroke-width="2.2" style="fill:none;stroke:{INK}"/>
    <path d="M10 52 L27 38 L44 52" stroke-width="2.2" style="fill:none;stroke:{INK}"/>
    <rect x="44" y="30" width="26" height="106" stroke-width="1.4" style="fill:{ALERT};fill-opacity:0.16;stroke:{ALERT}"/>
    {_text(57, 24, "ZONE 0", size=7.2, weight=700, anchor="middle", color=ALERT)}
    {_text(57, 150, "0&ndash;5 ft", size=7.2, anchor="middle", color=ALERT)}
    <rect x="70" y="30" width="120" height="106" stroke-width="1.4" style="fill:{AMBER};fill-opacity:0.14;stroke:{AMBER}"/>
    {_text(130, 24, "ZONE 1", size=7.2, weight=700, anchor="middle", color=AMBER)}
    {_text(130, 150, "5&ndash;30 ft &mdash; thinned, irrigated", size=7.2, anchor="middle", color=AMBER)}
    <rect x="190" y="30" width="150" height="106" stroke-width="1.4" style="fill:{INK_MUTE};fill-opacity:0.12;stroke:{INK_MUTE}"/>
    {_text(265, 24, "ZONE 2", size=7.2, weight=700, anchor="middle", color=INK_SOFT)}
    {_text(265, 150, "30&ndash;100 ft &mdash; ladder fuels removed", size=7.2, anchor="middle", color=INK_SOFT)}
    <path d="M340 40 l14 -6 l0 4 l10 0 l0 4 l-10 0 l0 4 z" style="fill:{INK_MUTE}"/>
    {_text(358, 30, "scale compressed", size=6.6, color=INK_MUTE)}
    {_text(358, 39, "past 30 ft", size=6.6, color=INK_MUTE)}
    <line x1="44" y1="90" x2="10" y2="90" stroke-width="1" style="stroke:{INK}"/>
    '''
    return _figure(6, "The three bands California statute defines around a structure: an "
                   "ember-resistant Zone 0 to five feet, thinned and irrigated Zone 1 to thirty "
                   "feet, and a thinned (not cleared) Zone 2 to one hundred feet.",
                   _svg((380, 165), 1.35, "Cutaway diagram of defensible space zones 0, 1, and 2 around a house", body))


# ---------------------------------------------------------------------------
# Figure 7 — Flood openings and wet floodproofing (Protection 80)
# ---------------------------------------------------------------------------
def fig_flood_openings():
    body = f'''
    <line x1="6" y1="150" x2="374" y2="150" stroke-width="1.2" style="stroke:{INK_MUTE}"/>
    {_text(378, 153, "grade", size=7, color=INK_MUTE)}
    <rect x="90" y="60" width="200" height="90" stroke-width="2.2" style="fill:#f2efe9;stroke:{INK}"/>
    <rect x="6" y="96" width="84" height="8" stroke-width="1.4" style="fill:{AMBER_BG};stroke:{AMBER}"/>
    {_text(48, 92, "water outside", size=7, anchor="middle", color=AMBER)}
    <rect x="290" y="96" width="84" height="8" stroke-width="1.4" style="fill:{AMBER_BG};stroke:{AMBER}"/>
    {_text(332, 92, "water inside", size=7, anchor="middle", color=AMBER)}
    <rect x="110" y="128" width="22" height="14" stroke-width="1.8" style="fill:none;stroke:{ALERT}"/>
    <rect x="248" y="128" width="22" height="14" stroke-width="1.8" style="fill:none;stroke:{ALERT}"/>
    <path d="M90 135 h20 M132 135 h20" stroke-width="1.4" marker-end="url(#fo-arrow)" style="stroke:{ALERT}"/>
    <path d="M228 135 h20 M270 135 h20" stroke-width="1.4" marker-end="url(#fo-arrow)" style="stroke:{ALERT}"/>
    <defs><marker id="fo-arrow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <path d="M0,0 L6,3 L0,6 z" style="fill:{ALERT}"/></marker></defs>
    {_text(190, 30, "minimum two openings, engineered to equalize pressure", size=7.6, anchor="middle", weight=700, color=ALERT)}
    <line x1="121" y1="128" x2="150" y2="46" stroke-width="1" stroke-dasharray="2,2" style="stroke:{INK_MUTE}"/>
    <line x1="259" y1="128" x2="230" y2="46" stroke-width="1" stroke-dasharray="2,2" style="stroke:{INK_MUTE}"/>
    {_text(190, 172, "opening bottom &le; 1 ft above grade &middot; net free area &ge; 1 sq in per sq ft enclosed", size=7.2, anchor="middle", color=INK_SOFT)}
    '''
    return _figure(7, "Flood vents let water move through an enclosure instead of pushing "
                   "against it — sealing the wall creates the pressure differential that "
                   "collapses it. Three numbers are the federal minimum (44 CFR 60.3(c)(5)).",
                   _svg((384, 190), 1.45, "Cross-section of a crawlspace enclosure with engineered flood openings equalizing water pressure", body))


# ---------------------------------------------------------------------------
# Figure 8 — CO and smoke alarm placement (Protections 47, 48)
# ---------------------------------------------------------------------------
def fig_alarm_placement():
    def alarm(x, y, label, color=AMBER):
        return (f'<circle cx="{x}" cy="{y}" r="7" stroke-width="2" style="fill:{PAPER};stroke:{color}"/>'
                f'{_text(x, y + 3, label, size=7, weight=700, anchor="middle", color=color)}')

    body = f'''
    <path d="M20 44 L170 12 L320 44" stroke-width="2" style="fill:none;stroke:{INK}"/>
    <rect x="20" y="44" width="300" height="70" stroke-width="2" style="fill:none;stroke:{INK}"/>
    <line x1="130" y1="44" x2="130" y2="114" stroke-width="1.2" style="stroke:{INK_MUTE}"/>
    <line x1="210" y1="44" x2="210" y2="114" stroke-width="1.2" style="stroke:{INK_MUTE}"/>
    {_text(75, 60, "bedroom", size=7, anchor="middle", color=INK_MUTE)}
    {_text(170, 60, "hallway", size=7, anchor="middle", color=INK_MUTE)}
    {_text(265, 60, "bedroom", size=7, anchor="middle", color=INK_MUTE)}
    {_text(170, 40, "upper floor", size=7, anchor="middle", color=INK_MUTE)}
    {alarm(75, 52, "S")}
    {alarm(265, 52, "S")}
    {alarm(170, 52, "C+S")}
    <rect x="20" y="114" width="300" height="60" stroke-width="2" style="fill:none;stroke:{INK}"/>
    {_text(170, 108, "main floor", size=7, anchor="middle", color=INK_MUTE)}
    {alarm(170, 122, "C+S")}
    <rect x="20" y="174" width="300" height="46" stroke-width="2" style="fill:none;stroke:{INK}"/>
    {_text(170, 168, "basement", size=7, anchor="middle", color=INK_MUTE)}
    {alarm(170, 182, "C")}
    <g transform="translate(20,232)">
      {alarm(8, 0, "S", color=AMBER)}{_text(20, 3, "smoke &mdash; every bedroom, every level", size=7.4)}
      {alarm(180, 0, "C", color=AMBER)}{_text(192, 3, "CO &mdash; every level, outside sleeping areas", size=7.4)}
    </g>
    '''
    return _figure(8, "Alarm placement by level, not by guess: a smoke alarm in every bedroom, "
                   "a combination unit outside each sleeping area, and one of each on every "
                   "floor including the basement.",
                   _svg((340, 250), 1.85, "House cross-section showing smoke and carbon monoxide alarm placement by floor", body))


# ---------------------------------------------------------------------------
# Figure 9 — The box-fan filter build (Protection 50)
# ---------------------------------------------------------------------------
def fig_box_fan_filter():
    def filt(x):
        return (f'<rect x="{x}" y="24" width="10" height="110" stroke-width="1.6" style="fill:#fff;stroke:{INK}"/>'
                f'<path d="M{x+5} 40 v18" stroke-width="1.6" marker-end="url(#bf-arrow)" style="stroke:{AMBER}"/>'
                f'<path d="M{x+5} 78 v18" stroke-width="1.6" marker-end="url(#bf-arrow)" style="stroke:{AMBER}"/>'
                f'<path d="M{x+5} 96 v-18" stroke-width="0"/>')

    body = f'''
    <defs><marker id="bf-arrow" markerWidth="6" markerHeight="6" refX="3" refY="5" orient="auto">
      <path d="M0,0 L6,0 L3,6 z" style="fill:{AMBER}"/></marker></defs>
    {filt(60)}{filt(76)}{filt(92)}{filt(108)}
    <path d="M60 24 h58 M60 134 h58" stroke-width="2" stroke-dasharray="3,2" style="stroke:{ALERT}"/>
    {_text(89, 16, "tape seals every seam", size=6.8, anchor="middle", color=ALERT)}
    <circle cx="210" cy="79" r="46" stroke-width="2.2" style="fill:none;stroke:{INK}"/>
    <rect x="164" y="33" width="92" height="92" stroke-width="2.2" style="fill:none;stroke:{INK}"/>
    <path d="M256 40 L300 20 L300 138 L256 118" stroke-width="1.6" style="fill:{AMBER_BG};stroke:{AMBER}"/>
    {_text(300, 12, "cardboard shroud", size=7, anchor="middle", color=AMBER)}
    {_text(300, 152, "reduces recirculation", size=7, anchor="middle", color=AMBER)}
    {_text(210, 79, "&#8594;", size=20, anchor="middle", weight=700)}
    {_text(133, 150, "4 filters, arrows pointing into the fan", size=7.2, anchor="middle")}
    {_text(210, 150, "box fan, 2012+", size=7.2, anchor="middle")}
    {_text(210, 160, "(fused plug)", size=7.2, anchor="middle")}
    '''
    return _figure(9, "Exploded view of the build: four filters facing the same way, seams "
                   "taped, a cardboard shroud on the outlet side. EPA-tested as effective as a "
                   "small commercial cleaner; dirty filters were not.",
                   _svg((340, 170), 1.4, "Exploded diagram of a box-fan filter build showing filter orientation and shroud", body))


# ---------------------------------------------------------------------------
# Figure 10 — The hurricane cone, and what it does not mean (Protection 90)
# ---------------------------------------------------------------------------
def fig_hurricane_cone():
    body = f'''
    <path d="M10 90 C 120 20, 260 20, 380 -10 L380 190 C 260 160, 120 160, 10 90 Z"
      stroke-width="1.2" stroke-dasharray="3,2" style="fill:{AMBER};fill-opacity:0.12;stroke:{AMBER}"/>
    {_text(190, 8, "actual hazard extent &mdash; surge, rain, tornadoes", size=7.6, anchor="middle", color=AMBER, weight=700)}
    <path d="M10 90 L380 30 L380 150 Z" stroke-width="1.8" style="fill:{INK};fill-opacity:0.14;stroke:{INK}"/>
    <line x1="10" y1="90" x2="380" y2="90" stroke-width="1.2" stroke-dasharray="2,2" style="stroke:{INK}"/>
    {_text(190, 84, "cone: probable path of the storm's CENTER only", size=7.6, anchor="middle", weight=700)}
    <circle cx="10" cy="90" r="5" style="fill:{INK}"/>
    {_text(10, 108, "now", size=7, anchor="middle")}
    <circle cx="392" cy="176" r="4" style="fill:{ALERT}"/>
    {_text(392, 190, "actual track,", size=6.8, anchor="end", color=ALERT)}
    <path d="M375 165 L392 176" stroke-width="1.2" style="stroke:{ALERT}"/>
    {_text(190, 205, "&asymp;1 in 3 times, the storm's center ends up outside the cone (NHC, 5-yr sample)", size=7.4, anchor="middle", color=INK_SOFT)}
    '''
    return _figure(10, "The cone shows where the storm's center is likely to track. It says "
                   "nothing about where the wind, rain, surge, or tornadoes reach — and about "
                   "one time in three, even the center ends up outside it.",
                   _svg((400, 215), 1.6, "Diagram contrasting the narrow hurricane forecast cone with the much wider actual hazard extent", body))


# ---------------------------------------------------------------------------
# Figure 11 — Severe thunderstorm damage-threat tiers (hail/derecho chapter)
# ---------------------------------------------------------------------------
def fig_hail_damage_tiers():
    body = f'''
    <rect x="10" y="140" width="100" height="30" stroke-width="1.6" style="fill:none;stroke:{INK_MUTE}"/>
    {_text(60, 128, "BASE", size=8, weight=700, anchor="middle", color=INK_MUTE)}
    {_text(60, 158, "no tag &mdash; still act", size=7.2, anchor="middle", color=INK_MUTE)}
    <rect x="130" y="100" width="100" height="70" stroke-width="1.8" style="fill:{AMBER_BG};stroke:{AMBER}"/>
    {_text(180, 88, "CONSIDERABLE", size=8, weight=700, anchor="middle", color=AMBER)}
    <circle cx="160" cy="140" r="10.5" stroke-width="1.6" style="fill:none;stroke:{AMBER}"/>
    {_text(180, 155, "1.75 in hail (golf ball)", size=7, anchor="start", color=AMBER)}
    {_text(180, 165, "or 70 mph wind", size=7, anchor="start", color=AMBER)}
    <rect x="250" y="50" width="120" height="120" stroke-width="2.2" style="fill:{AMBER_BG};stroke:{ALERT}"/>
    {_text(310, 38, "DESTRUCTIVE", size=8, weight=700, anchor="middle", color=ALERT)}
    <circle cx="285" cy="110" r="16.5" stroke-width="2" style="fill:none;stroke:{ALERT}"/>
    {_text(305, 130, "2.75 in hail (baseball)", size=7, anchor="start", color=ALERT)}
    {_text(305, 140, "or 80 mph wind", size=7, anchor="start", color=ALERT)}
    {_text(305, 155, "auto-fires a Wireless", size=7, anchor="start", color=ALERT)}
    {_text(305, 165, "Emergency Alert", size=7, anchor="start", color=ALERT)}
    '''
    return _figure(11, "The three damage-threat tiers on a severe thunderstorm warning, and "
                   "the two hail sizes to scale against each other — only the top tier pushes "
                   "an alert to every phone in the warned area.",
                   _svg((380, 180), 1.4, "Step chart of severe thunderstorm warning damage-threat tiers with hail size comparison", body))


# ---------------------------------------------------------------------------
# Figure 12 — Radiological proximity (Protection 125)
# ---------------------------------------------------------------------------
def fig_radiological_zones():
    body = f'''
    <circle cx="150" cy="150" r="140" stroke-width="1.6" style="fill:{AMBER_BG};fill-opacity:0.5;stroke:{AMBER}"/>
    <circle cx="150" cy="150" r="34" stroke-width="1.8" style="fill:{ALERT};fill-opacity:0.18;stroke:{ALERT}"/>
    <rect x="146" y="146" width="8" height="8" style="fill:{INK}"/>
    {_text(150, 195, "10 mi", size=9, weight=700, anchor="middle", color=ALERT)}
    {_text(150, 207, "plume exposure pathway", size=7, anchor="middle", color=ALERT)}
    {_text(150, 217, "shelter, evacuate, KI", size=7, anchor="middle", color=ALERT)}
    {_text(150, 20, "50 mi", size=9, weight=700, anchor="middle", color=AMBER)}
    {_text(150, 32, "ingestion exposure pathway &mdash; food and water", size=7, anchor="middle", color=AMBER)}
    '''
    return _figure(12, "The two federal planning zones around a nuclear facility: a ten-mile "
                   "ring where sheltering and evacuation are planned, inside a fifty-mile ring "
                   "governing food and water. Most readers are inside neither.",
                   _svg((300, 300), 2.1, "Concentric diagram of the ten-mile plume and fifty-mile ingestion emergency planning zones", body))


# ---------------------------------------------------------------------------
# Figure 13 — The clock: six disaster phases, log-scaled (Part One, Ch. 2)
# ---------------------------------------------------------------------------
def fig_disaster_timeline():
    import math
    # end-of-phase minutes, straight from the manuscript's own phase table (P1-C2) —
    # nothing here is a new number, only a log-scaled layout of published ones.
    bounds = [0.5, 30, 360, 4320, 20160, 1051200]  # minutes: ~instant,30m,6h,3d,2wk,2yr
    names = ["Warning", "Violent", "Isolation", "Degradation", "Decompensation", "Recovery"]
    labels = ["days&ndash;min before", "0&ndash;30 min", "30 min&ndash;6 hr", "6 hr&ndash;3 days", "3 days&ndash;2 wk", "2 wk&ndash;2 yr"]
    colors = [INK_MUTE, ALERT, AMBER, AMBER, INK_SOFT, INK_SOFT]
    logs = [math.log10(b) for b in bounds]
    lo, hi = logs[0] - 0.4, logs[-1]
    span = hi - lo
    MARGIN, W = 20, 440
    xs = [MARGIN + (l - lo) / span * W for l in logs]
    bars = []
    for i in range(6):
        x0 = xs[i - 1] if i > 0 else MARGIN
        x1 = xs[i]
        w = max(x1 - x0, 4)
        bars.append(f'<rect x="{x0:.1f}" y="60" width="{w:.1f}" height="34" stroke-width="1.4" '
                     f'style="fill:{colors[i]};fill-opacity:0.20;stroke:{colors[i]}"/>')
        above = i % 2 == 0
        ty = 52 if above else 112
        ly = ty + 10
        if w < 46:
            # too narrow to center text under — set the label beside the bar instead,
            # anchored so it never runs past the viewBox edge.
            anchor = "start" if x1 < 200 else "end"
            lx = x1 + 4 if anchor == "start" else x0 - 4
        else:
            anchor, lx = "middle", (x0 + x1) / 2
        bars.append(_text(lx, ty, names[i], size=7.2, weight=700, anchor=anchor, color=colors[i]))
        bars.append(_text(lx, ly, labels[i], size=6.6, anchor=anchor, color=INK_MUTE))
    body = "".join(bars) + _text(235, 138, "time axis is log-scaled &mdash; each phase is roughly an order of magnitude longer than the last", size=6.6, anchor="middle", color=INK_MUTE, italic=True)
    return _figure(13, "The six phases are not equal lengths, and the mismatch is the point: "
                   "the violent window that gets almost all the attention is minutes, and the "
                   "phases that take most of the injuries are days to years.",
                   _svg((470, 150), 1.35, "Log-scaled timeline of the six disaster phases from warning to recovery", body))


# ---------------------------------------------------------------------------
# registry
# ---------------------------------------------------------------------------
_RENDERERS = {
    "safe-room-plan": fig_safe_room_plan,
    "three-rooms": fig_three_rooms,
    "utility-shutoffs": fig_utility_shutoffs,
    "water-heater-drawoff": fig_water_heater_drawoff,
    "garage-door-pressure": fig_garage_door_pressure,
    "defensible-space-zones": fig_defensible_space_zones,
    "flood-openings": fig_flood_openings,
    "alarm-placement": fig_alarm_placement,
    "box-fan-filter": fig_box_fan_filter,
    "hurricane-cone": fig_hurricane_cone,
    "hail-damage-tiers": fig_hail_damage_tiers,
    "radiological-zones": fig_radiological_zones,
    "disaster-timeline": fig_disaster_timeline,
}

FIGURES = [
    {"id": "safe-room-plan", "number": 1, "file": "P2-C3-temperature-shelter.md", "protection": 23,
     "justification": "Mandatory — sold by name on the landing page. Shows the spatial relationship "
                       "(zero exterior walls, center of the house) a sentence forces the reader to build alone."},
    {"id": "three-rooms", "number": 2, "file": "P2-C3-temperature-shelter.md", "protection": "23, 26, 29",
     "justification": "The three room-selection criteria (wind/cold/heat) actively conflict — side-by-side "
                       "comparison shows that faster than reading three separate protections and cross-referencing."},
    {"id": "utility-shutoffs", "number": 3, "file": "P2-C3-temperature-shelter.md", "protection": 35,
     "justification": "Shows the three shut-offs are scattered across the house, not together — a spatial claim, not a fact list."},
    {"id": "water-heater-drawoff", "number": 4, "file": "P2-C1-water.md", "protection": 4,
     "justification": "A 5-step procedure on physical valves in physical locations — order-and-location is exactly what a diagram carries and prose does not."},
    {"id": "garage-door-pressure", "number": 5, "file": "P2-C7-structure-hardening.md", "protection": 74,
     "justification": "The failure mechanism (internal pressurization loading the roof from below) is a physical process, not a fact — seeing the pressure arrows is faster than reading the sentence twice."},
    {"id": "defensible-space-zones", "number": 6, "file": "P2-C7-structure-hardening.md", "protection": "76, 77",
     "justification": "Three nested distances (5/30/100 ft) around a structure are a spatial layout; a diagram shows the nesting a list of numbers hides."},
    {"id": "flood-openings", "number": 7, "file": "P2-C7-structure-hardening.md", "protection": 80,
     "justification": "The counterintuitive engineering point — let water through, don't seal it out — is a pressure/geometry relationship that a cross-section shows and a paragraph must talk around."},
    {"id": "alarm-placement", "number": 8, "file": "P2-C5-air-sanitation.md", "protection": "47, 48",
     "justification": "Two placement rules across multiple floors and room types — a floor-by-floor diagram beats parsing two separate bulleted rules against your own house."},
    {"id": "box-fan-filter", "number": 9, "file": "P2-C5-air-sanitation.md", "protection": 50,
     "justification": "An assembly instruction (orientation, seams, shroud) is inherently spatial — this is the class of content diagrams exist for."},
    {"id": "hurricane-cone", "number": 10, "file": "P5-C1-warning-literacy.md", "protection": 90,
     "justification": "The single most consequential misreading in the book is a graphic misunderstood as a graphic — the fix has to be visual, showing the cone against the true (wider) hazard extent."},
    {"id": "hail-damage-tiers", "number": 11, "file": "P3-07-hail-derecho.md", "protection": None,
     "justification": "A magnitude comparison (1.75in vs 2.75in hail, which alert tier fires) that a reader cannot judge from inches alone — scaled circles make the size difference legible instantly."},
    {"id": "radiological-zones", "number": 12, "file": "P3-22-radiological-proximity.md", "protection": 125,
     "justification": "Two nested radii (10mi/50mi) around a point is a map relationship; most readers' first question — am I inside either ring — is answered by the shape, not the number."},
    {"id": "disaster-timeline", "number": 13, "file": "P1-C2-the-timeline.md", "protection": None,
     "justification": "The chapter's central claim is a magnitude mismatch (public attention vs. where the phases actually run long) that a table of equal-height rows visually denies — a log-scaled bar shows the true disproportion."},
]


def render_figure(fig_id):
    """Return one <figure>...</figure> HTML string for fig_id, or raise KeyError."""
    if fig_id not in _RENDERERS:
        raise KeyError(f"unknown figure id: {fig_id!r}. Known ids: {sorted(_RENDERERS)}")
    return _RENDERERS[fig_id]()


if __name__ == "__main__":
    # smoke test: every registered figure renders without raising
    for entry in FIGURES:
        html = render_figure(entry["id"])
        assert "<figure>" in html and "</figure>" in html, entry["id"]
    print(f"OK — {len(FIGURES)} figures render.")
