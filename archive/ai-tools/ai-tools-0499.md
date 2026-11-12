---
id: ai-tools-0499
domain: ai-tools
claim: AI가 만든 코드를 검토할 때는 이메일 주소처럼 외부 정보가 들어가는 값이 어디서 오는지, 지금 계정 권한으로 정말 조회할 수 있는지부터
  확인해야 하는데, AI는 권한이 없는 정보도 조회할 수 있다고 가정하거나 값을 코드에 직접 박아 넣어 완성된 것처럼 보이게 만들기 때문이다.
status: candidate
evidence: anecdote
confidence: 0.7
sources:
- url: https://yozm.wishket.com/magazine/detail/4036/
  author: 김동혁
  seen: '2026-11-12'
  quote: AI는 필요한 정보를 조회할 수 있다는 가정으로 구현을 이어 가거나, 하드코딩으로 처리를 진행하려 했습니다.
  source: 요즘IT
first_seen: '2026-11-12'
last_confirmed: '2026-11-12'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 바이브코딩
- 코드검토
- 권한
- 하드코딩
- 에이전트
---
AI 코딩 에이전트는 필요한 정보를 얻을 방법이 정해지지 않았어도, 조회할 수 있다고 가정하거나 값을 코드에 직접 적어 넣고(하드코딩) 구현을 이어 갑니다. 이렇게 하면 발송·처리 단계까지는 돌아가는 것처럼 보이지만, 실제 운영에서는 그 정보를 얻을 수 없어 기능이 완성되지 않은 채로 남습니다. 검토할 때는 외부 값이 들어가는 부분마다 '이 값은 어디서 오는가, 내 계정 권한으로 조회할 수 있는가, 고정해서 써도 되는가'를 확인하세요. 코드가 돌아간다는 것만으로 완성됐다고 판단하지 마세요.
