"""Flow storyboards for a LawWorld course video (owner 19-10-2026: the BNSS / CPC storyboard series, "dont turn avatar right and
left, just straight like before"). Reads split/<set>_all_scenes.json and writes split/<set>_{6,8,10}s.json for split/run_queue.sh.
The presenter faces the camera squarely in EVERY clip (no "presents" turns, no pointing to the side), gestures stay in front of his
chest, and every clip is anchored to one frame: the first clip (c01) is rendered from the text in the video's own suit and every
later clip is matched to its last frame (--ref <jpg> borrows an anchor frame as c00 instead). Owner 19-10-2026: a different suit for
every video (OUTFITS), proper lip sync. Owner 19-10-2026 (after Video 1): "full energetic", faster, focus on content and
pronouncing the word - delivery/audio below ask for a fast, high-energy pace with crisp diction (Videos 4-8).
Usage: python3 split/make_course_sb.py <set> [--ref <jpg>] [--new-project]"""
import json, os, shutil, sys

SET = sys.argv[1]
REF = sys.argv[sys.argv.index("--ref") + 1] if "--ref" in sys.argv else None     # optional borrowed anchor frame (c00); default: c01 anchors
ALL = json.load(open(f"split/{SET}_all_scenes.json"))
D = os.path.abspath(f"downloads/{SET}")
os.makedirs(f"{D}/frames", exist_ok=True)
if REF and not os.path.exists(f"{D}/frames/c00_last.jpg"): shutil.copy(REF, f"{D}/frames/c00_last.jpg")
# owner 19-10-2026: "use different different suits for each video, dont repeat the same" - one suit per video, none repeated, none
# the Cause of Action navy blazer; no white or cream shirts (the backdrop flatten keys on the ivory)
OUTFITS = {
    "cog": "a tailored charcoal-grey two-piece business suit, a crisp light-blue formal shirt and a deep burgundy silk tie",
    "cpb": "a tailored black two-piece business suit and a pale-pink formal shirt with an open collar, no tie",
    "apl": "a tailored mid-grey two-piece business suit, a lavender formal shirt and a navy-blue silk tie",
    "dfc": "a tailored chocolate-brown two-piece business suit and a light-blue formal shirt with an open collar, no tie",
    "cus": "a tailored dark olive-green two-piece business suit, a pale-blue formal shirt and a brown knitted tie",
    "bail": "a tailored royal-blue two-piece business suit and a light-grey formal shirt with an open collar, no tie",
    "plt": "a tailored steel-blue two-piece business suit, a pale-pink formal shirt and a dark-grey silk tie",
    "trl": "a tailored deep maroon two-piece business suit and a light-blue formal shirt with an open collar, no tie",
    "tej": "a tailored midnight-blue two-piece business suit, a crisp white formal shirt and a deep red silk tie",  # judgment reel 26-10
    "ara": "a tailored dark teal-blue two-piece business suit, a crisp white formal shirt and a navy-blue silk tie",  # judgment reel 27-10
    "arun": "a tailored deep bottle-green two-piece business suit, a crisp white formal shirt and a dark-gold silk tie",  # judgment reel 27-10
    "krm": "a tailored graphite-grey pinstripe two-piece business suit, a pale-blue formal shirt and a deep burgundy silk tie",  # judgment reel 27-10
    "cft": "a tailored classic navy-blue two-piece business suit, a crisp white formal shirt and a silver-grey silk tie",  # judgment reel 27-10
    "rti": "a tailored black pinstripe two-piece business suit, a pale-lavender formal shirt and a silver silk tie",  # judgment reel 27-10
    "dgv": "a tailored deep aubergine-purple two-piece business suit, a crisp white formal shirt and a dark-grey silk tie",  # judgment reel 27-10
    "tex": "a tailored dark slate-blue two-piece business suit, a light-pink formal shirt and a navy-blue silk tie",  # judgment reel 27-10
    "levi": "a tailored warm chocolate-brown two-piece business suit, a cream formal shirt and a dark-green silk tie",  # judgment reel 28-10
    "khan": "a tailored mid-grey two-piece business suit, a crisp white formal shirt and a deep maroon silk tie",  # judgment reel 28-10
    "jain": "a tailored dark camel-tan two-piece business suit, a crisp white formal shirt and a navy-blue silk tie",  # judgment reel 28-10
}
OUTFIT = OUTFITS.get(SET) or sys.exit(f"[sb] no outfit for {SET}: add one to OUTFITS (every video its own suit)")

STYLE = {
    "avatar": "@me",
    "useAccountAvatar": True,
    "hostName": "the presenter",
    "channelName": "LawWorld",
    "voice": "@me verified avatar voice (identical pitch, tone, accent in every clip)",
    "outfit": OUTFIT + " (identical in every scene)",
    "background": "a seamless, plain, very light ivory off-white studio backdrop (almost white, with only a faint warm tint), brightly and evenly lit from edge to edge with no falloff, no vignette, no shadows, no texture and no objects - nothing else in the frame; identical in every scene",
    "gestures": "He faces the camera squarely for the whole clip: head, shoulders and body stay square to the lens, he never turns to the left or right and never points or presents to the side. Animated, energetic open-palm gestures in front of his chest, counting points on his fingers, small confident nods and a bright smile on emphasis; relaxed fingers close together; hands stay in front of his body, inside the frame and never in front of his face; he stays standing in the same spot, at the same distance from the camera, throughout",
    "audio": "@me verified avatar voice ONLY, crisp, clear and high-energy, fast continuous speech at a quick trainer's pace, NO background music, NO sound effects, NO silence at the start or end",
    "negativePrompts": "He stays in the same spot with his face and upper body fully visible at all times; NO turning the head or body to the side, NO looking away from the camera, NO pointing or presenting to the left or right, NO arm stretched out to the side, NO arms, elbows, hands or shoulders touching or cut by the frame edges, NO oversized hands, NO hands held toward the camera, NO big or spread-out fingers, NO thin or lanky body, NO wide-angle lens distortion, NO furniture, NO bookshelves, NO plants, NO lamps, NO props, NO objects behind him, NO icons or graphics, NO text on screen, NO captions, NO name tags, NO logos, NO outfit change, NO camera cut, NO tripod, NO camera or microphone or any studio equipment visible in frame, NO other people",
    "camera": "Locked-off static shot, vertical. A medium-wide shot: he is STANDING in the middle of the frame, framed from mid-thigh up and fairly small in the frame, so his body fills only about the middle half of the frame width with wide empty backdrop on BOTH sides of him; his shoulders, elbows and hands always stay well inside the frame; clear space above his head. Eye level, natural portrait-lens look, no zoom, no pan, no camera movement; the camera itself is never visible",
    "realism": "Photorealistic live-action footage of a real human presenter recorded in one studio session against a plain ivory backdrop, NOT a furnished room. Soft, bright, even high-key light: a soft frontal key light on his face with soft fill, no harsh shadows, natural skin texture, natural eye contact straight into the lens and PERFECT LIP SYNC: his lips, jaw and mouth shapes match every syllable of the dialogue exactly, in time with the voice, no mouth movement without sound and no sound without mouth movement, identical exposure and white balance in every scene. TRUE-TO-LIFE BODY: natural adult proportions that match his face - broad shoulders, a solid average build that fills the jacket (not slim, not lanky), and SLENDER, NATURAL-SIZE HANDS: each hand no longer than his face, relaxed fingers held close together, never spread wide, hands never closer to the camera than his chest",
    "delivery": "FAST, HIGH-ENERGY delivery, like a top law educator on YouTube coaching advocates straight to camera: quick, punchy pace (about 160 words per minute) with no slow stretches, a strong confident voice, rising energy, crisp emphasis on key words, bright smile, lively eyes; CRISP, PRECISE DICTION: every word pronounced fully, clearly and correctly in neutral Indian English, every consonant clear, the letters of an acronym spoken one by one (B N S S); only a very brief breath at each full stop; speak the dialogue exactly once, word for word, never repeat, stretch or slow down a word, never add words",
}
VISUAL = ("The presenter standing in the middle of the frame against the plain, evenly lit ivory backdrop, wide empty space on both sides "
          "of him, facing the camera squarely and speaking fast and energetically straight to camera with perfectly lip-synced speech, hands in front "
          "of his chest, same position, size, outfit and framing in every clip, no text.")
# scenes[0] of every storyboard is the anchor: c00 (never rendered) with a borrowed --ref frame, else c01 itself (rendered first,
# from the text alone; every later clip is matched to c01's last frame)
ANCHOR = ({"sceneId": "c00", "sanitizeDialogue": False, "visual3D": VISUAL, "dialogue": "Welcome to LawWorld."} if REF else
          {"sceneId": ALL["scenes"][0]["sceneId"], "sanitizeDialogue": False, "visual3D": VISUAL, "dialogue": ALL["scenes"][0]["dialogue"]})

for secs in (6, 8, 10):
    path = f"split/{SET}_{secs}s.json"
    old = json.load(open(path)) if os.path.exists(path) else {}
    scenes = [ANCHOR] + [{"sceneId": s["sceneId"], "sanitizeDialogue": False, "visual3D": VISUAL, "dialogue": s["dialogue"]}
                         for s in ALL["scenes"] if s["seconds"] == secs and s["sceneId"] != ANCHOR["sceneId"]]
    sb = {"aspectRatio": "9:16", "maxWordsPerClip": 32, "downloadFolder": D, "useLastFrameReference": True, "referenceFrameFrom": "first",
          "transition": {"type": "cut"}, "globalStyle": STYLE, "projectTitle": f"LawWorld_{SET}_{secs}s", "clipDurationSeconds": secs,
          "scenes": scenes}
    if old.get("flowProjectUrl") and "--new-project" not in sys.argv: sb["flowProjectUrl"] = old["flowProjectUrl"]   # keep the Flow project once it exists
    json.dump(sb, open(path, "w"), indent=1, ensure_ascii=False)
    print(f"[sb] {path}: {len(scenes) - 1} clips")
