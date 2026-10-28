# The Muppathadam Service Co-operative Bank Ltd. v. The State Chief Information Commissioner & Ors., 2026 INSC 1153 (J.B. Pardiwala J.,
# K. Vinod Chandran J. - Vinod Chandran J. wrote it; decided 26.10.2026, REPORTABLE): panel cues, run by split/build_course_plan.py
# (helpers: at S E cue fx have r3 PEND). Concept format as set ara.
# Facts from the judgment (paras): C.A. No. 13906 of 2026 @ SLP (C) No. 12283 of 2025 with C.A. No. 13907 of 2026 (cover); the 4th
# respondent, a Member of the appellant Bank, appeared in person; his RTI application to the 2nd respondent, the Joint Registrar
# (General) of Co-operative Societies, sought the construction agreement between the Bank and a Labour Co-operative Society entrusted
# with constructing a building, and the minutes of the last General Body Meeting (2); round 1 rejected up to the State Information
# Commissioner, Single Judge dismissed, Division Bench directed reconsideration; round 2 the State Information Commissioner, the Single
# Judge and the Division Bench affirmed his right (2); the Bank: not a 'public authority', Thalappalam (2013) 16 SCC 82; ss.65 and 66 of
# the Kerala Co-operative Societies Act, 1969 give access only after a subjective satisfaction to conduct an inquiry; with none entered,
# the Registrar "should be deemed to have no access" (3); s.2(f) RTI Act text (11); not only material physically available, but a
# private body's material accessible on the strength of statutory powers; "The power cannot be fettered at all" (12); prior
# satisfaction only to initiate an inquiry (13); s.65(2) free access at all reasonable times; "Access simpliciter, thus cannot be
# conditioned with a prior satisfaction" (14); s.8(1)(d): no trade secret / commercial confidence, the bid is over and a Labour Contract
# Society has the contract; s.8(1)(j): not personal information when a Member asks (8); different for a third party not connected with
# the Society (9); Division Bench "perfectly in order"; the 2nd respondent shall call for the two documents immediately and in any
# event within two weeks and supply them to the 4th respondent (15); appeals dismissed (16). The bench card uses the official portraits.
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow (24 + 58 px) ends inside the panel: the 9:16 band edge cut it into a line at 40
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen (no blobs / star behind the cards)
STING = {"kicker": "SUPREME COURT · JUDGMENT EXPLAINED", "title": "Section 2(f) RTI Act and a co-op bank", "sub": "Muppathadam Bank v. State Chief Information Commissioner · 2026 INSC 1153"}
ENDCARD = {"title": "Section 2(f) RTI Act and a co-op bank", "line": "A member gets these two records through the Registrar", "sub": "LawWorld: legal research for advocates"}

# ── 1 · rti and a co-op bank ─────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "bank"), text="Not a public authority: can a co-op bank's member still get its records under RTI?", hl="still get its records")
cue(type="bench", t0=S("c02"), t1=E("c02") + 0.05, tag="Supreme Court of India · 26 October 2026",
    judges=[{"name": "Justice J.B. Pardiwala", "photo": "../brand/judges/jb_pardiwala.jpg", "at": A("c02", "honourable")},
            {"name": "Justice K. Vinod Chandran", "photo": "../brand/judges/k_vinod_chandran.jpg", "at": A("c02", "honourable", 2)}])

# ── 2 · the request ──────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=A("c03", "member"), t1=E("c04") + 0.05, at=A("c03", "member"), tag="SUPREME COURT OF INDIA · 26.10.2026",
    cases=[{"name": "Muppathadam Service Co-operative Bank v. State Chief Information Commissioner", "cite": "2026 INSC 1153 · Civil Appeal No. 13906 of 2026"}])
cue(type="flow", t0=S("c03"), t1=E("c03") + 0.05, head="The RTI request", head_at=S("c03") + 0.05,
    steps=[{"label": "A member of the bank", "sub": "the 4th respondent · appeared in person", "icon": "user", "at": A("c03", "member")},
           {"label": "An application", "sub": "Right to Information Act, 2005", "icon": "file-text", "at": A("c03", "applied")},
           {"label": "To the Joint Registrar (General)", "sub": "of Co-operative Societies · the 2nd respondent", "icon": "landmark", "at": A("c03", "registrar")}])
cue(type="list", t0=S("c04"), t1=A("c04", "round") - 0.05, head="Two of the bank's documents", head_at=A("c04", "wanted"),
    items=[{"n": 1, "text": "Construction agreement with a Labour Co-operative Society", "at": A("c04", "building")},
           {"n": 2, "text": "Minutes of the last General Body Meeting", "at": A("c04", "minutes")}])
cue(type="flow", t0=A("c04", "round"), t1=E("c04") + 0.05, head="Two rounds", head_at=A("c04", "round"),
    steps=[{"label": "Round 1: rejected", "sub": "up to the State Information Commissioner · Division Bench: reconsider", "icon": "x", "tone": "stop", "at": A("c04", "round")},
           {"label": "Round 2: right affirmed", "sub": "by the State Information Commissioner", "icon": "check", "tone": "ok", "at": A("c04", "commissioner")},
           {"label": "High Court agrees", "sub": "Single Judge and Division Bench · the bank appeals", "icon": "landmark", "tone": "ok", "at": A("c04", "upheld")}])

# ── 3 · the bank's case ──────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c05"), t1=E("c05") + 0.05, head="The bank's case", head_at=S("c05") + 0.05,
    steps=[{"label": "Not a “public authority”", "sub": "relying on Thalappalam, (2013) 16 SCC 82", "icon": "landmark", "at": A("c05", "public")},
           {"label": "Kerala Co-op. Societies Act, ss. 65 & 66", "sub": "access only after satisfaction to hold an inquiry", "icon": "file-text", "at": A("c05", "registrar")},
           {"label": "No satisfaction, no access", "sub": "the Registrar “deemed to have no access”", "icon": "x", "tone": "stop", "at": A("c05", "satisfied")}])

# ── 4 · what the court held ──────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c06"), t1=E("c06") + 0.05, at=A("c06", "section"), act="RTI ACT, 2005", num="2(f)", title="“Information”",
    points=[{"text": "Any material: records, documents, contracts…", "at": A("c06", "information")},
            {"text": "+ information relating to any private body", "at": A("c06", "private")},
            {"text": "that a public authority can access under any other law", "at": A("c06", "access")}],
    note={"text": "Not only what the authority physically holds", "icon": "info", "at": A("c06", "law")})
cue(type="point", t0=S("c07"), t1=A("c07", "prior") - 0.05, text="“The power cannot be fettered at all”", icon="scale", accent=True, at=A("c07", "power"))
cue(type="list", t0=A("c07", "prior"), t1=E("c07") + 0.05, head="Kerala Co-op. Societies Act, s. 65", head_at=A("c07", "prior"),
    items=[{"n": 1, "text": "Prior satisfaction: only to start an inquiry", "at": A("c07", "inquiry")},
           {"n": 2, "text": "65(2): free access to the books and documents", "at": A("c07", "documents")},
           {"n": "→", "text": "Access cannot be conditioned on prior satisfaction", "at": A("c07", "decide")}])
cue(type="verdicts", t0=S("c08"), t1=E("c08") + 0.05,
    rows=[{"text": "§ 8(1)(d): trade secret · commercial confidence", "ok": False, "at": A("c08", "section"), "strike_at": A("c08", "secret")},
          {"text": "§ 8(1)(j): personal information", "ok": False, "at": A("c08", "member"), "strike_at": A("c08", "personal")},
          {"text": "A member is entitled · an unconnected outsider stands differently", "ok": True, "at": A("c08", "outsider")}])

# ── 5 · the orders ───────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c09"), t1=E("c09") + 0.05, head="The orders", head_at=S("c09") + 0.05,
    steps=[{"label": "Appeals dismissed", "sub": "Division Bench judgment “perfectly in order”", "icon": "scale", "at": A("c09", "dismissed")},
           {"label": "Joint Registrar calls for both documents", "sub": "immediately · within two weeks at the latest", "icon": "calendar", "at": A("c09", "registrar")},
           {"label": "Copies to the member", "sub": "the construction agreement · the General Body minutes", "icon": "file-check", "at": A("c09", "supply")}])
cue(type="point", t0=S("c10"), t1=E("c10") + 0.05, text="Like · Share · Subscribe · lawworld.ai", icon="check", accent=True, at=A("c10", "like"))
