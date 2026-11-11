# FIR, Zero FIR and e-FIR under the BNSS - CONCEPT VIDEO (legal-concept explainer, Cause of Action build): panel cues, run by
# split/build_course_plan.py (helpers: at S E cue fx have r3 PEND). No storyboard PDF: held to the `//` header of split/scripts/fir.txt
# (bare-act wording of BNSS 173 / 174 / 175(3) / 2(1)(i), BNS 217 / 248, BSA 148 / 160, case paragraphs, decisions). The running
# example was renamed Kavya -> Meera after drafting; the spoken text (and so every card) says Meera.
#  - a case is shown by name, court and year (+ the header's paragraph), never SCC / AIR / INSC; no LawWorld Citation ID is known
#    for any of them yet. Paragraphs the header marks unconfirmed (Satvinder Kaur, Thulia Kali, Gian Chand, Priyanka Srivastava)
#    are left off. Imran Pratapgadhi and Om Prakash Ambadkar are footers only (not named in the narration);
#  - Meera, Mysuru, Hubballi and the phone theft are labelled HYPOTHETICAL EXAMPLE (a kicker over every clip that tells her story);
#    c08 is an ASSUMPTION that her information discloses a cognizable offence - no "theft = cognizable" card, and her theft is
#    never placed inside or outside the 173(3) three-to-seven-year band;
#  - "Zero FIR" and "e-FIR" are popular names; the statute's words are "irrespective of the area where the offence is committed" and
#    "electronic communication". The Zero FIR's TRANSFER is "generally" done: s. 173 itself does not provide for it (c09 note);
#  - registration is not arrest and not proof of guilt: no accused, arrest, GUILTY or ARRESTED anywhere; c31 states it with ≠ rows;
#  - 173(3): police discretion, prior permission of an officer not below DSP rank, 14 days; Lalita Kumari's 7 days (old Code) are
#    not on screen, so the two are never mixed; Lalita Kumari's categories are illustrations ("limited cases");
#  - 173(4): in writing AND by post to the SP; the Magistrate route follows it ("failing which") and needs an affidavit (175(3));
#    the Magistrate MAY order investigation - no card promises it;
#  - non-cognizable information: entered in the book, informant referred; police need the Magistrate's order (never "refused");
#  - c35: false information "may be an offence"; a failed case is never shown as a lie ("the key word: knowingly").
# 07-11 layout lessons: a stamp after a question -> question y=215, stamp y=900; lists stay <= 3 rows under a citation bar; no
# compare card shares the screen with a two-case bar.
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

STING = {"kicker": "CRIMINAL PROCEDURE · BNSS EXPLAINED", "title": "FIR, Zero FIR and e-FIR",
         "sub": "Where and how to report a crime under the BNSS"}
ENDCARD = {"title": "FIR, Zero FIR and e-FIR", "line": "Report anywhere · take your free copy · not recorded? SP, then Magistrate",
           "sub": "LawWorld: legal research for advocates"}
HYPO = "HYPOTHETICAL EXAMPLE"
SC = "SUPREME COURT OF INDIA"

# ── 1 · where can you report a crime? ───────────────────────────────────────────────────────────────────────────────────────────
# the question and its stamp hold through "Hi, I'm Ravishankar from LawWorld" (the name tag sits on the presenter side)
cue(type="question", t0=S("c01"), t1=A("c02", "where") - 0.05, at=A("c01", "phone"),
    text="Phone stolen in another city: must you go back there to report it?", hl="go back there", y=215)
cue(type="stamp", t0=A("c01", "need") - 0.05, t1=A("c02", "where") - 0.05, at=A("c01", "need"), line1="NO NEED", line2="UNDER THE BNSS", y=900)
cue(type="list", t0=A("c02", "where") - 0.05, t1=E("c02") + 0.05, head="Three questions", head_at=A("c02", "where"),
    items=[{"n": 1, "text": "Where can an FIR be lodged?", "at": A("c02", "where") + 0.2},
           {"n": 2, "text": "How can the information be given?", "at": A("c02", "how")},
           {"n": 3, "text": "What if it is not recorded?", "at": A("c02", "what")}])
cue(type="cite", t0=A("c02", "bharatiya"), t1=E("c02") + 0.05, at=A("c02", "bharatiya"), tag="THE LAW",
    text="Bharatiya Nagarik Suraksha Sanhita, 2023 (BNSS)", icon="book-open")
cue(type="kicker", t0=S("c03"), t1=E("c03") + 0.05, at=S("c03") + 0.05, text=HYPO)
cue(type="flow", t0=S("c03"), t1=E("c03") + 0.05, head="Meera's phone", head_at=S("c03") + 0.05,
    steps=[{"label": "Meera", "sub": "a teacher from Mysuru", "icon": "user-round", "at": A("c03", "meera")},
           {"label": "Phone stolen", "sub": "at a bus stand", "icon": "smartphone", "at": A("c03", "stolen")},
           {"label": "In Hubballi", "sub": "another city", "icon": "map-pin", "tone": "ok", "at": A("c03", "hubballi")}])

# ── 2 · what an FIR is ───────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c04"), t1=E("c04") + 0.05, at=A("c04", "section"), act="BNSS, 2023", num="173(1)",
    title="Information in cognizable cases",
    points=[{"text": "Information relating to a cognizable offence", "at": A("c04", "information")},
            {"text": "Once recorded: commonly called the FIR", "at": A("c04", "commonly")}],
    note={"text": "Section 173 itself speaks of “information”", "icon": "info", "at": A("c04", "F")})
cue(type="checklist", t0=S("c05"), t1=E("c05") + 0.05, head="It may be given", head_at=S("c05") + 0.05,
    items=[{"n": 1, "text": "In writing", "at": A("c05", "writing")},
           {"n": 2, "text": "Orally", "at": A("c05", "orally")},
           {"n": 3, "text": "Electronically", "at": A("c05", "electronically")}])
cue(type="cite", t0=A("c05", "officer"), t1=E("c05") + 0.05, at=A("c05", "officer"), tag="BNSS 173(1)",
    text="To an officer in charge of a police station", icon="landmark")
cue(type="flow", t0=S("c06"), t1=E("c06") + 0.05, head="Oral information", head_at=S("c06") + 0.05,
    steps=[{"label": "Reduced to writing", "icon": "pen-line", "at": A("c06", "reduced")},
           {"label": "Read over to the informant", "icon": "message-square", "at": A("c06", "read")},
           {"label": "Signed", "sub": "by the person giving it", "icon": "signature", "tone": "ok", "at": A("c06", "signed")}])
cue(type="cite", t0=S("c06") + 0.3, t1=E("c06") + 0.05, at=S("c06") + 0.3, tag="BNSS 173(1)(i)",
    text="Given in writing or reduced to writing: signed by the person giving it", icon="book-open")

# ── 3 · Zero FIR: report anywhere ────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="quote", t0=S("c07"), t1=E("c07") + 0.05, at=A("c07", "notice"), reveal=r3(A("c07", "basis") - A("c07", "notice")),   # the words reveal at his pace
    text="Every information relating to the commission of a cognizable offence, irrespective of the area where the offence is "
         "committed, may be given orally or by electronic communication to an officer in charge of a police station",
    hl=["irrespective of the area where the offence is committed"],
    note={"text": "Zero FIR: the popular name for this rule", "at": A("c07", "zero")})
cue(type="cite", t0=S("c07") + 0.3, t1=E("c07") + 0.05, at=S("c07") + 0.3, tag="THE STATUTE'S WORDS",
    text="BNSS, 2023 · Section 173(1)", icon="book-open")
cue(type="kicker", t0=S("c08"), t1=E("c09") + 0.05, at=S("c08") + 0.05, text=HYPO)
cue(type="splitcard", t0=S("c08"), t1=E("c08") + 0.05,
    left={"title": "ASSUMED", "text": "Meera's information discloses a cognizable offence", "icon": "info", "at": A("c08", "assume")},
    right={"title": "IN MYSURU", "text": "she may report it at a police station there", "icon": "landmark", "at": A("c08", "report")})
cue(type="flow", t0=S("c09"), t1=E("c09") + 0.05, head="At the Mysuru station", head_at=S("c09") + 0.05,
    steps=[{"label": "Recorded there", "sub": "commonly called a Zero FIR", "icon": "file-check", "at": A("c09", "recorded")},
           {"label": "Generally transferred", "sub": "to the police station that has jurisdiction", "icon": "arrow-right", "tone": "ok",
            "at": A("c09", "generally")}],
    note={"text": "“Generally”: s. 173 itself does not provide for the transfer", "icon": "info", "at": A("c09", "jurisdiction")})
cue(type="point", t0=S("c10"), t1=A("c10", "police") - 0.05, text="Decided under the old Code of Criminal Procedure",
    icon="book-open", at=A("c10", "old"))
cue(type="notequal", t0=A("c10", "police") - 0.05, t1=E("c10") + 0.05, left="No jurisdiction", right="no FIR",
    at=A("c10", "refuse"), left_at=A("c10", "refuse"), icon="arrow-right",
    sub="It can be forwarded to the station having jurisdiction", sub_at=A("c10", "jurisdiction"))
cue(type="cite", t0=A("c10", "satvinder"), t1=E("c10") + 0.05, at=A("c10", "satvinder"), tag=f"{SC} · 1999 · OLD CODE",
    cases=[{"name": "Satvinder Kaur v. State (Govt. of NCT of Delhi)"}])

# ── 4 · e-FIR: electronic information ────────────────────────────────────────────────────────────────────────────────────────────
cue(type="kicker", t0=S("c11"), t1=E("c11") + 0.05, at=S("c11") + 0.05, text=HYPO)
cue(type="point", t0=S("c11"), t1=A("c11", "that") - 0.05, text="Meera reports electronically, from a laptop",
    icon="monitor", accent=True, at=A("c11", "now"))
cue(type="splitcard", t0=A("c11", "that") - 0.05, t1=E("c11") + 0.05,
    left={"title": "POPULAR NAME", "text": "the e-FIR", "icon": "monitor", "at": A("c11", "that")},
    right={"title": "THE SANHITA'S WORDS", "text": "electronic communication", "icon": "book-open", "at": A("c11", "calls")})
cue(type="cite", t0=A("c11", "calls"), t1=E("c11") + 0.05, at=A("c11", "calls"), tag="BNSS 2(1)(i)",
    text="Sent by an electronic device, including a telephone, mobile phone or computer", icon="book-open")
cue(type="counters", t0=S("c12"), t1=E("c12") + 0.05, head="Clause (ii): electronic information", head_at=S("c12") + 0.05,
    items=[{"value": 3, "unit": "DAYS", "label": "Signed by the person giving it", "sub": "then taken on record", "at": A("c12", "three")}])
cue(type="cite", t0=S("c12") + 0.3, t1=E("c12") + 0.05, at=S("c12") + 0.3, tag="BNSS 173(1)(ii)",
    text="“taken on record by him on being signed within three days by the person giving it”", icon="book-open")

# ── 5 · safeguards and a free copy ───────────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c13"), t1=E("c13") + 0.05, at=A("c13", "woman"), act="BNSS, 2023", num="173(1)",
    title="First proviso: a woman officer",
    points=[{"text": "Information given by the woman against whom the offence is alleged", "at": A("c13", "specified")},
            {"text": "Recorded by a woman police officer or any woman officer", "at": A("c13", "officer")}])
cue(type="cite", t0=A("c13", "sexual"), t1=E("c13") + 0.05, at=A("c13", "sexual"), tag="BNS OFFENCES COVERED",
    text="Sections 64–71, 74–79 and 124 (acid attack): committed or attempted", icon="book-open")
cue(type="checklist", t0=S("c14"), t1=E("c14") + 0.05, head="Second proviso: a disabled person", head_at=S("c14") + 0.05,
    items=[{"n": 1, "text": "At home, or a place of their choice", "at": A("c14", "home")},
           {"n": 2, "text": "An interpreter or special educator", "at": A("c14", "interpreter")},
           {"n": 3, "text": "Videographed", "at": A("c14", "videographed")}])
cue(type="cite", t0=A("c14", "disabled"), t1=E("c14") + 0.05, at=A("c14", "disabled"), tag="BNSS 173(1), SECOND PROVISO",
    text="Any victim of these offences, temporarily or permanently, mentally or physically disabled", icon="book-open")
cue(type="quote", t0=S("c15"), t1=E("c15") + 0.05, at=A("c15", "under"), reveal=r3(A("c15", "recorded") - A("c15", "under")),
    text="A copy of the information as recorded … shall be given forthwith, free of cost, to the informant or the victim.",
    hl=["forthwith, free of cost"])
cue(type="cite", t0=S("c15") + 0.3, t1=E("c15") + 0.05, at=S("c15") + 0.3, tag="BNSS, 2023", text="Section 173(2)", icon="book-open")

# ── 6 · preliminary enquiry ──────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c16"), t1=E("c16") + 0.05, head="Under the old Code", head_at=S("c16") + 0.05,
    steps=[{"label": "Constitution Bench", "sub": "Lalita Kumari", "icon": "landmark", "at": A("c16", "constitution")},
           {"label": "Registration mandatory", "sub": "when the information discloses a cognizable offence", "icon": "file-check",
            "tone": "ok", "at": A("c16", "registration")}])
cue(type="cite", t0=A("c16", "lalita"), t1=E("c16") + 0.05, at=A("c16", "lalita"), tag="SUPREME COURT · CONSTITUTION BENCH · 2013",
    cases=[{"name": "Lalita Kumari v. Govt. of U.P.", "cite": "para 120.1"}])
cue(type="list", t0=S("c17"), t1=E("c17") + 0.05, head="A preliminary inquiry", head_at=S("c17") + 0.05,
    items=[{"n": 1, "text": "Only in limited categories of cases", "at": A("c17", "limited")},
           {"n": 2, "text": "Only to check if a cognizable offence is disclosed", "at": A("c17", "check")},
           {"n": "!", "text": "Not to test whether the information is true", "at": A("c17", "disclosed")}])
cue(type="cite", t0=S("c17") + 0.1, t1=E("c17") + 0.05, at=S("c17") + 0.1, tag="SUPREME COURT · CONSTITUTION BENCH · 2013",
    cases=[{"name": "Lalita Kumari v. Govt. of U.P.", "cite": "paras 120.2, 120.5, 120.6"}])
cue(type="section", t0=S("c18"), t1=E("c18") + 0.05, at=A("c18", "sub"), act="BNSS, 2023", num="173(3)",
    title="New: a preliminary enquiry",
    points=[{"text": "Punishable for three years or more but less than seven years", "at": A("c18", "punishable")},
            {"text": "Police may hold a preliminary enquiry: a discretion", "at": A("c18", "may")}])
cue(type="flow", t0=S("c19"), t1=E("c19") + 0.05, head="The conditions", head_at=S("c19") + 0.05,
    steps=[{"label": "Prior permission", "sub": "an officer not below the rank of DSP", "icon": "badge-check", "at": A("c19", "permission")},
           {"label": "Within 14 days", "sub": "the enquiry", "icon": "clock", "at": A("c19", "fourteen")},
           {"label": "A prima facie case?", "sub": "for proceeding in the matter", "icon": "search", "tone": "ok", "at": A("c19", "prima")}])
cue(type="cite", t0=S("c19") + 0.3, t1=E("c19") + 0.05, at=S("c19") + 0.3, tag="BNSS 173(3)",
    text="“considering the nature and gravity of the offence” · a discretion, not a compulsory step", icon="book-open")
cue(type="splitcard", t0=S("c20"), t1=E("c20") + 0.05,
    left={"title": "SUB-SECTION (3)", "text": "an exception to sub-section (1)", "icon": "scale", "at": A("c20", "supreme")},
    right={"title": "ENQUIRY ALLOWED", "text": "even when a cognizable offence is disclosed", "icon": "search", "at": A("c20", "allowing")})
cue(type="cite", t0=A("c20", "supreme"), t1=E("c20") + 0.05, at=A("c20", "supreme"), tag=f"{SC} · 2025",
    cases=[{"name": "Imran Pratapgadhi v. State of Gujarat", "cite": "paras 23, 42(i)"}])
cue(type="point", t0=S("c21"), t1=A("c21", "and") - 0.05, text="Outside that exception: registration remains mandatory",
    icon="file-check", accent=True, at=A("c21", "outside"))
cue(type="flow", t0=A("c21", "and") - 0.05, t1=E("c21") + 0.05, head="If the enquiry finds no prima facie case", head_at=A("c21", "and"),
    steps=[{"label": "No prima facie case", "icon": "search", "at": A("c21", "finds")},
           {"label": "The informant is told immediately", "sub": "so the s. 173(4) remedy can be used", "icon": "bell", "tone": "ok",
            "at": A("c21", "informant")}])
cue(type="cite", t0=S("c21") + 0.1, t1=E("c21") + 0.05, at=S("c21") + 0.1, tag=f"{SC} · 2025",
    cases=[{"name": "Imran Pratapgadhi v. State of Gujarat", "cite": "paras 24, 25, 42(ii)"}])

# ── 7 · when information is not recorded ─────────────────────────────────────────────────────────────────────────────────────────
cue(type="kicker", t0=S("c22"), t1=E("c25") + 0.05, at=S("c22") + 0.05, text=HYPO)
cue(type="question", t0=S("c22"), t1=A("c22", "section") - 0.05, at=A("c22", "suppose"),
    text="Suppose the information is not recorded?", hl="not recorded?")
cue(type="section", t0=A("c22", "section") - 0.05, t1=E("c22") + 0.05, at=A("c22", "section"), act="BNSS, 2023", num="173(4)",
    title="When information is not recorded",
    points=[{"text": "A remedy for the person aggrieved: here, Meera", "at": A("c22", "meera")}])
cue(type="flow", t0=S("c23"), t1=E("c23") + 0.05, head="First: the Superintendent of Police", head_at=S("c23") + 0.05,
    steps=[{"label": "The substance of her information", "icon": "file-text", "at": A("c23", "substance")},
           {"label": "In writing and by post", "sub": "both", "icon": "mail", "at": A("c23", "writing")},
           {"label": "To the SP concerned", "icon": "landmark", "tone": "ok", "at": A("c23", "superintendent")}])
cue(type="point", t0=S("c24"), t1=A("c24", "superintendent") - 0.05, text="If satisfied it discloses a cognizable offence",
    icon="search-check", accent=True, at=A("c24", "satisfied"))
cue(type="splitcard", t0=A("c24", "superintendent") - 0.05, t1=E("c24") + 0.05,
    left={"title": "THE SP INVESTIGATES", "text": "the case himself", "icon": "search", "at": A("c24", "superintendent")},
    right={"title": "OR DIRECTS", "text": "an investigation by a subordinate officer", "icon": "users", "at": A("c24", "direct")})
cue(type="flow", t0=S("c25"), t1=E("c25") + 0.05, head="Then: the Magistrate", head_at=S("c25") + 0.05,
    steps=[{"label": "Failing that", "sub": "s. 173(4): “failing which”", "icon": "mail", "at": A("c25", "failing")},
           {"label": "Apply to the Magistrate", "icon": "gavel", "at": A("c25", "magistrate")},
           {"label": "An affidavit in support", "sub": "s. 175(3)", "icon": "file-pen-line", "tone": "ok", "at": A("c25", "affidavit")}])
cue(type="cite", t0=A("c25", "section"), t1=E("c25") + 0.05, at=A("c25", "section"), tag="BNSS 175(3)",
    text="The application supported by an affidavit made under section 173(4)", icon="book-open")
cue(type="checklist", t0=S("c26"), t1=E("c26") + 0.05, head="Before the Magistrate may order investigation", head_at=S("c26") + 0.05,
    items=[{"n": 1, "text": "The application and its affidavit", "at": A("c26", "magistrate")},
           {"n": 2, "text": "Such inquiry as he thinks necessary", "at": A("c26", "inquiry")},
           {"n": 3, "text": "The police officer's submissions", "at": A("c26", "submissions")}])
cue(type="cite", t0=S("c26") + 0.1, t1=E("c26") + 0.05, at=S("c26") + 0.1, tag=f"{SC} · 2025",
    cases=[{"name": "Om Prakash Ambadkar v. State of Maharashtra", "cite": "para 29"}])
cue(type="point", t0=S("c27"), t1=A("c27", "like") - 0.05, text="These conditions codify earlier judicial safeguards",
    icon="scale", accent=True, at=A("c27", "supreme"))
cue(type="splitcard", t0=A("c27", "like") - 0.05, t1=E("c27") + 0.05,
    left={"title": "OLD CODE · s. 156(3)", "text": "Priyanka Srivastava: an application supported by an affidavit", "icon": "scale",
          "at": A("c27", "priyanka")},
    right={"title": "BNSS · s. 175(3)", "text": "the affidavit is now in the statute", "icon": "book-open", "at": A("c27", "rule")})
cue(type="cite", t0=S("c27") + 0.1, t1=E("c27") + 0.05, at=S("c27") + 0.1, tag=SC,
    cases=[{"name": "Om Prakash Ambadkar v. State of Maharashtra", "cite": "2025 · para 34"},
           {"name": "Priyanka Srivastava v. State of U.P.", "cite": "2015 · old Code"}])

# ── 8 · non-cognizable information ───────────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c28"), t1=A("c28", "then") - 0.05, at=A("c28", "what"),
    text="What if it discloses only a non-cognizable offence?", hl="non-cognizable offence?")
cue(type="section", t0=A("c28", "then") - 0.05, t1=E("c28") + 0.05, at=A("c28", "section"), act="BNSS, 2023", num="174",
    title="Non-cognizable cases",
    points=[{"text": "Applies instead of section 173", "at": A("c28", "applies")}])
cue(type="flow", t0=S("c29"), t1=E("c29") + 0.05, head="Section 174(1)", head_at=S("c29") + 0.05,
    steps=[{"label": "Substance entered in a book", "sub": "kept by the officer", "icon": "book-text", "at": A("c29", "records")},
           {"label": "Informant referred to the Magistrate", "icon": "gavel", "tone": "ok", "at": A("c29", "refers")}])
cue(type="cite", t0=S("c29") + 0.3, t1=E("c29") + 0.05, at=S("c29") + 0.3, tag="BNSS 174(1)(ii)",
    text="Daily diary reports of such cases go to the Magistrate fortnightly", icon="book-open")
cue(type="section", t0=S("c30"), t1=A("c30", "but") - 0.05, at=A("c30", "police"), act="BNSS, 2023", num="174(2)",
    title="Investigating a non-cognizable case",
    points=[{"text": "Only on the order of a Magistrate who can try or commit the case", "at": A("c30", "order")}])
cue(type="equation", t0=A("c30", "but") - 0.05, t1=E("c30") + 0.05,
    terms=[{"text": "AT LEAST ONE OFFENCE COGNIZABLE", "at": A("c30", "but")},
           {"op": "=", "text": "THE WHOLE CASE: DEEMED COGNIZABLE", "result": True, "at": A("c30", "whole")}])
cue(type="cite", t0=A("c30", "but"), t1=E("c30") + 0.05, at=A("c30", "but"), tag="BNSS 174(4)",
    text="Even though the other offences are non-cognizable", icon="book-open")

# ── 9 · what an FIR is not ───────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="verdicts", t0=S("c31"), t1=E("c31") + 0.05,
    rows=[{"text": "Registration ≠ arrest", "ok": True, "at": A("c31", "registration")},
          {"text": "An FIR ≠ proof of guilt", "ok": True, "at": A("c31", "F")},
          {"text": "Guilt is for the court", "ok": True, "at": A("c31", "that")}])
cue(type="notequal", t0=S("c32"), t1=E("c32") + 0.05, left="An FIR", right="substantive evidence",
    at=A("c32", "it"), left_at=A("c32", "nor"), icon="scale",
    sub="Generally used only to corroborate or contradict its maker", sub_at=A("c32", "generally"))
cue(type="cite", t0=S("c32") + 0.3, t1=A("c32", "it", 2), at=S("c32") + 0.3, tag=f"{SC} · 1971",
    cases=[{"name": "Sheikh Hasib v. State of Bihar", "cite": "para 4"}])
cue(type="cite", t0=A("c32", "it", 2), t1=E("c32") + 0.05, at=A("c32", "it", 2), tag="BHARATIYA SAKSHYA ADHINIYAM, 2023",
    text="Corroborate: section 160 · contradict: section 148", icon="book-open")
cue(type="quote", t0=S("c33"), t1=E("c33") + 0.05, at=A("c33", "under"), reveal=r3(A("c33", "detail") - A("c33", "under")),
    text="… a first information report is not an encyclopaedia, which must disclose all facts and details relating to the offence reported.",
    hl=["not an encyclopaedia"])
cue(type="cite", t0=A("c33", "supreme"), t1=E("c33") + 0.05, at=A("c33", "supreme"), tag=f"{SC} · 2003 · OLD CODE",
    cases=[{"name": "Supdt. of Police, CBI v. Tapan Kumar Singh", "cite": "para 20"}])
cue(type="point", t0=S("c34"), t1=A("c34", "delay") - 0.05, text="Report promptly", icon="clock", accent=True, at=A("c34", "report"))
cue(type="verdicts", t0=A("c34", "delay") - 0.05, t1=E("c34") + 0.05,
    rows=[{"text": "Delay is fatal by itself", "ok": False, "at": A("c34", "delay"), "strike_at": A("c34", "itself")},
          {"text": "Courts look for a satisfactory explanation", "ok": True, "at": A("c34", "satisfactory")}])
cue(type="cite", t0=A("c34", "because"), t1=E("c34") + 0.05, at=A("c34", "because"), tag=f"{SC} · DELAY CAN INVITE EMBELLISHMENT",
    cases=[{"name": "Thulia Kali v. State of T.N.", "cite": "1972"}, {"name": "State of H.P. v. Gian Chand", "cite": "2001"}])
cue(type="compare", t0=S("c35"), t1=E("c35") + 0.05, head="Knowingly false information", head_at=S("c35") + 0.05,
    cols=[{"title": "BNS · s. 217", "icon": "file-text", "at": A("c35", "two")},
          {"title": "BNS · s. 248", "icon": "gavel", "at": A("c35", "two", 2)}],
    rows=[{"cells": ["False information to a public servant, with intent to injure another", "A false charge of an offence, made with intent to injure"],
           "cells_at": [A("c35", "seventeen"), A("c35", "forty")]}],
    verdict={"text": "“May be an offence”: the key word is knowingly", "icon": "scale", "at": A("c35", "bharatiya")})

# ── 10 · your checklist ──────────────────────────────────────────────────────────────────────────────────────────────────────────
# "check" #1 is "checklist" (at() prefix-matches words of 4+ letters): #2 is "check that it records"
cue(type="checklist", t0=S("c36"), t1=E("c36") + 0.05, head="Your checklist", head_at=S("c36") + 0.05,
    items=[{"n": 1, "text": "Take your free copy", "at": A("c36", "take")},
           {"n": 2, "text": "Check it records your facts accurately", "at": A("c36", "check", 2)},
           {"n": 3, "text": "Note the sections mentioned", "at": A("c36", "note")}])
cue(type="flow", t0=S("c37"), t1=E("c37") + 0.05, head="Not recorded?", head_at=A("c37", "not"),
    steps=[{"label": "Write to the SP", "sub": "in writing and by post", "icon": "mail", "at": A("c37", "write")},
           {"label": "If that fails: the Magistrate", "sub": "s. 175(3)", "icon": "gavel", "at": A("c37", "magistrate")},
           {"label": "Affidavit + a copy of that letter", "icon": "file-pen-line", "tone": "ok", "at": A("c37", "affidavit")}])
cue(type="cite", t0=A("c37", "magistrate"), t1=E("c37") + 0.05, at=A("c37", "magistrate"), tag=f"{SC} · 2025",
    cases=[{"name": "Om Prakash Ambadkar v. State of Maharashtra", "cite": "para 31(a)"}])
cue(type="point", t0=S("c38"), t1=E("c38") + 0.05, text="Like · Share · Subscribe · lawworld.ai",
    icon="check", accent=True, at=A("c38", "thanks"))
