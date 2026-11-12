---
id: ai-tools-0200
domain: ai-tools
claim: 배포한 서비스에서 502가 뜨면 재배포 중이거나 배포가 온전히 되지 않았는지, 503이 뜨면 과부하인지부터 확인하면 서버 오류의 원인을
  좁힐 수 있다.
status: candidate
evidence: consensus
confidence: 0.7
sources:
- url: https://www.youtube.com/watch?v=bBXtm7_9F4U
  author: 양실장 (양실장의 바이브코딩대학)
  seen: '2026-11-06'
  quote: 재배포 중이거나 배포가 온전히 되지 않았을 때 뜬다.
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
- 배포
- 서버오류
- 바이브코딩
---
5xx는 서버 쪽 오류이며 알아 둘 코드는 두세 개입니다. 500은 서버가 요청을 처리하다 실패한 경우로, 개발 중에도 사용 중에도 날 수 있습니다. 502는 웹서버가 요청을 어디로 보낼지 모르는 상태로, 재배포 중이거나 배포가 온전히 되지 않았을 때 뜹니다. 503은 과부하 등으로 일시적으로 처리할 수 없는 상태로, 공격을 받거나 여러 명이 크롤러를 과하게 쏠 때 나올 수 있습니다.
