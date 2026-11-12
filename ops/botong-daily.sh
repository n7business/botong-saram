#!/bin/bash
# 보통사람 매일 파이프라인 — 맥미니 launchd com.botong.daily (매일 06:30, 재시도 12:30). 같은 날 한 번만.
export PATH="$HOME/.local/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin"
# 무인 실행용 장기 토큰(claude setup-token). 파일이 있으면 읽는다 — 값은 파일에만.
[ -f "$HOME/.config/envs/claude-oauth.env" ] && set -a && . "$HOME/.config/envs/claude-oauth.env" && set +a
REPO="${BOTONG_REPO:-$HOME/gh/n7business/botong-saram}"
LOG="$HOME/Library/Logs/botong-daily.log"; STAMP="$HOME/Library/Logs/botong-daily.last"
DAY=$(date +%F)
[ -f "$STAMP" ] && [ "$(cat "$STAMP")" = "$DAY" ] && exit 0
exec >> "$LOG" 2>&1
echo "===== $(date '+%F %T') ====="
cd "$REPO" && git pull -q --ff-only
python3 scripts/collect.py && python3 scripts/extract.py && python3 scripts/cluster.py && python3 scripts/verify.py && python3 scripts/build_plugin.py && python3 scripts/build_site.py && python3 scripts/build_dashboard.py \
  && git add archive changelog plugin site README.md && git commit -qm "daily $DAY" && git push -q \
  && echo "$DAY" > "$STAMP"
python3 scripts/digest.py --check-only
