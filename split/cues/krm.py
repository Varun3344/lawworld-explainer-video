# P.K. Krishnamurthy v. C.V. James, OP(C) No. 1828 of 2026, 2026:KER:81403 (High Court of Kerala, Mohammed Nias C.P. J.; delivered
# 26.10.2026, C.R.): panel cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND). Concept format as set tej.
# Facts from the judgment (paras): award in Arbitration Claim No. 1 of 2023 for the petitioner on 26.03.2024; challenged under s.34 in
# OP(Arb) No. 4 of 2024, Additional Sub Court, Kottayam (1-2); unsigned copy received 08.04.2024, sent by speed post by the petitioner's
# counsel, Exts. P5 / P5(d) (2, 5, 14); duly signed copy obtained from the Arbitrator 23.06.2024 (2, 6, 16); petitioner: limitation from
# 08.04.2024, the respondent "was aware of its contents" (4); Ext.P6 order of 04.06.2026 in I.A. No. 3 of 2025 rejected the limitation
# plea (1, 3); question (6); s.31(1) signing essential, s.31(5) signed copy to each party, "not mere knowledge of its contents" (8);
# Tecco Trichy (2005) 4 SCC 239 (9); Ark Builders (2011) 4 SCC 616: receipt of a copy from the opposing party does not start limitation
# (10); Dakshin Haryana Bijli Vitran Nigam v. Navigant (2021) 7 SCC 657: signing mandatory, not an empty formality (11); Calcutta HC
# same view (12); a copy forwarded by the opposite party cannot substitute (13); s.33 likewise not triggered (15); limitation from
# 23.06.2024, s.34 petition within time, no interference with Ext.P6 (16); OP(C) dismissed, Additional District Court-IV, Kottayam
# (O.P.(Arb) No. 198 of 2024) to dispose of it within two months (final para). The bench card uses the official portrait.
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen, as tej)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
STING = {"kicker": "KERALA HIGH COURT · JUDGMENT EXPLAINED", "title": "Section 34(3) and the unsigned copy", "sub": "P.K. Krishnamurthy v. C.V. James · 2026:KER:81403"}
ENDCARD = {"title": "Section 34(3) and the unsigned copy", "line": "Limitation runs from receipt of the signed award", "sub": "LawWorld: legal research for advocates"}

# ── 1 · unsigned copy? ───────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "other"), text="Unsigned award copy from the other side: does the challenge clock start?", hl="challenge clock start?")
cue(type="bench", t0=S("c02"), t1=E("c02") + 0.05, tag="High Court of Kerala · 26 October 2026",
    judges=[{"name": "Justice Mohammed Nias C.P.", "photo": "../brand/judges/mohammed_nias_cp.jpg", "at": A("c02", "honourable")}])

# ── 2 · the case ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=A("c03", "arbitrator"), t1=E("c04") + 0.05, at=A("c03", "arbitrator"), tag="HIGH COURT OF KERALA · 26.10.2026",
    cases=[{"name": "P.K. Krishnamurthy v. C.V. James", "cite": "2026:KER:81403 · OP(C) No. 1828 of 2026"}])
cue(type="flow", t0=S("c03"), t1=E("c03") + 0.05, head="The dispute", head_at=S("c03") + 0.05,
    steps=[{"label": "Award for P.K. Krishnamurthy", "sub": "26 Mar 2024 · Arbitration Claim No. 1 of 2023", "icon": "file-text", "at": A("c03", "award")},
           {"label": "C.V. James challenges it", "sub": "OP(Arb) No. 4 of 2024 · Additional Sub Court, Kottayam", "icon": "landmark", "at": A("c03", "challenged")},
           {"label": "Section 34", "sub": "Arbitration and Conciliation Act, 1996", "icon": "scale", "at": A("c03", "section")}])
cue(type="timeline", t0=S("c04"), t1=E("c04") + 0.05,
    nodes=[{"label": "AWARD", "value": "26 Mar 2024", "sub": "made by the arbitrator", "at": A("c04", "on")},
           {"label": "UNSIGNED COPY", "value": "8 Apr 2024", "sub": "speed post, award holder's counsel", "at": A("c04", "unsigned")},
           {"label": "SIGNED COPY", "value": "23 Jun 2024", "sub": "obtained from the arbitrator", "at": A("c04", "signed")}])

# ── 3 · the question ─────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c05"), t1=E("c05") + 0.05, head="The limitation plea", head_at=S("c05") + 0.05,
    steps=[{"label": "Award holder: time-barred", "sub": "time ran from 8 Apr 2024; he knew the contents", "icon": "x", "tone": "stop", "at": A("c05", "late")},
           {"label": "Kottayam court: plea rejected", "sub": "Ext. P6 order, 4 Jun 2026 · I.A. No. 3 of 2025", "icon": "landmark", "at": A("c05", "disagreed")},
           {"label": "Award holder to the High Court", "sub": "OP(C) No. 1828 of 2026", "icon": "arrow-right", "at": A("c05", "high")}])
# the right column lands on the clip's last words ("signed award?"): the card holds into c07 until "Section" (no cut-off build)
cue(type="compare", t0=S("c06"), t1=A("c07", "section") - 0.05, head="Section 34(3): three months from which date?", head_at=A("c06", "section"),
    cols=[{"title": "Unsigned copy", "icon": "file-text", "at": A("c06", "unsigned")}, {"title": "Signed award", "icon": "file-check", "at": A("c06", "signed")}],
    rows=[{"cells": ["8 Apr 2024", "23 Jun 2024"], "cells_at": [A("c06", "copy"), A("c06", "award")]},
          {"cells": ["posted by the award holder's counsel", "obtained from the arbitrator"], "cells_at": [A("c06", "only"), A("c06", "award", d=0.25)]}])

# ── 4 · what starts the clock ────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=A("c07", "section"), t1=E("c07") + 0.05, at=A("c07", "section"), act="A&C ACT, 1996", num="31", title="Form and contents of arbitral award",
    points=[{"text": "31(1): the award must be signed", "at": A("c07", "signed")},
            {"text": "31(5): a signed copy delivered to each party", "at": A("c07", "delivered")}],
    note={"text": "Mere knowledge of the contents does not start limitation", "icon": "x", "at": A("c07", "knowledge")})
cue(type="cite", t0=A("c07", "award"), t1=E("c07") + 0.05, at=A("c07", "award"), tag="SUPREME COURT · SIGNING IS MANDATORY",
    cases=[{"name": "Dakshin Haryana Bijli Vitran Nigam v. Navigant", "cite": "(2021) 7 SCC 657"}])
cue(type="point", t0=S("c08"), t1=A("c08", "copy") - 0.05, text="Settled by the Supreme Court", icon="scale", accent=False, at=A("c08", "supreme"))
cue(type="cite", t0=A("c08", "tecco"), t1=E("c08") + 0.05, at=A("c08", "tecco"), tag="SUPREME COURT · FOLLOWED",
    cases=[{"name": "Union of India v. Tecco Trichy Engineers", "cite": "(2005) 4 SCC 239"},
           {"name": "State of Maharashtra v. Ark Builders", "cite": "(2011) 4 SCC 616"}])
cue(type="notequal", t0=A("c08", "copy"), t1=E("c08") + 0.05, left="Opposite party's copy", right="Section 31(5) delivery",
    at=A("c08", "copy"), left_at=A("c08", "copy"), sub="Starts neither the Section 34(3) nor the Section 33 period", sub_at=A("c08", "section"))   # no ", not" in sub: the renderer strikes what follows it

# ── 5 · the verdict ──────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="verdicts", t0=S("c09"), t1=A("c09", "advocates") - 0.05,
    rows=[{"text": "8 Apr 2024 · unsigned copy", "ok": False, "at": A("c09", "time"), "strike_at": A("c09", "june")},
          {"text": "23 Jun 2024 · signed copy: challenge in time", "ok": True, "at": A("c09", "challenge")},
          {"text": "OP(C) dismissed · trial court: 2 months", "ok": True, "at": A("c09", "petition")}])
cue(type="point", t0=A("c09", "advocates"), t1=E("c09") + 0.05, text="Count from receipt of the signed award", icon="calendar", accent=True, at=A("c09", "count"))
cue(type="point", t0=S("c10"), t1=E("c10") + 0.05, text="Like · Share · Subscribe · lawworld.ai", icon="check", accent=True, at=A("c10", "like"))
