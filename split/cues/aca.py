FORMAT = "hook"   # build_course_plan.py: no opening sting, 15-frame lead (the cover), name tag on the "Ravishankar" clip
# Pasam Lakshmi Narasaiah v. Rayani Venkata Subrahmanyam, C.R.P. No. 2239 of 2019, CNR APHC010241392019, High Court of Andhra Pradesh
# at Amaravati (Purushottam Kumar Chintalapudi J., reserved 31.07.2026, pronounced 30.10.2026, "Reportable √", "Lr. copy to be marked"):
# panel cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND). HOOK format (split/JUDGMENT_HOOK_FORMAT.md):
# c01 hook question, c02 curiosity, c03 "Hi, I'm Ravishankar" + bench, c04-c07 facts / case / both sides, c08 the LawWorld request,
# c09-c10 the verdict. Source: the Indian Kanoon court-copy render (doc 55781480); the court's own PDF is captcha-gated (not obtained).
# Facts from the judgment (paras): the revision (Art. 227) is the judgment-debtor's, against the order of 26.04.2019 in E.P. 41/2018 in
# O.S. 218/2015, Principal Civil Judge (Junior Division), Proddatur (1, 3, 11); E.P. for civil arrest under Order XXI Rules 37 and 38,
# allowed, arrest warrant "on payment of process" (2); money suit decreed 31.03.2017 (6); the D.Hr.'s affidavit: business, gold and
# cash, finance income, "wilfully avoiding payment" (7); the J.Dr.: no means, no gold or cash, heavy business losses (8); no documents
# marked on either side (9, 28); the court below relied on RW1: a pharma company at Hyderabad, turnover Rs.40-50 lakh a year,
# income-tax assessee -> sufficient means, intentionally evading (16, 28); the J.Dr.: no reasons, a last resort, past business is not
# present ability to pay (12, 13, 15); the D.Hr.: a reasoned finding; the 1/4 deposit under the stay order shows ability to pay
# (16, 17, 19); interim order 09.08.2019: warrant stayed on deposit of 1/4th of the E.P. amount with costs, complied (52, 53);
# the company closed in 2012 per the J.Dr., not considered below; IT returns not produced, the D.Hr. took no steps (29); a bare
# assertion of business, movables and cash does not discharge the D.Hr.'s burden (30); Jolly George Varghese: civil arrest "a measure
# of last resort", Art. 21 (31); no means shown on the decree of 31.03.2017; the mother's four acres / pension not shown to be his
# (33, 37); carrying on business "by itself, does not establish that he had sufficient means" (38); a Rule 38 warrant only brings
# him before the Court; process fee is not Rule 39 subsistence allowance (38, 39); "The simple default to discharge is not enough"
# (40); the D.Hr. must establish the s.51 conditions with sufficient material (41, 49); reasons, no cryptic orders (45); his liability
# exists (47); C.R.P. allowed in part: order of 26.04.2019 set aside, remanded for fresh adjudication; the D.Hr. may withdraw the
# deposit with accrued interest; the J.Dr. to pay 25% of the balance decretal amount within six weeks and the remaining 50% before
# the trial Court within three months, failing which the trial Court on remand passes appropriate orders in execution (56, 57).
# Not on any card: the Drugs Inspectors' cases (28); the decree amount (not in the judgment). Party names only in the cite bar.
# No section sign anywhere. List lines <= 52 chars. Official aphc.gov.in "Profiles" portrait on the bench card.

def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
ENDCARD = {"title": "Past business: enough for civil arrest?", "line": "Not by itself: the decree-holder must prove means and wilful refusal · the arrest order set aside, remanded", "sub": "LawWorld: legal research for advocates"}

# ── 1 · past business, present means? (hook, curiosity, intro) ──────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "money"), text="He lost a money suit, and once ran a pharma company. Is that alone enough to have him arrested?", hl="enough to have him arrested?")
cue(type="list", t0=S("c02"), t1=A("c02", "court", 2) - 0.05, head="One company, two stories", head_at=S("c02") + 0.05,
    items=[{"n": 1, "text": "Turnover ₹40–50 lakh a year, by his own evidence", "at": A("c02", "turnover")},
           {"n": 2, "text": "The company closed in 2012, he says", "at": A("c02", "closed")}])
cue(type="point", t0=A("c02", "court", 2) - 0.05, t1=E("c02") + 0.05, text="The court below ordered an arrest warrant. Was that right?", icon="search", accent=True, at=A("c02", "court", 2))
cue(type="bench", t0=S("c03"), t1=E("c03") + 0.05, tag="Andhra Pradesh High Court · 30 October 2026",
    judges=[{"name": "Justice Purushottam Kumar Chintalapudi", "photo": "../brand/judges/purushottam_kumar_chintalapudi.jpg", "at": A("c03", "honourable")}])

# ── 2 · the execution ───────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=S("c04"), t1=E("c05") + 0.05, at=A("c04", "won"), tag="HIGH COURT OF ANDHRA PRADESH · 30.10.2026",
    cases=[{"name": "Pasam Lakshmi Narasaiah v. Rayani Venkata Subrahmanyam", "cite": "C.R.P. No. 2239 of 2019"}])
cue(type="timeline", t0=S("c04"), t1=E("c04") + 0.05,
    nodes=[{"label": "MONEY DECREE", "value": "31.03.2017", "sub": "O.S. No. 218 of 2015 · recovery of money", "at": A("c04", "money")},
           {"label": "EXECUTION PETITION", "value": "civil arrest", "sub": "E.P. No. 41 of 2018 · Order XXI Rules 37, 38", "at": A("c04", "arrest")}])
cue(type="compare", t0=S("c05"), t1=E("c05") + 0.05, head="The execution petition", head_at=S("c05") + 0.05,
    cols=[{"title": "The decree-holder", "icon": "landmark", "at": A("c05", "said")}, {"title": "The judgment-debtor", "icon": "user", "at": A("c05", "judgment", 2)}],
    rows=[{"cells": ["He runs a business, has gold and cash", "No means, no gold or cash"], "cells_at": [A("c05", "runs"), A("c05", "denied")]},
          {"cells": ["Wilfully avoiding payment", "Heavy losses in the business"], "cells_at": [A("c05", "wilfully"), A("c05", "heavy")]}])

# ── 3 · the warrant ─────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="timeline", t0=S("c06"), t1=E("c06") + 0.05,
    nodes=[{"label": "THE ENQUIRY", "value": "no documents", "sub": "none marked by either side", "at": A("c06", "neither")},
           {"label": "HIS EVIDENCE", "value": "₹40–50 lakh", "sub": "pharma turnover · income-tax assessee", "at": A("c06", "citing")},
           {"label": "THE COURT BELOW", "value": "arrest warrant", "sub": "26.04.2019 · “sufficient means”", "tone": "red", "at": A("c06", "found")}])
cue(type="compare", t0=S("c07"), t1=E("c07") + 0.05, head="In the revision", head_at=S("c07") + 0.05,
    cols=[{"title": "The judgment-debtor", "icon": "user", "at": A("c07", "judgment")}, {"title": "The decree-holder", "icon": "landmark", "at": A("c07", "decree")}],
    rows=[{"cells": ["Past business is not present means", "His ¼ deposit shows he can pay"], "cells_at": [A("c07", "past"), A("c07", "deposit")]},
          {"cells": ["No reasons given for the warrant", "A reasoned finding below"], "cells_at": [A("c07", "means"), A("c07", "quarter")]}])

# ── 4 · before the verdict: the LawWorld request ────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c08"), t1=A("c08", "follow") - 0.05, text="The verdict is next. First, a quick request…", icon="scale", accent=True, at=A("c08", "decided"))
cue(type="list", t0=A("c08", "follow") - 0.05, t1=E("c08") + 0.05, head="Follow LawWorld · lawworld.ai", head_at=A("c08", "follow"),
    items=[{"n": 1, "text": "Search SC and High Court judgments, cited to source", "at": A("c08", "india's")},
           {"n": 2, "text": "Draft petitions, plaints and notices with AI", "at": A("c08", "platform")},
           {"n": 3, "text": "Sign up free · ₹200 AI credit included", "at": A("c08", "advocates")}])

# ── 5 · what the Court held ─────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "decree") - 0.05, text="What did the High Court decide?", icon="scale", accent=True, at=A("c09", "finally"))
cue(type="list", t0=A("c09", "decree") - 0.05, t1=E("c09") + 0.05, head="Section 51 CPC · Jolly George Varghese", head_at=A("c09", "decree"),
    items=[{"n": 1, "text": "Decree-holder must prove means and wilful refusal", "at": A("c09", "prove")},
           {"n": 2, "text": "Past business, by itself, does not prove means", "at": A("c09", "past")},
           {"n": 3, "text": "Parents' land and pension: not shown to be his", "at": A("c09", "parents")}])
cue(type="verdicts", t0=S("c10"), t1=E("c10") + 0.05,
    rows=[{"text": "The arrest warrant order of 26.04.2019", "ok": False, "at": A("c10", "arrest"), "strike_at": A("c10", "aside")},
          {"text": "Allowed in part: remanded for fresh adjudication", "ok": True, "at": A("c10", "remanded")},
          {"text": "Decree-holder may withdraw ¼ deposit with interest", "ok": True, "at": A("c10", "withdraw")},
          {"text": "25% in six weeks, the remaining 50% in three months", "ok": True, "at": A("c10", "pay")}])

MUSIC = {"file": "audio/bed_mixkit738_140s.mp3", "target_lufs": -21}   # owner 02-11-2026: trending-style royalty-free bed, audible under the voice
