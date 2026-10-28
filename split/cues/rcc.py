# M/s Royal Construction Company Pvt. Ltd. v. M/s National Projects Construction Corporation, 2026 INSC 1167 (Vikram Nath J. wrote it,
# Sandeep Mehta J., Aparesh Kumar Singh J.; decided 28.10.2026, REPORTABLE): panel cues, run by split/build_course_plan.py (helpers: at S
# E cue fx have r3 PEND). Concept format as sets tex / san.
# Facts from the judgment (paras): Civil Appeal @ SLP (C) No. 14005 of 2026 against the Delhi High Court's interim order of 16.02.2026 in
# Execution First Appeal (OS) No. 17 of 2018 (3); with M.A. @ Diary No. 48152 of 2026 in Civil Appeal No. 1991 of 2019 (cover, 18-19);
# the appellant is the award-holder, the respondent the award-debtor; internationally seated arbitration; award dated 10.08.2002 in
# the appellant's favour, amounts in a foreign currency (4.1); SC judgment 24.02.2015: minimal judicial intervention, Sections 34 and 37
# of the 1996 Act, the award's directions restored (4.2); Single Judge 26.07.2017: liability may be discharged in rupees at the exchange
# rate of the 1982 agreement date (4.3); Division Bench 17.12.2019: that order set aside, question certified under Articles 134-A and
# 133(1)(a): the relevant date for conversion into Indian rupees (4.4); SC 10.10.2023: answered in the negative, no occasion to fix a
# conversion date (4.5); payment to be made in foreign currency (8); the respondent contended the principal was already paid in Indian
# rupees in 2009 under High Court orders; 16.02.2026: liberty to seek clarification from the SC (3, 4.6); held: the Division Bench "has
# fallen into error" on the scope of the 2023 ruling (7); that jurisdiction was confined to answering the certified question (7, 9);
# the Court cannot be called upon "in the guise of seeking clarification" to assume a supervisory role over the continuing execution;
# the court seized of the execution and the appellate court over its orders decide (9); the scope "stood exhausted" (10); more than
# 24 years after the award the parties "continue to litigate over its enforcement" (11); the Law Commission asked to study the
# enforcement and execution of arbitral awards: disclosure of the award-debtor's assets, repetitive or dilatory objections, time taken,
# domestic and foreign awards (13, 14); appeal disposed of (15); copy to the Chairman of the Law Commission (16); the M.A. (by the
# award-debtor, to modify the 10.10.2023 judgment because its rupee deposits were withdrawn by the award-holder in 2009) dismissed;
# liberty to raise adjustment or set-off of those amounts before the executing court (19-22). The bench card uses the official portraits.
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen, as tex)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
STING = {"kicker": "SUPREME COURT · JUDGMENT EXPLAINED", "title": "Execution and a “clarification”", "sub": "Royal Construction v. NPCC · 2026 INSC 1167"}
ENDCARD = {"title": "Execution and a “clarification”", "line": "Questions in execution are for the executing court", "sub": "LawWorld: legal research for advocates"}

# ── 1 · a clarification? ─────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "twenty"), text="24 years after an arbitral award, execution is still pending: can the Supreme Court be asked to clarify?", hl="asked to clarify?")
cue(type="bench", t0=S("c02"), t1=E("c02") + 0.05, tag="Supreme Court of India · 28 October 2026",
    judges=[{"name": "Justice Vikram Nath", "photo": "../brand/judges/vikram_nath.jpg", "at": A("c02", "honourable")},
            {"name": "Justice Sandeep Mehta", "photo": "../brand/judges/sandeep_mehta.jpg", "at": A("c02", "honourable", 2)},
            {"name": "Justice Aparesh Kumar Singh", "photo": "../brand/judges/aparesh_kumar_singh.jpg", "at": A("c02", "honourable", 3)}])

# ── 2 · the award ────────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=A("c03", "royal"), t1=E("c04") + 0.05, at=A("c03", "royal"), tag="SUPREME COURT OF INDIA · 28.10.2026",
    cases=[{"name": "Royal Construction Co. v. National Projects Construction Corp.", "cite": "2026 INSC 1167 · C.A. @ SLP (C) No. 14005 of 2026"}])
cue(type="flow", t0=S("c03"), t1=E("c03") + 0.05, head="The award", head_at=S("c03") + 0.05,
    steps=[{"label": "Internationally seated arbitration", "sub": "award-holder: Royal Construction Company Pvt. Ltd.", "icon": "scale", "at": A("c03", "royal")},
           {"label": "Award · 10 Aug 2002", "sub": "against National Projects Construction Corporation · in a foreign currency", "icon": "file-text", "at": A("c03", "national")},
           {"label": "Supreme Court · 24 Feb 2015", "sub": "the award's directions restored · minimal judicial intervention", "icon": "check", "tone": "ok", "at": A("c03", "restored")}])
cue(type="flow", t0=S("c04"), t1=E("c04") + 0.05, head="The certified question", head_at=S("c04") + 0.05,
    steps=[{"label": "Delhi High Court · 17 Dec 2019", "sub": "Division Bench · Articles 134-A and 133(1)(a)", "icon": "landmark", "at": A("c04", "execution")},
           {"label": "The relevant date to convert into rupees?", "sub": "Single Judge, 2017: the 1982 rate · set aside", "icon": "search", "at": A("c04", "certified")},
           {"label": "Supreme Court · 10 Oct 2023: no such date", "sub": "payment to be made in foreign currency", "icon": "check", "tone": "ok", "at": A("c04", "conversion")}])

# ── 3 · back in execution ────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c05"), t1=E("c05") + 0.05, head="Back in execution", head_at=S("c05") + 0.05,
    steps=[{"label": "Award-debtor's plea: principal paid", "sub": "in Indian rupees, in 2009, under the High Court's orders", "icon": "user", "at": A("c05", "principal")},
           {"label": "Delhi HC Division Bench · 16 Feb 2026", "sub": "interim order: the parties may seek clarification from the Supreme Court", "icon": "landmark", "at": A("c05", "high")},
           {"label": "Royal Construction appeals", "sub": "C.A. @ SLP (C) No. 14005 of 2026", "icon": "arrow-right", "at": A("c05", "supreme")}])

# ── 4 · what the court held ──────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c06"), t1=A("c06", "the", 3), text="28 Oct 2026: the Division Bench “has fallen into error”", icon="x", at=A("c06", "twenty"))
cue(type="list", t0=A("c06", "the", 3), t1=E("c06") + 0.05, head="The 2023 ruling · C.A. No. 1991 of 2019", head_at=A("c06", "twenty", 2),
    items=[{"n": 1, "text": "Confined to answering the certified question", "at": A("c06", "answered")},
           {"n": 2, "text": "Once answered, its scope “stood exhausted”", "at": A("c06", "scope")}])
cue(type="point", t0=S("c07"), t1=A("c07", "the", 3), text="Not “in the guise of seeking clarification”: no supervisory role over execution", icon="scale", accent=True, at=A("c07", "cannot"))
cue(type="list", t0=A("c07", "the", 3), t1=E("c07") + 0.05, head="Who decides questions in execution", head_at=A("c07", "executing"),
    items=[{"n": 1, "text": "The court seized of the execution", "at": A("c07", "must")},
           {"n": 2, "text": "and the appellate court over its orders", "at": A("c07", "decide")}])

# ── 5 · the orders ───────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="verdicts", t0=S("c08"), t1=E("c08") + 0.05,
    rows=[{"text": "Award-debtor's application: modify the 10 Oct 2023 judgment", "ok": False, "at": A("c08", "application"), "strike_at": A("c08", "dismissed")},
          {"text": "Liberty: adjustment or set-off of its rupee deposits, before the executing court", "ok": True, "at": A("c08", "raise")}])
cue(type="cite", t0=A("c08", "application"), t1=E("c08") + 0.05, at=A("c08", "application"), tag="SUPREME COURT · M.A. DISMISSED",
    cases=[{"name": "M.A. @ Diary No. 48152 of 2026", "cite": "in Civil Appeal No. 1991 of 2019 (judgment of 10.10.2023)"}])
cue(type="counters", t0=S("c09"), t1=A("c09", "court"),
    items=[{"value": 24, "unit": "YEARS+", "label": "Since the award of 10 Aug 2002", "sub": "the parties “continue to litigate over its enforcement”", "at": A("c09", "twenty")}])
cue(type="list", t0=A("c09", "court"), t1=A("c09", "appeal"), head="Law Commission asked to study", head_at=A("c09", "law"),
    items=[{"n": 1, "text": "Disclosure of the award-debtor's assets", "at": A("c09", "study")},
           {"n": 2, "text": "Repetitive or dilatory objections · time taken", "at": A("c09", "arbitral")},
           {"n": 3, "text": "Domestic and foreign awards: one framework or two?", "at": A("c09", "enforced")}])
cue(type="point", t0=A("c09", "appeal"), t1=E("c09") + 0.05, text="Appeal disposed of · judgment sent to the Law Commission's Chairman", icon="check", accent=True, at=A("c09", "appeal"))
cue(type="point", t0=S("c10"), t1=E("c10") + 0.05, text="Like · Share · Subscribe · lawworld.ai", icon="check", accent=True, at=A("c10", "like"))
