# Chief Electoral Officer & Anr. v. M/s Mahlakshmi Light House, FAO(OS)(COMM) 43/2018, High Court of Delhi (Division Bench: Avneesh
# Jhingan J. wrote it, Shail Jain J.; reserved 13.10.2026, pronounced 28.10.2026; "Reportable:- Yes" at the end, page 8): panel cues,
# run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND).
# HOOK format (split/JUDGMENT_HOOK_FORMAT.md): c01 hook question (spoken to everyone, no "Advocates,"), c02 curiosity, c03 "Hi, I'm
# Ravishankar" + bench, c04-c06 the contract, the bills, the award, c07 both sides, c08 the LawWorld request, c09-c10 the verdict.
# Facts (para): Section 37 appeal against the Single Judge's decision of 02.05.2017 dismissing the Section 34 objections (1); tenders
# for tentage, furniture and electrical items on hire for the 1999 Lok Sabha elections; work for Karol Bagh and Outer Delhi awarded on
# 09.08.1999 (2); bills Rs.19,98,426 (Karol Bagh) and Rs.80,30,654 (Outer Delhi); the appellants alleged them inflated; clause 19:
# physical verification of the tentage before dismantling (2.1, 6, 7); the arbitrator allowed the claims: Rs.1,00,28,788, interest @9%
# on Rs.15,22,772 from February 2000, post-award interest @9% if unpaid in two months, costs Rs.2,00,000 (2.2); Single Judge dismissed
# the objections and upheld the award (2.3); appellants: the Finance Department's objections ignored, patent illegality, perversity
# (3.1); respondent: never pressed under Section 34, plausible view (4), goods physically verified by the RO (4.1); held: "The issues
# not raised under Section 34 of the Act cannot be permitted to be raised in the appeal under Section 37 of the Act." (11); the
# contention that the arbitrator ignored the Finance Department's objections "is misconceived" (12); verification by the RO before
# dismantling, scrutiny only from July 2000 (13); inquiry reports "much later, after dismantling"; quantum of evidence is the
# arbitrator's exclusive domain (14); "the view taken by the arbitrator is plausible, suffers from no factual or legal error, much
# less perversity and calls for no interference" (16); "the appeal is dismissed" (17). Not on any card: officials' / witnesses' names
# (12-15), "bogus bills" (10, a party's submission), "admitted" (8). The firm is named on the cite card only, as spelt in the cause
# title ("Mahlakshmi"). No section sign anywhere. List lines <= 52 chars.
# Bench photos: brand/judges/avneesh_jhingan.jpg, shail_jain.jpg (official delhihighcourt.nic.in portraits).
FORMAT = "hook"   # build_course_plan.py: no opening sting, 15-frame lead (the cover), name tag on the "Ravishankar" clip

def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
ENDCARD = {"title": "Election tents: whose check counts?", "line": "The arbitrator trusted the Returning Officer's on-site check: a plausible view, so the award stands and the appeal is dismissed", "sub": "LawWorld: legal research for advocates"}

# ── 1 · whose check counts? (hook, curiosity, intro) ─────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "tents"), text="Checked on site before the tents came down. Later, the bills are called inflated. Whose check counts?", hl="Whose check counts?")
cue(type="list", t0=S("c02"), t1=A("c02", "will") - 0.05, head="One election, a long dispute", head_at=S("c02") + 0.05,
    items=[{"n": 1, "text": "Lok Sabha election: 1999", "at": A("c02", "began")},
           {"n": 2, "text": "Arbitral award: about ₹1 crore", "at": A("c02", "arbitrator")}])
cue(type="point", t0=A("c02", "will") - 0.05, t1=E("c02") + 0.05, text="Will the award stand?", icon="search", accent=True, at=A("c02", "will"))
cue(type="bench", t0=S("c03"), t1=E("c03") + 0.05, tag="Delhi High Court · 28 October 2026",
    judges=[{"name": "Justice Avneesh Jhingan", "photo": "../brand/judges/avneesh_jhingan.jpg", "at": A("c03", "honourable")},
            {"name": "Justice Shail Jain", "photo": "../brand/judges/shail_jain.jpg", "at": A("c03", "honourable", 2)}])

# ── 2 · tents for two seats ──────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=S("c04"), t1=E("c04") + 0.05, at=A("c04", "election"), tag="HIGH COURT OF DELHI · 28.10.2026",
    cases=[{"name": "Chief Electoral Officer & Anr. v. M/s Mahlakshmi Light House", "cite": "FAO(OS)(COMM) No. 43 of 2018"}])
cue(type="timeline", t0=S("c04"), t1=E("c04") + 0.05,
    nodes=[{"label": "WORK AWARDED", "value": "9 Aug 1999", "sub": "tentage, furniture, electrical items on hire", "at": A("c04", "hired")},
           {"label": "TWO CONSTITUENCIES", "value": "Karol Bagh", "sub": "and Outer Delhi", "at": A("c04", "karol")}])
cue(type="point", t0=S("c05"), t1=A("c05", "bills") - 0.05, text="Clause 19: the Returning Officer checks the tentage before dismantling; the bills need the competent authority's approval", icon="file-text", accent=True, at=A("c05", "contract"))
cue(type="list", t0=A("c05", "bills") - 0.05, t1=E("c05") + 0.05, head="The contractor's bills", head_at=A("c05", "bills"),
    items=[{"n": 1, "text": "Karol Bagh: ₹19,98,426", "at": A("c05", "came", 2)},
           {"n": 2, "text": "Outer Delhi: ₹80,30,654", "at": A("c05", "crore")},
           {"n": 3, "text": "The electoral office: “inflated”", "at": A("c05", "electoral")}])
cue(type="timeline", t0=S("c06"), t1=E("c06") + 0.05,
    nodes=[{"label": "ARBITRAL AWARD", "value": "₹1,00,28,788", "sub": "claims in full · ₹2 lakh costs", "at": A("c06", "allowed")},
           {"label": "SINGLE JUDGE", "value": "2 May 2017", "sub": "Section 34 objections dismissed", "at": A("c06", "single")}])

# ── 3 · the appeal ───────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="compare", t0=S("c07"), t1=E("c07") + 0.05, head="The Section 37 appeal", head_at=S("c07") + 0.05,
    cols=[{"title": "The electoral office", "icon": "landmark", "at": A("c07", "office")}, {"title": "The contractor", "icon": "user", "at": A("c07", "contractor")}],
    rows=[{"cells": ["Finance objections ignored", "Never pressed under Section 34"], "cells_at": [A("c07", "ignored"), A("c07", "pressed")]},
          {"cells": ["Patent illegality, perversity", "Goods verified by the Returning Officers"], "cells_at": [A("c07", "objections"), A("c07", "single")]}])

# ── 4 · before the verdict: the LawWorld request ─────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c08"), t1=A("c08", "follow") - 0.05, text="The verdict is next. First, a quick request…", icon="scale", accent=True, at=A("c08", "decided"))
cue(type="list", t0=A("c08", "follow") - 0.05, t1=E("c08") + 0.05, head="Follow LawWorld · lawworld.ai", head_at=A("c08", "follow"),
    items=[{"n": 1, "text": "Search SC and High Court judgments, cited to source", "at": A("c08", "india's")},
           {"n": 2, "text": "Draft petitions, plaints and notices with AI", "at": A("c08", "platform")},
           {"n": 3, "text": "Sign up free · ₹200 AI credit included", "at": A("c08", "advocates")}])

# ── 5 · what the Court held ──────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "issues") - 0.05, text="What did the High Court decide?", icon="scale", accent=True, at=A("c09", "finally"))
cue(type="point", t0=A("c09", "issues") - 0.05, t1=A("c09", "and") - 0.05, text="“The issues not raised under Section 34 of the Act cannot be permitted to be raised in the appeal under Section 37 of the Act.”", icon="quote", accent=True, at=A("c09", "issues"))
cue(type="point", t0=A("c09", "and") - 0.05, t1=E("c09") + 0.05, text="That the arbitrator ignored the Finance Department's objections: “misconceived”", icon="scale", accent=True, at=A("c09", "finance"))
cue(type="timeline", t0=S("c10"), t1=A("c10", "weighing") - 0.05,
    nodes=[{"label": "RETURNING OFFICER", "value": "verified on site", "sub": "before the structures came down", "at": A("c10", "checked")},
           {"label": "FINANCE SCRUTINY", "value": "July 2000", "sub": "inquiry reports much later, after dismantling", "tone": "red", "at": A("c10", "inquiry")}])
cue(type="verdicts", t0=A("c10", "weighing") - 0.05, t1=E("c10") + 0.05,
    rows=[{"text": "Weighing the evidence: the arbitrator's domain", "ok": True, "at": A("c10", "arbitrator's")},
          {"text": "The office's plea: patent illegality, perversity", "ok": False, "at": A("c10", "plausible")},
          {"text": "Appeal dismissed: the award stands", "ok": True, "at": A("c10", "dismissed")}])

MUSIC = {"file": "audio/bed_mixkit738_140s.mp3", "target_lufs": -21}   # owner 02-11-2026: trending-style royalty-free bed, audible under the voice
