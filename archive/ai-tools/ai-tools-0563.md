---
id: ai-tools-0563
domain: ai-tools
claim: AI에게 외부 서비스(API)를 연결하는 코드를 맡길 때는 실제 서버 응답을 먼저 받아 두고, 그 형식대로 코드와 가짜 응답(mock)을
  만들게 해야 한다. 이렇게 하지 않으면 AI가 추측한 형식으로 코드와 mock을 함께 만들어, 테스트는 통과하는데 실제 서버에 연결하면 동작하지
  않는다.
status: candidate
evidence: anecdote
confidence: 0.7
sources:
- url: https://yozm.wishket.com/magazine/detail/4039/
  author: 요즘IT
  seen: '2026-11-14'
  quote: AI가 실제 응답을 보지 않고, 추측한 데이터 형식으로 구현 코드와 mock을 함께 만들었습니다.
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
- API
- 테스트
- mock
---
AI가 실제 응답을 보지 않고 데이터 형식을 추측하면, 구현 코드와 테스트용 mock에 같은 잘못이 들어갑니다. 둘이 서로 어긋나지 않으니 테스트는 통과하지만 실제 서버에 붙이면 화면이 제대로 움직이지 않습니다. 한 개발자는 이 일을 겪은 뒤 '실제 응답부터 캡처'를 새 API 체크리스트의 첫 항목으로 올렸습니다. mock으로 통과한 테스트는 코드의 의도를 확인할 뿐, 실제 상황을 확인하지는 않는다는 점을 기억하세요.
