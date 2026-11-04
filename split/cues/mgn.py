# S.R. Balakrishnan v. State of Tamil Nadu & Ors. (with W.P. 23311/2023 and W.P. 32020/2023), W.P. No. 27070 of 2024, 2026:MHC:4344,
# High Court of Judicature at Madras (C. Kumarappan J.; common order 28.10.2026; listed as Reportable in the court's judis database):
# panel cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND).
# HOOK format (split/JUDGMENT_HOOK_FORMAT.md): c01 hook question (spoken to everyone, no "Advocates,"), c02 curiosity, c03 "Hi, I'm
# Ravishankar" + bench, c04-c05 hiring, absorption and withdrawal, c06-c07 both sides, c08 the LawWorld request, c09-c10 the verdict.
# Facts (para): 521 petitioners (1 + 2 + 518 in the cause titles), Computer Assistants appointed 2006-2013 under MGNREGS on
# consolidated pay after due selection and communal rotation (2); G.O.(Ms) No.37, 22.03.2017: policy decision to absorb them (2, 9);
# G.O.(Ms) No.92, 13.07.2023: absorption withdrawn citing Umadevi (2006) 4 SCC 1 and Daya Lal (2011) 2 SCC 429 (2). Petitioners:
# sanctioned posts (2); overseers under the same scheme absorbed by G.O.(Ms) No.96, 06.06.2008 - Article 14 (4(a)); Umadevi
# distinguishable (5). State (Addl. AG): "in all fairness" not back door entrants (6(a)); contractual, consolidated pay, only while
# the scheme exists (6(a)); no sanctioned post, Nihal Singh (6(c)). Held: recruitment through the Employment Exchange with due
# procedure and communal rotation not seriously disputed (10); Umadevi / Daya Lal concern posts not sanctioned (10); 1,791 Computer
# Assistant posts sanctioned (11, 12); "not sanctioned" plea rejected; scheme permanent by Act 36/2025, post impliedly permanent (13);
# one view in 2017, another in 2023 "without there being any change in law": arbitrary (14); overseers absorbed, denial to others is
# discrimination (15); Sukhendu Bhattacharjee para 76, "model employer" (16); Jaggo: "the Government should be a model employer and
# cannot engage an employee on contractual basis perpetually"; G.O. 92 and Letter 94 quashed as illegal and arbitrary (17); ORDER:
# writs allowed, absorb as Junior Assistant by conducting a Special Qualifying Test per G.O. 37 within twelve weeks of receipt of the
# order, no costs (18). Names: only the lead cause title on the cite card. Not on any card: "mala fide", "change in ruling regime" (14).
# List lines <= 52 chars. No section sign anywhere. Bench photo: brand/judges/c_kumarappan.jpg (official Madras HC portrait,
# hcmadras.tn.gov.in present judges page, admin/view_image.php img_id 248).
FORMAT = "hook"   # build_course_plan.py: no opening sting, 15-frame lead (the cover), name tag on the "Ravishankar" clip

def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
ENDCARD = {"title": "Absorption decided, then withdrawn?", "line": "Quashed as illegal and arbitrary: absorb them as Junior Assistants through a Special Qualifying Test within 12 weeks", "sub": "LawWorld: legal research for advocates"}

# ── 1 · taken back? (hook, curiosity, intro) ─────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "hired"), text="Hired through a proper selection, then picked for absorption. Can the State take it back?", hl="Can the State take it back?")
cue(type="list", t0=S("c02"), t1=A("c02", "was") - 0.05, head="Tamil Nadu · the rural job scheme (MGNREGS)", head_at=S("c02") + 0.05,
    items=[{"n": 1, "text": "Over 500 computer assistants went to court", "at": A("c02", "five")},
           {"n": 2, "text": "Absorption decided, then withdrawn", "at": A("c02", "rural")},
           {"n": 3, "text": "The State relied on Supreme Court rulings", "at": A("c02", "relied")}])
cue(type="point", t0=A("c02", "was") - 0.05, t1=E("c02") + 0.05, text="Was it right?", icon="search", accent=True, at=A("c02", "right"))
cue(type="bench", t0=S("c03"), t1=E("c03") + 0.05, tag="Madras High Court · 28 October 2026",
    judges=[{"name": "Justice C. Kumarappan", "photo": "../brand/judges/c_kumarappan.jpg", "at": A("c03", "honourable")}])

# ── 2 · hired, then dropped ──────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=S("c04"), t1=E("c04") + 0.05, at=A("c04", "between"), tag="HIGH COURT OF MADRAS · 28.10.2026",
    cases=[{"name": "S.R. Balakrishnan v. State of Tamil Nadu, with two connected writs", "cite": "2026:MHC:4344 · W.P. No. 27070 of 2024 & batch"}])
cue(type="timeline", t0=S("c04"), t1=E("c04") + 0.05,
    nodes=[{"label": "HIRED · 2006 TO 2013", "value": "Computer Assistants", "sub": "MGNREGS, on consolidated pay", "at": A("c04", "hired")},
           {"label": "SELECTION", "value": "Employment Exchange", "sub": "due procedure, communal rotation", "at": A("c04", "exchange")}])
cue(type="timeline", t0=S("c05"), t1=E("c05") + 0.05,
    nodes=[{"label": "G.O. 37 · 22 MAR 2017", "value": "Absorb them", "sub": "a policy decision", "at": A("c05", "absorb")},
           {"label": "G.O. 92 · 13 JUL 2023", "value": "Withdrawn", "sub": "citing Umadevi and Daya Lal", "tone": "red", "at": A("c05", "withdrew")}])

# ── 3 · the arguments ────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="compare", t0=S("c06"), t1=E("c07") + 0.05, head="Absorb them, or not?", head_at=S("c06") + 0.05,
    cols=[{"title": "The computer assistants", "icon": "user", "at": A("c06", "computer")}, {"title": "The State", "icon": "landmark", "at": A("c07", "state")}],
    rows=[{"cells": ["Sanctioned posts, unlike Umadevi", "No backdoor entrants, but contract staff"], "cells_at": [A("c06", "sanctioned"), A("c07", "contract")]},
          {"cells": ["Overseers absorbed in 2008: why not us?", "Only while the scheme lasts; no sanctioned post"], "cells_at": [A("c06", "overseers"), A("c07", "sanctioned")]}])

# ── 4 · before the verdict: the LawWorld request ─────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c08"), t1=A("c08", "follow") - 0.05, text="The verdict is next. First, a quick request…", icon="scale", accent=True, at=A("c08", "decided"))
cue(type="list", t0=A("c08", "follow") - 0.05, t1=E("c08") + 0.05, head="Follow LawWorld · lawworld.ai", head_at=A("c08", "follow"),
    items=[{"n": 1, "text": "Search SC and High Court judgments, cited to source", "at": A("c08", "india's")},
           {"n": 2, "text": "Draft petitions, plaints and notices with AI", "at": A("c08", "platform")},
           {"n": 3, "text": "Sign up free · ₹200 AI credit included", "at": A("c08", "advocates")}])

# ── 5 · what the Court held ──────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "posts") - 0.05, text="What did the High Court decide?", icon="scale", accent=True, at=A("c09", "finally"))
cue(type="list", t0=A("c09", "posts") - 0.05, t1=E("c09") + 0.05, head="Umadevi and Daya Lal · no bar here", head_at=A("c09", "posts"),
    items=[{"n": 1, "text": "1,791 Computer Assistant posts were sanctioned", "at": A("c09", "sanctioned")},
           {"n": 2, "text": "Hired by due procedure and communal rotation", "at": A("c09", "hiring")},
           {"n": 3, "text": "One view in 2017, another in 2023: arbitrary", "at": A("c09", "switching")}])
cue(type="point", t0=S("c10"), t1=A("c10", "withdrawal") - 0.05, text="“The Government should be a model employer and cannot engage an employee on contractual basis perpetually.”", icon="quote", accent=True, at=A("c10", "model"))
cue(type="verdicts", t0=A("c10", "withdrawal") - 0.05, t1=E("c10") + 0.05,
    rows=[{"text": "G.O. 92 and Letter 94, withdrawing the absorption", "ok": False, "at": A("c10", "withdrawal")},
          {"text": "Absorb as Junior Assistants via a Special Qualifying Test", "ok": True, "at": A("c10", "absorb")},
          {"text": "Within 12 weeks of receiving the order · no costs", "ok": True, "at": A("c10", "twelve")}])

MUSIC = {"file": "audio/bed_mixkit738_140s.mp3", "target_lufs": -21}   # owner 02-11-2026: trending-style royalty-free bed, audible under the voice
