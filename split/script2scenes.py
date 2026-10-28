"""Course-video script (plain text) -> split/<set>_all_scenes.json.
Script format, one clip per line:   <seconds> | <what the presenter says>  [|| <caption form, when the automatic one is wrong>]
A line "# <label>" starts a new chapter: its label becomes the panel chip of the next clip. Blank lines and "//" comments are ignored.
What the presenter says is written the way it is spoken (Flow strips digits from prompts): "Section One Seventy Three, sub section
Two", "B N S S", "twenty five thousand rupees". The caption form ("shown", used by the captions and the 9:16 subtitles) is derived
automatically: Section 173(2), BNSS, ₹25,000, Order VII Rule 11, non-cognizable ...
Usage: python3 split/script2scenes.py <set> <script.txt> "<title>" [--check]"""
import json, re, sys

UNITS = {w: i for i, w in enumerate("zero one two three four five six seven eight nine".split())}
TEENS = {w: i + 10 for i, w in enumerate("ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split())}
TENS = {w: (i + 2) * 10 for i, w in enumerate("twenty thirty forty fifty sixty seventy eighty ninety".split())}
SCALES = {"thousand": 1000, "lakh": 100000, "crore": 10000000}
NUMW = "|".join(sorted(list(UNITS) + list(TEENS) + list(TENS) + ["hundred"] + list(SCALES), key=len, reverse=True))
NUMSEQ = rf"(?:(?:{NUMW})(?:[ -](?:{NUMW}))*)"

def groups(words):
    """'one seventy three' -> [1, 73]; 'three hundred three' -> [303]; 'twenty five thousand' -> [25000]"""
    out, total, cur, last = [], 0, 0, None
    def flush():
        nonlocal total, cur, last
        if last is not None: out.append(total + cur)
        total = cur = 0; last = None
    for t in re.split(r"[ -]+", words.lower().strip()):
        if t in UNITS or t in TEENS:
            if last in ("unit", "teen") or (last == "tens" and t in TEENS): flush()
            cur += UNITS.get(t, TEENS.get(t)); last = "unit" if t in UNITS else "teen"
        elif t in TENS:
            if last in ("unit", "teen", "tens"): flush()
            cur += TENS[t]; last = "tens"
        elif t == "hundred": cur = (cur or 1) * 100; last = "hundred"
        elif t in SCALES: total += (cur or 1) * SCALES[t]; cur = 0; last = "scale"
    flush()
    return out
def secnum(words): return "".join(str(g) for g in groups(words))          # section numbers are read digit-group by digit-group
def amount(words):
    n = groups(words); n = n[0] if len(n) == 1 else int("".join(map(str, n)))
    s = str(n)
    if len(s) <= 3: return s
    head, tail = s[:-3], s[-3:]
    head = re.sub(r"(\d)(?=(\d\d)+$)", r"\1,", head)                       # Indian grouping: 5,00,000
    return f"{head},{tail}"
ROMAN = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX", 10: "X", 11: "XI", 12: "XII", 13: "XIII", 14: "XIV",
         15: "XV", 16: "XVI", 17: "XVII", 18: "XVIII", 19: "XIX", 20: "XX", 21: "XXI", 22: "XXII", 23: "XXIII", 37: "XXXVII", 39: "XXXIX", 41: "XLI", 43: "XLIII"}

def shown(text):
    t = text
    for a, b in (("B N S S", "BNSS"), ("B N S", "BNS"), ("C r P C", "CrPC"), ("C P C", "CPC"), ("F I R", "FIR"), ("C C T V", "CCTV"),
                 ("I N S C", "INSC"), ("S C C", "SCC"), ("S P", "SP"), ("S L P", "SLP"), ("D S P", "DSP"), ("E D", "ED"), ("C B I", "CBI"),
                 ("O N G C", "ONGC"), ("E X L", "EXL"), ("A I R", "AIR"), ("N I Act", "NI Act"), ("I P C", "IPC")):
        t = re.sub(rf"\b{a}\b", b, t)
    t = re.sub(r"\bnon (cognizable|bailable|compoundable)", r"non-\1", t, flags=re.I)
    # Order Seven Rule Eleven, clause A -> Order VII Rule 11(a)
    def order(m):
        o = groups(m.group(1))[0]; r = secnum(m.group(2)); c = f"({m.group(3).lower()})" if m.group(3) else ""
        return f"Order {ROMAN.get(o, o)} Rule {r}{c}"
    t = re.sub(rf"\bOrder ({NUMSEQ}),? Rule ({NUMSEQ})(?:,? clause ([A-Za-z])\b)?", order, t, flags=re.I)
    t = re.sub(rf"\bOrder ({NUMSEQ})\b", lambda m: f"Order {ROMAN.get(groups(m.group(1))[0], m.group(1))}", t, flags=re.I)
    # Section(s) / Article(s) with sub-section and clause -> Section 173(1)(g) (a sub-section on its own: below)
    def sec(m):
        word, num, sub, cl, comma = m.group(1), m.group(2), m.group(3), m.group(4), m.group(5) or ""
        s = f"{word} {secnum(num)}"
        if sub: s += f"({secnum(sub)})"
        if cl: s += f"({cl.lower()})"
        # "Section 175(1) permits" (the subject: no comma), "Under Section 290(1), he must" and "Sections 2, 35, ..." keep it
        lead = m.string[max(0, m.start() - 6):m.start()].lower()
        return s + (comma if (not (sub or cl) or lead.endswith(("under ", "per "))) else "")
    t = re.sub(rf"(?<!sub )(?<!sub-)\b(Sections?|Articles?|Rules?|Schedule) ({NUMSEQ})(?:,? sub ?section ({NUMSEQ}))?(?:,? clause ([A-Za-z])\b)?(,?)", sec, t, flags=re.I)
    # lists after "Sections": "Sections 2, Thirty Five, One Seventy Three and ..." -> digits
    def lst(m):
        return re.sub(rf"\b({NUMSEQ})\b", lambda k: secnum(k.group(1)), m.group(0), flags=re.I)
    t = re.sub(rf"\b(Sections|Articles) \d+(?:(?:,| and| to) (?:\d+|{NUMSEQ}))+", lst, t, flags=re.I)
    t = re.sub(rf"\b([Ss]ub) ?section ({NUMSEQ})\b", lambda m: f"{m.group(1)}-section ({secnum(m.group(2))})", t, flags=re.I)
    t = re.sub(r"\b([Cc]lause) ([A-Za-z])\b", lambda m: f"{m.group(1)} ({m.group(2).lower()})", t)
    t = re.sub(rf"\b({NUMSEQ}) rupees\b", lambda m: f"₹{amount(m.group(1))}", t, flags=re.I)
    t = re.sub(rf"\b({NUMSEQ}) (days|months|years|weeks|hours)\b",
               lambda m: f"{amount(m.group(1))} {m.group(2)}" if groups(m.group(1)) and groups(m.group(1))[0] >= 10 else m.group(0), t, flags=re.I)
    t = re.sub(rf"\b({NUMSEQ}) (day|month|year|week|hour)\b",
               lambda m: f"{amount(m.group(1))}-{m.group(2)}" if groups(m.group(1)) and groups(m.group(1))[0] >= 10 else m.group(0), t, flags=re.I)
    t = re.sub(r"\bone (half|third|fourth|sixth)\b", r"one-\1", t, flags=re.I)
    t = re.sub(r"\bfirst time offender", "first-time offender", t, flags=re.I)
    t = re.sub(r"\bsocio economic", "socio-economic", t, flags=re.I)
    t = re.sub(r"\(\s+", "(", t); t = re.sub(r" ,", ",", t); t = re.sub(r",\.", ".", t)
    return t

def parse(path):
    scenes, chip, n = [], None, 0
    for raw in open(path, encoding="utf-8"):
        line = raw.strip()
        if not line or line.startswith("//"): continue
        if line.startswith("#"): chip = line.lstrip("#").strip(); continue
        secs, rest = line.split("|", 1)
        say, _, show = rest.partition("||")
        n += 1; say = say.strip(); s = {"sceneId": f"c{n:02d}", "seconds": int(secs), "dialogue": say}
        cap = show.strip() or shown(say)
        if cap != say: s["shown"] = cap
        if chip: s["chip"] = chip; chip = None
        scenes.append(s)
    return scenes

def syl(w):
    if re.search(r"[\u0C80-\u0CFF]", w):                       # Kannada: aksharas x 0.6 (approved KN reels: median 68 aksharas per 10 s line)
        cons = len(re.findall(r"[\u0C95-\u0CB9\u0CDE]", w)); vir = len(re.findall(r"[\u0C95-\u0CB9]\u0CCD", w)); vow = len(re.findall(r"[\u0C85-\u0C94]", w))
        return (cons - vir + vow) * 0.6
    w = re.sub(r"[^a-z]", "", w.lower())
    if not w: return 0
    if len(w) == 1: return 1                                     # spelled letters: B N S S
    n = len(re.findall(r"[aeiouy]+", w)); n -= 1 if w.endswith("e") and not w.endswith(("le", "ee")) and n > 1 else 0
    return max(1, n)
def nsyl(t): return sum(syl(w) for w in t.split())
def secs_for(n): return 6 if n <= 23 else 8 if n <= 30 else 10   # the avatar speaks 3.6-4.5 syl/s (Cause of Action clips)
def pack(scenes, cap=38, words=32):
    """Merge neighbouring clips of one chapter while the whole fits one 10 s clip (fewer renders, fewer cuts); re-time every clip."""
    out = []
    for s in scenes:
        if out and "chip" not in s and nsyl(out[-1]["dialogue"]) + nsyl(s["dialogue"]) <= cap \
                and len((out[-1]["dialogue"] + " " + s["dialogue"]).split()) <= words:
            o = out[-1]
            o["shown"] = (o.get("shown") or o["dialogue"]) + " " + (s.get("shown") or s["dialogue"])
            o["dialogue"] += " " + s["dialogue"]
            if o["shown"] == o["dialogue"]: del o["shown"]
        else:
            out.append(dict(s))
    for i, s in enumerate(out):
        s["sceneId"] = f"c{i + 1:02d}"; s["seconds"] = secs_for(nsyl(s["dialogue"]))
    return out

if __name__ == "__main__":
    SET, SRC, TITLE = sys.argv[1], sys.argv[2], sys.argv[3]
    sc = parse(SRC)
    if "--pack" in sys.argv: sc = pack(sc)
    json.dump({"projectTitle": f"LawWorld_{SET}", "title": TITLE, "source": SRC, "scenes": sc},
              open(f"split/{SET}_all_scenes.json", "w"), indent=1, ensure_ascii=False)
    for s in sc:
        if "shown" in s: print(f"{s['sceneId']}: {s['shown']}")
    print(f"[script] {len(sc)} clips -> split/{SET}_all_scenes.json")
