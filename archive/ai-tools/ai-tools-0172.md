---
id: ai-tools-0172
domain: ai-tools
claim: Jev로 한 리뷰에 감정·열광도·배송 지연 여부를 한 번에 물을 때는 각 질문이 서로의 답을 보지 않으므로, 앞 답을 전제로 하지 않게
  질문마다 독립적으로 써야 한다.
status: candidate
evidence: consensus
confidence: 0.55
sources:
- url: https://www.youtube.com/watch?v=6oZC4Ed2vnY
  author: 노마드 코더 Nomad Coders
  seen: '2026-11-06'
  quote: 각 질문은 서로의 답을 보지 않고 독립적으로 한꺼번에 실행된다고 합니다.
  source: 노마드 코더 Nomad Coders
first_seen: '2026-11-06'
last_confirmed: '2026-11-06'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- Jev
- 다중질문
- 리뷰분석
- 자동분류
---
Jev에는 같은 리뷰에 감정, 열광도, 배송 지연 여부처럼 여러 질문을 동시에 던질 수 있습니다. 각 질문은 서로의 답을 보지 않고 독립적으로 한꺼번에 실행됩니다. 따라서 '앞에서 부정으로 판정했다면'처럼 다른 질문의 답에 기대는 문장은 쓰지 않습니다. 응답 방식은 choice, score, 확률형뿐이므로 질문도 이 형식에 맞춥니다.
