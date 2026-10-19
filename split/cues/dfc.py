# Discharge and Framing of Charges (BNSS): panel cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND).
# Storyboard: ~/Downloads/Discharge_and_Framing_of_Charges_BNSS_Storyboard.pdf. Fact-check 19-10-2026: sections and triggers right;
# reported Supreme Court authority on screen for the charge-stage test (Prafulla Kumar Samal (1979) 3 SCC 4; Sajjan Kumar v. CBI
# (2010) 9 SCC 368); laptop > Rs 20,000 (smaller thefts: summary trial); s.274 proviso mandatory; no "automatic 60-day stay".
# v2 19-10-2026: cues rebuilt for the fast energetic script (40 clips; c01-c03 = the rendered pilot); citations as in v1.
# v2 fact-check 19-10-2026: c12 step reads "Never gamble on it" (as spoken); c23-c24 note back to v1's "Not a finding of guilt".
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

STING = {"kicker": "CRIMINAL PROCEDURE · BNSS EXPLAINED", "title": "Discharge and Framing of Charges", "sub": "How the court screens a case before trial"}
ENDCARD = {"title": "Discharge and Framing of Charges", "line": "Charge sheet ≠ conviction", "sub": "Next lesson: Police Custody and Judicial Custody"}

# ── 1 · the court screens the case ───────────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=A("c01", "court") - 0.05, at=A("c01", "filed"), text="Charge sheet filed. A full trial now?", hl="A full trial now?")
cue(type="stamp", t0=A("c01", "not") - 0.05, t1=A("c01", "court") - 0.05, at=A("c01", "not"), line1="NOT", line2="AUTOMATICALLY")
cue(type="point", t0=A("c01", "court") - 0.05, t1=E("c01") + 0.05, text="Screening: where a sharp advocate can win early", icon="search", accent=True, at=A("c01", "court"))
cue(type="flow", t0=S("c02"), t1=E("c02") + 0.05, head="The real question", head_at=A("c02", "real"),
    steps=[{"label": "Enough material to proceed?", "icon": "search", "at": A("c02", "enough")},
           {"label": "If not: discharge", "icon": "scale", "tone": "ok", "at": A("c02", "not")}])
cue(type="list", t0=S("c03"), t1=E("c03") + 0.05, head="BNSS: 2 screening tools", head_at=S("c03") + 0.05,
    items=[{"n": 1, "text": "Discharge", "at": A("c03", "discharge")}, {"n": 2, "text": "Framing of charge", "at": A("c03", "framing")},
           {"n": "→", "text": "Know the court, section, deadline", "at": A("c03", "know")}, {"n": "=", "text": "No unnecessary trial", "at": A("c03", "spare")}])
cue(type="cite", t0=A("c03", "discharge"), t1=E("c03") + 0.05, at=A("c03", "discharge"), tag="BNSS", text="§§ 250–251 (Sessions) · §§ 262–263 (Magistrate, police report)", icon="book-open")

# ── 2 · what discharge means ─────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c04"), t1=E("c04") + 0.05, text="Discharge: proceeding is not justified, at this stage", icon="scale", accent=True, at=A("c04", "discharge"))
cue(type="compare", t0=S("c05"), t1=E("c05") + 0.05, head="Discharge is not…", head_at=S("c05") + 0.05,
    cols=[{"title": "Bail", "icon": "key-round", "at": A("c05", "bail")}, {"title": "Acquittal", "icon": "gavel", "at": A("c05", "acquittal")}],
    rows=[{"cells": ["Liberty while the case continues", "After trial"], "cells_at": [A("c05", "liberty"), A("c05", "trial")]}])
cue(type="verdicts", t0=S("c06"), t1=E("c06") + 0.05,
    rows=[{"text": "Judicial consideration + recorded reasons", "ok": True, "at": A("c06", "judicial")},
          {"text": "A denial alone", "ok": False, "at": A("c06", "denial"), "strike_at": A("c06", "get") + 0.1},
          {"text": "Simply filing an application", "ok": False, "at": A("c06", "simply"), "strike_at": A("c06", "an")}])

# ── 3 · Sessions cases ───────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c07"), t1=E("c07") + 0.05, text="An ordinary Sessions case, committed under § 232", icon="landmark", at=A("c07", "sessions"))
cue(type="counters", t0=S("c08"), t1=E("c08") + 0.05, head="§ 250: apply for discharge", head_at=S("c08") + 0.05,
    items=[{"value": 60, "unit": "DAYS", "label": "Discharge application", "sub": "from commitment · § 250(1)", "at": A("c08", "sixty")}])
cue(type="section", t0=S("c09"), t1=E("c09") + 0.05, at=A("c09", "judge"), act="BNSS", num="250(2)", title="Discharge in a Sessions case",
    points=[{"text": "Record and documents; both sides heard", "at": A("c09", "record")},
            {"text": "No sufficient ground → discharge, with reasons", "at": A("c09", "discharge")}])
cue(type="section", t0=S("c10"), t1=E("c10") + 0.05, at=A("c10", "but"), act="BNSS", num="251(1)(b)", title="Framing the charge",
    points=[{"text": "Ground to presume an offence only Sessions can try", "at": A("c10", "presume")},
            {"text": "A written charge is required", "at": A("c10", "written")}])
cue(type="counters", t0=S("c11"), t1=E("c11") + 0.05, head="The framing clock", head_at=S("c11") + 0.05,
    items=[{"value": 60, "unit": "DAYS", "label": "Frame the written charge", "sub": "from the first hearing on charge", "at": A("c11", "sixty")}],
    note={"text": "A different starting point", "icon": "calendar", "at": A("c11", "different")})
cue(type="flow", t0=S("c12"), t1=E("c12") + 0.05,
    steps=[{"label": "Some High Courts: directory", "sub": "the 60-day application window", "icon": "landmark", "at": A("c12", "some")},
           {"label": "Never gamble on it", "icon": "triangle-alert", "tone": "stop", "at": A("c12", "never")},
           {"label": "File within time", "icon": "calendar", "tone": "ok", "at": A("c12", "file")}])

# ── 4 · Magistrate warrant cases on a police report ──────────────────────────────────────────────────────────────────────────────
cue(type="kicker", t0=S("c13"), t1=E("c16") + 0.05, at=S("c13") + 0.05, text="DIFFERENT COURT · DIFFERENT CLOCK")
cue(type="section", t0=S("c13"), t1=E("c14") + 0.05, at=A("c13", "magistrate's"), act="BNSS", num="262", title="Magistrate · warrant case · police report",
    points=[{"text": "Apply for discharge within 60 days", "at": A("c14", "sixty")},
            {"text": "…from supply of the document copies under § 230", "at": A("c14", "supply")}])
cue(type="flow", t0=S("c15"), t1=E("c15") + 0.05, head="The Magistrate considers", head_at=S("c15") + 0.05,
    steps=[{"label": "Police report and papers", "icon": "file-text", "at": A("c15", "report")},
           {"label": "Both sides heard", "icon": "users", "at": A("c15", "hears")},
           {"label": "Groundless → discharge, with reasons", "icon": "gavel", "tone": "ok", "at": A("c15", "groundless")}])
cue(type="section", t0=S("c16"), t1=E("c16") + 0.05, at=A("c16", "test"), act="BNSS", num="263(1)", title="Framing the charge",
    points=[{"text": "Test for proceeding met", "at": A("c16", "met")},
            {"text": "Written charge within 60 days of the first hearing on charge", "at": A("c16", "sixty", 2)}])

# ── 5 · which event starts the clock ─────────────────────────────────────────────────────────────────────────────────────────────
cue(type="list", t0=S("c17"), t1=E("c19") + 0.05, head="Three dates, three clocks", head_at=A("c17", "three"),
    items=[{"n": 1, "text": "1 June: committed → § 250", "at": A("c17", "committed")},
           {"n": 2, "text": "10 June: copies supplied → § 262", "at": A("c18", "supplied")},
           {"n": 3, "text": "1 July: first charge hearing → §§ 251, 263", "at": A("c19", "hearing")}])
cue(type="verdicts", t0=S("c20"), t1=E("c20") + 0.05,
    rows=[{"text": "The correct trigger for each clock", "ok": True, "at": A("c20", "correct")},
          {"text": "The arrest · the FIR", "ok": False, "at": A("c20", "arrest"), "strike_at": A("c20", "r") + 0.15},
          {"text": "One date for every deadline", "ok": False, "at": A("c20", "one"), "strike_at": A("c20", "every")}])

# ── 6 · what a charge does ───────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c21"), t1=E("c22") + 0.05, at=A("c21", "court's"), act="BNSS", num="234 · 235", title="The court's formal statement of the offence",
    points=[{"text": "The offence and the law", "at": A("c22", "offence")}, {"text": "Time and place", "at": A("c22", "time")},
            {"text": "The person involved", "at": A("c22", "person")}],
    note={"text": "Check every particular", "icon": "search-check", "at": A("c22", "check")})
cue(type="flow", t0=S("c23"), t1=E("c24") + 0.05, head="Under §§ 251(2) and 263(2)", head_at=S("c23") + 0.05,
    steps=[{"label": "Read and explained", "icon": "book-open", "at": A("c23", "read")},
           {"label": "Guilty, or claims trial?", "icon": "message-square", "at": A("c23", "pleads")},
           {"label": "Evidence, if he claims trial", "icon": "scale", "tone": "ok", "at": A("c24", "evidence")}],
    note={"text": "Not a finding of guilt: the prosecution must prove its case", "icon": "triangle-alert", "at": A("c24", "charge")})

# ── 7 · no mini trial ────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c25"), t1=E("c25") + 0.05, at=A("c25", "does"), text="A legally sufficient basis to proceed?", hl="legally sufficient basis")
cue(type="compare", t0=S("c26"), t1=E("c26") + 0.05, head="Here is the line", head_at=S("c26") + 0.05,
    cols=[{"title": "Charge stage", "icon": "search", "at": A("c26", "strong")}, {"title": "Guilt decision", "icon": "gavel", "at": A("c26", "proof")}],
    rows=[{"cells": ["Strong suspicion, founded on the material, can justify a charge", "Proof beyond reasonable doubt"], "cells_at": [A("c26", "suspicion"), A("c26", "beyond")]}])
cue(type="verdicts", t0=S("c27"), t1=E("c28") + 0.05,
    rows=[{"text": "Apply its mind", "ok": True, "at": A("c27", "apply")},
          {"text": "A mini trial: which witness is truthful?", "ok": False, "at": A("c27", "mini"), "strike_at": A("c27", "truthful") + 0.1},
          {"text": "A bare accusation, without the ingredients", "ok": False, "at": A("c28", "bare"), "strike_at": A("c28", "enough")},
          {"text": "Test the material against every ingredient", "ok": True, "at": A("c28", "test")}])
cue(type="point", t0=S("c29"), t1=E("c29") + 0.05, text="Screening ≠ deciding guilt", icon="scale", accent=True, at=A("c29", "supreme"))
cue(type="cite", t0=A("c29", "supreme"), t1=E("c29") + 0.05, at=A("c29", "supreme"), tag="SUPREME COURT OF INDIA",
    cases=[{"name": "Union of India v. Prafulla Kumar Samal", "cite": "(1979) 3 SCC 4"}, {"name": "Sajjan Kumar v. CBI", "cite": "(2010) 9 SCC 368"}])

# ── 8 · Arjun's case ─────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c30"), t1=A("c30", "look") - 0.05, text="Arjun: accused of stealing a ₹60,000 laptop", icon="user-round", at=A("c30", "arjun"))
cue(type="compare", t0=A("c30", "look"), t1=E("c32") + 0.05, head="Two possible files", head_at=A("c30", "look"),
    cols=[{"title": "First file", "icon": "file-text", "at": A("c31", "first")}, {"title": "Second file", "icon": "file-check", "at": A("c32", "second")}],
    rows=[{"cells": ["At face value, nothing connects Arjun to the theft", "A witness account + supporting material"], "cells_at": [A("c31", "nothing"), A("c32", "witness")]},
          {"cells": ["Argue groundless: seek discharge", "A reliability dispute may need evidence at trial"], "cells_at": [A("c31", "argue"), A("c32", "reliability")]}])
cue(type="cite", t0=S("c31") + 0.3, t1=E("c32") + 0.05, at=S("c31") + 0.3, tag="ILLUSTRATION", text="A Magistrate's police-report warrant case: BNSS 262–263", icon="info")
cue(type="point", t0=S("c33"), t1=E("c33") + 0.05, text="The record decides: no outcome is guaranteed", icon="scale", accent=True, at=A("c33", "actual"))

# ── 9 · other case types ─────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="strike", t0=S("c34"), t1=A("c34", "warrant") - 0.05, text="These 60-day clocks fit every case", icon="calendar", at=S("c34") + 0.05, strike_at=A("c34", "not"))
cue(type="section", t0=A("c34", "warrant") - 0.05, t1=E("c35") + 0.05, at=A("c34", "warrant"), act="BNSS", num="267–269 · 274", title="Other case types",
    points=[{"text": "Warrant case, not on a police report: §§ 267–269", "at": A("c34", "sections")},
            {"text": "Summons case: § 274, generally no formal charge", "at": A("c35", "summons")},
            {"text": "The particulars are stated to the accused", "at": A("c35", "particulars")}])
cue(type="flow", t0=S("c36"), t1=E("c36") + 0.05, head="If the accusation is groundless", head_at=S("c36") + 0.05,
    steps=[{"label": "Reasons recorded", "icon": "file-pen-line", "at": A("c36", "record")},
           {"label": "Accused released", "icon": "user-round", "at": A("c36", "release")},
           {"label": "Effect of a discharge", "icon": "scale", "tone": "ok", "at": A("c36", "effect")}])
cue(type="point", t0=S("c37"), t1=E("c37") + 0.05, text="Special courts and statutes: check their rules first", icon="book-open", accent=True, at=A("c37", "special"))

# ── 10 · act promptly ────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="compare", t0=S("c38"), t1=E("c38") + 0.05, head="Remember", head_at=S("c38") + 0.05,
    cols=[{"title": "Discharge", "icon": "scale", "at": A("c38", "discharge")}, {"title": "The charge", "icon": "gavel", "at": A("c38", "charge")}],
    rows=[{"cells": ["Should the case proceed?", "What must be answered?"], "cells_at": [A("c38", "whether"), A("c38", "identifies")]}],
    verdict={"text": "Neither is a finding of guilt", "icon": "triangle-alert", "at": A("c38", "neither")})
cue(type="checklist", t0=S("c39"), t1=E("c39") + 0.05, head="Your checklist", head_at=S("c39") + 0.05,
    items=[{"n": 1, "text": "Check the case type", "at": A("c39", "check", 2)}, {"n": 2, "text": "Record the correct trigger", "at": A("c39", "record")},
           {"n": 3, "text": "Raise discharge grounds promptly", "at": A("c39", "raise")}])
cue(type="question", t0=S("c40"), t1=E("c40") + 0.05, at=A("c40", "moving"), text="Court moving to frame the charge too early?", hl="too early?")
cue(type="stamp", t0=A("c40", "ask") - 0.05, t1=E("c40") + 0.05, at=A("c40", "ask"), line1="ASK FOR TIME", line2="OBJECT ON RECORD")
