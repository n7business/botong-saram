---
id: ai-tools-0564
domain: ai-tools
claim: AI가 만든 결과의 통과 여부는 그 코드를 쓴 AI가 아니라 별도의 검토용 AI에게 판단하게 해야 하고, 검토용 AI에게는 직접 고치는
  권한 없이 읽고 알리는 역할만 주어야 한다. 코드를 쓴 쪽은 자기가 만들려고 했던 것만 확인하기 때문이다.
status: candidate
evidence: anecdote
confidence: 0.7
sources:
- url: https://yozm.wishket.com/magazine/detail/4039/
  author: 요즘IT
  seen: '2026-11-14'
  quote: 코드를 쓰지 않은 에이전트가 내린 결과만 인정합니다.
  source: 요즘IT
first_seen: '2026-11-14'
last_confirmed: '2026-11-14'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- AI에이전트
- 검수
- 권한
- 코드리뷰
---
한 개발자는 PR이 열리면 별도 에이전트가 코드를 고치지 않고 읽기만 하면서, 원래 목적과 상관없는 변경이 섞였는지 알리게 했습니다. 지각 제출 판정만 바꾸기로 한 작업이었는데, 빌드와 테스트가 모두 통과한 상태에서 이 검토 에이전트가 순위 정렬 코드까지 바뀐 것을 잡아냈습니다. 그대로 머지했다면 참가자 순위가 아무도 모르게 바뀌었을 것입니다. 감시·검토 역할의 AI에게 실행 권한까지 주면 감시자가 오히려 위험해지므로 알리는 역할을 먼저 맡기세요. 최종 머지와 판단은 사람이 합니다.
