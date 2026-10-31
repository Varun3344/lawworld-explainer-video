# State of Karnataka & Ors. v. Shashikiran G & Ors., Writ Appeal No. 909 of 2026 (LA-RES) (High Court of Karnataka, Division Bench:
# D K Singh J. wrote it, H. Shanthi Bhushan J.; reserved 10.09.2026, pronounced 28.10.2026, REPORTABLE): panel cues, run by
# split/build_course_plan.py (helpers: at S E cue fx have r3 PEND). Concept format as sets kmv / vzj.
# Facts from the judgment (paras): the State appeals the Single Judge's order of 02.05.2025 in W.P. 51697/2013 and connected matters
# (Preface); subject lands: Sy.Nos. 65, 66, 67/2, 68/1, 69, 71, 19 acres 18 guntas, Naganathapura village, Begur Hobli, Bangalore South
# Taluk (1); 1980 notification for the Central Jail, used for a road to the new jail (2); 1989 notification, final declaration of
# 24.05.1990 withdrawn by the State (3); 1998 notification, the 2001 Section 17 urgency order quashed on 12.04.2012 with liberty to
# notify afresh (4); preliminary notification 19.07.2012 under Section 4(1), objections 23.08.2012, the SLAO's report 25/26.03.2013,
# final declaration 07.08.2013 under Section 6(1) (5); Single Judge: final declaration quashed, the State to decide afresh considering
# the Section 5A(2) report, the objections and the ADGP / IG of Prisons' version (6); the report did not consider the Devanahalli land,
# the Single Judge held (13), "no whisper" (15); the State's case: Rule 876(IV), Chapter 45, Prisons Correctional Services Manual 2021,
# no building up to 200 metres of the main wall; a high security prison; staff quarters for over a thousand officers and staff; over
# 5000 prisoners (8, 8.2, 8.3, 8.4); the landowners: no prior Government decision before the declaration (9.1); the report (14): price
# "likely to be hundreds of crores of rupees"; "discuss at a high level" why a small portion of the Prison Department's 113 acres at
# Devanahalli should not be used; a "220 kilowatt" high-voltage line crosses the land (21: "the high-tension power line"); no 75-metre buffer possible on all four sides; cost "high and
# unbearable"; the Government "free to take an appropriate decision". Held: the Devanahalli objection was considered and sent for
# high-level discussion; the contrary finding "unsustainable and contrary to the material available on record" (15, 21); Section 5A
# is administrative; no need to answer each objection separately or elaborately; the consideration must be real, not mechanical or
# perfunctory (16, 17, 25, 28); "Brevity of reasons is not synonymous with absence of reasons" (Alok Kotahwala, SC, quoted at 27);
# the report is recommendatory, not binding; the Government is the ultimate arbiter (HUDA v. Abhishek Gupta, 31) and may differ on an
# independent application of mind (30-33, 47); a Section 6 declaration need not contain reasons; the absence of reasons is distinct
# from the absence of application of mind; the decision must precede the declaration (Hindustan Petroleum v. Darius Shapur Chenai,
# 35-37, 46); expansion of the existing Central Prison is a bona fide public purpose, not to be set aside on "hyper-technicalities" (48).
# Orders (49): writ appeal allowed; the order of 02.05.2025 set aside; the State and the authorities to take necessary steps to address
# the RCC buildings, residential layouts, engineering workshops and developed sites on the notified lands, in accordance with law.
# Flow policy: no landowner named in speech (the case title appears only on the cite bar); no "fraud", "collusion", "admitted".
# Official Karnataka High Court portraits on the bench card (judiciary.karnataka.gov.in, common_folder/judge_profile/dksj.jpeg and
# gsbj.jpg). List lines <= 52 chars (9:16 list items do not wrap). No section sign anywhere.
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen, as kmv / vzj)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
STING = {"kicker": "KARNATAKA HIGH COURT · JUDGMENT EXPLAINED", "title": "Officer's doubts don't bind State", "sub": "State of Karnataka v. Shashikiran G · WA No. 909 of 2026"}
ENDCARD = {"title": "Officer's doubts don't bind State", "line": "A Section 5A report only recommends · prison expansion a bona fide public purpose", "sub": "LawWorld: legal research for advocates"}

# ── 1 · a report with doubts ─────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "officer"), text="The officer who heard the objections has reservations. Can the State still acquire the land?", hl="still acquire the land?")
cue(type="bench", t0=S("c02"), t1=E("c02") + 0.05, tag="Karnataka High Court · 28 October 2026",
    judges=[{"name": "Justice D.K. Singh", "photo": "../brand/judges/dk_singh.jpg", "at": A("c02", "honourable")},
            {"name": "Justice H. Shanthi Bhushan", "photo": "../brand/judges/h_shanthi_bhushan.jpg", "at": A("c02", "honourable", 2)}])

# ── 2 · the prison land ──────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=A("c03", "parappana"), t1=E("c05") + 0.05, at=A("c03", "parappana"), tag="HIGH COURT OF KARNATAKA · 28.10.2026",
    cases=[{"name": "State of Karnataka & Ors. v. Shashikiran G & Ors.", "cite": "Writ Appeal No. 909 of 2026 (LA-RES)"}])
cue(type="flow", t0=S("c03"), t1=A("c03", "two") - 0.05, head="The land", head_at=S("c03") + 0.05,
    steps=[{"label": "19 acres 18 guntas · Naganathapura", "sub": "Begur Hobli, Bangalore South Taluk", "icon": "file-text", "at": A("c03", "land")},
           {"label": "For the Central Prison", "sub": "Parappana Agrahara, Bengaluru · its expansion", "icon": "landmark", "at": A("c03", "parappana")}])
cue(type="timeline", t0=A("c03", "two") - 0.05, t1=E("c03") + 0.05,
    nodes=[{"label": "1989 NOTIFICATION", "value": "Withdrawn", "sub": "the State withdrew its 1990 declaration", "at": A("c03", "attempts")},
           {"label": "1998 NOTIFICATION", "value": "Order quashed", "sub": "the 2001 Section 17 urgency order · 12.04.2012", "tone": "stop", "at": A("c03", "fell")},
           {"label": "FRESH NOTIFICATION", "value": "19 July 2012", "sub": "Section 4(1) · the same lands", "at": A("c03", "twelve")}])
cue(type="flow", t0=S("c04"), t1=E("c04") + 0.05, head="Section 5A(2) report · 25.03.2013", head_at=S("c04") + 0.05,
    steps=[{"label": "Cost “high and unbearable”", "sub": "likely “hundreds of crores of rupees”", "icon": "x", "tone": "stop", "at": A("c04", "unbearable")},
           {"label": "Prison land at Devanahalli", "sub": "113 acres: “discuss at a high level” why a small portion should not be used", "icon": "search", "at": A("c04", "urged")},
           {"label": "Also flagged", "sub": "a high-tension power line across the land · no 75 m buffer possible on all four sides", "icon": "info", "at": A("c04", "look")}],
    note={"text": "The Government “free to take an appropriate decision”, the report says", "icon": "landmark", "at": A("c04", "department")})
cue(type="timeline", t0=S("c05"), t1=A("c05", "finding") - 0.05,
    nodes=[{"label": "FINAL DECLARATION", "value": "7 Aug 2013", "sub": "Section 6(1), Land Acquisition Act, 1894", "at": A("c05", "declaration")},
           {"label": "SINGLE JUDGE", "value": "2 May 2025", "sub": "declaration quashed · decide afresh", "tone": "stop", "at": A("c05", "twenty", 2)}])
cue(type="point", t0=A("c05", "finding") - 0.05, t1=E("c05") + 0.05, text="Single Judge: the report did not consider the alternative land at Devanahalli · the State to decide afresh on the report, the objections and the IG of Prisons' version", icon="search", at=A("c05", "finding"))

# ── 3 · the appeal ───────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="list", t0=S("c06"), t1=E("c06") + 0.05, head="The State's case in appeal", head_at=A("c06", "appealed"),
    items=[{"n": 1, "text": "Over 5,000 prisoners in the Central Prison", "at": A("c06", "holds")},
           {"n": 2, "text": "Buffer zone: no building within 200 m of the wall", "at": A("c06", "buffer")},
           {"n": 3, "text": "A high security prison and staff quarters", "at": A("c06", "security")}])

# ── 4 · what the court held ──────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c07"), t1=E("c07") + 0.05, head="Held: the objections were considered", head_at=S("c07") + 0.05,
    steps=[{"label": "Devanahalli: expressly considered", "sub": "sent for high-level discussion · the contrary finding “unsustainable”", "icon": "file-check", "tone": "ok", "at": A("c07", "weigh")},
           {"label": "Section 5A: real, objective consideration", "sub": "an administrative exercise, not mechanical or perfunctory", "icon": "search", "at": A("c07", "section")},
           {"label": "No judgment on every objection", "sub": "brief reasons suffice · the report read as a whole", "icon": "scale", "at": A("c07", "not")}],
    note={"text": "“Brevity of reasons is not synonymous with absence of reasons” · Supreme Court, Alok Kotahwala", "icon": "info", "at": A("c07", "judgment")})
cue(type="flow", t0=S("c08"), t1=A("c08", "section") - 0.05, head="The report only recommends", head_at=S("c08") + 0.05,
    steps=[{"label": "Not binding on the Government", "sub": "the Government is the ultimate arbiter · HUDA v. Abhishek Gupta", "icon": "landmark", "at": A("c08", "government")},
           {"label": "It may differ from the report", "sub": "on an independent application of mind to the record", "icon": "scale", "at": A("c08", "differ")}])
cue(type="notequal", t0=A("c08", "section") - 0.05, t1=E("c08") + 0.05, left="No reasons in the declaration", right="no application of mind", at=A("c08", "section"),
    left_at=A("c08", "declaration"), sub="Section 6: the Government's decision must precede the declaration · Hindustan Petroleum", sub_at=A("c08", "state"))

# ── 5 · the verdict ──────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="verdicts", t0=S("c09"), t1=A("c09", "address") - 0.05,
    rows=[{"text": "Prison expansion: a bona fide public purpose", "ok": True, "at": A("c09", "expanding")},
          {"text": "Not to be set aside on “hyper-technicalities”", "ok": True, "at": A("c09", "bona")},
          {"text": "Writ appeal allowed · Single Judge's order set aside", "ok": True, "at": A("c09", "allowed")}])
cue(type="list", t0=A("c09", "address") - 0.05, t1=E("c09") + 0.05, head="The State to address, in accordance with law", head_at=A("c09", "address"),
    items=[{"n": 1, "text": "RCC buildings and residential layouts", "at": A("c09", "buildings")},
           {"n": 2, "text": "Engineering workshops and developed sites", "at": A("c09", "sites")}])
cue(type="point", t0=S("c10"), t1=E("c10") + 0.05, text="Like · Share · Subscribe · lawworld.ai", icon="check", accent=True, at=A("c10", "like"))
