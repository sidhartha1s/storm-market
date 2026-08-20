import json

data = {
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Book",
      "name": "The Storm-Ready Home",
      "author": {"@type": "Person", "name": "Paul Raymond"},
      "numberOfPages": 486,
      "bookFormat": "https://schema.org/EBook",
      "inLanguage": "en",
      "url": "https://paulraymond.online/",
      "offers": {
        "@type": "Offer",
        "price": "47",
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
        {"@type": "Question", "name": "What exactly do I get, and in what format?",
         "acceptedAnswer": {"@type": "Answer", "text": "A single PDF of 486 pages, delivered to your inbox immediately after payment, plus the printable binder pages and your state packets. Readable on a phone, tablet or computer, and printable at a kitchen table. No app, no DRM, no subscription."}},
        {"@type": "Question", "name": "Isn't this information free from FEMA?",
         "acceptedAnswer": {"@type": "Answer", "text": "Some of it is, and the book cites those documents rather than hiding them. What the federal guides give you is pamphlet prose — no prices, no build steps, no fillable forms, no regional ordering and no state directory. This book was written because reading the source documents and turning them into a Saturday's work is the part nobody does."}},
        {"@type": "Question", "name": "I rent. Is this useful to me?",
         "acceptedAnswer": {"@type": "Answer", "text": "Yes, and the book flags it protection by protection. Most of the highest-value items need no permission at all — the room selection, the water store, the document vault, the alert enrollment, the prescription buffer, the trigger plan, the binder. The structural hardening chapters are marked so you can skip what you can't do."}},
        {"@type": "Question", "name": "Which region is mine?",
         "acceptedAnswer": {"@type": "Answer", "text": "The front matter walks you through it in about five minutes, and most readers are in two regions rather than one — which is fine, because regions only change the order you work in, not what you read. Every chapter is in every copy."}},
        {"@type": "Question", "name": "Is this a prepper book?",
         "acceptedAnswer": {"@type": "Answer", "text": "No. There is no bunker content, no firearms, no grid-down-forever scenario and no politics. It is a family safety manual about weather and natural disasters, and every instruction is traceable to a citable authority."}},
        {"@type": "Question", "name": "I'm not good with technology. Will I manage?",
         "acceptedAnswer": {"@type": "Answer", "text": "If you can open an email, you can use this book. It arrives as one ordinary PDF — no app to install, no account to create, no login to remember. Print any page at home or at a copy shop, and the binder is designed to be filled in with a pen."}},
        {"@type": "Question", "name": "What's your refund policy?",
         "acceptedAnswer": {"@type": "Answer", "text": "Seven days, no questions asked. Reply to the delivery email and the $47 comes back. You keep the files."}}
      ]
    }
  ]
}

s = json.dumps(data, indent=2, ensure_ascii=False)
block = f'<script type="application/ld+json">\n{s}\n</script>\n'
with open("ldjson_block.txt", "w", encoding="utf-8") as f:
    f.write(block)

# also verify it parses
json.loads(s)
print("OK, chars:", len(block))
