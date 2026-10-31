# State of Kerala & Ors. v. [a minor, rep. by her father] & Ors., Writ Appeal No. 2222 of 2026, 2026:KER:82291 (High Court of Kerala,
# Division Bench: Raja Vijayaraghavan V, J. wrote it, K. V. Jayakumar, J.; heard for admission and decided 27.10.2026, "CR"): panel cues,
# run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND). Concept format as vzj / kmv / arm.
# Facts from the judgment (paras): appeal by the State against the Single Judge's judgment of 23.10.2026 in W.P.(C) No. 28587 of 2026
# (1); the writ petitioner, R1, is a minor represented by her father, intending to appear for CLAT 2027; prayer: quash Ext.P8, the
# rejection of her request for inclusion in the Non-Creamy Layer and for an NCL certificate (2, 6); CLAT applications closed 31.10.2026,
# exam 06.12.2026: decided at admission with consent (3); Ext.P7 application to the Tahsildar (5(d)); rejected because her mother was
# a directly recruited Class I officer under Ext.P9, the OM No. 36012/22/93-Estt.(SCT) of 08.09.1993 (5(e)); her mother practised as
# an advocate and joined the Kerala State Higher Judicial Service in 2021 as an Additional District and Sessions Judge at 41 (5(c),
# 5(g), 11, 24); her income in 2019-20 about Rs.1,20,130, Ext.P4 (5(c), 11); Ext.P10, the clarification of 14.10.2004 (5(f), 20);
# Q.4(v): a husband directly recruited to Class II/B entering Class I at 40 or earlier -> children creamy layer; a father directly
# recruited to Class III/C or IV/D entering Class I at 40 or earlier -> children NOT creamy layer (20, 21). Single Judge (8): P9 and
# P10 "harmoniously read" in her favour, else "a clear case of discrimination"; the writ petition's assertion that Munsiff Magistrates
# promoted District Judge after 40 get the OBC (NCL) certificate, denied to her only because of direct recruitment: discrimination;
# Ext.P8 quashed, the Tahsildar to issue the certificate within three working days. Held: Category II A, children of parents either
# of whom is a Class I officer (direct recruits), subject to the Schedule's exceptions (13, 17); framed on the parent's status, not on
# entry through promotion or direct recruitment from a lower category (19); the post held and the manner of entry are material (18); P10's scope confined to a person initially recruited to
# Class III/C or IV/D who later enters Class I (22, 23); a practising advocate directly recruited to a Class I judicial post at 41 is
# outside it (23, 24); the age of entry in isolation is not the test (22, 25); harmonious construction cannot extend a clarification
# beyond its terms or create an exception (26); Union of India v. Rohith Nathan, (2026) 6 SCC 1: a mere Government letter cannot
# override the OM (27-29); the mother's professional income does not displace the service-status criterion (31); the Delhi High Court
# rulings distinguishable (32); equality does not require materially different service categories to be treated identically; no
# challenge to the validity of Ext.P9 (33); "sympathy, however genuine, cannot justify a departure from the criteria prescribed by
# law" (37). Orders (39): the Single Judge's judgment set aside; the Tahsildar's rejection upheld; no relief; writ appeal allowed.
# Privacy: the minor is never named; her mother's income figure is not shown (fact-check 31-10); no place, community, posting or date that would identify her or either parent on any card; the
# cite bar names her only as "a minor". No "admitted" anywhere. Official portraits (Kerala HC "Present Judges" page) on the bench card.
# List lines <= 52 chars (9:16 list items do not wrap). No section sign anywhere.
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen, as vzj)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
STING = {"kicker": "KERALA HIGH COURT · JUDGMENT EXPLAINED", "title": "Direct recruit at 41? Creamy layer", "sub": "High Court of Kerala · W.A. No. 2222 of 2026 · 2026:KER:82291"}
ENDCARD = {"title": "Direct recruit at 41? Creamy layer", "line": "Ext. P10 covers only Class III / IV entrants · the NCL refusal upheld", "sub": "LawWorld: legal research for advocates"}

# ── 1 · creamy layer? ────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "advocate"), text="An advocate is directly recruited as a District Judge at 41. Is her child still in the OBC creamy layer?", hl="creamy layer?")
cue(type="bench", t0=S("c02"), t1=E("c02") + 0.05, tag="Kerala High Court · 27 October 2026",
    judges=[{"name": "Justice Raja Vijayaraghavan V.", "photo": "../brand/judges/raja_vijayaraghavan_v.jpg", "at": A("c02", "honourable")},
            {"name": "Justice K.V. Jayakumar", "photo": "../brand/judges/kv_jayakumar.jpg", "at": A("c02", "honourable", 2)}])

# ── 2 · the certificate ──────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=A("c03", "minor"), t1=E("c05") + 0.05, at=A("c03", "minor"), tag="HIGH COURT OF KERALA · 27.10.2026",
    cases=[{"name": "State of Kerala & Ors. v. a minor (rep. by her father) & Ors.", "cite": "2026:KER:82291 · W.A. No. 2222 of 2026"}])
cue(type="flow", t0=S("c03"), t1=E("c03") + 0.05, head="The application", head_at=S("c03") + 0.05,
    steps=[{"label": "OBC Non-Creamy Layer certificate sought", "sub": "by a minor, for CLAT 2027 · Ext. P7, to the Tahsildar", "icon": "file-text", "at": A("c03", "sought")},
           {"label": "Refused · Ext. P8", "sub": "her mother: a directly recruited Class I / Group A officer", "icon": "x", "tone": "stop", "at": A("c03", "refused")},
           {"label": "Under the 1993 Office Memorandum · Ext. P9", "sub": "Schedule, Category II A: children of directly recruited Class I officers", "icon": "landmark", "at": A("c03", "directly")}])
cue(type="list", t0=S("c04"), t1=A("c04", "citing") - 0.05, head="Her case", head_at=S("c04") + 0.05,
    items=[{"n": 1, "text": "Her mother: a practising advocate before joining", "at": A("c04", "practising")},
           {"n": 2, "text": "Relied on her mother's pre-joining income (Ext. P4)", "at": A("c04", "advocate")},
           {"n": 3, "text": "Joined as Addl. District & Sessions Judge at 41", "at": A("c04", "became")}])
cue(type="point", t0=A("c04", "citing") - 0.05, t1=E("c04") + 0.05, text="Relied on Ext. P10, the clarification of 14.10.2004 to the 1993 Office Memorandum · W.P.(C) No. 28587 of 2026", icon="file-text", at=A("c04", "citing"))

# ── 3 · the single judge ─────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c05"), t1=E("c05") + 0.05, head="The Single Judge · 23.10.2026", head_at=S("c05") + 0.05,
    steps=[{"label": "Ext. P8 refusal quashed", "sub": "the Tahsildar to issue the OBC (NCL) certificate within three working days", "icon": "file-check", "at": A("c05", "quashed")},
           {"label": "Promoted District Judges' children", "sub": "Munsiff Magistrates promoted after 40 get the certificate, the petition said", "icon": "user", "at": A("c05", "promoted")},
           {"label": "Denied only for direct recruitment", "sub": "“a clear case of discrimination”, the Single Judge held", "icon": "scale", "at": A("c05", "denying")}],
    note={"text": "Exts. P9 and P10 “harmoniously read” in her favour", "icon": "info", "at": A("c05", "direct")})

# ── 4 · what the court held ──────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c06"), t1=A("c06", "both") - 0.05, text="1993 OM, Category II A: children of a directly recruited Class I officer fall in the creamy layer, subject to the Schedule's exceptions", icon="landmark", at=A("c06", "held"))
cue(type="point", t0=A("c06", "both") - 0.05, t1=E("c06") + 0.05, text="The post held and “the manner in which the parent entered the relevant service category are material considerations” (para 18)", icon="scale", at=A("c06", "both"))
cue(type="compare", t0=S("c07"), t1=E("c07") + 0.05, head="Ext. P10 · the 2004 clarification", head_at=S("c07") + 0.05,
    cols=[{"title": "Within its scope", "icon": "check", "at": A("c07", "covers")}, {"title": "Outside it", "icon": "x", "at": A("c07", "advocate")}],
    rows=[{"cells": ["Began in Class III or IV service", "A practising advocate"], "cells_at": [A("c07", "class"), A("c07", "advocate")]},
          {"cells": ["Later entered Class I", "Directly recruited to Class I · age of entry alone is not the test"], "cells_at": [A("c07", "rising"), A("c07", "recruited")]}])
cue(type="flow", t0=S("c08"), t1=E("c08") + 0.05, head="Why the Single Judge erred", head_at=S("c08") + 0.05,
    steps=[{"label": "A mere letter cannot override the 1993 OM", "sub": "nor can a harmonious reading create a new exception", "icon": "file-text", "tone": "stop", "at": A("c08", "letter")},
           {"label": "Different categories need not be treated alike", "sub": "materially different service categories · Ext. P9's validity never challenged", "icon": "scale", "at": A("c08", "equality")}],
    note={"text": "Her mother's income as an advocate does not, by itself, displace the service-status test (para 31)", "icon": "info", "at": A("c08", "categories")})
cue(type="cite", t0=A("c08", "rohith"), t1=E("c08") + 0.05, at=A("c08", "rohith"), tag="SUPREME COURT · RELIED ON",
    cases=[{"name": "Union of India v. Rohith Nathan", "cite": "(2026) 6 SCC 1"}])

# ── 5 · the result ───────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "state") - 0.05, text="“Sympathy, however genuine, cannot justify a departure from the criteria prescribed by law” (para 37)", icon="scale", at=A("c09", "sympathy"))
cue(type="verdicts", t0=A("c09", "state") - 0.05, t1=E("c09") + 0.05,
    rows=[{"text": "The State's writ appeal: allowed", "ok": True, "at": A("c09", "appeal")},
          {"text": "The Single Judge's judgment of 23.10.2026: set aside", "ok": False, "at": A("c09", "allowed")},
          {"text": "The Tahsildar's refusal upheld · no relief in the writ petition", "ok": True, "at": A("c09", "refusal")}])
cue(type="point", t0=S("c10"), t1=E("c10") + 0.05, text="Like · Share · Subscribe · lawworld.ai", icon="check", accent=True, at=A("c10", "like"))
