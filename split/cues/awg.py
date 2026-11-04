# M/s. Reha Environ Pvt. Ltd. & Anr. v. Government of Puducherry & Ors. (with C.R.P. 5220 & 5221/2026), C.R.P. No. 5394 of 2026,
# 2026:MHC:4381, High Court of Judicature at Madras (P.B. Balaji J.; reserved 22.09.2026, pronounced 30.10.2026; listed as Reportable
# in the court's judis database): panel cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND).
# HOOK format (split/JUDGMENT_HOOK_FORMAT.md): c01 hook question (spoken to everyone, no "Advocates,"), c02 curiosity, c03 "Hi, I'm
# Ravishankar" + bench, c04-c06 the contract, the award and the execution, c07 both sides, c08 the LawWorld request, c09-c10 the verdict.
# Facts (para): solid waste management projects, award holder the successful bidder; sole Arbitrator appointed by this Court; award
# 10.02.2022, amended 31.03.2022 (s.33): tipping fee Rs.21,36,68,616 -> Rs.25,53,42,384 (3); no award sufferer challenged it under s.34;
# final; E.P. 37/2024 (4); the Government's s.47 CPC application: never a party to the contract (4); Executing Court (27.07.2026):
# s.47 dismissed, but no attachment of Government departments' property as the contracts pertained only to four municipalities;
# execution only against JD3's property (Oulgaret Municipality) (5); award holder: participated from the s.21 notice, s.11 petition and
# before the Arbitrator without protest (6); ASG: operative portion does not divide the sum among the JDs; the Government not a party
# (8, 11). Held: concession agreement 18.10.2010 with JDs 2-4 alone, but s.21 notice 12.06.2012 to the Government, party in s.11
# without objection, Arbitrator appointed in its presence (13); participated, suffered the award and the amended award, no s.34 by any
# JD (14); "too late in the day" (15); "the Executing Court cannot go behind the decree" (16); "A Section 47 petition cannot be an
# appeal or challenge under Section 34 of the Arbitration Conciliation Act in disguise" (17); restriction to JD3 an error; "all the
# judgment debtors are jointly and severally liable to pay the award amount to the claimant" (20); S.N. Prasad, (2011) 1 SCC 320 (21);
# C.R.P. 5220, 5221 dismissed; restriction set aside; two months / eight weeks to settle, then execution against all JDs; E.P.
# corrections in two weeks (23, 24); C.R.P. 5394 allowed, no costs (25). Not on any card: the ASG's "fraud" plea (9, 10, 18, 19).
# Names: the parties only on the cite card. List lines <= 52 chars. No section sign anywhere.
# Bench photo: brand/judges/pb_balaji.jpg (official Madras HC portrait, byte-identical to hcmadras.tn.gov.in admin/view_image.php
# img_id MjM4 (238), alt "Hon'ble Mr.Justice P.B. Balaji"; as mcf / rnt / bcr).
FORMAT = "hook"   # build_course_plan.py: no opening sting, 15-frame lead (the cover), name tag on the "Ravishankar" clip

def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
ENDCARD = {"title": "Never signed, but took part: is the award enforceable?", "line": "Yes: having joined the arbitration without protest and never challenged the award, the Government of Puducherry could not say it was not a party", "sub": "LawWorld: legal research for advocates"}

# ── 1 · never signed, still bound? (hook, curiosity, intro) ─────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "government"), text="Never signed the contract, but joined the whole arbitration without protest. Can the government refuse to pay the award?", hl="refuse to pay the award?")
cue(type="counters", t0=S("c02"), t1=A("c02", "yet") - 0.05, head="The amended award", head_at=S("c02") + 0.05,
    items=[{"value": 25, "unit": "₹ CRORE+", "label": "The tipping fee alone", "sub": "₹21,36,68,616 raised to ₹25,53,42,384", "at": A("c02", "tipping")}])
cue(type="point", t0=A("c02", "yet") - 0.05, t1=E("c02") + 0.05, text="Execution against just one municipality's property? Was that right?", icon="search", accent=True, at=A("c02", "municipal"))
cue(type="bench", t0=S("c03"), t1=E("c03") + 0.05, tag="Madras High Court · 30 October 2026",
    judges=[{"name": "Justice P.B. Balaji", "photo": "../brand/judges/pb_balaji.jpg", "at": A("c03", "honourable")}])

# ── 2 · the award and the objection ─────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=S("c04"), t1=E("c04") + 0.05, at=A("c04", "company"), tag="HIGH COURT OF MADRAS · 30.10.2026",
    cases=[{"name": "Reha Environ Pvt. Ltd. & Anr. v. Government of Puducherry & Ors.", "cite": "2026:MHC:4381 · C.R.P. Nos. 5394, 5220 & 5221 of 2026"}])
cue(type="timeline", t0=S("c04"), t1=E("c04") + 0.05,
    nodes=[{"label": "CONCESSION AGREEMENT · 2010", "value": "Solid waste project", "sub": "the Government not a signatory", "at": A("c04", "won")},
           {"label": "ARBITRAL AWARD · 2022", "value": "For the company", "sub": "10 Feb, amended 31 Mar 2022", "at": A("c04", "arbitrator")}])
cue(type="timeline", t0=S("c05"), t1=E("c05") + 0.05,
    nodes=[{"label": "NO SECTION 34 CHALLENGE", "value": "Award final", "sub": "by none of the judgment debtors", "at": A("c05", "nobody")},
           {"label": "EXECUTION · E.P. 37/2024", "value": "Section 47 CPC objection", "sub": "the Government: never signed", "tone": "red", "at": A("c05", "execution")}])
cue(type="flow", t0=S("c06"), t1=E("c06") + 0.05, head="Executing court · 27.07.2026", head_at=S("c06") + 0.05,
    steps=[{"label": "Section 47 objection", "sub": "rejected", "icon": "check", "tone": "ok", "at": A("c06", "rejected")},
           {"label": "Government property", "sub": "not to be attached", "icon": "x", "tone": "stop", "at": A("c06", "attached")},
           {"label": "Only the third debtor", "sub": "one municipality's property", "icon": "landmark", "at": A("c06", "municipalities")}])

# ── 3 · the arguments ────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="compare", t0=S("c07"), t1=E("c07") + 0.05, head="Can the Government be made to pay?", head_at=S("c07") + 0.05,
    cols=[{"title": "The Government", "icon": "landmark", "at": A("c07", "government")}, {"title": "The award holder", "icon": "user", "at": A("c07", "holder")}],
    rows=[{"cells": ["Never signed the arbitration agreement", "Took part from the Section 21 notice"], "cells_at": [A("c07", "signed"), A("c07", "notice")]},
          {"cells": ["The award doesn't split who pays what", "To the final award, without protest"], "cells_at": [A("c07", "agreement"), A("c07", "award", 2)]}])

# ── 4 · before the verdict: the LawWorld request ─────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c08"), t1=A("c08", "follow") - 0.05, text="The verdict is next. First, a quick request…", icon="scale", accent=True, at=A("c08", "decided"))
cue(type="list", t0=A("c08", "follow") - 0.05, t1=E("c08") + 0.05, head="Follow LawWorld · lawworld.ai", head_at=A("c08", "follow"),
    items=[{"n": 1, "text": "Search SC and High Court judgments, cited to source", "at": A("c08", "india's")},
           {"n": 2, "text": "Draft petitions, plaints and notices with AI", "at": A("c08", "platform")},
           {"n": 3, "text": "Sign up free · ₹200 AI credit included", "at": A("c08", "advocates")}])

# ── 5 · what the Court held ──────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "having") - 0.05, text="What did the High Court decide?", icon="scale", accent=True, at=A("c09", "finally"))
cue(type="list", t0=A("c09", "having") - 0.05, t1=E("c09") + 0.05, head="Section 47 CPC · too late in the day", head_at=A("c09", "having"),
    items=[{"n": 1, "text": "Section 21 notice, Section 11 petition: no protest", "at": A("c09", "protest")},
           {"n": 2, "text": "Award never challenged under Section 34", "at": A("c09", "challenged")},
           {"n": 3, "text": "So it cannot now deny being a party", "at": A("c09", "deny")}])
cue(type="point", t0=S("c10"), t1=A("c10", "if") - 0.05, text="“…all the judgment debtors are jointly and severally liable to pay the award amount to the claimant.”", icon="quote", accent=True, at=A("c10", "all"))
cue(type="verdicts", t0=A("c10", "if") - 0.05, t1=E("c10") + 0.05,
    rows=[{"text": "Execution limited to one municipality's property", "ok": False, "at": A("c10", "if")},
          {"text": "8 weeks to settle the award", "ok": True, "at": A("c10", "settle")},
          {"text": "Then execution against all four debtors", "ok": True, "at": A("c10", "execution")}])

MUSIC = {"file": "audio/bed_mixkit738_140s.mp3", "target_lufs": -21}   # owner 02-11-2026: trending-style royalty-free bed, audible under the voice
# Fact-check 04-11-2026: c06 flow sub "one municipality's land" -> "property" (para 5: "the immovable property belonging to the Oulgaret Municipality").
