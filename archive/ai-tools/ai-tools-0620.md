---
id: ai-tools-0620
domain: ai-tools
claim: 클로드 코드에서 opusplan처럼 계획 모드에 비싼 모델을 쓰고 있다면 v2.1.326부터 계획 모드의 자동 압축도 그 모델로 처리되어
  비용이 더 들 수 있으므로, 긴 계획 세션의 사용량을 확인해야 한다.
status: verified
evidence: policy
confidence: 0.75
sources:
- url: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
  author: Anthropic
  seen: '2026-11-19'
  quote: Changed automatic compaction in plan mode to use the model answering you,
    such as Opus with `opusplan`, so it can cost more
  source: Claude Code 릴리스 노트 (CHANGELOG)
first_seen: '2026-11-19'
last_confirmed: '2026-11-19'
review_by: '2026-12-19'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- 비용
- plan-mode
- opusplan
verified_by: 공식 출처
---
v2.1.326부터 계획 모드(plan mode)에서 대화가 길어져 자동 압축(compaction)이 일어나면, 지금 답하고 있는 모델이 그 작업도 처리합니다. 예를 들어 opusplan 설정이라면 계획 단계의 Opus가 압축까지 맡습니다. 공식 변경 이력도 이 때문에 비용이 더 들 수 있다고 적고 있습니다. 계획 모드로 오래 대화하는 일이 많다면 /usage나 /cost로 이전과 사용량을 비교해 보세요.
