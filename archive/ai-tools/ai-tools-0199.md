---
id: ai-tools-0199
domain: ai-tools
claim: 바이브 코딩 결과물에서 4xx 오류가 나면 400은 요청 형식, 401은 인증, 403은 권한, 404는 주소 문제로 나눠 보면 원인을
  찾을 범위를 좁힐 수 있다.
status: candidate
evidence: consensus
confidence: 0.75
sources:
- url: https://www.youtube.com/watch?v=bBXtm7_9F4U
  author: 양실장 (양실장의 바이브코딩대학)
  seen: '2026-11-06'
  quote: 403 Forbidden은 로그인은 했지만 권한이 없는 경우로
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
- 오류해결
- 바이브코딩
---
4xx는 요청을 보낸 쪽의 오류입니다. 400은 요청 형식 자체가 이상한 경우이고, 401은 인증이 만료됐거나 로그인이 풀린 경우처럼 인증 문제입니다. 403은 로그인은 했지만 권한이 없는 경우로, 일반 사용자가 관리자 패널에 접근할 때가 대표적입니다. 404는 요청한 패스에 맞는 자원이나 기능이 없는 경우, 즉 주소를 잘못 찍은 경우입니다. 다만 상태 코드도 컨벤션이어서 실제 상태와 다를 수 있습니다.
