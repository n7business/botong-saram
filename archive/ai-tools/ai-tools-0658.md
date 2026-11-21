---
id: ai-tools-0658
domain: ai-tools
claim: 클로드 코드 예약 작업이나 /loop로 반복 업무를 돌리고 있다면 v2.1.330으로 업데이트한 뒤 예전에 만든 반복 작업을 다시 등록해야
  한다. 이 버전부터 반복 작업은 최대 30일까지 돌지만, 업데이트 전에 만든 작업은 계속 7일 뒤에 끝나기 때문이다.
status: verified
evidence: policy
confidence: 0.85
sources:
- url: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
  author: anthropics (Anthropic)
  seen: '2026-11-21'
  quote: tasks made before this release still end at 7 days
  source: Claude Code 릴리스 노트 (CHANGELOG)
first_seen: '2026-11-21'
last_confirmed: '2026-11-21'
review_by: '2026-12-21'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- 예약작업
- 자동화
- 업데이트
verified_by: 공식 출처
---
v2.1.330부터 반복 예약 작업과 /loop는 세션이 켜져 있는 동안 7일이 아니라 최대 30일까지 실행되고, 끝날 때는 끝난다고 알려 준다. 다만 이 버전 전에 만든 작업에는 바뀐 기간이 적용되지 않아 여전히 7일 뒤에 멈춘다. 업데이트한 뒤 /tasks에서 반복 작업 목록을 확인하고, 오래 돌려야 하는 작업은 지우고 새로 등록하는 게 좋다. 세션이 꺼지면 30일 전이라도 작업이 멈춘다는 점은 그대로다.
