# The Assessing Officer, Textiles Committee v. M/s. Premium Suiting Pvt. Ltd. & Anr., 2026 INSC 1158 (S.V.N. Bhatti J., N.V. Anjaria J.
# - Anjaria J. wrote it; decided 26.10.2026, REPORTABLE): panel cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3
# PEND). Concept format as set ara.
# Facts from the judgment (paras): Civil Appeal No. 785 of 2016 (cover); against the Allahabad High Court's order of 06.03.2013 in Writ
# Tax No. 354 of 2006, which quashed the cess demand (1, 2); s.5A, Textiles Committee Act, 1963 (inserted by Act 51 of 1973, w.e.f.
# 01.01.1975): a cess, a duty of excise, on all textiles and textile machinery manufactured in India, not exceeding 1% ad valorem;
# proviso: none on textiles manufactured from out of handloom or powerloom industry (5, 6.4); 'manufacture' not defined (5.1); the
# company bleaches, dyes and processes 100% man-made fabrics supplied by powerloom and handloom units, on job work, and returns them (3,
# 3.2, 6.3); show cause notice 20.08.2001, Rs 2,68,293 textile cess; assessment order 21.11.2001 (3.2, 3.3); Cess Appellate Tribunal,
# T.C.A. No. 223 of 2002, relying on Chandok Textile Exporters: processing amounted to manufacture, appeal dismissed (2, 3.4); High
# Court: bleaching and dyeing does not obliterate the status of the textile as a powerloom product; job workers "an extended hand" of the
# manufacturers (3.5-3.5.2); the Committee: borrow s.2(f), Central Excise Act, 1944 - any process incidental or ancillary to the
# completion of a manufactured product (5.4, 6); held: unless read in by reference or incorporation, another statute's definition cannot
# be applied (5.5, 5.6); "cannot be bodily lifted" (5.6); Union of India v. R.C. Jain (1981) 2 SCC 308 (5.5); Jagatram Ahuja v. CGT,
# Hyderabad (2000) 8 SCC 249 (5.7); Maheshwari Fish Seed Farm v. T.N. Electricity Board (2004) 4 SCC 705 (5.8); every statute has its
# own context (5.6); 'manufactured' in s.5A in its common parlance, "not in any special sense by borrowing" (6.1); no manufacturing by
# the company, "an extended arm" of the powerloom manufacturers (6.3, 6.5, 6.6); "At the best, it is the textile upgraded"; not liable
# to textile cess (6.7); appeal dismissed (7). The bench card uses the official portraits.
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow (24 + 58 px) ends inside the panel: the 9:16 band edge cut it into a line at 40
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen (no blobs / star behind the cards)
STING = {"kicker": "SUPREME COURT · JUDGMENT EXPLAINED", "title": "Textile cess and a borrowed definition", "sub": "Textiles Committee v. Premium Suiting · 2026 INSC 1158"}
ENDCARD = {"title": "Textile cess and a borrowed definition", "line": "Another Act's definition applies only by reference or incorporation", "sub": "LawWorld: legal research for advocates"}

# ── 1 · a borrowed definition? ───────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "cess"), text="“Manufacture” undefined in a cess law: can the revenue borrow the Central Excise Act's definition?", hl="borrow")
cue(type="bench", t0=S("c02"), t1=E("c02") + 0.05, tag="Supreme Court of India · 26 October 2026",
    judges=[{"name": "Justice S.V.N. Bhatti", "photo": "../brand/judges/svn_bhatti.jpg", "at": A("c02", "honourable")},
            {"name": "Justice N.V. Anjaria", "photo": "../brand/judges/nv_anjaria.jpg", "at": A("c02", "honourable", 2)}])

# ── 2 · the cess ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=A("c03", "textiles"), t1=E("c04") + 0.05, at=A("c03", "textiles"), tag="SUPREME COURT OF INDIA · 26.10.2026",
    cases=[{"name": "Assessing Officer, Textiles Committee v. Premium Suiting Pvt. Ltd.", "cite": "2026 INSC 1158 · Civil Appeal No. 785 of 2016"}])
cue(type="section", t0=S("c03"), t1=E("c03") + 0.05, at=A("c03", "section"), act="TEXTILES COMMITTEE ACT, 1963", num="5A", title="Cess on textiles manufactured in India",
    points=[{"text": "A duty of excise, up to 1% ad valorem", "at": A("c03", "cess")},
            {"text": "on textiles “manufactured in India”", "at": A("c03", "manufactured")},
            {"text": "Proviso: none on handloom or powerloom textiles", "tone": "no", "at": A("c03", "powerloom")}],
    note={"text": "“Manufacture” is not defined in the Act", "icon": "info", "at": A("c03", "handloom")})
cue(type="flow", t0=S("c04"), t1=E("c04") + 0.05, head="The demand", head_at=S("c04") + 0.05,
    steps=[{"label": "Premium Suiting Pvt. Ltd.", "sub": "bleaches, dyes and processes 100% man-made fabrics", "icon": "user", "at": A("c04", "premium")},
           {"label": "Job work", "sub": "for powerloom and handloom units · the fabric goes back", "icon": "arrow-right", "at": A("c04", "job")},
           {"label": "Show cause notice · 20 Aug 2001", "sub": "textile cess ₹2,68,293 · assessed 21 Nov 2001", "icon": "file-text", "tone": "stop", "at": A("c04", "demanded")}])

# ── 3 · tribunal and high court ──────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c05"), t1=E("c05") + 0.05, head="Before the appeal", head_at=S("c05") + 0.05,
    steps=[{"label": "Cess Appellate Tribunal: demand upheld", "sub": "processing is manufacture (Chandok Textile Exporters)", "icon": "x", "tone": "stop", "at": A("c05", "tribunal")},
           {"label": "Allahabad High Court · 6 Mar 2013", "sub": "demand quashed · Writ Tax No. 354 of 2006", "icon": "check", "tone": "ok", "at": A("c05", "quashed")},
           {"label": "Still a powerloom product", "sub": "job workers: “an extended hand” of the manufacturers", "icon": "file-check", "at": A("c05", "powerloom")}])
cue(type="section", t0=S("c06"), t1=E("c06") + 0.05, at=A("c06", "committee"), act="CENTRAL EXCISE ACT, 1944", num="2(f)", title="The Committee's borrowed definition",
    points=[{"text": "“Manufacture”: not defined in the 1963 Act", "at": A("c06", "define")},
            {"text": "Take the excise definition instead", "at": A("c06", "central")},
            {"text": "Any process incidental or ancillary to completing a product", "at": A("c06", "incidental")}],
    note={"text": "So, it said, bleaching and dyeing = manufacture", "icon": "arrow-right", "at": A("c06", "processes")})

# ── 4 · what the court held ──────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="notequal", t0=S("c07"), t1=E("c07") + 0.05, left="Undefined in this Act", right="another Act's definition", at=A("c07", "word"),
    left_at=A("c07", "word"), sub="Only if read in by reference or incorporation", sub_at=A("c07", "reference"))
cue(type="cite", t0=A("c07", "word"), t1=E("c07") + 0.05, at=A("c07", "word"), tag="SUPREME COURT · RELIED ON",
    cases=[{"name": "Union of India v. R.C. Jain", "cite": "(1981) 2 SCC 308"},
           {"name": "Jagatram Ahuja v. Commissioner of Gift Tax", "cite": "(2000) 8 SCC 249"}])
cue(type="point", t0=S("c08"), t1=A("c08", "so") - 0.05, text="Every statute: its own context, scheme and purpose", icon="scale", accent=True, at=A("c08", "statute"))
cue(type="compare", t0=A("c08", "so"), t1=E("c08") + 0.05, head="“Manufactured” in Section 5A", head_at=A("c08", "manufactured"),
    cols=[{"title": "Common parlance", "icon": "check", "at": A("c08", "common")}, {"title": "A borrowed sense", "icon": "x", "at": A("c08", "borrowed")}],
    rows=[{"cells": ["its ordinary meaning", "Central Excise Act, § 2(f)"], "cells_at": [A("c08", "meaning"), A("c08", "statute", 2)]}])

# ── 5 · the verdict ──────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="verdicts", t0=S("c09"), t1=E("c09") + 0.05,
    rows=[{"text": "Job-work dyeing and bleaching = manufacture?", "ok": False, "at": A("c09", "dyeing"), "strike_at": A("c09", "manufacture")},
          {"text": "At best, “the textile upgraded” · an extended arm of the powerloom industry", "ok": True, "at": A("c09", "upgraded")},
          {"text": "No textile cess · appeal dismissed", "ok": True, "at": A("c09", "cess")}])
cue(type="point", t0=S("c10"), t1=E("c10") + 0.05, text="Like · Share · Subscribe · lawworld.ai", icon="check", accent=True, at=A("c10", "like"))
