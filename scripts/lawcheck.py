#!/usr/bin/env python3
"""⑤ 개정 감시(주 1회). 법·세무 영역 claim의 law_ref를 korean-law MCP로 조회해 시행일 이후 개정이 있으면 stale + 기고자 알림.
사용: lawcheck.py [--dry]"""
import argparse, json
from common import *

PROMPT = """korean-law MCP의 search_law(필요하면 execute_tool search_law_bulk)로 아래 법령들의 **현행 시행일·최근 개정일**을 확인하세요.
각 항목의 effective(우리가 근거한 기준일) **이후에 시행된** 개정이 있으면 revised=true. 기준일 이전에 시행된 개정은 이미 반영된 것이므로 false.
다른 말 없이 JSON만: {{"results": [{{"law": "...", "current_effective": "YYYY-MM-DD", "revised": true|false, "note": "개정 요지 한 줄"}}]}}

법령 목록:
{laws}"""

def main():
    a = argparse.ArgumentParser(); a.add_argument("--dry", action="store_true"); a = a.parse_args()
    doms = domains(); legal = [c for c in claims() if doms[c["domain"]].get("legal") and c.get("law_ref") and c["law_ref"].get("law")]
    laws = {}
    for c in legal: laws.setdefault(c["law_ref"]["law"], c["law_ref"].get("effective") or c["first_seen"])
    if not laws: log("law_ref 있는 항목 없음"); heartbeat("lawcheck", note="no law_ref"); state_set("lawcheck", {"at": TODAY, "checked": 0}); return
    lst = "\n".join(f"- {l} (effective {e})" for l, e in laws.items())
    res = run_claude(PROMPT.format(laws=lst), allowed_tools=["mcp__korean-law__search_law", "mcp__korean-law__execute_tool", "mcp__korean-law__get_law_text"])
    revised = {r["law"]: r for r in res.get("results", []) if r.get("revised")}
    n = 0
    for c in legal:
        r = revised.get(c["law_ref"]["law"])
        if r and c["status"] == "verified":
            c["status"] = "stale"; c["law_ref"]["revised_note"] = r.get("note"); c["law_ref"]["current_effective"] = r.get("current_effective")
            record_change("stale", c["id"], f"개정: {c['law_ref']['law']} {r.get('note','')}"); n += 1
            if not a.dry: write_claim(c)
            log(f"{c['id']} stale — {c['law_ref']['law']} 개정")
    state_set("lawcheck", {"at": TODAY, "checked": len(laws), "revised": list(revised)})
    heartbeat("lawcheck", note=f"laws={len(laws)} revised={len(revised)} stale+={n}")
    if revised: telegram("⚖️ <b>보통사람 개정 감지</b>\n" + "\n".join(f"- {l}: {r.get('note','')}" for l, r in revised.items()) + f"\n→ {n}개 항목 stale, 기고자 확인 필요")

if __name__ == "__main__": main()
