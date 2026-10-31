# Girishbhai Natwarlal Patel v. Gautam Punjabhai Palkhiwala (Dead) by LRs & Ors., 2026 INSC 1177, Civil Appeal Nos. 14017-14018 of
# 2026 (J.B. Pardiwala J. wrote it, K. Vinod Chandran J.; decided 30.10.2026, REPORTABLE): panel cues, run by
# split/build_course_plan.py (helpers: at S E cue fx have r3 PEND). Concept format as sets srb / gpk.
# Facts from the judgment (paras): sale deed 29.08.1975, the original owner to the respondents' predecessor, "not in dispute" (18(i),
# 24(i), 60); registered agreement to sell 11.09.1996, the owner's heirs to a housing society (18(iii)(ii), 61); Civil Suit No. 322
# of 2012 for specific performance, May 2012 (18(v)); compromise pursis + consent decree 29.04.2013 (3, 18(vi)); execution 2020; sale
# deed 18.06.2022 by the Court Commissioner to the appellant, the society a confirming party (18(vii), 18(viii), 61); Respondents 1-9
# never parties to the suit or the compromise (34(ii), 39, 59); First Appeal 28.02.2024 (24(vii)); Gujarat High Court (27, 72): ex
# parte ad interim injunction 02.04.2024, no dealing with the land (3, 4); 14.08.2024: injunction confirmed, 11 years' delay
# condoned, leave granted (3, 7); the appellant's case: s.96(3) bars an appeal from a consent decree, a non-party "cannot get a cause
# of action" to challenge it; Pushpa Devi Bhagat, Triloki Nath Singh (13, 43); also the delay and the injunction (8); three issues
# (34); "thoroughly misplaced" (43); s.96(3) text (45); the bar and the estoppel rest on the compromise between the parties, finality,
# no resiling (47); Pushpa Devi relates only to parties (51); Triloki Nath: a buyer pendente lite through a party is bound; here
# complete strangers tracing no claim through any party: distinguished (52); a stranger not "deemed to have consented"; "limited to
# the parties to the compromise and act as an estoppel only with respect to them" (53); no unrestricted right of appeal: prima facie
# prejudice + leave (54, 55); a consent decree: no "distinct or more restrictive test" (56); not for a remote or indirect effect (58,
# H. Anjanappa); a legally cognisable interest, leave justified, no view on the merits (62); knowledge not assumed from the date of
# the decree (63); they CLAIM awareness around August 2023, RTI reply 21.03.2024 (64); no error in condoning (65); injunction: no error, the land
# might be alienated, the appellant heard before it was continued (37, 39, 40, 41); does not warrant interference (66); appeals
# dismissed (69); the High Court "requested" to decide the main appeal within three months (71).
# Flow policy: no private person is named in speech; party names on the cite card only (not the sting); no "fraud" / "collusion" on
# any card (the Court records no finding: 35, 61, 62, 67). No section card: it would print "§". Official portraits on the bench card.
# List lines <= 52 chars (9:16 list items do not wrap).
# Fact-check 31-10-2026: the compromise pursis was signed by the heirs AND the society (18(vi)); 14.08.2024 also confirmed the
# injunction (7); para 53 says "not precluded from asserting", not "free to assert" (54: leave still needed); para 56 has no "no"
# inside the quote; awareness ~Aug 2023 is the respondents' claim (64); c09 anchors moved with the new c09 line.
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen, as srb)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
STING = {"kicker": "SUPREME COURT · JUDGMENT EXPLAINED", "title": "Who can appeal a consent decree?", "sub": "2026 INSC 1177 · Civil Appeal Nos. 14017-14018 of 2026"}
ENDCARD = {"title": "Who can appeal a consent decree?", "line": "Section 96(3) binds only the parties to the compromise", "sub": "LawWorld: legal research for advocates"}

# ── 1 · can a stranger appeal? ───────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "consent"), text="Section 96(3) CPC: no appeal lies from a consent decree. Does that bar stop a stranger to the compromise?", hl="a stranger to the compromise?")
cue(type="bench", t0=S("c02"), t1=E("c02") + 0.05, tag="Supreme Court of India · 30 October 2026",
    judges=[{"name": "Justice J.B. Pardiwala", "photo": "../brand/judges/jb_pardiwala.jpg", "at": A("c02", "honourable")},
            {"name": "Justice K. Vinod Chandran", "photo": "../brand/judges/k_vinod_chandran.jpg", "at": A("c02", "honourable", 2)}])

# ── 2 · the consent decree ───────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=A("c03", "owner"), t1=E("c05") + 0.05, at=A("c03", "owner"), tag="SUPREME COURT OF INDIA · 30.10.2026",
    cases=[{"name": "Girishbhai Natwarlal Patel v. Gautam Punjabhai Palkhiwala (D) by LRs", "cite": "2026 INSC 1177 · Civil Appeal Nos. 14017-14018 of 2026"}])
cue(type="timeline", t0=S("c03"), t1=E("c03") + 0.05,
    nodes=[{"label": "SALE DEED", "value": "29 Aug 1975", "sub": "the owner → the respondents' predecessor", "at": A("c03", "sold")},
           {"label": "AGREEMENT TO SELL", "value": "11 Sep 1996", "sub": "the owner's heirs → a housing society", "at": A("c03", "agreed")}])
cue(type="flow", t0=S("c04"), t1=E("c04") + 0.05, head="The suit and the decree", head_at=S("c04") + 0.05,
    steps=[{"label": "Suit for specific performance", "sub": "Civil Suit No. 322 of 2012 · on the 1996 agreement", "icon": "file-text", "at": A("c04", "sued")},
           {"label": "Consent decree · 29 Apr 2013", "sub": "on a compromise pursis by the heirs and the society", "icon": "scale", "at": A("c04", "consent")},
           {"label": "Sale deed to the appellant · 18 Jun 2022", "sub": "in execution, by the Court Commissioner", "icon": "file-check", "at": A("c04", "conveyed")}])
cue(type="point", t0=S("c05"), t1=A("c05", "high") - 0.05, text="The respondents: never parties to the suit or the compromise · First Appeal filed 28 Feb 2024", icon="user", at=A("c05", "strangers"))
cue(type="timeline", t0=A("c05", "high") - 0.05, t1=E("c05") + 0.05,
    nodes=[{"label": "EX PARTE INJUNCTION", "value": "2 Apr 2024", "sub": "Gujarat High Court · no dealing with the land", "at": A("c05", "restrained")},
           {"label": "INJUNCTION CONFIRMED", "value": "14 Aug 2024", "sub": "11 years' delay condoned · leave granted", "at": A("c05", "condoned")}])

# ── 3 · the challenge ────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c06"), t1=E("c06") + 0.05, head="The appellant's case", head_at=A("c06", "appellant"),
    steps=[{"label": "Section 96(3) CPC: no appeal lies", "sub": "from a decree passed “with the consent of parties”", "icon": "scale", "at": A("c06", "section")},
           {"label": "A stranger has no cause of action", "sub": "to challenge the compromise decree", "icon": "user", "at": A("c06", "stranger")},
           {"label": "Pushpa Devi Bhagat · Triloki Nath Singh", "sub": "among the precedents relied on", "icon": "file-text", "at": A("c06", "compromise")}],
    note={"text": "Also challenged: the 11 years' delay and the ex parte injunction", "icon": "info", "at": A("c06", "challenge")})

# ── 4 · what the court held ──────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c07"), t1=E("c07") + 0.05, head="Section 96(3) r/w Order XXIII Rules 3 and 3A", head_at=A("c07", "bar"),
    steps=[{"label": "Founded on the compromise between the parties", "sub": "finality: no resiling from what they agreed", "icon": "file-text", "at": A("c07", "estoppel")},
           {"label": "Bar and estoppel bind only the parties", "sub": "“limited to the parties to the compromise”", "icon": "scale", "at": A("c07", "bind")},
           {"label": "A stranger: not deemed to have consented", "sub": "not barred from asserting an independent right", "icon": "user", "tone": "ok", "at": A("c07", "stranger")}],
    note={"text": "Pushpa Devi Bhagat: about parties only · Triloki Nath: a buyer through a party, distinguished", "icon": "info", "at": A("c07", "not")})
cue(type="list", t0=S("c08"), t1=A("c08", "consent") - 0.05, head="Leave to appeal: the test", head_at=A("c08", "stranger"),
    items=[{"n": 1, "text": "No unrestricted right: leave of the court", "at": A("c08", "needs")},
           {"n": 2, "text": "Prima facie prejudice to his rights or interests", "at": A("c08", "prima")}])
cue(type="point", t0=A("c08", "consent") - 0.05, t1=E("c08") + 0.05, text="A consent decree: no “distinct or more restrictive test” · here, leave rightly granted, with no view on the merits", icon="scale", accent=True, at=A("c08", "consent"))

# ── 5 · the verdict ──────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="notequal", t0=S("c09"), t1=A("c09", "condoning") - 0.05, left="The decree's date", right="their knowledge of it", at=A("c09", "knowledge"),
    left_at=A("c09", "knowledge"), sub="Non-parties: knowledge is not assumed from the date of the decree", sub_at=A("c09", "assumed"))
cue(type="flow", t0=A("c09", "condoning") - 0.05, t1=E("c09") + 0.05, head="The verdict", head_at=A("c09", "condoning"),
    steps=[{"label": "Delay condoned: no error", "sub": "their claim: aware around Aug 2023 · RTI reply 21 Mar 2024", "icon": "calendar", "tone": "ok", "at": A("c09", "error")},
           {"label": "Injunction: no interference", "sub": "the appellant was heard before it was continued", "icon": "landmark", "at": A("c09", "injunction")},
           {"label": "Appeals dismissed", "sub": "High Court requested to decide the main appeal in 3 months", "icon": "check", "tone": "ok", "at": A("c09", "appeals")}])
cue(type="point", t0=S("c10"), t1=E("c10") + 0.05, text="Like · Share · Subscribe · lawworld.ai", icon="check", accent=True, at=A("c10", "like"))
