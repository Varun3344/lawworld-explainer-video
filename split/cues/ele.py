# Krishnankutty U.P. v. State of Kerala & Anr., Crl.M.C. No. 6502 of 2025, 2026:KER:79734 (High Court of Kerala, A. Badharudeen J.;
# came up for admission and decided 15.10.2026, "C.R."): panel cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3
# PEND). Concept format as sets san / bis.
# Facts from the judgment (paras): Crl.M.C. by the sole accused to quash the FIS and FIR in Crime No. 1000/2023 of Karunagappally Police
# Station, ss.406 and 420 IPC (1); title and custody under Annexure A3 (3, 8); A3 recites: the elephant "Madhu", owned by its donor,
# gifted to a Math, which renamed it "Raman"; periodic musth with a direct impact on the safety of the devotees, so the Math gifted it
# back to the donor by Annexure A4 of 18.02.2017; the donor then gifted it to the petitioner (16; A3 dated 28.02.2017 per the appendix);
# the complaint: entrusted to the accused, as he had other elephants, during musth; not returned when asked (14); the complainant
# disputes A3 and A4 (17). Objection: Crl.M.C. No. 4989 of 2024 for the same relief, filed earlier, withdrawn without liberty while
# this one was pending: "not maintainable" (9); held: "mere technicalities would not stand in the way" of relief if the petitioner is
# really entitled (11); his case "was never decided by this Court in any proceedings"; objection dispelled (13). Merits: ss.420 and 406
# "are fundamentally contradictory and cannot co-exist or go together based on the exact same set of allegations"; Delhi Race Club
# (1940) Ltd. v. State of U.P., (2024) 10 SCC 690 (14); the complainant's counsel: s.420 not attracted prima facie, s.406 is (15);
# s.406 needs "entrustment of property by a person having dominion over it"; one who has parted with title and possession ceases to
# have any dominion, authority or control; disputed title under the gift deeds is for a competent civil court (17); "for want of even
# primary materials" for s.406 or s.420, the Crl.M.C. is allowed, the FIR and all further proceedings quashed (17, order).
# No private person's name and no institution's name on any card except the case title; the judgment's slips ("domain", "seized",
# "O.P.") are not repeated. No "§" anywhere (no section card: it draws "§" itself). The bench card uses the official portrait.
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen, as tej)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
STING = {"kicker": "KERALA HIGH COURT · JUDGMENT EXPLAINED", "title": "A gifted elephant and Section 406", "sub": "Krishnankutty U.P. v. State of Kerala · 2026:KER:79734"}
ENDCARD = {"title": "A gifted elephant and Section 406", "line": "No dominion, no entrustment: the FIR is quashed", "sub": "LawWorld: legal research for advocates"}

# ── 1 · gift or trust? ───────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "gifted"), text="Can a gifted elephant become a breach-of-trust case?", hl="breach-of-trust case?")
cue(type="bench", t0=S("c02"), t1=E("c02") + 0.05, tag="High Court of Kerala · 15 October 2026",
    judges=[{"name": "Justice A. Badharudeen", "photo": "../brand/judges/a_badharudeen.jpg", "at": A("c02", "honourable")}])

# ── 2 · the elephant ─────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=A("c03", "case"), t1=E("c04") + 0.05, at=A("c03", "case"), tag="HIGH COURT OF KERALA · 15.10.2026",
    cases=[{"name": "Krishnankutty U.P. v. State of Kerala", "cite": "2026:KER:79734 · Crl.M.C. No. 6502 of 2025"}])
cue(type="flow", t0=S("c03"), t1=E("c03") + 0.05, head="The petitioner's case: two gift deeds", head_at=S("c03") + 0.05,
    steps=[{"label": "Gifted to a Math", "sub": "“Madhu”, renamed “Raman” by the Math", "icon": "arrow-right", "at": A("c03", "gifted")},
           {"label": "Gifted back to the donor", "sub": "periodic musth, a risk to devotees' safety · deed of 18.02.2017", "icon": "file-text", "at": A("c03", "twenty")},
           {"label": "Gifted to the petitioner", "sub": "by the donor · deed of 28.02.2017", "icon": "file-check", "at": A("c03", "donor")}])
cue(type="flow", t0=S("c04"), t1=E("c04") + 0.05, head="The complaint, as alleged", head_at=S("c04") + 0.05,
    steps=[{"label": "Only entrusted, during musth", "sub": "as the petitioner had other elephants", "icon": "user", "at": A("c04", "entrusted")},
           {"label": "Not returned when asked", "sub": "despite an alleged promise to return it", "icon": "x", "tone": "stop", "at": A("c04", "returned")},
           {"label": "FIR · Sections 406 and 420 IPC", "sub": "Crime No. 1000/2023 · Karunagappally Police Station", "icon": "file-text", "at": A("c04", "registered")}])

# ── 3 · a second petition ────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c05"), t1=A("c05", "court") - 0.05, head="Objection: “not maintainable”", head_at=A("c05", "objected"),
    steps=[{"label": "Crl.M.C. No. 4989 of 2024", "sub": "filed earlier, to quash the same FIR", "icon": "file-text", "at": A("c05", "earlier")},
           {"label": "Withdrawn without liberty", "sub": "while this Crl.M.C. was pending", "icon": "x", "tone": "stop", "at": A("c05", "withdrawn")}])
cue(type="list", t0=A("c05", "court"), t1=E("c05") + 0.05, head="Objection rejected", head_at=A("c05", "court"),
    items=[{"n": 1, "text": "Mere technicalities do not block relief to one really entitled", "at": A("c05", "technicalities")},
           {"n": 2, "text": "His case had never been decided by the High Court", "at": A("c05", "way")}])

# ── 4 · what the court held ──────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="notequal", t0=S("c06"), t1=E("c06") + 0.05, left="Cheating", right="Breach of trust",
    at=A("c06", "cheating"), left_at=A("c06", "cheating"), sub="“Fundamentally contradictory”: they cannot co-exist on the same set of allegations", sub_at=A("c06", "co-exist"))
cue(type="cite", t0=A("c06", "held"), t1=E("c06") + 0.05, at=A("c06", "held"), tag="SUPREME COURT · RELIED ON",
    cases=[{"name": "Delhi Race Club (1940) Ltd. & Ors. v. State of U.P. & Anr.", "cite": "(2024) 10 SCC 690"}])
cue(type="point", t0=S("c07"), t1=A("c07", "but") - 0.05, text="Complainant's counsel: Section 420 not attracted, but Section 406 is", icon="user", at=A("c07", "counsel"))
cue(type="list", t0=A("c07", "but"), t1=E("c07") + 0.05, head="Section 406 IPC needs, at its root", head_at=A("c07", "section"),
    items=[{"n": 1, "text": "Entrustment of the property", "at": A("c07", "entrustment")},
           {"n": 2, "text": "by a person having dominion over it", "at": A("c07", "dominion")}])
cue(type="flow", t0=S("c08"), t1=A("c08", "complainant") - 0.05, head="No dominion, no entrustment", head_at=S("c08") + 0.05,
    steps=[{"label": "Title and possession parted with", "sub": "for instance, by a deed of gift", "icon": "file-check", "at": A("c08", "parted")},
           {"label": "Ceases to have dominion", "sub": "nothing left to entrust: no Section 406 offence, prima facie", "icon": "x", "tone": "stop", "at": A("c08", "ceases")}])
cue(type="point", t0=A("c08", "complainant"), t1=E("c08") + 0.05, text="Disputed gift deeds: title is for a competent civil court", icon="landmark", accent=True, at=A("c08", "disputes"))

# ── 5 · the result ───────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "court") - 0.05, text="Not even primary material for Section 406 or Section 420", icon="x", at=A("c09", "primary"))
cue(type="verdicts", t0=A("c09", "court"), t1=E("c09") + 0.05,
    rows=[{"text": "Crl.M.C. allowed", "ok": True, "at": A("c09", "allowed")},
          {"text": "FIR in Crime No. 1000/2023 and all further proceedings quashed", "ok": True, "at": A("c09", "further")}])
cue(type="point", t0=S("c10"), t1=E("c10") + 0.05, text="Like · Share · Subscribe · lawworld.ai", icon="check", accent=True, at=A("c10", "like"))
