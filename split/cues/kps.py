# Bank of India & Ors. v. S.M. Kamal Pasha & Ors., 2026 INSC 1154, Civil Appeal No. 12045 of 2026 (K. Vinod Chandran J. wrote it,
# J. B. Pardiwala J.; decided 26.10.2026, Reportable): panel cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3
# PEND). FIRST judgment reel in the HOOK format (owner 02-11-2026): c01 hook question, c02 curiosity, c03 "Hi, I'm Ravishankar" +
# bench, c04-c07 facts / case / discussion, c08 the LawWorld request before the verdict, c09-c10 the verdict. No title sting.
# Facts from the judgment (paras): the question (1); NCLT allowed the RP's withdrawal application, approved by the CoC unanimously;
# the CoC's plea - finances improved under the RP, a windfall for the SRA; CoC + RP sought a fresh Form-G, a new invitation of EoI
# (2); NCLAT: withdrawal violates the IBC (Ebix Singapore, Jalan-Fritsch), CoC has no jurisdiction to withdraw; the delay came from
# the stay in the earlier proceedings before this Court; IA 1505/2021 (approval) revived (3); appeal by six CoC members, the 1st
# appellant the Section 7 applicant (4); the lenders' counsel: plan amount Rs.172.55 crores, opening balance Rs.30 crores, later
# Rs.165 crores; toll collection on National Highway 45 hit by Covid-19; CoC's commercial wisdom has primacy (5); the plan binds
# the CoC and the SRA inter se even before the AA approves it (9, 10); the Ebix dictum "applies squarely to the CoC too" (14);
# withdrawal only till the CoC approves the plan, and once it is placed before the AA, no withdrawal of the application or the plan
# (17); delay "occasioned because of the stay granted by this Court" (20); "would not interfere with the impugned order"; NCLT to
# verify the present financial position and cash balance; "improved profitability alone cannot be a reason to refuse approval if
# the Resolution Plan meets the requirements under sub-section (2) of Section 30" (25); both applications together, "as
# expeditiously as possible" (26); appeal disposed of (27).
# Not on any card: the corporate debtor's name (not in the judgment); the SRA's "institutionalized rapacity" line (24).
# No section sign anywhere. List lines <= 52 chars. Official sci.gov.in portraits on the bench card.
FORMAT = "hook"   # build_course_plan.py: no opening sting, 15-frame lead (the cover), name tag on the "Ravishankar" clip

def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
ENDCARD = {"title": "Can lenders walk away from an approved plan?", "line": "Once the plan is before the NCLT, the committee cannot withdraw it", "sub": "LawWorld: legal research for advocates"}

# ── 1 · can lenders walk away? (hook, curiosity, intro) ──────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "lenders"), text="Can lenders back out of a resolution plan they already approved, just because the company is now earning more?", hl="just because the company is now earning more?")
cue(type="counters", t0=S("c02"), t1=A("c02", "who") - 0.05, head="The company's balance, as the lenders put it", head_at=S("c02") + 0.05,
    items=[{"value": 30, "unit": "₹ CRORE", "label": "When the plan was proposed", "sub": "opening balance", "at": A("c02", "thirty")},
           {"value": 165, "unit": "₹ CRORE", "label": "After a long delay", "sub": "by the end of the earlier round", "tone": "red", "at": A("c02", "hundred")}])
cue(type="point", t0=A("c02", "who") - 0.05, t1=E("c02") + 0.05, text="So who gets the windfall?", icon="search", accent=True, at=A("c02", "windfall"))
cue(type="bench", t0=S("c03"), t1=E("c03") + 0.05, tag="Supreme Court of India · 26 October 2026",
    judges=[{"name": "Justice J.B. Pardiwala", "photo": "../brand/judges/jb_pardiwala.jpg", "at": A("c03", "honourable")},
            {"name": "Justice K. Vinod Chandran", "photo": "../brand/judges/k_vinod_chandran.jpg", "at": A("c03", "honourable", 2)}])

# ── 2 · the insolvency ───────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=S("c05"), t1=E("c05") + 0.05, at=A("c05", "creditors"), tag="SUPREME COURT OF INDIA · 26.10.2026",
    cases=[{"name": "Bank of India & Ors. v. S.M. Kamal Pasha & Ors.", "cite": "2026 INSC 1154 · Civil Appeal No. 12045 of 2026"}])
cue(type="flow", t0=S("c04"), t1=E("c04") + 0.05, head="Insolvency and Bankruptcy Code, 2016", head_at=S("c04") + 0.05,
    steps=[{"label": "Bank of India files", "sub": "Section 7 · the financial creditor", "icon": "landmark", "at": A("c04", "started")},
           {"label": "Debtor: toll collection", "sub": "on National Highway 45", "icon": "file-text", "at": A("c04", "toll")},
           {"label": "Covid hit the business", "sub": "per the lenders: finances tottering", "icon": "info", "at": A("c04", "covid")}])
cue(type="timeline", t0=S("c05"), t1=E("c05") + 0.05,
    nodes=[{"label": "COMMITTEE OF CREDITORS", "value": "plan approved", "sub": "per the lenders: ₹172.55 crore", "at": A("c05", "approved")},
           {"label": "EARLIER PROCEEDINGS", "value": "a stay", "sub": "Supreme Court, the promoter's appeal", "at": A("c05", "stay")},
           {"label": "THE PLAN", "value": "delayed", "sub": "not the winning bidder's fault", "tone": "stop", "at": A("c05", "delayed")}])

# ── 3 · the U-turn ───────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c06"), t1=E("c06") + 0.05, head="The lenders change their mind", head_at=S("c06") + 0.05,
    steps=[{"label": "A “windfall gain” for the bidder", "sub": "opening balance up from ₹30 crore to ₹165 crore", "icon": "scale", "at": A("c06", "windfall")},
           {"label": "Committee votes to withdraw: unanimous", "sub": "a fresh Form-G sought: a new invitation for EoIs", "icon": "file-text", "at": A("c06", "unanimously")},
           {"label": "NCLT allows the withdrawal", "sub": "on the Resolution Professional's application", "icon": "landmark", "at": A("c06", "allowed")}])
cue(type="timeline", t0=S("c07"), t1=E("c07") + 0.05,
    nodes=[{"label": "NCLAT", "value": "withdrawal set aside", "sub": "against the IBC (Ebix Singapore)", "at": A("c07", "reversed")},
           {"label": "THE COMMITTEE", "value": "no power to withdraw", "sub": "approval plea back before the NCLT", "tone": "stop", "at": A("c07", "power")},
           {"label": "SUPREME COURT", "value": "the lenders appeal", "sub": "six CoC members: commercial wisdom", "at": A("c07", "lenders")}])

# ── 4 · before the verdict: the LawWorld request ────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c08"), t1=A("c08", "follow") - 0.05, text="The verdict is next. First, a quick request…", icon="scale", accent=True, at=A("c08", "decided"))
cue(type="list", t0=A("c08", "follow") - 0.05, t1=E("c08") + 0.05, head="Follow LawWorld · lawworld.ai", head_at=A("c08", "follow"),
    items=[{"n": 1, "text": "Search SC and High Court judgments, cited to source", "at": A("c08", "india's")},
           {"n": 2, "text": "Draft petitions, plaints and notices with AI", "at": A("c08", "platform")},
           {"n": 3, "text": "Sign up free · ₹200 AI credit included", "at": A("c08", "advocates")}])

# ── 5 · what the Court held ──────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "once") - 0.05, text="What did the Supreme Court decide?", icon="scale", accent=True, at=A("c09", "finally"))
cue(type="list", t0=A("c09", "once") - 0.05, t1=E("c09") + 0.05, head="Sections 12A, 30 and 31 of the IBC", head_at=A("c09", "once"),
    items=[{"n": 1, "text": "Withdrawal only until the committee approves", "at": A("c09", "approves")},
           {"n": 2, "text": "Plan before the NCLT: no withdrawal at all", "at": A("c09", "withdrawal")},
           {"n": 3, "text": "Ebix applies to the CoC too: the plan binds it", "at": A("c09", "binds")}])
cue(type="point", t0=S("c10"), t1=A("c10", "court") - 0.05, text="“Improved profitability alone cannot be a reason to refuse approval” · if the plan meets Section 30(2), checked against today's finances", icon="scale", accent=True, at=A("c10", "profits"))
cue(type="verdicts", t0=A("c10", "court") - 0.05, t1=E("c10") + 0.05,
    rows=[{"text": "NCLAT's order: not interfered with", "ok": True, "at": A("c10", "disturb")},
          {"text": "Plan approval + promoter's OTS plea: heard together", "ok": True, "at": A("c10", "asked")},
          {"text": "NCLT to decide as expeditiously as possible", "ok": True, "at": A("c10", "quickly")}])
