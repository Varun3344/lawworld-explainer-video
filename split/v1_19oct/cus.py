# Police Custody and Judicial Custody (BNSS): panel cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND).
# Storyboard: ~/Downloads/Police_and_Judicial_Custody_BNSS_Storyboard.pdf. Fact-check 19-10-2026: no errors; the 15-day police
# custody cap is the Supreme Court's reading of 187(2) (State of A.P. v. Suda Suresh Veera Venkata Naga Raju, 2026 INSC 744,
# 27.07.2026, para 22); s.47 "forthwith"; s.38 during interrogation, not throughout.
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

STING = {"kicker": "CRIMINAL PROCEDURE · BNSS EXPLAINED", "title": "Police Custody vs Judicial Custody", "sub": "Powers, time limits and safeguards"}
ENDCARD = {"title": "Police vs Judicial Custody", "line": "15 police days in all, not 40 or 60", "sub": "Next lesson: Regular, Anticipatory and Default Bail"}

# ── 1 · two kinds of custody ─────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="splitcard", t0=S("c01"), t1=A("c01", "who") - 0.05,
    left={"title": "POLICE CUSTODY", "text": "with the investigators", "icon": "lock", "at": A("c01", "police")},
    right={"title": "JUDICIAL CUSTODY", "text": "in prison, under court orders", "icon": "landmark", "at": A("c01", "judicial")})
cue(type="question", t0=A("c01", "who"), t1=E("c01") + 0.05, at=A("c01", "who"), text="Who controls the person, and for how long?", hl="for how long?")
cue(type="list", t0=S("c02"), t1=E("c02") + 0.05, head="Three questions", head_at=S("c02") + 0.05,
    items=[{"n": 1, "text": "Who holds the person?", "at": A("c02", "different")}, {"n": 2, "text": "Who authorises it?", "at": A("c02", "detention")},
           {"n": 3, "text": "What are the limits?", "at": A("c02", "safeguards")}])

# ── 2 · the first 24 hours ───────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="counters", t0=S("c03"), t1=E("c04") + 0.05, head="After an arrest without warrant", head_at=S("c03") + 0.05,
    items=[{"value": 24, "unit": "HOURS", "label": "Without a Magistrate's order", "sub": "§ 58 · necessary travel time excluded", "at": A("c03", "twenty")}],
    note={"text": "No unnecessary delay (§§ 57, 58)", "icon": "hourglass", "at": A("c04", "police")})
cue(type="timeline", t0=S("c05"), t1=E("c05") + 0.05,
    nodes=[{"label": "RAVI ARRESTED", "value": "Monday", "sub": "morning", "at": A("c05", "arrested")},
           {"label": "THE 24-HOUR POINT", "value": "Tuesday", "sub": "morning, travel time aside", "at": A("c05", "officers")},
           {"label": "DAYS IN THE STATION", "value": "No", "sub": "not for unfinished questioning", "tone": "red", "at": A("c05", "days")}])
cue(type="flow", t0=S("c06"), t1=E("c07") + 0.05,
    steps=[{"label": "More detention needed", "icon": "hourglass", "at": A("c06", "further")},
           {"label": "Produced before a Magistrate", "sub": "§ 187(1)", "icon": "landmark", "at": A("c06", "production")},
           {"label": "Is remand justified?", "icon": "scale", "tone": "ok", "at": A("c07", "remand")}])

# ── 3 · what each form means ─────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="compare", t0=S("c08"), t1=E("c11") + 0.05, head="Control and purpose", head_at=S("c08") + 0.05,
    cols=[{"title": "Police custody", "icon": "lock", "at": A("c08", "police")}, {"title": "Judicial custody", "icon": "landmark", "at": A("c10", "judicial")}],
    rows=[{"cells": ["With the investigating police", "In prison, under jail authorities"], "cells_at": [A("c08", "investigating"), A("c10", "prison")]},
          {"cells": ["Questioning, recovering evidence", "Police lose direct custody"], "cells_at": [A("c09", "questioning"), A("c11", "investigating")]},
          {"cells": ["Under the remand order", "Under the court's order"], "cells_at": [A("c08", "remand"), A("c10", "court's")]}])
cue(type="verdicts", t0=S("c12"), t1=E("c12") + 0.05,
    rows=[{"text": "Legal justification, always", "ok": True, "at": A("c12", "justification")},
          {"text": "A finding of guilt", "ok": False, "at": A("c12", "neither"), "strike_at": A("c12", "guilt") + 0.2},
          {"text": "Judicial custody = conviction", "ok": False, "at": A("c12", "judicial"), "strike_at": A("c12", "conviction") + 0.2}])

# ── 4 · 15 days in a window ──────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="counters", t0=S("c13"), t1=E("c14") + 0.05, head="The key limit", head_at=S("c13") + 0.1,
    items=[{"value": 15, "unit": "DAYS", "label": "Police custody, in all", "sub": "§ 187(2), as the Supreme Court reads it", "at": A("c14", "fifteen")}])
cue(type="cite", t0=A("c14", "supreme"), t1=E("c17") + 0.05, at=A("c14", "supreme"), tag="SUPREME COURT OF INDIA · 27.07.2026",
    cases=[{"name": "State of A.P. v. Suda Suresh Veera Venkata Naga Raju", "cite": "2026 INSC 744, para 22"}])
cue(type="compare", t0=S("c15"), t1=E("c16") + 0.05, head="The window", head_at=S("c15") + 0.05,
    cols=[{"title": "60-day case", "icon": "calendar", "at": A("c15", "sixty")}, {"title": "90-day case", "icon": "calendar", "at": A("c15", "ninety")}],
    rows=[{"cells": ["15 police days, within days 1–40", "15 police days, within days 1–60"], "cells_at": [A("c15", "forty"), A("c15", "first", 2)]}],
    verdict={"text": "40 and 60 are the window, not the police days", "icon": "triangle-alert", "at": A("c16", "forty")})
cue(type="point", t0=S("c17"), t1=E("c17") + 0.05, text="Every grant: the Magistrate decides", icon="gavel", accent=True, at=A("c17", "every"))

# ── 5 · Ravi moves between the two ───────────────────────────────────────────────────────────────────────────────────────────────
cue(type="timeline", t0=S("c18"), t1=E("c21") + 0.05,
    nodes=[{"label": "DAYS 1–5", "value": "Police", "sub": "5 days granted", "at": A("c18", "grants")},
           {"label": "DAYS 6–19", "value": "Judicial", "sub": "custody continues", "at": A("c19", "judicial")},
           {"label": "DAY 20 ON", "value": "Police", "sub": "5 more, if justified", "at": A("c20", "twenty")},
           {"label": "USED", "value": "10 of 15", "sub": "all inside days 1–40", "at": A("c21", "ten")}])
cue(type="cite", t0=S("c18") + 0.4, t1=E("c21") + 0.05, at=S("c18") + 0.4, tag="ILLUSTRATION", text="A 60-day case, continuous remand, ordinary BNSS rules", icon="info")
cue(type="verdicts", t0=S("c22"), t1=E("c22") + 0.05,
    rows=[{"text": "A fresh 15-day allowance", "ok": False, "at": A("c22", "fresh"), "strike_at": A("c22", "allowance") + 0.2},
          {"text": "The remand clock restarts", "ok": False, "at": A("c22", "restart"), "strike_at": A("c22", "clock") + 0.2}])

# ── 6 · production and reasons ───────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="compare", t0=S("c23"), t1=A("c25", "police", 2) - 0.05, head="Before the Magistrate", head_at=S("c23") + 0.05,
    cols=[{"title": "Police custody", "icon": "lock", "at": A("c23", "physical")}, {"title": "Judicial custody", "icon": "landmark", "at": A("c24", "judicial")}],
    rows=[{"cells": ["In person, every time · § 187(4)", "In person, or by audio-video"], "cells_at": [A("c23", "production"), A("c24", "audio")]}],
    verdict={"text": "Reasons recorded for police custody · § 187(7)", "icon": "file-pen-line", "at": A("c25", "reasons")})
cue(type="strike", t0=A("c25", "police", 2), t1=E("c25") + 0.05, text="Police request = custody", icon="file-text", at=A("c25", "police", 2), strike_at=A("c25", "order") + 0.15)
cue(type="flow", t0=S("c26"), t1=E("c26") + 0.05,
    steps=[{"label": "In prison", "sub": "judicial custody", "icon": "landmark", "at": A("c26", "prison")},
           {"label": "A fresh court order", "sub": "within the limits", "icon": "gavel", "tone": "ok", "at": A("c26", "fresh")},
           {"label": "Police custody", "icon": "lock", "at": A("c26", "limits")}])

# ── 7 · how 60 and 90 fit ────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c27"), t1=E("c29") + 0.05, at=A("c27", "section"), act="BNSS", num="187(3)", title="Investigation detention periods",
    points=[{"text": "90 days: death, life, or 10 years or more", "at": A("c28", "ninety")}, {"text": "60 days: other offences", "at": A("c29", "sixty")}],
    note={"text": "Check the exact charge and the binding interpretation", "icon": "search-check", "at": A("c29", "exact")})
cue(type="equation", t0=S("c30"), t1=E("c30") + 0.05,
    terms=[{"text": "POLICE DAYS", "at": A("c30", "police")}, {"op": "+", "text": "JUDICIAL DAYS", "at": A("c30", "judicial")},
           {"op": "=", "text": "THE 60 / 90 TOTAL", "result": True, "at": A("c30", "total")}])
cue(type="cite", t0=A("c30", "not"), t1=E("c30") + 0.05, at=A("c30", "not"), tag="NOT", text="15 + 60, or 15 + 90", icon="x")
cue(type="point", t0=S("c31"), t1=E("c31") + 0.05, text="Special laws can change these figures", icon="triangle-alert", at=A("c31", "special"))

# ── 8 · after the limit ──────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c32"), t1=A("c32", "if") - 0.05, text="Expiry alone does not open the gates", icon="lock", accent=True, at=A("c32", "expiry"))
cue(type="compare", t0=A("c32", "if"), t1=E("c33") + 0.05, head="When the period ends", head_at=A("c32", "if"),
    cols=[{"title": "Charge sheet missing", "icon": "triangle-alert", "at": A("c32", "missing")}, {"title": "Charge sheet on time", "icon": "file-check", "at": A("c33", "timely")}],
    rows=[{"cells": ["Claim default bail, in time", "Judicial custody can continue"], "cells_at": [A("c32", "claim"), A("c33", "continue")]},
          {"cells": ["Be ready to furnish bail", "Through lawful orders"], "cells_at": [A("c33", "ready"), A("c33", "lawful")]}])
cue(type="section", t0=S("c34"), t1=E("c35") + 0.05, at=A("c34", "section"), act="BNSS", num="346(2)", title="Remand after cognizance",
    points=[{"text": "When proceedings are postponed or adjourned", "at": A("c34", "postponed")}, {"text": "Up to 15 days at a time", "at": A("c35", "fifteen")}],
    note={"text": "Different from the 15-day police-custody limit", "icon": "triangle-alert", "at": A("c35", "different")})

# ── 9 · rights in custody ────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="checklist", t0=S("c36"), t1=E("c39") + 0.05, head="Rights in custody", head_at=A("c36", "custody"),
    items=[{"n": 1, "text": "Grounds of arrest (§ 47)", "at": A("c36", "grounds")}, {"n": 2, "text": "Relative informed (§ 48)", "at": A("c37", "informing")},
           {"n": 3, "text": "Meet an advocate (§ 38)", "at": A("c38", "advocate")}, {"n": 4, "text": "Medical examination (§ 53)", "at": A("c39", "medical")},
           {"n": 5, "text": "Health and safety (§ 56)", "at": A("c39", "health")}])
cue(type="cite", t0=A("c38", "though"), t1=E("c38") + 0.05, at=A("c38", "though"), tag="§ 38", text="During interrogation, though not throughout it", icon="info")
cue(type="point", t0=S("c40"), t1=E("c40") + 0.05, text="Seek bail before the limits run out", icon="key-round", accent=True, at=A("c40", "bail"))

# ── 10 · remember ────────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="compare", t0=S("c41"), t1=E("c42") + 0.05, head="Remember", head_at=S("c41") + 0.05,
    cols=[{"title": "Police custody", "icon": "lock", "at": A("c41", "police")}, {"title": "Judicial custody", "icon": "landmark", "at": A("c42", "judicial")}],
    rows=[{"cells": ["With the investigators", "In prison"], "cells_at": [A("c41", "investigators"), A("c42", "prison")]},
          {"cells": ["For authorised investigation", "Under court orders"], "cells_at": [A("c41", "authorised"), A("c42", "court")]}])
cue(type="counters", t0=S("c43"), t1=E("c44") + 0.05, head="The ordinary limits", head_at=A("c43", "remember"),
    items=[{"value": 24, "unit": "HOURS", "label": "Until a Magistrate authorises", "at": A("c43", "twenty")},
           {"value": 15, "unit": "DAYS", "label": "Police custody in all", "at": A("c43", "fifteen")},
           {"value": 90, "unit": "DAYS", "label": "60 or 90, by offence", "sub": "police days within the first 40 / 60", "at": A("c44", "ninety")}])
