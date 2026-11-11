# Writes yt_<set>_title.txt / yt_<set>_desc.txt for the 7-Nov concept videos.
# Chapter times = first spoken word of the chapter's clip in out/<set>/words.json (final 16:9 timeline). First chapter is 0:00.
import json, sys, os
PE = "/Users/admin/Downloads/New short/product-explainer"
OUT = os.path.expanduser("~/Downloads/LawWorld_posting_7to10nov")
BODY = """📖 Learn the law one concept at a time on LawWorld, India’s all-in-one AI platform for advocates.
✅ Search Supreme Court and High Court judgments, cited to source
✅ Draft petitions, plaints and notices with AI
✅ Track cases, hearings and e-Courts updates in one place
🎁 Sign up free, no credit card needed. ₹200 AI credit included.
👉 https://lawworld.ai
💬 WhatsApp: +91 81479 56600 (https://wa.me/918147956600)
📱 Android app: search “LawWorld” on Google Play

For educational purposes only. Not legal advice."""
SETS = {
 "bnb": dict(
  title="Bailable vs Non-Bailable Offences under BNSS | Sec 478, 480, 482 Explained",
  summary="Bailable and non-bailable offences under the BNSS, explained with simple examples. What bail means under Section 2(1)(b), how the First Schedule classifies offences, release as a right under Section 478 in a bailable case, the personal bond for a person who cannot find a surety, bail in non-bailable cases under Sections 480 and 483, how the court weighs an application, anticipatory bail under Section 482 and its exclusions, conditions after release under Section 485, and why cognizable does not automatically mean non-bailable.",
  chapters=[("c01","Does non-bailable mean no bail?"),("c04","What bail means"),("c07","A bailable offence"),("c12","No surety? Personal bond"),
            ("c16","Non-bailable can still get bail"),("c20","How the court decides"),("c24","Anticipatory bail"),("c29","After release"),
            ("c32","Bail vs cognizability"),("c36","The distinction to remember")],
  tags="#BNSS #Bail #BailableOffences #AnticipatoryBail #CriminalProcedure #LawWorld"),
 "chq": dict(
  title="Cheque Bounce Case Timeline | Section 138 NI Act: The Four Clocks Explained",
  summary="A cheque bounce complaint under Section 138 of the Negotiable Instruments Act runs on four clocks. The essentials and the presumption for the holder (Rangappa v. Sri Mohan), presenting the cheque within its validity, the 30-day demand notice after the bank's information, proving service, the 15 days the drawer gets to pay, why a complaint filed too early fails (Yogendra Pratap Singh v. Savitri Pandey), filing within one calendar month (Econ Antri), a worked example with dates, which court to approach, common mistakes and re-presentation (MSR Leathers).",
  chapters=[("c01","The four clocks"),("c03","The position of law"),("c07","Present the cheque in time"),("c10","The demand notice"),
            ("c13","Proving service"),("c16","Payment and reply"),("c19","Wait for the cause of action"),("c22","File within one month"),
            ("c25","A worked example"),("c29","Court and complaint"),("c33","Common mistakes"),("c37","Remember the sequence")],
  tags="#ChequeBounce #Section138 #NIAct #ChequeDishonour #LawWorld"),
 "csr": dict(
  title="Charge Sheet vs Closure Report under BNSS | Sec 193, 187, 230 Explained",
  summary="What happens when the police finish investigating. A charge sheet and a closure report under Section 193 of the BNSS, what a police report contains, a theft example, what the Magistrate can do with a closure report and the informant's right to be heard (Bhagwant Singh), the separate investigation timelines, the 60 or 90 days for default bail under Section 187(3), copies for the accused and the victim under Section 230, and further investigation with a supplementary report under Section 193(9).",
  chapters=[("c01","After the investigation"),("c06","What a charge sheet contains"),("c09","Example: a theft case"),("c12","When police recommend closure"),
            ("c16","The court and the informant"),("c22","Investigation timelines"),("c27","60 or 90 days and default bail"),("c30","Copies for the defence and victim"),
            ("c34","New evidence, further report"),("c38","Remember the difference")],
  tags="#BNSS #ChargeSheet #ClosureReport #CriminalProcedure #LawWorld"),
}
def ts(t):
    t = int(t); return f"{t//60}:{t%60:02d}"
for s in sys.argv[1:]:
    cfg = SETS[s]
    words = json.load(open(f"{PE}/out/{s}/words.json"))
    first = {}
    for w in words: first.setdefault(w["cid"], w["start"])
    lines, last = [], -99
    for i, (cid, name) in enumerate(cfg["chapters"]):
        t = 0 if i == 0 else max(0, first[cid] - 0.3)
        assert t - last >= 10, f"{s}: chapter {name} only {t-last:.1f}s after the previous one (YouTube needs 10 s)"
        lines.append(f"{ts(t)} {name}"); last = t
    assert len(cfg["title"]) <= 100, len(cfg["title"])
    desc = f"{cfg['summary']}\n\nChapters:\n" + "\n".join(lines) + f"\n\n{BODY}\n\n{cfg['tags']}"
    assert len(desc) <= 5000 and "<" not in desc and ">" not in desc
    open(f"{OUT}/yt_{s}_title.txt", "w").write(cfg["title"])
    open(f"{OUT}/yt_{s}_desc.txt", "w").write(desc)
    print(f"{s}: wrote title ({len(cfg['title'])} chars) + desc ({len(desc)} chars), {len(lines)} chapters, video {words[-1]['end']:.0f}s")
