# Temporary Injunctions under Order XXXIX CPC - CONCEPT VIDEO (legal-concept explainer, Cause of Action build): panel cues, run by
# split/build_course_plan.py (helpers: at S E cue fx have r3 PEND). Source: split/scripts/inj.txt (no storyboard PDF; its // header
# lists the bare-act wording and the judgment paragraphs, all checked 10-11-2026). 39 clips, c39 = the closing line.
# Held to the script header:
#  - a case is shown by its LawWorld Citation ID only, never SCC / AIR / INSC; no ID is known for any case here, so each footer
#    carries the case name, the court, the decision date and the paragraph(s) from the header. Cotton Corporation has no verified
#    SCC paragraph: its footer cites the SCR pages, as the header says;
#  - statutory wording on screen follows the header verbatim ("Order XXXIX Rule 1" style); quotation marks only around words the
#    header quotes;
#  - interim relief is discretionary and equitable: no "GRANTED" stamp, no card that promises an outcome; c16 strikes "the tests
#    met: an injunction follows automatically";
#  - prima facie case is not prima facie title (c12); Anita's sale deed "raises a serious question", it does not prove ownership
#    (c15); a prima facie case alone is not enough (c13);
#  - Rule 2A penalties are "may" and "not exceeding three months" (c27); Rule 3A's thirty days are an ENDEAVOUR, never a lapse (c24);
#  - Order XLIII Rule 1(r) lists Rules 1, 2, 2A, 4 and 10 only (c29): Rules 3 / 3A are not added;
#  - a mandatory interim injunction needs a higher standard; it is not barred (c33-c34);
#  - Anita, Naresh, the strip, the foundations, the concrete pour and the wall are HYPOTHETICAL: every card that shows them carries
#    the HYPOTHETICAL EXAMPLE kicker (c06, c15, c18, c19, c32) or says so itself (c09 note); Naresh is never shown as a wrongdoer
#    before an order exists (c27 = disobedience of an order, shown generically);
#  - on screen only (not narrated): Rule 4's second proviso (c25 footer), s. 95 CPC (c18 footer), Cotton Corporation (c35 footer),
#    s. 38 SRA (c05 footer), s. 104(1)(i) (c29 note), Dorab's guidelines "not exhaustive" (c34 head); no state-specific detail (c38).
# Layout (07-11 lessons): no list over 3 rows under a bar; the counters card (c24) carries a note, so no bar under it; one-row
# compare cards only.
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

STING = {"kicker": "CIVIL PROCEDURE · CPC EXPLAINED", "title": "Temporary Injunctions under Order XXXIX CPC",
         "sub": "Interim relief while a suit is pending"}
ENDCARD = {"title": "Temporary Injunctions under Order XXXIX CPC", "line": "Fit the rule · prove the three tests · the court's discretion",
           "sub": "LawWorld: legal research for advocates"}

HYP = "HYPOTHETICAL EXAMPLE"
SC = "SUPREME COURT OF INDIA"
DALPAT = "Dalpat Kumar v. Prahlad Singh"   # SC 16.12.1991
MORGAN = "Morgan Stanley Mutual Fund v. Kartick Das"   # SC 20.05.1994

# ── 1 · what a temporary injunction does ─────────────────────────────────────────────────────────────────────────────────────────
cue(type="timeline", t0=S("c01"), t1=A("c01", "can") - 0.05,
    nodes=[{"label": "CONSTRUCTION", "value": "Tomorrow", "sub": "on land you claim", "at": A("c01", "tomorrow")},
           {"label": "YOUR SUIT", "value": "Years", "sub": "before the rights are decided", "at": A("c01", "years")}])
cue(type="question", t0=A("c01", "can") - 0.05, t1=A("c02", "that") - 0.05, at=A("c01", "can"),
    text="Can a court freeze things today?", hl="freeze things today?")
cue(type="section", t0=A("c02", "that") - 0.05, t1=E("c02") + 0.05, at=A("c02", "that"), act="CPC, 1908", num="Order XXXIX",
    title="Temporary Injunctions and Interlocutory Orders",
    points=[{"text": "A temporary injunction", "at": A("c02", "temporary")}])
cue(type="flow", t0=S("c03"), t1=E("c03") + 0.05, head="A temporary injunction", head_at=S("c03") + 0.05,
    steps=[{"label": "An interim order", "sub": "made while the suit is pending", "icon": "gavel", "at": A("c03", "interim")},
           {"label": "Preserves the position", "sub": "for the time being", "icon": "lock", "at": A("c03", "preserving")},
           {"label": "Until the rights are decided", "icon": "scale", "at": A("c03", "rights")}])
cue(type="cite", t0=A("c03", "pending"), t1=E("c03") + 0.05, at=A("c03", "pending"), tag="SPECIFIC RELIEF ACT, 1963 · s. 37(1)",
    text="Temporary injunctions continue “until a specific time, or until the further order of the court”", icon="book-open")
cue(type="splitcard", t0=S("c04"), t1=E("c04") + 0.05,
    left={"title": "SECTION 94(c) CPC", "text": "gives the power", "icon": "landmark", "at": A("c04", "section")},
    right={"title": "ORDER XXXIX", "text": "sets out how it is used", "icon": "list-ordered", "at": A("c04", "order")})
cue(type="cite", t0=S("c04") + 0.3, t1=E("c04") + 0.05, at=S("c04") + 0.3, tag="CPC, 1908 · SECTION 94",
    text="“In order to prevent the ends of justice from being defeated”", icon="book-open")
cue(type="compare", t0=S("c05"), t1=E("c05") + 0.05, head="Temporary or perpetual?", head_at=S("c05") + 0.05,
    cols=[{"title": "Temporary", "icon": "clock", "at": S("c05") + 0.15},
          {"title": "Perpetual", "icon": "gavel", "at": A("c05", "perpetual")}],
    rows=[{"cells": ["At any stage of a suit, until a specific time or further order", "Only by the decree, at the hearing and on the merits"],
           "cells_at": [S("c05") + 0.4, A("c05", "decree")]}])
cue(type="cite", t0=A("c05", "contrast"), t1=E("c05") + 0.05, at=A("c05", "contrast"), tag="SPECIFIC RELIEF ACT, 1963 · s. 37(2) · s. 38",
    text="“A perpetual injunction can only be granted by the decree made at the hearing and upon the merits of the suit”", icon="book-open")

# ── 2 · when Rules 1 and 2 apply ─────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="kicker", t0=S("c06"), t1=E("c06") + 0.05, at=S("c06") + 0.05, text=HYP)
cue(type="flow", t0=S("c06"), t1=E("c06") + 0.05, head="Anita v. Naresh", head_at=S("c06") + 0.1,
    steps=[{"label": "Anita sues Naresh", "sub": "her neighbour", "icon": "users", "at": A("c06", "anita")},
           {"label": "A strip of land", "sub": "in dispute in the suit", "icon": "map-pin", "at": A("c06", "strip")},
           {"label": "He starts digging", "sub": "foundations on the strip", "icon": "house", "at": A("c06", "digging")}])
cue(type="section", t0=S("c07"), t1=E("c07") + 0.05, at=A("c07", "rule"), act="CPC, 1908", num="Order XXXIX Rule 1",
    title="Clause (a): property in dispute",
    points=[{"text": "In danger of being wasted, damaged or alienated by any party to the suit", "at": A("c07", "danger")},
            {"text": "Or wrongfully sold in execution of a decree", "at": A("c07", "wrongfully")}])
cue(type="cite", t0=A("c07", "covers"), t1=E("c08") + 0.05, at=A("c07", "covers"), tag="ORDER XXXIX RULE 1",
    text="“Where in any suit it is proved by affidavit or otherwise”", icon="book-open")
cue(type="flow", t0=S("c08"), t1=E("c08") + 0.05, head="Clause (b): the defendant's own property", head_at=S("c08") + 0.05,
    steps=[{"label": "The defendant threatens, or intends", "icon": "user-round", "at": A("c08", "threatens")},
           {"label": "To remove or dispose of his property", "icon": "briefcase", "at": A("c08", "remove")},
           {"label": "With a view to defrauding his creditors", "icon": "triangle-alert", "at": A("c08", "defraud")}])
cue(type="section", t0=S("c09"), t1=E("c09") + 0.05, at=S("c09") + 0.1, act="CPC, 1908", num="Order XXXIX Rule 1",
    title="Clause (c): threats to the plaintiff",
    points=[{"text": "The defendant threatens to dispossess the plaintiff", "at": A("c09", "dispossess")},
            {"text": "Or otherwise cause injury to the plaintiff in relation to any property in dispute", "at": A("c09", "injury")}],
    note={"text": "Hypothetical: Anita's case fits clause (c)", "icon": "info", "at": A("c09", "fits")})
cue(type="cite", t0=S("c09") + 0.1, t1=E("c09") + 0.05, at=S("c09") + 0.1, tag="ORDER XXXIX RULE 1 · THE COURT MAY GRANT",
    text="A temporary injunction, or “such other order … as the Court thinks fit”", icon="book-open")
cue(type="section", t0=S("c10"), t1=E("c10") + 0.05, at=A("c10", "rule"), act="CPC, 1908", num="Order XXXIX Rule 2",
    title="Restraining a breach or injury",
    points=[{"text": "A suit for restraining a breach of contract or other injury of any kind", "at": A("c10", "restrain")},
            {"text": "Rule 2(2) terms: duration, keeping an account, giving security, or otherwise", "at": A("c10", "terms")}])

# ── 3 · the three tests ──────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c11"), t1=A("c11", "in") - 0.05, text="Fitting Rule 1 or Rule 2 is only the start",
    icon="search-check", accent=True, at=S("c11") + 0.1)
cue(type="list", t0=A("c11", "in") - 0.05, t1=E("c11") + 0.05, head="Three tests", head_at=A("c11", "in"),
    items=[{"n": 1, "text": "A prima facie case", "at": A("c11", "supreme")},
           {"n": 2, "text": "Irreparable injury", "at": A("c11", "explained")},
           {"n": 3, "text": "The balance of convenience", "at": A("c11", "three")}])
cue(type="cite", t0=A("c11", "dalpat"), t1=E("c14") + 0.05, at=A("c11", "dalpat"), tag=f"{SC} · 16.12.1991",
    cases=[{"name": DALPAT, "cite": "paras 4–5"}])
cue(type="kicker", t0=S("c12"), t1=A("c12", "it") - 0.05, at=S("c12") + 0.05, text="TEST 1 · A PRIMA FACIE CASE")
cue(type="quote", t0=S("c12"), t1=A("c12", "it") - 0.05, at=S("c12") + 0.1, reveal=2.6,
    text="a substantial question raised, bona fide, which needs investigation and a decision on merits",
    hl=["substantial question", "bona fide"])
# the plan's gap check reads a notequal's `at` only (not left_at): `at` sits on "not", the left half from "It"
cue(type="notequal", t0=A("c12", "it") - 0.05, t1=E("c12") + 0.05, left="Prima facie case", right="prima facie title",
    at=A("c12", "not"), left_at=A("c12", "it"),
    sub="Title must be proved by evidence at the trial", sub_at=A("c12", "proved"))
cue(type="kicker", t0=S("c13"), t1=A("c13", "prima") - 0.05, at=S("c13") + 0.05, text="TEST 2 · IRREPARABLE INJURY")
cue(type="quote", t0=S("c13"), t1=A("c13", "prima") - 0.05, at=S("c13") + 0.1, reveal=2.8,
    text="the injury must be a material one, namely one that cannot be adequately compensated by way of damages",
    hl=["a material one", "adequately compensated"])
cue(type="strike", t0=A("c13", "prima") - 0.05, t1=E("c13") + 0.05, text="A prima facie case alone is enough", icon="scale",
    at=A("c13", "prima"), strike_at=A("c13", "not"))
cue(type="compare", t0=S("c14"), t1=E("c14") + 0.05, head="Test 3: the balance of convenience", head_at=S("c14") + 0.05,
    cols=[{"title": "If relief is refused", "icon": "user-round", "at": A("c14", "compares")},
          {"title": "If relief is granted", "icon": "users", "at": A("c14", "mischief")}],
    rows=[{"cells": ["The mischief to the applicant", "The mischief to the other side"],
           "cells_at": [A("c14", "refused"), A("c14", "granted")]}])
cue(type="kicker", t0=S("c15"), t1=E("c15") + 0.05, at=S("c15") + 0.05, text=HYP)
cue(type="compare", t0=S("c15"), t1=E("c15") + 0.05, head="Applying the tests", head_at=S("c15") + 0.1,
    cols=[{"title": "Prima facie case", "icon": "file-text", "at": A("c15", "sale")},
          {"title": "Balance of convenience", "icon": "scale", "at": A("c15", "pause")}],
    rows=[{"cells": ["Her sale deed raises a serious question: not proof of ownership", "Naresh: a short pause · Anita: a permanent structure"],
           "cells_at": [A("c15", "raises"), A("c15", "permanent")]}])

# ── 4 · conduct matters ──────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="verdicts", t0=S("c16"), t1=E("c16") + 0.05,
    rows=[{"text": "The tests met: an injunction follows automatically", "ok": False, "at": S("c16") + 0.1, "strike_at": A("c16", "discretionary")},
          {"text": "Discretionary and equitable: conduct counts", "ok": True, "at": A("c16", "conduct")}])
cue(type="cite", t0=A("c16", "relief"), t1=E("c16") + 0.05, at=A("c16", "relief"), tag=f"{SC} · 16.12.1991",
    cases=[{"name": DALPAT, "cite": "paras 4 and 6"}])
cue(type="quote", t0=S("c17"), t1=E("c17") + 0.05, at=S("c17") + 0.1, reveal=3.4,
    text="… may refuse to interfere unless his conduct was free from blame … His conduct should be fair and honest",
    hl=["free from blame", "fair and honest"])
cue(type="cite", t0=A("c17", "gujarat"), t1=E("c17") + 0.05, at=A("c17", "gujarat"), tag=f"{SC} · 04.08.1995",
    cases=[{"name": "Gujarat Bottling Co. Ltd. v. Coca Cola Co.", "cite": "para 47"}])
cue(type="kicker", t0=S("c18"), t1=E("c18") + 0.05, at=S("c18") + 0.05, text=HYP)
cue(type="list", t0=S("c18"), t1=E("c18") + 0.05, head="Can count against Anita", head_at=S("c18") + 0.05,
    items=[{"n": "!", "text": "Hiding a material fact", "at": A("c18", "hiding")},
           {"n": "!", "text": "Waiting months while the walls rise", "at": A("c18", "waiting")}])
cue(type="cite", t0=A("c18", "fact"), t1=E("c18") + 0.05, at=A("c18", "fact"), tag="CPC, 1908 · SECTION 95",
    text="Applied for on insufficient grounds? Compensation up to ₹50,000 may be awarded", icon="info")

# ── 5 · without notice: ex parte orders ──────────────────────────────────────────────────────────────────────────────────────────
cue(type="kicker", t0=S("c19"), t1=E("c19") + 0.05, at=S("c19") + 0.05, text=HYP)
cue(type="point", t0=S("c19"), t1=A("c19", "must") - 0.05, text="Naresh plans to pour the concrete tomorrow morning",
    icon="clock", at=A("c19", "now"))
cue(type="question", t0=A("c19", "must") - 0.05, t1=E("c19") + 0.05, at=A("c19", "must"),
    text="Must the court hear Naresh first?", hl="hear Naresh first?")
cue(type="section", t0=S("c20"), t1=A("c21", "in") - 0.05, at=A("c20", "rule"), act="CPC, 1908", num="Order XXXIX Rule 3",
    title="Before granting an injunction",
    points=[{"text": "Notice of the application to the opposite party, in all cases", "at": A("c20", "notice")},
            {"text": "Except where the object of granting the injunction would be defeated by the delay", "at": A("c20", "unless")},
            {"text": "Without notice: the court shall record its reasons", "at": A("c21", "without")}])
cue(type="quote", t0=A("c21", "in") - 0.05, t1=E("c21") + 0.05, at=A("c21", "in"), reveal=2.2,
    text="ex parte injunction could be granted only under exceptional circumstances", hl=["only under exceptional circumstances"])
cue(type="cite", t0=A("c21", "morgan"), t1=E("c21") + 0.05, at=A("c21", "morgan"), tag=f"{SC} · 20.05.1994",
    cases=[{"name": MORGAN, "cite": "para 36"}])
cue(type="checklist", t0=S("c22"), t1=E("c22") + 0.05, head="Deliver, or send by registered post", head_at=S("c22") + 0.05,
    items=[{"n": 1, "text": "A copy of the application", "at": A("c22", "application")},
           {"n": 2, "text": "The supporting affidavit", "at": A("c22", "affidavit")},
           {"n": 3, "text": "The plaint", "at": A("c22", "plaint")},
           {"n": 4, "text": "The documents relied on", "at": A("c22", "documents")}])
cue(type="cite", t0=A("c22", "deliver"), t1=E("c22") + 0.05, at=A("c22", "deliver"), tag="ORDER XXXIX RULE 3 · PROVISO (a)",
    text="“immediately after the order granting the injunction has been made”", icon="book-open")
cue(type="timeline", t0=S("c23"), t1=E("c23") + 0.05,
    nodes=[{"label": "INJUNCTION GRANTED", "value": "That day", "sub": "file the affidavit", "at": A("c23", "day")},
           {"label": "OR, AT THE LATEST", "value": "The next day", "sub": "the day immediately following", "at": A("c23", "next")}])
cue(type="cite", t0=S("c23") + 0.1, t1=E("c23") + 0.05, at=S("c23") + 0.1, tag="ORDER XXXIX RULE 3 · PROVISO (b)",
    text="An affidavit that the copies were delivered or sent", icon="book-open")
cue(type="counters", t0=S("c24"), t1=E("c24") + 0.05, head="Rule 3A: the court shall make an endeavour", head_at=S("c24") + 0.05,
    items=[{"value": 30, "unit": "DAYS", "label": "To finally dispose of the application", "sub": "from the date the injunction was granted",
            "at": A("c24", "thirty")}],
    note={"text": "If not, the court records its reasons", "icon": "file-pen-line", "at": A("c24", "record")})

# ── 6 · challenging the order ────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c25"), t1=E("c25") + 0.05, at=S("c25") + 0.1, act="CPC, 1908", num="Order XXXIX Rule 4",
    title="Discharge, vary or set aside",
    points=[{"text": "Any order for an injunction", "at": A("c25", "under")},
            {"text": "On the application of any party dissatisfied with it", "at": A("c25", "dissatisfied")}])
# the second proviso's footer stays under c25: with its two-line bar under c26 the vertical flow shrank its labels below its subs
cue(type="cite", t0=A("c25", "four"), t1=E("c25") + 0.05, at=A("c25", "four"), tag="ORDER XXXIX RULE 4 · SECOND PROVISO",
    text="Made after hearing a party? On that party's application, only for changed circumstances or undue hardship", icon="info")
cue(type="flow", t0=S("c26"), t1=E("c26") + 0.05, head="Rule 4, first proviso", head_at=S("c26") + 0.05, dir="v",
    steps=[{"label": "An injunction granted without notice", "icon": "gavel", "at": A("c26", "ex")},
           {"label": "A knowingly false or misleading statement", "sub": "in relation to a material particular", "icon": "triangle-alert",
            "at": A("c26", "knowingly")},
           {"label": "The court shall vacate the injunction", "sub": "unless, for reasons recorded, it is not necessary in the interests of justice",
            "icon": "scale", "at": A("c26", "vacated")}])

# ── 7 · if the order is disobeyed ────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c27"), t1=E("c27") + 0.05, head="Rule 2A: disobedience or breach", head_at=S("c27") + 0.05,
    steps=[{"label": "An order under Rule 1 or 2 is disobeyed", "icon": "ban", "at": A("c27", "keeps")},
           {"label": "The court may order attachment", "sub": "of the property", "icon": "landmark", "at": A("c27", "attach")},
           {"label": "It may order civil prison", "sub": "up to three months", "icon": "lock", "at": A("c27", "detain")}])
cue(type="cite", t0=A("c27", "rule"), t1=E("c27") + 0.05, at=A("c27", "rule"), tag="ORDER XXXIX RULE 2A(1)",
    text="“not exceeding three months, unless in the meantime the Court directs his release”", icon="book-open")
cue(type="timeline", t0=S("c28"), t1=E("c28") + 0.05,
    nodes=[{"label": "ATTACHMENT", "value": "Up to 1 year", "sub": "never in force longer", "at": A("c28", "attachment")},
           {"label": "IF THE BREACH CONTINUES", "value": "May be sold", "sub": "the attached property", "at": A("c28", "sold")},
           {"label": "THE COURT MAY AWARD", "value": "Compensation", "sub": "to the injured party", "at": A("c28", "injured")}])

# ── 8 · appeals ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c29"), t1=E("c29") + 0.05, at=S("c29") + 0.1, act="CPC, 1908", num="Order XLIII Rule 1(r)",
    title="Appeals from orders",
    points=[{"text": "An order under rule 1, rule 2, rule 2A, rule 4 or rule 10 of Order XXXIX", "at": A("c29", "rules")}],
    note={"text": "Read with Section 104(1)(i)", "icon": "book-open", "at": A("c29", "forty")})
cue(type="strike", t0=S("c30"), t1=E("c30") + 0.05, text="The appeal court substitutes its own discretion", icon="landmark",
    at=A("c30", "wander"), strike_at=A("c30", "substitute"))
cue(type="point", t0=A("c30", "discretion"), t1=E("c30") + 0.05, text="An appeal on principle", icon="scale", accent=True,
    at=A("c30", "discretion"))
cue(type="cite", t0=A("c30", "wander"), t1=E("c31") + 0.05, at=A("c30", "wander"), tag=f"{SC} · 26.04.1990",
    cases=[{"name": "Wander Ltd. v. Antox India P. Ltd.", "cite": "para 14"}])
cue(type="list", t0=S("c31"), t1=E("c31") + 0.05, head="Interference only if", head_at=S("c31") + 0.05,
    items=[{"n": 1, "text": "Discretion exercised arbitrarily", "at": A("c31", "arbitrarily")},
           {"n": 2, "text": "Or capriciously, or perversely", "at": A("c31", "capriciously")},
           {"n": 3, "text": "Or settled principles ignored", "at": A("c31", "settled")}])

# ── 9 · mandatory relief and legal bars ──────────────────────────────────────────────────────────────────────────────────────────
cue(type="kicker", t0=S("c32"), t1=E("c32") + 0.05, at=S("c32") + 0.05, text=HYP)
cue(type="flow", t0=S("c32"), t1=E("c32") + 0.05, head="The wall is already up", head_at=S("c32") + 0.1,
    steps=[{"label": "The wall is built", "sub": "before any order", "icon": "house", "at": A("c32", "wall")},
           {"label": "Anita wants it pulled down", "sub": "now, before the trial", "icon": "users", "at": A("c32", "pulled")},
           {"label": "A mandatory interim injunction", "icon": "gavel", "at": A("c32", "mandatory")}])
cue(type="compare", t0=S("c33"), t1=E("c33") + 0.05, head="Mandatory relief: a higher standard", head_at=S("c33") + 0.05,
    cols=[{"title": "Mandatory, interim", "icon": "triangle-alert", "at": A("c33", "supreme")},
          {"title": "Prohibitory", "icon": "ban", "at": A("c33", "higher")}],
    rows=[{"cells": ["A strong case for trial", "A prima facie case, normally"], "cells_at": [A("c33", "strong"), A("c33", "prima")]}])
cue(type="cite", t0=A("c33", "dorab"), t1=E("c34") + 0.05, at=A("c33", "dorab"), tag=f"{SC} · 13.02.1990",
    cases=[{"name": "Dorab Cawasji Warden v. Coomi Sorab Warden", "cite": "paras 16–17"}])
cue(type="checklist", t0=S("c34"), t1=E("c34") + 0.05, head="Guidelines, not exhaustive", head_at=S("c34") + 0.05,
    items=[{"n": 1, "text": "A strong case for trial", "at": S("c34") + 0.3},
           {"n": 2, "text": "Irreparable or serious injury", "at": A("c34", "irreparable")},
           {"n": 3, "text": "Balance of convenience for the applicant", "at": A("c34", "balance")}])
# one card for the whole clip: (h) lands early enough to be read; "its bars reach interim relief too" is its note (Cotton Corporation bar)
cue(type="section", t0=S("c35"), t1=E("c35") + 0.05, at=A("c35", "section"), act="SRA, 1963", num="41",
    title="“An injunction cannot be granted”",
    points=[{"text": "In the cases in clauses (a) to (j), including (ha)", "at": A("c35", "relief")},
            {"text": "(h) “when equally efficacious relief can certainly be obtained by any other usual mode of proceeding except in case of breach of trust”",
             "at": A("c35", "lists")}],
    note={"text": "Its bars reach interim relief too", "icon": "ban", "at": A("c35", "its")})
cue(type="cite", t0=A("c35", "its"), t1=E("c35") + 0.05, at=A("c35", "its"), tag=f"{SC} · 19.09.1983",
    cases=[{"name": "Cotton Corporation of India v. United Industrial Bank", "cite": "Supreme Court, 1983"}])

# ── 10 · drafting the application ────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c36"), t1=E("c36") + 0.05, head="Prove each test", head_at=S("c36") + 0.05,
    steps=[{"label": "Each of the three tests", "sub": "case · injury · convenience", "icon": "list-ordered", "at": A("c36", "prove")},
           {"label": "Documents", "sub": "the papers behind each one", "icon": "file-text", "at": A("c36", "documents")},
           {"label": "An affidavit", "sub": "supporting the application", "icon": "file-pen-line", "at": A("c36", "affidavit")}])
cue(type="cite", t0=A("c36", "since"), t1=E("c36") + 0.05, at=A("c36", "since"), tag="ORDER XXXIX RULE 1",
    text="“proved by affidavit or otherwise”", icon="book-open")
cue(type="checklist", t0=S("c37"), t1=E("c37") + 0.05, head="Seeking it without notice?", head_at=S("c37") + 0.05,
    items=[{"n": 1, "text": "Show the urgency", "at": A("c37", "urgency")},
           {"n": 2, "text": "Disclose every material fact", "at": A("c37", "disclose")},
           {"n": 3, "text": "Finish the Rule 3 steps on time", "at": A("c37", "finish")}])
cue(type="cite", t0=A("c37", "disclose"), t1=E("c37") + 0.05, at=A("c37", "disclose"), tag=f"{SC} · 20.05.1994",
    cases=[{"name": MORGAN, "cite": "para 36: utmost good faith"}])
cue(type="point", t0=S("c38"), t1=E("c38") + 0.05, text="Check any local High Court amendments to Order XXXIX before you file",
    icon="search-check", accent=True, at=A("c38", "finally"))
cue(type="point", t0=S("c39"), t1=E("c39") + 0.05, text="Like · Share · Subscribe · lawworld.ai",
    icon="check", accent=True, at=A("c39", "thanks"))
