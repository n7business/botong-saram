---
id: ai-tools-0281
domain: ai-tools
claim: 클로드 코드를 Homebrew나 WinGet으로 설치했다면 자동 업데이트가 되지 않으므로, 업그레이드 명령을 직접 실행해야 최신 기능과
  보안 수정을 받을 수 있다.
status: verified
evidence: policy
confidence: 0.95
sources:
- url: https://code.claude.com/docs/en/overview
  author: Anthropic
  seen: '2026-11-07'
  quote: Homebrew installations do not auto-update.
  source: Claude Code 공식 문서
- url: https://code.claude.com/docs/en/overview
  author: Anthropic
  seen: '2026-11-07'
  quote: WinGet installations do not auto-update.
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
- 업데이트
- 보안
verified_by: 공식 출처
---
네이티브 설치본은 백그라운드에서 자동으로 업데이트되지만 Homebrew와 WinGet 설치본은 자동으로 업데이트되지 않습니다. Homebrew는 설치한 cask에 맞춰 `brew upgrade claude-code` 또는 `brew upgrade claude-code@latest`를 실행합니다. WinGet은 `winget upgrade Anthropic.ClaudeCode`를 주기적으로 실행합니다. 직접 업데이트하지 않으면 보안 수정도 받지 못합니다.
