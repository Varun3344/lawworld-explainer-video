# Dr. I. A. Khan v. State & Anr., CRL.REV.P. 122/2020 (High Court of Delhi, Sanjeev Narula J.; pronounced 27.10.2026): panel cues, run
# by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND). Concept format as sets ara / krm.
# Facts from the judgment (paras): trial court conviction under s.138 NI Act 10.07.2019, sentence 19.07.2019: ten months' SI, Rs 42 lakh
# compensation, two months' SI in default; ASJ Shahdara dismissed Crl. Appeal 27/2019 on 30.01.2020 (1); collaboration agreement
# 13.09.2013, property No. 162, Vikram Enclave Extension, Village Pasonda, Ghaziabad, 200 sq. yds: the complainant to build ground, upper
# ground, first and second floors and get the first and second floors with roof rights over the second (2); per the complainant,
# settlement of 01.02.2016 (Ex. CW-1/Q): claim to the second floor and its roof rights given up for Rs 30 lakh, three cheques (3); three
# SBI cheques of Rs 10 lakh each: 315386 and 315388 returned for insufficiency of funds, 315387 with an objection on alteration in the
# amount (4); pleas: security cheques, to be returned on completion (5); 315387 void under s.87 (6); signatures and delivery admitted
# (10); ss.118(a), 139 presumptions (9); CW-2 attesting witness (12); presumptions not rebutted (15, 25); words "Ten Lakh only", figures
# "₹100,0000/-", the entries correspond; the bank's endorsement does not by itself establish an unauthorised material alteration
# rendering the cheque void under s.87 (22); Bir Singh v. Mukesh Kumar (2019) 4 SCC 197: completing a signed cheque is no alteration
# where no existing entry is changed (19); conviction, Rs 42 lakh compensation and the default sentence affirmed; sentence cut to six
# months' SI: property-development arrangement ending in a settlement, family circumstances, Rs 21 lakh deposited (29, 30). The bench
# card uses the official portrait.
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen, as tej)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
STING = {"kicker": "DELHI HIGH COURT · JUDGMENT EXPLAINED", "title": "Section 87 and the bank's “alteration” remark", "sub": "Dr. I.A. Khan v. State & Anr. · CRL.REV.P. 122/2020"}
ENDCARD = {"title": "Section 87 and the bank's “alteration” remark", "line": "The bank's remark alone proves no material alteration", "sub": "LawWorld: legal research for advocates"}

# ── 1 · altered cheque? ──────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "bank"), text="Cheque returned for “alteration in amount”: is it void under Section 87?", hl="void under Section 87?")
cue(type="bench", t0=S("c02"), t1=E("c02") + 0.05, tag="High Court of Delhi · 27 October 2026",
    judges=[{"name": "Justice Sanjeev Narula", "photo": "../brand/judges/sanjeev_narula.jpg", "at": A("c02", "honourable")}])

# ── 2 · the deal ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=A("c03", "collaboration"), t1=E("c04") + 0.05, at=A("c03", "collaboration"), tag="HIGH COURT OF DELHI · 27.10.2026",
    cases=[{"name": "Dr. I.A. Khan v. State & Anr.", "cite": "CRL.REV.P. 122/2020"}])
cue(type="flow", t0=S("c03"), t1=E("c03") + 0.05, head="The collaboration", head_at=S("c03") + 0.05,
    steps=[{"label": "Agreement · 13 Sep 2013", "sub": "collaboration to develop the property", "icon": "file-text", "at": A("c03", "collaboration")},
           {"label": "The complainant builds", "sub": "on the petitioner's 200 sq. yd property, Ghaziabad", "icon": "user", "at": A("c03", "develop")},
           {"label": "His share", "sub": "first and second floors, roof rights over the second", "icon": "landmark", "at": A("c03", "first")}])
cue(type="flow", t0=S("c04"), t1=E("c04") + 0.05, head="The settlement", head_at=S("c04") + 0.05,
    steps=[{"label": "Disputes", "sub": "over the construction and their rights", "icon": "x", "tone": "stop", "at": A("c04", "disputes")},
           {"label": "Settlement · 1 Feb 2016", "sub": "the complainant's case · handwritten Ex. CW-1/Q", "icon": "file-text", "at": A("c04", "settled")},
           {"label": "Second floor and roof rights given up", "sub": "for ₹30 lakh, in three cheques", "icon": "arrow-right", "at": A("c04", "gave")}])
cue(type="flow", t0=S("c05"), t1=E("c05") + 0.05, head="The cheques", head_at=S("c05") + 0.05,
    steps=[{"label": "Three SBI cheques · ₹10 lakh each", "sub": "Nos. 315386, 315387, 315388 · March 2016", "icon": "file-text", "at": A("c05", "three")},
           {"label": "Two: insufficient funds", "sub": "Nos. 315386 and 315388", "icon": "x", "tone": "stop", "at": A("c05", "two")},
           {"label": "The third: “alteration in amount”", "sub": "No. 315387 · returned for rectification", "icon": "x", "tone": "stop", "at": A("c05", "third")}])

# ── 3 · the defence ──────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c06"), t1=A("c06", "revision") - 0.05, head="The courts below", head_at=S("c06") + 0.05,
    steps=[{"label": "Trial court: convicted", "sub": "Section 138 NI Act · 10 Jul 2019", "icon": "scale", "at": A("c06", "convicted")},
           {"label": "10 months' SI · ₹42 lakh compensation", "sub": "2 months' SI in default", "icon": "file-text", "at": A("c06", "section")},
           {"label": "Appeal dismissed", "sub": "ASJ, Shahdara · 30 Jan 2020", "icon": "x", "tone": "stop", "at": A("c06", "appeal")}])
cue(type="list", t0=A("c06", "revision"), t1=E("c06") + 0.05, head="His pleas in revision", head_at=A("c06", "revision"),
    items=[{"n": 1, "text": "Security cheques, to be returned on completion of construction", "at": A("c06", "security")},
           {"n": 2, "text": "Cheque 315387 void under Section 87: material alteration", "at": A("c06", "third")}])

# ── 4 · what the court held ──────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c07"), t1=E("c07") + 0.05, at=A("c07", "signatures"), act="NI ACT, 1881", num="139", title="Presumption in favour of holder",
    points=[{"text": "Signatures and delivery: admitted", "at": A("c07", "admitted")},
            {"text": "Presumed: for a legally enforceable debt or liability", "at": A("c07", "presumption")}],
    note={"text": "Security plea: presumption not rebutted · attesting witness CW-2 backed the settlement", "icon": "x", "at": A("c07", "rebut")})
cue(type="point", t0=S("c08"), t1=A("c08", "no") - 0.05, text="In words “Ten Lakh only”, in figures ₹100,0000/-: the two correspond", icon="file-check", at=A("c08", "third"))
cue(type="verdicts", t0=A("c08", "no"), t1=E("c08") + 0.05,
    rows=[{"text": "A change to an existing entry proved?", "ok": False, "at": A("c08", "no"), "strike_at": A("c08", "proved")},
          {"text": "The bank's remark alone: not void under Section 87", "ok": True, "at": A("c08", "bank")}])
cue(type="cite", t0=A("c08", "existing"), t1=E("c08") + 0.05, at=A("c08", "existing"), tag="SUPREME COURT · FOLLOWED",
    cases=[{"name": "Bir Singh v. Mukesh Kumar", "cite": "(2019) 4 SCC 197 · completing a signed cheque is no alteration"}])

# ── 5 · the verdict ──────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="verdicts", t0=S("c09"), t1=A("c09", "but") - 0.05,
    rows=[{"text": "Conviction under Section 138: upheld", "ok": True, "at": A("c09", "conviction")},
          {"text": "₹42 lakh compensation: upheld", "ok": True, "at": A("c09", "compensation")}])
cue(type="flow", t0=A("c09", "but"), t1=E("c09") + 0.05, head="The sentence", head_at=A("c09", "but"),
    steps=[{"label": "A property-development deal", "sub": "that ended in a settlement", "icon": "landmark", "at": A("c09", "property")},
           {"label": "₹21 lakh deposited", "sub": "during the appeal and the revision", "icon": "file-check", "at": A("c09", "deposits")},
           {"label": "10 → 6 months' simple imprisonment", "sub": "the 2-month default term unchanged", "icon": "scale", "tone": "ok", "at": A("c09", "sentence")}])
cue(type="point", t0=S("c10"), t1=E("c10") + 0.05, text="Like · Share · Subscribe · lawworld.ai", icon="check", accent=True, at=A("c10", "like"))
