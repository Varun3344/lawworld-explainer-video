# Shanker Mahadevan Iyer v. Deputy Director, Directorate of Enforcement, W.P. No. 34513 of 2024 (GM-RES), 2026:KHC:59898,
# High Court of Karnataka at Bengaluru (Suraj Govindaraj J.; reserved 29.07.2026, CAV order 28.10.2026; circled "R" on page 1 and on
# the court's Reportable list): panel cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND).
# HOOK format (split/JUDGMENT_HOOK_FORMAT.md): c01 hook question (spoken to everyone, no "Advocates,"), c02 curiosity (Kerala v. Delhi),
# c03 "Hi, I'm Ravishankar" + bench, c04-c05 the properties and the attachment, c06-c07 both sides, c08 the LawWorld request, c09-c10
# the verdict.
# Facts (para): apartment bought 15.12.2004, non-agricultural property 28.03.2008, Mangaluru (5.8, 5.9, 8(ii)); the alleged scheduled
# offence and transactions 2011-12, an iron ore export deal (8(ii), 13.3, 13.4); Provisional Attachment Order 01/2024 of 29.10.2024
# under s.5(1) PMLA (4, 10.20); the ED does not claim the properties were bought with tainted funds, attached "in lieu of" the alleged
# proceeds as equivalent value (10.45, 11.19, 11.50, 11.84, 12.21); petitioner: bought before the offence, so not proceeds (5.4, 5.7);
# equivalent value only if proceeds are held abroad (11.53); ED: funds withdrawn in cash or transferred (11.84, 13.6), premature,
# statutory remedies (6.65, 14.3); Kerala HC (Satish Motilal Bidri): only when property is taken or held out of India (11.59, 11.60);
# Delhi HC (Axis Bank, para 171): other assets near or equivalent in value where the tainted property cannot be traced or reached
# (11.72, 11.73); held: bought before the crime -> not itself proceeds (11.47, 11.87); Vijay Madanlal Choudhary para 172 binds,
# Satish Motilal Bidri not followed to that extent (11.57, 11.62, 11.63, 11.88); conditions still to be met (11.58, 11.76); facts for
# the Adjudicating Authority (11.89); "the dates of acquisition do not, by themselves, invalidate the attachment as one of equivalent
# value" (11.90); ORDER: dismissed, remedies undisturbed, merits uninfluenced, s.14 Limitation Act, interim order +30 days (15.1).
# Names: only the cause title on the cite card; no firm or person named in speech or on any other card. List lines <= 52 chars.
# Bench photo: brand/judges/suraj_govindaraj.jpg (official KHC judge-profile portrait SGRJnew.jpeg, byte-identical per mhr, 04-11-2026).
FORMAT = "hook"   # build_course_plan.py: no opening sting, 15-frame lead (the cover), name tag on the "Ravishankar" clip

def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
ENDCARD = {"title": "Bought before the crime: can the ED attach it?", "line": "Yes, as property of equal value, if the PMLA's conditions are met; the Adjudicating Authority decides that", "sub": "LawWorld: legal research for advocates"}

# ── 1 · bought before the crime (hook, curiosity, intro) ─────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "enforcement"), text="Bought years before the alleged crime. Can the ED still attach it?", hl="Can the ED still attach it?")
cue(type="compare", t0=S("c02"), t1=A("c02", "so") - 0.05, head="Two High Courts, two views", head_at=S("c02") + 0.05,
    cols=[{"title": "Kerala HC · 2024", "icon": "landmark", "at": A("c02", "kerala")}, {"title": "Delhi HC · 2019", "icon": "landmark", "at": A("c02", "delhi")}],
    rows=[{"cells": ["Only if the proceeds went abroad", "Other assets, if tainted ones can't be reached"], "cells_at": [A("c02", "abroad"), A("c02", "took")]}])
cue(type="point", t0=A("c02", "so") - 0.05, t1=E("c02") + 0.05, text="Which view for Karnataka?", icon="scale", accent=True, at=A("c02", "which"))
cue(type="bench", t0=S("c03"), t1=E("c03") + 0.05, tag="Karnataka High Court · 28 October 2026",
    judges=[{"name": "Justice Suraj Govindaraj", "photo": "../brand/judges/suraj_govindaraj.jpg", "at": A("c03", "honourable")}])

# ── 2 · attached for its value ───────────────────────────────────────────────────────────────────────────────────────
cue(type="timeline", t0=S("c04"), t1=E("c04") + 0.05,
    nodes=[{"label": "FLAT BOUGHT", "value": "2004", "sub": "sale deed, 15 Dec 2004", "at": A("c04", "flat")},
           {"label": "LAND BOUGHT", "value": "2008", "sub": "sale deed, 28 Mar 2008", "at": A("c04", "land")},
           {"label": "ALLEGED OFFENCE", "value": "2011-12", "sub": "an iron ore export deal", "tone": "red", "at": A("c04", "offence")}])
cue(type="cite", t0=S("c05"), t1=E("c05") + 0.05, at=A("c05", "twenty"), tag="HIGH COURT OF KARNATAKA · 28.10.2026",
    cases=[{"name": "Shanker Mahadevan Iyer v. Directorate of Enforcement", "cite": "2026:KHC:59898 · W.P. No. 34513 of 2024"}])
cue(type="list", t0=S("c05"), t1=E("c05") + 0.05, head="Provisional attachment · 29 Oct 2024", head_at=S("c05") + 0.05,
    items=[{"n": 1, "text": "Both properties attached under Section 5(1) PMLA", "at": A("c05", "attached")},
           {"n": 2, "text": "Not said to be bought with crime money", "at": A("c05", "claim")},
           {"n": 3, "text": "Held “in lieu of” the alleged proceeds", "at": A("c05", "equal")}])

# ── 3 · only if it went abroad? ──────────────────────────────────────────────────────────────────────────────────────
cue(type="compare", t0=S("c06"), t1=E("c07") + 0.05, head="Can these properties be attached?", head_at=S("c06") + 0.05,
    cols=[{"title": "His counsel", "icon": "scale", "at": A("c06", "counsel")}, {"title": "The ED", "icon": "landmark", "at": A("c07", "said")}],
    rows=[{"cells": ["Bought before the crime: never its proceeds", "The original money was withdrawn or moved"], "cells_at": [A("c06", "never"), A("c07", "withdrawn")]},
          {"cells": ["Equal value only if proceeds go abroad", "Premature: the PMLA has its own remedies"], "cells_at": [A("c06", "equal"), A("c07", "premature")]}])

# ── 4 · before the verdict: the LawWorld request ─────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c08"), t1=A("c08", "follow") - 0.05, text="The verdict is next. First, a quick request…", icon="scale", accent=True, at=A("c08", "decided"))
cue(type="list", t0=A("c08", "follow") - 0.05, t1=E("c08") + 0.05, head="Follow LawWorld · lawworld.ai", head_at=A("c08", "follow"),
    items=[{"n": 1, "text": "Search SC and High Court judgments, cited to source", "at": A("c08", "india's")},
           {"n": 2, "text": "Draft petitions, plaints and notices with AI", "at": A("c08", "platform")},
           {"n": 3, "text": "Sign up free · ₹200 AI credit included", "at": A("c08", "advocates")}])

# ── 5 · what the Court held ──────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "property") - 0.05, text="What did the High Court decide?", icon="scale", accent=True, at=A("c09", "finally"))
cue(type="list", t0=A("c09", "property") - 0.05, t1=E("c09") + 0.05, head="Section 2(1)(u) PMLA · the value limb", head_at=A("c09", "property"),
    items=[{"n": 1, "text": "Bought before the crime: not itself its proceeds", "at": A("c09", "bought")},
           {"n": 2, "text": "Equal value: allowed if the conditions are met", "at": A("c09", "value")},
           {"n": 3, "text": "Kerala HC's abroad-only view: not followed", "at": A("c09", "even")}])
cue(type="list", t0=S("c10"), t1=A("c10", "so") - 0.05, head="For the Adjudicating Authority, on evidence", head_at=S("c10") + 0.05,
    items=[{"n": 1, "text": "Are the original proceeds unavailable?", "at": A("c10", "whether")},
           {"n": 2, "text": "Were the sums received proceeds of crime?", "at": A("c10", "conditions")},
           {"n": 3, "text": "Are the Act's conditions satisfied?", "at": A("c10", "authority")}])
cue(type="verdicts", t0=A("c10", "so") - 0.05, t1=E("c10") + 0.05,
    rows=[{"text": "Plea to quash the attachment", "ok": False, "at": A("c10", "dismissed")},
          {"text": "All PMLA remedies: left open", "ok": True, "at": A("c10", "remedies")},
          {"text": "Interim order: 30 more days to seek relief", "ok": True, "at": A("c10", "open")}])

MUSIC = {"file": "audio/bed_mixkit738_140s.mp3", "target_lufs": -21}   # owner 02-11-2026: trending-style royalty-free bed, audible under the voice
