---
id: ai-tools-0388
domain: ai-tools
claim: 클로드 코드 플러그인은 동료가 만든 것이든 공식 마켓플레이스에 있는 것이든 내 권한으로 코드를 실행하므로, 설치 전에 출처와 들어 있는
  구성 요소를 확인해야 한다.
status: merged
evidence: policy
confidence: 0.85
sources:
- url: https://code.claude.com/docs/en/plugins
  author: Anthropic
  seen: '2026-11-09'
  quote: Whatever the tier, a plugin you install can run code with your user privileges.
  source: Claude Code 릴리스 노트 (CHANGELOG)
first_seen: '2026-11-09'
last_confirmed: '2026-11-09'
review_by: '2026-12-09'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- 플러그인
- 보안
verified_by: 공식 출처
merged_into: ai-tools-0522
---
플러그인에는 스킬뿐 아니라 편집할 때마다 실행되는 훅이나 MCP 서버 같은 실행 코드가 들어 있을 수 있습니다. 공식(Official)·커뮤니티(Community)·서드파티 중 어느 마켓플레이스에서 받았든, 설치한 플러그인은 내 사용자 권한으로 실행됩니다. 공식·커뮤니티 이름은 github.com/anthropics/ 저장소에서 온 마켓플레이스에만 인정되고, 동료나 우리 조직이 배포한 마켓플레이스는 서드파티입니다. 고객 파일이 있는 컴퓨터라면 설치하기 전에 어떤 훅과 MCP 서버가 들어 있는지 확인하십시오.
