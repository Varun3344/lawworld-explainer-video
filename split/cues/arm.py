# M/s. Aruna Mills v. The State Tax Officer & Anr., W.P. Nos. 30908, 31022, 31026 & 31597 of 2024 (common order), High Court of
# Judicature at Madras (N. Senthilkumar J., single bench; reserved 16.09.2026, pronounced 28.10.2026; reportable per the court's judis
# "reportable = Y" list, the PDF's "Index : Yes / No" left unstruck; no neutral citation assigned yet): panel cues, run by
# split/build_course_plan.py (helpers: at S E cue fx have r3 PEND). Concept format as cdp / gms. First Madras High Court reel.
# Facts from the judgment (paras): the firm makes and supplies cotton, poly-cotton yarn and synthetic fibres, Tiruppur (cause title, 2);
# surprise inspection 19 and 20.10.2023 by the respondents, on the days of a family wedding at Karur, about 50 km away (3, 22); the
# firm's case: its accounting staff were coerced to pay through Form GST DRC-03 on 19 and 20.10.2023; amounts collected on the spot for
# 2020-21 to 2023-24 (3, 4); representation 06.11.2023: payments under protest, refund sought (4); DRC-01A 07.11.2023, four grounds (4);
# interest dropped, Rule 88B (5, 7); reply 22.11.2023: "not voluntary" (6); SCN DRC-01 15.12.2023, Nil proposals (6); order in Form
# GST DRC-05 27.03.2024 (7, 15); prayers: refund of Rs.2,20,09,106 (2020-21, W.P. 31022), Rs.2,59,151 (2021-22, W.P. 31026),
# Rs.3,84,871 (2022-23, W.P. 30908), Rs.1,40,687 (2023-24, W.P. 31597) "recovered during surprise inspection" (prayers); no DRC-04
# under Rule 142 (10); Rule 142(2): DRC-03 payment -> acknowledgement in Form GST DRC-04 (12, quoting ATR Malleable Casting / Shree
# Ganesh Molasses). Department: DRC-03 "a mechanism for voluntary payment" (18, 19); OTP sent only to the partners' registered mobile
# and email; coercion a disputed fact outside Article 226 (19); 17 days' delay; Rule 142(3), DRC-05 (20). Held: the partners' presence
# "could not be possible" (22); the delay "cannot, by itself, be a ground to reject the petitioner's claim" (23); delay plea "rejected
# at the outset" (25); from the counter, no DRC-04 issued; the 06.11.2023 representation not considered; "non issuance of Form GST DRC
# - 04 is fatal to the respondent"; ATR Malleable Casting (P.) Ltd. v. Inspector of Central Taxes, (2024) 164 taxmann.com 78 (Calcutta,
# DB) "squarely applies" (28); orders of 27.03.2024 set aside; refund of IGST, CGST, SGST remitted during the inspection, 2020-21 to
# 2023-24, "as prayed for", within eight weeks of receipt of the order (29); manual appeal within twelve weeks (30); allowed, no costs (31).
# Not on any card: no finding of coercion by the Court (coercion stays "the firm says"); no evasion word; no "admitted"; no person
# named (company only); no section sign (no section card). Official portrait (hcmadras.tn.gov.in) on the bench card. List lines <= 52 chars.
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen, as cdp)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
STING = {"kicker": "MADRAS HIGH COURT · JUDGMENT EXPLAINED", "title": "GST paid on the spot? Refund it", "sub": "Aruna Mills v. State Tax Officer · W.P. No. 30908 of 2024 & batch"}
ENDCARD = {"title": "GST paid on the spot? Refund it", "line": "No Form GST DRC-04: orders set aside, refund within 8 weeks", "sub": "LawWorld: legal research for advocates"}

# ── 1 · paid on the spot? ────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "tax"), text="GST paid on the spot in a surprise inspection, never acknowledged. Can the department keep it?", hl="keep it?")
cue(type="bench", t0=S("c02"), t1=E("c02") + 0.05, tag="Madras High Court · 28 October 2026",
    judges=[{"name": "Justice N. Senthilkumar", "photo": "../brand/judges/n_senthilkumar.jpg", "at": A("c02", "honourable")}])

# ── 2 · the inspection ───────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=A("c03", "aruna"), t1=E("c05") + 0.05, at=A("c03", "aruna"), tag="HIGH COURT OF MADRAS · 28.10.2026",
    cases=[{"name": "M/s. Aruna Mills v. The State Tax Officer & Anr.", "cite": "W.P. Nos. 30908, 31022, 31026 & 31597 of 2024"}])
cue(type="flow", t0=S("c03"), t1=E("c03") + 0.05, head="The inspection", head_at=S("c03") + 0.05,
    steps=[{"label": "Aruna Mills, Tiruppur", "sub": "makes cotton and poly-cotton yarn and synthetic fibres", "icon": "user", "at": A("c03", "yarn")},
           {"label": "Surprise GST inspection · 19 & 20 Oct 2023", "sub": "State Tax Officers, Tirupur Intelligence Division", "icon": "search", "at": A("c03", "surprise")},
           {"label": "The same days: a family wedding", "sub": "at Karur, about 50 km from the business premises", "icon": "calendar", "at": A("c03", "days")}])
cue(type="list", t0=S("c04"), t1=A("c04", "through") - 0.05, head="Refunds sought: paid during the inspection", head_at=A("c04", "firm"),
    items=[{"n": 1, "text": "2020-21 · ₹2,20,09,106", "at": A("c04", "over")},
           {"n": 2, "text": "2021-22 · ₹2,59,151", "at": A("c04", "crore")},
           {"n": 3, "text": "2022-23 · ₹3,84,871", "at": A("c04", "rupees")},
           {"n": 4, "text": "2023-24 · ₹1,40,687", "at": A("c04", "collected")}])
cue(type="point", t0=A("c04", "through") - 0.05, t1=E("c04") + 0.05, text="Paid through Form GST DRC-03 on 19 & 20 Oct 2023 · “not voluntary”, the firm says · refund sought on 6 Nov 2023", icon="file-text", at=A("c04", "through"))
cue(type="flow", t0=S("c05"), t1=A("c05", "but") - 0.05, head="From notice to order", head_at=S("c05") + 0.05,
    steps=[{"label": "Intimation · Form GST DRC-01A", "sub": "7 Nov 2023 · four grounds", "icon": "file-text", "at": A("c05", "officer")},
           {"label": "Show cause notice · Form GST DRC-01", "sub": "15 Dec 2023 · Nil proposals", "icon": "info", "at": A("c05", "passed")},
           {"label": "Orders · Form GST DRC-05", "sub": "27 Mar 2024 · for 2020-21 to 2023-24", "icon": "landmark", "at": A("c05", "march")}])
cue(type="point", t0=A("c05", "but") - 0.05, t1=E("c05") + 0.05, text="Rule 142(2): the officer shall acknowledge a DRC-03 payment in Form GST DRC-04 · here, none was issued", icon="file-check", accent=True, at=A("c05", "acknowledgement"))

# ── 3 · the department's case ────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c06"), t1=E("c06") + 0.05, head="The department's case", head_at=A("c06", "answer"),
    steps=[{"label": "DRC-03 is voluntary payment", "sub": "“a mechanism for voluntary payment”", "icon": "file-text", "at": A("c06", "voluntary")},
           {"label": "Payment needs the partners' OTP", "sub": "sent only to their registered mobile and email", "icon": "user", "at": A("c06", "sent")},
           {"label": "Protest came 17 days late", "sub": "the representation only on 6 Nov 2023", "icon": "calendar", "at": A("c06", "protest")}],
    note={"text": "Also argued: “coercion” is a disputed fact, outside writ jurisdiction", "icon": "info", "at": A("c06", "seventeen")})

# ── 4 · what the court held ──────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="verdicts", t0=S("c07"), t1=E("c07") + 0.05,
    rows=[{"text": "Inspection on the wedding days: the partners' presence “could not be possible”", "ok": True, "at": A("c07", "wedding")},
          {"text": "17-day delay: “cannot, by itself, be a ground to reject” the claim", "ok": True, "at": A("c07", "delay")},
          {"text": "The department's delay plea: rejected", "ok": False, "at": A("c07", "defeat")}])
cue(type="flow", t0=S("c08"), t1=E("c08") + 0.05, head="Why the orders fell", head_at=S("c08") + 0.05,
    steps=[{"label": "No Form GST DRC-04 issued", "sub": "clear from the respondents' own counter", "icon": "search", "at": A("c08", "counter")},
           {"label": "Representation of 6 Nov 2023 not considered", "sub": "the firm's stand was never weighed", "icon": "x", "at": A("c08", "protest")},
           {"label": "No DRC-04: “fatal to the respondent”", "sub": "the impugned orders liable to be set aside", "icon": "scale", "tone": "ok", "at": A("c08", "fatal")}])
cue(type="cite", t0=A("c08", "considered"), t1=E("c08") + 0.05, at=A("c08", "considered"), tag="CALCUTTA HIGH COURT · RELIED ON",
    cases=[{"name": "ATR Malleable Casting (P.) Ltd. v. Inspector of Central Taxes", "cite": "(2024) 164 taxmann.com 78 (Cal.) (DB) · “squarely applies”"}])

# ── 5 · the result ───────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="verdicts", t0=S("c09"), t1=E("c09") + 0.05,
    rows=[{"text": "DRC-05 orders of 27 Mar 2024: set aside", "ok": True, "at": A("c09", "aside")},
          {"text": "Refund of IGST, CGST and SGST paid during the inspection, as prayed for, within 8 weeks of receipt of the order", "ok": True, "at": A("c09", "refunded")},
          {"text": "Writ petitions allowed · no costs · the firm may appeal manually within 12 weeks", "ok": True, "at": A("c09", "allowed")}])
cue(type="point", t0=S("c10"), t1=E("c10") + 0.05, text="Like · Share · Subscribe · lawworld.ai", icon="check", accent=True, at=A("c10", "like"))
