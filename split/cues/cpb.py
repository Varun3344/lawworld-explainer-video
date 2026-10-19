# Compounding and Plea Bargaining (BNSS): panel cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND).
# Storyboard: ~/Downloads/Compounding_and_Plea_Bargaining_BNSS_Storyboard.pdf. Fact-check 19-10-2026: every section, table, time
# limit and fraction matches the Gazette text; 290(1) "may file" within 30 days of framing of charge (Rohan: a warrant case);
# compounding is still placed before the court; murder (BNS 103) is in neither table.
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

STING = {"kicker": "CRIMINAL PROCEDURE · BNSS EXPLAINED", "title": "Compounding and Plea Bargaining", "sub": "Two ways a case may end without a full trial"}
ENDCARD = {"title": "Compounding and Plea Bargaining", "line": "Compounding ≠ plea bargaining", "sub": "Next lesson: Criminal Appeals and Revisions"}

# ── 1 · two ways out ─────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="compare", t0=S("c01"), t1=E("c02") + 0.05, head="Two ways a case may end", head_at=S("c01") + 0.1,
    cols=[{"title": "Ravi and Mohan", "icon": "handshake", "at": A("c01", "ravi")}, {"title": "Rohan", "icon": "user-round", "at": A("c01", "rohan")}],
    rows=[{"cells": ["Settle after a fight", "Accepts responsibility"], "cells_at": [A("c01", "settle"), A("c01", "accept")]},
          {"cells": ["A compromise", "A lawful reduction in punishment"], "cells_at": [A("c02", "lawful") - 0.2, A("c02", "lawful")]}],
    verdict={"text": "Are these the same thing?", "icon": "circle-help", "at": A("c02", "are")})
cue(type="splitcard", t0=S("c03"), t1=E("c03") + 0.05,
    left={"title": "COMPOUNDING", "text": "BNSS § 359", "icon": "handshake", "at": A("c03", "compounding")},
    right={"title": "PLEA BARGAINING", "text": "BNSS §§ 289–300", "icon": "scale", "at": A("c03", "plea")})
cue(type="compare", t0=S("c04"), t1=E("c04") + 0.05, head="Different outcomes", head_at=A("c04", "one"),
    cols=[{"title": "Compounding", "icon": "handshake", "at": A("c04", "one")}, {"title": "Plea bargaining", "icon": "scale", "at": A("c04", "supervised") - 0.3}],
    rows=[{"cells": ["Effect of an acquittal", "Supervised by the court"], "cells_at": [A("c04", "acquittal"), A("c04", "supervised")]},
          {"cells": ["The case ends", "May end in conviction, with a reduced sentence"], "cells_at": [A("c04", "acquittal") + 0.5, A("c04", "conviction")]}])

# ── 2 · the statutory list ───────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c05"), t1=E("c05") + 0.05, at=A("c05", "section"), act="BNSS", num="359", title="Compounding of offences",
    points=[{"text": "Its tables list the offences that can be compounded", "at": A("c05", "lists")},
            {"text": "…and who may compound each one", "at": A("c05", "who")},
            {"text": "The person named in the table must agree", "at": A("c05", "agree")}])
cue(type="flow", t0=S("c06"), t1=E("c07") + 0.05, head="Simple hurt", head_at=A("c06", "suppose"),
    steps=[{"label": "BNS 115(2)", "sub": "voluntarily causing hurt", "icon": "scroll-text", "at": A("c06", "section")},
           {"label": "First table", "sub": "§ 359(1)", "icon": "list-ordered", "at": A("c07", "first")},
           {"label": "Mohan compounds", "sub": "no court permission needed", "icon": "handshake", "tone": "ok", "at": A("c07", "compound")}])
cue(type="point", t0=S("c08"), t1=E("c08") + 0.05, text="Placed before the court: a legal process, not a handshake", icon="gavel", accent=True, at=A("c08", "compromise"))

# ── 3 · court permission ─────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c09"), t1=E("c10") + 0.05, head="Grievous hurt", head_at=A("c09", "change"),
    steps=[{"label": "BNS 117(2)", "sub": "voluntarily causing grievous hurt", "icon": "scroll-text", "at": A("c09", "grievous")},
           {"label": "Second table", "sub": "§ 359(2)", "icon": "list-ordered", "at": A("c10", "second")},
           {"label": "Court's permission", "sub": "as well as Mohan's agreement", "icon": "gavel", "tone": "ok", "at": A("c10", "permission")}])
cue(type="section", t0=S("c11"), t1=E("c11") + 0.05, at=A("c11", "section"), act="BNSS", num="359(8)", title="Effect of lawful compounding",
    points=[{"text": "An acquittal of the accused concerned", "at": A("c11", "acquittal")}])
cue(type="compare", t0=S("c12"), t1=E("c12") + 0.05,
    cols=[{"title": "Simple hurt", "icon": "user-round", "at": A("c12", "simple")}, {"title": "Grievous hurt", "icon": "triangle-alert", "at": A("c12", "grievous")}],
    rows=[{"cells": ["BNS 115(2) · first table", "BNS 117(2) · second table"], "cells_at": [A("c12", "simple") + 0.3, A("c12", "grievous") + 0.3]},
          {"cells": ["The injured person compounds", "The court's permission is needed"], "cells_at": [A("c12", "compounding"), A("c12", "compounding") + 0.25]}],
    verdict={"text": "Always check the exact charge", "icon": "search-check", "at": A("c12", "always")})

# ── 4 · limits and stages ────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="strike", t0=S("c13"), t1=A("c13", "but") - 0.02, text="A general 30-day or 60-day deadline", icon="calendar", at=S("c13") + 0.05, strike_at=A("c13", "deadline") + 0.15)
cue(type="flow", t0=A("c13", "but"), t1=E("c14") + 0.05, head="But the stage matters", head_at=A("c13", "but"),
    steps=[{"label": "Prosecution", "icon": "file-text", "at": A("c13", "stage")},
           {"label": "Committed for trial", "sub": "court's leave · § 359(5)", "icon": "gavel", "at": A("c14", "commitment")},
           {"label": "Appeal after conviction", "sub": "court's leave · § 359(5)", "icon": "landmark", "at": A("c14", "appeal")}])
cue(type="strike", t0=S("c15"), t1=E("c15") + 0.05, text="Private settlement = every case ends", icon="handshake", at=A("c15", "private"), strike_at=A("c15", "every") + 0.3)
cue(type="cite", t0=A("c15", "murder"), t1=E("c15") + 0.05, at=A("c15", "murder"), tag="FOR EXAMPLE", text="Murder, BNS 103: outside the compounding tables", icon="book-open")
cue(type="point", t0=S("c16"), t1=E("c16") + 0.05, text="Check every charge, and the court process", icon="search-check", accent=True, at=A("c16", "before"))
cue(type="cite", t0=S("c16") + 0.1, t1=E("c16") + 0.05, at=S("c16") + 0.1, tag="ALSO CHECK", text="Special statutes may have their own compounding rules", icon="book-open")

# ── 5 · who can plea bargain ─────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c17"), t1=E("c19") + 0.05, at=A("c17", "eligibility"), act="BNSS", num="289", title="Who can plea bargain?",
    points=[{"text": "Not: death, life, or over seven years", "tone": "no", "at": A("c18", "death")},
            {"text": "Not: offences against women or children", "tone": "no", "at": A("c19", "women")},
            {"text": "Not: notified socio-economic offences", "tone": "no", "at": A("c19", "notified")}])
cue(type="verdicts", t0=S("c20"), t1=E("c21") + 0.05,
    rows=[{"text": "A juvenile or child accused (§ 300)", "ok": False, "at": A("c20", "juvenile"), "strike_at": E("c20") - 0.3},
          {"text": "An earlier conviction, same offence (§ 290)", "ok": False, "at": A("c21", "earlier"), "strike_at": A("c21", "obstacle")}])
cue(type="point", t0=S("c22"), t1=E("c22") + 0.05, text="Rohan must qualify first", icon="badge-check", accent=True, at=A("c22", "rohan"))

# ── 6 · the 30-day window ────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c23"), t1=E("c23") + 0.05, text="Rohan: an adult accused, an eligible property case", icon="user-round", at=A("c23", "assume"))
cue(type="counters", t0=S("c24"), t1=E("c24") + 0.05, head="The application window", head_at=A("c24", "under"),
    items=[{"value": 30, "unit": "DAYS", "label": "Apply to the trial court", "sub": "from framing of the charge · § 290(1)", "at": A("c24", "thirty")}])
cue(type="checklist", t0=S("c25"), t1=E("c26") + 0.05, head="His sworn affidavit", head_at=A("c25", "affidavit"),
    items=[{"n": 1, "text": "A voluntary choice", "at": A("c26", "voluntarily")}, {"n": 2, "text": "Understands the punishment", "at": A("c26", "understands")},
           {"n": 3, "text": "No previous conviction, same offence", "at": A("c26", "previous")}])
cue(type="verdicts", t0=S("c27"), t1=E("c27") + 0.05,
    rows=[{"text": "Charge framed: the clock starts", "ok": True, "at": A("c27", "framing")},
          {"text": "FIR registered", "ok": False, "at": A("c27", "f"), "strike_at": A("c27", "registered") + 0.3},
          {"text": "Arrest", "ok": False, "at": A("c27", "arrested") - 0.2, "strike_at": A("c27", "arrested") + 0.4}])

# ── 7 · the court's check ────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c28"), t1=E("c28") + 0.05, text="In private, the judge checks it is voluntary", icon="lock", at=A("c28", "judge"))
cue(type="counters", t0=S("c29"), t1=E("c30") + 0.05, head="A second, separate clock", head_at=A("c29", "if"),
    items=[{"value": 60, "unit": "DAYS", "label": "The court allows up to", "sub": "to work out a disposition · § 290(4)(a)", "at": A("c29", "sixty")}],
    note={"text": "It may include compensation and expenses for the victim", "icon": "indian-rupee", "at": A("c30", "compensation")})
cue(type="verdicts", t0=S("c31"), t1=E("c32") + 0.05,
    rows=[{"text": "60 days from arrest", "ok": False, "at": A("c31", "not"), "strike_at": A("c31", "arrest") + 0.25},
          {"text": "Case guaranteed over in 90 days", "ok": False, "at": A("c32", "guarantee"), "strike_at": A("c32", "ninety") + 0.3}])

# ── 8 · agreement or back to trial ───────────────────────────────────────────────────────────────────────────────────────────────
cue(type="list", t0=S("c33"), t1=E("c34") + 0.05, head="At the table (§ 291)", head_at=A("c33", "section"),
    items=[{"n": 1, "text": "Prosecutor", "at": A("c34", "prosecutor")}, {"n": 2, "text": "Investigating officer", "at": A("c34", "investigating")},
           {"n": 3, "text": "Accused", "at": A("c34", "accused")}, {"n": 4, "text": "Victim", "at": A("c34", "victim")}])
cue(type="compare", t0=S("c35"), t1=E("c35") + 0.05,
    cols=[{"title": "Agreement", "icon": "handshake", "at": A("c35", "signed") - 0.4}, {"title": "No agreement", "icon": "x", "at": A("c35", "not")}],
    rows=[{"cells": ["A report signed by all (§ 292)", "Back to the application stage"], "cells_at": [A("c35", "signed"), A("c35", "proceedings")]}])
cue(type="section", t0=S("c36"), t1=E("c36") + 0.05, at=A("c36", "section"), act="BNSS", num="299", title="Limited-use protection",
    points=[{"text": "Statements or facts in the application: used only for this chapter", "at": A("c36", "protects")}])
cue(type="verdicts", t0=S("c37"), t1=E("c37") + 0.05,
    rows=[{"text": "Forced to agree", "ok": False, "at": A("c37", "forced") - 0.3, "strike_at": A("c37", "agree") + 0.2},
          {"text": "Filing alone completes it", "ok": False, "at": A("c37", "filing"), "strike_at": A("c37", "complete") + 0.2}])

# ── 9 · the court decides ────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c38"), t1=E("c38") + 0.05, at=A("c38", "section"), act="BNSS", num="293", title="The court decides",
    points=[{"text": "Compensation for the victim", "at": A("c38", "compensation")}, {"text": "Probation, where applicable", "at": A("c38", "probation")}])
cue(type="kicker", t0=S("c39"), t1=E("c40") + 0.05, at=A("c39", "reduced"), text="§ 293(d) · NO MINIMUM · NEVER CONVICTED")
cue(type="point", t0=A("c39", "take"), t1=E("c39") + 0.05, text="No minimum sentence + never convicted before", icon="user-round", at=A("c39", "take"))
cue(type="equation", t0=S("c40"), t1=E("c40") + 0.05,
    terms=[{"text": "MAXIMUM: 3 YEARS", "at": A("c40", "maximum")}, {"op": "÷", "text": "6", "at": A("c40", "fraction")},
           {"op": "=", "text": "6 MONTHS", "result": True, "at": A("c40", "six")}])
cue(type="cite", t0=A("c40", "maximum"), t1=E("c40") + 0.05, at=A("c40", "maximum"), tag="ILLUSTRATION ONLY", text="The court decides; compensation and probation are considered too", icon="info")
cue(type="section", t0=S("c41"), t1=E("c41") + 0.05, at=A("c41", "statutory"), act="BNSS", num="293(c)", title="Where a statutory minimum applies",
    points=[{"text": "First-time offender: one-fourth of that minimum", "at": A("c41", "fourth")}])
cue(type="verdicts", t0=S("c42"), t1=E("c42") + 0.05,
    rows=[{"text": "Conditional court decisions", "ok": True, "at": A("c42", "conditional")},
          {"text": "A guaranteed, private discount", "ok": False, "at": A("c42", "not"), "strike_at": A("c42", "privately") + 0.2}])

# ── 10 · know the result ─────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c43"), t1=E("c44") + 0.05, at=A("c43", "section"), act="BNSS", num="294 · 295", title="The judgment",
    points=[{"text": "Delivered in open court (§ 294)", "at": A("c43", "delivered")},
            {"text": "Final: no ordinary appeal (§ 295)", "tone": "no", "at": A("c44", "appeal")},
            {"text": "Article 136 and Articles 226–227 remain", "at": A("c44", "constitutional")}])
cue(type="compare", t0=S("c45"), t1=E("c46") + 0.05, head="Remember the difference", head_at=S("c45") + 0.05,
    cols=[{"title": "Compounding", "icon": "handshake", "at": A("c45", "compounding")}, {"title": "Plea bargaining", "icon": "scale", "at": A("c46", "plea")}],
    rows=[{"cells": ["§ 359: effect of an acquittal", "§§ 289–300: conviction, with a sentencing benefit"], "cells_at": [A("c45", "acquittal"), A("c46", "conviction")]}])
cue(type="list", t0=S("c47"), t1=E("c47") + 0.05, head="Before agreeing", head_at=S("c47") + 0.05,
    items=[{"n": 1, "text": "Check eligibility", "at": A("c47", "check")}, {"n": 2, "text": "Independent advice", "at": A("c47", "independent")},
           {"n": 3, "text": "Know the consequences", "at": A("c47", "consequences")}])
cue(type="point", t0=S("c48"), t1=E("c48") + 0.05, text="No shortcut around the legal process", icon="scale", accent=True, at=A("c48", "neither"))
