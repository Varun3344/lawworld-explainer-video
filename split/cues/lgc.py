# Commissioner of Income-Tax & Anr. v. M/s Logica Pvt. Ltd., Income Tax Appeal No. 338 of 2013 (High Court of Karnataka, Vibhu
# Bakhru CJ wrote it, K.S. Hemalekha J.; reserved 28.09.2026, pronounced 28.10.2026, REPORTABLE): panel cues, run by
# split/build_course_plan.py (helpers: at S E cue fx have r3 PEND). Concept format as sets kmv / ssk.
# Facts from the judgment (paras): the Revenue's s.260A appeal against the ITAT's order of 28.02.2013 in ITA 1129/Bang/2011, AY 2007-08
# (1); assessment order 20.09.2011 under s.143(3) r/w s.144C(5), (8) on DRP directions of 02.09.2011 (2); admitted 24.03.2014 on ten
# questions (3); dismissed by this Court on 12.07.2018 following Softbrands (4); Supreme Court, 19.04.2023, SAP Labs India v. ITO,
# (2023) 454 ITR 121 (SC): order set aside, appeal remitted to be decided afresh (5, 6); Questions 9 and 10 (s.10A) do not survive (7);
# the Assessee: software development and consultancy services (10); international transactions, reference to the TPO (11); TPO order
# 30.09.2010 under s.92CA, adjustment ₹39,73,03,044 (12); the Assessee's TP study rejected (13, 15); TNMM, markup on cost as the PLI
# (14); the Assessee's comparables averaged 13% (14); the TPO's 26 comparables averaged 25.14% (23.84% working-capital adjusted),
# Infosys and Wipro among them (15); the ITAT accepted objections on comparables and filters (16); eight comparables (18): Accel
# (training: Accel IT Academy, 20-22), Avani (software product "DXchange", 23-25), Celestial (drug discovery, a specialised industry,
# no segment reporting, 26-37), Lucid (product "Muulam", product development spend, 38-40), KALS (products and training, no segment
# data, 41-46), Infosys (brand valued ₹22,915 crores, revenue over ₹13,145 crores, 47-48), Wipro (67% of sales from premium products,
# very large turnover, 49-51), Tata Elxsi (niche product company, 52-53); RPT filter: the TPO 25% with no specific reasons, the ITAT
# 15% of sales (61). The Revenue: brand / turnover irrelevant to the profit margin (50; Q6, Q7); no basis for the 15% cut-off (Q5).
# Held: size is relevant; a large company has a different FAR profile; TNMM tolerates variations but not an extremely large disparity
# in size; size may significantly alter the cost structure (50); an established brand and goodwill are intangible assets with a vital
# bearing on revenue margins; brand is not the only variable but bears on profit margins (64, 69); functional dissimilarity is a
# finding of fact, not perverse (22, 25, 37, 40, 46, 53); a segment is compared only on credible segmental financials; s.133(6)
# information must be credible and duly verified (57, 58); a narrower RPT filter is appropriate where sufficient comparables are found,
# and here they were; SAP Labs v. ITO (Karnataka HC, 28.08.2026) followed (61-63); Q5 and Q8 answered against the Revenue (63, 71);
# in the given facts, not substantial questions of law (72); appeal dismissed (73).
# Flow policy: companies and public offices only; no "admitted" / "concededly" on any card. Official Karnataka High Court portraits
# on the bench card. List lines <= 52 chars (9:16 list items do not wrap). No section sign anywhere.
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen, as kmv / ssk)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
STING = {"kicker": "KARNATAKA HIGH COURT · JUDGMENT EXPLAINED", "title": "Infosys, Wipro not comparables", "sub": "CIT v. M/s Logica Pvt. Ltd. · ITA No. 338 of 2013"}
ENDCARD = {"title": "Infosys, Wipro not comparables", "line": "Size and brand bear on margins · 15% RPT filter upheld · Revenue's appeal dismissed", "sub": "LawWorld: legal research for advocates"}

# ── 1 · giants as comparables ────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "client"), text="Your client writes software for its own group. Can the TPO compare it with giants like Infosys and Wipro?", hl="giants like Infosys and Wipro?")
cue(type="bench", t0=S("c02"), t1=E("c02") + 0.05, tag="Karnataka High Court · 28 October 2026",
    judges=[{"name": "Chief Justice Vibhu Bakhru", "photo": "../brand/judges/vibhu_bakhru.jpg", "at": A("c02", "honourable")},
            {"name": "Justice K.S. Hemalekha", "photo": "../brand/judges/ks_hemalekha.jpg", "at": A("c02", "honourable", 2)}])

# ── 2 · the adjustment ───────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=A("c03", "logica"), t1=E("c05") + 0.05, at=A("c03", "logica"), tag="HIGH COURT OF KARNATAKA · 28.10.2026",
    cases=[{"name": "Commissioner of Income-Tax v. M/s Logica Pvt. Ltd.", "cite": "Income Tax Appeal No. 338 of 2013 · AY 2007-08"}])
cue(type="flow", t0=S("c03"), t1=E("c03") + 0.05, head="The transfer pricing adjustment", head_at=S("c03") + 0.05,
    steps=[{"label": "Software development services", "sub": "Logica's international transactions with its associated enterprises", "icon": "file-text", "at": A("c03", "software")},
           {"label": "TPO's adjustment: ₹39,73,03,044", "sub": "order of 30 Sep 2010 under Section 92CA", "icon": "landmark", "tone": "stop", "at": A("c03", "adjustment")},
           {"label": "Assessment year 2007-08", "sub": "assessed under Section 143(3) read with Section 144C, on the DRP's directions", "icon": "calendar", "at": A("c03", "assessment")}])
cue(type="counters", t0=S("c04"), t1=E("c04") + 0.05, head="TNMM · markup on cost", head_at=S("c04") + 0.05,
    items=[{"value": 26, "unit": "COMPANIES", "label": "The TPO's comparables", "sub": "Infosys and Wipro among them", "at": A("c04", "picked")},
           {"value": 25, "unit": "% MARKUP", "label": "Their average markup on cost", "sub": "25.14% · 23.84% working-capital adjusted", "at": A("c04", "average")}],
    note={"text": "The TPO rejected Logica's own study: its comparables averaged 13%", "icon": "x", "at": A("c04", "cost")})
cue(type="list", t0=S("c05"), t1=A("c05", "related") - 0.05, head="The Tribunal struck out eight", head_at=A("c05", "struck"),
    items=[{"n": 1, "text": "Infosys and Wipro", "at": A("c05", "infosys")},
           {"n": 2, "text": "Accel, Avani, Celestial, KALS, Lucid, Tata Elxsi", "at": A("c05", "wipro")}])
cue(type="timeline", t0=A("c05", "related") - 0.05, t1=E("c05") + 0.05,
    nodes=[{"label": "TPO'S RPT FILTER", "value": "25%", "sub": "no specific reasons given for the figure", "tone": "stop", "at": A("c05", "related")},
           {"label": "TRIBUNAL'S RPT FILTER", "value": "15%", "sub": "related party transactions above 15% of sales: excluded", "at": A("c05", "fifteen")}])

# ── 3 · the Revenue's appeal ─────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="timeline", t0=S("c06"), t1=A("c06", "that") - 0.05,
    nodes=[{"label": "REVENUE'S APPEAL · 2013", "value": "Section 260A", "sub": "dismissed by the High Court on 12.07.2018", "at": A("c06", "appealed")},
           {"label": "SUPREME COURT · 2023", "value": "Remanded", "sub": "SAP Labs India v. ITO · to be decided afresh", "at": A("c06", "supreme")}])
cue(type="list", t0=A("c06", "that") - 0.05, t1=E("c06") + 0.05, head="The Revenue's case", head_at=A("c06", "that"),
    items=[{"n": 1, "text": "Brand and size don't affect the profit margin", "at": A("c06", "brand")},
           {"n": 2, "text": "No basis for the 15% related party filter", "at": A("c06", "fifteen")}])

# ── 4 · what the court held ──────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c07"), t1=E("c07") + 0.05, head="Held: size matters", head_at=A("c07", "disagreed"),
    steps=[{"label": "A large company: a different FAR profile", "sub": "size may significantly alter the cost structure", "icon": "scale", "at": A("c07", "giant")},
           {"label": "TNMM tolerates variations", "sub": "it does not accommodate an extremely large disparity in size", "icon": "search", "at": A("c07", "tolerates")},
           {"label": "Such giants: not comparables", "sub": "Per the Tribunal, Infosys: revenue over ₹13,145 crore · brand valued at ₹22,915 crore", "icon": "x", "tone": "stop", "at": A("c07", "extremely")}])
cue(type="verdicts", t0=S("c08"), t1=A("c08", "product") - 0.05,
    rows=[{"text": "An established brand: an intangible asset", "ok": True, "at": A("c08", "established")},
          {"text": "It has a vital bearing on revenue margins", "ok": True, "at": A("c08", "bears")},
          {"text": "Infosys and Wipro: rightly excluded", "ok": True, "at": A("c08", "infosys")}])
cue(type="flow", t0=A("c08", "product") - 0.05, t1=E("c08") + 0.05, head="Functionally different", head_at=A("c08", "product"),
    steps=[{"label": "Software products", "sub": "Avani (DXchange) · Lucid (Muulam) · Tata Elxsi", "icon": "file-text", "at": A("c08", "product")},
           {"label": "Training services", "sub": "Accel's IT Academy · KALS", "icon": "user", "at": A("c08", "training")},
           {"label": "Drug discovery", "sub": "Celestial: a specialised industry", "icon": "search", "at": A("c08", "discovery")}],
    note={"text": "Segment data called under Section 133(6) must be credible and duly verified", "icon": "info", "at": A("c08", "functionally")})

# ── 5 · the verdict ──────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="verdicts", t0=S("c09"), t1=E("c09") + 0.05,
    rows=[{"text": "15% related party filter upheld: enough comparables found", "ok": True, "at": A("c09", "related")},
          {"text": "No substantial question of law on these facts", "ok": True, "at": A("c09", "substantial")},
          {"text": "Revenue's appeal dismissed", "ok": True, "at": A("c09", "dismissed")}])
cue(type="point", t0=S("c10"), t1=E("c10") + 0.05, text="Like · Share · Subscribe · lawworld.ai", icon="check", accent=True, at=A("c10", "like"))
