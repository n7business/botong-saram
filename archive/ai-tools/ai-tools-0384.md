---
id: ai-tools-0384
domain: ai-tools
claim: 클로드 코드의 빠른 모드(/fast)를 쓸 거라면 대화 중간이 아니라 세션을 시작할 때 켜야, 그때까지 쌓인 대화 전체를 비싼 요금으로
  다시 읽는 비용을 줄일 수 있다.
status: merged
evidence: policy
confidence: 0.9
sources:
- url: https://code.claude.com/docs/en/fast-mode
  author: Anthropic
  seen: '2026-11-09'
  quote: the charge is smallest when you enable fast mode at the start.
  source: Claude Code 릴리스 노트 (CHANGELOG)
first_seen: '2026-11-09'
last_confirmed: '2026-11-09'
review_by: '2026-12-09'
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
merged_into: ai-tools-0520
---
빠른 모드는 같은 Opus 모델을 최대 2.5배 빠르게 돌리는 대신 토큰당 요금이 더 비쌉니다(Opus 5.5 기준 입력 100만 토큰당 8달러, 출력 40달러). 대화 도중 처음 켜면 그때까지의 대화 전체가 캐시 없는 빠른 모드 요금으로 청구되고, 대화가 길수록 이 비용이 커집니다. 빠른 모드와 일반 속도는 캐시를 따로 쓰므로, 켰다 껐다 할 때마다 대화를 다시 읽는 비용이 듭니다. 빠르게 고치고 확인하는 작업이라면 세션 처음에 켜고, 오래 걸리는 자동 작업이나 비용이 중요한 일은 일반 속도로 두십시오.
