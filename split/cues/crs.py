# C R Sons Infra Projects Ltd v. IRCON International Ltd, FAO(OS) (COMM) 60/2019, High Court of Delhi (Division Bench: Avneesh
# Jhingan J. wrote it (ORAL), Amit Sharma J.; decided 29.10.2026; "Reportable: Yes" at the end, page 8): panel cues, run by
# split/build_course_plan.py (helpers: at S E cue fx have r3 PEND).
# HOOK format (split/JUDGMENT_HOOK_FORMAT.md): c01 hook question (spoken to everyone, no "Advocates,"), c02 curiosity (the cut), c03
# "Hi, I'm Ravishankar" + bench, c04-c05 the contract and the award, c06-c07 both sides, c08 the LawWorld request, c09-c10 the verdict.
# Facts (para): Section 37 appeal against the Single Judge's judgment of 14.12.2018 partly allowing IRCON's Section 34 petition (1);
# corporate office buildings at C-4, District Centre, Saket; LoA 19.07.2004; agreement 17.08.2004 with arbitration (2); award
# 27.02.2018 (2.1); eight claims, partial success in two, cost Rs.5.5 lakhs; claim 1 (work done but not paid): Rs.2,70,25,343 claimed,
# Rs.11,83,921.94 awarded; total Rs.48,71,765.94 (2.2); set aside: Rs.9,28,205 under claim 1 and the Rs.5.5 lakh cost (2.3);
# contractor: the Single Judge exceeded Section 34, substituted a plausible view (3), costs reasoned under Section 31A (3.2); IRCON:
# the arbitrator found the final bill and deductions undisputed yet examined the deductions on merits; Section 31A(3) factors not
# considered (4); held: no pleading challenging the final bill or the deductions; deductions for defects accepted by the contractor;
# the arbitrator went beyond the issue in dispute (7); considered the deductions on merits "acting beyond the referred dispute" (8);
# Section 31A(3) factors not gone into, partial success not considered; costs "vitiated by patent illegality" (9, 10); "No case is
# made out for interference in the impugned judgement. The appeal is dismissed." (12).
# Not on any card: "frivolous" (10). The contractor is named on the cite card only. No section sign anywhere. List lines <= 52 chars.
# Bench photos: brand/judges/avneesh_jhingan.jpg, amit_sharma.jpg (official delhihighcourt.nic.in portraits, as adt).
FORMAT = "hook"   # build_course_plan.py: no opening sting, 15-frame lead (the cover), name tag on the "Ravishankar" clip

def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
ENDCARD = {"title": "Deductions never pleaded: open to re-check?", "line": "No: with no pleading against the final bill, examining each deduction went beyond the dispute; costs ignored Section 31A(3); appeal dismissed", "sub": "LawWorld: legal research for advocates"}

# ── 1 · cuts never challenged? (hook, curiosity, intro) ──────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "claim"), text="Your claim never disputes the deductions for defects. Can the arbitrator still go through each one?", hl="go through each one?")
cue(type="list", t0=S("c02"), t1=A("c02", "will") - 0.05, head="One office contract, one award", head_at=S("c02") + 0.05,
    items=[{"n": 1, "text": "Arbitral award: ₹48,71,765.94, costs included", "at": A("c02", "awarded")},
           {"n": 2, "text": "Set aside: ₹9,28,205 under claim 1, and the costs", "at": A("c02", "cut")}])
cue(type="point", t0=A("c02", "will") - 0.05, t1=E("c02") + 0.05, text="Will the High Court restore them?", icon="search", accent=True, at=A("c02", "restore"))
cue(type="bench", t0=S("c03"), t1=E("c03") + 0.05, tag="Delhi High Court · 29 October 2026",
    judges=[{"name": "Justice Avneesh Jhingan", "photo": "../brand/judges/avneesh_jhingan.jpg", "at": A("c03", "honourable")},
            {"name": "Justice Amit Sharma", "photo": "../brand/judges/amit_sharma.jpg", "at": A("c03", "honourable", 2)}])

# ── 2 · an office at Saket ───────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=S("c04"), t1=E("c04") + 0.05, at=A("c04", "ircon"), tag="HIGH COURT OF DELHI · 29.10.2026",
    cases=[{"name": "C R Sons Infra Projects Ltd v. IRCON International Ltd", "cite": "FAO(OS) (COMM) No. 60 of 2019"}])
cue(type="timeline", t0=S("c04"), t1=E("c04") + 0.05,
    nodes=[{"label": "AGREEMENT", "value": "17 Aug 2004", "sub": "corporate office buildings, Saket", "at": A("c04", "hired")},
           {"label": "ARBITRAL AWARD", "value": "27 Feb 2018", "sub": "arbitration invoked by the contractor", "at": A("c04", "arbitrator")}])
cue(type="list", t0=S("c05"), t1=E("c05") + 0.05, head="The award of 27 February 2018", head_at=S("c05") + 0.05,
    items=[{"n": 1, "text": "8 claims raised: partial success in 2", "at": A("c05", "eight")},
           {"n": 2, "text": "Unpaid work: ₹11,83,921.94 of ₹2,70,25,343", "at": A("c05", "part")},
           {"n": 3, "text": "Costs: ₹5.5 lakh", "at": A("c05", "costs")},
           {"n": 4, "text": "IRCON's Section 34 challenge: claim 1 and costs", "at": A("c05", "challenged")}])

# ── 3 · the appeal ───────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="compare", t0=S("c06"), t1=E("c07") + 0.05, head="The Section 37 appeal", head_at=S("c06") + 0.05,
    cols=[{"title": "The contractor", "icon": "user", "at": A("c06", "contractor")}, {"title": "IRCON", "icon": "landmark", "at": A("c07", "ircon")}],
    rows=[{"cells": ["Single Judge went beyond Section 34", "Bill undisputed, yet deductions examined"], "cells_at": [A("c06", "beyond"), A("c07", "examined")]},
          {"cells": ["Costs were well reasoned (Section 31A)", "Section 31A(3) factors ignored"], "cells_at": [A("c06", "costs"), A("c07", "factors")]}])

# ── 4 · before the verdict: the LawWorld request ─────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c08"), t1=A("c08", "follow") - 0.05, text="The verdict is next. First, a quick request…", icon="scale", accent=True, at=A("c08", "decided"))
cue(type="list", t0=A("c08", "follow") - 0.05, t1=E("c08") + 0.05, head="Follow LawWorld · lawworld.ai", head_at=A("c08", "follow"),
    items=[{"n": 1, "text": "Search SC and High Court judgments, cited to source", "at": A("c08", "india's")},
           {"n": 2, "text": "Draft petitions, plaints and notices with AI", "at": A("c08", "platform")},
           {"n": 3, "text": "Sign up free · ₹200 AI credit included", "at": A("c08", "advocates")}])

# ── 5 · what the Court held ──────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "arbitrator") - 0.05, text="What did the High Court decide?", icon="scale", accent=True, at=A("c09", "finally"))
cue(type="point", t0=A("c09", "arbitrator") - 0.05, t1=E("c09") + 0.05, text="The arbitrator's own finding: no pleading challenging the final bill or its deductions, made for defects the contractor accepted", icon="file-text", accent=True, at=A("c09", "pleading"))
cue(type="verdicts", t0=S("c10"), t1=E("c10") + 0.05,
    rows=[{"text": "Deductions examined on merits: “acting beyond the referred dispute”", "ok": True, "at": A("c10", "beyond")},
          {"text": "Costs ignored Section 31A(3): patent illegality", "ok": True, "at": A("c10", "ignored")},
          {"text": "The contractor's appeal: dismissed", "ok": False, "at": A("c10", "dismissed")}])

MUSIC = {"file": "audio/bed_mixkit738_140s.mp3", "target_lufs": -21}   # owner 02-11-2026: trending-style royalty-free bed, audible under the voice
