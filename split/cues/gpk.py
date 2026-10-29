# V. Gopalakrishanan v. The State of Kerala, 2026 INSC 1172, Criminal Appeal No. 5399 of 2025 (Sanjay Kumar J., Sanjeev Sachdeva J. -
# Sachdeva J. wrote it; decided 28.10.2026, REPORTABLE): panel cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3
# PEND). Concept format as sets nkp / rcc.
# Facts from the judgment (paras): HC 29.01.2025 in Crl.A. No. 1937 of 2009 confirmed the conviction of 27.08.2009 (C.C. No. 40 of 2005,
# s.13(2) r/w s.13(1)(e) PC Act 1988: 2 years RI + Rs 5,50,000 fine) and reduced it to 1 year RI + Rs 2,00,000 fine (delay, age, trauma)
# (1); LDC 13.05.1971, Sub Registrar 22.09.1993; check period 01.01.1993-16.01.2001 (2); FIR 15.01.2001, VACB Special Cell,
# Thiruvananthapuram; 45 PWs, 130 exhibits (3); Statement A Rs 1,93,898.26, B Rs 12,37,720, C (income) Rs 10,12,117.20, D (expenditure)
# Rs 4,93,424, E (likely savings) Rs 5,18,693 (4); F = assets acquired minus likely savings (5); assets acquired Rs 10,43,822, DA Rs
# 5,25,129 = 51.88% of the income of the appellant and his family, "much beyond the 10% threshold" of Krishnanand Agnihotri (1977) 1 SCC
# 816, which is not a "hard and fast rule" (6, 7); his pleas: "based on estimation and not actual evidence", criteria "of an
# agricultural family" (9); building Rs 8,59,153 (1996 PWD rates) vs his Rs 6,69,000 (10); household Rs 1,968.96 vs Rs 1,200 a month,
# Rs 67,200 (11); Ex. P58 "only a notebook containing sporadic entries of costs", not kept in the ordinary course of business; the HC
# held so "and rightly so" (13); building plea on a demurrer: Rs 3,34,976, "more than 33%" (14); with the household plea too: Rs
# 2,67,776, "more than 26%" (15, 29); prosecution proves the foundational facts, "a prima facie case stands established" (22); the
# evidentiary burden shifts to the accused (23); undisclosed sources "peculiarly and exclusively within the knowledge of the public
# servant", s.109 BSA / s.106 Evidence Act (24); no "open-ended, limitless, or roving enquiry" (26); appeal dismissed, interim bail of
# 28.03.2025 vacated, two weeks to surrender before the Trial Court to undergo the remaining sentence (30). No section card: it would
# print "§" (not Indian style). The High Court is not named in the judgment, so no card names it. Official portraits on the bench card.
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen, as nkp)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
STING = {"kicker": "SUPREME COURT · JUDGMENT EXPLAINED", "title": "Who must explain the assets?", "sub": "V. Gopalakrishanan v. State of Kerala · 2026 INSC 1172"}
ENDCARD = {"title": "Who must explain the assets?", "line": "Disproportion proved: the burden shifts to the accused", "sub": "LawWorld: legal research for advocates"}

# ── 1 · who must explain? ────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "disproportionate"), text="A disproportionate assets case: who must explain the excess, the prosecution or the public servant?", hl="the prosecution or the public servant?")
cue(type="bench", t0=S("c02"), t1=E("c02") + 0.05, tag="Supreme Court of India · 28 October 2026",
    judges=[{"name": "Justice Sanjay Kumar", "photo": "../brand/judges/sanjay_kumar.jpg", "at": A("c02", "honourable")},
            {"name": "Justice Sanjeev Sachdeva", "photo": "../brand/judges/sanjeev_sachdeva.jpg", "at": A("c02", "honourable", 2)}])

# ── 2 · the check period ─────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=A("c03", "appellant"), t1=E("c04") + 0.05, at=A("c03", "appellant"), tag="SUPREME COURT OF INDIA · 28.10.2026",
    cases=[{"name": "V. Gopalakrishanan v. The State of Kerala", "cite": "2026 INSC 1172 · Criminal Appeal No. 5399 of 2025"}])
cue(type="point", t0=S("c03"), t1=A("c03", "check") - 0.05, text="Lower Division Clerk from 13 May 1971 · Sub Registrar from 22 Sep 1993", icon="user", at=A("c03", "registrar"))
cue(type="timeline", t0=A("c03", "check") - 0.05, t1=E("c03") + 0.05,
    nodes=[{"label": "CHECK PERIOD FROM", "value": "1 Jan 1993", "sub": "assets: ₹1,93,898", "at": A("c03", "january")},
           {"label": "CHECK PERIOD TO", "value": "16 Jan 2001", "sub": "assets: ₹12,37,720", "at": A("c03", "january", 2)}])
cue(type="flow", t0=S("c04"), t1=A("c04", "fifty") - 0.05, head="The prosecution's computation", head_at=A("c04", "prosecution"),
    steps=[{"label": "Assets acquired: ₹10,43,822", "sub": "₹12,37,720 at the end − ₹1,93,898 at the start", "icon": "landmark", "at": A("c04", "assets")},
           {"label": "Likely savings: ₹5,18,693", "sub": "income ₹10,12,117 − expenditure ₹4,93,424", "icon": "file-text", "at": A("c04", "savings")},
           {"label": "Disproportionate: ₹5,25,129", "sub": "assets acquired − likely savings", "icon": "scale", "at": A("c04", "five")}])
cue(type="point", t0=A("c04", "fifty") - 0.05, t1=E("c04") + 0.05, text="51.88% of the family's income: “much beyond the 10% threshold” of Krishnanand Agnihotri", icon="info", accent=True, at=A("c04", "fifty"))
cue(type="timeline", t0=S("c05"), t1=E("c05") + 0.05,
    nodes=[{"label": "FIR", "value": "15 Jan 2001", "sub": "Section 13(1)(e) r/w 13(2)", "at": A("c05", "trial")},
           {"label": "TRIAL COURT", "value": "27 Aug 2009", "sub": "2 years RI + ₹5,50,000 fine", "at": A("c05", "convicted")},
           {"label": "HIGH COURT", "value": "29 Jan 2025", "sub": "conviction confirmed", "at": A("c05", "upheld")},
           {"label": "SENTENCE CUT", "value": "1 year RI", "sub": "+ ₹2,00,000 fine", "at": A("c05", "sentence")}])

# ── 3 · his pleas ────────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="list", t0=S("c06"), t1=E("c06") + 0.05, head="The appellant's pleas", head_at=A("c06", "appellant"),
    items=[{"n": 1, "text": "The case is “based on estimation and not actual evidence”", "at": A("c06", "estimates")},
           {"n": 2, "text": "Household spend priced for an agricultural family, not a government servant", "at": A("c06", "agricultural")},
           {"n": 3, "text": "Building: his ₹6,69,000, not ₹8,59,153 at PWD rates", "at": A("c06", "building")}])
cue(type="point", t0=S("c07"), t1=A("c07", "and") - 0.05, text="Ex. P58: “only a notebook containing sporadic entries of costs”, not kept in the ordinary course of business", icon="x", at=A("c07", "notebook"))
cue(type="counters", t0=A("c07", "and") - 0.05, t1=E("c07") + 0.05, head="Even on his own figures", head_at=A("c07", "and"),
    items=[{"value": 51, "unit": "%+", "label": "As proved", "sub": "₹5,25,129 · 51.88%", "at": A("c07", "even")},
           {"value": 33, "unit": "%+", "label": "Less his building plea", "sub": "₹3,34,976 · “more than 33%”", "at": A("c07", "figures")},
           {"value": 26, "unit": "%+", "label": "Less his household plea too", "sub": "₹2,67,776 · “more than 26%”", "tone": "red", "at": A("c07", "excess")}])

# ── 4 · what the court held ──────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c08"), t1=A("c08", "undisclosed") - 0.05, head="Disproportionate assets: the burden", head_at=S("c08") + 0.05,
    steps=[{"label": "Prosecution proves", "sub": "known sources of income + assets in the check period", "icon": "search", "at": A("c08", "proves")},
           {"label": "A disproportion emerges", "sub": "“a prima facie case stands established”", "icon": "file-text", "at": A("c08", "disproportion")},
           {"label": "Burden shifts to the accused", "sub": "to account for the assets", "icon": "scale", "tone": "ok", "at": A("c08", "shifts")}])
cue(type="point", t0=A("c08", "undisclosed") - 0.05, t1=E("c08") + 0.05, text="Undisclosed sources: “exclusively within the knowledge of the public servant” · Section 109 BSA (Section 106 Evidence Act)", icon="scale", accent=True, at=A("c08", "undisclosed"))

# ── 5 · the verdict ──────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "appeal") - 0.05, text="No “open-ended, limitless, or roving enquiry” into every source an accused may claim", icon="search", at=A("c09", "investigators"))
cue(type="flow", t0=A("c09", "appeal") - 0.05, t1=E("c09") + 0.05, head="The verdict", head_at=A("c09", "appeal"),
    steps=[{"label": "Appeal dismissed", "sub": "conviction under Section 13(2) r/w 13(1)(e) PC Act stands", "icon": "check", "tone": "ok", "at": A("c09", "dismissed")},
           {"label": "Interim bail vacated", "sub": "granted on 28 Mar 2025", "icon": "x", "at": A("c09", "appellant")},
           {"label": "Surrender within 2 weeks", "sub": "before the Trial Court · the remaining sentence", "icon": "calendar", "at": A("c09", "weeks")}])
cue(type="point", t0=S("c10"), t1=E("c10") + 0.05, text="Like · Share · Subscribe · lawworld.ai", icon="check", accent=True, at=A("c10", "like"))
