# Sri Sridhara Babu v. Karnataka State Financial Corporation & Ors., COMAP No. 446 of 2026, 2026:KHC:59867-DB, High Court of Karnataka
# at Bengaluru (Division Bench: D K Singh J. wrote the oral judgment, H. Shanthi Bhushan J.; 28.10.2026; "R" on page 1): panel cues,
# run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND).
# HOOK format (split/JUDGMENT_HOOK_FORMAT.md): c01 hook question (spoken to everyone, no "Advocates,"), c02 curiosity (names the
# court: c03 has no room), c03 "Hi, I'm Ravishankar" + bench, c04-c06 the loan, the guarantee, the decree, c07 both sides, c08 the
# LawWorld request, c09-c10 the verdict.
# Facts (para): KSFC term loans Rs.60,00,000 (20.07.1988) and Rs.13,50,000 (29.11.1989) to a company for a medium scale granite
# processing industry (4); deeds of guarantee 16.01.1989 and 17.12.1989, unconditional and irrevocable, liability continuing, joint and
# several (3); KSFC's recovery claim Rs.2,40,64,651 as on 10.03.2000 + 16.5% p.a. quarterly rests, ss.31(1)(aa) and 32 SFC Act (2);
# Commercial Court decree 06.07.2026 in Com. Misc. P. 12/2020: all respondents incl. the appellant (a legal heir) jointly and severally
# liable for Rs.40,82,49,500.80 + costs + 16.5% future interest compounded quarterly (1, 5); appellant: heirs liable only to the
# extent of the inherited estate (6); KSFC "does not dispute this legal position" but says the heirs have not furnished details of the
# inherited properties (7); point (8); held: no personal liability merely as heirs, unless separately assumed (9); "The death of the
# guarantor does not extinguish guarantor's existing liability", the heirs take the estate subject to it, liability limited to the
# inherited estate (10, Ram Kishun (2012) 11 SCC 511; SBI v. Jayanthi AIR 2011 Mad 179 at 9); "The heirs' personal income and
# independently acquired assets should not be made liable merely by reason of inheritance" (12); ORDER: decree modified, liable only to
# the extent of the estate/properties inherited, not jointly and severally for the entire Rs.40,82,49,500.80; heirs to disclose the
# inherited properties to the Executing Court (13); appeal disposed of (14).
# Names: only the cause title on the cite card; the company and the guarantor are never named. List lines <= 52 chars.
# Bench photos: brand/judges/dk_singh.jpg and h_shanthi_bhushan.jpg (official KHC judge-profile portraits dksj.jpeg / gsbj.jpg,
# byte-identical to judiciary.karnataka.gov.in/common_folder/judge_profile/, checked 04-11-2026).
FORMAT = "hook"   # build_course_plan.py: no opening sting, 15-frame lead (the cover), name tag on the "Ravishankar" clip

def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
ENDCARD = {"title": "Late guarantor's debt: must the heirs pay it all?", "line": "No: liable only up to the estate they inherited, not jointly and severally for the whole decree", "sub": "LawWorld: legal research for advocates"}

# ── 1 · must the heirs pay it all? (hook, curiosity, intro) ──────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "father"), text="Father stood guarantor, then died. Must you pay the entire debt from your own pocket?", hl="from your own pocket?")
cue(type="list", t0=S("c02"), t1=A("c02", "karnataka") - 0.05, head="One loan, one decree", head_at=S("c02") + 0.05,
    items=[{"n": 1, "text": "Loans: ₹73.5 lakh, in 1988 and 1989", "at": A("c02", "loans")},
           {"n": 2, "text": "Decree: over ₹40 crore, with interest", "at": A("c02", "decree")},
           {"n": 3, "text": "Against the guarantor's heirs too", "at": A("c02", "heirs")}])
cue(type="point", t0=A("c02", "karnataka") - 0.05, t1=E("c02") + 0.05, text="Karnataka High Court: must the heirs pay it all?", icon="search", accent=True, at=A("c02", "karnataka"))
cue(type="bench", t0=S("c03"), t1=E("c03") + 0.05, tag="Karnataka High Court · 28 October 2026",
    judges=[{"name": "Justice D.K. Singh", "photo": "../brand/judges/dk_singh.jpg", "at": A("c03", "honourable")},
            {"name": "Justice H. Shanthi Bhushan", "photo": "../brand/judges/h_shanthi_bhushan.jpg", "at": A("c03", "honourable", 2)}])

# ── 2 · the guarantee ────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=S("c04"), t1=E("c04") + 0.05, at=A("c04", "karnataka"), tag="HIGH COURT OF KARNATAKA · 28.10.2026",
    cases=[{"name": "Sridhara Babu v. Karnataka State Financial Corporation", "cite": "2026:KHC:59867-DB · COMAP No. 446 of 2026"}])
cue(type="timeline", t0=S("c04"), t1=E("c04") + 0.05,
    nodes=[{"label": "TERM LOAN", "value": "₹60 lakh", "sub": "sanctioned 20 July 1988", "at": A("c04", "eight")},
           {"label": "TERM LOAN", "value": "₹13.5 lakh", "sub": "29 November 1989 · granite unit", "at": A("c04", "lent")}])
cue(type="list", t0=S("c05"), t1=E("c05") + 0.05, head="Deeds of guarantee · 1989", head_at=S("c05") + 0.05,
    items=[{"n": 1, "text": "Unconditional and irrevocable", "at": A("c05", "unconditional")},
           {"n": 2, "text": "Liability continuing, joint and several", "at": A("c05", "joint")},
           {"n": 3, "text": "The guarantor has since died", "at": A("c05", "passed")}])

# ── 3 · forty crore on the heirs ─────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c06"), t1=E("c06") + 0.05, head="Commercial Court · 6 July 2026", head_at=S("c06") + 0.05,
    steps=[{"label": "Petition allowed", "sub": "Com. Misc. P. 12/2020 · with costs", "icon": "landmark", "at": A("c06", "commercial")},
           {"label": "All respondents liable", "sub": "the guarantor's heirs included", "icon": "user", "at": A("c06", "respondents")},
           {"label": "₹40.82 crore decree", "sub": "jointly and severally · + 16.5% interest", "icon": "file-text", "tone": "red", "at": A("c06", "jointly")}])
cue(type="compare", t0=S("c07"), t1=E("c07") + 0.05, head="The appeal · one question", head_at=S("c07") + 0.05,
    cols=[{"title": "The heir", "icon": "user", "at": A("c07", "heir")}, {"title": "KSFC", "icon": "landmark", "at": A("c07", "corporation")}],
    rows=[{"cells": ["Heirs liable only up to the inherited estate", "Does not dispute that legal position"], "cells_at": [A("c07", "liable"), A("c07", "dispute")]},
          {"cells": ["Not jointly and severally for the decree", "But no details of the inherited property"], "cells_at": [A("c07", "estate"), A("c07", "disclosed")]}])

# ── 4 · before the verdict: the LawWorld request ─────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c08"), t1=A("c08", "follow") - 0.05, text="The verdict is next. First, a quick request…", icon="scale", accent=True, at=A("c08", "decided"))
cue(type="list", t0=A("c08", "follow") - 0.05, t1=E("c08") + 0.05, head="Follow LawWorld · lawworld.ai", head_at=A("c08", "follow"),
    items=[{"n": 1, "text": "Search SC and High Court judgments, cited to source", "at": A("c08", "india's")},
           {"n": 2, "text": "Draft petitions, plaints and notices with AI", "at": A("c08", "platform")},
           {"n": 3, "text": "Sign up free · ₹200 AI credit included", "at": A("c08", "advocates")}])

# ── 5 · what the Court held ──────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "guarantor's") - 0.05, text="What did the High Court decide?", icon="scale", accent=True, at=A("c09", "finally"))
cue(type="point", t0=A("c09", "guarantor's") - 0.05, t1=E("c09") + 0.05, text="“The death of the guarantor does not extinguish guarantor's existing liability.”", icon="quote", accent=True, at=A("c09", "death"))
cue(type="point", t0=S("c10"), t1=A("c10", "decree") - 0.05, text="“The heirs' personal income and independently acquired assets should not be made liable merely by reason of inheritance.”", icon="quote", accent=True, at=A("c10", "own"))
cue(type="verdicts", t0=A("c10", "decree") - 0.05, t1=E("c10") + 0.05,
    rows=[{"text": "Heirs jointly and severally liable for all ₹40.82 crore", "ok": False, "at": A("c10", "modified")},
          {"text": "Liable only up to the estate they inherited", "ok": True, "at": A("c10", "answer")},
          {"text": "Disclose the inherited property to the Executing Court", "ok": True, "at": A("c10", "disclose")}])

MUSIC = {"file": "audio/bed_mixkit738_140s.mp3", "target_lufs": -21}   # owner 02-11-2026: trending-style royalty-free bed, audible under the voice
