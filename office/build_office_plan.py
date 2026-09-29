"""Full product video, office set, steady Sisinty-style edit.
Clips o01..o17 (whole clips, head/tail pauses trimmed), one static zoom per section, captions, chips, stat cards,
3D inserts (3-4 s), pricing canvas, dark logo end card, SFX at section changes."""
import os, json, subprocess, difflib, importlib.util
spec = importlib.util.spec_from_file_location("words", "scripts/words.py"); W = importlib.util.module_from_spec(spec); spec.loader.exec_module(W); norm = W.norm
def dur(f): return float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f],capture_output=True,text=True).stdout.strip())
D="downloads/office"; B="downloads/office_broll/broll_realistic"; OUT="out/office"; os.makedirs(OUT, exist_ok=True)
SCRIPT={s["sceneId"]: s["dialogue"] for s in json.load(open("office/office_all_scenes.json"))["scenes"]}
SCRIPT["o16"]="The Pro plan costs just ₹1,500 per month, or ₹12,000 for the whole year, plus GST."
IDS=[f"o{i:02d}" for i in range(1,18) if os.path.exists(f"{D}/o{i:02d}.mp4")]
SECTION={"o01":0,"o02":0,"o03":1,"o04":1,"o05":2,"o06":2,"o07":2,"o08":2,"o09":3,"o10":3,"o11":3,"o12":4,"o13":4,"o14":4,"o15":5,"o16":5,"o17":5}
ZOOM=[1.0,1.08,1.0,1.08,1.0,1.06]
HOOK=1.6; END=3.4
t=HOOK; segs=[]; words=[]
for cid in IDS:
    c=f"{D}/{cid}.mp4"; d=dur(c); wj=json.load(open(f"{D}/{cid}.words.json")); ws=wj["words"]
    toks=[x for x in SCRIPT[cid].split() if x.strip("—–-")]
    sm=difflib.SequenceMatcher(a=[norm(x) or "x" for x in toks], b=[norm(w["word"]) or "x" for w in ws], autojunk=False); tm=[None]*len(toks)
    for tag,i1,i2,j1,j2 in sm.get_opcodes():
        if tag=="equal":
            for k in range(i2-i1): tm[i1+k]=(ws[j1+k]["start"],ws[j1+k]["end"])
        elif tag=="replace" and j2>j1:
            a,b=ws[j1]["start"],ws[j2-1]["end"]; n=i2-i1
            for k in range(n): tm[i1+k]=(a+(b-a)*k/n,a+(b-a)*(k+1)/n)
    for i in range(len(toks)):
        if tm[i] is None:
            p=next((tm[k][1] for k in range(i-1,-1,-1) if tm[k]),0.0); q=next((tm[k][0] for k in range(i+1,len(toks)) if tm[k]),d); tm[i]=(p,min(q,p+0.3))
    s0=tm[0][0]; s1=tm[-1][1]
    tin=max(0.0,s0-0.12); tout=min(d,s1+0.25)
    segs.append({"clip":c,"in":round(tin,3),"out":round(tout,3),"zoom":ZOOM[SECTION[cid]],"base":round(t,3),"cid":cid})
    for i,x in enumerate(toks): words.append({"word":x,"start":round(t+tm[i][0]-tin,3),"end":round(t+tm[i][1]-tin,3),"cid":cid})
    t+=tout-tin
pend=round(t,3); total=round(pend+END,3)
def at(cid,target,nth=1,fb=None):
    tg=[norm(x) for x in (target if isinstance(target,list) else [target])]; h=0
    for w in words:
        if w["cid"]!=cid: continue
        n=norm(w["word"])
        if any(n==g or (len(g)>=4 and n.startswith(g)) for g in tg):
            h+=1
            if h==nth: return w["start"]
    print(f"[plan] WARNING {cid}: {target} not found"); 
    return fb if fb is not None else next((w["start"] for w in words if w["cid"]==cid),0)
S=lambda cid: next(s["base"] for s in segs if s["cid"]==cid)
E=lambda cid: next(round(s["base"]+s["out"]-s["in"],3) for s in segs if s["cid"]==cid)
cues=[]; cuts=[]; sfx=[]
def fx(n,tt,g=-10): sfx.append({"file":f"audio/sfx/{n}.mp3","at":round(max(0,tt),3),"gain_db":g})
def ins(scene,t0,L,off=1.0,title=None,sub=None):
    p=f"{B}/{scene}_broll.mp4"
    if not os.path.exists(p): print("[plan] WARNING no scene",scene); return
    cuts.append({"clip":p,"start":round(t0,3),"end":round(t0+L,3),"offset":off,"fade":0.18}); fx("whoosh",t0-0.12,-14)
    if title: cues.append({"type":"title","t0":round(t0+0.1,3),"t1":round(t0+L,3),"title":title,"sub":sub,"sub_at":round(t0+0.6,3),"fade_out":0.25})
def chips(t0,t1,items):
    cues.append({"type":"chips","t0":round(t0,3),"t1":round(t1,3),"side":"lowrow","fade_out":0.25,"items":[{"text":a,"icon":b,"at":round(c,3)} for a,b,c in items]})
    for _,_,c in items: fx("pop",c,-14)
def stat(t0,t1,num,label,sub=None,count=False):
    cues.append({"type":"stat","t0":round(t0,3),"t1":round(t1,3),"num":num,"label":label,"sub":sub,"count":count,"fade_out":0.25}); fx("slam",t0,-10)
def chapter(t0,t1,text): pass   # section labels removed: they collided with captions
# hook
cues.append({"type":"hook","t0":0,"t1":HOOK+0.15,"fade_out":0.15,"l1":"ONE PLATFORM.","l2":"15+ AI TOOLS","l3":"built for Indian advocates"}); fx("slam",0.02,-6); fx("riser",HOOK-0.9,-16)
cues.append({"type":"grain","t0":0,"t1":total,"fade_out":0.01})
# o01
tn=at("o01","Ravishankar"); cues.append({"type":"lower_third","t0":tn-0.1,"t1":tn+4.5,"name":"Ravishankar","role":"Founder, LawWorld"})
# o02
tb,tf,tc=at("o02","better"),at("o02","faster"),at("o02","cheaper")
cues.append({"type":"slam","t0":tb-0.05,"t1":at("o02","Let")-0.05,"words":[{"text":"BETTER.","at":tb-0.05},{"text":"FASTER.","at":tf-0.05},{"text":"CHEAPER.","at":tc-0.05,"hl":True}]}); [fx("slam",x,-12) for x in (tb,tf,tc)]
t15=at("o02",["fifteen","15"]); tlw=at("o02","LawWorld",2,fb=t15-1.2)
cues.append({"type":"orbit","t0":max(tlw-0.1,t15-1.6),"t1":E("o02")+0.15,"fade_out":0.3,"num":"15+","label":"AI features","icons":["message-square","file-pen","search","languages","landmark","book-open","presentation","headphones","users","receipt-indian-rupee","calendar","shield-check"]}); fx("riser",tlw-0.4,-16); fx("slam",t15,-8)
ins("n01_features",S("o03")+0.02,2.2,1.5)
# o03 case prep
chapter(at("o03","For")-0.05,E("o04")-0.1,"Case preparation")
ins("n02_caseprep",at("o03","For")-0.1,2.4,1.0)
chips(at("o03","chatbot")-0.15,E("o03"),[("AI Chatbot","message-square",at("o03","chatbot")-0.15),("Drafting","file-pen",at("o03","drafting")-0.1),("Legal Research","search",at("o03","research")-0.1),("Translation","languages",at("o03","translation")-0.1)])
# o04 database
ins("n03_database",at("o04","You")-0.1,4.0,1.5,"Legal database","Judgments · Acts · Rules · Regulations")
# o05 library
ins("n04_library",at("o05","library")-0.3,3.6,1.0,"Library","Thousands of e-books and videos")
# o06 slides
ins("n05_slides",S("o06")+0.05,4.0,1.0,"Slides","Ready-made presentations on law")
chips(at("o06","teach")-0.1,E("o06"),[("Teach","presentation",at("o06","teach")-0.1),("Train juniors","users",at("o06","juniors")-0.1)])
# o07 law stories
ins("n06_lawstories",S("o07")+0.05,4.0,1.5,"Law Stories","Audio discussions on legal topics")
# o08 languages
tt=at("o08",["ten","10"]); ins("n07_languages",tt-0.8,3.4,1.5); stat(tt-0.05,tt+2.4,"10+","Indian languages")
# o09 clients
ins("n08_clients",S("o09")+0.05,3.0,1.5,"Client management","Team chat · Billing · Client portal")
chapter(S("o09")+0.05,E("o09")-0.1,"Client management")
chips(at("o09","informed")-0.1,E("o09"),[("Clients informed","users",at("o09","informed")-0.1),("Office organised","check",at("o09","organised",fb=E("o09")-1.2)-0.1)])
# o10 your cases
ins("n09_yourcases",S("o10")+0.05,3.2,1.2,"Your Cases","Connected to e-Courts")
tk=at("o10","track"); cues.append({"type":"phone","t0":tk-0.1,"t1":E("o10")+0.1,"fade_out":0.25,"head":"Your Cases","rows":[{"d":"⚖","t":"Every case","s":"synced from e-Courts","at":at("o10","case",2)-0.1},{"d":"📅","t":"Hearings","s":"dates in one place","at":at("o10","hearing")-0.1},{"d":"📄","t":"Orders","s":"as soon as they land","at":at("o10","order")-0.1}]}); fx("whoosh",tk-0.1,-14)
# o11 argument presenter
ins("n10_argument",S("o11")+0.05,4.2,1.5,"Argument Presenter","No heavy files to carry")
# o12 security
ins("n11_security",S("o12")+0.05,2.6,1.5)
chapter(S("o12")+0.05,E("o12")-0.1,"Security")
chips(at("o12",["dpdp"])-0.1,E("o12"),[("DPDP Act compliant","shield-check",at("o12",["dpdp"])-0.1),("Private","lock",at("o12","private")-0.1),("In your control","check",at("o12","control")-0.1)])
# o13 devices
ins("n12_devices",S("o13")+0.05,3.4,1.0)
chips(at("o13","web")-0.1,E("o13"),[("Web","monitor",at("o13","web")-0.1),("Android","smartphone",at("o13","Android")-0.1),("iOS","tablet",at("o13","iOS")-0.1)])
# o14 training
ins("n13_training",at("o14","Our")-0.1,3.8,1.0,"Training videos","Basic computer skills are enough")
# o15-o17 pricing canvas
tp0=at("o15","two")-0.1
cues.append({"type":"pricing","t0":tp0,"t1":E("o17")+0.2,"fade_out":0.3,"heading_at":tp0+0.1,
  "payg_at":at("o15",["pay-as-you-go","pay"],2,fb=at("o15","With"))-0.1,"payg_lines":[{"text":"No monthly fee","at":at("o15","monthly")-0.1},{"text":"Pay only for what you use","at":at("o15","only")-0.1}],
  "pro_at":at("o16","Pro")-0.1,"pro_lines":[{"text":"₹1,500 / month","at":at("o16",["₹1,500","1500"])-0.1},{"text":"₹12,000 / year","at":at("o16",["₹12,000","12000"])-0.1},{"text":"+ GST","at":at("o16","GST")-0.1},
     {"text":"Covers most of your needs","at":at("o17","covers")-0.1},{"text":"Add-ons & AI usage extra","at":at("o17",["add-ons","add"])-0.1}]}); fx("whoosh",tp0-0.12,-12)
# end card
cues.append({"type":"sweep","t0":pend+0.4,"t1":pend+1.6,"fade_out":0.01})
cues.append({"type":"endc","t0":pend-0.1,"t1":total,"fade_out":0.01,"amt":"LawWorld","what":"The all-in-one AI platform","who":"for advocates in India","link":"lawworld.ai","link_at":pend+0.6,"logo_at":pend+1.0,"url":"LAWWORLD.AI"}); fx("slam",pend-0.1,-8)
# section whooshes
prev=None
for s in segs:
    if prev is not None and SECTION[s["cid"]]!=SECTION[prev]: fx("whoosh",s["base"]-0.12,-16)
    prev=s["cid"]
cues.append({"type":"kcap","t0":HOOK,"t1":pend+0.2,"words":[{"word":w["word"],"start":w["start"],"end":w["end"]} for w in words],"max_words":3,"max_dur":1.4})
cues=[c for c in cues if c["type"]!="sweep"]+[c for c in cues if c["type"]=="sweep"]
json.dump({"duration":total,"scrim_from":9999,"zones":True,"cues":cues},open(f"{OUT}/timeline.json","w"),indent=1,ensure_ascii=False)
plan={"fps":24,"out":f"{OUT}/office.mp4","presenter_start":HOOK,"presenter":[{"clip":s["clip"],"in":s["in"],"out":s["out"],"push":0.05} for s in segs],"cutaways":cuts,
 "endcard":{"clip":"brand/cream_tail.mp4","dur":round(END+0.3,3),"offset":0.0,"xfade":0.3},"music":{"file":"audio/bed_office_160s.mp3","target_lufs":-25,"fade_in":0.3,"fade_out":2.5,"duck":True},
 "voice_lufs":-15,"sfx":sfx,"grade_presenter":"eq=contrast=1.06:saturation=1.04,unsharp=5:5:0.4:5:5:0","overlays":{"dir":f"{OUT}/frames","fps":24},"delogo":None,"total":total,"tail_black":0}
json.dump(plan,open(f"{OUT}/plan.json","w"),indent=1)
print(f"[plan] {len(segs)} clips, {len(cuts)} inserts, {len(sfx)} sfx, total {total}s")
