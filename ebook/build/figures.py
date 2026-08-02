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
"""

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
            f'font-weight="{weight}" font-style="{style}" fill="{color}" '
            f'text-anchor="{anchor}">{s}</text>')


def _label_dot(x, y, r=3, color=AMBER):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{color}"/>'


# ---------------------------------------------------------------------------
# Figure 1 — Safe room selection (Protection 23) — MANDATORY, sold by name
# ---------------------------------------------------------------------------
def fig_safe_room_plan():
    body = f'''
    <rect x="6" y="6" width="328" height="116" fill="none" stroke="{INK}" stroke-width="2.5"/>
    <line x1="118" y1="6" x2="118" y2="78" stroke="{INK}" stroke-width="1.6"/>
    <line x1="118" y1="78" x2="232" y2="78" stroke="{INK}" stroke-width="1.6"/>
    <line x1="232" y1="6" x2="232" y2="78" stroke="{INK}" stroke-width="1.6"/>
    <line x1="232" y1="40" x2="334" y2="40" stroke="{INK}" stroke-width="1.6"/>
    <rect x="118" y="40" width="114" height="38" fill="{AMBER_BG}" stroke="{AMBER}" stroke-width="2"/>
    {_text(175, 63, "SAFE ROOM", size=10, weight=700, color=AMBER, anchor="middle")}
    <g stroke="{ALERT}" stroke-width="2.4">
      <line x1="30" y1="6" x2="66" y2="6"/><line x1="84" y1="6" x2="108" y2="6"/>
      <line x1="6" y1="52" x2="6" y2="88"/><line x1="334" y1="60" x2="334" y2="96"/>
      <line x1="150" y1="122" x2="190" y2="122"/><line x1="248" y1="122" x2="286" y2="122"/>
    </g>
    {_text(60, 30, "bedroom", size=8)}
    {_text(280, 28, "kitchen", size=8, anchor="end")}
    {_text(280, 104, "living", size=8, anchor="end")}
    {_text(46, 104, "garage", size=8)}
    <g transform="translate(6,140)">
      <line x1="0" y1="0" x2="18" y2="0" stroke="{ALERT}" stroke-width="2.4"/>
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
    def card(title, icon_svg, lines, accent):
        items = "".join(f'<div class="tr-line">{ln}</div>' for ln in lines)
        return (f'<div class="tr-card" style="border-color:{accent}">'
                f'<div class="tr-icon">{icon_svg}</div>'
                f'<div class="tr-title" style="color:{accent}">{title}</div>{items}</div>')

    icon_safe = (f'<svg viewBox="0 0 40 40" width="30" height="30">'
                 f'<rect x="4" y="4" width="32" height="32" fill="none" stroke="{INK}" stroke-width="2"/>'
                 f'<rect x="13" y="13" width="14" height="14" fill="{AMBER_BG}" stroke="{AMBER}" stroke-width="2"/></svg>')
    icon_warm = (f'<svg viewBox="0 0 40 40" width="30" height="30">'
                 f'<rect x="4" y="10" width="32" height="26" fill="none" stroke="{INK}" stroke-width="2"/>'
                 f'<circle cx="20" cy="4" r="5" fill="none" stroke="{ALERT}" stroke-width="2"/>'
                 f'<g stroke="{ALERT}" stroke-width="1.4">'
                 f'<line x1="20" y1="-4" x2="20" y2="-1"/><line x1="11" y1="-1" x2="13" y2="1"/>'
                 f'<line x1="29" y1="-1" x2="27" y2="1"/></g></svg>')
    icon_cool = (f'<svg viewBox="0 0 40 40" width="30" height="30">'
                 f'<rect x="4" y="10" width="32" height="26" fill="none" stroke="{INK}" stroke-width="2"/>'
                 f'<path d="M0 16 h10 M0 20 h14 M0 24 h10" stroke="{AMBER}" stroke-width="1.6" fill="none" marker-end="url(#arrow)"/>'
                 f'<path d="M40 16 h-10 M40 24 h-10" stroke="{AMBER}" stroke-width="1.6" fill="none"/></svg>')

    defs = (f'<defs><marker id="arrow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">'
            f'<path d="M0,0 L6,3 L0,6 z" fill="{AMBER}"/></marker></defs>')

    cards = (
        card("SAFE ROOM &middot; P23", icon_safe,
             ["Lowest floor.", "Zero exterior walls.", "No picture windows.", "For: wind, minutes"], ALERT)
        + card("WARM ROOM &middot; P26", icon_warm,
               ["Interior, small.", "South window for daytime sun.", "Body heat does the rest.", "For: cold outage, days"], AMBER)
        + card("COOLING ROOM &middot; P29", icon_cool,
               ["Lowest floor, north side.", "Fewest windows, best cross-flow.", "Fans exhaust, not blow on you above 90&deg;F.", "For: heat outage, days"], INK_SOFT)
    )
    style = (
        '<style>'
        '.tr-wrap{display:flex;gap:8pt;font-family:' + SANS + '}'
        '.tr-card{flex:1;border:.75pt solid;padding:6pt 7pt;background:#fff}'
        '.tr-icon{margin-bottom:3pt}'
        '.tr-title{font-size:7.4pt;font-weight:700;letter-spacing:.04em;text-transform:uppercase;margin-bottom:4pt}'
        '.tr-line{font-size:7.2pt;line-height:1.35;color:' + INK_SOFT + ';margin-bottom:2pt}'
        '</style>'
    )
    inner = f'{style}<div class="tr-wrap" style="height:1.55in;box-sizing:border-box">{cards}</div>'
    return (f'<figure>{defs}{inner}'
            f'<figcaption><b>Figure 2</b> — One house, three different best rooms. The room that '
            f'protects you from wind is not the room that keeps you warm, which is not the room '
            f'that keeps you cool — the criteria conflict on purpose. Original diagram.</figcaption>'
            f'</figure>')


# ---------------------------------------------------------------------------
# Figure 3 — Shut-off literacy (Protection 35)
# ---------------------------------------------------------------------------
def fig_utility_shutoffs():
    body = f'''
    <path d="M20 90 L140 20 L260 90 Z" fill="none" stroke="{INK}" stroke-width="2"/>
    <rect x="40" y="90" width="200" height="90" fill="none" stroke="{INK}" stroke-width="2.2"/>
    <line x1="40" y1="140" x2="240" y2="140" stroke="{INK_MUTE}" stroke-width="1.2" stroke-dasharray="3,3"/>
    {_text(244, 137, "main floor", size=7, color=INK_MUTE)}
    {_text(244, 176, "basement / crawlspace", size=7, color=INK_MUTE)}
    <rect x="330" y="150" width="26" height="26" fill="none" stroke="{INK}" stroke-width="1.6"/>
    {_text(343, 168, "P", size=9, weight=700, anchor="middle")}
    {_text(322, 195, "electrical panel", size=7.4, anchor="end")}
    <line x1="330" y1="163" x2="240" y2="163" stroke="{AMBER}" stroke-width="1.4" stroke-dasharray="2,2"/>
    <circle cx="16" cy="130" r="7" fill="none" stroke="{ALERT}" stroke-width="2"/>
    {_text(16, 133, "G", size=8, weight=700, anchor="middle", color=ALERT)}
    {_text(2, 112, "gas shut-off,", size=7.4, color=ALERT)}
    {_text(2, 121, "wrench hangs here", size=7.4, color=ALERT)}
    <line x1="20" y1="123" x2="40" y2="128" stroke="{ALERT}" stroke-width="1.2" stroke-dasharray="2,2"/>
    <circle cx="66" cy="180" r="7" fill="none" stroke="{AMBER}" stroke-width="2"/>
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
        t = "".join(_text(x + 16, y + 3 + i * 10, ln, size=7.4) for i, ln in enumerate(text_lines))
        return (f'<circle cx="{x}" cy="{y}" r="8" fill="{AMBER}"/>'
                f'{_text(x, y + 3, str(n), size=8.5, weight=700, color=PAPER, anchor="middle")}{t}')

    body = f'''
    <rect x="150" y="30" width="70" height="120" rx="8" fill="none" stroke="{INK}" stroke-width="2.4"/>
    <line x1="150" y1="20" x2="150" y2="30" stroke="{INK}" stroke-width="1.6"/>
    <path d="M150 20 h-20" stroke="{INK}" stroke-width="1.6" fill="none"/>
    <rect x="118" y="14" width="12" height="12" fill="none" stroke="{INK}" stroke-width="1.6"/>
    {_text(112, 12, "cold inlet valve", size=7, anchor="end")}
    <path d="M220 40 h20 v-14 h20" stroke="{INK}" stroke-width="1.6" fill="none"/>
    <rect x="234" y="18" width="10" height="10" fill="none" stroke="{INK}" stroke-width="1.4"/>
    {_text(248, 26, "hot tap opened elsewhere", size=7)}
    <rect x="176" y="150" width="18" height="10" fill="none" stroke="{INK}" stroke-width="1.6"/>
    <path d="M185 160 v14 h20" stroke="{INK}" stroke-width="1.6" fill="none"/>
    {_text(210, 178, "drain valve &rarr; clean container", size=7)}
    {_text(160, 165, "gas / breaker off at base", size=6.8, color=INK_MUTE)}
    {step(1, 60, 20, ["kill the energy —", "gas pilot or breaker"])}
    {step(2, 60, 55, ["shut the cold-water", "inlet at the tank"])}
    {step(3, 60, 90, ["open a hot tap", "elsewhere to admit air"])}
    {step(4, 60, 125, ["draw from the drain", "valve into a container"])}
    {step(5, 60, 160, ["do not refill or", "re-energize until safe"])}
    <line x1="70" y1="20" x2="118" y2="20" stroke="{INK_MUTE}" stroke-width="1" stroke-dasharray="2,2"/>
    <line x1="70" y1="55" x2="150" y2="60" stroke="{INK_MUTE}" stroke-width="1" stroke-dasharray="2,2"/>
    <line x1="70" y1="90" x2="220" y2="30" stroke="{INK_MUTE}" stroke-width="1" stroke-dasharray="2,2"/>
    <line x1="70" y1="125" x2="180" y2="155" stroke="{INK_MUTE}" stroke-width="1" stroke-dasharray="2,2"/>
    '''
    return _figure(4, "The five-step draw-off sequence in order, and where each valve is on the "
                   "tank — a conventional water heater holds forty to eighty gallons of potable "
                   "water most households never think to use.",
                   _svg((360, 200), 1.55, "Water heater schematic showing the five-step draw-off sequence", body))


# ---------------------------------------------------------------------------
# Figure 5 — Garage door bracing (Protection 74)
# ---------------------------------------------------------------------------
def fig_garage_door_pressure():
    body = f'''
    <g>
      <rect x="14" y="34" width="150" height="70" fill="#f2efe9" stroke="{INK}" stroke-width="2"/>
      <path d="M14 34 L89 10 L164 34" fill="none" stroke="{INK}" stroke-width="2"/>
      <rect x="36" y="58" width="106" height="46" fill="#fff" stroke="{INK}" stroke-width="1.4"/>
      <g stroke="{INK_MUTE}" stroke-width="1.6"><line x1="0" y1="74" x2="30" y2="74"/><line x1="0" y1="88" x2="30" y2="88"/></g>
      {_text(89, 118, "braced &mdash; 16 ft door holds", size=7.6, anchor="middle")}
      {_text(89, 127, "pressure stays outside", size=7.6, anchor="middle")}
    </g>
    <g>
      <rect x="214" y="34" width="150" height="70" fill="#f2efe9" stroke="{INK}" stroke-width="2"/>
      <path d="M210 30 L289 4 L368 30" fill="none" stroke="{ALERT}" stroke-width="2.4"/>
      <path d="M240 58 l106 0 l-16 46 l-74 0z" fill="{AMBER_BG}" stroke="{ALERT}" stroke-width="1.6"/>
      <g stroke="{ALERT}" stroke-width="1.8">
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
    <rect x="10" y="52" width="34" height="34" fill="none" stroke="{INK}" stroke-width="2.2"/>
    <path d="M10 52 L27 38 L44 52" fill="none" stroke="{INK}" stroke-width="2.2"/>
    <rect x="44" y="30" width="26" height="106" fill="{ALERT}" fill-opacity="0.16" stroke="{ALERT}" stroke-width="1.4"/>
    {_text(57, 24, "ZONE 0", size=7.2, weight=700, anchor="middle", color=ALERT)}
    {_text(57, 150, "0&ndash;5 ft", size=7.2, anchor="middle", color=ALERT)}
    <rect x="70" y="30" width="120" height="106" fill="{AMBER}" fill-opacity="0.14" stroke="{AMBER}" stroke-width="1.4"/>
    {_text(130, 24, "ZONE 1", size=7.2, weight=700, anchor="middle", color=AMBER)}
    {_text(130, 150, "5&ndash;30 ft &mdash; thinned, irrigated", size=7.2, anchor="middle", color=AMBER)}
    <rect x="190" y="30" width="150" height="106" fill="{INK_MUTE}" fill-opacity="0.12" stroke="{INK_MUTE}" stroke-width="1.4"/>
    {_text(265, 24, "ZONE 2", size=7.2, weight=700, anchor="middle", color=INK_SOFT)}
    {_text(265, 150, "30&ndash;100 ft &mdash; ladder fuels removed", size=7.2, anchor="middle", color=INK_SOFT)}
    <path d="M340 40 l14 -6 l0 4 l10 0 l0 4 l-10 0 l0 4 z" fill="{INK_MUTE}"/>
    {_text(358, 30, "scale compressed", size=6.6, color=INK_MUTE)}
    {_text(358, 39, "past 30 ft", size=6.6, color=INK_MUTE)}
    <line x1="44" y1="90" x2="10" y2="90" stroke="{INK}" stroke-width="1"/>
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
    <line x1="6" y1="150" x2="374" y2="150" stroke="{INK_MUTE}" stroke-width="1.2"/>
    {_text(378, 153, "grade", size=7, color=INK_MUTE)}
    <rect x="90" y="60" width="200" height="90" fill="#f2efe9" stroke="{INK}" stroke-width="2.2"/>
    <rect x="6" y="96" width="84" height="8" fill="{AMBER_BG}" stroke="{AMBER}" stroke-width="1.4"/>
    {_text(48, 92, "water outside", size=7, anchor="middle", color=AMBER)}
    <rect x="290" y="96" width="84" height="8" fill="{AMBER_BG}" stroke="{AMBER}" stroke-width="1.4"/>
    {_text(332, 92, "water inside", size=7, anchor="middle", color=AMBER)}
    <rect x="110" y="128" width="22" height="14" fill="none" stroke="{ALERT}" stroke-width="1.8"/>
    <rect x="248" y="128" width="22" height="14" fill="none" stroke="{ALERT}" stroke-width="1.8"/>
    <path d="M90 135 h20 M132 135 h20" stroke="{ALERT}" stroke-width="1.4" marker-end="url(#fo-arrow)"/>
    <path d="M228 135 h20 M270 135 h20" stroke="{ALERT}" stroke-width="1.4" marker-end="url(#fo-arrow)"/>
    <defs><marker id="fo-arrow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <path d="M0,0 L6,3 L0,6 z" fill="{ALERT}"/></marker></defs>
    {_text(190, 30, "minimum two openings, engineered to equalize pressure", size=7.6, anchor="middle", weight=700, color=ALERT)}
    <line x1="121" y1="128" x2="150" y2="46" stroke="{INK_MUTE}" stroke-width="1" stroke-dasharray="2,2"/>
    <line x1="259" y1="128" x2="230" y2="46" stroke="{INK_MUTE}" stroke-width="1" stroke-dasharray="2,2"/>
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
        return (f'<circle cx="{x}" cy="{y}" r="7" fill="{PAPER}" stroke="{color}" stroke-width="2"/>'
                f'{_text(x, y + 3, label, size=7, weight=700, anchor="middle", color=color)}')

    body = f'''
    <path d="M20 44 L170 12 L320 44" fill="none" stroke="{INK}" stroke-width="2"/>
    <rect x="20" y="44" width="300" height="70" fill="none" stroke="{INK}" stroke-width="2"/>
    <line x1="130" y1="44" x2="130" y2="114" stroke="{INK_MUTE}" stroke-width="1.2"/>
    <line x1="210" y1="44" x2="210" y2="114" stroke="{INK_MUTE}" stroke-width="1.2"/>
    {_text(75, 60, "bedroom", size=7, anchor="middle", color=INK_MUTE)}
    {_text(170, 60, "hallway", size=7, anchor="middle", color=INK_MUTE)}
    {_text(265, 60, "bedroom", size=7, anchor="middle", color=INK_MUTE)}
    {_text(170, 40, "upper floor", size=7, anchor="middle", color=INK_MUTE)}
    {alarm(75, 52, "S")}
    {alarm(265, 52, "S")}
    {alarm(170, 52, "C+S")}
    <rect x="20" y="114" width="300" height="60" fill="none" stroke="{INK}" stroke-width="2"/>
    {_text(170, 108, "main floor", size=7, anchor="middle", color=INK_MUTE)}
    {alarm(170, 122, "C+S")}
    <rect x="20" y="174" width="300" height="46" fill="none" stroke="{INK}" stroke-width="2"/>
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
        return (f'<rect x="{x}" y="24" width="10" height="110" fill="#fff" stroke="{INK}" stroke-width="1.6"/>'
                f'<path d="M{x+5} 40 v18" stroke="{AMBER}" stroke-width="1.6" marker-end="url(#bf-arrow)"/>'
                f'<path d="M{x+5} 78 v18" stroke="{AMBER}" stroke-width="1.6" marker-end="url(#bf-arrow)"/>'
                f'<path d="M{x+5} 96 v-18" stroke-width="0"/>')

    body = f'''
    <defs><marker id="bf-arrow" markerWidth="6" markerHeight="6" refX="3" refY="5" orient="auto">
      <path d="M0,0 L6,0 L3,6 z" fill="{AMBER}"/></marker></defs>
    {filt(60)}{filt(76)}{filt(92)}{filt(108)}
    <path d="M60 24 h58 M60 134 h58" stroke="{ALERT}" stroke-width="2" stroke-dasharray="3,2"/>
    {_text(89, 16, "tape seals every seam", size=6.8, anchor="middle", color=ALERT)}
    <circle cx="210" cy="79" r="46" fill="none" stroke="{INK}" stroke-width="2.2"/>
    <rect x="164" y="33" width="92" height="92" fill="none" stroke="{INK}" stroke-width="2.2"/>
    <path d="M256 40 L300 20 L300 138 L256 118" fill="{AMBER_BG}" stroke="{AMBER}" stroke-width="1.6"/>
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
      fill="{AMBER}" fill-opacity="0.12" stroke="{AMBER}" stroke-width="1.2" stroke-dasharray="3,2"/>
    {_text(190, 8, "actual hazard extent &mdash; surge, rain, tornadoes", size=7.6, anchor="middle", color=AMBER, weight=700)}
    <path d="M10 90 L380 30 L380 150 Z" fill="{INK}" fill-opacity="0.14" stroke="{INK}" stroke-width="1.8"/>
    <line x1="10" y1="90" x2="380" y2="90" stroke="{INK}" stroke-width="1.2" stroke-dasharray="2,2"/>
    {_text(190, 84, "cone: probable path of the storm's CENTER only", size=7.6, anchor="middle", weight=700)}
    <circle cx="10" cy="90" r="5" fill="{INK}"/>
    {_text(10, 108, "now", size=7, anchor="middle")}
    <circle cx="392" cy="176" r="4" fill="{ALERT}"/>
    {_text(392, 190, "actual track,", size=6.8, anchor="end", color=ALERT)}
    <path d="M375 165 L392 176" stroke="{ALERT}" stroke-width="1.2"/>
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
    <rect x="10" y="140" width="100" height="30" fill="none" stroke="{INK_MUTE}" stroke-width="1.6"/>
    {_text(60, 128, "BASE", size=8, weight=700, anchor="middle", color=INK_MUTE)}
    {_text(60, 158, "no tag &mdash; still act", size=7.2, anchor="middle", color=INK_MUTE)}
    <rect x="130" y="100" width="100" height="70" fill="{AMBER_BG}" stroke="{AMBER}" stroke-width="1.8"/>
    {_text(180, 88, "CONSIDERABLE", size=8, weight=700, anchor="middle", color=AMBER)}
    <circle cx="160" cy="140" r="10.5" fill="none" stroke="{AMBER}" stroke-width="1.6"/>
    {_text(180, 155, "1.75 in hail (golf ball)", size=7, anchor="start", color=AMBER)}
    {_text(180, 165, "or 70 mph wind", size=7, anchor="start", color=AMBER)}
    <rect x="250" y="50" width="120" height="120" fill="{AMBER_BG}" stroke="{ALERT}" stroke-width="2.2"/>
    {_text(310, 38, "DESTRUCTIVE", size=8, weight=700, anchor="middle", color=ALERT)}
    <circle cx="285" cy="110" r="16.5" fill="none" stroke="{ALERT}" stroke-width="2"/>
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
    <circle cx="150" cy="150" r="140" fill="{AMBER_BG}" fill-opacity="0.5" stroke="{AMBER}" stroke-width="1.6"/>
    <circle cx="150" cy="150" r="34" fill="{ALERT}" fill-opacity="0.18" stroke="{ALERT}" stroke-width="1.8"/>
    <rect x="146" y="146" width="8" height="8" fill="{INK}"/>
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
    W = 460
    xs = [10 + (l - lo) / span * W for l in logs]
    bars = []
    for i in range(6):
        x0 = xs[i - 1] if i > 0 else 10
        x1 = xs[i]
        w = max(x1 - x0, 4)
        bars.append(f'<rect x="{x0:.1f}" y="60" width="{w:.1f}" height="34" '
                     f'fill="{colors[i]}" fill-opacity="0.20" stroke="{colors[i]}" stroke-width="1.4"/>')
        mid = (x0 + x1) / 2
        above = i % 2 == 0
        ty = 52 if above else 112
        ly = ty + (10 if above else 10)
        bars.append(_text(mid, ty, names[i], size=7.2, weight=700, anchor="middle", color=colors[i]))
        bars.append(_text(mid, ly, labels[i], size=6.6, anchor="middle", color=INK_MUTE))
    body = "".join(bars) + _text(230, 135, "time axis is log-scaled &mdash; each phase is roughly an order of magnitude longer than the last", size=6.6, anchor="middle", color=INK_MUTE, italic=True)
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
