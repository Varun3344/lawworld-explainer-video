# M/s Teja Electricals v. The Chief Administrative Officer (Construction), South East Central Railway & Anr., ARBA No. 91 of 2017,
# 2026:CGHC:46107-DB, High Court of Chhattisgarh (Parth Prateem Sahu J. wrote it, Sushma Sawant J.; 30.10.2026, "AFR"): panel cues, run
# by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND). HOOK format (split/JUDGMENT_HOOK_FORMAT.md): c01 hook question,
# c02 curiosity, c03 "Hi, I'm Ravishankar" + bench, c04-c07 facts / case / both sides, c08 the LawWorld request, c09-c10 the verdict.
# Facts from the judgment (Indian Kanoon render, doc 136797738; paras): Section 37 appeal against the Commercial Court (District Level),
# Naya Raipur, 31.10.2017, MJC 31/2016, dismissing the Section 34 application against the award of 12.5.2015 (1); electrification of
# the private siding of M/s Ind Agro Synergy Ltd. at Kotarlia; LoA 04.08.2005; agreement 05.10.2005 (13); Item 3, Special Conditions:
# RITES inspection, "No payment will be made unless the inspection certificate has been submitted along with supplier's original
# challan. The materials have to be procured only from approved sources of RDSO/CORE." (14, 25); on-account up to 85%, balance 15%
# through the final bill (13); not in dispute: 85% paid on account on the test certificates without objection; work completed
# 14.5.2006, completion certificate 25.1.2007; final bill Rs.1,49,33,340, net payable Rs.41,63,602 (15); manufacturer's test
# certificate demanded, letter 06.06.2008 (2; award para 6.3 at 19); reports by M/s Unique Structure & Tower Ltd., Raipur, which only
# galvanised the masts; no original challan of the manufacturer; final bill withheld (15, 27, 28); claim Rs.1,00,11,599 (18); award
# dismissed the claim: contract not completed as per its conditions (16); Commercial Court upheld it (16, 21); the contractor: CORE
# letter 03.12.2014 (Unique Structure and Shri Bajrang Alloys CORE-approved), RITES certificate, 85% released on similar certificates
# (3, 4); the Railway: no re-appreciation under Section 37; on-account and final payment distinct stages (8-10). Held: no
# re-appreciation of evidence under Section 37 (22); approved sources "an essential contractual obligation and not a mere procedural
# formality"; the galvanising agency's reports cannot by themselves prove the source (28, 29); a finding of fact, not perverse (30);
# not against the fundamental policy of Indian law (31); on-account payment "cannot be construed as an acknowledgment of complete
# contractual compliance" (32); Item 3 reading "a plausible and reasonable interpretation" (34); appeal dismissed (44).
# Not on any card: the Railway Board's ban on the appellant and the Rs.32.11 lakh recovery (award paras 6.8, 6.10 at 19: the Railway's
# allegations); the proprietor's name; the "genuineness" doubt.
# No section sign anywhere. List lines <= 52 chars. Official highcourt.cg.gov.in portraits on the bench card.
FORMAT = "hook"   # build_course_plan.py: no opening sting, 15-frame lead (the cover), name tag on the "Ravishankar" clip

def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
ENDCARD = {"title": "85% paid on account: can the Railway hold back the rest?", "line": "An on-account payment is no proof of full compliance · the award stands, the contractor's appeal dismissed", "sub": "LawWorld: legal research for advocates"}

# ── 1 · can the Railway hold back? (hook, curiosity, intro) ─────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "railway"), text="The Railway paid 85% on account, against the contractor's test certificates. Can it still hold back the final payment?", hl="hold back the final payment?")
cue(type="list", t0=S("c02"), t1=A("c02", "can") - 0.05, head="Work done, claim lost twice", head_at=S("c02") + 0.05,
    items=[{"n": 1, "text": "Work completed: 14 May 2006 · certificate issued", "at": A("c02", "certified")},
           {"n": 2, "text": "Arbitrator: claim dismissed · 12 May 2015", "at": A("c02", "arbitrator")},
           {"n": 3, "text": "Commercial Court, Naya Raipur: award upheld", "at": A("c02", "commercial")}])
cue(type="point", t0=A("c02", "can") - 0.05, t1=E("c02") + 0.05, text="Can a Section 37 appeal change that?", icon="search", accent=True, at=A("c02", "appeal"))
cue(type="bench", t0=S("c03"), t1=E("c03") + 0.05, tag="Chhattisgarh High Court · 30 October 2026",
    judges=[{"name": "Justice Parth Prateem Sahu", "photo": "../brand/judges/parth_prateem_sahu.jpg", "at": A("c03", "honourable")},
            {"name": "Justice Sushma Sawant", "photo": "../brand/judges/sushma_sawant.jpg", "at": A("c03", "honourable", 2)}])

# ── 2 · the contract ────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=S("c04"), t1=E("c05") + 0.05, at=A("c04", "railway"), tag="HIGH COURT OF CHHATTISGARH · 30.10.2026",
    cases=[{"name": "M/s Teja Electricals v. Chief Administrative Officer (Construction), South East Central Railway", "cite": "2026:CGHC:46107-DB · ARBA No. 91 of 2017"}])
cue(type="timeline", t0=S("c04"), t1=E("c04") + 0.05,
    nodes=[{"label": "LETTER OF ACCEPTANCE", "value": "4 August 2005", "sub": "electrifying a private siding at Kotarlia", "at": A("c04", "hired")},
           {"label": "ITEM 3 · SPECIAL CONDITIONS", "value": "approved sources", "sub": "“procured only from approved sources of RDSO/CORE”", "at": A("c04", "materials")}])
cue(type="counters", t0=S("c05"), t1=E("c05") + 0.05, head="Work completed: 14 May 2006", head_at=A("c05", "completed"),
    items=[{"value": 85, "unit": "%", "label": "Paid on account", "sub": "against the test certificates", "at": A("c05", "eighty")},
           {"value": 41, "unit": "₹ LAKH", "label": "Left on the final bill", "sub": "₹41,63,602 net of on-account payments", "tone": "red", "at": A("c05", "balance")}])

# ── 3 · the withheld bill (tall cards: no cite bar) ─────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c06"), t1=E("c06") + 0.05, head="Processing the final bill", head_at=S("c06") + 0.05,
    steps=[{"label": "Maker's test certificates", "sub": "sought for the steel masts · 6 June 2008", "icon": "file-text", "at": A("c06", "asked")},
           {"label": "Reports from the galvaniser", "sub": "it galvanised the masts, did not make them", "icon": "search", "at": A("c06", "reports")},
           {"label": "Final bill withheld", "sub": "no original challan of the manufacturer", "icon": "x", "tone": "muted", "at": A("c06", "bill")}])
cue(type="compare", t0=S("c07"), t1=E("c07") + 0.05, head="Before the appeal bench", head_at=S("c07") + 0.05,
    cols=[{"title": "The contractor", "icon": "user", "at": A("c07", "contractor")}, {"title": "The Railway", "icon": "landmark", "at": A("c07", "railway")}],
    rows=[{"cells": ["CORE letter, 2014: the sources are approved", "Section 37: no re-appreciation of evidence"], "cells_at": [A("c07", "confirmed"), A("c07", "section")]},
          {"cells": ["85% was paid on similar certificates", "On-account and final bill: distinct stages"], "cells_at": [A("c07", "payment"), A("c07", "reweigh")]}])

# ── 4 · before the verdict: the LawWorld request ────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c08"), t1=A("c08", "follow") - 0.05, text="The verdict is next. First, a quick request…", icon="scale", accent=True, at=A("c08", "decided"))
cue(type="list", t0=A("c08", "follow") - 0.05, t1=E("c08") + 0.05, head="Follow LawWorld · lawworld.ai", head_at=A("c08", "follow"),
    items=[{"n": 1, "text": "Search SC and High Court judgments, cited to source", "at": A("c08", "india's")},
           {"n": 2, "text": "Draft petitions, plaints and notices with AI", "at": A("c08", "platform")},
           {"n": 3, "text": "Sign up free · ₹200 AI credit included", "at": A("c08", "advocates")}])

# ── 5 · what the Court held ─────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "an") - 0.05, text="What did the High Court decide?", icon="scale", accent=True, at=A("c09", "finally"))
cue(type="list", t0=A("c09", "an") - 0.05, t1=E("c09") + 0.05, head="Section 37: a narrow window", head_at=A("c09", "an"),
    items=[{"n": 1, "text": "Approved RDSO/CORE source: an essential term", "at": A("c09", "essential")},
           {"n": 2, "text": "Galvaniser's reports alone do not prove the source", "at": A("c09", "formality")},
           {"n": 3, "text": "Arbitrator's reading of Item 3: a plausible view", "at": A("c09", "plausible")}])
cue(type="point", t0=S("c10"), t1=A("c10", "award") - 0.05, text="An on-account payment “cannot be construed as an acknowledgment of complete contractual compliance”", icon="scale", accent=True, at=A("c10", "acknowledgment"))
cue(type="verdicts", t0=A("c10", "award") - 0.05, t1=E("c10") + 0.05,
    rows=[{"text": "The award: not perverse, no patent illegality", "ok": True, "at": A("c10", "perverse")},
          {"text": "The contractor's Section 37 appeal", "ok": False, "at": A("c10", "contractor's"), "strike_at": A("c10", "dismissed")}])

MUSIC = {"file": "audio/bed_mixkit738_140s.mp3", "target_lufs": -21}   # owner 02-11-2026: trending-style royalty-free bed, audible under the voice
