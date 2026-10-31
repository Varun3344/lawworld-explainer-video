# The Principal Commissioner of Income Tax, Bhubaneshwar v. Orissa Mining Corporation Ltd., 2026 INSC 1171, C.A. of 2026 @ SLP (C)
# No. 14546 of 2023, with four connected appeals (Sanjeev Sachdeva J. wrote it, Sanjay Kumar J.; decided 28.10.2026, REPORTABLE):
# panel cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND). Concept format as sets dvc / sbp.
# Facts from the judgment (paras): the Revenue's appeals against orders holding against it (2); Orissa Mining Corporation Ltd.: AY
# 2008-09, 2010-11, 2011-12; an individual assessee (not named): AY 2009-10, 2010-11 (2); returns under s.139 assessed under
# s.143(3); reopened under s.147, s.148 notices to file returns in the prescribed form (4); the company asked that its original
# return be treated as its return in response to the s.148 notice; the individual refiled the same return (5); no s.143(2) notice
# issued; s.142(1) notices sought documents / stock information (6); reassessment orders, appealed to the CIT(A) (7); CIT(A): having
# participated after the s.148 and s.142(1) notices, the assessees could not raise it at the appellate stage (8); ITAT: vitiated for
# want of the s.143(2) notice, reassessment orders set aside (9); High Court: the Revenue's challenge rejected, ITAT upheld (10). The
# Revenue: notice not required, its omission not fatal; reliance on s.292BB (14). Held: s.143(2) notice mandatory, the assessee's
# chance to produce evidence; "sine qua non for a proceeding for reassessment under Section 147"; without it "no further proceedings
# can be undertaken" (13); Hotel Blue Moon (2010) 3 SCC 259: not a curable procedural irregularity, cannot be dispensed with (12, 20);
# s.292BB: a notice deemed duly served, in time, properly, where the assessee appeared / co-operated, "only if notice is alleged to
# have been sent" (15, 16); mere participation confers no jurisdiction (17); Laxman Das Khandelwal (2021) 18 SCC 691: s.292BB "does
# not save complete absence of notice" (21); reiterating the original return does not dispense with the notice (18); a s.142(1)
# letter "would not validate what is non est" (22); no infirmity in the ITAT's view as affirmed by the High Court, three questions
# answered (23); appeals dismissed (24).
# Not on any card: which High Court (the judgment says only "the High Court"); costs (none ordered); the individual's name.
# No section sign anywhere: every section is written "Section 143(2)". List lines <= 52 chars (9:16 list items do not wrap). Official sci.gov.in
# portraits on the bench card.
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen, as dvc / sbp)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
STING = {"kicker": "SUPREME COURT · JUDGMENT EXPLAINED", "title": "Can 292BB save a missing notice?", "sub": "Pr. CIT v. Orissa Mining Corporation · 2026 INSC 1171"}
ENDCARD = {"title": "Can 292BB save a missing notice?", "line": "No Section 143(2) notice: taking part cannot save the reassessment", "sub": "LawWorld: legal research for advocates"}

# ── 1 · no notice, still valid? ──────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "section"), text="No Section 143(2) notice was issued, but your client took part anyway. Does that save the reassessment?", hl="Does that save the reassessment?")
cue(type="bench", t0=S("c02"), t1=E("c02") + 0.05, tag="Supreme Court of India · 28 October 2026",
    judges=[{"name": "Justice Sanjay Kumar", "photo": "../brand/judges/sanjay_kumar.jpg", "at": A("c02", "honourable")},
            {"name": "Justice Sanjeev Sachdeva", "photo": "../brand/judges/sanjeev_sachdeva.jpg", "at": A("c02", "honourable", 2)}])

# ── 2 · the reassessment ─────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=A("c03", "orissa"), t1=E("c04") + 0.05, at=A("c03", "orissa"), tag="SUPREME COURT OF INDIA · 28.10.2026",
    cases=[{"name": "Pr. CIT, Bhubaneshwar v. Orissa Mining Corporation Ltd.", "cite": "2026 INSC 1171 · @ SLP (C) No. 14546 of 2023"}])
cue(type="flow", t0=S("c03"), t1=E("c03") + 0.05, head="Orissa Mining Corporation · Income Tax Act", head_at=S("c03") + 0.05,
    steps=[{"label": "Returns for three assessment years", "sub": "AY 2008-09 · 2010-11 · 2011-12 · filed under Section 139", "icon": "calendar", "at": A("c03", "returns")},
           {"label": "Assessed under Section 143(3)", "sub": "assessment orders passed on those returns", "icon": "file-check", "at": A("c03", "assessed")},
           {"label": "Reopened under Section 147", "sub": "Section 148 notices: file returns in the prescribed form", "icon": "search", "at": A("c03", "reopened")}])
cue(type="timeline", t0=S("c04"), t1=E("c04") + 0.05,
    nodes=[{"label": "SECTION 148 NOTICES", "value": "reopening", "sub": "file a return in the prescribed form", "at": A("c04", "notices")},
           {"label": "THE COMPANY'S REPLY", "value": "original returns stand", "sub": "treat the Section 139 returns as the reply to the notices", "at": A("c04", "asked")},
           {"label": "SECTION 143(2) NOTICE", "value": "never issued", "sub": "only Section 142(1) notices, seeking documents and stock information", "tone": "stop", "at": A("c04", "no")}])

# ── 3 · the appeals ──────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="timeline", t0=S("c05"), t1=E("c05") + 0.05,
    nodes=[{"label": "REASSESSMENT ORDERS", "value": "passed", "sub": "challenged: no Section 143(2) notice", "at": A("c05", "reassessment")},
           {"label": "CIT (APPEALS)", "value": "objection rejected", "sub": "took part after the Section 148 and 142(1) notices: too late", "tone": "stop", "at": A("c05", "appellate")},
           {"label": "TRIBUNAL (ITAT)", "value": "set aside", "sub": "proceedings vitiated for want of the notice", "tone": "ok", "at": A("c05", "tribunal")},
           {"label": "HIGH COURT", "value": "Tribunal upheld", "sub": "the Revenue's challenge rejected", "tone": "ok", "at": A("c05", "high")}])
cue(type="flow", t0=S("c06"), t1=E("c06") + 0.05, head="The Revenue in the Supreme Court", head_at=S("c06") + 0.05,
    steps=[{"label": "Five civil appeals · leave granted", "sub": "against the company, and an individual assessee for AY 2009-10, 2010-11", "icon": "landmark", "at": A("c06", "appealed")},
           {"label": "“Not required to be given”", "sub": "the Revenue: failing to give the notice is not fatal to reassessment", "icon": "file-text", "at": A("c06", "needed")},
           {"label": "Section 292BB: deemed service", "sub": "an assessee who appeared or co-operated is deemed duly served", "icon": "scale", "at": A("c06", "relying")}],
    note={"text": "The assessee is then “precluded from taking any objection” that the notice was not served, late, or improperly served", "icon": "info", "at": A("c06", "having")})

# ── 4 · what the court held ──────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c07"), t1=A("c07", "following") - 0.05, text="Section 143(2) notice: “sine qua non for a proceeding for reassessment under Section 147” · without it, “no further proceedings can be undertaken”", icon="scale", accent=True, at=A("c07", "notice"))
cue(type="list", t0=A("c07", "following") - 0.05, t1=E("c07") + 0.05, head="Hotel Blue Moon · (2010) 3 SCC 259", head_at=A("c07", "hotel"),
    items=[{"n": 1, "text": "The notice cannot be dispensed with", "at": A("c07", "moon")},
           {"n": 2, "text": "Omission: not a mere procedural irregularity", "at": A("c07", "absence")},
           {"n": 3, "text": "Not curable: the reassessment stands vitiated", "at": A("c07", "cannot")}])
cue(type="list", t0=S("c08"), t1=A("c08", "cannot") - 0.05, head="Section 292BB: deemed service", head_at=S("c08") + 0.05,
    items=[{"n": 1, "text": "Works only for a notice the Revenue sent", "at": A("c08", "sent")},
           {"n": 2, "text": "Deemed duly served, in time, in proper manner", "at": A("c08", "served")},
           {"n": 3, "text": "Once the assessee appeared or co-operated", "at": A("c08", "takes")}])
cue(type="notequal", t0=A("c08", "cannot") - 0.05, t1=E("c08") + 0.05, left="A notice sent, with defects in its service", right="a notice never issued", at=A("c08", "cannot"),
    left_at=A("c08", "cannot"), sub="Laxman Das Khandelwal (2021) 18 SCC 691: Section 292BB “does not save complete absence of notice” · mere participation confers no jurisdiction", sub_at=A("c08", "never"))

# ── 5 · the verdict ──────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="list", t0=S("c09"), t1=A("c09", "revenue") - 0.05, head="The other two questions", head_at=S("c09") + 0.05,
    items=[{"n": 1, "text": "Original return reused: the notice is still due", "at": A("c09", "standing")},
           {"n": 2, "text": "A Section 142(1) letter is no substitute", "at": A("c09", "section")},
           {"n": 3, "text": "It “would not validate what is non est”", "at": A("c09", "letter")}])
cue(type="verdicts", t0=A("c09", "revenue") - 0.05, t1=E("c09") + 0.05,
    rows=[{"text": "All five Revenue appeals dismissed", "ok": True, "at": A("c09", "appeals")},
          {"text": "Tribunal's view, affirmed by the High Court, stands", "ok": True, "at": A("c09", "were")},
          {"text": "The reassessment orders stay set aside", "ok": True, "at": A("c09", "dismissed")}])
cue(type="point", t0=S("c10"), t1=E("c10") + 0.05, text="Like · Share · Subscribe · lawworld.ai", icon="check", accent=True, at=A("c10", "like"))
