# Mandya Urban Development Authority v. Sri. P. Chandrashekar & Ors., W.P. No. 43457 of 2015 (GM-RES), 2026:KHC:59899 (High Court of
# Karnataka at Bengaluru, Suraj Govindaraj J.; CAV order reserved 15.09.2026, pronounced 28.10.2026, REPORTABLE: "®" on page 1): panel
# cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND). KANNADA concept format (as czs); every anchor is a
# whole word of that clip's spoken Kannada.
# Facts from the judgment (paras): prayer to quash the order of R2 (State Commissioner for Persons with Disabilities) in Case
# No. 02/2013-14/481 dated 08.08.2013 and to dismiss the complaint of 26.06.2013 (1); complaint 26.06.2013 for a direction to allot a
# site in a layout of about 2,100 sites; summons 11.07.2013 under s.62 of the Disabilities Act, 1995; the authority's objections
# 18.07.2013 (2); order 08.08.2013: under s.43 not less than 3% to be reserved; directed the authority to allot a site and to reserve
# the required percentage (3), "3% reservation" (5.7-5.8); R1 has 80% locomotor disability with a certificate the authority does not
# contest (5.1, 10.10.1, 10.12); R1 paid Rs.600 on 22.08.2007 (9.12, 10.10.3); no site allotted (10.10.5); authority: 2% = 42 sites,
# only 11 applied, all 11 allotted; R1 never applied (4.3, 4.11, 9.1, 10.3, 10.10.2); R1: 3% was required (5.5); the 2007 payment was
# itself an application (10.10.4); 31 reserved sites lie unallotted (10.23).
# Held: reservation 2% until 14.12.2006; 3% from 14.12.2006 under Rule 28A(iii) (notification under s.73(1) of the 1995 Act inserting
# Chapter IVA into the Karnataka Rules of 2003); 5% under s.37(c) RPwD Act, 2016 only from the notification of 18.04.2026 (9.8, 9.19);
# registration and application are separate steps; an application needs the Rule 3(2) notice with a last date, Form II and the
# initial deposit, before the date and time fixed (10.16-10.20); the Rs.600 of 22.08.2007 was mere registration, not made in answer
# to any notice (there was none), not shown on Form II, not the initial deposit (10.21, 10.36); vacant reserved sites show
# availability, not entitlement; Rule 3(2) notice gives every eligible person the same chance to apply (10.23.1-10.23.2); s.62 lets the
# Commissioner look into complaints and take the matter up with the authorities, not allot property or order a statutory authority to
# give a particular site to a particular person (10.30.1, 10.30.3, 10.31, 10.34); W.P. allowed; the order of 08.08.2013 quashed,
# including the direction to allot a site and the direction to reserve the required percentage; complaint of 26.06.2013 dismissed;
# liberty to apply as and when the authority issues a notification; seniority in terms of the registration of 22.08.2007 (11.1).
# NOT shown: the CBI investigation, lottery allotments, officers in custody, the embargo (4.2, 5.12, 10.2, 10.7, 10.24-10.27); the
# 2021 amendment (9.11-9.12). R1 is named only on the cite card. The bench card uses the official portrait.
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen, as tej)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
STING = {"kicker": "ಕರ್ನಾಟಕ ಹೈಕೋರ್ಟ್ · ತೀರ್ಪು ವಿವರಣೆ", "title": "ನೋಂದಣಿ ಮಾತ್ರ, ಅರ್ಜಿ ಅಲ್ಲ", "sub": "W.P. No. 43457 of 2015 · 2026:KHC:59899"}
ENDCARD = {"title": "ನೋಂದಣಿ ಮಾತ್ರ, ಅರ್ಜಿ ಅಲ್ಲ", "line": "₹600 ನೋಂದಣಿ ನಿವೇಶನಕ್ಕೆ ಅರ್ಜಿ ಅಲ್ಲ; ಆಯುಕ್ತರು ಒಬ್ಬರಿಗೆ ನಿವೇಶನ ಹಂಚಲು ಆದೇಶಿಸುವಂತಿಲ್ಲ", "sub": "LawWorld: ವಕೀಲರಿಗಾಗಿ ಕಾನೂನು ಸಂಶೋಧನೆ"}

# ── 1 · ಅರ್ಜಿ ಇಲ್ಲದೆ ನಿವೇಶನ? ─────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "ಅಂಗವಿಕಲರ"), text="ಅರ್ಜಿ ಆಹ್ವಾನವಿಲ್ಲದೆ ಒಬ್ಬರಿಗೆ ಮೀಸಲು ನಿವೇಶನ: ಆಯುಕ್ತರು ಆದೇಶಿಸಬಹುದೇ?", hl="ಆದೇಶಿಸಬಹುದೇ?")
cue(type="bench", t0=S("c02"), t1=E("c02") + 0.05, tag="ಕರ್ನಾಟಕ ಹೈಕೋರ್ಟ್ · 28 ಅಕ್ಟೋಬರ್ 2026",
    judges=[{"name": "Justice Suraj Govindaraj", "photo": "../brand/judges/suraj_govindaraj.jpg", "at": A("c02", "ಗೌರವಾನ್ವಿತ")}])

# ── 2 · ಪಾವತಿ ಮತ್ತು ಆದೇಶ ───────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=A("c03", "ಮಂಡ್ಯ"), t1=E("c04") + 0.05, at=A("c03", "ಮಂಡ್ಯ"), tag="ಕರ್ನಾಟಕ ಹೈಕೋರ್ಟ್ · 28.10.2026",
    cases=[{"name": "Mandya Urban Development Authority v. P. Chandrashekar & Ors.", "cite": "W.P. No. 43457 of 2015 · 2026:KHC:59899"}])
cue(type="flow", t0=S("c03"), t1=E("c03") + 0.05, head="2007ರ ಪಾವತಿ", head_at=S("c03") + 0.05,
    steps=[{"label": "ಶೇ 80 ಚಲನ ಅಂಗವೈಕಲ್ಯ", "sub": "ಪ್ರಮಾಣಪತ್ರ ಇದೆ · ಪ್ರಾಧಿಕಾರದ ಆಕ್ಷೇಪವಿಲ್ಲ", "icon": "user", "at": A("c03", "ಚಲನ")},
           {"label": "₹600 ಪಾವತಿ · 22.08.2007", "sub": "ಮಂಡ್ಯ ನಗರಾಭಿವೃದ್ಧಿ ಪ್ರಾಧಿಕಾರಕ್ಕೆ", "icon": "file-text", "at": A("c03", "ಪಾವತಿಸಿದರು")},
           {"label": "ನಿವೇಶನ ಹಂಚಿಕೆ ಆಗಲಿಲ್ಲ", "icon": "x", "tone": "stop", "at": A("c03", "ಸಿಗಲಿಲ್ಲ")}])
cue(type="timeline", t0=S("c04"), t1=E("c04") + 0.05,
    nodes=[{"label": "ದೂರು", "value": "26.06.2013", "sub": "ಅಂಗವಿಕಲರ ರಾಜ್ಯ ಆಯುಕ್ತರಿಗೆ", "at": A("c04", "ದೂರಿನ")},
           {"label": "ಸಮನ್ಸ್", "value": "11.07.2013", "sub": "ಸೆಕ್ಷನ್ 62, ಅಂಗವಿಕಲರ ಕಾಯ್ದೆ, 1995", "at": A("c04", "ಆಯುಕ್ತರು")},
           {"label": "ಆಯುಕ್ತರ ಆದೇಶ", "value": "08.08.2013", "sub": "ಅವರಿಗೆ ನಿವೇಶನ ಹಂಚಿ", "at": A("c04", "ಹಂಚಲು")},
           {"label": "ಮೀಸಲು ನಿರ್ದೇಶನ", "value": "ಶೇ 3", "sub": "ಸೆಕ್ಷನ್ 43 · ನಿಯಮ 28A(iii)", "at": A("c04", "ಮೀಸಲಿಡಲು")}])

# ── 3 · ಎರಡೂ ಕಡೆಯ ವಾದ ──────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="compare", t0=S("c05"), t1=E("c05") + 0.05, head="ಆ ಪಾವತಿ ಅರ್ಜಿಯೇ?", head_at=S("c05") + 0.05,
    cols=[{"title": "ಪ್ರಾಧಿಕಾರ (ರಿಟ್ ಅರ್ಜಿದಾರ)", "icon": "landmark", "at": A("c05", "ಪ್ರಾಧಿಕಾರದ")}, {"title": "ದೂರುದಾರ", "icon": "user", "at": A("c05", "ದೂರುದಾರರ")}],
    rows=[{"cells": ["ಶೇ 2 ಮೀಸಲು: 42 ನಿವೇಶನ", "ಶೇ 3 ಮೀಸಲು ಬೇಕಿತ್ತು"], "cells_at": [A("c05", "ನಲವತ್ತೆರಡು"), A("c05", "ದೂರುದಾರರ")]},
          {"cells": ["ಅರ್ಜಿ ಹಾಕಿದ ಎಲ್ಲ 11 ಜನರಿಗೆ ನಿವೇಶನ", "31 ಮೀಸಲು ನಿವೇಶನ ಖಾಲಿ"], "cells_at": [A("c05", "ಹನ್ನೊಂದೂ"), A("c05", "ವಾದ", 2)]},
          {"cells": ["ದೂರುದಾರರು ಅರ್ಜಿ ಹಾಕಿಲ್ಲ", "22.08.2007ರ ₹600 ಪಾವತಿಯೇ ಅರ್ಜಿ"], "cells_at": [A("c05", "ಹಾಕಿಲ್ಲ"), A("c05", "ಪಾವತಿಯೇ")]}])

# ── 4 · ಹೈಕೋರ್ಟ್ ತೀರ್ಮಾನ ──────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="counters", t0=S("c06"), t1=E("c06") + 0.05, head="ಅಂಗವಿಕಲರ ಮೀಸಲು ಪಾಲು", head_at=S("c06") + 0.05,
    items=[{"value": 2, "unit": "%", "label": "14.12.2006ರವರೆಗೆ", "sub": "ನಿವೇಶನ ಹಂಚಿಕೆ ನಿಯಮ 13(2), 1991", "at": A("c06", "ಡಿಸೆಂಬರ್")},
           {"value": 3, "unit": "%", "label": "14.12.2006ರಿಂದ", "sub": "ನಿಯಮ 28A(iii), 2003ರ ಕರ್ನಾಟಕ ನಿಯಮಗಳು", "at": A("c06", "ನಂತರ")},
           {"value": 5, "unit": "%", "label": "18.04.2026ರಿಂದ", "sub": "ಸೆಕ್ಷನ್ 37(c), RPwD ಕಾಯ್ದೆ · ಅಧಿಸೂಚನೆ", "at": A("c06", "ಶೇಕಡ", 3)}])
cue(type="notequal", t0=S("c07"), t1=A("c07", "ಅರ್ಜಿ", 2, -0.3), left="₹600 ಪಾವತಿ", right="ನಿವೇಶನಕ್ಕೆ ಅರ್ಜಿ",
    at=A("c07", "ಪಾವತಿ"), left_at=A("c07", "ಪಾವತಿ"), sub="22.08.2007ರ ಪಾವತಿ ಕೇವಲ ನೋಂದಣಿ", sub_at=A("c07", "ನೋಂದಣಿ"))
cue(type="flow", t0=A("c07", "ಅರ್ಜಿ", 2, -0.3), t1=E("c07") + 0.05, head="ಅರ್ಜಿ ಎಂದರೆ", head_at=A("c07", "ಅರ್ಜಿ", 2),
    steps=[{"label": "ಅರ್ಜಿ ಆಹ್ವಾನಿಸುವ ಪ್ರಕಟಣೆ", "sub": "ಕೊನೆಯ ದಿನಾಂಕ ಸಹಿತ · ನಿಯಮ 3(2)", "icon": "file-text", "at": A("c07", "ಪ್ರಕಟಣೆಗೆ")},
           {"label": "ಫಾರ್ಮ್ IIರಲ್ಲಿ ಅರ್ಜಿ", "sub": "ನಿಯಮ 10(1)", "icon": "file-check", "at": A("c07", "ಫಾರ್ಮ್")},
           {"label": "ಆರಂಭಿಕ ಠೇವಣಿ", "sub": "ನಿಗದಿತ ದಿನಾಂಕದೊಳಗೆ · ನಿಯಮ 10", "icon": "check", "at": A("c07", "ಠೇವಣಿಯೊಂದಿಗೆ")}],
    note={"text": "ಇಲ್ಲಿ: ಪ್ರಕಟಣೆಯೇ ಇರಲಿಲ್ಲ", "icon": "x", "at": A("c07", "ಇಲ್ಲಿ")})
cue(type="point", t0=S("c08"), t1=A("c08", "ಆಯುಕ್ತರು", 1, -0.3), text="ಖಾಲಿ ಮೀಸಲು ನಿವೇಶನ ಒಬ್ಬರ ಹಕ್ಕಲ್ಲ: ಎಲ್ಲ ಅರ್ಹ ಅಂಗವಿಕಲರಿಗೂ ಅರ್ಜಿಯ ಸಮಾನ ಅವಕಾಶ", icon="scale", accent=True, at=A("c08", "ಖಾಲಿ"))
# owner: no section-sign glyph on any card (the "section" card type prints one), so the Commissioner's powers are a flow card
# (10.30.1, 10.30.3, 10.31, 10.34)
cue(type="flow", t0=A("c08", "ಆಯುಕ್ತರು", 1, -0.3), t1=E("c08") + 0.05, head="ಸೆಕ್ಷನ್ 61, 62 · ಅಂಗವಿಕಲರ ಕಾಯ್ದೆ, 1995", head_at=A("c08", "ಆಯುಕ್ತರು"),
    steps=[{"label": "ಆಯುಕ್ತರು ದೂರು ಪರಿಶೀಲಿಸಬಹುದು", "sub": "ಸಂಬಂಧಿತ ಪ್ರಾಧಿಕಾರದೊಂದಿಗೆ ವಿಷಯ ಕೈಗೆತ್ತಿಕೊಳ್ಳಬಹುದು", "icon": "search", "tone": "ok", "at": A("c08", "ಪರಿಶೀಲಿಸಬಹುದು")},
           {"label": "ಒಬ್ಬರಿಗೆ ನಿವೇಶನ ಹಂಚಲು ಆದೇಶಿಸುವಂತಿಲ್ಲ", "sub": "ನಿವೇಶನ ಹಂಚಿಕೆ ನಿಯಮಗಳನ್ನು ಮೀರುವಂತಿಲ್ಲ", "icon": "x", "tone": "stop", "at": A("c08", "ಒಬ್ಬರಿಗೆ")}])

# ── 5 · ಆದೇಶ ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="verdicts", t0=S("c09"), t1=A("c09", "ಅಧಿಸೂಚನೆ", 1, -0.3),
    rows=[{"text": "ಪ್ರಾಧಿಕಾರದ ರಿಟ್ ಅರ್ಜಿ ಪುರಸ್ಕೃತ", "ok": True, "at": A("c09", "ರಿಟ್")},
          {"text": "ಆಯುಕ್ತರ ಆದೇಶ · 08.08.2013 (ಹಂಚಿಕೆ, ಮೀಸಲು ನಿರ್ದೇಶನ)", "ok": False, "at": A("c09", "ಆಯುಕ್ತರ"), "strike_at": A("c09", "ರದ್ದುಗೊಳಿಸಿ")},
          {"text": "ದೂರು · 26.06.2013", "ok": False, "at": A("c09", "ದೂರು"), "strike_at": A("c09", "ವಜಾಗೊಳಿಸಿತು")}])
cue(type="list", t0=A("c09", "ಅಧಿಸೂಚನೆ", 1, -0.3), t1=E("c09") + 0.05, head="ಆದರೆ ದೂರುದಾರರಿಗೆ ದಾರಿ ಮುಕ್ತ", head_at=A("c09", "ಅಧಿಸೂಚನೆ"),
    items=[{"n": 1, "text": "ಅಧಿಸೂಚನೆ ಹೊರಡಿಸಿದಾಗ ಅರ್ಜಿ ಹಾಕಬಹುದು", "at": A("c09", "ಹಾಕಬಹುದು")},
           {"n": 2, "text": "ಹಿರಿತನ: 22.08.2007ರ ನೋಂದಣಿಯಂತೆ", "at": A("c09", "ಹಿರಿತನದೊಂದಿಗೆ")}])
cue(type="point", t0=S("c10"), t1=E("c10") + 0.05, text="Like · Share · Subscribe · lawworld.ai", icon="check", accent=True, at=A("c10", "ಲೈಕ್"))
