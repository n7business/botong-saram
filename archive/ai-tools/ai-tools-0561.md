---
id: ai-tools-0561
domain: ai-tools
claim: AI가 '개발 완료, 테스트 전부 통과'라고 보고해도 끝난 것으로 보지 말고, 요구사항 목록을 한 줄씩 대조해 각 항목이 실제 코드에
  들어갔는지 확인해야 한다. AI는 이미 만든 기능만 테스트하므로, 빠진 기능은 어디에서도 실패로 드러나지 않기 때문이다.
status: candidate
evidence: anecdote
confidence: 0.75
sources:
- url: https://yozm.wishket.com/magazine/detail/4039/
  author: 요즘IT
  seen: '2026-11-14'
  quote: 요구사항 명세 40개 가운데 코드에 실제로 들어간 것은 25개였습니다.
  source: 요즘IT
first_seen: '2026-11-14'
last_confirmed: '2026-11-14'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- AI코딩
- 테스트
- 검수
- 요구사항
---
AI 에이전트가 만든 테스트는 대개 자기가 구현한 동작만 확인합니다. 그래서 요구사항 일부가 빠져도 테스트는 모두 통과합니다. 한 개발자의 사례에서는 테스트가 전부 통과하고 '개발 완료' 보고까지 나왔지만, 요구사항 40개 가운데 실제로 들어간 것은 25개였습니다. 통과 보고를 받으면 요구사항 원문의 각 항목이 테스트와 코드 어디로 이어지는지 적은 추적표를 AI에게 만들게 하세요. 연결이 빠진 항목은 사람이 직접 확인해야 합니다.
