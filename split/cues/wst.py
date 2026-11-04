# The Secretary to Government, MAWS Department, Government of Tamil Nadu & Anr. v. Waste Management Operators Association of South
# India, W.A. No. 3362 of 2026, 2026:MHC:4432, High Court of Judicature at Madras (Division Bench: Sushrut Arvind Dharmadhikari CJ
# delivered it, G. Arul Murugan J.; dated and uploaded 03.11.2026; listed as Reportable in the court's judis database, "Index : Yes"):
# panel cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND).
# HOOK format (split/JUDGMENT_HOOK_FORMAT.md): c01 hook question (spoken to everyone, no "Advocates,"), c02 curiosity (can the State
# appeal an interim stay?), c03 "Hi, I'm Ravishankar" + bench, c04-c05 the G.O. and the stay, c06-c07 both sides, c08 the LawWorld
# request, c09-c10 the verdict.
# Facts (para): State's Clause 15 Letters Patent appeal against the interlocutory order of 30.10.2026 in W.M.P. 50214/2026 in
# W.P. 44715/2026 (1); "omnibus stay" of G.O. (Ms.) No. 181, MAWS (ME.3) Department, 09.10.2026: restructuring and execution of Solid
# Waste Management operations under "Category II" across 147 Urban Local Bodies (1); issue: an expansive interim order that in effect
# granted the final relief (2). Advocate General: executive domain, Article 243W / Entry 6 Twelfth Schedule (3.1); no vested right to
# perpetual renewals or to insist on outsourcing (3.3); "complete sanitation paralysis" (3.5). Respondent: Category I / II "without
# any intelligible differentia", Article 14 (4.2); investments in compactor trucks etc. under the 2022 policy, legitimate expectation,
# Article 19(1)(g) (4.3); the State ought to have sought to vacate the stay before the Single Judge (4.4). Held: an order with the
# characteristics of a "judgment" is appealable (5, 6: Midnapore, (2006) 5 SCC 399); not routine - "by paralyzing essential municipal
# sanitation operations across 147 urban centres and altering vital legal rights" (7); "When private commercial expectations are
# pitted against overwhelming public interest, public interest must decisively prevail."; balance of convenience "overwhelmingly in
# favour of the State" (8; N.G. Projects, (2022) 6 SCC 127; NHSRCL v. Montecarlo, (2022) 6 SCC 401); order of 30.10.2026 set aside
# (9); appeal allowed, "full liberty to implement G.O. (Ms.) No.181", no costs (10); observations "strictly prima facie", merits for
# the Single Judge, counter in three weeks, W.P. to be expedited (closing paragraph after 10).
# Not on any card: the State's allegations against intermediaries (3.2: EPF/ESI, "ghost workers", profiteering), its attack on the
# association's standing and the Rs.616.28 crore figure (3.4) - a neutral reel. The association is named on the cite card only.
# No section sign anywhere. List lines <= 52 chars. Bench photos: brand/judges/sushrut_arvind_dharmadhikari.jpg (official
# hcmadras.tn.gov.in portrait, img_id 641, as ikc/msm), brand/judges/g_arul_murugan.jpg (official, present judges page, img_id 619, as msm).
FORMAT = "hook"   # build_course_plan.py: no opening sting, 15-frame lead (the cover), name tag on the "Ravishankar" clip

def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
ENDCARD = {"title": "Waste plan stayed: can the State appeal?", "line": "Yes: the blanket stay was no routine order; public interest prevailed, the stay was set aside, and the main case continues", "sub": "LawWorld: legal research for advocates"}

# ── 1 · a stay on the waste plan (hook, curiosity, intro) ────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "state"), text="A new waste plan for 147 urban centres. A court stays the whole plan. Should it freeze public sanitation?", hl="freeze public sanitation?")
cue(type="list", t0=S("c02"), t1=A("c02", "can") - 0.05, head="One waste plan, one blanket stay", head_at=S("c02") + 0.05,
    items=[{"n": 1, "text": "Private waste operators: the plan is arbitrary", "at": A("c02", "arbitrary")},
           {"n": 2, "text": "A Single Judge: the whole plan stayed", "at": A("c02", "stayed")}])
cue(type="point", t0=A("c02", "can") - 0.05, t1=E("c02") + 0.05, text="Can the State appeal an interim stay?", icon="search", accent=True, at=A("c02", "appeal"))
cue(type="bench", t0=S("c03"), t1=E("c03") + 0.05, tag="Madras High Court · 3 November 2026",
    judges=[{"name": "Chief Justice Sushrut Arvind Dharmadhikari", "photo": "../brand/judges/sushrut_arvind_dharmadhikari.jpg", "at": A("c03", "honourable")},
            {"name": "Justice G. Arul Murugan", "photo": "../brand/judges/g_arul_murugan.jpg", "at": A("c03", "honourable", 2)}])

# ── 2 · one order, one stay ──────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=S("c04"), t1=E("c04") + 0.05, at=A("c04", "tamil"), tag="HIGH COURT OF MADRAS · 03.11.2026",
    cases=[{"name": "The Secretary to Government, MAWS Department & Anr. v. Waste Management Operators Association of South India", "cite": "2026:MHC:4432 · W.A. No. 3362 of 2026"}])
cue(type="timeline", t0=S("c04"), t1=E("c04") + 0.05,
    nodes=[{"label": "GOVERNMENT ORDER", "value": "9 Oct 2026", "sub": "G.O. (Ms.) No. 181 · MAWS Dept", "at": A("c04", "government")},
           {"label": "CATEGORY II", "value": "147 ULBs", "sub": "solid waste operations restructured", "at": A("c04", "solid")}])
cue(type="timeline", t0=S("c05"), t1=E("c05") + 0.05,
    nodes=[{"label": "WRIT PETITION", "value": "W.P. 44715/2026", "sub": "by the waste operators' association", "at": A("c05", "challenged")},
           {"label": "BLANKET STAY", "value": "30 Oct 2026", "sub": "the whole G.O. stayed", "tone": "red", "at": A("c05", "stayed")},
           {"label": "WRIT APPEAL", "value": "W.A. 3362/2026", "sub": "by the State · Clause 15", "at": A("c05", "appealed")}])

# ── 3 · both sides ───────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="compare", t0=S("c06"), t1=E("c07") + 0.05, head="Stay the waste plan?", head_at=S("c06") + 0.05,
    cols=[{"title": "The State", "icon": "landmark", "at": A("c06", "state")}, {"title": "The operators", "icon": "user", "at": A("c07", "operators")}],
    rows=[{"cells": ["Waste policy: the executive's domain", "Two categories: no rational basis"], "cells_at": [A("c06", "policy"), A("c07", "categories")]},
          {"cells": ["No right to endless contract renewals", "Invested in trucks under the 2022 policy"], "cells_at": [A("c06", "renewals"), A("c07", "invested")]},
          {"cells": ["A blanket stay: sanitation paralysis", "Ask the Single Judge to lift it first"], "cells_at": [A("c06", "paralysis"), A("c07", "first")]}])

# ── 4 · before the verdict: the LawWorld request ─────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c08"), t1=A("c08", "follow") - 0.05, text="The verdict is next. First, a quick request…", icon="scale", accent=True, at=A("c08", "decided"))
cue(type="list", t0=A("c08", "follow") - 0.05, t1=E("c08") + 0.05, head="Follow LawWorld · lawworld.ai", head_at=A("c08", "follow"),
    items=[{"n": 1, "text": "Search SC and High Court judgments, cited to source", "at": A("c08", "india's")},
           {"n": 2, "text": "Draft petitions, plaints and notices with AI", "at": A("c08", "platform")},
           {"n": 3, "text": "Sign up free · ₹200 AI credit included", "at": A("c08", "advocates")}])

# ── 5 · what the Court held ──────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "this") - 0.05, text="What did the High Court decide?", icon="scale", accent=True, at=A("c09", "finally"))
cue(type="point", t0=A("c09", "this") - 0.05, t1=E("c09") + 0.05, text="Not a routine order: the stay paralysed sanitation across 147 urban centres, so the State's appeal lies (Clause 15)", icon="scale", accent=True, at=A("c09", "routine"))
cue(type="point", t0=S("c10"), t1=A("c10", "so") - 0.05, text="“When private commercial expectations are pitted against overwhelming public interest, public interest must decisively prevail.”", icon="quote", accent=True, at=A("c10", "public"))
cue(type="verdicts", t0=A("c10", "so") - 0.05, t1=E("c10") + 0.05,
    rows=[{"text": "The blanket stay of 30 October 2026: set aside", "ok": False, "at": A("c10", "stay")},
          {"text": "Liberty to implement G.O. 181", "ok": True, "at": A("c10", "aside")},
          {"text": "Prima facie only: the Single Judge decides the merits", "ok": True, "at": A("c10", "continues")}])

MUSIC = {"file": "audio/bed_mixkit738_140s.mp3", "target_lufs": -21}   # owner 02-11-2026: trending-style royalty-free bed, audible under the voice
