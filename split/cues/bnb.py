# Bailable and Non-Bailable Offences (BNSS) - CONCEPT VIDEO (legal-concept explainer, Cause of Action build): panel cues, run by
# split/build_course_plan.py (helpers: at S E cue fx have r3 PEND). Storyboard: ~/Downloads/Bailable_and_Non_Bailable_Offences_BNSS_Storyboard.pdf
# (research-checked by the owner 19-10-2026). The storyboard cites no cases, so no case appears on screen.
# Held to the PDF's "Points to preserve" and its animation column:
#  - every example assumes ONLY the stated offence and subsection (BNS 115(2) ordinary hurt, 118(1) hurt by a dangerous weapon,
#    117(2) ordinary grievous hurt); the cards say "assumed", and other facts or charges can change the position;
#  - 117(2) = cognizable + bailable, and that entry is never applied to the different, aggravated offences in 117(3) and 117(4);
#  - s.478 does not make every accused produce a surety: its first proviso allows a personal bond, and requires one for an indigent
#    person who cannot furnish surety; no bail bond within a week of arrest = sufficient ground to PRESUME indigence, NOT a waiting
#    period; a bond amount is not automatically an upfront cash payment or a fine; 484(1): not excessive;
#  - non-bailable is not a blanket ban and keeps statutory release rights where their conditions apply (480(2)); 480(1), 480(3)-(4)
#    and 483 carry restrictions, exceptions, recorded reasons and prosecution-hearing requirements - no card promises bail;
#  - 482(4) excludes BNS 65 (all) and 70(2); special laws may add more; filing an application alone gives NO protection;
#  - breach: 478(2), 480(3), 480(5), 483(3), 485 - the court reviews the order, no automatic imprisonment;
#  - 47(2) is a footer only, shown while Amit is in court, never as if his ordinary hurt required or allowed arrest;
#  - default bail (187(3)), undertrial detention (479) and post-conviction release are not on screen;
#  - bail is never shown as acquittal or a finding of guilt; the accused is "accused", never depicted as guilty;
#  - final comparison: BAILABLE -> 478 · NON-BAILABLE -> 480 and 483 · BEFORE ARREST -> 482, where available; Bail ≠ acquittal.
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

STING = {"kicker": "CRIMINAL PROCEDURE · BNSS EXPLAINED", "title": "Bailable and Non-Bailable Offences",
         "sub": "Bail rights and court powers under the BNSS"}
ENDCARD = {"title": "Bailable and Non-Bailable Offences", "line": "Bailable → 478 · Non-bailable → 480, 483 · Before arrest → 482",
           "sub": "LawWorld: legal research for advocates"}

# ── 1 · does non bailable mean no bail? ──────────────────────────────────────────────────────────────────────────────────────────
cue(type="verdicts", t0=S("c01"), t1=A("c02", "a") - 0.05,
    rows=[{"text": "Non-bailable = no bail", "ok": False, "at": A("c01", "non"), "strike_at": A("c01", "both")},
          {"text": "Bailable = case over", "ok": False, "at": A("c01", "bailable", 2), "strike_at": A("c01", "wrong")}])
cue(type="compare", t0=A("c02", "a") - 0.05, t1=E("c03") + 0.05, head="Two misreadings", head_at=A("c02", "a"),
    cols=[{"title": "The family fears", "icon": "users", "at": A("c02", "family")}, {"title": "Others assume", "icon": "user-round", "at": A("c03", "others")}],
    rows=[{"cells": ["A relative accused of a non-bailable offence", "A bailable offence"], "cells_at": [A("c02", "non"), A("c03", "bailable")]},
          {"cells": ["Bail is now impossible", "The case disappears"], "cells_at": [A("c02", "impossible"), A("c03", "disappear")]}],
    verdict={"text": "Both misread the law", "icon": "triangle-alert", "at": A("c03", "let")})
cue(type="cite", t0=A("c03", "bharatiya"), t1=E("c03") + 0.05, at=A("c03", "bharatiya"), tag="THE LAW",
    text="Bharatiya Nagarik Suraksha Sanhita, 2023 (BNSS)", icon="book-open")

# ── 2 · start with the definitions ───────────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c04"), t1=E("c04") + 0.05, at=A("c04", "section"), act="BNSS, 2023", num="2(1)(b)", title="Bail",
    points=[{"text": "Release from legal custody", "at": A("c04", "release")},
            {"text": "On conditions set by an officer or court", "at": A("c04", "conditions")},
            {"text": "Through a bond, or a bail bond", "at": A("c04", "through")}])
cue(type="section", t0=S("c05"), t1=A("c06", "liberty") - 0.05, at=A("c05", "clause"), act="BNSS, 2023", num="2(1)(c)",
    title="Bailable and non-bailable",
    points=[{"text": "Shown as bailable in the First Schedule", "at": A("c05", "shown")},
            {"text": "Or made bailable by another law", "at": A("c05", "made")},
            {"text": "Every other offence: non-bailable", "at": A("c06", "non")}])
cue(type="cite", t0=A("c05", "first"), t1=A("c06", "liberty") - 0.05, at=A("c05", "first"), tag="BNSS FIRST SCHEDULE",
    text="A separate column marks each offence bailable or non-bailable", icon="book-open")
cue(type="flow", t0=A("c06", "liberty") - 0.05, t1=A("c06", "not") - 0.05, head="Bail concerns liberty", head_at=A("c06", "liberty"),
    steps=[{"label": "Legal custody", "icon": "lock", "at": A("c06", "liberty")},
           {"label": "Release on conditions", "icon": "key-round", "tone": "ok", "at": A("c06", "while")},
           {"label": "The case file stays open", "sub": "the case proceeds", "icon": "file-text", "at": A("c06", "proceeds")}])
cue(type="notequal", t0=A("c06", "not") - 0.05, t1=E("c06") + 0.05, left="Bail", right="an acquittal",
    at=A("c06", "acquittal"), left_at=A("c06", "not"),
    sub="Liberty while the case proceeds, not a finding of guilt", sub_at=A("c06", "finding"))

# ── 3 · a bailable offence and the right to release ──────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c07"), t1=E("c07") + 0.05, text="Amit is accused of slapping an adult neighbour", icon="user-round", at=A("c07", "amit"))
cue(type="section", t0=S("c08"), t1=E("c08") + 0.05, at=A("c08", "assume"), act="BNS, 2023", num="115(2)", title="Voluntarily causing hurt",
    points=[{"text": "Assumed: ordinary hurt only", "at": A("c08", "ordinary")},
            {"text": "BNSS First Schedule: bailable", "at": A("c08", "lists")}])
cue(type="cite", t0=A("c08", "section"), t1=E("c08") + 0.05, at=A("c08", "section"), tag="ASSUMED FACTS",
    text="Only the stated offence and subsection; other facts or charges can change it", icon="info")
cue(type="flow", t0=S("c09"), t1=E("c09") + 0.05, head="Amit before the Magistrate", head_at=S("c09") + 0.05,
    steps=[{"label": "He appears before the Magistrate", "icon": "landmark", "at": A("c09", "appears")},
           {"label": "Ready to meet the lawful bail requirements", "icon": "file-pen-line", "tone": "ok", "at": A("c09", "ready")}])
# on screen only (storyboard footer): shown while Amit is in court, so it never suggests that his ordinary hurt calls for an arrest
cue(type="cite", t0=A("c09", "ready"), t1=E("c10") + 0.05, at=A("c09", "ready"), tag="BNSS 47(2) · ON ARREST WITHOUT WARRANT",
    text="In a bailable case, police must tell the person they are entitled to bail", icon="info")
cue(type="section", t0=S("c10"), t1=E("c10") + 0.05, at=A("c10", "under"), act="BNSS, 2023", num="478(1)", title="Release in a bailable offence",
    points=[{"text": "His release is a right", "at": A("c10", "release")},
            {"text": "Once those requirements are met", "at": A("c10", "requirements")}])
cue(type="point", t0=S("c11"), t1=A("c11", "the", 2) - 0.05, text="The case continues: Amit must attend as required",
    icon="calendar", accent=True, at=A("c11", "case"))
cue(type="splitcard", t0=A("c11", "the", 2) - 0.05, t1=E("c11") + 0.05,
    left={"title": "BNS", "text": "defines the offence", "icon": "scroll-text", "at": A("c11", "bharatiya")},
    right={"title": "BNSS", "text": "supplies the procedure", "icon": "gavel", "at": A("c11", "supplies")})

# ── 4 · what if Amit cannot find a surety? ───────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c12"), t1=A("c12", "under") - 0.05, at=A("c12", "amit"), text="What if Amit cannot find a surety?", hl="cannot find a surety?")
cue(type="splitcard", t0=A("c12", "under") - 0.05, t1=E("c12") + 0.05,
    left={"title": "BAIL BOND · 2(1)(d)", "text": "involves a surety", "icon": "users", "at": A("c12", "section")},
    right={"title": "BOND · 2(1)(e)", "text": "a personal bond, without a surety", "icon": "file-pen-line", "at": A("c12", "clause", 2)})
cue(type="point", t0=S("c13"), t1=E("c13") + 0.05, text="A surety takes responsibility for the accused's appearance", icon="calendar", at=A("c13", "surety"))
cue(type="section", t0=S("c14"), t1=E("c14") + 0.05, at=A("c14", "section"), act="BNSS, 2023", num="478(1)", title="First proviso: a personal bond",
    points=[{"text": "The officer or court may accept a personal bond", "at": A("c14", "accept")},
            {"text": "Required for an indigent person who cannot furnish surety", "at": A("c14", "indigent")}],
    note={"text": "The one-week rule is a presumption, not a waiting period", "icon": "info", "at": A("c14", "furnish")})
# on screen only (production note): the Explanation's one-week presumption; the c15 bar takes over this one (linked hand-over)
cue(type="cite", t0=A("c14", "personal"), t1=E("c14") + 0.05, at=A("c14", "personal"), tag="BNSS 478(1) · EXPLANATION",
    text="No bail bond within a week of arrest: sufficient ground to presume indigence", icon="info")
cue(type="cite", t0=S("c15") + 0.1, t1=E("c15") + 0.05, at=S("c15") + 0.1, tag="BNSS 478(1), FIRST PROVISO · 484(1)",
    text="A bond is not automatically an upfront cash payment, or a fine", icon="book-open")
cue(type="section", t0=S("c15"), t1=A("c15", "bail") - 0.05, at=A("c15", "section"), act="BNSS, 2023", num="484(1)", title="The amount of the bond",
    points=[{"text": "The bond amount must not be excessive", "at": A("c15", "amount")}])
cue(type="point", t0=A("c15", "bail") - 0.05, t1=E("c15") + 0.05, text="Bail should never become a punishment for being poor",
    icon="scale", accent=True, at=A("c15", "bail"))

# ── 5 · non bailable can still attract bail ──────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c16"), t1=A("c16", "b") - 0.05, text="A new example: a person accused of causing hurt with a knife",
    icon="user-round", at=A("c16", "change"))
cue(type="section", t0=A("c16", "b") - 0.05, t1=A("c17", "does") - 0.05, at=A("c16", "b"), act="BNS, 2023", num="118(1)",
    title="Hurt by dangerous weapons or means",
    points=[{"text": "Assumed: hurt by a dangerous weapon", "at": A("c16", "section")},
            {"text": "First Schedule: non-bailable", "at": A("c17", "classifies")}])
cue(type="cite", t0=A("c16", "facts"), t1=A("c17", "does") - 0.05, at=A("c16", "facts"), tag="ASSUMED FACTS ONLY",
    text="Not every injury involving a knife falls under 118(1)", icon="info")
cue(type="question", t0=A("c17", "does") - 0.05, t1=E("c17") + 0.05, at=A("c17", "mean"), text="Does that mean bail is prohibited?", hl="prohibited?",
    y=230)   # 07-11 layout gate: card up, the stamp lands clear below it
cue(type="stamp", t0=A("c17", "no") - 0.05, t1=E("c17") + 0.05, at=A("c17", "no"), line1="NO", line2="NOT A BLANKET BAN", y=805)
cue(type="compare", t0=S("c18"), t1=E("c19") + 0.05, head="Bail in non-bailable cases", head_at=S("c18") + 0.05,
    cols=[{"title": "§ 480", "icon": "landmark", "at": A("c18", "section")}, {"title": "§ 483", "icon": "gavel", "at": A("c19", "section")}],
    rows=[{"cells": ["Before the Magistrate", "Special powers: the Sessions Court"], "cells_at": [A("c18", "magistrate"), A("c19", "sessions")]},
          {"cells": ["Within its limits, the officer in charge of a police station", "And the High Court"], "cells_at": [A("c18", "officer"), A("c19", "high")]}])
# on screen only: 480(2) (a statutory release right), then the storyboard's caption for the scene (linked hand-over at c19)
cue(type="cite", t0=A("c18", "governs"), t1=E("c18") + 0.05, at=A("c18", "governs"), tag="BNSS 480(2)",
    text="Statutory release rights still apply where their conditions are met", icon="book-open")
cue(type="cite", t0=S("c19") + 0.1, t1=E("c19") + 0.05, at=S("c19") + 0.1, tag="BNSS 480 · 483",
    text="Bail is possible; conditions and restrictions apply", icon="scale")

# ── 6 · how the court considers the application ──────────────────────────────────────────────────────────────────────────────────
cue(type="checklist", t0=S("c20"), t1=E("c21") + 0.05, head="How the court decides", head_at=A("c20", "how"),
    items=[{"n": 1, "text": "The material, and the role alleged", "at": A("c20", "material")},
           {"n": 2, "text": "The seriousness of the offence", "at": A("c20", "seriousness")},
           {"n": 3, "text": "Risk of absconding", "at": A("c21", "absconding")},
           {"n": 4, "text": "Risk to witnesses and evidence", "at": A("c21", "threatening")}])
cue(type="section", t0=S("c22"), t1=E("c22") + 0.05, at=A("c22", "section"), act="BNSS, 2023", num="480", title="Restrictions, with exceptions",
    points=[{"text": "Rules for offences punishable with death or life imprisonment", "at": A("c22", "rules")},
            {"text": "Alongside specified exceptions", "at": A("c22", "alongside")}])
cue(type="cite", t0=A("c22", "restrictions"), t1=E("c22") + 0.05, at=A("c22", "restrictions"), tag="BNSS 480(1), 480(3)–(4) · 483",
    text="Restrictions, conditions, recorded reasons and prosecution hearing requirements", icon="book-open")
cue(type="verdicts", t0=S("c23"), t1=E("c23") + 0.05,
    rows=[{"text": "The label “non-bailable” begins the analysis", "ok": True, "at": A("c23", "label")},
          {"text": "The label alone decides this person's bail", "ok": False, "at": A("c23", "itself"), "strike_at": A("c23", "decide")}])

# ── 7 · anticipatory bail before arrest ──────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c24"), t1=E("c25") + 0.05, head="Sita fears arrest", head_at=S("c24") + 0.05,
    steps=[{"label": "Reason to believe she may be arrested", "sub": "a non-bailable accusation", "icon": "triangle-alert", "at": A("c24", "reason")},
           {"label": "She applies under § 482", "sub": "Sessions Court or High Court", "icon": "file-pen-line", "at": A("c25", "apply")},
           {"label": "Court directs: bail if arrested", "sub": "on conditions", "icon": "key-round", "tone": "ok", "at": A("c25", "direct")}],
    note={"text": "Possible conditions: attend questioning, no pressure on witnesses", "icon": "shield-check", "at": A("c25", "on", 2)})
cue(type="compare", t0=S("c26"), t1=E("c26") + 0.05, head="Before arrest, or after custody", head_at=S("c26") + 0.05,
    cols=[{"title": "Anticipatory bail · § 482", "icon": "shield-check", "at": A("c26", "anticipatory")},
          {"title": "Ordinary bail · §§ 480, 483", "icon": "key-round", "at": A("c26", "ordinary")}],
    rows=[{"cells": ["Protection sought before arrest", "Sought after entering custody"], "cells_at": [A("c26", "protection"), A("c26", "after")]}])
cue(type="verdicts", t0=S("c27"), t1=E("c27") + 0.05,
    rows=[{"text": "Automatic immunity", "ok": False, "at": A("c27", "not"), "strike_at": A("c27", "immunity") + 0.3},
          {"text": "Filing alone protects Sita", "ok": False, "at": A("c27", "filing"), "strike_at": A("c27", "protect")},
          {"text": "Only a court direction secures release on bail", "ok": True, "at": A("c27", "only")}])
cue(type="cite", t0=A("c27", "filing"), t1=E("c27") + 0.05, at=A("c27", "filing"), tag="BNSS 482(1)–(4)",
    text="An application alone is not an order protecting against arrest", icon="info")
cue(type="section", t0=S("c28"), t1=E("c28") + 0.05, at=A("c28", "section"), act="BNSS, 2023", num="482(4)", title="Excluded from anticipatory bail",
    points=[{"text": "BNS 70(2): gang rape of a woman under 18", "tone": "no", "at": A("c28", "seventy")},
            {"text": "All of BNS 65: rape of a woman under 16", "tone": "no", "at": A("c28", "sixty")}],
    note={"text": "Special laws may add more", "icon": "book-open", "at": A("c28", "special")})

# ── 8 · release comes with responsibilities ──────────────────────────────────────────────────────────────────────────────────────
cue(type="checklist", t0=S("c29"), t1=E("c29") + 0.05, head="After release", head_at=A("c29", "after"),
    items=[{"n": 1, "text": "Obey the order and the bond", "at": A("c29", "obey")},
           {"n": 2, "text": "Attend when required", "at": A("c29", "attend")},
           {"n": 3, "text": "Cooperate as directed", "at": A("c29", "cooperate")},
           {"n": 4, "text": "No threats to witnesses, no tampering", "at": A("c29", "threaten")}])
cue(type="section", t0=S("c30"), t1=A("c30", "a") - 0.05, at=A("c30", "section"), act="BNSS, 2023", num="485", title="The bond and its conditions",
    points=[{"text": "Undertakings to appear", "at": A("c30", "appearance")},
            {"text": "Conditions recorded in the bond", "at": A("c30", "recorded")}])
cue(type="flow", t0=A("c30", "a") - 0.05, t1=E("c30") + 0.05, head="After an alleged breach", head_at=A("c30", "a"),
    steps=[{"label": "An alleged breach", "icon": "triangle-alert", "at": A("c30", "breach")},
           {"label": "The court reviews the bail order", "sub": "no automatic imprisonment", "icon": "gavel", "at": A("c30", "lead")},
           {"label": "A return to custody is possible", "sub": "under other provisions", "icon": "lock", "at": A("c30", "return")}])
# "under" #1 is "undertakings" (at() prefix-matches words of 4+ letters): #2 is "Under other provisions"
cue(type="cite", t0=A("c30", "under", 2), t1=E("c31") + 0.05, at=A("c30", "under", 2), tag="BNSS 478(2) · 480(3) · 480(5) · 483(3) · 485",
    text="Bail conditions, breach, and the power to return a person to custody", icon="book-open")
cue(type="section", t0=S("c31"), t1=E("c31") + 0.05, at=A("c31", "even"), act="BNSS, 2023", num="478(2)", title="Even in a bailable case",
    points=[{"text": "A missed court date", "at": A("c31", "missed")},
            {"text": "May let the court refuse bail on a later occasion", "at": A("c31", "refuse")},
            {"text": "In that same case", "at": A("c31", "same")}])

# ── 9 · do not confuse bail with cognizability ───────────────────────────────────────────────────────────────────────────────────
cue(type="compare", t0=S("c32"), t1=E("c32") + 0.05, head="Two different questions", head_at=S("c32") + 0.05,
    cols=[{"title": "Cognizability", "icon": "search", "at": A("c32", "cognizability")}, {"title": "Bail", "icon": "key-round", "at": A("c32", "bailable")}],
    rows=[{"cells": ["Cognizable or non-cognizable", "Bailable or non-bailable"], "cells_at": [A("c32", "cognizable"), A("c32", "non", 2)]},
          {"cells": ["Police powers", "Release on bail"], "cells_at": [A("c32", "police"), A("c32", "release")]}])
cue(type="cite", t0=A("c32", "police"), t1=E("c33") + 0.05, at=A("c32", "police"), tag="BNSS FIRST SCHEDULE",
    text="Separate columns · definitions in 2(1)(c), 2(1)(g) and 2(1)(o)", icon="book-open")
cue(type="section", t0=S("c33"), t1=E("c34") + 0.05, at=A("c33", "in"), act="BNS, 2023", num="117(2)", title="Voluntarily causing grievous hurt",
    points=[{"text": "Ordinary grievous hurt only", "at": A("c33", "ordinary")},
            {"text": "First Schedule: cognizable + bailable", "at": A("c33", "cognizable")},
            {"text": "Not the aggravated offences in 117(3) and 117(4)", "tone": "no", "at": A("c34", "cover")}])
cue(type="strike", t0=S("c35"), t1=A("c35", "check") - 0.05, text="Cognizable = automatically non-bailable", icon="lock",
    at=S("c35") + 0.05, strike_at=A("c35", "automatically") + 0.1)
cue(type="point", t0=A("c35", "check") - 0.05, t1=E("c35") + 0.05, text="Check the exact subsection and special laws, not the name",
    icon="search-check", accent=True, at=A("c35", "check"))

# ── 10 · the distinction to remember ─────────────────────────────────────────────────────────────────────────────────────────────
cue(type="compare", t0=S("c36"), t1=E("c38") + 0.05, head="The distinction to remember", head_at=S("c36") + 0.05,
    cols=[{"title": "The situation", "icon": "user-round", "at": A("c36", "remember")}, {"title": "The route", "icon": "key-round", "at": A("c36", "section")}],
    rows=[{"cells": ["Bailable", "BNSS 478: bail as a right"], "cells_at": [A("c36", "four"), A("c36", "provides")]},
          {"cells": ["Non-bailable", "BNSS 480 and 483: release remains possible"], "cells_at": [A("c37", "non"), A("c37", "sections")]},
          {"cells": ["Before arrest", "BNSS 482: anticipatory bail, where available"], "cells_at": [A("c38", "section"), A("c38", "anticipatory")]}],
    verdict={"text": "Bail ≠ acquittal · the case goes on", "icon": "scale", "at": A("c38", "bond")})
cue(type="list", t0=S("c39"), t1=E("c39") + 0.05, head="Identify", head_at=A("c39", "identify"),
    items=[{"n": 1, "text": "The exact offence", "at": A("c39", "exact")},
           {"n": 2, "text": "The correct bail route", "at": A("c39", "correct")},
           {"n": 3, "text": "The conditions of release", "at": A("c39", "conditions")}])
cue(type="point", t0=S("c40"), t1=E("c40") + 0.05, text="Like · Share · Subscribe · lawworld.ai", icon="check", accent=True, at=A("c40", "like"))
