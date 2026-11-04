#!/usr/bin/env python3
"""⑦ 주간 다이제스트 + 감시 생존 확인. 텔레그램으로 보낸다. 사후 거부: 답장에 「폐기 <id>」 → deprecate.py
사용: digest.py [--check-only]"""
import argparse, json
from common import *

def main():
    a = argparse.ArgumentParser(); a.add_argument("--check-only", action="store_true"); a = a.parse_args()
    hb = state_get("heartbeat"); now = datetime.now(); late = []
    for job in ("collect", "extract", "verify", "build"):
        at = hb.get(job, {}).get("at")
        if not at or (now - datetime.fromisoformat(at)) > timedelta(hours=48): late.append(f"{job}({at or '기록 없음'})")
    lc = hb.get("lawcheck", {}).get("at")
    if not lc or (now - datetime.fromisoformat(lc)) > timedelta(days=10): late.append(f"lawcheck({lc or '기록 없음'})")
    if a.check_only:
        if late: telegram("🚨 <b>보통사람 감시 지연</b>\n" + "\n".join("- " + l for l in late))
        else: log("heartbeat 정상")
        return
    week = []
    for i in range(7):
        p = CHANGELOG / f"{(date.today() - timedelta(days=i)).isoformat()}.json"
        if p.exists(): week += json.loads(p.read_text(encoding="utf-8"))
    kinds = {}
    for e in week: kinds.setdefault(e["kind"], []).append(e["id"])
    lines = ["📚 <b>보통사람 주간 다이제스트</b> " + TODAY]
    for k, ko in (("verified", "✅ 승격"), ("candidate", "🆕 후보"), ("stale", "⚠️ 주의 강등"), ("deprecated", "⛔ 폐기"), ("reconfirmed", "🔁 재확인")):
        if kinds.get(k): lines.append(f"{ko} {len(kinds[k])}: " + ", ".join(kinds[k][:12]) + (" …" if len(kinds[k]) > 12 else ""))
    if len(lines) == 1: lines.append("변경 없음")
    lines.append("\n거부: 「폐기 <id> 사유」로 답장 → scripts/deprecate.py")
    lines.append(("🚨 감시 지연: " + ", ".join(late)) if late else "🫀 감시 정상")
    telegram("\n".join(lines)); heartbeat("digest"); log("\n".join(lines))

if __name__ == "__main__": main()
