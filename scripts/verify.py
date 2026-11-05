#!/usr/bin/env python3
"""③ 검증·승격·노화. 규칙만으로 상태를 바꾼다(사람 게이트 없음).
- policy + 공식(weight 1.0) 출처 → verified
- consensus/observed + 독립 출처 ≥ min_sources 그리고 weight 합 ≥ min_weight → verified
- 법·세무 영역: law_ref 있고 모든 출처가 공식 또는 자격자여야 verified
- anecdote는 candidate 유지 · verified 후 review_by 지나면 stale
- 주장에 신청·모집 마감일(…까지/마감, A~B)이 있고 그날이 지나면 expired(플러그인·사이트 제외)
사용: verify.py [--dry]"""
import argparse
from common import *

def src_weight(s, idx):
    m = src_lookup(s, idx)
    if m: return float(m.get("weight", 0.5)), (m.get("type") == "official"), bool(m.get("license") or m.get("type") == "official")
    return 0.3, False, False  # 목록 밖 출처: 낮은 가중치, 자격 미확인

def independent(sources):
    keys = set()
    for s in sources:
        who = s.get("source") or (s.get("author") or "").split("(")[0].strip().lower()
        keys.add(who or norm_url(s.get("url")).split("/")[0])
    return len(keys)

def main():
    a = argparse.ArgumentParser(); a.add_argument("--dry", action="store_true"); a = a.parse_args()
    doms = domains(); idx = source_index(); today = date.today(); n_up = n_stale = 0
    for c in claims():
        if c["status"] == "merged": continue
        d = doms[c["domain"]]; st = c["status"]; new = st; note = ""
        if st == "expired": continue
        dl = deadline_of(c["claim"])
        if dl and c.get("first_seen") and dl < date.fromisoformat(str(c["first_seen"])): dl = None  # 수집 시점에 이미 지난 기간은 마감이 아님
        if dl and dl < today and st != "deprecated":  # 신청·모집 마감 지난 공고는 플러그인에서 뺀다(파일은 보관)
            log(f"{c['id']}: {st} → expired (마감 {dl} 지남)"); c["status"] = "expired"; c["review_by"] = dl.isoformat()
            record_change("expired", c["id"], f"마감 {dl} 지남")
            if not a.dry: write_claim(c)
            continue
        ws = [src_weight(s, idx) for s in c.get("sources", [])]
        wsum = sum(w for w, _, _ in ws); has_official = any(o for _, o, _ in ws); all_licensed = all(l for _, _, l in ws) if ws else False
        n_ind = independent(c.get("sources", []))
        has_book = any((src_lookup(s, idx) or {}).get("type") == "book" for s in c.get("sources", []))
        if st == "candidate":
            ok = False
            if c["evidence"] == "policy" and has_official: ok = True; note = "공식 출처"
            elif has_book and c["evidence"] != "anecdote": ok = True; note = "연구·저서"  # 11/4 민서: 조나 버거 책 등은 공식 출처급
            elif c["evidence"] in ("consensus", "observed") and n_ind >= d["min_sources"] and wsum >= d["min_weight"]: ok = True; note = f"독립 {n_ind}곳 weight {wsum:.1f}"
            elif c["evidence"] == "observed" and not d.get("legal") and max((w for w, _, _ in ws), default=0) >= d.get("single_observed_weight", 0.6):
                ok = True; note = "실무자 실측(단일 출처)"  # 11/3 민서 결정: 비법률 영역은 수치 제시 실무자 글 1곳이면 승격
            if ok and d.get("legal"):
                if not c.get("law_ref") or not c["law_ref"].get("law"): ok = False; note = "law_ref 없음"
                elif not all_licensed: ok = False; note = "자격 미확인 출처 포함"
            if ok:
                c["verified_by"] = note
                new = "verified"; c["review_by"] = min(today + timedelta(days=d["review_days"]), dl or date.max).isoformat()
        elif st == "verified" and c.get("review_by") and date.fromisoformat(c["review_by"]) < today:
            if c.get("last_confirmed") and date.fromisoformat(c["last_confirmed"]) + timedelta(days=d["review_days"]) >= today:
                c["review_by"] = (date.fromisoformat(c["last_confirmed"]) + timedelta(days=d["review_days"])).isoformat(); note = "재확인으로 연장"
            else: new = "stale"; note = "재검토 기한 경과"
        if new != st:
            log(f"{c['id']}: {st} → {new} ({note})"); c["status"] = new
            record_change(new, c["id"], note); n_up += new == "verified"; n_stale += new == "stale"
            if not a.dry: write_claim(c)
        elif note and not a.dry: write_claim(c)
    heartbeat("verify", note=f"verified+={n_up} stale+={n_stale}")
    log(f"검증 완료 승격 {n_up} 노화 {n_stale}")

if __name__ == "__main__": main()
