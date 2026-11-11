# Electronic Evidence and the Certificate under Section 63 BSA - CONCEPT VIDEO (legal-concept explainer, Cause of Action build): panel
# cues, run by split/build_course_plan.py (helpers: at S E cue fx have r3 PEND). Script: split/scripts/elv.txt (no owner storyboard; its
# // header lists the bare-act wording of BSA 2(1)(d), 57, 61-63, 170 and the Schedule, the case paragraphs and the panel rules, all
# checked 10-11-2026). 39 clips, c39 = the closing line.
# Held to the script header's panel rules:
#  - Anvar (2014) and Arjun Panditrao (2020) interpret s.65B of the OLD Evidence Act: a kicker "OLD EVIDENCE ACT · SECTION 65B" runs
#    over c26-c32 and every bar of theirs says OLD ACT; the only BSA ruling is the Pune Bar Association order (c24-c25). The two
#    politicians' names are never spoken; they appear on the case bars only (Arjun's long name is set on two rows of one bar so it
#    stays at full size);
#  - c29 (the original-device route) is the 2020 ruling under the old Act: its first step says so, its note tells the viewer to file the
#    certificate under the BSA; no "no certificate needed" card anywhere;
#  - Pune Bar (22.05.2026): the challenge was DECLINED (never "upheld"); hash value = an electronic fingerprint (c24, para 4); who may
#    sign Part B is an OPEN question (c25 note, paras 6-7), never shown as settled;
#  - Nisha, her bakery in Belagavi, the burglary, the pen drive, the chats and the call records are HYPOTHETICAL (kicker over c04-c05,
#    c11, c20); no accused, no "thief"; Nisha is "who runs the DVR", not "the party" (c20); no SECONDARY stamp on the pen drive (c11);
#  - the hash illustration (c22) uses real SHA256 values of the two texts shown (computed 10-11-2026 with shasum -a 256, no newline):
#    "Paid Rs. 5,000" -> 61e1c15d…4b9675, "Paid Rs. 8,000" -> 9eaa9cef…f7d2e2; c23's bar states the limit: a match shows the data is
#    unchanged, not who made the recording or that it is true;
#  - c32: later production is discretionary ("may") and subject to no serious prejudice; c33 "risks exclusion"; c34 no retention
#    number;
#  - on screen only (not narrated): s.2(1)(d) Illustration (vi) and s.2(1)(e)(ii) (c06), s.62 (c07), the old s.62's Explanations 1-3
#    (c08), s.57 Explanation 6 (c10), s.63(3) (c12 note), the old s.65B(4)'s signer (c16 note), Arjun para 58's "and" read as "or" (c17),
#    the Schedule's source particulars (c18), "Maintained" (c19), the hash algorithms (c21), s.39(2) / s.79A IT Act examiners (c25),
#    Arjun's network caveat (c29), Arjun paras 61-62 (c34).
# Case bars: name + court + year (or order date) + paragraph only - never SCC / AIR / INSC / SCR.
# Layout (07-11 lessons): the c01 question sits at y=215 with its stamp at y=900; lists stay <= 3 rows under a bar (the 4-row lists
# c19 and the c13-c14 checklist carry no bar); one-row compare cards under a bar.
def A(c, w, n=1, d=-0.08): return r3(at(c, w, n) + d)

STING = {"kicker": "EVIDENCE LAW · BSA EXPLAINED", "title": "Electronic Evidence under Section 63 BSA",
         "sub": "The certificate, its Schedule and the hash value"}
ENDCARD = {"title": "Electronic Evidence under Section 63 BSA", "line": "Part A + Part B + the hash value · file it with every submission",
           "sub": "LawWorld: legal research for advocates"}
HYPO = "HYPOTHETICAL EXAMPLE"
OLDK = "OLD EVIDENCE ACT · SECTION 65B"
ANVAR = "Anvar P.V. v. P.K. Basheer"                               # SC, 18.09.2014, three Judges (old Act, s.65B)
ANVAR_TAG = "SUPREME COURT · 2014 · THREE JUDGES · OLD ACT"
ARJ_TAG = "SUPREME COURT · 2020 · THREE JUDGES · OLD ACT"       # SC, 14.07.2020, three Judges (old Act, s.65B)
def ARJ(para): return [{"name": "Arjun Panditrao Khotkar v."}, {"name": "Kailash Kushanrao Gorantyal", "cite": para}]
PUNE = "Pune Bar Association v. Union of India"                  # SC, order of 22.05.2026 (BSA s.63(4))
PUNE_TAG = "SUPREME COURT OF INDIA · ORDER OF 22.05.2026"

# ── 1 · can a video clip be evidence? ───────────────────────────────────────────────────────────────────────────────────────────
# the question and its stamp hold through "Hi, I'm Ravishankar from LawWorld" (the name tag sits on the presenter side)
cue(type="question", t0=S("c01"), t1=A("c02", "today") - 0.05, at=A("c01", "footage"),
    text="The CCTV footage shows everything. Will the court admit it?", hl="admit it?", y=215)
cue(type="stamp", t0=A("c01", "refuse") - 0.05, t1=A("c02", "today") - 0.05, at=A("c01", "refuse"), line1="IT MAY BE REFUSED",
    line2="FOR WANT OF ONE CERTIFICATE", y=900)
cue(type="list", t0=A("c02", "today") - 0.05, t1=E("c02") + 0.05, head="Today", head_at=A("c02", "today"),
    items=[{"n": 1, "text": "Electronic evidence", "at": A("c02", "electronic")},
           {"n": 2, "text": "The certificate under Section 63 BSA", "at": A("c02", "certificate")}])
cue(type="cite", t0=A("c02", "bharatiya"), t1=E("c02") + 0.05, at=A("c02", "bharatiya"), tag="THE LAW",
    text="Bharatiya Sakshya Adhiniyam, 2023 (BSA)", icon="book-open")
cue(type="flow", t0=S("c03"), t1=E("c03") + 0.05, head="The old section replaced", head_at=A("c03", "replaced"),
    steps=[{"label": "Section 65B", "sub": "old Evidence Act, 1872", "icon": "book", "tone": "muted", "at": A("c03", "section")},
           {"label": "Section 63 BSA", "sub": "in force from 1 July 2024", "icon": "book-open", "tone": "ok", "at": A("c03", "july")}])
cue(type="kicker", t0=S("c04"), t1=E("c05") + 0.05, at=S("c04") + 0.05, text=HYPO)
cue(type="flow", t0=S("c04"), t1=E("c04") + 0.05,
    steps=[{"label": "Nisha's bakery", "sub": "in Belagavi", "icon": "house", "at": A("c04", "hypothetical")},
           {"label": "Burgled at night", "icon": "triangle-alert", "at": A("c04", "burgled")},
           {"label": "Her CCTV camera records it", "icon": "video", "tone": "ok", "at": A("c04", "camera")}])
cue(type="list", t0=S("c05"), t1=E("c05") + 0.05, head="The police rely on", head_at=A("c05", "police"),
    items=[{"n": 1, "text": "The footage, copied onto a pen drive", "at": A("c05", "copy")},
           {"n": 2, "text": "WhatsApp chats", "at": A("c05", "whatsapp")},
           {"n": 3, "text": "Call records", "at": A("c05", "call")}])

# ── 2 · electronic records are documents ─────────────────────────────────────────────────────────────────────────────────────────
cue(type="question", t0=S("c06"), t1=A("c06", "under") - 0.05, at=A("c06", "are"), text="Are these documents?", hl="documents?")
cue(type="section", t0=A("c06", "under") - 0.05, t1=E("c06") + 0.05, at=A("c06", "under"), act="BSA, 2023", num="2(1)(d)",
    title="“Document”",
    points=[{"text": "“… and includes electronic and digital records”", "at": A("c06", "includes")}],
    note={"text": "Illustration (vi): emails, server logs, messages, websites, locational evidence, voice mail", "icon": "info",
          "at": A("c06", "digital")})
cue(type="cite", t0=A("c06", "electronic"), t1=E("c06") + 0.05, at=A("c06", "electronic"), tag="DOCUMENTARY EVIDENCE",
    text="s.2(1)(e)(ii): all documents “including electronic or digital records” produced for the Court", icon="book-open")
cue(type="strike", t0=S("c07"), t1=E("c07") + 0.05, text="Refusing a record only because it is electronic", icon="ban",
    at=A("c07", "section"), strike_at=A("c07", "electronic"))
cue(type="point", t0=A("c07", "but") - 0.05, t1=E("c07") + 0.05, text="But Section 63 still applies", icon="book-open", accent=True,
    at=A("c07", "but"))
cue(type="cite", t0=A("c07", "bars"), t1=A("c07", "but"), at=A("c07", "bars"), tag="BSA 61",
    text="“… shall, subject to section 63, have the same legal effect, validity and enforceability as other document”", icon="book-open")
cue(type="cite", t0=A("c07", "but"), t1=E("c07") + 0.05, at=A("c07", "but"), tag="BSA 62",
    text="“The contents of electronic records may be proved in accordance with the provisions of section 63”", icon="book-open")

# ── 3 · primary or secondary? ────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c08"), t1=E("c08") + 0.05, at=A("c08", "primary"), act="BSA, 2023", num="57",
    title="Primary evidence",
    points=[{"text": "“The document itself produced for the inspection of the Court”", "at": A("c08", "document")},
            {"text": "New: Explanations 4 to 7, for electronic records", "at": A("c08", "explanations")}],
    note={"text": "The old Act's Section 62 had Explanations 1 to 3 only", "icon": "info", "at": A("c08", "electronic")})
cue(type="compare", t0=S("c09"), t1=E("c09") + 0.05, head="Section 57: electronic records", head_at=A("c09", "where"),
    cols=[{"title": "Explanation 4", "icon": "copy", "at": A("c09", "multiple")},
          {"title": "Explanation 7", "icon": "database", "at": A("c09", "storage")}],
    rows=[{"cells": ["Created or stored in multiple files, at once or in sequence", "In multiple storage spaces, temporary files too"],
           "cells_at": [A("c09", "files"), A("c09", "temporary")]}],
    verdict={"text": "Each is primary evidence", "icon": "check", "at": A("c09", "each")})
cue(type="splitcard", t0=S("c10"), t1=E("c10") + 0.05,
    left={"title": "EXPLANATION 5", "text": "a record produced from proper custody is primary evidence", "icon": "lock", "at": A("c10", "and")},
    right={"title": "UNLESS", "text": "it is disputed", "icon": "scale", "at": A("c10", "unless")})
# Explanation 6's bar sits under c10's splitcard: under c09's compare it shrank the cells to ~20 px (10-11 mock check)
cue(type="cite", t0=S("c10") + 0.1, t1=E("c10") + 0.05, at=S("c10") + 0.1, tag="BSA 57 · EXPLANATION 6",
    text="A video stored while transmitted, broadcast or transferred: “each of the stored recordings is primary evidence”", icon="info")
cue(type="kicker", t0=S("c11"), t1=E("c11") + 0.05, at=S("c11") + 0.05, text=HYPO)
cue(type="flow", t0=S("c11"), t1=E("c11") + 0.05,
    steps=[{"label": "Nisha's pen drive", "icon": "folder-open", "at": A("c11", "pen")},
           {"label": "A copy from the DVR", "icon": "copy", "at": A("c11", "copy")},
           {"label": "A computer output", "sub": "governed by Section 63", "icon": "file-check", "tone": "ok", "at": A("c11", "computer")}])
cue(type="cite", t0=A("c11", "computer"), t1=E("c11") + 0.05, at=A("c11", "computer"), tag="BSA 63(1) · THE COMPUTER OUTPUT",
    text="Information “copied in optical or magnetic media or semiconductor memory”", icon="book-open")

# ── 4 · Section 63: the conditions ──────────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c12"), t1=E("c12") + 0.05, at=A("c12", "sub"), act="BSA, 2023", num="63(1)",
    title="The computer output",
    points=[{"text": "“Deemed to be also a document”", "at": A("c12", "deems")},
            {"text": "Admissible “without further proof or production of the original”", "at": A("c12", "admissible")},
            {"text": "“If the conditions mentioned in this section are satisfied”", "at": A("c12", "conditions")}],
    note={"text": "Section 63(3): standalone, networked or via an intermediary, all the devices count as one", "icon": "info",
          "at": A("c12", "met")})
cue(type="checklist", t0=S("c13"), t1=E("c14") + 0.05, head="Section 63(2): the conditions", head_at=A("c13", "sub"),
    items=[{"n": "a", "text": "Used regularly, for an activity of the person in lawful control", "at": A("c13", "regularly")},
           {"n": "b", "text": "Such information regularly fed in, in the ordinary course", "at": A("c13", "information")},
           {"n": "c", "text": "Operating properly, or a fault did not affect the record", "at": A("c14", "worked")},
           {"n": "d", "text": "The record reproduces, or is derived from, what was fed in", "at": A("c14", "reproduces")}])

# ── 5 · the certificate and its Schedule ────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c15"), t1=E("c15") + 0.05, at=A("c15", "sub"), act="BSA, 2023", num="63(4)",
    title="A certificate is required",
    points=[{"text": "(a) Identifies the record and “the manner in which it was produced”", "at": A("c15", "identifies")},
            {"text": "(b) Particulars of the device", "at": A("c15", "describes")},
            {"text": "(c) Deals with the Section 63(2) conditions", "at": A("c15", "addresses")}])
cue(type="flow", t0=S("c16"), t1=E("c16") + 0.05, head="Signed by", head_at=A("c16", "signed"),
    steps=[{"label": "A person in charge", "sub": "of the device, or of the relevant activities", "icon": "user-round", "at": A("c16", "person")},
           {"label": "And an expert", "icon": "badge-check", "tone": "ok", "at": A("c16", "expert")}],
    note={"text": "New: Section 65B(4) (old Evidence Act) asked for no expert", "icon": "info", "at": A("c16", "that")})
cue(type="splitcard", t0=S("c17"), t1=E("c17") + 0.05,
    left={"title": "AT EACH INSTANCE", "text": "with the record, every time it is submitted for admission", "icon": "file-check",
          "at": A("c17", "accompany")},
    right={"title": "IT MAY BE STATED", "text": "to the best of knowledge and belief", "icon": "pen-line", "at": A("c17", "best")})
cue(type="cite", t0=A("c17", "stated"), t1=E("c17") + 0.05, at=A("c17", "stated"), tag="OLD ACT · ARJUN PANDITRAO, SC 2020, PARA 58",
    text="Under Section 65B, knowledge “and” belief was read as knowledge “or” belief", icon="info")
cue(type="compare", t0=S("c18"), t1=E("c18") + 0.05, head="The Schedule: the certificate form", head_at=A("c18", "schedule"),
    cols=[{"title": "Part A", "icon": "user-round", "at": A("c18", "part")},
          {"title": "Part B", "icon": "badge-check", "at": A("c18", "part", 3)}],      # "part" #2 is "party"
    rows=[{"cells": ["“To be filled by the Party”", "“To be filled by the Expert”"], "cells_at": [A("c18", "party"), A("c18", "expert")]}],
    verdict={"text": "Both identify the source device", "icon": "smartphone", "at": A("c18", "both")})
cue(type="cite", t0=A("c18", "both"), t1=E("c18") + 0.05, at=A("c18", "both"), tag="THE SCHEDULE · THE SOURCE",
    text="Computer, DVR, mobile, flash drive, CD/DVD, server or cloud · make, model, serial no., IMEI or MAC", icon="info")
cue(type="list", t0=S("c19"), t1=E("c19") + 0.05, head="Part A: the party affirms", head_at=A("c19", "part"),
    items=[{"n": 1, "text": "Lawful control", "at": A("c19", "lawful")},
           {"n": 2, "text": "Regular use", "at": A("c19", "regular")},
           {"n": 3, "text": "Proper working", "at": A("c19", "proper")},
           {"n": 4, "text": "Owned, maintained, managed or operated by me", "at": A("c19", "own")}])
cue(type="kicker", t0=S("c20"), t1=E("c20") + 0.05, at=S("c20") + 0.05, text=HYPO)
cue(type="splitcard", t0=S("c20"), t1=E("c20") + 0.05,
    left={"title": "COULD SIGN PART A", "text": "Nisha, who runs the DVR", "icon": "user-round", "at": A("c20", "bakery")},
    right={"title": "PART B", "text": "an expert", "icon": "badge-check", "at": A("c20", "expert")})

# ── 6 · hash value: a digital fingerprint ───────────────────────────────────────────────────────────────────────────────────────
cue(type="flow", t0=S("c21"), t1=E("c21") + 0.05, head="In Part A and in Part B", head_at=A("c21", "both"),
    steps=[{"label": "The hash value", "sub": "of the electronic record", "icon": "key-round", "at": A("c21", "hash")},
           {"label": "The algorithm", "sub": "SHA1, SHA256, MD5 or another legally acceptable standard", "icon": "layers",
            "at": A("c21", "algorithm")},
           {"label": "A hash report", "sub": "enclosed with the certificate", "icon": "file-check", "tone": "ok", "at": A("c21", "report")}])
cue(type="kicker", t0=S("c22"), t1=E("c22") + 0.05, at=S("c22") + 0.05, text="ILLUSTRATION · SHA256")
cue(type="compare", t0=S("c22"), t1=E("c22") + 0.05, head="A short code from a file's contents", head_at=A("c22", "hash"),
    cols=[{"title": "The file", "icon": "file-text", "at": A("c22", "short")},
          {"title": "One character changed", "icon": "file-pen-line", "at": A("c22", "change")}],
    rows=[{"cells": ["“Paid Rs. 5,000”", "“Paid Rs. 8,000”"], "cells_at": [A("c22", "calculated"), A("c22", "character")]},
          {"cells": ["61e1c15d…4b9675", "9eaa9cef…f7d2e2"], "cells_at": [A("c22", "contents"), A("c22", "hash", 2)]}])
cue(type="equation", t0=S("c23"), t1=E("c23") + 0.05,
    terms=[{"text": "HASH OF THE COPY IN COURT", "at": A("c23", "so")},
           {"op": "=", "text": "HASH IN THE CERTIFICATE", "at": A("c23", "same")},
           {"op": "→", "text": "UNCHANGED SINCE IT WAS RECORDED", "result": True, "at": A("c23", "data")}])
cue(type="cite", t0=A("c23", "changed"), t1=E("c23") + 0.05, at=A("c23", "changed"), tag="ITS LIMIT",
    text="A match shows the data is unchanged: not who made the recording, or that it is true", icon="info")
cue(type="point", t0=S("c24"), t1=A("c24", "it") - 0.05, text="May 2026: a challenge to this rule, declined", icon="gavel",
    at=A("c24", "may"))
cue(type="quote", t0=A("c24", "it") - 0.05, t1=E("c24") + 0.05, at=A("c24", "it"), reveal=r3(A("c24", "ensuring") - A("c24", "it")),
    text="Hash value of an electronic data is synonymous with an electronic fingerprint and provides a sure way of identifying and "
         "verifying digital data",
    hl=["synonymous with an electronic fingerprint"],
    note={"text": "Included: “to ensure its authenticity and integrity”", "at": A("c24", "ensuring")})
cue(type="cite", t0=A("c24", "supreme"), t1=E("c24") + 0.05, at=A("c24", "supreme"), tag=PUNE_TAG,
    cases=[{"name": PUNE, "cite": "para 4"}])
cue(type="flow", t0=S("c25"), t1=E("c25") + 0.05, head="Part B: what the Court observed", head_at=A("c25", "observed"),
    steps=[{"label": "Notified examiners", "sub": "s.79A IT Act · BSA s.39(2)", "icon": "badge-check", "at": A("c25", "notified")},
           {"label": "Or a person the court finds skilled", "sub": "in computer science and cyber forensics", "icon": "search-check",
            "at": A("c25", "skilled")}],
    note={"text": "The question of law kept open: no conclusive opinion", "icon": "info", "at": A("c25", "kept")})
cue(type="cite", t0=S("c25") + 0.05, t1=E("c25") + 0.05, at=S("c25") + 0.05, tag=PUNE_TAG,
    cases=[{"name": PUNE, "cite": "paras 6–7"}])

# ── 7 · what the Supreme Court held (both cases under the OLD Act) ──────────────────────────────────────────────────────────────
cue(type="kicker", t0=S("c26"), t1=E("c32") + 0.05, at=S("c26") + 0.05, text=OLDK)
cue(type="flow", t0=S("c26"), t1=E("c26") + 0.05,
    steps=[{"label": "2014", "sub": "three judges of the Supreme Court", "icon": "landmark", "at": A("c26", "fourteen")},
           {"label": "Section 65B (old Evidence Act)", "sub": "the certificate", "icon": "file-check", "at": A("c26", "section")},
           {"label": "Mandatory", "sub": "for secondary electronic evidence", "icon": "shield-check", "tone": "ok", "at": A("c26", "mandatory")}])
cue(type="cite", t0=A("c26", "supreme"), t1=E("c26") + 0.05, at=A("c26", "supreme"), tag=ANVAR_TAG,
    cases=[{"name": ANVAR, "cite": "para 22"}])
cue(type="splitcard", t0=S("c27"), t1=E("c27") + 0.05,
    left={"title": "THE RISK", "text": "“more susceptible to tampering, alteration, transposition, excision”", "icon": "triangle-alert",
          "at": A("c27", "electronic")},
    right={"title": "THE SAFEGUARD", "text": "the certificate, to “ensure the source and authenticity”", "icon": "shield-check",
           "at": A("c27", "safeguards")})
cue(type="cite", t0=S("c27") + 0.05, t1=E("c27") + 0.05, at=S("c27") + 0.05, tag=ANVAR_TAG,
    cases=[{"name": ANVAR, "cite": "para 16"}])
# one timeline for the whole clip: a strike from "Oral" on left the 2020 node on screen for only ~0.5 s
cue(type="timeline", t0=S("c28"), t1=E("c28") + 0.05,
    nodes=[{"label": "2014 · THREE JUDGES", "value": "Mandatory", "sub": "for secondary electronic evidence", "at": A("c28", "in")},
           {"label": "2020 · THREE JUDGES", "value": "A condition precedent", "sub": "to admissibility", "at": A("c28", "condition")},
           {"label": "ORAL EVIDENCE", "value": "Cannot replace it", "sub": "in place of the certificate", "tone": "red", "at": A("c28", "oral")}])
cue(type="cite", t0=A("c28", "another"), t1=E("c28") + 0.05, at=A("c28", "another"), tag=ARJ_TAG, cases=ARJ("para 59"))
# no head (no room above the old-Act bar): the first step builds on "held" so the panel is never empty; the network caveat sits
# under the witness-box step, the BSA advice in the note
cue(type="flow", t0=S("c29"), t1=E("c29") + 0.05,
    steps=[{"label": "The original produced", "sub": "a 2020 ruling under the old Act", "icon": "smartphone", "at": A("c29", "held")},
           {"label": "Its owner in the witness box", "sub": "not a network that cannot come to court", "icon": "user-round",
            "at": A("c29", "owner")},
           {"label": "Proves the device is his", "sub": "owned and/or operated by him", "icon": "check", "tone": "ok", "at": A("c29", "proves")}],
    note={"text": "Under the BSA: file the certificate", "icon": "info", "at": A("c29", "device")})
cue(type="cite", t0=A("c29", "held"), t1=E("c29") + 0.05, at=A("c29", "held"), tag=ARJ_TAG, cases=ARJ("paras 32, 72(b)"))

# ── 8 · when the certificate is missing (Arjun Panditrao, old Act) ──────────────────────────────────────────────────────────────
cue(type="question", t0=S("c30"), t1=A("c30", "the", 2) - 0.05, at=A("c30", "what"),
    text="What if the person who must sign refuses?", hl="refuses?")
cue(type="flow", t0=A("c30", "the", 2) - 0.05, t1=E("c30") + 0.05,
    steps=[{"label": "Apply to the court", "icon": "file-pen-line", "at": A("c30", "apply")},
           {"label": "It summons that person", "icon": "gavel", "at": A("c30", "summon")},
           {"label": "To produce the certificate", "icon": "file-check", "tone": "ok", "at": A("c30", "produce")}])
cue(type="cite", t0=A("c30", "the", 2), t1=E("c30") + 0.05, at=A("c30", "the", 2), tag=ARJ_TAG, cases=ARJ("paras 45, 50"))
cue(type="quote", t0=S("c31"), t1=E("c31") + 0.05, at=A("c31", "in"), reveal=r3(A("c31", "begins") - A("c31", "in")),
    text="… the electronic evidence, i.e. the computer output, has to be furnished at the latest before the trial begins",
    hl=["at the latest before the trial begins"],
    note={"text": "Why: so the accused can prepare a defence", "at": A("c31", "defence")})
cue(type="cite", t0=S("c31") + 0.05, t1=E("c31") + 0.05, at=S("c31") + 0.05, tag=ARJ_TAG, cases=ARJ("para 52"))
cue(type="splitcard", t0=S("c32"), t1=E("c32") + 0.05,
    left={"title": "UNTIL THE HEARING IS OVER", "text": "the judge may allow the certificate later", "icon": "gavel", "at": A("c32", "until")},
    right={"title": "ONLY IF", "text": "no serious or irreversible prejudice to the accused", "icon": "scale", "at": A("c32", "accused")})
cue(type="cite", t0=S("c32") + 0.05, t1=E("c32") + 0.05, at=S("c32") + 0.05, tag=ARJ_TAG, cases=ARJ("paras 54, 57"))

# ── 9 · screenshots, emails and call records ────────────────────────────────────────────────────────────────────────────────────
cue(type="equation", t0=S("c33"), t1=A("c33", "without") - 0.05,
    terms=[{"text": "A SCREENSHOT OR A PRINTOUT", "at": A("c33", "whatsapp")},
           {"op": "=", "text": "A COMPUTER OUTPUT TOO", "result": True, "at": A("c33", "computer")}])
cue(type="point", t0=A("c33", "without") - 0.05, t1=E("c33") + 0.05, text="Without a proper certificate, it risks exclusion",
    icon="triangle-alert", at=A("c33", "without"))
cue(type="cite", t0=A("c33", "computer"), t1=E("c33") + 0.05, at=A("c33", "computer"), tag="BSA 63(1)",
    text="Information “printed on paper … produced by a computer or any communication device”", icon="book-open")
cue(type="flow", t0=S("c34"), t1=E("c34") + 0.05,
    steps=[{"label": "Call records", "icon": "smartphone", "at": A("c34", "call")},
           {"label": "The provider's system", "icon": "database", "at": A("c34", "system")},
           {"label": "Its responsible officer certifies", "icon": "signature", "tone": "ok", "at": A("c34", "officer")}],
    note={"text": "Providers keep them only for a limited time", "icon": "clock", "at": A("c34", "limited")})
cue(type="cite", t0=A("c34", "providers"), t1=E("c34") + 0.05, at=A("c34", "providers"), tag=ARJ_TAG, cases=ARJ("paras 61–62"))
cue(type="list", t0=S("c35"), t1=E("c35") + 0.05, head="Common mistakes", head_at=A("c35", "common"),
    items=[{"n": "!", "text": "A screenshot with no certificate", "at": A("c35", "screenshot")},
           {"n": "!", "text": "A signer with no responsibility for the device", "at": A("c35", "signer")},
           {"n": "!", "text": "No expert part: Part B missing", "at": A("c35", "expert")}])

# ── 10 · old Act or new? your checklist ─────────────────────────────────────────────────────────────────────────────────────────
cue(type="section", t0=S("c36"), t1=E("c36") + 0.05, at=A("c36", "section"), act="BSA, 2023", num="170",
    title="Pending matters",
    points=[{"text": "The Indian Evidence Act, 1872 is repealed", "at": A("c36", "seventy")},
            {"text": "Pending: any application, trial, inquiry, investigation, proceeding or appeal", "at": A("c36", "trials")},
            {"text": "Dealt with under the old Evidence Act", "at": A("c36", "continue")}])
# "check" #1 is "checklist" (at() prefix-matches words of 4+ letters): #2 is "Check which law applies"
cue(type="checklist", t0=S("c37"), t1=E("c37") + 0.05, head="Your checklist", head_at=A("c37", "finally"),
    items=[{"n": 1, "text": "Check which law applies: Section 170", "at": A("c37", "check", 2)},
           {"n": 2, "text": "Preserve the original device", "at": A("c37", "preserve")},
           {"n": 3, "text": "Make the copy, with its hash value", "at": A("c37", "make")}])
cue(type="flow", t0=S("c38"), t1=E("c38") + 0.05,
    steps=[{"label": "Part A", "sub": "signed by the person in charge", "icon": "signature", "at": A("c38", "part")},
           {"label": "Part B", "sub": "signed by an expert", "icon": "badge-check", "at": A("c38", "part", 2)},
           {"label": "File the certificate", "sub": "with every submission", "icon": "file-check", "tone": "ok", "at": A("c38", "file")}])
cue(type="cite", t0=A("c38", "file"), t1=E("c38") + 0.05, at=A("c38", "file"), tag="SECTION 63(4) BSA",
    text="“at each instance where it is being submitted for admission”", icon="book-open")
cue(type="point", t0=S("c39"), t1=E("c39") + 0.05, text="Like · Share · Subscribe · lawworld.ai",
    icon="check", accent=True, at=A("c39", "thanks"))
