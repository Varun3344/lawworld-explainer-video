# Union of India & Ors. v. Narender Kumar, 2026 INSC 1166, C.A. @ SLP (C) Diary No. 27220 of 2026 (Pamidighantam Sri Narasimha J., Alok
# Aradhe J. - no named author; decided 28.10.2026, REPORTABLE): panel cues, run by split/build_course_plan.py (helpers: at S E cue fx have
# r3 PEND). Concept format as set tex.
# Facts from the judgment (paras): the Union (MoD) challenges the concurrent findings of the AFT (OA No. 221 of 2019, 08.04.2024) and the
# High Court (CWP No. 23117 of 2025, 11.08.2025) granting War Injury Pension in place of Disability Pension for rheumatoid arthritis,
# developed owing to his posting at Kargil as part of Operation Rakshak (2); enrolled 30.12.1996; at Kargil 13.07.2003-06.07.2005,
# diagnosed with Rheumatoid Arthritis (Seropositive); discharged 31.01.2013; Release Medical Board: all three disabilities aggravated by
# military service @70% for life, rounded off to 75%; 16+ years of service; Disability Pension, Service + Disability Element (3); about 6
# years later, the AFT claim under Part II, Category E(i), Para 4.1, MoD Policy Letter of 31.01.2001 (4); AFT: the entire J&K area is an
# operational area (6); High Court dismissed the MoD's challenge (7); Para 4.1 is now also in the Pension Regulations for the Army, 2008,
# Reg. 82 (10); Category E: war or war-like situations, (i) "Operations specially notified by the Govt. from time to time" (10, 11);
# the MoD/ASG: E(i) covers only operations like Operation Sindoor or Operation Snow Leopard, not ongoing ones like Operation Rakshak (entire
# J&K) or Operation Rhino (entire Assam) (13); once a notification is issued for a specific operation, E(i) is invoked unless something in
# the Policy or the notification indicates otherwise; only the ASG's oral statement, no other interpretative aid, to exclude Operation
# Rakshak (16); "the primary burden lies on the policymaker"; courts disregard its reading against the plain language (17); "What a policy
# says, it is and not what is in the imagination of the policymaker" (18); "A liberal interpretation is compelling" (19); the Government
# must declare in clear terms whether E(i) benefits apply when notifying (21); "high time" for comprehensive and clearly identifiable MoD
# subordinate legislation (9); appeal dismissed (22). The High Court is not named in the judgment, so no card names it. The bench card
# uses the official portraits; "Justice P.S. Narasimha" on the card (the full name wraps to three lines at 380 px; it is spoken in full).
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow (24 + 58 px) ends inside the panel: the 9:16 band edge cut it into a line at 40
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen (no blobs / star behind the cards)
STING = {"kicker": "SUPREME COURT · JUDGMENT EXPLAINED", "title": "War injury pension, read plainly", "sub": "Union of India v. Narender Kumar · 2026 INSC 1166"}
ENDCARD = {"title": "War injury pension, read plainly", "line": "E(i) covers notified operations unless the text says otherwise", "sub": "LawWorld: legal research for advocates"}

# ── 1 · who reads the policy? ────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "soldier"), text="A soldier's war injury pension: who decides what the policy means, its plain words or the Ministry?", hl="its plain words or the Ministry?")
cue(type="bench", t0=S("c02"), t1=E("c02") + 0.05, tag="Supreme Court of India · 28 October 2026",
    judges=[{"name": "Justice P.S. Narasimha", "photo": "../brand/judges/pamidighantam_sri_narasimha.jpg", "at": A("c02", "honourable")},
            {"name": "Justice Alok Aradhe", "photo": "../brand/judges/alok_aradhe.jpg", "at": A("c02", "honourable", 2)}])

# ── 2 · kargil ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=A("c03", "soldier"), t1=E("c04") + 0.05, at=A("c03", "soldier"), tag="SUPREME COURT OF INDIA · 28.10.2026",
    cases=[{"name": "Union of India & Ors. v. Narender Kumar", "cite": "2026 INSC 1166 · Civil Appeal @ SLP (C) Diary No. 27220 of 2026"}])
cue(type="flow", t0=S("c03"), t1=E("c03") + 0.05, head="The soldier", head_at=S("c03") + 0.05,
    steps=[{"label": "Indian Army", "sub": "enrolled 30 Dec 1996 · the respondent", "icon": "user", "at": A("c03", "soldier")},
           {"label": "Posted at Kargil", "sub": "13 Jul 2003 – 6 Jul 2005 · Operation Rakshak", "icon": "landmark", "at": A("c03", "kargil")},
           {"label": "Rheumatoid arthritis (seropositive)", "sub": "diagnosed while posted at Kargil", "icon": "file-text", "at": A("c03", "diagnosed")}])
cue(type="timeline", t0=S("c04"), t1=E("c04") + 0.05,
    nodes=[{"label": "DISCHARGED", "value": "31 Jan 2013", "sub": "after 16+ years of service", "at": A("c04", "discharged")},
           {"label": "MEDICAL BOARD", "value": "75% for life", "sub": "3 disabilities, 70% rounded off · aggravated", "at": A("c04", "disability")},
           {"label": "ARMED FORCES TRIBUNAL", "value": "OA 221 of 2019", "sub": "about 6 years later: war injury pension", "at": A("c04", "tribunal")}])

# ── 3 · the claim ────────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c05"), t1=A("c05", "tribunal") - 0.05, at=A("c05", "claim"), act="MoD POLICY LETTER · 31.01.2001", num="E(i)", title="War injury pension · Part II, Para 4.1",
    points=[{"text": "Category E: death or disability in war or war-like situations", "at": A("c05", "defence")},
            {"text": "(i) “Operations specially notified by the Govt. from time to time”", "at": A("c05", "operations")}])
cue(type="flow", t0=A("c05", "tribunal"), t1=E("c05") + 0.05, head="Before the appeal", head_at=A("c05", "tribunal"),
    steps=[{"label": "Armed Forces Tribunal · 8 Apr 2024", "sub": "allowed: the entire J&K area is an operational area", "icon": "check", "tone": "ok", "at": A("c05", "allowed")},
           {"label": "High Court · 11 Aug 2025", "sub": "the MoD's challenge dismissed · CWP No. 23117 of 2025", "icon": "check", "tone": "ok", "at": A("c05", "upheld")}])
cue(type="compare", t0=S("c06"), t1=E("c06") + 0.05, head="The Union's reading of E(i)", head_at=A("c06", "union"),
    cols=[{"title": "Covered", "icon": "check", "at": A("c06", "snow")}, {"title": "Not covered", "icon": "x", "at": A("c06", "ongoing")}],
    rows=[{"cells": ["Operation Sindoor", "Operation Rakshak · all of J&K"], "cells_at": [A("c06", "snow"), A("c06", "rakshak")]},
          {"cells": ["Operation Snow Leopard", "Operation Rhino · all of Assam"], "cells_at": [A("c06", "snow"), A("c06", "rakshak")]}])

# ── 4 · what the court held ──────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c07"), t1=E("c07") + 0.05, head="Category E(i), on its plain language", head_at=S("c07") + 0.05,
    steps=[{"label": "A specific operation is notified", "sub": "by the Government, from time to time", "icon": "file-text", "at": A("c07", "notified")},
           {"label": "Category E(i) is invoked", "sub": "war injury pension applies", "icon": "check", "tone": "ok", "at": A("c07", "applies")},
           {"label": "Unless the policy or the notification", "sub": "indicates otherwise", "icon": "info", "at": A("c07", "unless")}],
    note={"text": "Against Operation Rakshak: only the ASG's oral statement, no other interpretative aid", "icon": "x", "at": A("c07", "oral")})
cue(type="point", t0=S("c08"), t1=A("c08", "what") - 0.05, text="“The primary burden lies on the policymaker”", icon="scale", at=A("c08", "burden"))
cue(type="point", t0=A("c08", "what") - 0.05, t1=E("c08") + 0.05, text="“What a policy says, it is and not what is in the imagination of the policymaker.”", icon="scale", accent=True, at=A("c08", "what"))

# ── 5 · the verdict ──────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "appeal") - 0.05, text="Pension policies: “A liberal interpretation is compelling”", icon="check", at=A("c09", "pension"))
cue(type="flow", t0=A("c09", "appeal") - 0.05, t1=E("c09") + 0.05, head="The verdict", head_at=A("c09", "appeal"),
    steps=[{"label": "The Union's appeal dismissed", "sub": "the AFT and High Court orders stand", "icon": "check", "tone": "ok", "at": A("c09", "dismissed")},
           {"label": "When notifying under E(i)", "sub": "Govt must declare in clear terms if benefits apply", "icon": "file-text", "at": A("c09", "notifications")}],
    note={"text": "Observation: “high time” for MoD subordinate legislation", "icon": "info", "at": A("c09", "clearly")})
cue(type="point", t0=S("c10"), t1=E("c10") + 0.05, text="Like · Share · Subscribe · lawworld.ai", icon="check", accent=True, at=A("c10", "like"))
