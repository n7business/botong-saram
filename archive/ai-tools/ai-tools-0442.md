---
id: ai-tools-0442
domain: ai-tools
claim: 클로드 코드 훅으로 위험한 명령을 막을 때는 막기만 하지 말고 차단 사유와 안전한 대체 명령을 에이전트에게 함께 돌려줘야, 에이전트가
  사용자에게 다시 묻지 않고 안전한 방법으로 작업을 이어 간다.
status: candidate
evidence: anecdote
confidence: 0.55
sources:
- url: https://www.gpters.org/llm-service/post/case-resolving-conflict-occurs-5wJnzP5SBtG7tKh
  author: .
  seen: '2026-11-10'
  quote: 차단 사유와 안전한 대체 명령을 에이전트에게 함께 전달하도록 했습니다.
  source: 지피터스 GPTers
first_seen: '2026-11-10'
last_confirmed: '2026-11-10'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- 훅
- 에이전트
---
훅이 명령을 막으면서 이유와 대안을 함께 주면, 에이전트는 그 안내를 읽고 대체 명령으로 일을 계속합니다. 예를 들어 프로그램 이름으로 종료하려 할 때 '자기가 띄운 프로세스 번호(PID)만 종료하라'고 알려 주는 식입니다. 대안이 없으면 에이전트가 멈추거나 사용자에게 다시 물어 자동화의 흐름이 끊길 수 있습니다. 이 내용은 한 사용자의 구축 경험이므로, 내 환경에서 에이전트가 대안을 실제로 따르는지 확인한 뒤 써야 합니다.
