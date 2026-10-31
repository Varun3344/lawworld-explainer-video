# M/s. Bennett Property Holdings Company Limited v. M/s. PNB Techwaves Private Limited & Ors., C.R.P. No. 5206 of 2026 (Article 227),
# 2026:MHC:4388 (High Court of Judicature at Madras, P.B. Balaji J., single bench; reserved 28.09.2026, pronounced 30.10.2026;
# reportable per the court's judis "reportable = Y" list, the PDF's "Index : Yes/No" left unstruck): panel cues, run by
# split/build_course_plan.py (helpers: at S E cue fx have r3 PEND). Concept format as arm / kmv / vzj. English (High Courts page).
# Facts from the judgment (paras): the revision petitioner was the complainant before the Adjudicating Officer, TNRERA, Chennai (1);
# prayer: set aside the order of 15.07.2026 in C.C.P.(SR).No.38 of 2026 and direct the Registry to take the compensation complaint on
# file and number it (prayer); respondents served, named in the cause list, paper publication effected (order of 11.09.2026), no
# appearance, set ex parte (2); the complaint was dismissed on maintainability (4); the petitioner, as a property developer, entered
# into a Joint Venture Agreement with the land owners on 06.11.2012; by consent it stood terminated; role reversal: the land owners
# proposed to build, the petitioner desired to buy an apartment in the proposed construction; an agreement of sale for the undivided
# share + a separate construction agreement (4); the petitioner's grievance: the land owners, who assumed the role of a builder,
# delayed the construction and have not handed over possession as committed (5); its case: being the original proposed developer
# does not make the contract commercial; it qualifies as an aggrieved party under RERA (5). Held: Section 2(d) "allottee" and Section
# 2(zk) "promoter" quoted (7); the petitioner falls within "allottee" under Section 2; the agreement of sale for the undivided share
# and the construction agreement are not a commercial transaction; with the JVA ended the parties are "relegated to the status of
# strangers", all earlier relationship came to an end, no scope to reopen it to non-suit the petitioner (8); the sale and construction
# agreements are to be seen independently; land owners who assume the role of a developer are "equally bound to comply with the
# provisions of RERA" and liable to address apartment buyers' grievances; the officer "unnecessarily weighed" the earlier arrangement;
# even if a project is not registered, an aggrieved flat buyer or allottee may move the RERA authorities (9); the finding that the
# transaction is "an outcome of a monetary transaction" triable only by the Commercial Court is "clearly perverse, improper and
# unsubstantiated" (10). Orders (11): revision allowed; the order of 15.07.2026 set aside; the officer shall entertain the complaint
# if otherwise in order, number it, issue notice to the respondents, give them adequate and reasonable opportunity to file a counter
# or objection, and decide it on merits; no costs.
# Not on any card: no finding that the construction was in fact delayed (the delay stays Bennett's grievance); no compensation
# awarded; no claim that this project was unregistered (the para 9 rule is shown as a general rule); no "admitted" / "admittedly".
# Flow policy / neutrality: the respondents are "the land owners" on every card; the cite bar (which carries the first respondent's
# name, as the case title) runs over c03-c04 only, so it is off screen when c05 states the delay grievance.
# Official Madras High Court portrait (hcmadras.tn.gov.in, present judges page) on the bench card. List lines <= 52 chars.
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen, as cdp)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
STING = {"kicker": "MADRAS HIGH COURT · JUDGMENT EXPLAINED", "title": "Ex-developer is a RERA allottee", "sub": "High Court of Madras · C.R.P. No. 5206 of 2026 · 2026:MHC:4388"}
ENDCARD = {"title": "Ex-developer is a RERA allottee", "line": "Ended joint venture no bar · the complaint goes back to the RERA officer", "sub": "LawWorld: legal research for advocates"}

# ── 1 · developer turned buyer? ──────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "client"), text="Your client was the developer. The joint venture ended and it agreed to buy a flat. Can it still go to RERA?", hl="still go to RERA?")
cue(type="bench", t0=S("c02"), t1=E("c02") + 0.05, tag="Madras High Court · 30 October 2026",
    judges=[{"name": "Justice P.B. Balaji", "photo": "../brand/judges/pb_balaji.jpg", "at": A("c02", "honourable")}])

# ── 2 · the role reversal ────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=A("c03", "bennett"), t1=E("c04") + 0.05, at=A("c03", "bennett"), tag="HIGH COURT OF MADRAS · 30.10.2026",
    cases=[{"name": "M/s. Bennett Property Holdings Co. Ltd. v. M/s. PNB Techwaves Pvt. Ltd. & Ors.", "cite": "2026:MHC:4388 · C.R.P. No. 5206 of 2026"}])
cue(type="flow", t0=S("c03"), t1=E("c03") + 0.05, head="The joint venture", head_at=S("c03") + 0.05,
    steps=[{"label": "Joint Venture Agreement · 6 Nov 2012", "sub": "Bennett, a property developer, with the land owners", "icon": "file-text", "at": A("c03", "signed")},
           {"label": "Bennett: the developer", "sub": "it had agreed to develop the land owners' property", "icon": "user", "at": A("c03", "develop")},
           {"label": "Terminated by consent", "sub": "the joint venture came to an end", "icon": "x", "tone": "stop", "at": A("c03", "consent")}])
cue(type="flow", t0=S("c04"), t1=E("c04") + 0.05, head="Then the roles reversed", head_at=A("c04", "roles"),
    steps=[{"label": "The land owners would build", "sub": "they proposed to put up the construction", "icon": "landmark", "at": A("c04", "build")},
           {"label": "Bennett would buy an apartment", "sub": "in the proposed construction", "icon": "user", "at": A("c04", "apartment")},
           {"label": "Two agreements", "sub": "sale of an undivided share in the land · a separate construction agreement", "icon": "file-text", "at": A("c04", "agreement")}])
cue(type="list", t0=S("c05"), t1=A("c05", "sought") - 0.05, head="Bennett's grievance", head_at=A("c05", "says"),
    items=[{"n": 1, "text": "Construction delayed, Bennett says", "at": A("c05", "delayed")},
           {"n": 2, "text": "Possession not handed over as committed", "at": A("c05", "possession")}])
cue(type="point", t0=A("c05", "sought") - 0.05, t1=E("c05") + 0.05, text="Compensation complaint · C.C.P.(SR) No. 38 of 2026 · before the Adjudicating Officer, TNRERA, Chennai", icon="landmark", at=A("c05", "sought"))

# ── 3 · rejected as commercial ───────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c06"), t1=E("c06") + 0.05, head="The officer's order · 15 July 2026", head_at=A("c06", "july"),
    steps=[{"label": "Relied on the old joint venture", "sub": "the earlier arrangement between the parties", "icon": "search", "at": A("c06", "citing")},
           {"label": "Complaint rejected: not maintainable", "sub": "not taken on file · no case number", "icon": "x", "tone": "stop", "at": A("c06", "rejected")},
           {"label": "“an outcome of a monetary transaction”", "sub": "triable only by the Commercial Court, not RERA, the officer held", "icon": "landmark", "tone": "stop", "at": A("c06", "monetary")}])

# ── 4 · what the court held ──────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c07"), t1=A("c07", "buying") - 0.05, text="Section 2(d), RERA Act, 2016: “allottee” is the person to whom an apartment is allotted, sold or otherwise transferred by the promoter", icon="scale", accent=True, at=A("c07", "allottee"))
cue(type="notequal", t0=A("c07", "buying") - 0.05, t1=E("c07") + 0.05, left="This flat + undivided share", right="a commercial transaction", at=A("c07", "buying"),
    left_at=A("c07", "buying"), sub="Agreement of sale + construction agreement: not commercial, the Court held", sub_at=A("c07", "commercial"))
cue(type="flow", t0=S("c08"), t1=E("c08") + 0.05, head="Why the officer erred", head_at=S("c08") + 0.05,
    steps=[{"label": "Joint venture ended: the parties became strangers", "sub": "all ties under the joint venture came to an end", "icon": "x", "at": A("c08", "strangers")},
           {"label": "The old deal cannot non-suit the buyer", "sub": "the sale and construction agreements stand on their own", "icon": "file-check", "at": A("c08", "cannot")},
           {"label": "Land owners turned developers: bound by RERA", "sub": "liable to answer apartment buyers' grievances", "icon": "scale", "tone": "ok", "at": A("c08", "land")}],
    note={"text": "Even if a project is not registered, an aggrieved flat buyer or allottee may move RERA, the Court noted", "icon": "info", "at": A("c08", "bound")})

# ── 5 · the result ───────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="verdicts", t0=S("c09"), t1=A("c09", "complaint") - 0.05,
    rows=[{"text": "The “monetary transaction” finding: “clearly perverse, improper and unsubstantiated”", "ok": False, "at": A("c09", "perverse")},
          {"text": "Revision allowed · order of 15 July 2026 set aside · no costs", "ok": True, "at": A("c09", "allowed")}])
cue(type="list", t0=A("c09", "complaint") - 0.05, t1=E("c09") + 0.05, head="Back to the Adjudicating Officer", head_at=A("c09", "complaint"),
    items=[{"n": 1, "text": "Entertain and number it, if otherwise in order", "at": A("c09", "numbered")},
           {"n": 2, "text": "Notice to the land owners, set ex parte here", "at": A("c09", "owners")},
           {"n": 3, "text": "Time to file a counter, then decide on merits", "at": A("c09", "decided")}])
cue(type="point", t0=S("c10"), t1=E("c10") + 0.05, text="Like · Share · Subscribe · lawworld.ai", icon="check", accent=True, at=A("c10", "like"))
