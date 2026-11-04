# Paravada Ganesh & Ors. v. State of Andhra Pradesh & Ors., W.P. No. 27611 of 2025 & batch (W.P. Nos. 29972, 31717, 32771 of 2025;
# 7016, 11918 of 2026), common order, 2026:APHC:47018 (47019, 47020), High Court of Andhra Pradesh at Amaravati (Nyapathy Vijay J.;
# reserved 29.09.2026, pronounced 30.10.2026; "Note: L.R copy be marked." = marked to the Law Reporters): panel cues, run by
# split/build_course_plan.py (helpers: at S E cue fx have r3 PEND). HOOK format (split/JUDGMENT_HOOK_FORMAT.md): c01 hook question
# (spoken to everyone, no "Advocates,"), c02 curiosity, c03 "Hi, I'm Ravishankar" + bench, c04-c05 the recruitment and the drop-outs,
# c06-c07 the State's case and the Supreme Court's earlier reading, c08 the LawWorld request, c09-c10 the verdict.
# Facts from the order (para): SLPRB notification Rc.No.161/SLPRB/Rect.2/2022 of 28.11.2022, 3580 PC (Civil) + 2520 PC (APSP) (2);
# four stages (3); final selection strictly on relative merit (4); provisional selectees sent for antecedent verification and medical
# examination; drop-outs (selected in other departments, unwillingness) left 400 posts unfilled; the next meritorious sought them
# (5); not considered: the counter relied on Clause 33(ix) and on participation "with open eyes" (6); Clause 33(ix) and Clause 25
# quoted (9); G.O.Ms.No.81 / the 1998 Ad hoc Rule read by the Supreme Court (Munja Praveen, Narimetla Vamsi, K. Ashok) to apply only
# to relinquishment after appointment orders (11-16); Clause 33(ix) introduced "to overcome the Judgments" (17); Clauses 25 and 33(ix)
# contradict (18); "at the stage of verification, it would be unfair to deny consideration of the next meritorious in the line" (21);
# arbitrary, Articles 14 and 16 (22, 25); "their mere participation cannot amount to validation of arbitrary clauses" (26); relief:
# petitions disposed of - Clause 33(ix) "declared to be arbitrary and unfair"; steps for appointment in the left over vacancies "by
# adhering to merit as well as reservations"; within four months of receipt of the order; no costs (34).
# Names: the lead cause title only on the cite card; nobody is accused. List lines <= 52 chars. Bench photo: brand/judges/
# nyapathy_vijay.jpg (official aphc.gov.in "Profiles" portrait, 21092024142624.webp).
FORMAT = "hook"   # build_course_plan.py: no opening sting, 15-frame lead (the cover), name tag on the "Ravishankar" clip

def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
ENDCARD = {"title": "Drop-outs at verification: do the posts lapse?", "line": "No: the clause is arbitrary and unfair · fill the left-over vacancies by merit and reservation within four months", "sub": "LawWorld: legal research for advocates"}

# ── 1 · when selectees drop out (hook, curiosity, intro) ────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "clear"), text="Cleared every stage, just missed the list. Selectees drop out at verification. Do those posts simply lapse?", hl="Do those posts simply lapse?")
cue(type="list", t0=S("c02"), t1=A("c02", "state") - 0.05, head="AP constable recruitment · 2022", head_at=S("c02") + 0.05,
    items=[{"n": 1, "text": "6,100 constable posts notified by the SLPRB", "at": A("c02", "constable")},
           {"n": 2, "text": "400 posts left unfilled by drop-outs", "at": A("c02", "four")}])
cue(type="point", t0=A("c02", "state") - 0.05, t1=E("c02") + 0.05, text="A “no waiting list” clause. Was it valid?", icon="search", accent=True, at=A("c02", "waiting"))
cue(type="bench", t0=S("c03"), t1=E("c03") + 0.05, tag="Andhra Pradesh High Court · 30 October 2026",
    judges=[{"name": "Justice Nyapathy Vijay", "photo": "../brand/judges/nyapathy_vijay.jpg", "at": A("c03", "honourable")}])

# ── 2 · the recruitment ─────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=S("c04"), t1=E("c05") + 0.05, at=A("c04", "state"), tag="HIGH COURT OF ANDHRA PRADESH · 30.10.2026",
    cases=[{"name": "Paravada Ganesh & Ors. v. State of Andhra Pradesh & Ors., with five connected petitions", "cite": "2026:APHC:47018 · W.P. No. 27611 of 2025 & batch"}])
cue(type="timeline", t0=S("c04"), t1=E("c04") + 0.05,
    nodes=[{"label": "SLPRB NOTIFICATION", "value": "6,100 posts", "sub": "28.11.2022 · PC (Civil) and PC (APSP)", "at": A("c04", "notified")},
           {"label": "FOUR STAGES", "value": "strictly on merit", "sub": "written tests · PMT · PET", "at": A("c04", "strictly")}])
cue(type="timeline", t0=S("c05"), t1=E("c05") + 0.05,
    nodes=[{"label": "ANTECEDENT · MEDICAL CHECKS", "value": "drop-outs", "sub": "other departments, unwilling to join", "tone": "red", "at": A("c05", "antecedent")},
           {"label": "THE NEXT IN MERIT", "value": "seek the posts", "sub": "willing to join the police", "at": A("c05", "next")}])

# ── 3 · the no waiting list clause ──────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c06"), t1=A("c06", "left") - 0.05, text="Clause 33(ix): “… no waiting list shall be maintained under any circumstances.”", icon="quote", accent=True, at=A("c06", "relied"))
cue(type="point", t0=A("c06", "left") - 0.05, t1=E("c06") + 0.05, text="“The left over vacancies … shall be deemed to have lapsed for the recruitment notified.”", icon="quote", accent=True, at=A("c06", "left"))
cue(type="point", t0=S("c07"), t1=A("c07", "yet") - 0.05, text="The State: having taken part “with open eyes”, they cannot question Clause 33(ix)", icon="landmark", at=A("c07", "said"))
cue(type="list", t0=A("c07", "yet") - 0.05, t1=E("c07") + 0.05, head="Supreme Court · the old no-waiting-list rule", head_at=A("c07", "supreme"),
    items=[{"n": 1, "text": "Munja Praveen · Narimetla Vamsi · K. Ashok", "at": A("c07", "similar")},
           {"n": 2, "text": "Applies only to drop-outs after appointment orders", "at": A("c07", "drop")},
           {"n": 3, "text": "HC: Clause 33(ix) added to overcome those rulings", "at": A("c07", "orders")}])

# ── 4 · before the verdict: the LawWorld request ────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c08"), t1=A("c08", "follow") - 0.05, text="The verdict is next. First, a quick request…", icon="scale", accent=True, at=A("c08", "decided"))
cue(type="list", t0=A("c08", "follow") - 0.05, t1=E("c08") + 0.05, head="Follow LawWorld · lawworld.ai", head_at=A("c08", "follow"),
    items=[{"n": 1, "text": "Search SC and High Court judgments, cited to source", "at": A("c08", "india's")},
           {"n": 2, "text": "Draft petitions, plaints and notices with AI", "at": A("c08", "platform")},
           {"n": 3, "text": "Sign up free · ₹200 AI credit included", "at": A("c08", "advocates")}])

# ── 5 · what the Court held ─────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "clause") - 0.05, text="What did the High Court decide?", icon="scale", accent=True, at=A("c09", "finally"))
cue(type="list", t0=A("c09", "clause") - 0.05, t1=E("c09") + 0.05, head="Clause 33(ix) · what the Court found", head_at=A("c09", "clause"),
    items=[{"n": 1, "text": "Arbitrary and unfair: Articles 14 and 16", "at": A("c09", "arbitrary")},
           {"n": 2, "text": "Contradicts Clause 25: selection is provisional", "at": A("c09", "verification")},
           {"n": 3, "text": "Unfair to shut out the next in merit at verification", "at": A("c09", "shut")}])
cue(type="point", t0=S("c10"), t1=A("c10", "state") - 0.05, text="“Their mere participation cannot amount to validation of arbitrary clauses.”", icon="quote", accent=True, at=A("c10", "taking"))
cue(type="verdicts", t0=A("c10", "state") - 0.05, t1=E("c10") + 0.05,
    rows=[{"text": "Clause 33(ix): declared arbitrary and unfair", "ok": False, "at": A("c10", "state")},
          {"text": "Steps to fill the left-over vacancies", "ok": True, "at": A("c10", "fill")},
          {"text": "By merit as well as reservation", "ok": True, "at": A("c10", "merit")},
          {"text": "Within 4 months of the order · petitions disposed of", "ok": True, "at": A("c10", "four")}])

MUSIC = {"file": "audio/bed_mixkit738_140s.mp3", "target_lufs": -21}   # owner 02-11-2026: trending-style royalty-free bed, audible under the voice
