# N. Sridhar Reddy v. The State of A.P. through Secretary & Ors., 2026 INSC 1191, Criminal Appeal No. 5187 of 2026 with Crl.A. Nos.
# 5188 and 5189 of 2026 (Prashant Kumar Mishra J. wrote it, Shree Chandrashekhar J.; pronounced 03.11.2026, REPORTABLE on page 1):
# panel cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND). HOOK format (split/JUDGMENT_HOOK_FORMAT.md):
# c01 hook question (spoken to everyone, no "Advocates,"), c02 curiosity, c03 "Hi, I'm Ravishankar" + bench, c04-c05 the two divorce
# cases, c06-c07 the bigamy case and both sides, c08 the LawWorld request, c09-c10 the verdict.
# Facts (para): married 18.04.2003, Sattenapalli, Hindu rites (4.i); Indian divorce case dismissed, appeal withdrawn, the Hindu marriage
# subsists (4.v, 22); UK citizenship by naturalisation 01.02.2013 (4.vi); Cambridge County Court petition 16.08.2013, her objections to
# jurisdiction and competence (4.vii, 11, 24); decree absolute 29.01.2014 on irretrievable breakdown (4.viii); second marriage
# 03.03.2014, Norfolk (4.ix); complaint 01.02.2016, ss.494, 120B r/w 34 IPC (4.x); chargesheet against him and his parents, the
# Magistrate took cognizance against the second wife too (4.xi, 31); AP High Court, 08.07.2019: no quashing (3, 4.xii, 4.xiii). His
# pleas: British citizen, s.4 IPC (5); decree valid, s.14 CPC (6); delay (7). Hers: Hindu law only (10); irretrievable breakdown is no
# HMA ground, s.13 CPC, Y. Narasimha Rao (12). Held: the decree, on "a ground not statutorily recognized under the Hindu Laws", "cannot
# automatically be accorded recognition in India", it violates the s.13 CPC threshold and Y. Narasimha Rao (20, 22); no escape from
# s.494 IPC on it (23); "legal consequences flowing from the subsisting marriage cannot be defeated by a subsequent change in the
# nationality" (25); bigamy a continuing offence (26); only at the present stage, no final view on the merits (27); parents: no overt
# act (28, 29); second wife: no overt act, liability "qua each accused separately" (32); his appeal dismissed, the others allowed (33).
# Names: the cause title on the cite card only; no finding of guilt anywhere ("the case goes on"). No section sign. List lines <= 52
# chars. Bench photos: brand/judges/prashant_kumar_mishra.jpg, shree_chandrashekhar.jpg (official sci.gov.in portraits).
FORMAT = "hook"   # build_course_plan.py: no opening sting, 15-frame lead (the cover), name tag on the "Ravishankar" clip

def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
ENDCARD = {"title": "Divorced abroad, married again?", "line": "This UK divorce, on a ground Hindu law does not recognise, fails Section 13 CPC: his bigamy case goes on for now", "sub": "LawWorld: legal research for advocates"}

# ── 1 · divorced abroad, wed again (hook, curiosity, intro) ──────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "man"), text="Divorced in England on a ground Hindu law does not recognise, then married again. Can he still face a bigamy case in India?", hl="Can he still face a bigamy case in India?")
cue(type="list", t0=S("c02"), t1=A("c02", "so") - 0.05, head="The husband's plea", head_at=S("c02") + 0.05,
    items=[{"n": 1, "text": "A British citizen since February 2013", "at": A("c02", "british")},
           {"n": 2, "text": "Second marriage: in England, March 2014", "at": A("c02", "remarried")},
           {"n": 3, "text": "Section 4 IPC: not for a foreigner's acts abroad", "at": A("c02", "argued")}])
cue(type="point", t0=A("c02", "so") - 0.05, t1=E("c02") + 0.05, text="So who is right?", icon="search", accent=True, at=A("c02", "right"))
cue(type="bench", t0=S("c03"), t1=E("c03") + 0.05, tag="Supreme Court of India · 3 November 2026",
    judges=[{"name": "Justice Prashant Kumar Mishra", "photo": "../brand/judges/prashant_kumar_mishra.jpg", "at": A("c03", "honourable")},
            {"name": "Justice Shree Chandrashekhar", "photo": "../brand/judges/shree_chandrashekhar.jpg", "at": A("c03", "honourable", 2)}])

# ── 2 · two divorce cases ────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=S("c04"), t1=E("c04") + 0.05, at=A("c04", "married"), tag="SUPREME COURT OF INDIA · 03.11.2026",
    cases=[{"name": "N. Sridhar Reddy v. State of A.P. & Ors.", "cite": "2026 INSC 1191 · Criminal Appeal Nos. 5187-5189 of 2026"}])
cue(type="timeline", t0=S("c04"), t1=E("c04") + 0.05,
    nodes=[{"label": "HINDU MARRIAGE", "value": "18 Apr 2003", "sub": "Sattenapalli, Andhra Pradesh", "at": A("c04", "married")},
           {"label": "DIVORCE IN INDIA", "value": "dismissed", "sub": "appeal withdrawn: the marriage subsists", "tone": "stop", "at": A("c04", "lost")}])
cue(type="timeline", t0=S("c05"), t1=E("c05") + 0.05,
    nodes=[{"label": "UK CITIZENSHIP", "value": "1 Feb 2013", "sub": "by naturalisation", "at": A("c05", "citizen")},
           {"label": "CAMBRIDGE COUNTY COURT", "value": "16 Aug 2013", "sub": "she objects to its jurisdiction", "at": A("c05", "cambridge")},
           {"label": "DECREE MADE ABSOLUTE", "value": "29 Jan 2014", "sub": "irretrievable breakdown", "at": A("c05", "dissolved")}])

# ── 3 · the bigamy case ──────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c06"), t1=E("c06") + 0.05, head="Section 494 IPC · bigamy", head_at=S("c06") + 0.05,
    steps=[{"label": "He marries again", "sub": "3 March 2014 · Norfolk, UK", "icon": "calendar", "at": A("c06", "married")},
           {"label": "The first wife complains", "sub": "1 Feb 2016 · Sections 494, 120B r/w 34 IPC", "icon": "file-text", "at": A("c06", "complaint")},
           {"label": "Parents, second wife accused", "sub": "chargesheet · the Magistrate's cognizance", "icon": "users", "at": A("c06", "parents")}])
cue(type="point", t0=S("c07"), t1=A("c07", "before") - 0.05, text="Andhra Pradesh High Court, 8 July 2019: no quashing for any of them", icon="landmark", accent=True, at=A("c07", "refused"))
cue(type="compare", t0=A("c07", "before") - 0.05, t1=E("c07") + 0.05, head="An English divorce: valid in India?", head_at=A("c07", "before"),
    cols=[{"title": "The husband", "icon": "user-round", "at": A("c07", "he")}, {"title": "The first wife", "icon": "user-round", "at": A("c07", "she")}],
    rows=[{"cells": ["The decree is valid: Section 14 CPC", "No such ground in Hindu law"], "cells_at": [A("c07", "valid"), A("c07", "hindu")]},
          {"cells": ["The complaint came almost two years later", "Section 13 CPC · Y. Narasimha Rao"], "cells_at": [A("c07", "late"), A("c07", "ground")]}])

# ── 4 · before the verdict: the LawWorld request ─────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c08"), t1=A("c08", "follow") - 0.05, text="The verdict is next. First, a quick request…", icon="scale", accent=True, at=A("c08", "decided"))
cue(type="list", t0=A("c08", "follow") - 0.05, t1=E("c08") + 0.05, head="Follow LawWorld · lawworld.ai", head_at=A("c08", "follow"),
    items=[{"n": 1, "text": "Search SC and High Court judgments, cited to source", "at": A("c08", "india's")},
           {"n": 2, "text": "Draft petitions, plaints and notices with AI", "at": A("c08", "platform")},
           {"n": 3, "text": "Sign up free · ₹200 AI credit included", "at": A("c08", "advocates")}])

# ── 5 · what the Court held ──────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "this") - 0.05, text="What did the Supreme Court decide?", icon="scale", accent=True, at=A("c09", "finally"))
cue(type="list", t0=A("c09", "this") - 0.05, t1=E("c09") + 0.05, head="Section 13 CPC · Y. Narasimha Rao", head_at=A("c09", "this"),
    items=[{"n": 1, "text": "The ground must be in the law they married under", "at": A("c09", "ground")},
           {"n": 2, "text": "This decree fails it: no automatic recognition", "at": A("c09", "fails")},
           {"n": 3, "text": "At this stage, no shield from Section 494 IPC", "at": A("c09", "shield")}])
cue(type="point", t0=S("c10"), t1=A("c10", "so") - 0.05, text="“…legal consequences flowing from the subsisting marriage cannot be defeated by a subsequent change in the nationality…”", icon="quote", accent=True, at=A("c10", "citizenship"))
cue(type="verdicts", t0=A("c10", "so") - 0.05, t1=E("c10") + 0.05,
    rows=[{"text": "His plea to quash the case", "ok": False, "at": A("c10", "case")},
          {"text": "Case against him goes on · no final view on merits", "ok": True, "at": A("c10", "goes")},
          {"text": "Parents, second wife: no overt act · quashed", "ok": True, "at": A("c10", "parents")}])

MUSIC = {"file": "audio/bed_mixkit738_140s.mp3", "target_lufs": -21}   # owner 02-11-2026: trending-style royalty-free bed, audible under the voice
