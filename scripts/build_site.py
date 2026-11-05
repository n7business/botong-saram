#!/usr/bin/env python3
"""⑥ 아카이브 브라우저 페이지. archive + sources → site/botong-preview.html (역삼836 「보통사람」 메뉴 페이지).
구조: 영역 탭 → 이 영역의 사람들(소스) → 그 사람들이 계속 말하는 것(claim, 인용·링크·상태)."""
import json, base64, html, re
from common import *

TYPE_KO = {"threads": "Threads", "instagram": "인스타그램", "youtube": "유튜브", "blog": "블로그", "newsletter": "뉴스레터", "official": "공식", "book": "책·연구", "x": "X"}
STATUS_KO = {"verified": "검증됨", "candidate": "후보", "hypothesis": "검증 중", "stale": "주의", "deprecated": "하지 말 것"}

def esc(s): return html.escape(str(s if s is not None else ""))

def main():
    doms = domains(); srcs = sources(); idx = source_index(); cs = claims()
    logo = base64.b64encode((ROOT / "site/assets/logo.png").read_bytes()).decode()
    people = {}  # (dom, source name) → dict
    for dom, lst in srcs.items():
        for s in lst or []:
            if s.get("unverified") or s.get("license_unverified"): continue
            people[(dom, s["name"])] = {"dom": dom, "name": s["name"], "type": s.get("type"), "url": s.get("url"), "author": s.get("author"), "followers": s.get("followers"), "why": s.get("why", ""), "license": bool(s.get("license")), "weight": s.get("weight"), "claims": 0, "verified": 0, "last": None}
    items = []
    for c in cs:
        if c["status"] in ("merged", "expired"): continue
        srclist = []
        for s in c.get("sources", []):
            m = src_lookup(s, idx); pname = m["name"] if m else (s.get("author") or norm_url(s["url"]).split("/")[0])
            srclist.append({"url": s["url"], "author": s.get("author"), "seen": s.get("seen"), "quote": s.get("quote", ""), "person": pname})
            key = (c["domain"], pname)
            if key in people:
                people[key]["claims"] += 1; people[key]["verified"] += c["status"] == "verified"
                if not people[key]["last"] or (s.get("seen") or "") > people[key]["last"]: people[key]["last"] = s.get("seen")
        items.append({"id": c["id"], "dom": c["domain"], "claim": c["claim"], "body": c.get("_body", ""), "status": c["status"], "evidence": c["evidence"], "conf": c.get("confidence", 0),
                      "sources": srclist, "mentions": len(srclist), "first": c.get("first_seen"), "last": c.get("last_confirmed"), "review": c.get("review_by"),
                      "law": (c.get("law_ref") or {}).get("law"), "article": (c.get("law_ref") or {}).get("article"), "by": c.get("verified_by"), "tags": c.get("tags", [])})
    order = {"verified": 0, "hypothesis": 1, "candidate": 2, "stale": 3, "deprecated": 4}
    items.sort(key=lambda x: (order.get(x["status"], 9), -x["mentions"], -x["conf"]))
    data = {"built": TODAY, "domains": [{"key": k, "ko": v["ko"], "legal": bool(v.get("legal")), "total": sum(i["dom"] == k for i in items), "verified": sum(i["dom"] == k and i["status"] == "verified" for i in items), "people": sum(p["dom"] == k for p in people.values())} for k, v in doms.items()],
            "people": sorted(people.values(), key=lambda p: (-p["claims"], p["name"])), "items": items, "type_ko": TYPE_KO, "status_ko": STATUS_KO,
            "sources_total": sum(len(l or []) for l in srcs.values())}
    tot = len(items); ver = sum(i["status"] == "verified" for i in items)
    page = TEMPLATE.replace("{{LOGO}}", logo).replace("{{DATA}}", json.dumps(data, ensure_ascii=False).replace("</", "<\\/")).replace("{{VER}}", str(ver)).replace("{{TOT}}", str(tot)).replace("{{SRC}}", str(data["sources_total"])).replace("{{PEOPLE}}", str(len(people))).replace("{{BUILT}}", TODAY)
    out = ROOT / "site/botong-preview.html"; out.write_text(page, encoding="utf-8")
    log(f"site 빌드 {out} items={tot} verified={ver} people={len(people)}")

TEMPLATE = r'''<title>역삼836 보통사람</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700&display=swap">
<style>
/* 역삼836 실제 스타일(white · #111 · Noto Sans KR · 타이트 자간) · 「보통사람」 아카이브 브라우저 */
:root{--bg:#fff;--fg:#111;--muted:#777;--line:#e6e6e6;--soft:#f5f5f3;--pill:#111;--pill-fg:#fff;--ok:#1a7f4b;--warn:#b7791f;--bad:#b42318;--invert:0}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--bg:#111;--fg:#f2f2f2;--muted:#9a9a9a;--line:#2a2a2a;--soft:#1a1a1a;--pill:#f2f2f2;--pill-fg:#111;--ok:#5ad08c;--warn:#e2b155;--bad:#f08a80;--invert:1;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#111;--fg:#f2f2f2;--muted:#9a9a9a;--line:#2a2a2a;--soft:#1a1a1a;--pill:#f2f2f2;--pill-fg:#111;--ok:#5ad08c;--warn:#e2b155;--bad:#f08a80;--invert:1;color-scheme:dark}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font-family:'Noto Sans KR','Apple SD Gothic Neo','Malgun Gothic',sans-serif;letter-spacing:-.045em;word-break:keep-all;line-height:1.6}
body::before{content:"";position:fixed;inset:0 0 auto;height:env(safe-area-inset-top,0px);z-index:10;background:var(--bg)}
a{color:inherit}
header{position:sticky;top:env(safe-area-inset-top,0px);z-index:20;height:90px;display:flex;align-items:center;justify-content:space-between;padding-block:0;padding-left:max(4vw,env(safe-area-inset-left,0px));padding-right:max(4vw,env(safe-area-inset-right,0px));background:color-mix(in srgb,var(--bg) 93%,transparent);backdrop-filter:blur(16px);border-bottom:1px solid var(--line)}
.logo{display:block;width:151px;height:37px;position:relative;overflow:hidden}
.logo img{width:174px;height:174px;max-width:none;position:absolute;left:-11px;top:-72px;filter:invert(var(--invert))}
header nav{display:flex;align-items:center;gap:32px;font-size:12px}
header nav a{text-decoration:none;opacity:.75}
header nav a.active{opacity:1;font-weight:700;border-bottom:2px solid var(--fg);padding-bottom:2px}
.wrap{padding-left:max(7.5vw,env(safe-area-inset-left,0px));padding-right:max(7.5vw,env(safe-area-inset-right,0px))}
.section{padding-block:70px}
.section+.section{border-top:1px solid var(--line)}
.eyebrow{font-size:11px;font-weight:400;letter-spacing:0;margin:0 0 20px;color:var(--muted)}
h1{font-size:clamp(36px,4.6vw,66px);font-weight:500;line-height:1.2;letter-spacing:-.07em;margin:0;text-wrap:balance}
h2{font-size:clamp(24px,3vw,40px);font-weight:500;line-height:1.3;letter-spacing:-.065em;margin:0;text-wrap:balance}
h3{font-size:16px;font-weight:500;line-height:1.5;letter-spacing:-.05em;margin:0 0 8px}
.lead{font-size:14px;line-height:1.9;color:var(--muted);max-width:36em;margin:24px 0 0}
.install{margin-top:28px;background:var(--soft);border:1px solid var(--line);padding:16px 20px;display:flex;flex-wrap:wrap;gap:12px 20px;align-items:center;max-width:760px}
.install pre{margin:0;font:12px/1.7 ui-monospace,SFMono-Regular,Menlo,monospace;letter-spacing:0;white-space:pre;overflow-x:auto;min-width:0;flex:1 1 320px}
.copy{font:inherit;font-size:11px;letter-spacing:0;background:none;border:1px solid var(--fg);color:var(--fg);padding:8px 14px;cursor:pointer}
.copy[data-done="1"]{background:var(--fg);color:var(--bg)}
.stats{display:flex;flex-wrap:wrap;gap:24px;margin-top:30px;font-size:11px;color:var(--muted);letter-spacing:0}
.stats b{display:block;font-size:26px;color:var(--fg);font-weight:500;letter-spacing:-.05em;font-variant-numeric:tabular-nums;line-height:1.1}
.tabs{display:flex;gap:6px;overflow-x:auto;padding:4px 0 10px;margin:0;list-style:none;scrollbar-width:none;position:sticky;top:calc(90px + env(safe-area-inset-top,0px));background:var(--bg);z-index:5}
.tabs::-webkit-scrollbar{display:none}
.tab{flex:0 0 auto;font:inherit;font-size:12px;letter-spacing:-.03em;border:1px solid var(--line);background:var(--bg);color:var(--fg);padding:9px 14px;cursor:pointer;white-space:nowrap;display:flex;gap:8px;align-items:center}
.tab b{font-weight:500;font-variant-numeric:tabular-nums;color:var(--muted)}
.tab[aria-selected="true"]{background:var(--fg);color:var(--bg)}
.tab[aria-selected="true"] b{color:var(--bg);opacity:.7}
.sub{display:flex;flex-wrap:wrap;gap:8px 16px;align-items:center;margin:26px 0 0;font-size:11px;color:var(--muted);letter-spacing:0}
.sub button{font:inherit;font-size:11px;letter-spacing:0;background:none;border:0;color:var(--muted);padding:0;cursor:pointer;border-bottom:1px solid transparent}
.sub button[aria-pressed="true"]{color:var(--fg);border-bottom-color:var(--fg)}
.people{list-style:none;padding:0;margin:26px 0 0;display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:1px;background:var(--line);border:1px solid var(--line)}
.person{background:var(--bg);padding:18px 18px 16px;min-width:0;display:grid;gap:6px;align-content:start;text-decoration:none}
.person .k{font-size:10px;color:var(--muted);letter-spacing:0;display:flex;gap:8px;flex-wrap:wrap}
.person .k i{font-style:normal;border:1px solid var(--line);padding:0 5px}
.person .n{font-size:14px;font-weight:500;letter-spacing:-.04em;line-height:1.4}
.person .w{font-size:11px;color:var(--muted);letter-spacing:-.02em;line-height:1.6;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.person .c{font-size:11px;color:var(--muted);letter-spacing:0;font-variant-numeric:tabular-nums}
.person .c b{color:var(--fg);font-weight:500}
.items{display:grid;gap:0;margin-top:26px;border-top:1px solid var(--line)}
.item{min-width:0;border-bottom:1px solid var(--line);padding:22px 0}
.item .top{display:flex;gap:10px;flex-wrap:wrap;align-items:center;font-size:10px;letter-spacing:0;color:var(--muted);margin-bottom:10px}
.chip{border:1px solid var(--line);padding:1px 7px;font-size:10px}
.chip.verified{border-color:var(--ok);color:var(--ok)}
.chip.candidate{border-color:var(--line)}
.chip.stale{border-color:var(--warn);color:var(--warn)}
.chip.deprecated{border-color:var(--bad);color:var(--bad)}
.item h3{font-size:16px}
.item .body{font-size:13px;line-height:1.9;color:var(--muted);margin:0 0 12px;max-width:62em}
.item .q{font-size:12px;line-height:1.8;margin:0 0 6px;padding-left:12px;border-left:2px solid var(--line);color:var(--fg);max-width:60em}
.item .src{font-size:11px;color:var(--muted);letter-spacing:0;margin:0}
.item .src a{color:var(--fg);text-decoration:underline;text-underline-offset:3px;word-break:break-all}
.empty{padding:40px 0;color:var(--muted);font-size:13px}
.more{margin-top:20px}
.pill{display:inline-flex;align-items:center;gap:30px;font-size:12px;background:var(--pill);color:var(--pill-fg);padding:14px 20px;text-decoration:none;border:0;font-family:inherit;cursor:pointer}
.note{font-size:11px;color:var(--muted);letter-spacing:0;margin:14px 0 0;max-width:60em}
footer{background:#111;color:#fff;padding-block:55px 30px;padding-left:max(7.5vw,env(safe-area-inset-left,0px));padding-right:max(7.5vw,env(safe-area-inset-right,0px))}
footer .logo img{filter:invert(1)}
.footer-top{display:flex;align-items:center;justify-content:space-between;margin-bottom:40px;gap:20px;flex-wrap:wrap}
.footer-top p{font-size:12px;color:#888;margin:0}
.footer-bottom{display:flex;align-items:flex-end;justify-content:space-between;font-size:9px;letter-spacing:0;line-height:1.8;color:#888;gap:20px;flex-wrap:wrap}
.footer-bottom p{margin:0}
.preview-tag{position:fixed;left:0;right:0;bottom:0;z-index:30;background:#d8ff4a;color:#111;font-size:11px;letter-spacing:0;text-align:center;padding:8px max(16px,env(safe-area-inset-left,0px)) calc(8px + env(safe-area-inset-bottom,0px))}
@media (max-width:700px){header{height:72px;padding-left:max(22px,env(safe-area-inset-left,0px));padding-right:max(22px,env(safe-area-inset-right,0px))}.logo{width:125px;height:31px}.logo img{width:144px;height:144px;left:-9px;top:-60px}header nav{gap:14px;font-size:11px}.wrap{padding-left:max(7%,env(safe-area-inset-left,0px));padding-right:max(7%,env(safe-area-inset-right,0px))}.section{padding-block:48px}.tabs{top:calc(72px + env(safe-area-inset-top,0px))}body{padding-bottom:34px}}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}
:focus-visible{outline:2px solid var(--fg);outline-offset:3px}
</style>

<header>
  <a class="brand" href="https://yeoksam836.com" aria-label="역삼836 홈"><span class="logo"><img src="data:image/png;base64,{{LOGO}}" alt="역삼836"></span></a>
  <nav aria-label="메인 메뉴"><a href="https://yeoksam836.com/#office">공간</a><a href="https://yeoksam836.com/#programs">프로그램</a><a class="active" href="#top" aria-current="page">보통사람</a><a href="https://yeoksam836.com/#visit">방문 문의 ↗</a></nav>
</header>

<main id="top">
<section class="section wrap">
  <p class="eyebrow">보통사람 · 업계 노하우 아카이브</p>
  <h1>요즘 보통사람이라면<br>이 정도는 알아요.</h1>
  <p class="lead">각 업계에서 노하우를 올리는 사람들이 SNS에서 계속 말하는 것을 매일 모아 사람 단위로 쌓습니다. 누가, 무엇을, 몇 번 말했는지와 원문 링크가 그대로 남습니다. 같은 내용이 Claude Code 플러그인으로도 나갑니다.</p>
  <div class="install"><pre id="cmd">claude plugin marketplace add n7business/botong-saram
claude plugin install botong-saram@botong-saram</pre><button class="copy" id="copy-btn" type="button">복사</button></div>
  <p class="lead" style="font-size:14px;margin-top:10px">설치 뒤 Claude Code에서 <code>/plugin</code> → Marketplaces → botong-saram → <b>Enable auto-update</b>를 한 번 켜 두면 매일 새로 쌓인 내용이 자동으로 들어옵니다. Codex는 <code>codex plugin marketplace add n7business/botong-saram</code>. 모든 항목에 공식 발표인지, 몇 명이 말했는지, 한 사람의 말인지가 표시됩니다.</p>
  <div class="stats"><div><b>{{PEOPLE}}</b>추적 중인 사람·기관</div><div><b>{{TOT}}</b>모은 주장</div><div><b>{{VER}}</b>검증됨</div><div><b>{{BUILT}}</b>마지막 갱신</div></div>
</section>

<section class="section wrap" id="archive">
  <ul class="tabs" id="tabs" role="tablist"></ul>
  <div class="sub"><span>보기</span><button type="button" data-f="all" aria-pressed="true">전체</button><button type="button" data-f="verified" aria-pressed="false">검증됨만</button><span id="legal-note" hidden>· 이 영역은 자격이 확인된 사람과 공식 기관만</span></div>
  <h2 style="margin-top:34px">이 영역의 사람들</h2>
  <ul class="people" id="people"></ul>
  <h2 style="margin-top:50px">계속 말하는 것</h2>
  <div class="items" id="items"></div>
  <div class="more" id="more"></div>
  <p class="note">검증됨 = 공식 근거, 독립 출처 2곳 교차, 또는 수치를 제시한 실무자 실측 중 하나를 통과. 후보 = 한 사람이 한 번 말한 것. 같은 말이 다시 나오면 언급 횟수가 올라갑니다. 법·노무·세무·인허가는 조문 근거가 붙어야 검증으로 올라갑니다.</p>
</section>

<section class="section wrap">
  <p class="eyebrow">능력자를 찾습니다</p>
  <h2>각 영역에서 보통 사람에게 주기적으로<br>지식을 업데이트해 주실 분.</h2>
  <p class="lead">당신이 쓰고, 우리가 검증해 배포합니다. 항목마다 이름과 링크가 붙어 플러그인을 쓰는 모든 사람의 AI가 당신을 인용합니다. 기준은 정확한 팩트와 뛰어난 인사이트, 둘 다입니다.</p>
  <p class="more"><a class="pill" href="https://yeoksam836.com/#visit" target="_blank" rel="noopener"><span>기고 문의</span><span>↗</span></a></p>
  <p class="lead" id="takedown" style="font-size:13px;margin-top:28px;color:var(--muted,#666)"><b>원작자 삭제 요청</b> — 내 글이나 계정이 실려 있는데 빼고 싶으시면 계정 주소만 <a href="mailto:founder@yeoksam836.com?subject=%EB%B3%B4%ED%86%B5%EC%82%AC%EB%9E%8C%20%EC%82%AD%EC%A0%9C%20%EC%9A%94%EC%B2%AD">founder@yeoksam836.com</a> 또는 <a href="https://github.com/n7business/botong-saram/issues/new?template=takedown.md" target="_blank" rel="noopener">GitHub 이슈</a>로 알려 주세요. 확인 후 바로 수집에서 빼고 관련 항목을 모두 지웁니다. 원문은 출처 링크와 함께 짧게만 인용하며, 인용된 원문의 권리는 원작자에게 있습니다.</p>
</section>
</main>

<footer>
  <div class="footer-top"><span class="logo"><img src="data:image/png;base64,{{LOGO}}" alt="역삼836"></span><p>일감이 돌고, 사업이 태어나는 곳.</p></div>
  <div class="footer-bottom"><p>네스토리움 주식회사 · 대표 김수빈 · 운영 디렉터 강민서<br>사업자등록번호 174-86-03563</p><p>© 2026 역삼836</p></div>
</footer>
<div class="preview-tag">미리보기 · yeoksam836.com 상단 「보통사람」 메뉴 시안 · 배포 전</div>

<script id="data" type="application/json">{{DATA}}</script>
<script>
(function(){
  var D=JSON.parse(document.getElementById('data').textContent);
  var cur=D.domains[0].key, filt='all', LIMIT=20, shown=LIMIT;
  function esc(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];});}
  var tabs=document.getElementById('tabs');
  D.domains.forEach(function(d){var li=document.createElement('li');li.innerHTML='<button class="tab" role="tab" type="button" data-k="'+d.key+'">'+esc(d.ko)+' <b>'+d.verified+'/'+d.total+'</b></button>';tabs.appendChild(li);});
  tabs.addEventListener('click',function(e){var b=e.target.closest('.tab');if(!b)return;cur=b.dataset.k;shown=LIMIT;render();});
  document.querySelectorAll('.sub button').forEach(function(b){b.addEventListener('click',function(){filt=b.dataset.f;shown=LIMIT;render();});});
  function render(){
    document.querySelectorAll('.tab').forEach(function(b){b.setAttribute('aria-selected',b.dataset.k===cur?'true':'false');});
    document.querySelectorAll('.sub button').forEach(function(b){b.setAttribute('aria-pressed',b.dataset.f===filt?'true':'false');});
    var dom=D.domains.filter(function(d){return d.key===cur;})[0];
    document.getElementById('legal-note').hidden=!dom.legal;
    var ppl=D.people.filter(function(p){return p.dom===cur;});
    document.getElementById('people').innerHTML=ppl.length?ppl.map(function(p){return '<a class="person" href="'+esc(p.url)+'" target="_blank" rel="noopener"><span class="k"><i>'+esc(D.type_ko[p.type]||p.type)+'</i>'+(p.followers?'<span>팔로워 '+esc(p.followers)+'</span>':'')+(p.license&&p.type!=='official'?'<span>자격 확인</span>':'')+'</span><span class="n">'+esc(p.name)+'</span><span class="w">'+esc(p.why)+'</span><span class="c"><b>'+p.claims+'</b> 주장 · '+p.verified+' 검증'+(p.last?' · 최근 '+esc(p.last):'')+'</span></a>';}).join(''):'<li class="empty">아직 추적 중인 사람이 없습니다.</li>';
    var its=D.items.filter(function(i){return i.dom===cur&&(filt==='all'||i.status==='verified');});
    var box=document.getElementById('items');
    box.innerHTML=its.length?its.slice(0,shown).map(function(i){
      var s0=i.sources[0]||{};
      return '<article class="item"><div class="top"><span class="chip '+esc(i.status)+'">'+esc(D.status_ko[i.status]||i.status)+'</span>'+(i.mentions>1?'<span class="chip">'+i.mentions+'회 언급</span>':'')+(i.law?'<span>'+esc(i.law)+' '+esc(i.article||'')+'</span>':'')+(i.by&&i.by.indexOf('실측')>-1?'<span>'+esc(i.by)+'</span>':'')+'<span>'+esc(i.last)+' 확인'+(i.review?' · 재검토 '+esc(i.review):'')+'</span></div><h3>'+esc(i.claim)+'</h3><p class="body">'+esc(i.body)+'</p>'+(s0.quote?'<p class="q">“'+esc(s0.quote)+'”</p>':'')+'<p class="src">'+i.sources.map(function(s){return esc(s.person||s.author)+' <a href="'+esc(s.url)+'" target="_blank" rel="noopener">원문</a>';}).join(' · ')+'</p></article>';
    }).join(''):'<p class="empty">이 조건에 맞는 주장이 아직 없습니다. 매일 06:30 수집이 쌓이면 채워집니다.</p>';
    var more=document.getElementById('more'); more.innerHTML= its.length>shown ? '<button class="pill" type="button" id="more-btn"><span>'+(its.length-shown)+'개 더 보기</span><span>↓</span></button>' : '';
    var mb=document.getElementById('more-btn'); if(mb) mb.addEventListener('click',function(){shown+=LIMIT;render();});
  }
  render();
  var b=document.getElementById('copy-btn'), t=document.getElementById('cmd');
  b.addEventListener('click',function(){var txt=t.textContent;function done(){b.dataset.done='1';b.textContent='복사됨';setTimeout(function(){b.dataset.done='';b.textContent='복사';},1800);}function fb(){var r=document.createRange();r.selectNodeContents(t);var s=window.getSelection();s.removeAllRanges();s.addRange(r);b.textContent='선택됨 · 길게 눌러 복사';}
    if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(txt).then(done,fb);}else{fb();}});
})();
</script>
'''
if __name__ == "__main__": main()
