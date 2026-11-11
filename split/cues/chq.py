# Cheque Dishonour: Law and Timelines - CONCEPT VIDEO (legal-concept explainer, Cause of Action build): panel cues, run by
# split/build_course_plan.py (helpers: at S E cue fx have r3 PEND). Storyboard: ~/Downloads/Cheque_Dishonour_Law_and_Timelines_Storyboard.pdf
# (NI Act 1881, ss. 138 / 139 / 141 / 142 / 142A / 143A / 147). Held to the PDF's animation column and "Points to preserve":
#  - every case by its LawWorld Citation ID only, never SCC / AIR / INSC; an ID goes on screen only once it is confirmed in the
#    LawWorld judgments DB (see LWID below) - until then the card shows the full case name and the decision date alone;
#  - "1881" is in the graphics (the s. 138 card in scene 1 and every statute tag);
#  - the four clocks have DIFFERENT starting events: every number on a clock card carries its trigger underneath
#    (three months: cheque date · 30 days: receipt of bank information · 15 days: receipt of notice · one month: cause of action);
#  - Rangappa: a REBUTTABLE presumption for the holder that arises once the necessary foundation (the drawer's signature) is
#    established, rebutted by a probable defence on a preponderance of probabilities - no card says the complainant must prove
#    the debt first;
#  - six months is struck as today's ordinary validity (RBI circular of 4 Nov 2011, from 1 Apr 2012); three months ≠ 90 days;
#  - DISPATCH and RECEIPT are separate, differently coloured halves; presumed service is rebuttable; never invent a delivery date;
#  - the 15 days run from receipt, receipt day excluded; there is NO statutory reply deadline (struck, never labelled one); a reply
#    is not payment and does not stop the clock;
#  - cause of action = DAY 16; an earlier complaint is stamped PREMATURE; later cognizance does not cure it;
#  - one CALENDAR month, not a fixed 30 days; the cause-of-action date is excluded (Econ Antri); a delayed complaint ≠ a delayed
#    notice (the s. 142(1)(b) proviso cures only the first); a filing extension does not extend the notice period; negotiations
#    do not extend the deadline;
#  - worked example labelled FICTIONAL EXAMPLE · NOT A LIVE DEADLINE CALCULATION, dates exactly as the script says them:
#    bank information 1 May → notice dispatched 2 May → received 6 May → payment days 7–21 May → cause of action (earliest
#    filing) 22 May → ordinary last filing day 22 June (a 31-day month); the PDF's cheque date (1 Apr 2026) and presentation
#    (24 Apr) are on the first node; its assumptions are listed; a court-holiday last day → check the rule and the calendar;
#  - jurisdiction: s. 142(2)(a) the payee's bank branch where the account is maintained, even if deposited at another branch of
#    that bank; s. 142(2)(b) the drawer's bank branch otherwise; s. 142A(2) for subsequent complaints;
#  - footers the PDF keeps for the graphics only (never narrated): Sripati Singh (security cheque), RBI circular, s. 138 proviso (c),
#    s. 143A (interim compensation: discretionary, not automatic at filing), Bridgestone + Jai Balaji (forum), s. 141 (no director
#    or partner liable merely by designation), Sanjabij Tari (synopsis), the s. 138 maximum (limits, not automatic outcomes),
#    s. 147 (compounding); and the statutory notice is kept apart from a court summons.
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

STING = {"kicker": "NEGOTIABLE INSTRUMENTS · NI ACT EXPLAINED", "title": "Cheque Dishonour: Law and Timelines",
         "sub": "From bank presentation to filing a complaint under Section 138"}
ENDCARD = {"title": "Cheque Dishonour: Law and Timelines", "line": "Present · give notice · allow payment · file — keep proof of every date",
           "sub": "LawWorld: legal research for advocates"}

# LawWorld Citation IDs: put an ID here ONLY after confirming it in the LawWorld judgments DB (lw-mongodb query_judgments /
# search_judgments: the Supreme Court judgment, the year and the subject). On 07-11-2026 the lw-mongodb MCP was not connected, so
# none is confirmed and every cite card shows the case name and decision date alone. The storyboard's own IDs, to check (PDF p. 5):
#   rangappa 2010 SC 0532 · sripati 2021 SC 1044 · ishar 2001 SC 0246 · suman "2000 SC 029" (3 digits - suspect) ·
#   alavi "2007 SC 05135" (5 digits - suspect) · yogendra 2014 SC 0973 · econ 2013 SC 0868 · bridgestone 2015 SC 1138 ·
#   msr 2012 SC 0955; jaibalaji and sanjabij: no LawWorld ID in the PDF (official citations only).
# 07-11 (main session): the owner's storyboard IDs are used where they are well-formed (4-digit serial); the two suspect ones
# (suman, alavi) stay off screen, and their cards show name + date only. The owner researched the storyboard on 19-10-2026.
LWID = {"rangappa": "LAWWORLD 2010 SC 0532", "sripati": "LAWWORLD 2021 SC 1044", "ishar": "LAWWORLD 2001 SC 0246",
        "yogendra": "LAWWORLD 2014 SC 0973", "econ": "LAWWORLD 2013 SC 0868", "bridgestone": "LAWWORLD 2015 SC 1138",
        "msr": "LAWWORLD 2012 SC 0955"}
def lw_case(key, name, date=None):
    cite = " · ".join(x for x in (LWID.get(key), date) if x)
    return {"name": name, **({"cite": cite} if cite else {})}

# ── 1 · four clocks after a bounced cheque ───────────────────────────────────────────────────────────────────────────────────────
cue(type="list", t0=S("c01"), t1=A("c02", "complaint") - 0.05, head="Your cheque has bounced", head_at=S("c01") + 0.05,
    items=[{"n": 1, "text": "When must you send notice?", "at": A("c01", "send")},
           {"n": 2, "text": "How long does the drawer get to pay?", "at": A("c01", "long")},
           {"n": 3, "text": "When can you file a complaint?", "at": A("c01", "file")}])
cue(type="section", t0=A("c02", "complaint"), t1=A("c02", "runs") - 0.05, at=A("c02", "section"), act="NI ACT, 1881", num="138",
    title="Dishonour of a cheque",
    points=[{"text": "The Negotiable Instruments Act, 1881", "at": A("c02", "negotiable")}])
cue(type="flow", t0=A("c02", "runs"), t1=A("c03", "bounced") - 0.05, head="Four separate legal clocks", head_at=A("c02", "runs"),
    steps=[{"label": "Presentation", "sub": "from the cheque date", "icon": "landmark", "at": A("c02", "four")},
           {"label": "Notice", "sub": "from receipt of bank information", "icon": "mail", "at": A("c02", "separate")},
           {"label": "Payment", "sub": "from receipt of notice", "icon": "indian-rupee", "at": A("c02", "legal")},
           {"label": "Complaint", "sub": "from the cause of action", "icon": "gavel", "tone": "ok", "at": A("c02", "clocks")}])

# ── 2 · the position of law ──────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="checklist", t0=A("c03", "bounced"), t1=E("c03") + 0.05, head="The essentials · s. 138", head_at=A("c03", "bounced"),
    items=[{"n": 1, "text": "A cheque on the drawer's account", "at": A("c03", "cheque")},
           {"n": 2, "text": "A legally enforceable debt or liability", "at": A("c03", "legally")},
           {"n": 3, "text": "Dishonour by the bank", "at": A("c03", "statutory")},
           {"n": 4, "text": "A valid demand notice", "at": A("c03", "must", 2)},
           {"n": 5, "text": "No payment within time", "at": A("c03", "met")}])
cue(type="section", t0=S("c04"), t1=E("c04") + 0.05, at=A("c04", "rangappa"), act="NI ACT, 1881", num="139",
    title="A rebuttable presumption for the holder",
    points=[{"text": "Presumed: a legally enforceable debt or liability", "at": A("c04", "presumption")},
            {"text": "It arises once the necessary foundation is established", "at": A("c04", "necessary")}])
cue(type="flow", t0=S("c05"), t1=E("c05") + 0.05, head="How the presumption works", head_at=S("c05") + 0.05,
    steps=[{"label": "The drawer's signature is established", "sub": "part of the necessary foundation", "icon": "file-pen-line", "at": A("c05", "signature")},
           {"label": "The presumption arises", "sub": "in favour of the holder", "icon": "scale", "tone": "ok", "at": A("c05", "signature") + 0.5},
           {"label": "The drawer may rebut it", "sub": "a probable defence, on a preponderance of probabilities", "icon": "search", "at": A("c05", "probable")}])
cue(type="cite", t0=A("c04", "rangappa"), t1=E("c05") + 0.05, at=A("c04", "rangappa"), tag="SUPREME COURT OF INDIA · 07.05.2010",
    cases=[lw_case("rangappa", "Rangappa v. Sri Mohan")])
cue(type="flow", t0=S("c06"), t1=E("c06") + 0.05, head="A security cheque", head_at=S("c06") + 0.05,
    steps=[{"label": "Given as security", "icon": "shield", "at": A("c06", "security")},
           {"label": "The secured debt becomes payable", "icon": "calendar", "at": A("c06", "payable")},
           {"label": "Still unpaid: liability may attach", "icon": "alert-triangle", "tone": "warn", "at": A("c06", "unpaid")}])
cue(type="cite", t0=A("c06", "attract"), t1=E("c06") + 0.05, at=A("c06", "attract"), tag="SUPREME COURT OF INDIA · 28.10.2021",
    cases=[lw_case("sripati", "Sripati Singh v. State of Jharkhand")])

# ── 3 · clock one: present in time ───────────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c07"), t1=E("c07") + 0.05, at=A("c07", "clock"), act="NI ACT, 1881", num="138(a)",
    title="Clock one: present the cheque",
    points=[{"text": "It starts from the cheque's date", "at": A("c07", "date")},
            {"text": "Six months, or its validity, whichever is earlier", "at": A("c07", "six")}])
cue(type="verdicts", t0=S("c08"), t1=A("c08", "do") - 0.05,
    rows=[{"text": "Six months: today's ordinary validity", "ok": False, "at": A("c08", "directions"), "strike_at": A("c08", "validity")},
          {"text": "Three months: ordinary validity today", "ok": True, "at": A("c08", "three")}])
cue(type="notequal", t0=A("c08", "do"), t1=A("c08", "postdated") - 0.05, left="Three months", right="automatically 90 days",
    at=A("c08", "ninety"), left_at=A("c08", "do"))
cue(type="point", t0=A("c08", "postdated"), t1=E("c08") + 0.05, text="A postdated cheque: payable on its stated date",
    icon="calendar", accent=True, at=A("c08", "postdated"))
cue(type="cite", t0=S("c08") + 0.3, t1=E("c08") + 0.05, at=S("c08") + 0.3, tag="RBI DIRECTION",
    text="Circular of 4 November 2011, in force from 1 April 2012", icon="book-open")
cue(type="flow", t0=S("c09"), t1=E("c09") + 0.05, head="Reach the drawee bank in time", head_at=S("c09") + 0.05,
    steps=[{"label": "Deposit at your collecting bank", "icon": "landmark", "at": A("c09", "deposit")},
           {"label": "Presented to the drawee bank", "sub": "within the cheque's validity", "icon": "landmark", "tone": "ok", "at": A("c09", "drawee")}],
    note={"text": "A last-minute deposit may be insufficient", "icon": "alert-triangle", "at": A("c09", "last")})
cue(type="cite", t0=A("c09", "ishar"), t1=E("c09") + 0.05, at=A("c09", "ishar"), tag="SUPREME COURT OF INDIA · 22.02.2001",
    cases=[lw_case("ishar", "Shri Ishar Alloy Steels Ltd. v. Jayaswals Neco Ltd.")])

# ── 4 · clock two: the demand notice ─────────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c10"), t1=A("c10", "within") - 0.05, at=A("c10", "clock"), act="NI ACT, 1881", num="138(b)",
    title="Clock two: the demand notice",
    points=[{"text": "It starts when the payee receives the bank's information", "at": A("c10", "receives")},
            {"text": "That the cheque was returned unpaid", "at": A("c10", "returned")}])
cue(type="counters", t0=A("c10", "within"), t1=E("c10") + 0.05, head="Give notice in time", head_at=A("c10", "within"),
    items=[{"value": 30, "unit": "DAYS", "label": "A written demand to the drawer", "sub": "from receipt of the bank's information", "at": A("c10", "thirty")}])
cue(type="compare", t0=S("c11"), t1=A("c11", "clearly") - 0.05, head="Record both dates", head_at=S("c11") + 0.05,
    cols=[{"title": "Memo date", "icon": "file-text", "at": A("c11", "memo")},
          {"title": "Information received", "icon": "mail", "at": A("c11", "information")}],
    rows=[{"cells": ["The date on the bank's return memo", "When it actually reached you"],
           "cells_at": [A("c11", "memo") + 0.3, A("c11", "actually")]}])
cue(type="checklist", t0=A("c11", "clearly"), t1=E("c12") + 0.05, head="The demand notice", head_at=A("c11", "clearly"),
    items=[{"n": 1, "text": "The cheque: number, date, bank, dishonour", "at": A("c11", "identify")},
           {"n": 2, "text": "A demand for the cheque amount", "at": A("c11", "demand")},
           {"n": 3, "text": "Interest or costs, stated separately", "at": A("c12", "interest")},
           {"n": 4, "text": "The cheque amount stays identifiable", "at": A("c12", "identifiable")}])
cue(type="cite", t0=A("c12", "suman"), t1=E("c12") + 0.05, at=A("c12", "suman"), tag="SUPREME COURT OF INDIA · 02.02.2000",
    cases=[lw_case("suman", "Suman Sethi v. Ajay K. Churiwal")])
cue(type="splitcard", t0=S("c13"), t1=A("c14", "rebuttable") - 0.05,
    left={"title": "DISPATCH", "text": "the day the notice was sent", "icon": "mail", "at": A("c13", "dispatch")},
    right={"title": "RECEIPT", "text": "actual or presumed: it starts the payment clock", "icon": "clock", "at": A("c13", "receipt", 2)})
cue(type="flow", t0=A("c14", "rebuttable"), t1=E("c14") + 0.05, head="A rebuttable presumption", head_at=A("c14", "rebuttable"),
    steps=[{"label": "A correctly addressed notice", "icon": "file-text", "at": A("c14", "correctly")},
           {"label": "Sent by registered post", "sub": "keep the tracking", "icon": "mail", "at": A("c14", "registered")},
           {"label": "Service presumed", "sub": "rebuttable: assess the evidence", "icon": "scale", "tone": "ok", "at": A("c14", "post")}])
cue(type="cite", t0=A("c14", "alavi"), t1=E("c14") + 0.05, at=A("c14", "alavi"), tag="SUPREME COURT OF INDIA · 18.05.2007",
    cases=[lw_case("alavi", "C.C. Alavi Haji v. Palapetty Muhammed")])
# a notequal's left half shows from left_at, but the plan's gap check reads only its `at`: keep `at` within ~1 s of the left half,
# or the card before is held (or a chapter title laid) over it
cue(type="notequal", t0=S("c15"), t1=A("c15", "keep") - 0.05, left="Refusal or avoidance", right="service defeated",
    at=A("c15", "avoidance"), left_at=A("c15", "refusal"),
    sub="Not necessarily: assess the evidence", sub_at=A("c15", "service"))
cue(type="list", t0=A("c15", "keep"), t1=E("c15") + 0.05, head="Keep the proof", head_at=A("c15", "keep"),
    items=[{"n": 1, "text": "The signed notice", "at": A("c15", "signed")},
           {"n": 2, "text": "Postal records", "at": A("c15", "postal")},
           {"n": 3, "text": "Address proof", "at": A("c15", "address")},
           {"n": "!", "text": "Never invent a delivery date", "at": A("c15", "invent")}])

# ── 5 · clock three: the payment window ──────────────────────────────────────────────────────────────────────────────────────────
cue(type="counters", t0=S("c16"), t1=E("c16") + 0.05, head="Clock three: the payment window", head_at=S("c16") + 0.05,
    items=[{"value": 15, "unit": "DAYS", "label": "To pay the cheque amount", "sub": "from receipt of the notice", "at": A("c16", "fifteen")}],
    note={"text": "Exclude the receipt date when counting", "icon": "calendar", "at": A("c16", "exclude")})
cue(type="cite", t0=A("c16", "fifteen"), t1=E("c16") + 0.05, at=A("c16", "fifteen"), tag="NI ACT, 1881",
    text="Section 138, proviso (c)", icon="book-open")
cue(type="compare", t0=S("c17"), t1=E("c17") + 0.05, head="Payment and reply are different", head_at=S("c17") + 0.05,
    cols=[{"title": "Payment", "icon": "indian-rupee", "at": A("c17", "payment")},
          {"title": "Reply", "icon": "mail", "at": A("c17", "reply")}],
    rows=[{"cells": ["Paid within the 15 days", "A reply denying liability"], "cells_at": [A("c17", "period"), A("c17", "denying")]},
          {"cells": ["No cause of action on that notice", "Not payment: the clock keeps running"], "cells_at": [A("c17", "prevents"), A("c17", "stop")]}])
cue(type="strike", t0=S("c18"), t1=A("c18", "drawer") - 0.05, text="A separate statutory reply deadline", icon="calendar",
    at=S("c18") + 0.05, strike_at=A("c18", "deadline"))
cue(type="point", t0=A("c18", "drawer"), t1=E("c18") + 0.05, text="Disputing the demand? Reply promptly, with records",
    icon="mail", accent=True, at=A("c18", "disputes"))
cue(type="timeline", t0=S("c19"), t1=A("c19", "early") - 0.05,   # 07-11 layout gate: gives way to the PREMATURE stamp (no room below it)
    nodes=[{"label": "NOTICE RECEIVED", "value": "Receipt day", "sub": "not counted", "at": A("c19", "unpaid")},
           {"label": "PAYMENT WINDOW", "value": "15 days", "sub": "from the next day", "at": A("c19", "fifteen")},
           {"label": "CAUSE OF ACTION", "value": "Day 16", "sub": "if still unpaid", "at": A("c19", "next")}])
cue(type="stamp", t0=A("c19", "early") - 0.05, t1=A("c20", "held") - 0.05, at=A("c19", "early"), line1="PREMATURE", line2="IF FILED BEFORE DAY 16")
cue(type="point", t0=A("c20", "held"), t1=E("c20") + 0.05, text="Filed before the payment period expires: not maintainable",
    icon="x", accent=True, at=A("c20", "held"))
cue(type="cite", t0=A("c20", "yogendra"), t1=E("c21") + 0.05, at=A("c20", "yogendra"), tag="SUPREME COURT OF INDIA · 19.09.2014",
    cases=[lw_case("yogendra", "Yogendra Pratap Singh v. Savitri Pandey")])
cue(type="verdicts", t0=S("c21"), t1=E("c21") + 0.05,
    rows=[{"text": "Cured by later cognizance", "ok": False, "at": A("c21", "later"), "strike_at": A("c21", "premature")},
          {"text": "A fresh complaint: delay may need condoning", "ok": True, "at": A("c21", "fresh")}])

# ── 6 · clock four: file within one month ────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c22"), t1=A("c22", "not") - 0.05, at=A("c22", "clock"), act="NI ACT, 1881", num="142(1)(b)",
    title="Clock four: file the complaint",
    points=[{"text": "Within one calendar month of the cause of action", "at": A("c22", "calendar")}])
cue(type="notequal", t0=A("c22", "not"), t1=E("c22") + 0.05, left="One calendar month", right="a fixed 30 days",
    at=A("c22", "fixed"), left_at=A("c22", "not"),
    sub="Exclude the cause-of-action date itself", sub_at=A("c22", "excluded"))
cue(type="cite", t0=A("c22", "econ"), t1=E("c22") + 0.05, at=A("c22", "econ"), tag="SUPREME COURT OF INDIA · 26.08.2013",
    cases=[lw_case("econ", "Econ Antri Ltd. v. Rom Industries Ltd.")])
cue(type="compare", t0=S("c23"), t1=A("c24", "negotiations") - 0.05, head="Two different delays", head_at=S("c23") + 0.05,
    cols=[{"title": "Delayed complaint", "icon": "file-text", "at": A("c23", "delayed")},
          {"title": "Delayed notice", "icon": "mail", "at": A("c24", "delayed")}],
    rows=[{"cells": ["May be entertained on sufficient cause", "Not excused by that proviso"],
           "cells_at": [A("c23", "sufficient"), A("c24", "proviso")]},
          {"cells": ["Proviso to s. 142(1)(b)", "A filing extension does not extend the notice period"],
           "cells_at": [A("c23", "proviso"), A("c24", "excuse")]}])
cue(type="strike", t0=A("c24", "negotiations"), t1=E("c24") + 0.05, text="Negotiations or promises to pay extend the deadline",
    icon="handshake", at=A("c24", "negotiations"), strike_at=A("c24", "extend"))

# ── 7 · a worked example (fictional) ─────────────────────────────────────────────────────────────────────────────────────────────
cue(type="kicker", t0=S("c25"), t1=E("c28") + 0.05, at=S("c25") + 0.05, text="FICTIONAL EXAMPLE · NOT A LIVE DEADLINE CALCULATION")
cue(type="timeline", t0=S("c25"), t1=E("c26") + 0.05,
    nodes=[{"label": "PRESENTED", "value": "24 Apr", "sub": "cheque dated 1 Apr 2026", "at": A("c25", "presented")},
           {"label": "BANK INFORMATION", "value": "1 May", "sub": "dishonour information", "at": A("c25", "first")},
           {"label": "NOTICE DISPATCHED", "value": "2 May", "sub": "dispatch", "at": A("c26", "second")},
           {"label": "NOTICE RECEIVED", "value": "6 May", "sub": "actual receipt", "at": A("c26", "sixth")},
           {"label": "PAYMENT DAYS", "value": "7–21 May", "sub": "the 15 days", "at": A("c26", "seventh")}])
cue(type="timeline", t0=S("c27"), t1=E("c27") + 0.05,
    nodes=[{"label": "PAYMENT DAYS", "value": "7–21 May", "sub": "still unpaid", "at": A("c27", "unpaid")},
           {"label": "CAUSE OF ACTION", "value": "22 May", "sub": "earliest filing day", "at": A("c27", "twenty")},
           {"label": "LAST FILING DAY", "value": "22 June", "sub": "ordinary limit: a 31-day month", "tone": "red", "at": A("c27", "june")}])
cue(type="list", t0=S("c28"), t1=E("c28") + 0.05, head="These dates assume", head_at=S("c28") + 0.05,
    items=[{"n": 1, "text": "Proven actual receipt", "at": A("c28", "proven")},
           {"n": 2, "text": "No intervening payment", "at": A("c28", "intervening")},
           {"n": 3, "text": "No court closure or extension issue", "at": A("c28", "closure")}])
cue(type="cite", t0=A("c28", "special"), t1=E("c28") + 0.05, at=A("c28", "special"), tag="LAST DAY A COURT HOLIDAY?",
    text="Check the computation rule and the court calendar", icon="calendar")

# ── 8 · the court and the complaint ──────────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c29"), t1=E("c29") + 0.05, at=A("c29", "file"), act="NI ACT, 1881", num="142(1)",
    title="The complaint",
    points=[{"text": "In writing", "at": A("c29", "written")},
            {"text": "By the payee, or the holder in due course", "at": A("c29", "payee")},
            {"text": "Before the competent Magistrate", "at": A("c29", "competent")}])
cue(type="cite", t0=A("c29", "payee"), t1=E("c29") + 0.05, at=A("c29", "payee"), tag="s. 143A · INTERIM COMPENSATION",
    text="Discretionary: not an automatic award at filing", icon="info")
cue(type="compare", t0=S("c30"), t1=A("c31", "also") - 0.05, head="Which court? · s. 142(2)", head_at=S("c30") + 0.05,
    cols=[{"title": "Through an account", "icon": "landmark", "at": A("c30", "collection")},
          {"title": "Otherwise", "icon": "file-text", "at": A("c31", "presentation")}],
    rows=[{"cells": ["The payee's account branch", "The drawer's account branch"],
           "cells_at": [A("c30", "payee"), A("c31", "drawer")]}],   # 07-11: the (a)/(b) row dropped - with the case bar it shrank every cell to ~18 px
    verdict={"text": "Even if deposited at another branch of the payee's bank", "icon": "info", "at": A("c30", "deposited")})
cue(type="point", t0=A("c31", "also"), t1=E("c31") + 0.05, text="Subsequent complaints against the same drawer: check s. 142A(2)",
    icon="search-check", accent=True, at=A("c31", "check"))
cue(type="cite", t0=A("c30", "jurisdiction"), t1=E("c31") + 0.05, at=A("c30", "jurisdiction"), tag="SUPREME COURT OF INDIA",
    cases=[lw_case("bridgestone", "Bridgestone India Pvt. Ltd. v. Inderpal Singh", "24.11.2015"),
           lw_case("jaibalaji", "Jai Balaji Industries Ltd. v. HEG Ltd.", "28.11.2025")])
cue(type="list", t0=S("c32"), t1=E("c32") + 0.05, head="Organise the complaint file", head_at=S("c32") + 0.05,
    items=[{"n": 1, "text": "The cheque, return memo and debt records", "at": A("c32", "cheque")},
           {"n": 2, "text": "Notice, service proof and date calculation", "at": A("c32", "notice")},
           {"n": 3, "text": "The synopsis and affidavits", "at": A("c32", "synopsis")}])   # 07-11: 3 rows; a 4th/5th went under the case bar
cue(type="cite", t0=S("c32") + 0.3, t1=A("c32", "together") - 0.05, at=S("c32") + 0.3, tag="COMPANIES AND FIRMS · s. 141",
    text="Never assume every director or partner is liable merely by designation", icon="scale")
cue(type="cite", t0=A("c32", "together"), t1=E("c32") + 0.05, at=A("c32", "together"), tag="SUPREME COURT OF INDIA · 25.09.2025",
    cases=[lw_case("sanjabij", "Sanjabij Tari v. Kishore S. Borcar")])

# ── 9 · common mistakes ──────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="verdicts", t0=S("c33"), t1=E("c33") + 0.05,
    rows=[{"text": "Every return memo = automatic guilt", "ok": False, "at": A("c33", "every"), "strike_at": A("c33", "guilt")},
          {"text": "A reply = payment", "ok": False, "at": A("c33", "confusing"), "strike_at": A("c33", "payment")},
          {"text": "Filing early", "ok": False, "at": A("c33", "filing"), "strike_at": A("c33", "early")}])
cue(type="cite", t0=A("c33", "guilt"), t1=E("c33") + 0.05, at=A("c33", "guilt"), tag="s. 138 · THE MAXIMUM",
    text="Up to two years, a fine up to twice the cheque amount, or both: limits, not automatic outcomes", icon="scale")
cue(type="flow", t0=S("c34"), t1=E("c34") + 0.05, head="Presented again", head_at=S("c34") + 0.05,
    steps=[{"label": "A fresh presentation", "sub": "within validity", "icon": "landmark", "at": A("c34", "again")},
           {"label": "A subsequent dishonour", "icon": "ban", "at": A("c34", "subsequent")},
           {"label": "Fresh statutory compliance", "sub": "then prosecution is possible", "icon": "badge-check", "tone": "ok", "at": A("c34", "conditions")}])
cue(type="cite", t0=A("c34", "leathers"), t1=E("c34") + 0.05, at=A("c34", "leathers"), tag="SUPREME COURT OF INDIA · 26.09.2012",
    cases=[lw_case("msr", "MSR Leathers v. S. Palaniappan")])
cue(type="strike", t0=S("c35"), t1=E("c35") + 0.05, text="A reminder notice alone restarts the clock", icon="mail",
    at=S("c35") + 0.05, strike_at=A("c35", "restart"))
cue(type="point", t0=S("c36"), t1=A("c36", "it") - 0.05, text="After the payment window: document any later payment",
    icon="file-check", accent=True, at=S("c36") + 0.1)
cue(type="notequal", t0=A("c36", "it"), t1=E("c36") + 0.05, left="Later payment", right="the case erased",
    at=A("c36", "does"), left_at=A("c36", "it"),
    sub="Settlement or compounding needs legal steps", sub_at=A("c36", "settlement"))
cue(type="cite", t0=A("c36", "compounding"), t1=E("c36") + 0.05, at=A("c36", "compounding"), tag="NI ACT, 1881",
    text="Compounding: Section 147", icon="book-open")

# ── 10 · remember the sequence ───────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="timeline", t0=S("c37"), t1=E("c39") + 0.05,
    nodes=[{"label": "PRESENT", "value": "Three months", "sub": "from the cheque date", "at": A("c37", "three")},
           {"label": "NOTICE", "value": "30 days", "sub": "from receipt of bank information", "at": A("c37", "thirty")},
           {"label": "PAYMENT", "value": "15 days", "sub": "from receipt of notice", "at": A("c38", "fifteen")},
           {"label": "COMPLAINT", "value": "One month", "sub": "from the cause of action", "at": A("c38", "month")}])
cue(type="cite", t0=A("c38", "keep"), t1=E("c38") + 0.05, at=A("c38", "keep"), tag="EVERY CLOCK",
    text="Keep proof for every date", icon="file-check")
cue(type="cite", t0=S("c39") + 0.3, t1=E("c39") + 0.05, at=S("c39") + 0.3, tag="KEEP THEM APART",
    text="The statutory demand notice is not a court summons", icon="info")
cue(type="point", t0=S("c40"), t1=E("c40") + 0.05, text="Like · Share · Subscribe · lawworld.ai",
    icon="check", accent=True, at=A("c40", "thanks"))
