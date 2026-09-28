# LawWorld explainer video pipeline

Builds the 9:16 LawWorld product explainer from the founder's script: Google Flow renders the presenter
(verified avatar, its own voice) and stylised 3D cut-away scenes; everything readable (captions, feature
chips, title cards, pricing, call to action) is rendered locally in the LawWorld brand so it stays sharp.

## Flow of a build

1. `storyboards/full_presenter_{10,8,6}s.json` — the script split into whole-sentence clips (26–33 words
   per 10 s, 20–24 per 8 s), cream studio, `sanitizeDialogue: false`. `full_broll3d.json` — 14 3D scenes,
   no text in shot, full-body figures.
2. `scripts/run_full_all.sh` — drives the (unmodified) reel-service Flow pipeline clip by clip on one
   browser, then `retake_pass.sh` re-renders any clip whose transcript is not verbatim.
3. `scripts/words.py` — whisper word timings + verbatim gate per clip.
4. `scripts/build_full_plan.py` — cues on the spoken words (chips, titles, "15+", pricing, CTA), per-clip
   cuts (`CUT`), skipped clips (`SKIP`), script-spelled captions → `timeline.json` + `plan.json`.
5. `scripts/build_overlay_html.py` → `overlays/overlay_brand.html`; `scripts/render_overlays.ts` renders
   it to a transparent PNG per frame (deterministic seek, headless Chrome).
6. `scripts/compose2.py` — three ffmpeg passes: audio mix (voice at −16 LUFS, music bed ducked), base
   video (studio colour matched across takes, cut-aways with alpha fades, cream end clip), overlays.
7. `scripts/finalize.sh` — opens on the logo card, one video + one audio stream (WhatsApp safe).
8. `scripts/qa_full.sh` — stream/frame counts, loudness, frame sheets, transcript of the mix.

## Brand

Cream `#f5f0e8`, paper `#fffcf6`, ink `#1f1e1d`, accent `#cc785c`, brand `#d97757`; Instrument Serif for
headings, Manrope for text; Lucide icons with the site's feature names; copper four-point-star mark with the
serif "LawWorld" wordmark (`brand/`).

## Lessons that cost time

- Flow's "Agent" toggle hides the settings pill; turn it off once per profile.
- A clip can come back silent or with words skipped — the transcript gate catches both.
- Single-graph ffmpeg deadlocked and dropped frames (picture drifted from sound); the three-pass compositor
  and `fps=24` on both overlay inputs fixed it.
- 3D prompts with people must say "full body, feet on the floor, nobody cropped or floating".
- Never overlay anything on the presenter's face; chips live in the lower third.
