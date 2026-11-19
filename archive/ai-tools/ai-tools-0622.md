---
id: ai-tools-0622
domain: ai-tools
claim: 고객 응대용 AI 챗봇을 시험할 때는 질문 하나씩만 던져 보지 말고 여러 번 주고받는 대화로 시험해야 한다. 첫 질문에는 제대로 답한
  AI도 대화가 이어지면서 다섯 번째쯤에는 부적절하게 답할 수 있기 때문이다.
status: verified
evidence: observed
confidence: 0.75
sources:
- url: https://www.anthropic.com/research/building-strong-safety-evaluations
  author: Anthropic
  seen: '2026-11-20'
  quote: a model that handles the first message well may respond inappropriately by
    the fifth.
  source: Anthropic Engineering 블로그
first_seen: '2026-11-20'
last_confirmed: '2026-11-20'
review_by: '2026-12-20'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 챗봇
- 테스트
- 멀티턴
- 고객응대
verified_by: 실무자 실측(단일 출처)
---
챗봇을 고객에게 열기 전에 질문 하나에 답 하나를 받는 방식으로만 시험하면 거의 다 통과한 것처럼 보입니다. 앤트로픽 집계로는 최근 모델들이 한 번만 묻는 안전 시험에서 94~98%를 통과했지만, 여러 번 주고받는 시험에서는 결과가 훨씬 넓게 갈렸습니다. 실제 사용자는 조금씩 요구를 키우거나 앞에서 한 말을 바꿔 다시 묻기 때문에, 문제가 되는 답은 대화 중간에 나옵니다. 환불 요구를 점점 키우는 고객이나 거절당한 뒤 다른 핑계로 다시 묻는 고객처럼 실제로 있었던 문의를 바탕으로 5~10번 주고받는 시나리오를 만들고, 대화 전체에서 한 번이라도 잘못 답하면 실패로 처리하세요. 시나리오는 한 번 만들고 끝내지 말고 새 문의 유형이 보일 때마다 보태야 합니다.
