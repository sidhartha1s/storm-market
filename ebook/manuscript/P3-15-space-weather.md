# Part Three, Playbook 15 — Space Weather, Geomagnetic Storms and EMP

Target: 10 pages · draft 1, 2026-07-29

---

## The event

On 13 March 1989, at about half past two in the morning, the entire Hydro-Québec grid collapsed in under
two minutes. Six million people lost power in a Canadian March, and it took about nine hours to restore.
The cause was a geomagnetic storm driven by a coronal mass ejection from the sun: currents induced in the
long transmission lines destabilised the system faster than its protection could respond.
NOAA's own account is that the Hydro-Québec utility *"went from full operating capacity to"* blackout —
and the agency's G-scale puts numbers on how often this class of storm arrives. **G5, the top of the
scale (Kp=9), is described as: "widespread voltage control problems and protective system problems can
occur, some grid systems may experience complete collapse or blackouts. Transformers may experience
damage."** NOAA's stated average frequency for G5 conditions is **about four storm days per eleven-year
solar cycle.** This is not a once-a-century hazard. It is a several-times-a-decade hazard that has
mostly been lucky about where it landed.
«SRC: NOAA Space Weather Prediction Center, "Space Weather: Storms from the Sun" (booklet) — March
1989: "the Hydro-Quebec electrical utility went from full operating capacity to" blackout; NOAA G-scale
G5 (Extreme, Kp=9): "widespread voltage control problems and protective system problems can occur, some
grid systems may experience complete collapse or blackouts. Transformers may experience damage" — about
4 such storm days per 11-year cycle. |
https://www.swpc.noaa.gov/sites/default/files/images/u33/swx_booklet.pdf | retrieved 2026-07-29»

The reference event for the worst case is older. **The 1859 Carrington event is the largest geomagnetic
storm in recorded history.** NOAA's account of it: the aurora was bright enough that *people in the
northeastern United States could read a newspaper by it at night*, it was seen as far south as **Hawaii
and Central America**, and it *"crippled a large portion of the telegraph system"* — with operators
reporting **fires started by sparking equipment.** In 1859 the telegraph was essentially the only
long-conductor network that existed.

**The reason that matters now is scale, not novelty.** A comparable storm today would find a grid whose
total length of transmission line above 100 kilovolts has grown roughly **twenty-five-fold in the past
eighty-five years** — and geomagnetically induced current increases with line length. The National
Academies' estimate for a Carrington-level storm today, as NOAA reports it, is a cost approaching **$2
trillion**, with **20 to 40 million Americans at risk of an extended outage** lasting anywhere from
**sixteen days to one or two years.**

That last range is the honest shape of this hazard: nobody who studies it will give you a single number,
and the spread between sixteen days and two years is the difference between an inconvenience and a
different life. This book plans for the low end and tells you the high end exists.
«SRC: NOAA NESDIS, "What Was the Carrington Event?" and "When Solar Storms Attack: Space Weather and our
Infrastructure" — the 1859 Carrington event was the largest geomagnetic storm in recorded history; aurora
bright enough to read a newspaper by in the northeastern US, seen as far south as Hawaii and Central
America; crippled a large portion of the telegraph system with operators reporting fires from sparking
equipment; per the National Academies of Sciences a storm of that magnitude today could cost nearly $2
trillion, with 20–40 million in the US at risk of an extended power outage lasting 16 days to 1–2 years. |
https://www.nesdis.noaa.gov/news/when-solar-storms-attack-space-weather-and-our-infrastructure | retrieved
2026-07-29»

**And on 23 July 2012 a comparable ejection tore through Earth's orbit, and Earth was not there.** It hit
the STEREO-A spacecraft instead — which is the only reason the event is so well characterised, because
STEREO-A is an instrument built to measure exactly that.

The lead author of the study of it, Daniel Baker, put the margin plainly: *"if the eruption had occurred
only one week earlier, Earth would have been in the line of fire."* Had it hit, the analysis puts the
geomagnetic disturbance at a **Dst of about −1200 nanotesla — comparable to the Carrington event and
roughly twice as severe as the March 1989 Quebec blackout.** For scale, an ordinary storm that produces
aurora near the Arctic Circle and harms nothing sits around −50.

One published estimate of the probability of a Carrington-class storm striking Earth in any given decade
is **about 12 per cent**, which the researcher who calculated it called *"a sobering figure."* This book
reports that number as one estimate rather than a settled fact, because it is a statistical extrapolation
from a very short record. What is not in dispute is the near miss: an event of that class crossed our orbit
within living memory, and the only thing that saved us was timing.
«SRC: NASA Science, "Near Miss: The Solar Superstorm of July 2012" (23 July 2014), reporting D.N. Baker
et al., "A major solar eruptive event in July 2012," *Space Weather*, December 2013 — a powerful CME tore
through Earth orbit on 23 July 2012 and struck the STEREO-A spacecraft; Baker: "if the eruption had
occurred only one week earlier, Earth would have been in the line of fire"; a strike would have registered
Dst ≈ −1200 nT, comparable to the Carrington event and twice as bad as the March 1989 Quebec blackout;
ordinary geomagnetic storms register Dst = −50 nT; P. Riley's estimate of a ~12% chance of a
Carrington-class storm in a decade. |
https://science.nasa.gov/science-research/planetary-science/23jul_superstorm/ | retrieved 2026-07-29»

This playbook has to do two things at once, and the second is more important than the first. It has to
explain a real hazard with a real historical record. And it has to keep that hazard in proportion, because
this is the topic where the preparedness industry sells the most fear and the least usefulness.

**So the honest framing, stated up front: what reaches your household from space weather is a power
outage.** Possibly a very large, very long one. It is not the melting of your phone, and no amount of foil
changes what happens to a transformer three states away.

---

## What actually kills, and what actually costs

**Space weather does not kill people directly.** There is no exposure risk at ground level for the general
population. Airline crews and passengers on high-latitude polar routes receive measurably higher radiation
doses during major events, and airlines reroute for exactly that reason, and astronauts are at genuine
risk. Nobody on the ground is.

**The harm is entirely infrastructural, and the mechanism is well established even where the scale is
not.** Geomagnetically induced current flows in long conductors — high-voltage transmission lines,
pipelines, railway signalling. In a transformer it arrives as what is effectively direct current, offsetting
the alternating current and driving the core into **half-cycle saturation**. A saturated transformer leaks
magnetic field outside its core, heats up, and generates harmonics. In the Government Accountability Office's
words, *"saturated transformers are the root causes of nearly all GIC-induced disturbances in transmission
systems."*

**Two consequences, and the first is the more likely one.** The harmonics can make protective relays
misoperate and disconnect parts of the grid — which is what actually happened in Quebec in 1989, where
relay misoperation was *"a primary contributor"* to the blackout. That is a blackout without any equipment
being destroyed. The second consequence is thermal damage to the transformer itself, which is the scenario
that produces the long recovery.

**And that is where the honest number lives.** Large power transformers are custom-built, and the federal
energy department's 2024 report to Congress records that lead times have become *"exceptionally long, with
36-month lead times being commonly quoted and maximum lead times reaching as much as 60 months."* Before
2020 you could order one in under a year. Three to five years is the current reality — which is why the
sixteen-days-to-two-years range earlier in this chapter is not hysteria.

**But this book will not tell you the grid is certain to fall over.** The same federal assessment is blunt
that *"key studies lack consensus about the scale and likelihood of potential consequences,"* and notes
that **since 1932, only four geomagnetic disturbances have led to large-scale power outage or transformer
damage.** Utilities now operate under a mandatory reliability standard for geomagnetic disturbance, newer
transformer designs resist the thermal effects by roughly a factor of six, and forecasters can issue
warnings up to about **forty minutes** before a disturbance reaches Earth. The mechanism is real, the
recovery would be slow, and the probability is genuinely unknown. Prepare for the outage, not for the
apocalypse.
«SRC: US Government Accountability Office, *Technology Assessment: Protecting the Electric Grid from
Geomagnetic Disturbances*, GAO-19-98 (2019) — GIC adds a direct-current offset that drives transformers
into half-cycle saturation; "saturated transformers are the root causes of nearly all GIC-induced
disturbances in transmission systems"; misoperation of electro-mechanical protective relays was a primary
contributor to the 1989 Hydro-Québec blackout; total transmission above 100 kV in the United States has
increased 25-fold over the past 85 years and GIC increases with line length; newer design practices offer
about a factor of six improvement in resistance to GIC-induced thermal effects; forecasts and warnings up
to about 40 minutes in advance; since 1932 only four GMDs have led to large-scale outage or transformer
damage; key studies lack consensus about the scale and likelihood of consequences. |
https://www.gao.gov/assets/gao-19-98.pdf | retrieved 2026-07-29»
«SRC: US Department of Energy, *Large Power Transformer Resilience Report to Congress* (July 2024) —
LPTs are highly customised devices with long lead times for manufacture, testing, delivery and
installation; lead times "have become exceptionally long, with 36-month lead times being commonly quoted
and maximum lead times reaching as much as 60 months"; before the COVID-19 pandemic a large transformer
could be ordered with a lead time of less than a year. |
https://www.energy.gov/sites/default/files/2024-10/EXEC-2022-001242%20-%20Large%20Power%20Transformer%20Resilience%20Report%20signed%20by%20Secretary%20Granholm%20on%207-10-24.pdf | retrieved 2026-07-29»

**The other operational effects** are less dramatic and more likely: degradation or loss of GPS accuracy,
which matters more than people realise because timing signals from GPS synchronise financial systems and
parts of the grid itself; high-frequency radio blackouts; satellite anomalies and increased satellite drag;
and disruption to precision agriculture and survey work.

**Costs:** for a household, the cost is an outage of unknown length, and the correct response is exactly
the outage stack in Playbook 17 — held for longer.

**On EMP specifically**, which belongs here because it shares one mechanism and almost nothing else. A
high-altitude nuclear detonation produces a pulse that the federal strategy documents describe in **three
components**, and knowing the three is what lets you read anything else written about it:

**E1** is the fast one — a rise time measured in nanoseconds, a duration of hundreds of nanoseconds, and
field strengths *"on the order of tens of thousands of volts per meter."* It couples into short conductors,
which is why it is the component people mean when they talk about damage to electronics rather than to the
grid. **E2** is an intermediate pulse, longer and much weaker, whose main effect is to enhance currents
already induced on long lines. **E3** is the slow one, and it is *"comparable, but not equivalent"* to a
geomagnetic disturbance — the official comparison is that a geomagnetic storm delivers multiple peaks over
hours or days, while E3 is a single pulse *"more intense and prolonged than any one of these peaks."*

**So E3 is the geomagnetic-storm-like component, and it is the one that threatens the grid. E1 is the
component that has no natural analogue.** That distinction is the whole reason the effect on your own
devices is uncertain: the historical record contains severe geomagnetic storms and therefore tells us a
great deal about E3, and it contains no E1 at all.

It is an act of war rather than a natural hazard, its effects on small unconnected consumer electronics are
genuinely disputed among the people who study it, and the sensible household posture is a cheap hedge
rather than a project.
«SRC: US Department of Homeland Security, *Strategy for Protecting and Preparing the Homeland against
Threats of Electromagnetic Pulse and Geomagnetic Disturbance* (October 2018) — E1 is a fast (nanosecond
rise time, hundreds of nanoseconds duration) broad-band pulse that disrupts long-line electrical systems,
computers, sensors and electronic control systems, generating field strengths on the order of tens of
thousands of volts per metre; E2 is longer and much lower in amplitude, enhancing EMP currents on long
lines in the microsecond to millisecond regime; E3 effects are "comparable, but not equivalent" to those
from geomagnetic disturbances, a GMD featuring multiple peaks over hours or days while E3 is a singular
pulse more intense and prolonged than any one of those peaks. |
https://www.dhs.gov/sites/default/files/publications/18_1009_EMP_GMD_Strategy-Non-Embargoed.pdf | retrieved
2026-07-29»

---

## Before

The protections here are almost entirely the outage protections, which is the point.

- **1, 13 — water and no-cook food**, held at the two-week end of the range rather than the three-day end,
  because a severe grid event is the scenario where restoration is slow and regional.
- **37–46 — the whole power section**: the priority list, battery capacity, generator and transfer switch,
  fuel, medical device power, lighting, the car as a source, refuel cadence, and surge protection.
- **46 — whole-home surge protection**, which is the one piece of hardware in this playbook that addresses
  the mechanism directly, and which pays for itself against ordinary lightning and utility surges long
  before any space weather event.
- **120 — unplug on warning**, and here the warning is a real, published, freely available product: NOAA's
  Space Weather Prediction Center issues watches and warnings on a five-level geomagnetic storm scale, with
  a day or more of notice for a large ejection. A G4 or G5 watch is a genuine cue to unplug what you can
  spare and charge everything.
- **94 — space weather alerts**, subscribed to, so the cue actually reaches you.
- **119 — a battery radio**, because broadcast survives what the internet does not.
- **118 — offline maps and documents**, plus paper copies, because a GPS degradation event and an internet
  outage both make a phone much less useful.
- **98 — cash in small bills**, which is the most underrated protection in this playbook. In an extended
  regional grid event, card networks and ATMs do not work. Cash is the only functioning payment mechanism,
  and this is the scenario the owner of this book was right to call "cash is king."
- **42, 60, 61 — the medical dependencies**, which are what turn a long outage into a life-safety event.
- **122 — the shielded box**, done proportionately: a lined metal container with a spare cheap phone, a
  spare battery pack, a spare radio, a drive with the document vault and a torch. An hour and possibly no
  money at all.

**And the sequencing rule that governs this whole playbook:** if you have not done Protections 1, 13 and
37 to 46, do not build the box. The box protects a spare radio. The outage stack protects your household.
People do this backwards because the box is more interesting.

---

## During

**On a G4 or G5 geomagnetic storm watch — one to three days of notice.**

Charge everything: phones, battery packs, power stations, tool batteries, the laptop. Fill water containers.
Get cash out while ATMs work. Fuel the vehicles. Fill any prescriptions due. Unplug the expensive things you
do not need for the next day.

That is genuinely the whole list, and if nothing happens you have lost nothing — every item on it is
useful anyway.

**If the aurora is visible from an unusually low latitude, go and look at it.** This is the one hazard in
this book with a spectacular and harmless visible signature, and telling a household to enjoy it is
honest.

**If the grid does fail**, you are in Playbook 17 and the posture is the same, with three differences worth
noting:

**Assume it will be long.** Not because the lights are off, but because the failure mode in a severe event
involves equipment with long replacement times, and because the affected area may be very large, which
means mutual aid between utilities — the mechanism that normally restores power quickly — is
constrained.

**Assume payment systems are down**, not just the shops' terminals. Cash, and small bills.

**Assume communications are degraded and information is scarce.** The battery radio is your source. Do not
build your understanding of what is happening from social media in an information vacuum, because that
vacuum is where the wildest claims circulate, and a household making decisions on rumour is a household
making bad ones.

**What not to do:** do not attempt anything with your home's electrical system beyond the breaker panel,
do not touch anything utility-side, and do not backfeed a generator into a socket. That last rule kills
linemen and it is why Protection 39 specifies a transfer switch.

---

## After

**Restoration is when electronics die**, from the surge and the repeated cycling as sections come back.
Leave sensitive equipment unplugged for several minutes after power returns, then bring things back on in
stages rather than all at once.

**Check what died**, including things that appear to work: HVAC control boards, the well pump controller,
the router, the septic controller, the garage opener. Surge damage frequently manifests days later. Replace
any point-of-use surge protector that took a hit.

**Then the food and water**, per Protections 15 and 8: the freezer decision is made with a thermometer, not
by appearance, and any boil notice is followed until it is lifted.

**Then re-stock**, immediately rather than eventually, because the second event in a sequence is common —
solar activity comes in clusters, and a productive active region rotates back into view about
twenty-seven days later.

**And the honest post-event note**, which is this playbook's real contribution: the thing that hurt you was
the outage. Not the pulse, not the box, not the foil. Whatever failed during those days — the medication
that needed refrigeration, the phone that died on day two, the fact that nobody had cash, the neighbour on
oxygen — is what to fix on the annual review sheet. That is true whether the cause is the sun, a hurricane,
an ice storm or a squirrel in a substation, which is why the outage protections are the highest-value
pages in this book.

---

## The one-page version

| | |
|---|---|
| **What reaches you** | **A power outage.** Possibly very large and very long. Nothing else |
| **The record** | Québec 1989: 6 million people, 9 hours · Carrington 1859 · a near miss in July 2012 |
| **No ground risk** | No radiation exposure risk to people at ground level. Aurora is safe to watch |
| **The warning** | NOAA space weather watches, days ahead, free. Subscribe (Protection 94) |
| **On a G4/G5 watch** | Charge everything · fill water · **get cash** · fuel up · unplug what you can spare |
| **In the outage** | Assume long · assume cards dead · assume information scarce. Radio, not rumour |
| **On EMP** | An act of war, disputed effects on small electronics. A cheap lined metal box, an hour, no more |
| **The order** | Water, food, power, medical **first**. Build the box only after those are done |
| **Protections** | 1, 13, 37–46, 42, 60, 61, 94, 98, 118, 119, 120, 122 |
