---
id: ai-tools-0386
domain: ai-tools
claim: 클로드 코드 사용료가 어디로 청구되는지 헷갈리면 /status를 실행해 로그인 방식이 구독 계정인지 API 키인지 먼저 확인해야, 엉뚱한
  곳에 요금이 쌓이는 일을 막을 수 있다.
status: verified
evidence: policy
confidence: 0.85
sources:
- url: https://code.claude.com/docs/en/fast-mode
  author: Anthropic
  seen: '2026-11-09'
  quote: If it shows an `API key` row instead, your requests bill to a Claude Console
    organization.
  source: Claude Code 릴리스 노트 (CHANGELOG)
- url: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
  author: Anthropic
  seen: '2026-11-09'
  quote: Added a warning when your claude.ai login ends and Claude Code continues
    on the sign-in from `ant auth login`
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
- 요금
- 로그인
verified_by: 공식 출처
---
클로드 코드는 claude.ai 구독으로 로그인했는지, Claude Console의 API 키로 로그인했는지에 따라 요금이 청구되는 곳이 다릅니다. /status 결과에 'Claude Max account' 같은 Login method 줄이 보이면 구독 계정이고, API key 줄이 보이면 Console 조직으로 토큰당 요금이 청구됩니다. 최근 버전은 claude.ai 로그인이 끊긴 뒤 다른 로그인 정보로 계속 실행될 때 Console 조직에 청구된다는 경고를 띄웁니다. 이런 경고가 보이면 무시하지 말고 /status로 다시 확인하십시오.
