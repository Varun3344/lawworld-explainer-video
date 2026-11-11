# Charge Sheets and Closure Reports - CONCEPT VIDEO (legal-concept explainer, Cause of Action build): panel cues, run by
# split/build_course_plan.py (helpers: at S E cue fx have r3 PEND). Storyboard: ~/Downloads/Charge_Sheets_and_Closure_Reports_BNSS_Storyboard.pdf
# ("BNSS police reports, court powers and timelines explained", research-checked by the owner 19-10-2026).
# Held to the PDF's animation column and "Points to preserve":
#  - a case is shown by its LawWorld Citation ID only, never SCC / AIR / INSC. Bhagwant Singh v. Commissioner of Police (SC,
#    25.04.1985, Bhagwati, Sen and Madon JJ.; date checked on Indian Kanoon 07-11-2026) has NO confirmed LawWorld ID yet, so its
#    bar carries the name, date and para 4 only - add "LAWWORLD 1985 SC ####" once the ID is looked up. It is shown as decided under
#    the old Code of Criminal Procedure, as the narration says;
#  - the police report INFORMS the court and never replaces its decision; a charge sheet is the police assessment, not proof of
#    guilt; filing it is a different stage from the court framing charges (251 / 263 where applicable); "No automatic conviction"
#    stays on the stages card;
#  - Arjun is labelled ACCUSED throughout, never "thief" or "convict";
#  - s.190(1) proviso on screen: arrest is not a prerequisite for filing the report;
#  - closure: "untraced / unproven" is kept apart from "a false complaint"; closure is not a trial acquittal; NO "CLOSED" stamp
#    anywhere - a closure report does not end the case by itself, the court decides; one report may seek prosecution of some and
#    no action against others;
#  - the court's three options on a closure report + notice to the informant and a hearing (Bhagwant Singh); a protest petition
#    does not guarantee prosecution, a protest treated as a complaint follows the complaint procedure; no protest deadline shown;
#  - 193(2): the two-month period ONLY for BNS 64-68, 70-71 and POCSO 4, 6, 8, 10; 193(3)(ii) progress update within 90 days is
#    NOT a recurring duty and NOT a deadline to finish the investigation; 193(3)(iii) action taken told to the original informant;
#  - 187(3): 60 / 90 days depend on the offence (no thresholds on screen); default bail needs a timely claim and bail furnished;
#    expiry erases no FIR, bars no later charge sheet and frees no one automatically; bail consequence != end of the case;
#  - 230: free papers without delay, 14 days from the accused's PRODUCTION OR APPEARANCE (not the filing date); victim only if
#    represented by an advocate; exclusions, inspection of bulky papers, electronic supply;
#  - 193(9): a police report does not bar further investigation; permission + 90 days (extendable) apply to further investigation
#    DURING TRIAL; a further report adds to the earlier record and never replaces it automatically.
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

STING = {"kicker": "CRIMINAL PROCEDURE · BNSS EXPLAINED", "title": "Charge Sheets and Closure Reports",
         "sub": "Police reports, court powers and timelines"}
ENDCARD = {"title": "Charge Sheets and Closure Reports", "line": "The police recommend · the court decides",
           "sub": "LawWorld: legal research for advocates"}

# ── 1 · what follows the investigation ───────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "does"),
    text="“A charge sheet means guilt. A closure report ends the case.”", hl="ends the case.”", y=215)   # 07-11 layout gate: stamp clear below
cue(type="stamp", t0=A("c01", "wrong") - 0.05, t1=E("c01") + 0.05, at=A("c01", "wrong"), line1="BOTH WRONG", line2="THE COURT DECIDES", y=900)
cue(type="flow", t0=S("c02"), t1=E("c02") + 0.05, head="After the investigation", head_at=S("c02") + 0.05,
    steps=[{"label": "FIR registered", "sub": "the information is recorded", "icon": "file-text", "at": A("c02", "F")},
           {"label": "Investigation finished", "sub": "the police gather the material", "icon": "search", "at": A("c02", "finished")},
           {"label": "The police report", "sub": "what happens next?", "icon": "file-check", "tone": "ok", "at": A("c02", "what")}])
cue(type="splitcard", t0=S("c03"), t1=E("c03") + 0.05,
    left={"title": "CHARGE SHEET", "text": "recommends prosecution", "icon": "file-text", "at": A("c03", "charge")},
    right={"title": "CLOSURE REPORT", "text": "recommends that the case should not proceed", "icon": "file-check", "at": A("c03", "closure")})
cue(type="flow", t0=S("c04"), t1=A("c04", "does") - 0.05, head="Under the BNSS", head_at=A("c04", "under"),
    steps=[{"label": "The police report", "sub": "charge sheet or closure report", "icon": "file-text", "at": A("c04", "police")},
           {"label": "Informs the Magistrate", "sub": "the court considers it", "icon": "landmark", "tone": "ok", "at": A("c04", "informs")}])
cue(type="notequal", t0=A("c04", "does"), t1=E("c04") + 0.05, left="The police report", right="the court's decision",
    at=A("c04", "does"), left_at=A("c04", "does"),
    sub="It informs the court; the court decides", sub_at=A("c04", "replace"))
cue(type="cite", t0=S("c03") + 0.3, t1=E("c04") + 0.05, at=S("c03") + 0.3, tag="ON THE RECORD", text="BNSS 193(3) · 210(1)(b)", icon="book-open")

# ── 2 · what a charge sheet contains ─────────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c05"), t1=E("c05") + 0.05, at=A("c05", "section"), act="BNSS, 2023", num="193(3)",
    title="The police report goes to the Magistrate",
    points=[{"text": "Sent to the Magistrate", "at": A("c05", "sent")},
            {"text": "When the investigation is completed", "at": A("c05", "investigation")}],
    note={"text": "Arrest is not a filing prerequisite: s. 190(1) proviso", "icon": "info", "at": A("c05", "completed")})
cue(type="list", t0=S("c06"), t1=E("c07") + 0.05, head="Inside the charge sheet", head_at=S("c06") + 0.05,
    items=[{"n": 1, "text": "The parties", "at": A("c06", "parties")},
           {"n": 2, "text": "The allegations", "at": A("c06", "allegations")},
           {"n": 3, "text": "The witnesses", "at": A("c06", "witnesses")},
           {"n": 4, "text": "Findings: does an offence appear, and by whom?", "at": A("c07", "offence")},
           {"n": 5, "text": "Supporting material: documents and statements", "at": A("c07", "documents")}])
cue(type="flow", t0=S("c08"), t1=E("c08") + 0.05, head="Separate stages", head_at=S("c08") + 0.05,
    steps=[{"label": "Police report", "sub": "the police assessment", "icon": "file-text", "at": A("c08", "police")},
           {"label": "Court considers it", "sub": "s. 210(1)(b)", "icon": "landmark", "at": A("c08", "filing")},
           {"label": "Charge stage", "sub": "251 or 263, where applicable", "icon": "gavel", "at": A("c08", "framing")},
           {"label": "Trial", "sub": "the evidence is tested", "icon": "scale", "tone": "ok", "at": A("c08", "charges") + 0.35}],
    note={"text": "No automatic conviction", "icon": "alert-triangle", "at": A("c08", "neither")})
cue(type="cite", t0=S("c08") + 0.3, t1=E("c08") + 0.05, at=S("c08") + 0.3, tag="ON THE RECORD",   # 07-11: not under the 5-item list
    text="BNSS 193(3)(i), 193(6), 210(1)(b) · charge: 251 or 263, where applicable", icon="book-open")

# ── 3 · example: a theft investigation ───────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c09"), t1=E("c09") + 0.05, head="An illustration: Ravi's laptop", head_at=S("c09") + 0.05,
    steps=[{"label": "Ravi reports the theft", "sub": "his laptop is stolen", "icon": "file-text", "at": A("c09", "ravi")},
           {"label": "CCTV footage", "sub": "examined by the police", "icon": "video", "at": A("c09", "examine")},
           {"label": "Witness accounts", "sub": "the police speak to them", "icon": "users", "at": A("c09", "speak")}])
cue(type="equation", t0=S("c10"), t1=E("c10") + 0.05,
    terms=[{"text": "CCTV + WITNESS ACCOUNTS", "at": A("c10", "they")},
           {"op": "+", "text": "RECOVERY RECORD", "at": A("c10", "recover")},
           {"op": "=", "text": "CHARGE SHEET", "result": True, "at": A("c10", "charge")}])
cue(type="splitcard", t0=S("c11"), t1=E("c11") + 0.05,
    left={"title": "ARJUN · ACCUSED", "text": "can challenge the allegation and the evidence", "icon": "user-round", "at": A("c11", "arjun")},
    right={"title": "THE COURT", "text": "plays its own role: it examines the file independently", "icon": "landmark", "at": A("c11", "court")})
cue(type="cite", t0=S("c09") + 0.3, t1=E("c09") + 0.05, at=S("c09") + 0.3, tag="ILLUSTRATION", text="A hypothetical theft · BNSS 193 and 210", icon="info")
cue(type="cite", t0=S("c10") + 0.3, t1=E("c11") + 0.05, at=S("c10") + 0.3, tag="ILLUSTRATION",
    text="Arjun is the ACCUSED: a charge sheet is not proof of guilt", icon="info")

# ── 4 · when police recommend closure ────────────────────────────────────────────────────────────────────────────────────────────
cue(type="equation", t0=S("c12"), t1=A("c13", "other") - 0.05,
    terms=[{"text": "UNCLEAR FOOTAGE", "at": A("c12", "footage")},
           {"op": "+", "text": "NO RECOVERY · NOT ENOUGH MATERIAL", "at": A("c12", "recovered")},
           {"op": "=", "text": "REASONED CLOSURE RECOMMENDATION", "result": True, "at": A("c13", "closure")}])
cue(type="point", t0=A("c13", "other"), t1=E("c13") + 0.05, text="Other cases: the police may conclude no offence occurred",
    icon="search", accent=True, at=A("c13", "other"))
cue(type="cite", t0=S("c13") + 0.3, t1=E("c13") + 0.05, at=S("c13") + 0.3, tag="NOTE",
    text="Terms vary: one report may seek prosecution of some, and no action against others", icon="info")
cue(type="notequal", t0=S("c14"), t1=E("c14") + 0.05, left="Untraced or unproven", right="a false complaint",
    at=A("c14", "reasons"), left_at=A("c14", "untraced"),
    sub="Lack of proof does not show Ravi's complaint was false", sub_at=A("c14", "automatically"))
cue(type="verdicts", t0=S("c15"), t1=E("c15") + 0.05,
    rows=[{"text": "A recommendation for the court to consider", "ok": True, "at": A("c15", "recommendation")},
          {"text": "An acquittal after trial", "ok": False, "at": A("c15", "acquittal"), "strike_at": A("c15", "trial") + 0.2},
          {"text": "An automatic end to the case", "ok": False, "at": A("c15", "automatic"), "strike_at": A("c15", "further")}])
cue(type="cite", t0=S("c15") + 0.3, t1=E("c15") + 0.05, at=S("c15") + 0.3, tag="BNSS 193(3)",
    text="Nothing is closed until the court considers the report", icon="book-open")

# ── 5 · the court and the informant ──────────────────────────────────────────────────────────────────────────────────────────────
cue(type="list", t0=S("c16"), t1=E("c17") + 0.05, head="The Magistrate is not bound", head_at=A("c16", "magistrate"),
    items=[{"n": 1, "text": "Accept closure, and drop proceedings", "at": A("c16", "accept")},
           {"n": 2, "text": "Disagree, and take cognizance on sufficient material", "at": A("c16", "disagree")},
           {"n": 3, "text": "Direct further investigation", "at": A("c17", "direct")},
           {"n": "!", "text": "It cannot compel the police to a view on prosecution", "at": A("c17", "compel")}])
cue(type="cite", t0=S("c16") + 0.3, t1=A("c17", "but") - 0.05, at=S("c16") + 0.3, tag="BNSS", text="210(1)(b) · 175(3) · 193(9)", icon="book-open")
cue(type="flow", t0=S("c18"), t1=E("c19") + 0.05, head="Before closure is accepted", head_at=S("c18") + 0.05,
    steps=[{"label": "Notice to the informant", "sub": "Ravi, who gave the information", "icon": "mail", "at": A("c18", "informant")},
           {"label": "An opportunity to be heard", "sub": "when the report is considered", "icon": "message-square", "at": A("c18", "opportunity")},
           {"label": "Then the court decides", "sub": "accept closure, or not", "icon": "landmark", "tone": "ok", "at": A("c18", "heard")}],
    note={"text": "Decided under the old Code of Criminal Procedure", "icon": "info", "at": A("c19", "old")})
cue(type="cite", t0=A("c19", "supreme"), t1=E("c19") + 0.05, at=A("c19", "supreme"), tag="SUPREME COURT OF INDIA · 25.04.1985",
    cases=[{"name": "Bhagwant Singh v. Commissioner of Police and Another", "cite": "para 4"}])
cue(type="flow", t0=S("c20"), t1=E("c20") + 0.05, head="Ravi's objections", head_at=S("c20") + 0.05,
    steps=[{"label": "Ravi files objections", "sub": "commonly called a protest petition", "icon": "file-pen-line", "at": A("c20", "objections")},
           {"label": "An overlooked witness", "sub": "for example, one the police missed", "icon": "search", "at": A("c20", "witness")}])
cue(type="verdicts", t0=S("c21"), t1=E("c21") + 0.05,
    rows=[{"text": "The court chooses the lawful course", "ok": True, "at": A("c21", "court")},
          {"text": "Objections guarantee prosecution", "ok": False, "at": A("c21", "objections"), "strike_at": A("c21", "guarantee") + 0.3},
          {"text": "A protest treated as a complaint: the complaint procedure", "ok": True, "at": A("c21", "protest")}])

# ── 6 · investigation timelines are different ────────────────────────────────────────────────────────────────────────────────────
# the stamp holds to "Three" (not "Section"): "No. Section" left it 0.4 s, too short for its 0.6 s landing
cue(type="question", t0=S("c22"), t1=A("c22", "three") - 0.05, at=A("c22", "every"),
    text="Every charge sheet due within 90 days?", hl="90 days?", y=260)
cue(type="stamp", t0=A("c22", "no") - 0.05, t1=A("c22", "three") - 0.05, at=A("c22", "no"), line1="NO", y=760)
cue(type="section", t0=A("c22", "three") - 0.05, t1=E("c22") + 0.05, at=A("c22", "three"), act="BNSS, 2023", num="193(1)",
    title="Every investigation",
    points=[{"text": "Without unnecessary delay", "at": A("c22", "unnecessary")}])
cue(type="counters", t0=S("c23"), t1=E("c23") + 0.05, head="Sub-section (2): listed offences only", head_at=S("c23") + 0.05,
    items=[{"value": 2, "unit": "MONTHS", "label": "Investigation period", "sub": "from recording the information", "at": A("c23", "months")}],
    note={"text": "Only the listed offences, never every offence", "icon": "info", "at": A("c23", "only")})
cue(type="cite", t0=S("c23") + 0.3, t1=E("c23") + 0.05, at=S("c23") + 0.3, tag="BNSS 193(2)", text="BNS 64–68, 70–71 · POCSO Act 4, 6, 8, 10", icon="book-open")
cue(type="counters", t0=S("c24"), t1=E("c24") + 0.05, head="Sub-section (3)(ii): a progress update", head_at=S("c24") + 0.05,
    items=[{"value": 90, "unit": "DAYS", "label": "Progress update", "sub": "to the informant or victim", "at": A("c24", "progress")}],
    note={"text": "Not a recurring 90-day duty", "icon": "info", "at": A("c24", "victim")})
cue(type="section", t0=S("c25"), t1=E("c25") + 0.05, at=A("c25", "action"), act="BNSS, 2023", num="193(3)(iii)",
    title="The action taken is communicated",
    points=[{"text": "To the original informant", "at": A("c25", "communicated")}])
cue(type="notequal", t0=S("c26"), t1=E("c26") + 0.05, left="The 90-day update", right="a deadline to finish",
    at=A("c26", "update"), left_at=A("c26", "update"),
    sub="Identify the offence, and its own timeline", sub_at=A("c26", "always"))

# ── 7 · 60 or 90 days and default bail ───────────────────────────────────────────────────────────────────────────────────────────
cue(type="counters", t0=S("c27"), t1=E("c27") + 0.05, head="Section 187(3): detention limits", head_at=S("c27") + 0.05,
    items=[{"value": 60, "unit": "DAYS", "label": "Detention limit", "sub": "for some offences", "at": A("c27", "sixty")},
           {"value": 90, "unit": "DAYS", "label": "Detention limit", "sub": "for others: check the offence", "at": A("c27", "ninety")}],
    note={"text": "Investigation detention and default bail", "icon": "info", "at": A("c27", "concern")})
cue(type="cite", t0=S("c28") + 0.3, t1=E("c28") + 0.05, at=S("c28") + 0.3, tag="BNSS 187(3)",   # 07-11: not under the counters note
    text="Read with Explanation I · check the offence, case law and any special law", icon="book-open")
cue(type="flow", t0=S("c28"), t1=E("c28") + 0.05, head="If the limit runs out", head_at=S("c28") + 0.05,
    steps=[{"label": "No required report in time", "sub": "60 or 90 days, as applicable", "icon": "clock", "tone": "warn", "at": A("c28", "report")},
           {"label": "Default bail may be claimed", "sub": "by an accused in custody", "icon": "key-round", "at": A("c28", "claim")},
           {"label": "Subject to conditions", "sub": "a timely claim · bail furnished", "icon": "check", "tone": "ok", "at": A("c28", "timely")}])
cue(type="verdicts", t0=S("c29"), t1=E("c29") + 0.05,
    rows=[{"text": "Erases the FIR", "ok": False, "at": A("c29", "erase"), "strike_at": A("c29", "or")},
          {"text": "Bars a later charge sheet", "ok": False, "at": A("c29", "bar"), "strike_at": A("c29", "sheet")},
          {"text": "Frees anyone who has not claimed bail and met the conditions", "ok": False, "at": A("c29", "releases"), "strike_at": A("c29", "claimed")}])
cue(type="cite", t0=A("c29", "and"), t1=E("c29") + 0.05, at=A("c29", "and"), tag="REMEMBER",
    text="The bail consequence is different from the end of the case: the investigation goes on", icon="scale")

# ── 8 · copies for the defence and victim ────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c30"), t1=E("c30") + 0.05, at=A("c30", "cases"), act="BNSS, 2023", num="230",
    title="Free copies for the accused",
    points=[{"text": "In cases instituted on a police report", "at": A("c30", "instituted")},
            {"text": "Specified papers, free, without delay", "at": A("c30", "specified")}])
cue(type="counters", t0=S("c31"), t1=E("c31") + 0.05, head="The 14-day clock", head_at=S("c31") + 0.05,
    items=[{"value": 14, "unit": "DAYS", "label": "Free copies supplied", "sub": "from the accused's production or appearance", "at": A("c31", "fourteen")}],
    note={"text": "Not from the date the report is filed", "icon": "calendar", "at": A("c31", "clock")})
cue(type="list", t0=S("c32"), t1=E("c32") + 0.05, head="Who gets them, and what", head_at=S("c32") + 0.05,
    items=[{"n": "+", "text": "A victim represented by an advocate", "at": A("c32", "victim")},
           {"n": 1, "text": "The police report", "at": A("c32", "police")},
           {"n": 2, "text": "The FIR", "at": A("c32", "F")},
           {"n": 3, "text": "Relevant statements and documents", "at": A("c32", "statements")}])
cue(type="checklist", t0=S("c33"), t1=E("c33") + 0.05, head="Safeguards", head_at=S("c33") + 0.05,
    items=[{"n": 1, "text": "Statutory exclusions apply", "at": A("c33", "exclusions")},
           {"n": 2, "text": "Bulky papers: inspection instead of copies", "at": A("c33", "bulky")},
           {"n": 3, "text": "Electronic supply counts", "at": A("c33", "electronic")}])
cue(type="cite", t0=S("c33") + 0.3, t1=E("c33") + 0.05, at=S("c33") + 0.3, tag="ON THE RECORD", text="BNSS 230, read with 193(6)–(8)", icon="book-open")

# ── 9 · new evidence and a supplementary report ──────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c34"), t1=A("c34", "under") - 0.05, text="A police report does not bar further investigation",
    icon="search", accent=True, at=A("c34", "police"))
cue(type="section", t0=A("c34", "under") - 0.05, t1=E("c34") + 0.05, at=A("c34", "under"), act="BNSS, 2023", num="193(9)",
    title="Further investigation",
    points=[{"text": "New evidence can lead to a supplementary report", "at": A("c34", "evidence")}])
cue(type="flow", t0=S("c35"), t1=E("c35") + 0.05, head="During trial: a separate rule", head_at=A("c35", "during"),
    steps=[{"label": "Trial court's permission", "sub": "needed first", "icon": "gavel", "at": A("c35", "permission")},
           {"label": "90 days", "sub": "to complete it", "icon": "clock", "at": A("c35", "ninety")},
           {"label": "Extendable", "sub": "with that court's permission", "icon": "calendar", "tone": "ok", "at": A("c35", "extendable")}])
cue(type="cite", t0=S("c35") + 0.3, t1=E("c35") + 0.05, at=S("c35") + 0.3, tag="BNSS 193(9)",
    text="Permission and 90 days: expressly for further investigation during trial", icon="book-open")
cue(type="flow", t0=S("c36"), t1=E("c36") + 0.05, head="For Ravi", head_at=S("c36") + 0.05,
    steps=[{"label": "A new recording", "sub": "discovered later", "icon": "video", "at": A("c36", "recording")},
           {"label": "Lawful further investigation", "sub": "of evidence unavailable earlier", "icon": "search", "at": A("c36", "justify")},
           {"label": "Supplementary report", "icon": "file-text", "tone": "ok", "at": A("c36", "unavailable")}])
cue(type="verdicts", t0=S("c37"), t1=E("c37") + 0.05,
    rows=[{"text": "Adds to the earlier record", "ok": True, "at": A("c37", "adds")},
          {"text": "Replaces it automatically", "ok": False, "at": A("c37", "automatically"), "strike_at": A("c37", "replace")}])

# ── 10 · remember the difference ─────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="compare", t0=S("c38"), t1=E("c38") + 0.05, head="Remember the difference", head_at=S("c38") + 0.05,
    cols=[{"title": "Charge sheet", "icon": "file-text", "at": A("c38", "charge")},
          {"title": "Closure report", "icon": "file-check", "at": A("c38", "closure")}],
    rows=[{"cells": ["Prosecution recommended", "Closure recommended"], "cells_at": [A("c38", "prosecution"), A("c38", "closure", 2)]}],
    verdict={"text": "Either way, the court decides the next step", "icon": "scale", "at": A("c38", "either")})
cue(type="point", t0=S("c39"), t1=A("c39", "check") - 0.05, text="The informant is heard before closure is accepted",
    icon="users", accent=True, at=A("c39", "informant"))
cue(type="timeline", t0=A("c39", "check") - 0.05, t1=E("c39") + 0.05,
    nodes=[{"label": "LISTED OFFENCES", "value": "2 months", "sub": "BNSS 193(2)", "at": A("c39", "check")},
           {"label": "DEFAULT BAIL", "value": "60 / 90 days", "sub": "BNSS 187(3)", "at": A("c39", "deadline")},
           {"label": "FREE COPIES", "value": "14 days", "sub": "BNSS 230", "at": A("c39", "separately")},
           {"label": "FURTHER INVESTIGATION", "value": "90 days", "sub": "during trial · 193(9)", "at": A("c39", "get")}])
cue(type="cite", t0=A("c39", "get"), t1=E("c39") + 0.05, at=A("c39", "get"), tag="THEN",
    text="Get the relevant papers · respond to notices promptly", icon="check")
cue(type="point", t0=S("c40"), t1=E("c40") + 0.05, text="Like · Share · Subscribe · lawworld.ai",
    icon="check", accent=True, at=A("c40", "like"))
