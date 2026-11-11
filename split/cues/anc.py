# J. Rajesh (Minor) thr. his mother and natural guardian J. Gomathi v. M. Kumaran (Dead) thr. LRs. & Ors., 2026 INSC 1208, Civil Appeal
# No. 7020 of 2012, Supreme Court of India (Sunita Agarwal J. wrote it, Augustine George Masih J.; pronounced 06.11.2026, REPORTABLE):
# panel cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND). HOOK format (split/JUDGMENT_HOOK_FORMAT.md):
# c01 hook question (spoken to everyone, no "Advocates,"), c02 curiosity, c03 "Hi, I'm Ravishankar" + bench, c04-c05 the family
# timeline, c06 the courts below, c07 both sides, c08 the LawWorld request, c09-c10 the verdict. DRAFT 11-11-2026, awaiting the owner's yes.
# Facts (para): minor son's suit O.S. 1698 of 1997 through his mother, partition + half share of 1,811 sq. ft. (2, 37); pleaded as the
# late grandfather's joint family property (2); the father's sister's partition suit C.S. 1728 of 1993, compromise decree 03.02.1994,
# the father's share 1,811 sq. ft. (3, 35); sale deeds 03.04.1997 and 17.04.1997 to D2, D3 (4); no challenge to the decree or the sale
# deeds (4, 40); City Civil Court, Chennai: preliminary decree of partition (6) for the half share (19, 21); buyers' first appeal: the
# High Court set it aside, 11.08.2010 (6, 7, 13, 21) - Section 8: the son of a male dying intestate is absolute owner, his son has no
# right by birth (9-13); son born 06.01.1994, while the 1993 suit was pending (8, 17, 37); the grandfather died intestate, date not
# disclosed (35, 39). Son: coparcener by birth, Section 29-A (TN Amendment 1989), decree after his birth, father could not transfer
# the whole without demarcating his share (14-21). Buyers: Section 8, grandson not a Class I heir, divided son absolute owner, decree
# unchallenged, father alive (22-25). Held: son's son not a Class I heir, old right by birth not saved (34); devolved on Class I heirs
# under Section 8, not HUF of the son's branch incl. the grandson; each heir exclusive owner under the 1994 decree; coparcenary did not
# continue (35); succession opened before his birth (36); Chander Sen quoted on the c09 card verbatim (38); Sections 6 / 29-A no
# application, not a "surviving coparcener" (39); the father's share "cannot be said to be coparcenary", no infirmity (41); appeal
# dismissed, no order as to costs (42).
# Names: only the cause title on the cite card; no private name in speech. Not a sweeping "sons never get ancestral property" anywhere:
# the rule is shown with its condition (devolved under Section 8) and the case facts (1994 partition, born after the succession opened).
# List lines <= 52 chars. Bench photos: brand/judges/augustine_george_masih.jpg, brand/judges/sunita_agarwal.jpg (official sci.gov.in).
FORMAT = "hook"   # build_course_plan.py: no opening sting, 15-frame lead (the cover), name tag on the "Ravishankar" clip

def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
ENDCARD = {"title": "Ancestral property: can a son claim half?", "line": "Here, inherited under Section 8 and partitioned in 1994: the father's own, not coparcenary", "sub": "LawWorld: legal research for advocates"}

# ── 1 · ancestral property? (hook, curiosity, intro) ─────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "your"), text="Grandfather's property came to your father. Can you, his son, sue for half while he is alive?", hl="sue for half while he is alive?")
cue(type="flow", t0=S("c02"), t1=A("c02", "who") - 0.05, head="One plot, two answers", head_at=S("c02") + 0.05,
    steps=[{"label": "Trial court: yes", "sub": "a half share decreed for the son", "icon": "scale", "at": A("c02", "trial")},
           {"label": "High Court: no", "sub": "the decree set aside on appeal", "icon": "landmark", "at": A("c02", "reversed")},
           {"label": "Supreme Court", "sub": "29 years after the suit was filed", "icon": "gavel", "at": A("c02", "nearly")}])
cue(type="point", t0=A("c02", "who") - 0.05, t1=E("c02") + 0.05, text="Who was right?", icon="search", accent=True, at=A("c02", "who"))
cue(type="bench", t0=S("c03"), t1=E("c03") + 0.05, tag="Supreme Court of India · 6 November 2026",
    judges=[{"name": "Justice Augustine George Masih", "photo": "../brand/judges/augustine_george_masih.jpg", "at": A("c03", "honourable")},
            {"name": "Justice Sunita Agarwal", "photo": "../brand/judges/sunita_agarwal.jpg", "at": A("c03", "honourable", 2)}])

# ── 2 · a grandfather's plot ─────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=S("c04"), t1=E("c04") + 0.05, at=A("c04", "grandfather"), tag="SUPREME COURT OF INDIA · 06.11.2026",
    cases=[{"name": "J. Rajesh (Minor) thr. his mother and natural guardian J. Gomathi v. M. Kumaran (Dead) thr. LRs. & Ors.", "cite": "2026 INSC 1208 · Civil Appeal No. 7020 of 2012"}])
cue(type="timeline", t0=S("c04"), t1=E("c04") + 0.05,
    nodes=[{"label": "THE GRANDFATHER", "value": "no will", "sub": "died intestate · date not disclosed", "at": A("c04", "died")},
           {"label": "1993 · HIS DAUGHTER", "value": "partition suit", "sub": "to divide his property among the heirs", "at": A("c04", "daughter")},
           {"label": "6 JANUARY 1994", "value": "grandson born", "sub": "while that suit was pending", "at": A("c04", "grandson")}])
cue(type="timeline", t0=S("c05"), t1=E("c05") + 0.05,
    nodes=[{"label": "3 FEBRUARY 1994", "value": "compromise decree", "sub": "the father's share: 1,811 sq. ft. of land", "at": A("c05", "compromise")},
           {"label": "APRIL 1997", "value": "plot sold", "sub": "two sale deeds · 3 and 17 April 1997", "at": A("c05", "sold")}])

# ── 3 · by birth, or by Section 8? ──────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c06"), t1=E("c06") + 0.05, head="The son's suit, 1997", head_at=S("c06") + 0.05,
    steps=[{"label": "Partition, half share", "sub": "sued through his mother, as a minor", "icon": "file-pen", "at": A("c06", "sued")},
           {"label": "City Civil Court, Chennai", "sub": "preliminary decree of partition", "icon": "scale", "at": A("c06", "chennai")},
           {"label": "High Court, 11 August 2010", "sub": "father the absolute owner · decree set aside", "icon": "landmark", "at": A("c06", "absolute")}])
cue(type="compare", t0=S("c07"), t1=E("c07") + 0.05, head="Coparcener by birth, or Class I heir?", head_at=S("c07") + 0.05,
    cols=[{"title": "The son", "icon": "scale", "at": A("c07", "son")}, {"title": "The buyers", "icon": "landmark", "at": A("c07", "buyers")}],
    rows=[{"cells": ["Coparcener by birth · Section 29-A (TN)", "Section 8: a grandson is not a Class I heir"], "cells_at": [A("c07", "coparcener"), A("c07", "said", 2)]},
          {"cells": ["Born before the 3 Feb 1994 decree", "The divided son is the absolute owner"], "cells_at": [A("c07", "decree"), A("c07", "grandson")]},
          {"cells": ["Father could not sell the son's share", "The 1994 decree was never challenged"], "cells_at": [A("c07", "sell"), A("c07", "class")]}])

# ── 4 · before the verdict: the LawWorld request ─────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c08"), t1=A("c08", "follow") - 0.05, text="The verdict is next. First, a quick request…", icon="scale", accent=True, at=A("c08", "decided"))
cue(type="list", t0=A("c08", "follow") - 0.05, t1=E("c08") + 0.05, head="Follow LawWorld · lawworld.ai", head_at=A("c08", "follow"),
    items=[{"n": 1, "text": "Search SC and High Court judgments, cited to source", "at": A("c08", "india's")},
           {"n": 2, "text": "Draft petitions, plaints and notices with AI", "at": A("c08", "platform")},
           {"n": 3, "text": "Sign up free · ₹200 AI credit included", "at": A("c08", "advocates")}])

# ── 5 · what the Court held ──────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "what", 2) - 0.05, text="What did the Supreme Court decide?", icon="scale", accent=True, at=A("c09", "finally"))
cue(type="point", t0=A("c09", "what", 2) - 0.05, t1=E("c09") + 0.05, text="“It would be difficult to hold that the property which devolved on a Hindu under Section 8 of the Hindu Succession Act would be HUF in his hand vis-à-vis his own son”", icon="quote", accent=True, at=A("c09", "what", 2))
cue(type="list", t0=S("c10"), t1=A("c10", "so") - 0.05, head="Applied to this family", head_at=S("c10") + 0.05,
    items=[{"n": 1, "text": "1994 decree: each heir an exclusive owner", "at": A("c10", "partition")},
           {"n": 2, "text": "Father's share: “cannot be said to be coparcenary”", "at": A("c10", "exclusive")},
           {"n": 3, "text": "Grandfather died before the son was born", "at": A("c10", "grandfather")}])
cue(type="verdicts", t0=A("c10", "so") - 0.05, t1=E("c10") + 0.05,
    rows=[{"text": "Half share as a coparcener by birth", "ok": False, "at": A("c10", "claim")},
          {"text": "Section 6 / Section 29-A (TN): no application", "ok": False, "at": A("c10", "share", 2)},
          {"text": "High Court upheld · appeal dismissed", "ok": True, "at": A("c10", "dismissed")}])

MUSIC = {"file": "audio/bed_mixkit738_140s.mp3", "target_lufs": -21}   # owner 02-11-2026: trending-style royalty-free bed, audible under the voice
