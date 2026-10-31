# Damodar Valley Corporation v. Maithan Alloys Limited & Ors., 2026 INSC 1178, Civil Appeal No. 11106 of 2024 (K. Vinod Chandran J.
# wrote it, J.B. Pardiwala J.; decided 30.10.2026, REPORTABLE): panel cues, run by split/build_course_plan.py (helpers: at S E cue fx
# have r3 PEND). Concept format as sets cdp / srb.
# Facts from the judgment (paras): CERC fixed DVC's tariff for 2009 to 2014 under the Electricity Act 2003, the DVC Act 1948 and the
# Tariff Regulations of 2009 (2); the Sinking Fund = a portion of the profits appropriated to redeem the bonds issued by DVC (2);
# Regulation 43(2)(iv): Section 40 funds "items of expenditure to be recovered through tariff"; the Sinking Fund a first charge, an
# expense (20, 21); the very same issue upheld for the earlier years in Bhaskar Shrachi Alloys (2018) 8 SCC 281 (1, 2, 27); CERC
# order 2013 upheld by the Appellate Tribunal for Electricity "on its own reasoning and based on the binding precedent" (3), order
# dated 17.05.2019 (30); none challenged it, no appeal to this Court (3, 30); a review by one of the appellants (the consumers),
# pending 5 years, allowed in 2024 (1, 3); the first respondent was the review petitioner, one of the consumers (4, 8); the review:
# depreciation on bond-funded assets + the Sinking Fund = "duplication or double allowance", DVC may claim only one (7, 25); the issue
# "escaped the notice of this Court also" (7, 25); the respondents: a "double benefit", an undue burden on the consumer (6); SAIL, a
# Public Sector Undertaking, intervened (3). Held: Bhaskar Shrachi re-examined since a Larger Bench reference was open if the coordinate
# bench had erred (8); "absolutely no reason to doubt the earlier decision" (14, 15); depreciation with the Sinking Fund "specifically
# considered and upheld" (24); both under Section 40 of the DVC Act, though the words "duplication" / "double allowance" were not used
# (26); "no scope for a review" (23); "the Tribunal has gone haywire" (27); Kamal Sengupta (2008) 8 SCC 612, paras 22 and 35: an error
# "evident per se from the record", not one found by a long process of reasoning; "cannot sit in appeal" (27, 28); the review fits none
# of the principles (28); "clearly illegal, totally misplaced and blatantly in breach of the principles of judicial discipline", a
# violation of Article 141 (29). Orders: review order set aside, the order of 17.05.2019 restored; Rs 2,00,000 on the 1st respondent,
# "an abuse of process of law"; Rs 1,50,000 on SAIL, "ill-advised"; to DVC within one month, else 18% p.a. (30); appeal allowed with
# costs, in addition to the exemplary costs (31).
# Not on any card: the review section number (the judgment prints "Section 122(f)" of the Electricity Act; not voiced, not shown). No
# section card: it would print "§". Only companies and public bodies named. Official portraits on the bench card.
# List lines <= 52 chars (9:16 list items do not wrap).
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen, as srb / cdp)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
STING = {"kicker": "SUPREME COURT · JUDGMENT EXPLAINED", "title": "Can review reopen a settled point?", "sub": "DVC v. Maithan Alloys · 2026 INSC 1178"}
ENDCARD = {"title": "Can review reopen a settled point?", "line": "A tribunal cannot review away a Supreme Court ruling", "sub": "LawWorld: legal research for advocates"}

# ── 1 · reopen a settled point? ──────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "tribunal"), text="Can a tribunal, on review, reopen a point the Supreme Court had already settled, five years after its own order?", hl="the Supreme Court had already settled")
cue(type="bench", t0=S("c02"), t1=E("c02") + 0.05, tag="Supreme Court of India · 30 October 2026",
    judges=[{"name": "Justice J.B. Pardiwala", "photo": "../brand/judges/jb_pardiwala.jpg", "at": A("c02", "honourable")},
            {"name": "Justice K. Vinod Chandran", "photo": "../brand/judges/k_vinod_chandran.jpg", "at": A("c02", "honourable", 2)}])

# ── 2 · the tariff ───────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=A("c03", "damodar"), t1=E("c04") + 0.05, at=A("c03", "damodar"), tag="SUPREME COURT OF INDIA · 30.10.2026",
    cases=[{"name": "Damodar Valley Corporation v. Maithan Alloys Ltd & Ors.", "cite": "2026 INSC 1178 · Civil Appeal No. 11106 of 2024"}])
cue(type="flow", t0=S("c03"), t1=E("c03") + 0.05, head="DVC's tariff · 2009 to 2014", head_at=S("c03") + 0.05,
    steps=[{"label": "Fixed by the CERC", "sub": "Electricity Act 2003 · DVC Act 1948 · Tariff Regulations 2009", "icon": "landmark", "at": A("c03", "regulator")},
           {"label": "The Sinking Fund", "sub": "profits set aside to redeem the bonds DVC issued", "icon": "file-text", "at": A("c03", "sinking")},
           {"label": "Counted as an expense in the tariff", "sub": "Regulation 43: Section 40 funds, “items of expenditure”", "icon": "check", "at": A("c03", "counted")}])
cue(type="timeline", t0=S("c04"), t1=E("c04") + 0.05,
    nodes=[{"label": "BHASKAR SHRACHI ALLOYS", "value": "(2018) 8 SCC 281", "sub": "Supreme Court · Sinking Fund upheld, earlier years", "at": A("c04", "supreme")},
           {"label": "APPELLATE TRIBUNAL", "value": "17 May 2019", "sub": "CERC order upheld · own reasoning + the precedent", "at": A("c04", "nineteen")},
           {"label": "NO APPEAL", "value": "none challenged it", "sub": "no appeal to the Supreme Court", "at": A("c04", "no")}])

# ── 3 · the review ───────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c05"), t1=E("c05") + 0.05, head="The review", head_at=S("c05") + 0.05,
    steps=[{"label": "Filed by one consumer", "sub": "an appellant before the Tribunal · now the 1st respondent", "icon": "user", "at": A("c05", "consumer")},
           {"label": "Pending for five years", "sub": "allowed in 2024", "icon": "calendar", "at": A("c05", "waited")},
           {"label": "“Duplication or double allowance”", "sub": "depreciation on bond-funded assets + the Sinking Fund", "icon": "x", "tone": "stop", "at": A("c05", "calling")}])
cue(type="point", t0=S("c06"), t1=A("c06", "corporation") - 0.05, text="The review: the issue had “escaped the notice” of the Supreme Court too · DVC may claim only one: the Sinking Fund or depreciation on bond-funded assets", icon="search", at=A("c06", "point"))
cue(type="flow", t0=A("c06", "corporation") - 0.05, t1=E("c06") + 0.05, head="In the Supreme Court", head_at=A("c06", "corporation"),
    steps=[{"label": "DVC appeals", "sub": "Civil Appeal No. 11106 of 2024", "icon": "landmark", "at": A("c06", "appealed")},
           {"label": "SAIL intervenes", "sub": "a Public Sector Undertaking, backing the review", "icon": "user", "at": A("c06", "steel")}],
    note={"text": "The respondents' case: a “double benefit”, an undue burden on the consumer", "icon": "info", "at": A("c06", "intervened")})

# ── 4 · what the court held ──────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c07"), t1=A("c07", "but") - 0.05, text="Had the coordinate bench erred, a Larger Bench reference was open · the Court found “absolutely no reason to doubt the earlier decision”", icon="search", at=A("c07", "bhaskar"))
cue(type="list", t0=A("c07", "but") - 0.05, t1=E("c07") + 0.05, head="Bhaskar Shrachi had decided it", head_at=A("c07", "but"),
    items=[{"n": 1, "text": "Depreciation and Sinking Fund: considered together", "at": A("c07", "depreciation")},
           {"n": 2, "text": "Both allowed under Section 40 of the DVC Act", "at": A("c07", "sinking")},
           {"n": 3, "text": "So, no scope for a review of the 2019 order", "at": A("c07", "scope")}])
cue(type="list", t0=S("c08"), t1=A("c08", "court") - 0.05, head="Review: the limits · Kamal Sengupta", head_at=A("c08", "kamal"),
    items=[{"n": 1, "text": "The error must be evident per se from the record", "at": A("c08", "error")},
           {"n": 2, "text": "Not one found by a long process of reasoning", "at": A("c08", "record")},
           {"n": 3, "text": "No sitting in appeal over its own decision", "at": A("c08", "cannot")}])
cue(type="point", t0=A("c08", "court") - 0.05, t1=E("c08") + 0.05, text="“the Tribunal has gone haywire” · the review fits none of the Kamal Sengupta principles", icon="scale", accent=True, at=A("c08", "court"))

# ── 5 · the verdict ──────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c09"), t1=A("c09", "with") - 0.05, head="The verdict", head_at=S("c09") + 0.05,
    steps=[{"label": "Review order set aside", "sub": "“clearly illegal, totally misplaced” · in breach of judicial discipline", "icon": "x", "tone": "stop", "at": A("c09", "illegal")},
           {"label": "A violation of Article 141", "sub": "the highest court's decisions must be followed", "icon": "scale", "at": A("c09", "article")},
           {"label": "17 May 2019 order restored", "sub": "appeal allowed, with costs", "icon": "check", "tone": "ok", "at": A("c09", "twenty")}])
cue(type="list", t0=A("c09", "with") - 0.05, t1=E("c09") + 0.05, head="Exemplary costs, payable to DVC", head_at=A("c09", "costs"),
    items=[{"n": 1, "text": "₹2 lakh: the review petitioner, “abuse of process”", "at": A("c09", "consumer")},
           {"n": 2, "text": "₹1.5 lakh: SAIL, the intervener, “ill-advised”", "at": A("c09", "steel")},
           {"n": 3, "text": "Within a month, else 18% interest a year", "at": A("c09", "authority")}])
cue(type="point", t0=S("c10"), t1=E("c10") + 0.05, text="Like · Share · Subscribe · lawworld.ai", icon="check", accent=True, at=A("c10", "like"))
