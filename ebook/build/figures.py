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
point at art/illustrations/<id>.jpg, and render_figure raises if that file is missing.
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


def _figure(number, caption, inner_html, large=False, credit="Original diagram."):
    cap_style = ' style="font-size:11pt;line-height:1.35"' if large else ""
    return (f'<figure><b class="fignum" style="display:none">{number}</b>{inner_html}'
            f'<figcaption{cap_style}><b>Figure {number}</b> — {caption} {credit}</figcaption>'
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


# ===========================================================================
# Large-print set (Figures 14-28) — senior review 2026-10-27, INVESTIGATION.md section 5
# ===========================================================================
SERIF = "'Iowan Old Style', 'Palatino Linotype', Palatino, Georgia, serif"
PT_W = 342  # content width in points: viewBox units == pt at print size


def _t(x, y, s, size=13, weight=400, color=INK, anchor="start", italic=False):
    """Large-print SVG text: serif, ink by default. size is in pt at print size."""
    return _text(x, y, s, size=size, weight=weight, color=color, anchor=anchor, family=SERIF, italic=italic)


def _psvg(height_in, label, body):
    return _svg((PT_W, round(height_in * 72)), height_in, label, body)


def _redx(cx, cy, r, w=5):
    return (f'<g stroke-width="{w}" stroke-linecap="round" style="stroke:{ALERT}">'
            f'<line x1="{cx-r}" y1="{cy-r}" x2="{cx+r}" y2="{cy+r}"/>'
            f'<line x1="{cx-r}" y1="{cy+r}" x2="{cx+r}" y2="{cy-r}"/></g>')


def _arrow_defs(mid, color):
    return (f'<defs><marker id="{mid}" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">'
            f'<path d="M0,0 L8,4 L0,8 z" style="fill:{color}"/></marker></defs>')


_BOX = (f'<span style="flex:0 0 auto;display:inline-block;width:13pt;height:13pt;margin-top:3pt;'
        f'border:1.8pt solid {INK};background:#fff"></span>')


def _cutout(height_in, inner):
    """A dashed cut-line card, the D1/D8 pull-out shape."""
    # min-height, not height+overflow:hidden: a line that wraps grows the box (fitcheck sees it), never clips
    return (f'<div style="min-height:{height_in}in;box-sizing:border-box;'
            f'border:2pt dashed {INK};padding:10pt 14pt;background:#fff;font-family:{SERIF};color:{INK}">'
            f'<div style="font-family:{SANS};font-size:11pt;color:{INK_MUTE}">&#9986; Cut along the dashed line</div>'
            f'{inner}</div>')


def _hazard_card(number, hazard, bands):
    """D1 — large-print checklist card. Every line paraphrases the chapter's own
    '## The one-page version' table (source_file); nothing is added beyond it."""
    colors = {"WATCH": AMBER, "WARNING": ALERT, "AFTER": INK_SOFT}
    html = [f'<div style="font-size:24pt;font-weight:700;letter-spacing:.04em;margin:2pt 0 0">{hazard}</div>'
            f'<div style="font-size:12pt;color:{INK_SOFT}">Tick each box as you do it.</div>']
    for name, when, lines in bands:
        html.append(f'<div style="background:{colors[name]};color:#fff;font-size:16pt;font-weight:700;'
                    f'padding:2pt 8pt;margin-top:9pt">{name}'
                    + (f' <span style="font-size:13pt;font-weight:400">&mdash; {when}</span>' if when else '')
                    + '</div>')
        for ln in lines:
            html.append(f'<div style="display:flex;gap:9pt;font-size:14pt;line-height:1.28;margin-top:6pt">'
                        f'{_BOX}<span>{ln}</span></div>')
    return _figure(number, f"Cut-out card: the {hazard.lower()} chapter's one-page version in large print. "
                   f"Keep it where you will see it.", _cutout(6.6, "".join(html)), large=True)


def fig_card_tornado():
    return _hazard_card(14, "TORNADO", [
        ("WATCH", "a tornado is possible", [
            "Charge phones and flashlights",
            "Clear the safe room. Helmets and shoes in it",
            "Mobile home: <b>leave now</b>"]),
        ("WARNING", "a tornado is coming", [
            "<b>Go now. Do not wait to see it.</b>",
            "Lowest floor, inside room, no windows",
            "Helmets on. Cover your head",
            "In a car: never under an overpass"]),
        ("AFTER", "", [
            "Shoes on first",
            "No flames: flashlights only",
            "Blow the whistle for help",
            "Photograph before touching. Sign nothing"]),
    ])


def fig_card_hurricane():
    return _hazard_card(15, "HURRICANE", [
        ("WATCH", "days before", [
            "Medicines, cash, fuel. Test the generator",
            "Window covers up. Bring loose things in",
            "<b>Leaving? Go now, while the roads work</b>"]),
        ("WARNING", "the last day, and during", [
            "Fill water. Freeze bottles. Charge everything",
            "Photograph the whole house and yard",
            "Inside, lowest room, away from glass",
            "<b>The calm is the eye. Stay in</b>"]),
        ("AFTER", "", [
            "Generator outdoors only",
            "Tap water unsafe until you are told otherwise",
            "Dry the house out fast",
            "Sign nothing"]),
    ])


def fig_card_wildfire():
    return _hazard_card(16, "WILDFIRE", [
        ("WATCH", "Red Flag day", [
            "Fuel the car. Park it facing out",
            "Bags in the car",
            "Shoes and keys by the bed"]),
        ("WARNING", "fire is coming", [
            "<b>Leave at the warning, not the order</b>",
            "The roads work now. Go",
            "Trapped in the car: park clear of brush",
            "Windows shut. Lie low under wool. Call 911"]),
        ("AFTER", "", [
            "Ash is toxic. Never dry-sweep it",
            "Tap water may be unsafe",
            "Hot spots for weeks",
            "Heavy rain can bring mud: be ready to leave"]),
    ])


def fig_card_cold():
    return _hazard_card(17, "EXTREME COLD", [
        ("WATCH", "hard cold on the way", [
            "Wrap pipes. <b>Label the water main</b>",
            "Set up the warm room and sleeping bags",
            "Check CO alarms are in date",
            "Hoses off. Cabinet doors open"]),
        ("WARNING", "the hard freeze", [
            "Heat up, not down at night",
            "<b>Drip the far faucets</b>",
            "Frozen pipe: tap open, hair dryer, <b>never a flame</b>",
            "If you leave: water off, pipes drained"]),
        ("AFTER", "the thaw", [
            "Be home for the thaw",
            "Check the water meter with everything off",
            "Dry inside the walls, not just the floor"]),
    ])


def fig_call_card():
    """D8 — fridge card. Blank write-in lines only; no names, numbers or advice beyond
    the R2/R3 text (two drivers, far contact, county registry, pharmacist, doctor)."""
    line = f'flex:1 1 0;border-bottom:1.4pt solid {INK};height:24pt'
    lbl = f'font-family:{SANS};font-size:11pt;color:{INK_MUTE};align-self:flex-end;padding-bottom:2pt'

    def row(n, who):
        return (f'<div style="margin-top:9pt">'
                f'<div style="display:flex;align-items:center;gap:8pt;font-size:15pt;font-weight:700">'
                f'<span style="display:inline-block;width:20pt;height:20pt;border-radius:50%;background:{AMBER};'
                f'color:#fff;font-family:{SANS};font-size:12pt;text-align:center;line-height:20pt">{n}</span>{who}</div>'
                f'<div style="display:flex;gap:6pt"><span style="{lbl}">Name</span><span style="{line}"></span>'
                f'<span style="{lbl}">Phone</span><span style="{line};flex:0.8 1 0"></span></div></div>')

    inner = (f'<div style="font-size:24pt;font-weight:700;margin-top:2pt">Who I call, in order</div>'
             f'<div style="font-size:14pt;margin-top:8pt;display:flex;align-items:flex-end;gap:5pt">'
             f'<span>When</span><span style="{line}"></span></div>'
             f'<div style="font-size:14pt;margin-top:2pt;display:flex;align-items:flex-end;gap:5pt">'
             f'<span style="{line}"></span><span>happens, <b>I leave.</b></span></div>'
             + row(1, "Driver 1") + row(2, "Driver 2") + row(3, "Far-away contact")
             + row(4, "County registry") + row(5, "Pharmacist") + row(6, "Doctor"))
    return _figure(18, "Fill it in, cut it out, put it on the fridge. Both drivers must have "
                   "agreed out loud before their names go on it.", _cutout(6.3, inner), large=True)


def fig_weather_radio_setup():
    """D6 / P87 — generic radio, no brand. Steps from P87 (SAME code, tone alert, test,
    batteries); 'weekly' is the brief's cadence, P87 itself says only 'Test it'."""
    def btn(x, n, name):
        return (f'<rect x="{x}" y="118" width="62" height="34" rx="6" stroke-width="2.4" style="fill:#fff;stroke:{INK}"/>'
                f'{_t(x + 31, 141, name, size=13, weight=700, anchor="middle")}'
                f'<circle cx="{x + 31}" cy="176" r="12" style="fill:{AMBER}"/>'
                f'{_t(x + 31, 181, str(n), size=14, weight=700, color=PAPER, anchor="middle")}'
                f'<line x1="{x + 31}" y1="164" x2="{x + 31}" y2="154" stroke-width="2" style="stroke:{AMBER}"/>')

    def step(y, n, head, lines):
        out = (f'<circle cx="20" cy="{y - 5}" r="13" style="fill:{AMBER}"/>'
               f'{_t(20, y, str(n), size=15, weight=700, color=PAPER, anchor="middle")}'
               f'{_t(42, y, head, size=15, weight=700)}')
        return out + "".join(_t(42, y + 19 + i * 17, ln, size=13, color=INK_SOFT) for i, ln in enumerate(lines))

    body = f'''
    <rect x="14" y="8" width="314" height="158" rx="16" stroke-width="3" style="fill:{AMBER_BG};stroke:{INK}"/>
    <rect x="150" y="2" width="120" height="8" rx="3" style="fill:{INK}"/>
    <g stroke-width="2" style="stroke:{INK_MUTE}">
      <line x1="34" y1="34" x2="104" y2="34"/><line x1="34" y1="48" x2="104" y2="48"/>
      <line x1="34" y1="62" x2="104" y2="62"/><line x1="34" y1="76" x2="104" y2="76"/>
      <line x1="34" y1="90" x2="104" y2="90"/>
    </g>
    {_t(69, 112, "speaker", size=11, color=INK_MUTE, anchor="middle")}
    <rect x="124" y="26" width="190" height="62" rx="4" stroke-width="2.4" style="fill:#fff;stroke:{INK}"/>
    {_t(219, 52, "YOUR COUNTY CODE", size=12, weight=700, color=INK_SOFT, anchor="middle")}
    {_t(219, 76, "_ _ _ _ _ _", size=16, weight=700, anchor="middle")}
    {btn(124, 1, "SAME")}{btn(188, 2, "ALERT")}{btn(252, 3, "TEST")}
    {step(222, 1, "Set your county code", ["Press SAME. Type in your county's code.", "Now it wakes you only for your county."])}
    {step(290, 2, "Set it to sound the alarm tone", ["Choose the tone alert, loud enough to", "wake you, not a quiet voice message."])}
    {step(351, 3, "Test it", ["Press TEST. Change the batteries", "on a schedule."])}
    <rect x="4" y="404" width="334" height="82" stroke-width="2" style="fill:#fff;stroke:{AMBER}"/>
    {_t(14, 425, "Where to find your county code", size=14, weight=700, color=AMBER)}
    {_t(14, 445, "Online: weather.gov/nwr/counties", size=13)}
    {_t(14, 463, "No computer? Phone your county emergency", size=13)}
    {_t(14, 480, "office, or ask a relative to look it up.", size=13)}
    '''
    return _figure(19, "Three settings turn a weather radio from noise you switch off into "
                   "an alarm for your county only. Buttons differ by model; the manual names yours.",
                   _psvg(6.8, "A generic weather radio front with three numbered steps: county code, alert tone, test", body),
                   large=True)


def fig_battery_runtime():
    """D2 / P61 — the method from P38 ('device wattage x hours, add margin'). The 60 W
    row is labelled an example; no device spec is asserted, and no margin number is given
    because the book states none."""
    ex_w, ex_h = 60, 8  # same example as the P2-C6 CPAP paragraph
    ex_wh = ex_w * ex_h

    def box(x, w, top, bottom):
        return (f'<rect x="{x}" y="34" width="{w}" height="78" rx="6" stroke-width="2.6" style="fill:#fff;stroke:{INK}"/>'
                f'{_t(x + w / 2, 66, top, size=16, weight=700, anchor="middle")}'
                f'{_t(x + w / 2, 88, bottom[0], size=12, color=INK_SOFT, anchor="middle")}'
                f'{_t(x + w / 2, 103, bottom[1], size=12, color=INK_SOFT, anchor="middle")}')

    body = f'''
    {_t(171, 20, "Will my battery run my machine?", size=17, weight=700, anchor="middle")}
    {box(2, 92, "WATTS", ["on the power", "brick label"])}
    {_t(106, 82, "&#215;", size=26, weight=700, anchor="middle")}
    {box(118, 92, "HOURS", ["you need it", "running"])}
    {_t(222, 82, "=", size=26, weight=700, anchor="middle")}
    <rect x="234" y="34" width="106" height="78" rx="6" stroke-width="3" style="fill:{AMBER_BG};stroke:{AMBER}"/>
    {_t(287, 62, "WATT-", size=16, weight=700, color=AMBER, anchor="middle")}
    {_t(287, 80, "HOURS", size=16, weight=700, color=AMBER, anchor="middle")}
    {_t(287, 100, "battery you need", size=12, color=AMBER, anchor="middle")}
    <rect x="2" y="134" width="338" height="104" stroke-width="2" stroke-dasharray="6,4" style="fill:none;stroke:{INK_MUTE}"/>
    <rect x="12" y="124" width="138" height="20" style="fill:{PAPER}"/>
    {_t(18, 139, "EXAMPLE ONLY", size=13, weight=700, color=ALERT)}
    {_t(14, 166, f"If your label says {ex_w} watts", size=14)}
    {_t(14, 185, f"and you sleep {ex_h} hours:", size=14)}
    {_t(14, 220, f"{ex_w} &#215; {ex_h} = {ex_wh} watt-hours", size=20, weight=700)}
    {_t(14, 270, "Your machine's label will say its own number.", size=13, color=INK_SOFT)}
    {_t(14, 290, "Use that number, not this one.", size=13, color=INK_SOFT)}
    <rect x="2" y="306" width="338" height="54" style="fill:{AMBER_BG}"/>
    {_t(14, 329, "Then buy a battery bigger than that.", size=14, weight=700)}
    {_t(14, 349, "Add a margin (Protection 38).", size=13, color=INK_SOFT)}
    '''
    return _figure(20, "One multiplication sizes the battery: the watts on your machine's label "
                   "times the hours you need it, plus a margin. The numbers shown are an example.",
                   _psvg(5.1, "Watts times hours equals watt-hours, with a labelled example", body), large=True)


def fig_leave_early_no_car():
    """D3 / P111 — the order of hurricane products, not their exact hours. Days come from
    the P3-02 one-page version (5 / 3 / 2 / 1 days); positions of ORDER and WARNING
    are schematic and the figure says so."""
    xs = [20 + i * 60.4 for i in range(6)]
    days = ["5 days", "4 days", "3 days", "2 days", "1 day", "landfall"]
    ticks = "".join(f'<line x1="{x:.1f}" y1="150" x2="{x:.1f}" y2="162" stroke-width="2.4" style="stroke:{INK}"/>'
                    + (_t(x, 180, d, size=12, anchor="middle") if d != "landfall"
                       else _t(x + 10, 134, d, size=13, weight=700, anchor="end"))
                    for x, d in zip(xs, days))
    xw, xo, xr = xs[3], xs[3] + 22, xs[3] + 40  # watch at 2 days; order, warning schematic after it
    body = f'''
    {_arrow_defs("le-arrow", INK)}
    <rect x="{xs[0]:.1f}" y="140" width="{xw - xs[0]:.1f}" height="20" style="fill:{AMBER};fill-opacity:0.25"/>
    <rect x="{xw:.1f}" y="140" width="{xs[5] - xw:.1f}" height="20" style="fill:{ALERT};fill-opacity:0.18"/>
    <line x1="10" y1="160" x2="332" y2="160" stroke-width="3" marker-end="url(#le-arrow)" style="stroke:{INK}"/>
    {ticks}
    {_t(xs[0], 132, "time to leave", size=13, weight=700, color=AMBER)}
    <rect x="96" y="8" width="244" height="86" rx="6" stroke-width="3" style="fill:{AMBER_BG};stroke:{AMBER}"/>
    {_t(108, 34, "WATCH", size=18, weight=700, color=AMBER)}
    {_t(108, 58, "Call your driver.", size=17, weight=700)}
    {_t(108, 82, "Leave today.", size=17, weight=700)}
    <line x1="{xw:.1f}" y1="94" x2="{xw:.1f}" y2="150" stroke-width="3" style="stroke:{AMBER}"/>
    <circle cx="{xw:.1f}" cy="150" r="6" style="fill:{AMBER}"/>
    <line x1="{xo:.1f}" y1="150" x2="{xo:.1f}" y2="206" stroke-width="2.4" style="stroke:{ALERT}"/>
    <circle cx="{xo:.1f}" cy="150" r="5" style="fill:{ALERT}"/>
    <rect x="4" y="206" width="222" height="80" rx="6" stroke-width="2.4" style="fill:#fff;stroke:{ALERT}"/>
    {_t(14, 228, "ORDER", size=16, weight=700, color=ALERT)}
    {_t(14, 250, "County transport starts.", size=14)}
    {_t(14, 272, "May be too late.", size=14, weight=700, color=ALERT)}
    <line x1="{xr:.1f}" y1="150" x2="{xr:.1f}" y2="298" stroke-width="2.4" style="stroke:{INK}"/>
    <circle cx="{xr:.1f}" cy="150" r="5" style="fill:{INK}"/>
    <rect x="4" y="298" width="334" height="40" rx="6" stroke-width="2" style="fill:#fff;stroke:{INK}"/>
    {_t(14, 324, "WARNING", size=16, weight=700)}
    {_t(110, 324, "Hurricane conditions expected.", size=14)}
    {_t(171, 362, "Exact days differ for every storm.", size=12, color=INK_MUTE, anchor="middle", italic=True)}
    '''
    return _figure(21, "Without a car, your trigger is the watch, not the order. County "
                   "transport usually starts only after an order, which can be too late.",
                   _psvg(5.15, "Hurricane timeline: leave at the watch; county transport starts at the order", body),
                   large=True)


def fig_three_shelters():
    """D4 / P4-C2 manufactured-home section — the three places from R5. Drive times are
    blanks the reader fills in; nothing is measured here."""
    def mins(x, y):
        return (f'<rect x="{x - 36}" y="{y - 17}" width="72" height="26" rx="4" stroke-width="2" style="fill:#fff;stroke:{AMBER}"/>'
                f'{_t(x, y + 2, "___ min", size=14, weight=700, color=AMBER, anchor="middle")}')

    body = f'''
    {_arrow_defs("ts-arrow", AMBER)}
    <!-- neighbor's in-ground shelter, top left -->
    <path d="M14 70 Q 64 30 114 70 Z" stroke-width="2.4" style="fill:{AMBER_BG};stroke:{INK}"/>
    <rect x="52" y="56" width="24" height="14" stroke-width="2" style="fill:#fff;stroke:{INK}"/>
    {_t(64, 92, "Neighbor's", size=14, weight=700, anchor="middle")}
    {_t(64, 110, "in-ground shelter", size=14, weight=700, anchor="middle")}
    <!-- public building, top right -->
    <rect x="232" y="30" width="96" height="44" stroke-width="2.4" style="fill:{AMBER_BG};stroke:{INK}"/>
    <path d="M226 32 L280 8 L334 32" stroke-width="2.4" style="fill:none;stroke:{INK}"/>
    {_t(280, 92, "Public building,", size=14, weight=700, anchor="middle")}
    {_t(280, 110, "confirmed open", size=14, weight=700, anchor="middle")}
    <!-- city shelter, bottom -->
    <rect x="121" y="352" width="100" height="48" stroke-width="2.4" style="fill:{AMBER_BG};stroke:{INK}"/>
    {_t(171, 382, "SHELTER", size=13, weight=700, anchor="middle")}
    {_t(171, 422, "City shelter", size=14, weight=700, anchor="middle")}
    <!-- the trailer, center -->
    <rect x="96" y="196" width="150" height="50" stroke-width="2.6" style="fill:#fff;stroke:{INK}"/>
    {_t(171, 188, "mobile home", size=13, weight=700, anchor="middle")}
    {_redx(171, 221, 22, 6)}
    {_t(171, 276, "Stay in the trailer", size=15, weight=700, color=ALERT, anchor="middle")}
    <line x1="98" y1="271" x2="244" y2="271" stroke-width="2.4" style="stroke:{ALERT}"/>
    <!-- arrows -->
    <line x1="120" y1="194" x2="76" y2="122" stroke-width="3" marker-end="url(#ts-arrow)" style="stroke:{AMBER}"/>
    <line x1="222" y1="194" x2="266" y2="122" stroke-width="3" marker-end="url(#ts-arrow)" style="stroke:{AMBER}"/>
    <line x1="171" y1="286" x2="171" y2="344" stroke-width="3" marker-end="url(#ts-arrow)" style="stroke:{AMBER}"/>
    {mins(66, 160)}{mins(276, 160)}{mins(222, 320)}
    '''
    return _figure(22, "Three places, not one. Ask each one now, then drive there and write the "
                   "minutes on the arrow. A mobile home is not one of the places.",
                   _psvg(6.0, "Map with a mobile home at center crossed out and arrows to three shelters with blank drive times", body),
                   large=True)


def fig_insulin_cooler():
    """D5 / P60 — layout only (bottles at the sides, towel, pens bagged in the middle,
    thermometer inside, no ice on pens). No temperatures or durations are shown."""
    def bottle(x):
        return (f'<rect x="{x}" y="96" width="34" height="132" rx="8" stroke-width="2.4" style="fill:{AMBER_BG};stroke:{INK}"/>'
                f'<rect x="{x + 10}" y="86" width="14" height="10" style="fill:{INK}"/>')

    body = f'''
    <rect x="26" y="70" width="290" height="176" rx="6" stroke-width="5" style="fill:#fff;stroke:{INK}"/>
    <rect x="20" y="54" width="302" height="16" rx="4" stroke-width="3" style="fill:{INK_MUTE};stroke:{INK}"/>
    {bottle(38)}{bottle(270)}
    <rect x="84" y="100" width="174" height="128" rx="10" stroke-width="3" stroke-dasharray="7,4" style="fill:{AMBER};fill-opacity:0.14;stroke:{AMBER}"/>
    <rect x="104" y="128" width="112" height="74" rx="6" stroke-width="2.4" style="fill:#fff;stroke:{INK_SOFT}"/>
    <line x1="104" y1="140" x2="216" y2="140" stroke-width="2" style="stroke:{INK_SOFT}"/>
    <g stroke-width="2" style="fill:#fff;stroke:{INK}">
      <rect x="114" y="150" width="92" height="10" rx="4"/><rect x="114" y="167" width="92" height="10" rx="4"/>
      <rect x="114" y="184" width="92" height="10" rx="4"/>
    </g>
    <rect x="232" y="114" width="8" height="78" rx="4" stroke-width="2" style="fill:#fff;stroke:{ALERT}"/>
    <circle cx="236" cy="196" r="7" style="fill:{ALERT}"/>
    <!-- labels -->
    {_t(4, 24, "Frozen water bottle", size=13, weight=700)}
    {_t(4, 41, "at each side", size=13, weight=700)}
    <line x1="55" y1="46" x2="55" y2="84" stroke-width="1.6" style="stroke:{INK}"/>
    {_t(338, 24, "Thermometer", size=13, weight=700, color=ALERT, anchor="end")}
    {_t(338, 41, "inside", size=13, weight=700, color=ALERT, anchor="end")}
    <line x1="290" y1="46" x2="240" y2="112" stroke-width="1.6" style="stroke:{ALERT}"/>
    {_t(196, 24, "Towel", size=13, weight=700, color=AMBER, anchor="middle")}
    {_t(196, 41, "layer", size=13, weight=700, color=AMBER, anchor="middle")}
    <line x1="196" y1="46" x2="196" y2="100" stroke-width="1.6" style="stroke:{AMBER}"/>
    {_t(171, 282, "Insulin pens in a zip bag, in the middle", size=13, weight=700, anchor="middle")}
    <line x1="160" y1="202" x2="160" y2="266" stroke-width="1.6" style="stroke:{INK}"/>
    <!-- never: ice on pens -->
    <rect x="4" y="314" width="334" height="92" stroke-width="2.4" style="fill:#fff;stroke:{ALERT}"/>
    <rect x="24" y="332" width="40" height="40" rx="4" stroke-width="2.4" style="fill:{AMBER_BG};stroke:{INK}"/>
    <rect x="58" y="346" width="92" height="12" rx="5" stroke-width="2" style="fill:#fff;stroke:{INK}"/>
    {_redx(86, 352, 30, 6)}
    {_t(172, 348, "Never let ice", size=16, weight=700, color=ALERT)}
    {_t(172, 370, "touch the pens.", size=16, weight=700, color=ALERT)}
    {_t(172, 392, "Keep the towel between.", size=13, color=INK_SOFT)}
    '''
    return _figure(23, "How to pack the cooler: cold at the sides, a towel as a buffer, the pens "
                   "bagged in the middle where you can read the thermometer.",
                   _psvg(5.7, "Cutaway cooler with frozen bottles at the sides, towel layer, insulin pens bagged in the middle, thermometer", body),
                   large=True)


def fig_generator_20ft():
    """D7 / P32 — CDC's 'more than 20 feet from any window, door or vent', quoted in P32.
    Drawn to scale: house 40 ft = 140 pt, so 20 ft = 70 pt around the whole outline."""
    S = 3.5                                        # pt per foot
    hx, hy, hw, hh = 101, 126, 140, 108            # house footprint (40 x ~31 ft)
    gw = 62                                        # garage width
    c = 20 * S                                     # 20 ft clearance
    gy = hy + hh + c + 20                          # generator top, outside the line
    mx = hx + gw + (hw - gw) / 2                   # middle of the living part
    body = f'''
    {_arrow_defs("gn-arrow", INK)}
    <rect x="{hx - c}" y="{hy - c}" width="{hw + 2 * c}" height="{hh + 2 * c}" rx="{c}" stroke-width="2.6"
      stroke-dasharray="9,6" style="fill:{ALERT};fill-opacity:0.07;stroke:{ALERT}"/>
    <rect x="{hx}" y="{hy}" width="{hw}" height="{hh}" stroke-width="3" style="fill:#fff;stroke:{INK}"/>
    <line x1="{hx + gw}" y1="{hy}" x2="{hx + gw}" y2="{hy + hh}" stroke-width="2" style="stroke:{INK}"/>
    {_t(hx + gw / 2, hy + 24, "GARAGE", size=11, weight=700, anchor="middle")}
    {_redx(hx + gw / 2, hy + 62, 20, 5)}
    {_t(mx, hy + 34, "HOUSE", size=14, weight=700, anchor="middle")}
    <g stroke-width="6" style="stroke:{AMBER}">
      <line x1="{mx - 16}" y1="{hy}" x2="{mx + 16}" y2="{hy}"/>
      <line x1="{hx + hw}" y1="{hy + 22}" x2="{hx + hw}" y2="{hy + 50}"/>
      <line x1="{mx - 12}" y1="{hy + hh}" x2="{mx + 12}" y2="{hy + hh}"/>
    </g>
    <rect x="{hx + hw - 4}" y="{hy + 72}" width="8" height="14" style="fill:{AMBER}"/>
    {_t(mx, hy + 62, "windows,", size=11, color=AMBER, anchor="middle")}
    {_t(mx, hy + 76, "doors, vent", size=11, color=AMBER, anchor="middle")}
    <line x1="{hx + hw + 4}" y1="{hy + 36}" x2="{hx + hw + c}" y2="{hy + 36}" stroke-width="2.2" marker-end="url(#gn-arrow)" style="stroke:{INK}"/>
    {_t(hx + hw + c / 2, hy + 28, "20 ft", size=16, weight=700, anchor="middle")}
    <rect x="262" y="{gy}" width="56" height="34" rx="4" stroke-width="2.6" style="fill:{AMBER_BG};stroke:{INK}"/>
    {_t(290, gy + 22, "GEN", size=13, weight=700, anchor="middle")}
    <path d="M262 {gy + 17} C 200 {gy + 17}, 190 {hy + hh + 40}, {mx - 30} {hy + hh}" stroke-width="2.6"
      stroke-dasharray="3,4" style="fill:none;stroke:{INK_SOFT}"/>
    {_t(4, gy + 4, "cord to", size=12, color=INK_SOFT)}
    {_t(4, gy + 20, "the house", size=12, color=INK_SOFT)}
    {_t(4, 20, "More than 20 feet from every window,", size=14, weight=700, color=ALERT)}
    {_t(4, 38, "door and vent: outside the dashed line.", size=14, weight=700, color=ALERT)}
    {_t(4, gy + 58, "Never in the garage, even with the door open.", size=13, weight=700, color=ALERT)}
    {_t(4, gy + 76, "Point the exhaust away from the house.", size=13)}
    '''
    return _figure(24, "Pick the spot now, in daylight. Outside the dashed line, exhaust "
                   "aimed away, and a battery CO alarm inside the house while it runs.",
                   _psvg(5.95, "Top-down house and yard with a 20-foot clearance line; generator outside it; garage crossed out", body),
                   large=True)


def _illustration(fig_id, number, caption, height_in=3.4):
    """Raster illustration slot. src is relative to ebook/build/book.html, where the book
    renders. A missing PNG is a build error, never a silent skip."""
    path = ART_DIR / f"{fig_id}.jpg"
    if not path.is_file():
        raise FileNotFoundError(f"«FIG: {fig_id}» needs {path} — the illustration JPEG is missing.")
    img = (f'<img src="art/illustrations/{fig_id}.jpg" alt="{caption}" '
           f'style="height:{height_in}in;width:auto;max-width:100%;object-fit:contain;margin:0 auto;display:block">')
    return _figure(number, caption, img, large=True, credit="")


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
    "card-tornado": fig_card_tornado,
    "card-hurricane": fig_card_hurricane,
    "card-wildfire": fig_card_wildfire,
    "card-cold": fig_card_cold,
    "call-card": fig_call_card,
    "weather-radio-setup": fig_weather_radio_setup,
    "battery-runtime": fig_battery_runtime,
    "leave-early-no-car": fig_leave_early_no_car,
    "three-shelters": fig_three_shelters,
    "insulin-cooler": fig_insulin_cooler,
    "generator-20ft": fig_generator_20ft,
    "illus-walker-porch": lambda: _illustration("illus-walker-porch", 25, "A driver who has agreed, out loud, to leave at the watch. Name a second one too."),
    "illus-mobile-home": lambda: _illustration("illus-mobile-home", 26, "A manufactured home is not shelter from a tornado. Go before the warning."),
    "illus-bed-shaker": lambda: _illustration("illus-bed-shaker", 27, "If your hearing aids come out at night, your alarm has to shake the bed."),
    "illus-oxygen-car": lambda: _illustration("illus-oxygen-car", 28, "Tanks ride upright and secured. Know how many hours each lasts at your flow."),
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
    {"id": "card-tornado", "number": 14, "file": "P3-01-tornado.md", "protection": None,
     "justification": "D1. Older readers asked for a card they can cut out and tick: the one-page version in 14pt with tick boxes, by WATCH / WARNING / AFTER."},
    {"id": "card-hurricane", "number": 15, "file": "P3-02-hurricane-surge.md", "protection": None,
     "justification": "D1. The day-count table reorganised into the three moments a reader actually acts on, in large print with tick boxes."},
    {"id": "card-wildfire", "number": 16, "file": "P3-05-wildfire.md", "protection": None,
     "justification": "D1. 'Leave at the warning, not the order' is the line that saves lives; the card puts it in a red band at 14pt."},
    {"id": "card-cold", "number": 17, "file": "P3-11-extreme-cold.md", "protection": None,
     "justification": "D1. The pipe and CO steps as a tick list; cold has no single dramatic moment, so the card gives the sequence."},
    {"id": "call-card", "number": 18, "file": "P0-front-matter.md", "protection": None,
     "justification": "D8. The plan for a reader without a car is a list of people in order; a fill-in fridge card is the plan itself, not a description of it."},
    {"id": "weather-radio-setup", "number": 19, "file": "P5-C1-warning-literacy.md", "protection": 87,
     "justification": "D6. Programming SAME is the step people skip; three numbered buttons on a drawn radio map the prose onto the object in their hands."},
    {"id": "battery-runtime", "number": 20, "file": "P2-C6-medical.md", "protection": 61,
     "justification": "D2. The sizing rule is one multiplication; laid out as boxes with a labelled example, a reader can do it with their own label."},
    {"id": "leave-early-no-car", "number": 21, "file": "P5-C3-evacuation.md", "protection": 111,
     "justification": "D3. The danger is ordering: county transport comes after the order, which is after the watch. A timeline shows the gap a sentence hides."},
    {"id": "three-shelters", "number": 22, "file": "P4-C2-places.md", "protection": None,
     "justification": "D4. 'Three places, each with a drive time' becomes a map the reader fills in, with the trailer itself crossed out."},
    {"id": "insulin-cooler", "number": 23, "file": "P2-C6-medical.md", "protection": 60,
     "justification": "D5. Packing order (ice at the sides, towel, pens in the middle, never ice on pens) is spatial; a cutaway shows it at a glance."},
    {"id": "generator-20ft", "number": 24, "file": "P2-C3-temperature-shelter.md", "protection": 32,
     "justification": "D7. CDC's 20 feet from every window, door and vent is a line around the whole house, not one distance; drawn to scale it shows how far that is."},
    {"id": "illus-walker-porch", "number": 25, "file": "P5-C3-evacuation.md", "protection": 111,
     "justification": "I1. Older readers asked for pictures; the agreed-driver pickup shows the plan working, not the disaster."},
    {"id": "illus-mobile-home", "number": 26, "file": "P4-C2-places.md", "protection": None,
     "justification": "I2. A torn single-wide beside an intact brick house makes 'not shelter' undeniable."},
    {"id": "illus-bed-shaker", "number": 27, "file": "P5-C1-warning-literacy.md", "protection": 85,
     "justification": "R6. A sleeping reader without hearing aids cannot hear an alarm; the picture shows what the alternative device is."},
    {"id": "illus-oxygen-car", "number": 28, "file": "P2-C6-medical.md", "protection": 61,
     "justification": "R4. How tanks ride in a car is a physical arrangement; a picture shows upright and secured."},
]


def render_figure(fig_id):
    """Return one <figure>...</figure> HTML string for fig_id, or raise KeyError."""
    if fig_id not in _RENDERERS:
        raise KeyError(f"unknown figure id: {fig_id!r}. Known ids: {sorted(_RENDERERS)}")
    return _RENDERERS[fig_id]()


if __name__ == "__main__":
    # smoke test: every registered figure renders. A missing illustration PNG is reported
    # by path and fails the run; it is never counted as OK.
    assert sorted(e["id"] for e in FIGURES) == sorted(_RENDERERS), "FIGURES and _RENDERERS disagree"
    assert len({e["number"] for e in FIGURES}) == len(FIGURES), "duplicate figure number"
    missing = []
    for entry in FIGURES:
        try:
            html = render_figure(entry["id"])
        except FileNotFoundError as e:
            missing.append(str(e))
            print(f"MISSING  {entry['number']:>2}  {entry['id']}: {e}")
            continue
        assert "<figure>" in html and "</figure>" in html, entry["id"]
        print(f"OK       {entry['number']:>2}  {entry['id']}")
    if missing:
        raise SystemExit(f"FAIL — {len(missing)} of {len(FIGURES)} figures missing art.")
    print(f"OK — {len(FIGURES)} figures render.")
