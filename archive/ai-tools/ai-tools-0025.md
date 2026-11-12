---
id: ai-tools-0025
domain: ai-tools
claim: 2.1.317 이전 Claude Code에서는 입력창의 글자를 지우려고 Ctrl+C를 누르면 돌고 있던 백그라운드 에이전트가 전부 중단되므로,
  구버전에서는 Ctrl+C 대신 다른 방법으로 입력을 지우거나 업데이트한다.
status: verified
evidence: policy
confidence: 0.75
sources:
- url: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21317
  author: anthropics
  seen: '2026-11-03'
  quote: Fixed Ctrl+C stopping all running background agents when pressed to clear
    typed text at the prompt
  source: Claude Code 릴리스 노트 (CHANGELOG)
first_seen: '2026-11-03'
last_confirmed: '2026-11-03'
review_by: '2026-12-03'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- background-agent
- keyboard
- bugfix
verified_by: 공식 출처
---
2.1.317 릴리스 노트에 프롬프트에 입력한 글자를 지우려고 Ctrl+C를 눌렀을 때 실행 중인 모든 백그라운드 에이전트가 함께 멈추던 버그가 수정됐다고 기록돼 있다. 서브에이전트 여러 개를 띄워 놓고 다음 지시를 타이핑하다 오타를 지우는 흔한 동작이 작업 전체를 날릴 수 있었다는 뜻이다. 구버전을 쓴다면 백그라운드 작업 중에는 Ctrl+C를 피하고 백스페이스로 지운다. 업데이트가 가능하면 2.1.317 이상으로 올리는 것이 근본 해결이다.
