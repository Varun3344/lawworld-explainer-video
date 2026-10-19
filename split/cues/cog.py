# Cognizable and Non-Cognizable Offences (BNSS): panel cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND).
# Storyboard: ~/Downloads/Cognizable_and_Non_Cognizable_Offences_BNSS_Storyboard.pdf. Fact-check 19-10-2026: theft of the ₹25,000 phone
# is BNS 303(2), cognizable (the value matters: theft under ₹5,000 has a non-cognizable row); the "notice is the rule, arrest the
# exception" line is the Supreme Court's (Satender Kumar Antil v. CBI, 2026 INSC 115, order of 15.01.2026, paras 26, 31, 33);
# BNS 117(2) grievous hurt = cognizable + bailable (the "cognizable can be bailable" example).
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

# ── 1 · two reports ──────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="compare", t0=S("c01"), t1=A("c02", "reason") - 0.05, head="Two reports, one police station", head_at=S("c01") + 0.1,
    cols=[{"title": "Ravi", "icon": "smartphone", "at": A("c01", "ravi")}, {"title": "Meena", "icon": "user-round", "at": A("c01", "meena")}],
    rows=[{"cells": ["A stolen phone", "An ordinary hurt"], "cells_at": [A("c01", "stolen"), A("c01", "ordinary")]},
          {"cells": ["An offence", "An offence"], "cells_at": [A("c02", "both"), A("c02", "both") + 0.15]}],
    verdict={"text": "…but what follows may be very different", "icon": "triangle-alert", "at": A("c02", "but")})
cue(type="splitcard", t0=A("c02", "reason"), t1=E("c02") + 0.05,
    left={"title": "COGNIZABLE", "text": "Ravi's theft", "icon": "smartphone", "at": A("c02", "cognizable")},
    right={"title": "NON-COGNIZABLE", "text": "Meena's hurt", "icon": "user-round", "at": A("c02", "non")})
cue(type="point", t0=S("c03"), t1=E("c03") + 0.05, text="Wrong label → wrong view of police powers", icon="triangle-alert", accent=True, at=A("c03", "confuse"))

# ── 2 · the definitions ──────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="kicker", t0=S("c04"), t1=E("c07") + 0.05, at=S("c04") + 0.05, text="WHAT THE TERMS MEAN")
cue(type="section", t0=S("c04") + 0.1, t1=E("c05") + 0.05, at=A("c04", "defines"), act="BNSS", num="2(1)(g)", title="Cognizable offence",
    points=[{"text": "Police may arrest without a warrant, subject to law", "at": A("c05", "police")}],
    note={"text": "Warrant = a court's written authority to arrest", "icon": "scroll-text", "at": A("c05", "warrant", 2)})
cue(type="section", t0=S("c06"), t1=E("c06") + 0.05, at=A("c06", "clause"), act="BNSS", num="2(1)(o)", title="Non-cognizable offence",
    points=[{"text": "No power to arrest without a warrant merely because it is alleged", "tone": "no", "at": A("c06", "police")}])
cue(type="flow", t0=S("c07"), t1=E("c07") + 0.05, head="Where the label comes from", head_at=S("c07") + 0.05,
    steps=[{"label": "The offence", "sub": "its exact section", "icon": "scroll-text", "at": A("c07", "check")},
           {"label": "First Schedule", "sub": "or the special law", "icon": "book-open", "at": A("c07", "schedule")},
           {"label": "Classification", "sub": "cognizable or not", "icon": "badge-check", "tone": "ok", "at": A("c07", "special") + 0.35}],
    note={"text": "Never guess it from how serious it sounds", "icon": "triangle-alert", "at": A("c07", "never")})

# ── 3 · Ravi's stolen phone ──────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="timeline", t0=S("c08"), t1=E("c08") + 0.05,
    nodes=[{"label": "RAVI'S PHONE", "value": "₹25,000", "sub": "beside him on a park bench", "at": A("c08", "phone")},
           {"label": "HE LOOKS AWAY", "value": "Taken", "sub": "dishonestly, by a stranger", "tone": "red", "at": A("c08", "stranger")}])
cue(type="section", t0=S("c09"), t1=E("c09") + 0.05, at=A("c09", "theft"), act="BNS", num="303(2)", title="Theft",
    points=[{"text": "This theft is cognizable (First Schedule)", "at": A("c09", "nyaya")}])
cue(type="splitcard", t0=S("c10"), t1=E("c10") + 0.05,
    left={"title": "BNS", "text": "describes the offence", "icon": "scroll-text", "at": A("c10", "describes") - 0.25},
    right={"title": "BNSS", "text": "governs the procedure", "icon": "gavel", "at": A("c10", "governs") - 0.25})
cue(type="flow", t0=S("c11"), t1=E("c13") + 0.05, head="Ravi's complaint", head_at=S("c11") + 0.05,
    steps=[{"label": "Information recorded", "sub": "BNSS 173", "icon": "file-pen-line", "at": A("c11", "recorded")},
           {"label": "Police investigate", "sub": "175(1): no prior Magistrate's order", "icon": "search", "at": A("c12", "permits")},
           {"label": "Evidence", "sub": "CCTV · witness accounts", "icon": "video", "tone": "ok", "at": A("c13", "evidence")}])
cue(type="cite", t0=S("c11") + 0.3, t1=E("c13") + 0.05, at=S("c11") + 0.3, tag="ON THE RECORD", text="BNS 303(2) theft · BNSS First Schedule: cognizable · BNSS 173, 175(1)", icon="book-open")

# ── 4 · Meena's ordinary hurt ────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c14"), t1=E("c14") + 0.05, text="Meena: slapped in a private argument", icon="user-round", at=A("c14", "meena"))
cue(type="verdicts", t0=S("c15"), t1=E("c15") + 0.05,
    rows=[{"text": "A weapon", "ok": False, "at": A("c15", "weapon") - 0.1, "strike_at": A("c15", "weapon") + 0.35},
          {"text": "Grievous injury", "ok": False, "at": A("c15", "grievous") - 0.1, "strike_at": A("c15", "grievous") + 0.4},
          {"text": "Any other offence", "ok": False, "at": A("c15", "additional") - 0.1, "strike_at": A("c15", "additional") + 0.45},
          {"text": "Only ordinary hurt (assumed)", "ok": True, "at": A("c15", "offence") + 0.3}])
cue(type="section", t0=S("c16"), t1=E("c16") + 0.05, at=A("c16", "section"), act="BNS", num="115(2)", title="Voluntarily causing hurt",
    points=[{"text": "First Schedule: non-cognizable", "at": A("c16", "classifies")}])
cue(type="flow", t0=S("c17"), t1=E("c18") + 0.05, head="Meena's complaint", head_at=S("c17") + 0.05,
    steps=[{"label": "Police record it", "sub": "174(1)", "icon": "book-text", "at": A("c17", "record")},
           {"label": "Referred to the Magistrate", "sub": "174(1)", "icon": "landmark", "at": A("c17", "referral")},
           {"label": "Magistrate's order", "sub": "174(2): needed before investigating", "icon": "gavel", "tone": "ok", "at": A("c18", "order")}])
cue(type="cite", t0=S("c17") + 0.3, t1=E("c18") + 0.05, at=S("c17") + 0.3, tag="ON THE RECORD", text="BNSS 174(1)–(2) · an assumed case of ordinary hurt only", icon="book-open")

# ── 5 · investigate ≠ arrest ─────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="verdicts", t0=S("c19"), t1=E("c20") + 0.05,
    rows=[{"text": "Investigate: opened by the order", "ok": True, "at": A("c19", "permits")},
          {"text": "Arrest without a warrant", "ok": False, "at": A("c20", "authorise"), "strike_at": A("c20", "warrant") + 0.25}])
cue(type="section", t0=S("c21"), t1=E("c21") + 0.05, at=A("c21", "section"), act="BNSS", num="174(3)", title="Investigation order ≠ arrest power",
    points=[{"text": "Permission to investigate and authority to arrest are separate", "at": A("c21", "permission")}])
cue(type="notequal", t0=S("c22"), t1=E("c22") + 0.05, left="Investigation permission", right="arrest permission", at=A("c22", "investigation"),
    left_at=A("c22", "obtaining"), sub="Getting the first does not give you the second", sub_at=A("c22", "investigation") + 0.6)
cue(type="cite", t0=S("c21") + 0.3, t1=E("c22") + 0.05, at=S("c21") + 0.3, tag="SEE ALSO", text="BNSS 174(3); 35(2), subject to statutory exceptions", icon="book-open")

# ── 6 · no automatic arrest ──────────────────────────────────────────────────────────────────────────────────────────────────────
qa = A("c23", "must")
cue(type="question", t0=S("c23"), t1=E("c23") + 0.05, at=qa, text="Theft is cognizable. Automatic arrest?", hl="Automatic arrest?")
cue(type="stamp", t0=A("c23", "no") - 0.05, t1=E("c23") + 0.05, at=A("c23", "no"), line1="NO", line2="NOT AUTOMATIC")
cue(type="section", t0=S("c24"), t1=E("c24") + 0.05, at=A("c24", "section"), act="BNSS", num="35", title="Arrest without a warrant",
    points=[{"text": "Its legal conditions must be satisfied", "at": A("c24", "conditions")}])
cue(type="strike", t0=S("c25"), t1=E("c25") + 0.05, text="FIR registered = automatic arrest", icon="file-text", at=S("c25") + 0.05, strike_at=A("c25", "not") + 0.1)
cue(type="point", t0=S("c26"), t1=E("c26") + 0.05, text="Up to 7 years: arrest is the exception", icon="scale", accent=True, at=A("c26", "offences"))
cue(type="cite", t0=A("c26", "supreme"), t1=E("c27") + 0.05, at=A("c26", "supreme"), tag="SUPREME COURT OF INDIA · ORDER OF 15.01.2026",
    cases=[{"name": "Satender Kumar Antil v. CBI", "cite": "2026 INSC 115, paras 26, 31, 33"}])
cue(type="section", t0=S("c27"), t1=E("c27") + 0.05, at=A("c27", "notice"), act="BNSS", num="35(3)", title="Notice to appear: the rule",
    points=[{"text": "Officers must justify an arrest under the safeguards", "at": A("c27", "officers")}])
cue(type="notequal", t0=S("c28"), t1=E("c28") + 0.05, left="Investigation", right="arrest", at=A("c28", "arrest"), left_at=A("c28", "investigation"),
    sub="An allegation is not a finding of guilt", sub_at=A("c28", "allegation"))

# ── 7 · both in one case ─────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="equation", t0=S("c29"), t1=E("c30") + 0.05,
    terms=[{"text": "COGNIZABLE THEFT", "at": A("c29", "cognizable")}, {"op": "+", "text": "NON-COGNIZABLE HURT", "at": A("c29", "non")},
           {"op": "=", "text": "CASE: COGNIZABLE", "result": True, "at": A("c30", "treated")}])
cue(type="cite", t0=S("c30"), t1=E("c31") + 0.05, at=S("c30"), tag="BNSS 174(4)", text="At least one cognizable offence in the same case", icon="book-open")
cue(type="verdicts", t0=S("c31"), t1=E("c31") + 0.05,
    rows=[{"text": "Two investigation routes", "ok": False, "at": A("c31", "split"), "strike_at": A("c31", "routes") + 0.3},
          {"text": "One case, treated as cognizable", "ok": True, "at": A("c31", "merely")}])

# ── 8 · not about bail ───────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="compare", t0=S("c32"), t1=E("c33") + 0.05, head="Two different questions", head_at=A("c32", "another"),
    cols=[{"title": "Cognizable?", "icon": "search", "at": A("c32", "cognizable")}, {"title": "Bailable?", "icon": "key-round", "at": A("c33", "bailable")}],
    rows=[{"cells": ["Police powers and procedure", "Bail"], "cells_at": [A("c32", "police"), A("c33", "concern")]},
          {"cells": ["Its own column in the First Schedule", "Its own column in the First Schedule"], "cells_at": [A("c33", "columns"), A("c33", "columns") + 0.2]}])
cue(type="point", t0=S("c34"), t1=A("c34", "and") - 0.02, text="Cognizable can still be bailable", icon="key-round", at=A("c34", "cognizable"))
cue(type="cite", t0=A("c34", "cognizable"), t1=A("c34", "and") - 0.02, at=A("c34", "cognizable"), tag="FOR EXAMPLE", text="BNS 117(2), grievous hurt: cognizable and bailable", icon="book-open")
cue(type="strike", t0=A("c34", "and"), t1=E("c34") + 0.05, text="Non-bailable = bail can never be granted", icon="lock", at=A("c34", "and"), strike_at=A("c34", "never") + 0.15)
cue(type="point", t0=S("c35"), t1=E("c35") + 0.05, text="Check the exact offence and the applicable law", icon="search-check", accent=True, at=A("c35", "always"))

# ── 9 · reporting an offence ─────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="checklist", t0=S("c36"), t1=E("c36") + 0.05, head="Before you report", head_at=A("c36", "what"),
    items=[{"n": 1, "text": "Clear facts", "at": A("c36", "facts")}, {"n": 2, "text": "Dates", "at": A("c36", "clearly")},
           {"n": 3, "text": "Evidence preserved", "at": A("c36", "preserve")}, {"n": 4, "text": "Acknowledgement", "at": A("c36", "evidence", 1) + 0.45}])
cue(type="section", t0=S("c37"), t1=E("c38") + 0.05, at=A("c37", "section"), act="BNSS", num="173", title="Information in cognizable cases",
    points=[{"text": "Report it wherever the offence occurred: Zero FIR (173(1))", "at": A("c37", "irrespective")},
            {"text": "A free copy of the recorded information (173(2))", "at": A("c38", "free")}])
cue(type="flow", t0=S("c39"), t1=E("c40") + 0.05, head="If the police refuse", head_at=S("c39") + 0.05,
    steps=[{"label": "Recording refused", "icon": "ban", "tone": "stop", "at": A("c39", "refused")},
           {"label": "Write to the SP", "sub": "173(4): in writing, by post", "icon": "mail", "at": A("c39", "superintendent")},
           {"label": "Magistrate", "sub": "175(3): application with an affidavit", "icon": "landmark", "tone": "ok", "at": A("c40", "magistrate")}])
cue(type="notequal", t0=S("c41"), t1=E("c41") + 0.05, left="Non-cognizable", right="no remedy", at=A("c41", "absence"), left_at=A("c41", "purely"),
    sub="A different procedure: the Section 174 route", sub_at=A("c41", "route"))

# ── 10 · remember ────────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="list", t0=S("c42"), t1=E("c42") + 0.05, head="Two questions", head_at=A("c42", "remember"),
    items=[{"n": 1, "text": "Investigate without an order?", "at": A("c42", "can")}, {"n": 2, "text": "Authority to arrest?", "at": A("c42", "what")}])
cue(type="compare", t0=S("c43"), t1=A("c44", "check") - 0.05, head="Remember the distinction", head_at=S("c43") + 0.05,
    cols=[{"title": "Cognizable", "icon": "search", "at": A("c43", "cognizable")}, {"title": "Non-cognizable", "icon": "landmark", "at": A("c43", "non")}],
    rows=[{"cells": ["Police investigate without a prior order", "A Magistrate's order is needed"], "cells_at": [A("c43", "permit"), A("c43", "require")]},
          {"cells": ["Arrest: subject to the safeguards", "That order gives no arrest power"], "cells_at": [A("c44", "arrest"), A("c44", "safeguards")]}])
cue(type="list", t0=A("c44", "check"), t1=E("c45") + 0.05, head="Read together", head_at=A("c44", "check"),
    items=[{"n": "§", "text": "BNSS 2 · 35 · 173 · 174 · 175", "at": A("c44", "sections")}, {"n": "+", "text": "the First Schedule", "at": A("c45", "schedule")},
           {"n": "=", "text": "the right procedure", "at": A("c45", "procedure")}])

STING = {"kicker": "CRIMINAL PROCEDURE · BNSS EXPLAINED", "title": "Cognizable vs Non-Cognizable", "sub": "Police powers, through two everyday reports"}
ENDCARD = {"title": "Cognizable vs Non-Cognizable", "line": "Investigation power ≠ arrest power", "sub": "Next lesson: Compounding and Plea Bargaining"}
