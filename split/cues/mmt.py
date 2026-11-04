# MMTC Limited v. Aust Grain Exports Pty Ltd, FAO(OS) (COMM) 210/2023, High Court of Delhi (Division Bench: Avneesh Jhingan J. wrote
# it, Shail Jain J.; reserved 05.10.2026, pronounced 28.10.2026; "Reportable:- Yes" at the end, page 21): panel cues, run by
# split/build_course_plan.py (helpers: at S E cue fx have r3 PEND).
# HOOK format (split/JUDGMENT_HOOK_FORMAT.md): c01 hook question (spoken to everyone, no "Advocates,"), c02 curiosity, c03 "Hi, I'm
# Ravishankar" + bench, c04-c06 the contract, the shipment, the award, c07 the appeal, c08 the LawWorld request, c09-c10 the verdict.
# Facts (para): Section 37 appeal against the Single Judge's judgment of 12.06.2023 dismissing the Section 34 petition (1); MMTC a
# public sector undertaking; Australian exporter; contract 16.04.2009 for 35,000 MT (+/-10%) of yellow peas at USD 259/MT; shipment
# September-October 2009 (2); extension to 15.11.2009 and 30.11.2009, subject to the contract and penalty (2.1); shipped 27.11.2009,
# arrived 01.01.2010; delay compensation sought under clause 20; PBG invoked 12.01.2010, USD 271,950 appropriated (2.2); majority award
# 05.03.2021, dissent 16.06.2021 (2.4); delay claim rejected, PBG refund allowed, counter-claim 2 (interest on the PBG) rejected "in
# view of clause 13(2)" (2.5); MMTC: dissent after "a gap of 103 days", "two separate awards" (3); 9% interest on the PBG granted in
# the conclusion despite rejecting counter-claim 2 (3.2); clause 13(2) quoted (6); held: "not one of a missing signature" (10); "a
# difference of opinion among the members does not tantamount to the passing of two awards" (11); the majority award "is the decision
# of the tribunal" (12); delay claims rightly rejected (17); in conclusion refund with 9% from 12.01.2010 (18); "contrary to the
# statutory provisions and the terms agreed between the parties" (20); "In the peculiar facts of this case ... the award of interest
# on the PBG is in conflict with the public policy of India" (22); severable (24); appeal partly allowed, award set aside "to the
# limited extent of awarding interest at 9% per annum on the PBG" (25).
# Not on any card: para 19 (the respondent's counsel's concession; Flow policy). The exporter is named on the cite card only. No
# section sign anywhere. List lines <= 52 chars. Bench photos: brand/judges/avneesh_jhingan.jpg, shail_jain.jpg (official
# delhihighcourt.nic.in portraits, as elt).
FORMAT = "hook"   # build_course_plan.py: no opening sting, 15-frame lead (the cover), name tag on the "Ravishankar" clip

def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
ENDCARD = {"title": "No interest in the contract, interest in the award?", "line": "On these facts it conflicted with India's public policy: only the 9% interest on the guarantee is set aside, the rest of the award stands", "sub": "LawWorld: legal research for advocates"}

# ── 1 · no interest, then interest? (hook, curiosity, intro) ─────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "contract"), text="The contract: no interest on the guarantee. The tribunal agrees, then grants it anyway. Can that part stand?", hl="Can that part stand?")
cue(type="list", t0=S("c02"), t1=A("c02", "would") - 0.05, head="One shipment of yellow peas", head_at=S("c02") + 0.05,
    items=[{"n": 1, "text": "Contract: 16 April 2009, an Australian exporter", "at": A("c02", "deal")},
           {"n": 2, "text": "Single Judge: Section 34 challenge dismissed", "at": A("c02", "dismissed")}])
cue(type="point", t0=A("c02", "would") - 0.05, t1=E("c02") + 0.05, text="Will the High Court step in?", icon="search", accent=True, at=A("c02", "step"))
cue(type="bench", t0=S("c03"), t1=E("c03") + 0.05, tag="Delhi High Court · 28 October 2026",
    judges=[{"name": "Justice Avneesh Jhingan", "photo": "../brand/judges/avneesh_jhingan.jpg", "at": A("c03", "honourable")},
            {"name": "Justice Shail Jain", "photo": "../brand/judges/shail_jain.jpg", "at": A("c03", "honourable", 2)}])

# ── 2 · a shipment of yellow peas ────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=S("c04"), t1=E("c04") + 0.05, at=A("c04", "public"), tag="HIGH COURT OF DELHI · 28.10.2026",
    cases=[{"name": "MMTC Limited v. Aust Grain Exports Pty Ltd", "cite": "FAO(OS) (COMM) No. 210 of 2023"}])
cue(type="timeline", t0=S("c04"), t1=E("c04") + 0.05,
    nodes=[{"label": "CONTRACT", "value": "16 Apr 2009", "sub": "35,000 MT yellow peas · USD 259 per MT", "at": A("c04", "contracted")},
           {"label": "SHIPMENT PERIOD", "value": "Sep–Oct 2009", "sub": "from an Australian exporter", "at": A("c04", "october")}])
cue(type="timeline", t0=S("c05"), t1=E("c05") + 0.05,
    nodes=[{"label": "EXTENSION", "value": "to 30 Nov 2009", "sub": "subject to the contract and penalty", "at": A("c05", "extra")},
           {"label": "SHIPPED", "value": "27 Nov 2009", "sub": "delay compensation claimed", "at": A("c05", "compensation")},
           {"label": "GUARANTEE CASHED", "value": "USD 271,950", "sub": "12 Jan 2010 · the exporter's security", "tone": "red", "at": A("c05", "cashed")}])
cue(type="list", t0=S("c06"), t1=A("c06", "citing") - 0.05, head="The majority award · 5 March 2021", head_at=S("c06") + 0.05,
    items=[{"n": 1, "text": "Delay compensation claim: rejected", "at": A("c06", "rejected")},
           {"n": 2, "text": "Bank guarantee: refunded to the exporter", "at": A("c06", "refunded")}])
cue(type="point", t0=A("c06", "citing") - 0.05, t1=E("c06") + 0.05, text="Clause 13(2): “No claim shall be admissible against the Buyer in respect of interest on Performance Guarantee regardless of the time of the release.”", icon="quote", accent=True, at=A("c06", "contract"))

# ── 3 · the appeal ───────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c07"), t1=A("c07", "appeal") - 0.15, text="Yet the conclusion: the guarantee refunded with 9% interest a year from 12.01.2010", icon="info", accent=True, at=A("c07", "conclusion"))
cue(type="list", t0=A("c07", "appeal") - 0.15, t1=E("c07") + 0.05, head="The Section 37 appeal", head_at=A("c07", "appeal"),
    items=[{"n": 1, "text": "9% interest despite clause 13(2)", "at": A("c07", "attacked")},
           {"n": 2, "text": "Dissent signed 103 days after the majority", "at": A("c07", "dissent")}])

# ── 4 · before the verdict: the LawWorld request ─────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c08"), t1=A("c08", "follow") - 0.05, text="The verdict is next. First, a quick request…", icon="scale", accent=True, at=A("c08", "decided"))
cue(type="list", t0=A("c08", "follow") - 0.05, t1=E("c08") + 0.05, head="Follow LawWorld · lawworld.ai", head_at=A("c08", "follow"),
    items=[{"n": 1, "text": "Search SC and High Court judgments, cited to source", "at": A("c08", "india's")},
           {"n": 2, "text": "Draft petitions, plaints and notices with AI", "at": A("c08", "platform")},
           {"n": 3, "text": "Sign up free · ₹200 AI credit included", "at": A("c08", "advocates")}])

# ── 5 · what the Court held ──────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "dissent") - 0.05, text="What did the High Court decide?", icon="scale", accent=True, at=A("c09", "finally"))
cue(type="point", t0=A("c09", "dissent") - 0.05, t1=A("c09", "majority") - 0.05, text="“…a difference of opinion among the members does not tantamount to the passing of two awards.”", icon="quote", accent=True, at=A("c09", "dissent"))
cue(type="point", t0=A("c09", "majority") - 0.05, t1=E("c09") + 0.05, text="Majority award signed by two of three members: the decision of the tribunal (ICA Rule 61)", icon="scale", accent=True, at=A("c09", "signed"))
cue(type="verdicts", t0=S("c10"), t1=E("c10") + 0.05,
    rows=[{"text": "Clause 13(2): no interest on the guarantee", "ok": True, "at": A("c10", "barred")},
          {"text": "On these facts, “in conflict with the public policy of India”", "ok": True, "at": A("c10", "public")},
          {"text": "The 9% interest on the guarantee", "ok": False, "at": A("c10", "part")},
          {"text": "The rest of the award stands", "ok": True, "at": A("c10", "aside")}])

MUSIC = {"file": "audio/bed_mixkit738_140s.mp3", "target_lufs": -21}   # owner 02-11-2026: trending-style royalty-free bed, audible under the voice
