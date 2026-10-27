# N. Arasappa v. State of Karnataka & Ors., 2026 INSC 1151 (J.B. Pardiwala J., K. Vinod Chandran J. - Vinod Chandran J. wrote it;
# decided 26.10.2026, REPORTABLE): panel cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND).
# Facts from the judgment (paras): Annexure P1 agreement of 21.09.1984 between the 4th respondent housing society (Peenya, Bangalore)
# and a third party, who would ensure acquisition "as government land" for the society (37-38); s.3(f) incl. (vi) substituted by Act
# 68 of 1984 w.e.f. 24.09.1984 (37, 39); Government approval letter 13.11.1987, 97 acres (13, 45); s.4(1) notification 22.11.1988,
# s.6 declaration 04.12.1989 (12); WP 9412 of 2007 filed when possession was disturbed in 2007 (12); Single Judge quashed for fraud and
# colourable exercise of power (16); Division Bench reversed on delay and res judicata, relying on Karithimmaiah, 2002 (1) Kar.L.J. 469
# (DB) (17-20); approval "is not of the mere requisition ... forma et descriptio (the layout and the blueprint)" (40); "a sketch of land
# without any layout plan" (43); the agreement "clearly exposes the fraud intended to be carried out" (71(i)); "Fraud vitiates all
# solemn acts" (56); SLP dismissal no Art. 141 precedent (25, 66); res judicata and delay "pale into insignificance" (72); DB set aside,
# Single Judge restored, costs enhanced to Rs 50,000 each (73); possession to all landowners, challengers or not, on refund of the
# Government compensation without interest (private payments not refundable); the society has no claim; plots not resumed are
# auctioned, proceeds to victim compensation (74). The bench card uses the official portraits.
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow (24 + 58 px) ends inside the panel: the 9:16 band edge cut it into a line at 40
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen (no blobs / star behind the cards)
STING = {"kicker": "SUPREME COURT · JUDGMENT EXPLAINED", "title": "Section 3(f)(vi) and a housing society", "sub": "N. Arasappa v. State of Karnataka · 2026 INSC 1151"}
ENDCARD = {"title": "Section 3(f)(vi) and a housing society", "line": "Approve the scheme and its layout, not the requisition", "sub": "LawWorld: legal research for advocates"}

# ── 1 · approval of what? ────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "land"), text="Only the society's request approved, no housing scheme: can the land be acquired?", hl="can the land be acquired?")
cue(type="bench", t0=S("c02"), t1=E("c02") + 0.05, tag="Supreme Court of India · 26 October 2026",
    judges=[{"name": "Justice J.B. Pardiwala", "photo": "../brand/judges/jb_pardiwala.jpg", "at": A("c02", "honourable")},
            {"name": "Justice K. Vinod Chandran", "photo": "../brand/judges/k_vinod_chandran.jpg", "at": A("c02", "honourable", 2)}])

# ── 2 · the acquisition ──────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=A("c03", "bengaluru"), t1=E("c04") + 0.05, at=A("c03", "bengaluru"), tag="SUPREME COURT OF INDIA · 26.10.2026",
    cases=[{"name": "N. Arasappa v. State of Karnataka", "cite": "2026 INSC 1151 · Civil Appeal Nos. 13744-13747 of 2015"}])
cue(type="flow", t0=S("c03"), t1=E("c03") + 0.05, head="The 1984 agreement", head_at=S("c03") + 0.05,
    steps=[{"label": "A housing society", "sub": "Peenya, Bengaluru · the 4th respondent", "icon": "user", "at": A("c03", "society")},
           {"label": "Agreement · 21 Sep 1984", "sub": "with a third party (Annexure P1)", "icon": "file-text", "at": A("c03", "agreement")},
           {"label": "Land to be acquired “as government land”", "sub": "for the society, through the Government", "icon": "landmark", "at": A("c03", "acquired")}])
cue(type="timeline", t0=S("c04"), t1=E("c04") + 0.05,
    nodes=[{"label": "AGREEMENT", "value": "21 Sep 1984", "sub": "society and third party", "at": A("c04", "three")},
           {"label": "SECTION 3(f)(vi)", "value": "24 Sep 1984", "sub": "in force, Act 68 of 1984", "at": A("c04", "section")},
           {"label": "APPROVAL", "value": "13 Nov 1987", "sub": "97 acres for the society", "at": A("c04", "approval", 2)}])

# ── 3 · in the high court ────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c05"), t1=E("c05") + 0.05, head="In the High Court", head_at=S("c05") + 0.05,
    steps=[{"label": "Writ petition · 2007", "sub": "filed when interference with possession was attempted", "icon": "file-text", "at": A("c05", "landowners")},
           {"label": "Single Judge: quashed", "sub": "fraud · colourable exercise of power", "icon": "check", "tone": "ok", "at": A("c05", "quashed")},
           {"label": "Division Bench: reversed", "sub": "delay · res judicata (Karithimmaiah)", "icon": "x", "tone": "stop", "at": A("c05", "reversed")}])

# ── 4 · what the court held ──────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c06"), t1=E("c06") + 0.05, at=A("c06", "supreme"), act="LA ACT, 1894", num="3(f)(vi)", title="A cooperative society's housing scheme",
    points=[{"text": "Prior approval of the scheme itself", "at": A("c06", "approve")},
            {"text": "“forma et descriptio”: the layout and the blueprint", "at": A("c06", "layout")},
            {"text": "Not the society's mere requisition", "tone": "no", "at": A("c06", "mere")}])
cue(type="point", t0=S("c07"), t1=A("c07", "agreement") - 0.05, text="No layout before the Government: only a sketch of the land", icon="x", at=A("c07", "layout"))
cue(type="point", t0=A("c07", "agreement"), t1=E("c07") + 0.05, text="Signed before the law changed: “clearly exposes the fraud”", icon="file-text", accent=True, at=A("c07", "agreement"))
cue(type="point", t0=S("c08"), t1=A("c08", "res") - 0.05, text="“Fraud vitiates all solemn acts”", icon="scale", accent=True, at=A("c08", "fraud"))
cue(type="verdicts", t0=A("c08", "res"), t1=E("c08") + 0.05,
    rows=[{"text": "Res judicata and delay as a bar?", "ok": False, "at": A("c08", "res"), "strike_at": A("c08", "insignificance")},
          {"text": "Division Bench judgment set aside", "ok": True, "at": A("c08", "single")},
          {"text": "Single Judge restored · costs ₹50,000 each · contempt dropped", "ok": True, "at": A("c08", "restored")}])
cue(type="cite", t0=A("c08", "res"), t1=E("c08") + 0.05, at=A("c08", "res"), tag="EARLIER HIGH COURT RULING · NO BAR",
    cases=[{"name": "Karithimmaiah (Karnataka HC, DB)", "cite": "2002 (1) Kar.L.J. 469 · SLP dismissed: no Art. 141 precedent"}])

# ── 5 · the orders ───────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c09"), t1=E("c09") + 0.05, head="The land", head_at=S("c09") + 0.05,
    steps=[{"label": "Back to all owners", "sub": "even those who never challenged", "icon": "user", "at": A("c09", "owners")},
           {"label": "Refund the compensation", "sub": "the Government's payment, no interest", "icon": "arrow-right", "at": A("c09", "refunding")},
           {"label": "Plots not taken back: auctioned", "sub": "proceeds to victim compensation", "icon": "landmark", "at": A("c09", "auctioned")}],
    note={"text": "The society has no claim over the land", "icon": "x", "at": A("c09", "proceeds")})
cue(type="point", t0=S("c10"), t1=E("c10") + 0.05, text="Like · Share · Subscribe · lawworld.ai", icon="check", accent=True, at=A("c10", "like"))
