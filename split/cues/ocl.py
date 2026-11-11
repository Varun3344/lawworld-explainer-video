# Union of India & Ors. v. Rohith Nathan and Anr., etc., 2026 INSC 1201, M.A. Nos. 3313-3315 of 2026 (with M.A. Nos. 3316-3318 of 2026)
# in C.A. Nos. 2827-2829 of 2018, Supreme Court of India (an ORDER, no author line; Pamidighantam Sri Narasimha J., R. Mahadevan J.;
# New Delhi, 06.11.2026; REPORTABLE on page 1): panel cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND).
# HOOK format (split/JUDGMENT_HOOK_FORMAT.md): c01 hook question (spoken to everyone, no "Advocates,"), c02 curiosity, c03 "I'm
# Ravishankar" + bench, c04-c05 how the dispute began, c06-c07 the March ruling and the applications, c08 the LawWorld request,
# c09-c10 the verdict. DRAFT 11-11-2026, awaiting the owner's yes. POLITICALLY SENSITIVE: facts only, every card from the order.
# Facts (para): MA Diary 51879: CSE-2025 service allocation on the pre-11.03.2026 creamy-layer principles; MA Diary 51897: no
# retrospective reopening of completed selections etc., two years for equivalence of posts + a uniform policy (2); candidates cleared
# CSE, PSU posts never formally equated with Government posts, so DoPT applied the Income/Wealth Test (Category VI, 1993 OM + 2004
# Letter) to their PSU-employed parents' income for three years: creamy layer, no OBC-NCL reservation (3.1); CAT for them, the Union's
# writs dismissed by the Madras, Delhi and Kerala High Courts (3.2); 11.03.2026: appeals dismissed, six months to implement (3.4, 12);
# "the rejection of mechanical exclusion based on salary income" (11); respondents "fall within the non-creamy layer of the OBC
# category" (18(i)); SG: CSE-2025 result declared 06.03.2026, "five days prior to the judgment" (4); "potential impact on more than 6.69
# lakh reserved vacancies, including 3.70 lakh OBC vacancies, filled over the preceding ten years" (4); respondents: "an attempt to
# circumvent review jurisdiction and seek a rehearing", the Union's failure to do the equivalence exercise despite assurances (5).
# Held (18): (ii)/(v) no reopening of concluded selections on the ratio alone; (v) pending claims of others on their own merits;
# (vi) post-11.03.2026 selections governed by the 1993 OM as interpreted; (vii) Government at liberty to frame policy; (viii) no
# timeline, "domain of the executive and the legislature"; (ix) CSE-2025: "the creamy layer principle, as interpreted in the said
# judgment, shall govern the allocation of services to OBC candidates selected through the Civil Services Examination, 2025";
# (19) MAs disposed of, compliance time extended by two months.
# Names: only the cause title on the cite card; the 6.69 lakh figure is labelled as the Union's estimate; nothing says the CSE-2025
# result is cancelled or revised. List lines <= 52 chars. Bench photos: brand/judges/pamidighantam_sri_narasimha.jpg and
# brand/judges/r_mahadevan.jpg (official sci.gov.in portraits; r_mahadevan fetched 11-11-2026 from sci.gov.in/judge/justice-r-mahadevan/);
# "Justice P.S. Narasimha" on the card (nkp lesson: the full name wraps to three lines); spoken "P S Narasimha" in c03 (fact-check
# 11-11-2026: the standard "Hi, I'm Ravishankar ... On the sixth of November" shape with the full name ran 45 syllables).
FORMAT = "hook"   # build_course_plan.py: no opening sting, 15-frame lead (the cover), name tag on the "Ravishankar" clip

def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
ENDCARD = {"title": "Which creamy layer rule for CSE-2025?", "line": "The 11 March ruling governs CSE-2025 service allocation; concluded selections are not reopened by it alone", "sub": "LawWorld: legal research for advocates"}

# ── 1 · which rule applies? (hook, curiosity, intro) ─────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "result"), text="CSE-2025 result: 6 March. OBC creamy layer ruling: 11 March. Which rule governs service allocation?", hl="Which rule governs service allocation?")
cue(type="timeline", t0=S("c02"), t1=A("c02", "where") - 0.05,
    nodes=[{"label": "CSE-2025 ALLOCATION", "value": "old criteria", "sub": "the government's plea · pre-11 March basis", "at": A("c02", "earlier")},
           {"label": "IF REOPENED · UNION'S ESTIMATE", "value": "6.69 lakh+", "sub": "reserved posts filled over 10 years", "tone": "stop", "at": A("c02", "reopening")}])
cue(type="point", t0=A("c02", "where") - 0.05, t1=E("c02") + 0.05, text="Where does the Court draw the line?", icon="search", accent=True, at=A("c02", "where"))
cue(type="bench", t0=S("c03"), t1=E("c03") + 0.05, tag="Supreme Court of India · 6 November 2026",
    judges=[{"name": "Justice P.S. Narasimha", "photo": "../brand/judges/pamidighantam_sri_narasimha.jpg", "at": A("c03", "honourable")},
            {"name": "Justice R. Mahadevan", "photo": "../brand/judges/r_mahadevan.jpg", "at": A("c03", "honourable", 2)}])

# ── 2 · parents in PSUs ──────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=S("c04"), t1=E("c04") + 0.05, at=A("c04", "case"), tag="SUPREME COURT OF INDIA · 06.11.2026",
    cases=[{"name": "Union of India & Ors. v. Rohith Nathan and Anr., etc.", "cite": "2026 INSC 1201 · M.A. 3313-3315/2026 in C.A. 2827-2829/2018"}])
cue(type="timeline", t0=S("c04"), t1=E("c04") + 0.05,
    nodes=[{"label": "CIVIL SERVICES EXAM", "value": "cleared", "sub": "OBC candidates · parents in PSUs", "at": A("c04", "civil")},
           {"label": "PSU POSTS vs GOVT POSTS", "value": "no equivalence", "sub": "not formally determined", "tone": "stop", "at": A("c04", "equivalence")}])
cue(type="timeline", t0=S("c05"), t1=E("c05") + 0.05,
    nodes=[{"label": "PERSONNEL DEPARTMENT", "value": "creamy layer", "sub": "parents' income · 1993 OM + 2004 letter", "tone": "stop", "at": A("c05", "income")},
           {"label": "THE TRIBUNAL (CAT)", "value": "for them", "sub": "orders in the candidates' favour", "at": A("c05", "tribunal")},
           {"label": "THREE HIGH COURTS", "value": "upheld", "sub": "Madras · Delhi · Kerala", "at": A("c05", "three")}])

# ── 3 · after the March ruling ───────────────────────────────────────────────────────────────────────────────────────
cue(type="list", t0=S("c06"), t1=E("c06") + 0.05, head="Supreme Court · 11 March 2026", head_at=S("c06") + 0.05,
    items=[{"n": 1, "text": "The government's civil appeals: dismissed", "at": A("c06", "dismissed")},
           {"n": 2, "text": "The candidates: within the OBC non-creamy layer", "at": A("c06", "appeals")},
           {"n": 3, "text": "No mechanical exclusion based on salary income", "at": A("c06", "mechanical")},
           {"n": 4, "text": "To be implemented within six months", "at": A("c06", "months")}])
cue(type="compare", t0=S("c07"), t1=E("c07") + 0.05, head="The government's applications", head_at=S("c07") + 0.05,
    cols=[{"title": "The government", "icon": "landmark", "at": A("c07", "government")}, {"title": "The candidates", "icon": "users", "at": A("c07", "candidates")}],
    rows=[{"cells": ["Do not reopen completed selections", "An attempt to bypass review, a rehearing"], "cells_at": [A("c07", "completed"), A("c07", "candidates")]},
          {"cells": ["Two years to fix equivalence of posts", "Equivalence not done despite assurances"], "cells_at": [A("c07", "years"), A("c07", "called")]}])

# ── 4 · before the verdict: the LawWorld request ─────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c08"), t1=A("c08", "follow") - 0.05, text="The verdict is next. First, a quick request…", icon="scale", accent=True, at=A("c08", "decided"))
cue(type="list", t0=A("c08", "follow") - 0.05, t1=E("c08") + 0.05, head="Follow LawWorld · lawworld.ai", head_at=A("c08", "follow"),
    items=[{"n": 1, "text": "Search SC and High Court judgments, cited to source", "at": A("c08", "india's")},
           {"n": 2, "text": "Draft petitions, plaints and notices with AI", "at": A("c08", "platform")},
           {"n": 3, "text": "Sign up free · ₹200 AI credit included", "at": A("c08", "advocates")}])

# ── 5 · what the Court held ──────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "service") - 0.05, text="What did the Supreme Court decide?", icon="scale", accent=True, at=A("c09", "finally"))
cue(type="point", t0=A("c09", "service") - 0.05, t1=E("c09") + 0.05, text="“…the creamy layer principle, as interpreted in the said judgment, shall govern the allocation of services to OBC candidates selected through the Civil Services Examination, 2025.”", icon="quote", accent=True, at=A("c09", "pending"))
cue(type="list", t0=S("c10"), t1=A("c10", "court") - 0.05, head="Para 18 · also clarified", head_at=S("c10") + 0.05,
    items=[{"n": 1, "text": "Ruling alone: no ground to reopen past selections", "at": A("c10", "selections")},
           {"n": 2, "text": "After 11 March: the 1993 OM, as interpreted", "at": A("c10", "ruling")},
           {"n": 3, "text": "Pending claims of others: on their own merits", "at": A("c10", "reopened")}])
cue(type="verdicts", t0=A("c10", "court") - 0.05, t1=E("c10") + 0.05,
    rows=[{"text": "CSE-2025 allocation on the pre-March criteria", "ok": False, "at": A("c10", "court")},
          {"text": "A court-set timeline for equivalence of posts", "ok": False, "at": A("c10", "timeline")},
          {"text": "Policy: for the executive and the legislature", "ok": True, "at": A("c10", "posts")},
          {"text": "Time to comply extended by two months", "ok": True, "at": A("c10", "months")}])

MUSIC = {"file": "audio/bed_mixkit738_140s.mp3", "target_lufs": -21}   # owner 02-11-2026: trending-style royalty-free bed, audible under the voice
