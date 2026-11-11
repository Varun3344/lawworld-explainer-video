# The Chairman, National Book Trust, India & Anr. v. A.R. Abdul Gaffar & Ors., 2026 INSC 1202, Civil Appeal No. 14369 of 2015
# (Diary No. 29802 / 2012), Supreme Court of India (Prashant Kumar Mishra J. wrote it, Augustine George Masih J.; pronounced 06.11.2026;
# REPORTABLE on page 1): panel cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND).
# HOOK format (split/JUDGMENT_HOOK_FORMAT.md): c01 hook question (spoken to everyone, no "Advocates,"), c02 curiosity (fundamental rights,
# the 2012 Full Bench, fourteen years), c03 "Hi, I'm Ravishankar" + bench, c04-c05 who runs the Trust (the Rules), c06 the Trust's case,
# c07 the Article 12 tests, c08 the LawWorld request, c09-c10 the verdict.
# Facts (para): the only question: is NBT a 'State' under Article 12 (1); Delhi HC Full Bench, answering a reference, cumulative test (2),
# resolutions, Chairman at the Government's pleasure, nominees, objects (3); judgment of 01.06.2012: "deep and pervasive control",
# "instrumentality or alter ego", 'other authorities' (4). Amicus Shri Sanjay Jain, Sr. Adv. (5), looked at the financial, functional
# and administrative relationship cumulatively, not at whether funding is the entirety of the income (17), thanked (28). Ajay Hasia: a
# registered society can, on the facts, be an instrumentality; form not determinative (7). Pradeep Kumar Biswas: "financially,
# functionally and administratively dominated", control "particular to the body and pervasive"; "merely regulatory" control is not
# enough (8). The Trust: a society/trust, not like a statutory corporation (10); grants only one source of income, own receipts a
# substantial part "for certain years" (16). Control: Government of India resolution 15.06.1957, reorganised 28.09.1962 (11); literature
# "at moderate prices" (11, 19); Rule 3 Chairman appointed by the Government of India, at its pleasure; Ministries of Education, Finance,
# I&B in the governing body (12); Rule 26 Executive Committee with the same Ministries; regulatory power needs prior Government approval
# (13); annual report and audited accounts to the Government (Rule 59), CAG audit (Rule 58), Rule 60 approval for altering the rules and
# purposes (14). 'State' does not make the Trust a Government department nor every employee a civil servant (22, 23). Holding: para 25
# (verbatim on the c10 card), para 26 (verbatim on the c09 card); appeal dismissed (27).
# Names: only the cause title on the cite card; the respondents' grievance is not in the judgment and is not mentioned. No general rule
# (never "every society / every funded body is State"). List lines <= 52 chars. Bench photos: brand/judges/prashant_kumar_mishra.jpg,
# brand/judges/augustine_george_masih.jpg (official, sci.gov.in judge page, fetched 11-11-2026).
FORMAT = "hook"   # build_course_plan.py: no opening sting, 15-frame lead (the cover), name tag on the "Ravishankar" clip

def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
ENDCARD = {"title": "Is the National Book Trust the ‘State’?", "line": "Yes: pervasive Government control makes it an ‘other authority’ under Article 12", "sub": "LawWorld: legal research for advocates"}

# ── 1 · is a book trust the State? (hook, curiosity, intro) ─────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "registered"), text="Registered as a society. Earns money selling books. Is the National Book Trust still the ‘State’?", hl="still the ‘State’?")
cue(type="point", t0=S("c02"), t1=A("c02", "full") - 0.05, text="If it is the ‘State’, it must respect the fundamental rights in Part III", icon="shield-check", accent=True, at=A("c02", "state"))
cue(type="counters", t0=A("c02", "full") - 0.05, t1=E("c02") + 0.05, head="Delhi High Court Full Bench, 2012: “State”", head_at=A("c02", "full"),
    items=[{"value": 14, "unit": "YEARS", "label": "Did the Supreme Court agree?", "sub": "1 June 2012 → 6 November 2026", "at": A("c02", "fourteen")}])
cue(type="bench", t0=S("c03"), t1=E("c03") + 0.05, tag="Supreme Court of India · 6 November 2026",
    judges=[{"name": "Justice Prashant Kumar Mishra", "photo": "../brand/judges/prashant_kumar_mishra.jpg", "at": A("c03", "prashant")},
            {"name": "Justice Augustine George Masih", "photo": "../brand/judges/augustine_george_masih.jpg", "at": A("c03", "augustine")}])

# ── 2 · who runs the Trust? ───────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=S("c04"), t1=E("c04") + 0.05, at=A("c04", "government"), tag="SUPREME COURT OF INDIA · 06.11.2026",
    cases=[{"name": "The Chairman, National Book Trust, India & Anr. v. A.R. Abdul Gaffar & Ors.", "cite": "2026 INSC 1202 · Civil Appeal No. 14369 of 2015"}])
cue(type="flow", t0=S("c04"), t1=E("c04") + 0.05, head="National Book Trust, India", head_at=S("c04") + 0.05,
    steps=[{"label": "Govt. resolution, 1957", "sub": "15 June 1957 · reorganised 1962", "icon": "landmark", "at": A("c04", "created")},
           {"label": "Good books for all", "sub": "at moderate prices", "icon": "book-open", "at": A("c04", "publish")},
           {"label": "Chairman: Govt.'s pick", "sub": "holds office at its pleasure", "icon": "user-round", "at": A("c04", "appoints")}])
cue(type="list", t0=S("c05"), t1=A("c05", "high") - 0.05, head="The Trust's Rules · Government inside", head_at=S("c05") + 0.05,
    items=[{"n": 1, "text": "Education, Finance, I&B Ministries: governing body", "at": A("c05", "ministries")},
           {"n": 2, "text": "The same Ministries on the Executive Committee", "at": A("c05", "executive")},
           {"n": 3, "text": "Accounts audited by the CAG · reports to Govt.", "at": A("c05", "audits")},
           {"n": 4, "text": "Changes to its rules need Government approval", "at": A("c05", "accounts")}])
cue(type="point", t0=A("c05", "high") - 0.05, t1=E("c05") + 0.05, text="Delhi High Court Full Bench, 1 June 2012: “deep and pervasive control” · an ‘other authority’", icon="landmark", accent=True, at=A("c05", "found"))

# ── 3 · society, or State? ──────────────────────────────────────────────────────────────────────────────────────────
cue(type="list", t0=S("c06"), t1=E("c06") + 0.05, head="Before the Supreme Court", head_at=S("c06") + 0.05,
    items=[{"n": 1, "text": "Trust: a society, not a statutory corporation", "at": A("c06", "registered")},
           {"n": 2, "text": "Trust: grants are only one source of income", "at": A("c06", "grants")},
           {"n": 3, "text": "Amicus Sanjay Jain: weigh all control together", "at": A("c06", "source")}])
cue(type="compare", t0=S("c07"), t1=E("c07") + 0.05, head="Article 12 · the tests", head_at=S("c07") + 0.05,
    cols=[{"title": "Ajay Hasia (1981)", "icon": "scale", "at": A("c07", "hasia")}, {"title": "Pradeep Kumar Biswas (2002)", "icon": "landmark", "at": A("c07", "pradeep")}],
    rows=[{"cells": ["A registered society can be ‘State’", "Financially, functionally, administratively dominated?"], "cells_at": [A("c07", "society"), A("c07", "government")]},
          {"cells": ["The form is not decisive", "Pervasive control · not merely regulatory"], "cells_at": [A("c07", "state"), A("c07", "merely")]}])

# ── 4 · before the verdict: the LawWorld request ─────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c08"), t1=A("c08", "follow") - 0.05, text="The verdict is next. First, a quick request…", icon="scale", accent=True, at=A("c08", "decided"))
cue(type="list", t0=A("c08", "follow") - 0.05, t1=E("c08") + 0.05, head="Follow LawWorld · lawworld.ai", head_at=A("c08", "follow"),
    items=[{"n": 1, "text": "Search SC and High Court judgments, cited to source", "at": A("c08", "india's")},
           {"n": 2, "text": "Draft petitions, plaints and notices with AI", "at": A("c08", "platform")},
           {"n": 3, "text": "Sign up free · ₹200 AI credit included", "at": A("c08", "advocates")}])

# ── 5 · what the Court held ──────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "government") - 0.05, text="What did the Supreme Court decide?", icon="scale", accent=True, at=A("c09", "finally"))
cue(type="quote", t0=A("c09", "government") - 0.05, t1=E("c09") + 0.05, at=A("c09", "government"), reveal=r3(A("c09", "twelve") - A("c09", "government")),
    text="… National Book Trust is an ‘other authority’ within the meaning of Article 12 of the Constitution and is consequently a ‘State’ for that purpose.",
    hl=["‘other authority’", "consequently a ‘State’"],
    note={"text": "Upheld: Delhi High Court Full Bench, 2012", "at": A("c09", "high")})
cue(type="quote", t0=S("c10"), t1=A("c10", "but") - 0.05, at=S("c10") + 0.1, reveal=r3(A("c10", "change") - S("c10")),
    text="Its registration as a society, or the fact that it generates part of its income independently cannot displace the cumulative constitutional character of the institution.",
    hl=["cannot displace"])
cue(type="verdicts", t0=A("c10", "but") - 0.05, t1=E("c10") + 0.05,
    rows=[{"text": "The Trust becomes a Government department", "ok": False, "at": A("c10", "ruling")},
          {"text": "Every employee becomes a civil servant", "ok": False, "at": A("c10", "employee")},
          {"text": "Full Bench upheld · Trust's appeal dismissed", "ok": True, "at": A("c10", "dismissed")}])

MUSIC = {"file": "audio/bed_mixkit738_140s.mp3", "target_lufs": -21}   # owner 02-11-2026: trending-style royalty-free bed, audible under the voice
