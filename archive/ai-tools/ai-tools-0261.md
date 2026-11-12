---
id: ai-tools-0261
domain: ai-tools
claim: AI에게 같은 문제를 두 번 고치게 해도 그대로라면 같은 부탁을 반복하지 말고, 마지막 커밋으로 되돌리거나 /clear로 대화를 비운
  뒤 증상과 시도해서 알게 된 내용을 정리해 새로 요청해야 실패한 시도에 끌려 맴도는 일을 줄일 수 있다.
status: candidate
evidence: consensus
confidence: 0.7
sources:
- url: https://www.youtube.com/watch?v=zmpXdQmLeYA
  author: 코드깎는노인
  seen: '2026-11-06'
  quote: 그럴 때는 같은 부탁을 계속 반복하지 마세요.
  source: 코드깎는노인
- url: https://www.youtube.com/watch?v=xjHR00fV-XQ
  author: 코드깎는노인
  seen: '2026-11-07'
  quote: 안 된 시도가 기억 공간에 쌓여 Claude가 같은 자리를 맴돌기 쉽습니다.
  source: 코드깎는노인
first_seen: '2026-11-06'
last_confirmed: '2026-11-07'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- codex
- 디버깅
- 새대화
- 되돌리기
mentions: 2
---
처음 짚은 원인이 틀렸다면 그 위에 수정을 덧대게 되어 고칠수록 코드가 더 꼬일 수 있습니다. 코덱스에서는 마지막 커밋으로 되돌린 뒤 /new로 새 대화를 엽니다. 이전 대화의 틀린 시도에 끌려가지 않게 하기 위해서입니다. 새 대화에는 증상과 지금까지 해 본 것을 정리해 처음부터 다시 부탁합니다. 그래도 안 풀리면 /model에서 생각 깊이를 한 단계 올려 봅니다.
