# Compounding and Plea Bargaining (BNSS): panel cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND).
# Storyboard: ~/Downloads/Compounding_and_Plea_Bargaining_BNSS_Storyboard.pdf. Fact-check 19-10-2026: every section, table, time
# limit and fraction matches the Gazette text; 290(1) "may file" within 30 days of framing of charge (Rohan: a warrant case);
# compounding is still placed before the court; murder (BNS 103) is in neither table.
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

STING = {"kicker": "CRIMINAL PROCEDURE · BNSS EXPLAINED", "title": "Compounding and Plea Bargaining", "sub": "Two ways a case may end without a full trial"}
ENDCARD = {"title": "Compounding and Plea Bargaining", "line": "Compounding ≠ plea bargaining", "sub": "Next lesson: Criminal Appeals and Revisions"}

# ── 1 · two ways out ─────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="compare", t0=S("c01"), t1=E("c02") + 0.05, head="Two ways a case may end", head_at=S("c01") + 0.1,
    cols=[{"title": "Ravi and Mohan", "icon": "handshake", "at": A("c01", "ravi")}, {"title": "Rohan", "icon": "user-round", "at": A("c01", "rohan")}],
    rows=[{"cells": ["Settle after a fight", "Accepts responsibility"], "cells_at": [A("c01", "settle"), A("c01", "accept")]},
          {"cells": ["A compromise", "A lawful reduction in punishment"], "cells_at": [A("c02", "lawful") - 0.2, A("c02", "lawful")]}],
    verdict={"text": "Are these the same thing?", "icon": "circle-help", "at": A("c02", "are")})
cue(type="splitcard", t0=S("c03"), t1=E("c03") + 0.05,
    left={"title": "COMPOUNDING", "text": "BNSS § 359", "icon": "handshake", "at": A("c03", "compounding")},
    right={"title": "PLEA BARGAINING", "text": "BNSS §§ 289–300", "icon": "scale", "at": A("c03", "plea")})
