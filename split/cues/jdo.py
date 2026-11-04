# In Re: XXX, a Judicial Officer in the District Judge Cadre of Rajasthan Judicial Services, 2026 INSC 1188 (arising out of SLP (Crl.)
# No. 13501 of 2025) (Sandeep Mehta J. wrote it, Devendra Kumar Upadhyaya J.; decided 02.11.2026, Reportable): panel cues, run by
# split/build_course_plan.py (helpers: at S E cue fx have r3 PEND).
# HOOK format (split/JUDGMENT_HOOK_FORMAT.md): c01 hook question (spoken to everyone, no "Advocates,"), c02 curiosity, c03 "Hi, I'm
# Ravishankar" + bench, c04-c05 the two trials, c06-c07 the High Court's remarks / her explanation, c08 the LawWorld request,
# c09-c10 the verdict.
# Facts from the judgment (paras): officer of the District Judge cadre, name masked (3); "To err is human, to forgive, divine" (4);
# Article 227 (5); FIR 56/2019, PS Malsisar, Jhunjhunu; POCSO (7); the child in conflict with law tried as an adult before the Special
# Judge, POCSO Cases, Jhunjhunu (8); separate trial of the adult co-accused; s.23 JJ Act bars joint proceedings (9); separate judgments
# 20.01.2024 convicting both (10); overlapping extracts "inadvertently incorporated" (11); the High Court, 01.05.2025: suspension of
# sentence rejected; "cut, copy and paste"; "in all probability" scripted by the Stenographer / Clerk and signed without being read;
# "such a Judicial Officer is not entitled to remain in service of Judiciary"; directions 17 (Judicial Academy training) and 18 (a copy
# in her ACR for 2024, after her comments) (13); her explanation: witnesses and evidence almost the same (17); the sole Stenographer
# on leave, part dictated to the LDC; "bona fide typographical errors", according to her (19); recorded on the judicial side
# "without affording an opportunity ... to show cause or to place her explanation on record" - "the vice of non-adherence to the
# principles of natural justice" (16); "To castigate a Judicial Officer for inadvertent typographical errors ... was avoidable" (21);
# Kaushal Singh (22); chilling effect (23); "contrary to the fundamental principle of 'audi alteram partem'" (24); Shuvendu Saha,
# 2026 INSC 367: a remark slip before the administrative Judge or the Chief Justice, for follow-up on the administrative side (25);
# remarks in paras 9, 10, 11 and directions 17, 18 "expunged and set aside" (26); appeal allowed (27).
# Not on any card: the officer's name or anything identifying her; the accused, the victim or the offence details (only "POCSO" as the
# court's name). No section sign anywhere. List lines <= 52 chars. Official sci.gov.in portraits on the bench card.
FORMAT = "hook"   # build_course_plan.py: no opening sting, 15-frame lead (the cover), name tag on the "Ravishankar" clip

def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
ENDCARD = {"title": "Can a judge be condemned unheard?", "line": "No: strictures recorded without a chance to explain break natural justice. The remarks were expunged", "sub": "LawWorld: legal research for advocates"}

# ── 1 · condemned unheard? (hook, curiosity, intro) ─────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "verdict"), text="Typing errors in a verdict. Can a higher court condemn the judge in its order, without a hearing?", hl="without a hearing?")
cue(type="point", t0=S("c02"), t1=A("c02", "so") - 0.05, text="“…such a Judicial Officer is not entitled to remain in service of Judiciary.” · the High Court, 1 May 2025 · a copy to go into her ACR for 2024, after her comments", icon="quote", accent=True, at=A("c02", "wrote"))
cue(type="point", t0=A("c02", "so") - 0.05, t1=E("c02") + 0.05, text="Was that fair?", icon="search", accent=True, at=A("c02", "fair"))
cue(type="bench", t0=S("c03"), t1=E("c03") + 0.05, tag="Supreme Court of India · 2 November 2026",
    judges=[{"name": "Justice Sandeep Mehta", "photo": "../brand/judges/sandeep_mehta.jpg", "at": A("c03", "honourable")},
            {"name": "Justice Devendra Kumar Upadhyaya", "photo": "../brand/judges/devendra_kumar_upadhyaya.jpg", "at": A("c03", "honourable", 2)}])

# ── 2 · two trials, one slip ────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=S("c04"), t1=E("c05") + 0.05, at=A("c04", "district"), tag="SUPREME COURT OF INDIA · 02.11.2026",
    cases=[{"name": "In Re: XXX, a Judicial Officer, Rajasthan Judicial Services", "cite": "2026 INSC 1188 · arising out of SLP (Crl.) No. 13501 of 2025"}])
cue(type="timeline", t0=S("c04"), t1=E("c04") + 0.05,
    nodes=[{"label": "TRIAL ONE", "value": "a juvenile, as an adult", "sub": "Special Judge, POCSO Cases", "at": A("c04", "trials")},
           {"label": "TRIAL TWO", "value": "the adult co-accused", "sub": "Section 23 JJ Act: no joint trial", "at": A("c04", "adult", 2)}])
cue(type="timeline", t0=S("c05"), t1=E("c05") + 0.05,
    nodes=[{"label": "20 JANUARY 2024", "value": "both convicted", "sub": "two separate judgments", "at": A("c05", "january")},
           {"label": "THE SLIP", "value": "details crossed over", "sub": "“inadvertently incorporated”", "tone": "stop", "at": A("c05", "slipped")}])

# ── 3 · cut, copy and paste? ────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c06"), t1=E("c06") + 0.05, head="The High Court · 1 May 2025", head_at=S("c06") + 0.05,
    steps=[{"label": "Sentence not suspended", "sub": "after discussing the merits", "icon": "gavel", "at": A("c06", "refusing")},
           {"label": "“cut, copy and paste”", "sub": "“in all probability” scripted by the staff", "icon": "copy", "at": A("c06", "copy")},
           {"label": "Signed unread, it said", "sub": "adverse remarks · training · ACR", "icon": "triangle-alert", "at": A("c06", "signed")}])
cue(type="list", t0=S("c07"), t1=E("c07") + 0.05, head="Her explanation", head_at=S("c07") + 0.05,
    items=[{"n": 1, "text": "Two trials: almost the same witnesses, evidence", "at": A("c07", "witnesses")},
           {"n": 2, "text": "The sole stenographer was on leave", "at": A("c07", "stenographer")},
           {"n": 3, "text": "Bona fide typographical errors, she said", "at": A("c07", "typographical")}])

# ── 4 · before the verdict: the LawWorld request ────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c08"), t1=A("c08", "follow") - 0.05, text="The verdict is next. First, a quick request…", icon="scale", accent=True, at=A("c08", "decided"))
cue(type="list", t0=A("c08", "follow") - 0.05, t1=E("c08") + 0.05, head="Follow LawWorld · lawworld.ai", head_at=A("c08", "follow"),
    items=[{"n": 1, "text": "Search SC and High Court judgments, cited to source", "at": A("c08", "india's")},
           {"n": 2, "text": "Draft petitions, plaints and notices with AI", "at": A("c08", "platform")},
           {"n": 3, "text": "Sign up free · ₹200 AI credit included", "at": A("c08", "advocates")}])

# ── 5 · what the Court held ──────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "strictures") - 0.05, text="What did the Supreme Court decide?", icon="scale", accent=True, at=A("c09", "finally"))
cue(type="list", t0=A("c09", "strictures") - 0.05, t1=E("c09") + 0.05, head="Natural justice · audi alteram partem", head_at=A("c09", "strictures"),
    items=[{"n": 1, "text": "Strictures recorded on the judicial side", "at": A("c09", "judicial")},
           {"n": 2, "text": "No chance to show cause or explain", "at": A("c09", "explain")},
           {"n": 3, "text": "Unsustainable in the eyes of law", "at": A("c09", "breaks")}])
cue(type="point", t0=S("c10"), t1=A("c10", "remarks") - 0.05, text="Where warranted: a remark slip before the administrative Judge or the Chief Justice · the Supreme Court in 2026 INSC 367", icon="file-pen", accent=True, at=A("c10", "remark"))
cue(type="verdicts", t0=A("c10", "remarks") - 0.05, t1=E("c10") + 0.05,
    rows=[{"text": "Remarks in the High Court's paras 9, 10 and 11", "ok": False, "at": A("c10", "remarks")},
          {"text": "Training and ACR directions", "ok": False, "at": A("c10", "directions")},
          {"text": "Her appeal allowed", "ok": True, "at": A("c10", "allowed")}])

MUSIC = {"file": "audio/bed_mixkit738_140s.mp3", "target_lufs": -21}   # owner 02-11-2026: trending-style royalty-free bed, audible under the voice
# Fact-check 04-11-2026: c06 sub "on the merits of the appeal" -> "after discussing the merits" (para 13); c10 card: precedent
# party name dropped, 2026 INSC 367 kept (para 25).
# 04-11-2026 (parent): "Jhunjhunu" dropped from the c04 card - with the 20 Jan 2024 date it narrowed down the masked officer.
