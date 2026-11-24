---
id: growth-0565
domain: growth
claim: 토스페이먼츠 지급대행 지급을 API로 요청하고 있다면 권한 분리를 켜기 전에 토스페이먼츠 담당자에게 먼저 문의해야 한다. 권한 분리를
  켜면 전송된 요청이 바로 지급되지 않고 승인 대기 상태로 바뀌기 때문이다.
status: candidate
evidence: policy
confidence: 0.7
sources:
- url: https://www.tosspayments.com/blog/articles/55407
  author: 토스페이먼츠
  seen: '2026-11-24'
  quote: API로 지급을 요청하고 있다면 설정 전에 토스페이먼츠 담당자에게 먼저 문의해 주세요.
  source: 토스페이먼츠피드
first_seen: '2026-11-24'
last_confirmed: '2026-11-24'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 지급대행
- 토스페이먼츠
- API
- 권한분리
---
권한 분리 설정은 저장하는 즉시 적용된다. 설정한 뒤에는 지급요청서를 전송해도 바로 지급되지 않고 승인 대기 상태가 된다. API로 지급을 자동 요청하는 시스템은 이 변화 때문에 지급이 멈추거나 예상한 결과와 달라질 수 있다. 그래서 토스페이먼츠는 설정 전에 담당자에게 먼저 문의하라고 안내한다. 건당 최대 금액(10억 원 미만)과 지급 건수 같은 기존 지급 정책은 권한 분리를 켜도 그대로 유지된다.
