---
id: ai-tools-0704
domain: ai-tools
claim: 챗봇이 시험 질문을 거의 다 통과한다면 안전하다고 결론 내리지 말고, 그 시험은 예전에 고친 문제가 다시 생기지 않았는지 확인하는 용도로만
  쓰고 더 길고 자연스러운 대화로 된 어려운 시험을 새로 만들어야 한다.
status: verified
evidence: observed
confidence: 0.6
sources:
- url: https://www.anthropic.com/research/building-strong-safety-evaluations
  author: Anthropic Engineering
  seen: '2026-11-23'
  quote: the single-turn tasks are saturated, and are therefore useful mainly as regression
    checks
  source: Anthropic Engineering 블로그
first_seen: '2026-11-23'
last_confirmed: '2026-11-23'
review_by: '2026-12-23'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 챗봇
- 평가
- 시험난이도
verified_by: 실무자 실측(단일 출처)
---
Anthropic의 질문 한 번짜리 안전 시험은 최근 모델 모두 94~98% 통과해, 모델 사이의 차이를 거의 가려내지 못했습니다. 반면 여러 번 주고받는 시험에서는 점수가 훨씬 넓게 갈렸습니다. 시험을 어렵게 만들 때는 함정 문제를 넣지 말고, 대화를 더 길게 하거나 요청을 더 은근하게 하거나 실제 손님처럼 자연스럽게 쓰는 방식으로 바꿔야 합니다.
