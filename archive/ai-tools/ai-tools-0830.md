---
id: ai-tools-0830
domain: ai-tools
claim: 큰 작업을 AI에게 통째로 맡기기 전에는 결과가 맞는지 무엇으로 확인할지(규칙, 예시 테스트, 기존 시스템과의 비교 중 무엇을 쓸지)를
  먼저 정해야 한다. Anthropic은 AI가 핵심 코드를 약 1주일 만에 짰지만, 그 결과를 믿을 수 있게 확인하는 일이 진짜 병목이었다고 밝혔기
  때문이다.
status: verified
evidence: observed
confidence: 0.65
sources:
- url: https://www.anthropic.com/research/migrating-api-to-rust
  author: Anthropic Engineering
  seen: '2026-11-28'
  quote: Verification, not generation, had become the bottleneck.
  source: Anthropic Engineering 블로그
first_seen: '2026-11-28'
last_confirmed: '2026-11-28'
review_by: '2026-12-28'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- AI위임
- 검증
- 시스템이전
verified_by: 실무자 실측(단일 출처)
---
AI 덕분에 만드는 일은 빨라졌지만, 맞게 만들었는지 확인하는 일은 그만큼 빨라지지 않았습니다. Anthropic은 Messages API의 핵심 요청 처리 코드를 Claude가 약 1주일 만에 짰지만, 이 결과를 믿고 쓰려면 운영 중인 기존 API와 똑같이 동작하는지 확인할 방법부터 만들어야 했습니다. '맞다'를 정하는 방법은 세 가지입니다. 규칙으로 판정하기, 예시(테스트)로 확인하기, 기존 시스템과 결과 비교하기입니다. AI에게 일을 맡기기 전에 이 중 무엇으로 결과를 확인할지 정해 두지 않으면, 빨리 나온 결과물을 믿을 근거가 없습니다.
