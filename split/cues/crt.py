# Anisha Busa v. SIBAR Institute of Dental Sciences & Anr., W.P. No. 15274 of 2020, 2026:APHC:46012, High Court of Andhra Pradesh at
# Amaravati (Harinath N. J., order 28.10.2026; "LR COPY" endorsed on pp.10-11 = marked to the Law Reporters): panel cues, run by
# split/build_course_plan.py (helpers: at S E cue fx have r3 PEND). HOOK format (split/JUDGMENT_HOOK_FORMAT.md): c01 hook question
# (spoken to everyone, no "Advocates,"), c02 curiosity, c03 "Hi, I'm Ravishankar" + bench, c04-c05 the seat and the illness, c06-c07
# the college's case and the University's stand, c08 the LawWorld request, c09-c10 the verdict.
# Facts from the order (para): retention of her original certificates and a demand for the entire course fee, Rs.5,46,978 a year,
# for their release (1); NEET 2019, BDS seat in R2's (the University's) counselling, originals given to R2 and forwarded to the
# college (2); leg complications after an operation, could not join; letter 17.12.2019 and legal notice 16.03.2020 seeking them back
# (3); the college's counter: private unaided, writ not maintainable (5); returns them only if she pays the entire course fee of
# Rs.21,96,000 with other fees and the cancellation fee; a voluntary drop-out cannot deprive it of the fee (6); G.O.Ms. No.72 of
# 15.07.2019: BDS discontinuation fee Rs.1,00,000 + GST to the University (7); R2's Standing Counsel: the full-fee demand is not
# permissible under the UGC guidelines and regulations (8); UGC notification of October 2018 (11), the claim "evidently contrary" to
# it (12), cl. 4.2.2 return originals immediately after verification (14), cl. 4.2.4 institutional custody "strictly prohibited"
# (16); held: certificates are the student's property, Article 21, no lien, withholding not permissible as a mode of recovery, the
# remedy lies elsewhere (18); writ petition allowed, return within one week of receipt of the order (19).
# Names: the cause title only on the cite card; nobody is accused. The maintainability plea is not shown as rejected (not discussed).
# List lines <= 52 chars. Bench photo: brand/judges/harinath_nunepally.jpg (official aphc.gov.in "Profiles" portrait, 20092024174932.webp).
FORMAT = "hook"   # build_course_plan.py: no opening sting, 15-frame lead (the cover), name tag on the "Ravishankar" clip

def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
ENDCARD = {"title": "Can a college hold certificates for fees?", "line": "No: they are the student's property and no institution has a lien over them · returned within a week", "sub": "LawWorld: legal research for advocates"}

# ── 1 · certificates held for fees? (hook, curiosity, intro) ────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "college"), text="Got a seat, couldn't join. Can the college keep your original certificates until you pay the entire course fee?", hl="keep your original certificates")
cue(type="list", t0=S("c02"), t1=A("c02", "was") - 0.05, head="One seat, one demand", head_at=S("c02") + 0.05,
    items=[{"n": 1, "text": "Certificates back only for the whole course fee", "at": A("c02", "return")},
           {"n": 2, "text": "₹21,96,000 plus other fees, the college says", "at": A("c02", "lakh")},
           {"n": 3, "text": "She never joined the course", "at": A("c02", "never")}])
cue(type="point", t0=A("c02", "was") - 0.05, t1=E("c02") + 0.05, text="Was that lawful?", icon="search", accent=True, at=A("c02", "lawful"))
cue(type="bench", t0=S("c03"), t1=E("c03") + 0.05, tag="Andhra Pradesh High Court · 28 October 2026",
    judges=[{"name": "Justice Harinath N.", "photo": "../brand/judges/harinath_nunepally.jpg", "at": A("c03", "honourable")}])

# ── 2 · the seat and the surgery ────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=S("c04"), t1=E("c05") + 0.05, at=A("c04", "took"), tag="HIGH COURT OF ANDHRA PRADESH · 28.10.2026",
    cases=[{"name": "A BDS student v. SIBAR Institute of Dental Sciences & Anr.", "cite": "2026:APHC:46012 · W.P. No. 15274 of 2020"}])
cue(type="timeline", t0=S("c04"), t1=E("c04") + 0.05,
    nodes=[{"label": "NEET 2019", "value": "BDS seat", "sub": "Dr. NTR University of Health Sciences counselling", "at": A("c04", "neet")},
           {"label": "HER ORIGINALS", "value": "to the college", "sub": "SSC, Intermediate, transfer, migration…", "at": A("c04", "original")}])
cue(type="timeline", t0=S("c05"), t1=E("c05") + 0.05,
    nodes=[{"label": "AFTER A LEG OPERATION", "value": "could not join", "sub": "post-operation complications, she says", "at": A("c05", "complications")},
           {"label": "SHE ASKS FOR THEM", "value": "letter · legal notice", "sub": "17.12.2019 · 16.03.2020", "at": A("c05", "wrote")}])

# ── 3 · the college's case ──────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="list", t0=S("c06"), t1=E("c06") + 0.05, head="The college's counter", head_at=S("c06") + 0.05,
    items=[{"n": 1, "text": "Private and unaided: no writ lies against it", "at": A("c06", "private")},
           {"n": 2, "text": "A voluntary drop-out can't deny it the course fee", "at": A("c06", "voluntarily")}])
cue(type="compare", t0=S("c07"), t1=E("c07") + 0.05, head="Fee first, certificates later?", head_at=S("c07") + 0.05,
    cols=[{"title": "The college", "icon": "landmark", "at": A("c07", "cited")}, {"title": "The University's counsel", "icon": "scale", "at": A("c07", "university's")}],
    rows=[{"cells": ["G.O.Ms. No. 72: a BDS discontinuation fee", "The full-fee demand is not permissible"], "cells_at": [A("c07", "order"), A("c07", "agreed")]},
          {"cells": ["₹1 lakh + GST, payable to the University", "Under the UGC guidelines and regulations"], "cells_at": [A("c07", "discontinuation"), A("c07", "guidelines")]}])

# ── 4 · before the verdict: the LawWorld request ────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c08"), t1=A("c08", "follow") - 0.05, text="The verdict is next. First, a quick request…", icon="scale", accent=True, at=A("c08", "decided"))
cue(type="list", t0=A("c08", "follow") - 0.05, t1=E("c08") + 0.05, head="Follow LawWorld · lawworld.ai", head_at=A("c08", "follow"),
    items=[{"n": 1, "text": "Search SC and High Court judgments, cited to source", "at": A("c08", "india's")},
           {"n": 2, "text": "Draft petitions, plaints and notices with AI", "at": A("c08", "platform")},
           {"n": 3, "text": "Sign up free · ₹200 AI credit included", "at": A("c08", "advocates")}])

# ── 5 · what the Court held ─────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "twenty") - 0.05, text="What did the High Court decide?", icon="scale", accent=True, at=A("c09", "finally"))
cue(type="list", t0=A("c09", "twenty") - 0.05, t1=E("c09") + 0.05, head="UGC notification · October 2018", head_at=A("c09", "twenty"),
    items=[{"n": 1, "text": "Cl. 4.2.2: verify originals, return them at once", "at": A("c09", "notification")},
           {"n": 2, "text": "Cl. 4.2.4: institutional custody strictly barred", "at": A("c09", "strictly")},
           {"n": 3, "text": "The full-course-fee demand: evidently contrary", "at": A("c09", "keeping")}])
cue(type="point", t0=S("c10"), t1=A("c10", "any") - 0.05, text="“Original academic certificates are the property of the student.” “An institution has no lien over them.”", icon="quote", accent=True, at=A("c10", "certificates"))
cue(type="verdicts", t0=A("c10", "any") - 0.05, t1=E("c10") + 0.05,
    rows=[{"text": "Withholding certificates to recover fees", "ok": False, "at": A("c10", "any")},
          {"text": "Fee claim, if any: the remedy lies elsewhere", "ok": True, "at": A("c10", "elsewhere")},
          {"text": "Writ allowed: return within a week of receipt", "ok": True, "at": A("c10", "returned")}])

MUSIC = {"file": "audio/bed_mixkit738_140s.mp3", "target_lufs": -21}   # owner 02-11-2026: trending-style royalty-free bed, audible under the voice
