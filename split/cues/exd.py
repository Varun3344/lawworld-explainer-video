# Setting Aside an Ex Parte Decree (Order IX Rule 13 CPC) - CONCEPT VIDEO (legal-concept explainer, Cause of Action build): panel
# cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND). Source: split/scripts/exd.txt (no storyboard PDF; its
# // header lists the bare-act wording and the judgment passages, all read 10-11-2026). 38 clips, c38 = the closing line.
# Held to the script header:
#  - a case is shown by name, court and decision date (+ the header's paragraph), never SCC / AIR / INSC / SCR. G.P. Srivastava has
#    no confirmed paragraph: its bar carries no paragraph. Bhanu Kumar Jain: paras 26 and 38 as the header gives them;
#  - statutory wording on screen follows the header ("Order IX Rule 13" style, Article 123 of the Limitation Act, Section 96(2));
#    quotation marks only around words the header quotes;
#  - setting aside is never automatic or promised: "shall" only once the court is satisfied (c11); NO "DECREE SET ASIDE" stamp, no
#    stamp at all; relief comes "upon such terms" (c12); discretion is "normally" exercised in his favour (c25);
#  - the affixed summons is never declared "NOT SERVED": it is "Sunil's ground" (c13, c20); the second proviso can defeat a claim of
#    mere irregular service (c15-c16);
#  - Article 123's knowledge rule applies only where the summons was NOT duly served (c19); its Explanation (Order V Rule 20
#    substituted service) is a c19 footnote only and is never tied to Sunil's affixing (Rule 17); s. 5 is a discretion (c21);
#  - an appeal and an application may run together, but a dismissed appeal ends the Rule 13 route (c28-c29); only a REJECTION of a
#    Rule 13 application is appealable under Order XLIII Rule 1(d) (c33); neither route stays execution by itself (c34); no provision
#    is cited for a stay pending a Rule 13 application (c37); the bank-account attachment carries no rule citation (c01, c09);
#  - Pallavi, Sunil, the invoices, the old shop, the affixed summons and the attachment are HYPOTHETICAL: every clip that tells his
#    story carries the HYPOTHETICAL EXAMPLE kicker (c07-c09, c13, c16, c20);
#  - on screen only (not narrated): Order IX Rule 6(1)(c) (c05 footer), Order V Rule 19 (c13 footer), the 1976 amendment (c15 footer),
#    the Explanation's withdrawal carve-out (c17 footer), Article 123's Explanation (c19 footer), Order XXI carve-out of s. 5 (c21
#    footer), Bhanu Kumar Jain para 38's other pleas (c31 footer), Order XLI Rule 5(3) conditions (c34 footer), s. 104 (c33 note).
# Layout (07-11 / 10-11 lessons): lists <= 3 rows under a citation bar (the 4-row c37 checklist has no bar); one-row compare cards
# under single-text bars only; no two-case bars.
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

STING = {"kicker": "CIVIL PROCEDURE · CPC EXPLAINED", "title": "Setting Aside an Ex Parte Decree",
         "sub": "Order IX Rule 13 CPC: when a decree passed in your absence may be set aside"}
ENDCARD = {"title": "Setting Aside an Ex Parte Decree", "line": "Two grounds · apply within 30 days · the court sets the terms",
           "sub": "LawWorld: legal research for advocates"}

HYP = "HYPOTHETICAL EXAMPLE"
SC = "SUPREME COURT OF INDIA"
GPS = "G.P. Srivastava v. R.K. Raizada"      # SC 03.03.2000 - no confirmed paragraph
BHANU = "Bhanu Kumar Jain v. Archana Kumar"   # SC 17.12.2004 - paras 26, 38

# ── 1 · the decree you never saw ─────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="timeline", t0=S("c01"), t1=A("c01", "can") - 0.05,
    nodes=[{"label": "A MONEY DECREE", "value": "Passed", "sub": "in a suit you never knew about", "at": A("c01", "decree")},
           {"label": "NOW", "value": "Account attached", "sub": "your bank account", "tone": "red", "at": A("c01", "bank")}])
cue(type="question", t0=A("c01", "can") - 0.05, t1=A("c02", "today") - 0.05, at=A("c01", "can"),
    text="Can that decree be undone?", hl="undone?")
cue(type="section", t0=A("c02", "today") - 0.05, t1=E("c02") + 0.05, at=A("c02", "order"), act="CPC, 1908", num="Order IX Rule 13",
    title="Setting aside an ex parte decree",
    points=[{"text": "The defendant applies to the court that passed the decree", "at": A("c02", "setting")}])
cue(type="flow", t0=S("c03"), t1=E("c03") + 0.05, head="An ex parte decree", head_at=S("c03") + 0.05,
    steps=[{"label": "Passed in the defendant's absence", "icon": "user-round", "at": A("c03", "passed")},
           {"label": "After the suit is heard without him", "icon": "gavel", "tone": "ok", "at": A("c03", "heard")}])

# ── 2 · how a suit goes ex parte ─────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c04"), t1=E("c04") + 0.05, at=A("c04", "order"), act="CPC, 1908", num="Order IX Rule 6",
    title="When only the plaintiff appears",
    points=[{"text": "The plaintiff appears", "at": A("c04", "plaintiff")},
            {"text": "The defendant does not, when the suit is called on for hearing", "at": A("c04", "defendant")}])
cue(type="compare", t0=S("c05"), t1=E("c05") + 0.05, head="Was due service proved?", head_at=S("c05") + 0.05,
    cols=[{"title": "Proved", "icon": "file-check", "at": A("c05", "due")},
          {"title": "Not proved", "icon": "mail", "at": A("c05", "otherwise")}],
    rows=[{"cells": ["The court may order the suit to be heard ex parte", "A second summons must be issued and served"],
           "cells_at": [A("c05", "may"), A("c05", "second")]}])
cue(type="cite", t0=A("c05", "otherwise"), t1=E("c05") + 0.05, at=A("c05", "otherwise"), tag="ORDER IX RULE 6",
    text="Clause (c): served, but not in sufficient time? The hearing is postponed, with notice of the new day", icon="info")
cue(type="flow", t0=S("c06"), t1=E("c06") + 0.05, head="Order IX Rule 7: before the decree", head_at=S("c06") + 0.05,
    steps=[{"label": "He appears", "sub": "at or before the adjourned hearing", "icon": "user-round", "at": A("c06", "appear")},
           {"label": "Shows good cause", "sub": "for his previous non-appearance", "icon": "file-text", "at": A("c06", "good")},
           {"label": "Heard on terms", "sub": "as to costs or otherwise", "icon": "scale", "tone": "ok", "at": A("c06", "heard")}])
cue(type="cite", t0=A("c06", "rule"), t1=E("c06") + 0.05, at=A("c06", "rule"), tag="ORDER IX RULE 7",
    text="Heard in answer to the suit “as if he had appeared on the day fixed for his appearance”", icon="book-open")

# ── 3 · a hypothetical: Sunil's case ─────────────────────────────────────────────────────────────────────────────────────────────
cue(type="kicker", t0=S("c07"), t1=E("c09") + 0.05, at=S("c07") + 0.05, text=HYP)
cue(type="flow", t0=S("c07"), t1=E("c07") + 0.05, head="Pallavi v. Sunil", head_at=S("c07") + 0.1,
    steps=[{"label": "Pallavi", "sub": "a paper supplier · the plaintiff", "icon": "user-round", "at": A("c07", "pallavi")},
           {"label": "Sues Sunil", "sub": "a printer · the defendant", "icon": "gavel", "at": A("c07", "sunil")},
           {"label": "Money due", "sub": "on unpaid invoices", "icon": "receipt-text", "tone": "ok", "at": A("c07", "money")}])
cue(type="flow", t0=S("c08"), t1=E("c08") + 0.05, head="The summons", head_at=S("c08") + 0.05,
    steps=[{"label": "Sent to a shop", "sub": "Sunil's old address", "icon": "mail", "at": A("c08", "shop")},
           {"label": "Sunil left it", "sub": "two years ago", "icon": "house", "at": A("c08", "left")},
           {"label": "Affixed to the door", "sub": "says the process server's report", "icon": "file-text", "at": A("c08", "affixed")}])
cue(type="timeline", t0=S("c09"), t1=E("c09") + 0.05,
    nodes=[{"label": "THE COURT", "value": "Hears it ex parte", "at": A("c09", "hears")},
           {"label": "THEN", "value": "A money decree", "at": A("c09", "money")},
           {"label": "SUNIL FIRST LEARNS", "value": "Account attached", "sub": "his bank account", "tone": "red", "at": A("c09", "bank")}])

# ── 4 · Rule 13: two grounds ─────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c10"), t1=E("c10") + 0.05, head="Order IX Rule 13: after the decree", head_at=S("c10") + 0.05,
    steps=[{"label": "The defendant applies", "icon": "file-pen-line", "at": A("c10", "apply")},
           {"label": "To the court that passed it", "icon": "landmark", "at": A("c10", "passed")},
           {"label": "For an order setting it aside", "icon": "scale", "at": A("c10", "setting")}])
cue(type="list", t0=S("c11"), t1=E("c11") + 0.05, head="If satisfied, the court shall set it aside", head_at=S("c11") + 0.05,
    items=[{"n": 1, "text": "The summons was not duly served", "at": A("c11", "summons")},
           {"n": 2, "text": "Or he was prevented by sufficient cause from appearing", "at": A("c11", "prevented")}])
cue(type="cite", t0=A("c11", "satisfied"), t1=E("c11") + 0.05, at=A("c11", "satisfied"), tag="ORDER IX RULE 13 · TWO GROUNDS",
    text="Either ground, “if he satisfies the Court”", icon="book-open")
cue(type="flow", t0=S("c12"), t1=E("c12") + 0.05, head="“upon such terms … as it thinks fit”", head_at=S("c12") + 0.05,
    steps=[{"label": "Costs", "icon": "indian-rupee", "at": A("c12", "costs")},
           {"label": "Payment into court, or otherwise", "icon": "landmark", "at": A("c12", "payment")},
           {"label": "A day to proceed with the suit", "icon": "calendar-days", "tone": "ok", "at": A("c12", "appoints")}])
cue(type="kicker", t0=S("c13"), t1=E("c13") + 0.05, at=S("c13") + 0.05, text=HYP)
cue(type="point", t0=S("c13"), t1=A("c13", "under") - 0.05, text="Sunil's ground: the summons was not duly served",
    icon="search", accent=True, at=A("c13", "sunil"))
cue(type="section", t0=A("c13", "under") - 0.05, t1=E("c13") + 0.05, at=A("c13", "order"), act="CPC, 1908", num="Order V Rule 17",
    title="Service by affixing",
    points=[{"text": "On the outer door or a conspicuous part of the house", "at": A("c13", "affixing")},
            {"text": "Where he ordinarily resides, carries on business or personally works for gain", "at": A("c13", "ordinarily")}])
cue(type="cite", t0=A("c13", "under"), t1=E("c13") + 0.05, at=A("c13", "under"), tag="ORDER V RULE 19",
    text="Return not on affidavit: the court examines the serving officer, then declares due service or orders fresh service", icon="info")

# ── 5 · the provisos and the Explanation ─────────────────────────────────────────────────────────────────────────────────────────
cue(type="kicker", t0=S("c14"), t1=E("c14") + 0.05, at=S("c14") + 0.05, text="ORDER IX RULE 13 · FIRST PROVISO")
cue(type="splitcard", t0=S("c14"), t1=E("c14") + 0.05,
    left={"title": "AGAINST ONE ONLY?", "text": "a decree that cannot be set aside against one defendant only", "icon": "user-round",
          "at": A("c14", "decree")},
    right={"title": "ALL OR ANY", "text": "it may be set aside against the other defendants also", "icon": "users", "at": A("c14", "others")})
cue(type="quote", t0=S("c15"), t1=E("c15") + 0.05, at=A("c15", "second"), reveal=r3(A("c15", "appear") - A("c15", "second")),
    text="… no Court shall set aside a decree passed ex parte merely on the ground that there has been an irregularity in the service "
         "of summons, if it is satisfied that the defendant had notice of the date of hearing and had sufficient time to appear …",
    hl=["merely", "had notice of the date of hearing", "sufficient time to appear"])
cue(type="cite", t0=S("c15") + 0.3, t1=E("c15") + 0.05, at=S("c15") + 0.3, tag="ORDER IX RULE 13 · SECOND PROVISO",
    text="Added by Act 104 of 1976, in force from 1 February 1977", icon="book-open")
cue(type="kicker", t0=S("c16"), t1=E("c16") + 0.05, at=S("c16") + 0.05, text=HYP)
cue(type="equation", t0=S("c16"), t1=E("c16") + 0.05,
    terms=[{"text": "IF SUNIL KNEW THE DATE IN TIME", "at": A("c16", "sunil")},
           {"op": "+", "text": "IRREGULAR SERVICE ALONE", "at": A("c16", "irregular")},
           {"op": "=", "text": "NOT ENOUGH, ON ITS OWN", "result": True, "at": A("c16", "will")}])
cue(type="flow", t0=S("c17"), t1=E("c17") + 0.05, head="The Explanation", head_at=S("c17") + 0.05,
    steps=[{"label": "An appeal against the ex parte decree", "icon": "landmark", "at": A("c17", "appeal")},
           {"label": "Disposed of, other than by withdrawal", "icon": "gavel", "at": A("c17", "disposed")},
           {"label": "No Rule 13 application lies", "icon": "ban", "tone": "stop", "at": A("c17", "application")}])
cue(type="cite", t0=A("c17", "withdrawal"), t1=E("c17") + 0.05, at=A("c17", "withdrawal"), tag="ORDER IX RULE 13 · EXPLANATION",
    text="An appeal withdrawn? The Explanation does not bar the application", icon="info")

# ── 6 · the 30-day clock ─────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="counters", t0=S("c18"), t1=E("c18") + 0.05, head="Article 123, Limitation Act", head_at=S("c18") + 0.05,
    items=[{"value": 30, "unit": "DAYS", "label": "To apply to set it aside", "sub": "from the date of the decree", "at": A("c18", "thirty")}])
cue(type="cite", t0=A("c18", "limitation"), t1=E("c18") + 0.05, at=A("c18", "limitation"), tag="LIMITATION ACT, 1963 · ARTICLE 123",
    text="“To set aside a decree passed ex parte or to re-hear an appeal decreed or heard ex parte”", icon="book-open")
cue(type="compare", t0=S("c19"), t1=E("c19") + 0.05, head="When do the 30 days start?", head_at=S("c19") + 0.05,
    cols=[{"title": "Duly served", "icon": "file-check", "at": S("c19") + 0.15},
          {"title": "Not duly served", "icon": "mail", "at": A("c19", "summons")}],
    rows=[{"cells": ["The date of the decree", "When the applicant had knowledge of the decree"],
           "cells_at": [S("c19") + 0.4, A("c19", "knowledge")]}])
# Article 123's Explanation: a footnote under c19 only, worded generally (Sunil's summons was affixed, Order V Rule 17)
cue(type="cite", t0=A("c19", "thirty"), t1=E("c19") + 0.05, at=A("c19", "thirty"), tag="ARTICLE 123 · EXPLANATION",
    text="For this article, substituted service under Order V Rule 20 is not deemed due service", icon="info")
cue(type="kicker", t0=S("c20"), t1=E("c20") + 0.05, at=S("c20") + 0.05, text=HYP)
cue(type="splitcard", t0=S("c20"), t1=E("c20") + 0.05,
    left={"title": "IF SUNIL SHOWS", "text": "he was not duly served", "icon": "search", "at": A("c20", "sunil")},
    right={"title": "HIS 30 DAYS RUN", "text": "from when he learnt of the decree", "icon": "calendar-days", "at": A("c20", "thirty")})
cue(type="section", t0=S("c21"), t1=E("c21") + 0.05, at=A("c21", "section"), act="LIMITATION ACT, 1963", num="5",
    title="Missed the 30 days?",
    points=[{"text": "A late application “may be admitted”", "at": A("c21", "admit")},
            {"text": "On sufficient cause for the delay", "at": A("c21", "sufficient")}])
cue(type="cite", t0=A("c21", "limitation"), t1=E("c21") + 0.05, at=A("c21", "limitation"), tag="LIMITATION ACT, 1963 · SECTION 5",
    text="Any application other than under Order XXI CPC: a Rule 13 application is covered", icon="book-open")

# ── 7 · what counts as sufficient cause ──────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c22"), t1=A("c22", "supreme") - 0.05, text="Ground 2: prevented by sufficient cause",
    icon="scale", accent=True, at=A("c22", "second"))
cue(type="quote", t0=A("c22", "supreme") - 0.05, t1=E("c22") + 0.05, at=A("c22", "supreme"),
    reveal=r3(A("c22", "justice") - A("c22", "supreme")),
    text="The words ‘was prevented by any sufficient cause from appearing’ must be liberally construed to enable the court to do "
         "complete justice between the parties",
    hl=["liberally construed", "complete justice"])
# one case bar for the whole chapter (the header gives no confirmed paragraph)
cue(type="cite", t0=A("c22", "G"), t1=E("c26") + 0.05, at=A("c22", "G"), tag=f"{SC} · 03.03.2000",
    cases=[{"name": GPS}])
cue(type="splitcard", t0=S("c23"), t1=E("c23") + 0.05,
    left={"title": "PARTICULARLY WHERE", "text": "no negligence or inaction is imputable to him", "icon": "user-round",
          "at": A("c23", "particularly")},
    right={"title": "AN ELASTIC EXPRESSION", "text": "no hard and fast guidelines: the courts have wide discretion", "icon": "scale",
           "at": A("c23", "elastic")})
cue(type="verdicts", t0=S("c24"), t1=E("c24") + 0.05,
    rows=[{"text": "The cause on the date the court proceeded ex parte", "ok": True, "at": A("c24", "cause")},
          {"text": "Earlier lapses, already overlooked, count against him", "ok": False, "at": A("c24", "earlier"),
           "strike_at": A("c24", "cannot")}])
cue(type="equation", t0=S("c25"), t1=E("c25") + 0.05,
    terms=[{"text": "PROMPT, WITHIN TIME", "at": A("c25", "comes")},
           {"op": "+", "text": "ABSENCE NOT MALA FIDE OR INTENTIONAL", "at": A("c25", "mala")},
           {"op": "=", "text": "DISCRETION NORMALLY IN HIS FAVOUR", "result": True, "at": A("c25", "normally")}])
cue(type="quote", t0=S("c26"), t1=E("c26") + 0.05, at=S("c26") + 0.1, reveal=r3(A("c26", "merits") - S("c26")),
    text="For the absence of a party in the case the other side can be compensated by adequate costs and the lis decided on merits.",
    hl=["adequate costs", "decided on merits"])

# ── 8 · appeal, application, or both ─────────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c27"), t1=E("c27") + 0.05, at=A("c27", "section"), act="CPC, 1908", num="96(2)",
    title="Appeal from original decree",
    points=[{"text": "“An appeal may lie from an original decree passed ex parte”", "at": A("c27", "appeal")}])
cue(type="quote", t0=S("c28"), t1=E("c28") + 0.05, at=A("c28", "bhanu"), reveal=r3(A("c28", "simultaneously") - A("c28", "bhanu")),
    text="… two clear options, one, to file an appeal and another to file an application … He can take recourse to both the "
         "proceedings simultaneously",
    hl=["two clear options", "both the proceedings simultaneously"])
cue(type="cite", t0=A("c28", "bhanu"), t1=E("c29") + 0.05, at=A("c28", "bhanu"), tag=f"{SC} · 17.12.2004",
    cases=[{"name": BHANU, "cite": "para 26"}])
cue(type="flow", t0=S("c29"), t1=E("c29") + 0.05, head="If the appeal is dismissed", head_at=S("c29") + 0.05,
    steps=[{"label": "Appeal dismissed", "icon": "gavel", "at": A("c29", "dismissed")},
           {"label": "The decree merges", "sub": "with the appellate order", "icon": "layers", "at": A("c29", "merges")},
           {"label": "Rule 13 application not maintainable", "icon": "ban", "tone": "stop", "at": A("c29", "longer")}])
cue(type="flow", t0=S("c30"), t1=E("c30") + 0.05, head="The converse is not true", head_at=S("c30") + 0.05,
    steps=[{"label": "The Rule 13 application fails", "icon": "x", "at": A("c30", "fails")},
           {"label": "The appeal survives", "icon": "landmark", "tone": "ok", "at": A("c30", "survives")}],
    note={"text": "But he cannot reargue sufficient cause there", "icon": "ban", "at": A("c30", "reargue")})
cue(type="cite", t0=S("c30") + 0.05, t1=E("c30") + 0.05, at=S("c30") + 0.05, tag=f"{SC} · 17.12.2004",
    cases=[{"name": BHANU, "cite": "paras 26, 38"}])
cue(type="verdicts", t0=S("c31"), t1=E("c31") + 0.05,
    rows=[{"text": "Reargue sufficient cause", "ok": False, "at": S("c31") + 0.1, "strike_at": A("c31", "argue")},
          {"text": "The evidence on record did not justify the decree", "ok": True, "at": A("c31", "evidence")}])
cue(type="cite", t0=E("c30") + 0.05, t1=E("c31") + 0.05, at=E("c30") + 0.05, tag="BHANU KUMAR JAIN · PARA 38",
    text="Also open: the suit was otherwise not maintainable, or the court lacked jurisdiction", icon="scale")

# ── 9 · notice, appeal and execution ─────────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c32"), t1=E("c32") + 0.05, at=A("c32", "rule"), act="CPC, 1908", num="Order IX Rule 14",
    title="No decree set aside without notice",
    points=[{"text": "Notice of the application", "at": A("c32", "notice")},
            {"text": "“served on the opposite party”", "at": A("c32", "opposite")}])
cue(type="section", t0=S("c33"), t1=E("c33") + 0.05, at=A("c33", "rule"), act="CPC, 1908", num="Order XLIII Rule 1(d)",
    title="Appeals from orders",
    points=[{"text": "An order under Order IX Rule 13 rejecting the application", "at": A("c33", "rejected")},
            {"text": "“in a case open to appeal”", "at": A("c33", "forty")}],
    note={"text": "Only a rejection is listed · read with Section 104", "icon": "book-open", "at": A("c33", "clause")})
cue(type="notequal", t0=S("c34"), t1=A("c34", "order") - 0.05, left="An appeal alone", right="a stay",
    at=A("c34", "alone"), left_at=A("c34", "appeal"), icon="scale")
cue(type="section", t0=A("c34", "order") - 0.05, t1=E("c34") + 0.05, at=A("c34", "order"), act="CPC, 1908", num="Order XLI Rule 5",
    title="Stay by the appellate court",
    points=[{"text": "May order stay of execution, for sufficient cause", "at": A("c34", "stay", 2)}],
    note={"text": "Neither the appeal nor a Rule 13 application stays execution by itself", "icon": "info",
          "at": A("c34", "sufficient")})
cue(type="cite", t0=A("c34", "order"), t1=E("c34") + 0.05, at=A("c34", "order"), tag="ORDER XLI RULE 5(3)",
    text="Conditions: substantial loss, no unreasonable delay, and security", icon="book-open")

# ── 10 · your checklist ──────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="list", t0=S("c35"), t1=E("c35") + 0.05, head="Act fast", head_at=A("c35", "act"),
    items=[{"n": 1, "text": "Apply within 30 days of the decree", "at": A("c35", "apply")},
           {"n": 2, "text": "Or of learning of it, if the summons was not duly served", "at": A("c35", "learning")}])
cue(type="checklist", t0=S("c36"), t1=E("c36") + 0.05, head="Get certified copies", head_at=A("c36", "certified"),
    items=[{"n": 1, "text": "The order sheet", "at": A("c36", "order")},
           {"n": 2, "text": "The process server's report", "at": A("c36", "process")},
           {"n": 3, "text": "Check the address and manner of service", "at": A("c36", "address")}])
cue(type="checklist", t0=S("c37"), t1=E("c37") + 0.05, head="In the application", head_at=S("c37") + 0.05,
    items=[{"n": 1, "text": "Support sufficient cause with documents", "at": A("c37", "support")},
           {"n": 2, "text": "Offer costs", "at": A("c37", "offer")},
           {"n": 3, "text": "Check whether an appeal was filed", "at": A("c37", "check")},
           {"n": 4, "text": "Seek a stay of execution, if needed", "at": A("c37", "stay")}])
cue(type="point", t0=S("c38"), t1=E("c38") + 0.05, text="Like · Share · Subscribe · lawworld.ai",
    icon="check", accent=True, at=A("c38", "thanks"))
