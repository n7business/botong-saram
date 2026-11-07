---
id: ai-tools-0282
domain: ai-tools
claim: Homebrew로 클로드 코드를 설치할 때 큰 결함이 있는 버전을 피하고 싶으면 `claude-code`를, 새 버전을 바로 받고 싶으면
  `claude-code@latest`를 고른다.
status: verified
evidence: policy
confidence: 0.9
sources:
- url: https://code.claude.com/docs/en/overview
  author: Anthropic
  seen: '2026-11-07'
  quote: '`claude-code` tracks the stable release channel, which is typically about
    a week behind and skips releases with major regressions.'
  source: Claude Code 공식 문서
first_seen: '2026-11-07'
last_confirmed: '2026-11-07'
review_by: '2026-12-07'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- 설치
- homebrew
- 안정성
verified_by: 공식 출처
---
Homebrew에는 두 가지 cask가 있습니다. `claude-code`는 안정 채널을 따르며, 보통 최신보다 일주일쯤 늦고 큰 회귀가 있는 릴리스는 건너뜁니다. `claude-code@latest`는 최신 채널을 따르며 새 버전이 나오는 즉시 받습니다. 어느 쪽이든 자동으로 업데이트되지는 않으므로 설치한 cask에 맞는 업그레이드 명령을 직접 실행해야 합니다.
