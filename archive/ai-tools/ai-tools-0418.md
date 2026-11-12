---
id: ai-tools-0418
domain: ai-tools
claim: 클로드 코드 2.1.321부터 Pro·Max 요금제에서 저장해 둔 Fable 5.1 선택이 자동으로 최신 Fable(5.2)로 바뀌므로,
  업데이트 뒤 결과물 품질이나 비용이 달라졌다면 /model claude-fable-5-1로 이전 모델로 되돌려 비교해야 한다.
status: verified
evidence: policy
confidence: 0.85
sources:
- url: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
  author: anthropics
  seen: '2026-11-10'
  quote: use `/model claude-fable-5-1` to switch back
  source: Claude Code 릴리스 노트 (CHANGELOG)
first_seen: '2026-11-10'
last_confirmed: '2026-11-10'
review_by: '2026-12-10'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- 모델
- fable
- 요금
- 업데이트
verified_by: 공식 출처
---
2.1.321 업데이트로 Claude Fable 5.2가 기본 Fable 모델이 되었습니다. 예전에 Fable 5.1을 골라 저장해 두었다면 Pro·Max 요금제에서는 바로 fable로 옮겨지고, Team·Enterprise 요금제에서는 조직이 허용하면 옮겨집니다. Fable 5.2는 100만 토큰 컨텍스트를 지원하며, API 요금은 100만 토큰당 입력 8달러·출력 40달러이고 캐시 읽기는 0.20달러입니다. 잘 돌던 반복 작업의 결과가 업데이트 뒤 달라졌다면 /model claude-fable-5-1로 되돌려 같은 입력으로 비교해 보세요.
