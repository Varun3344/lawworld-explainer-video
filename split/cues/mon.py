# Smt. Monika v. The Registrar General, High Court of Karnataka & Anr., W.P. No. 674 of 2026 (S-RES) (High Court of Karnataka at
# Bengaluru, M. Nagaprasanna J.; reserved 25.09.2026, CAV order pronounced 16.10.2026, REPORTABLE: "R" on page 1, on the court's
# Reportable list; no neutral citation printed): panel cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND).
# KANNADA concept format (as ram); every anchor is a whole word of that clip's spoken Kannada.
# Facts from the judgment (paras): prayer to quash Order No. HCC-02/2009 (Software Technician) of 15.04.2025 passed by R1 (1);
# appointed Software Technician on 06.06.2019 in the High Court and placed on probation; transfers to Kalaburagi 27.02.2021, Tumakuru
# 29.06.2022 and Bengaluru 13.02.2023 (the last two on her request) (3, 7); in the unit of the Prl. District & Sessions Judge,
# Bengaluru Rural District since 16.02.2023 (notice in 7); maternity leave 180 days, 27.06.2023-24.12.2023, granted (7); then, on the
# grounds of taking care of the baby, earned leave 35 days 25.12.2023-28.01.2024 and EOLWA 70 days 29.01.2024-07.04.2024 and 99 days
# 08.04.2024-15.07.2024 (notice); office note 01.08.2024: 180 + 35 + 169 days availed, no leave left for a probationer (7); request of
# 15.07.2024 for EOL to 12.01.2025, only 30 days to 14.08.2024 granted (7, notice) - 199 days of EOL in all (70 + 99 + 30); did not
# report on 15.08.2024; notice of 25.09.2024 to report immediately and show cause within 7 days why disciplinary action should not be
# initiated (notice); reply: no one to take care of the baby, frequent health issues, more leave sought (3, 7); discharged 15.04.2025
# under Rule 6(1), Karnataka Civil Services (Probation) Rules, 1977, as unsuitable to hold the post; relieved 25.04.2025 (7);
# petitioner: discharged while on maternity leave, contrary to law; sympathetic consideration; reinstatement (4); question (8).
# Held: a probationer whose probation was never declared satisfactorily completed, while that of all other similarly placed employees
# was declared satisfactory in 2025 with retrospective effect; after exhausting the maternity leave to which she was legitimately
# entitled and every other leave, she remained absent without authorisation, not momentarily (9); maternity leave is a manifestation of
# the constitutional commitment to dignity, motherhood and substantive equality, a right the law zealously protects and not a
# concession; but a right cannot be stretched beyond its legitimate contours to become "an inexhaustible charter for unauthorised
# absence" (10); maternity leave was never denied; it cannot be made a convenient shield against the consequences of an independent and
# prolonged unauthorised absence (11, 13); petition dismissed (14). Not shown: the departmental-inquiry submission (4), on which the
# Court made no separate finding; the husband's employment (5); para 12. The petitioner is not named in speech; the case title is on
# the cite card only. The bench card uses the official portrait.
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen, as tej)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
STING = {"kicker": "ಕರ್ನಾಟಕ ಹೈಕೋರ್ಟ್ · ತೀರ್ಪು ವಿವರಣೆ", "title": "ಹೆರಿಗೆ ರಜೆ: ಹಕ್ಕು, ಗೈರಿಗೆ ಗುರಾಣಿಯಲ್ಲ", "sub": "W.P. No. 674 of 2026 (S-RES) · 16.10.2026"}
ENDCARD = {"title": "ಹೆರಿಗೆ ರಜೆ: ಹಕ್ಕು, ಗೈರಿಗೆ ಗುರಾಣಿಯಲ್ಲ", "line": "ಹೆರಿಗೆ ರಜೆ ಕಾನೂನಿನಿಂದ ರಕ್ಷಿತ ಹಕ್ಕು, ಆದರೆ ನಂತರದ ಅನಧಿಕೃತ ಗೈರಿಗೆ ಗುರಾಣಿಯಲ್ಲ", "sub": "LawWorld: ವಕೀಲರಿಗಾಗಿ ಕಾನೂನು ಸಂಶೋಧನೆ"}

# ── 1 · ಹೆರಿಗೆ ರಜೆ ಗುರಾಣಿಯೇ? ─────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "ಎಲ್ಲ"), text="ಎಲ್ಲ ರಜೆ ಮುಗಿದರೂ ಗೈರು: ಸೇವೆಯಿಂದ ಬಿಡುಗಡೆಯ ವಿರುದ್ಧ ಹೆರಿಗೆ ರಜೆ ಗುರಾಣಿಯೇ?", hl="ಗುರಾಣಿಯೇ?")
cue(type="bench", t0=S("c02"), t1=E("c02") + 0.05, tag="ಕರ್ನಾಟಕ ಹೈಕೋರ್ಟ್ · 16 ಅಕ್ಟೋಬರ್ 2026",
    judges=[{"name": "Justice M. Nagaprasanna", "photo": "../brand/judges/m_nagaprasanna.jpg", "at": A("c02", "ಗೌರವಾನ್ವಿತ")}])

# ── 2 · ನೇಮಕ ಮತ್ತು ರಜೆ ──────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=A("c03", "ಸಾಫ್ಟ್‌ವೇರ್"), t1=E("c04") + 0.05, at=A("c03", "ಸಾಫ್ಟ್‌ವೇರ್"), tag="ಕರ್ನಾಟಕ ಹೈಕೋರ್ಟ್ · 16.10.2026",
    cases=[{"name": "Smt. Monika v. Registrar General, High Court of Karnataka", "cite": "W.P. No. 674 of 2026 (S-RES)"}])
cue(type="flow", t0=S("c03"), t1=E("c03") + 0.05, head="ನೇಮಕ ಮತ್ತು ಹೆರಿಗೆ ರಜೆ", head_at=S("c03") + 0.05,
    steps=[{"label": "ಸಾಫ್ಟ್‌ವೇರ್ ಟೆಕ್ನಿಷಿಯನ್", "sub": "ನೇಮಕ: 06.06.2019", "icon": "user", "at": A("c03", "ಸಾಫ್ಟ್‌ವೇರ್")},
           {"label": "ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ ಜಿಲ್ಲಾ ನ್ಯಾಯಾಲಯ", "sub": "16.02.2023ರಿಂದ · ಇನ್ನೂ ಪ್ರೊಬೇಷನ್‌ನಲ್ಲಿ", "icon": "landmark", "at": A("c03", "ಪ್ರೊಬೇಷನ್")},
           {"label": "ಹೆರಿಗೆ ರಜೆ: 180 ದಿನ", "sub": "27.06.2023 – 24.12.2023 · ಮಂಜೂರು", "icon": "calendar", "tone": "ok", "at": A("c03", "ಹೆರಿಗೆ")}])
cue(type="counters", t0=S("c04"), t1=E("c04") + 0.05, head="ಮಂಜೂರಾದ ರಜೆ", head_at=S("c04") + 0.05,
    items=[{"value": 180, "unit": "ದಿನ", "label": "ಹೆರಿಗೆ ರಜೆ", "sub": "27.06.2023 – 24.12.2023", "at": A("c04", "ನಂತರ")},
           {"value": 35, "unit": "ದಿನ", "label": "ಗಳಿಕೆ ರಜೆ", "sub": "25.12.2023 – 28.01.2024", "at": A("c04", "ಗಳಿಕೆ")},
           {"value": 199, "unit": "ದಿನ", "label": "ಅಸಾಧಾರಣ ರಜೆ", "sub": "29.01.2024 – 14.08.2024 (70 + 99 + 30)", "at": A("c04", "ಅಸಾಧಾರಣ")}],
    note={"text": "15.08.2024ರಿಂದ ಕರ್ತವ್ಯಕ್ಕೆ ಹಾಜರಾಗಲಿಲ್ಲ", "icon": "x", "at": A("c04", "ಬಳಿಕ")})

# ── 3 · ಬಿಡುಗಡೆ ಮತ್ತು ವಾದ ─────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c05"), t1=E("c05") + 0.05, head="ನೋಟಿಸ್ ಮತ್ತು ಬಿಡುಗಡೆ", head_at=S("c05") + 0.05,
    steps=[{"label": "ನೋಟಿಸ್: ಕೂಡಲೇ ಹಾಜರಾಗಿ", "sub": "25.09.2024 · 7 ದಿನದಲ್ಲಿ ವಿವರಣೆ ಕೋರಿಕೆ", "icon": "file-text", "at": A("c05", "ನೋಟಿಸ್")},
           {"label": "ಉತ್ತರ: ಮಗುವನ್ನು ನೋಡಿಕೊಳ್ಳಲು ಯಾರೂ ಇಲ್ಲ", "sub": "ಆಗಾಗ ಆರೋಗ್ಯ ಸಮಸ್ಯೆ · ಇನ್ನಷ್ಟು ರಜೆಗೆ ಕೋರಿಕೆ", "icon": "user", "at": A("c05", "ಮಗುವನ್ನು")},
           {"label": "ಸೇವೆಯಿಂದ ಬಿಡುಗಡೆ · 15.04.2025", "sub": "ನಿಯಮ 6(1), KCS (Probation) Rules, 1977", "icon": "x", "tone": "stop", "at": A("c05", "ಸೇವೆಯಿಂದ")}])
cue(type="list", t0=S("c06"), t1=A("c06", "ಬಿಡುಗಡೆ", 2, -0.4), head="ರಿಟ್ ಅರ್ಜಿ · ಅರ್ಜಿದಾರೆಯ ವಾದ", head_at=S("c06") + 0.05,
    items=[{"n": 1, "text": "ಹೆರಿಗೆ ರಜೆಯಲ್ಲಿದ್ದಾಗಲೇ ಬಿಡುಗಡೆ: ಕಾನೂನುಬಾಹಿರ", "at": A("c06", "ಕಾನೂನುಬಾಹಿರ")},
           {"n": 2, "text": "ಸಹಾನುಭೂತಿಯಿಂದ ಪರಿಗಣಿಸಿ, ಮತ್ತೆ ಸೇವೆಗೆ ಸೇರಿಸಿಕೊಳ್ಳಬೇಕು", "at": A("c06", "ಸಹಾನುಭೂತಿಯಿಂದ")}])
cue(type="question", t0=A("c06", "ಬಿಡುಗಡೆ", 2, -0.35), t1=E("c06") + 0.05, at=A("c06", "ಬಿಡುಗಡೆ", 2), text="ಈ ಬಿಡುಗಡೆ ಪ್ರೊಬೇಷನ್ ನಿಯಮಗಳಿಗೆ ವಿರುದ್ಧವೇ?", hl="ವಿರುದ್ಧವೇ?")

# ── 4 · ಹೈಕೋರ್ಟ್ ತೀರ್ಮಾನ ──────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="list", t0=S("c07"), t1=E("c07") + 0.05, head="ಹೈಕೋರ್ಟ್ ಗಮನಿಸಿದ್ದು", head_at=S("c07") + 0.05,
    items=[{"n": 1, "text": "ಪ್ರೊಬೇಷನ್ ತೃಪ್ತಿಕರವೆಂದು ಎಂದೂ ಘೋಷಣೆಯಾಗಿರಲಿಲ್ಲ", "at": A("c07", "ಪ್ರೊಬೇಷನ್")},
           {"n": 2, "text": "ಸಮಾನ ಸ್ಥಿತಿಯ ಇತರರ ಪ್ರೊಬೇಷನ್ 2025ರಲ್ಲಿ ತೃಪ್ತಿಕರವೆಂದು ಘೋಷಿತ (ಪೂರ್ವಾನ್ವಯ)", "at": A("c07", "ಘೋಷಣೆಯಾಗಿರಲಿಲ್ಲ")},
           {"n": 3, "text": "ಎಲ್ಲ ರಜೆ ಮುಗಿದ ಮೇಲೂ ಅನಧಿಕೃತ ಗೈರುಹಾಜರಿ ಮುಂದುವರಿಕೆ", "at": A("c07", "ಅನಧಿಕೃತ")}])
cue(type="point", t0=S("c08"), t1=A("c08", "ಆದರೆ", 1, -0.3), text="ಹೆರಿಗೆ ರಜೆ ಕಾನೂನಿನಿಂದ ರಕ್ಷಿತ ಹಕ್ಕು: ಘನತೆ, ಮಾತೃತ್ವ, ವಾಸ್ತವಿಕ ಸಮಾನತೆಗೆ ಸಾಂವಿಧಾನಿಕ ಬದ್ಧತೆ", icon="check", accent=True, at=A("c08", "ಹೆರಿಗೆ"))
cue(type="notequal", t0=A("c08", "ಆದರೆ", 1, -0.3), t1=E("c08") + 0.05, left="ಹೆರಿಗೆ ರಜೆಯ ಹಕ್ಕು", right="ಗೈರಿನ ಪರವಾನಗಿ",
    at=A("c08", "ಆದರೆ"), left_at=A("c08", "ಆದರೆ"), sub="ಹಕ್ಕನ್ನು ಅದರ ನ್ಯಾಯಸಮ್ಮತ ಮಿತಿ ಮೀರಿ ವಿಸ್ತರಿಸಲಾಗದು", sub_at=A("c08", "ವಿಸ್ತರಿಸಲಾಗದು"))

# ── 5 · ಫಲಿತಾಂಶ ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="verdicts", t0=S("c09"), t1=E("c09") + 0.05,
    rows=[{"text": "ಹೆರಿಗೆ ರಜೆ ಎಂದೂ ನಿರಾಕರಿಸಿಲ್ಲ", "ok": True, "at": A("c09", "ಹೆರಿಗೆ")},
          {"text": "ನಂತರದ ದೀರ್ಘ ಅನಧಿಕೃತ ಗೈರಿಗೆ ಹೆರಿಗೆ ರಜೆ ಗುರಾಣಿಯಲ್ಲ", "ok": True, "at": A("c09", "ಗುರಾಣಿ")},
          {"text": "ಸೇವೆಯಿಂದ ಬಿಡುಗಡೆ ಆದೇಶದ ವಿರುದ್ಧ ರಿಟ್ ಅರ್ಜಿ", "ok": False, "at": A("c09", "ಹೈಕೋರ್ಟ್"), "strike_at": A("c09", "ವಜಾಗೊಳಿಸಿತು")}])
cue(type="point", t0=S("c10"), t1=E("c10") + 0.05, text="Like · Share · Subscribe · lawworld.ai", icon="check", accent=True, at=A("c10", "ಲೈಕ್"))
