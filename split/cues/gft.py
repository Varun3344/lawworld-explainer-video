# Lourde Marie Dhambarane & Anr. v. S. Santhi, C.R.P. No. 1196 of 2022, 2026:MHC:4366, High Court of Judicature at Madras
# (N. Anand Venkatesh J.; reserved 27.10.2026, delivered 29.10.2026; listed as Reportable in the court's judis database): panel cues,
# run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND).
# HOOK format (split/JUDGMENT_HOOK_FORMAT.md): c01 hook question (spoken to everyone, no "Advocates,"), c02 curiosity, c03 "Hi, I'm
# Ravishankar" + bench, c04-c06 the eviction, the settlement deed and sale, her suit, c07 both sides, c08 the LawWorld request,
# c09-c10 the verdict.
# Facts (para): strike off the plaint in O.S. 756/2020, Principal District Munsif Court, Puducherry, under Article 227 (prayer, 1);
# injunction suit on a sale deed of 27.1.2012 (4); ejectment suit O.S. 945/1982, decreed 11.11.1983, restored by this Court
# 18.8.2000, confirmed by the Supreme Court 23.11.2005 with time to vacate till 31.8.2006 (5(a)); settlement deed 10.8.2001 by the
# tenant and his wife to their son, two sale deeds by the son; the District Registrar cancelled the plaintiff's sale deed 11.12.2015
# (5(b)); her W.P. 5723/2014 dismissed 05.01.2016 (5(c)); the other buyer's W.P. 12168/2014 dismissed 21.4.2023 (5(e), (f));
# defendants: concealment, abuse of process (6); plaintiff: P. Suresh v. D. Kalaivani, 2026 (7) SCC 644 - no Article 227 petition to
# strike off a plaint (7); P. Suresh: Article 227 "an exceptional resort" where Order VII Rule 11 is available (8, 9). Held: "a text
# book case" (10); concealment of the earlier proceedings, "abuse of process of court and used the Court to perpetuate illegality"
# (11); "a clear abuse of process of court and a re-litigation, which are not grounds that can be raised under Order VII Rule 11 of
# the CPC"; Article 227 exercised "to prevent further miscarriage of justice" (12); same property (13-15); C.R.P. allowed, suit struck
# off the register, no costs (16). Names: only the cause title on the cite card. Not on any card: the Tahsildar's "fraud" finding
# (5(c)), the contempt remark (11). List lines <= 52 chars. No section sign anywhere.
# Bench photo: brand/judges/n_anand_venkatesh.jpg (official Madras HC portrait, hcmadras.tn.gov.in/present_judges.php,
# admin/view_image.php img_id NTI= (52), alt "Hon'ble Mr.Justice N. Anand Venkatesh"; CMYK converted to RGB).
FORMAT = "hook"   # build_course_plan.py: no opening sting, 15-frame lead (the cover), name tag on the "Ravishankar" clip

def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
ENDCARD = {"title": "A buyer from the tenant's son sues: thrown out?", "line": "Yes, on these facts: a clear abuse of process and re-litigation, so the High Court struck the suit off under Article 227", "sub": "LawWorld: legal research for advocates"}

# ── 1 · thrown out at once? (hook, curiosity, intro) ────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "tenant"), text="Eviction upheld by the Supreme Court, then a buyer from the tenant's son sues. Can the High Court throw that suit out itself?", hl="throw that suit out itself?")
cue(type="list", t0=S("c02"), t1=A("c02", "so") - 0.05, head="Over twenty years on · one question", head_at=S("c02") + 0.05,
    items=[{"n": 1, "text": "The owner won in the Supreme Court in 2005", "at": A("c02", "owner")},
           {"n": 2, "text": "His family is still in court in 2026", "at": A("c02", "family")},
           {"n": 3, "text": "Usual remedy: Order VII Rule 11, trial court", "at": A("c02", "usual")}])
cue(type="point", t0=A("c02", "so") - 0.05, t1=E("c02") + 0.05, text="Can the High Court step in directly?", icon="search", accent=True, at=A("c02", "directly"))
cue(type="bench", t0=S("c03"), t1=E("c03") + 0.05, tag="Madras High Court · 29 October 2026",
    judges=[{"name": "Justice N. Anand Venkatesh", "photo": "../brand/judges/n_anand_venkatesh.jpg", "at": A("c03", "honourable")}])

# ── 2 · signed over, then sold ───────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=S("c04"), t1=E("c04") + 0.05, at=A("c04", "owner"), tag="HIGH COURT OF MADRAS · 29.10.2026",
    cases=[{"name": "Lourde Marie Dhambarane & Anr. v. S. Santhi", "cite": "2026:MHC:4366 · C.R.P. No. 1196 of 2022"}])
cue(type="timeline", t0=S("c04"), t1=E("c04") + 0.05,
    nodes=[{"label": "EVICTION SUIT · 1982", "value": "Owner v. tenant", "sub": "decreed 11 Nov 1983", "at": A("c04", "evict")},
           {"label": "SUPREME COURT · 2005", "value": "Eviction upheld", "sub": "time to vacate till 31 Aug 2006", "at": A("c04", "upheld")}])
cue(type="timeline", t0=S("c05"), t1=E("c05") + 0.05,
    nodes=[{"label": "SETTLEMENT DEED · 10.08.2001", "value": "To the tenant's son", "sub": "by the tenant and his wife", "at": A("c05", "settlement")},
           {"label": "SALE DEED · 27.01.2012", "value": "Son sells to her", "sub": "one of two sale deeds he made", "at": A("c05", "sold")}])
cue(type="timeline", t0=S("c06"), t1=E("c06") + 0.05,
    nodes=[{"label": "DISTRICT REGISTRAR", "value": "Sale deed cancelled", "sub": "11 Dec 2015", "tone": "red", "at": A("c06", "cancelled")},
           {"label": "HER WRIT PETITION", "value": "Dismissed", "sub": "5 Jan 2016", "tone": "red", "at": A("c06", "failed")},
           {"label": "HER SUIT · 2020", "value": "Injunction", "sub": "O.S. 756/2020, Puducherry", "at": A("c06", "injunction")}])

# ── 3 · the arguments ────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="compare", t0=S("c07"), t1=E("c07") + 0.05, head="Strike off the suit under Article 227?", head_at=S("c07") + 0.05,
    cols=[{"title": "The defendants", "icon": "landmark", "at": A("c07", "defendants")}, {"title": "The buyer (plaintiff)", "icon": "user", "at": A("c07", "citing")}],
    rows=[{"cells": ["An abuse of process", "P. Suresh v. D. Kalaivani (SC, 2026)"], "cells_at": [A("c07", "abuse"), A("c07", "supreme")]},
          {"cells": ["The suit hid the earlier cases", "Article 227 can't strike off a plaint"], "cells_at": [A("c07", "hid"), A("c07", "strike")]}])

# ── 4 · before the verdict: the LawWorld request ─────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c08"), t1=A("c08", "follow") - 0.05, text="The verdict is next. First, a quick request…", icon="scale", accent=True, at=A("c08", "decided"))
cue(type="list", t0=A("c08", "follow") - 0.05, t1=E("c08") + 0.05, head="Follow LawWorld · lawworld.ai", head_at=A("c08", "follow"),
    items=[{"n": 1, "text": "Search SC and High Court judgments, cited to source", "at": A("c08", "india's")},
           {"n": 2, "text": "Draft petitions, plaints and notices with AI", "at": A("c08", "platform")},
           {"n": 3, "text": "Sign up free · ₹200 AI credit included", "at": A("c08", "advocates")}])

# ── 5 · what the Court held ──────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "abuse") - 0.05, text="What did the High Court decide?", icon="scale", accent=True, at=A("c09", "finally"))
cue(type="point", t0=A("c09", "abuse") - 0.05, t1=E("c09") + 0.05, text="“…a clear abuse of process of court and a re-litigation, which are not grounds that can be raised under Order VII Rule 11 of the CPC.”", icon="quote", accent=True, at=A("c09", "abuse"))
cue(type="point", t0=S("c10"), t1=A("c10", "revision") - 0.05, text="“… has indulged in abuse of process of court and used the Court to perpetuate illegality.”", icon="quote", accent=True, at=A("c10", "hid"))
cue(type="verdicts", t0=A("c10", "revision") - 0.05, t1=E("c10") + 0.05,
    rows=[{"text": "Revision petition allowed under Article 227", "ok": True, "at": A("c10", "revision")},
          {"text": "Her suit, O.S. 756 of 2020, struck off the register", "ok": False, "at": A("c10", "struck")},
          {"text": "No costs · connected petitions closed", "ok": True, "at": A("c10", "register")}])

MUSIC = {"file": "audio/bed_mixkit738_140s.mp3", "target_lufs": -21}   # owner 02-11-2026: trending-style royalty-free bed, audible under the voice
# Fact-check 04-11-2026: c02 head "Twenty" -> "Over twenty years on" (2005 to 2026); ENDCARD line tied to this suit ("on these facts", para 12).

# 05-11-2026 QA: the end-card line (166 chars) was clipped at both edges; shortened to 120 chars.
