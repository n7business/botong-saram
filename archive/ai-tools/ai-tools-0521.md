---
id: ai-tools-0521
domain: ai-tools
claim: 클로드 코드 플러그인은 켜 두기만 해도 쓰지 않는 세션에서까지 스킬 이름과 설명이 매번 컨텍스트에 들어가 사용량을 차지하므로, 잘 쓰지
  않는 플러그인은 /plugin에서 꺼 두어야 한다.
status: verified
evidence: policy
confidence: 0.9
sources:
- url: https://code.claude.com/docs/en/plugins
  author: Anthropic
  seen: '2026-11-13'
  quote: An enabled plugin is part of every session, not only the sessions where you
    use it.
  source: Claude Code 릴리스 노트 (CHANGELOG)
first_seen: '2026-11-13'
last_confirmed: '2026-11-13'
review_by: '2026-12-09'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- 플러그인
- 컨텍스트
- 비용
verified_by: 공식 출처
mentions: 1
---
켜진 플러그인은 그 플러그인을 쓰는 세션뿐 아니라 모든 세션에 포함됩니다. 클로드가 스스로 부를 수 있는 스킬·에이전트·명령의 이름과 설명은 매 턴 컨텍스트에 올라가므로, 사용량을 차지하고 컨텍스트 창의 여유도 줄어듭니다. 플러그인에 MCP 서버가 들어 있으면 세션마다 그 서버도 함께 실행됩니다. 공식 마켓플레이스 플러그인은 설치 전에 /plugin의 Marketplaces 탭에서 Context cost 추정치를 볼 수 있습니다. 설치한 뒤에는 Installed 탭의 'Not used recently' 목록을 확인해, 삭제하지 말고 /plugin이나 claude plugin disable로 꺼 두세요.
