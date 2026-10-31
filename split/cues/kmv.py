# M/s KMV Projects v. State Project Director, Rashtriya Madhyamika Shiksha Abhiyan & Anr., COMAP No. 87 of 2025 (High Court of
# Karnataka, Vibhu Bakhru CJ wrote it, K.S. Hemalekha J.; pronounced 28.10.2026, REPORTABLE): panel cues, run by
# split/build_course_plan.py (helpers: at S E cue fx have r3 PEND). Concept format as sets cdp / levi.
# Facts from the judgment (paras): appeal under s.13(1A) CC Act r/w s.37(1)(c) A&C Act against the Commercial Court's order of
# 05.12.2024 in Com.A.P. 99/2024 (1); RMSA, a centrally sponsored scheme for secondary education, run in Karnataka through the SPD (4);
# Package B-7, new school buildings / additional rooms for Government High Schools in Bidar District; KMV the L1 bidder, cut its rates
# in negotiations (5); LoA 18.03.2013, ₹2,417.83 lakh (6); Agreement 15.05.2013 (7); sixteen months to complete from 17.05.2013 (8);
# works not completed in time; KMV invoked the price adjustment clause, none of the bills paid; the SPD said no such clause applied
# (9); Claim No. 1, price adjustment/escalation ₹2,33,19,736 (16); the tribunal: delay solely attributable to the SPD; Claim 1 rejected
# because (i) no price variation clause in the Agreement, (ii) KMV failed to prove the amount was payable (20); award 10.11.2023:
# ₹61,61,668 (Claims 6(a), 7) + 9% future interest, ₹2,00,000 costs (1, 2, 22); the SPD's own appeal on the awarded sums is
# separate (COMAP 61/2025); this appeal confined to Claim 1 (3, 25); s.33 application 15.12.2023 for an additional award on Claim 1:
# "by inadvertent error" KMV had filed "old and obsolete tender documents"; not a clerical error under s.33, rejected 05.03.2024 (23);
# s.34 petition dismissed 05.12.2024 (24); KMV: the SPD never disputed the quantum (26); KMV should have been permitted to produce the
# tender documents without the note (34; the revised tender document, Ex.C79: 39); no averment on how ₹2,33,19,736 was computed (29);
# the tender documents' note: the Price Adjustment / Variation Clause "may be treated as deleted" (32, 38 quoting award para 190);
# Ex.C1, as produced by KMV, carried the note (37, 38); held: KMV failed to produce the documents it now relies on, the tribunal's
# decision "cannot be faulted" (40); the conclusion rested on the contract documents as proved by KMV; the SPD contested that the note
# was dropped and led evidence (41); limited scope of s.34, no interference (42); no evidence of the amounts per component (43); even
# with the clause, no amount without the quantum (44); no patent illegality; entitlement "but also the measure of such damages" (45);
# the Commercial Court rightly declined to interfere (46); appeal dismissed (47).
# Flow policy: a company and a public office only; the arbitrator (respondent 2) is not named. No "admitted" on any card.
# The clause number differs inside the judgment (Sl.No.39 in para 32, Sl.No.40 in the award quoted at 38): no number on the cards.
# Official Karnataka High Court portraits on the bench card. List lines <= 52 chars (9:16 list items do not wrap).
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen, as cdp)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
STING = {"kicker": "KARNATAKA HIGH COURT · JUDGMENT EXPLAINED", "title": "Price escalation clause deleted", "sub": "High Court of Karnataka · COMAP No. 87 of 2025"}
ENDCARD = {"title": "Price escalation clause deleted", "line": "KMV's own exhibit showed the clause deleted · quantum not proved", "sub": "LawWorld: legal research for advocates"}

# ── 1 · the deleted clause ───────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "tender"), text="Your client's own tender exhibit deletes the price escalation clause. Can a Section 34 court still save the claim?", hl="still save the claim?")
cue(type="bench", t0=S("c02"), t1=E("c02") + 0.05, tag="Karnataka High Court · 28 October 2026",
    judges=[{"name": "Chief Justice Vibhu Bakhru", "photo": "../brand/judges/vibhu_bakhru.jpg", "at": A("c02", "honourable")},
            {"name": "Justice K.S. Hemalekha", "photo": "../brand/judges/ks_hemalekha.jpg", "at": A("c02", "honourable", 2)}])

# ── 2 · the escalation claim ─────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=A("c03", "projects"), t1=E("c05") + 0.05, at=A("c03", "projects"), tag="HIGH COURT OF KARNATAKA · 28.10.2026",
    cases=[{"name": "M/s KMV Projects v. State Project Director, RMSA & Anr.", "cite": "Commercial Appeal (COMAP) No. 87 of 2025"}])
cue(type="flow", t0=S("c03"), t1=E("c03") + 0.05, head="The contract", head_at=S("c03") + 0.05,
    steps=[{"label": "RMSA Package B-7 · Bidar District", "sub": "school buildings · LoA 18 Mar 2013 · ₹2,417.83 lakh", "icon": "landmark", "at": A("c03", "contracted")},
           {"label": "The works ran late", "sub": "not completed within the 16 months stipulated", "icon": "calendar", "at": A("c03", "works")},
           {"label": "Price escalation bills: unpaid", "sub": "the Project Director: no price adjustment clause applied", "icon": "x", "tone": "stop", "at": A("c03", "escalation")}])
cue(type="verdicts", t0=S("c04"), t1=E("c04") + 0.05,
    rows=[{"text": "Delay: solely attributable to the Project Director", "ok": True, "at": A("c04", "arbitration")},
          {"text": "Awarded ₹61,61,668 + 9% interest (Claims 6(a), 7)", "ok": True, "at": A("c04", "awarded")},
          {"text": "Claim 1, price escalation: ₹2,33,19,736", "ok": False, "at": A("c04", "escalation"), "strike_at": A("c04", "rejected")}])
cue(type="flow", t0=S("c05"), t1=E("c05") + 0.05, head="Why Claim 1 failed", head_at=A("c05", "reason"),
    steps=[{"label": "Ex. C1: produced by KMV itself", "sub": "the tender document the tribunal relied on", "icon": "file-text", "at": A("c05", "document")},
           {"label": "Note in the Contract Data", "sub": "the price adjustment / variation clause “may be treated as deleted”", "icon": "x", "tone": "stop", "at": A("c05", "note")},
           {"label": "Amount not proved", "sub": "KMV failed to prove the sum claimed was payable", "icon": "search", "tone": "stop", "at": A("c05", "failed")}])

# ── 3 · the obsolete documents ───────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c06"), t1=E("c06") + 0.05, head="Section 33 application · 15 Dec 2023", head_at=A("c06", "section"),
    steps=[{"label": "An additional award on Claim 1", "sub": "sought from the tribunal", "icon": "file-text", "at": A("c06", "said")},
           {"label": "“old and obsolete tender documents”", "sub": "filed “by inadvertent error”, KMV said", "icon": "info", "at": A("c06", "obsolete")},
           {"label": "Not a clerical error", "sub": "rejected by the tribunal · 5 Mar 2024", "icon": "x", "tone": "stop", "at": A("c06", "clerical")}])
cue(type="point", t0=S("c07"), t1=A("c07", "appeal") - 0.05, text="Section 34 petition (Com.A.P. 99/2024) dismissed by the Commercial Court · 5 Dec 2024", icon="landmark", at=A("c07", "section"))
cue(type="list", t0=A("c07", "appeal") - 0.05, t1=E("c07") + 0.05, head="KMV's case in the appeal", head_at=A("c07", "appeal"),
    items=[{"n": 1, "text": "Should have been allowed to file its revised tender", "at": A("c07", "allowed")},
           {"n": 2, "text": "The quantum was never disputed", "at": A("c07", "amount")}])

# ── 4 · what the court held ──────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c08"), t1=E("c08") + 0.05, head="Held: no interference", head_at=A("c08", "held"),
    steps=[{"label": "The award rested on KMV's own documents", "sub": "the contract documents as proved by KMV", "icon": "file-check", "at": A("c08", "rested")},
           {"label": "They showed the clause deleted", "sub": "the Project Director contested the plea and led evidence", "icon": "x", "tone": "stop", "at": A("c08", "showed")},
           {"label": "Section 34: a limited scope", "sub": "the tribunal's decision “cannot be faulted”", "icon": "scale", "tone": "ok", "at": A("c08", "narrow")}],
    note={"text": "KMV failed to produce the documents it now relies on", "icon": "info", "at": A("c08", "scope")})

# ── 5 · the verdict ──────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c09"), t1=E("c09") + 0.05, head="Even with the clause", head_at=A("c09", "even"),
    steps=[{"label": "No basis shown for ₹2,33,19,736", "sub": "no averment on how it was computed · no calculation sheet", "icon": "search", "tone": "stop", "at": A("c09", "computed")},
           {"label": "Entitlement and the measure", "sub": "KMV had to establish both · no patent illegality", "icon": "scale", "at": A("c09", "measure")},
           {"label": "Appeal dismissed", "sub": "the Commercial Court rightly declined to interfere", "icon": "check", "tone": "ok", "at": A("c09", "dismissed")}])
cue(type="point", t0=S("c10"), t1=E("c10") + 0.05, text="Like · Share · Subscribe · lawworld.ai", icon="check", accent=True, at=A("c10", "like"))
