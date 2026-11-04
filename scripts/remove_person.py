#!/usr/bin/env python3
"""원작자 삭제 요청 처리. 이름·핸들·URL 조각으로 그 사람을 보통사람에서 완전히 뺀다.
- sources.yaml에서 해당 소스 삭제(수집 중단)
- 그 사람만 출처인 항목은 파일 삭제, 다른 사람과 같이 말한 항목은 그 사람 출처만 제거
- changelog·state·inbox에서 흔적 삭제
사용: remove_person.py "<핸들 또는 이름>" [--dry]   → 이후 build_plugin.py·build_site.py·commit·push"""
import sys, re, json
from common import *

def main():
    if len(sys.argv) < 2: sys.exit(__doc__)
    pat = re.compile(re.escape(sys.argv[1].lstrip("@")), re.I); dry = "--dry" in sys.argv
    hit = lambda o: bool(pat.search(json.dumps(o, ensure_ascii=False)))
    # 1) sources.yaml — 블록 단위로 삭제(주석·순서 보존)
    p = SOURCES
    lines = p.read_text(encoding="utf-8").split("\n"); out = []; block = []; removed_src = []
    def flush():
        if block and pat.search("\n".join(block)) and block[0].startswith("- name:"): removed_src.append(block[0][8:])
        else: out.extend(block)
    for l in lines:
        if l.startswith("- name:") or (l and not l.startswith(" ") and not l.startswith("-")): flush(); block = [l]
        else: block.append(l)
    flush()
    # 2) 항목
    deleted, trimmed = [], []
    for c in claims():
        srcs = c.get("sources", []); mine = [s for s in srcs if hit(s)]
        if not mine: continue
        if len(mine) == len(srcs):
            deleted.append(c["id"])
            if not dry: Path(c["_path"]).unlink()
        else:
            trimmed.append(c["id"])
            if not dry: c["sources"] = [s for s in srcs if s not in mine]; write_claim(c)
    print("소스 삭제:", removed_src or "없음"); print("항목 삭제:", deleted); print("출처만 제거:", trimmed)
    if dry: return
    p.write_text("\n".join(out), encoding="utf-8"); load_yaml(p)
    # 3) 흔적
    for f in CHANGELOG.glob("*.json"):
        lst = json.loads(f.read_text(encoding="utf-8"))
        new = [e for e in lst if e.get("id") not in deleted and not hit(e)]
        if len(new) != len(lst): f.write_text(json.dumps(new, ensure_ascii=False, indent=1), encoding="utf-8")
    for k in ("collect_seen", "extracted"):
        d = state_get(k); state_set(k, {a: b for a, b in d.items() if not pat.search(a)})
    for f in INBOX.glob("*/*.json"):
        if pat.search(f.name) or hit(json.loads(f.read_text(encoding="utf-8")).get("source", {})): f.unlink()
    # 변경 이력에는 기록하지 않는다 — 공개 저장소에 이름이 다시 남지 않게.
    log(f"삭제 완료 — build_plugin.py·build_site.py 실행 후 커밋·push. 남은 언급 확인: git grep -i '{sys.argv[1]}'")

if __name__ == "__main__": main()
