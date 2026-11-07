---
id: ai-tools-0322
domain: ai-tools
claim: AI에게 '안 돼, 고쳐 줘'라고만 하지 말고 화면·서버·DB 중 어디서 문제가 생겼을지 나눠 생각해야, 어디부터 확인할지 알 수 있다.
status: candidate
evidence: consensus
confidence: 0.7
sources:
- url: https://www.youtube.com/watch?v=D-3Iojr7dIc
  author: 양실장의 바이브코딩대학 (@VibecodingUniversity)
  seen: '2026-11-07'
  quote: 버튼을 눌렀을 때 요청이 서버에 도달했는지, 도달했지만 어떤 규칙 때문에 거절됐는지
  source: 양실장의 바이브코딩대학 (@VibecodingUniversity)
first_seen: '2026-11-07'
last_confirmed: '2026-11-07'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 바이브코딩
- 디버깅
- API
- 웹 구조
---
웹 서비스는 사용자가 보는 화면, 요청을 받아 비즈니스 규칙을 처리하는 서버, 정보를 저장하는 DB로 나눠 볼 수 있다. 예약 버튼을 눌렀는데 목록에 안 보인다면 요청이 서버에 도달했는지부터 따진다. 이어서 도달했지만 규칙 때문에 거절됐는지, DB에는 저장됐는데 목록에만 안 보이는지 구분한다. 요청과 응답은 브라우저에서 우클릭 → 검사 → Network 탭을 열고 새로고침하면 볼 수 있다. 이 구조를 아는 목적은 바로 정답을 찾는 것이 아니라 확인할 순서를 아는 것이다.
