---
id: ai-tools-0431
domain: ai-tools
claim: AI가 코드를 읽고 정리한 동작 규칙은 위치를 정확히 짚었더라도 해석이 뒤집힐 수 있으므로, 원본과 대조하거나 다른 AI에게 다시 대조시켜야
  틀린 규칙을 그대로 쓰는 일을 막을 수 있다.
status: verified
evidence: observed
confidence: 0.7
sources:
- url: https://yozm.wishket.com/magazine/detail/4028/
  author: 효빈
  seen: '2026-11-10'
  quote: 원본 소스가 없었다면 그 실수를 알아채지 못했을 것입니다.
  source: 요즘IT
first_seen: '2026-11-10'
last_confirmed: '2026-11-10'
review_by: '2026-12-10'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 검증
- 교차검토
- 환각
- REA
verified_by: 실무자 실측(단일 출처)
---
필자가 REA와 클로드 코드로 오픈소스 앱 기능을 분석해 정리한 규칙 18개를 원본 소스와 맞춰 보니 16개만 맞았습니다. 틀린 2개는 코드 위치는 정확했지만 압축된 조건식의 참·거짓을 거꾸로 읽은 경우였습니다. 그중 하나는 다른 AI(Codex)에게 원본과 다시 대조하게 하는 과정에서 발견됐습니다. 대조할 원본이 없었다면 그 실수를 알아채지 못했을 것이므로, 확인할 방법이 없는 상태에서 AI 분석 결과로 상용 서비스를 따라 만드는 것은 권하지 않습니다.
