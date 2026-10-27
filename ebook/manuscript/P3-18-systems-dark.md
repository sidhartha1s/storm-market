# Part Three, Playbook 18 — Systems Dark: Cash, Comms, Payment and Paper

Target: 8 pages · draft 1, 2026-07-29

---

## The event

**On 7 May 2021 the Colonial Pipeline Company proactively shut down its pipeline system in response to a
ransomware attack.** It announced the restart of the entire system on **13 May** — six days. The pipeline
itself was never damaged. The fuel existed. What was attacked was the company's business network, and the
shutdown was a precaution taken by the operator, not a physical failure.

Six days of one pipeline was enough to require federal emergency intervention across most of the eastern
seaboard: fuel waivers, emergency hours-of-service relief for tanker drivers, and a rolling list of states
added to the regional emergency declaration. The Energy Department stood up its emergency response
organization.

**And the shortages at the pump were mostly not a shortage.** They were the result of everybody who heard
there might be one going to fill up in the same forty-eight hours — including, memorably, people filling
plastic bags. This book does not print a peak percentage of stations dry, because the credible figures are
commercial estimates rather than a government count, and the number is not the lesson. The lesson is that
**a six-day interruption to one link produced a self-inflicted regional fuel emergency**, and that the
household protection against it is having bought fuel *before* the news, not faster than the neighbors
after it.
«SRC: US Department of Energy, Office of Cybersecurity, Energy Security, and Emergency Response,
"Colonial Pipeline Cyber Incident" — Colonial proactively shut down its pipeline system on 7 May 2021 in
response to a ransomware attack and announced the restart of the entire system on 13 May 2021; DOE Energy
Response Organization activated; DOT/FMCSA emergency hours-of-service measures and successive state
additions to the regional emergency declaration. | https://www.energy.gov/ceser/colonial-pipeline-cyber-incident | retrieved 2026-07-29»

That is this playbook. **The infrastructure a modern household depends on most is not physical. It is the
set of systems that let you pay, prove who you are, be contacted, and buy things** — and those systems fail
independently of the weather, fail regionally, and fail in ways that make a household with money in the bank
functionally broke.

The failures worth planning for are not exotic:

A **cellular or internet outage**, whether from a storm, a fiber cut or a carrier's own software fault, which
has taken major networks down nationally for a day at a time.

A **payment network outage**, which has repeatedly taken card processing down across whole countries for
hours.

A **cyber incident** at a utility, a hospital, a fuel distributor, a food distributor or a local
government — increasingly common, and frequently taking weeks to resolve.

And **a regional power failure**, which takes all of the above with it.

**One of these has been investigated in enough detail to be worth reading as a warning.** Just before
midnight on **9 April 2014**, a 911 call-routing facility in Englewood, Colorado stopped directing
emergency calls to **81 call centers across seven states** — California, Florida, Minnesota, North
Carolina, Pennsylvania, South Carolina and Washington. The cause was **a software coding error**: a counter
hit its threshold and the system could send no more calls. The federal communications regulator's finding:
a loss of 911 service for **more than 11 million people** — about three and a half per cent of the
population of the United States — *"for up to six hours,"* during which **over 6,600 calls to 911 never
reached a call center.** In Washington state, every single call center was affected to some degree.

**The detail that should stay with you is why it lasted six hours.** The monitoring system *"did not issue
any major or critical alarm for this outage. Instead, it issued several thousand minor alarms for calls not
completing, but these did not attract the attention"* of staff. Switching traffic to the backup hub in
Miami restored service *"almost immediately"* — once someone worked out what was wrong. Nobody is known to
have died. The regulator's own verdict on the whole thing was that *"it could have been prevented. But it
was not."*

This is what a systems failure looks like from the inside: not a dramatic collapse, but a wrong number in
software, thousands of ignored warnings, and six hours in which dialing the emergency number did nothing.
«SRC: Federal Communications Commission, Public Safety and Homeland Security Bureau, *April 2014
Multistate 911 Outage: Cause and Impact Report and Recommendations* (October 2014) — 9 April 2014, 11:54
p.m. PDT, Intrado's Englewood, Colorado ECMC; software coding error; 81 PSAPs in seven states (California,
Florida, Minnesota, North Carolina, Pennsylvania, South Carolina, Washington); loss of 911 service for more
than 11 million people (11,313,787, about 3.5% of the US population) for up to six hours; over 6,600 calls
to 911 never reached a PSAP; all of Washington's PSAPs affected; the monitoring system issued no major or
critical alarm but several thousand minor alarms that did not attract staff attention; switchover to the
Miami hub almost immediately restored service; "it could have been prevented. But it was not." |
https://docs.fcc.gov/public/attachments/DOC-330012A1.pdf | retrieved 2026-07-29»

The household consequence is identical in every case: **your money is inaccessible, your identity is
unverifiable, and nobody can reach you.**

---

## What actually kills, and what actually costs

**This hazard rarely kills directly**, and the book should say so plainly rather than inflating it. Its harm
is a cascade:

You cannot buy fuel, so you cannot evacuate. You cannot buy food or water, so the pantry has to be real.
You cannot fill a prescription because the pharmacy's system is down or cannot verify your insurance. You
cannot reach the person you need to reach, and nobody can reach you. You cannot prove who you are to a
shelter, an aid program, a bank or an employer.

The deaths, where they occur, are downstream: a delayed evacuation, a missed medication, an emergency call
that did not connect. **And the large 911 outages on record were caused by network and software failures
rather than by storms** — the April 2014 event at the top of this playbook took 911 away from eleven
million people across seven states, on a clear night, because of a counter in a piece of software.

**Costs:** modest in dollars and severe in disruption. The specific expensive failures are fuel bought at a
premium in a panic, a missed insurance deadline because you could not access documents, and identity fraud
in the aftermath of a records breach at an organization holding your data.

---

## Before

Every protection in this playbook is cheap. Several are free. This is the section of the book with the best
ratio of benefit to spend, and the one readers are most likely to skip because it is boring.

- **98 — cash, in small bills.** The single protection this playbook exists to insist on. Enough to cover
  fuel, food, and a few nights of lodging for your household. Small denominations, because a shop running on
  a cash box cannot change large notes. Kept somewhere fire-resistant, rotated so it does not get spent.
- **99 — payment redundancy.** More than one card, from more than one issuer, not stored together. One
  account number and one customer service number written on paper. Know your withdrawal limits. Tell the bank
  if you evacuate, so fraud systems do not freeze the card you are relying on.
- **96, 97 — the document vault and the grab-and-go envelope.** Digital copies in three places, and a
  physical envelope with identification, the insurance declarations page, the medication list, the contact
  sheet and cash. The envelope is the answer to "prove who you are" when your phone is dead.
- **112 — the out-of-area contact**, and the rule that **texts get through when calls do not**, because
  messages queue and retry while voice needs a circuit.
- **119 — a radio that is not a phone**, which is the only information source that works when both the
  cellular network and the internet are down.
- **121 — short-range radios**, for coordinating within a couple of miles when the network is gone.
- **118 — offline maps and documents on the phone**, plus the paper versions, because a navigation app
  without data is a blank screen.
- **123 — the off-site backup**, tested by restoring one file.
- **110 — fuel discipline.** Half a tank in season. The Colonial Pipeline event was survivable for anyone who
  simply kept the tank above half and did not need to wait in line.
- **13, 1 — pantry and water**, which are also the answer to a food distributor's systems being down.
- **59 — the prescription buffer**, which is the answer to a pharmacy that cannot process.

**Two habits, both free.** Know at least one important phone number from memory. And keep a paper copy of
the household's essential information — contacts, accounts, policy numbers, medications — updated once a
year, because the single point of failure in a modern household is one phone.

**And the password problem, honestly.** A password manager is the right answer for security and it is a
single point of failure in an outage. The resolution is to know the master password from memory, keep an
export or an offline copy in the document vault, and have a paper record of the few accounts that matter
most — bank, insurer, email — including the recovery method, because account recovery frequently requires a
phone number or a device you may no longer have.

---

## During

**Establish what is actually down**, because the response differs. No power? No cellular? No internet but
cellular works? Cards not processing but everything else fine? A battery radio and a neighbor answer this
faster than repeatedly reloading a page.

**Assume it will last longer than announced**, and act early rather than late. The distinguishing feature of
this hazard is that the line forms fast: the fuel, the cash, the bottled water and the batteries all go in
the first hours, and the households that do well are the ones who did not need to join the line at all.

**Then the sequence.**

**Cash first.** If ATMs are working and the outage is spreading, get cash while you can. If they are not,
you are on what you have — which is why Protection 98 exists.

**Then fuel**, if you need it and stations are working. Do not top up in a panic line for the sake of it if
your tank is already above half; that behavior is what creates the shortage.

**Then communications.** Text rather than call. Use the out-of-area contact as a hub so nobody is trying to
reach anybody specific. If data is intermittent, send short messages and let them queue. Conserve battery
aggressively: brightness down, background activity off, aeroplane mode when there is no signal — because a
phone hunting for a network it cannot find flattens itself in hours.

**And know how to call for help without a network.** In most cases a cell phone will place an emergency
call over **any** available carrier's network, not just yours, so a "no service" indicator does not
necessarily mean no emergency call. If 911 is down in your area, counties publish an alternative
ten-digit number — and it is worth writing that number on the household contact sheet now.

**If cards are not processing**, expect cash-only trading, expect some businesses to close entirely rather
than trade on paper, and expect prices to be inconsistent. Keep receipts, because errors in manual
transactions are common and reversals are your problem to prove.

**Do not do anything financially significant on a compromised or improvised system.** If a bank, a utility
or a retailer has had a cyber incident, the aftermath is the highest-risk period for fraud: unsolicited calls
claiming to be from the institution, urgent links, requests to "verify" details, and requests to move money
to a safe account. The rule is absolute — hang up and call the number on your card or your statement, never
a number or link you were given.

---

## After

**Reconcile everything.** Check statements against receipts for the whole period. Manual processing produces
duplicate charges, wrong amounts and delayed postings, and the window to dispute them is finite.

**Watch for the fraud that follows.** Disaster and outage aftermaths are when fraud spikes: fake charity
appeals, fake aid programs, fake utility calls demanding payment to restore service, fake insurance
adjusters, and identity theft using data that was exposed. Utilities do not phone demanding immediate
payment; that call is a scam every time.

**If any organization holding your data was breached**, take the credit freeze seriously — it is free, it is
reversible, and it is the single most effective protection against new-account identity fraud. Do it for
every adult in the household.

**Restore the redundancies you used.** Put the cash back. Recharge the packs. Refill the fuel. Update the
paper sheet with anything that changed.

**Then note what actually broke**, because this hazard exposes very specific single points of failure and
they are always cheap to fix: the number nobody knew, the document only in the cloud, the account with no
recovery method, the phone that was the only phone, the neighbor who could not be reached. Every one of
those is a five-minute fix in normal conditions and a serious problem in a dark week.

**And keep the honest perspective.** This playbook's protections are the least dramatic in the book. They are
also the ones most likely to be used, because payment and network outages happen far more often than
tornadoes.

---

## The one-page version

| | |
|---|---|
| **The failure** | Not physical. Your ability to **pay, prove who you are, and be reached** |
| **How it looks** | Cards dead · ATMs dry · no signal · pharmacy cannot process · fuel queues |
| **The protection** | **Cash in small bills**, and a paper copy of what matters. Both nearly free |
| **Comms rule** | **Text, don't call.** Messages queue; voice needs a circuit that isn't there |
| **Emergency calls** | Usually route over any carrier. Also write your county's 10-digit backup number down |
| **Fuel** | Half a tank in season means never needing the line |
| **During** | Establish what's down · act early · conserve phone battery hard · nothing financial on a shaky system |
| **The scam rule** | Hang up and call the number on your card. Never the number you were given |
| **After** | Reconcile every statement · freeze credit if data was exposed · put the cash back |
| **Protections** | 1, 13, 59, 96, 97, 98, 99, 110, 112, 118, 119, 121, 123 |
