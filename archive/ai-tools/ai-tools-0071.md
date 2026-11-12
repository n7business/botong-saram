---
id: ai-tools-0071
domain: ai-tools
claim: Claude Code 데스크톱에서 큰 일은 한 대화에 몰거나 대화를 따로 여는 대신 메인 세션이 하위 세션 여러 개를 거느리게 해, 갈래별
  수정은 하위 세션에 직접 말하고 전체 방향 변경은 메인에 한 번만 말한다.
status: candidate
evidence: anecdote
confidence: 0.7
sources:
- url: https://www.youtube.com/watch?v=zO68MQmfvcA
  author: '샘 호트만 : AI 엔지니어의 시선 (@ai.sam_hottman)'
  seen: '2026-11-03'
  quote: 큰 일을 맡길 때는 꼭 한번 써 보시길 권합니다.
  source: '샘 호트만 : AI 엔지니어의 시선 (@ai.sam_hottman)'
first_seen: '2026-11-03'
last_confirmed: '2026-11-03'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- 하위세션
- 컨텍스트관리
- 작업분할
---
메인 세션이 하위 세션을 열고 결과를 모아 보고하므로 팀장 한 명과만 이야기하는 구조가 된다. 예를 들어 썸네일 문구·설명란·쇼츠 구간을 하위 세션 3개로 나눠 맡긴다. 한 갈래만 손보려면 그 하위 세션에 직접 말하고, 시청자 타깃 변경처럼 전체에 걸친 지시는 메인에만 말하면 각 하위 세션에 전달된다. 서브에이전트는 내가 말을 걸 수 없지만 하위 세션은 직접 들어가 말을 걸 수 있다는 점이 다르다. 대화 하나에 일 하나를 두면 기억 용량이 넘쳐 답의 질이 떨어지는 문제를 피할 수 있다.
