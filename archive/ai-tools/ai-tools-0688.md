---
id: ai-tools-0688
domain: ai-tools
claim: 요금표처럼 표로 된 문서를 AI에 넣었다면 칸 사이의 관계가 보존됐는지 확인해야 한다. 일반 OCR은 글자와 숫자만 뽑아 '어느 강좌의
  어느 요금인지' 같은 연결이 끊어지고, 그러면 어떤 AI도 그 관계를 되찾지 못하기 때문이다.
status: candidate
evidence: anecdote
confidence: 0.7
sources:
- url: https://www.youtube.com/watch?v=bRzpzqedDSk
  author: 최승기 (테디노트 TeddyNote, AutoRAG Community Meetup 2026)
  seen: '2026-11-21'
  quote: 문서에는 문서의 구조 자체가 정보가 된다
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
- 표인식
- OCR
- 문서파싱
---
발표 예시에서 이용 요금표를 일반 OCR로 읽었더니 숫자와 글자는 나왔지만, '필라테스 기초반 화·목 청소년 요금 7만 원'에서 '필라테스'가 멀리 떨어져 나왔습니다. 사람은 표를 보면 알 수 있어도, 이렇게 뽑힌 텍스트만으로는 AI가 관계를 알아낼 수 없습니다. 문서에서는 표의 구조 자체가 정보입니다. 가격표·수수료표처럼 표가 핵심인 문서는 변환 결과를 열어 행과 열이 표 형태로 남았는지 확인하세요.
