# Inderchand Kochar & Anr. v. D. Devasitham, Arb O.P. (Com.Div.) No. 513 of 2026 (Section 11(6), A&C Act) with O.A. No. 528 of 2025
# (Section 9(1)(c)), 2026:MHC:4378 (High Court of Judicature at Madras, Sushrut Arvind Dharmadhikari CJ, sitting alone; reserved
# 16.10.2026, delivered 30.10.2026; reportable per the court's judis "reportable = Y" list, filename 1386455, citno 2026/MHC/4378; the
# PDF prints "Index : Yes"): panel cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND). Concept format as
# arm / bcr / kmv. English (High Courts page).
# Facts from the judgment (paras): prayers: s.11(6) petition to appoint a Sole Arbitrator under the Land Aggregator Agreement of
# 06.03.2016; O.A. under Order XIV Rule 8 O.S. Rules + s.9(1)(c) for an interim injunction against alienating the schedule property
# (prayers); one judgment disposes of both (1); the petitioners own land at Kalavakkam Village, Thiruporur Taluk and wanted the
# adjacent 24½ cents; the respondent claimed real estate expertise and agreed to act as land aggregator, to acquire it from its owner
# and convey it (2.1); "It is asserted": agreement 06.03.2016, total consideration Rs.90,00,000 paid in cash; settlement deed by the
# owner in the respondent's favour 02.03.2022; letter 12.01.2023 to the first petitioner: he had acquired the property and would soon
# execute the sale deed after clearing minor encroachments (2.2); the petitioners' case: a General Power of Attorney instead, on
# 20.02.2023, to a third party, found through an encumbrance certificate; legal notice under s.21 (2.3); full consideration received,
# Clause 5 violated (3.1); contradictory stands: O.A. counter "forged", stamp paper of October 2015, blank signed papers filled up;
# O.P. counter: signature not his (3.2); six rounds of mediation failed (3.3); Salson Liquors relied on (3.4). Respondent: "forged and
# fabricated", no money paid, unenforceable, against public policy (4.1); Rajia Begum v. Barnali Mukherjee, 2026 INSC 106 (4.2).
# Held: own confirmatory letter of 12.01.2023 enclosing parent documents, promising registration; the arbitration clause "not in
# genuine doubt"; disputes commercial, squarely within the clause (6); Rajia Begum's exceptional features: absent from contemporaneous
# records for nearly nine years, no standalone arbitration clause, s.9 proceedings final with a prima facie finding that the
# document's existence was highly doubtful (7); "fundamentally distinguishable"; contradictory positions across pleadings; forgery bars
# arbitration only when it goes to the root of the arbitration agreement itself; "merely a thin veil to wriggle out of binding
# commercial obligations" (8); Salson Liquors (order 20.02.2026, SLP (C) No. 16022 of 2025): genuineness / valid execution a
# preliminary issue for the Arbitrator, all contentions open; no shutting the doors on "a bald and afterthought plea of forgery" (9).
# Orders: Arb O.P. allowed; Justice R. Suresh Kumar, a retired judge of the Madras High Court, Sole Arbitrator; s.12 disclosure first;
# seat and venue Chennai (Clause 11); Madras High Court Arbitration Centre, its 2017 Rules, fee and charges borne equally; merits
# open (10); interim order in O.A. No. 528 of 2025 continues until the Arbitrator decides a s.17 application, to be filed within thirty
# days of entering upon the reference (11); the respondent may move s.16 before the Arbitrator; no costs (12).
# Not on any card as a finding: the agreement's genuineness, the payment and the power of attorney (they stay the petitioners' case);
# what the earlier interim order contained (the judgment does not say: "interim order", not "injunction"). No "admitted".
# Flow policy / neutrality: nobody is named in speech; the plot's owner and the attorney holder are not named on any card either; the
# cite bar (the parties' names, as the case title) runs over the letter sentence only (fact-check 31-10: not over the c03 cash-payment
# allegation, which he denies) and is gone before the power of attorney.
# Official Madras High Court portrait (hcmadras.tn.gov.in, present judges page, img_id 641) on the bench card. List lines <= 52 chars.
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen, as cdp)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
STING = {"kicker": "MADRAS HIGH COURT · JUDGMENT EXPLAINED", "title": "Forgery plea? Arbitrator appointed", "sub": "High Court of Madras · Arb. O.P. (Com. Div.) No. 513 of 2026 · 2026:MHC:4378"}
ENDCARD = {"title": "Forgery plea? Arbitrator appointed", "line": "Rajia Begum distinguished · genuineness goes to the arbitrator first", "sub": "LawWorld: legal research for advocates"}

# ── 1 · forged, so no arbitrator? ────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "other"), text="The other side calls the agreement forged. Can that plea alone stop a Section 11 court from appointing an arbitrator?", hl="appointing an arbitrator?")
cue(type="bench", t0=S("c02"), t1=E("c02") + 0.05, tag="Madras High Court · 30 October 2026",
    judges=[{"name": "Chief Justice Sushrut Arvind Dharmadhikari", "photo": "../brand/judges/sushrut_arvind_dharmadhikari.jpg", "at": A("c02", "honourable")}])

# ── 2 · the land deal ────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=A("c04", "january"), t1=A("c04", "but") - 0.05, at=A("c04", "january"), tag="HIGH COURT OF MADRAS · 30.10.2026",
    cases=[{"name": "Inderchand Kochar & Anr. v. D. Devasitham", "cite": "2026:MHC:4378 · Arb. O.P. (Com. Div.) No. 513 of 2026 & O.A. No. 528 of 2025"}])
cue(type="flow", t0=S("c03"), t1=E("c03") + 0.05, head="The petitioners' case", head_at=S("c03") + 0.05,
    steps=[{"label": "Land Aggregator Agreement · 6 Mar 2016", "sub": "the respondent agreed to act as land aggregator", "icon": "file-text", "at": A("c03", "aggregator")},
           {"label": "The adjacent 24½ cents", "sub": "next to their land at Kalavakkam Village, Thiruporur Taluk", "icon": "landmark", "at": A("c03", "plot")},
           {"label": "₹90,00,000 · paid in cash", "sub": "the total sale consideration, they say", "icon": "file-check", "at": A("c03", "rupees")}])
cue(type="timeline", t0=S("c04"), t1=E("c04") + 0.05,
    nodes=[{"label": "SETTLEMENT DEED", "value": "2 Mar 2022", "sub": "by the plot's owner, in the respondent's favour", "at": S("c04") + 0.1},
           {"label": "THE RESPONDENT'S LETTER", "value": "12 Jan 2023", "sub": "plot acquired · sale deed soon, after minor encroachments", "at": A("c04", "wrote")},
           {"label": "POWER OF ATTORNEY", "value": "20 Feb 2023", "sub": "to a third party, the petitioners say", "tone": "red", "at": A("c04", "power")},
           {"label": "LEGAL NOTICE", "value": "Section 21", "sub": "after an encumbrance certificate showed it", "at": A("c04", "third")}])

# ── 3 · the forgery plea ─────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="list", t0=S("c05"), t1=A("c05", "respondent") - 0.05, head="What the petitioners sought", head_at=A("c05", "sought"),
    items=[{"n": 1, "text": "Section 11(6): appoint a Sole Arbitrator", "at": A("c05", "arbitrator")},
           {"n": 2, "text": "Section 9(1)(c): interim injunction on the property", "at": A("c05", "injunction")}])
cue(type="flow", t0=A("c05", "respondent") - 0.05, t1=E("c05") + 0.05, head="The respondent's answer", head_at=A("c05", "answer"),
    steps=[{"label": "“forged and fabricated”", "sub": "the Land Aggregator Agreement, he argued", "icon": "file-text", "at": A("c05", "forged")},
           {"label": "No money was paid", "sub": "the agreement unenforceable, against public policy", "icon": "x", "tone": "stop", "at": A("c05", "money")}])
cue(type="cite", t0=A("c06", "rajia"), t1=E("c06") + 0.05, at=A("c06", "rajia"), tag="SUPREME COURT · RELIED ON BY THE RESPONDENT",
    cases=[{"name": "Rajia Begum v. Barnali Mukherjee", "cite": "2026 INSC 106"}])
cue(type="flow", t0=S("c06"), t1=E("c06") + 0.05, head="The respondent's authority", head_at=A("c06", "cited"),
    steps=[{"label": "Existence of an agreement “seriously disputed”", "sub": "an agreement with an arbitration clause · allegations of forgery and fraud", "icon": "search", "at": A("c06", "seriously")},
           {"label": "“non-arbitrable at that stage”", "sub": "the dispute stays out of arbitration, he argued", "icon": "x", "tone": "stop", "at": A("c06", "arbitrable")}])

# ── 4 · what the court held ──────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="list", t0=S("c07"), t1=A("c07", "here") - 0.05, head="Rajia Begum: exceptional features", head_at=A("c07", "exceptional"),
    items=[{"n": 1, "text": "Absent from records for nearly nine years", "at": A("c07", "document")},
           {"n": 2, "text": "No standalone arbitration clause in the document", "at": A("c07", "missing")},
           {"n": 3, "text": "Section 9, final: existence “highly doubtful”", "at": A("c07", "nearly")}])
cue(type="point", t0=A("c07", "here") - 0.05, t1=E("c07") + 0.05, text="Here, the respondent's own letter of 12 Jan 2023 “explicitly” acknowledged the acquisition · the arbitration clause is not in genuine doubt", icon="file-check", accent=True, at=A("c07", "here"))
cue(type="flow", t0=S("c08"), t1=E("c08") + 0.05, head="Why arbitration goes ahead", head_at=S("c08") + 0.05,
    steps=[{"label": "The respondent's contradictory pleas", "sub": "O.A. counter: blank signed papers filled up · O.P. counter: not his signature", "icon": "search", "at": A("c08", "contradicted")},
           {"label": "“merely a thin veil”", "sub": "to wriggle out of binding commercial obligations", "icon": "x", "tone": "stop", "at": A("c08", "veil")},
           {"label": "Genuineness: a preliminary issue", "sub": "for the arbitrator to decide · all contentions left open", "icon": "scale", "tone": "ok", "at": A("c08", "decide")}])
cue(type="cite", t0=A("c08", "salson"), t1=E("c08") + 0.05, at=A("c08", "salson"), tag="SUPREME COURT · FOLLOWED",
    cases=[{"name": "Salson Liquors Pvt. Ltd. v. United Spirits Ltd.", "cite": "Order dated 20.02.2026 · SLP (C) No. 16022 of 2025"}])

# ── 5 · the result ───────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="verdicts", t0=S("c09"), t1=A("c09", "interim") - 0.05,
    rows=[{"text": "Section 11 petition allowed · no costs", "ok": True, "at": A("c09", "allowed")},
          {"text": "Sole Arbitrator: Justice R. Suresh Kumar, a retired judge of the Madras High Court", "ok": True, "at": A("c09", "retired")},
          {"text": "Seat and venue Chennai · Madras High Court Arbitration Centre · fees shared equally", "ok": True, "at": A("c09", "appointed")}])
cue(type="list", t0=A("c09", "interim") - 0.05, t1=E("c09") + 0.05, head="Before the arbitrator", head_at=A("c09", "interim"),
    items=[{"n": 1, "text": "Interim order in O.A. 528/2025 continues", "at": A("c09", "continues")},
           {"n": 2, "text": "Section 17 application within 30 days of reference", "at": A("c09", "section")},
           {"n": 3, "text": "The respondent may object under Section 16", "at": A("c09", "ruling")}])
cue(type="point", t0=S("c10"), t1=E("c10") + 0.05, text="Like · Share · Subscribe · lawworld.ai", icon="check", accent=True, at=A("c10", "like"))
