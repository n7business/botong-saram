---
id: ai-tools-0785
domain: ai-tools
claim: 클로드 코드 업데이트를 직접 챙기기 어렵다면 Homebrew나 WinGet 말고 공식 설치 명령(네이티브 설치)으로 설치해야 한다. 네이티브
  설치는 백그라운드에서 자동으로 최신 버전으로 업데이트된다.
status: verified
evidence: policy
confidence: 0.9
sources:
- url: https://code.claude.com/docs/en/overview
  author: Anthropic
  seen: '2026-11-25'
  quote: Native installations automatically update in the background to keep you on
    the latest version.
  source: Claude Code 공식 문서
first_seen: '2026-11-25'
last_confirmed: '2026-11-25'
review_by: '2026-12-25'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- 설치
- 자동업데이트
- 보안
verified_by: 공식 출처
---
공식 문서는 네이티브 설치를 권장 방식으로 안내합니다. 맥·리눅스·WSL에서는 curl -fsSL https://claude.ai/install.sh | bash로 설치합니다. 이렇게 설치하면 백그라운드에서 저절로 업데이트되어 새 기능과 보안 수정이 따로 손대지 않아도 들어옵니다. Homebrew·WinGet으로 설치하면 자동 업데이트가 되지 않으니, 그때는 업그레이드 명령을 주기적으로 직접 실행해야 합니다.
