import csv

rows = [
["cpc-weekly-sst-departures-change-last-4weeks.png","https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/lanina/enso_evolution-status-fcsts-web.pdf","US-gov PD","NOAA Climate Prediction Center","Four-panel weekly relative SST anomaly maps for 19 Aug, 26 Aug, 2 Sept and 9 Sept 2026 showing the warm plume strengthening week by week","0","extracted page 8 of the 14-Sep-2026 CPC PDF","Four stacked equatorial-Pacific maps dated 19 Aug, 26 Aug, 2 Sept and 9 Sept 2026 each show a deep red-orange warm band stretching from the Date Line to South America, visibly darkening and extending week over week."],
["cpc-upper-ocean-heat-content-weekly-anomaly.png","https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/lanina/enso_evolution-status-fcsts-web.pdf","US-gov PD","NOAA Climate Prediction Center","Central/Eastern Pacific upper-ocean (0-300m) weekly heat content anomaly time series, Oct 2025-Sept 2026","0","extracted page 11 of the 14-Sep-2026 CPC PDF","A filled line chart from October 2025 to September 2026 shows a blue negative-anomaly dip through the winter turning into a steadily climbing orange positive anomaly that reaches its highest point, above 3 degrees C, in the final August-September weeks."],
["pixabay-pacific-coast-aerial-waves.mp4","https://pixabay.com/videos/id-24216/","Pixabay Content License (free to use)","javlemus via Pixabay","Aerial drone footage of Pacific coastline with waves rolling onto a sandy shore","31.0","stock b-roll","A drone shot looking down at a turquoise Pacific shoreline where white-capped waves break repeatedly onto a curving sandy beach, palm-lined in the background."],
["pixabay-dry-outback-red-earth-aerial.mp4","https://pixabay.com/videos/id-317977/","Pixabay Content License (free to use)","Ian5152 via Pixabay","Aerial drone footage of dry red-earth outback terrain","10.8","stock b-roll; similar-looking arid landscape, not claimed as a specific location","A drone shot flying low over cracked, rust-red arid outback ground dotted with sparse dry scrub, conveying drought-stricken terrain."],
]

path = r"C:\Users\Sidhartha\Automation Projects\storm-market\library\mini-storms\el-nino-2026\sept-2026\provenance.csv"
with open(path, "a", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    for r in rows:
        w.writerow(r)
print("appended", len(rows), "rows")
