# Discharge and Framing of Charges (BNSS): panel cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND).
# Storyboard: ~/Downloads/Discharge_and_Framing_of_Charges_BNSS_Storyboard.pdf. Fact-check 19-10-2026: sections and triggers right;
# reported Supreme Court authority on screen for the charge-stage test (Prafulla Kumar Samal (1979) 3 SCC 4; Sajjan Kumar v. CBI
# (2010) 9 SCC 368); laptop > Rs 20,000 (smaller thefts: summary trial); s.274 proviso mandatory; no "automatic 60-day stay".
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

STING = {"kicker": "CRIMINAL PROCEDURE · BNSS EXPLAINED", "title": "Discharge and Framing of Charges", "sub": "How the court screens a case before trial"}
ENDCARD = {"title": "Discharge and Framing of Charges", "line": "Charge sheet ≠ conviction", "sub": "Next lesson: Police Custody and Judicial Custody"}

# ── 1 · the court screens the case ───────────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "must"), text="Charge sheet filed. A full trial now?", hl="A full trial now?")
cue(type="stamp", t0=A("c01", "not") - 0.05, t1=E("c01") + 0.05, at=A("c01", "not"), line1="NOT", line2="AUTOMATICALLY")
cue(type="flow", t0=S("c02"), t1=E("c03") + 0.05, head="The court screens first", head_at=S("c02") + 0.05,
    steps=[{"label": "Charge sheet", "icon": "file-text", "at": S("c02") + 0.3},
           {"label": "Court scrutiny", "sub": "is the threshold met?", "icon": "search", "at": A("c02", "examine")},
           {"label": "Discharge, or charge framed", "icon": "scale", "tone": "ok", "at": A("c02", "threshold")}],
    note={"text": "A charge sheet is not a conviction", "icon": "triangle-alert", "at": A("c03", "screening")})
cue(type="cite", t0=A("c03", "discharge"), t1=E("c03") + 0.05, at=A("c03", "discharge"), tag="BNSS", text="§§ 250–251 (Sessions) · §§ 262–263 (Magistrate, police report)", icon="book-open")

# ── 2 · what discharge means ─────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c04"), t1=E("c04") + 0.05, text="Discharge: proceeding is not justified, at this stage", icon="scale", accent=True, at=A("c04", "discharge"))
cue(type="list", t0=S("c05"), t1=E("c05") + 0.05, head="Discharge is not…", head_at=S("c05") + 0.05,
    items=[{"n": "≠", "text": "Bail: liberty while the case runs", "at": A("c05", "bail")}, {"n": "≠", "text": "Acquittal: after the trial", "at": A("c05", "acquittal")}])
cue(type="verdicts", t0=S("c06"), t1=A("c07", "so") - 0.05,
    rows=[{"text": "Judicial consideration and reasons", "ok": True, "at": A("c06", "judicial")},
          {"text": "The accused denies it", "ok": False, "at": A("c06", "denies"), "strike_at": A("c06", "allegation") + 0.3},
          {"text": "An application is filed", "ok": False, "at": A("c07", "filing"), "strike_at": A("c07", "either") + 0.15}])
cue(type="point", t0=A("c07", "so"), t1=E("c07") + 0.05, text="First: which court, which type of case?", icon="search-check", at=A("c07", "so"))

# ── 3 · Sessions cases ───────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c08"), t1=E("c08") + 0.05, text="A Sessions case, committed under § 232", icon="landmark", at=A("c08", "take"))
cue(type="section", t0=S("c09"), t1=E("c11") + 0.05, at=A("c09", "section"), act="BNSS", num="250", title="Discharge in a Sessions case",
    points=[{"text": "Apply within 60 days from commitment", "at": A("c09", "sixty")},
            {"text": "Record and documents; both sides heard", "at": A("c10", "record")},
            {"text": "No sufficient ground → discharge, with reasons", "at": A("c11", "discharge")}])
cue(type="section", t0=S("c12"), t1=E("c13") + 0.05, at=A("c12", "section"), act="BNSS", num="251(1)(b)", title="Framing the charge",
    points=[{"text": "Ground to presume an offence exclusively triable by Sessions", "at": A("c12", "presuming")},
            {"text": "Written charge within 60 days of the first hearing on charge", "at": A("c13", "sixty")}],
    note={"text": "Two clocks, two different starting points", "icon": "calendar", "at": A("c13", "different")})
cue(type="point", t0=S("c14"), t1=E("c14") + 0.05, text="Some High Courts: the window is directory. Still, apply in time", icon="triangle-alert", at=A("c14", "some"))

# ── 4 · Magistrate warrant cases on a police report ──────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c15"), t1=E("c16") + 0.05, at=A("c15", "section"), act="BNSS", num="262", title="Magistrate · warrant case · police report",
    points=[{"text": "Discharge application within 60 days", "at": A("c16", "sixty")},
            {"text": "…from supply of the documents under § 230", "at": A("c16", "supply")}])
cue(type="flow", t0=S("c17"), t1=E("c17") + 0.05,
    steps=[{"label": "Police report and papers", "icon": "file-text", "at": A("c17", "report")},
           {"label": "Both sides heard", "icon": "users", "at": A("c17", "hears")},
           {"label": "Groundless → discharge, with reasons", "icon": "gavel", "tone": "ok", "at": A("c17", "groundless")}])
cue(type="section", t0=S("c18"), t1=E("c18") + 0.05, at=A("c18", "section"), act="BNSS", num="263(1)", title="Framing the charge",
    points=[{"text": "Written charge within 60 days of the first hearing on charge", "at": A("c18", "sixty")}])
cue(type="point", t0=S("c19"), t1=E("c19") + 0.05, text="Here the discharge clock starts at document supply", icon="calendar", accent=True, at=A("c19", "clock"))

# ── 5 · which event starts which clock ───────────────────────────────────────────────────────────────────────────────────────────
cue(type="list", t0=S("c20"), t1=E("c22") + 0.05, head="Three triggers, three clocks", head_at=A("c20", "three"),
    items=[{"n": 1, "text": "1 June: committed → § 250", "at": A("c20", "committed")},
           {"n": 2, "text": "10 June: copies supplied → § 262", "at": A("c21", "supplied")},
           {"n": 3, "text": "1 July: first charge hearing → §§ 251, 263", "at": A("c22", "hearing")}])
cue(type="point", t0=S("c23"), t1=E("c23") + 0.05, text="One event per deadline: record the right one", icon="calendar", accent=True, at=A("c23", "record"))

# ── 6 · what a charge does ───────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c24"), t1=E("c25") + 0.05, at=A("c24", "charge"), act="BNSS", num="234 · 235", title="The charge: what must be answered",
    points=[{"text": "The offence", "at": A("c25", "offence")}, {"text": "The law", "at": A("c25", "law")},
            {"text": "Time and place", "at": A("c25", "time")}, {"text": "The person involved", "at": A("c25", "person")}])
cue(type="flow", t0=S("c26"), t1=E("c27") + 0.05,
    steps=[{"label": "Read and explained", "sub": "§§ 251(2), 263(2)", "icon": "book-open", "at": A("c26", "read")},
           {"label": "Plea asked", "icon": "message-square", "at": A("c26", "plea")},
           {"label": "Evidence, if contested", "icon": "scale", "tone": "ok", "at": A("c27", "evidence")}],
    note={"text": "Not a finding of guilt: the prosecution must prove its case", "icon": "triangle-alert", "at": A("c27", "framing")})

# ── 7 · no mini trial ────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="compare", t0=S("c28"), t1=E("c29") + 0.05, head="Two different stages", head_at=S("c28") + 0.05,
    cols=[{"title": "Charge stage", "icon": "search", "at": A("c28", "stage")}, {"title": "Guilt decision", "icon": "gavel", "at": A("c29", "proof")}],
    rows=[{"cells": ["A legally sufficient basis in the material", "Evidence tested at trial"], "cells_at": [A("c28", "material"), A("c29", "proof") + 0.3]},
          {"cells": ["Strong suspicion can justify a charge", "Proof beyond reasonable doubt"], "cells_at": [A("c29", "strong"), A("c29", "beyond")]}])
cue(type="verdicts", t0=S("c30"), t1=E("c31") + 0.05,
    rows=[{"text": "Apply the mind to the material", "ok": True, "at": A("c30", "apply")},
          {"text": "A mini trial: which witness is truthful?", "ok": False, "at": A("c30", "mini"), "strike_at": A("c30", "truthful") + 0.2},
          {"text": "A bare accusation is enough", "ok": False, "at": A("c31", "bare"), "strike_at": A("c31", "not") + 0.1}])
cue(type="point", t0=S("c32"), t1=E("c32") + 0.05, text="Screening ≠ deciding guilt", icon="scale", accent=True, at=A("c32", "supreme"))
cue(type="cite", t0=A("c32", "supreme"), t1=E("c32") + 0.05, at=A("c32", "supreme"), tag="SUPREME COURT OF INDIA",
    cases=[{"name": "Union of India v. Prafulla Kumar Samal", "cite": "(1979) 3 SCC 4"}, {"name": "Sajjan Kumar v. CBI", "cite": "(2010) 9 SCC 368"}])

# ── 8 · Arjun's case ─────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c33"), t1=E("c33") + 0.05, text="Arjun: accused of stealing a ₹60,000 laptop", icon="user-round", at=A("c33", "suppose"))
cue(type="compare", t0=S("c34"), t1=E("c36") + 0.05, head="Two files", head_at=S("c34") + 0.05,
    cols=[{"title": "File A", "icon": "file-text", "at": A("c34", "imagine")}, {"title": "File B", "icon": "file-check", "at": A("c35", "suppose")}],
    rows=[{"cells": ["Nothing links Arjun to the theft", "A witness account and supporting material"], "cells_at": [A("c34", "nothing"), A("c35", "witness")]},
          {"cells": ["Argue the charge is groundless", "Reliability needs evidence at trial"], "cells_at": [A("c35", "groundless"), A("c36", "reliability")]}])
cue(type="cite", t0=S("c34") + 0.3, t1=E("c36") + 0.05, at=S("c34") + 0.3, tag="ILLUSTRATION", text="A Magistrate's police-report warrant case: BNSS 262–263", icon="info")
cue(type="point", t0=S("c37"), t1=E("c37") + 0.05, text="The record decides: no outcome is guaranteed", icon="scale", accent=True, at=A("c37", "actual"))

# ── 9 · other case types ─────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c38"), t1=E("c38") + 0.05, text="These 60-day clocks are not for every case", icon="triangle-alert", at=A("c38", "do"))
cue(type="section", t0=S("c39"), t1=E("c41") + 0.05, at=A("c39", "warrant"), act="BNSS", num="267–269 · 274", title="Other case types",
    points=[{"text": "Other warrant cases: §§ 267–269", "at": A("c39", "sections")},
            {"text": "Summons cases: § 274, no formal charge", "at": A("c40", "summons")},
            {"text": "Groundless → release, with the effect of discharge", "at": A("c41", "proviso")}])
cue(type="cite", t0=S("c42"), t1=E("c42") + 0.05, at=S("c42"), tag="ALSO CHECK", text="Special courts and special statutes: their own rules", icon="book-open")

# ── 10 · act promptly ────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="compare", t0=S("c43"), t1=E("c43") + 0.05, head="Remember", head_at=S("c43") + 0.05,
    cols=[{"title": "Discharge", "icon": "scale", "at": A("c43", "discharge")}, {"title": "Framing charges", "icon": "gavel", "at": A("c43", "framing")}],
    rows=[{"cells": ["Should the case proceed?", "What must be answered?"], "cells_at": [A("c43", "whether"), A("c43", "identifies")]}],
    verdict={"text": "Neither is a finding of guilt", "icon": "triangle-alert", "at": A("c43", "neither")})
cue(type="list", t0=S("c44"), t1=E("c45") + 0.05, head="Act promptly", head_at=S("c44") + 0.05,
    items=[{"n": 1, "text": "Check the case type", "at": A("c44", "check")}, {"n": 2, "text": "Record the right trigger", "at": A("c44", "record")},
           {"n": 3, "text": "Raise discharge grounds early", "at": A("c44", "raise")}, {"n": 4, "text": "Too early? Ask for time, object", "at": A("c45", "ask")}])
