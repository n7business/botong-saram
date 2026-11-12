---
id: ai-tools-0147
domain: ai-tools
claim: A2A 확장 에이전트 카드는 SDK 기본 구성에서 인증 없이도 내려가므로, 공개해도 되는 내용만 담아야 한다.
status: verified
evidence: observed
confidence: 0.75
sources:
- url: https://yozm.wishket.com/magazine/detail/4024/
  author: 조훈(Hoon Jo)
  seen: '2026-11-05'
  quote: 따라서 주소만 알면 누구나 받아 갈 수 있으니 공개해도 되는 내용만 담으시기 바랍니다.
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
- 정보 노출
verified_by: 실무자 실측(단일 출처)
---
스펙상 확장 카드는 인증된 요청에만 돌려주는 카드입니다. 그러나 SDK 기본 구성은 호출자의 신원을 확인하지 않아, 인증하지 않은 요청에도 공개 카드에 없는 스킬까지 그대로 돌려주었습니다. 인증을 통과한 상대에게만 보여 주려고 넣은 정보도 주소를 아는 누구에게나 나갈 수 있습니다. 민감한 내용은 빼 두고, 앱이나 앞단에 인증을 직접 건 뒤 인증 없이 호출해 실제로 막히는지 확인합니다.
