---
id: ai-tools-0848
domain: ai-tools
claim: AI 코딩 도구가 작업을 끝내면 화면만 눌러 보고 끝내지 말고, Git diff로 어떤 파일의 어느 줄이 추가되거나 삭제됐는지 확인해야
  한다. 이때 API 키나 비밀번호가 코드에 그대로 적혀 있지 않은지도 함께 봐야 한다.
status: candidate
evidence: consensus
confidence: 0.7
sources:
- url: https://www.youtube.com/watch?v=DwuZ5Rrj8Xo
  author: 양실장 (양실장의 바이브코딩대학)
  seen: '2026-11-28'
  quote: 화면만 대충 눌러 보지 말고, diff로 어떤 파일의 어떤 줄이 추가·삭제됐는지
  source: 양실장의 바이브코딩대학 (@VibecodingUniversity)
first_seen: '2026-11-28'
last_confirmed: '2026-11-28'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 바이브코딩
- Git
- 검증
- 보안
---
화자는 AI 작업 결과를 diff로 확인하는 습관이 시스템을 통제하는 핵심이라고 강조합니다. 화면이 잘 돌아가 보여도 시키지 않은 파일이 바뀌었을 수 있습니다. 큰 수정을 맡길 때는 잘 돌던 코드를 보존하도록 브랜치를 따로 만들어 작업시키고, 끝나면 diff를 확인한 뒤 합치세요. diff를 볼 때 DB 비밀번호, 결제 키, LLM API 키 같은 값이 코드에 문자열로 적혀 있지 않은지도 확인해야 합니다.
