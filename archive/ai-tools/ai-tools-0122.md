---
id: ai-tools-0122
domain: ai-tools
claim: 백업·개수 집계처럼 판단이 필요 없는 반복 작업은 AI 모델을 붙이지 말고 모델 없는 스크립트 예약으로 돌려야 모델 사용 비용이 0이
  된다.
status: candidate
evidence: anecdote
confidence: 0.75
sources:
- url: https://www.youtube.com/watch?v=k_n8fmTt8Ck
  author: 샘 호트만 (@ai.sam_hottman)
  seen: '2026-11-03'
  quote: 판단이 필요 없는 일(화자의 경우 GitHub 백업)은 모델 없는 스크립트로 돌려 비용을 없앤다.
  source: '샘 호트만 : AI 엔지니어의 시선 (@ai.sam_hottman)'
first_seen: '2026-11-03'
last_confirmed: '2026-11-03'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 자동화
- 비용절감
- 크론
- 스크립트
---
예약 작업을 모두 AI 에이전트로 돌리면 실행할 때마다 모델 사용량이 나갑니다. GitHub 백업이나 주간 개수 집계처럼 판단이 필요 없는 일은 일반 스크립트로 만들어 크론에 올리세요. 웹훅도 모델 없이 그대로 전달하는 방식을 고르면 비용 없이 1초 안에 끝납니다. AI는 분류·요약·초안처럼 판단이 필요한 단계에만 붙입니다.
