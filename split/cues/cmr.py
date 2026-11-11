# Chatur Singh Dhruw v. The State of Chhattisgarh & Ors., 2026 INSC 1205, Civil Appeal No. 14172 of 2026 (from SLP (C) No. 24392 of
# 2023, with the connected appeal from SLP (C) No. 25201 of 2023), Supreme Court of India (Manmohan J. wrote it, Shree Chandrashekhar J.;
# pronounced 06.11.2026; REPORTABLE on page 1): panel cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND).
# Appeal number: blank on the PDF's page 1, taken from the sci.gov.in "Latest Judgments" listing ("C.A. No. 14172/2026").
# HOOK format (split/JUDGMENT_HOOK_FORMAT.md): c01 hook question (spoken to everyone, no "Advocates,"), c02 curiosity, c03 "Hi, I'm
# Ravishankar" + bench, c04-c05 the careers and the 2017 review, c06-c07 the result, the High Court and both sides, c08 the LawWorld
# request, c09-c10 the verdict. DRAFT 11-11-2026, awaiting the owner's yes.
# Facts (para): Peons (Class-IV), Legal Metrology Department, Raipur, 1989 and 1993; Assistant Grade-III 2012 and 2013; regularised
# 19.06.2015 (3, 40). GAD Circular 25.04.2017: review of those with 50 years of age or 20 years of qualifying service, FR 56 + Rule 42 CG
# Civil Services (Pension) Rules 1976 (4, 31). Screening Committee met 04.09.2017 (13); 14 clerical staff (16); grades scored A+ = 5 ...
# D = 1, averaged over 2013-2017 (17(f), 19); 5 below the 'B' benchmark (18, 33), 9 retained (38); one appellant 'A' in 2013, then 'C'
# for four years (22, 41). Orders of 09.10.2017: "retired with immediate effect" in the public interest (5, 45). Single Judge declined
# to interfere 23.08.2019; Division Bench (WA 565 and 577 of 2019) affirmed 12.04.2023 (2). Appellants: others similarly placed spared
# (6), punitive and stigmatic in substance (7), a substitute for disciplinary proceedings (8), entries never communicated (10),
# promotion/regularisation made earlier entries lose significance (11). State: uniform application to all 14 (18).
# Held: "neither punitive nor stigmatic in character"; audi alteram partem and Article 311(2) do not apply to an order made under the
# service rules (24); no "re-weighing of the material by the Court" (27); interference only for no evidence, non-application of mind,
# manifest arbitrariness or perversity, mala fides (28); no negative equality (29, 30); parameters uniformly applied (36); entries
# after promotion not effaced (39-42); regularisation no endorsement (43); uncommunicated remarks no ground to quash (48); Dev Dutt and
# Sukhdev Singh "rendered in the context of promotion" (49); no arbitrariness, mala fides, perversity (50); HC judgments of 12.04.2023
# affirmed, appeals dismissed, no costs (51).
# Names: only the cause title on the cite card; no appellant or committee member named anywhere else. List lines <= 52 chars.
# Bench photos: brand/judges/manmohan.jpg (official sci.gov.in portrait, fetched 11-11-2026), brand/judges/shree_chandrashekhar.jpg.
FORMAT = "hook"   # build_course_plan.py: no opening sting, 15-frame lead (the cover), name tag on the "Ravishankar" clip

def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
ENDCARD = {"title": "Retired early, without a hearing?", "line": "Compulsory retirement under the rules is neither punitive nor stigmatic: courts check the material, not re-weigh it", "sub": "LawWorld: legal research for advocates"}

# ── 1 · retired early, no hearing? (hook, curiosity, intro) ───────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "you"), text="20+ years in government service. No inquiry against you, but poor grades. Can you still be retired early, without a hearing?", hl="Can you still be retired early, without a hearing?")
cue(type="list", t0=S("c02"), t1=A("c02", "were", 3) - 0.05, head="Two clerks, retired early", head_at=S("c02") + 0.05,
    items=[{"n": 1, "text": "Retired “with immediate effect” · 9 Oct 2017", "at": A("c02", "retired")},
           {"n": 2, "text": "Their plea: a punishment in disguise", "at": A("c02", "punishment")},
           {"n": 3, "text": "Poor grades never communicated to them", "at": A("c02", "never")}])
cue(type="point", t0=A("c02", "were", 3) - 0.05, t1=E("c02") + 0.05, text="Were they right?", icon="search", accent=True, at=A("c02", "right"))
cue(type="bench", t0=S("c03"), t1=E("c03") + 0.05, tag="Supreme Court of India · 6 November 2026",
    judges=[{"name": "Justice Manmohan", "photo": "../brand/judges/manmohan.jpg", "at": A("c03", "honourable")},
            {"name": "Justice Shree Chandrashekhar", "photo": "../brand/judges/shree_chandrashekhar.jpg", "at": A("c03", "honourable", 2)}])

# ── 2 · the review ───────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=S("c04"), t1=E("c04") + 0.05, at=A("c04", "both"), tag="SUPREME COURT OF INDIA · 06.11.2026",
    cases=[{"name": "Chatur Singh Dhruw v. The State of Chhattisgarh & Ors.", "cite": "2026 INSC 1205 · Civil Appeal No. 14172 of 2026"}])
cue(type="timeline", t0=S("c04"), t1=E("c04") + 0.05,
    nodes=[{"label": "JOINED AS PEONS", "value": "1989 · 1993", "sub": "Legal Metrology Dept., Raipur", "at": A("c04", "joined")},
           {"label": "PROMOTED", "value": "2012 · 2013", "sub": "to Assistant Grade-III", "at": A("c04", "promoted")},
           {"label": "REGULARISED", "value": "June 2015", "sub": "in the same post", "at": A("c04", "thirteen")}])
cue(type="list", t0=S("c05"), t1=E("c05") + 0.05, head="GAD Circular · 25 April 2017", head_at=S("c05") + 0.05,
    items=[{"n": 1, "text": "Review staff aged 50, or with 20 years' service", "at": A("c05", "review")},
           {"n": 2, "text": "FR 56 · Rule 42, CG Civil Services (Pension) Rules", "at": A("c05", "served")},
           {"n": 3, "text": "Screening Committee, 4 Sep 2017: 14 clerks", "at": A("c05", "committee")}])

# ── 3 · a punishment in disguise? ────────────────────────────────────────────────────────────────────────────────────
cue(type="counters", t0=S("c06"), t1=A("c06", "high") - 0.05, head="The Screening Committee's review", head_at=S("c06") + 0.05,
    items=[{"value": 14, "unit": "CLERKS", "label": "Reviewed", "sub": "age 50, or 20 years' service", "at": A("c06", "found")},
           {"value": 5, "unit": "BELOW 'B'", "label": "Recommended for retirement", "sub": "including the two appellants", "tone": "red", "at": A("c06", "five")},
           {"value": 9, "unit": "RETAINED", "label": "Met the standard", "at": A("c06", "benchmark")}])
cue(type="flow", t0=A("c06", "high") - 0.05, t1=E("c06") + 0.05, head="Chhattisgarh High Court · no interference", head_at=A("c06", "high"),
    steps=[{"label": "Retired", "sub": "9 October 2017", "icon": "file-text", "at": A("c06", "high")},
           {"label": "Single Judge", "sub": "2019: declined to interfere", "icon": "scale", "at": A("c06", "single")},
           {"label": "Division Bench", "sub": "12 April 2023: affirmed", "icon": "landmark", "at": A("c06", "division")}])
cue(type="compare", t0=S("c07"), t1=E("c07") + 0.05, head="Punishment, or public interest?", head_at=S("c07") + 0.05,
    cols=[{"title": "The appellants", "icon": "users", "at": A("c07", "they")}, {"title": "State of Chhattisgarh", "icon": "landmark", "at": A("c07", "state")}],
    rows=[{"cells": ["Others like them were spared", "All 14 judged by the same yardstick"], "cells_at": [A("c07", "spared"), A("c07", "fourteen")]},
          {"cells": ["Promotion wiped out old remarks", "2013-17 grades scored and averaged"], "cells_at": [A("c07", "promotion"), A("c07", "yardstick")]}])

# ── 4 · before the verdict: the LawWorld request ─────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c08"), t1=A("c08", "follow") - 0.05, text="The verdict is next. First, a quick request…", icon="scale", accent=True, at=A("c08", "decided"))
cue(type="list", t0=A("c08", "follow") - 0.05, t1=E("c08") + 0.05, head="Follow LawWorld · lawworld.ai", head_at=A("c08", "follow"),
    items=[{"n": 1, "text": "Search SC and High Court judgments, cited to source", "at": A("c08", "india's")},
           {"n": 2, "text": "Draft petitions, plaints and notices with AI", "at": A("c08", "platform")},
           {"n": 3, "text": "Sign up free · ₹200 AI credit included", "at": A("c08", "advocates")}])

# ── 5 · what the Court held ──────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "under") - 0.05, text="What did the Supreme Court decide?", icon="scale", accent=True, at=A("c09", "finally"))
cue(type="list", t0=A("c09", "under") - 0.05, t1=E("c09") + 0.05, head="Compulsory retirement under the rules", head_at=A("c09", "under"),
    items=[{"n": 1, "text": "“neither punitive nor stigmatic in character”", "at": A("c09", "punishment")},
           {"n": 2, "text": "Audi alteram partem, Art. 311(2): not applicable", "at": A("c09", "hearing")},
           {"n": 3, "text": "No “re-weighing of the material by the Court”", "at": A("c09", "re-weigh")}])
cue(type="list", t0=S("c10"), t1=A("c10", "with") - 0.05, head="Also held", head_at=S("c10") + 0.05,
    items=[{"n": 1, "text": "Grades recorded after promotion still count", "at": A("c10", "grades")},
           {"n": 2, "text": "Uncommunicated remarks alone: no ground to quash", "at": A("c10", "never")},
           {"n": 3, "text": "Dev Dutt & Sukhdev Singh were promotion cases", "at": A("c10", "shown")}])
cue(type="verdicts", t0=A("c10", "with") - 0.05, t1=E("c10") + 0.05,
    rows=[{"text": "Plea: a punishment in disguise", "ok": False, "at": A("c10", "with")},
          {"text": "Plea: others like them were spared", "ok": False, "at": A("c10", "mala")},
          {"text": "Plea: promotion wiped out the low grades", "ok": False, "at": A("c10", "arbitrariness")},
          {"text": "HC judgments affirmed · appeals dismissed", "ok": True, "at": A("c10", "dismissed")}])

MUSIC = {"file": "audio/bed_mixkit738_140s.mp3", "target_lufs": -21}   # owner 02-11-2026: trending-style royalty-free bed, audible under the voice
