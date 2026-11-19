---
id: ai-tools-0629
domain: ai-tools
claim: '클로드 코드에서 훅으로 위험한 작업을 막고 있다면 막아야 하는 훅마다 "onFailure": "block"을 넣어야 한다. v2.1.329부터
  Code Mode에서는 오류가 난 PreToolUse 훅이 더 이상 작업을 거부하지 않기 때문이다.'
status: verified
evidence: policy
confidence: 0.85
sources:
- url: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
  author: Anthropic (anthropics/claude-code)
  seen: '2026-11-20'
  quote: a PreToolUse hook that errors no longer refuses a script's tool call
  source: Claude Code 릴리스 노트 (CHANGELOG)
first_seen: '2026-11-20'
last_confirmed: '2026-11-20'
review_by: '2026-12-20'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- 훅
- 보안
- code-mode
- v2.1.329
verified_by: 공식 출처
---
PreToolUse 훅은 도구가 실행되기 전에 검사하는 스크립트입니다. v2.1.329부터는 Code Mode에서 이 훅이 오류를 내도 스크립트의 도구 호출이 그대로 실행됩니다. 이는 Code Mode 밖의 동작과 같아진 것입니다. 따라서 검사 스크립트가 고장 나더라도 반드시 막아야 하는 훅이라면 command·HTTP·MCP 도구 훅에 "onFailure": "block"을 지정하세요. mcp_tool 훅에도 v2.1.328부터 이 옵션을 쓸 수 있습니다.
