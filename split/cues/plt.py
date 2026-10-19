# Rejection and Return of Plaint (CPC O.VII R.10, 10A, 11): panel cues, run by split/build_course_plan.py (helpers: at S E cue fx
# have r3 PEND). Storyboard: ~/Downloads/Rejection_and_Return_of_Plaint_Storyboard.pdf. Fact-check 19-10-2026: paragraph pins only
# where they are SCC numbers (Arivandandam para 5); Dahiben: sale deed 02.07.2009, suit 15.12.2014, rejection upheld under R.11(a)
# and (d); after a return the proceedings must begin afresh (EXL, three judges); ss.24(2)/25(3): the transferee court may retry or
# continue; LAWWORLD IDs from the storyboard (LawWorld's own database).
# v2 19-10-2026: cues rebuilt for the fast energetic script (37 clips); citations, dates and IDs as in v1; O.XLIII R.1(a) card reads
# the rule's own exception ("except where the procedure in R.10A has been followed").
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

STING = {"kicker": "CIVIL PROCEDURE · CPC EXPLAINED", "title": "Rejection vs Return of Plaint", "sub": "Order VII Rules 10 and 11, through four judgments"}
ENDCARD = {"title": "Rejection vs Return of Plaint", "line": "Return = wrong court · Rejection = statutory ground", "sub": "LawWorld: legal research for advocates"}

# ── 1 · rejected or returned? ────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=A("c01", "is") - 0.05, at=A("c01", "judge"), text="“This plaint cannot proceed.”", hl="cannot proceed.”")
cue(type="splitcard", t0=A("c01", "is"), t1=E("c01") + 0.05,
    left={"title": "REJECTED", "text": "Order VII Rule 11", "icon": "x", "at": A("c01", "rejected")},
    right={"title": "RETURNED", "text": "Order VII Rule 10", "icon": "arrow-right", "at": A("c01", "returned")})
cue(type="list", t0=S("c02"), t1=E("c02") + 0.05, head="The answer", head_at=S("c02") + 0.1,
    items=[{"n": "→", "text": "Order VII, CPC", "at": A("c02", "order")},
           {"n": 1, "text": "Arivandandam (1977)", "at": A("c02", "four")}, {"n": 2, "text": "Dahiben (2020)", "at": A("c02", "four") + 0.3},
           {"n": 3, "text": "ONGC (2013)", "at": A("c02", "four") + 0.6}, {"n": 4, "text": "EXL Careers (2020)", "at": A("c02", "four") + 0.9}])

# ── 2 · two rules, two questions ─────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="compare", t0=S("c03"), t1=E("c04") + 0.05, head="Two rules, two questions", head_at=S("c03") + 0.05,
    cols=[{"title": "Rule 10 · Return", "icon": "arrow-right", "at": A("c03", "rule", 2)}, {"title": "Rule 11 · Rejection", "icon": "x", "at": A("c04", "rule")}],
    rows=[{"cells": ["Is this the proper court?", "Does a statutory ground stop it?"], "cells_at": [A("c03", "proper"), A("c04", "statutory")]},
          {"cells": ["Commonly: no territorial or pecuniary jurisdiction", "A weak case alone: not enough"], "cells_at": [A("c03", "territorial"), A("c04", "weak")]}])

# ── 3 · six grounds for rejection ────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c05"), t1=E("c07") + 0.05, at=A("c05", "rule"), act="CPC", num="O. VII R. 11", title="Six grounds for rejection",
    points=[{"text": "(a) No cause of action", "at": A("c05", "first")},
            {"text": "(b) Undervalued, not corrected in time", "at": A("c05", "second")},
            {"text": "(c) Under-stamped, not corrected in time", "at": A("c06", "third")},
            {"text": "(d) Barred by law, from the plaint's own statement", "at": A("c06", "fourth")},
            {"text": "(e) Not filed in duplicate", "at": A("c07", "fifth")},
            {"text": "(f) Rule 9 not complied with", "at": A("c07", "sixth")}],
    note={"text": "(b) and (c): time to correct comes first", "icon": "calendar", "at": A("c07", "valuation")})

# ── 4 · a meaningful reading ─────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=A("c08", "arivandandam"), t1=E("c11") + 0.05, at=A("c08", "arivandandam"), tag="SUPREME COURT OF INDIA · 14.10.1977",
    cases=[{"name": "T. Arivandandam v. T.V. Satyapal", "cite": "(1977) 4 SCC 467, para 5 · LAWWORLD 1977 SC 1018"}])
cue(type="question", t0=S("c08"), t1=A("c08", "said") - 0.02, at=A("c08", "closely"), text="How closely must a court read a plaint?", hl="read a plaint?")
cue(type="point", t0=A("c08", "said"), t1=E("c08") + 0.05, text="A meaningful reading of the plaint", icon="search", accent=True, at=A("c08", "said") + 0.05)
cue(type="notequal", t0=S("c09"), t1=E("c09") + 0.05, left="Clever drafting", right="a cause of action", at=A("c09", "manufacture"),
    left_at=A("c09", "clever"), sub="Look past the drafting, to the substance", sub_at=A("c09", "look"))
cue(type="verdicts", t0=S("c10"), t1=A("c10", "drafting") - 0.02,
    rows=[{"text": "Impressive allegations", "ok": False, "at": A("c10", "full"), "strike_at": A("c10", "missing")},
          {"text": "Material facts: a right to relief", "ok": True, "at": A("c10", "material")}])
cue(type="point", t0=A("c10", "drafting"), t1=E("c10") + 0.05, text="Drafting? Plead the material facts", icon="file-pen-line", accent=True, at=A("c10", "drafting") + 0.05)
cue(type="verdicts", t0=S("c11"), t1=E("c11") + 0.05,
    rows=[{"text": "A ground under Rule 11", "ok": True, "at": A("c11", "court")},
          {"text": "The case looks difficult", "ok": False, "at": A("c11", "merely"), "strike_at": A("c11", "difficult") + 0.15},
          {"text": "Seeking rejection? Name the ground", "ok": True, "at": A("c11", "seeking")}])

# ── 5 · the plaint and its documents ─────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=A("c12", "dahiben"), t1=E("c16") + 0.05, at=A("c12", "dahiben"), tag="SUPREME COURT OF INDIA · 09.07.2020",
    cases=[{"name": "Dahiben v. Arvindbhai Kalyanji Bhanusali", "cite": "(2020) 7 SCC 366 · LAWWORLD 2020 SC 073"}])
cue(type="compare", t0=S("c12"), t1=E("c13") + 0.05, head="What may the court read?", head_at=S("c12") + 0.05,
    cols=[{"title": "Inside", "icon": "file-check", "at": A("c12", "answer")}, {"title": "Outside", "icon": "x", "at": A("c13", "acting")}],
    rows=[{"cells": ["The plaint, as a whole", "The defendant's version"], "cells_at": [A("c12", "whole"), A("c13", "competing")]},
          {"cells": ["The documents it relies on", "Not decisive under Rule 11"], "cells_at": [A("c12", "documents"), A("c13", "decide")]}])
cue(type="timeline", t0=S("c14"), t1=E("c14") + 0.05,
    nodes=[{"label": "SALE DEED", "value": "2 Jul 2009", "at": A("c14", "sale")},
           {"label": "SUIT FILED", "value": "15 Dec 2014", "sub": "challenging the deed", "at": A("c14", "challenged")},
           {"label": "PLAINT", "value": "Rejected", "tone": "red", "sub": "time-barred, no cause of action", "at": A("c14", "upheld")}])
cue(type="list", t0=S("c15"), t1=E("c15") + 0.05, head="Practice point", head_at=A("c15", "practice"),
    items=[{"n": 1, "text": "Check the pleaded dates", "at": A("c15", "dates")}, {"n": 2, "text": "Check the documents", "at": A("c15", "documents")},
           {"n": "→", "text": "Limitation: only if apparent from the plaint", "at": A("c15", "limitation")}])
cue(type="strike", t0=S("c16"), t1=E("c16") + 0.05, text="Decide disputed facts against the plaintiff", icon="scale", at=S("c16") + 0.05, strike_at=A("c16", "resolved"))

# ── 6 · how return works ─────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c17"), t1=E("c18") + 0.05, head="The flip side: return", head_at=A("c17", "flip"),
    steps=[{"label": "Filed in the wrong court", "sub": "a properly pleaded claim", "icon": "landmark", "tone": "stop", "at": A("c17", "properly")},
           {"label": "Plaint returned", "sub": "Order VII Rule 10", "icon": "arrow-right", "at": A("c18", "returned")},
           {"label": "The proper court", "sub": "where it should have been instituted", "icon": "landmark", "tone": "ok", "at": A("c18", "instituted")}],
    note={"text": "Return is about the forum, not the merits", "icon": "info", "at": A("c18", "return", 2)})
cue(type="checklist", t0=S("c19"), t1=E("c19") + 0.05, head="The judge's endorsement", head_at=S("c19") + 0.05,
    items=[{"n": 1, "text": "Date of presentation", "at": A("c19", "presentation")}, {"n": 2, "text": "Date of return", "at": A("c19", "return")},
           {"n": 3, "text": "Presenter's name", "at": A("c19", "presenter's")}, {"n": 4, "text": "Brief reasons", "at": A("c19", "brief")}])
cue(type="point", t0=S("c20"), t1=E("c20") + 0.05, text="Rule 10A: an appearance date in the proper court", icon="calendar", at=S("c20") + 0.1)
cue(type="cite", t0=A("c20", "conditions"), t1=E("c20") + 0.05, at=A("c20", "conditions"), tag="CPC · ORDER VII RULE 10A", text="Where its conditions apply", icon="book-open")

# ── 7 · in the proper court ──────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=A("c21", "o"), t1=E("c24") + 0.05, at=A("c21", "o"), tag="SUPREME COURT OF INDIA · 07.10.2013",
    cases=[{"name": "ONGC Ltd. v. Modern Construction & Co.", "cite": "(2014) 1 SCC 648 · LAWWORLD 2013 SC 1039"}])
cue(type="question", t0=S("c21"), t1=A("c21", "treated") - 0.05, at=A("c21", "happens"), text="What happens in the proper court?", hl="the proper court?")
cue(type="verdicts", t0=A("c21", "treated") - 0.05, t1=A("c22", "so") - 0.02,
    rows=[{"text": "A fresh institution", "ok": True, "at": A("c21", "treated")},
          {"text": "The trial proceeds afresh", "ok": True, "at": A("c22", "trial")},
          {"text": "The earlier suit continues", "ok": False, "at": A("c22", "it"), "strike_at": A("c22", "continue") + 0.1}])
cue(type="section", t0=A("c22", "so"), t1=E("c23") + 0.05, at=A("c22", "limitation"), act="LIMITATION ACT", num="14", title="Time spent in a court without jurisdiction",
    points=[{"text": "May be excluded, if its conditions are met", "at": A("c23", "exclude")},
            {"text": "That protection must be established", "at": A("c23", "protection")}])
cue(type="verdicts", t0=S("c24"), t1=E("c24") + 0.05,
    rows=[{"text": "Return keeps the original filing date", "ok": False, "at": A("c24", "return"), "strike_at": A("c24", "original")},
          {"text": "Never assume it protects your client", "ok": True, "at": A("c24", "never")}])

# ── 8 · return ≠ transfer ────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=A("c25", "three"), t1=E("c29") + 0.05, at=A("c25", "three"), tag="SUPREME COURT OF INDIA · THREE JUDGES · 05.08.2020",
    cases=[{"name": "EXL Careers v. Frankfinn Aviation Services", "cite": "(2020) 12 SCC 667 · LAWWORLD 2020 SC 082"}])
cue(type="question", t0=S("c25"), t1=E("c25") + 0.05, at=A("c25", "return"), text="Is a return just a transfer?", hl="just a transfer?")
cue(type="stamp", t0=A("c25", "no") - 0.05, t1=E("c25") + 0.05, at=A("c25", "no"), line1="NO", line2="NOT A TRANSFER")
cue(type="compare", t0=S("c26"), t1=E("c27") + 0.05, head="Return ≠ transfer", head_at=S("c26") + 0.05,
    cols=[{"title": "Return · R. 10, 10A", "icon": "arrow-right", "at": A("c26", "return")}, {"title": "Transfer · ss. 24, 25", "icon": "landmark", "at": A("c27", "transfer")}],
    rows=[{"cells": ["Proceedings begin afresh", "The transferee court may retry or continue"], "cells_at": [A("c26", "afresh"), A("c27", "keeps")]}],
    verdict={"text": "Rule 10A simplifies appearance and service", "icon": "info", "at": A("c27", "simplifies")})
cue(type="section", t0=S("c28"), t1=E("c29") + 0.05, at=A("c28", "qualification"), act="CONSTITUTION", num="Art. 136 · 142", title="Case-specific relief in EXL",
    points=[{"text": "Exceptional facts: the High Court's order left undisturbed", "at": A("c28", "exceptional")},
            {"text": "The general rule stands", "at": A("c29", "general")},
            {"text": "Cite EXL for the rule, not its result", "at": A("c29", "cite")}])

# ── 9 · different remedies ───────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="compare", t0=S("c30"), t1=E("c31") + 0.05, head="Different remedies", head_at=S("c30") + 0.05,
    cols=[{"title": "Rejection", "icon": "x", "at": A("c30", "rejection")}, {"title": "Return", "icon": "arrow-right", "at": S("c31") + 0.05}],
    rows=[{"cells": ["Deemed a decree: Section 2(2)", "An order"], "cells_at": [A("c30", "decree"), A("c31", "returning")]},
          {"cells": ["Ordinarily, a first appeal: Section 96", "Appeal: Order XLIII Rule 1(a)"], "cells_at": [A("c30", "appeal"), A("c31", "forty")]}],
    verdict={"text": "Not where the Rule 10A procedure was followed", "icon": "info", "at": A("c31", "except")})
cue(type="section", t0=S("c32"), t1=E("c33") + 0.05, at=A("c32", "rejection"), act="CPC", num="O. VII R. 13", title="A fresh plaint",
    points=[{"text": "Rejection, by itself, is no bar to a fresh plaint", "at": A("c32", "fresh")},
            {"text": "…on the same cause of action", "at": A("c32", "same")},
            {"text": "Limitation and the defect must still be overcome", "at": A("c33", "limitation")},
            {"text": "Refiling a barred claim keeps the bar", "tone": "no", "at": A("c33", "refiling")}])

# ── 10 · apply the distinction ───────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="compare", t0=S("c34"), t1=E("c35") + 0.05, head="Test yourself", head_at=A("c34", "test"),
    cols=[{"title": "Plaint 1", "icon": "file-text", "at": A("c34", "first")}, {"title": "Plaint 2", "icon": "file-text", "at": A("c35", "second")}],
    rows=[{"cells": ["A debt, filed in the wrong territory", "No cause of action, read with its documents"], "cells_at": [A("c34", "debt"), A("c35", "discloses")]},
          {"cells": ["→ Return (Rule 10)", "→ Rejection (Rule 11)"], "cells_at": [A("c34", "think"), A("c35", "think")]}])
cue(type="checklist", t0=S("c36"), t1=E("c36") + 0.05, head="Before drafting or opposing", head_at=S("c36") + 0.05,
    items=[{"n": 1, "text": "The forum", "at": A("c36", "forum")}, {"n": 2, "text": "The material facts", "at": A("c36", "material")},
           {"n": 3, "text": "The documents relied on", "at": A("c36", "documents")}, {"n": 4, "text": "Limitation", "at": A("c36", "and")}])
cue(type="splitcard", t0=S("c37"), t1=A("c37", "get") - 0.02,
    left={"title": "RETURN", "text": "to the proper court", "icon": "arrow-right", "at": A("c37", "return")},
    right={"title": "REJECTION", "text": "on a statutory ground", "icon": "x", "at": A("c37", "rejection")})
cue(type="point", t0=A("c37", "get"), t1=E("c37") + 0.05, text="Get it right: it decides the next step", icon="target", accent=True, at=A("c37", "get") + 0.05)
