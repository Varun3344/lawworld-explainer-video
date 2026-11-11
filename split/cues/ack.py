# Yusuf v. Vigyapan Loke Delhi Advertising CGHS Ltd., 2026 INSC 1207, Civil Appeal No. 14175 of 2026 (from SLP (C) No. 30778 of 2024),
# Supreme Court of India (Vikram Nath J. wrote it, Augustine George Masih J., Sandeep Mehta J.; pronounced 06.11.2026; REPORTABLE on
# page 1): panel cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND). Appeal number: blank on the PDF's page 1,
# taken from the sci.gov.in "Latest Judgments" listing ("C.A. No. 14175/2026"). DRAFT 11-11-2026, awaiting the owner's yes.
# HOOK format (split/JUDGMENT_HOOK_FORMAT.md): c01 hook question (spoken to everyone, no "Advocates,"), c02 curiosity (two courts),
# c03 "Hi, I'm Ravishankar" + the three-judge bench, c04-c05 the contract, the suit and the society's records, c06-c07 the Order VII
# Rule 11 rejection and both sides, c08 the LawWorld request, c09-c10 the verdict.
# Facts (para): HC order 04.11.2024 in C.R.P. 66/2020, revision allowed, plaint rejected as time-barred (2, 3.5); suit of 2014 under
# Order XXXVII CPC on a civil works contract of 10.02.2000 for a multi-storey building in Mayur Vihar, Delhi; running bills 2000-2003;
# Rs 11,16,000 + Rs 11,04,840 interest at 9% p.a. (3.1); Order VII Rule 11 application: limitation, no cause of action (3.2); Trial
# Court 06.01.2020 rejected it: balance sheets 2004-2013 = acknowledgment, fresh limitation (3.3); HC: the 31.03.2013 balance sheet
# showed Rs 21,79,465 (sundry creditors, 2004-05) but not that it was "due and payable to the original plaintiff" (8); appeal by the
# legal heir (3.6); cheques to him dishonoured (6); 2004-05 bank reconciliation statements: three cheques in favour of "Wazir Hussain
# Contractor" (12); Rs 21,79,134 carried forward under "Balances pertaining to 2004-05" (13). Held: no creditor's name or fixed format
# needed; liability in the society's own balance sheets, carried forward to 2013, "renewing the limitation period every year" (14);
# entries not conclusive of the whole amount, "matters for trial"; at the Order VII Rule 11 stage the court "ought not to have gone into
# the depths of evidence ..." (15, quoted on the c10 card); plea that a time-barred debt cannot be revived indefinitely without a
# condonation application "cannot be sustained": a fresh period runs from each subsequent date of acknowledgment, no condonation
# application needed (16); HC order set aside, suit revived on the Trial Court's file, merits open (17); appeal allowed (18).
# Names: only the cause title on the cite card; no private name in speech; the "alleged embezzlement" plea (3.2) is not shown.
# Amount: para 8 Rs 21,79,465 vs para 13 Rs 21,79,134 -> the cards say "₹21.79 lakh" (true for both). List lines <= 52 chars.
# Bench photos (official sci.gov.in portraits): brand/judges/vikram_nath.jpg, augustine_george_masih.jpg, sandeep_mehta.jpg.
FORMAT = "hook"   # build_course_plan.py: no opening sting, 15-frame lead (the cover), name tag on the "Ravishankar" clip

def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
ENDCARD = {"title": "Too late to sue on old bills?", "line": "Here the society's own balance sheets were acknowledgments: a fresh period ran from each (Section 18)", "sub": "LawWorld: legal research for advocates"}

# ── 1 · too late to sue? (hook, curiosity, intro) ────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "your"), text="Bills from 2003, suit filed in 2014. Can the other side's own balance sheets keep the claim alive?", hl="keep the claim alive?")
cue(type="flow", t0=S("c02"), t1=A("c02", "so") - 0.05, head="One plaint, two courts", head_at=S("c02") + 0.05,
    steps=[{"label": "Trial Court", "sub": "6 Jan 2020 · balance sheets acknowledged the debt", "icon": "scale", "at": A("c02", "trial")},
           {"label": "Delhi High Court", "sub": "4 Nov 2024 · plaint rejected as time-barred", "icon": "landmark", "at": A("c02", "delhi")}])
cue(type="point", t0=A("c02", "so") - 0.05, t1=E("c02") + 0.05, text="So who was right?", icon="search", accent=True, at=A("c02", "who"))
cue(type="bench", t0=S("c03"), t1=E("c03") + 0.05, tag="Supreme Court of India · 6 November 2026",
    judges=[{"name": "Justice Vikram Nath", "photo": "../brand/judges/vikram_nath.jpg", "at": A("c03", "three")},
            {"name": "Justice Augustine George Masih", "photo": "../brand/judges/augustine_george_masih.jpg", "at": A("c03", "judges")},
            {"name": "Justice Sandeep Mehta", "photo": "../brand/judges/sandeep_mehta.jpg", "at": A("c03", "supreme")}])

# ── 2 · bills and balance sheets ─────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=S("c04"), t1=E("c04") + 0.05, at=A("c04", "in"), tag="SUPREME COURT OF INDIA · 06.11.2026",
    cases=[{"name": "Yusuf v. Vigyapan Loke Delhi Advertising CGHS Ltd.", "cite": "2026 INSC 1207 · Civil Appeal No. 14175 of 2026"}])
cue(type="timeline", t0=S("c04"), t1=E("c04") + 0.05,
    nodes=[{"label": "CONTRACT", "value": "10 Feb 2000", "sub": "building work · Mayur Vihar, Delhi", "at": A("c04", "hired")},
           {"label": "RUNNING BILLS", "value": "2000 to 2003", "sub": "₹11,16,000 claimed", "at": A("c04", "running")},
           {"label": "SUMMARY SUIT", "value": "2014", "sub": "plus ₹11,04,840 interest at 9%", "at": A("c04", "sued")}])
cue(type="list", t0=S("c05"), t1=E("c05") + 0.05, head="The society's own records", head_at=S("c05") + 0.05,
    items=[{"n": 1, "text": "2004-05 bank records: 3 cheques in his favour", "at": A("c05", "bank")},
           {"n": 2, "text": "Cheques issued to him were dishonoured", "at": A("c05", "favour")},
           {"n": 3, "text": "Balance sheets to 2013: ₹21.79 lakh carried forward", "at": A("c05", "carried")},
           {"n": 4, "text": "Head: ‘Balances pertaining to 2004-05’", "at": A("c05", "lakh")}])

# ── 3 · rejected at the threshold ────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c06"), t1=E("c06") + 0.05, head="Order VII Rule 11 · reject the plaint?", head_at=S("c06") + 0.05,
    steps=[{"label": "Society's application", "sub": "time-barred, no cause of action", "icon": "file-text", "at": A("c06", "rejection")},
           {"label": "Trial Court: refused", "sub": "6 Jan 2020: other issues need evidence", "icon": "scale", "at": A("c06", "eleven")},
           {"label": "High Court: rejected", "sub": "4 Nov 2024: not shown as due to him", "icon": "landmark", "at": A("c06", "agreed")}])
cue(type="compare", t0=S("c07"), t1=E("c07") + 0.05, head="Acknowledged, or time-barred?", head_at=S("c07") + 0.05,
    cols=[{"title": "The contractor's heir", "icon": "scale", "at": A("c07", "heir")}, {"title": "The society", "icon": "landmark", "at": A("c07", "society")}],
    rows=[{"cells": ["Entries are acknowledgments: Section 18", "A time-barred debt can't be revived forever"], "cells_at": [A("c07", "acknowledgments"), A("c07", "debt")]},
          {"cells": ["Acknowledged every year, 2005 to 2013", "No application to condone the delay"], "cells_at": [A("c07", "limitation"), A("c07", "forever")]}])

# ── 4 · before the verdict: the LawWorld request ─────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c08"), t1=A("c08", "follow") - 0.05, text="The verdict is next. First, a quick request…", icon="scale", accent=True, at=A("c08", "decided"))
cue(type="list", t0=A("c08", "follow") - 0.05, t1=E("c08") + 0.05, head="Follow LawWorld · lawworld.ai", head_at=A("c08", "follow"),
    items=[{"n": 1, "text": "Search SC and High Court judgments, cited to source", "at": A("c08", "india's")},
           {"n": 2, "text": "Draft petitions, plaints and notices with AI", "at": A("c08", "platform")},
           {"n": 3, "text": "Sign up free · ₹200 AI credit included", "at": A("c08", "advocates")}])

# ── 5 · what the Court held ──────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "entries") - 0.05, text="What did the Supreme Court decide?", icon="scale", accent=True, at=A("c09", "finally"))
cue(type="list", t0=A("c09", "entries") - 0.05, t1=E("c09") + 0.05, head="Section 18, Limitation Act · held", head_at=A("c09", "entries"),
    items=[{"n": 1, "text": "No creditor's name or fixed format needed", "at": A("c09", "entries")},
           {"n": 2, "text": "Here, the entries were acknowledgments", "at": A("c09", "acknowledgments")},
           {"n": 3, "text": "A fresh period from each date of acknowledgment", "at": A("c09", "fresh")},
           {"n": 4, "text": "No condonation of delay application needed", "at": A("c09", "condonation")}])
cue(type="point", t0=S("c10"), t1=A("c10", "its") - 0.05, text="Order VII Rule 11: the Court “ought not to have gone into the depths of evidence and conclusively determined the non-existence of liability.”", icon="quote", accent=True, at=A("c10", "threshold"))
cue(type="verdicts", t0=A("c10", "its") - 0.05, t1=E("c10") + 0.05,
    rows=[{"text": "High Court's rejection of the plaint", "ok": False, "at": A("c10", "its")},
          {"text": "Society's plea: no revival without condonation", "ok": False, "at": A("c10", "aside")},
          {"text": "Suit revived on the Trial Court's file", "ok": True, "at": A("c10", "revived")},
          {"text": "All questions on the merits remain open", "ok": True, "at": A("c10", "merits")}])

MUSIC = {"file": "audio/bed_mixkit738_140s.mp3", "target_lufs": -21}   # owner 02-11-2026: trending-style royalty-free bed, audible under the voice
