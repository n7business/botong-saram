---
id: ai-tools-0500
domain: ai-tools
claim: AI가 구현과 단위 테스트를 함께 만들어 테스트가 통과했더라도 그것만으로 맞다고 판단하지 말고, 테스트의 기대 결과가 실제 업무와 맞는지
  따로 확인해야 하는데, 둘 다 같은 명세를 바탕으로 만들었다면 명세의 잘못된 조건을 함께 받아들이기 때문이다.
status: candidate
evidence: anecdote
confidence: 0.75
sources:
- url: https://yozm.wishket.com/magazine/detail/4036/
  author: 김동혁
  seen: '2026-11-12'
  quote: 구현과 테스트가 같은 명세 내용을 바탕으로 작성됐다면, 잘못된 조건을 둘 다 받아들일 수 있습니다.
  source: 요즘IT
first_seen: '2026-11-12'
last_confirmed: '2026-11-12'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 바이브코딩
- 단위테스트
- 명세
- 코드검토
---
AI 에이전트에 명세를 넘기면 코드와 단위 테스트가 함께 나와 일이 다 끝난 것처럼 보입니다. 하지만 구현과 테스트가 같은 명세를 바탕으로 만들어졌다면, 명세가 틀렸을 때 둘 다 똑같이 틀리고 테스트는 그대로 통과합니다. 테스트가 통과했는지만 보지 말고, 기대 결과를 어디서 가져왔는지와 실제 업무와 맞는지를 확인하세요. 이상한 조건이 보이면 AI에게 다시 만들라고 하기 전에, 내가 넘긴 명세부터 업무를 아는 사람과 함께 살펴봐야 합니다.
