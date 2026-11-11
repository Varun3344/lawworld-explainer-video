# Matin Shankarrao Bhosale & Anr. v. State of Maharashtra & Anr., 2026 INSC 1198, Criminal Appeal No. 5171 of 2026 (from SLP (Crl.)
# No. 13889 of 2026), Supreme Court of India (ORDER by J.B. Pardiwala J., with Manmohan J.; New Delhi, 02.11.2026; REPORTABLE): panel
# cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND). DRAFT 11-11-2026, awaiting the owner's yes.
# HOOK format (split/JUDGMENT_HOOK_FORMAT.md): c01 hook question (spoken to everyone, no "Advocates,"), c02 curiosity (the High Court
# found a breach of duty and refused to quash; is a breach of duty, by itself, enough? paras 15, 39, 41 - FACT-CHECK 11-11: the para 61
# "painful ... the law remains the law" quote was dropped from c02, it gave the verdict's direction away), c03 "Hi, I'm Ravishankar" +
# bench, c04-c05 the school, the pillar and the charge sheet, c06 the High Court, c07 both sides, c08 the LawWorld request, c09-c10 the
# verdict.
# Facts (para): appellants = President and Superintendent of the school (9, 26); FIR by the father 19.02.2020, Mangrul Chawala PS,
# District Amravati (4, 6); [not used: hostel, other girls injured = FIR (7) / HC (15) only]; 7th standard, Adivasi Ashram Shala, 12 years (8); "some
# construction of a pillar was going on which unfortunately collapsed" (11); charge-sheet s.304 r/w 34 IPC, culpable homicide not
# amounting to murder (3, 12); HC order 25.02.2026, Crl. Application No. 239 of 2021: cement ratio not maintained (CA report), no solid
# base of cement and iron (spot panchanama), breach of duty, application rejected (2, 15). Appellants: causa causans, not causa sine qua
# non; "one of the causes" is not enough (18, 20). State: prima facie case only; "at least" s.304A, let the trial court decide (22, 23).
# Held: s.304 not attracted, no knowledge that inferior construction "in all probability was likely to cause death" (39); the test (41);
# Sushil Ansal, (2014) 6 SCC 173: causa causans = "The immediate cause; the last link in the chain of causation" (42); Kurban Hussein,
# AIR 1965 SC 1616 (Omkar Rampratap): "It must be the causa causans; it is not enough that it may have been the causa sine qua non" (43);
# "It was the contractor and his team who were actually undertaking the construction" (44); Ambalal D. Bhatt, (1972) 3 SCC 525: breaking
# rules does not by itself make the act the proximate and efficient cause (56); not to face trial under s.304A or s.304 (59); para 60
# quoted on the c10 card; proceedings from Chargesheet No. 15 of 2020 quashed "so far as appellants are concerned" (62); "The trial may
# proceed further against any other co-accused" (63).
# SENSITIVE: a child died. No name of the child, her family, the appellants or the school anywhere except the cause title on the cite
# card; no graphic word on any card. The contractor's prima facie remark (59) is NOT on a card (speech says only that his team did the
# construction, para 44). List lines <= 52 chars. Bench photos: brand/judges/jb_pardiwala.jpg, brand/judges/manmohan.jpg (official).
FORMAT = "hook"   # build_course_plan.py: no opening sting, 15-frame lead (the cover), name tag on the "Ravishankar" clip

def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
ENDCARD = {"title": "Negligent, but the immediate cause?", "line": "Section 304A needs the causa causans, not a causa sine qua non: here, an intervening cause broke the chain", "sub": "LawWorld: legal research for advocates"}

# ── 1 · who is criminally liable? (hook, curiosity, intro) ───────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "pillar"), text="A pillar under construction fell at her school. Should its President and Superintendent face a criminal trial?", hl="face a criminal trial?")
cue(type="point", t0=S("c02"), t1=A("c02", "but") - 0.05, text="High Court, 25 February 2026: breach of duty found, the plea to quash rejected", icon="landmark", accent=True, at=A("c02", "found"))
cue(type="point", t0=A("c02", "but") - 0.05, t1=E("c02") + 0.05, text="Is a breach of duty, by itself, enough for a criminal trial?", icon="search", accent=True, at=A("c02", "but"))
cue(type="bench", t0=S("c03"), t1=E("c03") + 0.05, tag="Supreme Court of India · 2 November 2026",
    judges=[{"name": "Justice J.B. Pardiwala", "photo": "../brand/judges/jb_pardiwala.jpg", "at": A("c03", "honourable")},
            {"name": "Justice Manmohan", "photo": "../brand/judges/manmohan.jpg", "at": A("c03", "honourable", 2)}])

# ── 2 · a pillar under construction ──────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=S("c04"), t1=E("c04") + 0.05, at=A("c04", "studied"), tag="SUPREME COURT OF INDIA · 02.11.2026",
    cases=[{"name": "Matin Shankarrao Bhosale & Anr. v. State of Maharashtra & Anr.", "cite": "2026 INSC 1198 · Criminal Appeal No. 5171 of 2026"}])
cue(type="timeline", t0=S("c04"), t1=E("c04") + 0.05,
    nodes=[{"label": "7TH STANDARD", "value": "Ashram school", "sub": "12 years old · Amravati district", "at": A("c04", "seventh")},
           {"label": "A PILLAR BEING BUILT", "value": "collapsed", "sub": "on the school premises", "at": A("c04", "pillar")}])
cue(type="timeline", t0=S("c05"), t1=E("c05") + 0.05,
    nodes=[{"label": "FIR BY HER FATHER", "value": "19 Feb 2020", "sub": "Mangrul Chawala police station", "at": A("c05", "father")},
           {"label": "CHARGE SHEET", "value": "Section 304 IPC", "sub": "read with 34 · President and Superintendent", "at": A("c05", "charge")}])

# ── 3 · the immediate cause? ─────────────────────────────────────────────────────────────────────────────────────────
cue(type="list", t0=S("c06"), t1=E("c06") + 0.05, head="High Court · 25 February 2026", head_at=S("c06") + 0.05,
    items=[{"n": 1, "text": "Cement ratio not maintained (CA report)", "at": A("c06", "cement")},
           {"n": 2, "text": "No solid base of cement and iron (panchanama)", "at": A("c06", "solid")},
           {"n": 3, "text": "Breach of duty found · quashing plea rejected", "at": A("c06", "breach")}])
cue(type="compare", t0=S("c07"), t1=E("c07") + 0.05, head="Was their act the cause of death?", head_at=S("c07") + 0.05,
    cols=[{"title": "The appellants", "icon": "scale", "at": A("c07", "two")}, {"title": "The State", "icon": "landmark", "at": A("c07", "state")}],
    rows=[{"cells": ["Not the causa causans, the immediate cause", "At least Section 304A IPC is made out"], "cells_at": [A("c07", "immediate"), A("c07", "least")]},
          {"cells": ["One of the causes is not enough", "Let the trial court decide the offence"], "cells_at": [A("c07", "death"), A("c07", "trial")]}])

# ── 4 · before the verdict: the LawWorld request ─────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c08"), t1=A("c08", "follow") - 0.05, text="The verdict is next. First, a quick request…", icon="scale", accent=True, at=A("c08", "decided"))
cue(type="list", t0=A("c08", "follow") - 0.05, t1=E("c08") + 0.05, head="Follow LawWorld · lawworld.ai", head_at=A("c08", "follow"),
    items=[{"n": 1, "text": "Search SC and High Court judgments, cited to source", "at": A("c08", "india's")},
           {"n": 2, "text": "Draft petitions, plaints and notices with AI", "at": A("c08", "platform")},
           {"n": 3, "text": "Sign up free · ₹200 AI credit included", "at": A("c08", "advocates")}])

# ── 5 · what the Court held ──────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "citing") - 0.05, text="What did the Supreme Court decide?", icon="scale", accent=True, at=A("c09", "finally"))
cue(type="list", t0=A("c09", "citing") - 0.05, t1=E("c09") + 0.05, head="Section 304A IPC · the causation test", head_at=A("c09", "citing"),
    items=[{"n": 1, "text": "Kurban Hussein: causa causans, not sine qua non", "at": A("c09", "kurban")},
           {"n": 2, "text": "Sushil Ansal: the immediate cause, the last link", "at": A("c09", "immediate")},
           {"n": 3, "text": "Ambalal Bhatt: breaking a rule does not prove cause", "at": A("c09", "just")}])
cue(type="point", t0=S("c10"), t1=A("c10", "case") - 0.05, text="“…cannot be said to be the causa causans, but there was a cause interveniens, which broke the chain of causation”", icon="quote", accent=True, at=A("c10", "noted"))
cue(type="verdicts", t0=A("c10", "case") - 0.05, t1=E("c10") + 0.05,
    rows=[{"text": "Trial for culpable homicide (Section 304)", "ok": False, "at": A("c10", "case")},
          {"text": "State's fallback: Section 304A, let trial decide", "ok": False, "at": A("c10", "two")},
          {"text": "Proceedings quashed for the two appellants", "ok": True, "at": A("c10", "quashed")},
          {"text": "Trial may go on against any other co-accused", "ok": True, "at": A("c10", "trial")}])

MUSIC = {"file": "audio/bed_mixkit738_140s.mp3", "target_lufs": -21}   # owner 02-11-2026: trending-style royalty-free bed, audible under the voice
