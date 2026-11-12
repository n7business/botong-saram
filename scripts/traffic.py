#!/usr/bin/env python3
"""⑧ GitHub 방문 기록. GitHub은 방문·클론·유입 경로를 14일치만 보여 주므로 매일 state/traffic.json에 쌓는다(공개 안 됨).
주간 다이제스트가 지난 7일 합계와 유입 경로를 한 줄로 보낸다. gh 로그인(저장소 push 권한) 필요.
사용: traffic.py [--show]"""
import argparse, json, subprocess
from common import *

REPO = "n7business/botong-saram"

def gh(path):
    r = subprocess.run(["gh", "api", f"repos/{REPO}" + (f"/{path}" if path else "")], capture_output=True, text=True, timeout=60)
    if r.returncode: raise RuntimeError(r.stderr.strip()[-200:])
    return json.loads(r.stdout)

def collect():
    t = state_get("traffic", {}) or {}
    daily = t.setdefault("daily", {})
    for kind in ("views", "clones"):
        for d in gh(f"traffic/{kind}").get(kind, []):
            day = d["timestamp"][:10]
            daily.setdefault(day, {})[kind] = d["count"]; daily[day][kind + "_u"] = d["uniques"]
    t.setdefault("referrers", {})[TODAY] = [{"src": r["referrer"], "n": r["count"], "u": r["uniques"]} for r in gh("traffic/popular/referrers")]
    t.setdefault("paths", {})[TODAY] = [{"path": p["path"], "n": p["count"], "u": p["uniques"]} for p in gh("traffic/popular/paths")][:10]
    repo = gh("")
    t.setdefault("stars", {})[TODAY] = {"stars": repo["stargazers_count"], "forks": repo["forks_count"], "watchers": repo["subscribers_count"]}
    state_set("traffic", t)
    return t

def week_line(t=None):
    """주간 다이제스트용 한 줄."""
    t = t or state_get("traffic", {}) or {}
    days = [(date.today() - timedelta(days=i)).isoformat() for i in range(1, 8)]
    v = sum(t.get("daily", {}).get(d, {}).get("views", 0) for d in days); c = sum(t.get("daily", {}).get(d, {}).get("clones", 0) for d in days)
    s = t.get("stars", {}); now = s[max(s)] if s else {}; before = s.get(min((d for d in s if d >= days[-1]), default=""), now) if s else {}
    refs = t.get("referrers", {}); top = refs[max(refs)][:3] if refs else []
    line = f"👀 GitHub 7일: 방문 {v} · 클론 {c} · ⭐ {now.get('stars', 0)}(+{now.get('stars', 0) - before.get('stars', 0)}) · 포크 {now.get('forks', 0)}"
    if top: line += " · 유입 " + ", ".join(f"{r['src']} {r['u']}명" for r in top)
    return line

if __name__ == "__main__":
    a = argparse.ArgumentParser(); a.add_argument("--show", action="store_true"); a = a.parse_args()
    try:
        t = collect(); heartbeat("traffic", note=week_line(t))
    except Exception as e:
        heartbeat("traffic", ok=False, note=str(e)[:200]); log(f"traffic 실패: {e}"); raise SystemExit(0)  # 방문 기록 실패로 매일 파이프라인을 멈추지 않는다
    log(week_line(t))
