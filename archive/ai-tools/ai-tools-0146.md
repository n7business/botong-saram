---
id: ai-tools-0146
domain: ai-tools
claim: A2A 에이전트 카드에 인증 방식을 적어도 공식 SDK 기본 구성은 검사하지 않으므로, 인증과 인가는 앱이나 별도 계층에서 직접 걸어야
  한다.
status: verified
evidence: observed
confidence: 0.8
sources:
- url: https://yozm.wishket.com/magazine/detail/4024/
  author: 조훈(Hoon Jo)
  seen: '2026-11-05'
  quote: 에이전트 카드에 인증 방식을 적어 두어도 SDK 기본 구성은 그것을 검사하지 않으니
  source: 요즘IT
- url: https://yozm.wishket.com/magazine/detail/4024/
  author: 조훈(Hoon Jo)
  seen: '2026-11-05'
  quote: 인증과 인가 모두 앱이나 다른 계층이 담당해야 합니다.
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
- 에이전트 보안
- 인증
verified_by: 실무자 실측(단일 출처)
---
공식 파이썬 SDK 기본 구성으로 만든 서버에 자격 증명 없이 호출해도, 틀린 키를 넣어 호출해도 200이 돌아왔습니다. 에이전트 카드의 인증 항목은 이런 방식으로 인증해서 오라고 알려 주는 선언일 뿐, 서버가 검사해 주는 장치가 아닙니다. agentgateway v1.5.0을 앞에 두어도 A2A 요청의 인가는 판단하지 않아 이 문제가 해결되지 않습니다. 배포 전에 자격 증명 없는 호출과 틀린 키 호출을 직접 보내 실제로 막히는지 확인합니다.
