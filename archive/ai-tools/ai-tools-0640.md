---
id: ai-tools-0640
domain: ai-tools
claim: AI 코딩 세션 하나에는 작업(이슈) 하나만 맡기고, 그 범위를 벗어난 작업은 시키지 말아야 한다. 한 세션에서 여러 기능을 다루면 예전
  논의와 새 결정이 뒤섞여, 왜 그렇게 정했는지 찾으려고 긴 대화를 거슬러 올라가야 하기 때문이다.
status: candidate
evidence: anecdote
confidence: 0.7
sources:
- url: https://yozm.wishket.com/magazine/detail/4043/
  author: 곰씨네 IT 블로그
  seen: '2026-11-20'
  quote: 각 세션은 이처럼 이슈 하나에 묶어서 열었고, 이슈 범위를 벗어나는 작업은 하지 않도록 했습니다.
  source: 요즘IT
first_seen: '2026-11-20'
last_confirmed: '2026-11-20'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 클로드코드
- 세션관리
- 이슈
---
화자는 처음에 한 세션에서 여러 기능을 개발했습니다. 그러다 요구사항이 바뀔 때마다 이전 논의와 새 결정이 섞였습니다. 이후에는 세션을 이슈 하나에 묶어 열고 범위 밖 작업은 하지 않게 했습니다. 큰 요구사항은 이슈 단위로 쪼갰고, 같은 이슈라도 실행 환경이나 배포 시점이 다르면 세션을 나눴습니다. 이렇게 하면 어떤 코드가 왜 만들어졌는지 확인할 때 해당 세션만 열어 보면 됩니다.
