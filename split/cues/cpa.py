# The Divisional Controller, KKRTC, Ballari Division v. Smt. Mantavva & Anr., W.A. No. 100758 of 2025 (S-KSRTC), 2026:KHC-D:17610-DB,
# High Court of Karnataka at Dharwad (M. Nagaprasanna J. and Hema Kulkarni J.; oral judgment 28.10.2026; circled "R" on page 1 and on
# the court's Reportable list): panel cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND).
# HOOK format (split/JUDGMENT_HOOK_FORMAT.md): c01 hook question (spoken to everyone, no "Advocates,"), c02 curiosity, c03 "Hi, I'm
# Ravishankar" + bench, c04-c07 the family / the Circular / the single judge / both sides, c08 the LawWorld request, c09-c10 the verdict.
# Facts from the judgment (para): Driver 18.03.2008 to his death 21.09.2023 (3.1, 9); wife predeceased 09.04.2022, no children (9);
# the mother sought the appointment for her other son, married and residing separately, who undertook on affidavit to maintain her
# (10); rejected 04.11.2024 because the employee was married (11, quoting the single judge's para 2); the Circular: married male
# employee -> widow and children; unmarried male employee -> dependent brother or sister residing with him (14, 15); the single
# judge: mere marriage no ground when the spouse predeceased and there are no children; appoint within twelve weeks (11); the
# Corporation: an exception to equality in public employment (4, 5); the family: the scheme rescues a family from sudden financial
# catastrophe (6, 7); held: "Marriage is a fact in the life of the employee; the death of the spouse does not obliterate that fact"
# (17); an undertaking cannot create eligibility (21, 22); appeal allowed, single judge's order set aside, rejection sustained (28).
# Not on any card: the names of the employee, his mother, his brother or his late wife; the cause title appears only on the cite card.
# List lines <= 52 chars. Bench photos: brand/judges/m_nagaprasanna.jpg, brand/judges/hema_kulkarni.jpg (official KHC portrait).
FORMAT = "hook"   # build_course_plan.py: no opening sting, 15-frame lead (the cover), name tag on the "Ravishankar" clip

def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
ENDCARD = {"title": "Wife died first: can his brother get a job?", "line": "No: a married employee's brother is not a dependent under the Circular, even if the wife died first", "sub": "LawWorld: legal research for advocates"}

# ── 1 · who gets the job? (hook, curiosity, intro) ───────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "driver"), text="Wife died first, no children. Can his brother get a compassionate job?", hl="Can his brother get a compassionate job?")
cue(type="list", t0=S("c02"), t1=E("c02") + 0.05, head="Compassionate job · who decides?", head_at=S("c02") + 0.05,
    items=[{"n": 1, "text": "Mother asks: a job for her other son", "at": A("c02", "mother")},
           {"n": 2, "text": "The bus corporation: no", "at": A("c02", "corporation")},
           {"n": 3, "text": "A single judge of the High Court: yes", "at": A("c02", "single")}])
cue(type="bench", t0=S("c03"), t1=E("c03") + 0.05, tag="Karnataka High Court · Dharwad · 28 October 2026",
    judges=[{"name": "Justice M. Nagaprasanna", "photo": "../brand/judges/m_nagaprasanna.jpg", "at": A("c03", "honourable")},
            {"name": "Justice Hema Kulkarni", "photo": "../brand/judges/hema_kulkarni.jpg", "at": A("c03", "honourable", 2)}])

# ── 2 · the family left behind ───────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=S("c04"), t1=E("c04") + 0.05, at=A("c04", "joined"), tag="HIGH COURT OF KARNATAKA AT DHARWAD · 28.10.2026",
    cases=[{"name": "Divisional Controller, KKRTC v. Smt. Mantavva & Anr.", "cite": "2026:KHC-D:17610-DB · W.A. No. 100758 of 2025"}])
cue(type="timeline", t0=S("c04"), t1=E("c04") + 0.05,
    nodes=[{"label": "JOINS AS A DRIVER", "value": "2008", "sub": "a State bus corporation", "at": A("c04", "joined")},
           {"label": "HIS WIFE DIES", "value": "2022", "sub": "no children", "at": A("c04", "wife")},
           {"label": "HE DIES IN SERVICE", "value": "2023", "sub": "his mother and brother survive", "at": A("c04", "died", 2)}])
cue(type="flow", t0=S("c05"), t1=E("c05") + 0.05, head="The corporation's Circular · who qualifies?", head_at=S("c05") + 0.05,
    steps=[{"label": "Married employee", "sub": "his widow and children", "icon": "users", "at": A("c05", "married")},
           {"label": "Unmarried employee", "sub": "a dependent brother or sister living with him", "icon": "user-round", "at": A("c05", "unmarried")},
           {"label": "Claim rejected", "sub": "he was married", "icon": "x", "at": A("c05", "rejected")}])
cue(type="list", t0=S("c06"), t1=E("c06") + 0.05, head="The single judge · W.P. No. 101661 of 2025", head_at=S("c06") + 0.05,
    items=[{"n": 1, "text": "Wife died first, and no children", "at": A("c06", "wife")},
           {"n": 2, "text": "So mere marriage cannot bar the claim", "at": A("c06", "marriage")},
           {"n": 3, "text": "Appoint him within 12 weeks", "at": A("c06", "appoint")}])

# ── 3 · compassion or the rule? ──────────────────────────────────────────────────────────────────────────────────────
cue(type="compare", t0=S("c07"), t1=E("c07") + 0.05, head="In appeal · the rule or compassion?", head_at=S("c07") + 0.05,
    cols=[{"title": "The corporation", "icon": "landmark", "at": A("c07", "corporation")}, {"title": "The family", "icon": "users", "at": A("c07", "family")}],
    rows=[{"cells": ["An exception to equal public employment", "Meant to rescue a family in distress"], "cells_at": [A("c07", "exception"), A("c07", "rescue")]},
          {"cells": ["The brother is not a dependent", "He has promised to care for the mother"], "cells_at": [A("c07", "employment"), A("c07", "lose")]}])

# ── 4 · before the verdict: the LawWorld request ─────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c08"), t1=A("c08", "follow") - 0.05, text="The verdict is next. First, a quick request…", icon="scale", accent=True, at=A("c08", "decided"))
cue(type="list", t0=A("c08", "follow") - 0.05, t1=E("c08") + 0.05, head="Follow LawWorld · lawworld.ai", head_at=A("c08", "follow"),
    items=[{"n": 1, "text": "Search SC and High Court judgments, cited to source", "at": A("c08", "india's")},
           {"n": 2, "text": "Draft petitions, plaints and notices with AI", "at": A("c08", "platform")},
           {"n": 3, "text": "Sign up free · ₹200 AI credit included", "at": A("c08", "advocates")}])

# ── 5 · what the Court held ──────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "marriage") - 0.05, text="What did the High Court decide?", icon="scale", accent=True, at=A("c09", "finally"))
cue(type="point", t0=A("c09", "marriage") - 0.05, t1=E("c09") + 0.05, text="“Marriage is a fact in the life of the employee; the death of the spouse does not obliterate that fact.”", icon="quote", accent=True, at=A("c09", "marriage"))
cue(type="point", t0=S("c10"), t1=A("c10", "so") - 0.05, text="A promise to care for the mother cannot create eligibility", icon="scale", accent=True, at=A("c10", "promise"))
cue(type="verdicts", t0=A("c10", "so") - 0.05, t1=E("c10") + 0.05,
    rows=[{"text": "The corporation's appeal: allowed", "ok": True, "at": A("c10", "allowed")},
          {"text": "The single judge's order: set aside", "ok": False, "at": A("c10", "aside")},
          {"text": "Rejection of the brother's claim: upheld", "ok": True, "at": A("c10", "upheld")}])

MUSIC = {"file": "audio/bed_mixkit738_140s.mp3", "target_lufs": -21}   # owner 02-11-2026: trending-style royalty-free bed, audible under the voice
