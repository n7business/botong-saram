---
id: ai-tools-0847
domain: ai-tools
claim: AI로 주문·결제 시스템을 만들 때는 주문 당시의 단가·할인율·세율·배송지를 주문 기록에 따로 복사해 저장하게 해야 한다. 주문이 상품
  테이블의 현재 가격을 그대로 불러오면, 가격을 올리는 순간 지난 영수증과 회계 금액까지 함께 바뀐다.
status: candidate
evidence: consensus
confidence: 0.75
sources:
- url: https://www.youtube.com/watch?v=DwuZ5Rrj8Xo
  author: 양실장 (양실장의 바이브코딩대학)
  seen: '2026-11-28'
  quote: 주문 당시 값을 복사해 시점 스냅샷으로 저장한다
  source: 양실장의 바이브코딩대학 (@VibecodingUniversity)
first_seen: '2026-11-28'
last_confirmed: '2026-11-28'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 바이브코딩
- DB설계
- 주문
- 회계
---
AI는 데이터 정리(정규화)는 잘하지만 시간에 따라 값이 바뀌는 문제는 사람이 짚어 줘야 합니다. 화자의 예시에서는 상품 가격을 1만 원에서 1만 5천 원으로 올리자 지난달 1만 원에 결제한 영수증까지 1만 5천 원으로 바뀌었습니다. 그래서 주문 당시의 가격·할인·세율·배송지는 그때 값을 복사해 둔 '시점 스냅샷'으로 저장하게 지시해야 합니다. 정산 잔액이나 계약 상태처럼 바뀐 과정 자체가 증거가 되는 데이터는 덮어쓰지 말고, 증감 내역을 계속 추가만 하는 방식으로 설계하게 하세요.
