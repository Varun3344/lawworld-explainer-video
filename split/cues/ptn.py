# Sri Jakkula Dasharatham & Ors. v. Sri Jakkula Balaiah & Ors., C.R.P. No. 6423 of 2012, High Court for the State of Telangana at
# Hyderabad (Vakiti Ramakrishna Reddy J.; reserved 29.07.2026, pronounced 28.10.2026; "Note: LR copy to be marked" under the
# signature): panel cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND).
# HOOK format (split/JUDGMENT_HOOK_FORMAT.md): c01 hook question (spoken to everyone, no "Advocates,"), c02 curiosity, c03 "Hi, I'm
# Ravishankar" + bench, c04 what a protected tenant is, c05-c06 the two rounds before the revenue authorities, c07 both sides, c08 the
# LawWorld request, c09-c10 the verdict.
# Source: the Indian Kanoon text (doc 111779084; the court's own search is captcha-gated, not bypassed). Facts (para): revision under
# s.91 against the Joint Collector, Mahabubnagar (01.09.2012) confirming the RDO, Mahabubnagar (30.03.2010): s.38-E certificates to
# all the legal heirs, Ac. 8.29 gts, Sy. No. 456, Yelikatta village (1); the protected tenant died in 1980-81 leaving five sons and five
# daughters (5); in 2007 the only surviving son applied, claiming exclusive possession; certificate 04.10.2007 (6); sales 13.12.2007
# (Ac. 2.09 gts) and 20.12.2007 (Ac. 6.20 gts) (7); the other heirs' s.90 appeal: set aside and remanded, 04.06.2009 (8); fresh enquiry
# after notice to all the legal heirs; certificate to all "with equal rights in accordance with their respective lineal shares"
# (9); Joint Collector: s.40, all lineal descendants succeed (10). Petitioners: family arrangement, continuous possession; revenue
# authorities cannot decide disputed succession (12, 15, 16). Respondents: s.40 lineal descendants (18, 20); relationship never
# disputed (21). Framework: s.38-E ownership transferred on the notified date 01.01.1973, certificate conclusive evidence; s.40 rights
# heritable (28); the certificate "evidences ownership that has already vested" (33). Held: s.40 (36); heirship not in dispute (43);
# entitlement "flows from Section 40 and not from their possession"; "equal shares as per the lineage" (45); family arrangement and
# sale deeds: no opinion (46, 50); C.R.P. dismissed, orders and the certificate to the legal heirs "with equal shares as per their
# lineage" confirmed (49, 51). Names: only the cause title on the cite card. List lines <= 52 chars.
# Bench photo: brand/judges/vakiti_ramakrishna_reddy.jpg (official portrait, tshc.gov.in sitting-judge profile id 399,
# /images/admin_2025_08_01T18_07_15RAMAKRISHNA REDDY.png, rounded border cropped).
FORMAT = "hook"   # build_course_plan.py: no opening sting, 15-frame lead (the cover), name tag on the "Ravishankar" clip

def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
ENDCARD = {"title": "A protected tenant dies: who gets the certificate?", "line": "All his lineal heirs, in equal shares by lineage, not one son on the strength of possession", "sub": "LawWorld: legal research for advocates"}

# ── 1 · one son, or every heir? (hook, curiosity, intro) ─────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "protected"), text="A protected tenant dies. Does the ownership certificate go to the one son on the land, or to every heir?", hl="or to every heir?")
cue(type="list", t0=S("c02"), t1=A("c02", "so") - 0.05, head="One certificate · many heirs", head_at=S("c02") + 0.05,
    items=[{"n": 1, "text": "The one surviving son gets it alone", "at": A("c02", "surviving")},
           {"n": 2, "text": "He sells the land", "at": A("c02", "sold")},
           {"n": 3, "text": "The other grandchildren object", "at": A("c02", "objected")}])
cue(type="point", t0=A("c02", "so") - 0.05, t1=E("c02") + 0.05, text="Who did the High Court back?", icon="search", accent=True, at=A("c02", "who"))
cue(type="bench", t0=S("c03"), t1=E("c03") + 0.05, tag="Telangana High Court · 28 October 2026",
    judges=[{"name": "Justice Vakiti Ramakrishna Reddy", "photo": "../brand/judges/vakiti_ramakrishna_reddy.jpg", "at": A("c03", "honourable")}])

# ── 2 · the protected tenant ─────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=S("c04"), t1=E("c04") + 0.05, at=A("c04", "protected"), tag="TELANGANA HIGH COURT · 28.10.2026",
    cases=[{"name": "Jakkula Dasharatham & Ors. v. Jakkula Balaiah & Ors.", "cite": "C.R.P. No. 6423 of 2012 · Section 91, Tenancy Act"}])
cue(type="timeline", t0=S("c04"), t1=E("c04") + 0.05,
    nodes=[{"label": "PROTECTED TENANT", "value": "a tenant farmer", "sub": "protected by the Tenancy Act, 1950", "at": A("c04", "farmer")},
           {"label": "SECTION 38-E", "value": "owner from 1.1.1973", "sub": "the certificate: conclusive evidence", "at": A("c04", "section")}])
cue(type="timeline", t0=S("c05"), t1=E("c05") + 0.05,
    nodes=[{"label": "THE TENANT DIES", "value": "1980-81", "sub": "five sons, five daughters", "at": A("c05", "died")},
           {"label": "CERTIFICATE TO ONE SON", "value": "4 Oct 2007", "sub": "the only surviving son", "at": A("c05", "certificate")},
           {"label": "LAND SOLD", "value": "Dec 2007", "sub": "Ac. 8.29 guntas, in two sale deeds", "at": A("c05", "sold")}])
cue(type="flow", t0=S("c06"), t1=E("c06") + 0.05, head="Back to the revenue authorities", head_at=S("c06") + 0.05,
    steps=[{"label": "Appeal: sent back", "sub": "Joint Collector, 4 Jun 2009", "icon": "file-text", "at": A("c06", "appealed")},
           {"label": "RDO: every heir, by lineage", "sub": "fresh enquiry, notice to all · 30 Mar 2010", "icon": "landmark", "at": A("c06", "lineage")},
           {"label": "Joint Collector agrees", "sub": "the son's side's appeal dismissed, 1 Sep 2012", "icon": "check", "tone": "ok", "at": A("c06", "agreed")}])

# ── 3 · the heirs' dispute ───────────────────────────────────────────────────────────────────────────────────────────
cue(type="compare", t0=S("c07"), t1=E("c07") + 0.05, head="Who gets the Section 38-E certificate?", head_at=S("c07") + 0.05,
    cols=[{"title": "The son's side", "icon": "user", "at": A("c07", "son's")}, {"title": "The other heirs", "icon": "scale", "at": A("c07", "other")}],
    rows=[{"cells": ["A family arrangement: the land fell to him", "Section 40: every lineal descendant inherits"], "cells_at": [A("c07", "arrangement"), A("c07", "forty")]},
          {"cells": ["Revenue officers can't decide disputed succession", "Heirship was never disputed"], "cells_at": [A("c07", "land"), A("c07", "descendant")]}])

# ── 4 · before the verdict: the LawWorld request ─────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c08"), t1=A("c08", "follow") - 0.05, text="The verdict is next. First, a quick request…", icon="scale", accent=True, at=A("c08", "decided"))
cue(type="list", t0=A("c08", "follow") - 0.05, t1=E("c08") + 0.05, head="Follow LawWorld · lawworld.ai", head_at=A("c08", "follow"),
    items=[{"n": 1, "text": "Search SC and High Court judgments, cited to source", "at": A("c08", "india's")},
           {"n": 2, "text": "Draft petitions, plaints and notices with AI", "at": A("c08", "platform")},
           {"n": 3, "text": "Sign up free · ₹200 AI credit included", "at": A("c08", "advocates")}])

# ── 5 · what the Court held ──────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "under") - 0.05, text="What did the High Court decide?", icon="scale", accent=True, at=A("c09", "finally"))
cue(type="list", t0=A("c09", "under") - 0.05, t1=E("c09") + 0.05, head="Section 40 · Telangana Tenancy Act", head_at=A("c09", "under"),
    items=[{"n": 1, "text": "A protected tenant's rights are heritable", "at": A("c09", "rights")},
           {"n": 2, "text": "Heirs: his lineal descendants", "at": A("c09", "lineal")},
           {"n": 3, "text": "Equal shares, as per their lineage", "at": A("c09", "equal")}])
cue(type="verdicts", t0=S("c10"), t1=A("c10", "sale") - 0.05,
    rows=[{"text": "One son's claim to the certificate alone", "ok": False, "at": A("c10", "possession"), "strike_at": A("c10", "shut")},
          {"text": "The son's side's revision petition", "ok": False, "at": A("c10", "revision"), "strike_at": A("c10", "dismissed")},
          {"text": "Certificate to all heirs, equal shares by lineage", "ok": True, "at": A("c10", "dismissed")}])
cue(type="point", t0=A("c10", "sale") - 0.05, t1=E("c10") + 0.05, text="Not decided: the sale deeds and the family arrangement, left open to the proper forum", icon="info", accent=True, at=A("c10", "sale"))

MUSIC = {"file": "audio/bed_mixkit738_140s.mp3", "target_lufs": -21}   # owner 02-11-2026: trending-style royalty-free bed, audible under the voice
