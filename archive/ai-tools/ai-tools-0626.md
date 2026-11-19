---
id: ai-tools-0626
domain: ai-tools
claim: AI 모델이나 프롬프트를 바꿀지 시험으로 정할 때는 질문 몇 개를 한 번씩만 돌려 보고 판단하지 말고, 같은 질문을 여러 번 돌려 결과가
  얼마나 흔들리는지 함께 봐야 한다. 몇 %p 차이는 우연일 수 있기 때문이다.
status: verified
evidence: observed
confidence: 0.7
sources:
- url: https://www.anthropic.com/research/building-strong-safety-evaluations
  author: Anthropic
  seen: '2026-11-20'
  quote: plan to run each test case several times and report the spread.
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
- 모델선택
- 테스트
- 통계
verified_by: 실무자 실측(단일 출처)
---
AI는 같은 질문에도 매번 조금씩 다르게 답하므로 몇 번만 돌려 본 결과로는 어느 쪽이 나은지 알 수 없습니다. 앤트로픽은 Claude Opus 5와 Opus 5.5가 한 시험에서 98%와 94%로 차이 났지만 통계적으로 의미 있는 차이가 아니어서 어느 쪽이 낫다고 결론 내리지 않았습니다. 두 모델을 비교할 때는 같은 질문 묶음에 둘 다 돌려 문항별로 비교하고, 각 문항을 여러 번 돌리세요. 무엇을 보고 어느 정도 차이가 나야 바꿀지도 결과를 보기 전에 미리 적어 두는 편이 좋습니다.
