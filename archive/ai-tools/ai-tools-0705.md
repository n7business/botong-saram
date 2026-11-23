---
id: ai-tools-0705
domain: ai-tools
claim: 챗봇이 손님 말투나 요청 수위에 따라 어떻게 달라지는지 보려면, 말투와 수위를 묶어서 바꾸지 말고 수위마다 모든 말투를 하나씩 짝지어
  시험해야 한다. 한쪽으로 묶어 두면 어떤 요인 때문에 답이 달라졌는지 가려낼 수 없기 때문이다.
status: candidate
evidence: consensus
confidence: 0.55
sources:
- url: https://www.anthropic.com/research/building-strong-safety-evaluations
  author: Anthropic Engineering
  seen: '2026-11-23'
  quote: You should also vary the dimensions you care about independently.
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
- 챗봇
- 시험설계
- 변수통제
---
예를 들어 심각한 요청은 모두 다급한 말투로, 가벼운 요청은 모두 짜증 섞인 말투로만 시험하면, 챗봇이 실수했을 때 그 원인이 요청 수위인지 말투인지 알 수 없습니다. 수위 3단계 × 말투 3종류처럼 모든 조합을 만들어 시험합니다. 시스템 프롬프트를 바꾼 효과를 보고 싶을 때도 다른 조건은 그대로 두고 그것 하나만 바꿔 비교해야 합니다.
