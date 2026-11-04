# Shiva Enterprises & Ors. v. State of Maharashtra & Ors. (W.P. No. 31910 of 2025) c/w Siddhi Agencies & Ors. v. State of Maharashtra
# & Ors. (W.P. No. 31320 of 2025), 2026:KHC:60505, High Court of Karnataka at Bengaluru (Suraj Govindaraj J.; reserved 09.09.2026,
# CAV order 29.10.2026; "R" on page 1): panel cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND).
# HOOK format (split/JUDGMENT_HOOK_FORMAT.md): c01 hook question (spoken to everyone, no "Advocates,"), c02 curiosity, c03 "Hi, I'm
# Ravishankar" + bench, c04-c05 the timeline, c06-c07 both sides, c08 the LawWorld request, c09-c10 the verdict.
# Facts (para): truck intercepted 19.08.2025 at Kagni Toll Naka, Hatkanangale, Kolhapur (5, 10); Crime No. 446/2025, Vadgaon PS,
# 20.08.2025, on a constable's complaint against unknown persons, FSS Act 2006 + BNS (6, 20.15); the petitioners (two Tumkur firms and
# their partners) not named in the FIR (7, 11, 20.15); 21.08.2025: five to six Vadgaon police at the Tumkur premises, notices to appear
# at Vadgaon, statements recorded at Tumkur (7, 11, 20.15); counsel: s.179 BNSS reaches only persons "within the limits of his own or
# any adjoining station" (13.3-13.5, 20.2); respondents 1-2 served, did not appear (20.11); Karnataka's AGA on instructions: never
# contacted, not informed before, during or after (16.2, 21.10, 21.12); held: Tumkur is outside Vadgaon PS and any adjoining station,
# the notices were without authority so far as they required attendance at Vadgaon (20.59); the Tumkur operation without coordination
# with the Karnataka police and without shown compliance with ss.185-186 BNSS was "unlawful" (21.98); statements not to be relied on as
# lawfully obtained, fresh statements may be taken in accordance with law (21.92); ORDER (ii)-(ix): notices unenforceable, no coercive
# action; no such notices while outside the limits; operation unsustainable, statements not relied on; ledger books and copies
# accounted for, documents held without lawful authority returned within 21 days, subject to any lawful order; prior written intimation
# to the jurisdictional Karnataka police station before any further operation in Karnataka; FIR / investigation not quashed; no finding
# on the merits or anyone's guilt. Names: only the firms' cause title on the cite card; no accusation in speech (goods and offences off
# speech; the FIR on a card only as "FSS Act + BNS, against unknown persons"). List lines <= 52 chars.
# Bench photo: brand/judges/suraj_govindaraj.jpg (official KHC judge-profile portrait SGRJnew.jpeg, byte-identical, checked 04-11-2026).
FORMAT = "hook"   # build_course_plan.py: no opening sting, 15-frame lead (the cover), name tag on the "Ravishankar" clip

def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
ENDCARD = {"title": "Summoned to another State: must you go?", "line": "Not from Tumkur: the Section 179 notices to appear at Vadgaon are unenforceable · the FIR stays", "sub": "LawWorld: legal research for advocates"}

# ── 1 · summoned to another State? (hook, curiosity, intro) ──────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "police"), text="Another State's police send a notice: come to our police station. Are you bound to go?", hl="Are you bound to go?")
cue(type="list", t0=S("c02"), t1=A("c02", "so") - 0.05, head="Tumkur, Karnataka · 21 August 2025", head_at=S("c02") + 0.05,
    items=[{"n": 1, "text": "Maharashtra police at two traders' premises", "at": A("c02", "came")},
           {"n": 2, "text": "Statements and business records taken", "at": A("c02", "statements")},
           {"n": 3, "text": "The Karnataka police never told", "at": A("c02", "never")}])
cue(type="point", t0=A("c02", "so") - 0.05, t1=E("c02") + 0.05, text="Was any of it lawful?", icon="search", accent=True, at=A("c02", "any"))
cue(type="bench", t0=S("c03"), t1=E("c03") + 0.05, tag="Karnataka High Court · 29 October 2026",
    judges=[{"name": "Justice Suraj Govindaraj", "photo": "../brand/judges/suraj_govindaraj.jpg", "at": A("c03", "honourable")}])

# ── 2 · from Kolhapur to Tumkur ──────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=S("c04"), t1=E("c05") + 0.05, at=A("c04", "maharashtra"), tag="HIGH COURT OF KARNATAKA · 29.10.2026",
    cases=[{"name": "Shiva Enterprises & Siddhi Agencies v. State of Maharashtra", "cite": "2026:KHC:60505 · W.P. Nos. 31910 & 31320 of 2025"}])
cue(type="timeline", t0=S("c04"), t1=E("c04") + 0.05,
    nodes=[{"label": "TRUCK STOPPED", "value": "19 Aug 2025", "sub": "Kagni toll naka, Kolhapur", "at": A("c04", "nineteenth")},
           {"label": "FIR AT VADGAON", "value": "20 Aug 2025", "sub": "FSS Act + BNS · unknown persons", "at": A("c04", "food")}])
cue(type="timeline", t0=S("c05"), t1=E("c05") + 0.05,
    nodes=[{"label": "VADGAON POLICE IN TUMKUR", "value": "21 Aug 2025", "sub": "two firms not named in the FIR", "at": A("c05", "visited")},
           {"label": "NOTICES TO THE PARTNERS", "value": "appear at Vadgaon", "sub": "Section 179 BNSS · Kolhapur district", "at": A("c05", "notices")}])

# ── 3 · who told Karnataka? ──────────────────────────────────────────────────────────────────────────────────────────
cue(type="compare", t0=S("c06"), t1=E("c07") + 0.05, head="Could Vadgaon summon Tumkur?", head_at=S("c06") + 0.05,
    cols=[{"title": "The traders", "icon": "user", "at": A("c06", "yet")}, {"title": "The two States", "icon": "landmark", "at": A("c07", "maharashtra")}],
    rows=[{"cells": ["Statements taken in Tumkur, not Vadgaon", "Maharashtra: served, did not appear"], "cells_at": [A("c06", "statements"), A("c07", "appear")]},
          {"cells": ["Section 179: own or adjoining station only", "Karnataka: never informed, before or after"], "cells_at": [A("c06", "section"), A("c07", "informed")]}])

# ── 4 · before the verdict: the LawWorld request ─────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c08"), t1=A("c08", "follow") - 0.05, text="The verdict is next. First, a quick request…", icon="scale", accent=True, at=A("c08", "decided"))
cue(type="list", t0=A("c08", "follow") - 0.05, t1=E("c08") + 0.05, head="Follow LawWorld · lawworld.ai", head_at=A("c08", "follow"),
    items=[{"n": 1, "text": "Search SC and High Court judgments, cited to source", "at": A("c08", "india's")},
           {"n": 2, "text": "Draft petitions, plaints and notices with AI", "at": A("c08", "platform")},
           {"n": 3, "text": "Sign up free · ₹200 AI credit included", "at": A("c08", "advocates")}])

# ── 5 · what the Court held ──────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "notices") - 0.05, text="What did the High Court decide?", icon="scale", accent=True, at=A("c09", "finally"))
cue(type="list", t0=A("c09", "notices") - 0.05, t1=E("c09") + 0.05, head="Section 179 BNSS · the Tumkur visit", head_at=A("c09", "notices"),
    items=[{"n": 1, "text": "Notices to appear at Vadgaon: unenforceable", "at": A("c09", "could")},
           {"n": 2, "text": "Tumkur: beyond Vadgaon's own and adjoining limits", "at": A("c09", "tumkur")},
           {"n": 3, "text": "Visit, Karnataka police not told: unlawful", "at": A("c09", "visit")}])
cue(type="verdicts", t0=S("c10"), t1=E("c10") + 0.05,
    rows=[{"text": "Relying on the statements taken at Tumkur", "ok": False, "at": A("c10", "statements")},
          {"text": "Ledgers: account for; return those held unlawfully", "ok": True, "at": A("c10", "ledgers")},
          {"text": "Next time: written intimation to Karnataka police", "ok": True, "at": A("c10", "next")},
          {"text": "FIR not quashed: the probe goes on, by law", "ok": True, "at": A("c10", "stays")}])

MUSIC = {"file": "audio/bed_mixkit738_140s.mp3", "target_lufs": -21}   # owner 02-11-2026: trending-style royalty-free bed, audible under the voice
