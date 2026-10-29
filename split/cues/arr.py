# Arrest Safeguards under the BNSS - concept-format topic reel (set arr), panel cues for split/build_course_plan.py.
# Source: the owner's storyboard 01_Arrest_Safeguards_LawWorld_v2.pdf (28-10-2026), condensed to ten clips.
# NO BENCH CARD: brand/judges/ has no Gavai CJI or Masih J. portrait and this is a topic explainer, not one judgment.
# Mihir Rajesh Shah v. State of Maharashtra, LAWWORLD 2025 SC 1125 (SC, 6 November 2025) rides on a text cite card at c04.
# Care from the PDF's "Points to preserve": the writing requirement and the two-hour rule are the Supreme Court's, not the
# bare statute's; the two hours sit INSIDE the 24-hour ceiling and never extend it; oral-first is exceptional only; the
# necessity test is tied to the up-to-seven-year cognizable category; arrest is not guilt.
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

CITE_B = 110      # the citation bar's shadow ends inside the panel (owner 26-10: one seamless screen)
PLAIN_BG = True   # owner 26-10-2026: cards and presenter on one plain cream screen, no blobs or star
STING = {"kicker": "BNSS · ARREST SAFEGUARDS", "title": "Arrest is a decision, not a reflex",
         "sub": "Notice to appear · grounds in writing · twenty four hours"}
ENDCARD = {"title": "Arrest safeguards under the BNSS", "line": "Notice, written grounds, intimation, counsel, and the Magistrate",
           "sub": "LawWorld: legal research for advocates"}

# ── 1 · an accusation and an arrest ──────────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c01"), t1=E("c01") + 0.05, at=A("c01", "ravi"),
    text="An FIR is registered. Must the police arrest him?", hl="Must the police arrest him?")
cue(type="point", t0=A("c01", "justified"), t1=E("c01") + 0.05, text="Arrest must be justified, never a reflex",
    icon="scale", accent=True, at=A("c01", "justified"))

# ── 2 · when arrest is necessary ─────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c02"), t1=E("c02") + 0.05, at=A("c02", "section"), act="BNSS, 2023", num="35(1)(b)",
    title="Arrest without a warrant",
    points=[{"text": "Cognizable offence punishable up to seven years", "at": A("c02", "seven")},
            {"text": "A reason to believe he committed it", "at": A("c02", "reason")},
            {"text": "A recorded satisfaction that arrest is necessary", "at": A("c02", "record")}],
    note={"text": "Reasons are recorded either way — arresting or not", "icon": "info", "at": A("c02", "necessity")})

# ── 3 · the notice to appear ─────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c03"), t1=E("c03") + 0.05, head="The notice to appear", head_at=S("c03") + 0.05,
    steps=[{"label": "BNSS 35(3): a written notice", "sub": "directing him to appear before the officer", "icon": "file-text", "at": A("c03", "notice")},
           {"label": "He complies, and keeps proof", "sub": "a record of every attendance", "icon": "check", "tone": "ok", "at": A("c03", "complies")},
           {"label": "Protection is conditional", "sub": "arrest only if fresh reasons are recorded", "icon": "alert-triangle", "tone": "warn", "at": A("c03", "fresh")}])

# ── 4 · knowing the grounds ──────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="cite", t0=A("c04", "mihir"), t1=E("c05") + 0.05, at=A("c04", "mihir"), tag="SUPREME COURT OF INDIA · 06.11.2025",
    cases=[{"name": "Mihir Rajesh Shah v. State of Maharashtra", "cite": "LAWWORLD 2025 SC 1125"}])
cue(type="list", t0=S("c04"), t1=A("c04", "mihir") - 0.05, head="The grounds of arrest", head_at=S("c04") + 0.05,
    items=[{"n": 1, "text": "Article 22(1): told the grounds of arrest", "at": A("c04", "article")},
           {"n": 2, "text": "BNSS 47: for every offence", "at": A("c04", "grounds")}])
cue(type="list", t0=A("c04", "mihir"), t1=E("c04") + 0.05, head="The Court's rule", head_at=A("c04", "mihir"),
    items=[{"n": 1, "text": "In writing", "at": A("c04", "written")},
           {"n": "→", "text": "In a language he understands", "at": A("c04", "language")}])
cue(type="verdicts", t0=S("c05"), t1=A("c05", "without") - 0.05,
    rows=[{"text": "Spoken first: exceptional circumstances only", "ok": False, "at": A("c05", "spoken")},
          {"text": "Written copy at least two hours before production for remand", "ok": True, "at": A("c05", "hours")}])
cue(type="point", t0=A("c05", "without"), t1=E("c05") + 0.05, text="Without it, the arrest and the remand are illegal",
    icon="x", accent=True, at=A("c05", "without"))

# ── 5 · recording the arrest ─────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c06"), t1=E("c06") + 0.05, head="Recording the arrest", head_at=S("c06") + 0.05,
    steps=[{"label": "BNSS 36: the arrest memorandum", "sub": "attested by a family member or respectable local person", "icon": "file-text", "at": A("c06", "memo")},
           {"label": "Countersigned by the arrested person", "sub": "the officer carries clear identification", "icon": "user-check", "at": A("c06", "attested")},
           {"label": "BNSS 48: someone he names is told", "sub": "the arrest and the place of detention, recorded at the station", "icon": "phone", "at": A("c06", "inform")}])

# ── 6 · counsel, health and special care ─────────────────────────────────────────────────────────────────────────────────────────
cue(type="list", t0=S("c07"), t1=E("c07") + 0.05, head="Counsel and bail", head_at=S("c07") + 0.05,
    items=[{"n": 1, "text": "BNSS 38: meet an advocate of his choice during interrogation", "at": A("c07", "advocate")},
           {"n": "!", "text": "During — not throughout — the interrogation", "at": A("c07", "throughout")},
           {"n": 2, "text": "BNSS 47(2): if bailable, he must be told he is entitled to bail", "at": A("c07", "bailable")}])
cue(type="list", t0=S("c08"), t1=E("c08") + 0.05, head="Health and special safeguards", head_at=S("c08") + 0.05,
    items=[{"n": 1, "text": "BNSS 56: reasonable care of health and safety in custody", "at": A("c08", "health")},
           {"n": 2, "text": "BNSS 43(5): a woman, after sunset and before sunrise — exceptionally, with a first class Judicial Magistrate's prior permission", "at": A("c08", "night")},
           {"n": 3, "text": "BNSS 35(7): infirm or above sixty, offence under three years — permission of a DSP or above", "at": A("c08", "infirm")}])

# ── 7 · twenty four hours, and the Magistrate ────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c09"), t1=A("c09", "magistrate") - 0.05, head="The outer limit", head_at=S("c09") + 0.05,
    steps=[{"label": "BNSS 57: production without unnecessary delay", "sub": "", "icon": "clock", "at": A("c09", "detention")},
           {"label": "BNSS 58: twenty four hours", "sub": "excluding necessary journey time", "icon": "alert-triangle", "tone": "warn", "at": A("c09", "hours")},
           {"label": "The two-hour rule sits inside it", "sub": "it never extends the ceiling", "icon": "info", "at": A("c09", "journey")}])
cue(type="list", t0=A("c09", "magistrate"), t1=A("c09", "guilt") - 0.05, head="What the Magistrate examines", head_at=A("c09", "magistrate"),
    items=[{"n": 1, "text": "BNSS 187: a lawful basis for further custody", "at": A("c09", "magistrate")},
           {"n": 2, "text": "The grounds of arrest, and any delay, in the remand papers", "at": A("c09", "grounds")}])
cue(type="point", t0=A("c09", "guilt"), t1=E("c09") + 0.05, text="Arrest does not establish guilt — that is for trial",
    icon="scale", accent=True, at=A("c09", "guilt"))

# ── 8 · close ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="point", t0=S("c10"), t1=E("c10") + 0.05, text="Like · Share · Subscribe · lawworld.ai",
    icon="check", accent=True, at=A("c10", "like"))
