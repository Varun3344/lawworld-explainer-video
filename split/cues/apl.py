# Criminal Appeals and Revisions (BNSS): panel cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND).
# Storyboard: ~/Downloads/Criminal_Appeals_and_Revisions_BNSS_Storyboard.pdf. Fact-check 19-10-2026: no errors; 430(1) proviso
# (prosecutor heard in writing for death / life / >= 10 years) and 430(3) added; "interlocutory" per 438(2), the "legal character"
# test from Amar Nath (1977) 4 SCC 137 and Madhu Limaye (1977) 4 SCC 551; Limitation Act Art. 115(b) 60/30 days, Art. 131 90 days.
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

STING = {"kicker": "CRIMINAL PROCEDURE · BNSS EXPLAINED", "title": "Appeals and Revisions", "sub": "Which remedy, which court, which deadline?"}
ENDCARD = {"title": "Appeals and Revisions", "line": "Appeal ≠ revision", "sub": "Next lesson: Discharge and Framing of Charges"}

# ── 1 · appeal or revision? ──────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="compare", t0=S("c01"), t1=E("c02") + 0.05, head="Two cases", head_at=S("c01") + 0.1,
    cols=[{"title": "Ravi", "icon": "user-round", "at": A("c01", "ravi")}, {"title": "Meera", "icon": "user-round", "at": A("c02", "meera")}],
    rows=[{"cells": ["Convicted", "A lower court's order"], "cells_at": [A("c01", "convicted"), A("c02", "lower")]},
          {"cells": ["Evidence misunderstood?", "Legal power exceeded?"], "cells_at": [A("c01", "misunderstood"), A("c02", "beyond")]}],
    verdict={"text": "Another trial for both?", "icon": "circle-help", "at": A("c02", "can")})
cue(type="splitcard", t0=S("c03"), t1=A("c03", "and", 2) - 0.05,
    left={"title": "APPEAL", "text": "challenge the decision", "icon": "scale", "at": A("c03", "appeal")},
    right={"title": "REVISION", "text": "a supervisory check", "icon": "search", "at": A("c03", "revision")})
cue(type="list", t0=A("c03", "and", 2), t1=E("c04") + 0.05, head="Get three things right", head_at=A("c03", "and", 2),
    items=[{"n": 1, "text": "The remedy", "at": A("c03", "remedy")}, {"n": 2, "text": "The court", "at": A("c03", "court")},
           {"n": 3, "text": "The deadline", "at": A("c03", "deadline")}])
cue(type="cite", t0=A("c04", "under"), t1=E("c04") + 0.05, at=A("c04", "under"), tag="BNSS", text="Chapter XXXI: Appeals · Chapter XXXII: Reference and Revision", icon="book-open")

# ── 2 · appeal: a right by statute ───────────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c05"), t1=E("c05") + 0.05, at=A("c05", "section"), act="BNSS", num="413", title="No appeal unless the law provides one")
cue(type="compare", t0=S("c06"), t1=E("c08") + 0.05, head="The ordinary route", head_at=S("c06") + 0.05,
    cols=[{"title": "Convicted by", "icon": "gavel", "at": A("c06", "conviction")}, {"title": "Appeal lies to", "icon": "landmark", "at": A("c06", "goes")}],
    rows=[{"cells": ["A Magistrate", "The Sessions Court · § 415(3)"], "cells_at": [A("c06", "magistrate"), A("c06", "sessions")]},
          {"cells": ["A Sessions or Additional Sessions Judge", "The High Court · § 415(2)"], "cells_at": [A("c07", "sessions"), A("c07", "high")]}],
    verdict={"text": "Ravi: Magistrate → Sessions", "icon": "arrow-right", "at": A("c08", "ravi's")})
cue(type="section", t0=S("c09"), t1=E("c10") + 0.05, at=A("c09", "but"), act="BNSS", num="416 · 417", title="Restricted appeals",
    points=[{"text": "After a plea of guilty (§ 416)", "tone": "no", "at": A("c09", "guilty")}, {"text": "In petty cases (§ 417)", "tone": "no", "at": A("c09", "petty")}],
    note={"text": "Always check whether the decision is appealable", "icon": "search-check", "at": A("c10", "always")})

# ── 3 · what an appeal examines ──────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c11"), t1=E("c11") + 0.05, text="Facts and law, within the permitted scope", icon="scale", at=A("c11", "appeal"))
cue(type="flow", t0=S("c12"), t1=E("c12") + 0.05, head="Ravi's appeal", head_at=S("c12") + 0.05,
    steps=[{"label": "His ground", "sub": "no identification in darkness", "icon": "triangle-alert", "at": A("c12", "eyewitness")},
           {"label": "The trial record", "sub": "testimony, lighting, judgment", "icon": "file-text", "at": A("c12", "record")},
           {"label": "Appellate examination", "icon": "search", "tone": "ok", "at": A("c12", "grounds")}])
cue(type="section", t0=S("c13"), t1=E("c14") + 0.05, at=A("c13", "section"), act="BNSS", num="427", title="What the appellate court may do",
    points=[{"text": "Dismiss the appeal", "at": A("c13", "dismissing")}, {"text": "Reverse the conviction", "at": A("c13", "reversing")},
            {"text": "Order a retrial", "at": A("c13", "retrial")}, {"text": "Alter the finding or sentence, within limits", "at": A("c14", "alter")}])
cue(type="point", t0=S("c15"), t1=E("c15") + 0.05, text="A real opportunity, never a guaranteed result", icon="scale", accent=True, at=A("c15", "appeal"))

# ── 4 · deadlines ────────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="kicker", t0=S("c16"), t1=E("c19") + 0.05, at=S("c16") + 0.05, text="ORDINARY CONVICTION APPEALS")
cue(type="counters", t0=S("c17"), t1=E("c19") + 0.05, head="Ordinary filing periods", head_at=S("c17") + 0.05,
    items=[{"value": 30, "unit": "DAYS", "label": "Appeal to Sessions", "sub": "Limitation Act, Art. 115(b)", "at": A("c17", "thirty")},
           {"value": 60, "unit": "DAYS", "label": "Appeal to the High Court", "sub": "Art. 115(b)", "at": A("c17", "sixty")},
           {"value": 90, "unit": "DAYS", "label": "Revision", "sub": "Art. 131", "at": A("c19", "ninety")}],
    note={"text": "From the sentence or order: the Limitation Act, not the BNSS", "icon": "calendar", "at": A("c18", "article")})
cue(type="checklist", t0=S("c20"), t1=E("c20") + 0.05, head="Check these separately", head_at=S("c20") + 0.05,
    items=[{"n": 1, "text": "Acquittal appeals", "at": A("c20", "acquittal")}, {"n": 2, "text": "Victim appeals", "at": A("c20", "victim")},
           {"n": 3, "text": "Death sentences", "at": A("c20", "death")}, {"n": 4, "text": "Supreme Court", "at": A("c20", "supreme")},
           {"n": 5, "text": "Special statutes", "at": A("c20", "special")}])

# ── 5 · copies and delay ─────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c21"), t1=E("c22") + 0.05, at=A("c21", "section"), act="LIMITATION ACT", num="12", title="Time excluded",
    points=[{"text": "The day from which the period runs", "at": A("c21", "relevant")},
            {"text": "Time legally required to obtain specified copies", "at": A("c22", "time")}])
cue(type="point", t0=S("c23"), t1=E("c23") + 0.05, text="Apply for the certified copy promptly; keep the dates", icon="calendar", at=A("c23", "apply"))
cue(type="section", t0=S("c24"), t1=E("c25") + 0.05, at=A("c24", "section"), act="LIMITATION ACT", num="5", title="Condonation of delay",
    points=[{"text": "Only when sufficient cause is shown", "at": A("c24", "sufficient")},
            {"text": "The court decides: never automatic", "at": A("c25", "decision")}])

# ── 6 · does filing stop the sentence? ───────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c26"), t1=E("c26") + 0.05, at=A("c26", "does"), text="Does filing stop the sentence?", hl="stop the sentence?")
cue(type="stamp", t0=A("c26", "no") - 0.05, t1=E("c26") + 0.05, at=A("c26", "no"), line1="NO", line2="NOT BY ITSELF")
cue(type="section", t0=S("c27"), t1=E("c28") + 0.05, at=A("c27", "section"), act="BNSS", num="430(1)", title="Suspension pending appeal",
    points=[{"text": "The appellate court may suspend execution, with written reasons", "at": A("c27", "suspend")},
            {"text": "Release on bail, or on his own bond", "at": A("c28", "release")}])
cue(type="point", t0=S("c29"), t1=E("c29") + 0.05, text="Death, life or 10+ years: the Public Prosecutor objects in writing first", icon="gavel", at=A("c29", "offences"))
cue(type="section", t0=S("c30"), t1=E("c30") + 0.05, at=A("c30", "if"), act="BNSS", num="430(3)", title="Short sentences: bail from the trial court",
    points=[{"text": "On bail, and three years or less", "at": A("c30", "three")},
            {"text": "Bail to file the appeal, unless special reasons", "at": A("c30", "unless")}])
cue(type="point", t0=S("c31"), t1=A("c31", "keep") - 0.05, text="Seek the interim order", icon="file-pen-line", accent=True, at=A("c31", "seek"))
cue(type="compare", t0=A("c31", "keep"), t1=E("c32") + 0.05, head="Two separate questions", head_at=A("c31", "keep"),
    cols=[{"title": "The conviction", "icon": "scale", "at": A("c32", "conviction")}, {"title": "The sentence", "icon": "hourglass", "at": A("c32", "execution")}],
    rows=[{"cells": ["Should it be overturned?", "Suspended while the appeal is pending?"], "cells_at": [A("c32", "overturned"), A("c32", "suspended")]}])

# ── 7 · revision ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c33"), t1=E("c35") + 0.05, at=A("c33", "section"), act="BNSS", num="438", title="Revision: calling for the record",
    points=[{"text": "Sessions Judge or High Court", "at": A("c33", "sessions")},
            {"text": "Correctness, legality, propriety, regularity", "at": A("c34", "correctness")}],
    note={"text": "The revisional powers: §§ 440 and 442", "icon": "book-open", "at": A("c35", "sections")})
cue(type="flow", t0=S("c36"), t1=E("c37") + 0.05, head="Meera's revision", head_at=S("c36") + 0.05,
    steps=[{"label": "Her ground", "sub": "the court lacked legal authority", "icon": "user-round", "at": A("c36", "meera")},
           {"label": "Maintainable?", "sub": "check it first", "icon": "search", "at": A("c37", "maintainable")},
           {"label": "Revision may address it", "icon": "badge-check", "tone": "ok", "at": A("c37", "address")}])
cue(type="notequal", t0=S("c38"), t1=E("c38") + 0.05, left="A supervisory remedy", right="a second appeal", at=A("c38", "routine"),
    left_at=A("c38", "discretionary"), sub="Not for re-arguing all the evidence", sub_at=A("c38", "arguing"))

# ── 8 · limits of revision ───────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="verdicts", t0=S("c39"), t1=E("c44") + 0.05,
    rows=[{"text": "Interlocutory orders · § 438(2)", "ok": False, "at": A("c39", "interlocutory") - 0.2, "strike_at": E("c39") - 0.2},
          {"text": "A second revision by the same person", "ok": False, "at": A("c41", "another"), "strike_at": A("c41", "high")},
          {"text": "An available appeal left unfiled · § 442(4)", "ok": False, "at": A("c42", "available"), "strike_at": A("c42", "unfiled") + 0.3},
          {"text": "Acquittal turned into conviction · § 442(3)", "ok": False, "at": A("c43", "acquittal"), "strike_at": A("c43", "conviction") + 0.3}])
cue(type="cite", t0=A("c40", "supreme"), t1=E("c40") + 0.05, at=A("c40", "supreme"), tag="SUPREME COURT OF INDIA · WHAT IS INTERLOCUTORY",
    cases=[{"name": "Amar Nath v. State of Haryana", "cite": "(1977) 4 SCC 137"}, {"name": "Madhu Limaye v. State of Maharashtra", "cite": "(1977) 4 SCC 551"}])
cue(type="cite", t0=S("c44"), t1=E("c44") + 0.05, at=S("c44"), tag="REMEMBER", text="Revision is not a shortcut around appeal restrictions", icon="triangle-alert")

# ── 9 · victim and State appeals ─────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c45"), t1=E("c46") + 0.05, at=A("c45", "proviso"), act="BNSS", num="413 proviso", title="The victim's right of appeal",
    points=[{"text": "Against an acquittal", "at": A("c46", "acquittal")}, {"text": "Conviction for a lesser offence", "at": A("c46", "lesser")},
            {"text": "Inadequate compensation", "at": A("c46", "inadequate")}])
cue(type="point", t0=S("c47"), t1=E("c47") + 0.05, text="An injured victim may appeal an acquittal", icon="user-round", at=A("c47", "injured"))
cue(type="compare", t0=S("c48"), t1=E("c49") + 0.05, head="The State's routes", head_at=S("c48") + 0.05,
    cols=[{"title": "§ 418", "icon": "landmark", "at": A("c48", "section")}, {"title": "§ 419", "icon": "landmark", "at": A("c49", "section")}],
    rows=[{"cells": ["Government appeal against an inadequate sentence", "Specified appeals against acquittal"], "cells_at": [A("c48", "government"), A("c49", "specified")]}])
cue(type="point", t0=S("c50"), t1=E("c50") + 0.05, text="Who appeals + what is challenged = the route", icon="scale", accent=True, at=A("c50", "who"))

# ── 10 · filing time ≠ disposal time ─────────────────────────────────────────────────────────────────────────────────────────────
cue(type="compare", t0=S("c51"), t1=E("c53") + 0.05, head="Two different clocks", head_at=A("c51", "one"),
    cols=[{"title": "Filing", "icon": "calendar", "at": A("c51", "timeline")}, {"title": "Disposal", "icon": "hourglass", "at": A("c51", "section")}],
    rows=[{"cells": ["Limitation Act: 30 · 60 · 90 days", "§ 415(4): six months from filing"], "cells_at": [A("c51", "section") + 0.2, A("c51", "six")]},
          {"cells": ["Every appeal and revision", "Only sentence appeals under BNS 64–68, 70–71"], "cells_at": [A("c52", "appeals"), A("c52", "sexual")]}],
    verdict={"text": "Not a six-month deadline for every appeal or revision", "icon": "triangle-alert", "at": A("c53", "not")})
cue(type="splitcard", t0=S("c54"), t1=E("c54") + 0.05,
    left={"title": "APPEAL", "text": "challenges the decision", "icon": "scale", "at": A("c54", "appeal")},
    right={"title": "REVISION", "text": "a narrower supervisory check", "icon": "search", "at": A("c54", "revision")})
cue(type="list", t0=S("c55"), t1=E("c56") + 0.05, head="Your checklist", head_at=S("c55") + 0.05,
    items=[{"n": 1, "text": "The remedy", "at": A("c55", "remedy")}, {"n": 2, "text": "The court", "at": A("c55", "court")},
           {"n": 3, "text": "The limitation period", "at": A("c55", "limitation")}, {"n": 4, "text": "Copies, grounds, interim order", "at": A("c56", "copies")}])
