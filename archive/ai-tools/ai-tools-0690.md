---
id: ai-tools-0690
domain: ai-tools
claim: 글자가 없는 현장 사진도 AI 검색에 걸리게 하려면 이미지를 내용 설명 텍스트로 바꿔 주는 VLM 기반 파서로 다시 색인해야 한다. 글자만
  읽는 일반 OCR로는 사진 속 정보가 검색되지 않기 때문이다.
status: candidate
evidence: anecdote
confidence: 0.6
sources:
- url: https://www.youtube.com/watch?v=bRzpzqedDSk
  author: 최승기 (테디노트 TeddyNote, AutoRAG Community Meetup 2026)
  seen: '2026-11-21'
  quote: 사진 속 정보도 검색할 수 있게 되어 검색 범위가 크게 넓어진다.
  source: 테디노트 TeddyNote
first_seen: '2026-11-21'
last_confirmed: '2026-11-21'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- RAG
- VLM
- 이미지검색
- 현장사진
---
일반 OCR은 이미지 속 글자만 인식합니다. VLM 기반 모델은 '콘크리트 벽면의 균열과 흩어진 돌'처럼 사진 내용을 문장으로 설명해 줍니다. 발표 데모에서는 사진 문서를 VLM 파서로 다시 파싱해 재색인하자, 원래 텍스트로는 없던 '벽 균열'이 검색됐습니다. 현장 사진이나 하자 사진을 많이 보관하는 업종이라면 이 방식을 시험해 볼 만합니다.
