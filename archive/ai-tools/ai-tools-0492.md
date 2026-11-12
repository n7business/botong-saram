---
id: ai-tools-0492
domain: ai-tools
claim: 클로드 코드에서 API 키로 페이블 5.2를 쓴다면 출력 토큰이 입력보다 5배 비싸고 캐시에서 다시 읽는 입력은 40분의 1 값이므로,
  긴 자료는 매번 새로 넣지 말고 같은 맥락을 이어 쓰게 하고 결과물은 필요한 만큼만 길게 쓰게 해야 비용을 줄일 수 있다.
status: verified
evidence: policy
confidence: 0.7
sources:
- url: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
  author: Anthropic
  seen: '2026-11-12'
  quote: 1M context, $8/$40 per Mtok with $0.20/Mtok cache reads
  source: Claude Code 릴리스 노트 (CHANGELOG)
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
- fable-5.2
- 요금
- 프롬프트캐시
- API
verified_by: 공식 출처
---
클로드 코드 2.1.321부터 페이블 5.2(claude-fable-5-2)가 기본 페이블 모델이 됐고, 공개된 요금은 100만 토큰당 입력 8달러, 출력 40달러, 캐시 읽기 0.20달러입니다. 출력이 입력의 5배이므로 긴 보고서를 통째로 다시 쓰게 하기보다 고칠 부분만 쓰게 하는 편이 쌉니다. 같은 문서와 지침을 반복해서 쓰는 작업은 캐시 읽기로 처리되면 입력 비용이 40분의 1로 줄어드므로, 작업을 잘게 나눠 매번 새 세션에서 자료를 처음부터 넣는 방식은 피하는 것이 좋습니다. 구독 요금제가 아니라 API 키로 과금되는 경우에 해당하며, 요금은 바뀔 수 있으니 결제 전에 최신 가격표를 확인해야 합니다.
