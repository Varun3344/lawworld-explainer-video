# Carl Zeiss India Pvt. Ltd. v. State of Karnataka (rep. by the Labour Inspector, Anekal Circle), Criminal Petition No. 847 of 2025,
# 2026:KHC:54744 (High Court of Karnataka at Bengaluru, Suraj Govindaraj J.; oral order 01.10.2026, REPORTABLE: "®" on page 1, on the
# court's Reportable list): panel cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND). KANNADA concept format
# (as drk); every anchor is a whole word of that clip's spoken Kannada.
# Facts from the judgment (paras): prayer to quash the complaint of 28.02.2023 (s.200 CrPC r/w s.26 CLRA Act) before the IV Addl. Civil
# Judge & JMFC, Anekal, C.C. No. 767/2023, the order of the same date taking cognizance of the offence punishable under s.24 CLRA Act, and
# the entire proceedings (1); petitioner's office: Plot No. 3, Jigani Link Road, Bommasandra Industrial Area (cause title); inspection
# by the respondent Labour Inspector at the petitioner's premises on 14.11.2022, violations "found" of Rules 72, 73, 74, 81(3), 25(v),
# Contract Labour (Regulation and Abolition) Act, 1970 r/w the Karnataka Rules, 1974 (2); observation note the same day; show-cause
# notice 23.11.2022; complaint 28.02.2023 (3); petitioner: s.27 three months run from the inspection; a show-cause notice is not an
# order, so the proviso does not apply; reply of 06.12.2022 (acknowledged the same day) with the complied registers and forms (4.1-4.4);
# HCGP: the proviso; the notice gave time to reply (natural justice); no reply; complaint within three months of that time (5);
# question (7); s.27 quoted (8). Held: three months from the date the alleged commission of the offence came to the Inspector's
# knowledge (9) = the inspection, 14.11.2022 (10); the six-month proviso only where the offence consists of disobeying a written order
# of the Inspector (11-12, 14); a show-cause notice merely calls for an explanation, it is not such an order and cannot postpone or
# extend limitation (13); the notice and the reply have no bearing on the commencement of limitation (16); complaint of 28.02.2023
# beyond three months; the notice does not postpone, the reply does not give a fresh period; the Magistrate could not have taken
# cognisance (17-18); petition allowed; complaint, cognisance order and the entire proceedings in C.C. 767/2023, insofar as the
# petitioner is concerned, quashed (19). NOT shown: Ben Salmon (4.2, 15; its printed date and statute are doubtful), J.U. Prabhu.
# The company is named on the cite card and in one neutral spoken sentence (c03). The bench card uses the official portrait.
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen, as tej)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
STING = {"kicker": "ಕರ್ನಾಟಕ ಹೈಕೋರ್ಟ್ · ತೀರ್ಪು ವಿವರಣೆ", "title": "ಕಾಲಮಿತಿ ತಪಾಸಣೆಯ ದಿನದಿಂದಲೇ", "sub": "Carl Zeiss India v. State of Karnataka · 2026:KHC:54744"}
ENDCARD = {"title": "ಕಾಲಮಿತಿ ತಪಾಸಣೆಯ ದಿನದಿಂದಲೇ", "line": "ಶೋಕಾಸ್ ನೋಟಿಸ್ ಲಿಖಿತ ಆದೇಶ ಅಲ್ಲ: ಸೆಕ್ಷನ್ 27ರ ಕಾಲಮಿತಿಯನ್ನು ಮುಂದೂಡುವುದಿಲ್ಲ", "sub": "LawWorld: ವಕೀಲರಿಗಾಗಿ ಕಾನೂನು ಸಂಶೋಧನೆ"}

# ── 1 · ಕಾಲಮಿತಿ ಎಂದಿನಿಂದ? ───────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "ಗುತ್ತಿಗೆ"), text="ದೂರಿನ 3 ತಿಂಗಳ ಕಾಲಮಿತಿ: ತಪಾಸಣೆಯ ದಿನದಿಂದಲೋ, ಶೋಕಾಸ್ ನೋಟಿಸ್‌ನಿಂದಲೋ?", hl="ಶೋಕಾಸ್ ನೋಟಿಸ್‌ನಿಂದಲೋ?")
cue(type="bench", t0=S("c02"), t1=E("c02") + 0.05, tag="ಕರ್ನಾಟಕ ಹೈಕೋರ್ಟ್ · 1 ಅಕ್ಟೋಬರ್ 2026",
    judges=[{"name": "Justice Suraj Govindaraj", "photo": "../brand/judges/suraj_govindaraj.jpg", "at": A("c02", "ಗೌರವಾನ್ವಿತ")}])

# ── 2 · ತಪಾಸಣೆ ಮತ್ತು ದೂರು ────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=A("c03", "ಕಾರ್ಲ್"), t1=E("c04") + 0.05, at=A("c03", "ಕಾರ್ಲ್"), tag="ಕರ್ನಾಟಕ ಹೈಕೋರ್ಟ್ · 01.10.2026",
    cases=[{"name": "Carl Zeiss India Pvt. Ltd. v. State of Karnataka", "cite": "2026:KHC:54744 · Crl.P. No. 847 of 2025"}])
cue(type="flow", t0=S("c03"), t1=E("c03") + 0.05, head="ತಪಾಸಣೆ", head_at=S("c03") + 0.05,
    steps=[{"label": "ಕಾರ್ಮಿಕ ನಿರೀಕ್ಷಕರು, ಆನೇಕಲ್ ವೃತ್ತ", "sub": "ಗುತ್ತಿಗೆ ಕಾರ್ಮಿಕ (ನಿಯಂತ್ರಣ ಮತ್ತು ರದ್ದತಿ) ಕಾಯ್ದೆ, 1970", "icon": "user", "at": A("c03", "ನಿರೀಕ್ಷಕರು")},
           {"label": "Carl Zeiss India Pvt. Ltd.", "sub": "ಬೊಮ್ಮಸಂದ್ರ ಕೈಗಾರಿಕಾ ಪ್ರದೇಶ, ಬೆಂಗಳೂರು", "icon": "landmark", "at": A("c03", "ಕಾರ್ಲ್")},
           {"label": "ಕಂಪನಿಯ ಆವರಣದಲ್ಲಿ ತಪಾಸಣೆ", "sub": "14 ನವೆಂಬರ್ 2022", "icon": "search", "at": A("c03", "ತಪಾಸಣೆ")}])
cue(type="timeline", t0=S("c04"), t1=E("c04") + 0.05,
    nodes=[{"label": "ಅವಲೋಕನ ಟಿಪ್ಪಣಿ", "value": "14 ನವೆಂಬರ್ 2022", "sub": "ತಪಾಸಣೆಯ ದಿನವೇ", "at": A("c04", "ಟಿಪ್ಪಣಿ")},
           {"label": "ಶೋಕಾಸ್ ನೋಟಿಸ್", "value": "23 ನವೆಂಬರ್ 2022", "sub": "ವಿವರಣೆಗೆ ಕೋರಿಕೆ", "at": A("c04", "ಶೋಕಾಸ್")},
           {"label": "ದೂರು", "value": "28 ಫೆಬ್ರವರಿ 2023", "sub": "ಉತ್ತರ ಬಂದಿಲ್ಲ ಎಂದು · C.C. No. 767/2023", "at": A("c04", "ಫೆಬ್ರವರಿ")},
           {"label": "ಕಾಗ್ನಿಜೆನ್ಸ್", "value": "28 ಫೆಬ್ರವರಿ 2023", "sub": "ಸೆಕ್ಷನ್ 24 · JMFC, ಆನೇಕಲ್", "tone": "stop", "at": A("c04", "ಕಾಗ್ನಿಜೆನ್ಸ್")}])

# ── 3 · ಎರಡೂ ಕಡೆಯ ವಾದ ──────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="compare", t0=S("c05"), t1=E("c05") + 0.05, head="ಕಾಲಮಿತಿ ಎಂದಿನಿಂದ?", head_at=S("c05") + 0.05,
    cols=[{"title": "ಅರ್ಜಿದಾರ ಕಂಪನಿ", "icon": "user", "at": A("c05", "ಕಂಪನಿಯ")}, {"title": "ಸರ್ಕಾರ", "icon": "landmark", "at": A("c05", "ಸರ್ಕಾರದ")}],
    rows=[{"cells": ["ತಪಾಸಣೆಯ ದಿನದಿಂದ 3 ತಿಂಗಳು", "ಸೆಕ್ಷನ್ 27ರ ಪ್ರೊವಿಸೊ: 6 ತಿಂಗಳು"], "cells_at": [A("c05", "ಕಾಲಮಿತಿ"), A("c05", "ಪ್ರೊವಿಸೊ")]},
          {"cells": ["ಶೋಕಾಸ್ ನೋಟಿಸ್ ಆದೇಶ ಅಲ್ಲ", "ಉತ್ತರಕ್ಕೆ ಸಮಯ ನೀಡಲಾಗಿತ್ತು, ಉತ್ತರ ಬಂದಿಲ್ಲ"], "cells_at": [A("c05", "ಶೋಕಾಸ್"), A("c05", "ಉತ್ತರಕ್ಕೆ")]},
          {"cells": ["06.12.2022ರಂದೇ ರಿಜಿಸ್ಟರ್, ಫಾರ್ಮ್‌ಗಳ ಸಹಿತ ಉತ್ತರ", "ಆ ಸಮಯದಿಂದ 3 ತಿಂಗಳೊಳಗೆ ದೂರು"], "cells_at": [A("c05", "ಅಲ್ಲ"), A("c05", "ತಿಂಗಳೊಳಗೆ")]}])

# ── 4 · ಹೈಕೋರ್ಟ್ ತೀರ್ಮಾನ ──────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c06"), t1=E("c06") + 0.05, at=A("c06", "ಸೆಕ್ಷನ್"), act="ಗುತ್ತಿಗೆ ಕಾರ್ಮಿಕ ಕಾಯ್ದೆ, 1970", num="27", title="ಅಭಿಯೋಜನೆಗೆ ಕಾಲಮಿತಿ",
    points=[{"text": "ಆಪಾದಿತ ಉಲ್ಲಂಘನೆ ನಿರೀಕ್ಷಕರ ಗಮನಕ್ಕೆ ಬಂದ ದಿನದಿಂದ 3 ತಿಂಗಳೊಳಗೆ ದೂರು", "at": A("c06", "ಗಮನಕ್ಕೆ")},
            {"text": "ಇಲ್ಲದಿದ್ದರೆ ಕೋರ್ಟ್ ಕಾಗ್ನಿಜೆನ್ಸ್ ತೆಗೆದುಕೊಳ್ಳುವಂತಿಲ್ಲ", "at": A("c06", "ಎಣಿಸಬೇಕು")}],
    note={"text": "ಇಲ್ಲಿ: ತಪಾಸಣೆಯ ದಿನ, 14.11.2022", "icon": "calendar", "at": A("c06", "ತಪಾಸಣೆಯ")})
cue(type="point", t0=S("c07"), t1=A("c07", "ಶೋಕಾಸ್", 1, -0.3), text="ಪ್ರೊವಿಸೊದ 6 ತಿಂಗಳು: ನಿರೀಕ್ಷಕರ ಲಿಖಿತ ಆದೇಶ ಪಾಲಿಸದಿದ್ದಾಗ ಮಾತ್ರ", icon="info", accent=True, at=A("c07", "ಪ್ರೊವಿಸೊದ"))
cue(type="notequal", t0=A("c07", "ಶೋಕಾಸ್", 1, -0.3), t1=E("c07") + 0.05, left="ಶೋಕಾಸ್ ನೋಟಿಸ್", right="ಲಿಖಿತ ಆದೇಶ",
    at=A("c07", "ಶೋಕಾಸ್"), left_at=A("c07", "ಶೋಕಾಸ್"), sub="ಏಕೆ ಕ್ರಮ ಕೈಗೊಳ್ಳಬಾರದು ಎಂದು ವಿವರಣೆ ಕೇಳುತ್ತದೆ ಅಷ್ಟೇ", sub_at=A("c07", "ವಿವರಣೆ"))
cue(type="flow", t0=S("c08"), t1=E("c08") + 0.05, head="ಕಾಲಮಿತಿಯ ಲೆಕ್ಕ", head_at=S("c08") + 0.05,
    steps=[{"label": "ಶೋಕಾಸ್ ನೋಟಿಸ್ · 23.11.2022", "sub": "ಕಾಲಮಿತಿಯ ಆರಂಭವನ್ನು ಮುಂದೂಡುವುದಿಲ್ಲ", "icon": "x", "at": A("c08", "ನೋಟಿಸ್‌ನಿಂದ")},
           {"label": "ಉತ್ತರ · 06.12.2022 (ಕಂಪನಿಯ ಪ್ರಕಾರ)", "sub": "ಹೊಸ ಕಾಲಮಿತಿ ಶುರುವಾಗುವುದಿಲ್ಲ", "icon": "x", "at": A("c08", "ಉತ್ತರದಿಂದ")},
           {"label": "ದೂರು · 28.02.2023", "sub": "14.11.2022ರಿಂದ 3 ತಿಂಗಳು ಮೀರಿದೆ", "icon": "calendar", "tone": "stop", "at": A("c08", "ಫೆಬ್ರವರಿ")}])

# ── 5 · ಆದೇಶ ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "ಹೈಕೋರ್ಟ್", 1, -0.3), text="ಕಾಲಮಿತಿ ಮೀರಿದ ದೂರು: ಮ್ಯಾಜಿಸ್ಟ್ರೇಟ್ ಕಾಗ್ನಿಜೆನ್ಸ್ ತೆಗೆದುಕೊಳ್ಳುವಂತಿರಲಿಲ್ಲ", icon="scale", accent=True, at=A("c09", "ಮ್ಯಾಜಿಸ್ಟ್ರೇಟ್"))
cue(type="verdicts", t0=A("c09", "ಹೈಕೋರ್ಟ್", 1, -0.3), t1=E("c09") + 0.05,
    rows=[{"text": "ಕ್ರಿಮಿನಲ್ ಅರ್ಜಿ ಪುರಸ್ಕೃತ", "ok": True, "at": A("c09", "ಕ್ರಿಮಿನಲ್")},
          {"text": "ದೂರು ಮತ್ತು ಕಾಗ್ನಿಜೆನ್ಸ್ ಆದೇಶ · 28.02.2023", "ok": False, "at": A("c09", "ದೂರು"), "strike_at": A("c09", "ರದ್ದುಗೊಳಿಸಿತು")},
          {"text": "C.C. No. 767/2023: ಕಂಪನಿಯ ವಿರುದ್ಧದ ಸಂಪೂರ್ಣ ಪ್ರಕರಣ", "ok": False, "at": A("c09", "ಕಂಪನಿಯ"), "strike_at": A("c09", "ರದ್ದುಗೊಳಿಸಿತು")}])
cue(type="point", t0=S("c10"), t1=E("c10") + 0.05, text="Like · Share · Subscribe · lawworld.ai", icon="check", accent=True, at=A("c10", "ಲೈಕ್"))
