# Surendra Manjhi & Anr. v. Union of India & Ors., 2026 INSC 1185, W.P. (C) No. 511 of 2022 with W.P. (C) Diary No. 32325 of 2026
# (Vikram Nath J. wrote it, Aparesh Kumar Singh J.; pronounced 02.11.2026, REPORTABLE on page 1): panel cues, run by
# split/build_course_plan.py (helpers: at S E cue fx have r3 PEND). DIRECTIONS IN PENDING WRIT PETITIONS, not a final disposal (38).
# HOOK format (split/JUDGMENT_HOOK_FORMAT.md): c01 hook question (spoken to everyone, no "Advocates,"), c02 curiosity, c03 "Hi, I'm
# Ravishankar" + bench, c04-c05 the rescue, c06-c07 why the delay / the petitions, c08 the LawWorld request, c09-c10 the directions.
# Facts (para): two Article 32 petitions (2, 3); rescued from a brick kiln, District Shahjahanpur, UP, 28.02.2019, taken from Bihar
# "on the pretext of repayment of a bonded debt", repatriated to Bihar with release certificates (5); several did not get the immediate
# financial assistance under the Central Sector Scheme; he got it only in 2022, "nearly three years after his rescue" (6, 18); the
# petitioners: 17 rescued with him still unpaid (6, 18, 30 - a party's figure, voiced as "the petitioners say"); Bihar: UP certificates
# not in the prescribed format (7); inter-State delays "frequently arise from inadequate coordination between the concerned
# authorities" (19); "rehabilitation delayed may, in substance, amount to rehabilitation denied" (18); Union's compliance affidavit
# 15.05.2026 with the revised SOP dated 14.05.2026 (10, 25). Directions: uniform SOP across the country, States/UTs comply in six months
# (25, 37); release certificate ordinarily within 24 hours of the determination, one format for all States (26); immediate assistance
# "shall ordinarily be disbursed within seven days of issuance of the release certificate, subject to necessary verification", not
# withheld merely because investigation or criminal proceedings remain pending (27); UP and Bihar to verify the 17 within one month,
# pay any amount found payable preferably within three and in any event within six months (30); petitions remain pending for
# monitoring (38), listed after seven months (39).
# Names: the cause title on the cite card only; no accusation against anyone. No section sign. List lines <= 52 chars.
# Bench photos: brand/judges/vikram_nath.jpg, aparesh_kumar_singh.jpg (official sci.gov.in portraits).
FORMAT = "hook"   # build_course_plan.py: no opening sting, 15-frame lead (the cover), name tag on the "Ravishankar" clip

def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
ENDCARD = {"title": "Freed from bondage, but unpaid?", "line": "Immediate aid ordinarily within 7 days of the release certificate, subject to verification; one SOP across India", "sub": "LawWorld: legal research for advocates"}

# ── 1 · freed, but still unpaid? (hook, curiosity, intro) ────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "worker"), text="Rescued from bonded labour: how long should the cash aid to restart life take? Days, months, or years?", hl="Days, months, or years?")
cue(type="counters", t0=S("c02"), t1=A("c02", "so") - 0.05, head="One brick-kiln rescue", head_at=S("c02") + 0.05,
    items=[{"value": 3, "unit": "YEARS", "label": "Nearly that long for his aid", "sub": "rescued 2019 · paid 2022", "at": A("c02", "nearly")},
           {"value": 17, "unit": "WORKERS", "label": "Still unpaid, the petitioners say", "sub": "rescued with him", "tone": "red", "at": A("c02", "seventeen")}])
cue(type="point", t0=A("c02", "so") - 0.05, t1=E("c02") + 0.05, text="So what is the deadline now?", icon="clock", accent=True, at=A("c02", "deadline"))
cue(type="bench", t0=S("c03"), t1=E("c03") + 0.05, tag="Supreme Court of India · 2 November 2026",
    judges=[{"name": "Justice Vikram Nath", "photo": "../brand/judges/vikram_nath.jpg", "at": A("c03", "honourable")},
            {"name": "Justice Aparesh Kumar Singh", "photo": "../brand/judges/aparesh_kumar_singh.jpg", "at": A("c03", "honourable", 2)}])

# ── 2 · the brick kiln ───────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=S("c04"), t1=E("c04") + 0.05, at=A("c04", "workers"), tag="SUPREME COURT OF INDIA · 02.11.2026",
    cases=[{"name": "Surendra Manjhi & Anr. v. Union of India & Ors.", "cite": "2026 INSC 1185 · W.P. (C) No. 511 of 2022 & connected"}])
cue(type="timeline", t0=S("c04"), t1=E("c04") + 0.05,
    nodes=[{"label": "RESCUED", "value": "28 Feb 2019", "sub": "a brick kiln, Shahjahanpur, UP", "at": A("c04", "rescued")},
           {"label": "TAKEN FROM BIHAR", "value": "a bonded debt", "sub": "on the pretext of repaying it", "at": A("c04", "pretext")}])
cue(type="flow", t0=S("c05"), t1=E("c05") + 0.05, head="Bonded Labour System (Abolition) Act, 1976", head_at=S("c05") + 0.05,
    steps=[{"label": "Sent home to Bihar", "sub": "repatriated after the rescue", "icon": "map-pin", "at": A("c05", "home")},
           {"label": "Release certificates", "sub": "issued by the authorities", "icon": "file-check", "at": A("c05", "release")},
           {"label": "Immediate aid: not for several", "sub": "Central Sector Scheme for Rehabilitation", "icon": "banknote", "tone": "stop", "at": A("c05", "several")}])

# ── 3 · why the delay? ───────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=S("c06"), t1=E("c06") + 0.05, at=A("c06", "bihar"), tag="SUPREME COURT OF INDIA · 02.11.2026",
    cases=[{"name": "Surendra Manjhi & Anr. v. Union of India & Ors.", "cite": "2026 INSC 1185 · W.P. (C) No. 511 of 2022 & connected"}])
cue(type="point", t0=S("c06"), t1=A("c06", "court") - 0.05, text="Bihar: some release certificates from UP were not in the prescribed format", icon="file-text", accent=True, at=A("c06", "certificates"))
cue(type="point", t0=A("c06", "court") - 0.05, t1=E("c06") + 0.05, text="Inter-State delays “frequently arise from inadequate coordination between the concerned authorities”", icon="quote", accent=True, at=A("c06", "noted"))
cue(type="timeline", t0=S("c07"), t1=E("c07") + 0.05,
    nodes=[{"label": "WRIT PETITION", "value": "2022", "sub": "a rescued worker · Article 32", "at": A("c07", "writ")},
           {"label": "NATIONAL CAMPAIGN", "value": "2026", "sub": "one uniform procedure", "at": A("c07", "campaign")},
           {"label": "UNION'S AFFIDAVIT", "value": "15 May 2026", "sub": "the revised SOP", "at": A("c07", "revised")}])

# ── 4 · before the verdict: the LawWorld request ─────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c08"), t1=A("c08", "follow") - 0.05, text="The verdict is next. First, a quick request…", icon="scale", accent=True, at=A("c08", "decided"))
cue(type="list", t0=A("c08", "follow") - 0.05, t1=E("c08") + 0.05, head="Follow LawWorld · lawworld.ai", head_at=A("c08", "follow"),
    items=[{"n": 1, "text": "Search SC and High Court judgments, cited to source", "at": A("c08", "india's")},
           {"n": 2, "text": "Draft petitions, plaints and notices with AI", "at": A("c08", "platform")},
           {"n": 3, "text": "Sign up free · ₹200 AI credit included", "at": A("c08", "advocates")}])

# ── 5 · what the Court directed ──────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "rescued") - 0.05, text="What did the Supreme Court decide?", icon="scale", accent=True, at=A("c09", "finally"))
cue(type="list", t0=A("c09", "rescued") - 0.05, t1=E("c09") + 0.05, head="Immediate financial assistance", head_at=A("c09", "rescued"),
    items=[{"n": 1, "text": "Ordinarily within 7 days of the release certificate", "at": A("c09", "ordinarily")},
           {"n": 2, "text": "Subject to the necessary verification", "at": A("c09", "seven")},
           {"n": 3, "text": "Not withheld merely because a case is pending", "at": A("c09", "certificate")}])
cue(type="list", t0=S("c10"), t1=A("c10", "uttar") - 0.05, head="One procedure for India", head_at=S("c10") + 0.05,
    items=[{"n": 1, "text": "The revised SOP, uniform across the country", "at": A("c10", "apply")},
           {"n": 2, "text": "Certificate: ordinarily 24 hours after identification", "at": A("c10", "india")},
           {"n": 3, "text": "States and UTs: comply within 6 months", "at": A("c10", "six")}])
cue(type="verdicts", t0=A("c10", "uttar") - 0.05, t1=E("c10") + 0.05,
    rows=[{"text": "UP + Bihar: verify the 17 workers within a month", "ok": True, "at": A("c10", "check")},
          {"text": "Dues found payable: preferably 3, at most 6 months", "ok": True, "at": A("c10", "dues")},
          {"text": "Not disposed of: kept pending for monitoring", "ok": True, "at": A("c10", "pending")}])

MUSIC = {"file": "audio/bed_mixkit738_140s.mp3", "target_lufs": -21}   # owner 02-11-2026: trending-style royalty-free bed, audible under the voice
