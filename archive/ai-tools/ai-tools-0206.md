---
id: ai-tools-0206
domain: ai-tools
claim: AI가 고친 코드는 테스트 통과만 보지 말고 작업 목적을 적은 결정 기록과 실제 변경 내용이 맞는지 대조해야, '정리하는 김에' 손댄
  다른 기능의 변경을 잡을 수 있다.
status: candidate
evidence: anecdote
confidence: 0.6
sources:
- url: https://yozm.wishket.com/magazine/detail/4027/
  author: 이정민
  seen: '2026-11-06'
  quote: 결정 기록에는 지각 제출 판정만 적혀 있는데, diff에는 순위를 정렬하는 코드도 바뀌어 있다
  source: 요즘IT
first_seen: '2026-11-06'
last_confirmed: '2026-11-06'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 코드리뷰
- AI에이전트
- 변경검토
---
한 개발자의 저장소에서 지각 제출 판정만 바꾸는 작업에 순위 정렬 코드 변경이 함께 들어갔습니다. 빌드와 테스트는 모두 통과했지만, 읽기 전용 검토 에이전트가 기록과 변경 내용의 차이를 짚어 냈습니다. 그대로 합쳤다면 참가자 순위가 아무도 모르게 바뀔 수 있었습니다. 필자는 그 변경을 별도 작업으로 떼어 다시 확인했고, 비슷한 일이 또 생기자 규칙 일부를 스크립트 검사로 옮겼습니다. 혼자 운영하는 작은 저장소의 경험이며, 이 에이전트는 문제없는 변경에도 가끔 경고를 남깁니다.
