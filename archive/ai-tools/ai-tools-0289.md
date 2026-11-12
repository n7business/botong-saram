---
id: ai-tools-0289
domain: ai-tools
claim: 클로드 코드의 빠른 응답이 꼭 필요한 대화형 작업에만 `/fast`를 켜고, 비용이 더 중요할 때는 꺼 두어야 토큰 비용을 불필요하게
  늘리지 않는다.
status: verified
evidence: policy
confidence: 0.9
sources:
- url: https://code.claude.com/docs/en/fast-mode
  author: Anthropic
  seen: '2026-11-07'
  quote: making the model up to 2.5x faster at a higher cost per token
  source: Claude Code 릴리스 노트 (CHANGELOG)
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
- fast-mode
- 비용
verified_by: 공식 출처
---
패스트 모드는 Claude Opus를 최대 2.5배 빠르게 쓰는 설정이지만 토큰당 비용이 더 높습니다. 다른 모델로 바뀌는 기능은 아닙니다. `/fast`로 켜고 끌 수 있습니다. 공식 문서는 빠르게 고치고 다시 시험하는 작업이나 실시간 디버깅에 켜고, 응답 속도보다 비용이 중요할 때는 끄라고 안내합니다.
