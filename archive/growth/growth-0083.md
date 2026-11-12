---
id: growth-0083
domain: growth
claim: 토스페이먼츠 결제 연동 시 상점아이디(MID)는 심사 중이거나 계약 취소된 아이디가 기본값으로 선택돼 있을 수 있으므로 상점관리자 '이용정보'에서
  계약 상태가 완료인 아이디인지 확인하고, 키인·빌링·브랜드페이를 추가 계약했다면 일반 결제용이 아닌 그 서비스 전용 상점아이디와 키 세트를 쓴다.
status: candidate
evidence: policy
confidence: 0.7
sources:
- url: https://www.tosspayments.com/blog/articles/54511
  author: 토스페이먼츠
  seen: '2026-11-03'
  quote: 심사 중이거나 계약이 취소된 상점아이디가 기본값으로 선택되어 있을 수도 있어요.
  source: 토스페이먼츠피드
first_seen: '2026-11-03'
last_confirmed: '2026-11-03'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 결제연동
- 상점아이디
- PG
- 토스페이먼츠
- 정기결제
---
API 키를 확인할 때 실제로 연동할 상점아이디가 맞는지 함께 봐야 하며, 계약이 완료되지 않았거나 다른 결제 서비스용 아이디를 고르면 예상한 결제 기능이 작동하지 않는다. 상점관리자의 '이용정보' 메뉴에서 현재 선택된 상점아이디의 계약 상태를 확인한다. 키인, 빌링(정기결제), 브랜드페이처럼 별도 결제 서비스를 추가 계약하면 그 서비스에 맞는 상점아이디와 키 세트가 따로 발급되므로 일반 결제용 키와 섞어 쓰지 않는다. 정기결제나 전화 주문 결제를 도입한 사업자는 개발사에 어떤 상점아이디를 썼는지 확인한다.
