FORMAT = "hook"   # build_course_plan.py: no opening sting, 15-frame lead (the cover), name tag on the "Ravishankar" clip
# Malabar Medical College Hospital & Research Centre v. Lobish L.B. & Anr., W.A. No. 1899 of 2026, 2026:KER:81416, High Court of
# Kerala (Devan Ramachandran J. wrote it, Basant Balaji J.; delivered on admission, 23.10.2026, "CR"): panel cues, run by
# split/build_course_plan.py (helpers: at S E cue fx have r3 PEND). HOOK format (split/JUDGMENT_HOOK_FORMAT.md): c01 hook question,
# c02 curiosity, c03 "Hi, I'm Ravishankar" + bench, c04-c07 facts / case / both sides, c08 the LawWorld request, c09-c10 the verdict.
# Facts from the judgment (paras): appeal against the Single Judge's judgment of 19.06.2026 in WP(C) 13971/2025 (the hospital the
# writ petitioner), so far as it holds the Minimum Wages Act notification of 23.04.2018 still in force (1); WP(C) 15243 and 14778 of
# 2018 by an Association of Nurses and owners of Private Hospitals; notification quashed by a Single Judge on 23.01.2023; W.A. 1002
# and 988 of 2023 pending, operation and enforcement "will remain stayed and shall be kept in abeyance" (2, 6); the hospital: Ext.P4,
# the Labour Court, Kozhikode order built solely on the notification, cannot be enforced (2); the employee: the quashing is fully
# stayed; Ext.P4 came while the notification was in force (3); Ext.P4 dated 07.11.2022, quashing only 23.01.2023, "would not take
# away its worth" (5); Shree Chamundi Mopeds (MANU/SC/0501/1992): quashing restores the position as on the date of the order, a stay
# only makes it inoperative from the date of the stay (7); a stayed Single Judge's judgment ceases to be in effect, "at least
# thereafter" (8); Ext.P4 can be put into operation, particularly given the interim stay (9); neither the quashing nor the stay has
# any real impact on Ext.P4, issued much earlier (10); no affirmative ruling on whether the notification is in force (11); "we cannot
# find the judgment impugned to be in error"; that question is for the Bench deciding W.A. No. 988/2023 (12). Ext.P4 = "the said
# Award" (9). Not on any card: the respondent's "admitted ... paying other employees" line (3, a party's submission); amounts in Ext.P4.
# No section sign anywhere. List lines <= 52 chars. Official highcourt.kerala.gov.in portraits on the bench card.

def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
ENDCARD = {"title": "Quashed later: does the Labour Court order fall?", "line": "No: passed while the notification was in force, it keeps its worth · a stay is not a quashing", "sub": "LawWorld: legal research for advocates"}

# ── 1 · quashed later: does it fall? (hook, curiosity, intro) ───────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "minimum"), text="If a wage notification is quashed later, does a Labour Court order already passed under it fall too?", hl="fall too?")
cue(type="list", t0=S("c02"), t1=A("c02", "so") - 0.05, head="One order, three turns", head_at=S("c02") + 0.05,
    items=[{"n": 1, "text": "Labour Court order: November 2022", "at": A("c02", "labour")},
           {"n": 2, "text": "Wage notification quashed: January 2023", "at": A("c02", "quashed")},
           {"n": 3, "text": "The quashing itself: stayed in appeal", "at": A("c02", "stayed")}])
cue(type="point", t0=A("c02", "so") - 0.05, t1=E("c02") + 0.05, text="So can the order still be enforced?", icon="search", accent=True, at=A("c02", "can"))
cue(type="bench", t0=S("c03"), t1=E("c03") + 0.05, tag="Kerala High Court · 23 October 2026",
    judges=[{"name": "Justice Devan Ramachandran", "photo": "../brand/judges/devan_ramachandran.jpg", "at": A("c03", "honourable")},
            {"name": "Justice Basant Balaji", "photo": "../brand/judges/basant_balaji.jpg", "at": A("c03", "honourable", 2)}])

# ── 2 · the wage notification ───────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c04"), t1=E("c04") + 0.05, head="Minimum Wages Act, 1948", head_at=S("c04") + 0.05,
    steps=[{"label": "Wage notification issued", "sub": "State Government · 23 April 2018", "icon": "file-text", "at": A("c04", "issued")},
           {"label": "Labour Court, Kozhikode", "sub": "relies on the notification", "icon": "landmark", "at": A("c04", "labour")},
           {"label": "Order for the employee", "sub": "Ext.P4 · against the hospital", "icon": "user", "at": A("c04", "ruled")}])
cue(type="cite", t0=S("c05"), t1=E("c06") + 0.05, at=A("c05", "came"), tag="HIGH COURT OF KERALA · 23.10.2026",
    cases=[{"name": "Malabar Medical College Hospital & Research Centre v. Lobish L.B. & Anr.", "cite": "2026:KER:81416 · W.A. No. 1899 of 2026"}])
cue(type="timeline", t0=S("c05"), t1=E("c05") + 0.05,
    nodes=[{"label": "LABOUR COURT", "value": "Ext.P4 order", "sub": "7 November 2022 · notification in force", "at": A("c05", "november")},
           {"label": "SINGLE JUDGE", "value": "notification quashed", "sub": "23 January 2023 · nurses' and hospitals' petitions", "tone": "red", "at": A("c05", "quashed")}])

# ── 3 · a stay on the quashing ──────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="timeline", t0=S("c06"), t1=E("c06") + 0.05,
    nodes=[{"label": "DIVISION BENCH", "value": "quashing stayed", "sub": "W.A. 1002 and 988 of 2023 · kept in abeyance", "at": A("c06", "stayed")},
           {"label": "SINGLE JUDGE", "value": "still in force", "sub": "19 June 2026 · the judgment under appeal", "at": A("c06", "held")}])
cue(type="compare", t0=S("c07"), t1=E("c07") + 0.05, head="Before the appeal bench", head_at=S("c07") + 0.05,
    cols=[{"title": "The hospital", "icon": "landmark", "at": A("c07", "hospital")}, {"title": "The employee", "icon": "user", "at": A("c07", "employee")}],
    rows=[{"cells": ["Ext.P4 rests only on the notification", "Ext.P4 came first: November 2022"], "cells_at": [A("c07", "rests"), A("c07", "first")]},
          {"cells": ["Quashed, so Ext.P4 cannot be enforced", "The quashing stands stayed"], "cells_at": [A("c07", "enforced"), A("c07", "quashing")]}])

# ── 4 · before the verdict: the LawWorld request ────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c08"), t1=A("c08", "follow") - 0.05, text="The verdict is next. First, a quick request…", icon="scale", accent=True, at=A("c08", "decided"))
cue(type="list", t0=A("c08", "follow") - 0.05, t1=E("c08") + 0.05, head="Follow LawWorld · lawworld.ai", head_at=A("c08", "follow"),
    items=[{"n": 1, "text": "Search SC and High Court judgments, cited to source", "at": A("c08", "india's")},
           {"n": 2, "text": "Draft petitions, plaints and notices with AI", "at": A("c08", "platform")},
           {"n": 3, "text": "Sign up free · ₹200 AI credit included", "at": A("c08", "advocates")}])

# ── 5 · what the Court held ─────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "later") - 0.05, text="What did the High Court decide?", icon="scale", accent=True, at=A("c09", "finally"))
cue(type="notequal", t0=A("c09", "later") - 0.05, t1=E("c09") + 0.05, left="Notification quashed later", right="the order loses its worth",
    at=A("c09", "worth"), left_at=A("c09", "later"), sub="Ext.P4 came on 7 November 2022, while the notification was in force", sub_at=A("c09", "passed"))
cue(type="point", t0=S("c10"), t1=A("c10", "court") - 0.05, text="Shree Chamundi Mopeds (Supreme Court): a stay is not a quashing; it bites only from the date of the stay", icon="scale", accent=True, at=A("c10", "stay"))
cue(type="verdicts", t0=A("c10", "court") - 0.05, t1=E("c10") + 0.05,
    rows=[{"text": "The hospital's plea: Ext.P4 cannot be enforced", "ok": False, "at": A("c10", "found")},
          {"text": "The Single Judge's judgment: no error found", "ok": True, "at": A("c10", "error")},
          {"text": "Notification in force or not: left to W.A. 988/2023", "ok": True, "at": A("c10", "fate")}])

MUSIC = {"file": "audio/bed_mixkit738_140s.mp3", "target_lufs": -21}   # owner 02-11-2026: trending-style royalty-free bed, audible under the voice
