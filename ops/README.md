# 맥미니 설치 (사용자 admin, 역삼836 주간 리포트와 같은 방식)

```bash
# 1) 레포
mkdir -p ~/gh/n7business && cd ~/gh/n7business && git clone https://github.com/n7business/botong-saram.git
python3 -m pip install --user --break-system-packages pyyaml
# 2) 스크립트·plist
cp ~/gh/n7business/botong-saram/ops/botong-*.sh ~/Library/Scripts/ && chmod +x ~/Library/Scripts/botong-*.sh
cp ~/gh/n7business/botong-saram/ops/com.botong.*.plist ~/Library/LaunchAgents/
launchctl load ~/Library/LaunchAgents/com.botong.daily.plist ~/Library/LaunchAgents/com.botong.weekly.plist
# 3) 전제: claude CLI 로그인, aside CLI 로그인(u0), ~/.config/envs/builderminseo-telegram.env, korean-law MCP 등록(claude mcp list)
# 4) 수동 1회
bash ~/Library/Scripts/botong-daily.sh; tail -20 ~/Library/Logs/botong-daily.log
```

잡 구성
| 잡 | 시각 | 하는 일 |
|---|---|---|
| com.botong.daily | 매일 06:30 (재시도 12:30) | collect → extract → verify → build → git push, heartbeat 48h 점검 |
| com.botong.weekly | 월 06:00 (재시도 11:00) | lawcheck(개정 감시) → verify → build → push → 텔레그램 다이제스트 |

사후 거부: 다이제스트를 보고 `python3 scripts/deprecate.py <id> "사유"` 후 build·push.
