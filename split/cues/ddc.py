# Sau. Kamalbai Waman Patil v. The State of Maharashtra, 2026 INSC 1196, Criminal Appeal No. 118 of 2018, Supreme Court of India
# (Atul S. Chandurkar J. wrote it, Ujjal Bhuyan J.; pronounced 05.11.2026, REPORTABLE): panel cues, run by split/build_course_plan.py
# (helpers: at S E cue fx have r3 PEND). HOOK format (split/JUDGMENT_HOOK_FORMAT.md): c01 hook question (spoken to everyone, no
# "Advocates,"), c02 curiosity, c03 "Hi, I'm Ravishankar" + bench, c04-c05 the case and the three statements, c06-c07 the two courts
# below, c08 the LawWorld request, c09-c10 the verdict. DRAFT 06-11-2026, awaiting the owner's yes.
# Facts (para): conviction by the Bombay HC, Aurangabad Bench, s.302 IPC, RI for life + Rs.25,000 fine, reversing the Sessions
# Court's acquittal (1); prosecution's case: A1 husband, A2 his father, A3 his mother (the appellant), A4 his younger brother;
# alleged ill-treatment for having no issue, dowry demand; alleged that on 10.04.2005 ~10 a.m. all four set her on fire; taken to
# the Civil Hospital by Vishwas Desle; statement at 10.30 a.m. implicated the appellant; further statements by ASI Prakash Wagh and
# the Special Executive Magistrate; died 15.04.2005 (2); charges ss.498A, 342, 406, 302 r/w 34 (2, 14). Dying declarations, all
# 10.04.2005: Ex-56 medico-legal case papers, the patient's history recorded by the Medical Officer PW-7 (7, 10, 21, 22), the HC's
# "initial" one (10): set on fire by the appellant (9); Ex-44 by ASI PW-4 (4; police ~1.40 p.m., 22) and Ex-48 by the Special
# Executive Magistrate PW-5 (5; ~2.15 p.m., 22): A1 and A4 tied her, the appellant poured kerosene, A2 set her on fire (4, 25) -
# i.e. set on fire by her father-in-law (9). Sessions Court: declarations inconsistent; Vishwas Desle not examined; no neighbours
# examined; all acquitted (9). Vishwas Patil (= Desle), a Police Patil, put out the fire, first at the house, admitted her to
# hospital; not examined, no reason given (7, 8, 23). HC: Ex-56 voluntary; per the defence the appellant alone was in the house and
# failed to explain; Ex-44/48 discarded; she alone convicted u/s 302, life; A1, A2, A4 acquittal upheld; 498A/342/406 not proved;
# acquittal held illegal and perverse (10). Held: only a joint s.302 r/w 34 charge, never an independent s.302 charge - "a charge that
# was never framed against her" (14, 15, 18); Abhishek Sharma principles on multiple dying declarations (20); conviction rested
# solely on PW-7 and Ex-56 (21); "Exhibit-56 without any corroboration cannot be the sole basis to reverse the acquittal" (24); s.106
# Evidence Act cannot fill the gap - initial burden not discharged (27); para 29: the Sessions Court was correct - "in view of
# inconsistency in the three dying declarations, the appellant was entitled to the benefit of doubt"; "The presumption of innocence
# in favour of the appellant was in fact enhanced by her acquittal by the Sessions Court"; its view "could not be said to be either
# perverse or illegal"; para 30: the HC's judgment in Criminal Appeal No. 63 of 2008 dated 28.09.2017 quashed, acquitted of s.302 IPC,
# set free forthwith if not required in any other case, appeal allowed.
# Names: only the cause title on the cite card; the dowry / ill-treatment allegations shown as the prosecution's (c04).
# No graphic detail on any card (no kerosene, rope or burn percentage). List lines <= 52 chars. Official sci.gov.in portraits.
FORMAT = "hook"   # build_course_plan.py: no opening sting, 15-frame lead (the cover), name tag on the "Ravishankar" clip

def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
ENDCARD = {"title": "Three dying declarations that don't match?", "line": "Here she got the benefit of doubt: one uncorroborated statement could not reverse her acquittal", "sub": "LawWorld: legal research for advocates"}

# ── 1 · which one is true? (hook, curiosity, intro) ──────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "before"), text="One statement names only the mother-in-law. Two name all four in the family. Which one would you believe?", hl="Which one would you believe?")
cue(type="flow", t0=S("c02"), t1=A("c02", "so") - 0.05, head="One record, two results", head_at=S("c02") + 0.05,
    steps=[{"label": "Sessions Court", "sub": "all four acquitted", "icon": "scale", "at": A("c02", "sessions")},
           {"label": "High Court", "sub": "believes only the first statement", "icon": "landmark", "at": A("c02", "believed")},
           {"label": "Life imprisonment", "sub": "the mother-in-law alone", "icon": "gavel", "at": A("c02", "gave")}])
cue(type="point", t0=A("c02", "so") - 0.05, t1=E("c02") + 0.05, text="So who was right?", icon="search", accent=True, at=A("c02", "so"))
cue(type="bench", t0=S("c03"), t1=E("c03") + 0.05, tag="Supreme Court of India · 5 November 2026",
    judges=[{"name": "Justice Ujjal Bhuyan", "photo": "../brand/judges/ujjal_bhuyan.jpg", "at": A("c03", "honourable")},
            {"name": "Justice Atul S. Chandurkar", "photo": "../brand/judges/atul_s_chandurkar.jpg", "at": A("c03", "honourable", 2)}])

# ── 2 · three statements ─────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=S("c04"), t1=E("c04") + 0.05, at=A("c04", "prosecution"), tag="SUPREME COURT OF INDIA · 05.11.2026",
    cases=[{"name": "Sau. Kamalbai Waman Patil v. The State of Maharashtra", "cite": "2026 INSC 1196 · Criminal Appeal No. 118 of 2018"}])
cue(type="timeline", t0=S("c04"), t1=E("c04") + 0.05,
    nodes=[{"label": "THE PROSECUTION ALLEGED", "value": "ill-treatment", "sub": "over dowry, and no child", "at": A("c04", "dowry")},
           {"label": "10 APRIL 2005", "value": "burns at home", "sub": "she died on 15 April 2005", "at": A("c04", "burns")}])
cue(type="list", t0=S("c05"), t1=E("c05") + 0.05, head="Three statements · 10 April 2005", head_at=S("c05") + 0.05,
    items=[{"n": 1, "text": "Doctor's record, Ex. 56: only the mother-in-law", "at": A("c05", "doctor")},
           {"n": 2, "text": "Police officer, Ex. 44: all four in the family", "at": A("c05", "police")},
           {"n": 3, "text": "Spl. Executive Magistrate, Ex. 48: all four", "at": A("c05", "magistrate")},
           {"n": 4, "text": "In both, the father-in-law sets the fire", "at": A("c05", "named")}])

# ── 3 · two courts, two views ────────────────────────────────────────────────────────────────────────────────────────
cue(type="compare", t0=S("c06"), t1=E("c07") + 0.05, head="Acquitted, then convicted", head_at=S("c06") + 0.05,
    cols=[{"title": "Sessions Court", "icon": "scale", "at": A("c06", "sessions")}, {"title": "High Court", "icon": "landmark", "at": A("c07", "high")}],
    rows=[{"cells": ["The statements do not match", "Doctor's record: voluntary, believed"], "cells_at": [A("c06", "match"), A("c07", "voluntary")]},
          {"cells": ["The man who took her to hospital: not examined", "Defence: the mother-in-law alone at home"], "cells_at": [A("c06", "witness"), A("c07", "alone")]},
          {"cells": ["No neighbour examined", "She gave no explanation"], "cells_at": [A("c06", "neighbour"), A("c07", "gave")]}])

# ── 4 · before the verdict: the LawWorld request ─────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c08"), t1=A("c08", "follow") - 0.05, text="The verdict is next. First, a quick request…", icon="scale", accent=True, at=A("c08", "decided"))
cue(type="list", t0=A("c08", "follow") - 0.05, t1=E("c08") + 0.05, head="Follow LawWorld · lawworld.ai", head_at=A("c08", "follow"),
    items=[{"n": 1, "text": "Search SC and High Court judgments, cited to source", "at": A("c08", "india's")},
           {"n": 2, "text": "Draft petitions, plaints and notices with AI", "at": A("c08", "platform")},
           {"n": 3, "text": "Sign up free · ₹200 AI credit included", "at": A("c08", "advocates")}])

# ── 5 · what the Court held ──────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "given") - 0.05, text="What did the Supreme Court decide?", icon="scale", accent=True, at=A("c09", "finally"))
cue(type="list", t0=A("c09", "given") - 0.05, t1=E("c09") + 0.05, head="The Sessions Court was right", head_at=A("c09", "given"),
    items=[{"n": 1, "text": "Three dying declarations, not consistent", "at": A("c09", "inconsistency")},
           {"n": 2, "text": "Its view was not perverse or illegal", "at": A("c09", "right")},
           {"n": 3, "text": "She was entitled to the benefit of doubt", "at": A("c09", "entitled")}])
cue(type="point", t0=S("c10"), t1=A("c10", "doctor") - 0.05, text="“The presumption of innocence in favour of the appellant was in fact enhanced by her acquittal by the Sessions Court.”", icon="quote", accent=True, at=A("c10", "acquittal"))
cue(type="verdicts", t0=A("c10", "doctor") - 0.05, t1=E("c10") + 0.05,
    rows=[{"text": "Uncorroborated Ex. 56 as the sole basis", "ok": False, "at": A("c10", "corroboration")},
          {"text": "Convicted alone, on a charge never framed", "ok": False, "at": A("c10", "alone")},
          {"text": "High Court's conviction and life sentence", "ok": False, "at": A("c10", "reverse")},
          {"text": "Acquitted · to be set free forthwith", "ok": True, "at": A("c10", "acquitted")}])

MUSIC = {"file": "audio/bed_mixkit738_140s.mp3", "target_lufs": -21}   # owner 02-11-2026: trending-style royalty-free bed, audible under the voice
