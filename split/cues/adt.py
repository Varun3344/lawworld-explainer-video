# Adit Buildwell Pvt. Ltd. v. Commissioner of CGST, South Commissionerate, New Delhi & Anr., W.P.(C) 2728/2024, High Court of Delhi
# (Division Bench: Avneesh Jhingan J. wrote it (ORAL), Amit Sharma J.; decided 29.10.2026; "Reportable: Yes" at the end, page 4):
# panel cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND).
# HOOK format (split/JUDGMENT_HOOK_FORMAT.md): c01 hook question (spoken to everyone, no "Advocates,"), c02 curiosity (the appeal
# remedy), c03 "Hi, I'm Ravishankar" + bench, c04-c05 the timeline, c06-c07 both sides, c08 the LawWorld request, c09-c10 the verdict.
# Facts (para): writ against the order of 24.11.2023 of the Commissioner, CGST, Delhi South (1); registered with the Service Tax
# Department; SCN; reply 23.05.2022; personal hearing 07.11.2023; adjourned to 15.11.2023 at the petitioner's request; on 15.11.2023
# it sought time till 24.11.2023 to produce documents; not considered; order passed 24.11.2023 (2); petitioner: no reasonable
# opportunity; email of 15.11.2023 sought a further ten days (3); department: sufficient opportunities, no document filed till
# 23.11.2023 (4); counter 5.6: waited "an additional period of 9 days" (8); held: the nine-days contention "lacks merit"; once the
# request was not considered there was no occasion to file; the order came on 24.11.2023, the very date up to which time was sought
# (6); appeal remedy exists, but Whirlpool (1998) 8 SCC 1: no bar on "a violation of the principle of natural justice" (7);
# "The request made for producing the additional material by 24.11.2023 was neither considered nor rejected." (8); request "not even
# noted"; one ground of the order: failure to produce documents; "The minimum that was expected from a quasi-judicial authority was
# at least to deal with the request for grant of further time and thereafter take an appropriate decision thereon." (9); order
# "violative of principles of natural justice and is set aside"; remanded to respondent no.1 to decide afresh from the stage of
# 15.11.2023 (10); appear on 02.12.2026 at 11.00 a.m. (11); petition disposed of (12). Not on any card: the tax amount (not given);
# the "admitted case of the department" line (9; Flow policy). Company named on the cite card only. List lines <= 52 chars.
# Bench photos: brand/judges/avneesh_jhingan.jpg, amit_sharma.jpg (official delhihighcourt.nic.in portraits).
FORMAT = "hook"   # build_course_plan.py: no opening sting, 15-frame lead (the cover), name tag on the "Ravishankar" clip

def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
ENDCARD = {"title": "Asked for time, order passed that very day?", "line": "The request was neither considered nor rejected: natural justice breached, order set aside, case remanded", "sub": "LawWorld: legal research for advocates"}

# ── 1 · order on the last day? (hook, curiosity, intro) ────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "ask"), text="You ask for time until a date. The order comes on that very date, with no word on your request. Is that fair?", hl="Is that fair?")
cue(type="list", t0=S("c02"), t1=A("c02", "so") - 0.05, head="One company, one tax order", head_at=S("c02") + 0.05,
    items=[{"n": 1, "text": "Time sought: till 24 November 2023", "at": A("c02", "company")},
           {"n": 2, "text": "Order passed: 24 November 2023", "at": A("c02", "exactly")},
           {"n": 3, "text": "A remedy of appeal was open", "at": A("c02", "remedy")}])
cue(type="point", t0=A("c02", "so") - 0.05, t1=E("c02") + 0.05, text="Hear the writ petition, or send it to appeal?", icon="search", accent=True, at=A("c02", "writ"))
cue(type="bench", t0=S("c03"), t1=E("c03") + 0.05, tag="Delhi High Court · 29 October 2026",
    judges=[{"name": "Justice Avneesh Jhingan", "photo": "../brand/judges/avneesh_jhingan.jpg", "at": A("c03", "honourable")},
            {"name": "Justice Amit Sharma", "photo": "../brand/judges/amit_sharma.jpg", "at": A("c03", "honourable", 2)}])

# ── 2 · the dates that matter ────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=S("c04"), t1=E("c04") + 0.05, at=A("c04", "company"), tag="HIGH COURT OF DELHI · 29.10.2026",
    cases=[{"name": "Adit Buildwell Pvt. Ltd. v. Commissioner of CGST, South Commissionerate, New Delhi & Anr.", "cite": "W.P.(C) No. 2728 of 2024"}])
cue(type="timeline", t0=S("c04"), t1=E("c04") + 0.05,
    nodes=[{"label": "SHOW CAUSE NOTICE", "value": "reply filed", "sub": "23 May 2022 · Service Tax", "at": A("c04", "replied")},
           {"label": "PERSONAL HEARING", "value": "7 Nov 2023", "sub": "an opportunity afforded", "at": A("c04", "hearing")}])
cue(type="timeline", t0=S("c05"), t1=E("c05") + 0.05,
    nodes=[{"label": "HEARING ADJOURNED", "value": "15 Nov 2023", "sub": "at the company's request", "at": A("c05", "moved")},
           {"label": "TIME SOUGHT", "value": "till 24 Nov", "sub": "by email, to produce documents", "at": A("c05", "asked")},
           {"label": "ORDER PASSED", "value": "24 Nov 2023", "sub": "the request not considered", "tone": "red", "at": A("c05", "order")}])

# ── 3 · a fair chance? ───────────────────────────────────────────────────────────────────────────────────────────────
cue(type="compare", t0=S("c06"), t1=E("c07") + 0.05, head="A fair chance to defend?", head_at=S("c06") + 0.05,
    cols=[{"title": "The company", "icon": "file-text", "at": A("c06", "company")}, {"title": "The department", "icon": "landmark", "at": A("c07", "department")}],
    rows=[{"cells": ["No reasonable chance to defend", "Enough chances were given"], "cells_at": [A("c06", "reasonable"), A("c07", "enough")]},
          {"cells": ["Email of 15 Nov: ten more days", "Waited 9 days, no document filed"], "cells_at": [A("c06", "email"), A("c07", "waited")]}])

# ── 4 · before the verdict: the LawWorld request ─────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c08"), t1=A("c08", "follow") - 0.05, text="The verdict is next. First, a quick request…", icon="scale", accent=True, at=A("c08", "decided"))
cue(type="list", t0=A("c08", "follow") - 0.05, t1=E("c08") + 0.05, head="Follow LawWorld · lawworld.ai", head_at=A("c08", "follow"),
    items=[{"n": 1, "text": "Search SC and High Court judgments, cited to source", "at": A("c08", "india's")},
           {"n": 2, "text": "Draft petitions, plaints and notices with AI", "at": A("c08", "platform")},
           {"n": 3, "text": "Sign up free · ₹200 AI credit included", "at": A("c08", "advocates")}])

# ── 5 · what the Court held ──────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "request") - 0.05, text="What did the High Court decide?", icon="scale", accent=True, at=A("c09", "finally"))
cue(type="point", t0=A("c09", "request") - 0.05, t1=A("c09", "yet") - 0.05, text="“The request made for producing the additional material by 24.11.2023 was neither considered nor rejected.”", icon="quote", accent=True, at=A("c09", "request"))
cue(type="point", t0=A("c09", "yet") - 0.05, t1=E("c09") + 0.05, text="Yet one ground of the order: the company did not produce the documents", icon="file-text", accent=True, at=A("c09", "ground"))
cue(type="point", t0=S("c10"), t1=A("c10", "natural") - 0.05, text="“The minimum that was expected from a quasi-judicial authority was at least to deal with the request for grant of further time…”", icon="quote", accent=True, at=A("c10", "minimum"))
cue(type="verdicts", t0=A("c10", "natural") - 0.05, t1=E("c10") + 0.05,
    rows=[{"text": "Natural justice breached: appeal no bar (Whirlpool)", "ok": True, "at": A("c10", "breached")},
          {"text": "The order of 24 November 2023: set aside", "ok": True, "at": A("c10", "aside")},
          {"text": "Remanded: afresh from the 15.11.2023 stage", "ok": True, "at": A("c10", "back")}])

MUSIC = {"file": "audio/bed_mixkit738_140s.mp3", "target_lufs": -21}   # owner 02-11-2026: trending-style royalty-free bed, audible under the voice
