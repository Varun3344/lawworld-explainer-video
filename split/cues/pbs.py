FORMAT = "hook"   # build_course_plan.py: no opening sting, 15-frame lead (the cover), name tag on the "Ravishankar" clip
# The Bihar Public Service Commission & Anr. v. Dr. Sushma Sharan & Ors., L.P.A. No. 472 of 2023 in CWJC No. 18940 of 2019, Patna High
# Court (Mohit Kumar Shah J. wrote it, Sourendra Pandey J.; CAV judgment 30.10.2026, AFR): panel cues, run by split/build_course_plan.py
# (helpers: at S E cue fx have r3 PEND). HOOK format (split/JUDGMENT_HOOK_FORMAT.md): c01 hook question, c02 curiosity, c03 "Hi, I'm
# Ravishankar" + bench, c04-c07 the recruitment / the general list / the appeal, c08 the LawWorld request, c09-c10 the verdict.
# Facts from the judgment (paras; source: the Indian Kanoon render, doc 102140170 - the court's PDF is captcha-gated): Single Judge,
# 14.02.2023: consider her under SC on merit, if otherwise suitable (1); Advt. 20/2017: 74 Assistant Professors in Medical Colleges and
# Hospitals, 13 SC, 5 of them for women; she applied under SC with the SDO's certificate No. 1598 of 02.08.2006; interview 28.02.2018,
# then the original documents incl. the caste certificate verified; result 08.08.2019 without her in the SC list (2, 12); her plea: SC by
# her father (Circle Officer, Patna Sadar certificate of 17.08.2019), her husband SC too (3, 13); BPSC: failed on merit in the unreserved
# list; not considered as reserved as the certificate bore her husband's name, not her father's; minutes of 08.08.2019: one chance by
# notices of 16.07.2018 and 21.07.2018 (4, 14); BPSC in appeal: advertisement and interview letter required a Circle Officer's
# certificate; the 2019 certificate first produced in the writ; 29 marks against the unreserved cut-off of 37.50 (7, 8); Vandana
# Govindam: the advertisement's terms bind (9); her counsel: no father's-name stipulation in the advertisement; the SDO outranks the
# Circle Officer and was competent in 2006 (10); held: "our answer is in negative" - no such condition in the advertisement (16); Braj
# Kishore Prasad (FB) 26(d): writ relief in deserving cases, "exactly what has been done by the writ court" (17, 18); a certificate only
# affirms an existing fact; not denied that she is SC; Articles 15(4), 16(4); not to be rejected "merely on the ground of non-existent
# technicalities/reasons"; undisputed that the SDO is higher in rank to the Circle Officer; the 17.08.2019 certificate annexed to the
# writ (19); no infirmity, appeal dismissed (20). The candidate is never named in speech; no allegation against her on any card.
# No section sign anywhere. List lines <= 52 chars. Official patnahighcourt.gov.in portraits on the bench card.

def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
ENDCARD = {"title": "Husband's name on the caste certificate: a ground to reject?", "line": "No: the advertisement never asked for the father's name, and her caste was not disputed · the BPSC's appeal dismissed", "sub": "LawWorld: legal research for advocates"}

# ── 1 · husband's name, not father's? (hook, curiosity, intro) ──────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "scheduled"), text="Can a Scheduled Caste candidate be moved to the general list because her caste certificate names her husband, not her father?", hl="names her husband, not her father?")
cue(type="list", t0=S("c02"), t1=A("c02", "so") - 0.05, head="The Commission's objections", head_at=S("c02") + 0.05,
    items=[{"n": 1, "text": "Husband's name, not father's, on the certificate", "at": A("c02", "commission")},
           {"n": 2, "text": "It wanted a Circle Officer's certificate", "at": A("c02", "circle")},
           {"n": 3, "text": "Hers: a Sub-divisional Officer's, higher in rank", "at": A("c02", "hers")}])
cue(type="point", t0=A("c02", "so") - 0.05, t1=E("c02") + 0.05, text="So is she out of the reserved category?", icon="search", accent=True, at=A("c02", "so"))
cue(type="bench", t0=S("c03"), t1=E("c03") + 0.05, tag="Patna High Court · 30 October 2026",
    judges=[{"name": "Justice Mohit Kumar Shah", "photo": "../brand/judges/mohit_kumar_shah.jpg", "at": A("c03", "honourable")},
            {"name": "Justice Sourendra Pandey", "photo": "../brand/judges/sourendra_pandey.jpg", "at": A("c03", "honourable", 2)}])

# ── 2 · the recruitment ─────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="counters", t0=S("c04"), t1=E("c04") + 0.05, head="BPSC Advertisement No. 20/2017", head_at=S("c04") + 0.05,
    items=[{"value": 74, "unit": "POSTS", "label": "Assistant Professors", "sub": "medical colleges and hospitals", "at": A("c04", "seventy")},
           {"value": 13, "unit": "POSTS", "label": "Scheduled Caste", "sub": "reserved", "at": A("c04", "thirteen")},
           {"value": 5, "unit": "POSTS", "label": "SC women", "sub": "out of those 13", "at": A("c04", "scheduled")}])
cue(type="cite", t0=S("c05"), t1=E("c05") + 0.05, at=A("c05", "candidate"), tag="HIGH COURT OF PATNA · 30.10.2026",
    cases=[{"name": "The Bihar Public Service Commission & Anr. v. Dr. Sushma Sharan & Ors.", "cite": "L.P.A. No. 472 of 2023 in CWJC No. 18940 of 2019 · AFR"}])
cue(type="timeline", t0=S("c05"), t1=E("c05") + 0.05,
    nodes=[{"label": "SC CATEGORY", "value": "she applies", "sub": "SDO's caste certificate of 2 August 2006", "at": A("c05", "applied")},
           {"label": "INTERVIEW", "value": "28 February 2018", "sub": "then her original documents verified", "at": A("c05", "interviewed")}])

# ── 3 · the general list ────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c06"), t1=E("c06") + 0.05, head="The Commission's case", head_at=S("c06") + 0.05,
    steps=[{"label": "Husband's name", "sub": "not father's · the 2006 certificate", "icon": "file-text", "at": A("c06", "husband")},
           {"label": "Moved to the general list", "sub": "29 marks, cut-off 37.50, it says", "icon": "x", "at": A("c06", "general")},
           {"label": "One chance given, it says", "sub": "notices of 16 and 21 July 2018", "icon": "info", "at": A("c06", "chance")}])
cue(type="point", t0=S("c07"), t1=A("c07", "commission") - 0.05, text="Single Judge, 14 February 2023: consider her in the Scheduled Caste category, on her merit, if otherwise suitable", icon="landmark", accent=True, at=A("c07", "single"))
cue(type="list", t0=A("c07", "commission") - 0.05, t1=E("c07") + 0.05, head="The Commission's appeal", head_at=A("c07", "commission"),
    items=[{"n": 1, "text": "Advertisement: a Circle Officer's certificate", "at": A("c07", "appealed")},
           {"n": 2, "text": "Circle Officer's 2019 certificate: too late", "at": A("c07", "terms")},
           {"n": 3, "text": "Vandana Govindam: the advertisement's terms bind", "at": A("c07", "candidates")}])

# ── 4 · before the verdict: the LawWorld request ────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c08"), t1=A("c08", "follow") - 0.05, text="The verdict is next. First, a quick request…", icon="scale", accent=True, at=A("c08", "decided"))
cue(type="list", t0=A("c08", "follow") - 0.05, t1=E("c08") + 0.05, head="Follow LawWorld · lawworld.ai", head_at=A("c08", "follow"),
    items=[{"n": 1, "text": "Search SC and High Court judgments, cited to source", "at": A("c08", "india's")},
           {"n": 2, "text": "Draft petitions, plaints and notices with AI", "at": A("c08", "platform")},
           {"n": 3, "text": "Sign up free · ₹200 AI credit included", "at": A("c08", "advocates")}])

# ── 5 · what the Court held ─────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "nothing") - 0.05, text="What did the High Court decide?", icon="scale", accent=True, at=A("c09", "finally"))
cue(type="notequal", t0=A("c09", "nothing") - 0.05, t1=E("c09") + 0.05, left="Husband's name, not father's", right="a ground for the general list",
    at=A("c09", "nothing"), left_at=A("c09", "nothing"), sub="Advertisement No. 20/2017 prescribes no such condition", sub_at=A("c09", "ground"))
cue(type="point", t0=S("c10"), t1=A("c10", "such") - 0.05, text="The SDO who issued her 2006 certificate ranks above a Circle Officer (not disputed) · she also produced a Circle Officer's certificate of 17.08.2019", icon="scale", accent=True, at=A("c10", "ranks"))
cue(type="verdicts", t0=A("c10", "such") - 0.05, t1=E("c10") + 0.05,
    rows=[{"text": "Rejection on “non-existent technicalities/reasons”", "ok": False, "at": A("c10", "technicalities")},
          {"text": "The Single Judge's judgment: no infirmity found", "ok": True, "at": A("c10", "candidature")},
          {"text": "Direction to consider her as SC, on merit: upheld", "ok": True, "at": A("c10", "failed")}])

MUSIC = {"file": "audio/bed_mixkit738_140s.mp3", "target_lufs": -21}   # owner 02-11-2026: trending-style royalty-free bed, audible under the voice
