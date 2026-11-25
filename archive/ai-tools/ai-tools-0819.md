---
id: ai-tools-0819
domain: ai-tools
claim: 손글씨 신청서나 팩스로 받은 서류를 AI 검색(RAG)에 넣을 때는 일반 OCR 결과를 그대로 넣지 말고, 전화번호·이메일 같은 칸이
  제대로 읽혔는지 먼저 확인해야 한다. 기울어진 표와 팩스 잡티 때문에 OCR이 휴대전화 번호를 '나누기 5678'로, 'com'을 '코인'으로
  읽은 사례가 있었고, 잘못 읽힌 내용은 그대로 저장돼 AI가 틀린 답을 내놓기 때문이다.
status: candidate
evidence: anecdote
confidence: 0.6
sources:
- url: https://www.youtube.com/watch?v=5HeF1R8J2Us
  author: 테디노트 TeddyNote (최송기 발표, 업스테이지)
  seen: '2026-11-25'
  quote: OCR이 휴대전화 번호를 '나누기 5678'로, 이메일 'com'을 '코인'으로 잘못 읽는다.
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
- OCR
- 문서파싱
- 손글씨
- 팩스
---
AI가 문서를 검색해 답하게 하려면 먼저 문서를 AI가 읽을 수 있는 글(보통 마크다운)로 바꾸는 파싱 단계를 거친다. 이 단계에서 틀리면 아무리 좋은 AI 모델을 써도 틀린 정보로 답한다. 손으로 써서 팩스로 보낸 문서는 기울어진 표와 점 잡티 때문에 일반 OCR이 숫자와 영문을 엉뚱하게 읽는 일이 잦다. 이런 서류는 변환 결과를 몇 건 뽑아 원본과 대조해 보고, 틀린 곳이 많으면 칸의 의미까지 보고 글자를 바로잡는 VLM(이미지를 읽는 AI) 기반 파서를 쓰는 편이 낫다. 다만 외부 API 파서를 쓰면 고객 서류가 외부 서버로 나가므로, 고객 자료라면 사전 동의를 받거나 내 컴퓨터에서 돌아가는 변환 도구를 써야 한다.
