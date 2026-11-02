# Km. Vidyawati v. State of U.P. & 4 Ors., Writ-C No. 28051 of 2023, 2026:AHC:221877-DB, Allahabad High Court (Prakash Padia J.,
# Garima Prashad J. wrote it; delivered 26.10.2026, A.F.R.): panel cues, run by split/build_course_plan.py (helpers: at S E cue fx
# have r3 PEND). HOOK format (split/JUDGMENT_HOOK_FORMAT.md): c01 hook question, c02 curiosity, c03 "Hi, I'm Ravishankar" + bench,
# c04-c07 facts / case / both sides, c08 the LawWorld request, c09-c10 the verdict. No title sting.
# Facts from the judgment (paras): rejection under the Mukhyamantri Kisan Evam Sarvahit Bima Yojana communicated by Oriental
# Insurance on 16.04.2021; Rs.5,00,000 sought for her brother's accidental death (2); road accident 18.05.2019; per the petition he
# cultivated the family land and was the head and breadwinner, she unmarried and dependent (3); insurer's letter 03.10.2019: a sister
# is not in the MoU's definition of family; District Committee, Basti, 18.11.2019, on the SDM Harraiya's report: he was the head of
# the family, the insurer to accept the claim and pay (4); rejection maintained 16.04.2021 (5); her case: nominee / legal heir (6);
# the insurer: MoU + policy govern, the family list has no sister, a beneficial object cannot force payment (7); policy period
# 14.09.2018-13.09.2019 (10); accident cover for the head or breadwinner up to Rs.5,00,000 (11); family composition: head or
# breadwinner, spouse, unmarried daughter, dependent son, dependent parents; no sister (12); on death the entire Rs.5.00 lakh to the
# nominee or legal heir (13, 14). Held: the family clause says who is covered, the death-payment clause who receives; it does not
# restrict a legal heir to the family list (15); the insurer's reading adds words (16); Uma Devi, (2021) 1 ILR (All) 314 (17);
# no rival heir (22, 23); wrong clause applied, "That error vitiates the rejection" (24); an unmarried sister is not disqualified,
# entitled as legal heir; the cover itself not enlarged (25); writ allowed, rejection quashed, Rs.5,00,000 within four weeks of a
# certified copy, DM Basti to facilitate, no costs (26).
# Private persons: the deceased and the claimant are never named on a card (only the cause title on the cite bar).
# No section sign anywhere. List lines <= 52 chars. Official allahabadhighcourt.in portrait for Justice Prakash Padia.
# PHOTO GAP (02-11-2026): no official portrait of Justice Garima Prashad exists online (her allahabadhighcourt.in profile, id 402,
# has an empty photo slot; the Shravasti district court site shows "No Image"). brand/judges/garima_prashad.jpg is NOT on disk:
# supply an official photo there before any render (the 330 x 420 frame would be blank).
FORMAT = "hook"   # build_course_plan.py: no opening sting, 15-frame lead (the cover), name tag on the "Ravishankar" clip

def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
ENDCARD = {"title": "Can an insurer refuse a farmer's sister?", "line": "Not listed as family, still paid as legal heir · the death benefit goes to the nominee or legal heir", "sub": "LawWorld: legal research for advocates"}

# ── 1 · the sister's claim (hook, curiosity, intro) ─────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "insurance"), text="Can an insurer refuse a farmer's accident death claim, just because the claimant is his sister?", hl="just because the claimant is his sister?")
cue(type="list", t0=S("c02"), t1=A("c02", "sister") - 0.05, head="“Family” under the scheme", head_at=S("c02") + 0.05,
    items=[{"n": 1, "text": "The head or breadwinner, and the spouse", "at": A("c02", "spouse")},
           {"n": 2, "text": "An unmarried daughter · a dependent son", "at": A("c02", "daughter")},
           {"n": 3, "text": "Dependent parents", "at": A("c02", "parents")}])
cue(type="point", t0=A("c02", "sister") - 0.05, t1=E("c02") + 0.05, text="No sister on the list. So does she get nothing?", icon="search", accent=True, at=A("c02", "list"))
cue(type="bench", t0=S("c03"), t1=E("c03") + 0.05, tag="Allahabad High Court · 26 October 2026",
    judges=[{"name": "Justice Prakash Padia", "photo": "../brand/judges/prakash_padia.jpg", "at": A("c03", "honourable")},
            {"name": "Justice Garima Prashad", "photo": "../brand/judges/garima_prashad.jpg", "at": A("c03", "honourable", 2)}])

# ── 2 · the accident claim ──────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c04"), t1=E("c04") + 0.05, head="Mukhyamantri Kisan Evam Sarvahit Bima Yojana", head_at=S("c04") + 0.05,
    steps=[{"label": "A farmer, head of the family", "sub": "the breadwinner, as the Committee found", "icon": "user", "at": A("c04", "farmer")},
           {"label": "Road accident", "sub": "18 May 2019 · inside the policy year", "icon": "calendar", "at": A("c04", "accident")},
           {"label": "Insured for ₹5 lakh", "sub": "personal accident cover", "icon": "file-check", "at": A("c04", "insured")}])
cue(type="cite", t0=S("c05"), t1=E("c06") + 0.05, at=A("c05", "unmarried"), tag="HIGH COURT OF JUDICATURE AT ALLAHABAD · 26.10.2026",
    cases=[{"name": "Km. Vidyawati v. State of U.P. & 4 Ors.", "cite": "2026:AHC:221877-DB · Writ-C No. 28051 of 2023"}])
cue(type="timeline", t0=S("c05"), t1=E("c05") + 0.05,
    nodes=[{"label": "THE CLAIM", "value": "his sister", "sub": "unmarried · ₹5 lakh under the scheme", "at": A("c05", "claimed")},
           {"label": "ORIENTAL INSURANCE", "value": "rejected", "sub": "letter of 3 October 2019", "tone": "stop", "at": A("c05", "rejected")},
           {"label": "THE REASON", "value": "not “family”", "sub": "a sister is not in the MoU's list", "at": A("c05", "definition")}])

# ── 3 · the insurer's stand ─────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="timeline", t0=S("c06"), t1=E("c06") + 0.05,
    nodes=[{"label": "DISTRICT COMMITTEE", "value": "head of family", "sub": "Basti, 18.11.2019 · on the SDM's report", "at": A("c06", "found")},
           {"label": "THE DIRECTION", "value": "accept and pay", "sub": "to the insurer", "at": A("c06", "directed")},
           {"label": "THE INSURER", "value": "refused again", "sub": "16 April 2021 · rejection maintained", "tone": "stop", "at": A("c06", "refused")}])
cue(type="compare", t0=S("c07"), t1=E("c07") + 0.05, head="In the High Court", head_at=S("c07") + 0.05,
    cols=[{"title": "The insurer", "icon": "landmark", "at": A("c07", "insurer")}, {"title": "The sister", "icon": "user", "at": A("c07", "she")}],
    rows=[{"cells": ["The MoU's family list has no sister", "She claims as his legal heir"], "cells_at": [A("c07", "covered"), A("c07", "claimed")]},
          {"cells": ["A beneficial aim cannot stretch the policy", "The scheme pays the nominee or legal heir"], "cells_at": [A("c07", "beneficial"), A("c07", "heir")]}])

# ── 4 · before the verdict: the LawWorld request ────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c08"), t1=A("c08", "follow") - 0.05, text="The verdict is next. First, a quick request…", icon="scale", accent=True, at=A("c08", "decided"))
cue(type="list", t0=A("c08", "follow") - 0.05, t1=E("c08") + 0.05, head="Follow LawWorld · lawworld.ai", head_at=A("c08", "follow"),
    items=[{"n": 1, "text": "Search SC and High Court judgments, cited to source", "at": A("c08", "india's")},
           {"n": 2, "text": "Draft petitions, plaints and notices with AI", "at": A("c08", "platform")},
           {"n": 3, "text": "Sign up free · ₹200 AI credit included", "at": A("c08", "advocates")}])

# ── 5 · what the Court held ─────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "family") - 0.05, text="What did the High Court decide?", icon="scale", accent=True, at=A("c09", "finally"))
cue(type="list", t0=A("c09", "family") - 0.05, t1=E("c09") + 0.05, head="Two different clauses", head_at=A("c09", "family"),
    items=[{"n": 1, "text": "Family list: whose own accident is insured", "at": A("c09", "accident")},
           {"n": 2, "text": "Death benefit: the nominee or legal heir", "at": A("c09", "death")},
           {"n": 3, "text": "The list does not limit who is a legal heir", "at": A("c09", "heir")}])
cue(type="point", t0=S("c10"), t1=A("c10", "rejection") - 0.05, text="The family clause was applied to a death claim: “That error vitiates the rejection”", icon="scale", accent=True, at=A("c10", "wrong"))
cue(type="verdicts", t0=A("c10", "rejection") - 0.05, t1=E("c10") + 0.05,
    rows=[{"text": "The insurer's rejection of 16.04.2021: quashed", "ok": False, "at": A("c10", "quashed")},
          {"text": "₹5,00,000 to the sister as legal heir, within four weeks", "ok": True, "at": A("c10", "pay")},
          {"text": "District Magistrate, Basti, to facilitate payment", "ok": True, "at": A("c10", "weeks")}])
