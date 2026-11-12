# claude -p로 자동 작업을 돌릴 때 백그라운드 명령은 10분이 지나면 중지되므로, 그보다 오래 걸리는 수집·빌드 작업은 백그라운드로 맡기지 말고 따로 실행하거나 단계를 나눠야 한다.

🏛 공식 발표 · Claude Code 릴리스 노트 (CHANGELOG)

2.1.321 이전 버전의 claude -p는 백그라운드 명령에 30분이 주어진다고 클로드에게 잘못 알려 주기도 했습니다. 실제로는 10분 뒤 중지됩니다. 예약 실행으로 claude -p를 돌리는데 긴 작업이 중간에 끊긴다면 이 제한 때문일 수 있습니다. 오래 걸리는 단계는 launchd·cron 스크립트에서 따로 실행하거나, 10분 안에 끝나는 단위로 쪼개세요.

- 근거 policy · 처음 2026-11-10 · 최근 확인 2026-11-10 · 재검토 2026-12-10 · 검증 공식 출처

## 출처
- anthropics · 2026-11-10 · https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
  > background commands get 30 minutes when they are stopped after 10
