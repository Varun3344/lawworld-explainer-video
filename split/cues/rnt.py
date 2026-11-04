# M/s. Jaison Electronics v. Mujahid Baig & Anr., C.R.P. No. 1837 of 2026, 2026:MHC:4386, High Court of Judicature at Madras
# (P.B. Balaji J.; reserved 28.09.2026, pronounced 30.10.2026; listed as Reportable in the court's judis database): panel cues, run by
# split/build_course_plan.py (helpers: at S E cue fx have r3 PEND).
# HOOK format (split/JUDGMENT_HOOK_FORMAT.md): c01 hook question (spoken to everyone, no "Advocates,"), c02 curiosity, c03 "Hi, I'm
# Ravishankar" + bench, c04-c05 notice and the two rent forums, c06-c07 both sides, c08 the LawWorld request, c09-c10 the verdict.
# Facts (para): eviction petition RLTOP 43/2023 on two grounds - failure to enter into a tenancy agreement, s.21(2)(a) r/w s.4(2) of
# the TNRRRLT Act (Act 42 of 2017), and rent default; Rent Court (29.09.2023) allowed s.21(2)(a), dismissed the default ground
# s.21(2)(b) (3); Rent Tribunal (RLTA 236/2023, 11.02.2026) confirmed (4); revision under Article 227 (prayer). Tenant's counsel:
# landlords' notice 19.10.2022 (sign a written tenancy agreement or vacate in a month), reply 11.11.2022 (the demand had lapsed by
# efflux of time, 575 days) (6); Hemalatha (DB, 2026 (4) CTC 39): a s.21(2)(a) petition after 575 days not maintainable, declared
# prospective; only the Supreme Court can overrule prospectively (Article 141), so it applies retrospectively (7, 10). Landlords:
# cause of action only after 575 days, reason for the failure irrelevant, Hemalatha does not affect pending proceedings (11). Held:
# window 90 -> 275 -> 575 days (15); agreed a High Court cannot invoke prospective overruling, but Hemalatha already held per incuriam
# (Neelavathi, CRP(MD) 1357/2026, 12.06.2026; L. Mohamed Ibrahim Sait, CRP 4791/2026, 12.08.2026), so not applied (14); "even on a
# plain reading of the statute, the cause of action for alleging failure can arise only after the expiry of 575 days"; consistent
# view on maintainability upheld by the SC in V. Ganesh (13, 15); C.R.P. dismissed, vacate and hand over possession by 31.12.2026,
# no costs (16). Names: only the cause title on the cite card; the Rs.89,000 figure (a party's, disputed) on no card.
# List lines <= 52 chars. No section sign anywhere. Bench photo: brand/judges/pb_balaji.jpg (official, as mcf / bcr).
FORMAT = "hook"   # build_course_plan.py: no opening sting, 15-frame lead (the cover), name tag on the "Ravishankar" clip

def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
ENDCARD = {"title": "Tenancy window over: too late to evict?", "line": "No: a failure to enter into a tenancy agreement can arise only after the 575 days, so a Section 21(2)(a) petition can be filed after them", "sub": "LawWorld: legal research for advocates"}

# ── 1 · too late to evict? (hook, curiosity, intro) ──────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "tenant"), text="Never signed a written tenancy agreement? Can the landlord evict you for that alone?", hl="evict you for that alone?")
cue(type="counters", t0=S("c02"), t1=A("c02", "so") - 0.05, head="Section 4(2) · TN Rent Act, 2017", head_at=S("c02") + 0.05,
    items=[{"value": 575, "unit": "DAYS", "label": "To sign a written agreement", "sub": "first 90 days, then 275, then 575", "at": A("c02", "five")}])
cue(type="point", t0=A("c02", "so") - 0.05, t1=E("c02") + 0.05, text="Window closed: too late to evict?", icon="search", accent=True, at=A("c02", "right"))
cue(type="bench", t0=S("c03"), t1=E("c03") + 0.05, tag="Madras High Court · 30 October 2026",
    judges=[{"name": "Justice P.B. Balaji", "photo": "../brand/judges/pb_balaji.jpg", "at": A("c03", "honourable")}])

# ── 2 · sign or vacate ───────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=S("c04"), t1=E("c04") + 0.05, at=A("c04", "according"), tag="HIGH COURT OF MADRAS · 30.10.2026",
    cases=[{"name": "M/s. Jaison Electronics v. Mujahid Baig & Anr.", "cite": "2026:MHC:4386 · C.R.P. No. 1837 of 2026"}])
cue(type="timeline", t0=S("c04"), t1=E("c04") + 0.05,
    nodes=[{"label": "LANDLORDS' NOTICE", "value": "19 Oct 2022", "sub": "sign an agreement, or vacate", "at": A("c04", "notice")},
           {"label": "TENANT'S REPLY", "value": "11 Nov 2022", "sub": "the demand had lapsed", "at": A("c04", "replied")}])
cue(type="timeline", t0=S("c05"), t1=E("c05") + 0.05,
    nodes=[{"label": "RENT COURT · 29.09.2023", "value": "Eviction ordered", "sub": "rent-default plea dismissed", "at": A("c05", "ordered")},
           {"label": "RENT TRIBUNAL · 11.02.2026", "value": "Eviction confirmed", "sub": "then this revision", "at": A("c05", "confirmed")}])

# ── 3 · the arguments ────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="compare", t0=S("c06"), t1=E("c07") + 0.05, head="Hemalatha (Division Bench) · does it apply?", head_at=S("c06") + 0.05,
    cols=[{"title": "The tenant", "icon": "user", "at": A("c06", "tenant")}, {"title": "The landlords", "icon": "landmark", "at": A("c07", "landlords")}],
    rows=[{"cells": ["No petition after 575 days", "It spared pending cases"], "cells_at": [A("c06", "division"), A("c07", "spared")]},
          {"cells": ["Made prospective, but only the SC can do that", "The reason for the failure is irrelevant"], "cells_at": [A("c06", "prospective"), A("c07", "irrelevant")]}])

# ── 4 · before the verdict: the LawWorld request ─────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c08"), t1=A("c08", "follow") - 0.05, text="The verdict is next. First, a quick request…", icon="scale", accent=True, at=A("c08", "decided"))
cue(type="list", t0=A("c08", "follow") - 0.05, t1=E("c08") + 0.05, head="Follow LawWorld · lawworld.ai", head_at=A("c08", "follow"),
    items=[{"n": 1, "text": "Search SC and High Court judgments, cited to source", "at": A("c08", "india's")},
           {"n": 2, "text": "Draft petitions, plaints and notices with AI", "at": A("c08", "platform")},
           {"n": 3, "text": "Sign up free · ₹200 AI credit included", "at": A("c08", "advocates")}])

# ── 5 · what the Court held ──────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "agreed") - 0.05, text="What did the High Court decide?", icon="scale", accent=True, at=A("c09", "finally"))
cue(type="list", t0=A("c09", "agreed") - 0.05, t1=E("c09") + 0.05, head="Prospective overruling · Hemalatha", head_at=A("c09", "agreed"),
    items=[{"n": 1, "text": "A High Court can't overrule prospectively", "at": A("c09", "overrule")},
           {"n": 2, "text": "But Hemalatha was already held per incuriam", "at": A("c09", "held")},
           {"n": 3, "text": "In Neelavathi and Mohamed Ibrahim Sait, 2026", "at": A("c09", "incuriam")}])
cue(type="point", t0=S("c10"), t1=A("c10", "revision") - 0.05, text="“Even on a plain reading of the statute, the cause of action for alleging failure can arise only after the expiry of 575 days.”", icon="quote", accent=True, at=A("c10", "failure"))
cue(type="verdicts", t0=A("c10", "revision") - 0.05, t1=E("c10") + 0.05,
    rows=[{"text": "The tenant's revision petition", "ok": False, "at": A("c10", "revision")},
          {"text": "Eviction under Section 21(2)(a) stands", "ok": True, "at": A("c10", "dismissed")},
          {"text": "Vacate by 31.12.2026 · no costs", "ok": True, "at": A("c10", "vacate")}])

MUSIC = {"file": "audio/bed_mixkit738_140s.mp3", "target_lufs": -21}   # owner 02-11-2026: trending-style royalty-free bed, audible under the voice
