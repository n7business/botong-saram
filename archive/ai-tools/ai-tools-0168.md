---
id: ai-tools-0168
domain: ai-tools
claim: AI 답을 프로그램에서 바로 쓰는 분류 자동화에는 'A, B, C로만 답하라'는 지시에 기대지 말고 허용값을 정한 구조화된 출력(JSON
  스키마)을 써야, 군말이 섞여 처리가 깨지는 일을 줄일 수 있다.
status: candidate
evidence: consensus
confidence: 0.7
sources:
- url: https://www.youtube.com/watch?v=6oZC4Ed2vnY
  author: 노마드 코더 Nomad Coders
  seen: '2026-11-06'
  quote: 모델이 'Certainly, the answer is…'처럼 그냥 말을 늘어놓을 수 있어 깨지기 쉽다고 합니다.
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
- 구조화된출력
- JSON스키마
- 자동분류
- 프롬프트
---
리뷰 긍정/부정 판정이나 모더레이션처럼 결과를 사람이 아니라 프로그램이 받는 일에는 문단이 아니라 바로 쓸 값이 필요합니다. 프롬프트로 'A, B, C로만 답하라'고 지시해도 모델이 'Certainly, the answer is…'처럼 말을 덧붙일 수 있어 깨지기 쉽습니다. 이럴 때는 필드와 허용값을 정한 JSON 스키마를 함께 넘깁니다. 예를 들어 리뷰 감정을 한 단어로 받으려면 필드 하나에 허용값 세 개짜리 스키마를 만듭니다.
