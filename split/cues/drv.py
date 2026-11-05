# The Branch Manager, Royal Sundaram General Insurance Co. Ltd. v. Asaraf Asad & Ors., C.M.A.(MD) No. 627 of 2024, Madurai Bench of
# Madras High Court (K.K. Ramakrishnan J.; reserved 31.08.2026, pronounced 02.11.2026; listed as Reportable in the court's judis
# database, filename 2115939; no neutral citation shown): panel cues, run by split/build_course_plan.py (helpers: at S E cue fx have
# r3 PEND).
# HOOK format (split/JUDGMENT_HOOK_FORMAT.md): c01 hook question (spoken to everyone, no "Advocates,"), c02 curiosity, c03 "Hi, I'm
# Ravishankar" + bench, c04-c05 the accident and the tribunal, c06-c07 both sides, c08 the LawWorld request, c09-c10 the verdict.
# Facts (para): insurer's appeal under s.173 MV Act against the award of 20.12.2022 in M.C.O.P. 341/2020, MACT (Principal District
# Judge), Pudukkottai (prayer, 1); the claimant drove a car insured with the appellant; accident 22.01.2020 in the course of his
# employment, severe injuries (2.1); insurer: no employer-employee relationship (2.2); tribunal: he was the driver, the MV Act claim
# treated as one under the Workmen's Compensation Act, Rs.19,77,595 with 7.25% p.a. interest from the petition to realisation (3.1);
# insurer: no evidence to convert, no jurisdiction to convert, amount not per the Employees' Compensation Act (4.1); claimant: PW1 and
# PW2 proved his employment as driver, amount properly calculated (5.1). Held: PW1 - driver on Rs.10,000 a month; PW2 - the owner
# asked him to arrange a driver and he arranged the claimant (7.1); evidence "cogent, corroborative and trustworthy", no contra
# evidence (7.2); Division Bench rule (Krishnan, (2003) 2 LW 73; Kaliya Pillai, (2002) 4 CTC 469): when an MV Act claim is not
# maintainable, the court must consider converting it into one under the Employees' Compensation Act and grant the lesser relief,
# provided employment by the owner and an accident in the course of it are established (7.3); the "not covered by the policy" plea
# rejected (7.4); C.M.A. dismissed, award confirmed, no costs (8.1). Names: the insurer only on the cite card; no private name.
# List lines <= 52 chars. No section sign anywhere. Bench photo: brand/judges/kk_ramakrishnan.jpg (official Madras HC portrait,
# hcmadras.tn.gov.in/present_judges.php, admin/view_image.php img_id MjQx (241), alt "Hon'ble Mr.Justice K.K. Ramakrishnan").
FORMAT = "hook"   # build_course_plan.py: no opening sting, 15-frame lead (the cover), name tag on the "Ravishankar" clip

def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
ENDCARD = {"title": "Hurt on duty, claimed under the MV Act?", "line": "MV Act claim not maintainable? With employment and an accident on duty proved, the court must consider conversion", "sub": "LawWorld: legal research for advocates"}

# ── 1 · a different law? (hook, curiosity, intro) ───────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "driver"), text="Hurt on duty, he claims under the Motor Vehicles Act. Can the tribunal pay him under a different law instead?", hl="under a different law instead?")
cue(type="list", t0=S("c02"), t1=A("c02", "who") - 0.05, head="The award · the insurer's challenge", head_at=S("c02") + 0.05,
    items=[{"n": 1, "text": "Tribunal: ₹19,77,595 as employee's compensation", "at": A("c02", "gave")},
           {"n": 2, "text": "Insurer: no power to switch laws", "at": A("c02", "insurer")},
           {"n": 3, "text": "Insurer: no proof he was employed", "at": A("c02", "proof")}])
cue(type="point", t0=A("c02", "who") - 0.05, t1=E("c02") + 0.05, text="Who was right?", icon="search", accent=True, at=A("c02", "right"))
cue(type="bench", t0=S("c03"), t1=E("c03") + 0.05, tag="Madras High Court · Madurai Bench · 2 November 2026",
    judges=[{"name": "Justice K.K. Ramakrishnan", "photo": "../brand/judges/kk_ramakrishnan.jpg", "at": A("c03", "honourable")}])

# ── 2 · hurt on duty ─────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=S("c04"), t1=E("c04") + 0.05, at=A("c04", "drove"), tag="HIGH COURT OF MADRAS · 02.11.2026",
    cases=[{"name": "Royal Sundaram General Insurance Co. Ltd. v. Asaraf Asad & Ors.", "cite": "C.M.A.(MD) No. 627 of 2024 · Madurai Bench"}])
cue(type="timeline", t0=S("c04"), t1=E("c04") + 0.05,
    nodes=[{"label": "THE CAR", "value": "Insured with the appellant", "sub": "he was employed as its driver", "at": A("c04", "insured")},
           {"label": "ACCIDENT · 22.01.2020", "value": "Severe injuries", "sub": "in the course of his employment", "tone": "red", "at": A("c04", "accident")}])
cue(type="flow", t0=S("c05"), t1=E("c05") + 0.05, head="MACT Pudukkottai · 20.12.2022", head_at=S("c05") + 0.05,
    steps=[{"label": "Claim under the MV Act", "sub": "M.C.O.P. No. 341 of 2020", "icon": "file-text", "at": A("c05", "claimed")},
           {"label": "He was the driver", "sub": "the tribunal's finding", "icon": "search", "at": A("c05", "finding")},
           {"label": "₹19,77,595 awarded", "sub": "as employee's compensation, 7.25% interest", "icon": "check", "tone": "ok", "at": A("c05", "compensation")}])

# ── 3 · the arguments ────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="compare", t0=S("c06"), t1=E("c07") + 0.05, head="Convert a Motor Vehicles Act claim?", head_at=S("c06") + 0.05,
    cols=[{"title": "The insurer", "icon": "landmark", "at": A("c06", "insurer")}, {"title": "The driver", "icon": "user", "at": A("c07", "driver")}],
    rows=[{"cells": ["No evidence to convert the claim", "Two witnesses proved he was the driver"], "cells_at": [A("c06", "evidence"), A("c07", "witnesses")]},
          {"cells": ["No jurisdiction; amount not as the Act allows", "Amount properly worked out under the Act"], "cells_at": [A("c06", "jurisdiction"), A("c07", "properly")]}])

# ── 4 · before the verdict: the LawWorld request ─────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c08"), t1=A("c08", "follow") - 0.05, text="The verdict is next. First, a quick request…", icon="scale", accent=True, at=A("c08", "decided"))
cue(type="list", t0=A("c08", "follow") - 0.05, t1=E("c08") + 0.05, head="Follow LawWorld · lawworld.ai", head_at=A("c08", "follow"),
    items=[{"n": 1, "text": "Search SC and High Court judgments, cited to source", "at": A("c08", "india's")},
           {"n": 2, "text": "Draft petitions, plaints and notices with AI", "at": A("c08", "platform")},
           {"n": 3, "text": "Sign up free · ₹200 AI credit included", "at": A("c08", "advocates")}])

# ── 5 · what the Court held ──────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "witnesses") - 0.05, text="What did the High Court decide?", icon="scale", accent=True, at=A("c09", "finally"))
cue(type="list", t0=A("c09", "witnesses") - 0.05, t1=E("c09") + 0.05, head="The evidence · PW1 and PW2", head_at=A("c09", "witnesses"),
    items=[{"n": 1, "text": "Cogent, corroborative and trustworthy", "at": A("c09", "cogent")},
           {"n": 2, "text": "The insurer led no contrary evidence", "at": A("c09", "contrary")},
           {"n": 3, "text": "Employed by the owner as the car's driver", "at": A("c09", "driver")}])
cue(type="point", t0=S("c10"), t1=A("c10", "appeal") - 0.05, text="“…it is the duty of the Court to consider converting the claim into one under the Employees’ Compensation Act and grant the lesser relief permissible thereunder…”", icon="quote", accent=True, at=A("c10", "motor"))
cue(type="verdicts", t0=A("c10", "appeal") - 0.05, t1=E("c10") + 0.05,
    rows=[{"text": "The insurer's appeal", "ok": False, "at": A("c10", "appeal")},
          {"text": "Award of ₹19,77,595 with interest confirmed", "ok": True, "at": A("c10", "award")},
          {"text": "No costs · petition closed", "ok": True, "at": A("c10", "stands")}])

MUSIC = {"file": "audio/bed_mixkit738_140s.mp3", "target_lufs": -21}   # owner 02-11-2026: trending-style royalty-free bed, audible under the voice
# Fact-check 04-11-2026: ENDCARD line restated as the Court's rule (para 7.3: not maintainable -> duty to consider converting, provided employment by the owner and an accident in its course are established).

# 05-11-2026 QA: the end-card line (169 chars) was clipped at both edges; shortened to 113 chars.
