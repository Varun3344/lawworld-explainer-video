# State of U.P. & Ors. v. M/s Apex Construction Company, Mathura & Anr., Appeal u/s 37 Arbitration Act No. 62 of 2023,
# 2026:AHC-LKO:76453-DB, Allahabad High Court, Lucknow (Arun Bhansali CJ., Jaspreet Singh J. wrote it; delivered 24.10.2026, AFR):
# panel cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND). HOOK format (split/JUDGMENT_HOOK_FORMAT.md):
# c01 hook question, c02 curiosity, c03 "Hi, I'm Ravishankar" + bench, c04-c07 facts / case / both sides, c08 the LawWorld request,
# c09-c10 the verdict. No title sting.
# Facts from the judgment (paras): appeal u/s 37 against Commercial Court No. 1, Lucknow, 09.02.2023, Section 34 petition dismissed,
# award of 30.07.2017 upheld (1, 15); widening and strengthening of the Raya-Math Road, District Mathura (2, 3); contract awarded
# 30.09.2008 (4); work completed 31.08.2009 (5, 54(b)); claim Rs.23,79,90,727 with 18% quarterly rest (7); final bill "false and
# misleading", Rs.1,56,79,034.65 allowed on the revised claim (11, 50); costs Rs.10 lakh (63); 14% from 01.09.2009 compounded
# annually till realisation (63, 64, 74); the State: no completion certificate under Clause 48.1, so the work was incomplete (17-19);
# contract silent on interest; Interest Act s.3(3)(c) bars interest upon interest; a tribunal is a "court" (23-25); the contractor:
# s.31(7) gives the power (35); banks charge interest with quarterly rest (39). Held: no notice, complaint or correspondence on
# defects (54(c)); CRRI / PWD reports: no finding of incomplete or substandard work (54(d)); no certificate does not mean the work
# was incomplete (55, 56); s.31(7) attracted, power for both periods (72, 80-82); no compound interest without a contract
# stipulation (75, 86); s.2(a) + s.3(3)(c) Interest Act, annual rest = interest upon interest (77-79); 14% simple from 01.09.2009 to
# 31.01.2016, then 14% simple on the crystallised sum till payment (87, 92); Rs.1,39,619 deduction at 14% simple (88); only the
# interest modified, Gayatri Balasamy (89-92); other findings affirmed (93); appeal partly allowed, no costs (94).
# No section sign anywhere. List lines <= 52 chars. Official allahabadhighcourt.in portraits on the bench card.
FORMAT = "hook"   # build_course_plan.py: no opening sting, 15-frame lead (the cover), name tag on the "Ravishankar" clip

def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
ENDCARD = {"title": "Can a tribunal compound interest the contract never mentions?", "line": "No: yearly compounding is interest upon interest · 14% simple interest instead", "sub": "LawWorld: legal research for advocates"}

# ── 1 · can the tribunal compound? (hook, curiosity, intro) ─────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "contract"), text="If the contract says nothing about interest, can an arbitral tribunal still compound it every year?", hl="compound it every year?")
cue(type="list", t0=S("c02"), t1=A("c02", "two") - 0.05, head="The State's two objections", head_at=S("c02") + 0.05,
    items=[{"n": 1, "text": "No completion certificate was ever issued", "at": A("c02", "completion")},
           {"n": 2, "text": "Yearly compounding, with no contract clause", "at": A("c02", "fourteen")}])
cue(type="point", t0=A("c02", "two") - 0.05, t1=E("c02") + 0.05, text="Two objections. Which one survives?", icon="search", accent=True, at=A("c02", "objections"))
cue(type="bench", t0=S("c03"), t1=E("c03") + 0.05, tag="Allahabad High Court · 24 October 2026",
    judges=[{"name": "Chief Justice Arun Bhansali", "photo": "../brand/judges/arun_bhansali.jpg", "at": A("c03", "honourable")},
            {"name": "Justice Jaspreet Singh", "photo": "../brand/judges/jaspreet_singh.jpg", "at": A("c03", "honourable", 2)}])

# ── 2 · the road contract ───────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c04"), t1=E("c04") + 0.05, head="The road contract", head_at=S("c04") + 0.05,
    steps=[{"label": "PWD hires a contractor", "sub": "contract of 30 September 2008", "icon": "landmark", "at": A("c04", "hired")},
           {"label": "Widen the Raya-Math Road", "sub": "District Mathura · 11.8 km built", "icon": "file-text", "at": A("c04", "widen")},
           {"label": "Work completed", "sub": "31 August 2009, on the record", "icon": "check", "at": A("c04", "completed")}])
cue(type="cite", t0=S("c05"), t1=E("c06") + 0.05, at=A("c05", "contractor"), tag="HIGH COURT OF JUDICATURE AT ALLAHABAD, LUCKNOW · 24.10.2026",
    cases=[{"name": "State of U.P. & Ors. v. M/s Apex Construction Company & Anr.", "cite": "2026:AHC-LKO:76453-DB · Section 37 Appeal No. 62 of 2023"}])
cue(type="timeline", t0=S("c05"), t1=E("c05") + 0.05,
    nodes=[{"label": "THE CLAIM", "value": "₹23.8 crore", "sub": "with 18% interest, quarterly rests", "at": A("c05", "claimed")},
           {"label": "THE FINAL BILL", "value": "rejected", "sub": "the tribunal went by the revised claim", "tone": "stop", "at": A("c05", "rejected")},
           {"label": "THE AWARD", "value": "₹1.57 crore", "sub": "+ ₹10 lakh costs · 30 July 2017", "at": A("c05", "awarded")}])

# ── 3 · two objections ──────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="timeline", t0=S("c06"), t1=E("c06") + 0.05,
    nodes=[{"label": "COMMERCIAL COURT", "value": "award upheld", "sub": "Lucknow · Section 34 petition dismissed", "at": A("c06", "upheld")},
           {"label": "SECTION 37 APPEAL", "value": "the State", "sub": "to the High Court", "at": A("c06", "appeal")},
           {"label": "OBJECTION ONE", "value": "no certificate", "sub": "Clause 48.1: so the work was incomplete?", "tone": "stop", "at": A("c06", "certificate")}])
cue(type="compare", t0=S("c07"), t1=E("c07") + 0.05, head="Objection two: the interest", head_at=S("c07") + 0.05,
    cols=[{"title": "The State", "icon": "landmark", "at": A("c07", "state")}, {"title": "The contractor", "icon": "user", "at": A("c07", "contractor")}],
    rows=[{"cells": ["The contract is silent on interest", "Section 31(7) gives the power"], "cells_at": [A("c07", "silent"), A("c07", "replied")]},
          {"cells": ["Interest Act: no interest upon interest", "Banks compound every quarter"], "cells_at": [A("c07", "bars"), A("c07", "quarter")]}])

# ── 4 · before the verdict: the LawWorld request ────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c08"), t1=A("c08", "follow") - 0.05, text="The verdict is next. First, a quick request…", icon="scale", accent=True, at=A("c08", "decided"))
cue(type="list", t0=A("c08", "follow") - 0.05, t1=E("c08") + 0.05, head="Follow LawWorld · lawworld.ai", head_at=A("c08", "follow"),
    items=[{"n": 1, "text": "Search SC and High Court judgments, cited to source", "at": A("c08", "india's")},
           {"n": 2, "text": "Draft petitions, plaints and notices with AI", "at": A("c08", "platform")},
           {"n": 3, "text": "Sign up free · ₹200 AI credit included", "at": A("c08", "advocates")}])

# ── 5 · what the Court held ─────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "missing") - 0.05, text="What did the High Court decide?", icon="scale", accent=True, at=A("c09", "finally"))
cue(type="notequal", t0=A("c09", "missing") - 0.05, t1=E("c09") + 0.05, left="No completion certificate", right="work incomplete",
    at=A("c09", "mean"), left_at=A("c09", "missing"), sub="The State never put the contractor on notice of any defect", sub_at=A("c09", "notice"))
cue(type="list", t0=S("c10"), t1=A("c10", "so") - 0.05, head="Interest Act, 1978 · Arbitration Act", head_at=S("c10") + 0.05,
    items=[{"n": 1, "text": "Section 2(a): “court” includes an arbitrator", "at": A("c10", "held")},
           {"n": 2, "text": "Section 3(3)(c): no interest upon interest", "at": A("c10", "upon")},
           {"n": 3, "text": "Compounding only if the contract provides it", "at": A("c10", "clause")}])
cue(type="verdicts", t0=A("c10", "so") - 0.05, t1=E("c10") + 0.05,
    rows=[{"text": "Interest compounded every year: struck off", "ok": False, "at": A("c10", "modified")},
          {"text": "14% simple to 31.01.2016, then 14% simple on that sum till payment", "ok": True, "at": A("c10", "fourteen")},
          {"text": "Appeal partly allowed · every other finding stands", "ok": True, "at": A("c10", "simple")}])

MUSIC = {"file": "audio/bed_mixkit738_140s.mp3", "target_lufs": -21}   # owner 02-11-2026: trending-style royalty-free bed, audible under the voice
