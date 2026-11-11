# Sri Sujit Das & Ors. etc. v. Union of India, 2026 INSC 1195, Criminal Appeal Nos. 5283-5285 of 2026 (from SLP (Crl.) Nos. 12451-12453
# of 2026), Supreme Court of India (Ujjal Bhuyan J. wrote it, Atul S. Chandurkar J.; pronounced 05.11.2026; REPORTABLE on page 1):
# panel cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND). Appeal number: blank on the PDF's page 1, taken
# from the sci.gov.in "Latest Judgments" listing ("Crl.A. No. 5283-5285/2026").
# HOOK format (split/JUDGMENT_HOOK_FORMAT.md): c01 hook question (spoken to everyone, no "Advocates,"), c02 curiosity, c03 "Hi, I'm
# Ravishankar" + bench, c04-c05 the timeline, c06-c07 the bail refusal and both sides, c08 the LawWorld request, c09-c10 the verdict.
# Facts (para): Tripura HC common order 29.04.2026 refused regular bail to the three appellants (2, 3), Section 37 NDPS rigour (7);
# 29.09.2025: four persons intercepted with a truck, tablets recovered, field-tested, NDPS case registered then and there (5, 9.2, 9.4,
# 65); intercepted at 2 pm, liberty curtailed from then, under the search team's control (65); search completed 5 pm at the Customs
# Division office (11.2, 65); shown formally arrested 30.09.2025 at 11:00 am / 11:15 am (11.10, 65); produced before the Judicial
# Magistrate 30.09.2025 at 4:45 pm, remanded to judicial custody (65). The 24-hour point was not argued before the HC; raised at the SC
# hearing of 21.09.2026; IO directed to file an affidavit (10). Appellants: liberty completely curtailed at 2 pm, so the 24 hours ran
# from then (12, 12.1). Union (IO's affidavit, ASG): "merely intercepted ... and not formally detained" (11.5), the interval for the
# statutory formalities (search and seizure, weighing, interrogation, travel) cannot be counted (11.5, 13.5, 13.7); even from 5 pm,
# within 24 hours (13.6, 13.10). High Courts divided (32-41). Article 22(2) text (16): produced before the nearest magistrate within 24
# hours, journey time excluded; only that time may be excluded (16.1). Held: 24 hours run from detention when liberty is curtailed (58,
# 64); arrest for Article 22(2) at 2 pm on 29.09.2025, production due before 2 pm on 30.09.2025, clear breach vitiating the arrest
# (66); 18 unexplained hours (5 pm to 11 am) not a reasonable period, s.58 BNSS / s.57 CrPC (67). 69(i) quoted verbatim on the c09
# card; 69(ii)/(vi) release forthwith on a breach; 69(iv) Aryaman Pattnayak (Orissa), Kannan (Madras), Arun K. Thomas (Kerala) not
# the correct law; 69(vi) the Magistrate records the actual date and time of detention; 69(viii) breach of Article 22(2) and s.58 BNSS;
# 69(ix) HC order set aside, produced before the Special Court within 7 days, then bail on terms; appeals allowed (71).
# Names: only the cause title on the cite card; no accused's name in speech; no drug name or quantity anywhere; no accusation against
# the officers. List lines <= 52 chars. Bench photos: brand/judges/ujjal_bhuyan.jpg, brand/judges/atul_s_chandurkar.jpg (official).
FORMAT = "hook"   # build_course_plan.py: no opening sting, 15-frame lead (the cover), name tag on the "Ravishankar" clip

def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
ENDCARD = {"title": "When does the 24-hour clock start?", "line": "From detention, when liberty is curtailed, not from the formal arrest: Article 22(2)", "sub": "LawWorld: legal research for advocates"}

# ── 1 · when does the clock start? (hook, curiosity, intro) ──────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "officers"), text="Stopped and held at 2 PM, arrest written down the next morning. When does the 24-hour clock start?", hl="When does the 24-hour clock start?")
cue(type="list", t0=S("c02"), t1=A("c02", "so") - 0.05, head="Article 22(2) · the 24-hour rule", head_at=S("c02") + 0.05,
    items=[{"n": 1, "text": "Before the nearest Magistrate within 24 hours", "at": A("c02", "magistrate")},
           {"n": 2, "text": "Only the journey time to the court is excluded", "at": A("c02", "arrest")},
           {"n": 3, "text": "High Courts differed: from detention or arrest?", "at": A("c02", "differed")}])
cue(type="point", t0=A("c02", "so") - 0.05, t1=E("c02") + 0.05, text="So who is right?", icon="search", accent=True, at=A("c02", "who"))
cue(type="bench", t0=S("c03"), t1=E("c03") + 0.05, tag="Supreme Court of India · 5 November 2026",
    judges=[{"name": "Justice Ujjal Bhuyan", "photo": "../brand/judges/ujjal_bhuyan.jpg", "at": A("c03", "honourable")},
            {"name": "Justice Atul S. Chandurkar", "photo": "../brand/judges/atul_s_chandurkar.jpg", "at": A("c03", "honourable", 2)}])

# ── 2 · stopped at two ───────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=S("c04"), t1=E("c04") + 0.05, at=A("c04", "officers"), tag="SUPREME COURT OF INDIA · 05.11.2026",
    cases=[{"name": "Sri Sujit Das & Ors. etc. v. Union of India", "cite": "2026 INSC 1195 · Criminal Appeal Nos. 5283-5285 of 2026"}])
cue(type="timeline", t0=S("c04"), t1=E("c04") + 0.05,
    nodes=[{"label": "INTERCEPTED", "value": "2:00 PM", "sub": "29 Sep 2025 · four men and a truck", "at": A("c04", "intercepted")},
           {"label": "CONTRABAND SEIZED", "value": "on the spot", "sub": "field-tested · NDPS case registered", "at": A("c04", "seized")}])
cue(type="timeline", t0=S("c05"), t1=E("c05") + 0.05,
    nodes=[{"label": "SEARCH COMPLETED", "value": "5:00 PM", "sub": "29 Sep · at the Customs office", "at": A("c05", "search")},
           {"label": "ARREST SHOWN", "value": "11:00 AM", "sub": "30 Sep · the others at 11:15 AM", "at": A("c05", "shown")},
           {"label": "BEFORE THE MAGISTRATE", "value": "4:45 PM", "sub": "30 Sep · judicial custody", "at": A("c05", "magistrate")}])

# ── 3 · detained, or arrested? ──────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c06"), t1=A("c06", "in", 2) - 0.05, text="Tripura High Court, 29 April 2026: regular bail refused · the Section 37 NDPS Act bar", icon="landmark", accent=True, at=A("c06", "refused"))
cue(type="point", t0=A("c06", "in", 2) - 0.05, t1=E("c06") + 0.05, text="Supreme Court, 21 September 2026: a new point, not argued in the High Court", icon="clock", accent=True, at=A("c06", "new"))
cue(type="compare", t0=S("c07"), t1=E("c07") + 0.05, head="Detained at 2 PM, or arrested next day?", head_at=S("c07") + 0.05,
    cols=[{"title": "The appellants", "icon": "scale", "at": A("c07", "they")}, {"title": "The Union of India", "icon": "landmark", "at": A("c07", "government")}],
    rows=[{"cells": ["Liberty curtailed from 2 PM", "Only intercepted, not detained"], "cells_at": [A("c07", "curtailed"), A("c07", "intercepted")]},
          {"cells": ["Produced at 4:45 PM next day: too late", "Search, weighing, questioning: not counted"], "cells_at": [A("c07", "missed"), A("c07", "formalities")]}])

# ── 4 · before the verdict: the LawWorld request ─────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c08"), t1=A("c08", "follow") - 0.05, text="The verdict is next. First, a quick request…", icon="scale", accent=True, at=A("c08", "decided"))
cue(type="list", t0=A("c08", "follow") - 0.05, t1=E("c08") + 0.05, head="Follow LawWorld · lawworld.ai", head_at=A("c08", "follow"),
    items=[{"n": 1, "text": "Search SC and High Court judgments, cited to source", "at": A("c08", "india's")},
           {"n": 2, "text": "Draft petitions, plaints and notices with AI", "at": A("c08", "platform")},
           {"n": 3, "text": "Sign up free · ₹200 AI credit included", "at": A("c08", "advocates")}])

# ── 5 · what the Court held ──────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "twenty") - 0.05, text="What did the Supreme Court decide?", icon="scale", accent=True, at=A("c09", "finally"))
cue(type="point", t0=A("c09", "twenty") - 0.05, t1=E("c09") + 0.05, text="“…would commence from the date and time of detention of the person detained when his liberty stands curtailed and not from the time of his formal arrest”", icon="quote", accent=True, at=A("c09", "twenty"))
cue(type="list", t0=S("c10"), t1=A("c10", "here") - 0.05, head="Article 22(2) · also held", head_at=S("c10") + 0.05,
    items=[{"n": 1, "text": "Magistrate records the actual time of detention", "at": A("c10", "magistrates")},
           {"n": 2, "text": "24 hours crossed: released forthwith", "at": A("c10", "record")},
           {"n": 3, "text": "Aryaman, Kannan, Arun K. Thomas: not correct law", "at": A("c10", "time")}])
cue(type="verdicts", t0=A("c10", "here") - 0.05, t1=E("c10") + 0.05,
    rows=[{"text": "Union's plea: clock starts at the formal arrest", "ok": False, "at": A("c10", "here")},
          {"text": "Article 22(2) breached · 18 hours unexplained", "ok": True, "at": A("c10", "missed")},
          {"text": "HC order set aside · bail on terms", "ok": True, "at": A("c10", "released")}])

MUSIC = {"file": "audio/bed_mixkit738_140s.mp3", "target_lufs": -21}   # owner 02-11-2026: trending-style royalty-free bed, audible under the voice
