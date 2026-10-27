# Arun @ Deepak v. State of U.P., 2026 INSC 1150, SLP (Crl.) No. 4859 of 2026 (J.B. Pardiwala J., K. Vinod Chandran J.; decided 26.10.2026,
# REPORTABLE): panel cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND). Concept-format judgment reel.
# Facts from the judgment (paras): SLP for bail after six years of custody as an undertrial; FIR 367/2019, PS Achhnera, Agra, s.364 r/w
# 302 and 201 IPC; in jail since 14.11.2019; case "hinging entirely on circumstantial evidence"; order of 23.03.2026: trial to finish in
# three months (1); acquitted; never named in the FIR or the s.161 statement; arrayed on CCTV footage + a co-accused's confession (2);
# "appalled at the manner in which the investigation was carried out" (3); the petitioner alone faced trial; none of the four circumstances
# proved: (i) ransom demand termed an extra-judicial confession, (ii) confessions, (iii) last seen, (iv) electronic evidence (10-12);
# motorcycle not produced, bones not identified by DNA (FSL result not disclosed), CCTV and CDR without a s.65B certificate (12-13);
# State Police "would do well to educate their officers in the process of investigation", copy to the DGP and Home Secretary, U.P. (14);
# "six years have been erased from the life of a man ... mere surmises and conjectures"; "a victim of the system" (15); the State to pay
# Rs 6,00,000 within one month, "though paltry", else interest @ 18% per annum (16); SLP disposed of, pending applications rejected (17).
# He was ACQUITTED: no card states the charge as a fact about him; the deceased is not described. The bench card uses the official portraits.
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow (24 + 58 px) ends inside the panel: the 9:16 band edge cut it into a line at 40
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen (no blobs / star behind the cards)
STING = {"kicker": "SUPREME COURT · JUDGMENT EXPLAINED", "title": "Six years an undertrial: the State pays ₹6 lakh", "sub": "Arun @ Deepak v. State of U.P. · 2026 INSC 1150"}
ENDCARD = {"title": "Six years an undertrial: the State pays ₹6 lakh", "line": "Acquitted after a slipshod investigation · ₹6 lakh compensation", "sub": "LawWorld: legal research for advocates"}

# ── 1 · who pays? ────────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "undertrial"), text="Six years as an undertrial, then acquitted: can the Court make the State pay?", hl="make the State pay?")
cue(type="bench", t0=S("c02"), t1=E("c02") + 0.05, tag="Supreme Court of India · 26 October 2026",
    judges=[{"name": "Justice J.B. Pardiwala", "photo": "../brand/judges/jb_pardiwala.jpg", "at": A("c02", "honourable")},
            {"name": "Justice K. Vinod Chandran", "photo": "../brand/judges/k_vinod_chandran.jpg", "at": A("c02", "honourable", 2)}])

# ── 2 · the case ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=A("c03", "petitioner"), t1=E("c04") + 0.05, at=A("c03", "petitioner"), tag="SUPREME COURT OF INDIA · 26.10.2026",
    cases=[{"name": "Arun @ Deepak v. State of U.P.", "cite": "2026 INSC 1150 · SLP (Crl.) No. 4859 of 2026"}])
cue(type="flow", t0=S("c03"), t1=E("c03") + 0.05, head="The bail plea", head_at=S("c03") + 0.05,
    steps=[{"label": "Arun @ Deepak", "sub": "in jail since 14 Nov 2019", "icon": "user", "at": A("c03", "petitioner")},
           {"label": "Bail plea in the Supreme Court", "sub": "after six years as an undertrial", "icon": "file-text", "at": A("c03", "bail")},
           {"label": "Circumstantial evidence only", "sub": "FIR 367/2019, Agra · IPC 364 r/w 302, 201", "icon": "search", "at": A("c03", "circumstantial")}])
cue(type="flow", t0=S("c04"), t1=E("c04") + 0.05, head="How he became an accused", head_at=S("c04") + 0.05,
    steps=[{"label": "Not named in the FIR", "sub": "nor in the s.161 statement", "icon": "x", "tone": "stop", "at": A("c04", "named")},
           {"label": "CCTV footage", "sub": "he was seen in it", "icon": "search", "at": A("c04", "footage")},
           {"label": "A co-accused's confession", "sub": "→ arrayed as an accused", "icon": "file-text", "at": A("c04", "confession")}])

# ── 3 · the acquittal ────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="timeline", t0=S("c05"), t1=E("c05") + 0.05,
    nodes=[{"label": "IN JAIL SINCE", "value": "14 Nov 2019", "sub": "an undertrial", "at": A("c05", "in")},
           {"label": "SUPREME COURT", "value": "23 Mar 2026", "sub": "finish the trial in 3 months", "at": A("c05", "march")},
           {"label": "TRIAL COURT", "value": "Acquitted", "sub": "the only accused who faced trial", "at": A("c05", "acquitted")}])

# ── 4 · what went wrong ──────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c06"), t1=A("c06", "ransom") - 0.05, text="Trial court: none of the four circumstances proved", icon="x", at=A("c06", "none"))
cue(type="verdicts", t0=A("c06", "ransom") - 0.05, t1=E("c06") + 0.05,
    rows=[{"text": "Ransom demand as an “extra-judicial confession”", "ok": False, "at": A("c06", "ransom"), "strike_at": A("c06", "evidence")},
          {"text": "Confessions to the police", "ok": False, "at": A("c06", "confessions"), "strike_at": A("c06", "reading")},
          {"text": "“Last seen” theory", "ok": False, "at": A("c06", "last"), "strike_at": A("c06", "that")},
          {"text": "Electronic evidence: CCTV, call records", "ok": False, "at": A("c06", "electronic"), "strike_at": A("c06", "judgment")}])
cue(type="list", t0=S("c07"), t1=E("c07") + 0.05, head="“Appalled” at the investigation", head_at=S("c07") + 0.05,
    items=[{"n": 1, "text": "Remains not identified by DNA", "at": A("c07", "remains")},
           {"n": 2, "text": "Motorcycle not produced at trial", "at": A("c07", "motorcycle")},
           {"n": 3, "text": "CCTV and call records: no § 65B certificate", "at": A("c07", "call")}])

# ── 5 · six years, six lakh ──────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c08"), t1=A("c08", "state") - 0.05, text="“Six years have been erased from the life of a man”", icon="scale", accent=True, at=A("c08", "six"))
cue(type="flow", t0=A("c08", "state"), t1=E("c08") + 0.05, head="To the State Police", head_at=A("c08", "state"),
    steps=[{"label": "“Educate their officers”", "sub": "in the process of investigation", "icon": "info", "at": A("c08", "educate")},
           {"label": "Order sent to the DGP", "sub": "and the Home Secretary, U.P.", "icon": "file-text", "at": A("c08", "officers")}])
cue(type="counters", t0=S("c09"), t1=E("c09") + 0.05, head="“A victim of the system”", head_at=A("c09", "victim"),
    items=[{"value": 6, "unit": "₹ LAKH", "label": "Compensation", "sub": "to the petitioner, “though paltry”", "at": A("c09", "six")},
           {"value": 1, "unit": "MONTH", "label": "Time to pay", "sub": "the State of Uttar Pradesh", "at": A("c09", "month")},
           {"value": 18, "unit": "% A YEAR", "label": "If paid late", "sub": "interest", "tone": "red", "at": A("c09", "eighteen")}],
    note={"text": "SLP disposed of · pending applications rejected", "icon": "check", "at": A("c09", "petition")})
cue(type="point", t0=S("c10"), t1=E("c10") + 0.05, text="Judgments made simple · lawworld.ai", icon="check", accent=True, at=A("c10", "judgments"))
