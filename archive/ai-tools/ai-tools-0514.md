---
id: ai-tools-0514
domain: ai-tools
claim: AI에게 규칙이나 사실을 메모로 남기게 할 때는 확인된 것과 아직 확인되지 않은 것을 구분해 표시하고, 그 규칙이 맞다는 근거도 함께
  적게 해야 다음 세션에서 추측을 사실처럼 쓰는 일을 막을 수 있다.
status: merged
evidence: observed
confidence: 0.65
sources:
- url: https://www.anthropic.com/research/components-of-agent-memory
  author: Anthropic Engineering
  seen: '2026-11-13'
  quote: began marking which facts it had checked and which were still unconfirmed
  source: Anthropic Engineering 블로그
first_seen: '2026-11-13'
last_confirmed: '2026-11-13'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- agent-memory
- 검증
- 메모
merged_into: ai-tools-0417
---
메모에 무언가를 적는다는 것은 다음 세션의 AI가 그 내용을 다시 확인하지 않고 쓸 것이라는 뜻입니다. Anthropic 실험에서 Sonnet 4.6의 메모 폴더에는 검증하지 않은 추측이 여러 파일에 흩어져 있었습니다. 성능이 더 좋았던 Opus 4.7은 확인한 사실과 미확인 사실을 표시하기 시작했고, Opus 5는 규칙과 함께 그 규칙이 맞다고 판단한 근거, 직접 겪은 함정에 대한 경고까지 적었습니다. AI에게 메모를 맡길 때는 '확인됨/미확인'과 근거를 함께 적으라고 요청하면 좋습니다.
