import re

RATE = 175.0 / 60.0  # words per second

def cues(label, text, phrases):
    words = text.split()
    # build lowercase, punctuation-stripped word list, keep original for phrase matching
    norm = [re.sub(r"[^a-z0-9]", "", w.lower()) for w in words]
    print(f"--- {label} ({len(words)} words, ~{len(words)/RATE:.2f}s total) ---")
    for phrase in phrases:
        pwords = [re.sub(r"[^a-z0-9]", "", w.lower()) for w in phrase.split()]
        n = len(pwords)
        found = None
        for i in range(len(norm) - n + 1):
            if norm[i:i+n] == pwords:
                found = i
                break
        if found is None:
            print(f"  MISSING: {phrase!r}")
        else:
            t = found / RATE
            print(f"  {phrase!r:45s} @ word {found:3d} -> {t:.2f}s")

# Comp 1/2: g-toll-counter / g-toll-counter-a4
cues("I toll (g-toll-counter)",
     "On the day it fell, Nepal's disaster agency counted twelve people who didn't survive the storm, with seven more missing. Later press counts ran as high as twenty four.",
     ["twelve people", "seven more missing", "twenty four"])

cues("A4 toll (g-toll-counter-a4)",
     "The toll is the first thing the reports disagree on. On the twenty seventh, Nepal's disaster agency counted twelve lives lost and seven missing. Across the border in India, fifty six more were lost. That weekend, the Indian news agency ANI put Nepal at twenty one, with five missing. The outlet NewsBytes reached twenty four, and the Indian channel CNBC TV18 added both countries together to reach about seventy. The counts cover different places and different hours, and the missing move into the toll as searches go on.",
     ["Nepal's disaster agency counted twelve", "seven missing", "ANI put Nepal at twenty one", "five missing", "NewsBytes reached twenty four", "about seventy"])

# Comp 3: g-gorge-vs-grand-canyon (inset in the I map beat)
cues("I gorge vs canyon",
     "The Kali Gandaki runs south out of the high Himalaya through one of the deepest gorges on Earth. The river sits about eighteen thousand feet below the summit beside it, three times the depth of the Grand Canyon in Arizona.",
     ["eighteen thousand feet", "three times the depth", "Grand Canyon"])

# Comp 4: g-himlung-height
cues("I himlung vs denali",
     "Up north, the same weather sent snow and rock down onto that camp on Himlung Himal. The peak rises about twenty three thousand four hundred feet. That's roughly three thousand feet higher than Denali, the tallest mountain in North America.",
     ["twenty three thousand four hundred feet", "three thousand feet higher than Denali"])

# Comp 5: g-hydro-card
cues("A1 hydro card",
     "Downstream, the river feeds a dam and power plant that was the largest in Nepal when it opened in two thousand two. It makes enough power for roughly one hundred and twenty thousand American homes. With a mountainside of mud in the water, the plant shut down until the river dropped.",
     ["largest in Nepal", "one hundred and twenty thousand American homes"])

# Comp 6: g-rain-bars
cues("A2 rain bars",
     "Just across the border in northern India, Al Jazeera reported about two and a half inches of rain that weekend. The normal for those days is under a third of an inch, so it was close to nine times as much.",
     ["two and a half inches of rain", "under a third of an inch", "nine times as much"])

# Comp 7: g-sep-2024
cues("A2 sep 2024",
     "Nepal has seen this late September calendar before. Two years ago, in the last days of September, late rain flooded the Kathmandu Valley. It set off landslides that took more than two hundred lives, on almost the same dates as this storm.",
     ["more than two hundred lives", "almost the same dates"])

# Comp 8: g-search-card
cues("A3 search card",
     "A helicopter reached the camp that evening. The next day, a ground team led by the climber Mingma G dug through snow about fifteen feet deep. Sixteen workers had been at the camp. By the twenty eighth, the searchers had found four, and twelve were still missing. Rescuers said survival was very unlikely.",
     ["snow about fifteen feet deep", "Sixteen workers had been at the camp", "found four", "twelve were still missing"])

# Comp 9: g-person-bhote (A3) and g-person-bhote-z (Z)
cues("A3 person bhote",
     "Then snow and rock came down onto the camp. One of the crew was Pasang Bhote, a climbing guide from the far east of Nepal.",
     ["Pasang Bhote", "climbing guide from the far east of Nepal"])

cues("Z person bhote return",
     "The climbers from the United Arab Emirates were due in Kathmandu on Thursday, October first. Their expedition didn't go ahead. The guides and cooks who went up first were the ones on the mountain. Four were found, and twelve were still missing on the twenty ninth. Pasang Bhote was among the first two they reached.",
     ["Four were found", "twelve were still missing", "Pasang Bhote was among the first two"])

# Comp 10: g-outro context (Z close, full)
cues("Z close full (for g-outro placement reference)",
     "The climbers from the United Arab Emirates were due in Kathmandu on Thursday, October first. Their expedition didn't go ahead. The guides and cooks who went up first were the ones on the mountain. Four were found, and twelve were still missing on the twenty ninth. Pasang Bhote was among the first two they reached. Nepal's monsoon usually starts leaving in early October, and in each of the last four years it left late. Until it does, trekkers on the Kali Gandaki road walk under soaked slopes. Crews on the high peaks work under fresh snow. This was The Warning Hour.",
     ["This was The Warning Hour"])
