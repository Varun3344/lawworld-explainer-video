# State of Himachal Pradesh v. Union of India and others, 2026 INSC 1200, Original Suit No. 2 of 1996 (Article 131, Civil Original
# Jurisdiction), Supreme Court of India (Surya Kant CJI wrote it, Joymalya Bagchi J., V. Mohana J.; dated 06.11.2026; REPORTABLE):
# panel cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND). DRAFT 11-11-2026, awaiting the owner's yes.
# HOOK format (split/JUDGMENT_HOOK_FORMAT.md): c01 hook question (spoken to everyone, no "Advocates,"), c02 curiosity (who owes whom),
# c03 "Hi, I'm Ravishankar" + the three-judge bench, c04-c05 the claim and the 2011 decree, c06-c07 the stalled execution and the Attorney
# General's plan, c08 the LawWorld request, c09-c10 the verdict and the directions.
# Facts (para): Article 131 suit for a share of the Bhakra-Nangal and Beas power against the Union, Punjab, Haryana, Rajasthan and
# Chandigarh (1); suit of 1996 (2, 5.13); Punjab reorganised from 01.11.1966, territory "together with its population" to Himachal (5.8);
# claim of 22.10.1969: 7.19%, the share of composite Punjab's population transferred (5.12); decree of 27.09.2011: 7.19% (3) = 6.095% of
# Bhakra-Nangal, 5.752% Beas I, 2.984% Beas II (5.23); 12% free power refused (5.22); the Union to compute the amount "within six months"
# (5.25); Union's affidavit 05.07.2013: 13,066 MU (8,523 + 3,145 + 1,398), accepted by Himachal, disputed by Punjab and Haryana (5.28);
# Punjab: net Rs. 6,683.68 crores recoverable from Himachal as on 31.03.2026 (14); AG's cashless framework, no direct financial
# transaction between the States (20, 21); Himachal and Haryana agreed in principle on 30.07.2026 and 20.08.2026 (23); Punjab's three
# objections: 1.2 lakh units a day -> 11,094 MU, conversion at the O&M rate of 79 paise, 30 years not 15 (24-26). Held: execution, not a
# reopening of the decree (30); "vague and superficial ... an attempt to relitigate issues already settled" (33); none accepted (32);
# 20 years instead of 15, to ease the burden on the Defendant States (38); directions 41(a)-(f): 13,066 MU; BBMB charges paid by Himachal
# for the year of supply; capital-cost share Rs. 420.77 crores (Punjab 249.23, Haryana 171.55) adjusted at Rs. 3.85 a unit = about
# 1,093 MU; balance about 11,973 MU at about 598 MU a year over 20 lean seasons (October-March), 58:42 Bhakra-Nangal, 60:40 Beas;
# cashless. Para 43 quoted verbatim on the c10 card. List lines <= 52 chars. Bench photos: brand/judges/surya_kant.jpg,
# joymalya_bagchi.jpg, v_mohana.jpg (official sci.gov.in portraits, fetched 11-11-2026).
FORMAT = "hook"   # build_course_plan.py: no opening sting, 15-frame lead (the cover), name tag on the "Ravishankar" clip

def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
ENDCARD = {"title": "Sued in 1996, won its share in 2011. Still waiting?", "line": "Capital cost set off, the rest of the power arrears over 20 lean seasons: the directions are binding", "sub": "LawWorld: legal research for advocates"}

# ── 1 · still waiting? (hook, curiosity, intro) ─────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "state"), text="Sued in 1996 for its share of power. Won it in 2011. So why was it still waiting for its arrears?", hl="still waiting for its arrears?")
cue(type="timeline", t0=S("c02"), t1=A("c02", "who") - 0.05,
    nodes=[{"label": "THE CENTRE'S FIGURE", "value": "13,066 MU", "sub": "Himachal's power arrears, 1966-2011", "at": A("c02", "thirteen")},
           {"label": "PUNJAB'S FIGURE", "value": "₹6,683.68 cr", "sub": "costs it said Himachal owed", "at": A("c02", "six")}])
cue(type="point", t0=A("c02", "who") - 0.05, t1=E("c02") + 0.05, text="So who owes whom?", icon="scale", accent=True, at=A("c02", "who"))
cue(type="bench", t0=S("c03"), t1=E("c03") + 0.05, tag="Supreme Court of India · 6 November 2026",
    judges=[{"name": "Chief Justice Surya Kant", "photo": "../brand/judges/surya_kant.jpg", "at": A("c03", "honourable")},
            {"name": "Justice Joymalya Bagchi", "photo": "../brand/judges/joymalya_bagchi.jpg", "at": A("c03", "justice", 2)},
            {"name": "Justice V. Mohana", "photo": "../brand/judges/v_mohana.jpg", "at": A("c03", "justice", 3)}])

# ── 2 · whose power? ─────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=S("c04"), t1=E("c04") + 0.05, at=A("c04", "punjab"), tag="SUPREME COURT OF INDIA · 06.11.2026",
    cases=[{"name": "State of Himachal Pradesh v. Union of India & Ors.", "cite": "2026 INSC 1200 · Original Suit No. 2 of 1996"}])
cue(type="timeline", t0=S("c04"), t1=E("c04") + 0.05,
    nodes=[{"label": "1 NOVEMBER 1966", "value": "Punjab split", "sub": "territory and people to Himachal", "at": A("c04", "split")},
           {"label": "22 OCTOBER 1969", "value": "the claim", "sub": "a share of Bhakra-Nangal and Beas power", "at": A("c04", "claimed")}])
cue(type="point", t0=S("c05"), t1=A("c05", "in") - 0.05, text="7.19%: the share of composite Punjab's population that went to Himachal", icon="users", accent=True, at=A("c05", "seven"))
cue(type="list", t0=A("c05", "in") - 0.05, t1=E("c05") + 0.05, head="The decree · 27 September 2011", head_at=A("c05", "in"),
    items=[{"n": 1, "text": "7.19% of composite Punjab's share of the power", "at": A("c05", "eleven")},
           {"n": 2, "text": "Bhakra 6.095% · Beas I 5.752% · Beas II 2.984%", "at": A("c05", "granted")},
           {"n": 3, "text": "12% free power as the 'Home State': refused", "at": A("c05", "refused")}])

# ── 3 · a decree stuck ───────────────────────────────────────────────────────────────────────────────────────────────
cue(type="timeline", t0=S("c06"), t1=E("c06") + 0.05,
    nodes=[{"label": "2011 · THE DECREE", "value": "6 months", "sub": "for the Centre to compute the dues", "at": A("c06", "six")},
           {"label": "2013 · THE CENTRE", "value": "13,066 MU", "sub": "Himachal accepted the figure", "at": A("c06", "figure")},
           {"label": "PUNJAB, HARYANA", "value": "disputed", "sub": "the computation", "tone": "red", "at": A("c06", "disputed")}])
cue(type="flow", t0=S("c07"), t1=E("c07") + 0.05, head="Mediation by the Attorney General", head_at=S("c07") + 0.05,
    steps=[{"label": "Attorney General", "sub": "a cashless plan: no payment between States", "icon": "handshake", "at": A("c07", "attorney")},
           {"label": "Himachal, Haryana", "sub": "agreed in principle, July and August 2026", "icon": "circle-check", "at": A("c07", "agreed")},
           {"label": "Punjab", "sub": "objected on three points", "icon": "triangle-alert", "at": A("c07", "punjab")}])

# ── 4 · before the verdict: the LawWorld request ─────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c08"), t1=A("c08", "follow") - 0.05, text="The verdict is next. First, a quick request…", icon="scale", accent=True, at=A("c08", "decided"))
cue(type="list", t0=A("c08", "follow") - 0.05, t1=E("c08") + 0.05, head="Follow LawWorld · lawworld.ai", head_at=A("c08", "follow"),
    items=[{"n": 1, "text": "Search SC and High Court judgments, cited to source", "at": A("c08", "india's")},
           {"n": 2, "text": "Draft petitions, plaints and notices with AI", "at": A("c08", "platform")},
           {"n": 3, "text": "Sign up free · ₹200 AI credit included", "at": A("c08", "advocates")}])

# ── 5 · what the Court held ──────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "punjab's") - 0.05, text="What did the Supreme Court decide?", icon="scale", accent=True, at=A("c09", "finally"))
cue(type="verdicts", t0=A("c09", "punjab's") - 0.05, t1=E("c09") + 0.05,
    rows=[{"text": "Punjab: deduct 1.2 lakh units a day", "ok": False, "at": A("c09", "objections")},
          {"text": "Punjab: convert at today's O&M rate", "ok": False, "at": A("c09", "attempt")},
          {"text": "Punjab: spread it over 30 years", "ok": False, "at": A("c09", "reopen")},
          {"text": "The 2011 decree is executed, not reopened", "ok": True, "at": A("c09", "twenty")}])
cue(type="flow", t0=S("c10"), t1=A("c10", "court") - 0.35, dir="v", head="The settlement · cashless", head_at=S("c10") + 0.05,
    steps=[{"label": "13,066 MU of arrears", "sub": "as the Centre computed them", "icon": "database", "at": A("c10", "himachal's")},
           {"label": "minus ₹420.77 crore capital cost", "sub": "Himachal's 7.19% share · ≈1,093 MU at ₹3.85 a unit", "icon": "indian-rupee", "at": A("c10", "set")},
           {"label": "≈11,973 MU over 20 lean seasons", "sub": "≈598 MU a year, October to March · up from 15", "icon": "calendar", "at": A("c10", "rest")}],
    note={"text": "Himachal pays BBMB charges for each year's power", "icon": "receipt-indian-rupee", "at": A("c10", "seasons")})
cue(type="point", t0=A("c10", "court") - 0.35, t1=E("c10") + 0.05, text="“…the directions issued by this Court are binding and are required to be acted upon without reservation.”", icon="quote", accent=True, at=A("c10", "warned"))

MUSIC = {"file": "audio/bed_mixkit738_140s.mp3", "target_lufs": -21}   # owner 02-11-2026: trending-style royalty-free bed, audible under the voice
