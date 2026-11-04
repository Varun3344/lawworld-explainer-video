# Mary Victoria v. Ministry of External Affairs, Government of India & Ors., WP(C) No. 35189 of 2025, High Court of Kerala
# (P.V. Kunhikrishnan J.; INTERIM order of 28.10.2026 adding directions to the interim order of 22.10.2026, posted to 26.11.2026;
# "CR" on pages 3-4): panel cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND).
# HOOK format (split/JUDGMENT_HOOK_FORMAT.md): c01 hook question (spoken to everyone, no "Advocates,"), c02 curiosity, c03 "Hi, I'm
# Ravishankar" + bench, c04-c05 the death and the two relatives, c06-c07 the stalemate and the 22.10 order, c08 the LawWorld request,
# c09-c10 the interim directions.
# Facts (para): body waiting since 26.03.2025 in a forensic laboratory, Ajman; 22.10.2026 interim order to repatriate; posted 26.11.2026
# (1); aged 71, died 26.03.2025 in the UAE; MSK Sheikh Khalifa Hospital, Ajman; petitioner = his elder sister's daughter; not married (4);
# petitioner: repatriate to Kerala, burial at the family tomb, St. Andrew's Church, Sasthamcotta, Kollam; the nephew (Addl. R4): funeral
# rites in the UAE itself; two conflicting views, body kept in the UAE (5); MEA and the Consulate: contradictory demands, not in a
# position to do the needful (6); 22.10.2026: niece and nephew among the legal heirs; no objection to repatriation; MEA and the Consulate
# to repatriate forthwith; the petitioner pays for the time being (7); that order did not address the place of burial (8); 1 1/2 years in
# a forensic lab; "A dead body deserves no label, but it deserves respect and dignity. This is part of the right under Article 21 of the
# Constitution of India." (9); the Court need not decide the relatives' disagreement, it steps in for a decent burial (10, 12);
# directions: police ensure no law-and-order problem and a dignified, decent burial; burial at St. Andrew's Church, Sasthamcotta, with
# the Church's consent; completed within four days of the petitioner receiving the body; the DMO, Kollam preserves the body till then;
# "Post on 26.11.2026" (13). Names: only the cause title on the cite card; no side taken in the family dispute (the nephew's claims
# (5), the property remark (11) and the attend-but-don't-disrupt line (12) are on no card). List lines <= 52 chars.
# Bench photo: brand/judges/pv_kunhikrishnan.jpg (the court's own portrait, highcourtofkerala.nic.in/images/PRjudges/pvkk.jpg via the
# Wayback Machine, 13.04.2020; matches the current highcourt.kerala.gov.in present-judges thumbnail).
FORMAT = "hook"   # build_course_plan.py: no opening sting, 15-frame lead (the cover), name tag on the "Ravishankar" clip

def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
ENDCARD = {"title": "Relatives disagree: who ensures the burial?", "line": "For now: burial within four days of her receiving the body, the police to ensure peace and dignity · the case continues on 26 November", "sub": "LawWorld: legal research for advocates"}

# ── 1 · a body waiting abroad (hook, curiosity, intro) ───────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "dies"), text="Relatives can't agree where to bury him. The body waits a year and a half. Who must step in?", hl="Who must step in?")
cue(type="list", t0=S("c02"), t1=A("c02", "so") - 0.05, head="Ajman, UAE · a body waiting", head_at=S("c02") + 0.05,
    items=[{"n": 1, "text": "An Indian, aged 71, died in the UAE: March 2025", "at": A("c02", "happened")},
           {"n": 2, "text": "October 2026: still not buried", "at": A("c02", "october")},
           {"n": 3, "text": "Still in the forensic lab, Ajman", "at": A("c02", "forensic")}])
cue(type="point", t0=A("c02", "so") - 0.05, t1=E("c02") + 0.05, text="So what can a court do?", icon="search", accent=True, at=A("c02", "court"))
cue(type="bench", t0=S("c03"), t1=E("c03") + 0.05, tag="Kerala High Court · 28 October 2026",
    judges=[{"name": "Justice P.V. Kunhikrishnan", "photo": "../brand/judges/pv_kunhikrishnan.jpg", "at": A("c03", "honourable")}])

# ── 2 · two relatives, two plans ─────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=S("c04"), t1=E("c04") + 0.05, at=A("c04", "died"), tag="HIGH COURT OF KERALA · 28.10.2026",
    cases=[{"name": "Mary Victoria v. Ministry of External Affairs & Ors.", "cite": "WP(C) No. 35189 of 2025 · interim order"}])
cue(type="timeline", t0=S("c04"), t1=E("c04") + 0.05,
    nodes=[{"label": "DIED IN THE UAE", "value": "26 March 2025", "sub": "aged 71 · unmarried", "at": A("c04", "died")},
           {"label": "FORENSIC LAB, AJMAN", "value": "body kept", "sub": "MSK Sheikh Khalifa Hospital", "at": A("c04", "ajman")}])
cue(type="compare", t0=S("c05"), t1=E("c05") + 0.05, head="Two legal heirs, two plans", head_at=S("c05") + 0.05,
    cols=[{"title": "His niece · the petitioner", "icon": "user", "at": A("c05", "niece")}, {"title": "His nephew", "icon": "user", "at": A("c05", "nephew")}],
    rows=[{"cells": ["Bring him home to Kerala", "Funeral rites in the UAE"], "cells_at": [A("c05", "wanted"), A("c05", "consulate")]},
          {"cells": ["Family tomb, St. Andrew's Church, Kollam", "Request to the Indian Consulate, Dubai"], "cells_at": [A("c05", "tomb"), A("c05", "rites")]}])

# ── 3 · home, but where? ─────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c06"), t1=E("c06") + 0.05, head="Stuck for a year and a half", head_at=S("c06") + 0.05,
    steps=[{"label": "Contradictory demands", "sub": "the niece and the nephew", "icon": "user", "at": A("c06", "contradictory")},
           {"label": "Ministry and consulate", "sub": "“not in a position” to act", "icon": "landmark", "at": A("c06", "ministry")},
           {"label": "Body stays in Ajman", "sub": "the forensic lab, UAE", "icon": "info", "at": A("c06", "body")}])
cue(type="timeline", t0=S("c07"), t1=E("c07") + 0.05,
    nodes=[{"label": "22 OCTOBER 2026", "value": "bring him home", "sub": "no objection from either side · niece pays for now", "at": A("c07", "october")},
           {"label": "STILL OPEN", "value": "where to bury?", "sub": "the order did not say", "tone": "red", "at": A("c07", "say")}])

# ── 4 · before the verdict: the LawWorld request ─────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c08"), t1=A("c08", "follow") - 0.05, text="The verdict is next. First, a quick request…", icon="scale", accent=True, at=A("c08", "decided"))
cue(type="list", t0=A("c08", "follow") - 0.05, t1=E("c08") + 0.05, head="Follow LawWorld · lawworld.ai", head_at=A("c08", "follow"),
    items=[{"n": 1, "text": "Search SC and High Court judgments, cited to source", "at": A("c08", "india's")},
           {"n": 2, "text": "Draft petitions, plaints and notices with AI", "at": A("c08", "platform")},
           {"n": 3, "text": "Sign up free · ₹200 AI credit included", "at": A("c08", "advocates")}])

# ── 5 · the interim directions ───────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "interim") - 0.05, text="What did the High Court decide?", icon="scale", accent=True, at=A("c09", "finally"))
cue(type="point", t0=A("c09", "interim") - 0.05, t1=E("c09") + 0.05, text="“A dead body deserves no label, but it deserves respect and dignity. This is part of the right under Article 21 of the Constitution of India.”", icon="quote", accent=True, at=A("c09", "dead"))
cue(type="verdicts", t0=S("c10"), t1=A("c10", "case") - 0.05,
    rows=[{"text": "Burial within 4 days of receiving the body, at St. Andrew's Church, Sasthamcotta, with its consent", "ok": True, "at": A("c10", "burial")},
          {"text": "District Medical Officer, Kollam: preserve the body till then", "ok": True, "at": A("c10", "receiving")},
          {"text": "Police: no law-and-order problem, a dignified burial", "ok": True, "at": A("c10", "police")}])
cue(type="point", t0=A("c10", "case") - 0.05, t1=E("c10") + 0.05, text="Interim order · the case continues on 26 November 2026", icon="calendar", accent=True, at=A("c10", "continues"))

MUSIC = {"file": "audio/bed_mixkit738_140s.mp3", "target_lufs": -21}   # owner 02-11-2026: trending-style royalty-free bed, audible under the voice
