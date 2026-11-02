FORMAT = "hook"   # build_course_plan.py: no opening sting, 15-frame lead (the cover), name tag on the "Ravishankar" clip
# Rajasthan Housing Board v. M/s Hariyali Rural Ventures Ltd. & Ors., 2026 INSC 1168, SLP (C) No. 35141/2026, Supreme Court of India
# (an order: Dipankar Datta J. wrote it, Sheel Nagu J.; New Delhi, 16.10.2026, REPORTABLE): panel cues, run by split/build_course_plan.py
# (helpers: at S E cue fx have r3 PEND). HOOK format (split/JUDGMENT_HOOK_FORMAT.md): c01 hook question, c02 curiosity, c03 "Hi, I'm
# Ravishankar" + bench, c04-c07 facts / the writ / the plea, c08 the LawWorld request, c09-c10 the verdict.
# Facts from the order (paras): SLP against the Rajasthan HC (Jaipur Bench) judgment of 06.07.2026 dismissing the Article 227 petition
# (S.B. CWP 4122/2026) of RHB, the State and the Special Officer, UDH (1); LARRA, Jaipur: 26.05.2025 allowed the first respondent's
# reference under Section 64; 12.09.2025 a minor modification in its favour while allowing its review petition (2); HC: writ not
# maintainable given the Section 74(1) appeal; even as an appeal, the proviso bars it - nothing 60 days beyond the 60 days; right to
# appeal foreclosed after the maximum condonable period (3); RHB relied on S.V. Global Mill (2026 SCC OnLine SC 171): 60 days in the
# proviso "not to be mandatory", unnoticed by the HC; liberty sought to appeal with a condonation plea (4); S.V. Global Mill summarised:
# Limitation Act not excluded (5); the Bench "expressed reservation"; counsel: then a reference to a larger Bench (6); reference not
# warranted, its ratio does not apply here; the precedent "does not commend our acceptance" (7); pari materia statutes with outer limits
# (8-10); it renders the proviso otiose, the 120-day outer limit "denuded of all its meaning"; Section 5 impliedly excluded (11);
# Hukumdev Narain Yadav (3-J) binding, "reverse prejudice" to landowners (14-16); the proviso: a Section 5-like provision with a statutory
# cap (17); "the period of 120 days in Section 74 is inflexible and rigid", not "even by a single day's delay"; "Even this Court in
# exercise of its power under Article 142 cannot condone the delay" (20); "we decline a reference" (21); even assuming S.V. Global Mill is
# right, RHB never filed a Section 74 appeal, it went under Article 227; the HC "was perfectly justified in spurning the challenge" (23);
# "pending time-barred appeals under Section 74 of the 2013 Act may be decided by the relevant high courts in accordance with law" (24);
# SLP dismissed (25). NOT on any card: "overruled" (S.V. Global Mill is a coordinate Bench; this Bench disagreed and declined a reference).
# No section sign anywhere. List lines <= 52 chars. Official sci.gov.in portraits on the bench card.

def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
ENDCARD = {"title": "Late by one day: can the appeal be heard?", "line": "Section 74's 120 days are “inflexible and rigid”: an appeal even a single day beyond is barred", "sub": "LawWorld: legal research for advocates"}

# ── 1 · late by one day? (hook, curiosity, intro) ───────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "land"), text="Can a High Court condone a land acquisition appeal filed even one day after the 120-day limit?", hl="even one day after the 120-day limit?")
cue(type="list", t0=S("c02"), t1=A("c02", "so") - 0.05, head="Two benches of the Supreme Court", head_at=S("c02") + 0.05,
    items=[{"n": 1, "text": "S.V. Global Mill: the Limitation Act applies", "at": A("c02", "global")},
           {"n": 2, "text": "Past 120 days: delay condonable on sufficient cause", "at": A("c02", "limitation")},
           {"n": 3, "text": "Now a second two-judge bench disagrees", "at": A("c02", "another")}])
cue(type="point", t0=A("c02", "so") - 0.05, t1=E("c02") + 0.05, text="So is the 120-day limit rigid?", icon="search", accent=True, at=A("c02", "so"))
cue(type="bench", t0=S("c03"), t1=E("c03") + 0.05, tag="Supreme Court of India · 16 October 2026",
    judges=[{"name": "Justice Dipankar Datta", "photo": "../brand/judges/dipankar_datta.jpg", "at": A("c03", "honourable")},
            {"name": "Justice Sheel Nagu", "photo": "../brand/judges/sheel_nagu.jpg", "at": A("c03", "honourable", 2)}])

# ── 2 · the writ ────────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c04"), t1=E("c04") + 0.05, head="Right to Fair Compensation Act, 2013", head_at=S("c04") + 0.05,
    steps=[{"label": "LARRA, Jaipur", "sub": "reference under Section 64", "icon": "landmark", "at": A("c04", "authority")},
           {"label": "Reference allowed", "sub": "the company's · 26 May 2025", "icon": "file-text", "at": A("c04", "reference")},
           {"label": "Review allowed too", "sub": "12 September 2025 · a minor change", "icon": "check", "at": A("c04", "review")}])
cue(type="cite", t0=S("c05"), t1=E("c05") + 0.05, at=A("c05", "rajasthan"), tag="SUPREME COURT OF INDIA · 16.10.2026",
    cases=[{"name": "Rajasthan Housing Board v. M/s Hariyali Rural Ventures Ltd. & Ors.", "cite": "2026 INSC 1168 · SLP (C) No. 35141 of 2026"}])
cue(type="timeline", t0=S("c05"), t1=E("c05") + 0.05,
    nodes=[{"label": "SECTION 74 APPEAL", "value": "not filed", "sub": "the remedy the Act gives", "tone": "stop", "at": A("c05", "housing")},
           {"label": "HIGH COURT, JAIPUR", "value": "Article 227 writ", "sub": "with the State and the Special Officer, UDH", "at": A("c05", "writ")}])

# ── 3 · too late to appeal ──────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c06"), t1=A("c06", "section") - 0.05, text="Rajasthan High Court, 6 July 2026: the writ is not maintainable · the remedy is an appeal under Section 74(1)", icon="landmark", accent=True, at=A("c06", "dismissed"))
cue(type="counters", t0=A("c06", "section") - 0.05, t1=E("c06") + 0.05, head="Section 74 of the 2013 Act", head_at=A("c06", "section"),
    items=[{"value": 60, "unit": "DAYS", "label": "To appeal", "sub": "from the award", "at": A("c06", "sixty")},
           {"value": 60, "unit": "DAYS", "label": "More, under the proviso", "sub": "delay condonable, up to a cap", "at": A("c06", "sixty", 2)},
           {"value": 120, "unit": "DAYS", "label": "The outer limit", "sub": "per the High Court: expired", "tone": "red", "at": A("c06", "even")}])
cue(type="flow", t0=S("c07"), t1=E("c07") + 0.05, head="Before the Supreme Court", head_at=S("c07") + 0.05,
    steps=[{"label": "Relies on S.V. Global Mill", "sub": "“unnoticed” by the High Court, it says", "icon": "file-text", "at": A("c07", "relied")},
           {"label": "Liberty to file a late appeal", "sub": "with a plea to condone the delay", "icon": "user", "at": A("c07", "liberty")},
           {"label": "The Bench doubts it", "sub": "the Board: refer it to a larger Bench", "icon": "scale", "at": A("c07", "doubted")}])

# ── 4 · before the verdict: the LawWorld request ────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c08"), t1=A("c08", "follow") - 0.05, text="The verdict is next. First, a quick request…", icon="scale", accent=True, at=A("c08", "decided"))
cue(type="list", t0=A("c08", "follow") - 0.05, t1=E("c08") + 0.05, head="Follow LawWorld · lawworld.ai", head_at=A("c08", "follow"),
    items=[{"n": 1, "text": "Search SC and High Court judgments, cited to source", "at": A("c08", "india's")},
           {"n": 2, "text": "Draft petitions, plaints and notices with AI", "at": A("c08", "platform")},
           {"n": 3, "text": "Sign up free · ₹200 AI credit included", "at": A("c08", "advocates")}])

# ── 5 · what the Court held ─────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "the", 2) - 0.05, text="What did the Supreme Court decide?", icon="scale", accent=True, at=A("c09", "finally"))
cue(type="list", t0=A("c09", "the", 2) - 0.05, t1=E("c09") + 0.05, head="Section 74 of the 2013 Act", head_at=A("c09", "hundred"),
    items=[{"n": 1, "text": "120 days: “inflexible and rigid”", "at": A("c09", "inflexible")},
           {"n": 2, "text": "Past 120 days, even by a single day: barred", "at": A("c09", "single")},
           {"n": 3, "text": "Art. 142 can't condone it; exemption may be sought", "at": A("c09", "day")}])
cue(type="point", t0=S("c10"), t1=A("c10", "any") - 0.05, text="S.V. Global Mill “does not commend our acceptance”: it renders the proviso otiose · a larger-Bench reference: declined", icon="scale", accent=True, at=A("c10", "disagreed"))
cue(type="verdicts", t0=A("c10", "any") - 0.05, t1=E("c10") + 0.05,
    rows=[{"text": "No appeal filed: High Court “perfectly justified”", "ok": True, "at": A("c10", "board")},
          {"text": "The Board's plea: liberty for a late appeal", "ok": False, "at": A("c10", "petition")},
          {"text": "Pending late appeals: “in accordance with law”", "ok": True, "at": A("c10", "failed")}])

MUSIC = {"file": "audio/bed_mixkit738_140s.mp3", "target_lufs": -21}   # owner 02-11-2026: trending-style royalty-free bed, audible under the voice
