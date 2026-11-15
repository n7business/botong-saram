#!/usr/bin/env python3
"""인용 당사자 통지 발송 목록. 개인 출처(official·book 제외)마다 영역·현재 항목 수·채널 주소. 발송은 사람이 한다(docs/notice.md)."""
from common import *
def main():
    idx = source_index(); cnt = {}
    for c in claims():
        if c["status"] in ("merged", "expired"): continue
        for s in c.get("sources", []):
            m = src_lookup(s, idx)
            if m and m.get("type") not in ("official", "book"): cnt[m["name"]] = cnt.get(m["name"], 0) + 1
    rows = sorted(((cnt.get(v["name"], 0), v["domain"], v["name"], v.get("type"), v.get("url", "")) for v in idx.values() if v.get("type") not in ("official", "book")), reverse=True)
    print(f"개인 출처 {len(rows)}곳 · 항목 {sum(r[0] for r in rows)}건\n")
    for n, dom, name, t, url in rows: print(f"{n:4d}  {dom:<14} {t:<10} {name}  {url}")
if __name__ == "__main__": main()
