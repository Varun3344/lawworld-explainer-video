# Goverdhan v. State of Rajasthan, 2026 INSC 1190, Criminal Appeal No. 1394 of 2017 (Sandeep Mehta J. wrote it, Devendra Kumar
# Upadhyaya J.; decided 03.11.2026, Reportable): panel cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND).
# HOOK format (split/JUDGMENT_HOOK_FORMAT.md): c01 hook question (spoken to everyone, no "Advocates,"), c02 curiosity, c03 "Hi, I'm
# Ravishankar" + bench, c04-c05 the case, c06-c07 the proof of the letters, c08 the LawWorld request, c09-c10 the verdict.
# SENSITIVE: a death by suicide. No private person's name anywhere except the cause title on the cite bar; no detail of how she died.
# Facts from the judgment (paras): s.306 IPC, Addl. Sessions Judge, Women Atrocities Cases No.1, Jaipur Metropolitan; convicted
# 09.12.2016, ten years' RI + Rs.50,000 fine; High Court (single Judge, Jaipur) dismissed the appeal 11.05.2017 (2); FIR 14/2009 under
# ss.498-A, 406, 323 IPC, 05.02.2009 (5); Domestic Violence Act proceedings, maintenance (6); four letters with abusive language and
# threats, per the prosecution (7); her mother's complaint 02.02.2011, FIR 45/2011 under s.306 IPC (8, 9), 15 days later (16); the High
# Court: continuous harassment "tantamounted to instigation" (12); "The only palpable evidence" = four postcard letters, Ex. P-16 to
# P-19; no specimen handwriting taken; compared with an application and a pocket diary (20); "it is essential to examine the
# handwriting expert in evidence"; the expert "was not examined by the prosecution" (23); his s.313 CrPC non-denial relied on below;
# "the prosecution must stand on its own legs and establish the guilt of the accused beyond reasonable doubt"; no "substitute for
# proof" (24); the letters also hold "fervent appeals ... for reconciliation" (27); living apart for more than 2 years, pursuing her
# cases; the letters by themselves not "the immediate cause"; even if in his handwriting, not abetment under s.107 IPC (29, 30);
# conviction set aside, acquitted of s.306 IPC (31); appeal allowed (32); bail bonds discharged (33).
# No section sign anywhere. List lines <= 52 chars. Official sci.gov.in portraits on the bench card.
FORMAT = "hook"   # build_course_plan.py: no opening sting, 15-frame lead (the cover), name tag on the "Ravishankar" clip

def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
ENDCARD = {"title": "What must be proved for abetment?", "line": "Instigation, beyond reasonable doubt, on the prosecution's own evidence. Unproved letters could not convict", "sub": "LawWorld: legal research for advocates"}

# ── 1 · what must be proved? (hook, curiosity, intro) ───────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "person"), text="Abetment of suicide: what must the prosecution prove before it can convict?", hl="what must the prosecution prove")
cue(type="counters", t0=S("c02"), t1=A("c02", "but") - 0.05, head="Section 306 IPC · the trial court, 2016", head_at=S("c02") + 0.05,
    items=[{"value": 10, "unit": "YEARS", "label": "Rigorous imprisonment", "sub": "and a ₹50,000 fine", "tone": "red", "at": A("c02", "ten")},
           {"value": 4, "unit": "LETTERS", "label": "The main evidence", "sub": "postcards, said to be his", "at": A("c02", "four")}])
cue(type="point", t0=A("c02", "but") - 0.05, t1=E("c02") + 0.05, text="Did anyone prove he wrote them?", icon="search", accent=True, at=A("c02", "prove"))
cue(type="bench", t0=S("c03"), t1=E("c03") + 0.05, tag="Supreme Court of India · 3 November 2026",
    judges=[{"name": "Justice Sandeep Mehta", "photo": "../brand/judges/sandeep_mehta.jpg", "at": A("c03", "honourable")},
            {"name": "Justice Devendra Kumar Upadhyaya", "photo": "../brand/judges/devendra_kumar_upadhyaya.jpg", "at": A("c03", "honourable", 2)}])

# ── 2 · the four letters ─────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=S("c04"), t1=E("c05") + 0.05, at=A("c04", "years"), tag="SUPREME COURT OF INDIA · 03.11.2026",
    cases=[{"name": "Goverdhan v. State of Rajasthan", "cite": "2026 INSC 1190 · Criminal Appeal No. 1394 of 2017"}])
cue(type="timeline", t0=S("c04"), t1=E("c04") + 0.05,
    nodes=[{"label": "LIVING APART", "value": "over two years", "sub": "at her parents' home", "at": A("c04", "years")},
           {"label": "HER CASES", "value": "cruelty · domestic violence", "sub": "Section 498-A IPC · the DV Act", "at": A("c04", "cruelty")}])
cue(type="timeline", t0=S("c05"), t1=E("c05") + 0.05,
    nodes=[{"label": "15 DAYS LATER", "value": "her mother's complaint", "sub": "FIR under Section 306 IPC", "at": A("c05", "mother")},
           {"label": "THE PROSECUTION'S CASE", "value": "four postcard letters", "sub": "abusive language and threats, it said", "at": A("c05", "postcard")}])

# ── 3 · who wrote them? ──────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c06"), t1=E("c06") + 0.05, head="Who wrote the four letters?", head_at=S("c06") + 0.05,
    steps=[{"label": "No specimen handwriting", "sub": "never taken during the investigation", "icon": "circle-x", "at": A("c06", "specimen")},
           {"label": "Other papers compared", "sub": "an application · a pocket diary", "icon": "file-text", "at": A("c06", "compared")},
           {"label": "Expert never examined", "sub": "no cross-examination in court", "icon": "triangle-alert", "at": A("c06", "examined")}])
cue(type="timeline", t0=S("c07"), t1=E("c07") + 0.05,
    nodes=[{"label": "TRIAL COURT · 2016", "value": "convicted", "sub": "Section 306 IPC", "at": A("c07", "convicted")},
           {"label": "HIGH COURT · 2017", "value": "appeal dismissed", "sub": "harassment “tantamounted to instigation”", "at": A("c07", "agreed")},
           {"label": "BOTH COURTS", "value": "no specific denial", "sub": "of the letters, in his Section 313 CrPC statement", "tone": "stop", "at": A("c07", "denied")}])

# ── 4 · before the verdict: the LawWorld request ────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c08"), t1=A("c08", "follow") - 0.05, text="The verdict is next. First, a quick request…", icon="scale", accent=True, at=A("c08", "decided"))
cue(type="list", t0=A("c08", "follow") - 0.05, t1=E("c08") + 0.05, head="Follow LawWorld · lawworld.ai", head_at=A("c08", "follow"),
    items=[{"n": 1, "text": "Search SC and High Court judgments, cited to source", "at": A("c08", "india's")},
           {"n": 2, "text": "Draft petitions, plaints and notices with AI", "at": A("c08", "platform")},
           {"n": 3, "text": "Sign up free · ₹200 AI credit included", "at": A("c08", "advocates")}])

# ── 5 · what the Court held ──────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "prosecution") - 0.05, text="What did the Supreme Court decide?", icon="scale", accent=True, at=A("c09", "finally"))
cue(type="list", t0=A("c09", "prosecution") - 0.05, t1=E("c09") + 0.05, head="Sections 306 and 107 IPC", head_at=A("c09", "prosecution"),
    items=[{"n": 1, "text": "The prosecution must stand on its own legs", "at": A("c09", "legs")},
           {"n": 2, "text": "Abetment must be proved beyond reasonable doubt", "at": A("c09", "abetment")},
           {"n": 3, "text": "A missing denial is no substitute for proof", "at": A("c09", "denial")}])
cue(type="point", t0=S("c10"), t1=A("c10", "and") - 0.05, text="“…it is essential to examine the handwriting expert in evidence…” · here, the expert was not examined", icon="quote", accent=True, at=A("c10", "expert"))
cue(type="verdicts", t0=A("c10", "and") - 0.05, t1=E("c10") + 0.05,
    rows=[{"text": "Even if his, the letters alone: not abetment", "ok": True, "at": A("c10", "wrote")},
          {"text": "Conviction under Section 306 IPC", "ok": False, "at": A("c10", "immediate")},
          {"text": "Acquitted · bail bonds discharged", "ok": True, "at": A("c10", "acquitted")}])

MUSIC = {"file": "audio/bed_mixkit738_140s.mp3", "target_lufs": -21}   # owner 02-11-2026: trending-style royalty-free bed, audible under the voice
# Fact-check 04-11-2026: c09 item 2 "Abetment proved ..." -> "Abetment must be proved beyond reasonable doubt" (paras 24, 29-30).
