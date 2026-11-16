---
id: ai-tools-0601
domain: ai-tools
claim: AI에게 검증 결과를 보고받을 때는 '통과'라는 판정만 받지 말고 무엇을 어디까지 확인했고 무엇이 남았는지 나눠 적게 해야 하며, 특히
  저장·삭제를 가짜 응답(mock)으로 검사했다면 실제 서버에 저장됐는지는 확인되지 않은 것으로 봐야 한다.
status: candidate
evidence: anecdote
confidence: 0.65
sources:
- url: https://yozm.wishket.com/magazine/detail/4040/
  author: 김의중
  seen: '2026-11-17'
  quote: 실제 서버에 데이터가 저장되거나 삭제되는 것까지 확인했다는 뜻은 아닙니다.
  source: 요즘IT
first_seen: '2026-11-17'
last_confirmed: '2026-11-17'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- AI코딩
- 검증
- mock
- 보고
---
AI 검증 보고에서는 판정을 한 줄로 먼저 받으세요. 그다음에 확인한 항목, 사람이 확인할 체크리스트, 스크린샷이나 동작 녹화를 차례로 정리하게 하면 검토가 빨라집니다. 실제 데이터를 건드리지 않으려고 생성·삭제 요청을 가짜 응답으로 대신하는 경우가 있습니다. 이때 확인된 것은 요청 내용과 그 뒤의 화면 동작까지입니다. 데이터가 실제로 저장되거나 삭제됐는지는 따로 확인해야 합니다. 자동 검사가 어디서 멈췄는지 알아야 사람이 그다음 확인을 이어갈 수 있습니다.
