"""Sanity check for split/<set>_all_scenes.json before any Flow render: whole sentences, <= 32 words, a fill rate the avatar can
speak without rushing or padding (syllable estimate), no digits in what Flow is asked to say (Flow strips digits from prompts).
Usage: python3 split/check_scenes.py <set>"""
import json, re, sys
S = json.load(open(f"split/{sys.argv[1]}_all_scenes.json"))["scenes"]
def syl(w):
    w = re.sub(r"[^a-z]", "", w.lower())
    if not w: return 0
    if len(w) == 1: return 1                                     # spelled letters: B N S S
    n = len(re.findall(r"[aeiouy]+", w)); n -= 1 if w.endswith("e") and not w.endswith(("le", "ee")) and n > 1 else 0
    return max(1, n)
bad = 0; tot_s = tot_w = 0
for s in S:
    d = s["dialogue"]; n = len(d.split()); sy = sum(syl(w) for w in d.split()); sec = s["seconds"]
    tot_s += sec; tot_w += n
    flags = []
    if n > 32: flags.append("WORDS>32")
    if re.search(r"\d", d): flags.append("DIGITS")
    if not re.search(r"[.?!]['\"’”)]*$", d.strip()): flags.append("NOT-A-SENTENCE-END")
    rate = sy / sec
    lo, hi = {6: (17, 23), 8: (23, 30), 10: (30, 38)}[sec]   # measured on Cause of Action: the avatar speaks 3.6 (median) to 4.5 syl/s
    if sy > hi: flags.append(f"TOO LONG for {sec}s ({sy} > {hi} syl)")
    if sy < lo: flags.append(f"SPARSE for {sec}s ({sy} < {lo} syl)")
    if flags: bad += 1
    print(f"{s['sceneId']} {sec:2d}s {n:2d}w {sy:3d}syl {rate:4.1f}/s {' '.join(flags)}")
print(f"{len(S)} clips, {tot_w} words, {tot_s} s of clips, flagged {bad}")
