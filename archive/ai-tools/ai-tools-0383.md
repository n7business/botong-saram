---
id: ai-tools-0383
domain: ai-tools
claim: AI로 코드를 많이 만드는 소규모 팀이라도 Anthropic이 자체 버전 관리 시스템으로 옮겼다는 이유로 git을 버리지 말아야 하는데,
  그런 시스템은 초대형 모노레포에서나 의미가 있기 때문이다.
status: verified
evidence: policy
confidence: 0.75
sources:
- url: https://www.anthropic.com/research/redesigning-source-control
  author: Anthropic Engineering
  seen: '2026-11-09'
  quote: Scion is by no means a suitable replacement for git for general use.
  source: Anthropic Engineering 블로그
first_seen: '2026-11-09'
last_confirmed: '2026-11-09'
review_by: '2026-12-09'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- git
- 버전관리
- 과잉도입
verified_by: 공식 출처
---
Anthropic은 하루 병합 건수가 3만 건을 넘자 git을 대신할 자체 시스템 Scion을 만들었습니다. 하지만 Anthropic 스스로 Scion이 일반적인 용도로 git을 대체할 수 없다고 밝혔습니다. 수만 명의 엔지니어나 대량의 에이전트가 코드를 쏟아내는 초대형 저장소에서만 의미가 있다는 것입니다. 직원 몇 명 규모의 사업자는 계속 git으로 커밋하고 백업하는 편이 맞으며, 대형 회사의 인프라 전환 사례를 그대로 따라 할 필요가 없습니다.
