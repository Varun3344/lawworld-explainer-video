# M/s AVS Bull v. The Sub Collector, Perinthalmanna & Anr., W.P.(C) No. 48444 of 2025, 2026:KER:80857, High Court of Kerala
# (M.A. Abdul Hakhim J., 23.10.2026, "CR"): panel cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND).
# HOOK format (split/JUDGMENT_HOOK_FORMAT.md): c01 hook question, c02 curiosity, c03 "Hi, I'm Ravishankar" + bench, c04-c07 facts /
# case / both sides, c08 the LawWorld request, c09-c10 the verdict.
# Facts from the judgment (Indian Kanoon render, doc 166033275; paras): the petitioner claims to be a registered partnership firm;
# Ext.P3, the Sub Collector's order of 10.12.2025 under Section 219U, Kerala Panchayat Raj Act, 1994, confiscating its soil excavator
# (1); seized by the Pulikkal Grama Panchayat Secretary on 15.08.2025 (Ext.P1 mahazar) "on the allegation that the said Excavator was
# used for dumping waste in an abandoned granite quarry"; to Kondotty Police Station; enquiry; confiscated, to be auctioned, the sale
# money to the Panchayat Fund (2); the Panchayat's counter: Rs.12,33,773 spent on removal (3); no reply affidavit (4); the owner:
# Section 219U needs a vehicle carrying waste through a public place / road, or on its return; Ext.P8 (agreement 13.06.2025): the
# lessee alone responsible for any penalty (6); the State: used for several days; the owner "cannot be allowed to shirk its
# responsibilities" by the lease (7); the owner: seized from private land, not in use or returning (10). Held: Section 219U(1), two
# contingencies; the second (on its return after the offence) needs no public place or road; Section 219N(2) bars waste in private
# places; Mischief Rule: return covers parking on return; parked on the spot; seizure justified (11, 12); Section 219U(2) (13);
# Ext.P8 "executed on a plain paper and it does not have the trappings of a Lease Deed"; even assuming a lease, the registered owner
# took no reasonable care; "A mere incorporation of a condition in the Lease Deed alone is not sufficient"; several days (14);
# confiscation fully justified (15, 16); writ petition dismissed (17). Appendix: Ext.P6 RC (15.05.2024), Ext.P8 dated 13.06.2025.
# Not on any card: the persons in FIR 968/2025; "hospital waste" (the State's / Panchayat's submission, 7, 8); the Rs.12.33 lakh figure.
# No section sign anywhere. List lines <= 52 chars. Official portrait from the High Court of Kerala's "Present Judges" page on the bench card.
FORMAT = "hook"   # build_course_plan.py: no opening sting, 15-frame lead (the cover), name tag on the "Ravishankar" clip

def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
ENDCARD = {"title": "Leased out your excavator: can it still be confiscated?", "line": "Plain paper: not a lease deed · the registered owner must take reasonable care · writ petition dismissed", "sub": "LawWorld: legal research for advocates"}

# ── 1 · leased out, still liable? (hook, curiosity, intro) ──────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "lease"), text="You lease out your excavator and it is used to dump waste. Can the authorities confiscate it from you, the registered owner?", hl="confiscate it from you")
cue(type="list", t0=S("c02"), t1=A("c02", "so") - 0.05, head="The owner's case", head_at=S("c02") + 0.05,
    items=[{"n": 1, "text": "A lease: the lessee alone bears any penalty", "at": A("c02", "lease")},
           {"n": 2, "text": "Seized on private land, while not in use", "at": A("c02", "seized")}])
cue(type="point", t0=A("c02", "so") - 0.05, t1=E("c02") + 0.05, text="So is the confiscation lawful?", icon="search", accent=True, at=A("c02", "confiscation"))
cue(type="bench", t0=S("c03"), t1=E("c03") + 0.05, tag="Kerala High Court · 23 October 2026",
    judges=[{"name": "Justice M.A. Abdul Hakhim", "photo": "../brand/judges/ma_abdul_hakhim.jpg", "at": A("c03", "honourable")}])

# ── 2 · the seizure ─────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=S("c04"), t1=E("c05") + 0.05, at=A("c04", "panchayat"), tag="HIGH COURT OF KERALA · 23.10.2026",
    cases=[{"name": "M/s AVS Bull v. The Sub Collector & Anr.", "cite": "2026:KER:80857 · W.P.(C) No. 48444 of 2025"}])
cue(type="timeline", t0=S("c04"), t1=E("c04") + 0.05,
    nodes=[{"label": "SEIZED", "value": "15 August 2025", "sub": "Pulikkal Grama Panchayat · a soil excavator", "at": A("c04", "seized")},
           {"label": "THE ALLEGATION", "value": "waste dumping", "sub": "in an abandoned granite quarry", "tone": "red", "at": A("c04", "alleging")}])
cue(type="timeline", t0=S("c05"), t1=E("c05") + 0.05,
    nodes=[{"label": "SUB COLLECTOR, PERINTHALMANNA", "value": "confiscated", "sub": "Ext.P3 · 10 December 2025 · Section 219U", "at": A("c05", "confiscated")},
           {"label": "TO BE AUCTIONED", "value": "Panchayat Fund", "sub": "the sale money goes to the Panchayat", "at": A("c05", "auctioned")}])

# ── 3 · the lease defence (tall cards: no cite bar) ─────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c06"), t1=E("c06") + 0.05, head="The owner's writ petition", head_at=S("c06") + 0.05,
    steps=[{"label": "A partnership firm", "sub": "the registered owner · Feroke, Kozhikode", "icon": "user", "at": A("c06", "partnership")},
           {"label": "Agreement, 13 June 2025", "sub": "Ext.P8 · relied on as a lease", "icon": "file-text", "at": A("c06", "lease")},
           {"label": "Lessee alone bears penalty", "sub": "so the owner is not liable, it says", "icon": "scale", "at": A("c06", "penalty")}])
cue(type="compare", t0=S("c07"), t1=E("c07") + 0.05, head="Section 219U and the lease", head_at=S("c07") + 0.05,
    cols=[{"title": "The owner", "icon": "user", "at": A("c07", "argued")}, {"title": "The State", "icon": "landmark", "at": A("c07", "state")}],
    rows=[{"cells": ["Seizure needs waste carried on a public road", "No shirking responsibility by a lease"], "cells_at": [A("c07", "public"), A("c07", "said")]},
          {"cells": ["Not in use or returning when seized", "Used for several days to dump waste"], "cells_at": [A("c07", "returning"), A("c07", "hide")]}])

# ── 4 · before the verdict: the LawWorld request ────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c08"), t1=A("c08", "follow") - 0.05, text="The verdict is next. First, a quick request…", icon="scale", accent=True, at=A("c08", "decided"))
cue(type="list", t0=A("c08", "follow") - 0.05, t1=E("c08") + 0.05, head="Follow LawWorld · lawworld.ai", head_at=A("c08", "follow"),
    items=[{"n": 1, "text": "Search SC and High Court judgments, cited to source", "at": A("c08", "india's")},
           {"n": 2, "text": "Draft petitions, plaints and notices with AI", "at": A("c08", "platform")},
           {"n": 3, "text": "Sign up free · ₹200 AI credit included", "at": A("c08", "advocates")}])

# ── 5 · what the Court held ─────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "vehicle") - 0.05, text="What did the High Court decide?", icon="scale", accent=True, at=A("c09", "finally"))
cue(type="flow", t0=A("c09", "vehicle") - 0.05, t1=E("c09") + 0.05, head="Section 219U(1): the second limb", head_at=A("c09", "vehicle"),
    steps=[{"label": "On its return after the offence", "sub": "seizure on reasonable cause to suspect", "icon": "arrow-right", "at": A("c09", "returning")},
           {"label": "No public road needed", "sub": "Section 219N(2) covers private places too", "icon": "landmark", "at": A("c09", "public")},
           {"label": "Parked at the spot counts", "sub": "the Mischief Rule: seizure justified", "icon": "check", "tone": "ok", "at": A("c09", "parking")}])
cue(type="point", t0=S("c10"), t1=A("c10", "confiscation") - 0.05, text="Ext.P8: plain paper, no trappings of a Lease Deed · even if it were, “A mere incorporation of a condition in the Lease Deed alone is not sufficient”", icon="scale", accent=True, at=A("c10", "plain"))
cue(type="verdicts", t0=A("c10", "confiscation") - 0.05, t1=E("c10") + 0.05,
    rows=[{"text": "Confiscation under Section 219U(2): justified", "ok": True, "at": A("c10", "confiscation")},
          {"text": "The firm's writ petition", "ok": False, "at": A("c10", "petition"), "strike_at": A("c10", "dismissed")}])

MUSIC = {"file": "audio/bed_mixkit738_140s.mp3", "target_lufs": -21}   # owner 02-11-2026: trending-style royalty-free bed, audible under the voice
