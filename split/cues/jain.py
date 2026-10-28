# Ram Roop Jain & Anr. v. Kalpana Jain & Anr., CM(M) 2311/2026 (High Court of Delhi, Ajay Digpaul J.; decided 27.10.2026): panel cues,
# run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND). Concept format as sets ara / krm.
# Facts from the judgment (paras): the landlords' eviction petition under s.14(1)(e) read with s.25-B DRC Act, 1958, Shop No. 1219/07,
# Ground Floor, Katra Sat Narayan, Chandni Chowk (2), RC ARC 582/25 "Kalpana Jain v. Ram Roop Jain" (1); summons served 23.09.2025,
# leave to defend filed 06.10.2025 (3); s.151 CPC application on 05.10.2026, with leave to defend listed for arguments (4); the material:
# the landlords' eviction petitions against other shops in the same premises, withdrawals / disposals, photographs of "SHOP AVAILABLE FOR
# RENT" banners (8-10, 18); dismissed by ARC-02 (Central), Tis Hazari on 06.10.2026 (1, 5); Art. 227 petition (6); tenants: the material
# negates / questions the bona fide requirement (8, 10); landlords: photographs fabricated / staged (14); the other petitions disclosed
# in para 31 of the eviction petition and para 15 of the reply, records on the e-courts portal, explanations "vague and not
# maintainable" (18-19); "not one shred of proof" that the landlords intend to or have let out the other shops (20); s.19 DRC Act
# protects evicted tenants, the tenants too if their shop is re-let (21); Gaya Prasad v. Pradeep Srivastava (2001) 2 SCC 604: need
# "completely eclipsed" (23, 25); "a dilatory tactic" (26); s.151 cannot give successive opportunities or bypass s.25-B (27-28, 31);
# Manpreet Singh v. Parmod Kumar Gupta 2026 SCC OnLine Del 7086 (28); no perversity under Art. 227 (30); petition dismissed (33).
# The bench card uses the official portrait.
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen, as tej)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
STING = {"kicker": "DELHI HIGH COURT · JUDGMENT EXPLAINED", "title": "Section 151 and the Section 25-B procedure", "sub": "Ram Roop Jain v. Kalpana Jain · CM(M) 2311/2026"}
ENDCARD = {"title": "Section 151 and the Section 25-B procedure", "line": "Section 151 cannot bypass the Section 25-B summary procedure", "sub": "LawWorld: legal research for advocates"}

# ── 1 · late documents? ──────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "leave"), text="Leave to defend already filed: can the tenant add fresh documents under Section 151 CPC?", hl="add fresh documents")
cue(type="bench", t0=S("c02"), t1=E("c02") + 0.05, tag="High Court of Delhi · 27 October 2026",
    judges=[{"name": "Justice Ajay Digpaul", "photo": "../brand/judges/ajay_digpaul.jpg", "at": A("c02", "honourable")}])

# ── 2 · the case ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=A("c03", "landlords"), t1=E("c04") + 0.05, at=A("c03", "landlords"), tag="HIGH COURT OF DELHI · 27.10.2026",
    cases=[{"name": "Ram Roop Jain & Anr. v. Kalpana Jain & Anr.", "cite": "CM(M) 2311/2026"}])
cue(type="flow", t0=S("c03"), t1=E("c03") + 0.05, head="The eviction petition", head_at=S("c03") + 0.05,
    steps=[{"label": "The landlords", "sub": "Kalpana Jain & Anr.", "icon": "user", "at": A("c03", "landlords")},
           {"label": "A shop in Chandni Chowk", "sub": "No. 1219/07, ground floor, Katra Sat Narayan", "icon": "landmark", "at": A("c03", "chandni")},
           {"label": "Sections 14(1)(e) and 25-B, DRC Act", "sub": "bona fide need · summary procedure", "icon": "scale", "at": A("c03", "summary")}])
cue(type="timeline", t0=S("c04"), t1=E("c04") + 0.05,
    nodes=[{"label": "SUMMONS", "value": "23 Sep 2025", "sub": "served on the tenants", "at": A("c04", "year")},
           {"label": "LEAVE TO DEFEND", "value": "6 Oct 2025", "sub": "application filed", "at": A("c04", "leave")},
           {"label": "SECTION 151 CPC", "value": "5 Oct 2026", "sub": "with leave to defend listed for arguments", "tone": "red", "at": A("c04", "applied")}])
cue(type="list", t0=S("c05"), t1=E("c05") + 0.05, head="What they wanted to add", head_at=S("c05") + 0.05,
    items=[{"n": 1, "text": "The landlords' eviction cases against other shops in the same premises", "at": A("c05", "landlords")},
           {"n": 2, "text": "Several withdrawn or disposed of", "at": A("c05", "several")},
           {"n": 3, "text": "Photos of “SHOP AVAILABLE FOR RENT” banners", "at": A("c05", "photos")}])

# ── 3 · the challenge ────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c06"), t1=E("c06") + 0.05, head="The challenge", head_at=S("c06") + 0.05,
    steps=[{"label": "Application dismissed", "sub": "ARC-02 (Central), Tis Hazari · 6 Oct 2026", "icon": "x", "tone": "stop", "at": A("c06", "dismissed")},
           {"label": "Article 227 petition", "sub": "to the Delhi High Court", "icon": "arrow-right", "at": A("c06", "article")},
           {"label": "Tenants: the bona fide need is in doubt", "sub": "the landlords say the photos are staged", "icon": "user", "at": A("c06", "undercut")}])

# ── 4 · what the court held ──────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c07"), t1=A("c07", "not") - 0.05, text="Already disclosed in the eviction petition · on the e-courts portal anyway", icon="search", at=A("c07", "high"))
cue(type="point", t0=A("c07", "not"), t1=E("c07") + 0.05, text="“not one shred of proof” that the landlords intend to, or have, let out the other shops", icon="x", accent=True, at=A("c07", "not"))
cue(type="section", t0=S("c08"), t1=A("c08", "and") - 0.05, at=A("c08", "even"), act="DRC ACT, 1958", num="19", title="Recovery of possession for occupation and re-entry",
    points=[{"text": "A safeguard if the landlord re-lets", "at": A("c08", "section")},
            {"text": "Open to these tenants too, if their shop is re-let", "at": A("c08", "protects")}])
cue(type="point", t0=A("c08", "and"), t1=E("c08") + 0.05, text="The need must be “completely eclipsed” by later events: not so here", icon="scale", accent=True, at=A("c08", "and"))
cue(type="cite", t0=A("c08", "gaya"), t1=E("c08") + 0.05, at=A("c08", "gaya"), tag="SUPREME COURT · APPLIED",
    cases=[{"name": "Gaya Prasad v. Pradeep Srivastava", "cite": "(2001) 2 SCC 604"}])

# ── 5 · the verdict ──────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "section") - 0.05, text="The application: “a dilatory tactic”", icon="x", accent=True, at=A("c09", "court"))
cue(type="verdicts", t0=A("c09", "section"), t1=E("c09") + 0.05,
    rows=[{"text": "Section 151 CPC to bypass the Section 25-B procedure?", "ok": False, "at": A("c09", "section"), "strike_at": A("c09", "chances")},
          {"text": "Petition dismissed · the Rent Controller's order stands", "ok": True, "at": A("c09", "petition")}])
cue(type="point", t0=S("c10"), t1=E("c10") + 0.05, text="Like · Share · Subscribe · lawworld.ai", icon="check", accent=True, at=A("c10", "like"))
