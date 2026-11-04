# Bandari Ramchander & Ors. v. Maitri Coop. Housing Society Ltd. & Ors., 2026 INSC 1175, Civil Appeal No. 10699 of 2013 with connected
# appeals (M.M. Sundresh J. wrote it, Satish Chandra Sharma J.; decided 29.10.2026, Reportable): panel cues, run by
# split/build_course_plan.py (helpers: at S E cue fx have r3 PEND).
# HOOK format (split/JUDGMENT_HOOK_FORMAT.md): c01 hook question (spoken to everyone, no "Advocates,"), c02 curiosity, c03 "Hi, I'm
# Ravishankar" + bench, c04-c05 firman to abolition, c06-c07 rival claims, c08 the LawWorld request, c09-c10 the verdict.
# Facts from the judgment (paras): High Court of A.P. common judgment 16.04.2003 (1); Survey Nos. 100 and 101, Village Miyapur,
# Serilingamapally Mandal, Ranga Reddy District, Telangana (4); individuals and societies claim through "three different sources";
# Special Court under the A.P. Land Grabbing (Prohibition) Act, 1982 (5); 550 acres and 39 guntas; 1912 survey: Sarkari poramboke (9);
# Reilly Commission report 30.04.1927 (10); Firman Isfandar 1338 Fasli, issued 1929: jagirs to the present heirs (11); no sale,
# mortgage or gift without the Nizam's sanction (12); Abolition of Jagirs Regulation 1358-Fasli from 15.08.1949; administration to the
# State of Hyderabad from 15.09.1949 (13); one woman's name inserted as pattedar in the pahanies of 1950-51 to 1952-53, against
# "Poramboke" / "Sarkari" in columns 11-12 (14); LGC 110/1994, 131/1995, 136/1995 (judgments 31.12.1997): the State the rightful
# owner (6, 23); the High Court, 16.04.2003: the State the rightful owner (24); the appellants on the firman, the jagirdar's status,
# the pahanies, revenue records and adverse possession (38-40); the State: vested under Regulation 5, commutation received (41-43);
# a jagir = the right in respect of land revenue; "a grant of jagir is not to be misconstrued as one of title over the property" (26);
# "a jagirdar is not a title holder" (29); the limited rights "statutorily removed" (45); the entries "constitute an act of nullity"
# (49); "There is absolutely no power to record the name of an individual as a pattedar, through a mere entry, sans any proceedings"
# (52); "the title of the State is clearly established" (58); appeals dismissed (60, 64); no costs (65).
# Not on any card: any person's name except the cause title on the cite bar; the "land grabbers" label and the fraud finding (23, 51,
# 58). No section sign anywhere. List lines <= 52 chars. Official sci.gov.in portraits on the bench card.
FORMAT = "hook"   # build_course_plan.py: no opening sting, 15-frame lead (the cover), name tag on the "Ravishankar" clip

def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
ENDCARD = {"title": "Does a jagir grant make you the owner?", "line": "No: a jagir is a right over land revenue, not title. The Miyapur lands belong to the State", "sub": "LawWorld: legal research for advocates"}

# ── 1 · does a jagir make you owner? (hook, curiosity, intro) ──────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "ruler"), text="A ruler granted a family a whole village as a jagir. Does the family own that land today?", hl="Does the family own that land today?")
cue(type="counters", t0=S("c02"), t1=A("c02", "who") - 0.05, head="Survey Nos. 100 and 101 · Miyapur", head_at=S("c02") + 0.05,
    items=[{"value": 550, "unit": "ACRES", "label": "The lands in dispute", "sub": "plus 39 guntas, in Telangana", "at": A("c02", "hundred")},
           {"value": 3, "unit": "SOURCES", "label": "Rival claims to title", "sub": "individuals and societies", "tone": "red", "at": A("c02", "three")}])
cue(type="point", t0=A("c02", "who") - 0.05, t1=E("c02") + 0.05, text="So who owns it?", icon="search", accent=True, at=A("c02", "owns"))
cue(type="bench", t0=S("c03"), t1=E("c03") + 0.05, tag="Supreme Court of India · 29 October 2026",
    judges=[{"name": "Justice M.M. Sundresh", "photo": "../brand/judges/mm_sundresh.jpg", "at": A("c03", "honourable")},
            {"name": "Justice Satish Chandra Sharma", "photo": "../brand/judges/satish_chandra_sharma.jpg", "at": A("c03", "honourable", 2)}])

# ── 2 · from firman to abolition ───────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=S("c04"), t1=E("c05") + 0.05, at=A("c04", "survey"), tag="SUPREME COURT OF INDIA · 29.10.2026",
    cases=[{"name": "Bandari Ramchander & Ors. v. Maitri Coop. Housing Society Ltd. & Ors.", "cite": "2026 INSC 1175 · Civil Appeal No. 10699 of 2013 & connected"}])
cue(type="timeline", t0=S("c04"), t1=E("c04") + 0.05,
    nodes=[{"label": "1912 SURVEY", "value": "Sarkari poramboke", "sub": "government land, Survey Nos. 100 and 101", "at": A("c04", "survey")},
           {"label": "THE NIZAM'S FIRMAN · 1929", "value": "Miyapur as a jagir", "sub": "after the Reilly Commission report, 1927", "at": A("c04", "firman")}])
cue(type="timeline", t0=S("c05"), t1=E("c05") + 0.05,
    nodes=[{"label": "THE FIRMAN'S CONDITION", "value": "no sale without sanction", "sub": "nor a mortgage or a gift", "at": A("c05", "sale")},
           {"label": "15 AUGUST 1949", "value": "all jagirs abolished", "sub": "administration to the State from 15 Sep 1949", "tone": "stop", "at": A("c05", "abolished")}])

# ── 3 · rival claims ───────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c06"), t1=E("c06") + 0.05, head="Village records (pahanies), 1950-53", head_at=S("c06") + 0.05,
    steps=[{"label": "Named as pattedar", "sub": "a woman, in the pahanies of 1950-53", "icon": "file-pen", "at": A("c06", "name")},
           {"label": "Over “Sarkari” land", "sub": "“Poramboke” in the same record", "icon": "triangle-alert", "at": A("c06", "records")},
           {"label": "Three sources of claim", "sub": "two women of one name, the jagirdar", "icon": "users", "at": A("c06", "claimants")}])
cue(type="point", t0=S("c07"), t1=A("c07", "appeal") - 0.05, text="Special Court (31.12.1997) and the High Court (16.04.2003): the State is the rightful owner", icon="landmark", accent=True, at=A("c07", "special"))
cue(type="compare", t0=A("c07", "appeal") - 0.05, t1=E("c07") + 0.05, head="In the Supreme Court: whose land?", head_at=A("c07", "appeal"),
    cols=[{"title": "The claimants", "icon": "users", "at": A("c07", "claimants")}, {"title": "State of Telangana", "icon": "landmark", "at": A("c07", "state", 2)}],
    rows=[{"cells": ["The firman · the jagirdar's status", "Vested in the State under the 1949 law"], "cells_at": [A("c07", "grant"), A("c07", "vested")]},
          {"cells": ["Pahanies · adverse possession", "Commutation received: no right left"], "cells_at": [A("c07", "records"), A("c07", "nineteen")]}])

# ── 4 · before the verdict: the LawWorld request ────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c08"), t1=A("c08", "follow") - 0.05, text="The verdict is next. First, a quick request…", icon="scale", accent=True, at=A("c08", "decided"))
cue(type="list", t0=A("c08", "follow") - 0.05, t1=E("c08") + 0.05, head="Follow LawWorld · lawworld.ai", head_at=A("c08", "follow"),
    items=[{"n": 1, "text": "Search SC and High Court judgments, cited to source", "at": A("c08", "india's")},
           {"n": 2, "text": "Draft petitions, plaints and notices with AI", "at": A("c08", "platform")},
           {"n": 3, "text": "Sign up free · ₹200 AI credit included", "at": A("c08", "advocates")}])

# ── 5 · what the Court held ──────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "jagir") - 0.05, text="What did the Supreme Court decide?", icon="scale", accent=True, at=A("c09", "finally"))
cue(type="list", t0=A("c09", "jagir") - 0.05, t1=E("c09") + 0.05, head="Abolition of Jagirs Regulation, 1358 Fasli", head_at=A("c09", "jagir"),
    items=[{"n": 1, "text": "A jagir: a right over land revenue", "at": A("c09", "revenue")},
           {"n": 2, "text": "Not to be read as title over the property", "at": A("c09", "title")},
           {"n": 3, "text": "A jagirdar is not a title holder", "at": A("c09", "holder")}])
cue(type="point", t0=S("c10"), t1=A("c10", "land") - 0.05, text="1949: even the limited rights “statutorily removed” · pattedar entries made without any proceedings: “an act of nullity”", icon="scale", accent=True, at=A("c10", "limited"))
cue(type="verdicts", t0=A("c10", "land") - 0.05, t1=E("c10") + 0.05,
    rows=[{"text": "Title through the jagir or the records", "ok": False, "at": A("c10", "land")},
          {"text": "The State's title: clearly established", "ok": True, "at": A("c10", "state")},
          {"text": "High Court's 2003 judgment: upheld", "ok": True, "at": A("c10", "dismissed")}])

MUSIC = {"file": "audio/bed_mixkit738_140s.mp3", "target_lufs": -21}   # owner 02-11-2026: trending-style royalty-free bed, audible under the voice
# Fact-check 04-11-2026: c02 counter label "Miyapur village" -> "The lands in dispute" (para 9: Survey Nos. 100 and 101).
