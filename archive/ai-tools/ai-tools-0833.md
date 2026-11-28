---
id: ai-tools-0833
domain: ai-tools
claim: 맥에서 Homebrew로 클로드 코드를 설치할 때 안정성이 중요하다면 'claude-code'를 설치하고, 새 기능을 바로 써야 한다면
  'claude-code@latest'를 설치해야 한다.
status: verified
evidence: policy
confidence: 0.85
sources:
- url: https://code.claude.com/docs/en/overview
  author: Anthropic
  seen: '2026-11-28'
  quote: typically about a week behind and skips releases with major regressions
  source: Claude Code 공식 문서
first_seen: '2026-11-28'
last_confirmed: '2026-11-28'
review_by: '2026-12-28'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- Homebrew
- 설치
verified_by: 공식 출처
---
Homebrew에는 클로드 코드 설치판(cask)이 두 가지 있습니다. claude-code는 안정판 채널을 따릅니다. 보통 최신판보다 1주일쯤 늦지만, 큰 문제가 있었던 버전은 건너뜁니다. claude-code@latest는 새 버전이 나오는 즉시 받습니다. 업무용 PC라면 안정판이 무난합니다. 어느 쪽이든 자동 업데이트는 되지 않으므로 업그레이드 명령을 직접 실행해야 합니다.
