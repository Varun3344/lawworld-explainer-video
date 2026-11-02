# Tamil Nadu Medical Services Corporation Ltd. v. U.P. State Micro and Small Enterprises Facilitation Council & Anr. (R2 Atul
# Generators Pvt Ltd, Agra), W.A. No. 2187 of 2025, 2026:MHC:4346, High Court of Judicature at Madras (Sushrut Arvind Dharmadhikari CJ
# wrote it, G. Arul Murugan J.; reserved 26.10.2026, delivered 29.10.2026, "Index : Yes"): panel cues, run by split/build_course_plan.py
# (helpers: at S E cue fx have r3 PEND). HOOK format (split/JUDGMENT_HOOK_FORMAT.md): c01 hook question, c02 curiosity, c03 "Hi, I'm
# Ravishankar" + bench, c04-c07 facts / case / both sides, c08 the LawWorld request, c09-c10 the verdict.
# Facts from the judgment (paras): Letters Patent appeal against the Single Judge's order of 18.10.2024 in W.P. No. 10688 of 2024,
# which dismissed the Corporation's writ against the Council's Section 18 MSMED Act award of 28.11.2016 (prayer, 1); purchase order
# 20.05.2009 for supply and installation of 130 Diesel Generator sets across Primary Health Centres in Tamil Nadu, repeat order for 4
# more on 22.10.2009 (2.1); Rs.19,71,049/- deducted as liquidated damages, "citing delayed delivery schedules" (2.2); Claim Petition
# No. 26 of 2012 under Section 18; conciliation failed; the Council as arbitral tribunal; award 28.11.2016: refund of the withheld
# principal with statutory compound interest under Section 16 (2.3); Section 34 read with Section 19 MSMED Act, Commercial Court, Kanpur
# Nagar, Arb. Misc. Case No. 274 of 2023, dismissed 30.10.2023 (2.4); then the Article 226 writ to quash the award, dismissed
# 18.10.2024 (2.5); interim stay of further proceedings on the award 16.07.2025, extended 24.09.2025 (2.6); the Corporation:
# jurisdictional flaws, procedural infirmities, a writ lies (3.1); Section 34 dismissed only on delay; Tamil Nadu Cements Larger Bench
# reference (SLP (C) Diary No. 3776 of 2023, 22.01.2025); keep the award in abeyance (3.2); the supplier: a Section 18(3) award has the
# status of a 1996 Act award; after Section 34 the remedy is a Section 37 appeal (4.1); having invoked Section 34 and lost, it cannot
# plead the order is not an award; approbate and reprobate; merger; no cause of action in Madras (4.2); Tamil Nadu Cements
# distinguishable (4.3); issues (5); Section 18(3)/(4): "the identical legal status, efficacy and binding force as an arbitral award
# passed under the 1996 Act" (6); Section 34 consciously filed at the competent Commercial Court, Kanpur Nagar; a Section 29A ground
# too; "A party cannot call the order an award for one purpose and a nullity for another."; recourse "exhaustively confined to filing
# an appeal under Section 37" (7); a writ would subvert the speedy-resolution intent of both Acts (8); the Single Judge's view affirmed;
# no Article 226 "as a substitute for a statutory appeal under Section 37"; appeal dismissed, order of 18.10.2024 confirmed, no costs,
# C.M.P.s closed, "the interim order granted is vacated" (9).
# Not on any card as a finding: territorial jurisdiction (the supplier's plea, never decided); the Tamil Nadu Cements reference (only
# as the Corporation's argument); whether Section 34 failed on merits or on delay ("dismissed" only); the merits of the deduction.
# No section sign anywhere. List lines <= 52 chars. Official hcmadras.tn.gov.in portraits on the bench card (CJ: img_id 641 as ikc;
# G. Arul Murugan J.: present judges page, img_id 619).
FORMAT = "hook"   # build_course_plan.py: no opening sting, 15-frame lead (the cover), name tag on the "Ravishankar" clip

def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
ENDCARD = {"title": "Lost under Section 34: can you file a writ?", "line": "No: a Council award is an arbitral award · the remedy is a Section 37 appeal", "sub": "LawWorld: legal research for advocates"}

# ── 1 · award or nullity? (hook, curiosity, intro) ──────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "lost"), text="Lost your Section 34 challenge to an MSME Council's award? Can you skip the appeal and file a writ instead?", hl="file a writ instead?")
cue(type="list", t0=S("c02"), t1=A("c02", "will") - 0.05, head="₹19,71,049 held back · three rounds", head_at=S("c02") + 0.05,
    items=[{"n": 1, "text": "UP MSME Council: the award goes against it", "at": A("c02", "council")},
           {"n": 2, "text": "Section 34 challenge at Kanpur: dismissed", "at": A("c02", "kanpur")},
           {"n": 3, "text": "Then a writ petition in Madras", "at": A("c02", "writ")}])
cue(type="point", t0=A("c02", "will") - 0.05, t1=E("c02") + 0.05, text="Will that work?", icon="search", accent=True, at=A("c02", "work"))
cue(type="bench", t0=S("c03"), t1=E("c03") + 0.05, tag="Madras High Court · 29 October 2026",
    judges=[{"name": "Chief Justice Sushrut Arvind Dharmadhikari", "photo": "../brand/judges/sushrut_arvind_dharmadhikari.jpg", "at": A("c03", "honourable")},
            {"name": "Justice G. Arul Murugan", "photo": "../brand/judges/g_arul_murugan.jpg", "at": A("c03", "honourable", 2)}])

# ── 2 · the generator sets ──────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c04"), t1=E("c04") + 0.05, head="Purchase order · 20 May 2009", head_at=S("c04") + 0.05,
    steps=[{"label": "The State corporation", "sub": "Tamil Nadu Medical Services, Chennai", "icon": "landmark", "at": A("c04", "tamil")},
           {"label": "130 diesel generator sets", "sub": "from Atul Generators, Agra", "icon": "file-text", "at": A("c04", "diesel")},
           {"label": "For Primary Health Centres", "sub": "+ 4 more in October 2009", "icon": "check", "at": A("c04", "primary")}])
cue(type="cite", t0=S("c05"), t1=E("c06") + 0.05, at=A("c05", "deducted"), tag="HIGH COURT OF MADRAS · 29.10.2026",
    cases=[{"name": "Tamil Nadu Medical Services Corporation Ltd. v. U.P. State Micro and Small Enterprises Facilitation Council & Anr.", "cite": "2026:MHC:4346 · W.A. No. 2187 of 2025"}])
cue(type="timeline", t0=S("c05"), t1=E("c05") + 0.05,
    nodes=[{"label": "THE CORPORATION", "value": "₹19,71,049 deducted", "sub": "liquidated damages · citing delay", "at": A("c05", "deducted")},
           {"label": "UP MSME COUNCIL · SECTION 18", "value": "award: refund", "sub": "28 Nov 2016 · + Section 16 interest", "at": A("c05", "award")}])

# ── 3 · lost, then a writ ───────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="timeline", t0=S("c06"), t1=E("c06") + 0.05,
    nodes=[{"label": "COMMERCIAL COURT, KANPUR NAGAR", "value": "Section 34: dismissed", "sub": "30 October 2023", "at": A("c06", "dismissed")},
           {"label": "MADRAS HIGH COURT", "value": "writ dismissed", "sub": "Single Judge · 18 October 2024", "at": A("c06", "single")}])
cue(type="compare", t0=S("c07"), t1=E("c07") + 0.05, head="Before the appeal bench", head_at=S("c07") + 0.05,
    cols=[{"title": "The Corporation", "icon": "landmark", "at": A("c07", "corporation")}, {"title": "The supplier", "icon": "file-text", "at": A("c07", "supplier")}],
    rows=[{"cells": ["Jurisdictional flaws: a writ lies", "After Section 34: a Section 37 appeal"], "cells_at": [A("c07", "writ"), A("c07", "having")]},
          {"cells": ["SC Larger Bench reference: keep award in abeyance", "Cannot approbate and reprobate"], "cells_at": [A("c07", "lost"), A("c07", "disown")]}])

# ── 4 · before the verdict: the LawWorld request ────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c08"), t1=A("c08", "follow") - 0.05, text="The verdict is next. First, a quick request…", icon="scale", accent=True, at=A("c08", "decided"))
cue(type="list", t0=A("c08", "follow") - 0.05, t1=E("c08") + 0.05, head="Follow LawWorld · lawworld.ai", head_at=A("c08", "follow"),
    items=[{"n": 1, "text": "Search SC and High Court judgments, cited to source", "at": A("c08", "india's")},
           {"n": 2, "text": "Draft petitions, plaints and notices with AI", "at": A("c08", "platform")},
           {"n": 3, "text": "Sign up free · ₹200 AI credit included", "at": A("c08", "advocates")}])

# ── 5 · what the Court held ─────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "council") - 0.05, text="What did the High Court decide?", icon="scale", accent=True, at=A("c09", "finally"))
cue(type="list", t0=A("c09", "council") - 0.05, t1=E("c09") + 0.05, head="Section 18, MSMED Act · the 1996 Act", head_at=A("c09", "council"),
    items=[{"n": 1, "text": "Council award: same force as an arbitral award", "at": A("c09", "same")},
           {"n": 2, "text": "No writ under Article 226 as a substitute", "at": A("c09", "writ")},
           {"n": 3, "text": "After Section 34: only a Section 37 appeal", "at": A("c09", "appeal")}])
cue(type="point", t0=S("c10"), t1=A("c10", "writ") - 0.05, text="“A party cannot call the order an award for one purpose and a nullity for another.”", icon="scale", accent=True, at=A("c10", "party"))
cue(type="verdicts", t0=A("c10", "writ") - 0.05, t1=E("c10") + 0.05,
    rows=[{"text": "The Corporation's writ appeal", "ok": False, "at": A("c10", "dismissed")},
          {"text": "Single Judge's order of 18.10.2024: confirmed", "ok": True, "at": A("c10", "dismissed", 1, 0.45)},
          {"text": "The interim stay on the award", "ok": False, "at": A("c10", "vacated")}])

MUSIC = {"file": "audio/bed_mixkit738_140s.mp3", "target_lufs": -21}   # owner 02-11-2026: trending-style royalty-free bed, audible under the voice
