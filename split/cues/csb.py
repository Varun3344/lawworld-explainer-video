# Chetan Sabharwal v. Assistant Commissioner of Income Tax, Circle 28(1), New Delhi, 2026 INSC 1163, Civil Appeal No. 13953 of 2026
# (@ SLP(C) No. 20045 of 2019) with C.A. Nos. 13954-13956 of 2026 (J.B. Pardiwala J., author; K. Vinod Chandran J.; decided
# 28.10.2026, REPORTABLE): panel cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND). Concept format as
# sets pan / nkp.
# Facts from the judgment (paras): Delhi High Court, W.P.(C) No. 10898 of 2015, 06.08.2019: writ dismissed, reassessment under
# ss.147/148 for AY 2008-09 and AY 2009-10 upheld (2, 13); the appellant, his brother (connected matters) and two other shareholders,
# SPAs of 19.10.2007 with the buyer company: shares of company no. 1 for Rs 195 crore and company no. 2 for Rs 60 crore, 1/4th each
# (3); ITR AY 2008-09 on 25.09.2008, loss Rs 90.37 lakh, Rs 37.64 crore as sundry credit (4); Rs 28 crore and Rs 3.915 crore in the
# Capital Gain Savings Account on 25.09.2009, s.54F(4) (6); 21.04.2010: the two jointly bought an undivided 1/2 share in a residential
# property in Delhi out of the gains, within 2 years, s.54F (7); s.142(1) notice 06.08.2010 on the Rs 37.62 crore transaction with
# the buyer company; s.133(6) notices 13.12.2010, replies filed (8, 9); s.143(3) assessment 22.12.2010, returned income accepted (10);
# after it, the Investigation Unit, Noida (DGIT (Inv.), Lucknow): shares prima facie overvalued, going by the cost of land and
# building, much lower than Rs 195 crore and Rs 60 crore; the sale proceeds the major source of the Sikandara Road purchase (11, 20);
# s.148 notice 31.03.2015, "after a gap of 4 years" (12); reasons communicated 24.04.2015; objections rejected 24.09.2015 (12, 13).
# Assessees: overvaluation cannot result in escapement in the seller's hands; the sale fully disclosed and thoroughly examined;
# reopening beyond 4 years without a failure to disclose; a mere change of opinion (16-19). Held: ss.147/148 "as it stood on
# 31.03.2015" (26, 27); "reason to believe" "means cause or justification"; tangible material with a rational connection or live link
# to the belief; need not be finally ascertained by legal evidence; "the sufficiency of the reasons is not a justiciable issue"
# (41, 57(i)); "A change of opinion presupposes a conscious application of mind and the formation of an opinion in the original
# assessment" (57(i)); principles at paras 41 and 46 (57(i)); fresh facts came through the report after 22.12.2010 (51); the reasons
# go beyond valuation to the gains and the s.54F claim (52); the brother: only a s.143(1) intimation, "no assessment was framed",
# no opinion (53); AY 2008-09 order "a bare acceptance of the returned income as it is" (55); AY 2009-10 order: no discussion on the
# LTCG (54); notice valid, no change of opinion (56, 57(ii)); appeals dismissed (58). Names only on the cite card. The section card is
# not used: its renderer prints "§" before the number (owner 28-10: "Section", never "§").
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen, as tej)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
STING = {"kicker": "SUPREME COURT · JUDGMENT EXPLAINED", "title": "Reopening vs change of opinion", "sub": "Supreme Court of India · 2026 INSC 1163"}
ENDCARD = {"title": "Reopening vs change of opinion", "line": "No opinion formed earlier · fresh report · reopening valid", "sub": "LawWorld: legal research for advocates"}

# ── 1 · change of opinion? ───────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "return"), text="Return accepted years ago. Can a fresh report reopen it, or is that a mere change of opinion?", hl="a mere change of opinion?")
cue(type="bench", t0=S("c02"), t1=E("c02") + 0.05, tag="Supreme Court of India · 28 October 2026",
    judges=[{"name": "Justice J.B. Pardiwala", "photo": "../brand/judges/jb_pardiwala.jpg", "at": A("c02", "honourable")},
            {"name": "Justice K. Vinod Chandran", "photo": "../brand/judges/k_vinod_chandran.jpg", "at": A("c02", "honourable", 2)}])

# ── 2 · the share sale ───────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=A("c03", "brothers"), t1=E("c04") + 0.05, at=A("c03", "brothers"), tag="SUPREME COURT OF INDIA · 28.10.2026",
    cases=[{"name": "Chetan Sabharwal v. ACIT, Circle 28(1), New Delhi", "cite": "2026 INSC 1163 · C.A. No. 13953 of 2026 & connected"}])
cue(type="flow", t0=S("c03"), t1=E("c03") + 0.05, head="Share Purchase Agreements · 19 Oct 2007", head_at=S("c03") + 0.05,
    steps=[{"label": "Two brothers + two other shareholders", "sub": "each entitled to ¼ of the price", "icon": "user", "at": A("c03", "brothers")},
           {"label": "Company no. 1 shares · ₹195 crore", "sub": "total sale consideration", "icon": "file-text", "at": A("c03", "companies")},
           {"label": "Company no. 2 shares · ₹60 crore", "sub": "total sale consideration", "icon": "file-text", "at": A("c03", "rupees")}])
cue(type="flow", t0=S("c04"), t1=A("c04", "december") - 0.05, head="Where the gains went", head_at=S("c04") + 0.05,
    steps=[{"label": "Capital Gain Savings Account", "sub": "one brother: ₹28 crore + ₹3.915 crore · 25 Sep 2009", "icon": "file-text", "at": A("c04", "gains")},
           {"label": "½ share of a Delhi residential property", "sub": "bought jointly by the brothers · 21 Apr 2010", "icon": "landmark", "at": A("c04", "half")},
           {"label": "Section 54F benefit claimed", "sub": "Income Tax Act, 1961 · bought within 2 years", "icon": "check", "at": A("c04", "claiming")}])
cue(type="flow", t0=A("c04", "december") - 0.05, t1=E("c04") + 0.05, head="The original assessment · AY 2008-09", head_at=A("c04", "december"),
    steps=[{"label": "Queries: Sections 142(1) and 133(6)", "sub": "on the ₹37.62 crore transaction with the buyer · Aug–Dec 2010", "icon": "search", "at": A("c04", "december")},
           {"label": "Section 143(3) order · 22 Dec 2010", "sub": "returned income accepted", "icon": "check", "tone": "ok", "at": A("c04", "accepted")}])

# ── 3 · reopened ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c05"), t1=A("c05", "then") - 0.05, head="After the assessment", head_at=S("c05") + 0.05,
    steps=[{"label": "Investigation Unit, Noida · DGIT (Inv.)", "sub": "enquiries into the value of the shares", "icon": "search", "at": A("c05", "tax")},
           {"label": "Shares prima facie overvalued", "sub": "land and building cost much lower than ₹195 crore and ₹60 crore", "icon": "info", "at": A("c05", "shares")},
           {"label": "Sale proceeds: major source of the property", "sub": "the half share at Sikandara Road, New Delhi", "icon": "landmark", "at": A("c05", "overvalued")}])
cue(type="timeline", t0=A("c05", "then") - 0.05, t1=E("c05") + 0.05,
    nodes=[{"label": "SECTION 148 NOTICE", "value": "31 Mar 2015", "sub": "AY 2008-09 and 2009-10 · after a gap of 4 years", "at": A("c05", "march")},
           {"label": "OBJECTIONS REJECTED", "value": "24 Sep 2015", "sub": "objections filed 20 May 2015", "at": A("c05", "notices")},
           {"label": "DELHI HIGH COURT", "value": "6 Aug 2019", "sub": "W.P.(C) 10898/2015 dismissed", "at": A("c05", "issued")}])
cue(type="list", t0=S("c06"), t1=E("c06") + 0.05, head="The assessees argued", head_at=A("c06", "brothers"),
    items=[{"n": 1, "text": "Overvalued shares cannot mean escaped income in the seller's hands", "at": A("c06", "overvalued")},
           {"n": 2, "text": "The sale was fully disclosed and examined in scrutiny", "at": A("c06", "disclosed")},
           {"n": 3, "text": "Same facts, already examined: a mere change of opinion", "at": A("c06", "change")}])

# ── 4 · what the court held ──────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c07"), t1=E("c07") + 0.05, head="“Reason to believe” · Section 147", head_at=A("c07", "reason"),
    steps=[{"label": "“means cause or justification”", "sub": "not the fact finally proved by legal evidence", "icon": "scale", "at": A("c07", "cause")},
           {"label": "Tangible material, a live link", "sub": "a rational connection with the belief that income escaped", "icon": "file-check", "at": A("c07", "tangible")},
           {"label": "Sufficiency: not for the courts", "sub": "“the sufficiency of the reasons is not a justiciable issue”", "icon": "x", "tone": "stop", "at": A("c07", "sufficiency")}],
    note={"text": "Sections 147–148 as they stood on 31.03.2015 · principles at paras 41 and 46", "icon": "info", "at": A("c07", "sufficiency", d=0.6)})
cue(type="point", t0=S("c08"), t1=A("c08", "here") - 0.05, text="“A change of opinion presupposes a conscious application of mind and the formation of an opinion in the original assessment”", icon="scale", accent=True, at=A("c08", "change"))
cue(type="flow", t0=A("c08", "here") - 0.05, t1=E("c08") + 0.05, head="No opinion was formed", head_at=A("c08", "here"),
    steps=[{"label": "One brother · Section 143(3) order", "sub": "AY 2008-09: “a bare acceptance of the returned income as it is”", "icon": "file-text", "at": A("c08", "brother's")},
           {"label": "The other · Section 143(1) intimation", "sub": "“no assessment was framed”", "icon": "file-text", "at": A("c08", "other")}],
    note={"text": "No opinion formed: Revenue may reopen on new facts", "icon": "info", "at": A("c08", "intimation")})

# ── 5 · the verdict ──────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "under") - 0.05, text="Investigation report, prepared after the assessment: fresh, tangible material", icon="file-check", at=A("c09", "report"))
cue(type="flow", t0=A("c09", "under") - 0.05, t1=E("c09") + 0.05, head="The verdict", head_at=A("c09", "under"),
    steps=[{"label": "Old law: Sections 147–148 as on 31.03.2015", "sub": "the law applied in this case", "icon": "calendar", "at": A("c09", "stood")},
           {"label": "Notice of 31.03.2015: valid", "sub": "no case of change of opinion made out", "icon": "check", "tone": "ok", "at": A("c09", "valid")},
           {"label": "Appeals dismissed", "sub": "C.A. Nos. 13953–13956 of 2026", "icon": "check", "tone": "ok", "at": A("c09", "dismissed")}])
cue(type="point", t0=S("c10"), t1=E("c10") + 0.05, text="Like · Share · Subscribe · lawworld.ai", icon="check", accent=True, at=A("c10", "like"))
