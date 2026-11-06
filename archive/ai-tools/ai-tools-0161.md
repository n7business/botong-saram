---
id: ai-tools-0161
domain: ai-tools
claim: Claude Code의 /schedule로 클라우드 예약 작업을 만들 때 요청하지 않은 커넥터가 붙었다는 경고가 뜨면, 안내된 방법으로
  제거해야 예약 작업이 필요 없는 외부 서비스까지 연결된 채 돌지 않는다.
status: verified
evidence: policy
confidence: 0.85
sources:
- url: https://github.com/anthropics/claude-code/releases/tag/v2.1.317
  author: ashwin-ant
  seen: '2026-11-06'
  quote: Added a warning to `/schedule` when a new cloud scheduled task gets connectors
    you did not ask for
  source: Claude Code 릴리스 노트 (CHANGELOG)
first_seen: '2026-11-06'
last_confirmed: '2026-11-06'
review_by: '2026-12-06'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- 예약작업
- 커넥터
- 권한
verified_by: 공식 출처
---
Claude Code v2.1.317부터 /schedule은 새 클라우드 예약 작업에 요청하지 않은 커넥터가 붙으면 경고하고 제거 방법을 함께 보여 준다. 예약 작업은 사람이 지켜보지 않을 때 실행되므로, 경고가 뜨면 넘기지 말고 어떤 커넥터가 붙었는지 확인한다. 그 작업에 필요 없는 커넥터는 경고에 나온 방법대로 제거한다.
