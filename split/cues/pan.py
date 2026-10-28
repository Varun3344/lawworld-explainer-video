# Lalit v. Union of India, Ministry of Finance through its Secretary & Ors., W.P.(C) 9365/2025 (High Court of Delhi, Division Bench:
# Dinesh Mehta J. (oral) and Dr. Aditi Choudhary J.; decided 06.10.2026, REPORTABLE): panel cues, run by split/build_course_plan.py
# (helpers: at S E cue fx have r3 PEND). Concept format as sets ara / krm / khan / levi.
# Facts from the judgment (paras): "an apparent case of misuse of Permanent Account Number" (1); PAN obtained as a government identity
# proof, income never taxable, per the petitioner; small contractual employee, security guard or cook, 01.04.2015-31.03.2019: Hotel
# Ashoka through Suraksha Security Agency, then Vigyan Bhawan through Mass Management Services Pvt. Ltd. as a cook (2, 9, 17, 20);
# s.148A(b) notice of 26.02.2024: per CBDT's Risk Management Strategy, cash payment of Rs 24,86,63,500 to a packaging-material firm,
# and a cash sale of Rs 24,62,01,485, under his PAN (3, 7, 22); police complaint 07.03.2024, PS Greater Kailash-I; Cyber Cell, Saket,
# 30.05.2024; "bore no fruit" (4); reply: no taxable income, no such transaction, PAN details misused; information and copies sought,
# "never supplied" (5); assessment order 17.03.2025: Rs 49,48,64,985 as turnover, 8% as income, AY 2017-18 (5); demand about
# Rs 3,91,06,511; penalty proceedings for misreporting, non-compliance, books not kept / not audited (6); Revenue: statutory remedy
# bypassed, disputed facts (10). Held: appeal "illusory and inefficacious" (12); CBDT OM F. No. 404/72/93-ITCC of 31.07.2017: standard
# stay condition 20% of the disputed demand; interest runs under s.220(2); "a sum approaching ₹78 lakh" (13); material not supplied,
# reply not considered: natural justice, Arts. 14 and 21 (Maneka Gandhi (1978) 1 SCC 248) (14); Art. 21: dignity (Francis Coralie
# Mullin (1981) 1 SCC 608), mental health (Sukdeb Saha v. State of A.P., 2025 INSC 893); "avoidable mental anguish to a person of no
# means ... impinges upon Article 21" (15-18); order "founded solely" on RMS / Form 26AS data, no independent inquiry; the Revenue
# could give no satisfactory reply (19); his stand plausible, no nexus with the transactions; "the least the AO ought to have done":
# a s.133(6) notice to the vendor (20); bank statements produced, no business shown; "once the petitioner had denied the transactions
# and rebutted the presumption, the burden was upon the AO" (22); the gross payment and the same sum net of 1% TCS (Rs 24,62,015) added
# into Rs 49,48,64,985 of "turnover", demand "twofold"; "either he did not understand the basics of accounting or he did not want to"
# (23); order of 17.03.2025 quashed (25); fresh proceedings open only on other cogent and incriminating evidence, subject to limitation
# (26); writ allowed (27). The packaging firm is never named; the petitioner's name appears only on the cite card. The bench card uses
# the official portraits.
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen, as tej)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
STING = {"kicker": "DELHI HIGH COURT · JUDGMENT EXPLAINED", "title": "PAN misuse and Form 26AS data", "sub": "High Court of Delhi · W.P.(C) 9365/2025"}
ENDCARD = {"title": "PAN misuse and Form 26AS data", "line": "Form 26AS data alone, no inquiry · assessment quashed", "sub": "LawWorld: legal research for advocates"}

# ── 1 · form 26AS alone? ─────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "contract"), text="His PAN misused, he says: can the AO assess him on Form 26AS data alone?", hl="Form 26AS data alone?")
cue(type="bench", t0=S("c02"), t1=E("c02") + 0.05, tag="High Court of Delhi · 6 October 2026",
    judges=[{"name": "Justice Dinesh Mehta", "photo": "../brand/judges/dinesh_mehta.jpg", "at": A("c02", "honourable")},
            {"name": "Dr. Justice Aditi Choudhary", "photo": "../brand/judges/aditi_choudhary.jpg", "at": A("c02", "honourable", 2)}])

# ── 2 · the notice ───────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=A("c03", "contract"), t1=E("c04") + 0.05, at=A("c03", "contract"), tag="HIGH COURT OF DELHI · 06.10.2026",
    cases=[{"name": "Lalit v. Union of India & Ors.", "cite": "2026:DHC:9012-DB · W.P.(C) 9365/2025"}])
cue(type="flow", t0=S("c03"), t1=E("c03") + 0.05, head="The notice", head_at=S("c03") + 0.05,
    steps=[{"label": "Contract security guard / cook", "sub": "Ashoka Hotel and Vigyan Bhawan, through agencies", "icon": "user", "at": A("c03", "contract")},
           {"label": "Section 148A(b) notice · 26 Feb 2024", "sub": "Income Tax Act, 1961 · CBDT risk-management data", "icon": "file-text", "at": A("c03", "notice")},
           {"label": "Alleged: ₹24,86,63,500 paid in cash", "sub": "to a packaging firm · plus a ₹24,62,01,485 “cash sale” under his PAN", "icon": "x", "tone": "stop", "at": A("c03", "alleged")}])
cue(type="flow", t0=S("c04"), t1=A("c04", "then") - 0.05, head="His response", head_at=S("c04") + 0.05,
    steps=[{"label": "Police and Cyber Cell complaints", "sub": "PS Greater Kailash-I, 7 Mar 2024 · Cyber Cell, Saket, 30 May 2024", "icon": "file-text", "at": A("c04", "police")},
           {"label": "Reply: no such transactions", "sub": "his PAN misused, he says · details and copies sought", "icon": "user", "at": A("c04", "denied")},
           {"label": "Material not supplied", "sub": "before the assessment order", "icon": "x", "tone": "stop", "at": A("c04", "it")}])
cue(type="list", t0=A("c04", "then"), t1=E("c04") + 0.05, head="Assessment order · 17 Mar 2025", head_at=A("c04", "then"),
    items=[{"n": 1, "text": "₹49,48,64,985 taken as his turnover · AY 2017-18", "at": A("c04", "then")},
           {"n": 2, "text": "8% of it taken as his income", "at": A("c04", "demand")},
           {"n": "→", "text": "Demand ≈ ₹3.91 crore, and penalty proceedings", "at": A("c04", "nearly")}])

# ── 3 · appeal first? ────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c05"), t1=A("c05", "but") - 0.05, text="The Department: statutory remedies bypassed · disputed facts, not for a writ court", icon="landmark", at=A("c05", "department"))
cue(type="flow", t0=A("c05", "but"), t1=E("c05") + 0.05, head="The price of a stay", head_at=A("c05", "but"),
    steps=[{"label": "Standard condition: 20% of the demand", "sub": "CBDT Office Memorandum, 31 Jul 2017", "icon": "file-text", "at": A("c05", "stay")},
           {"label": "A sum approaching ₹78 lakh", "sub": "beyond his limited means", "icon": "x", "tone": "stop", "at": A("c05", "about")},
           {"label": "Interest keeps running", "sub": "Section 220(2), Income Tax Act", "icon": "calendar", "at": A("c05", "interest")}])
cue(type="point", t0=S("c06"), t1=A("c06", "and") - 0.05, text="The appeal remedy: “illusory and inefficacious” for him", icon="scale", accent=True, at=A("c06", "called"))
cue(type="section", t0=A("c06", "and"), t1=E("c06") + 0.05, at=A("c06", "and"), act="CONSTITUTION OF INDIA", num="Article 21", title="Life with dignity, and mental health",
    points=[{"text": "Dignity · Francis Coralie Mullin, (1981) 1 SCC 608", "at": A("c06", "avoidable")},
            {"text": "Mental health · Sukdeb Saha, 2025 INSC 893", "at": A("c06", "anguish")}],
    note={"text": "Avoidable mental anguish to a person of no means impinges on Article 21", "icon": "info", "at": A("c06", "impinges")})

# ── 4 · what the court held ──────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c07"), t1=A("c07", "order") - 0.05, text="Material withheld, reply not considered: natural justice breached · Articles 14 and 21", icon="scale", at=A("c07", "denying"))
cue(type="flow", t0=A("c07", "order"), t1=E("c07") + 0.05, head="The basis of the order", head_at=A("c07", "order"),
    steps=[{"label": "Form 26AS and annual summary", "sub": "risk-management data: the sole basis", "icon": "file-text", "at": A("c07", "form")},
           {"label": "No independent inquiry", "sub": "the Department gave no satisfactory reply", "icon": "x", "tone": "stop", "at": A("c07", "independent")},
           {"label": "The least: a Section 133(6) notice", "sub": "to the vendor, for details or its statement", "icon": "search", "at": A("c07", "inquiry")}])
cue(type="flow", t0=S("c08"), t1=A("c08", "and", 2) - 0.05, head="Who must prove it?", head_at=S("c08") + 0.05,
    steps=[{"label": "He denied the transactions", "sub": "his stand plausible, the Court found", "icon": "user", "at": A("c08", "denied")},
           {"label": "Presumption rebutted", "sub": "bank statements produced · no proof of any business", "icon": "file-check", "at": A("c08", "rebutted")},
           {"label": "Burden on the Assessing Officer", "sub": "to prove he really entered into them", "icon": "scale", "tone": "ok", "at": A("c08", "burden")}])
cue(type="flow", t0=A("c08", "and", 2), t1=E("c08") + 0.05, head="The AO counted it twice", head_at=A("c08", "and", 2),
    steps=[{"label": "₹24,86,63,500 · “cash payment”", "sub": "gross amount, in notice and order", "icon": "file-text", "at": A("c08", "counted")},
           {"label": "₹24,62,01,485 · “cash sale”", "sub": "the same sum, net of 1% TCS", "icon": "file-text", "at": A("c08", "same")},
           {"label": "Added: ₹49,48,64,985 “turnover”", "sub": "the demand became twofold", "icon": "x", "tone": "stop", "at": A("c08", "twice")}])

# ── 5 · the verdict ──────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "order") - 0.05, text="“either he did not understand the basics of accounting or he did not want to”", icon="scale", accent=True, at=A("c09", "either"))
cue(type="verdicts", t0=A("c09", "order"), t1=E("c09") + 0.05,
    rows=[{"text": "Assessment order of 17 Mar 2025: quashed", "ok": True, "at": A("c09", "quashed")},
          {"text": "Fresh proceedings only on other cogent, incriminating evidence · within limitation", "ok": True, "at": A("c09", "fresh")},
          {"text": "Writ petition allowed", "ok": True, "at": A("c09", "cogent")}])
cue(type="point", t0=S("c10"), t1=E("c10") + 0.05, text="Like · Share · Subscribe · lawworld.ai", icon="check", accent=True, at=A("c10", "like"))
