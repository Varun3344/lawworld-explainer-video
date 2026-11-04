# Mangala Bhimrao Ingle v. The Additional Commissioner, Amravati Division & Ors., 2026 INSC 1193, C.A. @ SLP (C) No. 30772 of 2025
# (Pamidighantam Sri Narasimha J., Alok Aradhe J. - no named author; decided 04.11.2026, REPORTABLE on page 1): panel cues, run by
# split/build_course_plan.py (helpers: at S E cue fx have r3 PEND). A REFERENCE TO A LARGER BENCH WITH INTERIM PROTECTION, not a final
# ruling: nothing here says "struck down", "unconstitutional" or "invalid".
# HOOK format (split/JUDGMENT_HOOK_FORMAT.md): c01 hook question (spoken to everyone, no "Advocates,"), c02 curiosity, c03 "Hi, I'm
# Ravishankar" + bench, c04-c05 the Sarpanch's case, c06-c07 what has changed since 2003, c08 the LawWorld request, c09-c10 the decision.
# Facts (para): election as Sarpanch of Kakoda Gram Panchayat set aside, disqualified for having more than two children, Section
# 14(1)(j-1), Maharashtra Village Panchayats Act, 1959 (2); "laws that penalise having more than two children have lost their
# relevance. The foundation of such laws, i.e. the fear of overpopulation, has crumbled"; TFR "fallen from 3.02 to 1.9" since Javed;
# 2.1 the replacement rate (3); third child born 2014, elected in the 2022 elections (5); the enquiry was not the High Court's
# application of the laws: "We were concerned about the relevance of these laws when the very foundation for their articulation has
# changed" (6); Javed v. State of Haryana, (2003) 8 SCC 369: the two-child disqualification for panchayat positions upheld (Haryana
# Panchayati Raj Act, 1994); "the court relied on the then perception about population boom and its negative impact on the economy"
# (8); SRS: TFR 1.9 in 2024 (18); "below replacement level fertility" (20); aged 60+: about 8.3% (2014) to 9.7% (2024) (21); validity
# of the Maharashtra provision "has not been challenged before us" (31, 46); reference "to a larger bench for reconsideration of the
# ratio laid down in Javed", papers to the Chief Justice of India (66); the High Court's judgment stayed, she continues as Sarpanch,
# "The interim order shall continue until disposal of the Civil Appeal" (67).
# Names: the cause title on the cite card only; "Javed" on cards as the precedent's citation, never in speech. No section sign. List
# lines <= 52 chars. Bench photos: brand/judges/pamidighantam_sri_narasimha.jpg, alok_aradhe.jpg (official sci.gov.in portraits);
# "Justice P.S. Narasimha" on the card (nkp lesson: the full name wraps to three lines; it is spoken in full).
FORMAT = "hook"   # build_course_plan.py: no opening sting, 15-frame lead (the cover), name tag on the "Ravishankar" clip

def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110     # the citation bar's shadow ends inside the panel (one seamless screen)
PLAIN_BG = True   # owner 26-10-2026: the cards and the presenter on one plain cream screen
ENDCARD = {"title": "A third child, no election?", "line": "Laws penalising more than two children have lost their relevance, said the Court, without striking them down; the 2003 ruling goes to a larger bench, the interim stay continues", "sub": "LawWorld: legal research for advocates"}

# ── 1 · third child, no election? (hook, curiosity, intro) ──────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "child"), text="Should a third child stop you from contesting a village election? Do such laws still make sense today?", hl="Do such laws still make sense today?")
cue(type="timeline", t0=S("c02"), t1=A("c02", "should") - 0.05,
    nodes=[{"label": "A SARPANCH'S ELECTION", "value": "set aside", "sub": "more than two children · Maharashtra", "tone": "stop", "at": A("c02", "sarpanch's")},
           {"label": "INDIA'S FERTILITY RATE", "value": "1.9", "sub": "below the replacement level of 2.1", "at": A("c02", "fertility")}])
cue(type="point", t0=A("c02", "should") - 0.05, t1=E("c02") + 0.05, text="Should that rule still stand?", icon="search", accent=True, at=A("c02", "rule"))
cue(type="bench", t0=S("c03"), t1=E("c03") + 0.05, tag="Supreme Court of India · 4 November 2026",
    judges=[{"name": "Justice P.S. Narasimha", "photo": "../brand/judges/pamidighantam_sri_narasimha.jpg", "at": A("c03", "honourable")},
            {"name": "Justice Alok Aradhe", "photo": "../brand/judges/alok_aradhe.jpg", "at": A("c03", "honourable", 2)}])

# ── 2 · the Sarpanch's case ──────────────────────────────────────────────────────────────────────────────────────────────
cue(type="timeline", t0=S("c04"), t1=E("c04") + 0.05,
    nodes=[{"label": "THIRD CHILD", "value": "2014", "sub": "more than two children", "at": A("c04", "third")},
           {"label": "ELECTED SARPANCH", "value": "2022", "sub": "Kakoda Gram Panchayat", "at": A("c04", "became")},
           {"label": "ELECTION SET ASIDE", "value": "disqualified", "sub": "Section 14(1)(j-1) · 1959 Act", "tone": "stop", "at": A("c04", "disqualified")}])
cue(type="cite", t0=S("c05"), t1=E("c06") + 0.05, at=A("c05", "appealed"), tag="SUPREME COURT OF INDIA · 04.11.2026",
    cases=[{"name": "Mangala Bhimrao Ingle v. Addl. Commissioner, Amravati Division & Ors.", "cite": "2026 INSC 1193 · C.A. @ SLP (C) No. 30772 of 2025"}])
cue(type="list", t0=S("c05"), t1=A("c05", "court", 2) - 0.05, head="Before the Supreme Court", head_at=S("c05") + 0.05,
    items=[{"n": 1, "text": "An appeal against the High Court's judgment", "at": A("c05", "appealed")},
           {"n": 2, "text": "Section 14(1)(j-1) itself: not challenged", "at": A("c05", "maharashtra")}])
cue(type="point", t0=A("c05", "court", 2) - 0.05, t1=E("c05") + 0.05, text="“We were concerned about the relevance of these laws when the very foundation for their articulation has changed…”", icon="quote", accent=True, at=A("c05", "different"))

# ── 3 · what has changed ─────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c06"), t1=A("c06", "relied") - 0.05, text="Javed v. State of Haryana, (2003) 8 SCC 369: the two-child bar for panchayat posts upheld", icon="landmark", accent=True, at=A("c06", "upheld"))
cue(type="point", t0=A("c06", "relied") - 0.05, t1=E("c06") + 0.05, text="The Court in 2003 “relied on the then perception about population boom and its negative impact on the economy”", icon="quote", accent=True, at=A("c06", "perception"))
cue(type="timeline", t0=S("c07"), t1=E("c07") + 0.05,
    nodes=[{"label": "2003 · JAVED", "value": "TFR 3.02", "sub": "the fertility rate then", "at": A("c07", "fertility")},
           {"label": "2024 · SRS", "value": "TFR 1.9", "sub": "below the replacement level of 2.1", "tone": "stop", "at": A("c07", "nine")},
           {"label": "AGED 60 AND ABOVE", "value": "9.7%", "sub": "in 2024, from 8.3% in 2014", "at": A("c07", "population")}])

# ── 4 · before the verdict: the LawWorld request ─────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c08"), t1=A("c08", "follow") - 0.05, text="The verdict is next. First, a quick request…", icon="scale", accent=True, at=A("c08", "decided"))
cue(type="list", t0=A("c08", "follow") - 0.05, t1=E("c08") + 0.05, head="Follow LawWorld · lawworld.ai", head_at=A("c08", "follow"),
    items=[{"n": 1, "text": "Search SC and High Court judgments, cited to source", "at": A("c08", "india's")},
           {"n": 2, "text": "Draft petitions, plaints and notices with AI", "at": A("c08", "platform")},
           {"n": 3, "text": "Sign up free · ₹200 AI credit included", "at": A("c08", "advocates")}])

# ── 5 · what the Court held ──────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c09"), t1=A("c09", "in") - 0.05, text="What did the Supreme Court decide?", icon="scale", accent=True, at=A("c09", "finally"))
cue(type="point", t0=A("c09", "in") - 0.05, t1=A("c09", "but") - 0.05, text="“…laws that penalise having more than two children have lost their relevance. The foundation of such laws, i.e. the fear of overpopulation, has crumbled…”", icon="quote", accent=True, at=A("c09", "penalising"))
cue(type="point", t0=A("c09", "but") - 0.05, t1=E("c09") + 0.05, text="Not struck down: its validity was not challenged", icon="landmark", accent=True, at=A("c09", "strike"))   # fact-check 04-11-2026 (31, 46)
cue(type="verdicts", t0=S("c10"), t1=E("c10") + 0.05,
    rows=[{"text": "Javed (2003): to a larger bench to reconsider", "ok": True, "at": A("c10", "larger")},
          {"text": "The High Court's order: interim stay continues", "ok": True, "at": A("c10", "interim")},
          {"text": "She stays Sarpanch until the appeal is decided", "ok": True, "at": A("c10", "remains")}])

MUSIC = {"file": "audio/bed_mixkit738_140s.mp3", "target_lufs": -21}   # owner 02-11-2026: trending-style royalty-free bed, audible under the voice
