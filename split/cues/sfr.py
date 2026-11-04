# Perumalla Kasi Rao v. Nukala Muralikrishna & Ors., A.S. Nos. 82, 83 and 84 of 2013 (common judgment), 2026:APHC:47171 / 47170 /
# 47172, High Court of Andhra Pradesh at Amaravati (Division Bench: D. Ramesh J. and Alapati Giridhar J., who wrote it; pronounced
# 03.11.2026; "LR copy to be marked" on p.54 = marked to the Law Reporters): panel cues, run by split/build_course_plan.py (helpers: at
# S E cue fx have r3 PEND). HOOK format (split/JUDGMENT_HOOK_FORMAT.md): c01 hook question (spoken to everyone, no "Advocates,"), c02
# curiosity, c03 "Hi, I'm Ravishankar" + bench, c04-c05 the handwritten deal and the sale to others, c06-c07 the rejection pleas and
# the buyer's reply, c08 the LawWorld request, c09-c10 the verdict.
# Facts from the judgment (para): appeals against the VI Additional District Judge, Markapur, order of 15.02.2012 allowing petitions to
# reject the plaint under Order VII Rule 11 CPC in O.S. No. 43 of 2011, a suit for specific performance of an agreement of sale of
# 06.01.2010 (1); D1 wrote the terms in her own hand and signed, for herself and D2-D4, the plaint says (11, 36); nine documents of
# 20.08.2010 in favour of D5-D9 (15); the I.A.s of all the defendants (19): no executant / beneficiary, no description of the property
# (21), white paper, stamp duty (22), only terms for a later agreement, an agreement to agree is unenforceable (23), no written
# authority (25); the buyer: D1 never denied her handwriting or the Rs.5 lakh (4, 6); only the plaint and its documents, no
# mini-trial (30); recitals: 47.50 acres, Rs.2,38,00,000, 25% with Rs.5,00,000 advance on 06.01.2010, balance in four months (34, 70);
# all the essential ingredients; handwriting, advance and signature not disputed (35, 60, 67); disputed points for trial (45, 51, 57,
# 63, 66); prima facie all essential terms, subject to proof after trial (73); the trial court relied on the principle without the
# contents (75); "a drastic power" (77); ~16 years without trial (85); rejection "not sustainable" (90); stamp duty etc. at the
# appropriate stage (98); appeals allowed with costs, no view on the merits (101); balance sale consideration in fixed deposits within
# 10 days, else leave to alienate under S. 52 T.P. Act (102); suit to be disposed of preferably within 6 months (103).
# Names: the lead cause title only on the cite card; nobody is accused. The deposit figure is not shown (paras 100 and 102 differ).
# List lines <= 52 chars. Bench photos: brand/judges/donadi_ramesh.jpg and brand/judges/alapati_giridhar.jpg (official aphc.gov.in
# "Profiles" portraits, images/30102025072357.webp and images/14072026092139.webp, composited on white).
FORMAT = "hook"   # build_course_plan.py: no opening sting, 15-frame lead (the cover), name tag on the "Ravishankar" clip

def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
ENDCARD = {"title": "Plaint rejected as an agreement to agree?", "line": "Not here: on its face the deal had every essential term · appeals allowed with costs; the disputes go to trial", "sub": "LawWorld: legal research for advocates"}

# ── 1 · thrown out before trial? (hook, curiosity, intro) ───────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "advance"), text="A handwritten land deal, an advance paid, the land sold to others. Can your suit be thrown out before any trial?", hl="thrown out before any trial?")
cue(type="list", t0=S("c02"), t1=A("c02", "was") - 0.05, head="O.S. No. 43 of 2011 · Markapur", head_at=S("c02") + 0.05,
    items=[{"n": 1, "text": "Plaint rejected under Order VII Rule 11 CPC", "at": A("c02", "trial")},
           {"n": 2, "text": "Mainly: an agreement to agree can't be enforced", "at": A("c02", "mainly")},
           {"n": 3, "text": "The buyer appeals to the High Court", "at": A("c02", "buyer")}])
cue(type="point", t0=A("c02", "was") - 0.05, t1=E("c02") + 0.05, text="Was the deal incomplete?", icon="search", accent=True, at=A("c02", "was"))
cue(type="bench", t0=S("c03"), t1=E("c03") + 0.05, tag="Andhra Pradesh High Court · 3 November 2026",
    judges=[{"name": "Justice D. Ramesh", "photo": "../brand/judges/donadi_ramesh.jpg", "at": A("c03", "honourable")},
            {"name": "Justice Alapati Giridhar", "photo": "../brand/judges/alapati_giridhar.jpg", "at": A("c03", "honourable", 2)}])

# ── 2 · the handwritten deal ────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=S("c04"), t1=E("c05") + 0.05, at=A("c04", "deal"), tag="HIGH COURT OF ANDHRA PRADESH · 03.11.2026",
    cases=[{"name": "Perumalla Kasi Rao v. Nukala Muralikrishna & Ors., with two connected appeals", "cite": "2026:APHC:47171 · A.S. Nos. 82, 83 and 84 of 2013"}])
cue(type="timeline", t0=S("c04"), t1=E("c04") + 0.05,
    nodes=[{"label": "AGREEMENT · 6 JAN 2010", "value": "47.50 acres", "sub": "Narasimhapuram and Markapuram", "at": A("c04", "january")},
           {"label": "TOTAL PRICE", "value": "₹2.38 crore", "sub": "₹5 lakh advance · balance in four months", "at": A("c04", "crore")}])
cue(type="timeline", t0=S("c05"), t1=E("c05") + 0.05,
    nodes=[{"label": "IN ONE OWNER'S HAND", "value": "signed", "sub": "for her family too, the buyer says", "at": A("c05", "wrote")},
           {"label": "20 AUGUST 2010", "value": "sold to others", "sub": "nine documents · then the suit", "tone": "red", "at": A("c05", "august")}])

# ── 3 · reject it at the door? ──────────────────────────────────────────────────────────────────────────────────────────────
cue(type="list", t0=S("c06"), t1=E("c06") + 0.05, head="Reject the plaint, the defendants said", head_at=S("c06") + 0.05,
    items=[{"n": 1, "text": "The paper names no buyer and no seller", "at": A("c06", "named")},
           {"n": 2, "text": "No description of the property", "at": A("c06", "described")},
           {"n": 3, "text": "Only terms for a later agreement", "at": A("c06", "promised")}])
cue(type="compare", t0=S("c07"), t1=E("c07") + 0.05, head="Did she sign for the family?", head_at=S("c07") + 0.05,
    cols=[{"title": "The defendants", "icon": "landmark", "at": A("c07", "they")}, {"title": "The buyer", "icon": "user", "at": A("c07", "buyer")}],
    rows=[{"cells": ["No written authority from the others", "Her handwriting: never denied"], "cells_at": [A("c07", "authority"), A("c07", "handwriting")]},
          {"cells": ["Not binding on the other owners", "Nor the ₹5 lakh advance"], "cells_at": [A("c07", "owners"), A("c07", "five")]}])

# ── 4 · before the verdict: the LawWorld request ────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c08"), t1=A("c08", "follow") - 0.05, text="The verdict is next. First, a quick request…", icon="scale", accent=True, at=A("c08", "decided"))
cue(type="list", t0=A("c08", "follow") - 0.05, t1=E("c08") + 0.05, head="Follow LawWorld · lawworld.ai", head_at=A("c08", "follow"),
    items=[{"n": 1, "text": "Search SC and High Court judgments, cited to source", "at": A("c08", "india's")},
           {"n": 2, "text": "Draft petitions, plaints and notices with AI", "at": A("c08", "platform")},
           {"n": 3, "text": "Sign up free · ₹200 AI credit included", "at": A("c08", "advocates")}])

# ── 5 · what the Court held ─────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "stage") - 0.05, text="What did the High Court decide?", icon="scale", accent=True, at=A("c09", "finally"))
cue(type="list", t0=A("c09", "stage") - 0.05, t1=E("c09") + 0.05, head="Order VII Rule 11 · what the Court found", head_at=A("c09", "stage"),
    items=[{"n": 1, "text": "Only the plaint and its documents: no mini-trial", "at": A("c09", "plaint")},
           {"n": 2, "text": "Date, extent, price, payment times, registration", "at": A("c09", "essential")},
           {"n": 3, "text": "Prima facie all essential terms, subject to proof", "at": A("c09", "face")}])
cue(type="point", t0=S("c10"), t1=A("c10", "appeals") - 0.05, text="“These disputed points on authorization and allied aspects shall be adjudicated only after trial”", icon="quote", accent=True, at=A("c10", "disputed"))
cue(type="verdicts", t0=A("c10", "appeals") - 0.05, t1=E("c10") + 0.05,
    rows=[{"text": "Trial court order rejecting the plaint", "ok": False, "at": A("c10", "appeals")},
          {"text": "Appeals allowed with costs · no view on merits", "ok": True, "at": A("c10", "costs")},
          {"text": "Balance price in fixed deposits in 10 days", "ok": True, "at": A("c10", "deposit")},
          {"text": "Suit to be decided, preferably in 6 months", "ok": True, "at": A("c10", "fixed")}])

MUSIC = {"file": "audio/bed_mixkit738_140s.mp3", "target_lufs": -21}   # owner 02-11-2026: trending-style royalty-free bed, audible under the voice
