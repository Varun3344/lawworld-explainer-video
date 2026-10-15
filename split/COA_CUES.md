# Cause of Action full video: layout and cue contract (v4)

Owner, 15 Oct 2026: "avatar position jumping scene to scene (one scene in front, another backside) — make it properly; show avatar
on the RIGHT side and content on the LEFT side; make hand moves properly, sometimes show the content-side hand; create the full video".

## Layout (v4, `timeline.layout = {"presenter": "right", "px": 640}`)
- 1920x1080, 24 fps. Presenter (9:16 footage, backdrop flattened to the page cream) fills x 1280..1920 (right third).
- Panel (all explanation content) fills x 0..1280 (left two thirds). The seam is at x = 1280, the panel's RIGHT edge.
- ONE SCREEN: nothing marks the seam at rest; the 48 px feather sits over the presenter's LEFT edge (x 1280..1328: #f5f0e8 at
  1280 -> transparent at 1328); blobs/watermark fade out before the seam; no element may visibly emerge from, cross or be clipped
  at x = 1280 (enter from the left / top / bottom frame edges, or pop in place).
- Content column inside the panel: about 100 px from the frame's left edge to about 112 px before the seam (mirror of v3).
- The presenter gestures toward screen-left (the panel) in some clips.
- Lower third ("Ravishankar / LawWorld") on the presenter side, inside x 1280..1920.
- The sting retracts to reveal the presenter on the right; the endcard widens from the panel over the presenter.

## Cue contract
All times in seconds on the video timeline. Every cue has `type`, `t0`, `t1` (visible span) and optional `fade_out`.
Existing types keep their fields (see split/build_split_plan.py): sting, panel (scenes = chip labels), lower_third, title,
question, stamp, list, strike, point, kicker, quote, cite, equation, bundle, endcard.

New / extended types (scenes 3-7):

### blocks (scene 3a: the bundle opens into RIGHT and BREACH, then they slide together)
`{type:"blocks", t0, t1, open_at, items:[{label:"PLAINTIFF'S RIGHT", sub:"a right that belongs to the plaintiff", at},
  {label:"DEFENDANT'S BREACH", sub:"an act or omission that infringes it", at}], merge:{label:"CAUSE OF ACTION", at}}`
- open_at: a small tied bundle (same look as the scene-2 bundle) opens; item i builds at its `at` (number badge 1 / 2, label in
  caps, sub-line); at merge.at both blocks slide together and fuse into one accent block labelled merge.label.

### verdicts (scene 3b: two wrong combinations crossed out, the right one highlighted)
`{type:"verdicts", t0, t1, rows:[{text:"Right, no breach", ok:false, at}, {text:"Breach, but not of your right", ok:false, at},
  {text:"Your right + breach by this defendant", ok:true, at}]}`
- ok:false rows build then get struck through and greyed (red cross icon); the ok:true row lands highlighted in the accent colour
  (check icon), the others stay greyed above it.

### timeline (scene 4a: the loan story)
`{type:"timeline", t0, t1, nodes:[{label:"LOAN", value:"₹5,00,000", sub:"Ravi → Suresh", at}, {label:"DUE", value:"31 Mar 2025", at},
  {label:"REPAID", value:"₹0", tone:"red", at}]}`
- A horizontal line draws left to right; each node pops in at its `at` with label, value (large) and optional sub; tone "red"
  renders the value in red.

### checklist (scene 4b: what Ravi must prove, folding into a bundle)
`{type:"checklist", t0, t1, head:"What must Ravi prove?", head_at, items:[{n:1, text:"Loan given", at}, ...4 items],
  fold:{label:"Ravi's cause of action", at}}`
- Each item ticks in at its `at` (number + text + tick). At fold.at the four items shrink and fold into one tied bundle (same visual
  language as the scene-2 bundle) labelled fold.label.

### notequal (scene 5: "Cause of action ≠ the defence" / "≠ the relief")
`{type:"notequal", t0, t1, left:"Cause of action", right:"the defence", at, sub:"Read the plaint, not the written statement", sub_at}`
- Big "left ≠ right" line (the ≠ in accent), optional sub-line under it.

### splitcard (scene 5b: relief vs cause of action)
`{type:"splitcard", t0, t1, left:{title:"RELIEF", text:"what you ask for", at}, right:{title:"CAUSE OF ACTION", text:"why you are entitled to it", at}}`
- One card split in two halves; each half builds at its `at`; the right half in the accent colour.

### pin (scenes 4-6: the date the cause of action arose)
`{type:"pin", t0, t1, text:"Arose: 1 Apr 2025", land_at, fly_at, slot:5}`
- At land_at a date stamp lands (stamp-like hit) in the middle of the panel, then shrinks and parks in the panel's top corner (below
  the header, away from the seam), where it stays across scenes 5 and 6. At fly_at it flies into slot `slot` of the active `slots`
  cue (scene 6) and the slot's clock starts.

### slots (scene 6: five reasons it matters; persistent through the scene)
`{type:"slots", t0, t1, head:"Why it matters", head_at, slots:[
   {n:1, title:"PLEAD IT", at, rule:"O. VII R. 1(e) CPC", text:"the facts + the date it arose"},
   {n:2, title:"OR LOSE IT", at, rule:"O. VII R. 11(a) CPC", text:"no cause of action → plaint rejected",
         sub:"The court reads the plaint and its documents only", sub_at},
   {n:3, title:"WHERE TO SUE", at, rule:"S. 20(c) CPC", text:"where it arises, wholly or in part",
         visual:"map", pins:[{label:"Loan given here", at}, {label:"Repayment due here", at}]},
   {n:4, title:"ONE SHOT", at, rule:"O. II R. 2 CPC", text:"sue for the whole claim",
         visual:"bar", claimed:"₹3,00,000 claimed", lost:"₹2,00,000 lost", split_at},
   {n:5, title:"THE CLOCK", at, rule:"Limitation Act, 1963", text:"the Schedule fixes when time begins to run",
         visual:"clock", clock_at}]}`
- At head_at the heading and five EMPTY numbered slots appear; each slot fills at its `at` (title) and the active slot shows its
  detail (rule + text + visual) large; earlier slots stay filled but compact.

### cite (extended)
Optional `cases:[{name, cite}, ...]` (up to 2 lines) instead of `text`, for a caption bar that names two authorities at once.

### quote (unchanged)
Used in scene 6 for the Arivandandam line if the exact judgment wording is verified.

### endcard (extended)
Optional `line` (e.g. "Cause of action = every fact you must prove to win") shown between the title and `sub`.
