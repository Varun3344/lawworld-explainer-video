# South Bihar Power Distribution Company Ltd. v. India Power Corporation Ltd. & Anr., 2026 INSC 1165, Civil Appeal No. 9313 of 2026
# with C.A. No. 9325 of 2026 (Ujjal Bhuyan J. wrote it, Atul S. Chandurkar J.; decided 28.10.2026, REPORTABLE): panel cues, run by
# split/build_course_plan.py (helpers: at S E cue fx have r3 PEND). Concept format as sets dvc / cdp.
# Facts from the judgment (paras): the appellant, a distribution licensee in Bihar (5); tripartite Distribution Franchisee Agreement
# dated 31.12.2013 with India Power Corporation Ltd. (the successful bidder) and its special purpose vehicle (5.1); clause 17.2.5:
# unresolved disputes to arbitration "by a panel consisting of three arbitrators" (14.1, 14.2); on the SPV's Section 11 request, the
# Patna High Court, with the parties' consent, appointed a retired judge of that court sole arbitrator, 04.04.2018 (5.3); counter claim
# 02.02.2019, supplementary counter claim 28.03.2019 (5.4); NCLT admitted CIRP against the SPV (respondent No. 2), 08.11.2019 (5.5);
# again by consent, a former Chief Justice of India appointed, 10.03.2021 (5.6); procedural order 07.04.2021: no objection to the
# composition (5.7, 21.2); one year + six months by consent; before the extended period expired (07.08.2021) the respondents asked
# the High Court for four more months, Request Case No. 36 of 2021 (5.7, 15); the appellant objected: no jurisdiction to extend, a
# three-member tribunal (Request Case No. 78 of 2022), the SPV in CIRP had no locus (5.8, 5.11); High Court 15.09.2023: waiver and
# acquiescence, locus upheld, jurisdiction under Section 29A, mandate extended four months (3, 5.11). Held: (1) the appellant
# "clearly waived its right to object to the composition of the arbitral tribunal"; took part, consented to the extension, counter
# claim and supplementary counter claim = "clear acquiescence"; not open "at the very belated stage" (25); Sections 4, 16(2) (23, 24);
# appointment orders never assailed, final and binding (22); Pam Development (2014) 11 SCC 366 (26); affirmed (27). (2) Section 14 IBC
# moratorium bars debt recovery action against the corporate debtor, "would not impair any claim by the corporate debtor, such as, an
# arbitral claim, which if successful, would only bolster the financial health thereby enhancing the value of the corporate debtor"
# (29); resolution professional's authorisation approved by the committee of creditors, Section 28(1)(h) IBC (30); affirmed (31).
# (3) "court" = Section 2(1)(e)(i): principal civil court of original jurisdiction in a district, incl. a High Court in its ordinary
# original civil jurisdiction; Section 11 is about appointment, "nothing more should be read into it" (34); Associated Contractors
# (2015) 1 SCC 32 (37); BSC & C and C JV (38); Jagdeep Chowgule (2026) 5 SCC 667: Section 11 jurisdiction "stands exhausted upon the
# constitution of the arbitral tribunal" (39); C. Velusamy (2026) 5 SCC 340 (40); the High Court's view "clearly unsustainable in
# law", set aside (43). Result: this Court's order 21.01.2026 (8); Commercial Court, Patna, 23.03.2026: six more months (9); the
# set-aside "would have no bearing and would not materially affect the outcome" (44); Q1, Q2 affirmed, Q3 set aside (45); the
# 12.02.2024 embargo on declaring the award lifted, award within six weeks (6, 46); appeals dismissed, no costs (47, 48).
# Not on any card: whether the Patna High Court has an ordinary original civil side (the judgment does not say). No arbitrator or
# private person named; only the two companies. Official sci.gov.in portraits on the bench card. No section card: it would print the section sign.
# List lines <= 52 chars (9:16 list items do not wrap).
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen, as dvc / cdp)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
STING = {"kicker": "SUPREME COURT · JUDGMENT EXPLAINED", "title": "Which court extends the mandate?", "sub": "South Bihar Power v. India Power Corp. · 2026 INSC 1165"}
ENDCARD = {"title": "Which court extends the mandate?", "line": "Section 11 appoints; the Section 2(1)(e) court extends the time", "sub": "LawWorld: legal research for advocates"}

# ── 1 · who extends the mandate? ─────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "high"), text="The High Court appointed your arbitrator under Section 11. When time runs out, can that same High Court extend the mandate?", hl="that same High Court extend the mandate")
cue(type="bench", t0=S("c02"), t1=E("c02") + 0.05, tag="Supreme Court of India · 28 October 2026",
    judges=[{"name": "Justice Ujjal Bhuyan", "photo": "../brand/judges/ujjal_bhuyan.jpg", "at": A("c02", "honourable")},
            {"name": "Justice Atul S. Chandurkar", "photo": "../brand/judges/atul_s_chandurkar.jpg", "at": A("c02", "honourable", 2)}])

# ── 2 · the arbitration ──────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=A("c03", "south"), t1=E("c04") + 0.05, at=A("c03", "south"), tag="SUPREME COURT OF INDIA · 28.10.2026",
    cases=[{"name": "South Bihar Power Distribution Co. Ltd. v. India Power Corporation Ltd.", "cite": "2026 INSC 1165 · Civil Appeal No. 9313 of 2026"}])
cue(type="flow", t0=S("c03"), t1=E("c03") + 0.05, head="The arbitration clause", head_at=S("c03") + 0.05,
    steps=[{"label": "Franchisee agreement · 31 Dec 2013", "sub": "South Bihar Power, India Power Corporation and its special purpose company", "icon": "file-text", "at": A("c03", "franchisee")},
           {"label": "Clause 17.2.5: three arbitrators", "sub": "unresolved disputes go to “a panel consisting of three arbitrators”", "icon": "scale", "at": A("c03", "three")},
           {"label": "By consent: a sole arbitrator", "sub": "Patna High Court · Section 11 request · 4 April 2018", "icon": "landmark", "at": A("c03", "consent")}])
cue(type="timeline", t0=S("c04"), t1=E("c04") + 0.05,
    nodes=[{"label": "NEW ARBITRATOR", "value": "10 March 2021", "sub": "a former Chief Justice of India · by consent, no objection recorded", "at": A("c04", "former")},
           {"label": "TIME LIMIT", "value": "12 + 6 months", "sub": "Section 29A · the six months by consent", "at": A("c04", "year")},
           {"label": "HIGH COURT ASKED", "value": "4 more months", "sub": "the respondents' request, before the time expired", "at": A("c04", "asked")}])

# ── 3 · the objections ───────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="list", t0=S("c05"), t1=A("c05", "rejected") - 0.05, head="The appellant's objections", head_at=A("c05", "objected"),
    items=[{"n": 1, "text": "Three arbitrators, as the agreement requires", "at": A("c05", "three")},
           {"n": 2, "text": "The claimant in insolvency: no locus to arbitrate", "at": A("c05", "claimant")},
           {"n": 3, "text": "No power in the High Court to extend time", "at": A("c05", "power")}])
cue(type="point", t0=A("c05", "rejected") - 0.05, t1=E("c05") + 0.05, text="High Court, 15 Sep 2023: all three rejected · the mandate extended by four months under Section 29A", icon="landmark", at=A("c05", "rejected"))

# ── 4 · what the court held ──────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="list", t0=S("c06"), t1=A("c06", "waived") - 0.05, head="Three arbitrators? Waived", head_at=A("c06", "panel"),
    items=[{"n": 1, "text": "Consented twice: in 2018 and again in 2021", "at": A("c06", "consented")},
           {"n": 2, "text": "Took part, and agreed to six more months", "at": A("c06", "taken")},
           {"n": 3, "text": "Filed a counter claim and a supplementary one", "at": A("c06", "counter")}])
cue(type="point", t0=A("c06", "waived") - 0.05, t1=E("c06") + 0.05, text="Sections 4 and 16(2): the right to object was waived · “clear acquiescence”, too late at “the very belated stage”", icon="scale", accent=True, at=A("c06", "waived"))
cue(type="flow", t0=S("c07"), t1=E("c07") + 0.05, head="Insolvency was no bar", head_at=A("c07", "insolvency"),
    steps=[{"label": "Section 14 IBC moratorium", "sub": "bars debt recovery action against the corporate debtor", "icon": "x", "tone": "stop", "at": A("c07", "moratorium")},
           {"label": "Not the debtor's own claim", "sub": "pursued on the resolution professional's authority, approved by the creditors", "icon": "file-check", "at": A("c07", "own")},
           {"label": "A win only adds value", "sub": "an arbitral claim, if successful, “would only bolster the financial health”", "icon": "check", "tone": "ok", "at": A("c07", "only")}])
cue(type="notequal", t0=S("c08"), t1=A("c08", "only") - 0.05, left="The High Court under Section 11", right="the court under Section 29A", at=A("c08", "acting"),
    left_at=A("c08", "acting"), sub="Jagdeep Chowgule (2026): Section 11 jurisdiction stands exhausted once the arbitral tribunal is constituted", sub_at=A("c08", "role"))
cue(type="point", t0=A("c08", "only") - 0.05, t1=E("c08") + 0.05, text="Section 29A: the ‘court’ of Section 2(1)(e) · a principal civil court, or a High Court in its ordinary original civil jurisdiction", icon="landmark", accent=True, at=A("c08", "only"))

# ── 5 · the verdict ──────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="timeline", t0=S("c09"), t1=A("c09", "appeals") - 0.05,
    nodes=[{"label": "SUPREME COURT", "value": "21 Jan 2026", "sub": "the District Court to decide the extension", "at": A("c09", "since")},
           {"label": "COMMERCIAL COURT, PATNA", "value": "23 Mar 2026", "sub": "mandate extended by six months", "at": A("c09", "commercial")},
           {"label": "HIGH COURT'S 29A VIEW", "value": "set aside", "sub": "“clearly unsustainable” · but “no bearing” on the outcome", "at": A("c09", "error")}])
cue(type="verdicts", t0=A("c09", "appeals") - 0.05, t1=E("c09") + 0.05,
    rows=[{"text": "Both civil appeals dismissed · no costs", "ok": True, "at": A("c09", "dismissed")},
          {"text": "The 2024 bar on declaring the award: lifted", "ok": True, "at": A("c09", "award")},
          {"text": "Award within six weeks of the judgment", "ok": True, "at": A("c09", "within")}])
cue(type="point", t0=S("c10"), t1=E("c10") + 0.05, text="Like · Share · Subscribe · lawworld.ai", icon="check", accent=True, at=A("c10", "like"))
