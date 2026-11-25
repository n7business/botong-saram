---
id: ai-tools-0824
domain: ai-tools
claim: AI 에이전트가 스스로 실행할 수 있는 범위를 정할 때는 조회는 항상 허용하고 삭제·재시작·재배포처럼 되돌리기 어려운 작업은 막아야 하며,
  위험한지 판단하는 장치가 고장 나면 모든 작업을 거절하도록(fail-close) 설정해야 한다.
status: candidate
evidence: anecdote
confidence: 0.65
sources:
- url: https://www.youtube.com/watch?v=f1MqkjGyKsg
  author: 테디노트 TeddyNote (김현민 발표, 넥스클라우드)
  seen: '2026-11-25'
  quote: 모델에 문제가 생기는 경우에는 제가 fail close로 다 거절을 하게 됩니다.
  source: 테디노트 TeddyNote
first_seen: '2026-11-25'
last_confirmed: '2026-11-25'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 에이전트
- 권한관리
- 자동실행
- fail-close
---
읽기만 하는 작업은 데이터를 바꾸지 않으므로 항상 허용해도 된다. 삭제나 특정 값 수정, 서버 재시작·재배포는 위험하므로 자동 실행에서 빼고 사람이 확인하게 한다. 위험 여부를 AI 모델로 판정하게 했다면, 그 모델에 문제가 생겼을 때 기본값이 '전부 거절'이어야 사고가 나지 않는다. 고객에게 실제로 나가는 발송도 이 판정을 거치게 한다.
