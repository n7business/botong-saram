---
id: ai-tools-0197
domain: ai-tools
claim: API 응답이 성공 코드로 왔다고 실제 처리가 성공했다고 믿지 말아야 하며, 상태 코드는 약속일 뿐이어서 성공 코드 뒤에 에러가 숨어
  있을 수 있다.
status: candidate
evidence: consensus
confidence: 0.7
sources:
- url: https://www.youtube.com/watch?v=bBXtm7_9F4U
  author: 양실장 (양실장의 바이브코딩대학)
  seen: '2026-11-06'
  quote: 즉 성공이라고 했는데 실제로 에러가 나 있을 수도 있어요.
  source: 양실장의 바이브코딩대학 (@VibecodingUniversity)
first_seen: '2026-11-06'
last_confirmed: '2026-11-06'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- API
- HTTP
- 상태코드
- 디버깅
- 바이브코딩
---
HTTP 상태 코드는 서버 개발자가 지키는 컨벤션이지 실제 상태를 보장하지 않습니다. 성공 코드가 왔는데 실제로는 에러가 났을 수 있고, 서버 오류인데 500이 아닌 다른 코드를 주도록 설정하는 것도 가능합니다. 바이브 코딩으로 만든 기능을 점검할 때는 코드 숫자만 보고 끝내지 말고 응답 본문과 실제 처리 결과까지 함께 확인합니다.
