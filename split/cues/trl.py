# Stages of a Criminal Trial (BNSS): panel cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND).
# Storyboard: ~/Downloads/Stages_of_a_Criminal_Trial_BNSS_Storyboard.pdf. Fact-check 19-10-2026 (storyboard error fixed): police-report
# warrant trials 261-266, complaint warrant trials 267-270, conclusion 271-273; s.210 cognizance; 232/251 offences exclusively triable
# by the Court of Session; Suresh Sahu & Another v. State of Bihar (now Jharkhand), 2025 INSC 1382 (27.11.2025) paras 18-19: every
# incriminating circumstance put specifically; 258(1): 30 days from completion of arguments, 45 with written reasons.
# v2 19-10-2026: cues rebuilt for the fast energetic script (37 clips; v1: split/v1_19oct/trl.py); citations as in v1.
# v2 fact-check 19-10-2026: c06 stamp reads CASE COMMITTED / TO SESSIONS (a bare red "COMMITTED" in a murder illustration read as
# "offence committed"); c05 note names the two dates; builds re-anchored to the spoken word (c26 not, c30 these). c07 keeps "and":
# "evidence" is the clip's last word and its build would run past the card's fade.
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

STING = {"kicker": "CRIMINAL PROCEDURE · BNSS EXPLAINED", "title": "Stages of a Criminal Trial", "sub": "A contested Sessions trial, step by step"}
ENDCARD = {"title": "Stages of a Criminal Trial", "line": "Charge → evidence → explanation → defence → judgment", "sub": "LawWorld: legal research for advocates"}

# ── 1 · from FIR to judgment ─────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c01"), t1=A("c01", "does") - 0.05, text="Your client: accused of murder. He denies it.", icon="user-round", at=A("c01", "client"))
cue(type="question", t0=A("c01", "does") - 0.05, t1=A("c01", "presented") - 0.05, at=A("c01", "does"), text="Does the FIR lead straight to punishment?", hl="straight to punishment?")
cue(type="stamp", t0=A("c01", "no") - 0.05, t1=A("c01", "presented") - 0.05, at=A("c01", "no"), line1="NO", line2="NOT IN ONE STEP")
cue(type="flow", t0=A("c01", "presented") - 0.05, t1=A("c02", "arjun") - 0.05, head="Evidence must be…", head_at=A("c01", "presented"),
    steps=[{"label": "Presented", "icon": "file-text", "at": A("c01", "presented")}, {"label": "Tested", "icon": "search", "at": A("c01", "tested")},
           {"label": "Considered", "icon": "scale", "tone": "ok", "at": A("c01", "considered")}])
cue(type="splitcard", t0=A("c02", "arjun") - 0.05, t1=E("c02") + 0.05,
    left={"title": "ARJUN", "text": "your client · an illustration", "icon": "user-round", "at": A("c02", "arjun")},
    right={"title": "SESSIONS TRIAL", "text": "contested · under the BNSS", "icon": "gavel", "at": A("c02", "contested")})
cue(type="cite", t0=A("c02", "bharatiya"), t1=E("c02") + 0.05, at=A("c02", "bharatiya"), tag="THE LAW", text="Bharatiya Nagarik Suraksha Sanhita · BNSS", icon="book-open")

# ── 2 · before the trial ─────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="notequal", t0=S("c03"), t1=A("c03", "police") - 0.05, left="Investigation", right="trial", at=A("c03", "or"), left_at=A("c03", "investigation"),
    sub="Keep them separate", sub_at=A("c03", "keep"))
cue(type="flow", t0=A("c03", "police") - 0.05, t1=E("c04") + 0.05, head="Before the trial", head_at=A("c03", "police"),
    steps=[{"label": "Police investigate", "icon": "search", "at": A("c03", "investigate")},
           {"label": "Their report", "sub": "§ 193", "icon": "file-text", "at": A("c03", "report")},
           {"label": "Cognizance?", "sub": "§ 210 · the Magistrate decides", "icon": "landmark", "tone": "ok", "at": A("c04", "decides")}])
cue(type="counters", t0=S("c05"), t1=E("c05") + 0.05, head="§ 230: the papers, free", head_at=S("c05") + 0.05,
    items=[{"value": 14, "unit": "DAYS", "label": "Papers supplied free", "sub": "from production or appearance", "at": A("c05", "fourteen")}],
    note={"text": "Check both dates: production or appearance, and supply", "icon": "calendar", "at": A("c05", "check")})
cue(type="question", t0=S("c06"), t1=E("c06") + 0.05, at=A("c06", "is"), text="Is the offence triable exclusively by the Court of Session?", hl="exclusively")
cue(type="stamp", t0=A("c06", "committed") - 0.05, t1=E("c06") + 0.05, at=A("c06", "committed"), line1="CASE COMMITTED", line2="TO SESSIONS · § 232")
cue(type="section", t0=S("c07"), t1=E("c07") + 0.05, at=A("c07", "prosecutor"), act="BNSS", num="249", title="The Prosecutor opens the case",
    points=[{"text": "The accusation", "at": A("c07", "accusation")}, {"text": "The evidence", "at": A("c07", "and")}])

# ── 3 · discharge, charge, plea ──────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c08"), t1=A("c08", "under") - 0.05, at=A("c08", "can"), text="Can your client be discharged?", hl="discharged?")
cue(type="section", t0=A("c08", "under") - 0.05, t1=E("c09") + 0.05, at=A("c08", "section"), act="BNSS", num="250", title="Discharge",
    points=[{"text": "Application within 60 days from commitment", "at": A("c08", "sixty")},
            {"text": "Insufficient ground → must discharge, record reasons", "at": A("c09", "insufficient")}])
cue(type="counters", t0=S("c10"), t1=E("c10") + 0.05, head="§ 251(1)(b): the charge", head_at=A("c10", "section"),
    items=[{"value": 60, "unit": "DAYS", "label": "Frame a written charge", "sub": "from the first hearing on charge", "at": A("c10", "sixty")}],
    note={"text": "A second clock, with a different trigger", "icon": "calendar", "at": A("c10", "second")})
cue(type="flow", t0=S("c11"), t1=A("c11", "a") - 0.05, head="The charge", head_at=S("c11") + 0.05,
    steps=[{"label": "Read and explained", "icon": "book-open", "at": A("c11", "read")},
           {"label": "Plea recorded", "icon": "file-pen-line", "tone": "ok", "at": A("c11", "plea")}])
cue(type="compare", t0=A("c11", "a") - 0.05, t1=E("c11") + 0.05, head="The plea", head_at=A("c11", "guilty"),
    cols=[{"title": "Guilty plea", "icon": "gavel", "at": A("c11", "guilty")}, {"title": "Arjun's plea", "icon": "user-round", "at": A("c11", "arjun")}],
    rows=[{"cells": ["May lead to conviction · § 252", "Contests the charge"], "cells_at": [A("c11", "conviction"), A("c11", "contests")]}])

# ── 4 · prosecution evidence ─────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c12"), t1=A("c12", "sections") - 0.05, text="The prosecution must prove its case", icon="scale", accent=True, at=A("c12", "prosecution"))
cue(type="section", t0=A("c12", "sections") - 0.05, t1=E("c12") + 0.05, at=A("c12", "sections"), act="BNSS", num="253 · 254", title="Prosecution evidence",
    points=[{"text": "Witnesses testify", "at": A("c12", "witnesses")}, {"text": "Documents are presented", "at": A("c12", "documents")}])
cue(type="list", t0=S("c13"), t1=E("c13") + 0.05, head="In Arjun's case", head_at=S("c13") + 0.05,
    items=[{"n": 1, "text": "An eyewitness: the incident", "at": A("c13", "eyewitness")}, {"n": 2, "text": "A doctor: medical findings", "at": A("c13", "doctor")},
           {"n": 3, "text": "Recordings may be produced", "at": A("c13", "recordings")}])
cue(type="kicker", t0=S("c14"), t1=E("c14") + 0.05, at=S("c14") + 0.05, text="YOUR TURN · CROSS-EXAMINE")
cue(type="question", t0=S("c14"), t1=A("c14", "does") - 0.05, at=A("c14", "could"), text="Could the witness really see clearly?", hl="see clearly?")
cue(type="question", t0=A("c14", "does") - 0.05, t1=A("c15", "an") - 0.05, at=A("c14", "does"), text="Does the medical evidence actually support the account?", hl="support the account?")
cue(type="strike", t0=A("c15", "an") - 0.05, t1=E("c15") + 0.05, text="A charge-sheet allegation = proof of guilt", icon="file-text", at=A("c15", "allegation"), strike_at=A("c15", "not") + 0.1)
cue(type="question", t0=S("c16"), t1=A("c16", "section") - 0.05, at=A("c16", "what"), text="What about delay?", hl="delay?")
cue(type="section", t0=A("c16", "section") - 0.05, t1=E("c16") + 0.05, at=A("c16", "section"), act="BNSS", num="346", title="Day-to-day hearings, generally",
    points=[{"text": "While attending witnesses remain to be examined", "at": A("c16", "while")}],
    note={"text": "Subject to the lawful adjournment rules", "icon": "calendar", "at": A("c16", "remain")})

# ── 5 · the accused explains ─────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="timeline", t0=S("c17"), t1=E("c17") + 0.05,
    nodes=[{"label": "PROSECUTION WITNESSES", "value": "Over", "at": A("c17", "prosecution")},
           {"label": "BEFORE THE DEFENCE", "value": "§ 351", "sub": "a crucial safeguard", "at": A("c17", "crucial")}])
cue(type="section", t0=S("c18"), t1=E("c18") + 0.05, at=A("c18", "requires"), act="BNSS", num="351", title="Examination of the accused",
    points=[{"text": "The circumstances appearing against him", "at": A("c18", "circumstances")},
            {"text": "Put to him, for his explanation", "at": A("c18", "him")}])
cue(type="question", t0=S("c19"), t1=A("c19", "fair") - 0.05, at=A("c19", "witness"), text="A witness places Arjun at the scene?", hl="at the scene?")
cue(type="verdicts", t0=A("c19", "fair") - 0.05, t1=E("c19") + 0.05,
    rows=[{"text": "A fair opportunity to answer", "ok": True, "at": A("c19", "fair")},
          {"text": "Cross-examination on oath", "ok": False, "at": A("c19", "not"), "strike_at": A("c19", "oath") + 0.1},
          {"text": "His chance to explain", "ok": True, "at": A("c19", "it")}])
cue(type="point", t0=S("c20"), t1=A("c20", "so") - 0.05, text="Every incriminating circumstance, put specifically", icon="search-check", accent=True, at=A("c20", "every"))
cue(type="cite", t0=A("c20", "supreme"), t1=E("c20") + 0.05, at=A("c20", "supreme"), tag="SUPREME COURT OF INDIA · 27.11.2025",
    cases=[{"name": "Suresh Sahu & Another v. State of Bihar (now Jharkhand)", "cite": "2025 INSC 1382, paras 18–19"}])
cue(type="point", t0=A("c20", "so") - 0.05, t1=E("c20") + 0.05, text="So check the record", icon="file-check", at=A("c20", "check"))

# ── 6 · acquittal or defence ─────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c21"), t1=A("c21", "section") - 0.05, at=A("c21", "is"), text="Is there any evidence that he did it?", hl="he did it?")
cue(type="compare", t0=A("c21", "section") - 0.05, t1=E("c22") + 0.05, head="The § 255 checkpoint", head_at=A("c21", "section"),
    cols=[{"title": "No evidence he did it", "icon": "badge-check", "at": A("c21", "no")}, {"title": "Otherwise", "icon": "arrow-right", "at": A("c22", "otherwise")}],
    rows=[{"cells": ["The Judge must acquit · § 255", "Defence evidence · § 256"], "cells_at": [A("c21", "acquit"), A("c22", "defence")]}],
    verdict={"text": "Arjun: a workplace witness, attendance records", "icon": "user-round", "at": A("c22", "workplace")})
cue(type="verdicts", t0=S("c23"), t1=A("c23", "proving") - 0.05,
    rows=[{"text": "Forced into the witness box", "ok": False, "at": A("c23", "need"), "strike_at": A("c23", "box") + 0.3},
          {"text": "Testifies only on his written request · § 353", "ok": True, "at": A("c23", "testify")}])
cue(type="point", t0=A("c23", "proving") - 0.05, t1=E("c23") + 0.05, text="Proving guilt remains the prosecution's burden", icon="scale", accent=True, at=A("c23", "proving"))

# ── 7 · final arguments ──────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="compare", t0=S("c24"), t1=E("c25") + 0.05, head="Final arguments (§ 257)", head_at=A("c24", "done"),
    cols=[{"title": "Prosecution", "icon": "scale", "at": A("c24", "prosecutor")}, {"title": "Defence", "icon": "user-round", "at": A("c24", "defence")}],
    rows=[{"cells": ["Sums up", "Replies"], "cells_at": [A("c24", "sums"), A("c24", "replies")]},
          {"cells": ["Links the evidence to the offence", "Weaknesses, inconsistencies, reasonable doubt"], "cells_at": [A("c25", "links"), A("c25", "weaknesses")]}])
cue(type="point", t0=S("c26"), t1=A("c26", "lawyer") - 0.05, text="Tie every argument to the record", icon="file-check", accent=True, at=A("c26", "tie"))
cue(type="notequal", t0=A("c26", "lawyer") - 0.05, t1=E("c26") + 0.05, left="A lawyer's argument", right="proof of a disputed fact", at=A("c26", "not"), left_at=A("c26", "lawyer"))

# ── 8 · judgment and sentence ────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c27"), t1=A("c27", "under") - 0.05, at=A("c27", "how"), text="How long can the judgment take?", hl="judgment take?")
cue(type="counters", t0=A("c27", "under") - 0.05, t1=E("c28") + 0.05, head="Judgment · § 258(1)", head_at=A("c27", "section"),
    items=[{"value": 30, "unit": "DAYS", "label": "From the end of arguments", "at": A("c27", "thirty")},
           {"value": 45, "unit": "DAYS", "label": "Only with written reasons", "at": A("c28", "forty")}],
    note={"text": "Note the exact date the arguments end", "icon": "calendar", "at": A("c28", "note")})
cue(type="point", t0=S("c29"), t1=E("c29") + 0.05, text="Guilt proved beyond reasonable doubt?", icon="scale", at=A("c29", "court"))
cue(type="cite", t0=A("c29", "reasons"), t1=E("c29") + 0.05, at=A("c29", "reasons"), tag="EITHER WAY", text="Reasons for acquittal or conviction", icon="file-pen-line")
cue(type="kicker", t0=S("c30"), t1=E("c30") + 0.05, at=S("c30") + 0.05, text="COMMON MISTAKE")
cue(type="verdicts", t0=S("c30"), t1=E("c30") + 0.05,
    rows=[{"text": "30 or 45 days: from the end of arguments", "ok": True, "at": A("c30", "these")},
          {"text": "A deadline for the whole case, from the FIR", "ok": False, "at": A("c30", "deadline"), "strike_at": A("c30", "case") + 0.1}])
cue(type="flow", t0=S("c31"), t1=E("c32") + 0.05, head="If Arjun is convicted", head_at=S("c31") + 0.05,
    steps=[{"label": "Conviction", "icon": "gavel", "at": A("c31", "convicted")},
           {"label": "Hearing on sentence", "sub": "§ 258(2)", "icon": "users", "at": A("c31", "hearing")},
           {"label": "The lawful sentence", "icon": "scale", "tone": "ok", "at": A("c32", "passes")}],
    note={"text": "Any appeal is a separate process", "icon": "arrow-right", "at": A("c32", "appeal")})
cue(type="cite", t0=A("c32", "come"), t1=A("c32", "any") - 0.05, at=A("c32", "come"), tag="COME PREPARED", text="Sentencing material · the parties' submissions", icon="file-text")

# ── 9 · Magistrate trials ────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c33"), t1=A("c33", "warrant") - 0.05, at=A("c33", "magistrate"), text="Magistrate trial? The provisions change.", hl="provisions change.")
cue(type="list", t0=A("c33", "warrant") - 0.05, t1=E("c35") + 0.05, head="Magistrate trials", head_at=A("c33", "warrant"),
    items=[{"n": 1, "text": "Police-report warrant: §§ 261–266", "at": A("c33", "police")}, {"n": 2, "text": "Complaint warrant: §§ 267–270", "at": A("c34", "complaint")},
           {"n": 3, "text": "Both conclude: §§ 271–273", "at": A("c35", "both")}, {"n": 4, "text": "Summons: §§ 274–278", "at": A("c35", "summons")}])
cue(type="cite", t0=A("c34", "with"), t1=E("c34") + 0.05, at=A("c34", "with"), tag="COMPLAINT WARRANT CASES", text="Evidence is taken before the charge", icon="info")
cue(type="cite", t0=A("c35", "with"), t1=E("c35") + 0.05, at=A("c35", "with"), tag="SUMMONS CASES", text="No formal charge", icon="info")

# ── 10 · your trial checklist ────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="checklist", t0=S("c36"), t1=E("c36") + 0.05, head="The main Sessions route", head_at=A("c36", "remember"),
    items=[{"n": 1, "text": "Charge and plea", "at": A("c36", "charge")}, {"n": 2, "text": "Prosecution evidence", "at": A("c36", "prosecution")},
           {"n": 3, "text": "The accused's explanation", "at": A("c36", "explanation")}, {"n": 4, "text": "Any defence evidence", "at": A("c36", "defence")},
           {"n": 5, "text": "Arguments and judgment", "at": A("c36", "arguments")}])
cue(type="point", t0=S("c37"), t1=A("c37", "always") - 0.05, text="Sentencing: only after a conviction", icon="gavel", at=A("c37", "sentencing"))
cue(type="list", t0=A("c37", "always") - 0.05, t1=E("c37") + 0.05, head="Always check", head_at=A("c37", "always"),
    items=[{"n": 1, "text": "The case type", "at": A("c37", "case")}, {"n": 2, "text": "Each deadline's exact starting point", "at": A("c37", "deadline")}])
