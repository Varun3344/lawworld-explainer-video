# G. Sanil Kumar v. Sujith & Anr., Crl.A. No. 2002 of 2024, 2026:KER:78185 (High Court of Kerala, A. Badharudeen J.; heard and
# delivered 08.10.2026, CR): panel cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND). Concept format as set krm.
# Facts from the judgment (paras): appeal by the complainant against the acquittal by the JFCM, Varkala, ST No. 2754 of 2015, judgment
# 24.09.2024 (cause title, 1); counsel for the accused appointed as State Brief (2); the accused borrowed Rs 9,30,230 through various
# transactions / bank transfers; Ext.P1 cheque for Rs 9,30,230 dated 06.07.2015; "funds insufficient"; legal notice, no payment;
# s.138 NI Act, 1881 (4, 10, 11); the Magistrate found the transaction, the cheque and the failure to pay for the complainant, but on DW2
# and Ext.D5 (the accused's statement of accounts) the money went out in instalments in 2011-2012: time-barred debt, acquittal on that
# sole reason (6, 12); 2011-2012 not disputed by the complainant (7, 12); Ramakrishnan v. Parthasaradhy, 2003 (2) KLT 613 (DB), para 25:
# "When a person issues a cheque, he acknowledges his liability to pay" (7); State Brief: a time-barred debt is not legally enforceable
# on first principle, the position needs reconsideration (8); held: a cheque for a time-barred debt "is akin to revival of the debt"
# by acknowledging it, the debt ceases to be time-barred; issuing it "is not legally prohibited"; it "does not make a prosecution under
# Section 138 ... impermissible"; the Magistrate went wrong (13); acquittal set aside, convicted under s.138 (14); simple imprisonment
# till rising of the Court, fine Rs 14,00,000, default six months, Rs 13,50,000 compensation u/s 357(1)(b) CrPC, Rs 50,000 cost (15);
# appear before the JFCM, Varkala at 11 am on 31.10.2026 (16). The bench card uses the official portrait.
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen, as tej)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
STING = {"kicker": "KERALA HIGH COURT · JUDGMENT EXPLAINED", "title": "Section 138 and a time-barred debt", "sub": "G. Sanil Kumar v. Sujith · 2026:KER:78185"}
ENDCARD = {"title": "Section 138 and a time-barred debt", "line": "A time-barred debt alone does not bar a Section 138 case", "sub": "LawWorld: legal research for advocates"}

# ── 1 · a time-barred debt? ──────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "cheque"), text="A cheque for a time-barred debt bounces: can the drawer still be convicted?", hl="still be convicted?")
cue(type="bench", t0=S("c02"), t1=E("c02") + 0.05, tag="High Court of Kerala · 8 October 2026",
    judges=[{"name": "Justice A. Badharudeen", "photo": "../brand/judges/a_badharudeen.jpg", "at": A("c02", "honourable")}])

# ── 2 · the cheque ───────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=A("c03", "complainant"), t1=E("c04") + 0.05, at=A("c03", "complainant"), tag="HIGH COURT OF KERALA · 08.10.2026",
    cases=[{"name": "G. Sanil Kumar v. Sujith", "cite": "2026:KER:78185 · Crl.A. No. 2002 of 2024"}])
cue(type="flow", t0=S("c03"), t1=E("c03") + 0.05, head="The cheque", head_at=S("c03") + 0.05,
    steps=[{"label": "Loan of ₹9,30,230", "sub": "by bank transfers, to the accused", "icon": "arrow-right", "at": A("c03", "given")},
           {"label": "Cheque for ₹9,30,230", "sub": "Ext.P1 · dated 6 Jul 2015", "icon": "file-text", "at": A("c03", "cheque")},
           {"label": "Dishonoured", "sub": "“funds insufficient” · legal notice, no payment", "icon": "x", "tone": "stop", "at": A("c03", "bounced")}])

# ── 3 · in the trial court ───────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c04"), t1=E("c04") + 0.05, head="Varkala Magistrate · 24 Sep 2024", head_at=S("c04") + 0.05,
    steps=[{"label": "Loan and cheque proved", "sub": "transaction, cheque, unpaid demand: for the complainant", "icon": "check", "tone": "ok", "at": A("c04", "accepted")},
           {"label": "Money lent in 2011–2012", "sub": "in instalments · Ext.D5, the accused's own statement of accounts", "icon": "calendar", "at": A("c04", "lent")},
           {"label": "Time-barred debt: acquitted", "sub": "on that sole reason · ST No. 2754 of 2015", "icon": "x", "tone": "stop", "at": A("c04", "found")}])

# ── 4 · the arguments ────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c05"), t1=A("c05", "when") - 0.05, text="Complainant: lending in 2011–2012 not disputed", icon="user", at=A("c05", "accepted"))
cue(type="point", t0=A("c05", "when"), t1=E("c05") + 0.05, text="“When a person issues a cheque, he acknowledges his liability to pay”", icon="scale", accent=True, at=A("c05", "when"))
cue(type="cite", t0=A("c05", "division"), t1=E("c05") + 0.05, at=A("c05", "division"), tag="DIVISION BENCH · CITED IN APPEAL",
    cases=[{"name": "Ramakrishnan v. Parthasaradhy", "cite": "2003 (2) KLT 613 · para 25"}])
cue(type="list", t0=S("c06"), t1=E("c06") + 0.05, head="Counsel for the accused (State Brief)", head_at=S("c06") + 0.05,
    items=[{"n": 1, "text": "A time-barred debt is not legally enforceable", "at": A("c06", "time")},
           {"n": 2, "text": "The legal position needs reconsideration", "at": A("c06", "position")}])

# ── 5 · what the court held ──────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c07"), t1=E("c07") + 0.05, head="A cheque for a time-barred debt", head_at=S("c07") + 0.05,
    steps=[{"label": "Acknowledges the debt", "sub": "and the liability on it", "icon": "file-check", "at": A("c07", "acknowledges")},
           {"label": "Akin to reviving it", "sub": "“akin to revival of the debt”", "icon": "arrow-right", "at": A("c07", "akin")},
           {"label": "No longer time-barred", "sub": "the debt ceases to be time-barred", "icon": "check", "tone": "ok", "at": A("c07", "ceases")}])
cue(type="point", t0=S("c08"), t1=A("c08", "that") - 0.05, text="Issuing a cheque for a time-barred debt: “not legally prohibited”", icon="check", accent=True, at=A("c08", "issuing"))
cue(type="section", t0=A("c08", "that"), t1=E("c08") + 0.05, at=A("c08", "that"), act="NI ACT, 1881", num="138", title="Dishonour of cheque",
    points=[{"text": "Cheque given for a time-barred debt", "at": A("c08", "section")},
            {"text": "No bar to prosecution on that ground alone", "at": A("c08", "impermissible")}])

# ── 6 · the verdict ──────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="verdicts", t0=S("c09"), t1=A("c09", "sentence") - 0.05,
    rows=[{"text": "Acquittal by the Varkala Magistrate", "ok": False, "at": A("c09", "acquittal"), "strike_at": A("c09", "aside")},
          {"text": "Convicted under Section 138, NI Act", "ok": True, "at": A("c09", "convicted")}])
cue(type="counters", t0=A("c09", "sentence"), t1=E("c09") + 0.05, head="The sentence", head_at=A("c09", "sentence"),
    items=[{"value": 14, "unit": "LAKH", "label": "Fine, in rupees", "sub": "₹13.5 lakh to the complainant · § 357(1)(b) CrPC", "at": A("c09", "fine")}],
    note={"text": "Simple imprisonment till the Court rises · 6 months in default", "icon": "calendar", "at": A("c09", "simple")})
cue(type="point", t0=S("c10"), t1=E("c10") + 0.05, text="Like · Share · Subscribe · lawworld.ai", icon="check", accent=True, at=A("c10", "like"))
