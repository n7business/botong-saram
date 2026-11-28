---
id: ai-tools-0846
domain: ai-tools
claim: AI 코딩 도구로 결제·정산·발주·쿠폰 발급 기능을 만들었다면 트랜잭션 경계, 동시성 잠금, 멱등성 키 처리가 들어가 있는지 AI에게
  물어 확인해야 한다. 이 처리가 없으면 결제 버튼을 여러 번 누르거나 자동 재시도가 일어날 때 카드가 여러 번 승인되고, 재고가 1개 남은 상품이
  두 명에게 팔린다.
status: candidate
evidence: consensus
confidence: 0.75
sources:
- url: https://www.youtube.com/watch?v=DwuZ5Rrj8Xo
  author: 양실장 (양실장의 바이브코딩대학)
  seen: '2026-11-28'
  quote: 트랜잭션 경계, 동시성 잠금, 멱등성 키 검증 세 가지만 에이전트에게 물어 확인
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
- 결제
- 멱등성
- 검증
---
AI는 요구사항에 빈칸이 있으면 가장 흔한 평균적인 구조로 채운다. 그래서 중복 결제 방지나 동시 주문 처리는 말하지 않으면 빠지기 쉽다. 결제·정산·발주·쿠폰 기능을 만든 뒤에는 '네트워크 재시도로 생기는 중복 결제를 막는 멱등성 키 처리가 들어가 있는지 확인하고, 빠져 있으면 DB 제약조건까지 넣어 달라'처럼 구체적으로 지시하세요. 잔액 차감과 주문 생성이 한 묶음(트랜잭션)으로 처리되는지, 같은 재고를 동시에 사는 경우 잠금이 걸려 있는지도 함께 물어보세요. 화자는 이 세 가지만 확인해도 치명적인 금전 사고 대부분을 막을 수 있다고 말합니다.
