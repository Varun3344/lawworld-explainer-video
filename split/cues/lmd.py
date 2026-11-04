# Renuka Ramnath v. State of Karnataka (Inspector of Legal Metrology, Flying Squad), W.P. No. 18251 of 2021 (GM-RES), 2026:KHC:59939,
# High Court of Karnataka at Bengaluru (V Srishananda J.; oral order 28.10.2026, preliminary hearing; circled "R" on page 1 and on
# the court's Reportable list): panel cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND).
# HOOK format (split/JUDGMENT_HOOK_FORMAT.md): c01 hook question (spoken to everyone, no "Advocates,"), c02 curiosity, c03 "Hi, I'm
# Ravishankar" + bench, c04-c05 the inspection and the complaint, c06-c07 her plea and Section 49, c08 the LawWorld request, c09-c10
# the verdict.
# Facts (para): complaint dated 19.05.2016, C.C. No. 36296/2016, Metropolitan Magistrate, Traffic Court-1, Mayo Hall (cause title, 2);
# private complaint by the Inspector of Legal Metrology: s.18 Legal Metrology Act r/w Rule 18(2), Packaged Commodity Rules 2011 (3.1);
# she is accused no. 3, shown as a non-executive director (3.2); flying squad: violation with the weighing scale, scale seized, action
# initiated (3.3); her plea: s.49 bars prosecuting a non-executive director (4); not directors alone without the company as a party
# (5); the HCGP could not dispute the factual and legal aspects, having regard to s.49 (6); Form No. 32 before the Registrar of
# Companies shows her as a non-executive director (7, 8); s.49(1)(a)(i) nominated person, (ii) else every person in charge of and
# responsible to the company, (b) the company; Explanation (b) "director" (9); held: "a non-executive director cannot be proceeded
# criminally for the alleged violations committed by the company" (10); proceedings quashed qua the petitioner (11); ORDER (12): petition
# allowed; C.C. No. 36296/2016 quashed; no effect on the prosecution's rights as to the others.
# Names: only the cause title on the cite card; the company is not named. List lines <= 52 chars.
# Bench photo: brand/judges/v_srishananda.jpg (official KHC portrait, assets/images/judges/vsnj.jpg on judiciary.karnataka.gov.in,
# "Hon`ble Shri. Justice V Srishananda" on submenujprofile.php?nid=1; fetched 04-11-2026).
FORMAT = "hook"   # build_course_plan.py: no opening sting, 15-frame lead (the cover), name tag on the "Ravishankar" clip

def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
ENDCARD = {"title": "Can a non-executive director be prosecuted?", "line": "Not for the company's alleged Legal Metrology violations: the case was quashed as against her", "sub": "LawWorld: legal research for advocates"}

# ── 1 · just on the board? (hook, curiosity, intro) ──────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "inspectors"), text="A weights and measures violation at a company. Can its non-executive director be prosecuted?", hl="Can its non-executive director be prosecuted?")
cue(type="list", t0=S("c02"), t1=A("c02", "would") - 0.05, head="Company records · Form 32", head_at=S("c02") + 0.05,
    items=[{"n": 1, "text": "Shown as a non-executive director", "at": A("c02", "records")},
           {"n": 2, "text": "Yet made accused no. 3", "at": A("c02", "yet")}])
cue(type="point", t0=A("c02", "would") - 0.05, t1=E("c02") + 0.05, text="Can the case go on against her?", icon="scale", accent=True, at=A("c02", "would"))
cue(type="bench", t0=S("c03"), t1=E("c03") + 0.05, tag="Karnataka High Court · 28 October 2026",
    judges=[{"name": "Justice V. Srishananda", "photo": "../brand/judges/v_srishananda.jpg", "at": A("c03", "honourable")}])

# ── 2 · the weighing scale ───────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=S("c04"), t1=E("c04") + 0.05, at=A("c04", "legal"), tag="HIGH COURT OF KARNATAKA · 28.10.2026",
    cases=[{"name": "Renuka Ramnath v. State of Karnataka", "cite": "2026:KHC:59939 · W.P. No. 18251 of 2021"}])
cue(type="point", t0=S("c04"), t1=E("c04") + 0.05, text="Flying squad visit: a violation found with the weighing scale, the scale seized", icon="search", at=A("c04", "found"))
cue(type="timeline", t0=S("c05"), t1=E("c05") + 0.05,
    nodes=[{"label": "PRIVATE COMPLAINT", "value": "19 May 2016", "sub": "Legal Metrology Act, Section 18", "at": A("c05", "twenty")},
           {"label": "SHE IS NAMED", "value": "Accused no. 3", "sub": "C.C. No. 36296/2016, Traffic Court-1", "tone": "red", "at": A("c05", "named")}])

# ── 3 · who is liable? ───────────────────────────────────────────────────────────────────────────────────────────────
cue(type="list", t0=S("c06"), t1=E("c06") + 0.05, head="Her plea · Section 49", head_at=S("c06") + 0.05,
    items=[{"n": 1, "text": "No prosecution of a non-executive director", "at": A("c06", "bars")},
           {"n": 2, "text": "Not the directors alone, without the company", "at": A("c06", "directors")}])
cue(type="flow", t0=S("c07"), t1=A("c07", "state") - 0.05, head="Section 49(1) · who is liable", head_at=S("c07") + 0.05,
    steps=[{"label": "The nominated person", "sub": "in charge of, and responsible to, the company", "icon": "user-round", "at": A("c07", "nominated")},
           {"label": "If none nominated", "sub": "every person in charge and responsible", "icon": "users", "at": A("c07", "charge")}])
cue(type="point", t0=A("c07", "state") - 0.05, t1=E("c07") + 0.05, text="The State's counsel could not dispute her plea, given Section 49", icon="info", at=A("c07", "state"))

# ── 4 · before the verdict: the LawWorld request ─────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c08"), t1=A("c08", "follow") - 0.05, text="The verdict is next. First, a quick request…", icon="scale", accent=True, at=A("c08", "decided"))
cue(type="list", t0=A("c08", "follow") - 0.05, t1=E("c08") + 0.05, head="Follow LawWorld · lawworld.ai", head_at=A("c08", "follow"),
    items=[{"n": 1, "text": "Search SC and High Court judgments, cited to source", "at": A("c08", "india's")},
           {"n": 2, "text": "Draft petitions, plaints and notices with AI", "at": A("c08", "platform")},
           {"n": 3, "text": "Sign up free · ₹200 AI credit included", "at": A("c08", "advocates")}])

# ── 5 · what the Court held ──────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "under") - 0.05, text="What did the High Court decide?", icon="scale", accent=True, at=A("c09", "finally"))
cue(type="point", t0=A("c09", "under") - 0.05, t1=E("c09") + 0.05, text="“a non-executive director cannot be proceeded criminally for the alleged violations committed by the company”", icon="quote", accent=True, at=A("c09", "under"))
cue(type="point", t0=S("c10"), t1=A("c10", "so") - 0.05, text="Form 32, Registrar of Companies: a non-executive director", icon="file-check", at=A("c10", "form"))
cue(type="verdicts", t0=A("c10", "so") - 0.05, t1=E("c10") + 0.05,
    rows=[{"text": "Her petition: allowed", "ok": True, "at": A("c10", "allowed")},
          {"text": "The case against her: C.C. No. 36296/2016", "ok": False, "at": A("c10", "quashed")},
          {"text": "Prosecution's rights as to others: unaffected", "ok": True, "at": A("c10", "against")}])

MUSIC = {"file": "audio/bed_mixkit738_140s.mp3", "target_lufs": -21}   # owner 02-11-2026: trending-style royalty-free bed, audible under the voice
