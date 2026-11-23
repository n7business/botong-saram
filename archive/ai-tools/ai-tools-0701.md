---
id: ai-tools-0701
domain: ai-tools
claim: AI 답변을 AI에게 채점시킬 때는 답변을 만든 모델과 다른 모델을 채점에 쓰고, 채점 AI에게는 시험 설계 메모 없이 대화 내용만 보여
  줘야 한다. AI는 자기가 쓴 글을 알아보고 더 좋게 평가하는 경향이 있기 때문이다.
status: candidate
evidence: consensus
confidence: 0.65
sources:
- url: https://www.anthropic.com/research/building-strong-safety-evaluations
  author: Anthropic Engineering
  seen: '2026-11-23'
  quote: model graders have been shown to recognize and favor their own outputs.
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
- 평가
---
클로드로 만든 챗봇의 답은 다른 회사 모델로 채점하거나 그 반대로 하는 식으로, 만든 모델과 채점하는 모델을 나눕니다. 채점 AI에게 '이건 사기 유도 시나리오다' 같은 설계 정보까지 주면 그 정보 때문에 판단이 기울 수 있으니 대화 기록만 넘겨야 합니다.
