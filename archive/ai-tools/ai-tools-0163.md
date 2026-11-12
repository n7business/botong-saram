---
id: ai-tools-0163
domain: ai-tools
claim: claude -p 자동화는 v2.1.317 이상으로 올리고 종료 코드를 확인해야, 디스크나 용량 한도가 차서 기록 저장에 실패했는데도
  성공으로 넘어가는 일을 줄일 수 있다.
status: merged
evidence: policy
confidence: 0.9
sources:
- url: https://github.com/anthropics/claude-code/releases/tag/v2.1.317
  author: ashwin-ant
  seen: '2026-11-06'
  quote: Fixed `claude -p` exiting 0 when a full disk or quota lost its transcript
    or ~/.claude.json writes
  source: Claude Code 릴리스 노트 (CHANGELOG)
first_seen: '2026-11-06'
last_confirmed: '2026-11-06'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- 자동화
- 종료코드
- 모니터링
merged_into: ai-tools-0021
---
v2.1.317 이전의 claude -p는 디스크나 용량 한도가 차서 대화 기록이나 ~/.claude.json 쓰기를 잃어도 종료 코드 0으로 끝날 수 있었다. 이 버전부터는 오류를 출력하고, 텍스트·JSON 출력에서는 종료 코드 1로 끝난다. 예약 스크립트는 종료 코드가 0이 아닐 때 알림을 보내도록 만든다. 다만 NFS 내보내기 용량이 찬 경우는 잡히지 않을 수 있으므로, 네트워크 저장소를 쓰면 남은 용량도 따로 살핀다.
