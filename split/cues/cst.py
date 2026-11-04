# CESCOM v. J.K. Tyre and Industries Ltd. & Anr., W.A. No. 439 of 2025 (GM-KEB), High Court of Karnataka at Bengaluru
# (Vibhu Bakhru C.J. and K.S. Hemalekha J.; reserved 15.09.2026, C.A.V. judgment 29.10.2026; circled "R" on page 1 and on the court's
# Reportable list): panel cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND).
# HOOK format (split/JUDGMENT_HOOK_FORMAT.md): c01 hook question (spoken to everyone, no "Advocates,"), c02 curiosity, c03 "Hi, I'm
# Ravishankar" + bench, c04-c05 the lockdown bill, c06-c07 the single judge and the appeal, c08 the LawWorld request, c09-c10 the verdict.
# Facts (para): single judge's order 18.12.2024 in W.P. 9969/2021 (1); retain only 3.1% / 5.1% of April 2020 demand charges of
# Rs.16,95,750 / Rs.18,74,250, refund or adjust the rest (3); three tyre plants at Mysuru, two HT connections (4); lockdown
# 24.03.2020-03.05.2020 (6); G.O. 08.05.2020: MSMEs exempted from demand / fixed charges for April-May 2020, non-MSMEs could defer
# payment to 30.06.2020 (7); JKTIL is non-MSME (8); waiver refused 05.10.2020, only deferment (9); April use 3.1% / 5.1% of the
# preceding months' average (11); single judge: lockdown = force majeure within Clause 3, proportionate reduction (12); CESCOM's
# grounds: Consumer Grievance Redressal Forum (s.42(5)-(7) r/w s.181 Electricity Act 2003), demand charges are not minimum charges
# (13); held: Clause 3 applies only on an impediment to receiving power (war, mutiny, riot, strike, earthquake, hurricane, tempest ...);
# JKTIL received and used electricity in April 2020 (26); no notice under Clause 3 (23, 26, 29); no waiver for non-MSME units, only
# more time to pay, which JKTIL got (31); appeal allowed, impugned order set aside (32).
# Names: none spoken; the companies appear only on the cite card. List lines <= 52 chars.
# Bench photos: brand/judges/vibhu_bakhru.jpg, brand/judges/ks_hemalekha.jpg (official KHC portraits, used for kmv/lgc).
FORMAT = "hook"   # build_course_plan.py: no opening sting, 15-frame lead (the cover), name tag on the "Ravishankar" clip

def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
ENDCARD = {"title": "Lockdown: must the demand charges still be paid?", "line": "Here, yes: power was received and used, and no Clause 3 notice was given, so the reduction was set aside", "sub": "LawWorld: legal research for advocates"}

# ── 1 · lockdown: still pay? (hook, curiosity, intro) ────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "lockdown"), text="Lockdown cut a factory's power use to a fraction. Must it still pay the demand charges?", hl="Must it still pay the demand charges?")
cue(type="list", t0=S("c02"), t1=A("c02", "so") - 0.05, head="April 2020 · the demand charges", head_at=S("c02") + 0.05,
    items=[{"n": 1, "text": "A single judge: cut to match the power used", "at": A("c02", "single")},
           {"n": 2, "text": "The electricity company appealed", "at": A("c02", "electricity")}])
cue(type="point", t0=A("c02", "so") - 0.05, t1=E("c02") + 0.05, text="So who was right?", icon="scale", accent=True, at=A("c02", "so"))
cue(type="bench", t0=S("c03"), t1=E("c03") + 0.05, tag="Karnataka High Court · 29 October 2026",
    judges=[{"name": "Chief Justice Vibhu Bakhru", "photo": "../brand/judges/vibhu_bakhru.jpg", "at": A("c03", "honourable")},
            {"name": "Justice K.S. Hemalekha", "photo": "../brand/judges/ks_hemalekha.jpg", "at": A("c03", "honourable", 2)}])

# ── 2 · the lockdown bill ────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=S("c04"), t1=E("c04") + 0.05, at=A("c04", "tyre"), tag="HIGH COURT OF KARNATAKA · 29.10.2026",
    cases=[{"name": "CESCOM v. J.K. Tyre and Industries Ltd.", "cite": "W.A. No. 439 of 2025 (GM-KEB)"}])
cue(type="timeline", t0=S("c04"), t1=E("c04") + 0.05,
    nodes=[{"label": "LOCKDOWN BEGINS", "value": "24 Mar 2020", "sub": "nationwide", "at": A("c04", "lockdown")},
           {"label": "LOCKDOWN ENDS", "value": "3 May 2020", "sub": "eased from 4 May", "at": A("c04", "third")}])
cue(type="list", t0=S("c05"), t1=A("c05", "state") - 0.05, head="April 2020 · use against normal", head_at=S("c05") + 0.05,
    items=[{"n": 1, "text": "HT-57: 3.1% of its average use", "at": A("c05", "three")},
           {"n": 2, "text": "HT-138: 5.1% of its average use", "at": A("c05", "five")}])
cue(type="list", t0=A("c05", "state") - 0.05, t1=E("c05") + 0.05, head="State relief · G.O. of 8 May 2020", head_at=A("c05", "state"),
    items=[{"n": 1, "text": "MSME units: demand charges waived, April-May", "at": A("c05", "exempted")},
           {"n": 2, "text": "Non-MSME units, like this one: pay later", "at": A("c05", "others")}])

# ── 3 · demand or minimum charge? ────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c06"), t1=A("c06", "but") - 0.05, text="Waiver refused, 5 Oct 2020: only deferment for non-MSME units", icon="x", at=A("c06", "request"))
cue(type="list", t0=A("c06", "but") - 0.05, t1=E("c06") + 0.05, head="The single judge · W.P. No. 9969 of 2021", head_at=A("c06", "but"),
    items=[{"n": 1, "text": "The lockdown: force majeure under Clause 3", "at": A("c06", "force")},
           {"n": 2, "text": "Keep only 3.1% and 5.1% of April's demand charges", "at": A("c06", "cut")},
           {"n": 3, "text": "Refund or adjust the rest against future bills", "at": A("c06", "proportion")}])
cue(type="list", t0=S("c07"), t1=E("c07") + 0.05, head="CESCOM's appeal · two grounds", head_at=S("c07") + 0.05,
    items=[{"n": 1, "text": "Demand charges are not minimum charges", "at": A("c07", "demand")},
           {"n": 2, "text": "A billing dispute: for the Grievance Forum", "at": A("c07", "billing")},
           {"n": 3, "text": "Electricity Act 2003, Section 42(5) to (7)", "at": A("c07", "consumer")}])

# ── 4 · before the verdict: the LawWorld request ─────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c08"), t1=A("c08", "follow") - 0.05, text="The verdict is next. First, a quick request…", icon="scale", accent=True, at=A("c08", "decided"))
cue(type="list", t0=A("c08", "follow") - 0.05, t1=E("c08") + 0.05, head="Follow LawWorld · lawworld.ai", head_at=A("c08", "follow"),
    items=[{"n": 1, "text": "Search SC and High Court judgments, cited to source", "at": A("c08", "india's")},
           {"n": 2, "text": "Draft petitions, plaints and notices with AI", "at": A("c08", "platform")},
           {"n": 3, "text": "Sign up free · ₹200 AI credit included", "at": A("c08", "advocates")}])

# ── 5 · what the Court held ──────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "force") - 0.05, text="What did the High Court decide?", icon="scale", accent=True, at=A("c09", "finally"))
cue(type="point", t0=A("c09", "force") - 0.05, t1=E("c09") + 0.05, text="Clause 3: only if receiving power is prevented, by war, riot, strike or the like", icon="file-text", accent=True, at=A("c09", "force"))
cue(type="list", t0=S("c10"), t1=A("c10", "so") - 0.05, head="On these facts", head_at=S("c10") + 0.05,
    items=[{"n": 1, "text": "Power was received and used in April 2020", "at": A("c10", "receive")},
           {"n": 2, "text": "No notice was given under Clause 3", "at": A("c10", "notice")}])
cue(type="verdicts", t0=A("c10", "so") - 0.05, t1=E("c10") + 0.05,
    rows=[{"text": "CESCOM's appeal: allowed", "ok": True, "at": A("c10", "allowed")},
          {"text": "Single judge's order: set aside", "ok": False, "at": A("c10", "aside")}])

MUSIC = {"file": "audio/bed_mixkit738_140s.mp3", "target_lufs": -21}   # owner 02-11-2026: trending-style royalty-free bed, audible under the voice
