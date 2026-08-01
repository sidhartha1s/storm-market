#!/usr/bin/env python3
"""ep4 one-shot scaffold: expand research/shot_ledger.md decisions (transcribed below as
SHOTS) into picture-track HTML injected at the marker in index.html. Editorial decisions
live in the ledger; this file only does arithmetic. Not pipeline code — episode-local."""
import json, re
from pathlib import Path

EP = Path(__file__).parent
t = json.load(open(EP/'timing.json'))
host = {r['id']: (r['start'], r['dur']) for r in t['rows']}

# (segment, [(rel, dur, path, flags...)]) — flags: 'cb' callback, 'gate' broadcast pull, 'grade' unified grade
V = 'mp4';
SHOTS = {
 'A0-S2': [(0,6,'media/ai/ai-rain-wrapped-tornado-v1.png'),(6,5,'media/stock/rainwall-pavement-01.mp4'),
   (11,5,'media/weathergov/wxgov-storm-photo-elreno-1.jpg'),(16,6,'media/radar/ktlx-vel-2314utc-1814cdt.png'),
   (22,8,'media/ai/ai-multi-vortex-tornado-v1.png')],
 'A0-S3': [(0,6,'media/weathergov/wxgov-storm-photo-elreno-2.jpg'),(6,6,'media/wikimedia/wikimedia-elreno-radar-2310z.png'),
   (12,16,'HOST:g-title'),(28,6,'media/weathergov/wxgov-storm-photo-elreno-3.jpg')],
 'A1-S1': [(0,6,'media/dvids/dvids-moore-137th-arw-938052.jpg'),(6,6,'media/dvids/dvids-moore-137th-arw-938055.jpg'),
   (12,8,'media/nwsnorman/nwsnorman-moore-may20-office-broll.mp4'),(20,6,'media/dvids/dvids-moore-137th-arw-938057.jpg'),
   (26,6,'media/dvids/dvids-oknatlguard-response-940434.jpg'),(32,8,'media/nwsnorman/nwsnorman-moore-may20-briefing-a.mp4'),
   (40,6,'media/dvids/dvids-moore-137th-arw-938060.jpg'),(46,8,'media/stock/stormsky-timelapse-01.mp4')],
 'A1-S1b': [(0,6,'media/stock/radio-closeup-01.mp4'),(6,6,'media/weathergov/wxgov-graphic-tornado-safety.png'),
   (12,6,'media/stock/plains-wheat-01.mp4'),(18,9,'media/nwsnorman/nwsnorman-spotter-training-a.mp4'),
   (27,6,'media/stock/dawn-dusk-sky-01.mp4'),(33,7,'media/weathergov/wxgov-graphic-car-safety.png'),
   (40,5,'media/stock/lightning-01.mp4'),(45,8,'media/stock/stormsky-timelapse-02.mp4'),(53,7,'media/stock/radio-closeup-02.mp4')],
 'A1-S2': [(0,9,'media/nwsnorman/nwsnorman-elreno-may31-745am-update.mp4'),(9,7,'media/weathergov/wxgov-map-ingredients.png'),
   (16,7,'media/stock/supercell-timelapse-01.mp4'),(23,7,'media/nwsnorman/nwsnorman-briefing-may30-noon.mp4'),
   (30,8,'media/weathergov/wxgov-satellite-loop-elreno.gif'),(38,6,'media/stock/plains-wheat-02.mp4'),
   (44,7,'media/stock/supercell-timelapse-02.mp4'),(51,5,'media/stock/dashboard-pov-rain-01.mp4')],
 'A1-S3': [(0,-1,'HOST:g-met-elreno')],
 'h-dawn': [(0,-1,'media/stock/dawn-dusk-sky-02.mp4')],
 'A2-S1': [(0,6,'media/radar/ktlx-ref-2303utc-1803cdt.png'),(6,6,'media/weathergov/wxgov-storm-photo-brennan-jontz.jpg'),
   (12,6,'media/weathergov/wxgov-map-polygons-okc-metro.jpg'),(18,5,'media/stock/plains-wheat-03.mp4'),
   (23,6,'media/weathergov/wxgov-storm-photo-elreno-4.jpg'),(29,6,'media/wikimedia/wikimedia-ef3-tornado-photo.jpg'),
   (35,6,'media/stock/supercell-timelapse-03.mp4'),(41,6,'media/radar/ktlx-ref-2307utc-1807cdt.png'),
   (47,5,'media/stock/dashboard-pov-rain-02.mp4')],
 'A2-S1b': [(0,7,'media/wikimedia/wikimedia-phased-array-radar-reflectivity.gif'),(7,8,'media/wikimedia/wikimedia-raxpol-radar-2324z.png'),
   (15,9,'media/nwsnorman/nwsnorman-receiving-the-warning.mp4'),(24,5,'media/stock/lightning-02.mp4'),
   (29,9,'media/weathergov/wxgov-radar-loop-elreno.gif'),(38,7,'media/stock/supercell-timelapse-04.mp4'),
   (45,8,'media/radar/ktlx-vel-2305utc-1805cdt.png'),(53,7,'media/stock/stormsky-timelapse-03.mp4'),
   (60,7.4,'media/radar/ktlx-ref-2311utc-1811cdt.png')],
 'A2-S2': [(0,-1,'HOST:g-width')],
 'A2-S3': [(0,7,'media/ai/ai-rain-wrapped-tornado-v2.png'),(7,5,'media/stock/rainwall-pavement-02.mp4'),
   (12,6,'media/weathergov/wxgov-storm-photo-elreno-5.jpg'),(18,7,'media/radar/ktlx-vel-2314utc-1814cdt.png','cb'),
   (25,7,'media/ai/ai-multi-vortex-tornado-v2.png'),(32,6,'media/radar/ktlx-ref-2316utc-1816cdt.png'),
   (38,5,'media/stock/storm-debris-wind-01.mp4'),(43,6,'media/radar/ktlx-ref-2318utc-1818cdt.png'),
   (49,5,'media/stock/rainwall-pavement-03.mp4'),(54,7,'media/weathergov/wxgov-supercell-photo-magnuson.jpg'),
   (61,5.1,'media/stock/lightning-03.mp4')],
 'A2-S3c': [(0,-1,'HOST:g-gearing')],
 'A2-S3b': [(0,6,'media/weathergov/wxgov-map-overview1.png'),(6,9,'media/nwsnorman/nwsnorman-elreno-radar-loop-a.mp4'),
   (15,5,'media/stock/dashboard-pov-rain-03.mp4'),(20,6,'media/radar/ktlx-ref-2309utc-1809cdt.png'),
   (26,6,'media/radar/ktlx-ref-2313utc-1813cdt.png'),(32,5,'media/stock/highway-traffic-rain-01.mp4'),
   (37,5,'media/stock/rainwall-pavement-04.mp4'),(42,6,'media/stock/plains-wheat-04.mp4'),
   (48,6,'media/radar/ktlx-ref-2315utc-1815cdt.png'),(54,5.8,'media/stock/stormsky-timelapse-04.mp4')],
 'a2-broadcast': [(0,-1,'media/broadcast/kfor-sutton-josefy-up-close.mp4','gate','grade')],
 'A3-S1': [(0,-1,'HOST:g-turn')],
 'A3-S1b': [(0,6,'media/stock/plains-wheat-05.mp4'),(6,8,'media/weathergov/wxgov-map-pns-damage-path.png'),
   (14,5,'media/stock/dashboard-pov-rain-04.mp4'),(19,6,'media/radar/ktlx-ref-2317utc-1817cdt.png'),
   (25,5,'media/stock/rainwall-pavement-05.mp4'),(30,7,'media/wikimedia/wikimedia-ground-scar.jpg'),
   (37,5,'media/stock/storm-debris-wind-02.mp4'),(42,6,'media/weathergov/wxgov-storm-photo-elreno-6.jpg'),
   (48,5,'media/stock/emergency-lights-rain-01.mp4'),(53,7,'media/stock/supercell-timelapse-05.mp4'),
   (60,5,'media/stock/highway-traffic-rain-02.mp4'),(65,10.9,'media/radar/ktlx-ref-2319utc-1819cdt.png')],
 'A3-S2': [(0,5,'media/broadcast/cnn-samaras-family-interview.mp4','gate','grade'),(5,7,'media/stock/supercell-timelapse-06.mp4'),
   (12,4,'media/broadcast/abc-3-storm-chasers-killed.mp4','gate','grade'),(16,6,'media/stock/plains-wheat-06.mp4'),
   (22,7,'media/nwsnorman/nwsnorman-spotter-training-d.mp4'),(29,6,'media/stock/dawn-dusk-sky-03.mp4'),
   (35,5,'media/stock/dashboard-pov-rain-05.mp4'),(40,5,'media/stock/lightning-04.mp4'),
   (45,8,'media/stock/stormsky-timelapse-05.mp4'),(53,7,'media/radar/ktlx-ref-2321utc-1821cdt.png'),
   (60,6,'media/stock/storm-debris-wind-03.mp4'),(66,6.4,'media/broadcast/koco-reshaped-storm-chasing.mp4','gate','grade')],
 'A3-S3': [(0,8,'media/radar/ktlx-vel-2319utc-1819cdt.png'),(8,5,'media/stock/rainwall-pavement-06.mp4'),
   (13,10,'media/stock/plains-wheat-01.mp4','cb'),(23,9,'media/stock/stormsky-timelapse-01.mp4','cb'),
   (32,13,'HOST:g-quote-robinson'),(45,5,'media/wikimedia/wikimedia-samaras-car-PDgov.jpg'),
   (51.5,6,'media/stock/storm-debris-wind-04.mp4'),(57.5,7,'media/radar/ktlx-ref-2323utc-1823cdt.png'),
   (64.5,8,'media/stock/dawn-dusk-sky-04.mp4'),(72.5,6.7,'media/stock/lightning-05.mp4')],
 'h-cobalt': [(0,-1,'media/ai/ai-rural-section-road-v1.png')],
 'A3-S3b': [(0,4,'media/broadcast/twc-bettes-suv-toss-marquee.mp4','gate','grade'),(4,5,'media/stock/storm-debris-wind-05.mp4'),
   (9,4,'media/broadcast/twc-bettes-describes-direct-hit.mp4','gate','grade'),(13,5,'media/stock/emergency-lights-rain-02.mp4'),
   (18,4,'media/broadcast/twc-bettes-returns.mp4','gate','grade'),(22,6,'media/weathergov/wxgov-damage-01.jpg'),
   (28,4,'media/broadcast/kfor-sutton-very-close-call.mp4','gate','grade'),(32,5,'media/stock/highway-traffic-rain-03.mp4'),
   (37,6,'media/radar/ktlx-ref-2325utc-1825cdt.png'),(43,7,'media/stock/stormsky-timelapse-02.mp4','cb'),
   (50,6.5,'media/weathergov/wxgov-damage-02.jpg')],
 'A4-S1': [(0,6,'media/stock/highway-traffic-rain-04.mp4'),(6,4,'media/broadcast/kfor-10yr-recap.mp4','gate','grade'),
   (10,6,'media/stock/highway-traffic-rain-05.mp4'),(16,6,'media/weathergov/wxgov-map-polygons-okc-metro.jpg','cb'),
   (22,5,'media/stock/dashboard-pov-rain-01.mp4','cb'),(27,6,'media/stock/radio-closeup-03.mp4'),
   (33,6,'media/stock/stormsky-timelapse-03.mp4','cb'),(39,8,'media/stock/highway-traffic-rain-06.mp4'),
   (47,5,'media/stock/emergency-lights-rain-03.mp4'),(52,6,'media/dvids/dvids-oknatlguard-response-940435.jpg'),
   (58,6.1,'media/stock/lightning-01.mp4','cb')],
 'A4-S2': [(0,7,'media/stock/radio-closeup-04.mp4'),(7,7,'media/weathergov/wxgov-graphic-car-safety.png','cb'),
   (14,36,'HOST:g-tweet-nws'),(50,6,'media/stock/lightning-02.mp4','cb'),
   (56,8,'media/weathergov/wxgov-map-overview2.png'),(64,9.3,'media/stock/dawn-dusk-sky-05.mp4')],
 'A4-S3': [(0,-1,'HOST:g-evac')],
 'A4-S4': [(0,8,'media/weathergov/wxgov-map-ef-contour-timing.jpg'),(8,6,'media/fema/fema-booher-elreno-damage-02.jpg'),
   (14,6,'media/weathergov/wxgov-damage-03.jpg'),(20,6,'media/radar/ktlx-ref-2331utc-1831cdt.png'),
   (26,7,'media/wikimedia/wikimedia-highest-rated-damage-indicator.jpg'),(33,6,'media/fema/fema-booher-elreno-damage-03.jpg'),
   (39,6,'media/dvids/dvids-guardsman-firefighter-rubble-search-9148500.jpg'),(45,6,'media/weathergov/wxgov-damage-04.jpg'),
   (51,6,'media/radar/ktlx-ref-2335utc-1835cdt.png'),(57,6,'media/stock/highway-traffic-rain-02.mp4','cb'),
   (63,6,'media/stock/stormsky-timelapse-05.mp4','cb'),(69,6.9,'media/weathergov/wxgov-damage-05.jpg')],
 'A5-S1': [(0,6,'media/stock/night-flood-street-01.mp4'),(6,7,'media/weathergov/wxgov-hydro-rainfall-48hr.png'),
   (13,6,'media/stock/night-flood-street-02.mp4'),(19,7,'media/ai/ai-night-city-flooding-v1.png'),
   (26,5,'media/stock/rainwall-pavement-01.mp4','cb'),(31,7,'media/weathergov/wxgov-hydro-24hr-mpe.png'),
   (38,6,'media/stock/night-flood-street-03.mp4'),(44,5,'media/stock/emergency-lights-rain-04.mp4'),
   (49,5.6,'media/stock/lightning-03.mp4','cb')],
 'A5-S2': [(0,8,'media/stock/night-flood-street-04.mp4'),(8,32,'HOST:g-numbers'),
   (40,7.3,'media/weathergov/wxgov-hydro-exceedance-probabilities.png')],
 'A5-S2b': [(0,6,'media/stock/night-flood-street-05.mp4'),(6,6,'media/weathergov/wxgov-graphic-tornado-safety.png','cb'),
   (12,6,'media/dvids/dvids-oknatlguard-response-940442.jpg'),(18,5,'media/stock/emergency-lights-rain-05.mp4'),
   (23,6,'media/dvids/dvids-oknatlguard-response-940443.jpg'),(29,6,'media/dvids/dvids-oknatlguard-response-940436.jpg'),
   (35,6,'media/stock/radio-closeup-01.mp4','cb'),(41,7,'media/weathergov/wxgov-map-storm-reports.jpg'),
   (48,6,'media/dvids/dvids-oknatlguard-response-940441.jpg'),(54,6,'media/stock/rainwall-pavement-02.mp4','cb'),
   (60,5.2,'media/stock/stormsky-timelapse-01.mp4','cb')],
 'h-rain': [(0,-1,'media/stock/lightning-04.mp4','cb')],
 'A6-S1': [(0,7,'media/wikimedia/wikimedia-preliminary-ef5-rating-survey.jpg'),(7,6,'media/weathergov/wxgov-damage-06.jpg'),
   (13,7,'media/radar/ktlx-vel-2309utc-1809cdt.png'),(20,6,'media/wikimedia/wikimedia-ef3-damage.jpeg'),
   (26,6,'media/fema/fema-booher-elreno-damage-04.jpg'),(32,6.5,'media/weathergov/wxgov-damage-07.jpg')],
 'A6-S2': [(0,-1,'HOST:g-efscale')],
 'A6-S2b': [(0,8,'media/wikimedia/wikimedia-preliminary-okc-tornado-tracks-map.png'),(8,7,'media/spc/spc-storm-reports-may31.gif'),
   (15,7,'media/wikimedia/wikimedia-ground-scar.jpg','cb'),(22,6,'media/weathergov/wxgov-damage-08.jpg'),
   (28,8,'media/wikimedia/wikimedia-tornado-timeline.jpg'),(36,6,'media/fema/fema-booher-elreno-damage-05.jpg'),
   (42,6,'media/weathergov/wxgov-damage-09.jpg'),(48,7,'media/wikimedia/wikimedia-raxpol-radar-2324z.png','cb'),
   (55,6,'media/fema/fema-booher-elreno-damage-06.jpg'),(61,8.4,'media/weathergov/wxgov-damage-10.jpg')],
 'A6-S3': [(0,7,'media/nwsnorman/lessons-most-dangerous-tornado.mp4'),(7,8,'media/nwsnorman/nwsnorman-roundtable-staff-recollections.mp4'),
   (15,6,'media/nwsnorman/nwsnorman-spotter-training-b.mp4'),(21,7,'media/nwsnorman/lessons-most-dangerous-tornado.mp4','cb'),
   (28,5,'media/stock/dashboard-pov-rain-02.mp4','cb'),(33,7,'media/nwsnorman/nwsnorman-spotter-training-c.mp4'),
   (40,7,'media/stock/supercell-timelapse-03.mp4','cb'),(47,8.4,'media/nwsnorman/nwsnorman-elreno-radar-loop-b.mp4')],
 'A7-S1': [(0,7,'media/ai/ai-rural-section-road-v2.png'),(7,6,'media/stock/plains-wheat-03.mp4','cb'),
   (13,5,'media/broadcast/kfor-tenth-victim.mp4','gate','grade'),(18,6,'media/stock/dawn-dusk-sky-01.mp4','cb'),
   (24,6,'media/wikimedia/wikimedia-ef3-tornado-photo.jpg','cb'),(30,5,'media/stock/lightning-05.mp4','cb'),
   (35,8,'media/ai/ai-rural-section-road-v1.png','cb'),(43,6,'media/stock/dawn-dusk-sky-02.mp4','cb'),
   (49,6.6,'media/weathergov/wxgov-storm-photo-elreno-1.jpg','cb')],
 'A7-S2': [(0,4,'media/broadcast/cnn-samaras-family-interview.mp4','gate','grade','cb'),
   (4,7,'media/wikimedia/wikimedia-phased-array-radar-reflectivity.gif','cb'),
   (11,7,'media/nwsnorman/nwsnorman-spotter-training-e.mp4'),(18,6,'media/weathergov/wxgov-supercell-photo-magnuson.jpg','cb'),
   (24,8,'media/spc/spc-satellite-tornado-9frame-anim.gif'),(32,7,'media/nwsnorman/nwsnorman-spotter-training-f.mp4'),
   (39,7,'media/stock/supercell-timelapse-04.mp4','cb'),(46,7.9,'media/nwsnorman/nwsnorman-briefing-may18-20-outlook.mp4')],
 'A7-S2b': [(0,7,'media/weathergov/wxgov-map-overview1.png','cb'),(7,7,'media/nwsnorman/nwsnorman-spotter-training-g.mp4'),
   (14,6,'media/dvids/dvids-oknatlguard-response-940446.jpg'),(20,4,'media/broadcast/koco-survivor-testimony-a.mp4','gate','grade'),
   (24,6,'media/fema/fema-booher-elreno-damage-07.jpg'),(30,6,'media/weathergov/wxgov-hydro-rainfall-48hr.png','cb'),
   (36,6,'media/dvids/dvids-oknatlguard-response-940447.jpg'),(42,7,'media/nwsnorman/nwsnorman-briefing-may17-18-a.mp4'),
   (49,7,'media/fema/fema-booher-elreno-damage-08.jpg')],
 'A7-S3': [(0,10,'media/radar/ktlx-ref-2340utc-1840cdt.png'),(10,9,'media/radar/ktlx-ref-2345utc-1845cdt.png'),
   (19,9,'media/fema/fema-booher-elreno-damage-09.jpg'),(28,10.3,'media/radar/ktlx-ref-0000utc-1900cdt-jun1.png'),
   (3,33,'PANEL:g-stat-elreno')],
 'A8-S1': [(0,-1,'media/stock/dawn-dusk-sky-03.mp4','cb'),(2,18,'PANEL:g-outro')],
}

lines=[]
counts={}
for seg, shots in SHOTS.items():
    if seg not in host: raise SystemExit(f'unknown segment {seg}')
    s0, sd = host[seg]
    # segments are followed by GAP except structure rows; extend last picture window to cover it
    lines.append(f'\n<!-- ── {seg} ({s0}, {sd}s) ── -->')
    plain=[x for x in shots if not str(x[2]).startswith(('HOST:','PANEL:'))]
    last_end_target = sd + (0.7 if seg.upper().startswith('A') else 0.0)
    for i,(rel,dur,path,*flags) in enumerate(shots):
        start=round(s0+rel,2)
        ishost=str(path).startswith('HOST:'); ispanel=str(path).startswith('PANEL:')
        if dur==-1: dur=round(last_end_target-rel,2)
        elif (not ishost and not ispanel) and plain and (rel,dur,path,*flags)==plain[-1]:
            dur=round(last_end_target-rel,2)  # clamp last plain window to segment end
        dur=round(dur,2)
        if ishost or ispanel:
            g=path.split(':')[1]
            trk = 2
            lines.append(f'<div id="host-{g}-{seg.lower()}" data-composition-id="{g}" data-composition-src="compositions/{g}.html" data-start="{start}" data-duration="{dur}" data-track-index="{trk}" data-width="1920" data-height="1080"></div>')
            continue
        name=Path(path).stem
        counts[name]=counts.get(name,0)+1
        uid=f'{seg.lower()}-{name}-{counts[name]}'
        cb=' data-callback="intentional-callback-spaced"' if 'cb' in flags else ''
        gate=' data-owner-gate="pending"' if 'gate' in flags else ''
        cls='clip'+(' grade-bc' if 'grade' in flags else '')
        ext=Path(path).suffix.lower()
        if ext=='.mp4':
            inner=f'<video id="v-{uid}" src="{path}" muted data-start="{start}" data-duration="{dur}"></video>'
        else:
            inner=f'<img id="i-{uid}" src="{path}">'
        lines.append(f'<section class="{cls}" id="{uid}" data-start="{start}" data-duration="{dur}" data-track-index="1"{cb}{gate}>{inner}</section>')

html=(EP/'index.html').read_text(encoding='utf-8')
MARK='<!-- PICTURE WINDOWS: authored per act below this line -->'
assert MARK in html
html=html.replace(MARK, MARK+'\n'+'\n'.join(lines))
(EP/'index.html').write_text(html, encoding='utf-8')
print('injected', sum(1 for l in lines if l.startswith('<')), 'elements')
print('reuse>2:', {k:v for k,v in counts.items() if v>2} or 'none')
