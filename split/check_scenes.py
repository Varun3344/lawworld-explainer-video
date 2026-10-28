"""Sanity check for split/<set>_all_scenes.json before any Flow render: whole sentences, <= 32 words, a fill rate the avatar can
speak without rushing or padding (syllable estimate), no digits in what Flow is asked to say (Flow strips digits from prompts).
Usage: python3 split/check_scenes.py <set>"""
import json, os, re, sys
S = json.load(open(f"split/{sys.argv[1]}_all_scenes.json"))["scenes"]
def syl(w):
    if re.search(r"[\u0C80-\u0CFF]", w):                       # Kannada: aksharas x 0.6 (approved KN reels: median 68 aksharas per 10 s line)
        cons = len(re.findall(r"[\u0C95-\u0CB9\u0CDE]", w)); vir = len(re.findall(r"[\u0C95-\u0CB9]\u0CCD", w)); vow = len(re.findall(r"[\u0C85-\u0C94]", w))
        return (cons - vir + vow) * 0.6
    w = re.sub(r"[^a-z]", "", w.lower())
    if not w: return 0
    if len(w) == 1: return 1                                     # spelled letters: B N S S
    n = len(re.findall(r"[aeiouy]+", w)); n -= 1 if w.endswith("e") and not w.endswith(("le", "ee")) and n > 1 else 0
    return max(1, n)
bad = 0; tot_s = tot_w = 0
for s in S:
    d = s["dialogue"]; n = len(d.split()); sy = round(sum(syl(w) for w in d.split())); sec = s["seconds"]
    tot_s += sec; tot_w += n
    flags = []
    if n > 32: flags.append("WORDS>32")
    if re.search(r"\d", d): flags.append("DIGITS")
    if not re.search(r"[.?!]['\"’”)]*$", d.strip()): flags.append("NOT-A-SENTENCE-END")
    rate = sy / sec
    # v1 (Videos 1-3): measured on Cause of Action, 3.6 (median) to 4.5 syl/s -> the avatar spoke ~130 words a minute. Owner 19-10-2026
    # after Video 1: "full energetic ... raise some speed": the fast budget (~4.6 syl/s over 92 % of the clip) is the default now
    lo, hi = ({6: (17, 23), 8: (23, 30), 10: (30, 38)} if os.environ.get("PACE") == "v1" else {6: (22, 25), 8: (30, 34), 10: (38, 43)})[sec]   # pilot 19-10: 25/33/42 syl filled 5.70/7.72/9.70 s (tails ~0.3 s)
    if sy > hi: flags.append(f"TOO LONG for {sec}s ({sy} > {hi} syl)")
    if sy < lo: flags.append(f"SPARSE for {sec}s ({sy} < {lo} syl)")
    if flags: bad += 1
    print(f"{s['sceneId']} {sec:2d}s {n:2d}w {sy:3d}syl {rate:4.1f}/s {' '.join(flags)}")
print(f"{len(S)} clips, {tot_w} words, {tot_s} s of clips, flagged {bad}")
