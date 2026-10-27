# Mohammed Rafi v. State of Kerala & connected cases, WP(C) No. 819 of 2017 + 11 (2026:KER:81906, Bechu Kurian Thomas J., 26.10.2026,
# "C.R."): panel cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND). Concept-format judgment reel (27-10-2026).
# Facts from the judgment (paras): S.R.O. 315/2016 (G.O.(P) 5/2016/Law) of 07.04.2016 under s.76(1) of the Kerala Court Fees and Suits
# Valuation Act, 1959: additional court fee on suits, petitions, appeals and revisions raised from 0.5% to 1% of the amount in dispute
# (Rs 50 -> Rs 100 otherwise), credited to the Kerala Legal Benefit Fund (s.76(2)), deemed in force from 01.04.2016 (1, 7, 9); 0.5%
# since the 2002 notification (8, 9); petitioners all KVAT Act assessees, told to pay the enhanced rate on appeals / revisions filed after
# the notification (2); plea: impairs the vested right of appeal, not for assessment years before 2016-17 (3, 5); State: payable on
# appeals filed after 07.04.2016 (4, 6); Hoosein Kasam Dada AIR 1953 SC 221 (14, 18), approved by the Constitution Bench in Vitthalbhai
# Naranbhai Patel AIR 1967 SC 344 (14); Hardeodas Jagannath AIR 1970 SC 724 did not note that approval (13, 15); IVECO Magirus (2024)
# 2 SCC 86: the earlier decision binds (16, 17); enhanced fee only where the lis commenced after 01.04.2016, no retrospective stipulation
# (17, 19); a tax lis commences when the authority, not satisfied with the return, calls for materials or evidence (19); "the critical
# and relevant date is the date of initiation of proceedings and not the decision itself" (18); Sobha Ltd. (WP 1710/2017): notice
# 12.11.2015, assessment order 20.05.2016 -> not liable; Manappuram Jewellers (WP 12501/2023): inspection 23.03.2015, books called for
# 20.08.2018 -> liable; WP 28493, 32515, 33920/2017, 9667/2018, 27634/2020: no dates pleaded -> for the appellate forum; disposed of (20).
# Not on any card: WP 16785/2017 (para 20 says lis before the notification yet "is liable") - no per-rate counts anywhere.
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow (24 + 58 px) ends inside the panel: the 9:16 band edge cut it into a line at 40
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen (no blobs / star behind the cards)
STING = {"kicker": "KERALA HIGH COURT · JUDGMENT EXPLAINED", "title": "Court fee and the date the lis began", "sub": "WP(C) No. 819 of 2017 & connected cases · 2026:KER:81906"}
ENDCARD = {"title": "Court fee and the date the lis began", "line": "Lis begun before 1 April 2016 · no enhanced court fee", "sub": "LawWorld: legal research for advocates"}

# ── 1 · which court fee? ─────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "kerala"), text="Additional court fee doubled in 2016: does it hit a tax dispute that began earlier?", hl="began earlier?")
cue(type="bench", t0=S("c02"), t1=E("c02") + 0.05, tag="Kerala High Court · 26 October 2026",
    judges=[{"name": "Justice Bechu Kurian Thomas", "photo": "../brand/judges/bechu_kurian_thomas.jpg", "at": A("c02", "honourable")}])

# ── 2 · the case ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=A("c03", "court"), t1=E("c04") + 0.05, at=A("c03", "court"), tag="HIGH COURT OF KERALA · 26.10.2026",
    cases=[{"name": "Mohammed Rafi v. State of Kerala & connected cases", "cite": "2026:KER:81906 · WP(C) No. 819 of 2017 + 11 writ petitions"}])
cue(type="section", t0=S("c03"), t1=A("c03", "notification") - 0.05, at=A("c03", "court"), act="KERALA COURT FEES ACT, 1959", num="76", title="Additional court fee",
    points=[{"text": "Credited to the Kerala Legal Benefit Fund", "at": A("c03", "legal")}])
cue(type="timeline", t0=A("c03", "notification") - 0.05, t1=E("c03") + 0.05,
    nodes=[{"label": "SINCE 2002", "value": "0.5%", "sub": "of the amount in dispute", "at": A("c03", "notification")},
           {"label": "NOTIFIED 7 APR 2016", "value": "1%", "sub": "S.R.O. 315/2016", "tone": "red", "at": A("c03", "percent")},
           {"label": "IN FORCE FROM", "value": "1 Apr 2016", "sub": "deemed, by the notification", "at": A("c03", "force")}])
cue(type="flow", t0=S("c04"), t1=E("c04") + 0.05, head="The demand", head_at=S("c04") + 0.05,
    steps=[{"label": "12 KVAT assessees", "sub": "Sobha Ltd., Manappuram Jewellers and others", "icon": "users", "at": A("c04", "twelve")},
           {"label": "Appeals and revisions filed", "sub": "after the 2016 notification", "icon": "file-text", "at": A("c04", "filed")},
           {"label": "Told to pay 1%", "sub": "the enhanced additional court fee", "icon": "x", "tone": "stop", "at": A("c04", "told")}])

# ── 3 · the clash ────────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="compare", t0=S("c05"), t1=E("c05") + 0.05, head="Which appeals pay 1%?", head_at=S("c05") + 0.05,
    cols=[{"title": "Assessees", "icon": "users", "at": A("c05", "plea")}, {"title": "The State", "icon": "landmark", "at": A("c05", "state")}],
    rows=[{"cells": ["Vested right of appeal impaired", "Every appeal filed after 7.4.2016"], "cells_at": [A("c05", "vested"), A("c05", "every")]},
          {"cells": ["Not for years before 2016-17", "pays the 1% rate"], "cells_at": [A("c05", "older"), A("c05", "pays")]}])

# ── 4 · when the right vests ─────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="list", t0=S("c06"), t1=A("c06", "hoosein") - 0.05, head="Vested when the lis begins", head_at=A("c06", "held"),
    items=[{"n": 1, "text": "The right of appeal", "at": A("c06", "right")},
           {"n": 2, "text": "The court fee payable on it, as on that date", "at": A("c06", "court", 2)}])
cue(type="timeline", t0=A("c06", "hoosein") - 0.05, t1=E("c06") + 0.05,
    nodes=[{"label": "HOOSEIN KASAM DADA", "value": "1953", "sub": "the lis begins: rights crystallise", "at": A("c06", "hoosein")},
           {"label": "VITTHALBHAI PATEL", "value": "1967", "sub": "a Constitution Bench approves it", "at": A("c06", "constitution")},
           {"label": "HARDEODAS JAGANNATH", "value": "1970", "sub": "did not notice it: 1967 still binds", "tone": "red", "at": A("c06", "still")}])
cue(type="cite", t0=A("c06", "hoosein"), t1=E("c06") + 0.05, at=A("c06", "hoosein"), tag="SUPREME COURT · THE BINDING LINE",
    cases=[{"name": "Hoosein Kasam Dada (India) Ltd. v. State of M.P.", "cite": "AIR 1953 SC 221"},
           {"name": "Vitthalbhai Naranbhai Patel v. CST, M.P.", "cite": "AIR 1967 SC 344 · Constitution Bench"}])
cue(type="point", t0=S("c07"), t1=A("c07", "percent") - 0.05, text="No retrospective stipulation, express or by necessary intendment", icon="info", accent=False, at=A("c07", "nothing"))
cue(type="compare", t0=A("c07", "percent") - 0.05, t1=E("c07") + 0.05, head="When did the lis begin?", head_at=A("c07", "percent"),
    cols=[{"title": "Before 1 Apr 2016", "icon": "check", "at": A("c07", "only")}, {"title": "After 1 Apr 2016", "icon": "x", "at": A("c07", "after")}],
    rows=[{"cells": ["Old rate · 0.5%", "New rate · 1%"], "cells_at": [A("c07", "began"), A("c07", "april")]}])

# ── 5 · when a tax lis begins ────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c08"), t1=A("c08", "notice") - 0.1, head="When a tax lis begins", head_at=S("c08") + 0.05,
    steps=[{"label": "Officer not satisfied", "sub": "with the return filed", "icon": "search", "at": A("c08", "officer")},
           {"label": "Calls for materials or evidence", "sub": "a notice on the return will do", "icon": "file-text", "at": A("c08", "calls")},
           {"label": "The lis begins", "sub": "“initiation … not the decision itself”", "icon": "check", "tone": "ok", "at": A("c08", "evidence")}])
cue(type="timeline", t0=A("c08", "notice") - 0.15, t1=E("c08") + 0.05,
    nodes=[{"label": "SOBHA LTD. · NOTICE", "value": "12 Nov 2015", "sub": "pre-assessment notice", "at": A("c08", "notice")},
           {"label": "ASSESSMENT ORDER", "value": "20 May 2016", "sub": "after the new rate began", "at": A("c08", "fifteen")},
           {"label": "ITS APPEAL", "value": "0.5%", "sub": "the old rate: no enhanced fee", "at": A("c08", "need")}])

# ── 6 · the result ───────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="timeline", t0=S("c09"), t1=A("c09", "five") - 0.05,
    nodes=[{"label": "SHOP INSPECTION", "value": "23 Mar 2015", "sub": "Manappuram Jewellers", "at": A("c09", "manappuram")},
           {"label": "BOOKS CALLED FOR", "value": "20 Aug 2018", "sub": "the lis begins", "at": A("c09", "called")},
           {"label": "ITS APPEAL", "value": "1%", "sub": "the new rate", "tone": "red", "at": A("c09", "pays")}])
cue(type="point", t0=A("c09", "five") - 0.05, t1=E("c09") + 0.05, text="5 petitions, no dates pleaded: the appellate forum decides", icon="search", accent=True, at=A("c09", "five"))
cue(type="point", t0=S("c10"), t1=E("c10") + 0.05, text="Like · Share · Subscribe · lawworld.ai", icon="check", accent=True, at=A("c10", "like"))
