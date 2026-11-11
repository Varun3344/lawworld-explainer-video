# Writes yt_<set>_title.txt / yt_<set>_desc.txt for the 10-Nov concept videos.
# Chapter times = first spoken word of the chapter's clip in out/<set>/words.json (final 16:9 timeline). First chapter is 0:00.
import json, sys, os
PE = "/Users/admin/Downloads/New short/product-explainer"
OUT = os.path.expanduser("~/Downloads/LawWorld_posting_10nov")
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
 "fir": dict(
  title="FIR, Zero FIR and e-FIR under BNSS | Section 173, 174, 175(3) Explained",
  summary="Where and how to report a crime under the BNSS. What an FIR is under Section 173(1), the Zero FIR (information can be given irrespective of the area where the offence was committed), e-FIR by electronic communication and the three-day signature rule, recording safeguards for women and disabled victims, the free copy under Section 173(2), the preliminary enquiry under Section 173(3) and Lalita Kumari, what to do when information is not recorded (the Superintendent of Police under Section 173(4), then the Magistrate under Section 175(3) with an affidavit), non-cognizable information under Section 174, and what an FIR is not.",
  chapters=[("c01","Where can you report a crime?"),("c04","What an FIR is"),("c07","Zero FIR: report anywhere"),("c11","e-FIR: electronic information"),
            ("c13","Safeguards and a free copy"),("c16","Preliminary enquiry"),("c22","When information is not recorded"),("c28","Non-cognizable information"),
            ("c31","What an FIR is not"),("c36","Your checklist")],
  tags="#FIR #ZeroFIR #BNSS #CriminalProcedure #LawWorld"),
 "inj": dict(
  title="Temporary Injunction under Order 39 CPC | Rules 1, 2, 2A, 3 and 3A Explained",
  summary="How a civil court preserves the position while a suit is pending. Temporary injunctions under Section 94(c) and Order 39 of the CPC, when Rules 1 and 2 apply, the three tests of prima facie case, irreparable injury and balance of convenience (Dalpat Kumar v. Prahlad Singh), why the applicant's conduct matters, ex parte injunctions and the Rule 3 and 3A safeguards, discharge or variation under Rule 4, disobedience under Rule 2A, appeals under Order 43 Rule 1(r) (Wander v. Antox), mandatory interim injunctions (Dorab Cawasji Warden) and Section 41 of the Specific Relief Act.",
  chapters=[("c01","What a temporary injunction does"),("c06","When Rules 1 and 2 apply"),("c11","The three tests"),("c16","Conduct matters"),
            ("c19","Without notice: ex parte orders"),("c25","Challenging the order"),("c27","If the order is disobeyed"),("c29","Appeals"),
            ("c32","Mandatory relief and legal bars"),("c36","Drafting the application")],
  tags="#TemporaryInjunction #CPC #Order39 #CivilProcedure #LawWorld"),
 "qsh": dict(
  title="Quashing of FIR under Section 528 BNSS | Bhajan Lal Categories Explained",
  summary="When can a High Court quash an FIR or a criminal case? The inherent power under Section 528 of the BNSS (formerly Section 482 CrPC), what can be quashed, the seven illustrative categories in State of Haryana v. Bhajan Lal, why the High Court does not hold a mini-trial (Neeharika Infrastructure), a business dispute given a criminal colour, quashing on settlement in non-compoundable cases (Gian Singh, Narinder Singh, Parbatbhai Aahir), revision and Article 226, and how to prepare the petition.",
  chapters=[("c01","Can an FIR be quashed?"),("c04","What Section 528 says"),("c06","What can be quashed"),("c09","The Bhajan Lal categories"),
            ("c17","What the High Court will not do"),("c20","A business dispute with a criminal colour"),("c25","Settlement in non-compoundable cases"),
            ("c31","Other routes to the High Court"),("c34","Preparing the petition"),("c37","Remember the test")],
  tags="#Quashing #Section528 #BNSS #HighCourt #LawWorld"),
 "elv": dict(
  title="Electronic Evidence under Section 63 BSA | Certificate, Part A, Part B and Hash Value",
  summary="When is a CCTV clip, WhatsApp chat, email or call record admissible? Electronic records as documents under the Bharatiya Sakshya Adhiniyam, primary and secondary electronic evidence under Section 57, the conditions in Section 63(2), the certificate under Section 63(4) and its Schedule (Part A by the party, Part B by an expert), the hash value as a digital fingerprint (Pune Bar Association v. Union of India, 2026), what the Supreme Court held on the old Section 65B certificate in 2014 and 2020, what to do when the certificate is missing, and which law applies to pending cases under Section 170.",
  chapters=[("c01","Can a video clip be evidence?"),("c06","Electronic records are documents"),("c08","Primary or secondary?"),("c12","Section 63: the conditions"),
            ("c15","The certificate and its Schedule"),("c21","Hash value: a digital fingerprint"),("c26","What the Supreme Court held"),("c30","When the certificate is missing"),
            ("c33","Screenshots, emails and call records"),("c36","Old Act or new? Your checklist")],
  tags="#ElectronicEvidence #BSA #Section63 #Section65B #LawWorld"),
 "mnt": dict(
  title="Maintenance under Section 144 BNSS | Wife, Children and Parents Explained",
  summary="Who can claim maintenance under Section 144 of the BNSS (formerly Section 125 CrPC): a wife, children and parents, against a person with sufficient means who neglects or refuses. Who counts as a wife, how much can be ordered and interim maintenance within sixty days, from when it is payable and the disclosure affidavit (Rajnesh v. Neha), when a wife cannot claim under Section 144(4), enforcing the order and the one-year limit, why jail does not wipe out arrears (Kuldip Kaur), where to file under Section 145 including the new option where the respondent's parents reside, and alteration under Section 146.",
  chapters=[("c01","Maintenance: a right, not charity"),("c05","Who can claim"),("c10","Who counts as a wife"),("c12","Example: Deepa's claim"),
            ("c15","How much, and interim relief"),("c19","From when, and full disclosure"),("c23","When a wife cannot claim"),("c27","Enforcing the order"),
            ("c31","Where to file, and later changes"),("c35","Your checklist")],
  tags="#Maintenance #Section144 #BNSS #FamilyLaw #LawWorld"),
 "exd": dict(
  title="Setting Aside an Ex Parte Decree | Order 9 Rule 13 CPC and Article 123 Explained",
  summary="A decree passed in a suit you never knew about: how to undo it. When a suit proceeds ex parte under Order 9 Rule 6, the two grounds in Order 9 Rule 13 (summons not duly served, or sufficient cause), the provisos and the Explanation, the 30-day limit under Article 123 of the Limitation Act and Section 5, what counts as sufficient cause (G.P. Srivastava v. R.K. Raizada), choosing between an appeal under Section 96(2) and a Rule 13 application (Bhanu Kumar Jain v. Archana Kumar), notice under Rule 14, appeal under Order 43 Rule 1(d) and stay of execution, with a practical checklist.",
  chapters=[("c01","The decree you never saw"),("c04","How a suit goes ex parte"),("c07","Example: Sunil's case"),("c10","Rule 13: two grounds"),
            ("c14","The provisos and the Explanation"),("c18","The 30-day clock"),("c22","What counts as sufficient cause"),("c27","Appeal, application, or both"),
            ("c32","Notice, appeal and execution"),("c35","Your checklist")],
  tags="#ExParteDecree #CPC #Order9Rule13 #CivilProcedure #LawWorld"),
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
