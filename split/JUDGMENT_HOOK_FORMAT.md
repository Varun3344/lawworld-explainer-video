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
| c01 | Hook | A question an advocate cares about. No greeting. Starts the video. |
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

## Everything else is unchanged from the classic judgment reels
Reportable judgments only, official PDF, facts with paragraph numbers in the header comments, Flow policy (no private names with
accusations, no "fraud" / "collusion" / "admitted"), no digits in speech, 38-43 syllables per 10 s clip (`check_scenes.py`),
list items <= 52 chars, `"ok": False` only for what the Court rejected, own suit per reel (OUTFITS, dark colours only), pilot c01
then `touch split/GO<set>`, `V_LAYOUT=judgment NO_DELIVER=1 OVERLAY_WORKERS=1 post_course.sh`, `thumb_brand.py`,
`finish_judgment_reel.sh <set> qa|ship`. First reel in this format: `kps` (Bank of India v. S.M. Kamal Pasha, 2026 INSC 1154).
