---
id: ai-tools-0663
domain: ai-tools
claim: 클로드 코드 설정의 deniedMcpServers에 이름을 적어 claude.ai 커넥터를 막고 있다면 v2.1.330부터는 같은 주소를
  쓰는 다른 커넥터까지 막으려면 이름 대신 정확한 서버 URL을 적어야 한다. 이제 이름 항목은 그 이름의 커넥터 하나만 숨기기 때문이다.
status: verified
evidence: policy
confidence: 0.7
sources:
- url: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
  author: anthropics (Anthropic)
  seen: '2026-11-21'
  quote: to block them all, deny its exact URL
  source: Claude Code 릴리스 노트 (CHANGELOG)
first_seen: '2026-11-21'
last_confirmed: '2026-11-21'
review_by: '2026-12-21'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- MCP
- 커넥터
- 권한
- 보안
verified_by: 공식 출처
---
v2.1.330부터 deniedMcpServers의 이름 항목은 해당 이름의 claude.ai 커넥터 하나만 숨기고, 같은 URL을 쓰는 다른 이름의 커넥터는 막지 않는다. 고객 자료가 오가지 않게 특정 외부 도구를 막아 두었다면, 이름만 적은 설정으로는 다른 이름으로 다시 연결된 같은 서버를 놓칠 수 있다. 업데이트한 뒤 차단 목록을 열어 막아야 할 서버를 정확한 URL로 적고, /mcp에서 해당 서버가 실제로 빠졌는지 확인해야 한다.
