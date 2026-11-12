---
id: ai-tools-0452
domain: ai-tools
claim: 업무용 컴퓨터에 Homebrew로 클로드 코드를 설치할 때는 claude-code@latest 대신 claude-code를 고르는 편이
  좋은데, 일주일쯤 늦게 받는 대신 큰 문제가 생긴 버전은 건너뛰기 때문이다.
status: verified
evidence: policy
confidence: 0.85
sources:
- url: https://code.claude.com/docs/en/overview
  author: Anthropic
  seen: '2026-11-11'
  quote: skips releases with major regressions
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
- Homebrew
- 안정성
verified_by: 공식 출처
---
Homebrew에는 클로드 코드 패키지가 두 가지 있습니다. claude-code는 안정(stable) 채널로, 보통 최신판보다 일주일쯤 늦고 큰 오류(회귀)가 있었던 버전은 건너뜁니다. claude-code@latest는 새 버전이 나오는 즉시 받습니다. 새 기능보다 매일 쓰는 업무가 멈추지 않는 게 중요하다면 안정 채널이 낫습니다. 어느 쪽이든 자동 업데이트는 되지 않으니 업그레이드는 직접 실행해야 합니다.
