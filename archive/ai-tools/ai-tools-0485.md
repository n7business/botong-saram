---
id: ai-tools-0485
domain: ai-tools
claim: 클로드 코드 업데이트를 따로 챙기기 어렵다면 Homebrew나 WinGet 대신 공식 설치 명령(Native Install)으로 설치해야
  하는데, 이 방식만 백그라운드에서 자동으로 최신 버전으로 업데이트되기 때문이다.
status: verified
evidence: policy
confidence: 0.9
sources:
- url: https://code.claude.com/docs/en/overview
  author: Anthropic
  seen: '2026-11-12'
  quote: Native installations automatically update in the background to keep you on
    the latest version.
  source: Claude Code 공식 문서
first_seen: '2026-11-12'
last_confirmed: '2026-11-12'
review_by: '2026-12-12'
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
클로드 코드는 설치 방법에 따라 업데이트 방식이 다릅니다. 맥·리눅스·WSL에서는 curl 설치 명령, 윈도우에서는 PowerShell용 irm 명령이나 CMD용 curl 명령으로 설치하면 백그라운드에서 자동으로 최신 버전이 유지됩니다. Homebrew나 WinGet으로 설치하면 자동 업데이트가 되지 않아 직접 업그레이드 명령을 실행해야 합니다. 업데이트를 잊기 쉬운 업무용 컴퓨터라면 공식 설치 명령을 쓰는 편이 보안 수정을 놓치지 않는 방법입니다.
