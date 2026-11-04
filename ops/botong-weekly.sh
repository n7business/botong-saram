#!/bin/bash
# 보통사람 주간 — 맥미니 launchd com.botong.weekly (월 06:00, 재시도 11:00). 개정 감시 → 재검증 → 빌드 → 다이제스트.
export PATH="$HOME/.local/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin"
# 무인 실행용 장기 토큰(claude setup-token). 파일이 있으면 읽는다 — 값은 파일에만.
[ -f "$HOME/.config/envs/claude-oauth.env" ] && set -a && . "$HOME/.config/envs/claude-oauth.env" && set +a
REPO="${BOTONG_REPO:-$HOME/gh/n7business/botong-saram}"
LOG="$HOME/Library/Logs/botong-weekly.log"; STAMP="$HOME/Library/Logs/botong-weekly.last"
WEEK=$(date +%G-W%V)
[ -f "$STAMP" ] && [ "$(cat "$STAMP")" = "$WEEK" ] && exit 0
exec >> "$LOG" 2>&1
echo "===== $(date '+%F %T') $WEEK ====="
cd "$REPO" && git pull -q --ff-only
python3 scripts/lawcheck.py && python3 scripts/verify.py && python3 scripts/build_plugin.py && python3 scripts/build_site.py \
  && git add archive changelog plugin site && git commit -qm "weekly $WEEK" ; git push -q
python3 scripts/digest.py && echo "$WEEK" > "$STAMP"
