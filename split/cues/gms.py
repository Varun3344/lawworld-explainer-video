# Greenmount Spices Pvt. Ltd. v. Wipro Enterprises Pvt. Ltd., F.A.O. No. 95 of 2026, 2026:KER:82024 (High Court of Kerala, C.S. Dias J.;
# heard for admission 23.10.2026, judgment 27.10.2026, "C.R"): panel cues, run by split/build_course_plan.py (helpers: at S E cue fx have
# r3 PEND). Concept format as ele.
# Facts from the judgment (paras): appeal against the order of 10.04.2026 in I.A. 4/2024 in O.S. No. 22 of 2024, II Additional District
# Court, Ernakulam; the suit seeks to restrain use of the respondent's mark or any identical or deceptively similar mark, with or without
# a prefix or suffix; temporary injunction granted as prayed for (cause title, 1). Appellant: its trade mark is 'Greenmount', the rest of
# the product name is used only descriptively, protected by s.30(2)(a); Ext. B1 series: use since 2011; co-existence without confusion
# (3, 10). Respondent: Wander v. Antox standard; acquired the group business with trade mark and goodwill in 2023; 29 registrations
# for the word; certificates R1(a) to R1(m); thirteen classes, including sambar powder (4, 6, 10). Held: s.30(2)(a) "does not confer an
# unrestricted licence to use a registered expression merely because the user characterises it as descriptive"; overall presentation:
# "prominence, placement and relative size of the words and the presence of other distinctive features"; "These matters can only be
# decided after a full-fledged trial" (11). Ext. A1 (13.07.1987) prima facie: launched in 1987; Ext. A2 licence 04.07.1987; appellant's
# own case: use only from 2011; "lend prima facie support to the respondent's claim of prior use"; the mark 'Greenmount' "does not, by
# itself, answer the question of infringement"; "how the average consumer is likely to perceive the mark and the product as a whole";
# peaceful co-existence does not, by itself, settle it (12). Shruti Manav Sharma v. Sunanina Singh [2026 KHC OnLine 6611]: interim
# principles, limited appellate interference, the vice of the mini-trial (14); Midas Hygiene [2004 KHC 467]: in infringement an
# injunction would ordinarily follow; prima facie case and balance of convenience for the respondent; conclusions "tentative"; no
# arbitrariness or perversity; appeal dismissed; the trial court to decide the suit "untrammelled by any observation" (15).
# Sensitivity: the brand word appears on no card (spoken once in c03, as the business's name); no community or cuisine comment. Interim
# only: no card states infringement as a final finding. No "§" anywhere (no section card: it draws "§" itself). Official portrait.
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen, as tej)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
STING = {"kicker": "KERALA HIGH COURT · JUDGMENT EXPLAINED", "title": "‘Descriptive’ is no free licence", "sub": "Greenmount Spices v. Wipro Enterprises · 2026:KER:82024"}
ENDCARD = {"title": "‘Descriptive’ is no free licence", "line": "Injunction upheld for now: the trial will decide", "sub": "LawWorld: legal research for advocates"}

# ── 1 · just descriptive? ────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=A("c01", "and") - 0.05, at=A("c01", "registered"), text="Can a rival use a registered mark just by calling it descriptive?", hl="descriptive?")
cue(type="question", t0=A("c01", "and"), t1=E("c01") + 0.05, at=A("c01", "house"), text="Does its own house mark save it?", hl="house mark")
cue(type="bench", t0=S("c02"), t1=E("c02") + 0.05, tag="High Court of Kerala · 27 October 2026",
    judges=[{"name": "Justice C.S. Dias", "photo": "../brand/judges/cs_dias.jpg", "at": A("c02", "honourable")}])

# ── 2 · the dispute ──────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=A("c03", "case"), t1=E("c04") + 0.05, at=A("c03", "case"), tag="HIGH COURT OF KERALA · 27.10.2026",
    cases=[{"name": "Greenmount Spices Pvt. Ltd. v. Wipro Enterprises Pvt. Ltd.", "cite": "2026:KER:82024 · F.A.O. No. 95 of 2026"}])
cue(type="flow", t0=S("c03"), t1=E("c03") + 0.05, head="Wipro's case", head_at=S("c03") + 0.05,
    steps=[{"label": "Acquired the group business in 2023", "sub": "with its trade mark and goodwill", "icon": "file-check", "at": A("c03", "acquired")},
           {"label": "29 registrations · 13 certificates", "sub": "including sambar powder · certificates R1(a) to R1(m)", "icon": "file-text", "at": A("c03", "holds")}])
cue(type="flow", t0=S("c04"), t1=E("c04") + 0.05, head="The suit and the interim order", head_at=S("c04") + 0.05,
    steps=[{"label": "Suit: O.S. No. 22 of 2024", "sub": "to restrain use of the mark or any identical or deceptively similar mark, with or without a prefix or suffix", "icon": "file-text", "at": A("c04", "sued")},
           {"label": "Greenmount's sambar powder", "sub": "the word appears in its product name", "icon": "search", "at": A("c04", "powder")},
           {"label": "Temporary injunction granted", "sub": "II Additional District Court, Ernakulam · 10.04.2026 · then this appeal", "icon": "landmark", "at": A("c04", "granted")}])

# ── 3 · the defence ──────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="list", t0=S("c05"), t1=E("c05") + 0.05, head="Greenmount's defence", head_at=S("c05") + 0.05,
    items=[{"n": 1, "text": "Its trade mark is ‘Greenmount’", "at": A("c05", "trademark")},
           {"n": 2, "text": "The other words only describe the product", "at": A("c05", "describe")},
           {"n": 3, "text": "Section 30(2)(a): descriptive use is not infringement", "at": A("c05", "section")}])

# ── 4 · what the court held ──────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c06"), t1=A("c06", "context") - 0.05, text="Section 30(2)(a) is not “an unrestricted licence” to use a registered expression", icon="scale", at=A("c06", "unrestricted"))
cue(type="list", t0=A("c06", "context"), t1=E("c06") + 0.05, head="Judged in context: the overall presentation", head_at=A("c06", "context"),
    items=[{"n": 1, "text": "Prominence of the words", "at": A("c06", "decides")},          # each item one word early: the three
           {"n": 2, "text": "Placement", "at": A("c06", "prominence")},                      # words are spoken in ~1 s at the clip end
           {"n": 3, "text": "Relative size · other distinctive features", "at": A("c06", "placement")}])
cue(type="verdicts", t0=S("c07"), t1=A("c07", "what") - 0.05,
    rows=[{"text": "Own mark ‘Greenmount’: no answer, by itself", "ok": False, "at": A("c07", "house")},
          {"text": "Peaceful co-existence: no answer, by itself", "ok": False, "at": A("c07", "nor")}])
cue(type="point", t0=A("c07", "what"), t1=E("c07") + 0.05, text="The test: “how the average consumer is likely to perceive the mark and the product as a whole”", icon="user", accent=True, at=A("c07", "what"))
cue(type="point", t0=S("c08"), t1=A("c08", "brand") - 0.05, text="“These matters can only be decided after a full-fledged trial”", icon="landmark", at=S("c08") + 0.05)
cue(type="cite", t0=A("c08", "trial"), t1=E("c08") + 0.05, at=A("c08", "trial"), tag="SUPREME COURT · RELIED ON",
    cases=[{"name": "Shruti Manav Sharma v. Sunanina Singh", "cite": "2026 KHC OnLine 6611 · no mini-trial at the interim stage"}])
cue(type="timeline", t0=A("c08", "brand") - 0.05, t1=E("c08") + 0.05,
    nodes=[{"label": "PRIMA FACIE LAUNCH", "value": "1987", "sub": "Ext. A1 notice · Ext. A2 licence", "at": A("c08", "brand")},
           {"label": "GREENMOUNT'S PRODUCT NAME", "value": "2011", "sub": "on its own case", "tone": "red", "at": A("c08", "greenmount's")}])

# ── 5 · the result ───────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="verdicts", t0=S("c09"), t1=E("c09") + 0.05,
    rows=[{"text": "No arbitrariness or perversity in the order", "ok": True, "at": A("c09", "perversity")},
          {"text": "Appeal dismissed: the temporary injunction stands", "ok": True, "at": A("c09", "dismissed")},
          {"text": "Findings tentative: the suit decided “untrammelled” by them", "ok": True, "at": A("c09", "tentative")}])
cue(type="cite", t0=A("c09", "dismissed"), t1=A("c09", "findings") - 0.05, at=A("c09", "dismissed"), tag="SUPREME COURT · RELIED ON",
    cases=[{"name": "Midas Hygiene Industries Pvt. Ltd. v. Sudhir Bhatia", "cite": "2004 KHC 467 · in infringement, an injunction ordinarily follows"}])
cue(type="point", t0=S("c10"), t1=E("c10") + 0.05, text="Like · Share · Subscribe · lawworld.ai", icon="check", accent=True, at=A("c10", "like"))
