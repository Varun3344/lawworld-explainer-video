# Sri Ramanjalu v. State of Karnataka & Anr., Criminal Petition No. 3658 of 2022 (High Court of Karnataka at Bengaluru, M. Nagaprasanna
# J.; reserved 11.08.2026, CAV order pronounced 16.10.2026, REPORTABLE list): panel cues, run by split/build_course_plan.py (helpers: at S
# E cue fx have r3 PEND). KANNADA concept format (as krm); every anchor is a whole word of that clip's spoken Kannada.
# Facts from the judgment (paras): s.482 CrPC petition to quash C.C. No. 50442 of 2022 (XXIX Addl. CMM, Mayo Hall, Bengaluru) arising
# from Crime No. 245 of 2021, HAL P.S., IPC 279, 307, 353, 427, 506 (prayer, 1); the complainant, a Head Constable of the HAL Airport
# Traffic P.S., on special duty to detect drunken driving on the night of 23.10.2021; complaint 24.10.2021; the petitioner, driving a
# car, allegedly tried to evade the checking by speeding away and, when the complainant tried to intercept, drove so that it ran over
# him; the Department's drunken-driving detection machine damaged (3.1, 7); spot mahazar 25.10.2021 on the public road opposite
# Vimanapura Post Office (3.2); charge sheet; cognizance 01.02.2022 (3.2); petitioner: no intention or knowledge for s.307, no grievous
# injury (4.1-4.2); wound certificate: a displaced fracture of the head of the fibula, medically grievous; discharge summary (8, 12.3);
# s.307: the gravamen is intention or knowledge, not the magnitude of the injury; neither a fatal injury nor grievous hurt is an
# indispensable prerequisite (12); Surender Kumar v. State of Haryana, 2026 SCC OnLine SC 1912 (12.1); Abhishek v. State of Rajasthan,
# 2026 SCC OnLine SC 2079 (12.2); a motor vehicle so driven towards a human being is capable of becoming an instrument of death; survival
# cannot by itself dilute the gravity of the act alleged (12.4); intention or knowledge may prima facie be inferred from the cumulative
# circumstances (12.5); prima facie case on all five offences (11.2, 12.6, 13.3, 14.1, 15.2, 20); truth from the crucible of trial (19);
# petition rejected (21); observations confined to s.482, not findings on guilt; the trial court to proceed independently (after 21).
# Every act is shown as an allegation; no injury detail beyond the fracture the Court relied on. The bench card uses the official portrait.
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen, as tej)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
STING = {"kicker": "ಕರ್ನಾಟಕ ಹೈಕೋರ್ಟ್ · ತೀರ್ಪು ವಿವರಣೆ", "title": "ಸೆಕ್ಷನ್ 307: ಗಾಯವಲ್ಲ, ಉದ್ದೇಶ ಮುಖ್ಯ", "sub": "Sri Ramanjalu v. State of Karnataka · Crl.P. No. 3658 of 2022"}
ENDCARD = {"title": "ಸೆಕ್ಷನ್ 307: ಗಾಯವಲ್ಲ, ಉದ್ದೇಶ ಮುಖ್ಯ", "line": "ಬದುಕುಳಿದದ್ದೇ ಆರೋಪ ತಗ್ಗಿಸದು: ಸತ್ಯ ವಿಚಾರಣೆಯಲ್ಲೇ ಹೊರಬರಬೇಕು", "sub": "LawWorld: ವಕೀಲರಿಗಾಗಿ ಕಾನೂನು ಸಂಶೋಧನೆ"}

# ── 1 · ಬದುಕುಳಿದರೆ? ─────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "ವ್ಯಕ್ತಿಯ"), text="ಕಾರು ಹತ್ತಿಸಿದ ಆರೋಪ, ವ್ಯಕ್ತಿ ಬದುಕುಳಿದರು: ಸೆಕ್ಷನ್ 307ರ ಪ್ರಕರಣ ರದ್ದಾಗುತ್ತದೆಯೇ?", hl="ಪ್ರಕರಣ ರದ್ದಾಗುತ್ತದೆಯೇ?")
cue(type="bench", t0=S("c02"), t1=E("c02") + 0.05, tag="ಕರ್ನಾಟಕ ಹೈಕೋರ್ಟ್ · 16 ಅಕ್ಟೋಬರ್ 2026",
    judges=[{"name": "Justice M. Nagaprasanna", "photo": "../brand/judges/m_nagaprasanna.jpg", "at": A("c02", "ಗೌರವಾನ್ವಿತ")}])

# ── 2 · ಆರೋಪಿತ ಘಟನೆ ─────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=A("c03", "ರಾತ್ರಿ"), t1=E("c04") + 0.05, at=A("c03", "ರಾತ್ರಿ"), tag="ಕರ್ನಾಟಕ ಹೈಕೋರ್ಟ್ · 16.10.2026",
    cases=[{"name": "Sri Ramanjalu v. State of Karnataka", "cite": "Crl.P. No. 3658 of 2022 · C.C. No. 50442 of 2022"}])
cue(type="flow", t0=S("c03"), t1=E("c03") + 0.05, head="ಘಟನೆ, ದೂರಿನ ಪ್ರಕಾರ", head_at=S("c03") + 0.05,
    steps=[{"label": "23 ಅಕ್ಟೋಬರ್ 2021, ರಾತ್ರಿ", "sub": "ವಿಮಾನಪುರ ಅಂಚೆ ಕಚೇರಿ ಎದುರಿನ ರಸ್ತೆ, ಬೆಂಗಳೂರು", "icon": "calendar", "at": A("c03", "ರಾತ್ರಿ")},
           {"label": "ಹೆಡ್ ಕಾನ್ಸ್‌ಟೇಬಲ್ · ದೂರುದಾರ", "sub": "ಎಚ್‌ಎಎಲ್ ಏರ್‌ಪೋರ್ಟ್ ಸಂಚಾರ ಪೊಲೀಸ್ ಠಾಣೆ", "icon": "user", "at": A("c03", "ಸಂಚಾರ")},
           {"label": "ಮದ್ಯಪಾನ ಚಾಲನೆ ತಪಾಸಣೆ", "sub": "ವಿಶೇಷ ಕರ್ತವ್ಯ", "icon": "search", "at": A("c03", "ಮದ್ಯಪಾನ")}])
cue(type="flow", t0=S("c04"), t1=E("c04") + 0.05, head="ಆರೋಪದ ಪ್ರಕಾರ", head_at=S("c04") + 0.05,
    steps=[{"label": "ತಪಾಸಣೆ ತಪ್ಪಿಸಲು ಯತ್ನ", "sub": "ಆರೋಪಿ ಕಾರು ಚಲಾಯಿಸುತ್ತಿದ್ದರು", "icon": "arrow-right", "at": A("c04", "ತಪಾಸಣೆ")},
           {"label": "ತಡೆಯಲು ಬಂದ ದೂರುದಾರರ ಮೇಲೆ ಕಾರು", "sub": "ಕರ್ತವ್ಯ ನಿರತ ಪೊಲೀಸ್", "icon": "x", "tone": "stop", "at": A("c04", "ದೂರುದಾರರ")},
           {"label": "ಮದ್ಯ ತಪಾಸಣಾ ಯಂತ್ರಕ್ಕೆ ಹಾನಿ", "sub": "ಇಲಾಖೆಯ ಯಂತ್ರ", "icon": "file-text", "at": A("c04", "ಮದ್ಯ")}])

# ── 3 · ಪ್ರಕರಣ ಹೈಕೋರ್ಟ್‌ಗೆ ─────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="timeline", t0=S("c05"), t1=E("c05") + 0.05,
    nodes=[{"label": "ದೂರು", "value": "24 ಅಕ್ಟೋಬರ್ 2021", "sub": "ಅಪರಾಧ ಸಂಖ್ಯೆ 245/2021 · ಎಚ್‌ಎಎಲ್ ಠಾಣೆ", "at": A("c05", "ದೂರು")},
           {"label": "ಚಾರ್ಜ್‌ಶೀಟ್", "value": "ತನಿಖೆಯ ನಂತರ", "sub": "ಆರೋಪಿಯ ವಿರುದ್ಧ", "at": A("c05", "ಚಾರ್ಜ್‌ಶೀಟ್")},
           {"label": "ಸಂಜ್ಞಾನ", "value": "1 ಫೆಬ್ರವರಿ 2022", "sub": "ಐಪಿಸಿ 279, 307, 353, 427, 506 · ಸಿ.ಸಿ. 50442/2022", "at": A("c05", "ಸಂಜ್ಞಾನ")}])
cue(type="list", t0=S("c06"), t1=E("c06") + 0.05, head="ಆರೋಪಿಯ ವಾದ · ಸೆಕ್ಷನ್ 482 ಸಿಆರ್‌ಪಿಸಿ", head_at=S("c06") + 0.05,
    items=[{"n": 1, "text": "ಸೆಕ್ಷನ್ 307ಕ್ಕೆ ಬೇಕಾದ ಉದ್ದೇಶ ಅಥವಾ ಅರಿವು ಇಲ್ಲ", "at": A("c06", "ಉದ್ದೇಶ")},
           {"n": 2, "text": "ಗಂಭೀರ ಗಾಯವಾಗಿಲ್ಲ", "at": A("c06", "ಗಂಭೀರ")}])

# ── 4 · ಹೈಕೋರ್ಟ್ ತೀರ್ಮಾನ ──────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c07"), t1=E("c07") + 0.05, at=A("c07", "ಹೈಕೋರ್ಟ್"), act="ಐಪಿಸಿ", num="307", title="ಕೊಲೆ ಯತ್ನ",
    points=[{"text": "ಮುಖ್ಯ: ಉದ್ದೇಶ ಅಥವಾ ಅರಿವು, ಗಾಯದ ಪ್ರಮಾಣವಲ್ಲ", "at": A("c07", "ಉದ್ದೇಶ")},
            {"text": "ಮಾರಣಾಂತಿಕ ಅಥವಾ ಗಂಭೀರ ಗಾಯ ಅನಿವಾರ್ಯವಲ್ಲ", "at": A("c07", "ಮಾರಣಾಂತಿಕ")}],
    note={"text": "ಇಲ್ಲಿ: ವೈದ್ಯಕೀಯ ದಾಖಲೆಯಲ್ಲಿ ಮೂಳೆ ಮುರಿತ (ಗಂಭೀರ ಗಾಯ)", "icon": "file-text", "at": A("c07", "ಮೂಳೆ")})
cue(type="cite", t0=A("c07", "ಮಾರಣಾಂತಿಕ"), t1=E("c07") + 0.05, at=A("c07", "ಮಾರಣಾಂತಿಕ"), tag="ಸುಪ್ರೀಂ ಕೋರ್ಟ್ · ಅನುಸರಿಸಿದ ತೀರ್ಪುಗಳು",
    cases=[{"name": "Surender Kumar v. State of Haryana", "cite": "2026 SCC OnLine SC 1912"},
           {"name": "Abhishek v. State of Rajasthan", "cite": "2026 SCC OnLine SC 2079"}])
cue(type="point", t0=S("c08"), t1=A("c08", "ದೂರುದಾರ") - 0.05, text="ವ್ಯಕ್ತಿಯತ್ತ ನುಗ್ಗಿಸಿದ ವಾಹನ “ಸಾವಿನ ಸಾಧನ” ಆಗಬಹುದು", icon="scale", accent=True, at=A("c08", "ವಾಹನ"))
cue(type="notequal", t0=A("c08", "ದೂರುದಾರ"), t1=E("c08") + 0.05, left="ಬದುಕುಳಿದರು", right="ಆರೋಪ ಹಗುರ",
    at=A("c08", "ಬದುಕುಳಿದದ್ದೇ"), left_at=A("c08", "ಬದುಕುಳಿದದ್ದೇ"), sub="ಉದ್ದೇಶ ಅಥವಾ ಅರಿವು: ಒಟ್ಟು ಸಂದರ್ಭಗಳಿಂದ ಮೇಲ್ನೋಟಕ್ಕೆ", sub_at=A("c08", "ಉದ್ದೇಶ"))

# ── 5 · ಫಲಿತಾಂಶ ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="verdicts", t0=S("c09"), t1=A("c09", "ಅಭಿಪ್ರಾಯಗಳು", d=-0.35),
    rows=[{"text": "ಐದೂ ಆರೋಪಗಳಿಗೆ ಮೇಲ್ನೋಟದ ಆಧಾರ", "ok": True, "at": A("c09", "ಆರೋಪಗಳಿಗೆ")},
          {"text": "ಸತ್ಯ ವಿಚಾರಣೆಯಲ್ಲೇ ಹೊರಬರಬೇಕು", "ok": True, "at": A("c09", "ಸತ್ಯ")},
          {"text": "ಸೆಕ್ಷನ್ 482 ರದ್ದತಿ ಅರ್ಜಿ", "ok": False, "at": A("c09", "ಹೈಕೋರ್ಟ್"), "strike_at": A("c09", "ತಿರಸ್ಕರಿಸಿತು")}])
cue(type="point", t0=A("c09", "ಅಭಿಪ್ರಾಯಗಳು", d=-0.3), t1=E("c09") + 0.05, text="ಈ ಅಭಿಪ್ರಾಯಗಳು ದೋಷ-ನಿರ್ದೋಷದ ಕುರಿತ ತೀರ್ಮಾನವಲ್ಲ: ವಿಚಾರಣಾ ಕೋರ್ಟ್ ಸ್ವತಂತ್ರವಾಗಿ ಮುಂದುವರಿಯಬೇಕು", icon="info", at=A("c09", "ಅಭಿಪ್ರಾಯಗಳು"))
cue(type="point", t0=S("c10"), t1=E("c10") + 0.05, text="Like · Share · Subscribe · lawworld.ai", icon="check", accent=True, at=A("c10", "ಲೈಕ್"))
