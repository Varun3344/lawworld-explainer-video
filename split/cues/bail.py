# Regular, Anticipatory and Default Bail (BNSS): panel cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND).
# Storyboard: ~/Downloads/Regular_Anticipatory_and_Default_Bail_BNSS_Storyboard.pdf. Fact-check 19-10-2026: no errors; 482(4)
# excludes BNS 65 (all) and 70(2); ED v. Kapil Wadhawan (27.03.2023) para 50: the remand day is day 1; M. Ravindran v.
# Intelligence Officer, DRI (2021) 2 SCC 485 paras 18.1-18.4; 2026 calendar checked (1 March = day 60, a Sunday; 2 March = day 61).
# v2 19-10-2026: cues rebuilt for the fast energetic script (37 clips, v1 in split/v1_19oct/bail.py); citations as in v1.
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

STING = {"kicker": "CRIMINAL PROCEDURE · BNSS EXPLAINED", "title": "Regular, Anticipatory and Default Bail", "sub": "Three routes to release"}
ENDCARD = {"title": "Three Routes to Bail", "line": "Know the stage · check the section · act in time", "sub": "Next lesson: Rejection and Return of Plaint"}

# ── 1 · three situations ─────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="compare", t0=S("c01"), t1=E("c02") + 0.05, head="Three clients, three routes", head_at=S("c01") + 0.1,
    cols=[{"title": "The situation", "icon": "user-round", "at": A("c01", "one")}, {"title": "The route", "icon": "key-round", "at": A("c01", "which")}],
    rows=[{"cells": ["Already in custody", "Regular bail"], "cells_at": [A("c01", "custody"), A("c02", "regular")]},
          {"cells": ["Fears arrest", "Anticipatory bail"], "cells_at": [A("c01", "fears"), A("c02", "anticipatory")]},
          {"cells": ["Detained past the deadline", "Default bail"], "cells_at": [A("c01", "deadline"), A("c02", "default")]}])
cue(type="cite", t0=A("c02", "under"), t1=E("c02") + 0.05, at=A("c02", "under"), tag="BNSS", text="§§ 478, 480, 482, 483 and 187(3)", icon="book-open")

# ── 2 · regular bail ─────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c03"), t1=E("c03") + 0.05, text="Release after arrest, or after surrender to the court", icon="key-round", at=A("c03", "regular"))
cue(type="list", t0=S("c04"), t1=A("c06", "non") - 0.05, head="Who grants regular bail", head_at=S("c04") + 0.05,
    items=[{"n": "478", "text": "Bailable: release as of right", "at": A("c04", "section")},
           {"n": "480", "text": "Non-bailable: the Magistrate", "at": A("c05", "section")},
           {"n": "483", "text": "Sessions Court, High Court", "at": A("c06", "section")}])
# a notequal's left side builds at left_at, but the plan's gap check sees only at: keep at within ~1 s of the card before it
cue(type="notequal", t0=A("c06", "non") - 0.05, t1=E("c06") + 0.05, left="Non-bailable", right="no bail", at=A("c06", "does"), left_at=A("c06", "non"))
cue(type="checklist", t0=S("c07"), t1=E("c07") + 0.05, head="The court weighs", head_at=A("c07", "what"),
    items=[{"n": 1, "text": "The accusation", "at": A("c07", "accusation")}, {"n": 2, "text": "The material", "at": A("c07", "material")},
           {"n": 3, "text": "Risk of absconding", "at": A("c07", "absconding")}, {"n": 4, "text": "Risk to witnesses", "at": A("c07", "influencing")}])

# ── 3 · Arjun is arrested ────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="list", t0=S("c08"), t1=E("c08") + 0.05, head="Arjun's case for bail", head_at=A("c08", "arjun"),
    items=[{"n": 1, "text": "A fixed address", "at": A("c08", "fixed")}, {"n": 2, "text": "Will attend court", "at": A("c08", "attend")},
           {"n": 3, "text": "No contact with witnesses", "at": A("c08", "contact")}])
cue(type="compare", t0=S("c09"), t1=E("c09") + 0.05, head="The hearing", head_at=S("c09") + 0.05,
    cols=[{"title": "Prosecution", "icon": "scale", "at": A("c09", "prosecution")}, {"title": "The court", "icon": "gavel", "at": A("c09", "court")}],
    rows=[{"cells": ["Custody concerns", "Weighs the circumstances and the legal restrictions"], "cells_at": [A("c09", "concerns"), A("c09", "weighs")]}])
cue(type="verdicts", t0=S("c10"), t1=E("c10") + 0.05,
    rows=[{"text": "Release on conditions", "ok": True, "at": A("c10", "granted")},
          {"text": "A finding on guilt", "ok": False, "at": A("c10", "remember"), "strike_at": A("c10", "decide")}])

# ── 4 · anticipatory bail ────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c11"), t1=A("c11", "anticipatory") - 0.05, at=A("c11", "no"), text="No arrest yet, but your client fears one?", hl="fears one?")
cue(type="point", t0=A("c11", "anticipatory") - 0.05, t1=E("c11") + 0.05, text="Anticipatory bail: protection before arrest", icon="shield-check", accent=True, at=A("c11", "anticipatory"))
cue(type="flow", t0=S("c12"), t1=A("c14", "filing") - 0.05, head="How it works (§ 482)", head_at=S("c12") + 0.05,
    steps=[{"label": "Reasonable fear of arrest", "sub": "a non-bailable accusation", "icon": "triangle-alert", "at": A("c12", "apprehends")},
           {"label": "Sessions Court or High Court", "icon": "landmark", "at": A("c12", "sessions")},
           {"label": "If arrested: released on bail", "icon": "key-round", "tone": "ok", "at": A("c13", "released")}])
cue(type="notequal", t0=A("c14", "filing") - 0.05, t1=E("c14") + 0.05, left="Filing the application", right="automatic protection",
    at=A("c14", "application"), left_at=A("c14", "filing"), sub="The court's order protects, not the filing", sub_at=A("c14", "court's"))
cue(type="section", t0=S("c15"), t1=E("c16") + 0.05, at=A("c15", "exclusions"), act="BNSS", num="482(4)", title="Excluded from anticipatory bail",
    points=[{"text": "BNS 65: rape of a woman under 16", "tone": "no", "at": A("c15", "sixty")},
            {"text": "BNS 70(2): gang rape of a woman under 18", "tone": "no", "at": A("c15", "seventy")}],
    note={"text": "Some special laws also bar anticipatory bail", "icon": "book-open", "at": A("c16", "special")})

# ── 5 · Meera's case ─────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c17"), t1=E("c17") + 0.05, head="How do you protect Meera?", head_at=S("c17") + 0.05,
    steps=[{"label": "A non-bailable accusation", "icon": "file-text", "at": A("c17", "non")},
           {"label": "Concrete reasons to fear arrest", "icon": "triangle-alert", "at": A("c17", "concrete")},
           {"label": "She applies under § 482", "icon": "file-pen-line", "tone": "ok", "at": A("c17", "applies")}])
cue(type="checklist", t0=S("c18"), t1=E("c18") + 0.05, head="Possible conditions (§ 482(2))", head_at=S("c18") + 0.05,
    items=[{"n": 1, "text": "Attend police questioning", "at": A("c18", "attend")}, {"n": 2, "text": "No pressure on witnesses", "at": A("c18", "threatening")},
           {"n": 3, "text": "Permission to leave India", "at": A("c18", "permission")}])
cue(type="verdicts", t0=S("c19"), t1=E("c19") + 0.05,
    rows=[{"text": "Protects liberty while the case proceeds", "ok": True, "at": A("c19", "anticipatory")},
          {"text": "Cancels the FIR", "ok": False, "at": A("c19", "cancel"), "strike_at": A("c19", "r") + 0.2},
          {"text": "Excuses cooperation", "ok": False, "at": A("c19", "excuse"), "strike_at": A("c19", "lawful")}])

# ── 6 · default bail ─────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c20"), t1=E("c21") + 0.05, at=A("c20", "default"), act="BNSS", num="187(3)", title="Default (statutory) bail",
    points=[{"text": "No charge sheet within the period of detention during investigation", "at": A("c21", "charge")}])
cue(type="counters", t0=S("c22"), t1=E("c23") + 0.05, head="The investigation clock", head_at=S("c22") + 0.05,
    items=[{"value": 90, "unit": "DAYS", "label": "Death, life, or 10 years or more", "at": A("c22", "ninety")},
           {"value": 60, "unit": "DAYS", "label": "Other offences", "at": A("c23", "sixty")}],
    note={"text": "Claim the right, and be ready to furnish bail", "icon": "key-round", "at": A("c23", "claim")})
cue(type="checklist", t0=S("c24"), t1=E("c24") + 0.05, head="Before you pick the deadline", head_at=S("c24") + 0.05,
    items=[{"n": 1, "text": "The exact offence", "at": A("c24", "exact")}, {"n": 2, "text": "The judicial interpretation", "at": A("c24", "judicial")},
           {"n": 3, "text": "Any special law", "at": A("c24", "special")}])

# ── 7 · where counting begins ────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c25"), t1=A("c25", "f") - 0.3, at=A("c25", "where"), text="Where does the clock start?", hl="clock start?")
cue(type="timeline", t0=A("c25", "f") - 0.35, t1=E("c26") + 0.05,
    nodes=[{"label": "THE FIR", "value": "Not day 1", "tone": "red", "sub": "the count does not start here", "at": A("c25", "f")},
           {"label": "FIRST REMAND ORDER", "value": "Day 1", "sub": "that day counts", "at": A("c25", "first")},
           {"label": "POLICE → JUDICIAL", "value": "No reset", "sub": "one continuous count", "at": A("c26", "moving")}])
cue(type="cite", t0=A("c26", "supreme"), t1=E("c26") + 0.05, at=A("c26", "supreme"), tag="SUPREME COURT OF INDIA · 27.03.2023",
    cases=[{"name": "Enforcement Directorate v. Kapil Wadhawan", "cite": "para 50"}])
cue(type="compare", t0=S("c27"), t1=E("c27") + 0.05, head="Investigation, not trial", head_at=S("c27") + 0.05,
    cols=[{"title": "§ 187(3)", "icon": "hourglass", "at": A("c27", "these")}, {"title": "The trial", "icon": "gavel", "at": A("c27", "trial")}],
    rows=[{"cells": ["60 / 90 days of detention during investigation", "Need not end within 60 / 90 days"], "cells_at": [A("c27", "concern"), A("c27", "need")]}],
    verdict={"text": "Prolonged undertrial detention: separate rules (§ 479)", "icon": "calendar", "at": A("c27", "prolonged")})

# ── 8 · a 60-day example ─────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c28"), t1=A("c28", "january") - 0.9, text="Ravi: the 60-day category, no special-law extension", icon="user-round", at=A("c28", "ravi's"))
cue(type="cite", t0=A("c28", "his"), t1=E("c30") + 0.05, at=A("c28", "his"), tag="ILLUSTRATION", text="A 60-day case, no special law; a Sunday does not extend the period", icon="info")
cue(type="timeline", t0=A("c28", "january") - 0.95, t1=E("c30") + 0.05,
    nodes=[{"label": "1 JAN 2026", "value": "Day 1", "sub": "first remand", "at": A("c28", "january")},
           {"label": "31 JAN", "value": "Day 31", "at": A("c29", "thirty")},
           {"label": "28 FEB", "value": "Day 59", "at": A("c29", "fifty")},
           {"label": "1 MAR (SUNDAY)", "value": "Day 60", "at": A("c30", "first")},
           {"label": "2 MAR", "value": "Day 61", "sub": "the right can be claimed", "at": A("c30", "second")}])
cue(type="flow", t0=S("c31"), t1=E("c31") + 0.05, head="On day 61", head_at=S("c31") + 0.05,
    steps=[{"label": "Claim default bail", "icon": "file-pen-line", "at": A("c31", "claim")},
           {"label": "Offer to furnish bail", "icon": "indian-rupee", "at": A("c31", "offer")},
           {"label": "Court order + compliance", "icon": "gavel", "tone": "ok", "at": A("c31", "court")}],
    note={"text": "He does not simply walk out", "icon": "lock", "at": A("c31", "walk")})

# ── 9 · why a timely claim matters ───────────────────────────────────────────────────────────────────────────────────────────────
cue(type="compare", t0=S("c32"), t1=E("c34") + 0.05, head="Who moves first?", head_at=A("c32", "who"),
    cols=[{"title": "Claim first", "icon": "key-round", "at": A("c32", "suppose")}, {"title": "Charge sheet first", "icon": "file-text", "at": A("c34", "if")}],
    rows=[{"cells": ["Claims as soon as the period expires", "A valid charge sheet is filed first"], "cells_at": [A("c32", "claims"), A("c34", "filed")]},
          {"cells": ["Offers to furnish bail", "Then the claim is made"], "cells_at": [A("c33", "offers"), A("c34", "claims")]},
          {"cells": ["A later charge sheet cannot defeat it", "Default bail ordinarily lost: seek regular bail"], "cells_at": [A("c33", "cannot"), A("c34", "unavailable")]}])
cue(type="cite", t0=A("c33", "later"), t1=E("c34") + 0.05, at=A("c33", "later"), tag="SUPREME COURT OF INDIA",
    cases=[{"name": "M. Ravindran v. Intelligence Officer, DRI", "cite": "(2021) 2 SCC 485, paras 18.1–18.4"}])
cue(type="verdicts", t0=S("c35"), t1=E("c35") + 0.05,
    rows=[{"text": "Rests on the missed deadline", "ok": True, "at": A("c35", "default")},
          {"text": "An acquittal", "ok": False, "at": A("c35", "acquittal") - 0.3, "strike_at": A("c35", "acquittal") + 0.4},
          {"text": "The investigation stops", "ok": False, "at": A("c35", "investigation"), "strike_at": A("c35", "continue")}])

# ── 10 · remember ────────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="list", t0=S("c36"), t1=A("c37", "know") - 0.05, head="Three questions", head_at=A("c36", "three"),
    items=[{"n": 1, "text": "In custody? → Regular", "at": A("c36", "already")}, {"n": 2, "text": "Fearing arrest? → Anticipatory", "at": A("c36", "reasonably")},
           {"n": 3, "text": "Deadline missed? → Default", "at": A("c37", "investigation")}])
cue(type="cite", t0=A("c36", "already"), t1=A("c37", "know") - 0.05, at=A("c36", "already"), tag="BNSS",
    text="Regular: §§ 478, 480, 483 · Anticipatory: § 482 · Default: § 187(3)", icon="book-open")
cue(type="point", t0=A("c37", "know") - 0.05, t1=E("c37") + 0.05, text="Know the stage. Check the section. Act in time.", icon="scale", accent=True, at=A("c37", "know"))
