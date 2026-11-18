---
id: ai-tools-0616
domain: ai-tools
claim: 클로드 코드에 토큰이 필요한 MCP 서버를 등록할 때는 토큰을 명령줄에 직접 적지 말고, v2.1.327부터 생긴 claude mcp
  add-json <이름> - 명령으로 설정 JSON을 표준 입력으로 넘겨야 토큰이 명령줄에 남지 않는다.
status: verified
evidence: policy
confidence: 0.85
sources:
- url: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
  author: Anthropic
  seen: '2026-11-19'
  quote: Added `claude mcp add-json <name> -` to read the server's JSON from stdin,
    so tokens can stay off the command line
  source: Claude Code 릴리스 노트 (CHANGELOG)
first_seen: '2026-11-19'
last_confirmed: '2026-11-19'
review_by: '2026-12-19'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- mcp
- 보안
- 토큰관리
verified_by: 공식 출처
---
외부 서비스 MCP 서버를 연결할 때 API 토큰을 명령어에 그대로 적으면 셸 기록이나 화면에 그대로 남을 수 있습니다. v2.1.327부터는 claude mcp add-json 뒤에 이름과 '-'를 붙이면 서버 설정 JSON을 표준 입력(stdin)으로 읽습니다. 공식 변경 이력은 이 기능이 토큰을 명령줄 밖에 두기 위한 것이라고 설명합니다. 다만 이 명령은 클로드 코드 세션 안에서는 쓸 수 없으므로 일반 터미널에서 직접 실행해야 합니다.
