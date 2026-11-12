---
id: growth-0082
domain: growth
claim: PG 결제를 실제 서비스에 배포하기 전에는 테스트 API 키가 아닌 라이브 API 키로 바꿨는지와, 라이브 환경에서는 계약·심사가 완료된
  결제수단만 작동하므로 카드사·간편결제별 심사 완료 여부를 확인한다.
status: candidate
evidence: policy
confidence: 0.75
sources:
- url: https://www.tosspayments.com/blog/articles/54511
  author: 토스페이먼츠
  seen: '2026-11-03'
  quote: 라이브 환경에서는 계약과 심사가 완료된 결제수단만 정상적으로 이용할 수 있으므로, 서비스 배포 전에 결제수단별 이용 가능 여부를 확인하는
    것이 좋아요.
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
- API키
- PG
- 배포전체크
- 토스페이먼츠
---
테스트 API 키는 실제 결제가 발생하지 않는 환경용이고 라이브 API 키는 실제 서비스 배포용이므로 둘을 혼동하면 결제가 진행되지 않는다. 테스트 환경에서는 추가 계약한 일부 간편결제 수단이 표시되지 않을 수 있고, 라이브 환경에서는 해당 카드사·결제수단의 심사가 끝나지 않았으면 결제가 실패한다. 토스페이먼츠는 상점관리자 왼쪽 하단 '개발자 센터'에서 API 키를 확인할 수 있으며, 외주 개발사와 작업한다면 개발 담당자를 상점관리자에 초대해 함께 확인할 수 있다. 오픈 전 결제수단별로 실제 소액 결제를 해 보고 계약·심사 상태를 점검한다.
