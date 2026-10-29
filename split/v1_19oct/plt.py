# Rejection and Return of Plaint (CPC O.VII R.10, 10A, 11): panel cues, run by split/build_course_plan.py (helpers: at S E cue fx
# have r3 PEND). Storyboard: ~/Downloads/Rejection_and_Return_of_Plaint_Storyboard.pdf. Fact-check 19-10-2026: paragraph pins only
# where they are SCC numbers (Arivandandam para 5); Dahiben: sale deed 02.07.2009, suit 15.12.2014, rejection upheld under R.11(a)
# and (d); after a return the proceedings must begin afresh (EXL, three judges); ss.24(2)/25(3): the transferee court may retry or
# continue; LAWWORLD IDs from the storyboard (LawWorld's own database).
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

STING = {"kicker": "CIVIL PROCEDURE · CPC EXPLAINED", "title": "Rejection vs Return of Plaint", "sub": "Order VII Rules 10 and 11, through four judgments"}
ENDCARD = {"title": "Rejection vs Return of Plaint", "line": "Return = wrong court · Rejection = statutory ground", "sub": "LawWorld: legal research for advocates"}

# ── 1 · rejected or returned? ────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=A("c01", "but") - 0.05, at=A("c01", "judge"), text="“This plaint cannot proceed.”", hl="cannot proceed.”")
cue(type="splitcard", t0=A("c01", "but"), t1=E("c02") + 0.05,
    left={"title": "REJECTED", "text": "Order VII Rule 11", "icon": "x", "at": A("c01", "rejected")},
    right={"title": "RETURNED", "text": "Order VII Rule 10", "icon": "arrow-right", "at": A("c01", "returned")})
cue(type="list", t0=S("c03"), t1=E("c03") + 0.05, head="Four leading judgments", head_at=A("c03", "understand"),
    items=[{"n": 1, "text": "Arivandandam (1977)", "at": A("c03", "four")}, {"n": 2, "text": "Dahiben (2020)", "at": A("c03", "four") + 0.35},
           {"n": 3, "text": "ONGC (2013)", "at": A("c03", "four") + 0.7}, {"n": 4, "text": "EXL Careers (2020)", "at": A("c03", "four") + 1.05}])

# ── 2 · the two provisions ───────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="compare", t0=S("c04"), t1=E("c07") + 0.05, head="Two different questions", head_at=S("c04") + 0.05,
    cols=[{"title": "Rule 10 · Return", "icon": "arrow-right", "at": A("c04", "order")}, {"title": "Rule 11 · Rejection", "icon": "x", "at": A("c06", "rule")}],
    rows=[{"cells": ["Presented to the proper court", "Rejected on specified grounds"], "cells_at": [A("c04", "proper"), A("c06", "rejection")]},
          {"cells": ["Territorial or pecuniary jurisdiction missing", "A statutory ground stops it"], "cells_at": [A("c05", "territorial"), A("c07", "statutory")]}],
    verdict={"text": "A weak case alone is not enough", "icon": "triangle-alert", "at": A("c07", "weak")})

# ── 3 · six grounds for rejection ────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c08"), t1=E("c12") + 0.05, at=A("c08", "rule"), act="CPC", num="O. VII R. 11", title="Six grounds for rejection",
    points=[{"text": "(a) No cause of action", "at": A("c08", "first")},
            {"text": "(b) Undervalued, not corrected in time", "at": A("c09", "second")},
            {"text": "(c) Under-stamped, not corrected in time", "at": A("c10", "third")},
            {"text": "(d) Barred by law, from the plaint's own statement", "at": A("c11", "fourth")},
            {"text": "(e) Not filed in duplicate", "at": A("c11", "fifth")},
            {"text": "(f) Rule 9 not complied with", "at": A("c12", "sixth")}],
    note={"text": "(b) and (c): the chance to correct comes first", "icon": "calendar", "at": A("c12", "valuation")})

# ── 4 · a meaningful reading ─────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=A("c13", "first"), t1=E("c16") + 0.05, at=A("c13", "first"), tag="SUPREME COURT OF INDIA · 14.10.1977",
    cases=[{"name": "T. Arivandandam v. T.V. Satyapal", "cite": "(1977) 4 SCC 467, para 5 · LAWWORLD 1977 SC 1018"}])
cue(type="point", t0=S("c13"), t1=E("c13") + 0.05, text="A meaningful reading of the plaint", icon="search", accent=True, at=A("c13", "meaningful"))
cue(type="notequal", t0=S("c14"), t1=E("c14") + 0.05, left="Clever drafting", right="a cause of action", at=A("c14", "manufacture"),
    left_at=A("c14", "clever"), sub="The court examines the substance", sub_at=A("c14", "substance"))
cue(type="verdicts", t0=S("c15"), t1=E("c15") + 0.05,
    rows=[{"text": "Impressive allegations", "ok": False, "at": A("c15", "impressive"), "strike_at": A("c15", "missing")},
          {"text": "Material facts: a right to relief", "ok": True, "at": A("c15", "material")}])
cue(type="verdicts", t0=S("c16"), t1=E("c16") + 0.05,
    rows=[{"text": "A ground under Rule 11", "ok": True, "at": A("c16", "ground")},
          {"text": "The case looks difficult", "ok": False, "at": A("c16", "merely"), "strike_at": A("c16", "difficult") + 0.2}])

# ── 5 · the plaint and its documents ─────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=A("c17", "dahiben"), t1=E("c22") + 0.05, at=A("c17", "dahiben"), tag="SUPREME COURT OF INDIA · 09.07.2020",
    cases=[{"name": "Dahiben v. Arvindbhai Kalyanji Bhanusali", "cite": "(2020) 7 SCC 366 · LAWWORLD 2020 SC 073"}])
cue(type="compare", t0=S("c17"), t1=E("c18") + 0.05, head="What the court reads", head_at=A("c17", "read"),
    cols=[{"title": "Inside", "icon": "file-check", "at": A("c17", "read")}, {"title": "Outside", "icon": "x", "at": A("c18", "defendant's")}],
    rows=[{"cells": ["The plaint, as a whole", "The defendant's version"], "cells_at": [A("c17", "whole"), A("c18", "competing")]},
          {"cells": ["The documents it relies on", "Not decisive under Rule 11"], "cells_at": [A("c17", "documents"), A("c18", "decide")]}])
cue(type="timeline", t0=S("c19"), t1=E("c20") + 0.05,
    nodes=[{"label": "SALE DEED", "value": "2 Jul 2009", "at": A("c19", "sale")},
           {"label": "SUIT FILED", "value": "15 Dec 2014", "sub": "challenging the deed", "at": A("c19", "suit")},
           {"label": "PLAINT", "value": "Rejected", "tone": "red", "sub": "time-barred, no cause of action", "at": A("c20", "barred")}])
cue(type="point", t0=S("c21"), t1=E("c21") + 0.05, text="Limitation: only when the bar is apparent from the plaint", icon="calendar", accent=True, at=A("c21", "limitation"))
cue(type="strike", t0=S("c22"), t1=E("c22") + 0.05, text="Decide disputed facts against the plaintiff", icon="scale", at=S("c22") + 0.05, strike_at=A("c22", "stage") + 0.1)

# ── 6 · how return works ─────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c23"), t1=E("c24") + 0.05,
    steps=[{"label": "Filed in the wrong court", "icon": "landmark", "tone": "stop", "at": A("c23", "wrong")},
           {"label": "Plaint returned", "sub": "Order VII Rule 10", "icon": "arrow-right", "at": A("c24", "returned")},
           {"label": "The proper court", "icon": "landmark", "tone": "ok", "at": A("c24", "instituted")}])
cue(type="checklist", t0=S("c25"), t1=E("c25") + 0.05, head="The endorsement", head_at=S("c25") + 0.05,
    items=[{"n": 1, "text": "Date of presentation", "at": A("c25", "presentation")}, {"n": 2, "text": "Date of return", "at": A("c25", "return")},
           {"n": 3, "text": "Presenter's name", "at": A("c25", "presenter's")}, {"n": 4, "text": "Brief reasons", "at": A("c25", "brief")}])
cue(type="point", t0=S("c26"), t1=E("c26") + 0.05, text="Rule 10A: an appearance date in the proper court", icon="calendar", at=A("c26", "rule"))
cue(type="cite", t0=S("c26"), t1=E("c26") + 0.05, at=S("c26"), tag="REMEMBER", text="Return addresses the forum, not the merits", icon="info")

# ── 7 · in the proper court ──────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=A("c27", "o"), t1=E("c30") + 0.05, at=A("c27", "o"), tag="SUPREME COURT OF INDIA · 07.10.2013",
    cases=[{"name": "ONGC Ltd. v. Modern Construction & Co.", "cite": "(2014) 1 SCC 648 · LAWWORLD 2013 SC 1039"}])
cue(type="point", t0=S("c27"), t1=E("c27") + 0.05, text="A returned plaint, presented to the competent court", icon="landmark", at=A("c27", "returned"))
cue(type="verdicts", t0=S("c28"), t1=E("c28") + 0.05,
    rows=[{"text": "A fresh institution; the trial afresh", "ok": True, "at": A("c28", "fresh")},
          {"text": "The earlier suit continues", "ok": False, "at": A("c28", "continue"), "strike_at": A("c28", "suit") + 0.3}])
cue(type="section", t0=S("c29"), t1=E("c30") + 0.05, at=A("c29", "section"), act="LIMITATION ACT", num="14", title="Time spent in a court without jurisdiction",
    points=[{"text": "May be excluded, if its conditions are met", "at": A("c29", "exclude")},
            {"text": "The original filing date is not preserved", "tone": "no", "at": A("c30", "preserve")}])

# ── 8 · return ≠ transfer ────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=A("c31", "three"), t1=E("c35") + 0.05, at=A("c31", "three"), tag="SUPREME COURT OF INDIA · THREE JUDGES · 05.08.2020",
    cases=[{"name": "EXL Careers v. Frankfinn Aviation Services", "cite": "(2020) 12 SCC 667 · LAWWORLD 2020 SC 082"}])
cue(type="compare", t0=S("c31"), t1=E("c33") + 0.05, head="Return ≠ transfer", head_at=A("c31", "confirmed"),
    cols=[{"title": "Return · R. 10, 10A", "icon": "arrow-right", "at": A("c32", "return")}, {"title": "Transfer · ss. 24, 25", "icon": "landmark", "at": A("c33", "transfer")}],
    rows=[{"cells": ["Proceedings begin afresh", "The transferee court may retry or continue"], "cells_at": [A("c32", "afresh"), A("c33", "keeps")]}],
    verdict={"text": "Rule 10A simplifies appearance and service only", "icon": "info", "at": A("c33", "simplifies")})
cue(type="section", t0=S("c34"), t1=E("c35") + 0.05, at=A("c34", "qualification"), act="CONSTITUTION", num="Art. 136 · 142", title="Case-specific relief in EXL",
    points=[{"text": "Exceptional facts: the High Court's order left undisturbed", "at": A("c35", "left")},
            {"text": "The general rule stands", "at": A("c35", "general")}])

# ── 9 · different remedies ───────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="compare", t0=S("c36"), t1=E("c38") + 0.05, head="Different remedies", head_at=S("c36") + 0.05,
    cols=[{"title": "Rejection", "icon": "x", "at": A("c36", "rejection")}, {"title": "Return", "icon": "arrow-right", "at": A("c38", "returning")}],
    rows=[{"cells": ["A decree: Section 2(2)", "An order"], "cells_at": [A("c36", "decree"), A("c38", "order")]},
          {"cells": ["First appeal: Section 96", "Appeal: Order XLIII Rule 1(a)"], "cells_at": [A("c37", "appeal"), A("c38", "forty")]}],
    verdict={"text": "Subject to the Rule 10A exception", "icon": "info", "at": A("c38", "subject")})
cue(type="section", t0=S("c39"), t1=E("c40") + 0.05, at=A("c39", "rejection"), act="CPC", num="O. VII R. 13", title="A fresh plaint",
    points=[{"text": "Rejection does not bar a fresh plaint", "at": A("c39", "fresh")},
            {"text": "Limitation and the defect must still be overcome", "at": A("c40", "limitation")},
            {"text": "Refiling a barred claim keeps the bar", "tone": "no", "at": A("c40", "refiling")}])

# ── 10 · apply the distinction ───────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="compare", t0=S("c41"), t1=E("c42") + 0.05, head="Two examples", head_at=A("c41", "try"),
    cols=[{"title": "Plaint A", "icon": "file-text", "at": A("c41", "plaint")}, {"title": "Plaint B", "icon": "file-text", "at": A("c42", "another")}],
    rows=[{"cells": ["A debt, filed in the wrong territory", "No cause of action, read with its documents"], "cells_at": [A("c41", "debt"), A("c42", "discloses")]},
          {"cells": ["→ Return (Rule 10)", "→ Rejection (Rule 11)"], "cells_at": [A("c41", "think"), A("c42", "think")]}])
cue(type="list", t0=S("c43"), t1=E("c43") + 0.05, head="Before you file or oppose", head_at=S("c43") + 0.05,
    items=[{"n": 1, "text": "The forum", "at": A("c43", "forum")}, {"n": 2, "text": "The material facts", "at": A("c43", "material")},
           {"n": 3, "text": "The documents relied on", "at": A("c43", "documents")}, {"n": 4, "text": "Limitation", "at": A("c43", "limitation")}])
cue(type="splitcard", t0=S("c44"), t1=E("c45") + 0.05,
    left={"title": "RETURN", "text": "to the proper court", "icon": "arrow-right", "at": A("c44", "return")},
    right={"title": "REJECTION", "text": "on a statutory ground", "icon": "x", "at": A("c44", "rejection")})
