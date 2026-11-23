---
id: ai-tools-0700
domain: ai-tools
claim: AI에게 두 답변 중 더 나은 것을 고르게 할 때는 순서를 바꿔 한 번 더 물어야 하고, 길이가 긴 답변에 점수가 쏠리지 않는지 확인해야
  한다. 채점 AI는 먼저 보여 준 답과 긴 답을 더 좋게 보는 경향이 있기 때문이다.
status: candidate
evidence: consensus
confidence: 0.7
sources:
- url: https://www.anthropic.com/research/building-strong-safety-evaluations
  author: Anthropic Engineering
  seen: '2026-11-23'
  quote: Graders also favor longer responses and the first option they are shown in
    a pairwise comparison
  source: Anthropic Engineering 블로그
first_seen: '2026-11-23'
last_confirmed: '2026-11-23'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- LLM채점
- 편향
- 비교평가
---
두 모델이나 두 프롬프트의 답을 나란히 놓고 AI에게 고르게 하면, 내용과 상관없이 먼저 나온 쪽이나 더 긴 쪽이 이기는 경우가 생깁니다. 같은 비교를 A·B 순서를 뒤집어 다시 돌리고, 두 번 모두 같은 쪽이 이겼을 때만 결과를 믿습니다. 점수가 답변 길이와 함께 오르내리는지도 살펴봐야 합니다.
