---
id: ai-tools-0136
domain: ai-tools
claim: 'Claude Code에 자연어로 요청했는데 연결해 둔 MCP가 작동하지 않으면, 대화에서 그 MCP 이름(예: Serena)을 직접
  말해 부르게 한다.'
status: candidate
evidence: anecdote
confidence: 0.6
sources:
- url: https://www.youtube.com/watch?v=L94yAQR9VvA
  author: 짐코딩 (@gymcoding)
  seen: '2026-11-03'
  quote: 명시적으로 MCP를 한번 대화해서 언급을 해 주세요.
  source: 짐코딩 (@gymcoding)
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
- MCP
- serena
---
MCP를 설치해도 자연어 요청만으로는 Claude가 그 도구를 쓰지 않을 때가 있습니다. 그럴 때는 요청 문장에 MCP 이름을 직접 넣습니다. Serena는 이렇게 부르면 프로젝트가 활성화되면서 도구를 제대로 씁니다. 그래도 안 되면 /mcp에서 연결 상태가 failed인지 먼저 확인합니다.
