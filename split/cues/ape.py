# Suo Motu PIL on the safety of Advocates, High Court of Karnataka at Bengaluru, oral order of 03.11.2026 (D K Singh J., H. Shanthi
# Bhushan J.); notice returnable and listed on 08.12.2026. Facts and paragraph numbers: see the header of split/scripts/<set>.txt.
# HOOK format. Names of the deceased/injured Advocates never shown or spoken. Bench photos: brand/judges/dk_singh.jpg, h_shanthi_bhushan.jpg.
FORMAT = "hook"
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)
CITE_B = 110
PLAIN_BG = True
ENDCARD = {"title": "Lawyers under attack: the High Court steps in", "line": "A suo motu PIL on the safety of Advocates · police stations are no forum for civil disputes · listed on 8 December 2026", "sub": "LawWorld: legal research for advocates"}

# ── 1 · who protects the lawyers? ─────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "october"), text="Two lawyers killed, a senior lawyer attacked. Can the High Court act on its own?", hl="Can the High Court act on its own?")
cue(type="list", t0=S("c02"), t1=A("c02", "so") - 0.05, head="A second complaint", head_at=S("c02") + 0.05,
    items=[{"n": 1, "text": "Police stations acting like courts", "at": A("c02", "police")},
           {"n": 2, "text": "Settling property and contract disputes", "at": A("c02", "settling")}])
cue(type="point", t0=A("c02", "so") - 0.05, t1=E("c02") + 0.05, text="What did the High Court do?", icon="search", accent=True, at=A("c02", "what"))
cue(type="bench", t0=S("c03"), t1=E("c03") + 0.05, tag="Karnataka High Court · 3 November 2026",
    judges=[{"name": "Justice D K Singh", "photo": "../brand/judges/dk_singh.jpg", "at": A("c03", "honourable")},
            {"name": "Justice H. Shanthi Bhushan", "photo": "../brand/judges/h_shanthi_bhushan.jpg", "at": A("c03", "honourable", 2)}])

# ── 2 · the Bar's grievance ───────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=S("c04"), t1=E("c05") + 0.05, at=A("c04", "association"), tag="HIGH COURT OF KARNATAKA · 03.11.2026",
    cases=[{"name": "In re: safety of Advocates (Suo Motu PIL)", "cite": "Oral order of 03.11.2026 · listed on 08.12.2026"}])
cue(type="point", t0=A("c04", "threats") - 0.05, t1=E("c04") + 0.05, text="Rising threats, assaults and violence against lawyers", icon="scale", accent=True, at=A("c04", "threats"))
cue(type="list", t0=S("c05"), t1=E("c05") + 0.05, head="3 November 2026 · lawyers abstain", head_at=S("c05") + 0.05,
    items=[{"n": 1, "text": "Across Karnataka, away from court work", "at": A("c05", "abstained")},
           {"n": 2, "text": "A stronger Advocates Protection Act", "at": A("c05", "stronger")},
           {"n": 3, "text": "Safety at work", "at": A("c05", "safety")}])
cue(type="list", t0=S("c06"), t1=E("c06") + 0.05, head="The Bar's second grievance", head_at=S("c06") + 0.05,
    items=[{"n": 1, "text": "Police stations as parallel courts", "at": A("c06", "parallel")},
           {"n": 2, "text": "Settling civil disputes at the station", "at": A("c06", "civil")},
           {"n": 3, "text": "Despite senior officers' instructions", "at": A("c06", "senior")}])

# ── 3 · why it matters ────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c07"), t1=A("c07", "attack") - 0.05, text="“Advocates are not merely representatives of litigants; they are officers of the Court.”", icon="quote", accent=True, at=A("c07", "officers"))
cue(type="point", t0=A("c07", "attack") - 0.05, t1=E("c07") + 0.05, text="An attack on an Advocate “cannot be viewed as an isolated incident”", icon="scale", accent=True, at=A("c07", "attack"))

# ── 4 · before the verdict: the LawWorld request ─────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c08"), t1=A("c08", "follow") - 0.05, text="The verdict is next. First, a quick request…", icon="scale", accent=True, at=A("c08", "decided"))
cue(type="list", t0=A("c08", "follow") - 0.05, t1=E("c08") + 0.05, head="Follow LawWorld · lawworld.ai", head_at=A("c08", "follow"),
    items=[{"n": 1, "text": "Search SC and High Court judgments, cited to source", "at": A("c08", "india's")},
           {"n": 2, "text": "Draft petitions, plaints and notices with AI", "at": A("c08", "platform")},
           {"n": 3, "text": "Sign up free · ₹200 AI credit included", "at": A("c08", "advocates")}])

# ── 5 · what the Court ordered ───────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "ordered") - 0.05, text="What did the High Court decide?", icon="scale", accent=True, at=A("c09", "finally"))
cue(type="point", t0=A("c09", "ordered") - 0.05, t1=A("c09", "said") - 0.05, text="Registry: register a suo motu public interest litigation", icon="file-text", accent=True, at=A("c09", "ordered"))
cue(type="point", t0=A("c09", "said") - 0.05, t1=E("c09") + 0.05, text="“A Police Station cannot be converted into a forum for adjudication of civil rights or settlement of disputes…”", icon="quote", accent=True, at=A("c09", "police"))
cue(type="verdicts", t0=S("c10"), t1=E("c10") + 0.05,
    rows=[{"text": "State and DG&IGP: place the existing SOPs", "ok": True, "at": A("c10", "file")},
          {"text": "Examine strengthening the Advocates Protection Act", "ok": True, "at": A("c10", "study")},
          {"text": "Police: case-wise details of every Advocate's murder", "ok": True, "at": A("c10", "detail")},
          {"text": "Next hearing: 8 December 2026", "ok": True, "at": A("c10", "hearing")}])

MUSIC = {"file": "audio/bed_mixkit738_140s.mp3", "target_lufs": -21}
