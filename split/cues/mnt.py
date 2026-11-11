# Maintenance under Section 144 BNSS - CONCEPT VIDEO (legal-concept explainer, Cause of Action build): panel cues, run by
# split/build_course_plan.py (helpers: at S E cue fx have r3 PEND). Script: split/scripts/mnt.txt (no owner storyboard; its // header
# gives the BNSS s.144-146 wording from the Gazette, the case paragraphs and the panel rules, all checked 10-11-2026). 38 clips,
# c38 = the closing line.
# Held to the script header:
#  - a case is shown by name + court + year (+ the header's paragraph), never SCC / AIR / INSC / SCR; every case was decided on
#    s.125 CrPC, so each case bar says OLD CODE. Paragraphs the header marks unconfirmed are left off: Chaturbhuj paras 7-8 (c13),
#    Rajnesh Part B-III (c16-c17) and Final Directions VI(a) (c22), Kuldip Kaur (c30); Vijaya Manohar Arbat has headnotes only (c08).
#    Printed: Chaturbhuj para 6 (c04, c37), Anju Garg para 10 (c14), Rajnesh para 113 (c20) and para 72 (c21, c35, c36), Abdul Samad's
#    numbered conclusions (c11). Mohd. Abdul Samad is not spoken: footer only (c11);
#  - s.145(1)(b) is shown as the statute words "where he or his wife resides" (c31), never "where the claimant resides";
#  - s.144(1)(b) dropped "minor" (c09): shown side by side with s.125(1)(b), then "NOT YET SETTLED" - adult children are never shown
#    as entitled under (b); the c07 card is clause (c) only (an adult child with an abnormality or injury);
#  - Deepa, her son and Raghu are HYPOTHETICAL: a kicker over every clip that names them (c12-c13, c25, c27-c29, c31); Raghu is the
#    RESPONDENT, never a defaulter or deserter;
#  - no amount is promised or computed: the only figure is the old ₹500 ceiling (c15); "the Magistrate decides" / "the evidence";
#  - the s.144(4)-(5) bars are a WIFE's only (c23 note, c24); parents claim against a son OR a daughter (c08);
#  - "maintenance is not a penalty" stays on screen in chapter 10 (c37 split card, right half); c35-c36 are filing practice (c35 footer);
#  - on screen only (not narrated): "Magistrate of the first class" (c05 footer), Act 50 of 2001 (c15 footer), the second / third
#    provisos (c18 counters), s.144(3) Explanation in full (c26), s.147 (c27 footer), (c)'s illegitimate-child limb (c31), Family Courts
#    Act s.7(2)(a) (c33 footer), s.146(3)(a) remarriage (c34 footer).
# Layout (07-11 lessons): a stamp after a question -> question y=215, stamp y=900; no list over 3 rows under a citation bar; no
# compare card shares the screen with a two-case bar; clause letters stay out of capitalised fields (tags, column / split titles,
# timeline labels): "(b)" would read "(B)".
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

STING = {"kicker": "CRIMINAL PROCEDURE · BNSS EXPLAINED", "title": "Maintenance under Section 144 BNSS",
         "sub": "Who can claim, how much can be ordered, and how the order is enforced"}
ENDCARD = {"title": "Maintenance under Section 144 BNSS", "line": "Prevents destitution, not a penalty · the evidence decides the amount",
           "sub": "LawWorld: legal research for advocates"}

HYP = "HYPOTHETICAL EXAMPLE"
HYP_DR = "HYPOTHETICAL EXAMPLE · DEEPA AND RAGHU"
SC = "SUPREME COURT OF INDIA"
OLD = "OLD CODE"
CHAT = "Chaturbhuj v. Sita Bai"            # SC 27.11.2007
RAJ = "Rajnesh v. Neha"                    # SC 04.11.2020

# ── 1 · maintenance: a right, not charity ────────────────────────────────────────────────────────────────────────────────────────
cue(type="list", t0=S("c01"), t1=E("c01") + 0.05, head="Three questions", head_at=S("c01") + 0.05,
    items=[{"n": 1, "text": "Can a wife who earns a salary still claim?", "at": A("c01", "wife")},
           {"n": 2, "text": "Can parents claim from a married daughter?", "at": A("c01", "parents")},
           {"n": 3, "text": "Does jail wipe out arrears?", "at": A("c01", "jail")}])
cue(type="flow", t0=S("c02"), t1=E("c02") + 0.05, head="In this video", head_at=S("c02") + 0.05,
    steps=[{"label": "Who can claim", "icon": "users", "at": A("c02", "who")},
           {"label": "How much can be ordered", "icon": "indian-rupee", "at": A("c02", "much")},
           {"label": "How the order is enforced", "icon": "gavel", "tone": "ok", "at": A("c02", "enforced")}])
cue(type="section", t0=S("c03"), t1=E("c03") + 0.05, at=A("c03", "section"), act="BNSS, 2023", num="144",
    title="Order for maintenance of wives, children and parents",
    points=[{"text": "Bharatiya Nagarik Suraksha Sanhita, 2023", "at": A("c03", "bharatiya")},
            {"text": "Replaces Section 125 CrPC (old Code)", "at": A("c03", "replaces")}])
cue(type="quote", t0=S("c04"), t1=E("c04") + 0.05, at=S("c04") + 0.1, reveal=r3(A("c04", "destitution") - S("c04") - 0.1),
    text="… a measure of social justice and is specially enacted to protect women and children … "
         "The object is to prevent vagrancy and destitution.",
    hl=["a measure of social justice", "prevent vagrancy and destitution"])
cue(type="cite", t0=A("c04", "chaturbhuj"), t1=E("c04") + 0.05, at=A("c04", "chaturbhuj"), tag=f"{SC} · 2007 · {OLD}",
    cases=[{"name": CHAT, "cite": "para 6"}])

# ── 2 · who can claim ────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c05"), t1=E("c05") + 0.05, head="Who can claim?", head_at=A("c05", "who"),
    steps=[{"label": "Four groups of relatives", "sub": "wife · children · parents", "icon": "users", "at": A("c05", "four")},
           {"label": "Against a person with sufficient means", "icon": "briefcase", "at": A("c05", "sufficient")},
           {"label": "Who neglects or refuses to maintain them", "icon": "ban", "tone": "ok", "at": A("c05", "neglects")}])
cue(type="cite", t0=A("c05", "against"), t1=E("c05") + 0.05, at=A("c05", "against"), tag="BNSS 144(1)",
    text="A Magistrate of the first class may order a monthly allowance, upon proof of the neglect or refusal", icon="book-open")
cue(type="compare", t0=S("c06"), t1=E("c06") + 0.05,
    cols=[{"title": "First: a wife", "icon": "user-round", "at": A("c06", "first")},
          {"title": "Second: a child", "icon": "users", "at": A("c06", "second")}],
    rows=[{"cells": ["Unable to maintain herself", "Legitimate or illegitimate, whether married or not, unable to maintain itself"],
           "cells_at": [A("c06", "unable"), A("c06", "legitimate")]}])
cue(type="cite", t0=S("c06") + 0.3, t1=E("c06") + 0.05, at=S("c06") + 0.3, tag="BNSS, 2023",
    text="Section 144(1), clauses (a) and (b)", icon="book-open")
cue(type="section", t0=S("c07"), t1=E("c07") + 0.05, at=A("c07", "third"), act="BNSS, 2023", num="144(1)(c)",
    title="Third: an adult child",
    points=[{"text": "Has attained majority, and is not a married daughter", "at": A("c07", "adult")},
            {"text": "Unable to maintain itself", "at": A("c07", "unable")},
            {"text": "By reason of a physical or mental abnormality or injury", "at": A("c07", "physical")}])
cue(type="splitcard", t0=S("c08"), t1=E("c08") + 0.05,
    left={"title": "FOURTH: A FATHER OR MOTHER", "text": "unable to maintain himself or herself", "icon": "users", "at": A("c08", "fourth")},
    right={"title": "FROM A SON OR A DAUGHTER", "text": "a married daughter too, with means of her own, apart from her husband's",
           "icon": "user-round", "at": A("c08", "daughter")})
cue(type="cite", t0=A("c08", "vijaya"), t1=E("c08") + 0.05, at=A("c08", "vijaya"), tag=f"{SC} · 1987 · {OLD}",
    cases=[{"name": "Dr. Vijaya Manohar Arbat v. Kashirao Rajaram Sawai"}])
# the word "minor" is gone from clause (b); its effect is an open question (stamp), never a settled right of adult children
cue(type="compare", t0=S("c09"), t1=A("c09", "whether") - 0.05, head="Clause (b): the word “minor”", head_at=S("c09") + 0.05,
    cols=[{"title": "Old Code", "icon": "book-open", "at": S("c09") + 0.3},
          {"title": "BNSS", "icon": "landmark", "at": A("c09", "clause")}],
    rows=[{"cells": ["Section 125(1)(b) CrPC: “legitimate or illegitimate minor child”",
                     "Section 144(1)(b) BNSS: “legitimate or illegitimate child”"],
           "cells_at": [A("c09", "old"), A("c09", "uses")]}])
cue(type="question", t0=A("c09", "whether") - 0.05, t1=E("c09") + 0.05, at=A("c09", "whether"),
    text="Does that help adult children?", hl="help adult children?", y=215)
cue(type="stamp", t0=A("c09", "settled") - 0.05, t1=E("c09") + 0.05, at=A("c09", "settled"), line1="NOT YET SETTLED",
    line2="BY THE COURTS", y=900)

# ── 3 · who counts as a wife ─────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="quote", t0=S("c10"), t1=E("c10") + 0.05, at=S("c10") + 0.1, reveal=r3(A("c10", "remarried") - S("c10") - 0.1),
    text="For the purposes of this Chapter, “wife” includes a woman who has been divorced by, or has obtained a divorce from, "
         "her husband and has not remarried.",
    hl=["divorced by, or has obtained a divorce from", "has not remarried"])
cue(type="cite", t0=S("c10") + 0.3, t1=E("c10") + 0.05, at=S("c10") + 0.3, tag="THE STATUTE'S WORDS",
    text="BNSS, 2023 · Section 144(1), Explanation", icon="book-open")
cue(type="list", t0=S("c11"), t1=E("c11") + 0.05, head="A secular remedy: it applies to", head_at=A("c11", "remedy"),
    items=[{"n": 1, "text": "All married women, including Muslim married women", "at": A("c11", "held")},
           {"n": 2, "text": "All non-Muslim divorced women", "at": A("c11", "covers")},
           {"n": 3, "text": "Muslim divorced women: s.125 and/or the 1986 Act", "at": A("c11", "faith")}])
cue(type="cite", t0=A("c11", "supreme"), t1=E("c11") + 0.05, at=A("c11", "supreme"), tag=f"{SC} · 2024 · {OLD}",
    cases=[{"name": "Mohd. Abdul Samad v. State of Telangana", "cite": "conclusions (a), (b), (c)(ii)"}])

# ── 4 · hypothetical: Deepa's claim ──────────────────────────────────────────────────────────────────────────────────────────────
cue(type="kicker", t0=S("c12"), t1=E("c13") + 0.05, at=S("c12") + 0.05, text=HYP)
cue(type="flow", t0=S("c12"), t1=E("c12") + 0.05, head="Deepa's claim", head_at=S("c12") + 0.1,
    steps=[{"label": "Deepa and her young son", "sub": "living with her parents", "icon": "users", "at": A("c12", "deepa")},
           {"label": "Raghu, her husband", "sub": "an engineer: the respondent", "icon": "user-round", "at": A("c12", "raghu")},
           {"label": "Has stopped paying for them", "icon": "indian-rupee", "at": A("c12", "stopped")}])
cue(type="verdicts", t0=S("c13"), t1=E("c13") + 0.05,
    rows=[{"text": "Her small income ends her claim", "ok": False, "at": A("c13", "earns"), "strike_at": A("c13", "end")},
          {"text": "The test: can she live as she did in her husband's home?", "ok": True, "at": A("c13", "can")}])
cue(type="cite", t0=A("c13", "chaturbhuj"), t1=E("c13") + 0.05, at=A("c13", "chaturbhuj"), tag=f"{SC} · 2007 · {OLD}",
    cases=[{"name": CHAT}])
cue(type="quote", t0=S("c14"), t1=E("c14") + 0.05, at=S("c14") + 0.1, reveal=r3(A("c14", "labour") - S("c14") - 0.1),
    text="The husband is required to earn money even by physical labour, if he is an able-bodied, and could not avoid his "
         "obligation, except on the legally permissible grounds mentioned in the statute.",
    hl=["even by physical labour", "able-bodied"])
cue(type="cite", t0=A("c14", "anju"), t1=E("c14") + 0.05, at=A("c14", "anju"), tag=f"{SC} · 2022 · {OLD}",
    cases=[{"name": "Anju Garg v. Deepak Kumar Garg", "cite": "para 10"}])

# ── 5 · how much, and interim relief ─────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c15"), t1=A("c15", "old") - 0.05, text="How much? No statutory ceiling", icon="indian-rupee",
    accent=True, at=A("c15", "how"))
cue(type="timeline", t0=A("c15", "old") - 0.05, t1=E("c15") + 0.05,
    nodes=[{"label": "OLD CODE · SECTION 125", "value": "₹500", "sub": "a month: the old ceiling", "at": A("c15", "five")},
           {"label": "AMENDED IN 2001", "value": "Removed", "sub": "no ceiling since", "at": A("c15", "removed")}])
cue(type="cite", t0=A("c15", "removed"), t1=E("c15") + 0.05, at=A("c15", "removed"), tag="AMENDMENT ACT 50 OF 2001",
    text="Omitted the words “not exceeding five hundred rupees in the whole”", icon="book-open")
cue(type="checklist", t0=S("c16"), t1=E("c16") + 0.05, head="The Magistrate weighs", head_at=S("c16") + 0.05,
    items=[{"n": 1, "text": "Status of the parties", "at": A("c16", "status")},
           {"n": 2, "text": "Reasonable needs", "at": A("c16", "reasonable")},
           {"n": 3, "text": "Independent income", "at": A("c16", "independent")},
           {"n": 4, "text": "The standard of living", "at": A("c16", "standard")}])
cue(type="cite", t0=A("c16", "monthly"), t1=E("c16") + 0.05, at=A("c16", "monthly"), tag="BNSS 144(1)",
    text="“at such monthly rate as such Magistrate thinks fit”", icon="book-open")
cue(type="compare", t0=S("c17"), t1=E("c17") + 0.05, head="The amount: a balance", head_at=S("c17") + 0.05,
    cols=[{"title": "Not oppressive", "icon": "user-round", "at": A("c17", "oppress")},
          {"title": "Not so meagre", "icon": "users", "at": A("c17", "meagre")}],
    rows=[{"cells": ["“so extravagant which becomes oppressive and unbearable for the respondent”",
                     "“so meagre that it drives the wife to penury”"],
           "cells_at": [A("c17", "payer"), A("c17", "penury")]}])
cue(type="cite", t0=A("c17", "rajnesh"), t1=E("c17") + 0.05, at=A("c17", "rajnesh"), tag=f"{SC} · 2020 · {OLD}",
    cases=[{"name": RAJ}])
# counters never shrink: no citation bar under it (a two-line bar overlapped the ring card); s.144(1) 2nd / 3rd provisos
cue(type="counters", t0=S("c18"), t1=E("c18") + 0.05, head="Pending the case: interim maintenance and expenses",
    head_at=S("c18") + 0.05,
    items=[{"value": 60, "unit": "DAYS", "label": "To dispose of the interim application", "sub": "as far as possible, from service of notice",
            "at": A("c18", "sixty")}])

# ── 6 · from when, and full disclosure ───────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c19"), t1=E("c19") + 0.05, at=A("c19", "sub"), act="BNSS, 2023", num="144(2)",
    title="From when the allowance runs",
    points=[{"text": "From the date of the order", "at": A("c19", "date")},
            {"text": "Or, if so ordered, from the date of the application", "at": A("c19", "date", 2)}])
cue(type="flow", t0=S("c20"), t1=E("c20") + 0.05, head="Awarded from the date of application", head_at=S("c20") + 0.05,
    steps=[{"label": "The application is filed", "sub": "maintenance runs from this date", "icon": "file-text", "at": A("c20", "application")},
           {"label": "The case stays pending", "sub": "“not within the control of the applicant”", "icon": "clock", "tone": "ok",
            "at": A("c20", "delays")}])
cue(type="cite", t0=A("c20", "rajnesh"), t1=E("c20") + 0.05, at=A("c20", "rajnesh"), tag=f"{SC} · 2020 · {OLD}",
    cases=[{"name": RAJ, "cite": "para 113"}])
cue(type="flow", t0=S("c21"), t1=E("c21") + 0.05, head="A disclosure affidavit", head_at=S("c21") + 0.05,
    steps=[{"label": "Assets and liabilities", "sub": "disclosed on affidavit", "icon": "file-pen-line", "at": A("c21", "assets")},
           {"label": "Mandatory for both sides", "sub": "applicant and respondent", "icon": "users", "at": A("c21", "mandatory")},
           {"label": "False statements", "sub": "may invite perjury proceedings", "icon": "triangle-alert", "at": A("c21", "false")}])
cue(type="cite", t0=S("c21") + 0.3, t1=E("c21") + 0.05, at=S("c21") + 0.3, tag=f"{SC} · 2020 · {OLD}",
    cases=[{"name": RAJ, "cite": "para 72"}])
cue(type="flow", t0=S("c22"), t1=E("c22") + 0.05, head="Claims under more than one law", head_at=S("c22") + 0.05,
    steps=[{"label": "A claim under another law", "sub": "e.g. the Domestic Violence Act", "icon": "book-open", "at": A("c22", "another")},
           {"label": "Disclose that order", "sub": "and the earlier proceeding", "icon": "file-text", "at": A("c22", "disclose")},
           {"label": "The court considers an adjustment", "sub": "a set-off of the amounts", "icon": "scale", "tone": "ok",
            "at": A("c22", "adjusting")}])
cue(type="cite", t0=S("c22") + 0.3, t1=E("c22") + 0.05, at=S("c22") + 0.3, tag=f"{SC} · 2020 · {OLD}",
    cases=[{"name": RAJ}])

# ── 7 · when a wife cannot claim ─────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c23"), t1=E("c23") + 0.05, at=A("c23", "sub"), act="BNSS, 2023", num="144(4)",
    title="When a wife is not entitled",
    points=[{"text": "She is living in adultery", "tone": "no", "at": A("c23", "adultery")},
            {"text": "She refuses, without sufficient reason, to live with her husband", "tone": "no", "at": A("c23", "refuses")},
            {"text": "They live separately by mutual consent", "tone": "no", "at": A("c23", "mutual")}],
    note={"text": "A wife's claim only: not a child's or a parent's", "icon": "info", "at": A("c23", "consent")})
cue(type="equation", t0=S("c24"), t1=E("c24") + 0.05,
    terms=[{"text": "PROOF OF ANY OF THESE", "at": A("c24", "proof")},
           {"op": "=", "text": "THE MAGISTRATE SHALL CANCEL THE ORDER", "result": True, "at": A("c24", "cancel")}])
cue(type="cite", t0=S("c24") + 0.3, t1=E("c24") + 0.05, at=S("c24") + 0.3, tag="BNSS 144(5)",
    text="An order in favour of a wife: “the Magistrate shall cancel the order”", icon="book-open")
cue(type="kicker", t0=S("c25"), t1=E("c25") + 0.05, at=S("c25") + 0.05, text=HYP_DR)
cue(type="flow", t0=S("c25"), t1=E("c25") + 0.05, head="Raghu's offer", head_at=S("c25") + 0.1,
    steps=[{"label": "Maintenance, on a condition", "sub": "only if Deepa returns", "icon": "handshake", "at": A("c25", "offers")},
           {"label": "Her reasons for refusing", "sub": "the Magistrate may weigh them", "icon": "scale", "at": A("c25", "weigh")},
           {"label": "May still order it", "sub": "on just ground", "icon": "gavel", "tone": "ok", "at": A("c25", "order")}])
cue(type="cite", t0=A("c25", "magistrate"), t1=E("c25") + 0.05, at=A("c25", "magistrate"), tag="BNSS 144(3) · SECOND PROVISO",
    text="“if he is satisfied that there is just ground for so doing”", icon="book-open")
cue(type="quote", t0=S("c26"), t1=E("c26") + 0.05, at=S("c26") + 0.1, reveal=r3(A("c26", "refusal") - S("c26") - 0.1),
    text="If a husband has contracted marriage with another woman or keeps a mistress, it shall be considered to be just ground "
         "for his wife's refusal to live with him.",
    hl=["marriage with another woman", "just ground for his wife's refusal"])
cue(type="cite", t0=S("c26") + 0.3, t1=E("c26") + 0.05, at=S("c26") + 0.3, tag="THE STATUTE'S WORDS",
    text="BNSS, 2023 · Section 144(3), Explanation", icon="book-open")

# ── 8 · enforcing the order ──────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="kicker", t0=S("c27"), t1=E("c29") + 0.05, at=S("c27") + 0.05, text=HYP_DR)
cue(type="flow", t0=S("c27"), t1=E("c27") + 0.05, head="If the order is not obeyed", head_at=S("c27") + 0.1,
    steps=[{"label": "Raghu, the respondent, does not pay", "sub": "without sufficient cause", "icon": "ban", "at": A("c27", "fails")},
           {"label": "A warrant for every breach", "sub": "issued by the Magistrate", "icon": "file-text", "at": A("c27", "warrant")},
           {"label": "The amount due is levied", "sub": "as fines are levied", "icon": "indian-rupee", "tone": "ok", "at": A("c27", "levy")}])
cue(type="cite", t0=S("c27") + 0.3, t1=E("c27") + 0.05, at=S("c27") + 0.3, tag="BNSS 147",
    text="Enforceable “by any Magistrate in any place where the person against whom it is made may be”", icon="book-open")
cue(type="timeline", t0=S("c28"), t1=E("c28") + 0.05,
    nodes=[{"label": "EACH MONTH'S ALLOWANCE", "value": "Unpaid", "sub": "after the warrant", "at": A("c28", "each")},
           {"label": "IMPRISONMENT", "value": "Up to 1 month", "sub": "for each such month", "at": A("c28", "imprisoned")},
           {"label": "OR, IF SOONER", "value": "Until he pays", "at": A("c28", "pays")}])
cue(type="counters", t0=S("c29"), t1=E("c29") + 0.05, head="A time limit", head_at=S("c29") + 0.05,
    items=[{"value": 1, "unit": "YEAR", "label": "To apply to levy the amount", "sub": "from the date it became due", "at": A("c29", "one")}])
cue(type="cite", t0=A("c29", "apply"), t1=E("c29") + 0.05, at=A("c29", "apply"), tag="BNSS 144(3) · FIRST PROVISO",
    text="No warrant unless the application is made within one year from the date the amount became due", icon="book-open")
cue(type="strike", t0=S("c30"), t1=A("c30", "kuldip") - 0.05, text="Jail wipes out the arrears", icon="lock",
    at=S("c30") + 0.05, strike_at=A("c30", "wipe"))
cue(type="quote", t0=A("c30", "kuldip") - 0.05, t1=E("c30") + 0.05, at=A("c30", "kuldip"),
    reveal=r3(A("c30", "satisfaction") - A("c30", "kuldip")),
    text="Sentencing a person to jail is a ‘mode of enforcement’. It is not a ‘mode of satisfaction’ of the liability. "
         "The liability can be satisfied only by making actual payment of the arrears.",
    hl=["mode of enforcement", "mode of satisfaction", "actual payment of the arrears"])
cue(type="cite", t0=A("c30", "kuldip"), t1=E("c30") + 0.05, at=A("c30", "kuldip"), tag=f"{SC} · 1988 · {OLD}",
    cases=[{"name": "Kuldip Kaur v. Surinder Singh"}])

# ── 9 · where to file, and later changes ─────────────────────────────────────────────────────────────────────────────────────────
cue(type="kicker", t0=S("c31"), t1=E("c31") + 0.05, at=S("c31") + 0.05, text=HYP_DR)
cue(type="section", t0=S("c31"), t1=E("c31") + 0.05, at=A("c31", "section"), act="BNSS, 2023", num="145(1)",
    title="In any district",
    points=[{"text": "(a) Where he is", "at": A("c31", "raghu")},
            {"text": "(b) Where he or his wife resides", "at": A("c31", "resides")},
            {"text": "(c) Where he last resided with his wife, or with the mother of the illegitimate child", "at": A("c31", "last")}])
cue(type="compare", t0=S("c32"), t1=E("c32") + 0.05, head="A new option", head_at=S("c32") + 0.05,
    cols=[{"title": "Old Code", "icon": "book-open", "at": S("c32") + 0.3},
          {"title": "BNSS", "icon": "landmark", "at": A("c32", "adds")}],
    rows=[{"cells": ["Section 126(1) CrPC: clauses (a) to (c) only", "Section 145(1)(d): where his father or mother resides"],
           "cells_at": [S("c32") + 0.5, A("c32", "father")]}])
cue(type="splitcard", t0=S("c33"), t1=E("c33") + 0.05,
    left={"title": "A FAMILY COURT", "text": "set up for the area", "icon": "landmark", "at": A("c33", "family")},
    right={"title": "IT EXERCISES", "text": "this maintenance jurisdiction", "icon": "gavel", "at": A("c33", "exercises")})
cue(type="cite", t0=A("c33", "family"), t1=E("c33") + 0.05, at=A("c33", "family"), tag="FAMILY COURTS ACT, 1984",
    text="Family Courts Act s.7(2)(a): the jurisdiction of a Magistrate of the first class over maintenance", icon="book-open")
cue(type="section", t0=S("c34"), t1=E("c34") + 0.05, at=A("c34", "section"), act="BNSS, 2023", num="146(1)",
    title="Alteration in allowance",
    points=[{"text": "On proof of a change in the circumstances", "at": A("c34", "proof")},
            {"text": "The Magistrate may alter the allowance: up or down", "at": A("c34", "alter")}])
cue(type="cite", t0=A("c34", "alter"), t1=E("c34") + 0.05, at=A("c34", "alter"), tag="BNSS 146 · REMARRIAGE",
    text="Section 146(3)(a): an order for a divorced woman is cancelled “as from the date of her remarriage”", icon="book-open")

# ── 10 · your checklist ──────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="checklist", t0=S("c35"), t1=E("c35") + 0.05, head="Gather proof of", head_at=S("c35") + 0.05,
    items=[{"n": 1, "text": "The relationship", "at": A("c35", "relationship")},
           {"n": 2, "text": "The respondent's income and assets", "at": A("c35", "income")},
           {"n": 3, "text": "Your own monthly expenses", "at": A("c35", "monthly")}])
cue(type="cite", t0=S("c35") + 0.3, t1=E("c35") + 0.05, at=S("c35") + 0.3, tag="PRACTICE NOTE",
    text="Filing practice drawn from Rajnesh v. Neha, para 72: not a statutory rule", icon="info")
cue(type="flow", t0=S("c36"), t1=E("c36") + 0.05, head="File, and follow up", head_at=S("c36") + 0.05,
    steps=[{"label": "The disclosure affidavit", "sub": "filed with your application", "icon": "file-pen-line", "at": A("c36", "disclosure")},
           {"label": "Seek interim maintenance", "sub": "early", "icon": "clock", "at": A("c36", "interim")},
           {"label": "Payments stop?", "sub": "apply within one year of each missed payment", "icon": "calendar", "tone": "ok",
            "at": A("c36", "stop")}])
cue(type="cite", t0=S("c36") + 0.3, t1=E("c36") + 0.05, at=S("c36") + 0.3, tag=f"{SC} · 2020 · {OLD}",
    cases=[{"name": RAJ, "cite": "para 72"}])
# "maintenance is not a penalty" (Chaturbhuj para 6: "not to punish a person for his past neglect"), then the evidence line
cue(type="splitcard", t0=S("c37"), t1=A("c37", "the") - 0.05,
    left={"title": "MAINTENANCE", "text": "prevents destitution", "icon": "shield-check", "at": A("c37", "maintenance")},
    right={"title": "NOT A PENALTY", "text": "not to punish past neglect", "icon": "scale", "at": A("c37", "not")})
cue(type="point", t0=A("c37", "the") - 0.05, t1=E("c37") + 0.05, text="The amount always depends on the evidence before the court",
    icon="search-check", accent=True, at=A("c37", "the"))
cue(type="cite", t0=A("c37", "not"), t1=E("c37") + 0.05, at=A("c37", "not"), tag=f"{SC} · 2007 · {OLD}",
    cases=[{"name": CHAT, "cite": "para 6"}])
cue(type="point", t0=S("c38"), t1=E("c38") + 0.05, text="Like · Share · Subscribe · lawworld.ai",
    icon="check", accent=True, at=A("c38", "thanks"))
