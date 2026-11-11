# G. Pazhanivel v. S. Thilagavathy, 2026 INSC 1197, Civil Appeal No. 13154 of 2026, Supreme Court of India (Atul S. Chandurkar J.
# wrote it, Ujjal Bhuyan J.; pronounced 05.11.2026, REPORTABLE): panel cues, run by split/build_course_plan.py (helpers: at S E cue
# fx have r3 PEND). HOOK format (split/JUDGMENT_HOOK_FORMAT.md): c01 hook question (spoken to everyone, no "Advocates,"), c02
# curiosity, c03 "Hi, I'm Ravishankar" + bench, c04-c05 the plaintiff's case, c06-c07 the two courts below and both sides, c08 the
# LawWorld request, c09-c10 the verdict. DRAFT 06-11-2026, awaiting the owner's yes. Re-checked 11-11-2026 against the PDF: c03
# now "On the fifth of November," (brief shape); c10 verdicts name the Order IV Rule 2 register (20) and Section 122 CPC (20).
# Facts (para): appeal against the trial Court's order, upheld by the HC, rejecting the plaint under O.VII R.11 CPC prior to
# registration (1). PLAINTIFF'S CASE (2, 13; on cards only as "he says" / "the plaintiff says"): land settled on him by his son,
# registered settlement deed 26.02.2021; borrowed Rs.25,00,000 from the defendant's husband at 24% per month; on the husband's
# insistence a sale deed registered 15.03.2021 in the defendant's name; possession stayed with him; the sale deed only security;
# offered to repay Rs.25,00,000 with interest; the defendant avoided reconveying and attempted forcible possession on 25.05.2025;
# reliefs: declaration of title + permanent injunction, redemption of "the mortgage deed, styled as sale deed", mandatory injunction
# to reconvey (2). Principal District Judge, Cuddalore, before registration: heard the plaintiff, perused the documents; no re-sale
# provision in the sale deed, no agreement filed; plaint rejected, court fees refunded (3); verbatim: "The sale deed does not contain
# the resale provision. No agreement is filed by the plaintiff in mark of agreeing for resale." (12); Unnumbered O.S., order dated
# 11.07.2025 (19). Madras HC Division Bench: rejection proper, no inference of mortgage / conditional sale; "for lack of cause of
# action, the plaint was rightly rejected" (SC's account, 4); A.S. No. 970 of 2025, 16.10.2025 (19). Plaintiff: no O.VII R.11 before
# registration; registration a ministerial act; plaint discloses a cause of action (5, 10). Defendant: an outright sale, no inference
# of security; no bar to R.11 at any stage (6).
# Held: the trial Court erred in rejecting the plaint "after entering into the merits of the case"; the HC too erred (7); the
# plaintiff's pre-registration contention "cannot be accepted" (10); "In a given case, such power may be exercised even prior to
# registration of the plaint" (11); no clause of R.11 named (12); "On a meaningful reading of the entire plaint, it is evident that
# the same discloses a cause of action"; prayers not noticed; not permissible to ignore material averments or refuse to read the
# plaint as a whole (14); HC did not consider the evidence ground (15); "Likelihood of a suit being dismissed after trial does not
# furnish a ground for the Court to reject the plaint prior to the trial" ... "it has to go for trial" (16); rejection a "decree",
# a record of pre-registration rejections needed, O.VII R.13 (17). Orders: the trial Court's order of 11.07.2025 and the HC's
# judgment of 16.10.2025 set aside; "The plaint is restored for being duly registered"; suit to be decided in accordance with law;
# no expression on the merits (19); pre-registration rejections "shall be duly recorded in a register maintained for such purpose
# under Order IV Rule 2"; HCs may act under s.122 CPC (20); copies to the Registrars General of the HCs and the Directors of the
# State Judicial Academies (21); appeal allowed, no costs (22).
# Names: only the cause title on the cite card; loan, interest, security, possession and refusal shown as the plaintiff's case.
# List lines <= 52 chars. Official sci.gov.in portraits (brand/judges, same files as ddc).
FORMAT = "hook"   # build_course_plan.py: no opening sting, 15-frame lead (the cover), name tag on the "Ravishankar" clip

def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
ENDCARD = {"title": "Rejected before it was even registered?", "line": "Possible in a given case, but a likely loss at trial is no ground: this plaint was restored", "sub": "LawWorld: legal research for advocates"}

# ── 1 · thrown out before registration? (hook, curiosity, intro) ─────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "file"), text="Rejected before it is even registered, because the judge thinks you will lose. Can a court do that?", hl="Can a court do that?")
cue(type="flow", t0=S("c02"), t1=A("c02", "so") - 0.05, head="Security, or a sale?", head_at=S("c02") + 0.05,
    steps=[{"label": "The plaintiff says", "sub": "the sale deed was only security", "icon": "user", "at": A("c02", "plaintiff")},
           {"label": "Trial court", "sub": "rejects the plaint", "icon": "scale", "at": A("c02", "trial")},
           {"label": "High Court", "sub": "agrees", "icon": "landmark", "at": A("c02", "high")}])
cue(type="point", t0=A("c02", "so") - 0.05, t1=E("c02") + 0.05, text="So who was right?", icon="search", accent=True, at=A("c02", "so"))
cue(type="bench", t0=S("c03"), t1=E("c03") + 0.05, tag="Supreme Court of India · 5 November 2026",
    judges=[{"name": "Justice Ujjal Bhuyan", "photo": "../brand/judges/ujjal_bhuyan.jpg", "at": A("c03", "honourable")},
            {"name": "Justice Atul S. Chandurkar", "photo": "../brand/judges/atul_s_chandurkar.jpg", "at": A("c03", "honourable", 2)}])

# ── 2 · a loan and a sale deed (the plaintiff's case) ────────────────────────────────────────────────────────────────
cue(type="cite", t0=S("c04"), t1=E("c04") + 0.05, at=A("c04", "plaintiff"), tag="SUPREME COURT OF INDIA · 05.11.2026",
    cases=[{"name": "G. Pazhanivel v. S. Thilagavathy", "cite": "2026 INSC 1197 · Civil Appeal No. 13154 of 2026"}])
cue(type="timeline", t0=S("c04"), t1=E("c04") + 0.05,
    nodes=[{"label": "SETTLEMENT DEED, HE SAYS", "value": "26 Feb 2021", "sub": "his son settles the land on him", "at": A("c04", "settled")},
           {"label": "LOAN FROM HER HUSBAND", "value": "₹25 lakh", "sub": "at 24% a month, he says", "at": A("c04", "borrowed")}])
cue(type="list", t0=S("c05"), t1=E("c05") + 0.05, head="The plaintiff says", head_at=S("c05") + 0.05,
    items=[{"n": 1, "text": "Sale deed in her name, 15 March 2021: only security", "at": A("c05", "sale")},
           {"n": 2, "text": "He stayed in possession of the land", "at": A("c05", "possession")},
           {"n": 3, "text": "Offered to repay; the land was not returned", "at": A("c05", "offered")},
           {"n": 4, "text": "Suit: title, redemption, reconveyance, injunction", "at": A("c05", "sued")}])

# ── 3 · rejected at the door ─────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c06"), t1=A("c06", "sale") - 0.05, text="Principal District Judge, Cuddalore · unnumbered suit: plaint rejected", icon="gavel", accent=True, at=A("c06", "district"))
cue(type="point", t0=A("c06", "sale") - 0.05, t1=E("c06") + 0.05, text="“The sale deed does not contain the resale provision. No agreement is filed by the plaintiff in mark of agreeing for resale.”", icon="quote", at=A("c06", "sale"))
cue(type="point", t0=S("c07"), t1=A("c07", "defendant") - 0.05, text="Madras High Court bench, 16 Oct 2025: rightly rejected, no cause of action", icon="landmark", accent=True, at=A("c07", "madras"))
cue(type="list", t0=A("c07", "defendant") - 0.05, t1=E("c07") + 0.05, head="In the Supreme Court", head_at=A("c07", "defendant"),
    items=[{"n": 1, "text": "Defendant: an outright sale, not security", "at": A("c07", "real")},
           {"n": 2, "text": "Plaintiff: Rule 11 only after registration", "at": A("c07", "argued")},
           {"n": 3, "text": "Plaintiff: the plaint shows a cause of action", "at": A("c07", "rejected")}])

# ── 4 · before the verdict: the LawWorld request ─────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c08"), t1=A("c08", "follow") - 0.05, text="The verdict is next. First, a quick request…", icon="scale", accent=True, at=A("c08", "decided"))
cue(type="list", t0=A("c08", "follow") - 0.05, t1=E("c08") + 0.05, head="Follow LawWorld · lawworld.ai", head_at=A("c08", "follow"),
    items=[{"n": 1, "text": "Search SC and High Court judgments, cited to source", "at": A("c08", "india's")},
           {"n": 2, "text": "Draft petitions, plaints and notices with AI", "at": A("c08", "platform")},
           {"n": 3, "text": "Sign up free · ₹200 AI credit included", "at": A("c08", "advocates")}])

# ── 5 · what the Court held ──────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "plaint") - 0.05, text="What did the Supreme Court decide?", icon="scale", accent=True, at=A("c09", "finally"))
cue(type="list", t0=A("c09", "plaint") - 0.05, t1=E("c09") + 0.05, head="Order VII Rule 11 CPC", head_at=A("c09", "plaint"),
    items=[{"n": 1, "text": "Even before registration, in a given case", "at": A("c09", "registration")},
           {"n": 2, "text": "Read the whole plaint, meaningfully", "at": A("c09", "because")},
           {"n": 3, "text": "Likely to fail after trial? Not a ground", "at": A("c09", "fail")}])
cue(type="verdicts", t0=S("c10"), t1=E("c10") + 0.05,
    rows=[{"text": "Rejection of the plaint, and the High Court's order", "ok": False, "at": A("c10", "disclosed")},
          {"text": "Plaint discloses a cause of action", "ok": True, "at": A("c10", "cause")},
          {"text": "Restored for registration · no view on merits", "ok": True, "at": A("c10", "restored")},
          {"text": "Pre-registration rejection: Order IV Rule 2 register", "ok": True, "at": A("c10", "rejections")},
          {"text": "High Courts: Section 122 CPC, if rules lack it", "ok": True, "at": A("c10", "must")}])

MUSIC = {"file": "audio/bed_mixkit738_140s.mp3", "target_lufs": -21}   # owner 02-11-2026: trending-style royalty-free bed, audible under the voice
