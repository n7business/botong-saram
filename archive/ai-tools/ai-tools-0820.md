---
id: ai-tools-0820
domain: ai-tools
claim: 요금표처럼 표로 된 문서를 AI 검색에 넣을 때는 글자만 뽑는 일반 OCR을 쓰면 안 되고, 표 구조를 살려 변환하는 파서를 써야 한다.
  일반 OCR로 읽으면 '필라테스'와 '기초반 화목', '7만 원'이 서로 떨어져 나와서, 어떤 AI도 '필라테스 기초반 청소년 이용료가 7만 원'이라는
  관계를 찾을 수 없기 때문이다.
status: candidate
evidence: anecdote
confidence: 0.65
sources:
- url: https://www.youtube.com/watch?v=5HeF1R8J2Us
  author: 테디노트 TeddyNote (최송기 발표, 업스테이지)
  seen: '2026-11-25'
  quote: 문서에는 문서의 구조 자체가 정보가 된다
  source: 테디노트 TeddyNote
first_seen: '2026-11-25'
last_confirmed: '2026-11-25'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- RAG
- 표인식
- 문서파싱
- 마크다운
---
문서에서는 글자뿐 아니라 표의 행과 열, 즉 구조 자체가 정보다. 일반 OCR은 글자만 순서대로 뽑아서 표 머리글과 값의 관계를 잃어버린다. 가격표·요금표·수수료표처럼 칸끼리의 관계가 중요한 문서는 표를 마크다운 표 형태로 살려 주는 파서로 변환해야 한다. 변환한 뒤에는 표 한두 개를 열어 머리글과 값이 제대로 짝지어졌는지 직접 확인한다.
