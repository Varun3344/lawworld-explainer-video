# M/s Siddhivinayak Coal Carriers Pvt. Ltd. v. Coal India Ltd. & Ors., with M/s Maa Pitambara Coal Carriers Pvt. Ltd. v. Coal India Ltd.
# & Ors., FAO(OS) (COMM) 248/2026 and 249/2026 (High Court of Delhi, Division Bench: Dinesh Mehta J. and Dr. Aditi Choudhary J., author;
# decided 06.10.2026, REPORTABLE): panel cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND).
# Concept format as sets pan / ara / krm.
# Facts from the judgment (paras): appellants transport coal "in coordination with the Directorate General of Resettlement since 2018";
# in 2023 disputes with the respondents "qua certain amounts deducted by the respondents"; summary suits CS(COMM) 711/2026 and 709/2026
# under Order XXXVII CPC (2); Single Judge, 08.07.2026: "the parameters of Order XXXVII of the CPC were not met", suits converted into
# regular suits (3); appeals under s.13 of the Commercial Courts Act, 2015 (4); 16.09.2026: time granted, on the request of the
# appellants' counsel, to satisfy the Court on maintainability; 28.09.2026: none appeared for the appellants, adjourned "in the interest
# of justice"; 06.10.2026: none appeared (5). Issue: maintainability under the proviso to s.13(1A): an appeal lies from orders
# "specifically enumerated under Order XLIII" CPC and s.37 of the Arbitration and Conciliation Act, 1996 (6); s.13(2): "Notwithstanding
# anything contained in any other law ... or Letters Patent of a High Court", no appeal otherwise than under the Act (7). Law: HPL (India)
# Ltd. & Ors. v. QRG Enterprises & Anr., 2017 SCC OnLine Del 6955 (Coordinate Bench): "this restricts the appealable orders to only those
# orders which are specifically enumerated in Order XLIII" (8); affirmed in Kandla Export Corporation & Anr. v. OCI Corporation & Anr.,
# (2018) 14 SCC 715: "orders that are not specifically enumerated under Order 43 CPC would, therefore, not be appealable" (9); appeal
# under s.13 lies only against orders enumerated in Order XLIII and s.37 (10). Held: "On perusal of Order XLIII of the CPC, we find that no
# appeal has been provided against such orders" (11); appeals not maintainable (12); dismissed as not maintainable, pending applications
# disposed of as infructuous (13). The judgment names no alternative remedy, so none is shown. No contested hearing is described.
# No section card: its renderer prefixes "§" to a Section number (owner: never "§"), so the statute is shown as a list card.
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen, as tej)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
STING = {"kicker": "DELHI HIGH COURT · JUDGMENT EXPLAINED", "title": "Summary suit converted: no appeal", "sub": "High Court of Delhi · FAO(OS) (COMM) 248 & 249/2026"}
ENDCARD = {"title": "Summary suit converted: no appeal", "line": "Not listed in Order XLIII · Section 13 appeals not maintainable", "sub": "LawWorld: legal research for advocates"}

# ── 1 · can you appeal? ──────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "judge"), text="Your summary suit converted into a regular suit: can you appeal under the Commercial Courts Act?", hl="can you appeal")
cue(type="bench", t0=S("c02"), t1=E("c02") + 0.05, tag="High Court of Delhi · 6 October 2026",
    judges=[{"name": "Justice Dinesh Mehta", "photo": "../brand/judges/dinesh_mehta.jpg", "at": A("c02", "honourable")},
            {"name": "Dr. Justice Aditi Choudhary", "photo": "../brand/judges/aditi_choudhary.jpg", "at": A("c02", "honourable", 2)}])

# ── 2 · the suits ────────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=A("c03", "coal"), t1=E("c04") + 0.05, at=A("c03", "coal"), tag="HIGH COURT OF DELHI · 06.10.2026",
    cases=[{"name": "Siddhivinayak Coal Carriers Pvt. Ltd. v. Coal India Ltd. & Ors.", "cite": "2026:DHC:8877-DB · FAO(OS) (COMM) 248 & 249/2026"}])
cue(type="flow", t0=S("c03"), t1=E("c03") + 0.05, head="The parties", head_at=S("c03") + 0.05,
    steps=[{"label": "Two coal transport firms", "sub": "Siddhivinayak Coal Carriers · Maa Pitambara Coal Carriers", "icon": "user", "at": A("c03", "coal")},
           {"label": "With the DGR since 2018", "sub": "Directorate General of Resettlement · transportation of coal", "icon": "calendar", "at": A("c03", "directorate")},
           {"label": "2023: dispute over deductions", "sub": "amounts deducted by the respondents, Coal India Ltd. & Ors.", "icon": "file-text", "at": A("c03", "disputed")}])
cue(type="timeline", t0=S("c04"), t1=E("c04") + 0.05,
    nodes=[{"label": "SUMMARY SUITS", "value": "Order XXXVII", "sub": "CS(COMM) 711/2026 and 709/2026", "at": A("c04", "summary")},
           {"label": "SINGLE JUDGE · 8 JUL 2026", "value": "Not met", "sub": "“the parameters of Order XXXVII of the CPC were not met”", "tone": "red", "at": A("c04", "single")},
           {"label": "CONVERTED", "value": "Regular suits", "sub": "the orders under appeal", "at": A("c04", "converted")}])

# ── 3 · is an appeal maintainable? ───────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c05"), t1=A("c05", "their") - 0.05, text="Appeals under Section 13 of the Commercial Courts Act, 2015", icon="landmark", at=A("c05", "appealed"))
cue(type="timeline", t0=A("c05", "their"), t1=E("c05") + 0.05,
    nodes=[{"label": "16 SEP 2026", "value": "Time granted", "sub": "at the appellants' counsel's request, on maintainability", "at": A("c05", "sought")},
           {"label": "28 SEP 2026", "value": "None appeared", "sub": "adjourned in the interest of justice", "tone": "red", "at": A("c05", "next")},
           {"label": "6 OCT 2026", "value": "None appeared", "sub": "for the appellants, again", "tone": "red", "at": A("c05", "appeared")}])
cue(type="list", t0=S("c06"), t1=E("c06") + 0.05, head="Section 13(1A), proviso: an appeal lies from", head_at=A("c06", "proviso"),
    items=[{"n": 1, "text": "Orders “specifically enumerated under Order XLIII” of the CPC", "at": A("c06", "orders")},
           {"n": 2, "text": "Orders under Section 37, Arbitration and Conciliation Act, 1996", "at": A("c06", "section", 2)},
           {"n": "→", "text": "Section 13(2): no other appeal, “notwithstanding … Letters Patent of a High Court”", "at": A("c06", "arbitration")}])

# ── 4 · the binding law ──────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=S("c07"), t1=E("c07") + 0.05, at=A("c07", "coordinate"), tag="COORDINATE BENCH · HIGH COURT OF DELHI",
    cases=[{"name": "HPL (India) Ltd. & Ors. v. QRG Enterprises & Anr.", "cite": "2017 SCC OnLine Del 6955"}])
cue(type="point", t0=S("c07"), t1=E("c07") + 0.05, text="“this restricts the appealable orders to only those orders which are specifically enumerated in Order XLIII”", icon="scale", accent=True, at=A("c07", "twenty"))
cue(type="cite", t0=S("c08"), t1=E("c08") + 0.05, at=A("c08", "kandla"), tag="SUPREME COURT OF INDIA · AFFIRMED",
    cases=[{"name": "Kandla Export Corporation & Anr. v. OCI Corporation & Anr.", "cite": "(2018) 14 SCC 715"}])
cue(type="point", t0=S("c08"), t1=A("c08", "orders") - 0.05, text="Supreme Court: the HPL position affirmed", icon="landmark", at=A("c08", "supreme"))
cue(type="point", t0=A("c08", "orders"), t1=E("c08") + 0.05, text="“orders that are not specifically enumerated under Order 43 CPC would, therefore, not be appealable”", icon="scale", accent=True, at=A("c08", "orders"))

# ── 5 · the verdict ──────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "so") - 0.05, text="Order XLIII: “no appeal has been provided against such orders”", icon="scale", accent=True, at=A("c09", "provides"))
cue(type="verdicts", t0=A("c09", "so"), t1=E("c09") + 0.05,
    rows=[{"text": "Appeal against the conversion orders under Section 13?", "ok": False, "at": A("c09", "so"), "strike_at": A("c09", "dismissed")},
          {"text": "Both appeals dismissed as not maintainable", "ok": True, "at": A("c09", "dismissed")},
          {"text": "Pending applications disposed of as infructuous", "ok": True, "at": A("c09", "maintainable")}])
cue(type="point", t0=S("c10"), t1=E("c10") + 0.05, text="Like · Share · Subscribe · lawworld.ai", icon="check", accent=True, at=A("c10", "like"))
