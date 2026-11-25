---
id: ai-tools-0822
domain: ai-tools
claim: 현장 사진처럼 글자가 없는 이미지도 AI 검색으로 찾고 싶다면 VLM 기반 파서로 사진 내용을 글로 설명하게 해서 함께 저장해야 한다.
  일반 OCR은 글자만 읽어서 사진 속 정보가 검색되지 않지만, 사진을 설명문으로 바꿔 저장한 데모에서는 사진에 글자로 없던 '벽 균열'로 검색해도
  그 사진이 찾아졌다.
status: candidate
evidence: anecdote
confidence: 0.6
sources:
- url: https://www.youtube.com/watch?v=5HeF1R8J2Us
  author: 테디노트 TeddyNote (최송기 발표, 업스테이지)
  seen: '2026-11-25'
  quote: 원래 사진에 텍스트로 없던 '벽 균열'을 검색했는데 잘 찾아졌다.
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
- 이미지검색
- VLM
- 현장사진
---
일반 OCR은 이미지 속 글자만 뽑기 때문에 하자 사진이나 현장 사진은 검색 대상에서 빠진다. VLM 기반 파서는 '콘크리트 벽면의 균열과 흩어진 돌'처럼 사진 내용을 문장으로 설명해 준다. 이 설명문을 문서와 함께 저장(인덱싱)하면 사진도 말로 검색할 수 있다. 이미 저장해 둔 사진 문서는 새 파서로 다시 변환한 뒤 저장도 새로 해야 반영된다.
