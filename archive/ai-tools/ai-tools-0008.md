---
id: ai-tools-0008
domain: ai-tools
claim: Claude Code를 안정적으로 쓰려면 Homebrew의 stable 채널(claude-code)을 설치하고, 신기능을 바로 쓰려면
  latest 채널(claude-code@latest)을 설치한다.
status: verified
evidence: policy
confidence: 0.9
sources:
- url: https://code.claude.com/docs/en/overview
  author: Anthropic (Claude Code Docs)
  seen: '2026-11-03'
  quote: claude-code tracks the stable release channel, which is typically about a
    week behind and skips releases with major regressions.
  source: Claude Code 공식 문서
first_seen: '2026-11-03'
last_confirmed: '2026-11-03'
review_by: '2026-12-03'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- 설치
- homebrew
- 릴리스채널
---
Homebrew는 두 개의 cask를 제공한다. `claude-code`는 stable 채널로 보통 1주일 정도 늦게 나오지만 큰 회귀가 있는 버전은 건너뛴다. `claude-code@latest`는 새 버전이 나오는 즉시 받는다. 업무용으로 안정성이 중요하면 stable, 최신 기능 검증이 목적이면 latest를 고른다. 어느 쪽이든 자동 갱신은 안 되니 직접 업그레이드해야 한다.
