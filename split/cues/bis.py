# Bureau of Indian Standards v. M/s Mars Veneers and Boards & Ors., Crl.A. No. 1211 of 2013, 2026:KER:79827 (High Court of Kerala,
# A. Badharudeen J.; heard 24.09.2026, delivered 14.10.2026, "CR"): panel cues, run by split/build_course_plan.py (helpers: at S E cue fx
# have r3 PEND). Concept format as set krm.
# Facts from the judgment (paras): appeal by the BIS (complainant), arising from Crl.L.P. No. 45 of 2013, against the judgment of
# 01.01.2010 of the JFCM, Taliparamba in C.C. No. 923 of 2006 (cause title, 1); complaint under ss.11(1), 12(b) r/w s.33 BIS Act, 1986:
# the BIS Joint Director, Thiruvananthapuram, with three other officials inspected the factory, found the first accused (the partnership
# firm) possessing a roller with a spurious ISI mark without a valid BIS licence; a spurious ISI mark also on the factory wall; the firm
# (A1) and its partners (A2-A5) arrayed (4); PW1-3, Exts.P1-P6, MO1 roller (5); the Magistrate: no cogent and believable evidence that the
# firm used a trade mark or ISI mark on any article, no finished product with the fake mark produced, MO1's seizure not properly proved
# to show it in working condition and capable of applying the mark; all acquitted (5); BIS: mere possession of a spurious ISI mark
# suffices, the Magistrate wrongly required proof of use (6); the accused: mere possession for affixing on goods does not attract ss.11
# and 12 r/w 33 (7); s.11, s.12, s.33 extracted (9); held: "the legislature vigilantly incorporated the word 'used'" and "never intended
# the word 'possess' to fasten criminal culpability on mere possession of a spurious ISI mark"; no goods bearing the fake mark detected,
# seized or produced; "mere possession of an object capable of affixing such a mark, without any evidence to establish its use in the
# manufacture of goods, does not attract" ss.11 and 12 r/w 33; the Magistrate right (10); appeal dismissed, acquittal confirmed (11-12).
# The bench card uses the official portrait.
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen, as tej)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
STING = {"kicker": "KERALA HIGH COURT · JUDGMENT EXPLAINED", "title": "A fake ISI mark: possession is not use", "sub": "BIS v. M/s Mars Veneers and Boards · 2026:KER:79827"}
ENDCARD = {"title": "A fake ISI mark: possession is not use", "line": "No proof of use: Sections 11 and 12 r/w 33 not attracted", "sub": "LawWorld: legal research for advocates"}

# ── 1 · possession or use? ───────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "factory"), text="A roller with a fake ISI mark, no proof of use: is possession an offence?", hl="is possession an offence?")
cue(type="bench", t0=S("c02"), t1=E("c02") + 0.05, tag="High Court of Kerala · 14 October 2026",
    judges=[{"name": "Justice A. Badharudeen", "photo": "../brand/judges/a_badharudeen.jpg", "at": A("c02", "honourable")}])

# ── 2 · the case ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=A("c03", "bureau"), t1=E("c04") + 0.05, at=A("c03", "bureau"), tag="HIGH COURT OF KERALA · 14.10.2026",
    cases=[{"name": "Bureau of Indian Standards v. M/s Mars Veneers and Boards", "cite": "2026:KER:79827 · Crl.A. No. 1211 of 2013"}])
cue(type="flow", t0=S("c03"), t1=E("c03") + 0.05, head="The inspection, as alleged", head_at=S("c03") + 0.05,
    steps=[{"label": "BIS officials inspect", "sub": "the Joint Director, Thiruvananthapuram, and 3 officials", "icon": "search", "at": A("c03", "officials")},
           {"label": "A roller with a spurious ISI mark", "sub": "MO1 · held by the partnership firm", "icon": "file-text", "at": A("c03", "roller")},
           {"label": "No valid BIS licence", "sub": "to have and hold the ISI mark", "icon": "x", "at": A("c03", "licence")}])
cue(type="flow", t0=S("c04"), t1=E("c04") + 0.05, head="The complaint", head_at=S("c04") + 0.05,
    steps=[{"label": "A spurious ISI mark on the wall", "sub": "of the factory, also alleged", "icon": "search", "at": A("c04", "wall")},
           {"label": "The firm and its 4 partners", "sub": "arrayed as accused 1 to 5", "icon": "user", "at": A("c04", "partners")},
           {"label": "BIS Act, 1986", "sub": "§ 11(1), § 12(b) r/w § 33 · C.C. No. 923 of 2006", "icon": "scale", "at": A("c04", "act")}])

# ── 3 · in the trial court ───────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="list", t0=S("c05"), t1=E("c05") + 0.05, head="Taliparamba Magistrate", head_at=S("c05") + 0.05,
    items=[{"n": 1, "text": "No cogent proof the firm used the mark on any article", "at": A("c05", "cogent")},
           {"n": 2, "text": "No finished product with the fake mark produced", "at": A("c05", "finished")}])
cue(type="flow", t0=S("c06"), t1=E("c06") + 0.05, head="The roller (MO1)", head_at=S("c06") + 0.05,
    steps=[{"label": "Seizure not properly proved", "sub": "beyond reasonable doubt", "icon": "x", "tone": "stop", "at": A("c06", "seizure")},
           {"label": "Working, able to apply the mark?", "sub": "not shown", "icon": "x", "tone": "stop", "at": A("c06", "worked")},
           {"label": "All accused acquitted", "sub": "judgment of 1 Jan 2010", "icon": "check", "tone": "ok", "at": A("c06", "acquitted")}])

# ── 4 · the appeal ───────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="compare", t0=S("c07"), t1=E("c07") + 0.05, head="On appeal: is possession enough?", head_at=A("c07", "appeal"),
    cols=[{"title": "The Bureau argued", "icon": "landmark", "at": A("c07", "bureau")}, {"title": "The firm replied", "icon": "user", "at": A("c07", "firm")}],
    rows=[{"cells": ["Mere possession of a spurious ISI mark is enough", "Mere possession is no offence"], "cells_at": [A("c07", "possession"), A("c07", "possession", 2)]},
          {"cells": ["No need to prove use", "§§ 11 and 12 r/w § 33 not attracted"], "cells_at": [A("c07", "without"), A("c07", "offence")]}])

# ── 5 · what the court held ──────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c08"), t1=E("c08") + 0.05, at=A("c08", "high"), act="BIS ACT, 1986", num="11 & 12", title="Both prohibit the use of the mark",
    points=[{"text": "§ 11(1): no use of the Standard Mark, except under a licence", "at": A("c08", "eleven")},
            {"text": "§ 12(b): no use of an “Indian Standard” mark without permission", "at": A("c08", "twelve")}],
    note={"text": "The legislature chose “use”, never “possess”", "icon": "x", "at": A("c08", "legislature")})
cue(type="notequal", t0=S("c09"), t1=A("c09", "bureau") - 0.05, left="Possession", right="Use",
    at=A("c09", "possessing"), left_at=A("c09", "possessing"), sub="An object able to affix the mark, no evidence of its use: §§ 11, 12 not attracted", sub_at=A("c09", "attract"))
cue(type="verdicts", t0=A("c09", "bureau"), t1=E("c09") + 0.05,
    rows=[{"text": "Bureau's appeal dismissed", "ok": True, "at": A("c09", "bureau")},
          {"text": "Acquittal of all accused confirmed", "ok": True, "at": A("c09", "dismissed")}])
cue(type="point", t0=S("c10"), t1=E("c10") + 0.05, text="Like · Share · Subscribe · lawworld.ai", icon="check", accent=True, at=A("c10", "like"))
