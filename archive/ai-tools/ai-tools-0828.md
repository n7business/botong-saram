---
id: ai-tools-0828
domain: ai-tools
claim: AI로 다시 만든 사내 시스템으로 갈아타기 전에는 테스트 통과율만 보지 말고, 기존 시스템과 새 시스템에 같은 실제 업무 데이터를 넣어
  결과가 같은지 비교해야 한다. Anthropic에서는 새 버전이 테스트를 약 98% 통과했는데도, 실제 요청으로 비교하면 입력이 일치한 경우가
  약 4분의 1뿐이었기 때문이다.
status: verified
evidence: observed
confidence: 0.8
sources:
- url: https://www.anthropic.com/research/migrating-api-to-rust
  author: Anthropic Engineering
  seen: '2026-11-28'
  quote: only about a quarter of inputs matched on production traffic
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
- AI코딩
- 시스템이전
- 병행운영
- 검증
verified_by: 실무자 실측(단일 출처)
---
테스트는 누군가 미리 떠올린 경우만 검사합니다. 실제 업무에는 테스트가 다루지 않는 예외와 습관이 섞여 있습니다. Anthropic의 Rust 버전 API는 4월에 테스트를 약 98% 통과했지만, 실제 운영 요청으로 비교하자 입력이 일치한 경우는 약 4분의 1에 그쳤습니다. 이모지 같은 특수문자를 처리하는 방식이 몇 바이트 다른 것처럼 테스트에 없던 차이 때문이었습니다. 또 실제 업무에서는 자주 나오는 버그 하나가 수많은 건을 틀리게 만듭니다. 그러니 한동안은 기존 시스템을 그대로 쓰면서 같은 데이터를 새 시스템에도 넣어 결과를 대조하고, 차이가 없어진 뒤에 갈아타야 합니다. 이때 주문·결제처럼 두 번 처리되면 안 되는 작업이 이중으로 실행되지 않게 조심해야 합니다.
