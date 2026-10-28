# Dakshin Gujarat Vij Company Ltd. & Anr. v. Vaibhav Metal Crusher, with Paschim Gujarat Vij Company Ltd. & Anr. v. Jamanbhai
# Nanajibhai Bhuva, 2026 INSC 1157 (Manoj Misra J., K.V. Viswanathan J. - Misra J. wrote it; decided 26.10.2026, REPORTABLE): panel
# cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND). Concept format as set ara.
# Facts from the judgment (paras): C.A. @ SLP (C) No. 17868 of 2024 with C.A. @ SLP (C) No. 8778 of 2025 (cover); the consumer was
# accused of an offence under s.135, Electricity Act, 2003; on 03.01.2024 the distribution licensee issued a notice titled a
# supplementary bill: Rs 92,99,077.55 towards theft and Rs 23,45,845 compounding charges, prosecution under s.135 if unpaid (4(i));
# Single Judge, High Court of Gujarat at Ahmedabad, 12.02.2024: deposit 50% of the bill incl. reconnection charges, then reconnect
# (4(ii), fn 3); LPA No. 592 of 2024 (4(iii)); Division Bench, 25.06.2024: reply within two weeks before the Executive Engineer, who must
# deal with all objections; bill, deposits, reconnection subject to his decision; if adverse, appeal under s.127 (4(iv)); licensee: no
# s.126(3) objection and no s.127 appeal in theft cases; s.127(4) finality would make the Special Court's s.154(5) power nugatory (7, 8);
# 50% "too lenient" (38); no assessment provision other than s.126 and no Assessing Officer for theft: the "assessed amount" of the third
# proviso to s.135(1A) by the s.126 procedure - provisional assessment, objection, hearing - until the Supply Code prescribes one (31,
# 34, 37(i)); subject to a s.127 appeal; where a criminal complaint is filed, not binding on the Special Court, which determines civil
# liability (s.154(5)); excess refunded (s.154(6)) (35-37); "a circumspect approach is required"; the High Court may even decline
# restoration till the entire provisionally assessed amount is deposited (39); prima facie arbitrary: restoration on not less than 50%,
# for reasons recorded, as s.127(2) asks half for an appeal (40); High Court "well within its jurisdiction", clarified: subject to a
# s.127 appeal and to civil liability fixed by the Special Court; appeal dismissed; the connected appeal (a remand) dismissed (41, 41).
# Theft stays an allegation on every card ("alleged", "accused"); the bench card uses the official portraits.
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow (24 + 58 px) ends inside the panel: the 9:16 band edge cut it into a line at 40
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen (no blobs / star behind the cards)
STING = {"kicker": "SUPREME COURT · JUDGMENT EXPLAINED", "title": "Alleged power theft and the assessed amount", "sub": "Dakshin Gujarat Vij Co. v. Vaibhav Metal Crusher · 2026 INSC 1157"}
ENDCARD = {"title": "Alleged power theft and the assessed amount", "line": "Assess it the Section 126 way: objection, hearing, appeal", "sub": "LawWorld: legal research for advocates"}

# ── 1 · half to reconnect? ───────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "power"), text="Supply cut over alleged theft: a hearing on the bill? Reconnection on 50%?", hl="Reconnection on 50%?")
cue(type="bench", t0=S("c02"), t1=E("c02") + 0.05, tag="Supreme Court of India · 26 October 2026",
    judges=[{"name": "Justice Manoj Misra", "photo": "../brand/judges/manoj_misra.jpg", "at": A("c02", "honourable")},
            {"name": "Justice K.V. Viswanathan", "photo": "../brand/judges/kv_viswanathan.jpg", "at": A("c02", "honourable", 2)}])

# ── 2 · the bill ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=A("c03", "january"), t1=E("c04") + 0.05, at=A("c03", "january"), tag="SUPREME COURT OF INDIA · 26.10.2026",
    cases=[{"name": "Dakshin Gujarat Vij Company Ltd. v. Vaibhav Metal Crusher", "cite": "2026 INSC 1157 · C.A. @ SLP (C) No. 17868 of 2024"},
           {"name": "Paschim Gujarat Vij Company Ltd. v. Jamanbhai Nanajibhai Bhuva", "cite": "connected · C.A. @ SLP (C) No. 8778 of 2025"}])
cue(type="flow", t0=S("c03"), t1=E("c03") + 0.05, head="The notice", head_at=S("c03") + 0.05,
    steps=[{"label": "Dakshin Gujarat Vij Company", "sub": "the distribution licensee", "icon": "landmark", "at": A("c03", "dakshin")},
           {"label": "Supplementary bill · 3 Jan 2024", "sub": "pay, or prosecution under Section 135 follows", "icon": "file-text", "at": A("c03", "supplementary")},
           {"label": "To Vaibhav Metal Crusher", "sub": "accused under Section 135 · alleged electricity theft", "icon": "user", "at": A("c03", "consumer")}])
cue(type="timeline", t0=S("c04"), t1=E("c04") + 0.05,
    nodes=[{"label": "DEMANDED", "value": "₹92,99,077.55", "sub": "towards the alleged theft", "at": A("c04", "bill")},
           {"label": "COMPOUNDING", "value": "₹23,45,845", "sub": "charges, same notice", "at": A("c04", "compounding")},
           {"label": "SINGLE JUDGE", "value": "12 Feb 2024", "sub": "deposit 50%, then reconnect", "at": A("c04", "single")}])

# ── 3 · the dispute ──────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c05"), t1=E("c05") + 0.05, head="Division Bench · 25 Jun 2024", head_at=S("c05") + 0.05,
    steps=[{"label": "Object to the bill", "sub": "reply within two weeks", "icon": "file-text", "at": A("c05", "object")},
           {"label": "Executive Engineer decides", "sub": "must deal with every objection", "icon": "user", "at": A("c05", "engineer")},
           {"label": "If adverse: appeal", "sub": "Section 127, Electricity Act", "icon": "arrow-right", "at": A("c05", "appeal")}])
cue(type="list", t0=S("c06"), t1=E("c06") + 0.05, head="The licensee's case", head_at=A("c06", "distribution"),
    items=[{"n": 1, "text": "Theft cases: no objection, no Section 127 appeal", "at": A("c06", "theft")},
           {"n": 2, "text": "The Special Court fixes civil liability · § 154(5)", "at": A("c06", "special")},
           {"n": 3, "text": "Reconnection on 50%: “too lenient”", "at": A("c06", "half")}])

# ── 4 · what the court held ──────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c07"), t1=E("c07") + 0.05, at=A("c07", "act"), act="ELECTRICITY ACT, 2003", num="126", title="The only assessment provision",
    points=[{"text": "No other provision, no other Assessing Officer", "at": A("c07", "provision")},
            {"text": "The “assessed amount” to restore supply · § 135(1A)", "at": A("c07", "amount")},
            {"text": "Same procedure, until the Supply Code prescribes one", "at": A("c07", "procedure")}])
cue(type="flow", t0=S("c08"), t1=E("c08") + 0.05, head="Natural justice", head_at=S("c08") + 0.05,
    steps=[{"label": "Provisional assessment", "sub": "served on the consumer · § 126(2)", "icon": "file-text", "at": A("c08", "provisional")},
           {"label": "Objections and a hearing", "sub": "then the final assessment · § 126(3)", "icon": "user", "at": A("c08", "hearing")},
           {"label": "Appeal", "sub": "§ 127 · final only for restoring supply", "icon": "arrow-right", "at": A("c08", "appeal")}],
    note={"text": "Complaint filed: the Special Court fixes civil liability · any excess refunded", "icon": "scale", "at": A("c08", "special")})

# ── 5 · the verdict ──────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c09"), t1=E("c09") + 0.05, head="Restoring supply", head_at=S("c09") + 0.05,
    steps=[{"label": "Theft cases: “a circumspect approach”", "sub": "may even insist on the entire provisionally assessed amount", "icon": "info", "at": A("c09", "theft")},
           {"label": "Prima facie arbitrary: at least 50%", "sub": "reasons recorded · as § 127(2) asks half for an appeal", "icon": "scale", "at": A("c09", "arbitrary")},
           {"label": "Both appeals dismissed", "sub": "clarified: subject to any § 127 appeal and the Special Court", "icon": "check", "tone": "ok", "at": A("c09", "appeals")}])
cue(type="point", t0=S("c10"), t1=E("c10") + 0.05, text="Like · Share · Subscribe · lawworld.ai", icon="check", accent=True, at=A("c10", "like"))
