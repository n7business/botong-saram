---
id: ai-tools-0201
domain: ai-tools
claim: 크롤러나 API 호출에서 429를 받으면 요청을 줄이고, 응답에 Retry-After가 있으면 안내된 시간만큼 기다린 뒤 다시 보내야
  한다.
status: candidate
evidence: consensus
confidence: 0.75
sources:
- url: https://www.youtube.com/watch?v=bBXtm7_9F4U
  author: 양실장 (양실장의 바이브코딩대학)
  seen: '2026-11-06'
  quote: 크롤러를 무지막지하게 돌리다 429를 받으면 자중해야 한다.
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
- 크롤러
- 레이트리밋
- '429'
- Retry-After
---
429 Too Many Requests는 분당·초당·일당처럼 정해진 기간에 허용 횟수(예: 초당 10회)를 넘겼다는 뜻입니다. 크롤러를 과하게 돌리다 이 코드를 받으면 호출 속도를 낮춰야 합니다. Retry-After 헤더는 다음 요청까지 기다릴 시간을 안내합니다. 영상 업로드처럼 통신 비용이 큰 기능은 기준이 더 촘촘할 수 있어 기능마다 한도가 다를 수 있습니다.
