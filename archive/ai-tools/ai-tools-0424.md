---
id: ai-tools-0424
domain: ai-tools
claim: claude -p로 자동 작업을 돌릴 때 백그라운드 명령은 10분이 지나면 중지되므로, 그보다 오래 걸리는 수집·빌드 작업은 백그라운드로
  맡기지 말고 따로 실행하거나 단계를 나눠야 한다.
status: verified
evidence: policy
confidence: 0.7
sources:
- url: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
  author: anthropics
  seen: '2026-11-10'
  quote: background commands get 30 minutes when they are stopped after 10
  source: Claude Code 릴리스 노트 (CHANGELOG)
first_seen: '2026-11-10'
last_confirmed: '2026-11-10'
review_by: '2026-12-10'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- 자동화
- headless
- 백그라운드
- 시간제한
verified_by: 공식 출처
---
2.1.321 이전 버전의 claude -p는 백그라운드 명령에 30분이 주어진다고 클로드에게 잘못 알려 주기도 했습니다. 실제로는 10분 뒤 중지됩니다. 예약 실행으로 claude -p를 돌리는데 긴 작업이 중간에 끊긴다면 이 제한 때문일 수 있습니다. 오래 걸리는 단계는 launchd·cron 스크립트에서 따로 실행하거나, 10분 안에 끝나는 단위로 쪼개세요.
