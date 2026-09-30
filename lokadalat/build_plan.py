import json,re,difflib,subprocess,os
os.chdir("/Users/admin/Downloads/New short/product-explainer")
SRC="/Users/admin/Downloads/FAAAH/ Lok Adalats.mp4"; OUT="out/lokadalat"; os.makedirs(OUT,exist_ok=True)
d=json.load(open("lokadalat/words_raw.json")); W=d["words"]; S=json.load(open("lokadalat/sentences.json"))
KEEP=[0,2,3,7,8,9,10]
norm=lambda w: re.sub(r"[^a-z0-9]","",w.lower())
HOOK=1.5; END=3.0; t=HOOK; segs=[]; words=[]
for n,i in enumerate(KEEP):
    s=S[i]; nxt=S[i+1]["start"] if i+1<len(S) else 999
    tin=max(0,s["start"]-0.12); tout=min(s["end"]+0.3,nxt-0.06)
    text=s["text"].replace("Law World","LawWorld")
    toks=[x for x in text.split() if norm(x)]
    ws=[w for w in W if w["start"]>=s["start"]-0.05 and w["end"]<=s["end"]+0.05]
    sm=difflib.SequenceMatcher(a=[norm(x) for x in toks],b=[norm(w["word"]) for w in ws],autojunk=False); tm=[None]*len(toks)
    for tag,i1,i2,j1,j2 in sm.get_opcodes():
        if tag=="equal":
            for k in range(i2-i1): tm[i1+k]=(ws[j1+k]["start"],ws[j1+k]["end"])
        elif tag=="replace" and j2>j1:
            a,b=ws[j1]["start"],ws[j2-1]["end"];m=i2-i1
            for k in range(m): tm[i1+k]=(a+(b-a)*k/m,a+(b-a)*(k+1)/m)
    for k in range(len(toks)):
        if tm[k] is None:
            p=next((tm[j][1] for j in range(k-1,-1,-1) if tm[j]),s["start"]); tm[k]=(p,p+0.25)
    for k,x in enumerate(toks): words.append({"word":x,"start":round(t+tm[k][0]-tin,3),"end":round(t+tm[k][1]-tin,3),"sid":i})
    segs.append({"clip":SRC,"in":round(tin,3),"out":round(tout,3),"push":0.045,"base":round(t,3),"sid":i}); t+=tout-tin
pend=round(t,3); total=round(pend+END,3)
def at(sid,target,nth=1):
    h=0
    for w in words:
        if w["sid"]==sid and norm(w["word"]).startswith(norm(target)):
            h+=1
            if h==nth: return w["start"]
    print("WARN",sid,target); return next(w["start"] for w in words if w["sid"]==sid)
E=lambda sid: max(w["end"] for w in words if w["sid"]==sid)
cues=[]; sfx=[]; cuts=[]
def stock(name,t0,L,off=1.5):
    cuts.append({"clip":f"stock/v/{name}.mp4","start":round(t0,3),"end":round(t0+L,3),"offset":off,"fade":0.12}); sfx.append({"file":"audio/sfx/whoosh.mp3","at":round(t0-0.12,3),"gain_db":-14})
fx=lambda n,tt,g=-10: sfx.append({"file":f"audio/sfx/{n}.mp3","at":round(max(0,tt),3),"gain_db":g})
cues.append({"type":"hook","t0":0,"t1":HOOK+0.15,"fade_out":0.15,"l1":"WHAT IS A","l2":"LOK ADALAT?","l3":"India's People's Court"}); fx("slam",0.02,-6); fx("riser",HOOK-0.8,-16)
cues.append({"type":"grain","t0":0,"t1":total,"fade_out":0.01})
tr=at(0,"Rani"); cues.append({"type":"lower_third","t0":tr-0.1,"t1":E(0)+1.2,"name":"Rani","role":"LawWorld"})
tp=at(2,"People"); cues.append({"type":"title","t0":tp-0.1,"t1":E(2),"title":"People's Court","sub":"Alternative dispute resolution","sub_at":at(2,"alternative")-0.05,"fade_out":0.25}); fx("pop",tp,-12)
# s3: the source already shows the map + "14th March 1982" -> no card here
ts=at(7,"Section"); cues.append({"type":"title","t0":ts-0.1,"t1":E(7),"title":"Section 21","sub":"Award = decree of a civil court","sub_at":at(7,"deemed")-0.05,"fade_out":0.2}); fx("pop",ts,-12)
INS_END=next(sg["base"] for sg in segs if sg["sid"]==8)+(64.65-next(sg["in"] for sg in segs if sg["sid"]==8))
f1=max(at(8,"final")-0.05,INS_END)
cues.append({"type":"slam","t0":f1,"t1":E(8)+0.15,"words":[{"text":"FINAL.","at":f1},{"text":"BINDING.","at":at(8,"binding")-0.05},{"text":"NO APPEAL.","at":at(8,"appeal")-0.35,"hl":True}]}); [fx("slam",at(8,x),-12) for x in ("final","binding")]
tc=at(9,"court"); cues.append({"type":"chips","t0":tc-0.2,"t1":E(9),"side":"lowrow","top":1420,"fade_out":0.25,"items":[{"text":"No court fees","icon":"indian-rupee","at":tc-0.2},{"text":"No strict procedure","icon":"file-text","at":at(9,"strict")-0.1},{"text":"Compoundable cases only","icon":"scale","at":at(9,"cannot")-0.1}]}); [fx("pop",x,-14) for x in (tc,at(9,"strict"),at(9,"cannot"))]
tb=at(10,"backlog"); cues.append({"type":"stat","t0":tb-0.2,"t1":E(10)+0.2,"num":"↓","label":"Court backlog","sub":"cases settled faster","fade_out":0.25}); fx("ding",tb,-12)
stock("the-scales-of-justice-47602",at(2,"rooted")-0.05,1.8,1.0)
stock("judge-pronounces-sentence-in-court-46820",at(7,"award")-0.05,1.9,2.0)
stock("handshake-over-the-contract-24229",at(9,"Lok")-0.05,1.5,1.0)
stock("close-up-of-a-tall-stack-of-papers-on-a-45923",at(10,"massive")-0.05,1.9,2.0)
for a in segs[1:]: fx("whoosh",a["base"]-0.1,-18)
cues.append({"type":"endc","t0":pend-0.1,"t1":total,"fade_out":0.01,"amt":"LawWorld","what":"Law, made simple","who":"follow for more legal explainers","link":"lawworld.ai","link_at":pend+0.5,"logo_at":pend+0.9,"url":"LAWWORLD.AI"}); fx("slam",pend-0.1,-8)
cues.append({"type":"kcap","t0":HOOK,"t1":pend+0.2,"words":[{k:w[k] for k in ("word","start","end")} for w in words],"max_words":3,"max_dur":1.4})
json.dump({"duration":total,"scrim_from":9999,"zlow":True,"cues":cues},open(f"{OUT}/timeline.json","w"),indent=1,ensure_ascii=False)
plan={"fps":24,"out":f"{OUT}/lokadalat.mp4","presenter_start":HOOK,"presenter":[{k:s[k] for k in ("clip","in","out","push")} for s in segs],"cutaways":cuts,
 "endcard":{"clip":"brand/cream_tail.mp4","dur":END+0.3,"offset":0,"xfade":0.3},"music":{"file":"audio/bed_office_160s.mp3","target_lufs":-25,"fade_in":0.3,"fade_out":2.2,"duck":True},
 "voice_lufs":-15,"sfx":sfx,"match_bg":False,"grade_presenter":"eq=contrast=1.05:saturation=1.04,unsharp=5:5:0.35:5:5:0","overlays":{"dir":f"{OUT}/frames","fps":24},"delogo":None,"total":total,"tail_black":0}
json.dump(plan,open(f"{OUT}/plan.json","w"),indent=1)
print(f"segments {len(segs)}, speech {HOOK}-{pend}s, total {total}s")
