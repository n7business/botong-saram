---
id: ai-tools-0633
domain: ai-tools
claim: 클로드 코드의 MCP 연결이나 설정이 갑자기 초기화된 적이 있다면 v2.1.329 이상으로 업데이트해야 한다. 이전 버전에서는 네트워크가
  멈추거나 파일이 잠긴 상태에서 저장하면 ~/.claude.json이 기본값으로 초기화되는 문제가 있었기 때문이다.
status: verified
evidence: policy
confidence: 0.8
sources:
- url: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
  author: Anthropic (anthropics/claude-code)
  seen: '2026-11-20'
  quote: Fixed `~/.claude.json` sometimes being reset to defaults
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
- 설정
- 백업
- 업데이트
- v2.1.329
verified_by: 공식 출처
---
~/.claude.json에는 클로드 코드의 사용자 설정과 등록한 MCP 서버 정보 등이 들어 있습니다. 이전 버전에서는 저장하는 도중 네트워크가 멈추거나 파일이 잠겨 이 파일을 읽지 못하면, 파일이 지워지고 기본값으로 초기화되는 경우가 있었습니다. v2.1.329에서 이 문제가 고쳐졌습니다. 업데이트 전까지는 이 파일을 따로 백업해 두면 복구가 쉽습니다.
