---
id: ai-tools-0780
domain: ai-tools
claim: 챗봇 지시문(시스템 프롬프트)을 고친 덕분에 답이 좋아졌는지 알려면, 다른 조건은 그대로 두고 같은 모델에 같은 시험 질문을 넣어 고치기
  전과 후를 비교해야 한다.
status: candidate
evidence: consensus
confidence: 0.7
sources:
- url: https://www.anthropic.com/research/building-strong-safety-evaluations
  author: Anthropic Engineering
  seen: '2026-11-25'
  quote: need a design that varies one variable at a time
  source: Anthropic Engineering 블로그
first_seen: '2026-11-25'
last_confirmed: '2026-11-25'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 챗봇
- 평가
- 시스템프롬프트
- 비교시험
---
모델 A와 모델 B의 점수 차이만 봐서는 점수가 왜 달라졌는지 알 수 없습니다. 특정 변경이 효과가 있었는지 알려면 한 번에 한 가지만 바꿔야 합니다. 예를 들어 같은 모델과 같은 질문 목록을 쓰고 지시문만 바꾼 두 버전을 나란히 시험합니다. 지시문과 모델을 동시에 바꾸면 어느 쪽 때문에 좋아졌는지 가려낼 수 없습니다.
