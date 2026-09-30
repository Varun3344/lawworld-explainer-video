"""Kannada version of the premium office product video.
Clips q01..q18 (Kannada, same office), the 13 premium scenes made for this video, Kannada captions and cards in layout zones."""
import os, json, re, subprocess
os.chdir("/Users/admin/Downloads/New short/product-explainer")
def dur(f): return float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f],capture_output=True,text=True).stdout.strip())
D=os.environ.get("KN_D","downloads/office_kn"); B="downloads/office_broll/broll_realistic"; OUT=os.environ.get("KN_OUT","out/office_kn"); os.makedirs(OUT, exist_ok=True)
IDS=[f"q{i:02d}" for i in range(1,19)]
missing=[c for c in IDS if not (os.path.exists(f"{D}/{c}.mp4") and os.path.exists(f"{D}/{c}.words.json"))]
if missing and "--allow-missing" not in os.sys.argv: raise SystemExit(f"[plan] missing clips: {missing}")
IDS=[c for c in IDS if c not in missing]
SECTION={**{f"q{i:02d}":0 for i in (1,2,3)},**{f"q{i:02d}":1 for i in (4,5)},**{f"q{i:02d}":2 for i in (6,7,8,9)},**{f"q{i:02d}":3 for i in (10,11,12)},**{f"q{i:02d}":4 for i in (13,14,15)},**{f"q{i:02d}":5 for i in (16,17,18)}}
HOOK=1.6; END=3.6
t=HOOK; segs=[]; words=[]
for cid in IDS:
    c=f"{D}/{cid}.mp4"; d=dur(c); w=json.load(open(f"{D}/{cid}.words.json")); s0,s1=w["speech_start"],w["speech_end"]
    tin=max(0.0,s0-0.12); tout=min(d,s1+0.28)
    if s1>=d-0.06 and w["words"]: tout=min(d,max(w["words"][-1]["end"]+0.45,d-0.35))   # no detectable tail pause: cut shortly after the last word
    segs.append({"clip":c,"in":round(tin,3),"out":round(tout,3),"base":round(t,3),"cid":cid})
    for x in w["words"]:
        a=min(max(x["start"],tin),tout); b=min(max(x["end"],a+0.05),tout)
        words.append({"word":x["word"],"start":round(t+a-tin,3),"end":round(t+b-tin,3),"cid":cid})
    t+=tout-tin
pend=round(t,3); total=round(pend+END,3)
strip=lambda w: re.sub(r"[\s.,;:!?\"'()\-–—]+","",w)
def at(cid,target,nth=1,fb=None):
    tg=[strip(x) for x in (target if isinstance(target,list) else [target])]; h=0
    for w in words:
        if w["cid"]!=cid: continue
        n=strip(w["word"])
        if any(n==g or n.startswith(g) for g in tg):
            h+=1
            if h==nth: return w["start"]
    if cid in IDS: print(f"[plan] WARNING {cid}: {target} not found")
    return fb if fb is not None else next((w["start"] for w in words if w["cid"]==cid),0)
has=lambda cid: cid in IDS
S=lambda cid: next(s["base"] for s in segs if s["cid"]==cid)
E=lambda cid: next(round(s["base"]+s["out"]-s["in"],3) for s in segs if s["cid"]==cid)
cues=[]; cuts=[]; sfx=[]
def fx(n,tt,g=-10): sfx.append({"file":f"audio/sfx/{n}.mp3","at":round(max(0,tt),3),"gain_db":g})
def ins(scene,t0,L,off=1.0,title=None,sub=None,cap=None):
    p=f"{B}/{scene}_broll.mp4"
    if not os.path.exists(p): print("[plan] WARNING no scene",scene); return
    if cap is not None: L=min(L,cap-t0)
    cuts.append({"clip":p,"start":round(t0,3),"end":round(t0+L,3),"offset":off,"fade":0.18}); fx("whoosh",t0-0.12,-14)
    if title: cues.append({"type":"title","t0":round(t0+0.1,3),"t1":round(t0+L,3),"title":title,"sub":sub,"sub_at":round(t0+0.6,3),"fade_out":0.25})
def chips(t0,t1,items):
    cues.append({"type":"chips","t0":round(t0,3),"t1":round(t1,3),"side":"lowrow","fade_out":0.25,"items":[{"text":a,"icon":b,"at":round(c,3)} for a,b,c in items]})
    for _,_,c in items: fx("pop",c,-14)
def stat(t0,t1,num,label,sub=None,count=False):
    cues.append({"type":"stat","t0":round(t0,3),"t1":round(t1,3),"num":num,"label":label,"sub":sub,"count":count,"fade_out":0.25}); fx("slam",t0,-10)
cues.append({"type":"hook","t0":0,"t1":HOOK+0.15,"fade_out":0.15,"l1":"ಒಂದೇ ವೇದಿಕೆ.","l2":"15+ AI ಸಾಧನಗಳು","l3":"ಭಾರತದ ವಕೀಲರಿಗಾಗಿ","instant":True}); fx("slam",0.02,-6); fx("riser",HOOK-0.9,-16)
cues.append({"type":"grain","t0":0,"t1":total,"fade_out":0.01})
if has("q01"):
    tn=at("q01","ರವಿಶಂಕರ್"); cues.append({"type":"lower_third","t0":tn-0.1,"t1":min(tn+4.5,E("q01")),"name":"ರವಿಶಂಕರ್","role":"ಸಂಸ್ಥಾಪಕ, LawWorld"})
if has("q02"):
    tb,tf,tc=at("q02","ಉತ್ತಮ"),at("q02","ವೇಗ"),at("q02","ಕಡಿಮೆ"); tl=at("q02","ಲಾ")
    cues.append({"type":"slam","t0":tb-0.05,"t1":tl-0.05,"words":[{"text":"ಉತ್ತಮ.","at":tb-0.05},{"text":"ವೇಗ.","at":tf-0.05},{"text":"ಕಡಿಮೆ ವೆಚ್ಚ.","at":tc-0.05,"hl":True}]}); [fx("slam",x,-12) for x in (tb,tf,tc)]
    cues.append({"type":"stat","t0":tl-0.05,"t1":E("q02"),"num":"LawWorld","label":"ವಕೀಲರಿಗಾಗಿ AI ವೇದಿಕೆ","sub":"ಭಾರತದ ಹೊಸ ಮತ್ತು ಅತ್ಯಂತ ಶಕ್ತಿಶಾಲಿ","fade_out":0.25}); fx("pop",tl,-12)
if has("q03"):
    t15=at("q03","ಹದಿನೈದ"); tp=at("q03","ಪ್ರತಿಯೊಂದೂ")
    cues.append({"type":"orbit","t0":S("q03")+0.05,"t1":tp-0.05,"fade_out":0.3,"num":"15+","label":"AI ವೈಶಿಷ್ಟ್ಯಗಳು","icons":["message-square","file-pen","search","languages","landmark","book-open","presentation","headphones","users","receipt-indian-rupee","calendar","shield-check"]}); fx("riser",S("q03")-0.3,-16); fx("slam",t15,-8)
    ins("n01_features",tp-0.05,E("q03")-(tp-0.05),1.5)   # hold to the end of the clip: no 1 s flash of the presenter between two inserts
if has("q04"):
    ins("n02_caseprep",at("q04","ಎಐ")-0.15,2.6,1.0)
    chips(at("q04","ಚಾಟ್")-0.15,E("q04"),[("AI Chatbot","message-square",at("q04","ಚಾಟ್")-0.15),("Drafting","file-pen",at("q04","ಡ್ರಾಫ್ಟಿಂಗ್")-0.1),("ಕಾನೂನು ಸಂಶೋಧನೆ","search",at("q04","ಸಂಶೋಧನೆ")-0.1),("ಅನುವಾದ","languages",at("q04","ಅನುವಾದ")-0.1)])
if has("q05"): ins("n03_database",S("q05")+0.05,4.2,1.5,"Legal Database","ತೀರ್ಪುಗಳು · ಕಾಯ್ದೆಗಳು · ನಿಯಮಗಳು")
if has("q06"): ins("n04_library",S("q06")+0.05,3.8,1.0,"Library","ಸಾವಿರಾರು ಇ-ಪುಸ್ತಕಗಳು ಮತ್ತು ವಿಡಿಯೋಗಳು")
if has("q07"):
    ins("n05_slides",S("q07")+0.05,4.0,1.0,"Slides","ಕಾನೂನು ವಿಷಯಗಳ ಸಿದ್ಧ ಪ್ರಸ್ತುತಿಗಳು")
    chips(at("q07","ಬೋಧಿಸಲು")-0.1,E("q07"),[("ಬೋಧನೆ","presentation",at("q07","ಬೋಧಿಸಲು")-0.1),("ಕಿರಿಯರಿಗೆ ತರಬೇತಿ","users",at("q07","ತರಬೇತಿ")-0.1),("ಸ್ಪಷ್ಟ ವಿವರಣೆ","sparkles",at("q07","ಸ್ಪಷ್ಟವಾಗಿ")-0.1)])
if has("q08"):
    ins("n06_lawstories",S("q08")+0.05,4.0,1.5,"Law Stories","ಕಾನೂನು ವಿಷಯಗಳ ಆಡಿಯೋ ಚರ್ಚೆಗಳು")
    chips(at("q08","ಪ್ರಯಾಣದಲ್ಲಿರಲಿ")-0.1,E("q08"),[("ಪ್ರಯಾಣದಲ್ಲಿ","map-pin",at("q08","ಪ್ರಯಾಣದಲ್ಲಿರಲಿ")-0.1),("ನ್ಯಾಯಾಲಯದಲ್ಲಿ ಕಾಯುವಾಗ","scale",at("q08","ನ್ಯಾಯಾಲಯದಲ್ಲಿ")-0.1)])
if has("q09"):
    tt=at("q09","ಹತ್ತ"); ins("n07_languages",tt-0.8,3.6,1.5); stat(tt-0.05,tt+2.6,"10+","ಭಾರತೀಯ ಭಾಷೆಗಳು")
if has("q10"):
    ins("n08_clients",S("q10")+0.05,3.4,1.5,"Client Management","Team Chat · Billing · Client Portal")
    tk=at("q10","ಕಕ್ಷಿದಾರರಿಗೆ"); chips(tk-0.1,E("q10"),[("ಕಕ್ಷಿದಾರರಿಗೆ ಸದಾ ಮಾಹಿತಿ","users",tk-0.1),("ವ್ಯವಸ್ಥಿತ ಕಚೇರಿ","check",at("q10","ಕಚೇರಿ")-0.1)])
if has("q11"):
    ins("n09_yourcases",S("q11")+0.05,3.0,1.2,"Your Cases","e-Courts ಜೊತೆ ಸಂಪರ್ಕ")
    tk=at("q11","ಪ್ರತಿದಿನ"); cues.append({"type":"phone","t0":tk-0.1,"t1":E("q11")+0.1,"fade_out":0.25,"head":"Your Cases","rows":[{"d":"⚖","t":"ಪ್ರತಿ ಕೇಸ್","s":"e-Courts ನಿಂದ","at":at("q11","ಕೇಸ್")-0.1},{"d":"📅","t":"ವಿಚಾರಣೆಗಳು","s":"ದಿನಾಂಕಗಳು ಒಂದೇ ಕಡೆ","at":at("q11","ವಿಚಾರಣೆ")-0.1},{"d":"📄","t":"ಆದೇಶಗಳು","s":"ಬಂದ ತಕ್ಷಣ","at":at("q11","ಆದೇಶ")-0.1}]}); fx("whoosh",tk-0.1,-14)
if has("q12"): ins("n10_argument",S("q12")+0.05,4.2,1.5,"Argument Presenter","ಭಾರವಾದ ಕಡತಗಳು ಬೇಕಿಲ್ಲ")
if has("q13"):
    ins("n11_security",S("q13")+0.05,2.8,1.5)
    chips(at("q13","ಡಿಪಿಡಿಪಿ")-0.1,E("q13"),[("DPDP ಕಾಯ್ದೆಗೆ ಅನುಗುಣ","shield-check",at("q13","ಡಿಪಿಡಿಪಿ")-0.1),("ಖಾಸಗಿ","lock",at("q13","ಖಾಸಗಿ")-0.1),("ನಿಮ್ಮ ನಿಯಂತ್ರಣದಲ್ಲಿ","check",at("q13","ನಿಯಂತ್ರಣ")-0.1)])
if has("q14"):
    ins("n12_devices",S("q14")+0.05,3.4,1.0)
    chips(at("q14","ವೆಬ್")-0.1,E("q14"),[("Web","monitor",at("q14","ವೆಬ್")-0.1),("Android","smartphone",at("q14","ಆಂಡ್ರಾಯ್ಡ್")-0.1),("iOS","tablet",at("q14","ಐಒಎಸ್")-0.1)])
if has("q15"): ins("n13_training",at("q15","ಪ್ರತಿ")-0.1,4.0,1.0,"Training Videos","ಸಾಮಾನ್ಯ ಕಂಪ್ಯೂಟರ್ ಜ್ಞಾನ ಸಾಕು",cap=E("q15"))
if has("q16") and has("q17") and has("q18"):
    tp0=at("q16","ಎರಡು")-0.1
    cues.append({"type":"pricing","t0":tp0,"t1":E("q18")+0.2,"fade_out":0.3,"heading_at":tp0+0.1,"heading":"ಪಾವತಿಗೆ ಎರಡು ಸರಳ <i>ಆಯ್ಕೆಗಳು</i>","per_month":"/ ತಿಂಗಳಿಗೆ","per_year":"/ ವರ್ಷಕ್ಕೆ",
      "payg_at":at("q16","ಪೇ")-0.1,"payg_lines":[{"text":"ಮಾಸಿಕ ಶುಲ್ಕ ಇಲ್ಲ","at":at("q16","ಮಾಸಿಕ")-0.1},{"text":"ಬಳಸಿದ್ದಕ್ಕೆ ಮಾತ್ರ ಪಾವತಿ","at":at("q16","ಬಳಸಿದ್ದಕ್ಕೆ")-0.1}],
      "pro_at":at("q17","ಪ್ರೊ")-0.1,"pro_lines":[{"text":"₹1,500","at":at("q17","ಒಂದು")-0.1},{"text":"₹12,000","at":at("q17","ಹನ್ನೆರಡು")-0.1},{"text":"+ GST","at":at("q17","ಜಿಎಸ್")-0.1},
         {"text":"ಬಹುತೇಕ ಅಗತ್ಯಗಳಿಗೆ ಸಾಕು","at":at("q18","ಬಹುತೇಕ")-0.1},{"text":"ಆಡ್-ಆನ್ ಮತ್ತು AI ಬಳಕೆಗೆ ಮಾತ್ರ ಹೆಚ್ಚುವರಿ","at":at("q18","ಆಡ್")-0.1}]})   # no whoosh here: it landed on the first words of the pricing line
cues.append({"type":"sweep","t0":pend+0.4,"t1":pend+1.6,"fade_out":0.01})
cues.append({"type":"endc","t0":pend-0.1,"t1":total,"fade_out":0.01,"amt":"LawWorld","what":"ವಕೀಲರಿಗಾಗಿ ಆಲ್-ಇನ್-ಒನ್ AI ವೇದಿಕೆ","who":"ಇಂದೇ ಪ್ರಯತ್ನಿಸಿ","link":"lawworld.ai","link_at":pend+0.6,"logo_at":pend+1.0,"url":"LAWWORLD.AI"}); fx("slam",pend-0.1,-8)
prev=None
for s in segs:
    if prev is not None and SECTION[s["cid"]]!=SECTION[prev]: fx("whoosh",s["base"]-0.12,-16)
    prev=s["cid"]
cues.append({"type":"kcap","t0":HOOK,"t1":pend+0.2,"words":[{"word":w["word"],"start":w["start"],"end":w["end"]} for w in words],"max_words":2,"max_dur":1.7})
cues=[c for c in cues if c["type"]!="sweep"]+[c for c in cues if c["type"]=="sweep"]
json.dump({"duration":total,"scrim_from":9999,"zones":True,"lang":"kn","cues":cues},open(f"{OUT}/timeline.json","w"),indent=1,ensure_ascii=False)
plan={"fps":24,"out":f"{OUT}/office_kn.mp4","presenter_start":HOOK,"presenter":[{"clip":s["clip"],"in":s["in"],"out":s["out"],"push":0.05} for s in segs],"cutaways":cuts,
 "endcard":{"clip":"brand/cream_tail.mp4","dur":round(END+0.3,3),"offset":0.0,"xfade":0.3},"music":{"file":"audio/bed_office_180s.mp3","target_lufs":-25,"fade_in":0.3,"fade_out":2.8,"duck":True},
 "voice_lufs":-15,"level_voice":True,"limit":0.78,"sfx":sfx,"grade_presenter":"eq=contrast=1.06:saturation=1.04,unsharp=5:5:0.4:5:5:0","overlays":{"dir":f"{OUT}/frames","fps":24},"delogo":None,"total":total,"tail_black":0}
json.dump(plan,open(f"{OUT}/plan.json","w"),indent=1)
print(f"[plan] {len(segs)} clips, {len(cuts)} inserts, {len(sfx)} sfx, speech {HOOK}-{pend}s, total {total}s")
