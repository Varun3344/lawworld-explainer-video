# Arjun Gopal & Ors. v. Union of India & Ors., 2026 INSC 1181, I.A.s in W.P. (C) No. 728/2015 with Suo Motu W.P. (C) No. 15/2026,
# Supreme Court of India (an ORDER of M.M. Sundresh J. and Prasanna B. Varale J.; New Delhi, 29.10.2026, REPORTABLE): panel cues, run by
# split/build_course_plan.py (helpers: at S E cue fx have r3 PEND). HOOK format (split/JUDGMENT_HOOK_FORMAT.md): c01 hook question,
# c02 curiosity, c03 "Hi, I'm Ravishankar" + bench, c04-c07 history / the test year / the pleas / the Constitution, c08 the LawWorld
# request, c09-c10 the verdict. Source: the Court's own PDF (23 pages, scratchpad sc3nov/pdf/arjun_gopal_2026INSC1181.pdf).
# Facts from the order (paras): interventions of the Delhi Fireworks Shopkeepers Association and the Federation of Fireworks Traders
# allowed (1); severe air and noise pollution, AQI spikes after the festival, more so in Delhi-NCR (6); 23.10.2018, Arjun Gopal:
# reduced-emission ("improved") and green crackers permitted, held the field till 2024 (10); GNCTD, 19.12.2024: a complete perpetual
# ban on manufacturing, storage, selling and bursting all kinds of firecrackers throughout the year, from 01.01.2025; UP and Haryana a
# similar ban in their NCR parts (11); 15.10.2025 (M.C. Mehta): green crackers, bursting 6-7 AM and 8-10 PM on the day before and on
# Diwali, "only on a test case basis" (14, 15); the IAs - shopkeepers: restore cancelled licences; traders: allow CSIR-NEERI green
# crackers; MoEF&CC: reduced Barium Nitrate formulations; petitioners: a complete ban on all firecrackers (17); the amicus: a complete
# ban and a health assessment of Delhi-NCR (18); the intervenors: no licences "would facilitate the business of illegal firecrackers,
# manufactured and transported from across the border" (19); Article 25(1) "certainly subject to public order, morality, health";
# Article 21: "a healthy, safe and a pollution-free environment"; a practice with a religious colour "is only a qualified one" (22);
# "the problem lies in the implementation" (23); "Though imposition of a blanket ban seems to be the ideal solution", the Court "is
# short of adequate data"; "no significant improvement in the AQI readings" (25); the 2025 relaxation was also to let the States
# determine the effects; "the State has utterly failed in complying with the directions thereunder" (26); the amicus's note: an AQI
# spike on Dussehra this year despite the ban; conventional firecrackers sold "under the guise of Green Crackers" (27); regulate
# "instead of maintaining the complete ban", "for a temporary period" (28); directions (29): A bursting only 6-7 AM and 8-10 PM on 7 and
# 8 November 2026; B no bursting within 300 metres of hospitals, nursing homes, health centres, old-age homes, silence zones and
# educational institutions; C/E only CSIR-NEERI listed green crackers, no Barium, no 'ladis'; F product-specific QR codes; G cancelled
# licences restored 04-06.11.2026; I sale only at designated places, none online; U "the complete ban ... shall be restored with effect
# from 09.11.2026"; V affidavits by 14.12.2026; IAs listed on 16.12.2026 (33).
# NOT on any card: that the plea for a complete ban was dismissed (it was not; regulation is "for a temporary period"); "smuggled".
# No section sign anywhere. List lines <= 52 chars. Official sci.gov.in portraits on the bench card.
FORMAT = "hook"   # build_course_plan.py: no opening sting, 15-frame lead (the cover), name tag on the "Ravishankar" clip

def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
ENDCARD = {"title": "Can you burst crackers in Delhi this Diwali?", "line": "Only approved green crackers, on 7 and 8 November, at fixed hours; the complete ban returns on 9 November", "sub": "LawWorld: legal research for advocates"}

# ── 1 · crackers this Diwali? (hook, curiosity, intro) ──────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "burst"), text="Can you burst crackers in Delhi this Diwali, under a complete, year-round ban?", hl="under a complete, year-round ban?")
cue(type="list", t0=S("c02"), t1=A("c02", "so") - 0.05, head="Delhi-NCR, even with the complete ban", head_at=S("c02") + 0.05,
    items=[{"n": 1, "text": "No significant improvement in AQI readings", "at": A("c02", "significant")},
           {"n": 2, "text": "Amicus's note: an AQI spike on Dussehra too", "at": A("c02", "quality")},
           {"n": 3, "text": "Conventional crackers sold as “Green Crackers”", "at": A("c02", "ordinary")}])
cue(type="point", t0=A("c02", "so") - 0.05, t1=E("c02") + 0.05, text="So does a ban work?", icon="search", accent=True, at=A("c02", "so"))
cue(type="bench", t0=S("c03"), t1=E("c03") + 0.05, tag="Supreme Court of India · 29 October 2026",
    judges=[{"name": "Justice M.M. Sundresh", "photo": "../brand/judges/mm_sundresh.jpg", "at": A("c03", "honourable")},
            {"name": "Justice Prasanna B. Varale", "photo": "../brand/judges/prasanna_b_varale.jpg", "at": A("c03", "honourable", 2)}])

# ── 2 · from green to a total ban ───────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=S("c04"), t1=E("c04") + 0.05, at=A("c04", "arjun"), tag="SUPREME COURT OF INDIA · 29.10.2026",
    cases=[{"name": "Arjun Gopal & Ors. v. Union of India & Ors.", "cite": "2026 INSC 1181 · I.A.s in W.P. (C) No. 728 of 2015"}])
cue(type="timeline", t0=S("c04"), t1=E("c04") + 0.05,
    nodes=[{"label": "ARJUN GOPAL · 2018", "value": "green crackers allowed", "sub": "reduced-emission and green crackers", "at": A("c04", "allowed")},
           {"label": "DELHI · DECEMBER 2024", "value": "a complete ban", "sub": "all year, from 1 January 2025", "tone": "red", "at": A("c04", "banned")}])
cue(type="flow", t0=S("c05"), t1=E("c05") + 0.05, head="The test year: October 2025", head_at=S("c05") + 0.05,
    steps=[{"label": "Green crackers on two days", "sub": "at fixed hours · a test", "icon": "calendar", "at": A("c05", "allowed")},
           {"label": "States to study the effect", "sub": "environment and health", "icon": "search", "at": A("c05", "study")},
           {"label": "The State “utterly failed”", "sub": "in complying", "icon": "info", "tone": "stop", "at": A("c05", "utterly")}])

# ── 3 · ban or regulate? ────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="compare", t0=S("c06"), t1=E("c06") + 0.05, head="The pleas before the Court", head_at=S("c06") + 0.05,
    cols=[{"title": "Petitioners, amicus", "icon": "user", "at": A("c06", "petitioners")}, {"title": "Fireworks traders", "icon": "landmark", "at": A("c06", "traders")}],
    rows=[{"cells": ["A complete ban on all firecrackers", "Restore the cancelled licences"], "cells_at": [A("c06", "complete"), A("c06", "licences")]},
          {"cells": ["A health assessment of Delhi-NCR", "Refusing licences aids illegal cross-border crackers"], "cells_at": [A("c06", "ban"), A("c06", "illegal")]}])
cue(type="point", t0=S("c07"), t1=A("c07", "article", 2) - 0.05, text="Article 25(1): religious practice is “subject to public order, morality, health”", icon="scale", at=A("c07", "religious"))
cue(type="point", t0=A("c07", "article", 2) - 0.05, t1=E("c07") + 0.05, text="Article 21: “a healthy, safe and a pollution-free environment”", icon="scale", accent=True, at=A("c07", "protects"))

# ── 4 · before the verdict: the LawWorld request ────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c08"), t1=A("c08", "follow") - 0.05, text="The verdict is next. First, a quick request…", icon="scale", accent=True, at=A("c08", "decided"))
cue(type="list", t0=A("c08", "follow") - 0.05, t1=E("c08") + 0.05, head="Follow LawWorld · lawworld.ai", head_at=A("c08", "follow"),
    items=[{"n": 1, "text": "Search SC and High Court judgments, cited to source", "at": A("c08", "india's")},
           {"n": 2, "text": "Draft petitions, plaints and notices with AI", "at": A("c08", "platform")},
           {"n": 3, "text": "Sign up free · ₹200 AI credit included", "at": A("c08", "advocates")}])

# ── 5 · what the Court held ─────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "blanket") - 0.05, text="What did the Supreme Court decide?", icon="scale", accent=True, at=A("c09", "finally"))
cue(type="list", t0=A("c09", "blanket") - 0.05, t1=E("c09") + 0.05, head="Ban or regulate?", head_at=A("c09", "blanket"),
    items=[{"n": 1, "text": "A blanket ban “seems to be the ideal solution”", "at": A("c09", "ideal")},
           {"n": 2, "text": "But the Court is “short of adequate data”", "at": A("c09", "data")},
           {"n": 3, "text": "So: regulate, “for a temporary period”", "at": A("c09", "now")}])
cue(type="verdicts", t0=S("c10"), t1=E("c10") + 0.05,
    rows=[{"text": "Only NEERI-approved green crackers", "ok": True, "at": A("c10", "approved")},
          {"text": "7 and 8 November: 6-7 AM and 8-10 PM only", "ok": True, "at": A("c10", "seventh")},
          {"text": "No bursting within 300 m of hospitals, schools", "ok": True, "at": A("c10", "night")},
          {"text": "Complete ban restored from 9 November", "ok": True, "at": A("c10", "ninth")}])

MUSIC = {"file": "audio/bed_mixkit738_140s.mp3", "target_lufs": -21}   # owner 02-11-2026: trending-style royalty-free bed, audible under the voice
