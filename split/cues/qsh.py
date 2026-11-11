# Quashing under Section 528 BNSS - CONCEPT VIDEO (legal-concept explainer, Cause of Action build): panel cues, run by
# split/build_course_plan.py (helpers: at S E cue fx have r3 PEND). Script: split/scripts/qsh.txt (no owner storyboard; every legal
# point checked 10-11-2026 against the BNSS text and the judgments on Indian Kanoon - see the script's // header).
# Held to the script header's panel rules:
#  - quashing is EXCEPTIONAL: NO "QUASHED" stamp anywhere and no outcome promised; Kavya's case stays open ("the facts decide");
#  - Kavya (hypothetical) is labelled ACCUSED wherever she is named, never "cheat" or "forger"; Harish is the COMPLAINANT; the
#    story clips carry a "HYPOTHETICAL EXAMPLE" kicker;
#  - Bhajan Lal's seven categories: every category clip carries a kicker "... ILLUSTRATIVE, NOT EXHAUSTIVE" (c10-c16);
#    "rarest of rare" is not used;
#  - never "s.482" alone on a panel (s.482 BNSS = anticipatory bail): always "s.482 CrPC (old Code)"; every case named was decided
#    under the old Code, so each case bar says so;
#  - s.528 is shown VERBATIM on the c04 quote card (the narration paraphrases it); s.531(2)(a) (pending matters) is a footer only;
#  - compounding (s.359: the parties, the trial court) and quashing on settlement (s.528: the High Court's discretion) stay on
#    separate columns (c27);
#  - a dismissed petition is not a finding of guilt (c36); c34-c35 are drafting practice, not a statutory rule (footer).
# Case bars: name + court + decision date + paragraph only - never SCC / AIR / INSC (house rule: a case is shown by its LawWorld
# Citation ID, and none is confirmed for these cases). Paragraphs are the script header's primary numbers (where the header also
# gives an "as delivered" number, the primary one is printed). Neeharika's SCC paragraph is unconfirmed: its bar cites the
# numbered conclusions only. Hridaya Ranjan (c23) and Indian Oil v. NEPC (c24) are not named in the narration: footer only.
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

STING = {"kicker": "CRIMINAL PROCEDURE · BNSS EXPLAINED", "title": "Quashing under Section 528 BNSS",
         "sub": "When the High Court will end an FIR or a criminal case, and when it will refuse"}
ENDCARD = {"title": "Quashing under Section 528 BNSS", "line": "Prevents abuse of process · used sparingly · the facts decide",
           "sub": "LawWorld: legal research for advocates"}
SC = "SUPREME COURT OF INDIA"
OLD = "s.482 CrPC (old Code)"
KICK_BL = "BHAJAN LAL · {} · ILLUSTRATIVE, NOT EXHAUSTIVE"

# ── 1 · can an FIR be quashed? ───────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "can"),
    text="Can a High Court end a criminal case before trial?", hl="before trial?", y=215)   # 07-11 layout lesson: stamp clear below
cue(type="stamp", t0=A("c01", "yes") - 0.05, t1=E("c01") + 0.05, at=A("c01", "yes"), line1="YES, BUT RARELY",
    line2="“IT IS FALSE” IS NOT ENOUGH", y=900)
cue(type="list", t0=S("c02"), t1=E("c02") + 0.05, head="Two questions", head_at=S("c02") + 0.05,
    items=[{"n": 1, "text": "When will it quash an FIR or a case?", "at": A("c02", "when")},
           {"n": 2, "text": "When will it refuse?", "at": A("c02", "when", 2)}])
cue(type="section", t0=S("c03"), t1=E("c03") + 0.05, at=A("c03", "section"), act="BNSS, 2023", num="528",
    title="Saving of inherent powers of High Court",
    points=[{"text": "Bharatiya Nagarik Suraksha Sanhita", "at": A("c03", "bharatiya")},
            {"text": "Succeeds " + OLD, "at": A("c03", "succeeds")}],
    note={"text": "Not s.482 BNSS: that section is anticipatory bail", "icon": "alert-triangle", "at": A("c03", "eighty")})
cue(type="cite", t0=A("c03", "succeeds"), t1=E("c03") + 0.05, at=A("c03", "succeeds"), tag="PENDING MATTERS",   # tags are set in capitals: "(a)" would read "(A)"
    text="Matters pending on 1 July 2024 may still run under s.482 CrPC · BNSS 531(2)(a)", icon="book-open")

# ── 2 · what section 528 says ────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="quote", t0=S("c04"), t1=E("c04") + 0.05, at=A("c04", "nothing"), reveal=6.0,
    text="Nothing in this Sanhita shall be deemed to limit or affect the inherent powers of the High Court to make such orders as may "
         "be necessary to give effect to any order under this Sanhita, or to prevent abuse of the process of any Court or otherwise "
         "to secure the ends of justice.",
    hl=["give effect to any order under this Sanhita", "prevent abuse of the process of any Court", "secure the ends of justice"])
cue(type="cite", t0=S("c04") + 0.3, t1=E("c04") + 0.05, at=S("c04") + 0.3, tag="BNSS 528 · VERBATIM",
    text="The words of s.482 CrPC (old Code), with “Sanhita” for “Code”", icon="book-open")
cue(type="verdicts", t0=S("c05"), t1=E("c05") + 0.05,
    rows=[{"text": "Creates a new power", "ok": False, "at": A("c05", "creates"), "strike_at": A("c05", "power")},
          {"text": "Preserves the High Court's own inherent power", "ok": True, "at": A("c05", "preserves")}])
cue(type="cite", t0=S("c05") + 0.3, t1=E("c05") + 0.05, at=S("c05") + 0.3, tag=SC + " · 04.10.2017",
    cases=[{"name": "Parbatbhai Aahir v. State of Gujarat", "cite": "para 16.1 · " + OLD}])

# ── 3 · what can be quashed ──────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="list", t0=S("c06"), t1=E("c06") + 0.05, head="What can be quashed?", head_at=A("c06", "what"),
    items=[{"n": 1, "text": "The FIR and its investigation", "at": A("c06", "F")},
           {"n": 2, "text": "A charge sheet", "at": A("c06", "charge")},
           {"n": 3, "text": "A summoning order (s.227 BNSS)", "at": A("c06", "summoning")},
           {"n": 4, "text": "The proceedings themselves", "at": A("c06", "proceedings")}])
cue(type="strike", t0=S("c07"), t1=E("c07") + 0.05, text="A charge sheet closes the door", icon="file-text",
    at=S("c07") + 0.05, strike_at=A("c07", "close"))
cue(type="point", t0=S("c07"), t1=E("c07") + 0.05, text="Abuse of process may then be aggravated", icon="alert-triangle",
    accent=True, at=A("c07", "abuse"))
cue(type="cite", t0=A("c07", "anand"), t1=E("c07") + 0.05, at=A("c07", "anand"), tag=SC + " · 15.11.2018",
    cases=[{"name": "Anand Kumar Mohatta v. State (NCT of Delhi)", "cite": "para 17 · " + OLD}])
cue(type="quote", t0=S("c08"), t1=E("c08") + 0.05, at=A("c08", "pepsi"), reveal=2.6,
    text="Summoning of an accused in a criminal case is a serious matter.", hl=["serious matter"],
    note={"text": "The order must reflect an application of mind", "at": A("c08", "summoning")})
cue(type="cite", t0=A("c08", "pepsi"), t1=E("c08") + 0.05, at=A("c08", "pepsi"), tag=SC + " · 04.11.1997",
    cases=[{"name": "Pepsi Foods Ltd. v. Special Judicial Magistrate", "cite": "para 28 · " + OLD}])

# ── 4 · the Bhajan Lal categories ────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c09"), t1=E("c09") + 0.05, head="The leading case", head_at=S("c09") + 0.05,
    steps=[{"label": "State of Haryana v. Bhajan Lal", "sub": "Supreme Court of India", "icon": "landmark", "at": A("c09", "state")},
           {"label": "Article 226 and " + OLD, "sub": "both powers", "icon": "book-open", "at": A("c09", "old")},
           {"label": "Seven illustrative categories", "sub": "not an exhaustive list", "icon": "list-ordered", "tone": "ok", "at": A("c09", "seven")}])
# one case bar for the seven categories (para 102), handed over to para 103 at c16
cue(type="cite", t0=A("c09", "state"), t1=E("c15") + 0.05, at=A("c09", "state"), tag=SC + " · 21.11.1990",
    cases=[{"name": "State of Haryana v. Bhajan Lal", "cite": "para 102 · Art. 226 and " + OLD}])
for cid, lab in (("c10", "CATEGORY 1"), ("c11", "CATEGORIES 2 AND 3"), ("c12", "CATEGORY 4"), ("c13", "CATEGORY 5"),
                 ("c14", "CATEGORY 6"), ("c15", "CATEGORY 7"), ("c16", None)):
    cue(type="kicker", t0=S(cid), t1=E(cid) + 0.05, at=S(cid) + 0.08,
        text=KICK_BL.format(lab) if lab else "BHAJAN LAL · ILLUSTRATIVE, NOT EXHAUSTIVE")
cue(type="equation", t0=S("c10"), t1=E("c10") + 0.05,
    terms=[{"text": "ALLEGATIONS TAKEN AT FACE VALUE", "at": A("c10", "allegations")},
           {"op": "+", "text": "ACCEPTED IN FULL", "at": A("c10", "accepted")},
           {"op": "=", "text": "NO OFFENCE MADE OUT", "result": True, "at": A("c10", "make")}])
cue(type="compare", t0=S("c11"), t1=E("c11") + 0.05,
    cols=[{"title": "2 · No cognizable offence", "icon": "search", "at": A("c11", "two")},
          {"title": "3 · Uncontroverted material", "icon": "file-text", "at": A("c11", "three")}],
    rows=[{"cells": ["No cognizable offence disclosed", "Uncontroverted allegations and evidence"],
           "cells_at": [A("c11", "cognizable"), A("c11", "uncontroverted")]},
          {"cells": ["Nothing to justify a police investigation", "They disclose no offence"],
           "cells_at": [A("c11", "justify"), A("c11", "disclose", 2)]}])
cue(type="section", t0=S("c12"), t1=E("c12") + 0.05, at=A("c12", "four"), act="BNSS, 2023", num="174(2)",
    title="A non-cognizable case",
    points=[{"text": "Only a non-cognizable offence disclosed", "at": A("c12", "only")},
            {"text": "No police investigation without a Magistrate's order", "at": A("c12", "magistrate")}],
    note={"text": "Successor of s.155(2) CrPC (old Code), which Bhajan Lal cites", "icon": "info", "at": A("c12", "police")})
cue(type="flow", t0=S("c13"), t1=E("c13") + 0.05, head="The allegations are", head_at=S("c13") + 0.05,
    steps=[{"label": "So absurd", "icon": "alert-triangle", "at": A("c13", "absurd")},
           {"label": "Inherently improbable", "icon": "search", "at": A("c13", "improbable")},
           {"label": "No sufficient ground to proceed", "sub": "for any prudent person", "icon": "scale", "tone": "ok", "at": A("c13", "prudent")}])
cue(type="splitcard", t0=S("c14"), t1=E("c14") + 0.05,
    left={"title": "AN EXPRESS LEGAL BAR", "text": "to starting or continuing the case", "icon": "ban", "at": A("c14", "six")},
    right={"title": "OR A SPECIFIC REMEDY", "text": "a provision giving effective redress", "icon": "scale", "at": A("c14", "specific")})
cue(type="checklist", t0=S("c15"), t1=E("c15") + 0.05, head="Mala fide proceedings", head_at=S("c15") + 0.05,
    items=[{"n": "A", "text": "Manifestly mala fide", "at": A("c15", "manifestly")},
           {"n": "B", "text": "Or maliciously filed, to wreak vengeance out of a private, personal grudge", "at": A("c15", "maliciously")}])
cue(type="strike", t0=S("c16"), t1=E("c16") + 0.05, text="An exhaustive list", icon="list-ordered",
    at=S("c16") + 0.05, strike_at=A("c16", "exhaustive"))
cue(type="point", t0=S("c16"), t1=E("c16") + 0.05, text="Use the power very sparingly, with circumspection", icon="scale",
    accent=True, at=A("c16", "power"))
cue(type="cite", t0=S("c16") + 0.05, t1=E("c17") + 0.05, at=S("c16") + 0.05, tag=SC + " · 21.11.1990",
    cases=[{"name": "State of Haryana v. Bhajan Lal", "cite": "para 103 · " + OLD}])

# ── 5 · what the High Court will not do ──────────────────────────────────────────────────────────────────────────────────────────
cue(type="verdicts", t0=S("c17"), t1=E("c17") + 0.05,
    rows=[{"text": "Hold a mini-trial", "ok": False, "at": A("c17", "does"), "strike_at": A("c17", "mini") + 0.3},
          {"text": "Test whether the allegations are true", "ok": False, "at": A("c17", "test"), "strike_at": A("c17", "true")},
          {"text": "Disputed defences: left for trial", "ok": True, "at": A("c17", "disputed")}])
cue(type="point", t0=S("c18"), t1=A("c18", "quashing") - 0.05, text="Courts should not thwart the investigation", icon="search",
    at=A("c18", "neeharika"))
cue(type="notequal", t0=A("c18", "quashing") - 0.05, t1=E("c18") + 0.05, left="Quashing", right="the ordinary rule",
    at=A("c18", "quashing"), left_at=A("c18", "quashing"), sub="It is the exception", sub_at=A("c18", "exception"), icon="scale")
cue(type="cite", t0=A("c18", "neeharika"), t1=E("c18") + 0.05, at=A("c18", "neeharika"), tag=SC + " · 13.04.2021 · THREE JUDGES",
    cases=[{"name": "Neeharika Infrastructure v. State of Maharashtra", "cite": "conclusions (ii), (vii) · " + OLD}])
cue(type="compare", t0=S("c19"), t1=E("c19") + 0.05, head="Interim protection: not routine", head_at=S("c19") + 0.05,
    cols=[{"title": "An interim stay", "icon": "clock", "at": A("c19", "stay")},
          {"title": "“No coercive steps”", "icon": "shield-check", "at": A("c19", "coercive")}],
    rows=[{"cells": ["Needs brief reasons", "Must say what it means"], "cells_at": [A("c19", "brief"), A("c19", "say")]}])
cue(type="cite", t0=S("c19") + 0.05, t1=E("c19") + 0.05, at=S("c19") + 0.05, tag=SC + " · 13.04.2021 · THREE JUDGES",
    cases=[{"name": "Neeharika Infrastructure v. State of Maharashtra", "cite": "conclusions (xvi)–(xviii)"}])

# ── 6 · a business dispute with a criminal colour (hypothetical) ─────────────────────────────────────────────────────────────────
cue(type="kicker", t0=S("c20"), t1=E("c21") + 0.05, at=S("c20") + 0.08, text="HYPOTHETICAL EXAMPLE")
cue(type="timeline", t0=S("c20"), t1=E("c20") + 0.05,
    nodes=[{"label": "HARISH · COMPLAINANT", "value": "Pays an advance", "sub": "for furniture", "at": A("c20", "pays")},
           {"label": "KAVYA · ACCUSED", "value": "Delivers late", "tone": "red", "at": A("c20", "delivery")},
           {"label": "HARISH · COMPLAINANT", "value": "Withholds the balance", "at": A("c20", "withholds")}])
cue(type="flow", t0=S("c21"), t1=E("c21") + 0.05,
    steps=[{"label": "A civil suit", "sub": "not pursued", "icon": "scale", "tone": "muted", "at": A("c21", "instead")},
           {"label": "An FIR: cheating and forgery", "sub": "by Harish, the complainant", "icon": "file-text", "at": A("c21", "files")},
           {"label": "A petition to quash it", "sub": "by Kavya, the accused", "icon": "landmark", "at": A("c21", "kavya")}])
cue(type="question", t0=S("c22"), t1=E("c22") + 0.05, at=A("c22", "tells"),
    text="Is a civil dispute given “a cloak of criminal offence”?", hl="cloak of criminal offence")
cue(type="cite", t0=A("c22", "paramjeet"), t1=E("c22") + 0.05, at=A("c22", "paramjeet"), tag=SC + " · 14.12.2012",
    cases=[{"name": "Paramjeet Batra v. State of Uttarakhand", "cite": "para 12 · " + OLD}])
cue(type="notequal", t0=S("c23"), t1=E("c23") + 0.05, left="A mere breach of contract", right="cheating",
    at=A("c23", "supreme"), left_at=A("c23", "supreme"),
    sub="Unless dishonest intention existed at the start", sub_at=A("c23", "without"), icon="search")
cue(type="cite", t0=A("c23", "supreme"), t1=E("c23") + 0.05, at=A("c23", "supreme"), tag=SC + " · 2000",
    cases=[{"name": "Hridaya Ranjan Prasad Verma v. State of Bihar", "cite": "para 15"}])
cue(type="equation", t0=S("c24"), t1=E("c24") + 0.05,
    terms=[{"text": "A CIVIL DISPUTE", "at": A("c24", "civil")},
           {"op": "+", "text": "SPECIFIC FACTS OF FORGERY IN THE FIR", "at": A("c24", "specific")},
           {"op": "=", "text": "THE CASE MAY PROCEED", "result": True, "at": A("c24", "case")}])
cue(type="cite", t0=S("c24") + 0.05, t1=E("c24") + 0.05, at=S("c24") + 0.05, tag=SC + " · 2006",
    cases=[{"name": "Indian Oil Corpn. v. NEPC India Ltd.", "cite": "paras 12(v) and 13"}])

# ── 7 · settlement in non-compoundable cases ─────────────────────────────────────────────────────────────────────────────────────
cue(type="kicker", t0=S("c25"), t1=E("c25") + 0.05, at=S("c25") + 0.08, text="HYPOTHETICAL EXAMPLE")
cue(type="flow", t0=S("c25"), t1=E("c25") + 0.05, head="Now suppose they settle", head_at=A("c25", "now"),
    steps=[{"label": "Part of the advance refunded", "sub": "by Kavya, the accused", "icon": "indian-rupee", "at": A("c25", "refunds")},
           {"label": "An affidavit supporting quashing", "sub": "by Harish, the complainant", "icon": "file-pen-line", "at": A("c25", "affidavit")}])
cue(type="section", t0=S("c26"), t1=E("c26") + 0.05, at=A("c26", "section"), act="BNSS, 2023", num="359",
    title="Compounding of offences",
    points=[{"text": "Table 1: by the persons named", "at": A("c26", "compounded")},
            {"text": "Table 2: only with the court's permission", "at": A("c26", "permission")},
            {"text": "Forgery: in neither table", "tone": "no", "at": A("c26", "forgery")}])
cue(type="cite", t0=S("c26") + 0.3, t1=E("c26") + 0.05, at=S("c26") + 0.3, tag="BNSS 359 · BNS, 2023",
    text="Cheating 318(2): Table 1 · cheating 318(4), breach of trust 316(2): Table 2 · forgery 336, 338, 340: neither",
    icon="book-open")
cue(type="compare", t0=S("c27"), t1=E("c27") + 0.05, head="Two different things", head_at=S("c27") + 0.05,
    cols=[{"title": "Compounding · s.359", "icon": "handshake", "at": S("c27") + 0.4},
          {"title": "Quashing on settlement · s.528", "icon": "landmark", "at": A("c27", "quash")}],
    rows=[{"cells": ["The parties, before the trial court", "The High Court's discretion"],
           "cells_at": [A("c27", "holds"), A("c27", "settlement")]},
          {"cells": ["Only offences in its tables", "Can reach non-compoundable offences"],
           "cells_at": [A("c27", "using"), A("c27", "distinct")]}])
cue(type="cite", t0=A("c27", "gian"), t1=E("c27") + 0.05, at=A("c27", "gian"), tag=SC + " · 24.09.2012 · THREE JUDGES",
    cases=[{"name": "Gian Singh v. State of Punjab", "cite": "para 61 · " + OLD}])
cue(type="flow", t0=S("c28"), t1=E("c28") + 0.05, head="When settlement may count", head_at=S("c28") + 0.05,
    steps=[{"label": "An overwhelmingly civil flavour", "sub": "commercial, matrimonial, family", "icon": "briefcase", "at": A("c28", "overwhelmingly")},
           {"label": "The entire dispute resolved", "sub": "by the parties", "icon": "handshake", "at": A("c28", "resolve")},
           {"label": "May be quashed", "sub": "in the High Court's discretion", "icon": "landmark", "tone": "ok", "at": A("c28", "entire")}])
cue(type="cite", t0=S("c28") + 0.05, t1=E("c28") + 0.05, at=S("c28") + 0.05, tag="GIAN SINGH · PARA 61",
    text="Also: conviction remote and bleak, and continuing the case oppressive", icon="scale")
cue(type="list", t0=S("c29"), t1=E("c29") + 0.05, head="Settlement alone cannot end them", head_at=S("c29") + 0.05,
    items=[{"n": 1, "text": "Heinous: murder, rape, dacoity", "at": A("c29", "murder")},
           {"n": "!", "text": "They affect society", "at": A("c29", "society")},
           {"n": 2, "text": "Prevention of Corruption Act cases", "at": A("c29", "prevention")}])
cue(type="cite", t0=S("c29") + 0.05, t1=E("c29") + 0.05, at=S("c29") + 0.05, tag="GIAN SINGH · PARA 61",
    text="Nor offences by public servants while working in that capacity", icon="scale")
cue(type="splitcard", t0=S("c30"), t1=E("c30") + 0.05,
    left={"title": "NARINDER SINGH", "text": "Timing: an early settlement is viewed more liberally", "icon": "clock", "at": A("c30", "narinder")},
    right={"title": "PARBATBHAI AAHIR", "text": "Economic offences affecting the State may not be quashed", "icon": "landmark", "at": A("c30", "economic")})
cue(type="cite", t0=A("c30", "narinder"), t1=E("c30") + 0.05, at=A("c30", "narinder"), tag=SC + " · " + OLD.upper(),
    cases=[{"name": "Narinder Singh v. State of Punjab", "cite": "27.03.2014 · para 29.7"},
           {"name": "Parbatbhai Aahir v. State of Gujarat", "cite": "04.10.2017 · para 16.10"}])

# ── 8 · other routes to the High Court ───────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c31"), t1=E("c31") + 0.05, at=A("c31", "another"), act="BNSS, 2023", num="438–442",
    title="Revision",
    points=[{"text": "By the High Court or a Sessions Judge", "at": A("c31", "sections")},
            {"text": "Not against interlocutory orders", "tone": "no", "at": A("c31", "interlocutory")}])
cue(type="cite", t0=S("c31") + 0.3, t1=E("c31") + 0.05, at=S("c31") + 0.3, tag="BNSS 438(3)",
    text="One application: to the High Court or the Sessions Judge, not both", icon="book-open")
cue(type="quote", t0=S("c32"), t1=E("c32") + 0.05, at=A("c32", "supreme"), reveal=2.2,
    text="The limitation is self-restraint, nothing more.", hl=["self-restraint"],
    note={"text": "A revision remedy ≠ a bar to the inherent power", "at": A("c32", "revision")})
cue(type="cite", t0=S("c32") + 0.05, t1=E("c32") + 0.05, at=S("c32") + 0.05, tag=SC + " · 05.09.2016 · THREE JUDGES",
    cases=[{"name": "Prabhu Chawla v. State of Rajasthan", "cite": "paras 4–6 · " + OLD}])
cue(type="splitcard", t0=S("c33"), t1=A("c33", "bhajan") - 0.05,
    left={"title": "SECTION 528 BNSS", "text": "the High Court's inherent power", "icon": "book-open", "at": A("c33", "quashing")},
    right={"title": "ARTICLE 226", "text": "the Constitution's writ power", "icon": "landmark", "at": A("c33", "article")})
cue(type="point", t0=A("c33", "bhajan") - 0.05, t1=E("c33") + 0.05, text="Bhajan Lal's categories cover both powers", icon="check",
    accent=True, at=A("c33", "bhajan"))
cue(type="cite", t0=A("c33", "bhajan"), t1=E("c33") + 0.05, at=A("c33", "bhajan"), tag=SC + " · 21.11.1990",
    cases=[{"name": "State of Haryana v. Bhajan Lal", "cite": "para 102"}])

# ── 9 · preparing the petition ───────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="checklist", t0=S("c34"), t1=E("c34") + 0.05, head="Attach, and show", head_at=S("c34") + 0.05,
    items=[{"n": 1, "text": "The FIR or charge sheet under challenge", "at": A("c34", "attach")},
           {"n": 2, "text": "Which category applies", "at": A("c34", "category")},
           {"n": 3, "text": "From the prosecution's own papers", "at": A("c34", "prosecution")}])
cue(type="cite", t0=S("c34") + 0.3, t1=E("c34") + 0.05, at=S("c34") + 0.3, tag="PRACTICE NOTE",
    text="Drafting practice, not a statutory rule", icon="info")
cue(type="flow", t0=S("c35"), t1=E("c35") + 0.05, head="In a settlement case", head_at=S("c35") + 0.05,
    steps=[{"label": "The complainant's affidavit", "sub": "filed with the petition", "icon": "file-pen-line", "at": A("c35", "affidavit")},
           {"label": "The State and the complainant heard", "icon": "users", "at": A("c35", "heard")},
           {"label": "A real and complete settlement", "sub": "the court must find it", "icon": "scale", "tone": "ok", "at": A("c35", "real")}])
cue(type="cite", t0=S("c35") + 0.05, t1=E("c35") + 0.05, at=S("c35") + 0.05, tag="PRACTICE · GIAN SINGH, PARA 61",
    text="A “full and complete settlement”: the parties resolved their entire dispute", icon="scale")
cue(type="point", t0=S("c36"), t1=A("c36", "that") - 0.05, text="Petition dismissed: the case simply continues", icon="arrow-right",
    at=A("c36", "if"))
cue(type="notequal", t0=A("c36", "that") - 0.05, t1=E("c36") + 0.05, left="A dismissed petition", right="a finding of guilt",
    at=A("c36", "that"), left_at=A("c36", "that"),
    sub="The trial court still weighs the evidence", sub_at=A("c36", "trial"), icon="scale")

# ── 10 · remember the test ───────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="list", t0=S("c37"), t1=E("c37") + 0.05, head="Remember", head_at=S("c37") + 0.05,
    items=[{"n": 1, "text": "Section 528: to prevent abuse of process", "at": A("c37", "prevent")},
           {"n": 2, "text": "Used sparingly", "at": A("c37", "sparingly")},
           {"n": 3, "text": "The facts decide", "at": A("c37", "facts")}])
cue(type="kicker", t0=S("c38"), t1=E("c38") + 0.05, at=S("c38") + 0.08, text="HYPOTHETICAL EXAMPLE · KAVYA, THE ACCUSED")
cue(type="splitcard", t0=S("c38"), t1=E("c38") + 0.05,
    left={"title": "WHAT THE FIR ALLEGES", "text": "Specific facts of forgery, or a civil dispute?", "icon": "file-text", "at": A("c38", "kavya")},
    right={"title": "WHAT WAS SETTLED", "text": "The entire dispute, truly?", "icon": "handshake", "at": A("c38", "what", 2)})
cue(type="point", t0=S("c39"), t1=E("c39") + 0.05, text="Like · Share · Subscribe · lawworld.ai",
    icon="check", accent=True, at=A("c39", "thanks"))
