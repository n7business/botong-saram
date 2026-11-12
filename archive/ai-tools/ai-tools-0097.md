---
id: ai-tools-0097
domain: ai-tools
claim: AI로 주문을 분류해 집계할 때는 기간 밖 주문을 먼저 빼고 남은 주문을 취소와 결제 대기로 나누게 해야, 기간에 걸친 취소 주문이 두
  번 세어져 빠진 주문 수가 부풀려지는 일을 막는다.
status: candidate
evidence: anecdote
confidence: 0.65
sources:
- url: https://www.youtube.com/watch?v=HcPX_oGftIw
  author: 직장인 AI 업무 자동화 | 라핀
  seen: '2026-11-03'
  quote: 기간 밖 주문을 먼저 빼고, 남은 주문에서 취소와 결제 대기를 나누도록 고쳤다.
  source: 직장인 AI 업무 자동화 | 라핀
first_seen: '2026-11-03'
last_confirmed: '2026-11-03'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 매출집계
- 주문분류
- 중복카운트
- 온라인셀러
---
기간이 걸쳐 있으면서 취소된 주문은 '기간 외' 항목과 '취소' 항목에 모두 들어가기 쉽습니다. 그러면 제외된 주문 수가 실제보다 많아 보입니다. AI에게 분류 순서를 정해 주세요. 먼저 기간 밖 주문을 빼고, 남은 주문 안에서 취소와 결제 대기를 나누게 합니다. 이번 주 매출을 보려면 결제 완료 주문을, 취소가 궁금하면 취소 건수를 따로 보는 것처럼 목적에 맞는 숫자를 정하는 일은 사람이 합니다.
