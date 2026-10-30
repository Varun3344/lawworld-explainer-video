# Shreeram Builders v. Upendra Kantilal Thanawala and others, 2026 INSC 1176, Civil Appeal Nos. 9817-9818 of 2024 (Sanjay Kumar J.
# wrote it, Sanjeev Sachdeva J.; decided 29.10.2026, REPORTABLE): panel cues, run by split/build_course_plan.py (helpers: at S E cue fx
# have r3 PEND). Concept format as sets gpk / rcc / nkp.
# Facts from the judgment (paras): 'Agreement for Development' 06.08.2003, five Thanawalas (the owners) and the builder firm with its
# three partners (2, 15); Lands A, B, C in Village Panchpakhadi, Taluka & District Thane (8); the owners' undivided 2/9th share (15);
# Clause 1: the right to develop the 2/9th share (17); Clause 3: Rs 915 per sq ft on 25,000 sq ft of FSI = Rs 2,28,75,000 (17);
# Clause 5: Rs 55,00,000 earnest; Clause 6: ten instalments of Rs 17,37,500 (18, 19); Clauses 7, 63, 64: payment on the due dates and
# "time shall be the essence" (19, 29); Clause 37: no conveyance "till payment of all the instalments and amounts due" (27); bungalow, gardens, Room No. 1 in Chawl No. 1 excluded (16, 28); instalments 1-6 paid 2 to
# 50 days late, accepted without protest; 7-9 offered late, cheques returned 16.04.2008; the 10th never tendered; the balance "was not
# completed by 01.03.2008" (55, 56); termination by legal notice 09.04.2008 (2); majority award 10.12.2011, one arbitrator dissented
# (3): termination illegal, specific performance on depositing Rs 10,91,30,164 within 3 months (3); six times the agreed rate, Rs 5,490
# per sq ft (38); alternative damages Rs 23,21,19,892 if specific performance were reversed (38); the award left out only the owners'
# 2/9th of the excluded property: the other 7/9th pulled into the conveyance, its owners not before the tribunal (58); Principal
# District Judge, Thane, 25.01.2020: award upheld "in its entirety"; Bombay High Court 05.03.2024: award set aside (6); unamended s.34
# applies, both s.34 applications filed long before 23.10.2015 (44); s.28(3): decide by the terms of the contract and the trade
# usages (52); against the terms of the contract = patently illegal (R.S. Sharma, OPG Power) (47, 50); "the nomenclature of a document
# would not be decisive as to its nature" (14); label not essential, the terms stipulating sequential performance mattered (52); "the
# correct finding by the High Court that Section 28(3) ... stood violated by the rewriting of the contract" (61); "completely supplanted
# them with new terms, as per their own fancies" (61); "no grounds to uphold the majority award"; Clause 54 (repay without interest)
# not followed, money retained; Article 142: refund with simple interest @ 9% p.a. from each payment till the refund; the builder's
# deposits returned with interest accrued, if any; appeals disposed of; own costs (62). No section card: it would print "§". The
# Court's general stamp-duty remark (14) is on no card. Official portraits on the bench card.
# Fact-check 30-10-2026: Act named in full (the "Arbitration Act 1996" is the UK statute); "patently illegal" shown as the recited
# precedent (47, 50), not the Court's own label; the supplanting was by the two majority arbitrators (61), not the dissenter; the award
# "not upheld" (62), the Court's own words, not "stays set aside".
# 30-10 QA: list lines shortened to <= 52 chars (9:16 list items do not wrap; longer lines ran off the frame)
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen, as gpk)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
STING = {"kicker": "SUPREME COURT · JUDGMENT EXPLAINED", "title": "An award that rewrote the deal", "sub": "Shreeram Builders v. Thanawala · 2026 INSC 1176"}
ENDCARD = {"title": "An award that rewrote the deal", "line": "Section 28(3): arbitrators cannot rewrite the contract", "sub": "LawWorld: legal research for advocates"}

# ── 1 · rewrite the deal? ────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "arbitrators"), text="Can arbitrators order specific performance at six times the agreed rate, on terms the contract never contained?", hl="on terms the contract never contained?")
cue(type="bench", t0=S("c02"), t1=E("c02") + 0.05, tag="Supreme Court of India · 29 October 2026",
    judges=[{"name": "Justice Sanjay Kumar", "photo": "../brand/judges/sanjay_kumar.jpg", "at": A("c02", "honourable")},
            {"name": "Justice Sanjeev Sachdeva", "photo": "../brand/judges/sanjeev_sachdeva.jpg", "at": A("c02", "honourable", 2)}])

# ── 2 · the agreement ────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=A("c03", "landowners"), t1=E("c04") + 0.05, at=A("c03", "landowners"), tag="SUPREME COURT OF INDIA · 29.10.2026",
    cases=[{"name": "Shreeram Builders v. Upendra Kantilal Thanawala & Ors.", "cite": "2026 INSC 1176 · Civil Appeal Nos. 9817-9818 of 2024"}])
cue(type="flow", t0=S("c03"), t1=E("c03") + 0.05, head="Agreement for Development · 6 Aug 2003", head_at=S("c03") + 0.05,
    steps=[{"label": "The builder: the right to develop", "sub": "a firm and its three partners · Clause 1", "icon": "user", "at": A("c03", "builder")},
           {"label": "The owners' 2/9th undivided share", "sub": "Village Panchpakhadi, Thane · the bungalow excluded", "icon": "landmark", "at": A("c03", "share")},
           {"label": "₹915 per sq ft of FSI", "sub": "on 25,000 sq ft: ₹2,28,75,000 · ₹55 lakh earnest", "icon": "file-text", "at": A("c03", "nine")}])
cue(type="list", t0=S("c04"), t1=A("c04", "balance") - 0.05, head="The agreed terms", head_at=A("c04", "time"),
    items=[{"n": 1, "text": "Clauses 7, 63, 64: “time shall be the essence”", "at": A("c04", "essence")},
           {"n": 2, "text": "Clause 37: no conveyance till full payment", "at": A("c04", "conveyance")}])
cue(type="timeline", t0=A("c04", "balance") - 0.05, t1=E("c04") + 0.05,
    nodes=[{"label": "INSTALMENTS 1–6", "value": "2–50 days late", "sub": "accepted without protest", "at": A("c04", "balance")},
           {"label": "FULL PAYMENT DUE", "value": "1 Mar 2008", "sub": "balance not completed · 10th never tendered", "tone": "red", "at": A("c04", "march")},
           {"label": "TERMINATION", "value": "9 Apr 2008", "sub": "the owners' legal notice", "at": A("c04", "terminated")}])

# ── 3 · the award ────────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c05"), t1=E("c05") + 0.05, head="The majority award · 10 Dec 2011", head_at=S("c05") + 0.05,
    steps=[{"label": "Termination “illegal”", "sub": "2 of 3 arbitrators · one dissented", "icon": "scale", "at": A("c05", "termination")},
           {"label": "Specific performance", "sub": "a sale deed for the owners' 2/9th share", "icon": "file-check", "at": A("c05", "specific")},
           {"label": "Rate × 6: ₹915 → ₹5,490 per sq ft", "sub": "deposit ₹10,91,30,164 within 3 months", "icon": "file-text", "at": A("c05", "six")}])
cue(type="list", t0=S("c06"), t1=A("c06", "judge") - 0.05, head="Beyond the contract", head_at=A("c06", "also"),
    items=[{"n": 1, "text": "Excluded property: the other owners' 7/9th taken in", "at": A("c06", "excluded")},
           {"n": 2, "text": "Alternative damages of ₹23,21,19,892", "at": A("c06", "fixed")}])
cue(type="timeline", t0=A("c06", "judge") - 0.05, t1=E("c06") + 0.05,
    nodes=[{"label": "DISTRICT JUDGE, THANE", "value": "25 Jan 2020", "sub": "Section 34 · award upheld in its entirety", "at": A("c06", "upheld")},
           {"label": "BOMBAY HIGH COURT", "value": "5 Mar 2024", "sub": "Section 37 · award set aside", "tone": "red", "at": A("c06", "bombay")}])

# ── 4 · what the court held ──────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c07"), t1=A("c07", "the", 3) - 0.05, text="Unamended Section 34 applies: both Section 34 applications were filed long before 23.10.2015", icon="calendar", at=A("c07", "testing"))
cue(type="flow", t0=A("c07", "the", 3) - 0.05, t1=E("c07") + 0.05, head="Section 28(3), Arbitration & Conciliation Act", head_at=A("c07", "supreme"),
    steps=[{"label": "Decide by the terms of the contract", "sub": "and the trade usages applicable to the transaction", "icon": "file-text", "at": A("c07", "held")},
           {"label": "Rewriting the contract violates it", "sub": "“the correct finding by the High Court”", "icon": "x", "tone": "stop", "at": A("c07", "rewriting")},
           {"label": "Against the contract's terms: patently illegal", "sub": "precedent: DDA v. R.S. Sharma · OPG Power Generation", "icon": "scale", "at": A("c07", "section", 2)}])
cue(type="notequal", t0=S("c08"), t1=A("c08", "and") - 0.05, left="The document's label", right="its nature", at=A("c08", "development"),
    left_at=A("c08", "development"), sub="Its terms decide, not the label", sub_at=A("c08", "terms"))
cue(type="point", t0=A("c08", "and") - 0.05, t1=E("c08") + 0.05, text="The two majority arbitrators “completely supplanted” the express terms “with new terms, as per their own fancies”", icon="scale", accent=True, at=A("c08", "and"))

# ── 5 · the orders ───────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c09"), t1=E("c09") + 0.05, head="The orders", head_at=S("c09") + 0.05,
    steps=[{"label": "Majority award not upheld", "sub": "“no grounds to uphold the majority award”", "icon": "x", "tone": "stop", "at": A("c09", "award")},
           {"label": "The owners kept the money", "sub": "Clause 54: repay the consideration, without interest", "icon": "file-text", "at": A("c09", "owners")},
           {"label": "Refund + 9% simple interest a year", "sub": "Article 142 · from each payment till the refund", "icon": "check", "tone": "ok", "at": A("c09", "refund")}],
    note={"text": "The builder's court deposits returned, with interest accrued, if any · appeals disposed of", "icon": "info", "at": A("c09", "interest")})
cue(type="point", t0=S("c10"), t1=E("c10") + 0.05, text="Like · Share · Subscribe · lawworld.ai", icon="check", accent=True, at=A("c10", "like"))
