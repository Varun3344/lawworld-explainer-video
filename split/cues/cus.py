# Police Custody and Judicial Custody (BNSS): panel cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND).
# Storyboard: ~/Downloads/Police_and_Judicial_Custody_BNSS_Storyboard.pdf. Fact-check 19-10-2026: no errors; the 15-day police
# custody cap is the Supreme Court's reading of 187(2) (State of A.P. v. Suda Suresh Veera Venkata Naga Raju, 2026 INSC 744,
# 27.07.2026, para 22); s.47 "forthwith"; s.38 during interrogation, not throughout.
# v2 19-10-2026: fast energetic rewrite (owner); facts as in v1; every cue rebuilt for the 37 new clips (v1: split/v1_19oct/cus.py).
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

STING = {"kicker": "CRIMINAL PROCEDURE · BNSS EXPLAINED", "title": "Police Custody vs Judicial Custody", "sub": "Powers, time limits and safeguards"}
ENDCARD = {"title": "Police vs Judicial Custody", "line": "15 police days in all, not 40 or 60", "sub": "Next lesson: Regular, Anticipatory and Default Bail"}

# ── 1 · two kinds of custody ─────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c01"), t1=A("c01", "will") - 0.05, text="Arrested, and wanted for questioning", icon="user-round", at=A("c01", "arrested"))
cue(type="question", t0=A("c01", "will"), t1=A("c01", "who") - 0.05, at=A("c01", "will"), text="Police custody, or judicial custody?", hl="judicial custody?")
cue(type="list", t0=A("c01", "who"), t1=A("c02", "these") - 0.05,
    items=[{"n": 1, "text": "Who holds him?", "at": A("c01", "who")}, {"n": 2, "text": "Who authorises it?", "at": A("c01", "who", 2)},
           {"n": 3, "text": "For how long?", "at": A("c01", "how")}])
cue(type="cite", t0=A("c02", "bharatiya"), t1=E("c02") + 0.05, at=A("c02", "bharatiya"), tag="THE LAW", text="Bharatiya Nagarik Suraksha Sanhita · BNSS", icon="book-open")
cue(type="notequal", t0=A("c02", "these"), t1=E("c02") + 0.05, left="Police custody", right="judicial custody", at=A("c02", "distinct"),
    left_at=A("c02", "these"), sub="Distinct forms of detention, with safeguards", sub_at=A("c02", "forms"))

# ── 2 · the first 24 hours ───────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="counters", t0=S("c03"), t1=A("c04", "note") - 0.05, head="The first deadline", head_at=S("c03") + 0.05,
    items=[{"value": 24, "unit": "HOURS", "label": "After arrest without warrant", "sub": "§ 58: no longer without a Magistrate's authorisation", "at": A("c03", "twenty")}],
    note={"text": "Necessary travel time excluded · no unnecessary delay (§§ 57, 58)", "icon": "hourglass", "at": A("c04", "necessary")})
cue(type="point", t0=A("c04", "note"), t1=E("c04") + 0.05, text="Note the exact arrest time", icon="clock", accent=True, at=A("c04", "note"))
cue(type="timeline", t0=S("c05"), t1=E("c05") + 0.05,
    nodes=[{"label": "RAVI ARRESTED", "value": "Monday", "sub": "morning", "at": A("c05", "arrested")},
           {"label": "DAYS AT THE STATION", "value": "No", "sub": "not for unfinished questioning", "tone": "red", "at": A("c05", "days")}])
cue(type="flow", t0=S("c06"), t1=E("c06") + 0.05,
    steps=[{"label": "Police need further detention", "icon": "hourglass", "at": A("c06", "police")},
           {"label": "Produced before a Magistrate", "sub": "§ 187(1)", "icon": "landmark", "at": A("c06", "production")},
           {"label": "Is remand justified?", "icon": "scale", "tone": "ok", "at": A("c06", "remand")}])

# ── 3 · control and purpose ──────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="compare", t0=S("c07"), t1=E("c09") + 0.05, head="Who holds your client, and why?", head_at=S("c07") + 0.05,
    cols=[{"title": "Police custody", "icon": "lock", "at": A("c07", "police")}, {"title": "Judicial custody", "icon": "landmark", "at": A("c08", "judicial")}],
    rows=[{"cells": ["Entrusted to investigating police", "Ordinarily kept in prison"], "cells_at": [A("c07", "entrusted"), A("c08", "ordinarily")]},
          {"cells": ["Lawful investigation, under the remand order", "Jail authorities, on the court's order"], "cells_at": [A("c07", "lawful"), A("c09", "jail")]},
          {"cells": ["Questioning, recovering evidence", "Investigating officer: no direct custody"], "cells_at": [A("c08", "questioning"), A("c09", "investigating")]}])
cue(type="verdicts", t0=S("c10"), t1=E("c10") + 0.05,
    rows=[{"text": "Both need legal justification", "ok": True, "at": A("c10", "both")},
          {"text": "A finding of guilt", "ok": False, "at": A("c10", "neither"), "strike_at": A("c10", "guilt") + 0.2},
          {"text": "Judicial custody = conviction", "ok": False, "at": A("c10", "judicial"), "strike_at": A("c10", "conviction") - 0.05}])

# ── 4 · 15 days in a window ──────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c11"), t1=E("c11") + 0.05, at=A("c11", "is"), text="Police custody: 15 days, or 40?", hl="or 40?")
cue(type="cite", t0=A("c11", "here"), t1=E("c11") + 0.05, at=A("c11", "here"), tag="THE KEY LIMIT", text="In the ordinary BNSS scheme", icon="scale")
cue(type="counters", t0=S("c12"), t1=A("c12", "each") - 0.05, head="§ 187(2), as the Supreme Court reads it", head_at=S("c12") + 0.05,
    items=[{"value": 15, "unit": "DAYS", "label": "Police custody, in all", "at": A("c12", "fifteen")}])
cue(type="point", t0=A("c12", "each"), t1=E("c12") + 0.05, text="Each grant still needs the Magistrate's decision", icon="gavel", accent=True, at=A("c12", "each"))
cue(type="cite", t0=A("c12", "supreme"), t1=E("c14") + 0.05, at=A("c12", "supreme"), tag="SUPREME COURT OF INDIA · 27.07.2026",
    cases=[{"name": "State of A.P. v. Suda Suresh Veera Venkata Naga Raju", "cite": "2026 INSC 744, para 22"}])
cue(type="compare", t0=S("c13"), t1=A("c14", "supreme") - 0.05, head="Those 15 days must fall within", head_at=S("c13") + 0.05,
    cols=[{"title": "The first 40 days", "icon": "calendar", "at": A("c13", "forty")}, {"title": "The first 60 days", "icon": "calendar", "at": A("c13", "first", 2)}],
    rows=[{"cells": ["of remand, in a 60-day case", "in a 90-day case"], "cells_at": [A("c13", "sixty"), A("c13", "ninety")]}],
    verdict={"text": "40 and 60 only describe the window, not the police days", "icon": "triangle-alert", "at": A("c14", "forty")})
cue(type="point", t0=A("c14", "supreme"), t1=E("c14") + 0.05, text="Confirmed by the Supreme Court, July 2026", icon="gavel", accent=True, at=A("c14", "supreme"))

# ── 5 · Ravi moves between the two ───────────────────────────────────────────────────────────────────────────────────────────────
cue(type="list", t0=S("c15"), t1=A("c15", "magistrate") - 0.05, head="Test it on Ravi", head_at=S("c15") + 0.05,
    items=[{"n": 1, "text": "A 60-day case", "at": A("c15", "sixty")}, {"n": 2, "text": "In custody throughout", "at": A("c15", "custody")}])
cue(type="cite", t0=S("c15") + 0.4, t1=E("c17") + 0.05, at=S("c15") + 0.4, tag="ILLUSTRATION", text="A 60-day case, continuous remand, ordinary BNSS rules", icon="info")
cue(type="timeline", t0=A("c15", "magistrate"), t1=E("c17") + 0.05,
    nodes=[{"label": "DAYS 1–5", "value": "Police", "sub": "5 days granted", "at": A("c15", "grants")},
           {"label": "DAYS 6–19", "value": "Judicial", "sub": "custody follows", "at": A("c16", "judicial")},
           {"label": "DAY 20", "value": "5 more?", "sub": "new evidence, police ask", "at": A("c16", "twenty")},
           {"label": "IF JUSTIFIED", "value": "10 of 15", "sub": "all inside days 1–40", "at": A("c17", "ten")}])
cue(type="verdicts", t0=S("c18"), t1=E("c18") + 0.05,
    rows=[{"text": "Back to police custody = a fresh 15 days", "ok": False, "at": A("c18", "returning"), "strike_at": A("c18", "allowance") + 0.2},
          {"text": "The remand clock restarts", "ok": False, "at": A("c18", "restart"), "strike_at": A("c18", "clock") + 0.2},
          {"text": "Check: days used + the window", "ok": True, "at": A("c18", "check")}])

# ── 6 · production and reasons ───────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c19"), t1=A("c19", "physical") - 0.05, at=A("c19", "is"), text="Is a video link enough for police custody?", hl="video link")
cue(type="stamp", t0=A("c19", "no") - 0.05, t1=A("c19", "physical") - 0.05, at=A("c19", "no"), line1="NO", line2="§ 187(4)")
cue(type="compare", t0=A("c19", "physical"), t1=E("c20") + 0.05, head="Before the Magistrate", head_at=A("c19", "physical"),
    cols=[{"title": "Police custody", "icon": "lock", "at": A("c19", "production")}, {"title": "Judicial custody", "icon": "landmark", "at": A("c20", "judicial")}],
    rows=[{"cells": ["In person, each time · § 187(4)", "In person, or by audio-video"], "cells_at": [A("c19", "each"), A("c20", "audio")]}])
cue(type="section", t0=S("c21"), t1=E("c21") + 0.05, at=A("c21", "under"), act="BNSS", num="187(7)", title="Reasons for police custody",
    points=[{"text": "The Magistrate must record reasons", "at": A("c21", "record")},
            {"text": "A police request is not a remand order", "tone": "no", "at": A("c21", "request")},
            {"text": "Check the order for reasons", "at": A("c21", "check")}])
cue(type="flow", t0=S("c22"), t1=E("c22") + 0.05,
    steps=[{"label": "Ravi, in prison", "sub": "judicial custody", "icon": "landmark", "at": A("c22", "move")},
           {"label": "A fresh court order", "sub": "within the limits", "icon": "gavel", "tone": "ok", "at": A("c22", "fresh")},
           {"label": "Police custody", "icon": "lock", "at": A("c22", "within")}])

# ── 7 · how 60 and 90 fit ────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c23"), t1=A("c23", "section") - 0.05, at=A("c23", "where"), text="Where do 60 and 90 come from?", hl="60 and 90")
cue(type="section", t0=A("c23", "section"), t1=E("c24") + 0.05, at=A("c23", "section"), act="BNSS", num="187(3)", title="Investigation detention periods",
    points=[{"text": "Linked to default bail", "at": A("c23", "default")},
            {"text": "90 days: death, life, or 10 years or more", "at": A("c24", "ninety")},
            {"text": "60 days: other offences", "at": A("c24", "sixty")}])
cue(type="equation", t0=S("c25"), t1=E("c25") + 0.05,
    terms=[{"text": "POLICE DAYS", "at": A("c25", "police")}, {"op": "+", "text": "JUDICIAL DAYS", "at": A("c25", "judicial")},
           {"op": "=", "text": "THE 60 / 90 TOTAL", "result": True, "at": A("c25", "total")}])
cue(type="cite", t0=A("c25", "not"), t1=E("c25") + 0.05, at=A("c25", "not"), tag="NOT", text="15 + 60, or 15 + 90", icon="x")
cue(type="checklist", t0=S("c26"), t1=E("c26") + 0.05, head="Check", head_at=A("c26", "check"),
    items=[{"n": 1, "text": "The exact charge", "at": A("c26", "exact")}, {"n": 2, "text": "The applicable judicial interpretation", "at": A("c26", "applicable")},
           {"n": 3, "text": "Special laws: they can modify the rules", "at": A("c26", "special")}])

# ── 8 · after the limit ──────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c27"), t1=E("c27") + 0.05,
    steps=[{"label": "The period ends", "icon": "calendar", "at": A("c27", "period")},
           {"label": "Charge sheet missing", "icon": "file-text", "at": A("c27", "missing")},
           {"label": "Free on expiry alone?", "sub": "it does not open the gates", "icon": "lock", "tone": "stop", "at": A("c27", "free")}])
cue(type="compare", t0=S("c28"), t1=E("c28") + 0.05,
    cols=[{"title": "Charge sheet missing", "icon": "triangle-alert", "at": S("c28") + 0.1}, {"title": "Charge sheet on time", "icon": "file-check", "at": A("c28", "timely")}],
    rows=[{"cells": ["Claim default bail, in time", "Judicial custody can continue"], "cells_at": [A("c28", "claim"), A("c28", "continue")]},
          {"cells": ["Be ready to furnish bail", "Through lawful orders"], "cells_at": [A("c28", "ready"), A("c28", "through")]}])
cue(type="section", t0=S("c29"), t1=E("c30") + 0.05, at=A("c29", "after"), act="BNSS", num="346(2)", title="Remand after cognizance",
    points=[{"text": "When proceedings are postponed or adjourned", "at": A("c29", "postponed")}, {"text": "At most 15 days at a time", "at": A("c30", "fifteen")}],
    note={"text": "Not the 15-day police-custody limit", "icon": "triangle-alert", "at": A("c30", "confuse")})

# ── 9 · rights in custody ────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="checklist", t0=S("c31"), t1=E("c34") + 0.05, head="Basic rights remain", head_at=S("c31") + 0.05,
    items=[{"n": 1, "text": "Grounds of arrest, forthwith (§ 47)", "at": A("c31", "grounds")}, {"n": 2, "text": "Relative or friend informed (§ 48)", "at": A("c32", "nominated")},
           {"n": 3, "text": "Meet an advocate (§ 38)", "at": A("c33", "advocate")}, {"n": 4, "text": "Medical examination (§ 53)", "at": A("c34", "medical")},
           {"n": 5, "text": "Health and safety (§ 56)", "at": A("c34", "health")}])
cue(type="cite", t0=A("c33", "though"), t1=E("c33") + 0.05, at=A("c33", "though"), tag="§ 38", text="During interrogation, though not throughout it", icon="info")
cue(type="point", t0=S("c35"), t1=E("c35") + 0.05, text="Seek bail before the maximum periods expire", icon="key-round", accent=True, at=A("c35", "bail"))
cue(type="cite", t0=A("c35", "court"), t1=E("c35") + 0.05, at=A("c35", "court"), tag="REMEMBER", text="The court need not use every available day", icon="info")

# ── 10 · your custody checklist ──────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="counters", t0=S("c36"), t1=A("c37", "count") - 0.05, head="The ordinary limits", head_at=S("c36") + 0.05,
    items=[{"value": 24, "unit": "HOURS", "label": "Until a Magistrate must authorise", "at": A("c36", "twenty")},
           {"value": 15, "unit": "DAYS", "label": "Police custody in all", "at": A("c36", "fifteen")},
           {"value": 90, "unit": "DAYS", "label": "60 or 90, by offence", "sub": "police days within the first 40 / 60", "at": A("c37", "forty")}])
cue(type="list", t0=A("c37", "count"), t1=E("c37") + 0.05, head="Your checklist", head_at=A("c37", "count"),
    items=[{"n": 1, "text": "Count the days", "at": A("c37", "count")}, {"n": 2, "text": "Check the order", "at": A("c37", "check")},
           {"n": 3, "text": "Claim default bail in time", "at": A("c37", "claim")}])
