# Nirmala Johny & Ors. v. State of Kerala & Ors. (the Vizhinjam coastal-erosion case), W.P.(C) No. 34157 of 2022, 2026:KER:83112
# (High Court of Kerala, Harisankar V. Menon J., single bench; finally heard 08.10.2026, judgment 30.10.2026, "C.R."): panel cues, run by
# split/build_course_plan.py (helpers: at S E cue fx have r3 PEND). Concept format as cdp / gms / cft.
# Facts from the judgment (paras): petitioners: residents of fishing villages within 20 km north of Vizhinjam, where the seaport is being
# built; they CONTEND its construction caused substantial erosion on the northern side, accretion on the southern side (1); Ext.P11 G.O.
# dated 06.10.2022: an Expert Committee to examine whether there was coastal erosion consequent to the port work and to identify measures
# to address it, hearing the local population first (2); the alleged conflict of interest (1, 3, 6(ii), 14): the chairman an expert
# member of the "Technical Sub-committee" for the development of the Vizhinjam Seaport since 2012, per the CWPRS employee register
# (15(i)); another member President-Technical of a company which "has connection with the 7th respondent" (15(ii), 20), the 7th
# respondent being the concessionaire (6(vi)); the report "diametrically opposite" to the chairman's 2010 paper (15(iv)); the State: the
# erosion came from high wave activity and cyclones "as has been reported by the Committee"; no fresh committee needed (7(ii), 7(iii));
# delay and laches (8(iii), 11). Held: delay repelled, the petition being with reference to the 2022 G.O. (11, 12); no stay of the
# project sought, recorded 22.07.2026: only the committee and its report examined (13); N.K. Bajpai (18); A.K. Kraipak: "a mere
# suspicion of bias is not sufficient. There must be a reasonable likelihood of bias" (19); the chairman's earlier involvement "not
# disputed by any of the respondents"; his inclusion "ought to have been avoided"; the other member's link "not seen denied" by
# respondents 6 and 7; the attack on a third member rejected (his qualification unchallenged) (20); the report "in stark contrast" to
# the chairman's 2010 article (21); challenge accepted (22); "all the more so": one inspection, 23.05.2023, residents met 24.05.2023,
# report approved by G.O. 02.08.2024 (23); the Government cannot now set its own committee aside for the NGT one (24); the Court did not
# name members: the Government to form a fresh committee after the stakeholders' views (25). Orders (26): constitution declared flawed;
# final report not to be acted upon; the Government to constitute an independent committee for the Ext.P11 studies, ensuring no
# conflict of interest. No time limit fixed.
# Not said: the G.O. is NOT quashed; no finding on the erosion or on the report's merits (21); no finding of actual bias.
# Neutral: no company name and no committee member's name on any card (roles only: "the chairman", "another member", "R7").
# List lines <= 52 chars (9:16 list items do not wrap). No section sign anywhere. Official portrait (Kerala HC website) on the bench card.
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen, as srb)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
STING = {"kicker": "KERALA HIGH COURT · JUDGMENT EXPLAINED", "title": "Expert panel flawed by conflict", "sub": "Nirmala Johny v. State of Kerala · 2026:KER:83112"}
ENDCARD = {"title": "Expert panel flawed by conflict", "line": "Report not to be acted upon · an independent committee to be formed", "sub": "LawWorld: legal research for advocates"}

# ── 1 · an insider on the panel? ─────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "expert"), text="Can an expert who worked on a port project sit on the committee checking whether it caused erosion?", hl="sit on the committee")
cue(type="bench", t0=S("c02"), t1=E("c02") + 0.05, tag="Kerala High Court · 30 October 2026",
    judges=[{"name": "Justice Harisankar V. Menon", "photo": "../brand/judges/harisankar_v_menon.jpg", "at": A("c02", "honourable")}])

# ── 2 · the committee ────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=A("c03", "vizhinjam"), t1=E("c06") + 0.05, at=A("c03", "vizhinjam"), tag="HIGH COURT OF KERALA · 30.10.2026",
    cases=[{"name": "Nirmala Johny & Ors. v. State of Kerala & Ors.", "cite": "2026:KER:83112 · W.P.(C) No. 34157 of 2022"}])
cue(type="flow", t0=S("c03"), t1=E("c03") + 0.05, head="The dispute", head_at=S("c03") + 0.05,
    steps=[{"label": "Fishing villages north of Vizhinjam", "sub": "within 20 km of the seaport being built", "icon": "user", "at": A("c03", "fishing")},
           {"label": "Alleged: substantial coastal erosion", "sub": "on the northern side · accretion to the south", "icon": "search", "at": A("c03", "construction")},
           {"label": "Expert Committee · Ext. P11", "sub": "Government Order dated 06.10.2022", "icon": "file-text", "at": A("c03", "formed")}])
cue(type="list", t0=S("c04"), t1=A("c04", "inspected") - 0.05, head="The committee's task · Ext. P11", head_at=S("c04") + 0.05,
    items=[{"n": 1, "text": "Examine: did the port work cause coastal erosion?", "at": A("c04", "check")},
           {"n": 2, "text": "Identify measures to address any erosion", "at": A("c04", "remedies")}])
cue(type="timeline", t0=A("c04", "inspected") - 0.05, t1=E("c04") + 0.05,
    nodes=[{"label": "SITE INSPECTION", "value": "23 May 2023", "sub": "the only one · residents met on 24 May", "at": A("c04", "inspected")},
           {"label": "REPORT APPROVED", "value": "2 Aug 2024", "sub": "the State: high waves and cyclones", "at": A("c04", "report")}])

# ── 3 · the challenge ────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c05"), t1=E("c05") + 0.05, head="Alleged: a conflict of interest", head_at=A("c05", "alleged"),
    steps=[{"label": "The chairman: a Technical Sub-committee member", "sub": "for the development of the Vizhinjam Seaport", "icon": "user", "at": A("c05", "chairman")},
           {"label": "Since 2012", "sub": "per the CWPRS employee register, the petitioners said", "icon": "calendar", "at": A("c05", "since")}])
cue(type="flow", t0=S("c06"), t1=E("c06") + 0.05, head="Also alleged", head_at=S("c06") + 0.05,
    steps=[{"label": "Another member: President-Technical of a company", "sub": "connected with R7, the port concessionaire", "icon": "user", "at": A("c06", "another")},
           {"label": "The report vs the chairman's 2010 paper", "sub": "“diametrically opposite”, the petitioners argued", "icon": "file-text", "at": A("c06", "contradicted")}])

# ── 4 · what the court held ──────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c07"), t1=A("c07", "bias") - 0.05, text="Delay and laches repelled, in the light of the Ext. P11 order of 06.10.2022 that formed the Committee", icon="calendar", at=A("c07", "delay"))
cue(type="notequal", t0=A("c07", "bias") - 0.05, t1=E("c07") + 0.05, left="Mere suspicion of bias", right="a reasonable likelihood", at=A("c07", "suspicion"),
    left_at=A("c07", "suspicion"), sub="“There must be a reasonable likelihood of bias”", sub_at=A("c07", "likelihood"))
cue(type="cite", t0=A("c07", "bias"), t1=E("c07") + 0.05, at=A("c07", "bias"), tag="SUPREME COURT · RELIED ON",
    cases=[{"name": "A.K. Kraipak v. Union of India", "cite": "(1969) 2 SCC 262"},
           {"name": "N.K. Bajpai v. Union of India", "cite": "(2012) 4 SCC 653"}])
cue(type="verdicts", t0=S("c08"), t1=A("c08", "other") - 0.05,
    rows=[{"text": "Chairman's earlier involvement “not disputed by any of the respondents”", "ok": False, "at": A("c08", "disputed")},
          {"text": "His inclusion “ought to have been avoided”", "ok": False, "at": A("c08", "inclusion")}])
cue(type="list", t0=A("c08", "other") - 0.05, t1=E("c08") + 0.05, head="Also noted", head_at=A("c08", "other"),
    items=[{"n": 1, "text": "Other member's link with R7: not denied by R6, R7", "at": A("c08", "member")},
           {"n": 2, "text": "Chairman's 2010 article vs report: “stark contrast”", "at": A("c08", "denied")}])

# ── 5 · the result ───────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c09"), t1=E("c09") + 0.05, head="The orders · para 26", head_at=S("c09") + 0.05,
    steps=[{"label": "The committee's constitution: flawed", "sub": "declared, for the reasons in the judgment", "icon": "x", "at": A("c09", "flawed")},
           {"label": "Its final report: not to be acted upon", "sub": "the Court did not rule on its findings (para 21)", "icon": "file-text", "at": A("c09", "acted")},
           {"label": "Government to form an independent committee", "sub": "for the Ext. P11 studies · no conflict of interest", "icon": "landmark", "tone": "ok", "at": A("c09", "independent")}],
    note={"text": "The Court did not pick members: the Government will, weighing the judgment and stakeholders' views", "icon": "info", "at": A("c09", "free")})
cue(type="point", t0=S("c10"), t1=E("c10") + 0.05, text="Like · Share · Subscribe · lawworld.ai", icon="check", accent=True, at=A("c10", "like"))
