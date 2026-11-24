---
id: ai-tools-0753
domain: ai-tools
claim: 개발을 모르는 직원이 AI로 주문·판매·세금계산서 흐름을 고칠 때는 매출과 회계 기록 순서를 아는 사람이 확인해야 한다. 예를 들어 주문
  단계에서 바로 세금계산서 발행 대상에 넣으면 매출 기록과 회계 기록이 어긋난다.
status: candidate
evidence: anecdote
confidence: 0.65
sources:
- url: https://yozm.wishket.com/magazine/detail/4052/
  author: 오윤성 (위시켓 AIDP FDE)
  seen: '2026-11-24'
  quote: 그렇게 하면 매출 기록과 회계 기록이 어긋납니다.
  source: 요즘IT
first_seen: '2026-11-24'
last_confirmed: '2026-11-24'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- ERP
- 세금계산서
- 회계
- 검토
- 비개발자
---
이 사례에서는 견적에서 주문, 주문에서 판매로 이어지는 흐름을 만들어 두었습니다. 그런데 직원들이 주문 단계에서 바로 세금계산서 발행 대상에 넣으려고 했습니다. 코드는 AI 에이전트가 짜 주기 때문에 처음 개발을 접하는 사람에게서 이런 발상이 자연스럽게 나옵니다. 그래서 회계와 맞물린 흐름을 바꿀 때는 그 흐름을 아는 사람이 멈춰 세우고 이유를 설명해야 합니다. 직원이 만든 변경을 그대로 반영하지 말고 회계에 영향을 주는지부터 확인하세요.
