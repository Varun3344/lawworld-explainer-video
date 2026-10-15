"""Cause of Action, FULL video (owner's 7-scene script, 36 clips c01..c36): presenter on the RIGHT third (x 1280..1920, 9:16 ivory
clips flattened to the panel cream by split/flatten_bg.py), animated panel on the LEFT two thirds (overlays/split_panel.html +
split_cues_coa*.js; contract in split/COA_CUES.md). Builds land on the spoken words: script tokens are aligned to whisper word
times (same alignment as build_split_plan.py), head/tail pauses are trimmed, clips are laid end to end after the opening sting.
Any anchor word that cannot be found is FATAL. No punch-in zoom and no push (the owner saw the presenter "jump" between clips);
per-clip size/position matching comes from out/coa/place.json when present (split/presenter_geom.py).
Usage: python3 split/build_coa_plan.py [--allow-missing]
Writes out/coa/timeline.json, plan.json, anchors.txt, captions.srt."""
import os, sys, json, subprocess, difflib, importlib.util
spec = importlib.util.spec_from_file_location("words", "scripts/words.py"); W = importlib.util.module_from_spec(spec); spec.loader.exec_module(W); norm = W.norm
def dur(f): return float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f],capture_output=True,text=True).stdout.strip())

D = "downloads/coa"; CLIPS = f"{D}/flat"; OUT = "out/coa"; os.makedirs(OUT, exist_ok=True)
SCENES = "split/coa_all_scenes.json"
ALL = json.load(open(SCENES))["scenes"]
SCRIPT = {s["sceneId"]: s["spoken"] for s in ALL}                 # what the avatar was asked to say (alignment)
# c18/c32: the owner's script said "arose on 1st April 2025, the first day of default"; the adversarial fact-check (15 Oct) showed
# Indian loan cases put the cause of action on the due date itself ("the date when the loan ought to have been repaid but is not
# repaid", Harcharan Singh v. Sunil Sarin, Del HC 2013; Jailebdeen, AIR 1992 Ker 31), so both lines and the pin say 31 March 2025.
SHOWN = {                                                            # how the words are written in the captions
    "c05": "The classic statement comes from an English case, Read v. Brown, decided in 1888.",
    "c07": "Our Supreme Court adopted this in A.B.C. Laminart v. A.P. Agencies.",
    "c14": "Suresh promises to repay by 31 March 2025. The date passes. Suresh pays nothing.",
    "c18": "It arose on 31 March 2025, the due date he missed. Remember that date. We'll need it.",
    "c20": "The Privy Council said in Chand Kour v. Partab Singh that it refers entirely to the grounds set out in the plaint.",
    "c23": "One: pleading. Order VII Rule 1(e) requires every plaint to state the facts constituting the cause of action, and when it arose.",
    "c24": "Two: rejection. Under Order VII Rule 11(a), a plaint that discloses no cause of action must be rejected.",
    "c27": "Three: jurisdiction. Besides where the defendant lives, Section 20(c) lets you sue where the cause of action arises, wholly or in part.",
    "c29": "Under Order II Rule 2, if Ravi sues for only three lakh, he cannot later sue for the other two.",
    "c32": "The Limitation Act fixes the exact starting point for each kind of suit. That's why we pinned 31 March 2025.",
}
IDS = [s["sceneId"] for s in ALL]
missing = [c for c in IDS if not (os.path.exists(f"{D}/{c}.mp4") and os.path.exists(f"{D}/{c}.words.json") and os.path.exists(f"{CLIPS}/{c}.mp4"))]
if missing and "--allow-missing" not in sys.argv: sys.exit(f"[plan] missing clips (source, words or flat): {missing}")
stale = [c for c in IDS if c not in missing and os.path.getmtime(f"{CLIPS}/{c}.mp4") < os.path.getmtime(f"{D}/{c}.mp4")]
if stale: sys.exit(f"[plan] FATAL flattened clips older than their source (retake?): {stale} -> python3 split/flatten_bg.py --seam left " + " ".join(f"{D}/{c}.mp4" for c in stale))
IDS = [c for c in IDS if c not in missing]
FX = json.load(open(f"{OUT}/face_x.json")) if os.path.exists(f"{OUT}/face_x.json") else {}
PLACE = json.load(open(f"{OUT}/place.json")) if os.path.exists(f"{OUT}/place.json") else {}
HOOK = 1.6; END = 4.2

t = HOOK; segs = []; words = []
for cid in IDS:
    c = f"{D}/{cid}.mp4"; d = dur(c); ws = json.load(open(f"{D}/{cid}.words.json"))["words"]
    toks = [x for x in SCRIPT[cid].split() if x.strip("—–-")]
    sm = difflib.SequenceMatcher(a=[norm(x) or "x" for x in toks], b=[norm(w["word"]) or "x" for w in ws], autojunk=False); tm = [None] * len(toks)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            for k in range(i2 - i1): tm[i1 + k] = (ws[j1 + k]["start"], ws[j1 + k]["end"])
        elif tag == "replace" and j2 > j1:
            a, b = ws[j1]["start"], ws[j2 - 1]["end"]; n = i2 - i1
            for k in range(n): tm[i1 + k] = (a + (b - a) * k / n, a + (b - a) * (k + 1) / n)
    for i in range(len(toks)):
        if tm[i] is None:
            p = next((tm[k][1] for k in range(i - 1, -1, -1) if tm[k]), 0.0); q = next((tm[k][0] for k in range(i + 1, len(toks)) if tm[k]), d); tm[i] = (p, min(q, p + 0.3))
    s0 = tm[0][0]; s1 = tm[-1][1]
    tin = max(0.0, s0 - 0.12); tout = d if cid == IDS[-1] else min(d, s1 + 0.28)   # the last clip runs to its end: room for the payoff
    segs.append({"clip": f"{CLIPS}/{cid}.mp4", "in": round(tin, 3), "out": round(tout, 3), "base": round(t, 3), "cid": cid, "fx": FX.get(cid), "place": PLACE.get(cid)})
    for i, x in enumerate(toks): words.append({"word": x, "start": round(t + tm[i][0] - tin, 3), "end": round(t + tm[i][1] - tin, 3), "cid": cid})
    t += tout - tin
pend = round(t, 3); total = round(pend + END, 3)

ANCH = []
def at(cid, target, nth=1):
    tg = [norm(x) for x in (target if isinstance(target, list) else [target])]; h = 0
    for w in words:
        if w["cid"] != cid: continue
        n = norm(w["word"])
        if any(n == g or (len(g) >= 4 and n.startswith(g)) for g in tg):
            h += 1
            if h == nth: ANCH.append(f"{cid:4} {str(target):28} #{nth} -> {w['start']:7.3f}  ({w['word']})"); return w["start"]
    sys.exit(f"[plan] FATAL {cid}: anchor {target!r} (#{nth}) not found in {[w['word'] for w in words if w['cid'] == cid]}")
have = lambda *cs: all(c in IDS for c in cs)
S = lambda cid: next(s["base"] for s in segs if s["cid"] == cid)
E = lambda cid: next(round(s["base"] + s["out"] - s["in"], 3) for s in segs if s["cid"] == cid)
r3 = lambda x: round(x, 3)
cues = []; sfx = []
def fx(n, tt, g=-16): sfx.append({"file": f"audio/sfx/{n}.mp3", "at": r3(max(0, tt)), "gain_db": g})
def cue(**k): cues.append({kk: (r3(v) if isinstance(v, float) else v) for kk, v in k.items()})

# ── opening sting (frame 0 = finished logo card = thumbnail), persistent panel, presenter name ─────────────────────────────
cue(type="sting", t0=0.0, t1=HOOK + 0.35, kicker="CIVIL PROCEDURE · EXPLAINED", title="Cause of Action", sub="The starting point of every civil suit")
fx("slam", 0.02, -8); fx("riser", HOOK - 0.9, -18)
chips = [{"at": r3(HOOK), "label": "1 · THE HOOK"}]
if have("c04"): chips.append({"at": r3(S("c04") - 0.1), "label": "2 · WHAT IT IS"})
if have("c10"): chips.append({"at": r3(S("c10") - 0.1), "label": "3 · RIGHT + BREACH"})
if have("c13"): chips.append({"at": r3(at("c13", "let's") - 0.1), "label": "4 · WORKED EXAMPLE"})
if have("c19"): chips.append({"at": r3(S("c19") - 0.1), "label": "5 · WHAT IT IS NOT"})
if have("c22"): chips.append({"at": r3(at("c22", "so") - 0.1), "label": "6 · WHY IT MATTERS"})
if have("c33"): chips.append({"at": r3(S("c33") - 0.1), "label": "7 · BEFORE YOU DRAFT"})
cue(type="panel", t0=HOOK - 0.3, t1=pend + 0.25, scenes=chips)
cue(type="lower_third", t0=S("c01") + 0.5, t1=S("c01") + 5.2, name="Ravishankar", role="LawWorld")

# ── Scene 1: hook ──────────────────────────────────────────────────────────────────────────────────────────────────────
if have("c01", "c02", "c03"):
    q_at = at("c02", "do") - 0.1
    cue(type="title", t0=HOOK, t1=q_at - 0.05, title="CAUSE OF ACTION", title_at=S("c01") + 0.1, sub="The starting point of every civil suit", sub_at=at("c01", "begins"))
    fx("pop", S("c01") + 0.1, -18); fx("pop", at("c01", "begins"), -20)
    st_at = at("c02", "thrown") - 0.12
    cue(type="question", t0=q_at - 0.05, t1=E("c02") + 0.05, at=q_at, text="Do you have a cause of action?", hl="cause of action")
    cue(type="stamp", t0=st_at - 0.05, t1=E("c02") + 0.05, at=st_at, line1="NO CAUSE OF ACTION", line2="= PLAINT REJECTED")
    fx("whoosh", q_at - 0.12, -18); fx("slam", st_at + 0.06, -9)
    items = [{"n": 1, "text": "What it is", "at": r3(at("c03", "what") - 0.08)},
             {"n": 2, "text": "How to spot it", "at": r3(at("c03", "how") - 0.08)},
             {"n": 3, "text": "Why it matters", "at": r3(at("c03", "why") - 0.08)}]
    cue(type="list", t0=S("c03"), t1=E("c03") + 0.05, head="In the next 5 minutes", head_at=at("c03", "next") - 0.1, items=items)
    fx("pop", at("c03", "next") - 0.1, -18)
    for it in items: fx("pop", it["at"], -16)

# ── Scene 2: what it is ────────────────────────────────────────────────────────────────────────────────────────────────
if have("c04", "c05", "c06", "c07", "c08", "c09"):
    fx("whoosh", S("c04") - 0.15, -16)
    cpc = min(at("c04", "code") - 0.1, S("c04") + 0.25)            # the card is up while he says "Surprisingly" (no empty panel)
    cue(type="strike", t0=S("c04"), t1=E("c04") + 0.05, text="CPC, 1908: no definition", at=cpc, strike_at=at("c04", "never"), icon="book-open")
    courts = at("c04", "comes") - 0.05
    cue(type="point", t0=courts - 0.05, t1=E("c04") + 0.05, text="Defined by the courts", at=courts, icon="landmark", accent=True)
    fx("pop", cpc, -16); fx("whoosh", at("c04", "never") + 0.1, -20); fx("ding", courts, -18)
    cue(type="kicker", t0=S("c05"), t1=E("c06") + 0.05, at=at("c05", "classic") - 0.1, text="THE CLASSIC DEFINITION")
    rb = at("c05", ["read", "reid", "reed"]) - 0.1
    cue(type="cite", t0=rb - 0.05, t1=E("c06") + 0.02, at=rb, text="Read v. Brown (1888) 22 QBD 128", tag="ENGLISH COURT OF APPEAL")
    fx("pop", rb, -16)
    qa = at("c05", "statement") - 0.05
    cue(type="quote", t0=qa - 0.05, t1=E("c06") + 0.02, at=qa, reveal=r3(min(6.0, max(3.5, S("c06") + 1.0 - qa))),
        text="Every fact which it would be necessary for the plaintiff to prove, if traversed, in order to support his right to the judgment of the Court.",
        hl=["every fact", "to prove", "if traversed"], note={"text": "traversed = denied", "at": r3(at("c06", "denied") - 0.05)})
    fx("whoosh", qa - 0.1, -20); fx("pop", at("c06", "denied") - 0.05, -18)
    sc = at("c07", "supreme") - 0.1
    cue(type="point", t0=S("c07"), t1=E("c07") + 0.05, text="Adopted by the Supreme Court of India", at=min(sc, S("c07") + 0.25), icon="landmark", accent=False)
    lam = at("c07", ["laminart", "laminar", "lamina", "laminate"]) - 0.25
    cue(type="cite", t0=lam - 0.05, t1=E("c08") + 0.05, at=lam, text="A.B.C. Laminart Pvt. Ltd. v. A.P. Agencies, Salem (1989) 2 SCC 163", tag="SUPREME COURT OF INDIA")
    fx("pop", sc, -18); fx("pop", lam, -16)
    b1 = at("c08", "bundle") - 0.1; b2 = at("c08", "law") - 0.1; b3 = at("c08", "right") - 0.1
    cue(type="equation", t0=S("c08"), t1=E("c08") + 0.05,
        terms=[{"text": "BUNDLE OF FACTS", "at": r3(b1)}, {"op": "+", "text": "APPLICABLE LAW", "at": r3(b2)}, {"op": "=", "text": "RIGHT TO RELIEF", "at": r3(b3), "result": True}])
    fx("pop", b1, -16); fx("pop", b2, -16); fx("ding", b3, -14)
    one = at("c09", "one") - 0.05; many = at("c09", "every") - 0.25; gather = at("c09", "every") + 0.45
    cue(type="bundle", t0=S("c09"), t1=E("c09") + 0.35, one_at=one, many_at=many, gather_at=gather, label="Bundle of facts",
        icons=["file-text", "calendar", "indian-rupee", "handshake", "pen-line", "receipt", "file-signature"])
    fx("pop", one, -16); fx("whoosh", many, -20); fx("whoosh", gather, -18); fx("ding", gather + 0.55, -16)

# ── Scene 3: right plus breach ─────────────────────────────────────────────────────────────────────────────────────────
if have("c10", "c11", "c12", "c13"):
    op = at("c10", "open") - 0.05; r1 = at("c10", "first") - 0.08; r2 = at("c11", "second") - 0.08; mg = at("c11", "infringes") - 0.05
    cue(type="blocks", t0=S("c10"), t1=S("c12") + 0.35, open_at=op, merge={"label": "CAUSE OF ACTION", "at": r3(mg)},
        items=[{"label": "PLAINTIFF'S RIGHT", "sub": "a right that belongs to the plaintiff", "at": r3(r1)},
               {"label": "DEFENDANT'S BREACH", "sub": "an act or omission that infringes it", "at": r3(r2)}])
    fx("whoosh", op, -18); fx("pop", r1, -16); fx("pop", r2, -16); fx("ding", mg + 0.3, -16)
    v1 = at("c12", "right") - 0.1; v2 = at("c12", "breach", 2) - 0.1; v3 = at("c13", "need") - 0.1
    cue(type="verdicts", t0=S("c12") + 0.05, t1=at("c13", "let's") - 0.05,
        rows=[{"text": "Right, no breach", "ok": False, "at": r3(v1)}, {"text": "Breach, but not of your right", "ok": False, "at": r3(v2)},
              {"text": "Your right + breach by this defendant", "ok": True, "at": r3(v3)}])
    fx("pop", v1, -18); fx("pop", v2, -18); fx("ding", v3, -14)

# ── Scene 4: worked example ────────────────────────────────────────────────────────────────────────────────────────────
if have("c13", "c14", "c15", "c16", "c17", "c18"):
    lt = at("c13", "let's") - 0.05
    n1 = at("c13", "lends") - 0.1; n2 = at("c14", "repay") - 0.1; n3 = at("c14", "pays") - 0.1
    cue(type="timeline", t0=lt, t1=S("c15") + 0.3,
        nodes=[{"label": "LOAN", "value": "₹5,00,000", "sub": "Ravi → Suresh", "at": r3(n1)}, {"label": "DUE", "value": "31 Mar 2025", "at": r3(n2)},
               {"label": "REPAID", "value": "₹0", "tone": "red", "at": r3(n3)}])
    fx("whoosh", lt, -18); fx("pop", n1, -16); fx("pop", n2, -16); fx("slam", n3 + 0.05, -14)
    k1 = at("c15", "one") - 0.08; k2 = at("c15", "two") - 0.08; k3 = at("c16", "three") - 0.08; k4 = at("c16", "four") - 0.08; fold = at("c17", "together") - 0.1
    cue(type="checklist", t0=S("c15"), t1=S("c18") + 0.25, head="What must Ravi prove?", head_at=S("c15") + 0.1,
        items=[{"n": 1, "text": "Loan given", "at": r3(k1)}, {"n": 2, "text": "Promise to repay by 31 Mar 2025", "at": r3(k2)},
               {"n": 3, "text": "Due date passed", "at": r3(k3)}, {"n": 4, "text": "Amount still unpaid", "at": r3(k4)}],
        fold={"label": "Ravi's cause of action", "at": r3(fold)})
    for k in (k1, k2, k3, k4): fx("pop", k, -16)
    fx("whoosh", fold, -18); fx("ding", fold + 0.6, -16)
    land = at("c18", "arose") - 0.05
    fly = at("c32", "pinned") - 0.05 if have("c32") else None
    cue(type="pin", t0=land - 0.1, t1=(E("c32") + 0.05) if have("c32") else pend + 0.25, text="Arose: 31 Mar 2025", land_at=land, fly_at=fly, slot=5)
    fx("slam", land + 0.12, -10)

# ── Scene 5: what it is not ────────────────────────────────────────────────────────────────────────────────────────────
if have("c19", "c20", "c21", "c22"):
    cue(type="kicker", t0=S("c19"), t1=at("c22", "so") - 0.05, at=at("c19", "two") - 0.1, text="TWO COMMON MISTAKES")
    ne1 = at("c19", "depend") - 0.1; sub1 = at("c20", "grounds") - 0.1
    cue(type="notequal", t0=S("c19") + 0.2, t1=E("c20") + 0.05, left="Cause of action", right="the defence", at=ne1,
        sub="Read the plaint, not the written statement", sub_at=sub1)
    ck = at("c20", ["chand", "chandkour"]) - 0.1
    cue(type="cite", t0=ck - 0.05, t1=E("c20") + 0.05, at=ck, text="Chand Kour v. Partab Singh (1888) 15 IA 156", tag="PRIVY COUNCIL")
    fx("pop", ne1, -16); fx("pop", sub1, -18); fx("pop", ck, -16)
    ne2 = at("c21", "relief") - 0.1; rel = at("c21", "relief", 2) - 0.1; why = at("c22", "cause") - 0.1
    cue(type="notequal", t0=S("c21"), t1=rel + 0.15, left="Cause of action", right="the relief", at=ne2)
    cue(type="splitcard", t0=rel - 0.05, t1=at("c22", "so") - 0.05,
        left={"title": "RELIEF", "text": "what you ask for", "at": r3(rel)}, right={"title": "CAUSE OF ACTION", "text": "why you are entitled to it", "at": r3(why)})
    fx("pop", ne2, -16); fx("whoosh", rel - 0.1, -18); fx("ding", why, -16)

# ── Scene 6: why it matters ────────────────────────────────────────────────────────────────────────────────────────────
if have("c22", "c23", "c24", "c25", "c26", "c27", "c28", "c29", "c30", "c31", "c32"):
    so = at("c22", "so") - 0.05; five = at("c22", "five") - 0.1
    s1 = at("c23", "one") - 0.08; s2 = at("c24", "two") - 0.08; sub2 = S("c25") + 0.1; s3 = at("c27", "three") - 0.08
    p1 = at("c28", "loan") - 0.1; p2 = at("c28", "repayment") - 0.1; s4 = at("c28", "four") - 0.08; split = at("c29", "only") - 0.05
    s5 = at("c31", "five") - 0.08; clock = at("c32", "pinned") + 0.55
    cue(type="slots", t0=so, t1=E("c32") + 0.05, head="Why it matters", head_at=five, slots=[
        {"n": 1, "title": "PLEAD IT", "at": r3(s1), "rule": "O. VII R. 1(e) CPC", "text": "the facts + the date it arose"},
        {"n": 2, "title": "OR LOSE IT", "at": r3(s2), "rule": "O. VII R. 11(a) CPC", "text": "no cause of action → plaint rejected",
         "sub": "The court reads the plaint and its documents only", "sub_at": r3(sub2)},
        {"n": 3, "title": "WHERE TO SUE", "at": r3(s3), "rule": "S. 20(c) CPC", "text": "where it arises, wholly or in part",
         "visual": "map", "pins": [{"label": "Loan given here", "at": r3(p1)}, {"label": "Repayment due here", "at": r3(p2)}]},
        {"n": 4, "title": "ONE SHOT", "at": r3(s4), "rule": "O. II R. 2 CPC", "text": "sue for the whole claim",
         "visual": "bar", "claimed": "₹3,00,000 claimed", "lost": "₹2,00,000 lost", "split_at": r3(split)},
        {"n": 5, "title": "THE CLOCK", "at": r3(s5), "rule": "Limitation Act, 1963", "text": "the Schedule fixes when time begins to run",
         "visual": "clock", "clock_at": r3(clock)}])
    for x in (s1, s2, s3, s4, s5): fx("pop", x, -15)
    fx("whoosh", so, -18); fx("pop", p1, -18); fx("pop", p2, -18); fx("whoosh", split, -18); fx("ding", clock, -16)
    cs = S("c25") + 0.05
    cue(type="cite", t0=cs - 0.05, t1=E("c25") + 0.05, at=cs, tag="SUPREME COURT OF INDIA",
        cases=[{"name": "Saleem Bhai v. State of Maharashtra", "cite": "(2003) 1 SCC 557"},
               {"name": "Dahiben v. Arvindbhai Kalyanji Bhanusali", "cite": "(2020) 7 SCC 366"}])
    ar = at("c26", "krishna") - 0.15
    cue(type="cite", t0=min(ar, E("c25") - 0.02) - 0.05, t1=E("c26") + 0.05, at=min(ar, E("c25") - 0.02),
        text="T. Arivandandam v. T.V. Satyapal (1977) 4 SCC 467", tag="SUPREME COURT · KRISHNA IYER J.")
    fx("pop", cs, -16); fx("pop", ar, -16)

# ── Scene 7: close ─────────────────────────────────────────────────────────────────────────────────────────────────────
if have("c33", "c34", "c35", "c36"):
    h7 = at("c33", "before") - 0.1
    q1 = at("c33", "what") - 0.08; q2 = at("c34", "what") - 0.08; q3 = at("c34", "when") - 0.08
    cue(type="list", t0=S("c33"), t1=E("c34") + 0.05, head="Before you draft", head_at=h7,
        items=[{"n": 1, "text": "What RIGHT?", "at": r3(q1)}, {"n": 2, "text": "What BREACH?", "at": r3(q2)}, {"n": 3, "text": "WHEN and WHERE?", "at": r3(q3)}])
    for x in (h7, q1, q2, q3): fx("pop", x, -16)
    ans = at("c35", "answer") - 0.1
    cue(type="point", t0=S("c35"), t1=pend + 0.25, text="All three, with facts you can prove", at=min(ans, S("c35") + 0.25), icon="check", accent=True)
    fx("ding", ans, -16)

# ── close ──────────────────────────────────────────────────────────────────────────────────────────────────────────────
cue(type="endcard", t0=pend + 0.2, t1=total, title="Cause of Action", line="Cause of action = every fact you must prove to win",
    sub="Next episode: Jurisdiction", url="lawworld.ai")
fx("whoosh", pend + 0.1, -16)

json.dump({"duration": total, "width": 1920, "height": 1080, "layout": {"px": 640, "presenter": "right"}, "cues": cues},
          open(f"{OUT}/timeline.json", "w"), indent=1, ensure_ascii=False)
def seg(s):
    d = {"clip": s["clip"], "in": s["in"], "out": s["out"]}
    if s["fx"] is not None: d["fx"] = s["fx"]
    if s["place"]: d["place"] = s["place"]
    return d
plan = {"fps": 24, "out": f"{OUT}/coa_full.mp4", "size": [1920, 1080],
        # fy 0.78 crops the top ~50 source px (dark cove line at y≈36 in the ivory clips)
        "presenter_box": {"x": 1280, "y": 0, "w": 640, "h": 1080, "fx": 0.5, "fy": 0.78, "pad": "0xf5f0e8"},
        "presenter_start": HOOK, "presenter": [seg(s) for s in segs],
        "match_bg": False, "cutaways": [], "endcard": {"clip": "brand/cream_tail.mp4", "dur": END + 0.3, "offset": 0, "xfade": 0.3},
        "music": {"file": "audio/bed_coa_300s.mp3", "target_lufs": -26, "fade_in": 0.2, "fade_out": 2.5, "duck": True},
        "voice_lufs": -14, "level_voice": True, "limit": 0.85, "sfx": sfx,
        "grade_presenter": "unsharp=5:5:0.5:5:5:0", "scenes": SCENES,
        "overlays": {"dir": f"{OUT}/frames", "fps": 24}, "delogo": None, "total": total, "tail_black": 0}
json.dump(plan, open(f"{OUT}/plan.json", "w"), indent=1)
open(f"{OUT}/anchors.txt", "w").write("\n".join(ANCH) + "\n")

# captions (.srt) in the script's own spelling, timed on the aligned words (same grouping as build_split_plan.py)
def ts(x): h = int(x // 3600); m = int(x % 3600 // 60); s = x % 60; return f"{h:02d}:{m:02d}:{int(s):02d},{int(round((s - int(s)) * 1000)):03d}"
srt_cues = []
def endch(w): return w.rstrip("'\"”’)")[-1:]
for cid in IDS:
    toks = [x for x in SCRIPT[cid].split() if x.strip("—–-")]; shown = SHOWN.get(cid, SCRIPT[cid]).split()
    cw = [w for w in words if w["cid"] == cid]
    if len(shown) != len(toks):
        srt_cues.append([cw[0]["start"], cw[-1]["end"], shown]); continue
    chunks, cur = [], []
    for i, w in enumerate(shown):
        cur.append(i)
        if endch(w) in ".?!:;": chunks.append(cur); cur = []
    if cur: chunks.append(cur)
    out = []
    for ch in chunks:
        while len(ch) > 10:
            commas = [k for k in range(2, len(ch) - 2) if endch(shown[ch[k]]) == ","]
            cut = min(commas, key=lambda k: abs(k - len(ch) / 2)) + 1 if commas else len(ch) // 2
            out.append(ch[:cut]); ch = ch[cut:]
        out.append(ch)
    merged = []
    for ch in out:
        if merged and (len(ch) < 3 or len(merged[-1]) < 3) and len(merged[-1]) + len(ch) <= 12: merged[-1] = merged[-1] + ch
        else: merged.append(ch)
    for ch in merged: srt_cues.append([cw[ch[0]]["start"], cw[ch[-1]]["end"], [shown[k] for k in ch]])
srt = []
for i, (a, b, ws) in enumerate(srt_cues):
    nxt = srt_cues[i + 1][0] if i + 1 < len(srt_cues) else total
    b = min(max(b + 0.2, a + 0.8), nxt - 0.04)
    srt.append(f"{i + 1}\n{ts(a)} --> {ts(b)}\n{' '.join(ws)}\n")
open(f"{OUT}/captions.srt", "w").write("\n".join(srt))
print(f"[plan] clips {len(IDS)}/{len(ALL)}  presenter {HOOK}-{pend}s  total {total}s  cues {len(cues)}  sfx {len(sfx)}  anchors {len(ANCH)}" + (f"  MISSING {missing}" if missing else ""))
