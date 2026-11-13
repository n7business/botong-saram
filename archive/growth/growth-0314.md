---
id: growth-0314
domain: growth
claim: 고객 글을 대신 써 주는 AI 기능을 만들 때 분량을 강하게 요구하면 AI가 없는 사실을 지어내므로, 목표 분량을 문장 수로 주고 실제
  글자 수는 서버에서 세어 부족할 때만 '새 사실 없이 늘려라'로 다시 요청해 볼 만하다.
status: candidate
evidence: observed
confidence: 0.6
sources:
- url: https://disquiet.io/products/b0679f65-d33a-4c40-ad3e-d233b1a98896
  author: 도트폴드
  seen: '2026-11-13'
  quote: 분량을 85~92%로 강하게 걸면 메모에 없는 행동·감정·결과를 지어냈어요.
  source: 디스콰이엇
first_seen: '2026-11-13'
last_confirmed: '2026-11-13'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- AI기능
- 환각
- 프롬프트
- 품질검증
---
한 1인 개발자는 AI 자소서 초안 기능에 분량을 제한의 85~92%로 강하게 걸자, 사용자 메모에 없는 행동·감정·결과를 지어냈다고 전한다. 반대로 지어내기를 강하게 막으면 분량이 제한의 35~50%로 짧아졌다. 그래서 AI에게는 목표를 문장 수로 주고, 결과가 70% 미만이면 서버가 실제 글자 수를 센 뒤 새 사실 없이 늘리라고 한 번 더 요청했다. 가상 사례 10개를 돌리고 별도의 채점 에이전트로 검사해, 지어낸 사실 0건을 유지하면서 분량을 66~89%로 맞췄다고 한다. AI에게는 사용자가 적은 메모와 요약만 넘기고 이름·연락처는 보내지 않았다.
