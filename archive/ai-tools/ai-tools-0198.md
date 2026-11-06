---
id: ai-tools-0198
domain: ai-tools
claim: API 메소드 이름만 보고 동작을 넘겨짚지 말아야 하며, 컨벤션에 어긋나게 개발된 서버에서는 DELETE를 보내도 생성처럼 동작할 수
  있다.
status: candidate
evidence: consensus
confidence: 0.65
sources:
- url: https://www.youtube.com/watch?v=bBXtm7_9F4U
  author: 양실장 (양실장의 바이브코딩대학)
  seen: '2026-11-06'
  quote: 컨벤션에 어긋나게 개발하면 DELETE를 보내도 생성처럼 동작할 수 있다.
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
- 메소드
- 컨벤션
- 바이브코딩
---
GET·POST·PUT·PATCH·DELETE는 어떤 작업이 필요한지 표시하는 약속일 뿐, 그 메소드를 썼다고 서버가 반드시 그렇게 동작하지는 않습니다. 컨벤션을 지키면 유지보수와 여러 명의 공동 작업이 쉬워지지만, 어긋나게 개발되면 DELETE가 생성처럼 동작할 수도 있습니다. AI가 만든 API나 처음 쓰는 API는 메소드 이름만 믿지 말고 실제 결과를 확인합니다.
