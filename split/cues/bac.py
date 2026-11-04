# Mohammad Irfan K.I. v. State Bank of India & Ors., W.A. No. 2209 of 2026, 2026:KER:82568, High Court of Kerala (Devan Ramachandran J.
# wrote it, Basant Balaji J.; delivered on admission, 28.10.2026, "C.R." on page 3): panel cues, run by split/build_course_plan.py
# (helpers: at S E cue fx have r3 PEND). HOOK format (split/JUDGMENT_HOOK_FORMAT.md): c01 hook question (spoken to everyone, no
# "Advocates,"), c02 curiosity, c03 "Hi, I'm Ravishankar" + bench, c04-c05 the freeze and the Single Judge, c06-c07 both sides, c08 the
# LawWorld request, c09-c10 the verdict.
# Facts from the judgment (p / para): appellant aged 20, Kasaragod (p1); R2 = SHO, Cyber Crimes Cell Puducherry, R3 = SHO Bekal (p2);
# writ petition to discharge his account of R2's "freezing order" (1); his case: the disputed entries are sums from his cousin and her
# husband; alternatively confine the freeze to the disputed amount (2); Single Judge (WP(C) 41222/2025, 28.09.2026) dismissed the writ
# petition and directed a police investigation of his account (3, cause title), noticing "large amounts also credited in the account of
# the petitioner" (8); his counsel: source explained, no investigation pending, so only a dismissal was open (5); SBI: no information
# from R2 or R3 of any investigation; acts on R2's requisition (6); Senior Government Pleader: as of now R2 has issued no letter
# implicating him or his account; the freeze follows six disputed entries (7); held: no investigation "solely because of certain entries
# in the statement of such account presented by the SBI"; "None of the Police Officers on record imputes that the appellant is involved
# in any Crime"; "This itself being only a presumption at this stage, an investigation cannot be ordered by this Court independently"
# (9, 10); freeze only to the six entries (11); appeal allowed, judgment set aside; R2's freeze stands only for the disputed entries;
# further requisitions by R2 or any competent police officer bind SBI, subject to his rights (12).
# Names: the appellant is a private person - his name appears only in the cause title on the cite card. No accusation in speech.
# No section sign anywhere. List lines <= 52 chars. Bench photos: brand/judges/devan_ramachandran.jpg, basant_balaji.jpg (as mmc).
FORMAT = "hook"   # build_course_plan.py: no opening sting, 15-frame lead (the cover), name tag on the "Ravishankar" clip

def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
ENDCARD = {"title": "Large credits: can a court order a police probe?", "line": "Not on account entries alone, when no police officer on record alleges a crime · the freeze stays only on the six disputed entries", "sub": "LawWorld: legal research for advocates"}

# ── 1 · a probe into your account? (hook, curiosity, intro) ──────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "account"), text="Account frozen over a few credits. Can the court order a police probe instead?", hl="police probe instead?")
cue(type="list", t0=S("c02"), t1=A("c02", "could") - 0.05, head="One frozen account · Kasaragod", head_at=S("c02") + 0.05,
    items=[{"n": 1, "text": "Bank account frozen at a police request", "at": A("c02", "happened")},
           {"n": 2, "text": "He asks the High Court to free it", "at": A("c02", "asked")},
           {"n": 3, "text": "A judge orders a police probe instead", "at": A("c02", "judge")}])
cue(type="point", t0=A("c02", "could") - 0.05, t1=E("c02") + 0.05, text="Could a court do that?", icon="search", accent=True, at=A("c02", "could"))
cue(type="bench", t0=S("c03"), t1=E("c03") + 0.05, tag="Kerala High Court · 28 October 2026",
    judges=[{"name": "Justice Devan Ramachandran", "photo": "../brand/judges/devan_ramachandran.jpg", "at": A("c03", "honourable")},
            {"name": "Justice Basant Balaji", "photo": "../brand/judges/basant_balaji.jpg", "at": A("c03", "honourable", 2)}])

# ── 2 · the frozen account ───────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=S("c04"), t1=E("c04") + 0.05, at=A("c04", "puducherry"), tag="HIGH COURT OF KERALA · 28.10.2026",
    cases=[{"name": "Mohammad Irfan K.I. v. State Bank of India & Ors.", "cite": "2026:KER:82568 · W.A. No. 2209 of 2026"}])
cue(type="timeline", t0=S("c04"), t1=E("c04") + 0.05,
    nodes=[{"label": "CYBER CRIME POLICE", "value": "account frozen", "sub": "Puducherry's request to SBI · six disputed entries", "at": A("c04", "freeze")},
           {"label": "HE SAYS", "value": "family money", "sub": "sums from his cousin and her husband", "at": A("c04", "cousin")}])
cue(type="flow", t0=S("c05"), t1=E("c05") + 0.05, head="Writ petition · Single Judge", head_at=S("c05") + 0.05,
    steps=[{"label": "Lift the freeze", "sub": "or limit it to the disputed sums", "icon": "file-text", "at": A("c05", "lift")},
           {"label": "Petition dismissed", "sub": "28 September 2026", "icon": "landmark", "at": A("c05", "dismissed")},
           {"label": "Police probe ordered", "sub": "“large amounts also credited”", "icon": "search", "at": A("c05", "citing")}])

# ── 3 · who alleged a crime? ─────────────────────────────────────────────────────────────────────────────────────────
cue(type="compare", t0=S("c06"), t1=E("c07") + 0.05, head="Could the judge order a probe?", head_at=S("c06") + 0.05,
    cols=[{"title": "The account holder", "icon": "user", "at": A("c06", "counsel")}, {"title": "The bank · the State", "icon": "landmark", "at": A("c07", "bank")}],
    rows=[{"cells": ["Source of the money explained", "SBI: no police word of any probe"], "cells_at": [A("c06", "explained"), A("c07", "informed")]},
          {"cells": ["No probe pending: dismiss, don't investigate", "State: no letter implicating him, as of now"], "cells_at": [A("c06", "dismiss"), A("c07", "implicated")]}])

# ── 4 · before the verdict: the LawWorld request ─────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c08"), t1=A("c08", "follow") - 0.05, text="The verdict is next. First, a quick request…", icon="scale", accent=True, at=A("c08", "decided"))
cue(type="list", t0=A("c08", "follow") - 0.05, t1=E("c08") + 0.05, head="Follow LawWorld · lawworld.ai", head_at=A("c08", "follow"),
    items=[{"n": 1, "text": "Search SC and High Court judgments, cited to source", "at": A("c08", "india's")},
           {"n": 2, "text": "Draft petitions, plaints and notices with AI", "at": A("c08", "platform")},
           {"n": 3, "text": "Sign up free · ₹200 AI credit included", "at": A("c08", "advocates")}])

# ── 5 · what the Court held ──────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "no") - 0.05, text="What did the High Court decide?", icon="scale", accent=True, at=A("c09", "finally"))
cue(type="point", t0=A("c09", "no") - 0.05, t1=E("c09") + 0.05, text="“None of the Police Officers on record imputes that the appellant is involved in any Crime.”", icon="quote", accent=True, at=A("c09", "police"))
cue(type="point", t0=S("c10"), t1=A("c10", "appeal") - 0.05, text="“This itself being only a presumption at this stage, an investigation cannot be ordered by this Court independently.”", icon="quote", accent=True, at=A("c10", "single"))
cue(type="verdicts", t0=A("c10", "appeal") - 0.05, t1=E("c10") + 0.05,
    rows=[{"text": "The Single Judge's order for a police probe", "ok": False, "at": A("c10", "appeal")},
          {"text": "Freeze stays only on the six disputed entries", "ok": True, "at": A("c10", "freeze")},
          {"text": "New police requisitions still bind SBI, subject to his rights", "ok": True, "at": A("c10", "disputed")}])

MUSIC = {"file": "audio/bed_mixkit738_140s.mp3", "target_lufs": -21}   # owner 02-11-2026: trending-style royalty-free bed, audible under the voice
