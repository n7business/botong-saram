---
id: ai-tools-0150
domain: ai-tools
claim: A2A의 JSON-RPC 오류는 HTTP 200 안에 실려 오므로, 상태 코드만 보는 모니터링 대신 JSON-RPC 오류 코드까지 기록하고
  확인해야 실패를 놓치지 않는다.
status: verified
evidence: observed
confidence: 0.7
sources:
- url: https://yozm.wishket.com/magazine/detail/4024/
  author: 조훈(Hoon Jo)
  seen: '2026-11-05'
  quote: 상태 코드만 보는 모니터링은 이를 성공으로 집계하게 되는데
  source: 요즘IT
first_seen: '2026-11-05'
last_confirmed: '2026-11-05'
review_by: '2026-12-05'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- A2A
- 모니터링
- 오류 처리
verified_by: 실무자 실측(단일 출처)
---
지원하지 않는 메서드를 호출해도 HTTP는 200으로 오고, 오류는 그 응답 안에 실립니다. 상태 코드만 보면 이런 실패가 성공으로 집계됩니다. agentgateway를 쓰면 액세스 로그에 호출한 메서드와 결과, JSON-RPC 오류 코드가 남습니다. 오류 형식은 바인딩마다 달라 REST는 404에 다른 형식으로 오므로 따로 처리합니다. 완료된 태스크를 취소하면 스펙이 정한 -32002가 아니라 내부 오류 코드인 -32603이 오니, 서버 장애로 오해해 재시도하지 않도록 합니다.
