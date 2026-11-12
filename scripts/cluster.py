#!/usr/bin/env python3
"""②-b 묶기. 영역마다 후보·검증 주장 전체를 Claude에 보내 '같은 말'끼리 묶는다.
대표 항목에 다른 항목의 출처를 합치고(언급 횟수↑), 나머지는 status=merged(merged_into)로 남긴다.
서로 다른 사람 2명 이상이 같은 말을 하면 anecdote → consensus 로 올려 verify가 교차 확인으로 판정하게 한다.
사용: cluster.py [--domain marketing] [--dry]"""
import argparse
from common import *

PROMPT = """아래는 한국 소규모 사업자용 노하우 아카이브의 '{ko}' 영역 주장 목록입니다(id: 주장).
**같은 행동·같은 결론**을 말하는 주장끼리 묶으세요. 표현이 달라도 실질이 같으면 같은 묶음, 조건·수치·대상이 다르면 다른 묶음.
2개 이상인 묶음만 출력. 각 묶음의 대표(keep)는 가장 구체적이고 정확한 주장 id. 대표 문장을 더 정확하게 다듬을 필요가 있으면 claim에 새 문장(한 문장), 아니면 null.
다른 말 없이 JSON만: {{"groups": [{{"keep": "id", "merge": ["id", ...], "claim": null}}]}}

{items}"""

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--domain"); ap.add_argument("--dry", action="store_true"); a = ap.parse_args()
    doms = domains(); total_m = 0
    for dom, d in doms.items():
        if a.domain and dom != a.domain: continue
        cs = [c for c in claims(dom) if c["status"] in ("candidate", "verified", "hypothesis", "stale")]
        if len(cs) < 2: continue
        by = {c["id"]: c for c in cs}
        groups = []
        for i in range(0, len(cs), 180):  # 영역이 크면 나눠서
            chunk = cs[i:i + 180]
            items = "\n".join(f"{c['id']}: {c['claim']}" for c in chunk)
            try: groups += run_claude(PROMPT.format(ko=d["ko"], items=items)).get("groups", [])
            except Exception as e: log(f"{dom} 묶기 실패: {e}")
        n_m = 0
        for g in groups:
            keep = by.get(g.get("keep")); merge = [by[m] for m in g.get("merge", []) if m in by and m != g.get("keep")]
            if not keep or not merge or keep["status"] == "merged": continue
            known = {norm_url(s["url"]) for s in keep.get("sources", [])}
            for m in merge:
                if m["status"] == "merged": continue
                for s in m.get("sources", []):
                    if norm_url(s["url"]) not in known: keep["sources"].append(s); known.add(norm_url(s["url"]))
                if m["status"] == "verified" and keep["status"] != "verified": keep["status"] = "verified"; keep["review_by"] = m.get("review_by"); keep["verified_by"] = m.get("verified_by")
                if m.get("law_ref") and not keep.get("law_ref"): keep["law_ref"] = m["law_ref"]
                m["status"] = "merged"; m["merged_into"] = keep["id"]
                if not a.dry: write_claim(m)
                n_m += 1
            if g.get("claim"): keep["claim"] = g["claim"]
            people = {(s.get("source") or (s.get("author") or "").split("(")[0].strip().lower() or norm_url(s["url"]).split("/")[0]) for s in keep["sources"]}
            if len(people) >= 2 and keep["evidence"] == "anecdote": keep["evidence"] = "consensus"
            keep["mentions"] = len(keep["sources"]); keep["last_confirmed"] = max(s.get("seen") or "" for s in keep["sources"]) or keep["last_confirmed"]
            if not a.dry: write_claim(keep)
            record_change("merged", keep["id"], f"+{len(merge)}")
        log(f"{dom}: 묶음 {len(groups)} · 합친 항목 {n_m}"); total_m += n_m
    heartbeat("cluster", note=f"merged={total_m}")

if __name__ == "__main__": main()
