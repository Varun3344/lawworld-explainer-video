# Uday Chand Vedi v. Puneet Vedi, C.C.C.A. No. 68 of 2010, High Court for the State of Telangana at Hyderabad (Suddala Chalapathi Rao J.;
# reserved 29.07.2026, pronounced 30.10.2026; cover sheet: "marked to Law Reporters/Journals? : Yes"): panel cues, run by
# split/build_course_plan.py (helpers: at S E cue fx have r3 PEND). LawWorld's first Telangana reel.
# HOOK format (split/JUDGMENT_HOOK_FORMAT.md): c01 hook question (spoken to everyone, no "Advocates,"), c02 curiosity, c03 "Hi, I'm
# Ravishankar" + bench, c04-c06 the deal and the decree, c07 both sides, c08 the LawWorld request, c09-c10 the verdict.
# Source: the Indian Kanoon text (doc 175732047; the court's own search is captcha-gated, not bypassed). Facts (para): appeal against
# the decree dated 29.01.2010 in O.S. 2124/2006, X Addl. Senior Civil Judge (FTC), City Civil Court, Hyderabad (2); agreement of sale
# 26.12.2005 for Rs. 10,00,000 (4); Rs. 50,000 advance, balance Rs. 9,50,000 by 20.01.2006; buyer temporarily residing in the USA (5);
# Ex.A1: balance "on or before 20.01.2006, failing which the advance ... shall be forfeited and the defendant shall be entitled to
# alienate the property to any third party" (22); letter 16.01.2006 under Certificate of Posting (Ex.A2); Ex.A3 13.03.2006, telegram
# 18.10.2006 (Ex.A4), GPA 15.07.2008 (Ex.A8) all after 20.01.2006 (6, 7, 12, 25); reply notice 31.10.2006 cancelled the agreement and
# forfeited the advance (7, 23); trial court: ready and willing, time not the essence, sale deed and possession in 45 days (12, 13);
# seller: time the essence, a telegraphic notice does not establish readiness (14, 15); buyer: Exs.A1-A9 show readiness, no automatic
# cancellation (19). Held: "the time was the essence of the contract" (22); except Ex.A2, readiness within the time not established
# (25); certificate of posting "not a proper mode"; "there is no concrete material placed by plaintiff to show that he was always ready
# and willing to perform his part" (27); only Rs. 50,000 of Rs. 10,00,000 paid (29, 30); decree set aside, appeal allowed, suit
# dismissed (31, 32). Names: only the cause title on the cite card. List lines <= 52 chars.
# Bench photo: brand/judges/suddala_chalapathi_rao.jpg (official portrait, tshc.gov.in sitting-judge profile id 398,
# /images/admin_2025_08_01T18_06_28CHALAPATHI RAO.png, rounded border cropped).
FORMAT = "hook"   # build_course_plan.py: no opening sting, 15-frame lead (the cover), name tag on the "Ravishankar" clip

def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
ENDCARD = {"title": "Late with the balance: can you force the sale?", "line": "Not on these facts: ₹50,000 of ₹10 lakh paid, readiness and willingness not proved, so the suit was dismissed", "sub": "LawWorld: legal research for advocates"}

# ── 1 · late with the balance? (hook, curiosity, intro) ──────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "pay"), text="Paid ₹50,000 of ₹10 lakh, then missed the deadline for the balance. Can you still force the sale?", hl="force the sale?")
cue(type="list", t0=S("c02"), t1=A("c02", "so") - 0.05, head="One sale · two courts", head_at=S("c02") + 0.05,
    items=[{"n": 1, "text": "Trial court, 2010: sale deed ordered", "at": A("c02", "trial")},
           {"n": 2, "text": "The seller appeals to the High Court", "at": A("c02", "appealed")},
           {"n": 3, "text": "The appeal waits 16 years", "at": A("c02", "sixteen")}])
cue(type="point", t0=A("c02", "so") - 0.05, t1=E("c02") + 0.05, text="So who was right?", icon="search", accent=True, at=A("c02", "who"))
cue(type="bench", t0=S("c03"), t1=E("c03") + 0.05, tag="Telangana High Court · 30 October 2026",
    judges=[{"name": "Justice Suddala Chalapathi Rao", "photo": "../brand/judges/suddala_chalapathi_rao.jpg", "at": A("c03", "honourable")}])

# ── 2 · ten lakh, fifty thousand paid ────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=S("c04"), t1=E("c04") + 0.05, at=A("c04", "december"), tag="TELANGANA HIGH COURT · 30.10.2026",
    cases=[{"name": "Uday Chand Vedi v. Puneet Vedi", "cite": "C.C.C.A. No. 68 of 2010 · appeal from O.S. No. 2124 of 2006"}])
cue(type="timeline", t0=S("c04"), t1=E("c04") + 0.05,
    nodes=[{"label": "AGREEMENT OF SALE", "value": "₹10,00,000", "sub": "26 Dec 2005", "at": A("c04", "agreed")},
           {"label": "ADVANCE PAID", "value": "₹50,000", "sub": "₹9,50,000 due by 20 Jan 2006", "at": A("c04", "paid")}])
cue(type="timeline", t0=S("c05"), t1=E("c05") + 0.05,
    nodes=[{"label": "BEFORE THE DEADLINE", "value": "16 Jan 2006", "sub": "one letter, certificate of posting", "at": A("c05", "before")},
           {"label": "THE DEADLINE", "value": "20 Jan 2006", "sub": "the ₹9,50,000 is not paid", "tone": "red", "at": A("c05", "posting")},
           {"label": "EVERYTHING ELSE", "value": "after the date", "sub": "Mar 2006 letter, Oct 2006 telegram", "at": A("c05", "everything")}])
cue(type="cite", t0=S("c06"), t1=E("c06") + 0.05, at=A("c06", "october"), tag="TELANGANA HIGH COURT · 30.10.2026",
    cases=[{"name": "Uday Chand Vedi v. Puneet Vedi", "cite": "C.C.C.A. No. 68 of 2010 · appeal from O.S. No. 2124 of 2006"}])
cue(type="timeline", t0=S("c06"), t1=E("c06") + 0.05,
    nodes=[{"label": "SELLER CANCELS", "value": "31 Oct 2006", "sub": "the ₹50,000 advance forfeited", "tone": "red", "at": A("c06", "cancelled")},
           {"label": "TRIAL COURT DECREE", "value": "29 Jan 2010", "sub": "time not the essence: sale deed ordered", "at": A("c06", "decreed")}])

# ── 3 · the appeal ───────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="compare", t0=S("c07"), t1=E("c07") + 0.05, head="Was the buyer ready and willing?", head_at=S("c07") + 0.05,
    cols=[{"title": "The seller", "icon": "user", "at": A("c07", "seller")}, {"title": "The buyer", "icon": "file-text", "at": A("c07", "buyer")}],
    rows=[{"cells": ["Time was the essence of the deal", "Exs. A1 to A9 show his readiness"], "cells_at": [A("c07", "essence"), A("c07", "letters")]},
          {"cells": ["A telegram does not prove readiness", "No automatic cancellation clause"], "cells_at": [A("c07", "telegram"), A("c07", "always")]}])

# ── 4 · before the verdict: the LawWorld request ─────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c08"), t1=A("c08", "follow") - 0.05, text="The verdict is next. First, a quick request…", icon="scale", accent=True, at=A("c08", "decided"))
cue(type="list", t0=A("c08", "follow") - 0.05, t1=E("c08") + 0.05, head="Follow LawWorld · lawworld.ai", head_at=A("c08", "follow"),
    items=[{"n": 1, "text": "Search SC and High Court judgments, cited to source", "at": A("c08", "india's")},
           {"n": 2, "text": "Draft petitions, plaints and notices with AI", "at": A("c08", "platform")},
           {"n": 3, "text": "Sign up free · ₹200 AI credit included", "at": A("c08", "advocates")}])

# ── 5 · what the Court held ──────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "read") - 0.05, text="What did the High Court decide?", icon="scale", accent=True, at=A("c09", "finally"))
cue(type="flow", t0=A("c09", "read") - 0.05, t1=E("c09") + 0.05, head="“The time was the essence of the contract.”", head_at=A("c09", "read"),
    steps=[{"label": "Pay by 20 Jan 2006", "sub": "the balance of ₹9,50,000", "icon": "calendar", "at": A("c09", "agreement")},
           {"label": "Or lose the advance", "sub": "the ₹50,000 is forfeited", "icon": "x", "tone": "muted", "at": A("c09", "miss")},
           {"label": "Seller may sell", "sub": "to any third party · Ex.A1", "icon": "check", "at": A("c09", "others")}])
cue(type="point", t0=S("c10"), t1=A("c10", "decree") - 0.05, text="“…there is no concrete material placed by plaintiff to show that he was always ready and willing to perform his part.”", icon="quote", accent=True, at=A("c10", "only"))
cue(type="verdicts", t0=A("c10", "decree") - 0.05, t1=E("c10") + 0.05,
    rows=[{"text": "Trial court decree of 29.01.2010", "ok": False, "at": A("c10", "decree"), "strike_at": A("c10", "aside")},
          {"text": "Seller's appeal allowed", "ok": True, "at": A("c10", "aside")},
          {"text": "Buyer's suit for specific performance", "ok": False, "at": A("c10", "buyer's"), "strike_at": A("c10", "dismissed")}])

MUSIC = {"file": "audio/bed_mixkit738_140s.mp3", "target_lufs": -21}   # owner 02-11-2026: trending-style royalty-free bed, audible under the voice
