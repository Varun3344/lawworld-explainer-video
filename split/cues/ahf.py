# Aadhar Housing Finance Ltd. v. Manpreet Singh & Ors., WPC No. 4952 of 2021, 2026:CGHC:45681, High Court of Chhattisgarh at Bilaspur
# (Amitendra Kishore Prasad J., delivered 29.10.2026, AFR): panel cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3
# PEND). HOOK format (owner 02-11-2026): c01 hook question, c02 curiosity, c03 "Hi, I'm Ravishankar" + bench, c04-c07 facts / case /
# discussion, c08 the LawWorld request before the verdict, c09-c10 the verdict. No title sting.
# Facts from the judgment (paras; the judgment numbers 12, 13 and 15 twice: 12a/12b ...): DM Rajnandgaon's order 06.09.2021 rejecting
# the s.14 SARFAESI application (1); loan Rs.7,96,388, house mortgaged, agreement 24.05.2017; NPA 10.08.2019; s.13(2) notice for
# Rs.8,29,436 unpaid; s.14 application before the DM; rejected because "the secured asset has been sold to respondent no. 03
# (Subsequent Purchaser), vide registered sale deed dated 13.12.2019" (2); the lender: s.14 "purely ministerial", R.D. Jain (3); a
# transfer to a third party does not oust the secured creditor's right (4); respondent 3 and the State support the order (5, 6); the
# question (8); adjudicatory issues are for the DRT (9); a later transfer gives the DM no jurisdiction to adjudicate it (11); the DM's
# role "is ministerial in nature" (12a); Balkrishna Rama Tarle: no adjudication between the borrower / any third party and the secured
# creditor, objections under s.17 before the DRT (13a); Only Wheel (Cal): administrative functions (12b); the DM "travelled beyond the
# scope of the jurisdiction", order "erroneous and unsustainable" (13b); writ allowed, order set aside (14); remand, decide "within a
# period of 30 days from the date of receipt of a copy of this order" after hearing the parties (15a).
# Not on any card: who sold the house (the judgment does not say); any finding on the sale's validity (left to the DRT).
# No section sign anywhere. List lines <= 52 chars. Official portrait from highcourt.cg.gov.in on the bench card.
FORMAT = "hook"   # build_course_plan.py: no opening sting, 15-frame lead (the cover), name tag on the "Ravishankar" clip

def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
ENDCARD = {"title": "Can a sale stop SARFAESI?", "line": "Section 14 is ministerial: a buyer's objections go to the DRT", "sub": "LawWorld: legal research for advocates"}

# ── 1 · can a sale stop SARFAESI? (hook, curiosity, intro) ───────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "loan"), text="The loan turns bad and the mortgaged house is sold. Can the District Magistrate refuse possession over that sale?", hl="over that sale?")
cue(type="point", t0=S("c02"), t1=A("c02", "but") - 0.05, text="District Magistrate, Rajnandgaon: Section 14 application rejected · the secured asset “has been sold”", icon="x", at=A("c02", "turned"))
cue(type="point", t0=A("c02", "but") - 0.05, t1=E("c02") + 0.05, text="Can a Section 14 magistrate decide a buyer's rights at all?", icon="search", accent=True, at=A("c02", "magistrate", 2))
cue(type="bench", t0=S("c03"), t1=E("c03") + 0.05, tag="Chhattisgarh High Court · 29 October 2026",
    judges=[{"name": "Justice Amitendra Kishore Prasad", "photo": "../brand/judges/amitendra_kishore_prasad.jpg", "at": A("c03", "honourable")}])

# ── 2 · the loan and the sale ────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=S("c04"), t1=E("c05") + 0.05, at=A("c04", "borrowers"), tag="HIGH COURT OF CHHATTISGARH · 29.10.2026",
    cases=[{"name": "Aadhar Housing Finance Ltd. v. Manpreet Singh & Ors.", "cite": "2026:CGHC:45681 · WPC No. 4952 of 2021"}])
cue(type="timeline", t0=S("c04"), t1=E("c05") + 0.05,
    nodes=[{"label": "THE LOAN", "value": "₹7,96,388", "sub": "house mortgaged · 24.05.2017", "at": A("c04", "mortgaged")},
           {"label": "LOAN ACCOUNT", "value": "NPA", "sub": "declared 10.08.2019", "tone": "red", "at": A("c04", "declared")},
           {"label": "SECTION 14", "value": "application", "sub": "the 13(2) demand notice unpaid", "at": A("c05", "moved")},
           {"label": "THE DM'S REASON", "value": "sold", "sub": "deed of 13.12.2019 · order of 06.09.2021", "at": A("c05", "sold")}])

# ── 3 · the magistrate says no ───────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c06"), t1=E("c06") + 0.05, head="District Magistrate, Rajnandgaon", head_at=S("c06") + 0.05,
    steps=[{"label": "Order of 6 Sep 2021", "sub": "the Section 14 application rejected", "icon": "landmark", "at": A("c06", "rejected")},
           {"label": "The ground: the sale", "sub": "sold to a subsequent purchaser", "icon": "x", "tone": "stop", "at": A("c06", "sale")},
           {"label": "The lender's writ", "sub": "WPC No. 4952 of 2021 · High Court", "icon": "scale", "at": A("c06", "writ")}])
cue(type="compare", t0=S("c07"), t1=E("c07") + 0.05, head="The arguments", head_at=S("c07") + 0.05,
    cols=[{"title": "The lender", "icon": "landmark", "at": A("c07", "lender")}, {"title": "The buyer and the State", "icon": "user", "at": A("c07", "buyer")}],
    rows=[{"cells": ["Section 14 is purely ministerial", "The house was sold: no possession"], "cells_at": [A("c07", "ministerial"), A("c07", "state")]},
          {"cells": ["A sale cannot oust its security", "The Magistrate's order is right"], "cells_at": [A("c07", "defeat"), A("c07", "backed")]}])

# ── 4 · before the verdict: the LawWorld request ────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c08"), t1=A("c08", "follow") - 0.05, text="The verdict is next. First, a quick request…", icon="scale", accent=True, at=A("c08", "decided"))
cue(type="list", t0=A("c08", "follow") - 0.05, t1=E("c08") + 0.05, head="Follow LawWorld · lawworld.ai", head_at=A("c08", "follow"),
    items=[{"n": 1, "text": "Search SC and High Court judgments, cited to source", "at": A("c08", "india's")},
           {"n": 2, "text": "Draft petitions, plaints and notices with AI", "at": A("c08", "platform")},
           {"n": 3, "text": "Sign up free · ₹200 AI credit included", "at": A("c08", "advocates")}])

# ── 5 · what the Court held ──────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "magistrate's") - 0.05, text="What did the High Court decide?", icon="scale", accent=True, at=A("c09", "finally"))
cue(type="list", t0=A("c09", "magistrate's") - 0.05, t1=E("c09") + 0.05, head="Section 14 of the SARFAESI Act", head_at=A("c09", "magistrate's"),
    items=[{"n": 1, "text": "The Magistrate's role is only ministerial", "at": A("c09", "ministerial")},
           {"n": 2, "text": "He cannot adjudicate the parties' rights", "at": A("c09", "cannot")},
           {"n": 3, "text": "A later sale gives him no such power", "at": A("c09", "buyer")}])
cue(type="point", t0=S("c10"), t1=A("c10", "order") - 0.05, text="A buyer's or borrower's objections: under Section 17, before the Debts Recovery Tribunal", icon="scale", accent=True, at=A("c10", "objections"))
cue(type="verdicts", t0=A("c10", "order") - 0.05, t1=E("c10") + 0.05,
    rows=[{"text": "The DM's order of 6 September 2021", "ok": False, "at": A("c10", "order"), "strike_at": A("c10", "aside")},
          {"text": "Writ allowed · back to the Magistrate", "ok": True, "at": A("c10", "magistrate")},
          {"text": "Fresh decision within 30 days, after hearing", "ok": True, "at": A("c10", "thirty")}])

MUSIC = {"file": "audio/bed_mixkit738_140s.mp3", "target_lufs": -21}   # owner 02-11-2026: trending-style royalty-free bed, audible under the voice
