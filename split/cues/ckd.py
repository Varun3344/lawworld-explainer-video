# Chokkad Service Co-operative Bank Ltd. v. Labour Court, Kozhikode & Anr., W.P.(C) No. 26370 of 2026, 2026:KER:81613, High Court of
# Kerala (Viju Abraham J., 23.10.2026, C.R.): panel cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND).
# HOOK format (owner 02-11-2026): c01 hook question, c02 curiosity, c03 "Hi, I'm Ravishankar" + bench, c04-c07 facts / case /
# discussion, c08 the LawWorld request before the verdict, c09-c10 the verdict. No title sting.
# Facts from the judgment (paras): Ext.P11 in I.A. 55/2026 in I.D. 46/2025, Labour Court Kozhikode; Peon from 30.05.2008; suspended,
# detailed enquiry, dismissed (Ext.P4); the Rule 198(4) appeal to the Executive Committee / Board of Management not filed, the Labour
# Court approached directly; the maintainability I.A. rejected, the claim maintainable (1); Ext.P4 dated 07.12.2023, Ext.P11 dated
# 12.06.2026 (appendix); the bank: the President imposed the punishment; s.28 KCS Act - management vested in the Committee - so only
# the Board's appellate order is final and open to challenge; S. Murali (DB) (2); the employee: Ext.P11 lawful; no writ against a
# maintainability order, the Award can be challenged (3); S. Murali (limitation, s.2A(3)) does not apply; Rule 198(3): the President
# imposes the penalty; Rule 198(4): the Board is an Appellate Authority, not an original authority; "it is his choice to file any
# appeal" (6); Annamma K.A. (SC): the KCS Act and the I.D. Act "both possess and enjoy the concurrent jurisdiction" (7); Veerankavu:
# no need to exhaust the statutory appellate remedy before s.2A(2) (8, 9), followed in Channapetta (9); Basil Scaria: no interference
# on preliminary issues such as maintainability; "no reason to interfere", writ petition dismissed (10).
# Not on any card: the employee's name; the allegations behind the suspension.
# No section sign anywhere. List lines <= 52 chars. Official portrait from the High Court of Kerala's "Present Judges" page on the bench card.
FORMAT = "hook"   # build_course_plan.py: no opening sting, 15-frame lead (the cover), name tag on the "Ravishankar" clip

def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
ENDCARD = {"title": "Skip the appeal, go to the Labour Court?", "line": "The Rule 198(4) appeal is his choice: he may go straight to the Labour Court", "sub": "LawWorld: legal research for advocates"}

# ── 1 · skip the appeal? (hook, curiosity, intro) ────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "bank"), text="A co-operative bank dismisses its peon. Must he first file the appeal under the Society Rules, or go straight to the Labour Court?", hl="go straight to the Labour Court?")
cue(type="compare", t0=S("c02"), t1=A("c02", "so") - 0.05, head="Is the dismissal final?", head_at=S("c02") + 0.05,
    cols=[{"title": "The bank", "icon": "landmark", "at": A("c02", "bank")}, {"title": "Labour Court, Kozhikode", "icon": "scale", "at": A("c02", "labour")}],
    rows=[{"cells": ["Not until the Board decides an appeal", "The claim is maintainable"], "cells_at": [A("c02", "final"), A("c02", "rejected")]}])
cue(type="point", t0=A("c02", "so") - 0.05, t1=E("c02") + 0.05, text="So who was right in law?", icon="search", accent=True, at=A("c02", "right"))
cue(type="bench", t0=S("c03"), t1=E("c03") + 0.05, tag="Kerala High Court · 23 October 2026",
    judges=[{"name": "Justice Viju Abraham", "photo": "../brand/judges/viju_abraham.jpg", "at": A("c03", "honourable")}])

# ── 2 · the dismissal ────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=S("c04"), t1=E("c04") + 0.05, at=A("c04", "employee"), tag="HIGH COURT OF KERALA · 23.10.2026",
    cases=[{"name": "Chokkad Service Co-operative Bank Ltd. v. Labour Court, Kozhikode & Anr.", "cite": "2026:KER:81613 · W.P.(C) No. 26370 of 2026"}])
cue(type="timeline", t0=S("c04"), t1=E("c04") + 0.05,
    nodes=[{"label": "JOINED AS PEON", "value": "30.05.2008", "sub": "Chokkad Service Co-operative Bank", "at": A("c04", "joined")},
           {"label": "SUSPENSION", "value": "enquiry", "sub": "a detailed disciplinary enquiry", "at": A("c04", "enquiry")},
           {"label": "DISMISSED", "value": "07.12.2023", "sub": "by the President of the Society", "tone": "red", "at": A("c04", "dismissed")}])
cue(type="flow", t0=S("c05"), t1=E("c05") + 0.05, head="Two routes after a dismissal", head_at=S("c05") + 0.05,
    steps=[{"label": "Appeal to the Board", "sub": "Rule 198(4), Kerala Co-operative Societies Rules", "icon": "file-text", "at": A("c05", "appeal")},
           {"label": "Not filed", "sub": "no appeal to the Executive Committee", "icon": "x", "tone": "muted", "at": A("c05", "instead")},
           {"label": "The Labour Court", "sub": "I.D. No. 46 of 2025 · Industrial Disputes Act", "icon": "landmark", "at": A("c05", "straight")}])

# ── 3 · the bank's objection ─────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=S("c06"), t1=E("c06") + 0.05, at=A("c06", "bank"), tag="HIGH COURT OF KERALA · 23.10.2026",
    cases=[{"name": "Chokkad Service Co-operative Bank Ltd. v. Labour Court, Kozhikode & Anr.", "cite": "2026:KER:81613 · W.P.(C) No. 26370 of 2026"}])
cue(type="timeline", t0=S("c06"), t1=E("c06") + 0.05,
    nodes=[{"label": "THE BANK'S OBJECTION", "value": "maintainability", "sub": "I.A. No. 55 of 2026", "at": A("c06", "objected")},
           {"label": "LABOUR COURT", "value": "objection rejected", "sub": "Ext.P11, 12.06.2026: the claim maintainable", "at": A("c06", "rejected")},
           {"label": "HIGH COURT", "value": "writ petition", "sub": "the bank challenges Ext.P11", "at": A("c06", "writ")}])
cue(type="compare", t0=S("c07"), t1=E("c07") + 0.05, head="The arguments", head_at=S("c07") + 0.05,
    cols=[{"title": "The bank", "icon": "landmark", "at": A("c07", "bank")}, {"title": "The employee", "icon": "user", "at": A("c07", "employee")}],
    rows=[{"cells": ["Section 28: the Committee manages the Society", "The Labour Court's order is lawful"], "cells_at": [A("c07", "twenty"), A("c07", "backed")]},
          {"cells": ["Only the Board's appeal order is final", "No writ at the maintainability stage"], "cells_at": [A("c07", "final"), A("c07", "labour")]}])

# ── 4 · before the verdict: the LawWorld request ────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c08"), t1=A("c08", "follow") - 0.05, text="The verdict is next. First, a quick request…", icon="scale", accent=True, at=A("c08", "decided"))
cue(type="list", t0=A("c08", "follow") - 0.05, t1=E("c08") + 0.05, head="Follow LawWorld · lawworld.ai", head_at=A("c08", "follow"),
    items=[{"n": 1, "text": "Search SC and High Court judgments, cited to source", "at": A("c08", "india's")},
           {"n": 2, "text": "Draft petitions, plaints and notices with AI", "at": A("c08", "platform")},
           {"n": 3, "text": "Sign up free · ₹200 AI credit included", "at": A("c08", "advocates")}])

# ── 5 · what the Court held ──────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "president's") - 0.05, text="What did the High Court decide?", icon="scale", accent=True, at=A("c09", "finally"))
cue(type="flow", t0=A("c09", "president's") - 0.05, t1=E("c09") + 0.05, head="Rule 198: punishment and appeal", head_at=A("c09", "president's"),
    steps=[{"label": "The President punishes", "sub": "Rule 198(3): the competent authority", "icon": "landmark", "at": A("c09", "punishment")},
           {"label": "The Board: appeals only", "sub": "Rule 198(4): an Appellate Authority", "icon": "file-text", "at": A("c09", "appellate")},
           {"label": "Appeal: his choice", "sub": "the dismissal order is the punishment", "icon": "check", "tone": "ok", "at": A("c09", "choice")}])
cue(type="verdicts", t0=S("c10"), t1=E("c10") + 0.05,
    rows=[{"text": "No need to exhaust the Rule 198(4) appeal", "ok": True, "at": A("c10", "exhaust")},
          {"text": "Annamma (SC): KCS Act and I.D. Act forums concurrent", "ok": True, "at": A("c10", "concurrent")},
          {"text": "The bank's writ petition", "ok": False, "at": A("c10", "bank's"), "strike_at": A("c10", "dismissed")}])

MUSIC = {"file": "audio/bed_mixkit738_140s.mp3", "target_lufs": -21}   # owner 02-11-2026: trending-style royalty-free bed, audible under the voice
