# ep-mayfield-2021 geo data (10-11 Dec 2021)

All files fetched 22 Oct 2026. All sources are US government works (NOAA, NWS, SPC, NASA, USGS, Census): public domain,
no licence needed. Coordinates are EPSG:4326, GeoJSON order [lon, lat]. Times in properties are UTC unless the field
name says `cst` (CST = UTC minus 6 h). Check: every `*.geojson` here loads with `json.load`.

## Vector files (this folder, tracked)

| File | Source URL | Holds |
|---|---|---|
| `tornado_tracks_dat.geojson` | https://services.dat.noaa.gov/arcgis/rest/services/nws_damageassessmenttoolkit/DamageViewer/FeatureServer/1 (NWS Damage Assessment Toolkit, layer "Damage Lines", query `stormdate` 10-12 Dec 2021, `outSR=4326`) | All 71 tornado tracks of the outbreak as LineStrings (the real surveyed path, 2 to 106 vertices). Attributes: `wfo`, `efscale`, `efnum`, `length` (miles), `width` (yards), `injuries`, `fatalities`, `starttime`/`endtime` (epoch ms), plus added `start_utc`, `end_utc`, `start_cst`, `end_cst`, `time_suspect`, `length_mi`, `track_name`. |
| `tornado_tracks_named.geojson` | same, filtered | The three tracks the graphics name. `track_name` = "Mayfield (Woodland Mills TN to Falls of Rough KY)" (EF4, 165.6 mi, 8:49 to 11:47 PM CST, 82 vertices), "Bay AR to Samburg TN" (EF4, 81.6 mi, 7:07 to 8:36 PM CST, 59 vertices), "Edwardsville IL" (EF3, 4.28 mi, 8:27 to 8:32 PM CST, 32 vertices). |
| `dat_raw.geojson` | same query, unmodified | The raw response that `tornado_tracks_dat.geojson` was built from (no added fields). |
| `warnings.geojson` | https://mesonet.agron.iastate.edu/geojson/sbw.py (IEM archive of NWS storm-based warning polygons) | Three Tornado Warning polygons: LSX TO.W.0051, issued 2021-12-11T02:06Z = 8:06 PM CST (contains Edwardsville); PAH TO.W.0036, issued 03:05Z = 9:05 PM CST (contains Mayfield); PAH TO.W.0038, issued 03:26Z = 9:26 PM CST, the Tornado Emergency for Mayfield (`is_emergency` true, damage tag CATASTROPHIC; polygon spans -88.75..-88.57 lon, 36.67..36.79 lat). Point-in-polygon checked. |
| `product_202112110206-KLSX-WFUS53-TORLSX.txt`, `product_202112110305-KPAH-WFUS53-TORPAH.txt`, `product_202112110326-KPAH-WFUS53-TORPAH.txt` | https://mesonet.agron.iastate.edu/api/1/nwstext/<product id> | The full NWS text of those three warnings (the 9:26 PM one is headed "TORNADO EMERGENCY for Mayfield"). |
| `iem_raw_LSX.geojson`, `iem_raw_PAH.geojson` | same `sbw.py`, snapshots at 02:10Z (LSX) and 03:30Z (PAH) | Every tornado and severe-thunderstorm warning in force at those instants (5 and 6 features), with all IEM attributes. The names are misleading: they hold warning snapshots, not raw per-office dumps. |
| `spc_outlooks.geojson` | https://mesonet.agron.iastate.edu/api/1/nws/spc_outlook.geojson (day, valid=2021-12-10, cycle) | 32 polygons, `day` field 1/2/3. Day 3 product 2021-12-08T08:15Z (2:15 AM CST): categorical TSTM/MRGL/SLGT plus any-severe 5% and 15%. Day 2 product 2021-12-09T06:58Z (12:58 AM CST): categorical up to ENH, tornado 2/5/10% and SIGN (hatched), wind, hail. Day 1 product 2021-12-10T16:18Z (10:18 AM CST): categorical up to MDT, tornado 2/5/10/15% and SIGN, wind, hail. Each feature has `category`, `threshold`, `product_issue`, `product_id`. Issue times match the fact sheet. |
| `watches.geojson` | https://mesonet.agron.iastate.edu/api/1/spc_watch_outline.geojson?valid=2021-12-11T00:00:00Z | Tornado Watch 552 (issued 21:00Z = 3:00 PM CST; contains Mayfield) and 553 (issued 23:20Z = 5:20 PM CST; contains Edwardsville), the four-sided outlines, not county unions. |
| `places.geojson` | Census 2021 Gazetteer places (https://www2.census.gov/geo/docs/maps-data/data/gazetteer/2021_Gazetteer/2021_Gaz_place_national.zip), internal points; Falls of Rough from USGS GNIS (gaz_id 507976); Amazon from the Census geocoder | 11 points: Mayfield KY, Edwardsville IL, Woodland Mills TN, Falls of Rough KY, Bay AR, Samburg TN, Dawson Springs KY, Memphis TN, Paducah KY, St. Louis MO, and the Amazon delivery station at 3077 Gateway Commerce Dr S, Edwardsville (address per St. Louis Public Radio, 26 Aug 2022). Each point carries its own `source`. |
| `t.json` | none | Stray scratch file left by the fetch run; it holds one note line and can be deleted. |

## Caveats the builders need

- DAT `fatalities` is per-track and incomplete (the 71 tracks sum to 32, the Mayfield track shows 0). Do not use it for
  death counts; use the NWS Service Assessment numbers in `research/fact-sheet.md`.
- DAT lengths differ slightly from the Service Assessment (Bay-Samburg 81.6 vs 80.3 mi; Edwardsville 4.28 vs 3.65 mi;
  Mayfield 165.6 matches). The script uses the Service Assessment figures; draw the DAT geometry.
- Two tracks have impossible end times in DAT (end before start, or days later); flagged `time_suspect: true`, `end_*` null.
- Census place points are internal points of city boundaries, not city-hall points. The Amazon point is address-range
  interpolated, accurate to the street frontage.
- The warning polygons are the issuance polygons. Later updates (SVS) reshaped some of them; not fetched.

## Bulk data (gitignored, `episodes/ep-mayfield-2021/media/data/`)

NEXRAD Level II, 11 Dec 2021 UTC. The public NOAA bucket `noaa-nexrad-level2` refused listing (HTTP 403 AccessDenied for
list and for guessed keys), and Unidata THREDDS held no 2021 catalog. Same NOAA archive, from the free Google Cloud
public mirror: `https://storage.googleapis.com/gcp-public-data-nexrad-l2/2021/12/11/<site>/` (hourly tars, no login).
Volumes in the window were extracted to `nexrad/<site>/*.ar2v` (header `AR2V0006`); the tars sit in `nexrad/<site>/tar/`.

| Site | Window asked (CST) | Volumes extracted | Size |
|---|---|---|---|
| KPAH | 20:45-21:40 | 9, 02:46:43Z to 03:35:29Z | 126 MB |
| KLSX | 20:00-20:40 | 7, 02:04:01Z to 02:38:50Z (first volume starts 4 min in) | 92 MB |
| KNQA | 19:00-20:55 | 20, 01:04:40Z to 02:54:59Z | 155 MB |

Tars: 537 MB in total. `nexrad/_dl_done.txt` is a marker file from the download run.

NASA Worldview snapshots, `worldview/`, fetched from https://wvs.earthdata.nasa.gov/api/v1/snapshot (EPSG:4326,
BBOX 33,-95,41,-82, 1920 x 1182 px, JPEG, TIME=2021-12-10, daytime, before any storm). NASA imagery, public domain.
- `mid-south-2021-12-10-VIIRS_SNPP_CorrectedReflectance_TrueColor.jpg`: seamless, no swath edge.
- `mid-south-2021-12-10-MODIS_Terra_CorrectedReflectance_TrueColor.jpg`: has a diagonal swath seam at the right edge.
Both frames are mostly solid cloud: the mid-South was overcast that day, so little ground shows (dark patches at lower
left and top right only). That is the honest picture of the day, but a builder wanting visible terrain needs another day.

## Not found

- Illinois Public Act 104-0262 (HB 2987) text: ilga.gov did not answer (connection timeout on `www.ilga.gov` and
  `ilga.gov`, home page included, 22 Oct 2026); nothing saved to `research/sources/`.
