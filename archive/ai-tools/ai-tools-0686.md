---
id: ai-tools-0686
domain: ai-tools
claim: 사내 문서로 AI 검색(RAG)을 만들 때 팩스·손글씨·사진 문서를 그대로 넣지 말고, 문서를 텍스트로 바꾼 파싱 결과부터 열어 제대로
  읽혔는지 확인해야 한다. 이 단계에서 잘못 읽힌 정보는 그대로 색인되어 검색과 답변까지 틀리게 만들기 때문이다.
status: candidate
evidence: anecdote
confidence: 0.7
sources:
- url: https://www.youtube.com/watch?v=bRzpzqedDSk
  author: 최승기 (테디노트 TeddyNote, AutoRAG Community Meetup 2026)
  seen: '2026-11-21'
  quote: 이 단계가 잘못되면 최고 성능의 LLM도 제대로 읽지 못한다.
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
- OCR
- 문서파싱
- 팩스
- 사내검색
---
AI 검색은 원본 문서를 AI가 읽을 수 있는 텍스트(보통 마크다운)로 바꾸는 파싱 단계를 먼저 거칩니다. 발표 예시에서는 기울어진 표와 팩스 잡티 때문에 휴대전화 번호가 '나누기 5678'로 나왔고, 이메일의 'com'은 '코인'으로 읽혔습니다. 이렇게 잘못 읽힌 내용은 그대로 색인되고, 성능이 가장 좋은 AI도 그 잘못된 정보를 바탕으로 답합니다. 시스템을 만들기 전에 실제 신청서·팩스 몇 건을 파싱해 보고, 전화번호·이메일·금액이 원본과 같은지 직접 대조해 보세요.
