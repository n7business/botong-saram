---
id: ai-tools-0267
domain: ai-tools
claim: 서브 에이전트를 쓰는 에이전트는 recursion limit을 기본값 25보다 크게 잡아야, 호출 횟수가 한도를 넘어 작업이 멈추는 일을
  줄일 수 있다.
status: candidate
evidence: anecdote
confidence: 0.65
sources:
- url: https://www.youtube.com/watch?v=QI2KVJ2ciiY
  author: 테디노트 TeddyNote
  seen: '2026-11-06'
  quote: 보통은이 리컬 리미트를 더 크게 주는 것을 권장해 드리고 있습니다.
  source: 테디노트 TeddyNote
first_seen: '2026-11-06'
last_confirmed: '2026-11-06'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 멀티에이전트
- 서브에이전트
- recursion-limit
- 설정
---
영상의 빌더에서는 툴 호출 한 번과 결과 수신마다 1회씩 세며, 기본값 25를 넘으면 작업이 멈춥니다. 메인 에이전트가 위임 요청을 자세하게 보내면 서브 에이전트가 검색을 많이 해 한도에 금방 닿을 수 있습니다. 화자는 이 값을 100으로 늘렸습니다. 검색이 과하면 시스템 프롬프트에 간결하게 검색해 달라고 요청하라는 지시를 넣어 호출 자체를 줄입니다. 호출이 늘면 비용도 늘 수 있으니 한도만 올리지 말고 호출 횟수도 함께 봐야 합니다.
