# Summons, Warrants and Proclamation - CONCEPT VIDEO (legal-concept explainer, Cause of Action build): panel cues, run by
# split/build_course_plan.py (helpers: at S E cue fx have r3 PEND). Storyboard: ~/Downloads/02_Summons_Warrants_Proclamation_LawWorld_v2.pdf.
# Held to the PDF's "Points to preserve":
#  - every case by its LawWorld Citation ID only; no SCC / AIR / INSC anywhere on screen;
#  - the ladder (summons -> bailable warrant -> non-bailable warrant) is labelled JUDICIAL GUIDANCE from Inder Mohan Goswami
#    and Satender Kumar Antil, NOT the text of s.90; s.90 supplies the grounds and the duty to record reasons;
#  - warrant TYPE is never equated with the offence's classification: a non-bailable warrant = no s.73 endorsement;
#  - s.84(4) reads "a grave offence" on screen; the ten-years/life/death threshold stays out of the cards;
#  - anticipatory bail: "normally not entitled", never an absolute bar;
#  - BNS 209 is tied to a proclamation under s.84, never to an ordinary summons;
#  - the sample summons is marked "Illustration only" and carries no real personal details.
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

STING = {"kicker": "CRIMINAL PROCEDURE · BNSS EXPLAINED", "title": "Summons, Warrants and Proclamation",
         "sub": "How a criminal court secures attendance"}
ENDCARD = {"title": "Summons, Warrants and Proclamation", "line": "A summons calls · a warrant authorises arrest · a proclamation needs findings",
           "sub": "LawWorld: legal research for advocates"}

# ── 1 · three different court processes ──────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "neighbour"),
    text="“A summons means the police will arrest you.”", hl="will arrest you.”")
cue(type="compare", t0=S("c02"), t1=E("c03") + 0.05, head="Three different things", head_at=S("c02") + 0.05,
    cols=[{"title": "Summons", "icon": "file-text", "at": A("c02", "summons")},
          {"title": "Warrant", "icon": "user", "at": A("c02", "warrant")},
          {"title": "Proclamation", "icon": "megaphone", "at": A("c03", "proclamation")}],
    rows=[{"cells": ["Directs attendance", "Authorises arrest", "Addresses absconding or hiding"],
           "cells_at": [A("c02", "directs"), A("c02", "authorises"), A("c03", "absconding")]}])
cue(type="point", t0=S("c04"), t1=E("c04") + 0.05, text="Each has its own conditions — courts must move through them in order",
    icon="scale", accent=True, at=A("c04", "conditions"))
cue(type="cite", t0=A("c04", "supreme"), t1=E("c04") + 0.05, at=A("c04", "supreme"), tag="SUPREME COURT OF INDIA · 11.07.2022",
    cases=[{"name": "Satender Kumar Antil v. CBI", "cite": "LAWWORLD 2022 SC 0738, para 32"}])

# ── 2 · understanding a summons ──────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c05"), t1=E("c06") + 0.05, at=A("c05", "section"), act="BNSS, 2023", num="63",
    title="The form of a summons",
    points=[{"text": "In writing, signed and sealed", "at": A("c05", "writing")},
            {"text": "Or an encrypted electronic communication", "at": A("c06", "encrypted")},
            {"text": "Bearing the image of the court's seal, or a digital signature", "at": A("c06", "digital")}])
cue(type="list", t0=S("c07"), t1=A("c07", "accused") - 0.05, head="Read it carefully — illustration only", head_at=S("c07") + 0.05,
    items=[{"n": 1, "text": "The court", "at": A("c07", "court")},
           {"n": 2, "text": "The case", "at": A("c07", "case")},
           {"n": 3, "text": "The person summoned", "at": A("c07", "person")},
           {"n": 4, "text": "The purpose", "at": A("c07", "purpose")},
           {"n": 5, "text": "The date", "at": A("c07", "date")}])
cue(type="verdicts", t0=A("c07", "accused"), t1=E("c07") + 0.05,
    rows=[{"text": "It can call an accused, or a witness", "ok": True, "at": A("c07", "accused")},
          {"text": "It establishes guilt", "ok": False, "at": A("c07", "guilt"), "strike_at": A("c07", "guilt")}])
cue(type="point", t0=S("c08"), t1=E("c08") + 0.05, text="Verify an electronic message through official court channels",
    icon="shield", accent=True, at=A("c08", "verified"))

# ── 3 · service and the appearance date ──────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c09"), t1=E("c10") + 0.05, at=A("c09", "section"), act="BNSS, 2023", num="64 · 65–71",
    title="Service of a summons",
    points=[{"text": "Personally, where practicable", "at": A("c09", "personally")},
            {"text": "Or electronically, in the form State rules prescribe", "at": A("c09", "electronic")},
            {"text": "ss. 65–71: companies, absent persons, government servants, witnesses", "at": A("c10", "companies")}])
cue(type="notequal", t0=S("c11"), t1=E("c11") + 0.05, left="A fixed seven or fifteen days", right="the rule",
    at=A("c11", "universal"), left_at=A("c11", "seven"),
    sub="There is no universal period", sub_at=A("c11", "universal"))
cue(type="list", t0=S("c12"), t1=E("c12") + 0.05, head="What controls", head_at=S("c12") + 0.05,
    items=[{"n": "→", "text": "The appearance date on the document", "at": A("c12", "appearance")},
           {"n": 1, "text": "Preserve it, and act promptly", "at": A("c12", "preserve")},
           {"n": "!", "text": "Refusing the envelope does not make the case disappear", "at": A("c12", "refusing")}])

# ── 4 · when attendance is difficult ─────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c13"), t1=E("c13") + 0.05, head="Attendance is genuinely difficult", head_at=S("c13") + 0.05,
    steps=[{"label": "In hospital on the hearing date", "sub": "Asha is an accused", "icon": "alert-triangle", "tone": "warn", "at": A("c13", "hospital")},
           {"label": "Place the difficulty before the court", "sub": "through counsel, before the date", "icon": "landmark", "at": A("c13", "counsel")}])
cue(type="section", t0=S("c14"), t1=E("c14") + 0.05, at=A("c14", "section"), act="BNSS, 2023", num="228",
    title="Dispensing with personal attendance",
    points=[{"text": "A Magistrate who issues a summons may dispense with it", "at": A("c14", "dispense")},
            {"text": "And permit appearance through an advocate", "at": A("c14", "advocate")}],
    note={"text": "Accused only — not witnesses", "icon": "info", "at": A("c14", "appearance")})
cue(type="cite", t0=S("c15"), t1=E("c15") + 0.05, at=A("c15", "bhaskar"), tag="SUPREME COURT OF INDIA · 27.08.2001",
    cases=[{"name": "Bhaskar Industries Ltd. v. Bhiwani Denim and Apparels Ltd.", "cite": "LAWWORLD 2001 SC 0870, paras 8 and 9"}])
cue(type="verdicts", t0=S("c16"), t1=E("c16") + 0.05,
    rows=[{"text": "The court's permission", "ok": True, "at": A("c16", "court")},
          {"text": "A private message to the complainant", "ok": False, "at": A("c16", "private"), "strike_at": A("c16", "complainant")}])

# ── 5 · what a warrant does ──────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c17"), t1=E("c17") + 0.05, at=A("c17", "section"), act="BNSS, 2023", num="72",
    title="The arrest warrant",
    points=[{"text": "A written order of the court", "at": A("c17", "written")},
            {"text": "Signed by the presiding officer", "at": A("c17", "presiding")},
            {"text": "Bearing the court's seal", "at": A("c17", "seal")}])
cue(type="point", t0=S("c18"), t1=A("c18", "expire") - 0.05, text="Valid until executed, or cancelled by the issuing court",
    icon="check", accent=True, at=A("c18", "force"))
cue(type="point", t0=A("c18", "expire"), t1=E("c18") + 0.05, text="It does not expire because a hearing date passed",
    icon="alert-triangle", accent=True, at=A("c18", "expire"))
cue(type="flow", t0=S("c19"), t1=E("c19") + 0.05, head="If Asha learns of a warrant", head_at=S("c19") + 0.05,
    steps=[{"label": "Obtain its details", "sub": "", "icon": "search", "at": A("c19", "details")},
           {"label": "Apply promptly to recall or convert it", "sub": "a non-bailable warrant may be cancelled or converted", "icon": "landmark", "tone": "ok", "at": A("c19", "recall")},
           {"label": "Do not hide", "sub": "hiding is what leads to a proclamation", "icon": "x", "tone": "stop", "at": A("c19", "hide")}])

# ── 6 · security endorsed on a warrant ───────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c20"), t1=E("c20") + 0.05, at=A("c20", "section"), act="BNSS, 2023", num="73",
    title="Security endorsed on the warrant",
    points=[{"text": "The court may endorse a bond with sureties", "at": A("c20", "endorse")},
            {"text": "The executing officer must then release the person", "at": A("c20", "release")}])
cue(type="compare", t0=S("c21"), t1=E("c22") + 0.05, head="With the endorsement, and without", head_at=S("c21") + 0.05,
    cols=[{"title": "s. 73 endorsement", "icon": "check", "at": A("c21", "bailable")},
          {"title": "No endorsement", "icon": "x", "at": A("c21", "without")}],
    rows=[{"cells": ["The officer may release on the warrant", "The officer cannot release on the warrant itself"],
           "cells_at": [A("c21", "bailable"), A("c22", "officer")]},
          {"cells": ["Commonly called a bailable warrant", "Bail must be sought from the court"],
           "cells_at": [A("c21", "called"), A("c22", "sought")]}])
cue(type="notequal", t0=A("c21", "never"), t1=E("c21") + 0.05, left="No endorsement", right="bail can never be granted",
    at=A("c21", "never"), left_at=A("c21", "endorsement"),
    sub="Warrant type is not the offence's classification", sub_at=A("c21", "never"))
cue(type="cite", t0=S("c23"), t1=E("c23") + 0.05, at=A("c23", "cautioned"), tag="SUPREME COURT OF INDIA · 09.10.2007",
    cases=[{"name": "Inder Mohan Goswami v. State of Uttaranchal", "cite": "LAWWORLD 2007 SC 1025, paras 46 and 52–55"}])

# ── 7 · when a court may issue a warrant ─────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c24"), t1=E("c26") + 0.05, at=A("c24", "section"), act="BNSS, 2023", num="90",
    title="A warrant instead of, or with, a summons",
    points=[{"text": "Reasons must be recorded in writing", "at": A("c24", "recording")},
            {"text": "Reason to believe he has absconded, or will not obey", "at": A("c25", "absconded")},
            {"text": "Or: failure to appear without reasonable excuse, after due service", "at": A("c26", "excuse")}])
cue(type="flow", t0=S("c27"), t1=E("c27") + 0.05, head="The Court's ladder — judicial guidance, not s. 90", head_at=S("c27") + 0.05,
    steps=[{"label": "1 · Summons first", "sub": "including appearance through a lawyer", "icon": "file-text", "at": A("c27", "summons")},
           {"label": "2 · Then a bailable warrant", "sub": "if he does not appear despite service", "icon": "user", "tone": "warn", "at": A("c27", "bailable")},
           {"label": "3 · Non-bailable warrant last", "sub": "only when the person is avoiding court", "icon": "alert-triangle", "tone": "stop", "at": A("c27", "avoiding")}])

# ── 8 · the proclamation stage ───────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c28"), t1=E("c29") + 0.05, at=A("c28", "section"), act="BNSS, 2023", num="84(1)–(3)",
    title="Before a proclamation can issue",
    points=[{"text": "A warrant has already been issued", "at": A("c28", "warrant")},
            {"text": "Reason to believe he has absconded, or is hiding", "at": A("c28", "absconded")},
            {"text": "So that the warrant cannot be executed", "at": A("c29", "executed")}])
cue(type="point", t0=S("c30"), t1=E("c30") + 0.05, text="Appearance at a specified place and time — at least thirty days from publication",
    icon="calendar", accent=True, at=A("c30", "thirty"))
cue(type="point", t0=S("c31"), t1=E("c31") + 0.05, text="One missed hearing does not satisfy these conditions",
    icon="x", accent=True, at=A("c31", "missed"))
# "section" is the ninth word here, so anchoring the header on it left the panel blank for 4.5 s while the
# points (on "proclamation", "offence") waited on a card that did not exist yet: build on the first word.
cue(type="section", t0=S("c32"), t1=E("c32") + 0.05, at=A("c32", "ignoring"), act="BNS, 2023", num="209",
    title="Ignoring a proclamation is an offence",
    points=[{"text": "Failure to appear in answer to a s. 84 proclamation", "at": A("c32", "proclamation")}],
    note={"text": "Not an ordinary summons", "icon": "info", "at": A("c32", "offence")})

# ── 9 · property and further consequences ────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c33"), t1=E("c34") + 0.05, at=A("c33", "section"), act="BNSS, 2023", num="85",
    title="Attachment of property",
    points=[{"text": "By a reasoned order, after proclamation", "at": A("c33", "reasoned")},
            {"text": "Simultaneously only where property may be disposed of or removed", "at": A("c34", "simultaneously")}],
    note={"text": "A summons alone never leads to attachment", "icon": "info", "at": A("c34", "never")})
cue(type="flow", t0=S("c35"), t1=E("c35") + 0.05, head="Proclaimed offender — s. 84(4)", head_at=S("c35") + 0.05,
    steps=[{"label": "Proclaimed for a grave offence", "sub": "", "icon": "megaphone", "at": A("c35", "grave")},
           {"label": "Still fails to appear", "sub": "as the proclamation required", "icon": "x", "tone": "stop", "at": A("c35", "fails")},
           {"label": "After inquiry: declared a proclaimed offender", "sub": "a separate judicial decision", "icon": "landmark", "at": A("c35", "inquiry")}])
cue(type="list", t0=S("c36"), t1=E("c36") + 0.05, head="What follows", head_at=S("c36") + 0.05,
    items=[{"n": 1, "text": "Normally not entitled to anticipatory bail", "at": A("c36", "anticipatory")},
           {"n": 2, "text": "BNSS 356: trial in absence becomes possible", "at": A("c36", "allows")}])
cue(type="cite", t0=A("c36", "anticipatory"), t1=E("c36") + 0.05, at=A("c36", "anticipatory"), tag="SUPREME COURT OF INDIA",
    cases=[{"name": "Lavesh v. State (NCT of Delhi)", "cite": "LAWWORLD 2012 SC 0827, para 10"},
           {"name": "Srikant Upadhyay v. State of Bihar", "cite": "LAWWORLD 2024 SC 0351"}])

# ── 10 · the practical response ──────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="list", t0=S("c37"), t1=E("c39") + 0.05, head="Organised action", head_at=S("c37") + 0.05,
    items=[{"n": 1, "text": "Verify the document", "at": A("c37", "verify")},
           {"n": 2, "text": "Note the appearance date", "at": A("c37", "note")},
           {"n": 3, "text": "Are you an accused, or a witness?", "at": A("c38", "identify")},
           {"n": 4, "text": "Obtain legal assistance", "at": A("c38", "assistance")},
           {"n": 5, "text": "Seek the court's permission before the date, not after", "at": A("c39", "permission")}])
cue(type="compare", t0=S("c40"), t1=E("c40") + 0.05, head="Know the difference", head_at=S("c40") + 0.05,
    cols=[{"title": "Summons", "icon": "file-text", "at": A("c40", "summons")},
          {"title": "Warrant", "icon": "user", "at": A("c40", "warrant")},
          {"title": "Proclamation", "icon": "megaphone", "at": A("c40", "proclamation")}],
    rows=[{"cells": ["Calls you to court", "Authorises arrest", "Requires further findings about evasion"],
           "cells_at": [A("c40", "calls"), A("c40", "authorises"), A("c40", "evasion")]}])
cue(type="point", t0=S("c41"), t1=E("c41") + 0.05, text="Respond without panic, or dangerous delay",
    icon="shield", accent=True, at=A("c41", "panic"))
cue(type="point", t0=S("c42"), t1=E("c42") + 0.05, text="Like · Share · Subscribe · lawworld.ai",
    icon="check", accent=True, at=A("c42", "like"))
