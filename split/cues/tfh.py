# Naveen v. State of Karnataka by Aldur PS, Crl.P. No. 13177 of 2026, 2026:KHC:60797, High Court of Karnataka at Bengaluru
# (S. Vishwajith Shetty J.; reserved 28.10.2026, CAV order 02.11.2026; "R" on page 1 and on the court's Reportable list):
# panel cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND).
# HOOK format (split/JUDGMENT_HOOK_FORMAT.md): c01 hook question (spoken to everyone, no "Advocates,"), c02 curiosity, c03 "Hi, I'm
# Ravishankar" + bench, c04-c05 the timeline, c06-c07 both sides, c08 the LawWorld request, c09-c10 the verdict.
# Facts (para): FIR 12.10.2025 against him and his parents after his wife's death, BNS and s.4 Dowry Prohibition Act (1, 3, 6);
# surrendered 14.10.2025 ~11.00 a.m.; arrest shown 9.45 p.m.; produced 15.10.2025 5.45 p.m. (6, 27); counsel: custody from
# 11 a.m., Articles 21 and 22(2) (4); SPP: came voluntarily, did not cooperate, presence in the station is not arrest (5);
# held: "Detention for the purpose of interrogation is unknown to law"; "Arrest commences with the restraint placed on the liberty
# of the accused and not with the time of arrest recorded by the police officer"; 24 hours run from when liberty was curtailed
# (27); not produced within 24 hours of detention -> detention illegal, arrest vitiated (28); bail, Rs. 1,00,000 bond with two
# sureties and conditions (29). Names: only the cause title on the cite card; no accusation in speech (offences on the card only).
# List lines <= 52 chars. Bench photo: brand/judges/s_vishwajith_shetty.jpg (official KHC judge-profile portrait, SVSJ.jpeg).
FORMAT = "hook"   # build_course_plan.py: no opening sting, 15-frame lead (the cover), name tag on the "Ravishankar" clip

def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
ENDCARD = {"title": "When does the 24-hour clock start?", "line": "From the moment liberty is actually curtailed, not from the arrest time the police record", "sub": "LawWorld: legal research for advocates"}

# ── 1 · when does the clock start? (hook, curiosity, intro) ──────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "walk"), text="Walked in at 11 AM, arrest recorded at night. When does the 24-hour clock start?", hl="When does the 24-hour clock start?")
cue(type="list", t0=S("c02"), t1=A("c02", "so") - 0.05, head="Article 22(2) · the 24-hour rule", head_at=S("c02") + 0.05,
    items=[{"n": 1, "text": "Arrested person: before a Magistrate in 24 hours", "at": A("c02", "arrested")},
           {"n": 2, "text": "This man: produced the next evening", "at": A("c02", "reached")},
           {"n": 3, "text": "Counted from when?", "at": A("c02", "evening")}])
cue(type="point", t0=A("c02", "so") - 0.05, t1=E("c02") + 0.05, text="Late or not?", icon="search", accent=True, at=A("c02", "late"))
cue(type="bench", t0=S("c03"), t1=E("c03") + 0.05, tag="Karnataka High Court · 2 November 2026",
    judges=[{"name": "Justice S. Vishwajith Shetty", "photo": "../brand/judges/s_vishwajith_shetty.jpg", "at": A("c03", "honourable")}])

# ── 2 · eleven in the morning ────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=S("c04"), t1=E("c04") + 0.05, at=A("c04", "after"), tag="HIGH COURT OF KARNATAKA · 02.11.2026",
    cases=[{"name": "Naveen v. State of Karnataka", "cite": "2026:KHC:60797 · Crl.P. No. 13177 of 2026"}])
cue(type="timeline", t0=S("c04"), t1=E("c04") + 0.05,
    nodes=[{"label": "CASE REGISTERED", "value": "12 Oct 2025", "sub": "against him and his parents", "at": A("c04", "registered")},
           {"label": "HE SURRENDERS", "value": "11:00 AM", "sub": "14 Oct 2025, on his own", "at": A("c04", "surrendered")}])
cue(type="timeline", t0=S("c05"), t1=E("c05") + 0.05,
    nodes=[{"label": "ARREST RECORDED", "value": "9:45 PM", "sub": "the same day", "at": A("c05", "nine")},
           {"label": "BEFORE THE MAGISTRATE", "value": "5:45 PM", "sub": "the next day, 15 Oct 2025", "at": A("c05", "produced")}])

# ── 3 · when was he arrested? ────────────────────────────────────────────────────────────────────────────────────────
cue(type="compare", t0=S("c06"), t1=E("c07") + 0.05, head="Arrested at 11 AM, or at 9:45 PM?", head_at=S("c06") + 0.05,
    cols=[{"title": "His counsel", "icon": "scale", "at": A("c06", "counsel")}, {"title": "The State", "icon": "landmark", "at": A("c07", "state")}],
    rows=[{"cells": ["In police custody from 11 AM", "Came on his own, did not cooperate"], "cells_at": [A("c06", "custody"), A("c07", "cooperate")]},
          {"cells": ["24 hours crossed: Articles 21 and 22", "Sitting in a police station is not arrest"], "cells_at": [A("c06", "breaching"), A("c07", "merely")]}])

# ── 4 · before the verdict: the LawWorld request ─────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c08"), t1=A("c08", "follow") - 0.05, text="The verdict is next. First, a quick request…", icon="scale", accent=True, at=A("c08", "decided"))
cue(type="list", t0=A("c08", "follow") - 0.05, t1=E("c08") + 0.05, head="Follow LawWorld · lawworld.ai", head_at=A("c08", "follow"),
    items=[{"n": 1, "text": "Search SC and High Court judgments, cited to source", "at": A("c08", "india's")},
           {"n": 2, "text": "Draft petitions, plaints and notices with AI", "at": A("c08", "platform")},
           {"n": 3, "text": "Sign up free · ₹200 AI credit included", "at": A("c08", "advocates")}])

# ── 5 · what the Court held ──────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "twenty") - 0.05, text="What did the High Court decide?", icon="scale", accent=True, at=A("c09", "finally"))
cue(type="point", t0=A("c09", "twenty") - 0.05, t1=E("c09") + 0.05, text="“Arrest commences with the restraint placed on the liberty of the accused and not with the time of arrest recorded by the police officer.”", icon="quote", accent=True, at=A("c09", "twenty"))
cue(type="point", t0=S("c10"), t1=A("c10", "so") - 0.05, text="“Detention for the purpose of interrogation is unknown to law.”", icon="quote", accent=True, at=A("c10", "detention"))
cue(type="verdicts", t0=A("c10", "so") - 0.05, t1=E("c10") + 0.05,
    rows=[{"text": "State's plea: no arrest till 9:45 PM", "ok": False, "at": A("c10", "so")},
          {"text": "Not produced in 24 hours: arrest vitiated", "ok": True, "at": A("c10", "vitiated")},
          {"text": "Bail granted: ₹1 lakh bond, two sureties", "ok": True, "at": A("c10", "bail")}])

MUSIC = {"file": "audio/bed_mixkit738_140s.mp3", "target_lufs": -21}   # owner 02-11-2026: trending-style royalty-free bed, audible under the voice
