---
id: ai-tools-0522
domain: ai-tools
claim: 클로드 코드 플러그인은 공식 마켓플레이스 것이든 동료나 회사가 만든 것이든 내 사용자 권한으로 코드를 실행할 수 있으므로, 설치 전에
  출처와 내용을 반드시 확인해야 한다.
status: verified
evidence: policy
confidence: 0.9
sources:
- url: https://code.claude.com/docs/en/plugins
  author: Anthropic
  seen: '2026-11-13'
  quote: Whatever the tier, a plugin you install can run code with your user privileges.
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
- 보안
- 권한
verified_by: 공식 출처
mentions: 1
---
클로드 코드는 마켓플레이스를 공식(Official), 커뮤니티(Community), 제3자(Third-party) 세 단계로 나눕니다. 공식·커뮤니티 이름은 github.com/anthropics/ 저장소에서 온 마켓플레이스에만 허용되고, 동료나 우리 회사가 만든 마켓플레이스는 모두 제3자로 분류됩니다. 공식 문서는 어느 단계든 설치한 플러그인이 내 사용자 권한으로 코드를 실행할 수 있다고 밝힙니다. 따라서 '공식처럼 보인다'거나 '아는 사람이 만들었다'는 이유만으로 설치하지 말고, 어떤 훅·MCP 서버·명령이 들어 있는지 먼저 확인하세요. 직원이 여럿이라면 관리 설정으로 허용할 마켓플레이스를 정해 둘 수 있습니다.
