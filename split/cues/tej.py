# Tejaram v. State of Rajasthan, 2026 INSC 1147 (S.V.N. Bhatti J., N.V. Anjaria J.; decided 16.10.2026, REPORTABLE): panel cues, run by
# split/build_course_plan.py (helpers: at S E cue fx have r3 PEND). First judgment reel in the concept format (owner 26-10-2026).
# Facts from the judgment (paras): FIR 174/2021 of 04.06.2021 under s.7A PC Act + s.120B IPC (5); s.19 sanction 08.12.2023 (5);
# charge under s.7 framed 12.09.2024 by the Special Judge, ACB, Pali (2, 3.2); High Court at Jodhpur dismissed the revision 26.03.2025
# (2); s.17A(1) text (5.1); "a pure criminal act unconnected to discharge of the official functions or duties" (6.1); Santosh Karnani
# (2023) SCC OnLine SC 427 paras 33-34 and Anil Daima 2026 SCC OnLine SC 807 para 7 (5.2-5.4); CPIL reference of 13.01.2026 (7);
# s.19 sanction before cognizance, at most an irregularity (8); appeal dismissed (11). The bench card uses the official portraits.
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

STING = {"kicker": "SUPREME COURT · JUDGMENT EXPLAINED", "title": "Section 17A and a bribe demand", "sub": "Tejaram v. State of Rajasthan · 2026 INSC 1147"}
ENDCARD = {"title": "Section 17A and a bribe demand", "line": "No official decision or recommendation · no Section 17A", "sub": "LawWorld: legal research for advocates"}

# ── 1 · prior approval? ──────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "accused"), text="Accused of a bribe demand: can “no approval under Section 17A” stop the case?", hl="stop the case?")
cue(type="bench", t0=S("c02"), t1=E("c02") + 0.05, tag="Supreme Court of India · 16 October 2026",
    judges=[{"name": "Justice S.V.N. Bhatti", "photo": "../brand/judges/svn_bhatti.jpg", "at": A("c02", "honourable")},
            {"name": "Justice N.V. Anjaria", "photo": "../brand/judges/nv_anjaria.jpg", "at": A("c02", "honourable", 2)}])

# ── 2 · the case ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=A("c03", "tejaram"), t1=E("c04") + 0.05, at=A("c03", "tejaram"), tag="SUPREME COURT OF INDIA · 16.10.2026",
    cases=[{"name": "Tejaram v. State of Rajasthan", "cite": "2026 INSC 1147 · Criminal Appeal @ SLP (Crl.) No. 11709 of 2025"}])
cue(type="flow", t0=S("c03"), t1=E("c03") + 0.05, head="The accusation", head_at=S("c03") + 0.05,
    steps=[{"label": "Tejaram", "sub": "police constable, Sirohi", "icon": "user", "at": A("c03", "tejaram")},
           {"label": "A fellow constable complains", "sub": "to the Anti-Corruption Bureau", "icon": "file-text", "at": A("c03", "colleague")},
           {"label": "Alleged demand: ₹1.5 lakh", "sub": "in the name of the Superintendent of Police", "icon": "x", "tone": "stop", "at": A("c03", "lakh")}])
cue(type="timeline", t0=S("c04"), t1=E("c04") + 0.05,
    nodes=[{"label": "FIR", "value": "4 Jun 2021", "sub": "s.7A PC Act, s.120B IPC", "at": A("c04", "came")},
           {"label": "SANCTION", "value": "8 Dec 2023", "sub": "Section 19", "at": A("c04", "sanction")},
           {"label": "CHARGE", "value": "12 Sep 2024", "sub": "Section 7, PC Act", "at": A("c04", "charge")},
           {"label": "HIGH COURT", "value": "26 Mar 2025", "sub": "revision dismissed", "tone": "red", "at": A("c04", "upheld")}])

# ── 3 · his argument ─────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c05"), t1=E("c05") + 0.05, at=A("c05", "section"), act="PC ACT", num="17A", title="Prior approval to investigate",
    points=[{"text": "Police enquiry or investigation", "at": A("c05", "investigate")},
            {"text": "of a public servant's official acts", "at": A("c05", "official")}],
    note={"text": "His plea: no approval was taken", "icon": "x", "at": A("c05", "none")})

# ── 4 · what section 17A covers ──────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="list", t0=S("c06"), t1=E("c06") + 0.05, head="Approval needed only if the offence relates to", head_at=A("c06", "approval"),
    items=[{"n": 1, "text": "a recommendation made", "at": A("c06", "recommendation")},
           {"n": 2, "text": "or a decision taken", "at": A("c06", "decision")},
           {"n": "→", "text": "in discharge of official duties", "at": A("c06", "official")}])
cue(type="notequal", t0=S("c07"), t1=A("c07", "earlier") - 0.05, left="A bribe demand", right="an official act", at=A("c07", "neither"),
    left_at=A("c07", "bribe"), sub="“a pure criminal act”", sub_at=A("c07", "pure"))
cue(type="cite", t0=A("c07", "earlier"), t1=E("c07") + 0.05, at=A("c07", "earlier"), tag="SUPREME COURT · THE SAME VIEW",
    cases=[{"name": "CBI v. Santosh Karnani", "cite": "(2023) SCC OnLine SC 427, paras 33-34"},
           {"name": "Anil Daima v. State of Rajasthan", "cite": "2026 SCC OnLine SC 807, para 7"}])

# ── 5 · the verdict ──────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="verdicts", t0=S("c08"), t1=E("c08") + 0.05,
    rows=[{"text": "Wait for the larger bench on 17A?", "ok": False, "at": A("c08", "pending"), "strike_at": A("c08", "bearing")},
          {"text": "Section 19 sanction: before cognizance", "ok": True, "at": A("c08", "nineteen")},
          {"text": "No fatal defect", "ok": True, "at": A("c08", "fatal")}])
cue(type="point", t0=S("c09"), t1=A("c09", "section") - 0.05, text="Appeal dismissed · the trial goes on", icon="scale", accent=True, at=A("c09", "dismissed"))
cue(type="compare", t0=A("c09", "section"), t1=E("c09") + 0.05, head="Section 17A, in one line", head_at=A("c09", "section"),
    cols=[{"title": "Needs approval", "icon": "check", "at": A("c09", "link")}, {"title": "Does not", "icon": "x", "at": A("c09", "bribe")}],
    rows=[{"cells": ["Official decision", "A bribe demand"], "cells_at": [A("c09", "decision"), A("c09", "bribe")]},
          {"cells": ["Official recommendation", "A pure criminal act"], "cells_at": [A("c09", "recommendation"), A("c09", "none")]}])
cue(type="point", t0=S("c10"), t1=E("c10") + 0.05, text="Judgments made simple · lawworld.ai", icon="check", accent=True, at=A("c10", "judgments"))
