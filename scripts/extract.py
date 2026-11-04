#!/usr/bin/env python3
"""② 추출. inbox 원문 → claim 단위 md(candidate). Claude Code headless 사용.
출처 URL 없는 주장은 버린다. 기존 항목과 중복이면 last_confirmed 갱신, 충돌이면 supersedes 연결.
사용: extract.py [--date YYYY-MM-DD] [--limit N]"""
import argparse, json
from common import *

PROMPT = """당신은 한국 소규모 사업자용 지식 아카이브의 추출기입니다. 아래 원문에서 "보통사람(직원 0~10명 사업자)이 알아야 할 실행 가능한 주장"만 뽑으세요.

영역: {dom} ({ko}){legal_note}{also_note}
{domain_guide}
원문 출처: {src_name} ({src_type}) {src_url}
수집일: {today}

기존 아카이브 항목(중복·충돌 판단용, id: 주장):
{existing}

규칙
- 주장 1개 = 한 문장. 근거 URL이 원문 안에 없으면 원문 페이지 URL을 출처로 쓰되, 원문이 목록 페이지라서 개별 글 URL이 없으면 그 주장은 버린다.
- 광고·단순 소개·근거 없는 일반론은 버린다. 실무 영역은 "무엇을 하면/하지 말면 어떤 결과"가 있는 것만. mindset 영역이 허용되면 화자가 반복해서 강조하는 사장의 원칙·습관·관점(예: "매출보다 현금 잔고를 매일 본다")도 1문장 주장으로 뽑되 domain을 mindset으로 둔다.
- 각 주장에 "domain" 필드: 허용 영역 중 하나.
- quote는 원문에서 그대로 1~2문장(50자 이내 권장). 지어내지 말 것.
- evidence: policy(공식 기관·플랫폼 정책 문서) | consensus(전문가 의견) | observed(수치·실험 결과 제시) | anecdote(단일 경험담)
- duplicate_of: 기존 항목과 같은 주장이면 그 id. contradicts: 기존 항목을 뒤집는 주장이면 그 id.
- 법·세무 영역이면 law_ref에 {{law: 법령명, article: 제n조, effective: 시행일}}을 가능한 한 채운다. 모르면 null.
- 최대 {limit}개. 없으면 빈 배열.

다른 말 없이 JSON만:
{{"claims": [{{"domain": "허용 영역 중 하나", "claim": "...", "body": "무엇을/어떻게/주의점 3~6문장, 플러그인에 그대로 실릴 문장", "evidence": "policy|consensus|observed|anecdote", "confidence": 0.0~1.0, "sources": [{{"url": "...", "author": "...", "seen": "{today}", "quote": "..."}}], "law_ref": null, "duplicate_of": null, "contradicts": null, "tags": ["..."]}}]}}

원문:
<<<
{text}
>>>"""

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--date", default=TODAY); ap.add_argument("--limit", type=int, default=8)
    a = ap.parse_args()
    doms = domains(); done = state_get("extracted"); day = INBOX / a.date
    cur_src = {(d, x.get("name")): x for d, l in sources().items() for x in l or []}
    if not day.exists(): log("inbox 없음", day); return
    n_new = n_dup = n_conf = n_drop = 0
    for f in sorted(day.glob("*.json")):
        rec = json.loads(f.read_text(encoding="utf-8")); dom = rec["domain"]; src = rec["source"]
        src = dict(src, **{k: v for k, v in cur_src.get((dom, src.get("name")), {}).items() if k in ("also", "weight", "license", "contributor_info")})  # 수집 뒤 바뀐 소스 설정 반영
        key = f"{a.date}/{f.name}@{rec.get('fetched_at','')}"  # 같은 날 재수집(내용 변경)도 다시 추출
        if key in done: continue
        text = rec.get("text", "")
        post_urls = {norm_url(p.get("url", "")) for p in rec.get("posts", []) + rec.get("items", [])}
        if len(text) < 200: done[key] = "short"; continue
        existing = claims(dom)
        ex_txt = "\n".join(f"- {c['id']}: {c['claim']}" for c in existing[-80:]) or "(없음)"
        legal = doms[dom].get("legal")
        also = [d for d in (src.get("also") or []) if d in doms]
        allowed = [dom] + also
        guides = {"mindset": "mindset 지침: 동기부여 구호가 아니라 그 사람이 실제로 지키는 원칙·습관·판단 기준만. 누가 말했는지가 핵심이므로 author를 정확히.",
                  "metrics": "metrics 지침: 숫자·비율·주기가 들어간 관리 기준(예: 월 손익 마감일, 마진율 하한, 현금 몇 달치)을 우선.",
                  "marketing": "marketing 지침: 플랫폼별 구체 행동(게시 형식·빈도·훅·CTA·금지 행동)과 그 근거·수치."}
        domain_guide = "\n".join(guides[d] for d in allowed if d in guides)
        if also: existing = existing + [c for d2 in also for c in claims(d2)]
        prompt = PROMPT.format(dom=dom, ko=doms[dom]["ko"], legal_note=" — 법·세무 영역: 조문 근거 필수" if legal else "", also_note=(" · 허용 영역: " + ", ".join(allowed)) if also else "", domain_guide=domain_guide,
                               src_name=src["name"], src_type=src["type"], src_url=src["url"], today=a.date, existing=ex_txt, limit=a.limit, text=text[:24000])
        res = None
        for attempt in (1, 2):
            try: res = run_claude(prompt if attempt == 1 else prompt + "\n\n(이전 응답이 올바른 JSON이 아니었습니다. 문자열 안의 따옴표는 \\\" 로 이스케이프하고, 코드펜스 없이 JSON 객체 하나만 출력하세요.)"); break
            except Exception as e: log(f"추출 실패({attempt}/2)", f.name, str(e)[:160])
        if res is None: continue
        by_id = {c["id"]: c for c in existing}
        for c in res.get("claims", []):
            srcs = [s for s in c.get("sources", []) if s.get("url", "").startswith("http")]
            if not srcs: n_drop += 1; continue
            src_host = norm_url(src["url"]).split("/")[0]
            for s in srcs:
                s.setdefault("seen", a.date); s.setdefault("author", src.get("author", src["name"]))
                if norm_url(s["url"]).split("/")[0] == src_host or norm_url(s["url"]) in post_urls: s["source"] = src["name"]
            if c.get("duplicate_of") in by_id:
                old = by_id[c["duplicate_of"]]; old["last_confirmed"] = a.date
                known = {norm_url(s["url"]) for s in old.get("sources", [])}
                old["sources"] += [s for s in srcs if norm_url(s["url"]) not in known]
                write_claim(old); record_change("reconfirmed", old["id"], src["name"]); n_dup += 1; continue
            cdom = c.get("domain") if c.get("domain") in allowed else dom
            cid = next_id(cdom)
            fm = {"id": cid, "domain": cdom, "claim": c["claim"], "status": "candidate", "evidence": c.get("evidence", "anecdote"),
                  "confidence": float(c.get("confidence", 0.5)), "sources": srcs, "first_seen": a.date, "last_confirmed": a.date,
                  "review_by": None, "supersedes": None, "superseded_by": None, "experiment": None,
                  "law_ref": c.get("law_ref"), "contributor": src.get("contributor_info"), "tags": c.get("tags", []),
                  "_path": str(claim_path(cid)), "_body": c.get("body", "")}
            if fm["law_ref"] and isinstance(fm["law_ref"], dict) and not fm["law_ref"].get("effective"):
                fm["law_ref"]["effective"] = a.date  # 시행일 미상 → 항목 작성일을 기준일로(그 시점 현행법에 근거)
            if c.get("contradicts") in by_id:
                old = by_id[c["contradicts"]]; fm["supersedes"] = old["id"]; old["superseded_by"] = cid
                if old["status"] == "verified": old["status"] = "stale"; record_change("stale", old["id"], f"충돌: {cid}")
                write_claim(old); n_conf += 1
            write_claim(fm); by_id[cid] = fm; existing.append(fm); record_change("candidate", cid, src["name"]); n_new += 1
        done[key] = "ok"; state_set("extracted", done)
        log(f"{f.name}: 신규 {n_new} 재확인 {n_dup} 충돌 {n_conf} 폐기 {n_drop}")
    heartbeat("extract", note=f"new={n_new} dup={n_dup} conflict={n_conf} drop={n_drop}")

if __name__ == "__main__": main()
