# Smt. Drakshayini @ Girija & Anr. v. Assistant Commissioner and Sub-Divisional Magistrate, Shimoga Sub-Division & Anr., W.P. No. 34895
# of 2025 (GM-RES), 2026:KHC:58865 (High Court of Karnataka at Bengaluru, Suraj Govindaraj J.; CAV order 14.10.2026, REPORTABLE list):
# panel cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND). KANNADA concept format (as krm); every anchor is a
# whole word of that clip's spoken Kannada.
# Facts from the judgment (paras): Petitioner 1 the daughter of Respondent 2, Petitioner 2 her husband (2); registered release deed of
# 09.01.2025 by the father in her favour, relinquishing all his rights in Sy. No. 42, 1 acre 30 guntas, Hunasekatte, Kasba-2 Hobli,
# Bhadravathi Taluk (3.1-3.2); the father about 74 when he executed it (8.3); his s.23 application (Maintenance and Welfare of Parents
# and Senior Citizens Act, 2007) to the AC, Shimoga Sub-Division, allowed 08.09.2025, corrigendum 06.10.2025 (2, 4.9); petitioners:
# Agreement of Sale 31.07.2023 for Rs 17,25,000 (Rs 7,25,000 in cash, balance in 6 months), receipt 01.08.2023, no maintenance condition
# in the deed so no s.23 jurisdiction (3.1-3.6, 9.3); the father: transfer on the understanding the daughter would care for him in old
# age (8.5, 8.7); no consideration paid, documents disputed (4.4-4.7); point 1 (6); following Sri Venkataiah v. State of Karnataka
# (W.P. No. 13313 of 2025), an express condition is not by itself a prerequisite; where the application specifically alleges a transfer
# on an understanding of care, the AC must examine it (8.1, 8.6, 8.8); receipt of 01.08.2023 refers to a Will of 09.08.2023, doubtful,
# cannot be relied on (9.6); even per the receipt the money went to the brothers, not the father: no consideration to him that takes the
# transfer out of s.23 (9.7); no infirmity in the AC's order, petition dismissed (9.11, 9.24, 10.1(i)); per RBANMS Educational
# Institution v. B. Gunashekar (2025 INSC 490), the matter referred to the Chief Commissioner, Income Tax; the Registrar (Judicial) to
# forward a copy of the entire file, Chief Commissioner, Income Tax, Karnataka (10.1(ii)-(iii)). The bench card uses the official portrait.
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen, as tej)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
STING = {"kicker": "ಕರ್ನಾಟಕ ಹೈಕೋರ್ಟ್ · ತೀರ್ಪು ವಿವರಣೆ", "title": "ಷರತ್ತಿಲ್ಲದ ರಿಲೀಸ್ ಡೀಡ್, ಸೆಕ್ಷನ್ 23", "sub": "Drakshayini v. Assistant Commissioner, Shimoga · 2026:KHC:58865"}
ENDCARD = {"title": "ಪೋಷಣೆಯ ಷರತ್ತು ಇಲ್ಲದ ರಿಲೀಸ್ ಡೀಡ್ ಮತ್ತು ಸೆಕ್ಷನ್ 23", "line": "ಷರತ್ತು ಡೀಡ್‌ನಲ್ಲಿ ಇರಲೇಬೇಕಿಲ್ಲ: ನೋಡಿಕೊಳ್ಳುವ ತಿಳಿವಳಿಕೆಯನ್ನು ಪರಿಶೀಲಿಸಬೇಕು", "sub": "LawWorld: ವಕೀಲರಿಗಾಗಿ ಕಾನೂನು ಸಂಶೋಧನೆ"}

# ── 1 · ಷರತ್ತು ಬೇಕೇ? ───────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "ರಿಲೀಸ್"), text="ಪೋಷಣೆಯ ಷರತ್ತೇ ಇಲ್ಲದ ರಿಲೀಸ್ ಡೀಡ್: ಸೆಕ್ಷನ್ 23ರಡಿ ರದ್ದು ಸಾಧ್ಯವೇ?", hl="ರದ್ದು ಸಾಧ್ಯವೇ?")
cue(type="bench", t0=S("c02"), t1=E("c02") + 0.05, tag="ಕರ್ನಾಟಕ ಹೈಕೋರ್ಟ್ · 14 ಅಕ್ಟೋಬರ್ 2026",
    judges=[{"name": "Justice Suraj Govindaraj", "photo": "../brand/judges/suraj_govindaraj.jpg", "at": A("c02", "ಗೌರವಾನ್ವಿತ")}])

# ── 2 · ರಿಲೀಸ್ ಡೀಡ್ ──────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=A("c03", "ಭದ್ರಾವತಿ"), t1=E("c04") + 0.05, at=A("c03", "ಭದ್ರಾವತಿ"), tag="ಕರ್ನಾಟಕ ಹೈಕೋರ್ಟ್ · 14.10.2026",
    cases=[{"name": "Smt. Drakshayini @ Girija v. Assistant Commissioner, Shimoga", "cite": "2026:KHC:58865 · W.P. No. 34895 of 2025"}])
cue(type="flow", t0=S("c03"), t1=E("c03") + 0.05, head="ರಿಲೀಸ್ ಡೀಡ್", head_at=S("c03") + 0.05,
    steps=[{"label": "ತಂದೆ, ಸುಮಾರು 74 ವರ್ಷ", "sub": "ಭದ್ರಾವತಿ ತಾಲ್ಲೂಕು", "icon": "user", "at": A("c03", "ತಂದೆ")},
           {"label": "ಜಮೀನಿನ ಎಲ್ಲ ಹಕ್ಕು ಮಗಳಿಗೆ", "sub": "ಸರ್ವೆ ನಂ. 42 · 1 ಎಕರೆ 30 ಗುಂಟೆ", "icon": "landmark", "at": A("c03", "ಜಮೀನಿನ")},
           {"label": "ನೋಂದಾಯಿತ ರಿಲೀಸ್ ಡೀಡ್", "sub": "9 ಜನವರಿ 2025", "icon": "file-text", "at": A("c03", "ನೋಂದಾಯಿತ")}])
cue(type="timeline", t0=S("c04"), t1=E("c04") + 0.05,
    nodes=[{"label": "ರಿಲೀಸ್ ಡೀಡ್", "value": "9 ಜನವರಿ 2025", "sub": "ಮಗಳ ಪರವಾಗಿ", "at": A("c04", "ನಂತರ")},
           {"label": "ತಂದೆಯ ಅರ್ಜಿ", "value": "ಸೆಕ್ಷನ್ 23", "sub": "ಹಿರಿಯ ನಾಗರಿಕರ ಕಾಯ್ದೆ, 2007", "at": A("c04", "ಅರ್ಜಿ")},
           {"label": "ಡೀಡ್ ರದ್ದು", "value": "8 ಸೆಪ್ಟೆಂಬರ್ 2025", "sub": "ಸಹಾಯಕ ಆಯುಕ್ತರು, ಶಿವಮೊಗ್ಗ ಉಪವಿಭಾಗ · ತಿದ್ದುಪಡಿ 6.10.2025", "at": A("c04", "ಸೆಪ್ಟೆಂಬರ್")}])

# ── 3 · ಹೈಕೋರ್ಟ್‌ನಲ್ಲಿ ─────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c05"), t1=E("c05") + 0.05, head="ಮಗಳು ಮತ್ತು ಅಳಿಯನ ವಾದ", head_at=S("c05") + 0.05,
    steps=[{"label": "ರಿಟ್ ಅರ್ಜಿ", "sub": "ಸಹಾಯಕ ಆಯುಕ್ತರ ಆದೇಶದ ವಿರುದ್ಧ", "icon": "file-text", "at": A("c05", "ರಿಟ್")},
           {"label": "₹17.25 ಲಕ್ಷದ ಮಾರಾಟ ಒಪ್ಪಂದ", "sub": "31.07.2023 · ರಸೀದಿ 01.08.2023", "icon": "file-text", "at": A("c05", "ಮಾರಾಟ")},
           {"label": "ಡೀಡ್‌ನಲ್ಲಿ ಪೋಷಣೆಯ ಷರತ್ತಿಲ್ಲ", "sub": "ಹಾಗಾಗಿ ಸೆಕ್ಷನ್ 23 ಅನ್ವಯಿಸದು ಎಂಬ ವಾದ", "icon": "x", "at": A("c05", "ಷರತ್ತೇ")}])
cue(type="list", t0=S("c06"), t1=A("c06", "ಪೋಷಣೆಯ") - 0.05, head="ತಂದೆಯ ವಾದ", head_at=S("c06") + 0.05,
    items=[{"n": 1, "text": "ವೃದ್ಧಾಪ್ಯದಲ್ಲಿ ಮಗಳು ನೋಡಿಕೊಳ್ಳುವ ತಿಳಿವಳಿಕೆಯ ಮೇಲೆ ವರ್ಗಾವಣೆ", "at": A("c06", "ವೃದ್ಧಾಪ್ಯದಲ್ಲಿ")},
           {"n": 2, "text": "ಯಾವುದೇ ಹಣ ಸಿಕ್ಕಿಲ್ಲ; ಒಪ್ಪಂದ, ರಸೀದಿ ವಿವಾದಿತ", "at": A("c06", "ಸಿಕ್ಕಿಲ್ಲ")}])
cue(type="question", t0=A("c06", "ಪೋಷಣೆಯ"), t1=E("c06") + 0.05, at=A("c06", "ಷರತ್ತು"), text="ಸೆಕ್ಷನ್ 23ಕ್ಕೆ ಪೋಷಣೆಯ ಷರತ್ತು ಡೀಡ್‌ನಲ್ಲಿ ಇರಲೇಬೇಕೇ?", hl="ಇರಲೇಬೇಕೇ?")

# ── 4 · ಹೈಕೋರ್ಟ್ ತೀರ್ಮಾನ ──────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c07"), t1=E("c07") + 0.05, at=A("c07", "ಹೈಕೋರ್ಟ್"), act="ಹಿರಿಯ ನಾಗರಿಕರ ಕಾಯ್ದೆ, 2007", num="23", title="ಷರತ್ತು ಇಲ್ಲದಿದ್ದರೂ ಅರ್ಜಿ ಪರಿಶೀಲನೆ",
    points=[{"text": "ಡೀಡ್‌ನಲ್ಲಿ ಸ್ಪಷ್ಟ ಷರತ್ತು ಕಡ್ಡಾಯ ಪೂರ್ವಷರತ್ತಲ್ಲ", "at": A("c07", "ಇರಲೇಬೇಕಿಲ್ಲ")},
            {"text": "ನೋಡಿಕೊಳ್ಳುವ ತಿಳಿವಳಿಕೆ ಅರ್ಜಿಯಲ್ಲಿ ನಿರ್ದಿಷ್ಟವಾಗಿ ಹೇಳಿರಬೇಕು", "at": A("c07", "ನಿರ್ದಿಷ್ಟವಾಗಿ")}],
    note={"text": "ಆಗ ಸಹಾಯಕ ಆಯುಕ್ತರು ಆ ಹೇಳಿಕೆಯನ್ನು ಪರಿಶೀಲಿಸಬೇಕು", "icon": "check", "at": A("c07", "ಸಹಾಯಕ")})
cue(type="cite", t0=A("c07", "ನೋಡಿಕೊಳ್ಳುವ"), t1=E("c07") + 0.05, at=A("c07", "ನೋಡಿಕೊಳ್ಳುವ"), tag="ಕರ್ನಾಟಕ ಹೈಕೋರ್ಟ್ · ಅನುಸರಿಸಿದ ತೀರ್ಪು",
    cases=[{"name": "Sri Venkataiah v. State of Karnataka", "cite": "W.P. No. 13313 of 2025"}])
cue(type="timeline", t0=S("c08"), t1=A("c08", "ಪ್ರಕಾರವೂ", d=-0.1),
    nodes=[{"label": "ರಸೀದಿ", "value": "1 ಆಗಸ್ಟ್ 2023", "sub": "ನಂತರದ ವಿಲ್ ಉಲ್ಲೇಖಿಸುತ್ತದೆ", "at": A("c08", "ರಸೀದಿ")},
           {"label": "ವಿಲ್", "value": "9 ಆಗಸ್ಟ್ 2023", "sub": "ರಸೀದಿಗಿಂತ ನಂತರದ ದಿನಾಂಕ", "at": A("c08", "ವಿಲ್")},
           {"label": "ಕೋರ್ಟ್", "value": "ಸಂಶಯಾಸ್ಪದ", "sub": "ರಸೀದಿಯನ್ನು ಅವಲಂಬಿಸಲಾಗದು", "tone": "stop", "at": A("c08", "ಸಂಶಯಾಸ್ಪದ")}])
cue(type="point", t0=A("c08", "ಪ್ರಕಾರವೂ", d=-0.1), t1=E("c08") + 0.05, text="ರಸೀದಿಯ ಪ್ರಕಾರವೂ ಹಣ ಸಹೋದರರಿಗೆ, ತಂದೆಗಲ್ಲ: ಸೆಕ್ಷನ್ 23ರಿಂದ ಹೊರಗಿಡದು", icon="x", accent=True, at=A("c08", "ಹಣ"))

# ── 5 · ಆದೇಶ ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c09"), t1=E("c09") + 0.05, head="ಆದೇಶ", head_at=S("c09") + 0.05,
    steps=[{"label": "ರಿಟ್ ಅರ್ಜಿ ವಜಾ", "sub": "ಸಹಾಯಕ ಆಯುಕ್ತರ ಆದೇಶದಲ್ಲಿ ದೋಷವಿಲ್ಲ", "icon": "check", "tone": "ok", "at": A("c09", "ವಜಾಗೊಳಿಸಿತು")},
           {"label": "ದೊಡ್ಡ ಮೊತ್ತದ ನಗದು ಪಾವತಿಯ ವಾದ", "sub": "₹17.25 ಲಕ್ಷ ನಗದು ಪಾವತಿಸಿದ್ದಾಗಿ ಹೇಳಿಕೆ", "icon": "search", "at": A("c09", "ನಗದು")},
           {"label": "ಕಡತದ ಪ್ರತಿ ಆದಾಯ ತೆರಿಗೆ ಇಲಾಖೆಗೆ", "sub": "ಮುಖ್ಯ ಆಯುಕ್ತರು, ಆದಾಯ ತೆರಿಗೆ, ಕರ್ನಾಟಕ", "icon": "arrow-right", "at": A("c09", "ಆದಾಯ")}])
cue(type="cite", t0=A("c09", "ಸುಪ್ರೀಂ"), t1=E("c09") + 0.05, at=A("c09", "ಸುಪ್ರೀಂ"), tag="ಸುಪ್ರೀಂ ಕೋರ್ಟ್ · ನಗದು ಪಾವತಿಯ ಹೇಳಿಕೆ: ಐಟಿ ಇಲಾಖೆಗೆ ಉಲ್ಲೇಖ",
    cases=[{"name": "RBANMS Educational Institution v. B. Gunashekar", "cite": "2025 INSC 490"}])
cue(type="point", t0=S("c10"), t1=E("c10") + 0.05, text="Like · Share · Subscribe · lawworld.ai", icon="check", accent=True, at=A("c10", "ಲೈಕ್"))
