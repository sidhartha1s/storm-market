#!/usr/bin/env python3
"""Builds landing/index.html (the home page) in the approved Binder design.

Deterministic, no deps. Content sources:
  - landing/index.html (live page, pre-redesign) -- copy of record, ported verbatim
    except em dashes (rewritten to commas/colons/periods per owner style rule).
  - landing/tools/binder-concept.html (approved concept) -- section structure,
    CSS classes, and the 4 "recent" testimonials (concept-original, not on live).
  - landing/tools/chrome.py -- shared chrome (band/brand/tabs/dock/toast/footer/CSS/JS).

Run: python3 landing/tools/build_home.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import chrome  # noqa: E402

OUT = pathlib.Path(__file__).parent.parent / "index.html"

TITLE = "The Storm-Ready Home · What the survivors did differently · Paul Raymond"
DESCRIPTION = (
    "How to prepare your home before the next storm, a 486-page manual: 130 numbered "
    "protections, 23 hazard playbooks, a 60-day sequence, printable binder. $14.99."
)
CANONICAL = "https://paulraymond.online/"

TABS = [
    ("sheet-start", "Start here"),
    ("sheet-why", "Why this book"),
    ("sheet-inside", "Inside"),
    ("sheet-saves", "What it saves"),
    ("sheet-readers", "Testimonials"),
    ("sheet-paul", "About the author"),
    ("sheet-questions", "FAQs"),
    ("sheet-get", "Get my copy"),
]

# ---------------------------------------------------------------------------
# head_extra: OG/Twitter meta, both JSON-LD graphs (byte-identical to live
# except em dashes fixed to match the visible-copy rewrite), a hero-image
# preload, and a small supplemental stylesheet for content shapes the
# approved concept never needed (stat rows, chips, gap cards, region rows).
# chrome.py's own CSS is untouched; nothing here duplicates a class it defines.
# ---------------------------------------------------------------------------
HEAD_EXTRA = """
<link rel="preload" as="image" href="assets/cover-hero.webp">
<meta property="og:title" content="The Storm-Ready Home">
<meta property="og:description" content="What the survivors did differently: the 130 things you can do before the next one.">
<meta property="og:image" content="https://paulraymond.online/assets/og.png">
<meta property="og:type" content="website">
<meta property="og:url" content="https://paulraymond.online/">
<meta name="twitter:card" content="summary_large_image">
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Book",
      "name": "The Storm-Ready Home",
      "author": {
        "@type": "Person",
        "name": "Paul Raymond"
      },
      "numberOfPages": 486,
      "bookFormat": "https://schema.org/EBook",
      "inLanguage": "en",
      "url": "https://paulraymond.online/",
      "offers": {
        "@type": "Offer",
        "price": "14.99",
        "priceCurrency": "USD",
        "availability": "https://schema.org/InStock",
        "url": "https://paulraymond.gumroad.com/l/ebook",
        "hasMerchantReturnPolicy": {
          "@type": "MerchantReturnPolicy",
          "applicableCountry": "US",
          "returnPolicyCategory": "https://schema.org/MerchantReturnFiniteReturnWindow",
          "merchantReturnDays": 7,
          "returnMethod": "https://schema.org/ReturnByMail",
          "returnFees": "https://schema.org/FreeReturn"
        }
      }
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What exactly do I get, and in what format?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A single PDF of 486 pages, delivered to your inbox immediately after payment, plus the printable binder pages and your state packets. Readable on a phone, tablet or computer, and printable at a kitchen table. No app, no DRM, no subscription."
          }
        },
        {
          "@type": "Question",
          "name": "Isn't this information free from FEMA?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Some of it is, and the book cites those documents rather than hiding them. What the federal guides give you is pamphlet prose: no prices, no build steps, no fillable forms, no regional ordering and no state directory. This book was written because reading the source documents and turning them into a Saturday's work is the part nobody does."
          }
        },
        {
          "@type": "Question",
          "name": "I rent. Is this useful to me?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes, and the book flags it protection by protection. Most of the highest-value items need no permission at all: the room selection, the water store, the document vault, the alert enrollment, the prescription buffer, the trigger plan, the binder. The structural hardening chapters are marked so you can skip what you can't do."
          }
        },
        {
          "@type": "Question",
          "name": "Which region is mine?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The front matter walks you through it in about five minutes, and most readers are in two regions rather than one, which is fine, because regions only change the order you work in, not what you read. Every chapter is in every copy."
          }
        },
        {
          "@type": "Question",
          "name": "Is this a prepper book?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "No. There is no bunker content, no firearms, no grid-down-forever scenario and no politics. It is a family safety manual about weather and natural disasters, and every instruction is traceable to a citable authority."
          }
        },
        {
          "@type": "Question",
          "name": "I'm not good with technology. Will I manage?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "If you can open an email, you can use this book. It arrives as one ordinary PDF: no app to install, no account to create, no login to remember. Print any page at home or at a copy shop, and the binder is designed to be filled in with a pen."
          }
        },
        {
          "@type": "Question",
          "name": "What's your refund policy?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Seven days, no questions asked. Reply to the delivery email and the $14.99 comes back. You keep the files."
          }
        }
      ]
    }
  ]
}
</script>
<style>
.trustline{font-size:16px;color:var(--soft);margin:14px 0 0}
.trustline .stars{color:var(--tab5);letter-spacing:.15em;margin-right:8px}
.counts{display:flex;flex-wrap:wrap;gap:26px;margin:22px 0}
.counts div{text-align:center;min-width:84px}
.counts b{display:block;font-family:var(--display);font-weight:900;font-size:32px;color:var(--tab3);letter-spacing:-.01em}
.counts span{display:block;font-family:var(--mono);font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--faded);margin-top:4px}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin:20px 0}
.chip{font-family:var(--mono);font-size:13px;background:var(--paper2);border:1px solid var(--rule);padding:6px 13px;border-radius:999px;color:var(--soft)}
.gap2{display:grid;grid-template-columns:1fr 1fr;gap:22px;margin:30px 0}
.gapcard{border:2px solid var(--rule);border-radius:10px;padding:22px 24px;background:var(--paper2)}
.gapcard b{display:block;font-family:var(--display);font-weight:900;font-size:44px;letter-spacing:-.02em}
.gapcard.alert b{color:var(--bad)}
.gapcard.gain b{color:var(--good)}
.gapcard p{margin:10px 0 0;color:var(--soft);font-size:15px}
.ruled .rst{grid-column:2;display:block;font-family:var(--mono);font-size:12px;color:var(--faded);margin:2px 0 4px}
.gallery.g3{grid-template-columns:repeat(3,1fr)}
@media (max-width:900px){.gap2{grid-template-columns:1fr}.gallery.g3{grid-template-columns:1fr}}
</style>
"""

STATE_OPTIONS = (
    '<option value="">Choose your state…</option>'
    '<option value="Alabama">Alabama</option><option value="Alaska">Alaska</option>'
    '<option value="Arizona">Arizona</option><option value="Arkansas">Arkansas</option>'
    '<option value="California">California</option><option value="Colorado">Colorado</option>'
    '<option value="Connecticut">Connecticut</option><option value="Delaware">Delaware</option>'
    '<option value="District of Columbia">District of Columbia</option>'
    '<option value="Florida">Florida</option><option value="Georgia">Georgia</option>'
    '<option value="Hawaii">Hawaii</option><option value="Idaho">Idaho</option>'
    '<option value="Illinois">Illinois</option><option value="Indiana">Indiana</option>'
    '<option value="Iowa">Iowa</option><option value="Kansas">Kansas</option>'
    '<option value="Kentucky">Kentucky</option><option value="Louisiana">Louisiana</option>'
    '<option value="Maine">Maine</option><option value="Maryland">Maryland</option>'
    '<option value="Massachusetts">Massachusetts</option><option value="Michigan">Michigan</option>'
    '<option value="Minnesota">Minnesota</option><option value="Mississippi">Mississippi</option>'
    '<option value="Missouri">Missouri</option><option value="Montana">Montana</option>'
    '<option value="Nebraska">Nebraska</option><option value="Nevada">Nevada</option>'
    '<option value="New Hampshire">New Hampshire</option><option value="New Jersey">New Jersey</option>'
    '<option value="New Mexico">New Mexico</option><option value="New York">New York</option>'
    '<option value="North Carolina">North Carolina</option><option value="North Dakota">North Dakota</option>'
    '<option value="Ohio">Ohio</option><option value="Oklahoma">Oklahoma</option>'
    '<option value="Oregon">Oregon</option><option value="Pennsylvania">Pennsylvania</option>'
    '<option value="Rhode Island">Rhode Island</option><option value="South Carolina">South Carolina</option>'
    '<option value="South Dakota">South Dakota</option><option value="Tennessee">Tennessee</option>'
    '<option value="Texas">Texas</option><option value="Utah">Utah</option>'
    '<option value="Vermont">Vermont</option><option value="Virginia">Virginia</option>'
    '<option value="Washington">Washington</option><option value="West Virginia">West Virginia</option>'
    '<option value="Wisconsin">Wisconsin</option><option value="Wyoming">Wyoming</option>'
)

# ---------------------------------------------------------------------------
# Sheet 1: Start here (hero)
# ---------------------------------------------------------------------------
SHEET_START = """
<section class="sheet" id="sheet-start">
  <div class="row">
    <div>
      <h1>The storm doesn't<br>warn twice.<br><em>The survivors knew that.</em></h1>
      <p class="lead">A 486-page American disaster manual, built from the reports written
        after real storms: 130 numbered protections, 23 hazard playbooks, a 60-day sequence,
        and a printable binder your family can actually fill in, this weekend.</p>
      <p><a class="btn" href="@@BUY@@">Get My Copy</a></p>
      <p style="font-family:var(--mono);font-size:13px;color:var(--faded);margin-top:14px">
        Instant PDF download &middot; Pay once, own it forever &middot; 7-day money-back guarantee</p>
      <p class="trustline"><span class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</span>Rated
        five stars by early readers. Built from National Weather Service &amp; FEMA post-storm
        reports.</p>
      <div class="counts">
        <div><b>486</b><span>Pages</span></div>
        <div><b>130</b><span>Protections</span></div>
        <div><b>23</b><span>Hazards</span></div>
        <div><b>60</b><span>Day sequence</span></div>
        <div><b>7-day</b><span>Refund, no questions</span></div>
      </div>
    </div>
    <figure style="margin:0">
      <img class="cover" src="assets/cover-hero.webp" width="860" height="1290"
        alt="The Storm-Ready Home by Paul Raymond, book cover" fetchpriority="high">
    </figure>
  </div>
</section>
"""

# ---------------------------------------------------------------------------
# Sheet 2: Why this book -- Joplin story (opener) + the concept's 5 reasons
# ---------------------------------------------------------------------------
SHEET_WHY = """
<section class="sheet" id="sheet-why">
  <p class="kick">The story &middot; Joplin, Missouri &middot; May 22, 2011 &middot; 5:11 p.m.</p>
  <p>It was a Sunday evening. Graduation day. Families were driving home from the high-school
    ceremony with the windows down when the sirens started, and most people did what most
    people always do. They waited. They looked at the sky. They turned on the TV to see if it
    was serious this time.</p>
  <p>The sirens sounded at 5:11. The tornado touched down at 5:34. <strong>In those
    twenty-three minutes almost nobody moved.</strong> One hundred and fifty-eight people were
    killed directly that evening, and four more in the days that followed. The National Weather
    Service assessment written afterwards is blunt about why: <strong>most residents did not
    take protective action until they had gone and found confirmation</strong>: seeing it
    themselves, hearing it said on air, or waiting for the second siren. <strong>The families
    who moved at 5:11 had decided what 5:11 meant long before it happened.</strong></p>
  <div class="row" style="margin:34px 0 10px">
    <p class="lead" style="margin:0">Every disaster report says the same quiet thing: the
      survivors decided before the storm did. This book is that decision, written down.</p>
    <figure style="margin:0">
      <img class="photo" src="assets/paul-tornado-selfie.webp" width="880" height="880"
        alt="Paul Raymond in the field, a tornado on the ground behind him" loading="lazy">
      <figcaption>Yes, that's me, closer than anyone needs to be. The book exists so you
        never are. Paul.</figcaption>
    </figure>
  </div>

  <h2 style="margin-top:54px">Five reasons it earns the shelf space.</h2>
  <ol class="ruled">
    <li><b>It is built from the after-action reports.</b><p>National Weather Service service
      assessments, NIST investigations, day-after archives: the documents written after each
      storm, turned into numbered actions with real prices next to them.</p></li>
    <li><b>The first week costs nothing.</b><p>Room selection, alert paths, the trigger plan.
      Free protections first, hardware later.</p></li>
    <li><b>It tells you the limits of its own advice.</b><p>Every protection has a "what this
      does not do" box. No miracle claims.</p></li>
    <li><b>It works for renters and 68-year-olds.</b><p>Marked protection by protection. No
      app, no login, print any page.</p></li>
    <li><b>Your state is already in it.</b><p>All 51 state packets: forecast office,
      emergency management, insurance department, mitigation credits.</p></li>
  </ol>
</section>
"""

# ---------------------------------------------------------------------------
# Sheet 3: Inside -- hazard coverage (stats + chips) + five regions + gallery
# ---------------------------------------------------------------------------
SHEET_INSIDE = """
<section class="sheet" id="sheet-inside">
  <p class="kick">The manual</p>
  <h2>Every hazard America actually gets. One book.</h2>
  <p class="lead">Not a survival fantasy and not a rewrite of a government pamphlet. A
    reference manual organised the way disasters actually work: six ways they kill you, six
    things every household needs, then twenty-three playbooks for the specific events that
    reach your door.</p>
  <div class="counts">
    <div><b>130</b><span>Protections</span></div>
    <div><b>23</b><span>Hazards</span></div>
    <div><b>60</b><span>Days</span></div>
    <div><b>5</b><span>Regions</span></div>
    <div><b>51</b><span>State packets</span></div>
  </div>
  <div class="chips">
    <span class="chip">Tornado</span><span class="chip">Hurricane &amp; storm surge</span>
    <span class="chip">Extreme rainfall &amp; flash flood</span><span class="chip">Riverine &amp; coastal flooding</span>
    <span class="chip">Wildfire</span><span class="chip">Wildfire smoke &amp; air quality</span>
    <span class="chip">Hail &amp; derecho</span><span class="chip">Lightning</span>
    <span class="chip">Blizzard &amp; ice storm</span><span class="chip">Extreme heat</span>
    <span class="chip">Extreme cold &amp; deep freeze</span><span class="chip">Drought &amp; dust</span>
    <span class="chip">Earthquake</span><span class="chip">Tsunami</span>
    <span class="chip">Space weather</span><span class="chip">Volcanic ashfall</span>
    <span class="chip">Grid failure</span><span class="chip">Systems dark</span>
    <span class="chip">Water &amp; sanitation failure</span><span class="chip">Hazmat</span>
    <span class="chip">Radiological proximity</span><span class="chip">When EMS can't reach you</span>
    <span class="chip">Electronics &amp; records</span>
  </div>

  <p class="kick" style="margin-top:54px">Find your region</p>
  <h2>Most families sit in two of these regions. The book orders
    the chapters for you.</h2>
  <p class="lead">Every chapter applies to every reader: hazards are not exclusive. What your
    region changes is the order. The front matter hands you your ordered first ten, and the
    60-day sequence takes the rest.</p>
  <ol class="ruled">
    <li><b>Tornado Alley</b><span class="rst">KS &middot; OK &middot; TX &middot; NE &middot; IA &middot; MO &middot; AR &middot; IL &middot; IN &middot; KY &middot; TN &middot; N. AL &middot; MS</span>
      <p>Safe room selection, the helmet rule, two alert paths, NOAA radio, SAME.</p></li>
    <li><b>Hurricane Coast</b><span class="rst">TX &middot; LA &middot; MS &middot; AL &middot; FL &middot; GA &middot; SC &middot; NC &middot; VA &middot; MD &middot; DE &middot; NJ &middot; NY &middot; New England</span>
      <p>Leave-early trigger, window protection, garage door bracing, sealed roof deck.</p></li>
    <li><b>Wildfire West</b><span class="rst">CA &middot; OR &middot; WA &middot; ID &middot; MT &middot; NV &middot; UT &middot; AZ &middot; NM &middot; CO &middot; WY</span>
      <p>Ember vents, Zone 0, defensible space, Red Flag &amp; evac zone, MERV-13 filtration.</p></li>
    <li><b>Ice &amp; Snow North</b><span class="rst">MN &middot; WI &middot; MI &middot; ND &middot; SD &middot; NY &middot; VT &middot; NH &middot; ME &middot; PA &middot; OH</span>
      <p>Pipe freeze prevention, shut-off literacy, warm-room consolidation, generator siting.</p></li>
    <li><b>Quake West</b><span class="rst">CA &middot; OR &middot; WA &middot; AK &middot; HI &middot; NV &middot; UT &middot; MO bootheel</span>
      <p>Anchoring &amp; strapping, gas shutoff literacy, water store, trauma kit.</p></li>
  </ol>

  <p class="kick" style="margin-top:54px">Look inside</p>
  <h2>Real pages, not a mockup.</h2>
  <p class="lead">Every protection carries the same seven fields: what it prevents, what it
    costs, how long it takes, what to buy, the steps, which regions rank it first, and the
    line most books leave out: what it does not do.</p>
  <div class="gallery">
    <figure><img src="assets/inside-protection.webp" width="576" height="864"
      alt="A protection page from the manual" loading="lazy">
      <figcaption>Protection 23: safe room selection, with the floor-plan diagram and the
        honesty box.</figcaption></figure>
    <figure><img src="assets/inside-money.webp" width="576" height="864"
      alt="The money chapter page" loading="lazy">
      <figcaption>The gap page. Every figure sourced to the issuing document.</figcaption></figure>
    <figure><img src="assets/inside-binder.webp" width="576" height="864"
      alt="A fillable binder form" loading="lazy">
      <figcaption>One of the printable binder forms, fill it in, put it in the
        go-bag.</figcaption></figure>
    <figure><img src="assets/inside-week.webp" width="576" height="864"
      alt="A week of the 60-day sequence" loading="lazy">
      <figcaption>Week four of eight, the paper week. The cheapest one, and the book puts it
        before every week that costs money.</figcaption></figure>
  </div>
</section>
"""

# ---------------------------------------------------------------------------
# Sheet 4: What it saves -- money chapter, then the vs cards (live worth rows)
# ---------------------------------------------------------------------------
SHEET_SAVES = """
<section class="sheet" id="sheet-saves">
  <p class="kick">The money chapter</p>
  <h2>What the average household gets, and what the program allows.</h2>
  <p class="lead">Federal disaster aid is not insurance and it is not compensation. It is a
    floor. How close you land to the ceiling is decided almost entirely by what you can
    prove, and most of that proof has to exist before the event.</p>

  <div class="gap2">
    <div class="gapcard alert"><b>$3,029</b><p><strong>Average FEMA Individuals and
      Households Program award.</strong> Congressional Research Service, average award
      following the Disaster Recovery Reform Act.</p></div>
    <div class="gapcard gain"><b>$43,600</b><p><strong>Statutory maximum</strong> for
      housing assistance, with a separate maximum of the same amount for other needs
      assistance. Federal Register notice, 24 October 2024.</p></div>
  </div>

  <table class="ledger">
    <tr class="total"><td>Also on the record</td><td>Figure</td></tr>
    <tr><td>Share of housing-assistance recipients who received the maximum</td><td>10.8%</td></tr>
    <tr><td>Share of all recipients earning $30,000 a year or less</td><td>53.6%</td></tr>
    <tr><td>Average award, homeowners, 2016&#8211;2018</td><td>~$4,200</td></tr>
    <tr><td>Average award, renters, 2016&#8211;2018</td><td>~$1,700</td></tr>
  </table>
  <p style="font-family:var(--mono);font-size:12px;color:var(--faded);margin-top:6px">Source:
    Congressional Research Service, <em>FEMA Individual Assistance Grants for Disaster
    Survivors</em> (R48310, IF13127); Federal Register notice of maximum IHP amounts, 24
    October 2024. Retrieved July 2026.</p>

  <p style="background:var(--paper2);border-left:4px solid var(--faded);padding:18px 22px;margin-top:22px">
    <strong style="display:block;font-family:var(--mono);font-size:12px;letter-spacing:.12em;text-transform:uppercase;margin-bottom:8px;color:var(--ink)">What this is not</strong>
    This is not a promise that documentation moves you from three thousand dollars to
    forty-three thousand. Awards are determined by verified loss, insurance status and
    eligibility, and most households will never approach the maximum. What documentation
    removes is the loss you cannot prove, which is the only part of the gap you control.</p>

  <p style="margin-top:26px"><strong>Three of the protections cost nothing at all.</strong>
    The twenty-minute video walkthrough of every room. The document vault. The insurance
    audit that makes you read the five numbers on your own policy. All three sit in week
    four of eight, the paper week, which the book places before every week that costs
    money.</p>

  <p class="kick" style="margin-top:54px">What $14.99 is</p>
  <h2>One bad afternoon, two ways it can go.</h2>
  <p class="lead">Nobody ever wished they'd spent it on one more tank of gas. Put the price
    next to what it's up against. This isn't just a book you read, it's the cheapest item on
    a list where everything else costs real money, and it tells you which of those things
    your house actually needs, in order.</p>
  <div class="vs">
    <div class="col bad">
      <div class="col-head"><span class="dot"></span>Without the book</div>
      <ul>
        <li><span>A single sheet of plywood, cut wrong, the day before landfall</span><b>~$70</b></li>
        <li><span>A typical homeowner's wind or hail deductible</span><b>$1,000&#8211;$2,500</b></li>
        <li><span>A portable generator bought in a panic, possibly the wrong size</span><b>$700&#8211;$1,200</b></li>
        <li><span>A week in a hotel after an evacuation, out of pocket</span><b>$900+</b></li>
        <li><span>The loss you can't prove because there are no photographs</span><b>Unrecoverable</b></li>
      </ul>
      <div class="col-total"><span>One afternoon</span><b>$2,670+</b></div>
    </div>
    <div class="col good">
      <div class="col-head"><span class="dot"></span>With the book</div>
      <ul>
        <li><span>The manual, 486 pages <em>($14.99)</em></span><b>included</b></li>
        <li><span>The binder, 61 fillable forms <em>($19)</em></span><b>included</b></li>
        <li><span>The 60-day sequence <em>($15)</em></span><b>included</b></li>
        <li><span>All 51 state packets <em>($19)</em></span><b>included</b></li>
        <li><span>Lifetime updates <em>($20)</em></span><b>included</b></li>
      </ul>
      <div class="col-total"><span>$87.99 of value, once</span><b>$14.99</b></div>
    </div>
  </div>
  <p class="vsnote" style="font-family:var(--mono);font-size:14px;color:var(--faded)">The
    manual that sequences all of it, starting with the free week: $14.99, once.</p>
  <p class="vsnote">And the protection the reports keep coming back to, the written trigger
    plan, Protection 95, costs nothing at all. If one page of this book changes one decision
    on one bad afternoon, the price stops being a number worth discussing.</p>
  <p class="vsnote"><a class="btn" href="@@BUY@@">Get My Copy, $14.99</a></p>
</section>
"""

# ---------------------------------------------------------------------------
# Sheet 5: Testimonials -- 4 concept "recent" quotes + all 12 live quotes
# ---------------------------------------------------------------------------
SHEET_READERS = """
<section class="sheet" id="sheet-readers">
  <p class="kick">From readers</p>
  <h2>The binder is on their refrigerators now.</h2>
  <div class="quotes">
    <blockquote class="quote recent"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><span class="tag">Tornado &middot; this spring</span><p>"When the sirens went off we already knew which room to go to. Grabbed the bag, grabbed the dog, done. We lost part of the roof. Nobody got hurt."</p><cite>Janet &middot; Kentucky</cite></blockquote>
    <blockquote class="quote recent"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><span class="tag">Hurricane &middot; last season</span><p>"I braced the garage door the weekend before the storm, sixty dollars at the hardware store. Ours held up. A couple on our street did not."</p><cite>Ray &middot; Florida</cite></blockquote>
    <blockquote class="quote recent"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><span class="tag">Wildfire &middot; last summer</span><p>"The evacuation order came while we were eating dinner. The binder was already in the car, so we just went. My wife said it was the calmest we have ever left the house."</p><cite>Carol &middot; Oregon</cite></blockquote>
    <blockquote class="quote recent"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><span class="tag">A note to Paul</span><p>"Thank you, Paul. I bought this for my mother after the ice storm and ended up doing every page myself. It is the first one of these books that talks to you like an adult."</p><cite>Susan &middot; Arkansas</cite></blockquote>
    <blockquote class="quote"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p>"We did the free week first, like the book says. My husband found out our 'safe spot' for eleven years was the wrong room. That alone was worth it."</p><cite>Linda &middot; Oklahoma</cite></blockquote>
    <blockquote class="quote"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p>"I'm 68 and not technical. Printed the binder at the library, filled it in with a pen over two evenings. My daughter has a copy of every page now."</p><cite>Margaret &middot; Florida</cite></blockquote>
    <blockquote class="quote"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p>"Retired firefighter. Most of these books are junk. This one cites the service assessments I used to read on shift. Bought copies for both my sons."</p><cite>Dale &middot; Missouri</cite></blockquote>
    <blockquote class="quote"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p>"The money chapter paid for the book before the first storm. We photographed the house in twenty minutes, exactly the way it says. Our agent was impressed."</p><cite>Carol &amp; Jim &middot; Texas</cite></blockquote>
    <blockquote class="quote"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p>"I rent, and I expected half the book not to apply. It's marked, protection by protection. Did nine of the first ten without asking my landlord anything."</p><cite>Diane &middot; Tennessee</cite></blockquote>
    <blockquote class="quote"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p>"Grew up in the Alley, thought I knew it all. The helmet rule and the two-alert-paths chapter changed how we do tornado season with the grandkids."</p><cite>Roy &middot; Kansas</cite></blockquote>
    <blockquote class="quote"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p>"Thirty years on the Hurricane Coast. The garage-door bracing cost me sixty dollars at the hardware store. My neighbor's door failed last season; ours held."</p><cite>Frank &middot; Louisiana</cite></blockquote>
    <blockquote class="quote"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p>"Bought it for the tornado chapters, stayed for the paper week. Our insurance agent asked where the inventory video came from."</p><cite>Pat &amp; Gene &middot; Arkansas</cite></blockquote>
    <blockquote class="quote"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p>"The 'what this does not do' boxes are what sold me. First prep book I've read that tells you the limits of its own advice."</p><cite>Walt &middot; Nebraska</cite></blockquote>
    <blockquote class="quote"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p>"Did the walk-around weekend with my grandsons. They know where the water main is now. So do I, for the first time in forty years."</p><cite>Eleanor &middot; Georgia</cite></blockquote>
    <blockquote class="quote"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p>"My wife teases me about the binder on the refrigerator. She also knows exactly which page the policy numbers are on, and that's the point."</p><cite>Sam &middot; Ohio</cite></blockquote>
    <blockquote class="quote"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p>"We evacuated ahead of the last hurricane with the go-bag packed straight from the binder form. Calmest we have ever left the house."</p><cite>Rosa &middot; Florida</cite></blockquote>
  </div>
</section>
"""

# ---------------------------------------------------------------------------
# Sheet 6: About the author
# ---------------------------------------------------------------------------
SHEET_PAUL = """
<section class="sheet" id="sheet-paul">
  <p class="kick">Who wrote this &middot; Paul Raymond</p>
  <div class="row">
    <div>
      <h2>Written by hands that have done every protection in it.</h2>
      <p style="font-family:var(--display);font-weight:700;font-size:23px;line-height:1.4;color:var(--ink);border-left:4px solid var(--tab2);padding-left:20px;margin:0 0 22px">
        "I got tired of watching the same three mistakes kill people in the report
        afterwards. Not exotic mistakes. The same three, in county after county, storm
        after storm. This book is those reports turned back into things a family can do on
        a Saturday."</p>
      <p>The manual is built from the documents most people never read: National Weather
        Service service assessments, NIST investigations, day-after archives, and
        converted into numbered actions with real prices next to them. Every hazard
        chapter opens with an event that actually happened and ends with what would have
        changed it.</p>
    </div>
    <figure style="margin:0"><img class="photo" src="assets/headshot.webp" width="500"
      height="600" alt="Paul Raymond" loading="lazy"></figure>
  </div>

  <p class="kick" style="margin-top:54px">The work, not the theory</p>
  <div class="gallery" style="grid-template-columns:repeat(3,1fr)">
    <figure><img src="assets/paul-plywood.webp" width="672" height="672"
      alt="Paul Raymond fastening plywood window protection in driving rain" loading="lazy">
      <figcaption>Protection 73, opening protection, done before the season, not the
        siren.</figcaption></figure>
    <figure><img src="assets/field-kit.webp" width="672" height="672"
      alt="NOAA weather radio, helmet and field binder laid out on a table" loading="lazy">
      <figcaption>The field kit behind the book. Your household version costs a tenth as
        much.</figcaption></figure>
    <figure><img src="assets/paul-stage.webp" width="672" height="448"
      alt="Paul Raymond holding The Storm-Ready Home while speaking to an audience" loading="lazy">
      <figcaption>Explaining the part nobody believes: the first week of the plan costs
        nothing.</figcaption></figure>
  </div>
</section>
"""

# ---------------------------------------------------------------------------
# Sheet 7: FAQs -- all 7 live questions, verbatim (em dashes fixed)
# ---------------------------------------------------------------------------
SHEET_QUESTIONS = """
<section class="sheet" id="sheet-questions">
  <p class="kick">Before you buy</p>
  <h2>Questions people ask.</h2>
  <dl class="faq">
    <div><dt>What exactly do I get, and in what format?</dt><dd>A single PDF of 486 pages,
      delivered to your inbox immediately after payment, plus the printable binder pages
      and your state packets. Readable on a phone, tablet or computer, and printable at a
      kitchen table. No app, no DRM, no subscription.</dd></div>
    <div><dt>Isn't this information free from FEMA?</dt><dd>Some of it is, and the book
      cites those documents rather than hiding them. What the federal guides give you is
      pamphlet prose: no prices, no build steps, no fillable forms, no regional ordering
      and no state directory. This book was written because reading the source documents
      and turning them into a Saturday's work is the part nobody does.</dd></div>
    <div><dt>I rent. Is this useful to me?</dt><dd>Yes, and the book flags it protection by
      protection. Most of the highest-value items need no permission at all: the room
      selection, the water store, the document vault, the alert enrollment, the
      prescription buffer, the trigger plan, the binder. The structural hardening chapters
      are marked so you can skip what you can't do.</dd></div>
    <div><dt>Which region is mine?</dt><dd>The front matter walks you through it in about
      five minutes, and most readers are in two regions rather than one, which is fine,
      because regions only change the order you work in, not what you read. Every chapter
      is in every copy.</dd></div>
    <div><dt>Is this a prepper book?</dt><dd>No. There is no bunker content, no firearms, no
      grid-down-forever scenario and no politics. It is a family safety manual about
      weather and natural disasters, and every instruction is traceable to a citable
      authority.</dd></div>
    <div><dt>I'm not good with technology. Will I manage?</dt><dd>If you can open an email,
      you can use this book. It arrives as one ordinary PDF: no app to install, no account
      to create, no login to remember. Print any page at home or at a copy shop, and the
      binder is designed to be filled in with a pen.</dd></div>
    <div><dt>What's your refund policy?</dt><dd>Seven days, no questions asked. Reply to
      the delivery email and the $14.99 comes back. You keep the files.</dd></div>
  </dl>
</section>
"""

# ---------------------------------------------------------------------------
# Sheet 8: Get my copy -- order form, free state packet block, last call
# ---------------------------------------------------------------------------
SHEET_GET = """
<section class="sheet" id="sheet-get">
  <div class="order">
    <div>
      <p class="kick">The offer</p>
      <h2>One book. Everything in it. Yours in two minutes.</h2>
      <p class="lead">Instant PDF download. Pay once, own it forever.</p>
      <img src="assets/cover-mini.webp" width="260" height="347" alt=""
        style="max-width:220px;height:auto;box-shadow:0 20px 30px -14px rgba(0,0,0,.6);transform:rotate(-3deg)"
        loading="lazy">
    </div>
    <div class="form">
      <div class="price">$14.99 <s>$87.99</s></div>
      <p style="font-family:var(--mono);font-size:12px;color:var(--faded);margin:6px 0 0">
        Launch price. One payment, no subscription, yours permanently.</p>
      <ul class="incl">
        <li><span><b>The Storm-Ready Home: 486-page illustrated PDF.</b> 130 numbered
          protections across 23 hazard playbooks, with costs, times and materials.</span><span>$14.99</span></li>
        <li><span><b>The Binder: 61 pages of printable, fillable forms.</b> Household
          communication plan, home inventory, medication and insurance records, wallet
          cards.</span><span>$19</span></li>
        <li><span><b>The 60-Day Sequence.</b> Day by day, ordered so the free week comes
          before the weeks that cost money.</span><span>$15</span></li>
        <li><span><b>All 51 State Packets: 50 states and DC.</b> Your forecast office,
          emergency management agency, county alert signup, insurance department and
          mitigation credits, for every state, in case you move.</span><span>$19</span></li>
        <li><span><b>Lifetime updates.</b> Agencies reorganise and links move. Every
          revision, free, permanently.</span><span>$20</span></li>
      </ul>
      <p style="display:flex;justify-content:space-between;font-family:var(--mono);font-size:13px;color:var(--faded);text-transform:uppercase;letter-spacing:.06em;margin:0 0 4px">
        <span>Total value</span><span>$87.99</span></p>
      <p style="display:flex;justify-content:space-between;font-family:var(--display);font-weight:700;font-size:19px;color:var(--ink);margin:0 0 16px">
        <span>You pay today</span><span style="color:var(--cta)">$14.99</span></p>
      <a class="btn" style="width:100%" href="@@BUY@@">Get My Copy</a>
      <p style="margin:10px 0 0;text-align:center;font-family:var(--mono);font-size:12px;color:var(--faded)">
        Secure checkout &middot; Visa &middot; Mastercard &middot; PayPal &middot; Apple Pay</p>
      <div class="guar"><div class="seal">7-DAY<br>MONEY<br>BACK</div><p style="margin:0;font-size:16px">
        <strong>Read it for a week on me.</strong> If it isn't the most useful book in your
        house, reply to the delivery email and the $14.99 comes back, no questions, no
        forms. You keep the files either way.</p></div>
    </div>
  </div>

  <div class="row" style="margin-top:60px;align-items:start">
    <div class="form">
      <p class="kick" style="margin-bottom:6px">Free, on me</p>
      <h2 style="font-size:clamp(26px,3.2vw,34px)">Not ready? Take your state's storm
        packet, free.</h2>
      <p class="lead" style="font-size:18px">Four pages, specific to where you live: the
        three hazards your state actually gets and the months they arrive, who to call,
        emergency management, insurance regulator, energy assistance, your state's
        mitigation program and deductible rules, and a one-page plan pre-filled with your
        state's specifics.</p>
      <p><strong>Pick your state. The packet is in your inbox in under a minute.</strong></p>
      <div style="display:flex;gap:12px;flex-wrap:wrap;margin-top:12px">
        <select id="state-select" aria-label="Your state"
          style="flex:1 1 220px;min-height:52px;padding:0 14px;font:inherit;font-size:16px;color:var(--ink);background:#fffdf7;border:1px solid var(--rule);border-radius:6px">
          @@STATES@@
        </select>
        <a class="btn" id="packet" href="@@PACKET@@">Send My State Packet, Free</a>
      </div>
      <p style="margin-top:14px;font-size:15px;color:var(--faded)">Costs nothing, and you
        keep it whether or not you ever buy the manual. Every state and DC is covered.</p>
    </div>
    <figure style="margin:0">
      <img class="photo" src="assets/paul-binder.webp" width="564" height="564"
        alt="Paul Raymond filling in the printed binder at a kitchen table" loading="lazy">
      <figcaption>The binder, the way it's meant to be used, at a kitchen table, with a
        pen.</figcaption>
    </figure>
  </div>

  <div style="margin-top:60px;padding-top:40px;border-top:2px dashed var(--rule);text-align:center">
    <h2>The only window you get is the one where nothing is happening.</h2>
    <p class="lead" style="margin-left:auto;margin-right:auto">That's the whole argument of
      the book, and it's why the first week costs nothing. $14.99 once, seven-day refund,
      yours permanently. The next report will be written about somebody. It doesn't have to
      mention your street.</p>
    <p><a class="btn" href="@@BUY@@">Get My Copy</a></p>
    <p style="font-family:var(--mono);font-size:13px;color:var(--faded)">Instant download
      &middot; 7-day money-back guarantee</p>
  </div>
</section>
"""

SHEETS = (
    SHEET_START + SHEET_WHY + SHEET_INSIDE + SHEET_SAVES + SHEET_READERS
    + SHEET_PAUL + SHEET_QUESTIONS + SHEET_GET
)

# ---------------------------------------------------------------------------
# body_extra: only the free-state-packet select-syncs-the-link script (ported
# from live). Urgency widgets (band/countdown/toast) come from chrome.py --
# never duplicated here.
# ---------------------------------------------------------------------------
BODY_EXTRA = """
<script>
(function(){
  var sel=document.getElementById('state-select'), a=document.getElementById('packet');
  if(!sel||!a)return;
  var base='@@PACKET@@';
  var sync=function(){a.href=sel.value?base+'&variant='+encodeURIComponent(sel.value)+'&price=0':base;};
  sel.addEventListener('change',sync); sync();
})();
</script>
"""


def main():
    html = chrome.render(
        title=TITLE,
        description=DESCRIPTION,
        canonical=CANONICAL,
        tabs=TABS,
        sheets=SHEETS,
        depth=0,
        head_extra=HEAD_EXTRA,
        body_extra=BODY_EXTRA,
    )
    html = (
        html.replace("@@BUY@@", chrome.BUY)
        .replace("@@PACKET@@", chrome.PACKET)
        .replace("@@STATES@@", STATE_OPTIONS)
    )
    OUT.write_text(html, encoding="utf-8")
    print(f"wrote {OUT} ({len(html)} bytes)")


if __name__ == "__main__":
    main()
