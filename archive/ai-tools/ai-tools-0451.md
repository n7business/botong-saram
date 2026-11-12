---
id: ai-tools-0451
domain: ai-tools
claim: 클로드 코드를 Homebrew나 WinGet으로 설치했다면 자동으로 업데이트되지 않으므로, brew upgrade나 winget upgrade를
  주기적으로 실행해야 보안 수정을 놓치지 않는다.
status: verified
evidence: policy
confidence: 0.9
sources:
- url: https://code.claude.com/docs/en/overview
  author: Anthropic
  seen: '2026-11-11'
  quote: Homebrew installations do not auto-update.
  source: Claude Code 공식 문서
first_seen: '2026-11-11'
last_confirmed: '2026-11-11'
review_by: '2026-12-11'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 클로드코드
- 설치
- 업데이트
- 보안
verified_by: 공식 출처
---
공식 설치 스크립트(Native Install)로 설치한 클로드 코드는 백그라운드에서 스스로 최신 버전으로 업데이트됩니다. 하지만 Homebrew나 WinGet으로 설치했다면 자동 업데이트가 되지 않습니다. 맥은 brew upgrade claude-code(또는 claude-code@latest), 윈도우는 winget upgrade Anthropic.ClaudeCode를 주기적으로 실행해야 합니다. 업데이트를 빠뜨리면 이미 고쳐진 권한 관련 버그가 그대로 남을 수 있습니다. 업데이트를 따로 챙기기 어렵다면 공식 설치 스크립트로 설치하는 것이 편합니다.
