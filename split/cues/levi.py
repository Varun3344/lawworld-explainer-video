# Rishi Levi v. CBI, W.P.(CRL) 3123/2026 (High Court of Delhi, Sanjeev Narula J.; pronounced 27.10.2026): panel cues, run by
# split/build_course_plan.py (helpers: at S E cue fx have r3 PEND). Concept format as sets ara / krm.
# Facts from the judgment (paras): in Philippine custody, faces extradition to India in a criminal case investigated by the CBI;
# challenges the ACMM's (East, Karkardooma) November 2014 Proclaimed Offender order under s.82 CrPC and seeks a stay of the CJM's (Rouse
# Avenue) order of 01.07.2026 on the extradition request; Arts. 226/227 with s.528 BNSS (1); FIR 20.11.2006 (3); charge-sheet 23.12.2009
# (4, 25); joined the investigation once in 2008, then left India (5); charge-sheet records a Gurgaon and an Australian address (6);
# 30.03.2010: not served, nothing shows later service (7, 25); NBWs 29.05.2013 unexecuted (8-9); s.82 process 12.08.2014, declared PO
# November 2014 (9-10); the CBI's reply shows no attempt to verify or serve at the Australian address (26); satisfaction "must be founded
# on material indicating deliberate evasion", the mere return of a warrant unexecuted is not enough (24); the agency "was already aware
# of his overseas address, but had demonstrated no effort to pursue it" (27); offences not enumerated in s.82(4) (31-32); proclamation
# and the PO declaration set aside, s.83 process ceases (32, 37, 50(i)-(ii)); "does not absolve the Petitioner of his obligation to face
# the pending prosecution" (36); warrants and proclamation "distinct judicial processes", warrants of May 2013, Nov 2024, June 2026 not
# cancelled (42, 50(iii)); Treaty Arts. 8 and 9 need no PO declaration (39); stay of the 01.07.2026 order and the extradition declined; no
# suspension or withdrawal of the Red Notice or the extradition request required by the judgment (42, 50(iv)); liberty of voluntary
# surrender, Treaty Art. 15 (48, 50(vi)). Owner 28-10-2026: the name only on the cite card (not in the sting); the alleged offences are
# not described anywhere. The bench card uses the official portrait.
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen, as tej)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
STING = {"kicker": "DELHI HIGH COURT · JUDGMENT EXPLAINED", "title": "Section 82 proclamation and extradition", "sub": "High Court of Delhi · W.P.(CRL) 3123/2026"}
ENDCARD = {"title": "Section 82 proclamation and extradition", "line": "Proclamation set aside · no stay of the extradition", "sub": "LawWorld: legal research for advocates"}

# ── 1 · proclaimed offender? ─────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "proclaimed"), text="Proclaimed offender order set aside: do the warrants, Red Notice and extradition fall too?", hl="fall too?")
cue(type="bench", t0=S("c02"), t1=E("c02") + 0.05, tag="High Court of Delhi · 27 October 2026",
    judges=[{"name": "Justice Sanjeev Narula", "photo": "../brand/judges/sanjeev_narula.jpg", "at": A("c02", "honourable")}])

# ── 2 · the case ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=A("c03", "petitioner"), t1=E("c04") + 0.05, at=A("c03", "petitioner"), tag="HIGH COURT OF DELHI · 27.10.2026",
    cases=[{"name": "Rishi Levi v. CBI", "cite": "W.P.(CRL) 3123/2026"}])
cue(type="flow", t0=S("c03"), t1=E("c03") + 0.05, head="The case", head_at=S("c03") + 0.05,
    steps=[{"label": "A criminal case", "sub": "FIR of 20 Nov 2006 · charge-sheet 23 Dec 2009", "icon": "file-text", "at": A("c03", "criminal")},
           {"label": "Investigated by the CBI", "sub": "Central Bureau of Investigation", "icon": "search", "at": A("c03", "investigated")},
           {"label": "Left India · 2008", "sub": "after joining the investigation once", "icon": "arrow-right", "at": A("c03", "left")}])
cue(type="timeline", t0=S("c04"), t1=E("c04") + 0.05,
    nodes=[{"label": "CHARGE-SHEET", "value": "23 Dec 2009", "sub": "an Australian address recorded", "at": A("c04", "charge")},
           {"label": "SUMMONS", "value": "30 Mar 2010", "sub": "recorded as not served", "at": A("c04", "serve")},
           {"label": "WARRANTS", "value": "29 May 2013", "sub": "non-bailable · unexecuted", "at": A("c04", "shown")},
           {"label": "DECLARATION", "value": "Nov 2014", "sub": "proclaimed offender · s.82 CrPC", "tone": "red", "at": A("c04", "declared")}])
cue(type="flow", t0=S("c05"), t1=E("c05") + 0.05, head="Before the High Court", head_at=S("c05") + 0.05,
    steps=[{"label": "In custody in the Philippines", "sub": "facing extradition to India", "icon": "user", "at": A("c05", "philippine")},
           {"label": "Challenges the 2014 declaration", "sub": "Arts. 226, 227 · Section 528 BNSS", "icon": "file-text", "at": A("c05", "challenged")},
           {"label": "Seeks a stay", "sub": "of the CJM's 1 Jul 2026 order on the extradition request", "icon": "scale", "at": A("c05", "stay")}])

# ── 3 · what section 82 needs ────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c06"), t1=E("c06") + 0.05, at=A("c06", "high"), act="CrPC, 1973", num="82", title="Proclamation for person absconding",
    points=[{"text": "Material showing deliberate evasion", "at": A("c06", "proof")},
            {"text": "Warrants returned unexecuted: not enough", "tone": "no", "at": A("c06", "unexecuted")}],
    note={"text": "The agency knew his overseas address, but showed no effort to pursue it", "icon": "info", "at": A("c06", "overseas")})
cue(type="section", t0=S("c07"), t1=A("c07", "proclamation") - 0.05, at=A("c07", "offences"), act="CrPC, 1973", num="82(4)", title="Who can be declared a proclaimed offender",
    points=[{"text": "Only where the offence is listed in 82(4)", "at": A("c07", "section")},
            {"text": "The offences alleged here are not listed", "tone": "no", "at": A("c07", "could")}])
cue(type="point", t0=A("c07", "proclamation"), t1=E("c07") + 0.05, text="Proclamation and the Nov 2014 declaration: set aside", icon="check", accent=True, at=A("c07", "proclamation"))

# ── 4 · warrants and extradition ─────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c08"), t1=A("c08", "warrants") - 0.05, text="“does not absolve the Petitioner of his obligation to face the pending prosecution”", icon="scale", accent=True, at=A("c08", "this"))
cue(type="notequal", t0=A("c08", "warrants"), t1=E("c08") + 0.05, left="Warrants of arrest", right="Section 82 proclamation",
    at=A("c08", "warrants"), left_at=A("c08", "warrants"), sub="Distinct processes: the warrants of 2013, 2024 and 2026 remain unaffected", sub_at=A("c08", "unaffected"))
cue(type="point", t0=S("c09"), t1=A("c09", "so") - 0.05, text="India–Philippines Extradition Treaty (Arts. 8, 9): no proclaimed offender declaration needed", icon="landmark", at=A("c09", "treaty"))
cue(type="verdicts", t0=A("c09", "so"), t1=E("c09") + 0.05,
    rows=[{"text": "Stay of the 1 Jul 2026 order and the extradition?", "ok": False, "at": A("c09", "so"), "strike_at": A("c09", "stay")},
          {"text": "Red Notice, extradition request: this ruling alone requires no withdrawal", "ok": True, "at": A("c09", "red")},
          {"text": "Liberty: voluntary surrender under Treaty Art. 15", "ok": True, "at": A("c09", "request")}])
cue(type="point", t0=S("c10"), t1=E("c10") + 0.05, text="Like · Share · Subscribe · lawworld.ai", icon="check", accent=True, at=A("c10", "like"))
