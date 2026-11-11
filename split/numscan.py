# Flag numbers heard in a clip (words.json, local whisper) that the script's spoken number words cannot produce.
# Catches the 07-11 bnb c08 stumble: "Section One Fifteen" spoken as "one five one fifteen" (heard "15115", recall 1.00).
import json, re, sys
U = {"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"ten":10,"eleven":11,"twelve":12,
     "thirteen":13,"fourteen":14,"fifteen":15,"sixteen":16,"seventeen":17,"eighteen":18,"nineteen":19}
T = {"twenty":20,"thirty":30,"forty":40,"fifty":50,"sixty":60,"seventy":70,"eighty":80,"ninety":90}
O = {"first":1,"second":2,"third":3,"fourth":4,"fifth":5,"sixth":6,"seventh":7,"eighth":8,"ninth":9,"tenth":10,"eleventh":11,"twelfth":12,
     "thirteenth":13,"fourteenth":14,"fifteenth":15,"sixteenth":16,"twentieth":20,"thirtieth":30}
def groups(text):
    out, cur = [], []
    for w in re.findall(r"[a-z]+|\d+", text.lower()):
        if w in U or w in T or w in O or w in ("hundred", "thousand") or w.isdigit(): cur.append(w)
        else:
            if cur: out.append(cur); cur = []
    if cur: out.append(cur)
    return out
def values(g):
    vals, i = [], 0
    while i < len(g):
        w = g[i]
        if w in T and i + 1 < len(g) and (g[i+1] in U and U[g[i+1]] < 10 or g[i+1] in O and O[g[i+1]] < 10):
            vals.append(T[w] + (U.get(g[i+1]) or O.get(g[i+1]))); i += 2; continue
        if w == "hundred" and vals: vals[-1] *= 100; i += 1; continue
        if w == "thousand" and vals: vals[-1] *= 1000; i += 1; continue
        vals.append(int(w) if w.isdigit() else (U.get(w) if w in U else T.get(w) if w in T else O.get(w))); i += 1
    return vals
def cands(text):
    c = set()
    for g in groups(text):
        v = [str(x) for x in values(g)]
        for a in range(len(v)):
            for b in range(a + 1, len(v) + 1):
                c.add("".join(v[a:b]))
                if b - a == 2 and v[a].endswith("00"): c.add(str(int(v[a]) + int(v[b-1])))
    return c
for s in sys.argv[1:]:
    sc = {x["sceneId"]: x["dialogue"] for x in json.load(open(f"split/{s}_all_scenes.json"))["scenes"]}
    bad = 0
    for cid, dia in sc.items():
        try: heard = json.load(open(f"downloads/{s}/{cid}.words.json"))["text"]
        except Exception as e: print(s, cid, "no words", e); continue
        ok = cands(dia)
        nums = re.findall(r"\d+", heard.replace(",", ""))
        odd = [n for n in nums if n not in ok]
        if odd: bad += 1; print(f"{s} {cid}: heard {odd} | script nums {sorted(ok, key=len)[:12]} | {heard[:120]}")
    print(f"{s}: {len(sc)} clips scanned, {bad} flagged")
