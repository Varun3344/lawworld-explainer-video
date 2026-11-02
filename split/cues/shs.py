# Shanta Sinha (through LRs) v. Ruma Devi & Anr., First Appeal No. 128 of 2017, CNR BRHC010972642017, High Court of Judicature at
# Patna (Ramesh Chand Malviya J., single Judge, oral judgment, 29.10.2026, "AFR"): panel cues, run by split/build_course_plan.py
# (helpers: at S E cue fx have r3 PEND). HOOK format (split/JUDGMENT_HOOK_FORMAT.md): c01 hook question, c02 curiosity,
# c03 "Hi, I'm Ravishankar" + bench, c04-c07 facts / case / both sides, c08 the LawWorld request, c09-c10 the verdict.
# Who is who: propounders / plaintiffs = the testatrix's two nieces (daughters of her brother Bijali Prasad Singh), granted probate
# at trial, respondents here; objector / defendant = her late husband's sister, then her daughter Shanta Sinha, the appellant (now
# through LRs). The appellants won.
# Facts from the judgment (paras): F.A. under s.299 Indian Succession Act v. judgment of 05.07.2017, VIIIth ADJ Begusarai, Title Suit
# 02/2007 (Probate Case 01/1995) (2); nieces sought probate (s.276) of the Will of 17.12.1994, Exhibit 3, Schedules I-III (4); no
# issue of her own; L.T.I. identified by her brother; "not illiterate" but her hands trembled, so an L.T.I.; died 20.01.1995; probate
# application 14.03.1995 (5); objection 25.07.1995 by the husband's full sister, later her daughter; became a regular Title Suit (6);
# trial court: L.T.I. hers, identified by the brother, attesting witnesses + scribe supported execution; probate granted (13, 14);
# appeal by the defendant (15); appellants: literate, signed the F.I.R. days earlier, L.T.I. at the top right of every page,
# unregistered, witnesses not independent (16, 16.i); respondents: placement + non-registration never pleaded, not to be argued
# first in appeal, Ram Sarup Gupta (17, 22); held: forgery pleaded, so how the mark came on the paper was in issue (23); s.63(a), (b)
# are for the propounder to prove; "Even where the contestant has not pleaded a suspicious circumstance with particularity", the Will
# is not proved if the circumstance is inherent in the document (Derek A.C. Lobo) (24); s.63(c) + s.68 Evidence Act; "Proof that the
# mark is the testatrix's own is not proof that she executed this Will" (26); she signed Exhibit A, the F.I.R. of 08.12.1994, nine
# days before the Will (31-33); mark at the head of each page, no witness explains it (35); the nieces' father took a prominent part
# (37); PW-2 business partner of Ajay Kumar, husband of plaintiff no. 1; PW-5 his brother-in-law; third witness died; "The whole of
# the evidence of execution comes from the circle of the beneficiaries" (38); unregistered, no reason shown (40); Issue V against
# the plaintiffs, the Will not proved (44); title not decided (45); appeal allowed, 05.07.2017 judgment set aside, probate refused,
# probate case dismissed (46).
# Not on any card: any finding of forgery (the Court holds the Will NOT PROVED, and does not find incapacity, 30); the F.I.R.'s
# kidnapping account and the names in it (31); the appellants' "habit of forging Wills" line (16.ii); "about 90" / "8 pages" (counsel).
# No section sign anywhere. List lines <= 52 chars. Official patnahighcourt.gov.in portrait on the bench card.
FORMAT = "hook"   # build_course_plan.py: no opening sting, 15-frame lead (the cover), name tag on the "Ravishankar" clip

def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
ENDCARD = {"title": "A thumb mark on every page: is the Will proved?", "line": "Suspicions inherent in the Will must be dispelled by the propounder, even if not pleaded in detail · probate refused", "sub": "LawWorld: legal research for advocates"}

# ── 1 · a thumb mark, not a signature (hook, curiosity, intro) ──────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "thumb"), text="A Will bears a thumb impression, not a signature, at the top of every page. If the objector never pleaded that, can the Court still doubt the Will?", hl="can the Court still doubt the Will?")
cue(type="list", t0=S("c02"), t1=A("c02", "so") - 0.05, head="Probate granted at trial, though…", head_at=S("c02") + 0.05,
    items=[{"n": 1, "text": "The Will: not registered", "at": A("c02", "unregistered")},
           {"n": 2, "text": "PW-2: business partner of a beneficiary's husband", "at": A("c02", "attesting")},
           {"n": 3, "text": "PW-5: that husband's brother-in-law", "at": A("c02", "husband")}])
cue(type="point", t0=A("c02", "so") - 0.05, t1=E("c02") + 0.05, text="So is proving the thumb mark enough?", icon="search", accent=True, at=A("c02", "proving"))
cue(type="bench", t0=S("c03"), t1=E("c03") + 0.05, tag="Patna High Court · 29 October 2026",
    judges=[{"name": "Justice Ramesh Chand Malviya", "photo": "../brand/judges/ramesh_chand_malviya.jpg", "at": A("c03", "honourable")}])

# ── 2 · a widow's bequest ────────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=S("c04"), t1=E("c05") + 0.05, at=A("c04", "widow"), tag="PATNA HIGH COURT · 29.10.2026",
    cases=[{"name": "Shanta Sinha (through LRs) v. Ruma Devi & Anr.", "cite": "First Appeal No. 128 of 2017 · AFR"}])
cue(type="timeline", t0=S("c04"), t1=E("c04") + 0.05,
    nodes=[{"label": "THE WILL", "value": "17.12.1994", "sub": "her property to her two nieces · unregistered", "at": A("c04", "nieces")},
           {"label": "SHE DIES", "value": "20.01.1995", "sub": "about a month after the Will", "tone": "red", "at": A("c04", "died")}])
cue(type="compare", t0=S("c05"), t1=E("c05") + 0.05, head="Probate Case No. 1 of 1995", head_at=S("c05") + 0.05,
    cols=[{"title": "The propounders", "icon": "user", "at": A("c05", "propounders")}, {"title": "The objector", "icon": "user", "at": A("c05", "sister")}],
    rows=[{"cells": ["The widow's two nieces", "Her late husband's sister"], "cells_at": [A("c05", "propounders"), A("c05", "sister")]},
          {"cells": ["Probate of the Will, 17.12.1994", "Denies the Will · then her daughter"], "cells_at": [A("c05", "probate"), A("c05", "daughter")]}])

# ── 3 · probate, then appeal ───────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="timeline", t0=S("c06"), t1=E("c06") + 0.05,
    nodes=[{"label": "TRIAL COURT, BEGUSARAI", "value": "probate granted", "sub": "5 July 2017 · Title Suit No. 2 of 2007", "at": A("c06", "granted")},
           {"label": "THE THUMB MARK", "value": "held to be hers", "sub": "identified by the nieces' father", "at": A("c06", "identified")},
           {"label": "HIGH COURT", "value": "First Appeal", "sub": "by the objector · Section 299", "at": A("c06", "appealed")}])
cue(type="compare", t0=S("c07"), t1=E("c07") + 0.05, head="Before the High Court", head_at=S("c07") + 0.05,
    cols=[{"title": "The objector", "icon": "user", "at": A("c07", "objector")}, {"title": "The propounders", "icon": "user", "at": A("c07", "propounders")}],
    rows=[{"cells": ["Literate, yet a thumb mark", "Never pleaded at the trial"], "cells_at": [A("c07", "thumb"), A("c07", "pleaded")]},
          {"cells": ["Top right of every page · unregistered", "Not to be raised first in appeal"], "cells_at": [A("c07", "position"), A("c07", "trial")]}])

# ── 4 · before the verdict: the LawWorld request ────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c08"), t1=A("c08", "follow") - 0.05, text="The verdict is next. First, a quick request…", icon="scale", accent=True, at=A("c08", "decided"))
cue(type="list", t0=A("c08", "follow") - 0.05, t1=E("c08") + 0.05, head="Follow LawWorld · lawworld.ai", head_at=A("c08", "follow"),
    items=[{"n": 1, "text": "Search SC and High Court judgments, cited to source", "at": A("c08", "india's")},
           {"n": 2, "text": "Draft petitions, plaints and notices with AI", "at": A("c08", "platform")},
           {"n": 3, "text": "Sign up free · ₹200 AI credit included", "at": A("c08", "advocates")}])

# ── 5 · what the Court held ─────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "suspicions") - 0.05, text="What did the High Court decide?", icon="scale", accent=True, at=A("c09", "finally"))
cue(type="point", t0=A("c09", "suspicions") - 0.05, t1=E("c09") + 0.05, text="Section 63 is for the propounder to prove; a suspicion inherent in the Will itself must be dispelled, even if not pleaded “with particularity” (Derek A.C. Lobo, SC)", icon="scale", accent=True, at=A("c09", "dispelled"))
cue(type="list", t0=S("c10"), t1=A("c10", "appeal") - 0.05, head="A proved thumb mark is not a proved Will", head_at=S("c10") + 0.05,
    items=[{"n": 1, "text": "She signed an F.I.R. nine days before the Will", "at": A("c10", "sign")},
           {"n": 2, "text": "Thumb mark at the head of each page, unexplained", "at": A("c10", "thumb")},
           {"n": 3, "text": "All evidence of execution: the beneficiaries' circle", "at": A("c10", "beneficiaries")}])
cue(type="verdicts", t0=A("c10", "appeal") - 0.05, t1=E("c10") + 0.05,
    rows=[{"text": "The objector's First Appeal: allowed", "ok": True, "at": A("c10", "appeal")},
          {"text": "Trial court's judgment of 05.07.2017", "ok": False, "at": A("c10", "allowed"), "strike_at": A("c10", "probate")},
          {"text": "Probate of the Will of 17.12.1994", "ok": False, "at": A("c10", "refused")}])

MUSIC = {"file": "audio/bed_mixkit738_140s.mp3", "target_lufs": -21}   # owner 02-11-2026: trending-style royalty-free bed, audible under the voice
