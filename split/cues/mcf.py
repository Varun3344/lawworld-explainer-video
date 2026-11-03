# Susheela Kawar v. M. Pettu Lakshmi, with S. Ranjani (died) through LRs v. Gopi @ Gopala Krishnan & Anr., C.R.P. Nos. 4064 & 4106 of
# 2026, 2026:MHC:4385, High Court of Judicature at Madras (P.B. Balaji J.; reserved 23.09.2026, pronounced 30.10.2026; listed as
# Reportable in the court's judis database): panel cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND).
# HOOK format (split/JUDGMENT_HOOK_FORMAT.md): c01 hook question (spoken to everyone, no "Advocates," - owner 03-11-2026), c02
# curiosity, c03 "Hi, I'm Ravishankar" + bench, c04-c07 the two suits / both sides, c08 the LawWorld request, c09-c10 the verdict.
# Facts from the judgment (page / para): the question - refund of court fee on the plaint after trial has commenced (p2, 1). CRP 4064:
# O.S. 3/2019 for specific performance (Thiruvallur at Ponneri); settled out of court and withdrawn after issues were framed and PW1's
# proof affidavit was filed; decree: half the court fee refunded after deducting 5% (23, 24). CRP 4106: O.S. 133/2007 (Chengalpattu);
# compromise memo 09.10.2025 after PW1, DW1, DW2 and court witness CW1 were examined; refund refused (4, 25). Petitioners: M.C.
# Subramaniam, (2021) 3 SCC 560 - 100% refund under s.69-A even for an out-of-court settlement (3). The Advocate General: M.C.
# Subramaniam did not factor Afcons, (2010) 8 SCC 24 (8); the amicus: only s.69-A with s.89 CPC was analysed, s.69 was not in issue
# (9, 10). s.69: refund only if the suit is dismissed as settled out of court "before any evidence has been recorded on the merits of
# the claim" (12); M.C. Subramaniam did not deal with s.69 or the stage of settlement (14, 18); "a party is not entitled to any refund
# once evidence is recorded" (19); Afcons followed as the earlier binding ratio (21, 22); CRP 4106: refusal right; CRP 4064: no
# refund was due, but the 50% less 5% is not interfered with as the State did not challenge it (22, 24); both CRPs dismissed (31).
# Not on any card: the parties' allegations or the merits of either suit; the Tamil Nadu Law Commission reference (31). The cause title
# appears only on the cite card. No section sign anywhere. List lines <= 52 chars. Bench photo: brand/judges/pb_balaji.jpg.
FORMAT = "hook"   # build_course_plan.py: no opening sting, 15-frame lead (the cover), name tag on the "Ravishankar" clip

def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
ENDCARD = {"title": "Settled after evidence: court fee back?", "line": "No: under Section 69, a refund only if the suit settles before any evidence is recorded", "sub": "LawWorld: legal research for advocates"}

# ── 1 · refund after trial? (hook, curiosity, intro) ─────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "civil"), text="Settled out of court after the witnesses testified? Is the court fee refunded?", hl="court fee refunded?")
cue(type="list", t0=S("c02"), t1=A("c02", "so") - 0.05, head="Court fee refund · one question", head_at=S("c02") + 0.05,
    items=[{"n": 1, "text": "Supreme Court: full refund, even private deals", "at": A("c02", "supreme")},
           {"n": 2, "text": "One trial court: half the fee", "at": A("c02", "half")},
           {"n": 3, "text": "Another trial court: nothing", "at": A("c02", "nothing")}])
cue(type="point", t0=A("c02", "so") - 0.05, t1=E("c02") + 0.05, text="Who got it right?", icon="search", accent=True, at=A("c02", "right"))
cue(type="bench", t0=S("c03"), t1=E("c03") + 0.05, tag="Madras High Court · 30 October 2026",
    judges=[{"name": "Justice P.B. Balaji", "photo": "../brand/judges/pb_balaji.jpg", "at": A("c03", "honourable")}])

# ── 2 · two settlements ──────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c04"), t1=E("c04") + 0.05, head="Suit 1 · specific performance", head_at=S("c04") + 0.05,
    steps=[{"label": "Trial begins", "sub": "issues framed", "icon": "scale", "at": A("c04", "suit")},
           {"label": "Proof affidavit filed", "sub": "the plaintiff's first witness", "icon": "file-text", "at": A("c04", "proof")},
           {"label": "Settled: half refunded", "sub": "less 5% · trial court", "icon": "check", "at": A("c04", "half")}])
cue(type="cite", t0=S("c05"), t1=E("c05") + 0.05, at=A("c05", "other"), tag="HIGH COURT OF MADRAS · 30.10.2026",
    cases=[{"name": "Susheela Kawar v. M. Pettu Lakshmi, with a connected revision", "cite": "2026:MHC:4385 · C.R.P. Nos. 4064 & 4106 of 2026"}])
cue(type="timeline", t0=S("c05"), t1=E("c05") + 0.05,
    nodes=[{"label": "SUIT 2 · EVIDENCE", "value": "both sides' witnesses", "sub": "and a court witness", "at": A("c05", "examined")},
           {"label": "TRIAL COURT", "value": "no refund at all", "sub": "after the compromise", "at": A("c05", "refused")}])

# ── 3 · the arguments ────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="compare", t0=S("c06"), t1=E("c07") + 0.05, head="Tamil Nadu Court Fees Act · 69-A or 69?", head_at=S("c06") + 0.05,
    cols=[{"title": "The plaintiffs", "icon": "file-text", "at": A("c06", "plaintiffs")}, {"title": "Advocate General · amicus", "icon": "landmark", "at": A("c07", "advocate")}],
    rows=[{"cells": ["M.C. Subramaniam (SC): full refund", "AG: it never considered Afcons"], "cells_at": [A("c06", "subramaniam"), A("c07", "afcons")]},
          {"cells": ["Even for a private settlement", "Amicus: it never dealt with Section 69"], "cells_at": [A("c06", "private"), A("c07", "amicus")]}])

# ── 4 · before the verdict: the LawWorld request ─────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c08"), t1=A("c08", "follow") - 0.05, text="The verdict is next. First, a quick request…", icon="scale", accent=True, at=A("c08", "decided"))
cue(type="list", t0=A("c08", "follow") - 0.05, t1=E("c08") + 0.05, head="Follow LawWorld · lawworld.ai", head_at=A("c08", "follow"),
    items=[{"n": 1, "text": "Search SC and High Court judgments, cited to source", "at": A("c08", "india's")},
           {"n": 2, "text": "Draft petitions, plaints and notices with AI", "at": A("c08", "platform")},
           {"n": 3, "text": "Sign up free · ₹200 AI credit included", "at": A("c08", "advocates")}])

# ── 5 · what the Court held ──────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "under") - 0.05, text="What did the High Court decide?", icon="scale", accent=True, at=A("c09", "finally"))
cue(type="list", t0=A("c09", "under") - 0.05, t1=E("c09") + 0.05, head="Section 69 · Tamil Nadu Court Fees Act", head_at=A("c09", "under"),
    items=[{"n": 1, "text": "The suit settles out of court", "at": A("c09", "suit")},
           {"n": 2, "text": "Before any evidence is recorded", "at": A("c09", "before")},
           {"n": 3, "text": "Only then is the court fee refunded", "at": A("c09", "recorded")}])
cue(type="point", t0=S("c10"), t1=A("c10", "both") - 0.05, text="“A party is not entitled to any refund once evidence is recorded.”", icon="scale", accent=True, at=A("c10", "afcons"))
cue(type="verdicts", t0=A("c10", "both") - 0.05, t1=E("c10") + 0.05,
    rows=[{"text": "Both revision petitions", "ok": False, "at": A("c10", "both")},
          {"text": "Suit 2: no refund, the trial court upheld", "ok": True, "at": A("c10", "failed")},
          {"text": "Suit 1's half refund stays: State didn't challenge", "ok": True, "at": A("c10", "unchallenged")}])

MUSIC = {"file": "audio/bed_mixkit738_140s.mp3", "target_lufs": -21}   # owner 02-11-2026: trending-style royalty-free bed, audible under the voice
