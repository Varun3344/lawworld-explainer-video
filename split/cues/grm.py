# Greenmount Spices Private Limited v. Wipro Enterprises Private Limited, F.A.O. No. 95 of 2026, 2026:KER:82024 (High Court of Kerala,
# C.S. Dias J., single bench; heard for admission 23.10.2026, judgment 27.10.2026, "C.R" printed above "C.S.DIAS,J." on page 3): panel
# cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND). Concept format as vzj / smt / bcr. English (High Courts).
# Facts from the judgment (paras): appeal against the order of 10.04.2026 in I.A. 4/2024 in O.S. No. 22 of 2024, II Additional District
# Court, Ernakulam; the suit seeks to restrain the appellant from selling food products, including sambar powder, under the
# respondent's mark or any identical or deceptively similar mark, with or without a prefix or suffix; the temporary injunction
# application allowed as prayed for (cause title, 1). Appellant: its trade mark is 'Greenmount'; the rest of the product name is used
# only descriptively; the Trial Court wrongly assumed that expression was used as its trade mark; Section 30(2)(a); Ext. B1 series:
# use since 2011; co-existence for years without confusion (3, 10). Respondent: Wander v. Antox; acquired the group business with trade
# mark and goodwill in 2023; 29 registrations for the word (4, 10); certificates R1(a) to R1(m), thirteen classes, incl. sambar powder
# (6, 10). Held: the interlocutory stage does not decide whether infringement will finally be established (9); Section 30(2)(a) "does
# not confer an unrestricted licence to use a registered expression merely because the user characterises it as descriptive"; whether,
# in context, it is "genuinely used to indicate the kind or another characteristic of the goods"; "Conversely, the existence of a
# registration does not relieve the proprietor of the obligation to establish the elements required by the statutory provision";
# prominence, placement, relative size, other distinctive features: decided only after a full-fledged trial (11). Ext. A1 (13.07.1987)
# prima facie: launched in 1987; Ext. A2 licence (04.07.1987); on the appellant's own case its use began only in 2011; prima facie
# support for the respondent's claim of prior use; the mark 'Greenmount' "does not, by itself, answer the question of infringement";
# the mere appearance of a word on packaging does not establish infringement; average consumer, product as a whole; peaceful
# co-existence does not, by itself, settle it; both sides' pleas "are matters to be adjudicated" (12). Shruti Manav Sharma v. Sunanina
# Singh [2026 KHC OnLine 6611], Supreme Court: interim principles, limited appellate interference (14). Midas Hygiene [2004 KHC 467];
# prima facie case "supported by materials indicating prior commercial use"; balance of convenience for the respondent; continued use,
# if ultimately found infringing, "may erode the distinctiveness"; conclusions "tentative"; no arbitrariness or perversity; appeal
# dismissed; the suit to be decided "untrammelled by any observation" in the impugned order or this judgment (15).
# Interim only: no card states infringement as a final finding; no dishonesty finding against either company is implied.
# Sensitivity: the mark (a community name) appears on NO card; cards say "the word" / "the registered mark"; no comment on any community
# or cuisine. No individual named (no director, no attorney). No "admitted". No section sign anywhere (no "section" card type: it draws one).
# Bench photo: brand/judges/cs_dias_official.jpg = the portrait on the High Court of Kerala's "Present Judges" page (31-10-2026).
# List lines <= 52 chars (9:16 list items do not wrap).
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen, as vzj)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
STING = {"kicker": "KERALA HIGH COURT · JUDGMENT EXPLAINED", "title": "House mark is no free pass", "sub": "High Court of Kerala · F.A.O. No. 95 of 2026 · 2026:KER:82024"}
ENDCARD = {"title": "House mark is no free pass", "line": "Interim injunction upheld · findings tentative: the trial decides", "sub": "LawWorld: legal research for advocates"}

# ── 1 · a rival's word? ──────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "client"), text="Your client sells under its own house mark, but uses a rival's registered word to describe the product. Is that a defence?", hl="a defence?")
cue(type="bench", t0=S("c02"), t1=E("c02") + 0.05, tag="Kerala High Court · 27 October 2026",
    judges=[{"name": "Justice C.S. Dias", "photo": "../brand/judges/cs_dias_official.jpg", "at": A("c02", "honourable")}])

# ── 2 · the dispute ──────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=A("c03", "wipro"), t1=E("c05") + 0.05, at=A("c03", "wipro"), tag="HIGH COURT OF KERALA · 27.10.2026",
    cases=[{"name": "Greenmount Spices Pvt. Ltd. v. Wipro Enterprises Pvt. Ltd.", "cite": "2026:KER:82024 · F.A.O. No. 95 of 2026"}])
cue(type="flow", t0=S("c03"), t1=E("c03") + 0.05, head="Wipro's case", head_at=S("c03") + 0.05,
    steps=[{"label": "Acquired the group business in 2023", "sub": "with its trade mark and goodwill, Wipro says", "icon": "file-check", "at": A("c03", "acquired")},
           {"label": "Relies on 29 registrations for the word", "sub": "13 certificates, R1(a) to R1(m), incl. for sambar powder", "icon": "file-text", "at": A("c03", "trademark")},
           {"label": "Suit against Greenmount Spices", "sub": "the word appears in its sambar powder's name", "icon": "landmark", "at": A("c03", "sued")}])
cue(type="flow", t0=S("c04"), t1=E("c04") + 0.05, head="The interim order", head_at=S("c04") + 0.05,
    steps=[{"label": "Temporary injunction granted", "sub": "II Additional District Court, Ernakulam · 10.04.2026 · I.A. 4/2024 in O.S. 22/2024", "icon": "landmark", "at": A("c04", "granted")},
           {"label": "Greenmount appealed · F.A.O. No. 95 of 2026", "sub": "the trial court took a description to be its trade mark, it argued", "icon": "scale", "at": A("c04", "appealed")}])

# ── 3 · the defence ──────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="list", t0=S("c05"), t1=E("c05") + 0.05, head="Greenmount's defence", head_at=S("c05") + 0.05,
    items=[{"n": 1, "text": "Its trade mark is ‘Greenmount’", "at": A("c05", "greenmount")},
           {"n": 2, "text": "The other words only describe the product", "at": A("c05", "describe")},
           {"n": 3, "text": "Section 30(2)(a), Trade Marks Act, 1999", "at": A("c05", "section")}])

# ── 4 · what the court held ──────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c06"), t1=A("c06", "what") - 0.05, text="Section 30(2)(a) is not “an unrestricted licence to use a registered expression merely because the user characterises it as descriptive”", icon="scale", accent=True, at=A("c06", "calling"))
cue(type="list", t0=A("c06", "what") - 0.05, t1=E("c06") + 0.05, head="Judged in context (para 11)", head_at=A("c06", "what"),
    items=[{"n": 1, "text": "Genuinely shows the kind of goods?", "at": A("c06", "whether")},      # one word early each: the
           {"n": 2, "text": "Prominence and placement of the words", "at": A("c06", "context")},   # clip's last words come fast
           {"n": 3, "text": "Relative size · other distinctive features", "at": A("c06", "genuinely")}])
cue(type="notequal", t0=S("c07"), t1=A("c07", "and") - 0.05, left="Registration alone", right="proof of infringement", at=A("c07", "registration"),
    left_at=A("c07", "registration"), sub="It “does not relieve the proprietor” of proving what the statute requires", sub_at=A("c07", "infringement"))
cue(type="verdicts", t0=A("c07", "and") - 0.05, t1=E("c07") + 0.05,
    rows=[{"text": "Its own mark ‘Greenmount’: no answer, by itself", "ok": False, "at": A("c07", "house")},
          {"text": "Peaceful co-existence: does not, by itself, settle it", "ok": False, "at": A("c07", "peaceful")},
          {"text": "Both sides' pleas: “matters to be adjudicated” at trial", "ok": True, "at": A("c07", "matters")}])
cue(type="timeline", t0=S("c08"), t1=A("c08", "backs") - 0.05,
    nodes=[{"label": "PRIMA FACIE LAUNCH", "value": "1987", "sub": "Ext. A1 notice · Ext. A2 licence", "at": A("c08", "documents")},
           {"label": "GREENMOUNT'S USE", "value": "2011", "sub": "on its own case · Ext. B1 series", "tone": "red", "at": A("c08", "greenmount")}])
cue(type="point", t0=A("c08", "backs") - 0.05, t1=E("c08") + 0.05, text="Prima facie case “supported by materials indicating prior commercial use” · balance of convenience with Wipro (para 15)", icon="file-check", at=A("c08", "backs"))

# ── 5 · the result ───────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="verdicts", t0=S("c09"), t1=E("c09") + 0.05,
    rows=[{"text": "No arbitrariness or perversity in the order", "ok": True, "at": A("c09", "perversity")},
          {"text": "Appeal dismissed: the temporary injunction stays", "ok": True, "at": A("c09", "dismissed")},
          {"text": "Findings tentative: no final finding of infringement", "ok": True, "at": A("c09", "tentative")},
          {"text": "Suit to be decided “untrammelled” by any observation", "ok": True, "at": A("c09", "decided")}])
cue(type="cite", t0=A("c09", "dismissed"), t1=A("c09", "findings") - 0.05, at=A("c09", "dismissed"), tag="SUPREME COURT · RELIED ON",
    cases=[{"name": "Shruti Manav Sharma v. Sunanina Singh", "cite": "2026 KHC OnLine 6611 · limited appellate interference"},
           {"name": "Midas Hygiene Industries v. Sudhir Bhatia", "cite": "2004 KHC 467 · an injunction ordinarily follows"}])
cue(type="point", t0=S("c10"), t1=E("c10") + 0.05, text="Like · Share · Subscribe · lawworld.ai", icon="check", accent=True, at=A("c10", "like"))
