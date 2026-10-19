# Regular, Anticipatory and Default Bail (BNSS): panel cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND).
# Storyboard: ~/Downloads/Regular_Anticipatory_and_Default_Bail_BNSS_Storyboard.pdf. Fact-check 19-10-2026: no errors; 482(4)
# excludes BNS 65 (all) and 70(2); ED v. Kapil Wadhawan (27.03.2023) para 50: the remand day is day 1; M. Ravindran v.
# Intelligence Officer, DRI (2021) 2 SCC 485 paras 18.1-18.4; 2026 calendar checked (1 March = day 60, a Sunday; 2 March = day 61).
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

STING = {"kicker": "CRIMINAL PROCEDURE · BNSS EXPLAINED", "title": "Regular, Anticipatory and Default Bail", "sub": "Three routes to release"}
ENDCARD = {"title": "Three Routes to Bail", "line": "Know the stage · check the section · act in time", "sub": "Next lesson: Rejection and Return of Plaint"}

# ── 1 · three situations ─────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="compare", t0=S("c01"), t1=E("c02") + 0.05, head="Three situations, three routes", head_at=S("c01") + 0.1,
    cols=[{"title": "The situation", "icon": "user-round", "at": A("c01", "someone")}, {"title": "The route", "icon": "key-round", "at": A("c02", "these")}],
    rows=[{"cells": ["Already in custody", "Regular bail"], "cells_at": [A("c01", "custody"), A("c02", "regular")]},
          {"cells": ["Fears arrest", "Anticipatory bail"], "cells_at": [A("c01", "fears"), A("c02", "anticipatory")]},
          {"cells": ["Detained past the deadline", "Default bail"], "cells_at": [A("c01", "deadline"), A("c02", "default")]}])
cue(type="cite", t0=A("c03", "under"), t1=E("c03") + 0.05, at=A("c03", "under"), tag="BNSS", text="§§ 478, 480, 482, 483 and 187(3)", icon="book-open")
cue(type="point", t0=A("c03", "under") + 0.2, t1=E("c03") + 0.05, text="The route depends on the situation", icon="scale", accent=True, at=A("c03", "under") + 0.2)

# ── 2 · regular bail ─────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c04"), t1=E("c04") + 0.05, text="Release after arrest, or after surrender to the court", icon="key-round", at=A("c04", "regular"))
cue(type="list", t0=S("c05"), t1=A("c07", "and") - 0.05, head="Who grants regular bail", head_at=S("c05") + 0.05,
    items=[{"n": "478", "text": "Bailable: release as of right", "at": A("c05", "section")},
           {"n": "480", "text": "Non-bailable: the Magistrate", "at": A("c06", "section")},
           {"n": "483", "text": "Sessions Court, High Court", "at": A("c07", "section")}])
cue(type="notequal", t0=A("c07", "and"), t1=E("c07") + 0.05, left="Non-bailable", right="no bail", at=A("c07", "impossible") - 0.6, left_at=A("c07", "non"))
cue(type="checklist", t0=S("c08"), t1=E("c08") + 0.05, head="The court weighs", head_at=S("c08") + 0.05,
    items=[{"n": 1, "text": "The accusation", "at": A("c08", "accusation")}, {"n": 2, "text": "The material", "at": A("c08", "material")},
           {"n": 3, "text": "Risk of absconding", "at": A("c08", "absconding")}, {"n": 4, "text": "Risk to witnesses", "at": A("c08", "influencing")}])

# ── 3 · Arjun is arrested ────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="compare", t0=S("c09"), t1=E("c11") + 0.05, head="Arjun's bail hearing", head_at=S("c09") + 0.05,
    cols=[{"title": "Defence", "icon": "user-round", "at": A("c09", "lawyer")}, {"title": "Prosecution", "icon": "scale", "at": A("c11", "prosecution")}],
    rows=[{"cells": ["A fixed address", "Custody concerns"], "cells_at": [A("c10", "fixed"), A("c11", "concerns")]},
          {"cells": ["Will attend court", "Legal restrictions"], "cells_at": [A("c10", "attend"), A("c11", "restrictions")]},
          {"cells": ["No contact with witnesses", "The court weighs it all"], "cells_at": [A("c10", "contact"), A("c11", "weighs")]}])
cue(type="verdicts", t0=S("c12"), t1=E("c12") + 0.05,
    rows=[{"text": "Release on conditions", "ok": True, "at": A("c12", "granted")},
          {"text": "A finding on guilt", "ok": False, "at": A("c12", "bail", 2), "strike_at": A("c12", "guilt") + 0.2}])

# ── 4 · anticipatory bail ────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c13"), t1=E("c13") + 0.05, text="Anticipatory bail: protection before arrest", icon="shield-check", accent=True, at=A("c13", "anticipatory"))
cue(type="flow", t0=S("c14"), t1=E("c16") + 0.05, head="How it works (§ 482)", head_at=S("c14") + 0.05,
    steps=[{"label": "Reasonable fear of arrest", "sub": "a non-bailable accusation", "icon": "triangle-alert", "at": A("c14", "apprehends")},
           {"label": "Sessions Court or High Court", "icon": "landmark", "at": A("c14", "sessions")},
           {"label": "If arrested: released on bail", "icon": "key-round", "tone": "ok", "at": A("c15", "released")}],
    note={"text": "Filing alone gives no protection: the court's order does", "icon": "file-text", "at": A("c16", "merely")})
cue(type="section", t0=S("c17"), t1=E("c18") + 0.05, at=A("c17", "section"), act="BNSS", num="482(4)", title="Excluded from anticipatory bail",
    points=[{"text": "BNS 65: rape of a woman under 16", "tone": "no", "at": A("c17", "sixty")},
            {"text": "BNS 70(2): gang rape of a woman under 18", "tone": "no", "at": A("c17", "seventy")}],
    note={"text": "Some special laws also bar anticipatory bail", "icon": "book-open", "at": A("c18", "special")})

# ── 5 · Meera's case ─────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c19"), t1=E("c19") + 0.05, text="Meera: concrete reasons to fear arrest, applies under § 482", icon="user-round", at=A("c19", "meera"))
cue(type="checklist", t0=S("c20"), t1=A("c21", "anticipatory") - 0.05, head="Possible conditions (§ 482(2))", head_at=S("c20") + 0.05,
    items=[{"n": 1, "text": "Attend police questioning", "at": A("c20", "attend")}, {"n": 2, "text": "No pressure on witnesses", "at": A("c20", "threatening")},
           {"n": 3, "text": "Permission to leave India", "at": A("c21", "permission")}])
cue(type="verdicts", t0=A("c21", "anticipatory"), t1=E("c22") + 0.05,
    rows=[{"text": "Protects liberty while the case proceeds", "ok": True, "at": A("c21", "anticipatory")},
          {"text": "Cancels the FIR", "ok": False, "at": A("c22", "cancel"), "strike_at": A("c22", "r") + 0.2},
          {"text": "Excuses cooperation", "ok": False, "at": A("c22", "excuse"), "strike_at": A("c22", "investigation") + 0.2}])

# ── 6 · default bail ─────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c23"), t1=E("c24") + 0.05, at=A("c23", "section"), act="BNSS", num="187(3)", title="Default (statutory) bail",
    points=[{"text": "No charge sheet within the period of detention during investigation", "at": A("c24", "charge")}])
cue(type="counters", t0=S("c25"), t1=E("c26") + 0.05, head="The investigation clock", head_at=S("c25") + 0.05,
    items=[{"value": 90, "unit": "DAYS", "label": "Death, life, or 10 years or more", "at": A("c25", "ninety")},
           {"value": 60, "unit": "DAYS", "label": "Other offences", "at": A("c26", "sixty")}],
    note={"text": "Claim the right, and be ready to furnish bail", "icon": "key-round", "at": A("c26", "claim")})
cue(type="point", t0=S("c27"), t1=E("c27") + 0.05, text="Check the offence, the interpretation, any special law", icon="search-check", accent=True, at=A("c27", "check"))

# ── 7 · where counting begins ────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="timeline", t0=S("c28"), t1=E("c29") + 0.05,
    nodes=[{"label": "THE FIR", "value": "Not day 1", "tone": "red", "sub": "the count does not start here", "at": A("c29", "do")},
           {"label": "FIRST REMAND ORDER", "value": "Day 1", "sub": "that day counts", "at": A("c28", "first")},
           {"label": "POLICE → JUDICIAL", "value": "No reset", "sub": "one continuous count", "at": A("c29", "moving")}])
cue(type="cite", t0=A("c28", "supreme"), t1=E("c29") + 0.05, at=A("c28", "supreme"), tag="SUPREME COURT OF INDIA · 27.03.2023",
    cases=[{"name": "Enforcement Directorate v. Kapil Wadhawan", "cite": "para 50"}])
cue(type="compare", t0=S("c30"), t1=E("c31") + 0.05, head="Two different clocks", head_at=S("c30") + 0.05,
    cols=[{"title": "§ 187(3)", "icon": "hourglass", "at": A("c30", "these")}, {"title": "§ 479", "icon": "calendar", "at": A("c30", "separate")}],
    rows=[{"cells": ["60 / 90 days of detention during investigation", "Prolonged undertrial detention"], "cells_at": [A("c30", "concern"), A("c30", "prolonged")]}],
    verdict={"text": "The trial need not finish within 60 / 90 days", "icon": "info", "at": A("c31", "trial")})

# ── 8 · a 60-day example ─────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="timeline", t0=S("c32"), t1=E("c35") + 0.05,
    nodes=[{"label": "1 JAN 2026", "value": "Day 1", "sub": "first remand", "at": A("c33", "january")},
           {"label": "31 JAN", "value": "Day 31", "at": A("c34", "thirty")},
           {"label": "28 FEB", "value": "Day 59", "at": A("c34", "fifty")},
           {"label": "1 MAR (SUNDAY)", "value": "Day 60", "at": A("c35", "first")},
           {"label": "2 MAR", "value": "Day 61", "sub": "the right can be claimed", "at": A("c35", "second")}])
cue(type="cite", t0=S("c32") + 0.3, t1=E("c35") + 0.05, at=S("c32") + 0.3, tag="ILLUSTRATION", text="A 60-day case, no special law; a Sunday does not extend the period", icon="info")
cue(type="flow", t0=S("c36"), t1=E("c37") + 0.05, head="On day 61", head_at=S("c36") + 0.05,
    steps=[{"label": "Claim default bail", "icon": "file-pen-line", "at": A("c36", "claim")},
           {"label": "Offer to furnish bail", "icon": "indian-rupee", "at": A("c36", "offer")},
           {"label": "Court order + compliance", "icon": "gavel", "tone": "ok", "at": A("c37", "court")}],
    note={"text": "No walking out when the calendar changes", "icon": "lock", "at": A("c36", "walk")})

# ── 9 · why a timely claim matters ───────────────────────────────────────────────────────────────────────────────────────────────
cue(type="compare", t0=S("c38"), t1=E("c41") + 0.05, head="Who moves first?", head_at=S("c38") + 0.05,
    cols=[{"title": "Claim first", "icon": "key-round", "at": A("c38", "suppose")}, {"title": "Charge sheet first", "icon": "file-text", "at": A("c41", "if")}],
    rows=[{"cells": ["Claims as soon as the period expires", "A valid charge sheet is filed first"], "cells_at": [A("c38", "claims"), A("c41", "filed")]},
          {"cells": ["Offers to furnish bail", "Then the claim is made"], "cells_at": [A("c39", "offers"), A("c41", "claims")]},
          {"cells": ["A later charge sheet cannot defeat it", "Default bail ordinarily lost: seek regular bail"], "cells_at": [A("c40", "cannot"), A("c41", "unavailable")]}])
cue(type="cite", t0=A("c40", "charge"), t1=E("c41") + 0.05, at=A("c40", "charge"), tag="SUPREME COURT OF INDIA",
    cases=[{"name": "M. Ravindran v. Intelligence Officer, DRI", "cite": "(2021) 2 SCC 485, paras 18.1–18.4"}])
cue(type="verdicts", t0=S("c42"), t1=E("c42") + 0.05,
    rows=[{"text": "Rests on the missed deadline", "ok": True, "at": A("c42", "rests")},
          {"text": "An acquittal", "ok": False, "at": A("c42", "acquittal") - 0.3, "strike_at": A("c42", "acquittal") + 0.4},
          {"text": "The investigation stops", "ok": False, "at": A("c42", "investigation"), "strike_at": A("c42", "continue") + 0.2}])

# ── 10 · remember ────────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="list", t0=S("c43"), t1=E("c44") + 0.05, head="Three questions", head_at=A("c43", "remember"),
    items=[{"n": 1, "text": "In custody? → Regular", "at": A("c43", "already")}, {"n": 2, "text": "Fearing arrest? → Anticipatory", "at": A("c43", "reasonably")},
           {"n": 3, "text": "Deadline missed? → Default", "at": A("c44", "investigation")}])
cue(type="point", t0=S("c45"), t1=E("c45") + 0.05, text="Know the stage. Check the section. Act in time.", icon="scale", accent=True, at=A("c45", "every"))
