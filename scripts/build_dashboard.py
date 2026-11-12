#!/usr/bin/env python3
"""⑦ 플러그인 현황판. archive + changelog → site/dashboard.html
- 플러그인 지도: 영역(스킬)마다 SKILL.md / all.md / people.md 에 무엇이 몇 건 실렸나 (build_plugin.layout과 같은 기준)
- 새로 들어온 것: 처음 수집일 기준 오늘·7일·30일 + 변경 기록(승격·재언급·병합·마감 빠짐·주의)
사용: build_dashboard.py  (build_plugin.py 다음에 실행)"""
import json
from common import *
from build_plugin import layout, SKILL_CAP, removed_guard, REPO

GRADE_KO = {"dep": "⛔ 하지 말 것", "off": "🏛 공식·연구", "multi": "👥 여러 명", "single": "👤 한 사람", "hyp": "🧪 실험 중", "stale": "⚠️ 다시 확인"}
KIND_KO = {"candidate": "새로 들어옴", "verified": "수치·교차 확인", "reconfirmed": "다시 언급됨", "merged": "같은 말로 합쳐짐", "expired": "마감 지나 빠짐", "stale": "다시 확인 필요", "deprecated": "하지 말 것으로 바뀜", "hypothesis": "실험 시작"}

def main():
    doms = domains(); idx = source_index(); allc = claims(); byid = {c["id"]: c for c in allc}
    items, dstat = [], []
    for dom, d in doms.items():
        cs = [c for c in allc if c["domain"] == dom and c["status"] not in ("merged", "expired")]
        if not cs: continue
        groups = layout(cs, idx); n = {k: len(v) for k, v in groups.items()}; inskill = 0
        for k, xs in groups.items():
            for i, (c, g, ppl) in enumerate(xs):
                loc = "people" if k == "single" else ("skill" if i < SKILL_CAP[k] else "all")
                inskill += loc == "skill"
                items.append([c["id"], dom, k, c["claim"], ppl[:3], len(ppl), str(c.get("first_seen") or ""), str(c.get("last_confirmed") or ""), loc, c["status"] == "verified"])
        base = PLUGIN / "skills" / dom
        size = {f: (base / f"{f}.md").stat().st_size if (base / f"{f}.md").exists() else 0 for f in ("SKILL", "all", "people")}
        dstat.append({"key": dom, "ko": d["ko"], "legal": bool(d.get("legal")), "n": n, "total": len(cs), "inskill": inskill, "size": size})
    events, gone = [], {}
    for p in sorted(CHANGELOG.glob("*.json"))[-30:]:
        for e in json.loads(p.read_text(encoding="utf-8")):
            events.append([p.stem, e["kind"], e["id"], e.get("note") or ""])
            c = byid.get(e["id"])
            if c and c["status"] in ("merged", "expired") and e["kind"] in ("expired", "merged"): gone[e["id"]] = c["claim"]
    people = sum(1 for lst in sources().values() for s in (lst or []) if not s.get("unverified"))
    data = {"built": TODAY, "repo": REPO, "grades": GRADE_KO, "kinds": KIND_KO, "domains": dstat, "items": items, "events": events, "gone": gone, "people": people}
    page = TEMPLATE.replace("{{DATA}}", json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")).replace("{{BUILT}}", TODAY).replace("{{REPO}}", REPO)
    out = ROOT / "site/dashboard.html"; out.write_text(page, encoding="utf-8")
    log(f"dashboard 빌드 {out} items={len(items)} events={len(events)} {out.stat().st_size // 1024}KB")

TEMPLATE = r'''<title>보통사람 플러그인 현황</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
/* 역삼836 톤(흰 바탕·먹색·Noto Sans KR). 위→아래: 요약 숫자 → 일별 신규 → 플러그인 지도(영역×파일) → 항목 탐색 → 변경 기록 */
:root{
  --bg:#fff;--fg:#111;--muted:#6f6f6b;--faint:#a3a39e;--line:#e7e7e3;--soft:#f6f6f3;--hi:#fff7d6;
  --g-dep:#e34948;--g-off:#2a78d6;--g-multi:#1baf7a;--g-single:#6250d6;--g-hyp:#e87ba4;--g-stale:#eda100;
  --bar:#111;--bar-dim:#d6d6d1;
  --sans:'Noto Sans KR','Apple SD Gothic Neo','Malgun Gothic',sans-serif;--mono:'IBM Plex Mono',ui-monospace,Menlo,monospace}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--bg:#121212;--fg:#efefec;--muted:#a2a29c;--faint:#6e6e69;--line:#2a2a28;--soft:#1b1b1a;--hi:#3a3216;
  --g-dep:#e66767;--g-off:#3987e5;--g-multi:#199e70;--g-single:#9085e9;--g-hyp:#d55181;--g-stale:#c98500;--bar:#efefec;--bar-dim:#3a3a37;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#121212;--fg:#efefec;--muted:#a2a29c;--faint:#6e6e69;--line:#2a2a28;--soft:#1b1b1a;--hi:#3a3216;
  --g-dep:#e66767;--g-off:#3987e5;--g-multi:#199e70;--g-single:#9085e9;--g-hyp:#d55181;--g-stale:#c98500;--bar:#efefec;--bar-dim:#3a3a37;color-scheme:dark}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font-family:var(--sans);letter-spacing:-.03em;word-break:keep-all;line-height:1.6;font-size:14px}
body::before{content:"";position:fixed;inset:0 0 auto;height:env(safe-area-inset-top,0px);z-index:10;background:var(--bg)}
a{color:inherit}
.wrap{max-width:1180px;margin:0 auto;padding-block:0 80px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}
header{padding-block:40px 28px;border-bottom:1px solid var(--line);display:flex;flex-wrap:wrap;gap:12px 24px;align-items:flex-end;justify-content:space-between}
header h1{margin:0;font-size:clamp(26px,3.4vw,40px);font-weight:500;letter-spacing:-.06em;line-height:1.2;text-wrap:balance}
header p{margin:6px 0 0;color:var(--muted);font-size:13px}
.mono{font-family:var(--mono);letter-spacing:0;font-variant-numeric:tabular-nums}
section{padding-block:36px 8px}
h2{font-size:18px;font-weight:500;letter-spacing:-.04em;margin:0 0 4px;text-wrap:balance}
.sub{color:var(--muted);font-size:12.5px;margin:0 0 18px}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:1px;background:var(--line);border:1px solid var(--line);margin-top:28px}
.stat{background:var(--bg);padding:16px 18px;display:flex;flex-direction:column;gap:2px;min-width:0}
.stat span{font-size:12px;color:var(--muted)}
.stat b{font-family:var(--mono);font-weight:500;font-size:26px;letter-spacing:-.02em;font-variant-numeric:tabular-nums;line-height:1.2}
.stat small{font-size:11.5px;color:var(--faint)}
.chart{position:relative;border:1px solid var(--line);padding:16px 12px 8px}
.chart svg{display:block;width:100%;height:auto;overflow:visible}
.chart text{fill:var(--muted);font-family:var(--mono);font-size:10px}
.tip{position:fixed;pointer-events:none;background:var(--fg);color:var(--bg);font-size:12px;padding:6px 9px;z-index:30;max-width:260px;line-height:1.45}
.legend{display:flex;flex-wrap:wrap;gap:6px 16px;font-size:12px;color:var(--muted);margin:0 0 12px}
.legend i{display:inline-block;width:10px;height:10px;border-radius:2px;margin-right:6px;vertical-align:-1px}
.scroll{overflow-x:auto;border:1px solid var(--line)}
table{border-collapse:collapse;width:100%;min-width:760px;font-size:13px}
th,td{padding:10px 12px;border-bottom:1px solid var(--line);text-align:left;vertical-align:middle}
th{font-weight:500;font-size:11.5px;color:var(--muted);background:var(--soft);white-space:nowrap}
td.num{font-family:var(--mono);text-align:right;font-variant-numeric:tabular-nums;white-space:nowrap}
tr.dom{cursor:pointer}
tr.dom:hover td,tr.dom.on td{background:var(--soft)}
tr.dom.on td:first-child{box-shadow:inset 3px 0 0 var(--fg)}
.files a{text-decoration:none;border-bottom:1px solid var(--line);white-space:nowrap}
.files a:hover{border-color:var(--fg)}
.files small{color:var(--faint);font-family:var(--mono);margin-left:4px}
.dist{display:flex;gap:2px;height:12px;min-width:180px}
.dist span{display:block;height:100%;min-width:2px}
.dist span:first-child{border-radius:3px 0 0 3px}.dist span:last-child{border-radius:0 3px 3px 0}
.new{font-family:var(--mono);font-weight:500}
.new.z{color:var(--faint);font-weight:400}
.filters{display:flex;flex-direction:column;gap:10px;margin-bottom:14px}
.row{display:flex;flex-wrap:wrap;gap:6px;align-items:center}
.row>label{font-size:11.5px;color:var(--muted);width:44px;flex:0 0 auto}
.chip{font:inherit;font-size:12.5px;border:1px solid var(--line);background:var(--bg);color:var(--fg);padding:5px 11px;cursor:pointer;border-radius:999px;display:inline-flex;gap:6px;align-items:center}
.chip:hover{border-color:var(--fg)}
.chip[aria-pressed="true"]{background:var(--fg);color:var(--bg);border-color:var(--fg)}
.chip i{width:8px;height:8px;border-radius:2px;display:inline-block}
.chip:focus-visible,select:focus-visible,input:focus-visible,button:focus-visible,tr.dom:focus-visible{outline:2px solid var(--g-off);outline-offset:2px}
select,input[type=search]{font:inherit;font-size:13px;border:1px solid var(--line);background:var(--bg);color:var(--fg);padding:7px 10px;min-width:0}
input[type=search]{flex:1 1 220px}
.count{font-size:12.5px;color:var(--muted);margin:0 0 8px}
ol.items{list-style:none;margin:0;padding:0;border-top:1px solid var(--line)}
ol.items li{display:grid;grid-template-columns:86px 1fr;gap:4px 14px;padding:12px 0;border-bottom:1px solid var(--line)}
ol.items .d{font-family:var(--mono);font-size:11.5px;color:var(--muted);padding-top:2px}
ol.items .d b{display:block;color:var(--fg);font-weight:500}
.c{min-width:0}
.c a.t{text-decoration:none;font-size:14px;line-height:1.55}
.c a.t:hover{text-decoration:underline}
.meta{display:flex;flex-wrap:wrap;gap:4px 10px;font-size:11.5px;color:var(--muted);margin-top:4px}
.pill{display:inline-flex;align-items:center;gap:5px;white-space:nowrap}
.pill i{width:8px;height:8px;border-radius:2px;display:inline-block}
.loc{font-family:var(--mono);font-size:11px;border:1px solid var(--line);padding:0 6px;border-radius:3px;color:var(--fg)}
.loc.skill{background:var(--hi)}
mark{background:var(--hi);color:inherit}
.more{font:inherit;font-size:13px;margin-top:14px;border:1px solid var(--fg);background:none;color:var(--fg);padding:9px 18px;cursor:pointer}
.feed{display:flex;flex-direction:column;border-top:1px solid var(--line)}
details{border-bottom:1px solid var(--line)}
summary{cursor:pointer;padding:12px 0;display:flex;flex-wrap:wrap;gap:6px 16px;align-items:baseline;list-style:none}
summary::-webkit-details-marker{display:none}
summary::before{content:"+";font-family:var(--mono);color:var(--muted);width:12px}
details[open] summary::before{content:"−"}
summary b{font-family:var(--mono);font-weight:500;min-width:84px}
summary span{font-size:12.5px;color:var(--muted)}
summary span em{font-style:normal;color:var(--fg);font-family:var(--mono)}
.ev{padding:0 0 14px 28px;display:flex;flex-direction:column;gap:12px}
.ev h4{margin:0 0 4px;font-size:12px;font-weight:500;color:var(--muted)}
.ev ul{margin:0;padding:0 0 0 16px;font-size:13px;display:flex;flex-direction:column;gap:3px}
.ev ul small{color:var(--faint)}
.empty{padding:28px 0;color:var(--muted);font-size:13px}
footer{margin-top:48px;padding-top:18px;border-top:1px solid var(--line);font-size:12px;color:var(--muted);display:flex;flex-wrap:wrap;gap:8px 20px}
@media (max-width:560px){ol.items li{grid-template-columns:1fr}ol.items .d b{display:inline;margin-right:8px}.row>label{width:100%}}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}
</style>
<div class="wrap">
<header>
  <div><h1>보통사람 플러그인 현황</h1><p>스킬마다 어떤 파일에 무엇이 실렸는지, 최근에 무엇이 새로 들어왔는지 봅니다.</p></div>
  <p class="mono">빌드 {{BUILT}}</p>
</header>
<div class="stats" id="stats"></div>

<section>
  <h2>날마다 새로 들어온 항목</h2>
  <p class="sub" id="chartSub">처음 수집된 날 기준, 지금 플러그인에 들어 있는 항목만 셉니다. 막대를 누르면 그날 항목만 봅니다.</p>
  <div class="chart" id="chart"></div>
</section>

<section>
  <h2>플러그인 지도</h2>
  <p class="sub">영역 하나가 스킬 하나입니다. SKILL.md는 스킬을 부를 때 통째로 읽히는 요약(등급별 최근 것만), all.md는 공식·여러 명·주의 전체, people.md는 한 사람만 말한 것입니다. 줄을 누르면 아래 목록이 그 영역으로 좁혀집니다.</p>
  <div class="legend" id="legend"></div>
  <div class="scroll"><table><thead><tr><th>영역</th><th style="text-align:right">항목</th><th>등급 분포</th><th>파일 · 실린 수 · 크기</th><th style="text-align:right">7일 신규</th></tr></thead><tbody id="map"></tbody></table></div>
</section>

<section id="browse">
  <h2>항목 찾기</h2>
  <p class="sub">항목을 누르면 GitHub의 상세(원문 인용·출처 링크)가 열립니다.</p>
  <div class="filters">
    <div class="row"><label>기간</label><span id="fPeriod" class="row"></span></div>
    <div class="row"><label>등급</label><span id="fGrade" class="row"></span></div>
    <div class="row"><label>파일</label><span id="fLoc" class="row"></span></div>
    <div class="row"><label for="fDom">영역</label><select id="fDom"></select><input type="search" id="fQ" placeholder="주장·사람 이름으로 찾기" aria-label="검색"></div>
  </div>
  <p class="count" id="count"></p>
  <ol class="items" id="list"></ol>
  <button class="more" id="more" hidden>더 보기</button>
</section>

<section>
  <h2>날짜별 변경 기록</h2>
  <p class="sub">매일 아침 자동 실행이 남긴 기록입니다. 날짜를 펼치면 마감이 지나 빠진 공고, 다시 확인이 필요해진 항목, 여러 번 언급된 항목을 볼 수 있습니다.</p>
  <div class="feed" id="feed"></div>
</section>
<footer><span>매일 06:30 맥미니 자동 빌드</span><a href="https://github.com/{{REPO}}">github.com/n7business/botong-saram</a></footer>
</div>
<div class="tip" id="tip" hidden></div>
<script>
const D = {{DATA}};
const GH = `https://github.com/${D.repo}/blob/main/plugin/skills/`;
const ORDER = ["dep","off","multi","single","hyp","stale"];
const LOC = {skill:"SKILL.md", all:"all.md", people:"people.md"};
const DOMKO = Object.fromEntries(D.domains.map(d => [d.key, d.ko]));
const items = D.items.map(r => ({id:r[0], dom:r[1], g:r[2], claim:r[3], ppl:r[4], np:r[5], first:r[6], last:r[7], loc:r[8], ver:r[9]}));
const byId = Object.fromEntries(items.map(i => [i.id, i]));
const dayMs = 864e5, built = new Date(D.built + "T00:00:00");
const ago = s => s ? Math.round((built - new Date(s + "T00:00:00")) / dayMs) : 9999;
const esc = s => String(s ?? "").replace(/[&<>"]/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
const fmt = n => n.toLocaleString("ko-KR");
const kb = b => b >= 1024 ? Math.round(b/1024) + "KB" : b + "B";
const md = s => s ? s.slice(5).replace("-", "/") : "";
const S = {period:"7", grade:"all", loc:"all", dom:"all", q:"", day:null, shown:60};
const $ = id => document.getElementById(id);
const tip = $("tip");
function showTip(e, html){ tip.innerHTML = html; tip.hidden = false; const x = Math.min(e.clientX + 14, innerWidth - tip.offsetWidth - 8); tip.style.left = x + "px"; tip.style.top = (e.clientY + 14) + "px"; }
function hideTip(){ tip.hidden = true; }

function stats(){
  const n0 = items.filter(i => ago(i.first) === 0).length, n7 = items.filter(i => ago(i.first) < 7).length;
  const ev7 = D.events.filter(e => ago(e[0]) < 7);
  const cnt = k => ev7.filter(e => e[1] === k).length;
  const tiles = [["플러그인 항목", fmt(items.length), `영역 ${D.domains.length}개 · 추적 출처 ${D.people}곳`],
    ["오늘 새로 들어옴", fmt(n0), D.built],["최근 7일 새로 들어옴", fmt(n7), "처음 수집일 기준"],
    ["7일 다시 언급됨", fmt(cnt("reconfirmed")), "같은 말을 또 함"],["7일 마감 지나 빠짐", fmt(cnt("expired")), "공고 신청 기한 경과"]];
  $("stats").innerHTML = tiles.map(t => `<div class="stat"><span>${t[0]}</span><b>${t[1]}</b><small>${t[2]}</small></div>`).join("");
}

function chart(){
  const days = []; for (let k = 20; k >= 0; k--){ const d = new Date(built - k*dayMs); days.push(d.toISOString().slice(0,10)); }
  const pool = items.filter(i => S.dom === "all" || i.dom === S.dom);
  const c = Object.fromEntries(days.map(d => [d, 0])); pool.forEach(i => { if (i.first in c) c[i.first]++; });
  const W = 760, H = 190, L = 34, B = 22, T = 14, R = 6, max = Math.max(10, ...Object.values(c));
  const step = Math.pow(10, Math.floor(Math.log10(max))); const top = Math.ceil(max/step)*step; const ticks = [0, top/2, top];
  const bw = (W - L - R) / days.length, y = v => T + (H - T - B) * (1 - v/top);
  let s = `<svg viewBox="0 0 ${W} ${H}" role="img" aria-label="최근 21일 일별 신규 항목 수">`;
  ticks.forEach(t => { s += `<line x1="${L}" x2="${W-R}" y1="${y(t)}" y2="${y(t)}" stroke="var(--line)" stroke-width="1"/><text x="${L-6}" y="${y(t)+3}" text-anchor="end">${fmt(t)}</text>`; });
  days.forEach((d, k) => {
    const v = c[d], x = L + k*bw + 3, w = bw - 6, h = (H - T - B) - (y(v) - T), on = S.day === d, dim = S.day && !on;
    const fill = dim ? "var(--bar-dim)" : "var(--bar)";
    if (v > 0) s += `<path d="M${x},${y(0)} V${y(v)+Math.min(4,h)} q0,-4 4,-4 h${w-8} q4,0 4,4 V${y(0)} Z" fill="${fill}"/>`;
    if (v > 0 && (on || k === days.length-1 || v === max)) s += `<text x="${x+w/2}" y="${y(v)-5}" text-anchor="middle" style="fill:var(--fg)">${v}</text>`;
    if (k % 3 === 0 || k === days.length-1) s += `<text x="${x+w/2}" y="${H-6}" text-anchor="middle">${md(d)}</text>`;
    s += `<rect class="hit" data-d="${d}" data-v="${v}" x="${L+k*bw}" y="${T}" width="${bw}" height="${H-T-B}" fill="transparent" style="cursor:${v?"pointer":"default"}"/>`;
  });
  $("chart").innerHTML = s + "</svg>";
  $("chartSub").textContent = (S.dom === "all" ? "전체 영역" : DOMKO[S.dom]) + " · 처음 수집된 날 기준, 지금 플러그인에 들어 있는 항목만 셉니다. 막대를 누르면 그날 항목만 봅니다.";
  $("chart").querySelectorAll(".hit").forEach(r => {
    r.addEventListener("mousemove", e => showTip(e, `<b>${r.dataset.d}</b><br>새 항목 ${fmt(+r.dataset.v)}건`));
    r.addEventListener("mouseleave", hideTip);
    r.addEventListener("click", () => { if (!+r.dataset.v) return; S.day = S.day === r.dataset.d ? null : r.dataset.d; S.period = S.day ? "day" : "7"; S.shown = 60; renderAll(); $("browse").scrollIntoView({behavior:"smooth", block:"start"}); });
  });
}

function legend(){ $("legend").innerHTML = ORDER.map(g => `<span><i style="background:var(--g-${g})"></i>${D.grades[g]}</span>`).join(""); }

function map(){
  $("map").innerHTML = D.domains.map(d => {
    const segs = ORDER.filter(g => d.n[g]).map(g => `<span data-tip="${esc(d.ko)} · ${D.grades[g]} ${d.n[g]}건" style="flex:${d.n[g]};background:var(--g-${g})"></span>`).join("");
    const skillN = d.inskill, allN = d.total - d.n.single, pplN = d.n.single;
    const f = (file, n, size) => `<a href="${GH}${d.key}/${file}" target="_blank" rel="noopener">${file}</a><small>${n}건 · ${kb(size)}</small>`;
    const n7 = items.filter(i => i.dom === d.key && ago(i.first) < 7).length;
    return `<tr class="dom${S.dom===d.key?" on":""}" data-k="${d.key}" tabindex="0"><td><b style="font-weight:500">${esc(d.ko)}</b>${d.legal?' <small style="color:var(--faint)">법령</small>':''}<br><small class="mono" style="color:var(--faint)">${d.key}</small></td>
      <td class="num">${fmt(d.total)}</td><td><div class="dist">${segs}</div></td>
      <td class="files"><div style="display:flex;flex-direction:column;gap:2px">${f("SKILL.md", skillN, d.size.SKILL)}${f("all.md", allN, d.size.all)}${f("people.md", pplN, d.size.people)}</div></td>
      <td class="num"><span class="new${n7?"":" z"}">${n7?"+"+n7:"0"}</span></td></tr>`;
  }).join("");
  $("map").querySelectorAll("tr.dom").forEach(tr => {
    const pick = () => { S.dom = S.dom === tr.dataset.k ? "all" : tr.dataset.k; S.shown = 60; renderAll(); };
    tr.addEventListener("click", e => { if (!e.target.closest("a")) pick(); });
    tr.addEventListener("keydown", e => { if (e.key === "Enter" || e.key === " "){ e.preventDefault(); pick(); } });
  });
  $("map").querySelectorAll(".dist span").forEach(s => { s.addEventListener("mousemove", e => showTip(e, esc(s.dataset.tip))); s.addEventListener("mouseleave", hideTip); });
}

function chips(el, opts, key){
  $(el).innerHTML = opts.map(([v, label, color]) => `<button class="chip" aria-pressed="${S[key]===v}" data-v="${v}">${color?`<i style="background:var(--g-${color})"></i>`:""}${label}</button>`).join("");
  $(el).querySelectorAll("button").forEach(b => b.addEventListener("click", () => { S[key] = b.dataset.v; if (key === "period") S.day = null; S.shown = 60; renderAll(); }));
}

function filtered(){
  const q = S.q.trim().toLowerCase();
  return items.filter(i => (S.dom === "all" || i.dom === S.dom) && (S.grade === "all" || i.g === S.grade) && (S.loc === "all" || i.loc === (S.loc === "all.md" ? "all" : S.loc))
    && (S.period === "day" ? i.first === S.day : S.period === "all" ? true : ago(i.first) < +S.period)
    && (!q || i.claim.toLowerCase().includes(q) || i.ppl.join(" ").toLowerCase().includes(q) || i.id.includes(q)))
    .sort((a, b) => b.first.localeCompare(a.first) || b.id.localeCompare(a.id));
}

function hl(s){ const q = S.q.trim(); if (!q) return esc(s); const i = s.toLowerCase().indexOf(q.toLowerCase()); return i < 0 ? esc(s) : esc(s.slice(0,i)) + "<mark>" + esc(s.slice(i, i+q.length)) + "</mark>" + esc(s.slice(i+q.length)); }

function list(){
  const per = [["day", S.day ? md(S.day) + " 하루" : "", null], ["0","오늘"], ["7","7일"], ["30","30일"], ["all","전체"]].filter(o => o[1]);
  chips("fPeriod", per, "period");
  chips("fGrade", [["all","전체"], ...ORDER.map(g => [g, D.grades[g], g])], "grade");
  $("fLoc").innerHTML = [["any","전체"],["skill","SKILL.md (요약)"],["allmd","all.md (전체 목록)"],["people","people.md (한 사람)"]].map(([v,l]) => `<button class="chip" aria-pressed="${(S.loc==="all"?"any":S.loc==="all.md"?"allmd":S.loc)===v}" data-v="${v}">${l}</button>`).join("");
  $("fLoc").querySelectorAll("button").forEach(b => b.addEventListener("click", () => { S.loc = b.dataset.v === "any" ? "all" : b.dataset.v === "allmd" ? "all.md" : b.dataset.v; S.shown = 60; renderAll(); }));
  const rows = filtered();
  const label = S.period === "day" ? `${S.day}에 들어온` : S.period === "0" ? "오늘 들어온" : S.period === "all" ? "전체" : `최근 ${S.period}일 동안 들어온`;
  $("count").textContent = `${S.dom === "all" ? "전체 영역" : DOMKO[S.dom]} · ${label} 항목 ${fmt(rows.length)}건`;
  $("list").innerHTML = rows.length ? rows.slice(0, S.shown).map(i => `<li><div class="d"><b>${md(i.first)}</b>${esc(DOMKO[i.dom])}</div><div class="c">
    <a class="t" href="${GH}${i.dom}/items/${i.id}.md" target="_blank" rel="noopener">${hl(i.claim)}</a>
    <div class="meta"><span class="pill"><i style="background:var(--g-${i.g})"></i>${D.grades[i.g]}${i.g==="multi"?` ${i.np}명`:""}</span>
    <span>${hl(i.ppl.join(", "))}${i.np > 3 ? ` 외 ${i.np-3}` : ""}</span><span class="loc ${i.loc}">${LOC[i.loc]}</span>${i.ver?"<span>수치·교차 확인</span>":""}${i.last && i.last !== i.first ? `<span>최근 언급 ${md(i.last)}</span>` : ""}</div></div></li>`).join("")
    : `<li class="empty" style="display:block">조건에 맞는 항목이 없습니다. 기간을 '전체'로 넓히거나 검색어를 줄여 보세요.</li>`;
  $("more").hidden = rows.length <= S.shown; $("more").textContent = `더 보기 (${fmt(rows.length - S.shown)}건 남음)`;
}

function feed(){
  const by = {}; D.events.forEach(e => { if (S.dom !== "all" && !e[2].startsWith(S.dom + "-")) return; (by[e[0]] ||= []).push(e); });
  const days = Object.keys(by).sort().reverse();
  const KS = ["candidate","verified","reconfirmed","merged","stale","expired","deprecated","hypothesis"];
  const claimOf = id => byId[id]?.claim || D.gone[id] || id;
  const link = id => { const it = byId[id]; return it ? `<a href="${GH}${it.dom}/items/${id}.md" target="_blank" rel="noopener">${esc(it.claim)}</a>` : esc(claimOf(id)); };
  $("feed").innerHTML = days.map((d, n) => {
    const ev = by[d], cnt = k => ev.filter(e => e[1] === k);
    const head = KS.filter(k => cnt(k).length).map(k => `<span>${D.kinds[k]} <em>${cnt(k).length}</em></span>`).join("");
    const block = (k, lim) => { const xs = cnt(k); if (!xs.length) return ""; const uniq = [...new Map(xs.map(e => [e[2], e])).values()];
      return `<div><h4>${D.kinds[k]} ${uniq.length}건</h4><ul>${uniq.slice(0, lim).map(e => `<li>${link(e[2])} <small>${esc(e[3])}</small></li>`).join("")}${uniq.length > lim ? `<li><small>… 외 ${uniq.length - lim}건</small></li>` : ""}</ul></div>`; };
    return `<details${n===0?" open":""}><summary><b>${d}</b>${head}</summary><div class="ev">${block("expired", 20)}${block("stale", 20)}${block("deprecated", 20)}${block("reconfirmed", 12)}</div></details>`;
  }).join("") || `<p class="empty">기록이 없습니다.</p>`;
}

function domSelect(){
  $("fDom").innerHTML = `<option value="all">전체 영역</option>` + D.domains.map(d => `<option value="${d.key}"${S.dom===d.key?" selected":""}>${esc(d.ko)} (${d.total})</option>`).join("");
}
function renderAll(){ stats(); chart(); map(); domSelect(); list(); feed(); }
$("fDom").addEventListener("change", e => { S.dom = e.target.value; S.shown = 60; renderAll(); });
let qt; $("fQ").addEventListener("input", e => { clearTimeout(qt); qt = setTimeout(() => { S.q = e.target.value; S.shown = 60; list(); }, 150); });
$("more").addEventListener("click", () => { S.shown += 100; list(); });
legend(); renderAll();
</script>
'''

if __name__ == "__main__":
    main(); removed_guard()
