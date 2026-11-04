---
id: ai-tools-0145
domain: ai-tools
claim: 오래 걸리지 않고 중간 상태 관리도 필요 없는 호출이면 MCP로 충분하고, A2A는 호출할 에이전트가 5군데쯤 되거나 외부 업체가 운영하는
  에이전트일 때 도입을 검토한다.
status: verified
evidence: observed
confidence: 0.7
sources:
- url: https://yozm.wishket.com/magazine/detail/4024/
  author: 조훈(Hoon Jo)
  seen: '2026-11-05'
  quote: 호출한 일이 오래 걸리지 않고 중간에 상태를 확인하거나 관리할 필요도 없다면 MCP로 충분합니다.
  source: 요즘IT
- url: https://yozm.wishket.com/magazine/detail/4025/
  author: 조훈(Hoon Jo)
  seen: '2026-11-05'
  quote: 호출할 곳이 5군데쯤 되거나 외부 업체가 운영하는 에이전트라면
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
- MCP
- 프로토콜 선택
verified_by: 실무자 실측(단일 출처)
---
A2A로 얻는 것은 맡긴 일의 진행 확인과 취소에 대한 규약입니다. 규약이 정해져 있어 상대 에이전트가 바뀌어도 쓰던 클라이언트 코드를 그대로 쓸 수 있습니다. 그 대신 응답 바이트가 늘고, 순수 HTTP보다 호출당 1.2~2.1ms가 더 걸렸습니다. 사내 에이전트 1개만 호출한다면 이 이점은 의미가 없습니다. 시간을 들여 일하다가 중간에 되묻거나 거절할 수 있는 에이전트가 상대일 때 A2A가 의미를 가집니다.
