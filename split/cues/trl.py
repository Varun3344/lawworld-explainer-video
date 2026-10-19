# Stages of a Criminal Trial (BNSS): panel cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND).
# Storyboard: ~/Downloads/Stages_of_a_Criminal_Trial_BNSS_Storyboard.pdf. Fact-check 19-10-2026 (storyboard error fixed): police-report
# warrant trials 261-266, complaint warrant trials 267-270, conclusion 271-273; s.210 cognizance; 232/251 offences exclusively triable
# by the Court of Session; Suresh Sahu & Another v. State of Bihar (now Jharkhand), 2025 INSC 1382 (27.11.2025) paras 18-19: every
# incriminating circumstance put specifically; 258(1): 30 days from completion of arguments, 45 with written reasons.
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

STING = {"kicker": "CRIMINAL PROCEDURE · BNSS EXPLAINED", "title": "Stages of a Criminal Trial", "sub": "A contested Sessions trial, step by step"}
ENDCARD = {"title": "Stages of a Criminal Trial", "line": "Charge → evidence → explanation → defence → judgment", "sub": "LawWorld: legal research for advocates"}

# ── 1 · from FIR to judgment ─────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="strike", t0=S("c01"), t1=A("c01", "evidence") - 0.05, text="FIR → punishment, in one step", icon="file-text", at=S("c01") + 0.05, strike_at=A("c01", "punishment") + 0.15)
cue(type="flow", t0=A("c01", "evidence"), t1=E("c01") + 0.05, head="Evidence must be…", head_at=A("c01", "evidence"),
    steps=[{"label": "Presented", "icon": "file-text", "at": A("c01", "presented")}, {"label": "Tested", "icon": "search", "at": A("c01", "tested")},
           {"label": "Considered", "icon": "scale", "tone": "ok", "at": A("c01", "considered")}])
cue(type="flow", t0=S("c02"), t1=E("c02") + 0.05, head="A contested Sessions trial", head_at=S("c02") + 0.05,
    steps=[{"label": "Before trial", "icon": "file-text", "at": A("c02", "follow")}, {"label": "Charge and plea", "icon": "gavel", "at": A("c02", "follow") + 1.0},
           {"label": "Evidence", "sub": "prosecution · § 351 · defence", "icon": "search", "at": A("c02", "follow") + 2.0},
           {"label": "Judgment", "icon": "scale", "tone": "ok", "at": A("c02", "follow") + 3.0}])
cue(type="point", t0=S("c03"), t1=E("c03") + 0.05, text="Arjun: accused of murder, denies it (an illustration)", icon="user-round", at=A("c03", "arjun"))

# ── 2 · before the trial ─────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c04"), t1=E("c08") + 0.05, head="Before the trial", head_at=S("c04") + 0.05, dir="v",
    steps=[{"label": "Police report", "sub": "§ 193", "icon": "file-text", "at": A("c04", "police")},
           {"label": "Cognizance decided", "sub": "§ 210", "icon": "search", "at": A("c05", "decides")},
           {"label": "Papers supplied free", "sub": "§ 230 · within 14 days", "icon": "copy", "at": A("c06", "papers")},
           {"label": "Committed to Sessions", "sub": "§ 232", "icon": "landmark", "at": A("c07", "committed")},
           {"label": "Prosecutor opens the case", "sub": "§ 249", "icon": "gavel", "tone": "ok", "at": A("c08", "opens")}])

# ── 3 · discharge, charge, plea ──────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c09"), t1=E("c10") + 0.05, at=A("c09", "section"), act="BNSS", num="250", title="Discharge",
    points=[{"text": "Application within 60 days from commitment", "at": A("c09", "sixty")},
            {"text": "Insufficient ground → discharge, with reasons", "at": A("c10", "insufficient")}])
cue(type="section", t0=S("c11"), t1=E("c11") + 0.05, at=A("c11", "section"), act="BNSS", num="251(1)(b)", title="Charge",
    points=[{"text": "Written charge within 60 days of the first hearing on charge", "at": A("c11", "sixty")}])
cue(type="compare", t0=S("c12"), t1=E("c13") + 0.05, head="The plea", head_at=S("c12") + 0.05,
    cols=[{"title": "Guilty plea", "icon": "gavel", "at": A("c12", "guilty")}, {"title": "Contested", "icon": "scale", "at": A("c13", "contests")}],
    rows=[{"cells": ["May lead to conviction · § 252", "The prosecution's evidence follows"], "cells_at": [A("c12", "conviction"), A("c13", "evidence")]}],
    verdict={"text": "A charge framed is not guilt proved", "icon": "triangle-alert", "at": A("c13", "arjun") + 0.2})

# ── 4 · prosecution evidence ─────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c14"), t1=E("c14") + 0.05, at=A("c14", "sections"), act="BNSS", num="253 · 254", title="Prosecution evidence",
    points=[{"text": "Witnesses testify", "at": A("c14", "witnesses")}, {"text": "Documents are presented", "at": A("c14", "documents")}])
cue(type="list", t0=S("c15"), t1=E("c15") + 0.05, head="In Arjun's case", head_at=S("c15") + 0.05,
    items=[{"n": 1, "text": "An eyewitness", "at": A("c15", "eyewitness")}, {"n": 2, "text": "A doctor: medical findings", "at": A("c15", "doctor")},
           {"n": 3, "text": "Recordings", "at": A("c15", "recordings")}])
cue(type="list", t0=S("c16"), t1=E("c16") + 0.05, head="Cross-examination", head_at=A("c16", "defence"),
    items=[{"n": "?", "text": "Could the witness see clearly?", "at": A("c16", "could")}, {"n": "?", "text": "Does the medical evidence fit?", "at": A("c16", "does")}])
cue(type="notequal", t0=S("c17"), t1=E("c17") + 0.05, left="An allegation", right="proof", at=A("c17", "not"), left_at=A("c17", "allegation"))
cue(type="section", t0=S("c18"), t1=E("c18") + 0.05, at=A("c18", "section"), act="BNSS", num="346", title="Day-to-day hearings",
    points=[{"text": "While attending witnesses remain to be examined", "at": A("c18", "while")}],
    note={"text": "Subject to the lawful adjournment rules", "icon": "calendar", "at": A("c18", "examined")})

# ── 5 · the accused explains ─────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c19"), t1=E("c20") + 0.05, at=A("c19", "crucial"), act="BNSS", num="351", title="Examination of the accused",
    points=[{"text": "After the prosecution witnesses, before the defence", "at": A("c19", "after") + 0.6},
            {"text": "The circumstances against him, put for his explanation", "at": A("c20", "circumstances")}])
cue(type="question", t0=S("c21"), t1=E("c21") + 0.05, at=A("c21", "witness"), text="A witness places you at the scene. Your explanation?", hl="Your explanation?")
cue(type="cite", t0=A("c21", "this"), t1=E("c21") + 0.05, at=A("c21", "this"), tag="§ 351", text="Not cross-examination: no oath", icon="info")
cue(type="point", t0=S("c22"), t1=E("c22") + 0.05, text="Every incriminating circumstance, put specifically", icon="search-check", accent=True, at=A("c22", "every"))
cue(type="cite", t0=A("c22", "supreme"), t1=E("c22") + 0.05, at=A("c22", "supreme"), tag="SUPREME COURT OF INDIA · 27.11.2025",
    cases=[{"name": "Suresh Sahu & Another v. State of Bihar (now Jharkhand)", "cite": "2025 INSC 1382, paras 18–19"}])

# ── 6 · acquittal or defence ─────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="compare", t0=S("c23"), t1=E("c24") + 0.05, head="The § 255 checkpoint", head_at=A("c23", "checkpoint"),
    cols=[{"title": "No evidence he did it", "icon": "badge-check", "at": A("c23", "no")}, {"title": "Otherwise", "icon": "arrow-right", "at": A("c24", "otherwise")}],
    rows=[{"cells": ["The Judge must acquit · § 255", "Defence evidence · § 256"], "cells_at": [A("c23", "acquit"), A("c24", "defence")]},
          {"cells": ["The trial ends here", "A workplace witness, attendance records"], "cells_at": [A("c23", "acquit") + 0.4, A("c24", "workplace")]}])
cue(type="verdicts", t0=S("c25"), t1=E("c25") + 0.05,
    rows=[{"text": "Testifies only on his written request · § 353", "ok": True, "at": A("c25", "testify")},
          {"text": "Forced into the witness box", "ok": False, "at": A("c25", "need"), "strike_at": A("c25", "box") + 0.3}])
cue(type="point", t0=S("c26"), t1=E("c26") + 0.05, text="The burden stays on the prosecution", icon="scale", accent=True, at=A("c26", "prosecution"))

# ── 7 · final arguments ──────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="compare", t0=S("c27"), t1=E("c28") + 0.05, head="Final arguments (§ 257)", head_at=A("c27", "section"),
    cols=[{"title": "Prosecution", "icon": "scale", "at": A("c27", "prosecutor")}, {"title": "Defence", "icon": "user-round", "at": A("c27", "defence")}],
    rows=[{"cells": ["Sums up", "Replies"], "cells_at": [A("c27", "sums"), A("c27", "replies")]},
          {"cells": ["Connects the evidence to the offence", "Weaknesses, inconsistencies, reasonable doubt"], "cells_at": [A("c28", "connects"), A("c28", "weaknesses")]}])
cue(type="notequal", t0=S("c29"), t1=E("c29") + 0.05, left="An argument", right="proof", at=A("c29", "not"), left_at=A("c29", "argument"))

# ── 8 · judgment and its deadline ────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="counters", t0=S("c30"), t1=E("c31") + 0.05, head="Judgment · § 258(1)", head_at=A("c30", "section"),
    items=[{"value": 30, "unit": "DAYS", "label": "From the end of arguments", "at": A("c30", "thirty")},
           {"value": 45, "unit": "DAYS", "label": "Only with written reasons", "at": A("c31", "forty")}])
cue(type="point", t0=S("c32"), t1=E("c32") + 0.05, text="Guilt proved beyond reasonable doubt? Reasons, either way", icon="scale", at=A("c32", "court"))
cue(type="strike", t0=S("c33"), t1=E("c33") + 0.05, text="A deadline for the whole case", icon="calendar", at=A("c33", "they"), strike_at=A("c33", "r") + 0.2)

# ── 9 · if convicted ─────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c34"), t1=E("c35") + 0.05,
    steps=[{"label": "Conviction", "icon": "gavel", "at": A("c34", "convicted")},
           {"label": "Hearing on sentence", "sub": "§ 258(2)", "icon": "users", "at": A("c34", "hearing")},
           {"label": "The lawful sentence", "icon": "scale", "tone": "ok", "at": A("c35", "passes")}])
cue(type="compare", t0=S("c36"), t1=E("c36") + 0.05,
    cols=[{"title": "Conviction", "icon": "gavel", "at": A("c36", "conviction")}, {"title": "Sentencing", "icon": "scale", "at": A("c36", "sentencing")}],
    rows=[{"cells": ["Decides guilt", "Its legal consequence"], "cells_at": [A("c36", "decides"), A("c36", "consequence")]}],
    verdict={"text": "Any appeal is a separate process", "icon": "arrow-right", "at": A("c36", "appeal")})

# ── 10 · other trials ────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="list", t0=S("c37"), t1=E("c40") + 0.05, head="Magistrate trials", head_at=A("c37", "magistrate"),
    items=[{"n": 1, "text": "Police-report warrant: §§ 261–266", "at": A("c37", "warrant")}, {"n": 2, "text": "Complaint warrant: §§ 267–270", "at": A("c38", "complaint")},
           {"n": 3, "text": "Conclusion: §§ 271–273", "at": A("c39", "both")}, {"n": 4, "text": "Summons: §§ 274–278", "at": A("c40", "summons")}])
cue(type="checklist", t0=S("c41"), t1=E("c42") + 0.05, head="The main route", head_at=A("c41", "remember"),
    items=[{"n": 1, "text": "Charge and plea", "at": A("c41", "charge")}, {"n": 2, "text": "Prosecution evidence", "at": A("c41", "prosecution")},
           {"n": 3, "text": "The accused's explanation", "at": A("c41", "explanation")}, {"n": 4, "text": "Defence evidence", "at": A("c41", "defence")},
           {"n": 5, "text": "Arguments and judgment", "at": A("c41", "arguments")}])
cue(type="cite", t0=A("c42", "always"), t1=E("c42") + 0.05, at=A("c42", "always"), tag="ALWAYS", text="Check the case type and each deadline's starting point", icon="search-check")
