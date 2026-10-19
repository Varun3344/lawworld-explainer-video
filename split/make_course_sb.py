"""Flow storyboards for a LawWorld course video (owner 19-10-2026: the BNSS / CPC storyboard series, "dont turn avatar right and
left, just straight like before"). Reads split/<set>_all_scenes.json and writes split/<set>_{6,8,10}s.json for split/run_queue.sh.
The presenter faces the camera squarely in EVERY clip (no "presents" turns, no pointing to the side), gestures stay in front of his
chest, and every clip is anchored to one reference frame: scenes[0] of every storyboard is c00, which is never rendered - its
frame is downloads/<set>/frames/c00_last.jpg (by default the Cause of Action anchor, so the series keeps one look).
Usage: python3 split/make_course_sb.py <set> [--ref <jpg>]"""
import json, os, shutil, sys

SET = sys.argv[1]
REF = sys.argv[sys.argv.index("--ref") + 1] if "--ref" in sys.argv else "downloads/coa/frames/c01_last.jpg"
ALL = json.load(open(f"split/{SET}_all_scenes.json"))
D = os.path.abspath(f"downloads/{SET}")
os.makedirs(f"{D}/frames", exist_ok=True)
if not os.path.exists(f"{D}/frames/c00_last.jpg"): shutil.copy(REF, f"{D}/frames/c00_last.jpg")

STYLE = {
    "avatar": "@me",
    "useAccountAvatar": True,
    "hostName": "the presenter",
    "channelName": "LawWorld",
    "voice": "@me verified avatar voice (identical pitch, tone, accent in every clip)",
    "outfit": "a tailored navy-blue blazer over a crisp light-blue open-collar formal shirt, no tie (identical in every scene)",
    "background": "a seamless, plain, very light ivory off-white studio backdrop (almost white, with only a faint warm tint), brightly and evenly lit from edge to edge with no falloff, no vignette, no shadows, no texture and no objects - nothing else in the frame; identical in every scene",
    "gestures": "He faces the camera squarely for the whole clip: head, shoulders and body stay square to the lens, he never turns to the left or right and never points or presents to the side. Lively but controlled open-palm gestures in front of his chest, counting points on his fingers, small confident nods and a bright smile on emphasis; relaxed fingers close together; hands stay in front of his body, inside the frame and never in front of his face; he stays standing in the same spot, at the same distance from the camera, throughout",
    "audio": "@me verified avatar voice ONLY, clear and energetic, continuous speech at a brisk trainer's pace, NO background music, NO sound effects, NO silence at the start or end",
    "negativePrompts": "He stays in the same spot with his face and upper body fully visible at all times; NO turning the head or body to the side, NO looking away from the camera, NO pointing or presenting to the left or right, NO arm stretched out to the side, NO arms, elbows, hands or shoulders touching or cut by the frame edges, NO oversized hands, NO hands held toward the camera, NO big or spread-out fingers, NO thin or lanky body, NO wide-angle lens distortion, NO furniture, NO bookshelves, NO plants, NO lamps, NO props, NO objects behind him, NO icons or graphics, NO text on screen, NO captions, NO name tags, NO logos, NO outfit change, NO camera cut, NO tripod, NO camera or microphone or any studio equipment visible in frame, NO other people",
    "camera": "Locked-off static shot, vertical. A medium-wide shot exactly like the reference frame: he is STANDING in the middle of the frame, framed from mid-thigh up and fairly small in the frame, so his body fills only about the middle half of the frame width with wide empty backdrop on BOTH sides of him; his shoulders, elbows and hands always stay well inside the frame; clear space above his head. Eye level, natural portrait-lens look, no zoom, no pan, no camera movement; the camera itself is never visible",
    "realism": "Photorealistic live-action footage of a real human presenter recorded in one studio session against a plain ivory backdrop, NOT a furnished room. Soft, bright, even high-key light: a soft frontal key light on his face with soft fill, no harsh shadows, natural skin texture, natural eye contact straight into the lens and accurate lip sync, identical exposure and white balance in every scene. TRUE-TO-LIFE BODY: natural adult proportions that match his face - broad shoulders, a solid average build that fills the jacket (not slim, not lanky), and SLENDER, NATURAL-SIZE HANDS: each hand no longer than his face, relaxed fingers held close together, never spread wide, hands never closer to the camera than his chest",
    "delivery": "Highly energetic, enthusiastic legal trainer leading a masterclass for advocates, like a motivating coach talking straight to camera: bright smile, lively eyes, confident emphasis on key words, brisk clear pace, a tiny pause after each full stop; speak the dialogue exactly once, word for word, never repeat, stretch or slow down a word, never add words",
}
VISUAL = ("The presenter standing in the middle of the frame against the plain, evenly lit ivory backdrop, wide empty space on both sides "
          "of him, facing the camera squarely and speaking energetically straight to camera, hands in front of his chest, same position, "
          "size, outfit and framing as the reference frame, no text.")
ANCHOR = {"sceneId": "c00", "sanitizeDialogue": False, "visual3D": VISUAL, "dialogue": "Welcome to LawWorld."}   # never rendered

for secs in (6, 8, 10):
    path = f"split/{SET}_{secs}s.json"
    old = json.load(open(path)) if os.path.exists(path) else {}
    scenes = [ANCHOR] + [{"sceneId": s["sceneId"], "sanitizeDialogue": False, "visual3D": VISUAL, "dialogue": s["dialogue"]}
                         for s in ALL["scenes"] if s["seconds"] == secs]
    sb = {"aspectRatio": "9:16", "maxWordsPerClip": 32, "downloadFolder": D, "useLastFrameReference": True, "referenceFrameFrom": "first",
          "transition": {"type": "cut"}, "globalStyle": STYLE, "projectTitle": f"LawWorld_{SET}_{secs}s", "clipDurationSeconds": secs,
          "scenes": scenes}
    if old.get("flowProjectUrl"): sb["flowProjectUrl"] = old["flowProjectUrl"]   # keep the Flow project once it exists
    json.dump(sb, open(path, "w"), indent=1, ensure_ascii=False)
    print(f"[sb] {path}: {len(scenes) - 1} clips")
