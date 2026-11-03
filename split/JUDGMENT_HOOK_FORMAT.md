# Judgment reels, HOOK format (v2, owner 02-11-2026)

Why: viewers were leaving in the first seconds of the classic reels (greeting first, "Thanks for watching" last). The classic format
stays as it is; this is a second format for the same toolchain, switched on per reel by one line in its cue file:

    FORMAT = "hook"        # in split/cues/<set>.py

What the flag changes (split/build_course_plan.py, split/build_vertical_course.py; sets without it build exactly as before):
- no opening title sting and no slam/riser: the lead is 15 frames (0.625 s), which is exactly the cover thumbnail that
  `finish_judgment_reel.sh ship` lays over frames 0-14, so the hook question starts right after the cover;
- the "Ravishankar · LawWorld" name tag sits on the clip where he introduces himself (the first clip whose text has "Ravishankar");
- the panel slides in under the cover; the 9:16 edit starts on the presenter's first frame.

## Order (10 clips x 10 s, about 100 s)

| Clip | Part | Rule |
|---|---|---|
| c01 | Hook | A question an advocate cares about. No greeting and NO address: never open with "Advocates," (owner 03-11-2026: "i dont need that advocate name in the starting"). Start straight on the question or the situation, e.g. "Can lenders back out of a resolution plan they already approved...?" Starts the video. `check_scenes.py` flags a c01 that starts with "Advocate". |
| c02 | Curiosity | Build up the story: the stakes, a twist, a number, two forums disagreeing. End on a question or a cliff-hanger. |
| c03 | Intro | "Hi, I'm Ravishankar from LawWorld." + date + bench ("Honourable Justice ..." once per judge). Bench card here. |
| c04-c07 | Facts, case, discussion | Facts -> what went wrong below -> each side's argument. Whole sentences, every clip ends on a full stop. |
| c08 | The request | "Before I tell you what the Supreme Court decided, a quick request: follow LawWorld, and try India's all in one A I platform for advocates at lawworld dot A I." (HC reels: "what the High Court decided") |
| c09 | Verdict | Starts "Finally, what did the Supreme Court decide?" then the holding. |
| c10 | Verdict | Reasoning / result / orders. The video ends on the verdict (no "Thanks for watching" clip). |

Chapters: `# 1 · <HOOK TITLE>` (c01-c03, the intro keeps the Sisinty cuts), `# 2 · ...` facts, `# 3 · ...` discussion,
`# 4 · BEFORE THE VERDICT` (c08), `# 5 · WHAT THE COURT HELD` (c09-c10).

## Cards
- c01 `question` (the hook); c02 `counters` / `point` / `notequal` (the tension); c03 `bench` with official photos.
- `cite` bar for the case during the facts; c08 a `point` ("The verdict is next. First, a quick request…") then a `list`
  headed "Follow LawWorld · lawworld.ai" (search judgments, draft with AI, ₹200 AI credit); c09-c10 `list` / `point` / `verdicts`.
- No `STING` needed. `ENDCARD` as before.

## Card layout gate (owner 02-11-2026: "dont make those type of faults again")
After the mock plan and BEFORE any render: `V_LAYOUT=judgment python3 split/check_layout.py <set> --mock` must print `LAYOUT OK`.
It renders every card alone at the moment it is fully built and fails on two cards covering each other (kps c04: the step boxes hid
the case bar) or a card cut off at the 9:16 edge. post_course.sh runs it again and stops on a FAIL; the ship step refuses without
`LAYOUT OK`. Keep step / node labels short (two lines in a box) and give a tall card its own clip without the cite bar.

## Everything else is unchanged from the classic judgment reels
Reportable judgments only, official PDF, facts with paragraph numbers in the header comments, Flow policy (no private names with
accusations, no "fraud" / "collusion" / "admitted"), no digits in speech, 38-43 syllables per 10 s clip (`check_scenes.py`),
list items <= 52 chars, `"ok": False` only for what the Court rejected, own suit per reel (OUTFITS, dark colours only), pilot c01
then `touch split/GO<set>`, `V_LAYOUT=judgment NO_DELIVER=1 OVERLAY_WORKERS=1 post_course.sh`, thumbnail `python3 split/thumb_darkfoot.py out/<set>/thumb_brand.json`
(owner 02-11-2026: this design for every judgment reel - cream top, three strips in copper / blue / green, the court as a picture block with the
judges at its sides, a dark foot for the apps' view count; writes thumb_brand.png, which the ship step lays over the first 15 frames),
`finish_judgment_reel.sh <set> qa|ship`. First reel in this format: `kps` (Bank of India v. S.M. Kamal Pasha, 2026 INSC 1154).
