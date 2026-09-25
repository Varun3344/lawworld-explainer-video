"""Writes overlays/overlay_brand.html with the site's Lucide icons inlined (file:// pages cannot fetch JSON)."""
import json, os
P = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
icons = json.load(open(os.path.join(P, "brand", "lucide_icons.json")))
html = r'''<!doctype html>
<html><head><meta charset="utf-8"><title>LawWorld overlay</title>
<style>
  @font-face{font-family:"Instrument Serif";font-style:normal;font-weight:400;src:url(../brand/fonts/Instrument_Serif_jizBRFtNs2ka5fXjeivQ4LroWlx-6zUTjnTLgNs.woff2) format("woff2");}
  @font-face{font-family:"Instrument Serif";font-style:italic;font-weight:400;src:url(../brand/fonts/Instrument_Serif_jizHRFtNs2ka5fXjeivQ4LroWlx-6zAjjH7Motmp5g.woff2) format("woff2");}
  @font-face{font-family:"Manrope";font-style:normal;font-weight:200 800;src:url(../brand/fonts/Manrope_xn7gYHE41ni1AdIRggexSvfedN4.woff2) format("woff2");}
  :root{--cream:#f5f0e8;--cream-soft:#faf7f2;--cream-deep:#ede6d9;--paper:#fffcf6;--ink:#1f1e1d;--ink-soft:#2a2624;--muted:#6b6660;--rule:#e0d7c6;--accent:#cc785c;--accent-deep:#b3573f;--accent-soft:#e8bfa9;--wash:#f5dfd0;--brand:#d97757;}
  html,body{margin:0;padding:0;width:1080px;height:1920px;overflow:hidden;background:transparent;}
  body{font-family:"Manrope",-apple-system,"Helvetica Neue",Arial,sans-serif;color:var(--ink);-webkit-font-smoothing:antialiased;}
  .serif{font-family:"Instrument Serif",Georgia,serif;font-weight:400;}
  .abs{position:absolute;left:0;top:0;}
  #scrim-bot{top:1400px;width:1080px;height:520px;background:linear-gradient(0deg,rgba(245,240,232,.94) 0%,rgba(245,240,232,.6) 42%,rgba(245,240,232,0) 100%);}
  .card{background:var(--paper);border:1.5px solid var(--rule);border-radius:24px;box-shadow:0 18px 50px rgba(31,30,29,.10),0 2px 6px rgba(31,30,29,.05);}
  .tile{width:60px;height:60px;border-radius:16px;background:var(--wash);display:flex;align-items:center;justify-content:center;flex:none;}
  .tile svg{width:32px;height:32px;stroke:var(--accent-deep);fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round;}
  /* sting */
  #sting{width:1080px;height:1920px;background:var(--cream);}
  #sting .wash{position:absolute;left:0;top:0;width:1080px;height:1920px;background:radial-gradient(circle at 82% 10%,rgba(245,223,208,.95) 0%,rgba(245,223,208,.5) 18%,rgba(245,240,232,0) 42%),radial-gradient(circle at 50% 46%,rgba(255,252,246,.9) 0%,rgba(245,240,232,0) 40%);}
  #sting .ring{position:absolute;left:390px;top:640px;width:300px;height:300px;border-radius:50%;border:1.5px solid rgba(179,87,63,.35);}
  #sting .mark{position:absolute;left:380px;top:630px;width:320px;height:320px;background:url(../brand/site_logo_mark.png) center/contain no-repeat;filter:drop-shadow(0 28px 50px rgba(120,60,30,.28));}
  #sting .word{position:absolute;left:200px;top:1010px;width:680px;height:182px;background:url(../brand/wordmark_ink.png) center/contain no-repeat;}
  #sting .tag{position:absolute;left:0;top:1230px;width:1080px;text-align:center;font-size:48px;color:var(--ink);}
  #sting .tag i{color:var(--accent);}
  /* lower third */
  .lt{left:64px;top:1225px;width:640px;height:144px;overflow:hidden;}
  .lt .bar{position:absolute;left:0;top:0;width:7px;height:144px;background:linear-gradient(180deg,var(--brand),var(--accent-deep));}
  .lt .mk{position:absolute;left:34px;top:36px;width:72px;height:72px;background:url(../brand/site_logo_mark.png) center/contain no-repeat;}
  .lt .name{position:absolute;left:134px;top:26px;font-size:54px;line-height:1;}
  .lt .role{position:absolute;left:136px;top:90px;font-size:28px;font-weight:500;color:var(--muted);}
  /* pills */
  .pills{left:0;top:130px;width:1080px;height:100px;display:flex;justify-content:center;gap:18px;}
  .pill{height:88px;padding:0 36px;border-radius:44px;background:var(--paper);border:1.5px solid var(--rule);display:flex;align-items:center;gap:14px;font-size:40px;font-weight:600;box-shadow:0 12px 34px rgba(31,30,29,.10);}
  .pill .dot{width:14px;height:14px;border-radius:50%;background:linear-gradient(135deg,var(--brand),var(--accent-deep));}
  /* lockup */
  .lockup{left:0;top:96px;width:1080px;height:150px;}
  .lockup .in{position:relative;margin:0 auto;width:620px;height:150px;}
  .lockup .mk{position:absolute;left:0;top:6px;width:138px;height:138px;background:url(../brand/site_logo_mark.png) center/contain no-repeat;filter:drop-shadow(0 10px 24px rgba(120,60,30,.25));}
  .lockup .wd{position:absolute;left:160px;top:12px;width:460px;height:124px;background:url(../brand/wordmark_ink.png) center/contain no-repeat;}
  /* big number */
  .bignum{left:0;top:940px;width:1080px;height:560px;text-align:center;background:radial-gradient(ellipse 62% 58% at 50% 45%,rgba(245,240,232,.92) 0%,rgba(245,240,232,.6) 45%,rgba(245,240,232,0) 75%);}
  .bignum .n{font-size:340px;letter-spacing:-8px;line-height:1;color:var(--ink);display:inline-block;}
  .bignum .rule{width:180px;height:3px;margin:20px auto 26px;background:linear-gradient(90deg,rgba(204,120,92,0),var(--accent),rgba(204,120,92,0));}
  .bignum .l{font-size:46px;font-weight:500;letter-spacing:10px;text-transform:uppercase;color:var(--accent-deep);}
  /* chapter */
  .chapter{left:0;top:118px;width:1080px;text-align:center;font-size:28px;font-weight:600;letter-spacing:7px;text-transform:uppercase;color:var(--accent-deep);display:flex;justify-content:center;align-items:center;gap:26px;}
  .chapter i{display:block;width:56px;height:1.5px;background:var(--accent-soft);}
  /* chips */
  .chips{left:0;top:0;width:1080px;height:1920px;}
  .chip{position:absolute;height:98px;border-radius:22px;display:flex;align-items:center;gap:18px;padding:0 24px 0 18px;box-sizing:border-box;white-space:nowrap;}
  .chip .t{font-size:38px;color:var(--ink);}
  .chips.right .chip{left:690px;width:350px;}
  .chips.left .chip{left:40px;width:350px;}
  .chips.row{top:1160px;height:auto;display:flex;flex-wrap:wrap;justify-content:center;gap:16px 16px;padding:0 60px;box-sizing:border-box;}
  .chips.row .chip{position:relative;left:auto;width:auto;}
  .chips.lowrow{top:1140px;height:auto;display:flex;flex-wrap:wrap;justify-content:center;gap:16px 16px;padding:0 60px;box-sizing:border-box;}
  .chips.lowrow .chip{position:relative;left:auto;width:auto;}
  /* title card over 3D */
  .title{left:0;top:140px;width:1080px;display:flex;justify-content:center;}
  .title .in{padding:26px 46px 28px;max-width:920px;text-align:center;}
  .title .h{font-size:76px;line-height:1.05;color:var(--ink);}
  .title .s{font-size:30px;font-weight:500;color:var(--muted);margin-top:10px;}
  /* captions */
  .caps{left:60px;top:1500px;width:960px;text-align:center;font-size:54px;font-weight:600;letter-spacing:-.4px;line-height:1.25;}
  .caps .box{display:inline-block;background:rgba(255,252,246,.92);border:1.5px solid var(--rule);border-radius:22px;padding:12px 26px;box-shadow:0 10px 30px rgba(31,30,29,.08);}
  .caps span{display:inline-block;margin:0 8px;color:rgba(107,102,96,.75);}
  .caps span.on{color:var(--accent-deep);}
  .caps span.done{color:var(--ink);}
  /* pricing canvas */
  .pricing{width:1080px;height:1920px;background:var(--cream);}
  .pricing .wash{position:absolute;left:0;top:0;width:1080px;height:1920px;background:radial-gradient(circle at 85% 8%,rgba(245,223,208,.9) 0%,rgba(245,240,232,0) 38%);}
  .pricing .h{position:absolute;left:0;top:190px;width:1080px;text-align:center;font-size:74px;color:var(--ink);}
  .pricing .h i{color:var(--accent);}
  .pcard{position:absolute;left:90px;width:900px;padding:34px 40px;box-sizing:border-box;}
  .pcard .head{display:flex;align-items:center;gap:20px;}
  .pcard .name{font-size:62px;line-height:1;color:var(--ink);}
  .pcard .price{display:flex;align-items:baseline;gap:16px;margin-top:22px;}
  .pcard .big{font-size:112px;line-height:1;color:var(--ink);letter-spacing:-2px;}
  .pcard .per{font-size:34px;font-weight:500;color:var(--muted);}
  .pcard .line{display:flex;align-items:center;gap:16px;font-size:36px;font-weight:500;color:var(--ink);margin-top:16px;}
  .pcard .line svg{width:30px;height:30px;stroke:var(--accent-deep);fill:none;stroke-width:2.4;stroke-linecap:round;stroke-linejoin:round;flex:none;}
  .pcard .line.sub{font-size:30px;color:var(--muted);}
  /* cta canvas */
  .cta{width:1080px;height:1920px;background:var(--cream);}
  .cta .wash{position:absolute;left:0;top:0;width:1080px;height:1920px;background:radial-gradient(circle at 80% 10%,rgba(245,223,208,.95) 0%,rgba(245,240,232,0) 40%),radial-gradient(circle at 20% 90%,rgba(245,223,208,.7) 0%,rgba(245,240,232,0) 35%);}
  .cta .card{position:absolute;left:90px;top:380px;width:900px;padding:46px 40px 44px;box-sizing:border-box;text-align:center;}
  .cta .amt{font-size:170px;line-height:1;color:var(--ink);letter-spacing:-4px;}
  .cta .what{font-size:64px;line-height:1.1;color:var(--accent-deep);margin-top:8px;}
  .cta .who{font-size:34px;font-weight:500;color:var(--muted);margin-top:14px;}
  .cta .link{position:absolute;left:0;top:1000px;width:1080px;text-align:center;font-size:46px;font-weight:600;color:var(--ink);}
  .cta .arrow{position:absolute;left:510px;top:1070px;width:60px;height:60px;}
  .cta .arrow svg{width:60px;height:60px;stroke:var(--accent-deep);fill:none;stroke-width:2.4;stroke-linecap:round;stroke-linejoin:round;}
  .cta .lk{position:absolute;left:0;top:1190px;width:1080px;height:160px;}
  .cta .lk .in{position:relative;margin:0 auto;width:640px;height:160px;}
  .cta .lk .mk{position:absolute;left:0;top:6px;width:148px;height:148px;background:url(../brand/site_logo_mark.png) center/contain no-repeat;}
  .cta .lk .wd{position:absolute;left:170px;top:16px;width:470px;height:126px;background:url(../brand/wordmark_ink.png) center/contain no-repeat;}
  .cta .url{position:absolute;left:0;top:1380px;width:1080px;text-align:center;font-size:34px;font-weight:600;letter-spacing:8px;text-transform:uppercase;color:var(--accent-deep);}
</style></head>
<body><div id="stage"></div>
<script>
const ICONS = __ICONS__;
const svg=(n)=>'<svg viewBox="0 0 24 24">'+(ICONS[n]||ICONS['sparkles']||'')+'</svg>';
const clamp=(x,a=0,b=1)=>Math.max(a,Math.min(b,x));
const outExpo=x=>x>=1?1:1-Math.pow(2,-10*x);
const outBack=x=>{const c1=1.70158,c3=c1+1;return 1+c3*Math.pow(x-1,3)+c1*Math.pow(x-1,2);};
const outCubic=x=>1-Math.pow(1-x,3);
const P=(t,t0,d)=>clamp((t-t0)/d);
let EL=[]; const stage=document.getElementById('stage');
function div(cls,html){const d=document.createElement('div');d.className='abs '+(cls||'');if(html!==undefined)d.innerHTML=html;stage.appendChild(d);return d;}
function chipHTML(i){return '<div class="chip card"><div class="tile">'+svg(i.icon)+'</div><div class="t serif">'+i.text+'</div></div>';}
function init(tl){
  stage.innerHTML='';EL=[];
  const sb=div(''); sb.id='scrim-bot'; EL.push({type:'_scrim',el:sb,t0:tl.scrim_from??0,t1:tl.duration});
  for(const c of tl.cues){
    switch(c.type){
      case 'sting':{const e=div('');e.id='sting';e.innerHTML='<div class="wash"></div><div class="ring"></div><div class="mark"></div><div class="word"></div><div class="tag serif">'+(c.tag||'The all-in-one AI platform for advocates').replace('AI platform','<i>AI platform</i>')+'</div>';EL.push({c,el:e,q:{ring:e.querySelector('.ring'),mark:e.querySelector('.mark'),word:e.querySelector('.word'),tag:e.querySelector('.tag')}});break;}
      case 'lower_third':{const e=div('lt card','<div class="bar"></div><div class="mk"></div><div class="name serif">'+c.name+'</div><div class="role">'+c.role+'</div>');EL.push({c,el:e});break;}
      case 'pills':{const e=div('pills',c.items.map(i=>'<div class="pill"><div class="dot"></div>'+i.text+'</div>').join(''));EL.push({c,el:e,items:[...e.querySelectorAll('.pill')]});break;}
      case 'lockup':{const e=div('lockup','<div class="in"><div class="mk"></div><div class="wd"></div></div>');EL.push({c,el:e});break;}
      case 'bignum':{const e=div('bignum','<div class="n serif">'+c.num+'</div><div class="rule"></div><div class="l">'+c.label+'</div>');EL.push({c,el:e,q:{n:e.querySelector('.n'),r:e.querySelector('.rule'),l:e.querySelector('.l')}});break;}
      case 'chapter':{const e=div('chapter','<i></i><span>'+c.text+'</span><i></i>');EL.push({c,el:e});break;}
      case 'chips':{const side=c.side||'right';const e=div('chips '+side,c.items.map(chipHTML).join(''));const items=[...e.querySelectorAll('.chip')];if(side!=='row'&&side!=='lowrow')items.forEach((p,k)=>p.style.top=((c.top??400)+k*116)+'px');EL.push({c,el:e,items});break;}
      case 'title':{const e=div('title','<div class="in card"><div class="h serif">'+c.title+'</div>'+(c.sub?'<div class="s">'+c.sub+'</div>':'')+'</div>');EL.push({c,el:e,q:{s:e.querySelector('.s')}});break;}
      case 'captions':{const e=div('caps','');EL.push({c,el:e,phrases:groupWords(c.words,c),cur:-1});break;}
      case 'pricing':{const e=div('pricing','<div class="wash"></div><div class="h serif">Two simple ways to <i>pay</i></div>'
        +'<div class="pcard card" id="payg" style="top:330px"><div class="head"><div class="tile">'+svg('badge-indian-rupee')+'</div><div class="name serif">Pay-as-you-go</div></div>'+c.payg_lines.map(l=>'<div class="line">'+svg('check')+'<span>'+l.text+'</span></div>').join('')+'</div>'
        +'<div class="pcard card" id="pro" style="top:790px"><div class="head"><div class="tile">'+svg('star')+'</div><div class="name serif">Pro</div></div><div class="price"><div class="big serif" id="p1">₹1,500</div><div class="per">/ month</div></div><div class="price" style="margin-top:6px"><div class="big serif" id="p2" style="font-size:72px">₹12,000</div><div class="per">/ year</div><div class="per" id="p3" style="color:var(--accent-deep)">+ GST</div></div>'+c.pro_lines.slice(3).map(l=>'<div class="line">'+svg('check')+'<span>'+l.text+'</span></div>').join('')+'</div>');
        EL.push({c,el:e,q:{h:e.querySelector('.h'),payg:e.querySelector('#payg'),pro:e.querySelector('#pro'),paygLines:[...e.querySelectorAll('#payg .line')],p1:e.querySelector('#p1'),p2:e.querySelector('#p2'),p3:e.querySelector('#p3'),proLines:[...e.querySelectorAll('#pro .line')]}});break;}
      case 'cta':{const e=div('cta','<div class="wash"></div><div class="card"><div class="tile" style="margin:0 auto 14px;width:76px;height:76px;border-radius:20px">'+svg('gift').replace('<svg','<svg style="width:40px;height:40px"')+'</div><div class="amt serif">₹200</div><div class="what serif">free AI credits</div><div class="who">for every new user</div></div><div class="link">Click the link below to start</div><div class="arrow">'+svg('arrow-down')+'</div><div class="lk"><div class="in"><div class="mk"></div><div class="wd"></div></div></div><div class="url">'+(c.url||'lawworld.ai')+'</div>');
        EL.push({c,el:e,q:{card:e.querySelector('.card'),link:e.querySelector('.link'),arrow:e.querySelector('.arrow'),lk:e.querySelector('.lk'),url:e.querySelector('.url')}});break;}
    }
  }
  return EL.length;
}
function groupWords(words,c){
  const maxW=c.max_words||4, maxD=c.max_dur||1.7; const out=[]; let cur=null;
  for(const w of words){const txt=(w.word||'').trim(); if(!txt) continue; const endsSent=/[.!?]$/.test(txt);
    if(!cur||cur.words.length>=maxW||(w.end-cur.start)>maxD){cur={start:w.start,end:w.end,words:[]};out.push(cur);}
    cur.words.push({t:txt,s:w.start,e:w.end}); cur.end=w.end; if(endsSent) cur=null;}
  for(let i=0;i<out.length-1;i++){const gap=out[i+1].start-out[i].end; out[i].hold=gap<0.6?out[i+1].start:out[i].end+0.35;}
  if(out.length) out[out.length-1].hold=out[out.length-1].end+0.6; return out;
}
const show=(el,on)=>{el.style.visibility=on?'visible':'hidden';};
const rise=(el,a,px=40)=>{el.style.opacity=String(clamp(a*1.6));el.style.transform=`translateY(${(1-outExpo(a))*px}px)`;};
function seek(t){
  let active=false;
  for(const x of EL){
    if(x.type==='_scrim'){const on=t>=x.t0&&t<=x.t1;show(x.el,on);x.el.style.opacity=on?String(P(t,x.t0,0.4)):'0';if(on)active=true;continue;}
    const c=x.c,el=x.el; const on=t>=c.t0&&t<=c.t1; show(el,on); if(!on) continue; active=true;
    const fo=c.fade_out??0.35; const outA=clamp((c.t1-t)/fo);
    switch(c.type){
      case 'sting':{const a=P(t,c.t0,0.7),b=P(t,c.t0+0.45,0.7),g=P(t,c.t0+1.05,0.6);
        x.q.mark.style.transform=`scale(${0.6+0.4*outBack(a)}) rotate(${-8*(1-outCubic(a))}deg)`;x.q.mark.style.opacity=String(clamp(a*2));
        x.q.ring.style.transform=`scale(${0.7+1.9*outExpo(P(t,c.t0+0.25,1.3))})`;x.q.ring.style.opacity=String(0.7*(1-P(t,c.t0+0.25,1.3)));
        x.q.word.style.opacity=String(outCubic(b));x.q.word.style.transform=`translateY(${26*(1-outExpo(b))}px)`;x.q.word.style.filter=`blur(${10*(1-outExpo(b))}px)`;
        x.q.tag.style.opacity=String(outCubic(g));x.q.tag.style.transform=`translateY(${16*(1-outExpo(g))}px)`;el.style.opacity=String(outA);break;}
      case 'lower_third':{const a=outExpo(P(t,c.t0,0.55));el.style.opacity=String(Math.min(a,outA));el.style.transform=`translateY(${(1-a)*46+(1-outA)*30}px)`;break;}
      case 'pills':{el.style.opacity=String(outA);x.items.forEach((p,k)=>{const a=P(t,c.items[k].at??c.t0,0.45);p.style.opacity=String(clamp(a*2));p.style.transform=`scale(${0.7+0.3*outBack(a)}) translateY(${(1-outExpo(a))*14}px)`;});break;}
      case 'lockup':{const a=outExpo(P(t,c.t0,0.6));el.style.opacity=String(Math.min(clamp(a*1.5),outA));el.style.transform=`translateY(${(1-a)*-34}px)`;break;}
      case 'bignum':{const a=P(t,c.t0,0.9);const n=parseInt(c.num)||0;const plus=c.num.replace(/^\d+/,'');x.q.n.textContent=(a<1?Math.round(n*outCubic(a)):n)+(a>=0.85?plus:'');
        x.q.n.style.transform=`translateY(${(1-outExpo(P(t,c.t0,0.8)))*40-(t-c.t0)*1.2}px) scale(${0.92+0.08*outExpo(P(t,c.t0,0.8))})`;x.q.n.style.opacity=String(clamp(a*3));
        const r=P(t,c.t0+0.5,0.5);x.q.r.style.transform=`scaleX(${outExpo(r)})`;x.q.r.style.opacity=String(r);const l=P(t,c.t0+0.7,0.6);x.q.l.style.opacity=String(outCubic(l));x.q.l.style.transform=`translateY(${(1-outExpo(l))*18}px)`;el.style.opacity=String(outA);break;}
      case 'chapter':{const a=outExpo(P(t,c.t0,0.5));el.style.opacity=String(Math.min(a,outA));el.style.transform=`translateY(${(1-a)*-14}px)`;break;}
      case 'chips':{el.style.opacity=String(outA);const row=['row','lowrow'].includes(c.side||'right');x.items.forEach((p,k)=>{const a=P(t,c.items[k].at??c.t0,0.5);p.style.opacity=String(clamp(a*2));p.style.transform=row?`translateY(${(1-outExpo(a))*40}px) scale(${0.94+0.06*outBack(a)})`:`translateX(${(1-outExpo(a))*70}px) scale(${0.94+0.06*outBack(a)})`;});break;}
      case 'title':{const a=outExpo(P(t,c.t0,0.55));el.style.opacity=String(Math.min(clamp(a*1.4),outA));el.style.transform=`translateY(${(1-a)*-24}px)`;if(x.q.s){const s=P(t,c.sub_at??(c.t0+0.8),0.5);x.q.s.style.opacity=String(outCubic(s));x.q.s.style.transform=`translateY(${(1-outExpo(s))*10}px)`;}break;}
      case 'captions':{const ph=x.phrases.find(p=>t>=p.start-0.12&&t<=p.hold);if(!ph){el.style.opacity='0';break;}const idx=x.phrases.indexOf(ph);
        if(x.cur!==idx){el.innerHTML='<div class="box">'+ph.words.map(w=>'<span>'+w.t+'</span>').join('')+'</div>';x.cur=idx;x.spans=[...el.querySelectorAll('span')];}
        const a=outExpo(P(t,ph.start-0.12,0.22));el.style.opacity=String(a);el.style.transform=`translateY(${(1-a)*14}px)`;
        x.spans.forEach((s,k)=>{const w=ph.words[k];const on=t>=w.s-0.02&&t<w.e+0.05;const done=t>=w.e+0.05;s.className=on?'on':(done?'done':'');const pop=on?1+0.05*Math.sin(Math.PI*clamp((t-w.s)/Math.max(0.18,w.e-w.s))):1;s.style.transform=`scale(${pop})`;});break;}
      case 'pricing':{el.style.opacity=String(Math.min(P(t,c.t0,0.35),outA));rise(x.q.h,P(t,c.heading_at??c.t0,0.6),30);rise(x.q.payg,P(t,c.payg_at,0.6),50);
        x.q.paygLines.forEach((l,k)=>rise(l,P(t,c.payg_lines[k].at,0.45),18));rise(x.q.pro,P(t,c.pro_at,0.6),50);
        rise(x.q.p1,P(t,c.pro_lines[0].at,0.5),20);rise(x.q.p2,P(t,c.pro_lines[1].at,0.5),20);rise(x.q.p3,P(t,c.pro_lines[2].at,0.4),10);
        x.q.proLines.forEach((l,k)=>rise(l,P(t,(c.pro_lines[k+3]||{}).at??c.t1,0.45),18));break;}
      case 'cta':{el.style.opacity=String(Math.min(P(t,c.t0,0.4),outA));rise(x.q.card,P(t,c.credit_at,0.7),60);rise(x.q.link,P(t,c.link_at,0.5),24);
        const la=P(t,c.link_at+0.2,0.5);x.q.arrow.style.opacity=String(la);x.q.arrow.style.transform=`translateY(${10*Math.sin((t-c.link_at)*4)}px)`;
        rise(x.q.lk,P(t,c.logo_at,0.7),30);rise(x.q.url,P(t,c.logo_at+0.4,0.6),14);break;}
    }
  }
  return active;
}
window.__init=init;window.__seek=seek;
</script></body></html>
'''
out = os.path.join(P, "overlays", "overlay_brand.html")
open(out, "w").write(html.replace("__ICONS__", json.dumps(icons)))
print("wrote", out, os.path.getsize(out), "bytes")
