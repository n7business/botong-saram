---
id: ai-tools-0291
domain: ai-tools
claim: AI 에이전트의 '완료' 보고를 믿으려면 주장을 증명할 명령을 새로 실행하고 그 출력과 종료 코드를 근거로 붙이게 해야, 테스트도 안
  한 코드를 다 됐다고 넘기는 일을 줄일 수 있다.
status: candidate
evidence: anecdote
confidence: 0.7
sources:
- url: https://www.youtube.com/watch?v=3JCgiVYlLFo
  author: 노마드 코더 Nomad Coders
  seen: '2026-11-07'
  quote: Evidence before claims always
  source: 노마드 코더 Nomad Coders
first_seen: '2026-11-07'
last_confirmed: '2026-11-07'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 코딩에이전트
- 검증
- 완료보고
- 스킬
---
에이전트는 아무것도 테스트하지 않고 '완료, 다 동작할 거예요'라고 말할 수 있습니다. done·fixed·passing이라고 말하기 전에 그 주장을 증명할 명령을 밝히고, 기억에 의존하지 말고 새로 실행하고, 전체 출력과 종료 코드를 읽게 합니다. 출력이 주장을 뒷받침하지 않으면 실제 상태를 그대로 보고하게 합니다. 'should work'나 'probably passes' 같은 표현은 확인하지 않았다는 뜻이므로 금지합니다. 영상은 이 규칙을 담은 스킬로 Superpowers 모음의 Verification Before Completion을 소개합니다. 린트와 타입 체크를 통과하고 diff가 작아도 기능은 고장 나 있을 수 있으므로, 이 확인은 따로 해야 합니다.
