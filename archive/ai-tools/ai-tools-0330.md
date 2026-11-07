---
id: ai-tools-0330
domain: ai-tools
claim: AI가 만든 테스트가 전부 통과했다는 보고를 받으면 요구사항별로 수용 조건·테스트·코드가 연결된 추적표부터 확인해야, 아예 구현되지 않은
  기능을 놓치지 않는다.
status: verified
evidence: observed
confidence: 0.8
sources:
- url: https://yozm.wishket.com/magazine/detail/4032/
  author: 요즘IT (꼼비 사례)
  seen: '2026-11-07'
  quote: 요구사항 명세 40개 가운데 코드에 실제로 들어간 건 25개였습니다.
  source: 요즘IT
- url: https://yozm.wishket.com/magazine/detail/4032/
  author: 요즘IT (꼼비 사례)
  seen: '2026-11-07'
  quote: 요즘은 전체 PASS 보고를 받으면 요구사항 추적표를 먼저 연다.
  source: 요즘IT
first_seen: '2026-11-07'
last_confirmed: '2026-11-07'
review_by: '2026-12-07'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 검증
- 테스트
- 요구사항
- 완료보고
verified_by: 실무자 실측(단일 출처)
---
AI가 작성한 테스트는 이미 구현된 동작만 검사할 수 있어서, 빠진 기능은 어디서도 실패로 잡히지 않습니다. 사례에서는 테스트가 전부 통과해 개발 완료 보고가 나왔지만, 요구사항 명세 40개 중 코드에 실제로 들어간 것은 25개였습니다. 이후 작성자는 요구사항마다 수용 조건, 테스트, 코드의 연결 위치를 적은 추적표를 AI에게 만들게 하고, 빠진 연결은 직접 확인합니다. 같은 시나리오가 아홉 번 실패하면 AI가 더 붙잡지 않고 로그와 판단 근거를 들고 사람에게 묻도록 정해 두기도 했습니다.
