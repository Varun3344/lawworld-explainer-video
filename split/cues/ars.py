# Arrest Safeguards under the BNSS - CONCEPT VIDEO (legal-concept explainer, Cause of Action build): panel cues, run by
# split/build_course_plan.py (helpers: at S E cue fx have r3 PEND). Storyboard: ~/Downloads/01_Arrest_Safeguards_LawWorld_v2.pdf.
# Citations are the LawWorld Citation IDs the storyboard uses; no other reporter appears on screen (the PDF's own rule).
# Held to the PDF's "Points to preserve": the writing requirement and the two-hour rule are the Supreme Court's ruling under
# Article 22(1) read with s.47, not the bare statute; the two hours sit INSIDE the 24-hour ceiling and never extend it; the
# oral-first route is exceptional only; the s.35(1)(b) necessity test is tied to the up-to-seven-year cognizable category;
# arrest does not establish guilt. Scene 1 shows FIR / investigation / arrest as three SEPARATE cards - never a line from
# FIR to handcuffs. The arrest memorandum is kept visually distinct from the grounds-of-arrest document.
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

STING = {"kicker": "CRIMINAL PROCEDURE · BNSS EXPLAINED", "title": "Arrest Safeguards under the BNSS",
         "sub": "Police notices, legal assistance and production before a Magistrate"}
ENDCARD = {"title": "Arrest Safeguards under the BNSS", "line": "Notice · written grounds · intimation · counsel · twenty four hours",
           "sub": "LawWorld: legal research for advocates"}

# ── 1 · an accusation and an arrest ──────────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=A("c01", "accused") - 0.05, at=A("c01", "customer"),
    text="A customer accuses Ravi of cheating.", hl="accuses Ravi")
cue(type="flow", t0=A("c01", "accused"), t1=E("c01") + 0.05, head="Three separate things", head_at=A("c01", "accused"),
    steps=[{"label": "An FIR is registered", "sub": "information recorded", "icon": "file-text", "at": A("c01", "accused")},
           {"label": "An investigation follows", "sub": "evidence is gathered", "icon": "search", "at": A("c01", "cheating")},
           {"label": "An arrest — only if justified", "sub": "not an automatic next step", "icon": "alert-triangle", "tone": "warn", "at": A("c01", "registered")}])
cue(type="question", t0=S("c02"), t1=A("c02", "justified") - 0.05, at=A("c02", "police"),
    text="Must the police now arrest him?", hl="Must the police")
cue(type="cite", t0=A("c02", "under"), t1=A("c02", "justified") - 0.05, at=A("c02", "under"), tag="SUPREME COURT OF INDIA · 25.04.1994",
    cases=[{"name": "Joginder Kumar v. State of U.P.", "cite": "LAWWORLD 1994 SC 0431"}])
cue(type="point", t0=A("c02", "justified"), t1=E("c02") + 0.05, text="Arrest must be justified, never a reflex",
    icon="scale", accent=True, at=A("c02", "justified"))
cue(type="flow", t0=S("c03"), t1=E("c03") + 0.05, head="Ravi's road through the BNSS", head_at=S("c03") + 0.05,
    steps=[{"label": "A police notice", "sub": "BNSS 35(3)", "icon": "file-text", "at": A("c03", "notice")},
           {"label": "A possible arrest", "sub": "only where necessity is recorded", "icon": "user", "at": A("c03", "arrest")},
           {"label": "Before a Magistrate", "sub": "production and remand", "icon": "landmark", "at": A("c03", "magistrate")}])
cue(type="point", t0=S("c04"), t1=E("c04") + 0.05, text="A safeguard at every step", icon="shield", accent=True, at=A("c04", "safeguards"))

# ── 2 · when arrest is necessary ─────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c05"), t1=E("c05") + 0.05, at=A("c05", "section"), act="BNSS, 2023", num="35(1)(b)",
    title="Arrest without a warrant",
    points=[{"text": "A cognizable offence", "at": A("c05", "cognizable")},
            {"text": "Punishable up to seven years", "at": A("c05", "seven")},
            {"text": "Clause (b) of sub-section (1) applies", "at": A("c05", "clause")}])
cue(type="list", t0=S("c06"), t1=E("c06") + 0.05, head="What the officer must have", head_at=S("c06") + 0.05,
    items=[{"n": 1, "text": "A reason to believe he committed the offence", "at": A("c06", "reason")},
           {"n": 2, "text": "A recorded satisfaction that arrest is necessary", "at": A("c06", "recorded")}])
cue(type="list", t0=S("c07"), t1=E("c07") + 0.05, head="“Necessary” can mean", head_at=S("c07") + 0.05,
    items=[{"n": 1, "text": "Protecting the evidence", "at": A("c07", "evidence")},
           {"n": 2, "text": "Securing his presence in court", "at": A("c07", "presence")},
           {"n": "!", "text": "Reasons are recorded either way — arresting or not", "at": A("c07", "reasons")}])
cue(type="cite", t0=S("c08"), t1=E("c08") + 0.05, at=A("c08", "arnesh"), tag="SUPREME COURT OF INDIA",
    cases=[{"name": "Arnesh Kumar v. State of Bihar", "cite": "LAWWORLD 2014 SC 0719 · 02.07.2014"},
           {"name": "Satender Kumar Antil v. CBI", "cite": "LAWWORLD 2022 SC 0738 · 11.07.2022"}])

# ── 3 · the notice to appear ─────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c09"), t1=E("c09") + 0.05, at=A("c09", "required"), act="BNSS, 2023", num="35(3)",
    title="The notice to appear",
    points=[{"text": "Issued where arrest is not required", "at": A("c09", "required")},
            {"text": "In writing, directing him to appear", "at": A("c09", "notice")}])
cue(type="list", t0=S("c10"), t1=E("c10") + 0.05, head="What Ravi should do", head_at=S("c10") + 0.05,
    items=[{"n": 1, "text": "Comply with the notice", "at": A("c10", "comply")},
           {"n": 2, "text": "Keep a record of each attendance", "at": A("c10", "record")}])
cue(type="flow", t0=S("c11"), t1=E("c11") + 0.05, head="While he complies", head_at=S("c11") + 0.05,
    steps=[{"label": "He cannot be arrested for that offence", "sub": "BNSS 35(5)", "icon": "check", "tone": "ok", "at": A("c11", "complies")},
           {"label": "Unless the officer records reasons", "sub": "why arrest is nevertheless necessary", "icon": "alert-triangle", "tone": "warn", "at": A("c11", "unless")}])
cue(type="point", t0=S("c12"), t1=A("c12", "neither") - 0.05, text="The protection is conditional — ignore it and the police may arrest",
    icon="alert-triangle", accent=True, at=A("c12", "conditional"))
cue(type="notequal", t0=A("c12", "neither"), t1=E("c12") + 0.05, left="A notice", right="innocence or immunity",
    at=A("c12", "neither"), left_at=A("c12", "neither"),
    sub="Neither a finding of guilt nor permanent immunity", sub_at=A("c12", "immunity"))

# ── 4 · knowing the grounds ──────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c13"), t1=E("c13") + 0.05, at=A("c13", "article"), act="CONSTITUTION + BNSS", num="22(1) · 47",
    title="He must be told the grounds",
    points=[{"text": "Article 22(1): a constitutional guarantee", "at": A("c13", "article")},
            {"text": "BNSS 47: the grounds of arrest", "at": A("c13", "grounds")}])
cue(type="cite", t0=S("c14"), t1=E("c16") + 0.05, at=A("c14", "mihir"), tag="SUPREME COURT OF INDIA · 06.11.2025",
    cases=[{"name": "Mihir Rajesh Shah v. State of Maharashtra", "cite": "LAWWORLD 2025 SC 1125, paras 52 and 56"}])
cue(type="list", t0=A("c14", "held"), t1=E("c14") + 0.05, head="The Court's rule", head_at=A("c14", "held"),
    items=[{"n": 1, "text": "In writing", "at": A("c14", "writing")},
           {"n": 2, "text": "In a language he understands", "at": A("c14", "language")},
           {"n": 3, "text": "For every offence, under all statutes", "at": A("c14", "every")}])
cue(type="point", t0=S("c15"), t1=E("c15") + 0.05, text="Orally first: exceptional circumstances only",
    icon="alert-triangle", accent=True, at=A("c15", "impractical"))
cue(type="point", t0=S("c16"), t1=E("c16") + 0.05, text="Written copy: at least two hours before production for remand",
    icon="clock", accent=True, at=A("c16", "hours"))

# ── 5 · recording the arrest ─────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c17"), t1=E("c17") + 0.05, at=A("c17", "section"), act="BNSS, 2023", num="36",
    title="Identification and the arrest memorandum",
    points=[{"text": "The officer carries clear identification", "at": A("c17", "identification")},
            {"text": "An arrest memorandum is prepared", "at": A("c17", "memorandum")}])
cue(type="list", t0=S("c18"), t1=E("c18") + 0.05, head="The memorandum", head_at=S("c18") + 0.05,
    items=[{"n": 1, "text": "Attested by a family member or respectable local person", "at": A("c18", "attested")},
           {"n": 2, "text": "Countersigned by the arrested person", "at": A("c18", "countersigned")}])
cue(type="section", t0=S("c19"), t1=E("c19") + 0.05, at=A("c19", "section"), act="BNSS, 2023", num="48",
    title="Someone he names is told",
    points=[{"text": "A relative, a friend, or a person he nominates", "at": A("c19", "relative")},
            {"text": "Told of the arrest and the place of detention", "at": A("c19", "detention")}])
cue(type="point", t0=S("c20"), t1=A("c20", "directed") - 0.05, text="Recorded at the police station",
    icon="file-check", accent=True, at=A("c20", "recorded"))
cue(type="cite", t0=A("c20", "directed"), t1=E("c20") + 0.05, at=A("c20", "directed"), tag="SUPREME COURT OF INDIA · 18.12.1996",
    cases=[{"name": "D.K. Basu v. State of West Bengal", "cite": "LAWWORLD 1996 SC 1287"}])

# ── 6 · access to a lawyer ───────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c21"), t1=E("c21") + 0.05, at=A("c21", "section"), act="BNSS, 2023", num="38",
    title="Meeting an advocate",
    points=[{"text": "An advocate of his choice, during interrogation", "at": A("c21", "advocate")}],
    note={"text": "During — not throughout — the interrogation", "icon": "info", "at": A("c21", "throughout")})
cue(type="section", t0=S("c22"), t1=E("c22") + 0.05, at=A("c22", "section"), act="BNSS, 2023", num="47(2)",
    title="Bailable offences",
    points=[{"text": "The police must tell him he is entitled to bail", "at": A("c22", "bailable")}])
cue(type="point", t0=S("c23"), t1=E("c23") + 0.05, text="Neither right ends the investigation — both keep it lawful",
    icon="scale", accent=True, at=A("c23", "neither"))
cue(type="point", t0=S("c24"), t1=E("c24") + 0.05, text="Written grounds give counsel time to oppose remand",
    icon="clock", accent=True, at=A("c24", "lawyer"))

# ── 7 · health and special safeguards ────────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c25"), t1=E("c25") + 0.05, at=A("c25", "section"), act="BNSS, 2023", num="56",
    title="Health and safety in custody",
    points=[{"text": "Reasonable care of the arrested person's health", "at": A("c25", "health")}])
cue(type="section", t0=S("c26"), t1=E("c27") + 0.05, at=A("c26", "section"), act="BNSS, 2023", num="43(5)",
    title="Arrest of a woman at night",
    points=[{"text": "Not after sunset and before sunrise", "at": A("c26", "sunset")},
            {"text": "Exceptional circumstances only", "at": A("c26", "exceptional")},
            {"text": "On a woman officer's written report", "at": A("c27", "report")},
            {"text": "With a Judicial Magistrate of the first class's prior permission", "at": A("c27", "permission")}])
cue(type="section", t0=S("c28"), t1=E("c29") + 0.05, at=A("c28", "section"), act="BNSS, 2023", num="35(7)",
    title="Infirm, or above sixty",
    points=[{"text": "An infirm person, or one above sixty", "at": A("c28", "infirm")},
            {"text": "Permission of a Deputy Superintendent or above", "at": A("c28", "permission")},
            {"text": "Where the offence is punishable below three years", "at": A("c29", "applies")}])

# ── 8 · the twenty four hour limit ───────────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c30"), t1=E("c30") + 0.05, at=A("c30", "section"), act="BNSS, 2023", num="57",
    title="Production before a Magistrate",
    points=[{"text": "Without unnecessary delay", "at": A("c30", "delay")}])
cue(type="section", t0=S("c31"), t1=E("c31") + 0.05, at=A("c31", "section"), act="BNSS, 2023", num="58",
    title="The outer limit",
    points=[{"text": "Detention cannot exceed twenty four hours", "at": A("c31", "detention")},
            {"text": "Unless a Magistrate orders otherwise under s. 187", "at": A("c31", "order")}])
cue(type="flow", t0=S("c32"), t1=E("c32") + 0.05, head="Monday morning", head_at=S("c32") + 0.05,
    steps=[{"label": "Arrest", "sub": "the clock starts", "icon": "user", "at": A("c32", "monday")},
           {"label": "Necessary journey time", "sub": "excluded from the twenty four hours", "icon": "arrow-right", "at": A("c32", "journey")},
           {"label": "Not Wednesday", "sub": "the police cannot extend it on their own authority", "icon": "x", "tone": "stop", "at": A("c32", "wednesday")}])
cue(type="point", t0=S("c33"), t1=A("c33", "two") - 0.05, text="Twenty four hours is an outer limit, not a target",
    icon="alert-triangle", accent=True, at=A("c33", "outer"))
cue(type="point", t0=A("c33", "two"), t1=E("c33") + 0.05, text="The two-hour rule operates inside that ceiling",
    icon="clock", accent=True, at=A("c33", "two"))

# ── 9 · what the Magistrate examines ─────────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c34"), t1=E("c35") + 0.05, at=A("c34", "production"), act="BNSS, 2023", num="187",
    title="Further custody needs a lawful basis",
    points=[{"text": "The remand papers carry the grounds of arrest", "at": A("c35", "grounds")},
            {"text": "And explain any delay", "at": A("c35", "delay")}])
cue(type="list", t0=S("c36"), t1=E("c36") + 0.05, head="What counsel can point to", head_at=S("c36") + 0.05,
    items=[{"n": 1, "text": "The grounds of arrest", "at": A("c36", "grounds")},
           {"n": 2, "text": "The arrest memorandum", "at": A("c36", "memorandum")},
           {"n": 3, "text": "Intimation to the family", "at": A("c36", "intimation")},
           {"n": 4, "text": "Access to counsel", "at": A("c36", "counsel")},
           {"n": 5, "text": "His health in custody", "at": A("c36", "health")}])
cue(type="point", t0=S("c37"), t1=E("c37") + 0.05, text="No written grounds in time → the arrest and remand are illegal, and he is set free",
    icon="x", accent=True, at=A("c37", "illegal"))
cue(type="notequal", t0=S("c38"), t1=E("c38") + 0.05, left="A lawful arrest and remand", right="proof of guilt",
    at=A("c38", "guilt"), left_at=A("c38", "guilt"), sub="Guilt remains a question for the trial", sub_at=A("c38", "trial"))

# ── 10 · remember the sequence ───────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="list", t0=S("c39"), t1=E("c41") + 0.05, head="Remember the sequence", head_at=S("c39") + 0.05,
    items=[{"n": 1, "text": "Comply with a lawful notice, and keep proof", "at": A("c39", "comply")},
           {"n": 2, "text": "Ask for the written grounds, and note when they arrive", "at": A("c39", "ask")},
           {"n": 3, "text": "Name the person the police must inform", "at": A("c40", "name")},
           {"n": 4, "text": "Ask for your advocate", "at": A("c40", "advocate")},
           {"n": 5, "text": "Raise any health concern at once", "at": A("c40", "health")},
           {"n": 6, "text": "Keep copies of every document", "at": A("c41", "copies")}])
cue(type="point", t0=A("c41", "remember"), t1=E("c41") + 0.05, text="Arrest does not establish guilt",
    icon="scale", accent=True, at=A("c41", "remember"))
cue(type="point", t0=S("c42"), t1=E("c42") + 0.05, text="The safeguards keep the process fair while a court decides on the evidence",
    icon="shield", accent=True, at=A("c42", "fair"))
cue(type="point", t0=S("c43"), t1=E("c43") + 0.05, text="Like · Share · Subscribe · lawworld.ai",
    icon="check", accent=True, at=A("c43", "like"))
