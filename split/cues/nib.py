# The National Insurance Company Limited v. Bammidi Savithri & Ors., M.A.C.M.A. No. 3096 of 2017, 2026:APHC:46786, High Court of
# Andhra Pradesh at Amaravati (Sunitha Gandham J., judgment 02.11.2026; "Note: L.R. Copy to be marked." on p.16 = marked to the Law
# Reporters): panel cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND). HOOK format
# (split/JUDGMENT_HOOK_FORMAT.md): c01 hook question (spoken to everyone, no "Advocates,"), c02 curiosity, c03 "Hi, I'm Ravishankar"
# + bench, c04-c05 the crash and the claim, c06-c07 the insurer's appeal and both sides on raising the award, c08 the LawWorld
# request, c09-c10 the verdict.
# Facts from the judgment (para): appeal by the insurer against the Tribunal's order and decree of 25.07.2017 (M.V.O.P. 213/2013,
# MACT-cum-I Addl. District Judge, Srikakulam) granting Rs.9,14,800 for a death in an accident of 12.02.2011 (1); 12.02.2011 about
# 8.30 PM, a car from Palasa to Srikakulam, a tractor and trailer near Akula Nandigam village; aged about 24, male nursing orderly,
# Rs.9,600 a month; claim against the driver (R1), owner (R2) and insurer (R3) (3); R3: the deceased negligent, no valid fitness
# certificate (4); Tribunal: Rs.9,14,800 with 9% interest; appeal grounds incl. negligence of the deceased, no fitness certificate,
# salary not properly assessed (6); no appeal or cross objections by the claimants (9, 11(c)); PW.2 the only eyewitness; R3 only
# RW.1's "self-serving statement"; R1 ex parte, not examined (10(a)-(b)); charge sheet, MVI report: no mechanical defect; accident due
# to R1's rash and negligent driving (10(c)); age 24 (11(a)), income Rs.9,600 (11(b)); claimants' counsel: just and fair compensation
# may be awarded; the respondents' counsel: 2011 accident, present principles should not apply; Order 41 Rule 33, Sharanamma (11(c));
# Surekha v. Santhosh: "this Court is under obligation to award just and fair compensation" (11(e)); SC law applies retrospectively
# unless expressly prospective (11(f)); the Tribunal used the mother's age instead of the deceased's, multiplier 11, a 1/3 deduction
# though he was unmarried (11(g)); reassessed with 1/2 deduction, 40% future prospects, multiplier 18, filial consortium Rs.40,000 x 2:
# Rs.15,76,500 (11(h)-(i)); no valid permit (RW.2): the owner liable, but the deceased is a third party: the insurer pays first and
# recovers, Ss. 149, 157(2) MV Act (11(j)-(s)); award modified (12); appeal allowed in part: Rs.15,76,500 with 7.5% simple interest
# from the petition till realisation, Rs.7,88,250 to each parent, R3 to deposit within one month of the Tribunal receiving the
# judgment and recover from R1 and R2, no costs (13).
# Names: the cause title only on the cite card; no private name in speech. List lines <= 52 chars. Bench photo: brand/judges/
# sunitha_gandham.jpg (official aphc.gov.in "Profiles" portrait, images/06072026043335.webp, composited on white).
FORMAT = "hook"   # build_course_plan.py: no opening sting, 15-frame lead (the cover), name tag on the "Ravishankar" clip

def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
ENDCARD = {"title": "Insurer's appeal: can the award go up?", "line": "Yes: no cross-appeal needed for just and fair compensation · ₹9,14,800 raised to ₹15,76,500; insurer pays first", "sub": "LawWorld: legal research for advocates"}

# ── 1 · can the award go up? (hook, curiosity, intro) ───────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "insurer"), text="The insurer appeals to cut the award. The family doesn't appeal. Can the High Court still raise it?", hl="Can the High Court still raise it?")
cue(type="list", t0=S("c02"), t1=A("c02", "so") - 0.05, head="One award, one appeal", head_at=S("c02") + 0.05,
    items=[{"n": 1, "text": "Tribunal: over ₹9 lakh to the parents", "at": A("c02", "awarded")},
           {"n": 2, "text": "The insurer appeals, blaming the young man", "at": A("c02", "appealed")}])
cue(type="point", t0=A("c02", "so") - 0.05, t1=E("c02") + 0.05, text="Who pays, and how much?", icon="search", accent=True, at=A("c02", "pays"))
cue(type="bench", t0=S("c03"), t1=E("c03") + 0.05, tag="Andhra Pradesh High Court · 2 November 2026",
    judges=[{"name": "Justice Sunitha Gandham", "photo": "../brand/judges/sunitha_gandham.jpg", "at": A("c03", "honourable")}])

# ── 2 · the crash and the claim ─────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=S("c04"), t1=E("c05") + 0.05, at=A("c04", "february"), tag="HIGH COURT OF ANDHRA PRADESH · 02.11.2026",
    cases=[{"name": "The National Insurance Co. Ltd. v. Bammidi Savithri & Ors.", "cite": "2026:APHC:46786 · M.A.C.M.A. No. 3096 of 2017"}])
cue(type="timeline", t0=S("c04"), t1=E("c04") + 0.05,
    nodes=[{"label": "12 FEBRUARY 2011", "value": "about 8.30 PM", "sub": "a car, Palasa to Srikakulam", "at": A("c04", "february")},
           {"label": "A TRACTOR AND TRAILER", "value": "hits the car", "sub": "near Akula Nandigam village", "tone": "red", "at": A("c04", "tractor")}])
cue(type="timeline", t0=S("c05"), t1=E("c05") + 0.05,
    nodes=[{"label": "AGED 24, UNMARRIED", "value": "₹9,600 a month", "sub": "a male nursing orderly", "at": A("c05", "twenty")},
           {"label": "HIS PARENTS CLAIM", "value": "M.V.O.P. 213 of 2013", "sub": "against the driver, owner and insurer", "at": A("c05", "claimed")}])

# ── 3 · the insurer's appeal ────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="list", t0=S("c06"), t1=A("c06", "parents") - 0.05, head="The insurer's grounds", head_at=S("c06") + 0.05,
    items=[{"n": 1, "text": "The young man drove negligently, it says", "at": A("c06", "blamed")},
           {"n": 2, "text": "The tractor had no fitness certificate", "at": A("c06", "fitness")},
           {"n": 3, "text": "His salary was not properly assessed", "at": A("c06", "disputed")}])
cue(type="point", t0=A("c06", "parents") - 0.05, t1=E("c06") + 0.05, text="The parents: no appeal and no cross-objections on the amount", icon="user", at=A("c06", "parents"))
cue(type="compare", t0=S("c07"), t1=E("c07") + 0.05, head="Raise it without a cross-appeal?", head_at=S("c07") + 0.05,
    cols=[{"title": "The parents' counsel", "icon": "user", "at": A("c07", "parents")}, {"title": "The other side", "icon": "landmark", "at": A("c07", "other")}],
    rows=[{"cells": ["No appeal, yet asks for a just award", "The accident was back in 2011"], "cells_at": [A("c07", "asked"), A("c07", "replied")]},
          {"cells": ["“just and fair compensation”", "Present principles should not apply"], "cells_at": [A("c07", "fair"), A("c07", "principles")]}])

# ── 4 · before the verdict: the LawWorld request ────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c08"), t1=A("c08", "follow") - 0.05, text="The verdict is next. First, a quick request…", icon="scale", accent=True, at=A("c08", "decided"))
cue(type="list", t0=A("c08", "follow") - 0.05, t1=E("c08") + 0.05, head="Follow LawWorld · lawworld.ai", head_at=A("c08", "follow"),
    items=[{"n": 1, "text": "Search SC and High Court judgments, cited to source", "at": A("c08", "india's")},
           {"n": 2, "text": "Draft petitions, plaints and notices with AI", "at": A("c08", "platform")},
           {"n": 3, "text": "Sign up free · ₹200 AI credit included", "at": A("c08", "advocates")}])

# ── 5 · what the Court held ─────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "tractor") - 0.05, text="What did the High Court decide?", icon="scale", accent=True, at=A("c09", "finally"))
cue(type="list", t0=A("c09", "tractor") - 0.05, t1=E("c09") + 0.05, head="What the Court found", head_at=A("c09", "tractor"),
    items=[{"n": 1, "text": "The tractor driver was rash and negligent", "at": A("c09", "rash")},
           {"n": 2, "text": "Order 41 Rule 33: no cross-appeal needed", "at": A("c09", "cross")},
           {"n": 3, "text": "“obligation to award just and fair compensation”", "at": A("c09", "bound")}])
cue(type="timeline", t0=S("c10"), t1=A("c10", "which") - 0.05,
    nodes=[{"label": "TRIBUNAL · 2017", "value": "₹9,14,800", "sub": "mother's age, multiplier 11 · 9% interest", "tone": "red", "at": A("c10", "tribunal")},
           {"label": "HIGH COURT · 2026", "value": "₹15,76,500", "sub": "multiplier 18 · 7.5% simple interest", "at": A("c10", "rose")}])
cue(type="verdicts", t0=A("c10", "which") - 0.05, t1=E("c10") + 0.05,
    rows=[{"text": "The insurer deposits first, within a month", "ok": True, "at": A("c10", "insurer")},
          {"text": "Then recovers it from the owner and driver", "ok": True, "at": A("c10", "recover")},
          {"text": "Appeal allowed in part · award modified", "ok": True, "at": A("c10", "driver")}])

MUSIC = {"file": "audio/bed_mixkit738_140s.mp3", "target_lufs": -21}   # owner 02-11-2026: trending-style royalty-free bed, audible under the voice

# 05-11-2026 QA: the end-card line (147 chars) was clipped at both edges; shortened to 111 chars.
